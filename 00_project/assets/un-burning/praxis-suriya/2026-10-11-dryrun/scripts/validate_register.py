"""Manual validator for harm-register.json against harm-register.schema.json (jsonschema is not installed).
Checks: required fields, additionalProperties, enums, patterns, simple types, date-time shape, minItems, allOf done-rule."""
import json, re, sys
SCHEMA = json.load(open("/Users/martindrendel/741website/00_project/un-burning-workflow/harm-register.schema.json"))
REG = json.load(open(sys.argv[1]))
errs = []
DT = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$")
def resolve(sch):
    while "$ref" in sch:
        ref = sch["$ref"].split("/")[-1]
        sch = SCHEMA["$defs"][ref]
    return sch
def tmatch(v, t):
    m = {"string": str, "number": (int, float), "integer": int, "boolean": bool, "object": dict, "array": list, "null": type(None)}
    return any(isinstance(v, m[x]) and not (x in ("number", "integer") and isinstance(v, bool)) for x in (t if isinstance(t, list) else [t]))
def check(v, sch, path):
    sch = resolve(sch)
    if "const" in sch and v != sch["const"]: errs.append(f"{path}: const {sch['const']!r} != {v!r}")
    if "enum" in sch and v not in sch["enum"]: errs.append(f"{path}: {v!r} not in enum {sch['enum']}")
    if "type" in sch and not tmatch(v, sch["type"]): errs.append(f"{path}: wrong type {type(v).__name__}, want {sch['type']}"); return
    if sch.get("format") == "date-time" and isinstance(v, str) and not DT.match(v): errs.append(f"{path}: bad date-time {v!r}")
    if "pattern" in sch and isinstance(v, str) and not re.search(sch["pattern"], v): errs.append(f"{path}: pattern {sch['pattern']} fails for {v!r}")
    if "minimum" in sch and isinstance(v, (int, float)) and v < sch["minimum"]: errs.append(f"{path}: below minimum")
    if isinstance(v, dict):
        for r in sch.get("required", []):
            if r not in v: errs.append(f"{path}: missing required {r}")
        props = sch.get("properties", {})
        if sch.get("additionalProperties") is False:
            for k in v:
                if k not in props and not any(re.search(pp, k) for pp in sch.get('patternProperties', {})): errs.append(f"{path}: additional property {k}")
        for k, x in v.items():
            if k in props: check(x, props[k], f"{path}.{k}")
            elif "patternProperties" in sch:
                for pp, ps in sch["patternProperties"].items():
                    if re.search(pp, k): check(x, ps, f"{path}.{k}")
    if isinstance(v, list):
        if "minItems" in sch and len(v) < sch["minItems"]: errs.append(f"{path}: fewer than {sch['minItems']} items")
        if "items" in sch:
            for n, x in enumerate(v): check(x, sch["items"], f"{path}[{n}]")
    for rule in sch.get("allOf", []):
        cond = rule.get("if")
        if cond:
            ok = all((k in v and (("const" in p and v[k] == p["const"]) or "const" not in p)) for k, p in cond.get("properties", {}).items()) and all(r in v for r in cond.get("required", []))
            if ok and "then" in rule:
                for r in rule["then"].get("required", []):
                    if r not in v or v[r] in (None,): errs.append(f"{path}: done-rule requires non-null {r}")
check(REG, SCHEMA, "$")
ids = [i["id"] for i in REG["items"]]
if len(ids) != len(set(ids)): errs.append("duplicate ids")
for i in REG["items"]:
    if not i["id"].startswith(f"H-{i['area']}-"): errs.append(f"{i['id']}: id area differs from area {i['area']}")
    if i["check_id"][3] != i["area"]: errs.append(f"{i['id']}: check_id area differs")
    if i["approval"] != "proposed" and i["approval"] != "blocked": errs.append(f"{i['id']}: approval must be proposed (or blocked) in a dry run")
print("items:", len(REG["items"]), "errors:", len(errs))
for e in errs[:50]: print(" -", e)
sys.exit(1 if errs else 0)
