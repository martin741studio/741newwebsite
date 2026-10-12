#!/bin/bash
# Sample-input tests for the 741 hooks. Run: bash .claude/hooks/test_hooks.sh
cd "$(dirname "$0")/../.." || exit 1
export CLAUDE_PROJECT_DIR=$PWD
H=.claude/hooks; SID=hooktest-$$; pass=0; fail=0
t() { # name expect(deny|ask|allow|block|warn) script json
  local out; out=$(echo "$4" | python3 "$H/$3" 2>&1)
  local got=allow
  [[ $out == *'"deny"'* ]] && got=deny; [[ $out == *'"ask"'* ]] && got=ask
  [[ $out == *'"block"'* ]] && got=block; [[ $out == *systemMessage* ]] && got=warn
  if [[ $got == "$2" ]]; then pass=$((pass+1)); echo "PASS  $1"; else fail=$((fail+1)); echo "FAIL  $1 (want $2, got $got): $out"; fi
}
pre() { echo "{\"session_id\":\"$SID\",\"tool_name\":\"$1\",\"tool_input\":$2}"; }
prompt() { echo "{\"session_id\":\"$SID\",\"prompt\":\"$1\"}" | python3 $H/go_marker.py >/dev/null; }

prompt "check the deploy plan"   # no go -> marker cleared
t "ftp upload.js without go"        deny  live_change_gate.py "$(pre Bash '{"command":"node upload.js"}')"
t "npm run deploy without go"       deny  live_change_gate.py "$(pre Bash '{"command":"npm run deploy"}')"
t "upload_only.mjs without go"      deny  live_change_gate.py "$(pre Bash '{"command":"node 00_project/prospect-mini/scripts/upload_only.mjs review/x"}')"
t "curl -T without go"              deny  live_change_gate.py "$(pre Bash '{"command":"curl -T a.html ftp://741.studio/"}')"
t "curl GET live url is fine"       allow live_change_gate.py "$(pre Bash '{"command":"curl -sI https://741.studio/review/x/"}')"
t "git status is fine"              allow live_change_gate.py "$(pre Bash '{"command":"git status"}')"
t "php read is fine"                allow live_change_gate.py "$(pre mcp__novamira-shuiguru-de__mcp-adapter-execute-ability '{"ability_name":"novamira/execute-php","parameters":{"code":"echo get_option(\"blogname\");"}}')"
t "php update_option without go"    deny  live_change_gate.py "$(pre mcp__novamira-shuiguru-de__mcp-adapter-execute-ability '{"ability_name":"novamira/execute-php","parameters":{"code":"update_option(\"blogname\",\"x\");"}}')"
t "write-file without go"           deny  live_change_gate.py "$(pre mcp__novamira-suriya-praxis-de__mcp-adapter-execute-ability '{"ability_name":"novamira/write-file","parameters":{}}')"
t "elementor-get-content is fine"   allow live_change_gate.py "$(pre mcp__novamira-shuiguru-de__mcp-adapter-execute-ability '{"ability_name":"novamira/elementor-get-content","parameters":{}}')"
t "unknown ability asks"            ask   live_change_gate.py "$(pre mcp__novamira-shuiguru-de__mcp-adapter-execute-ability '{"ability_name":"novamira/flux-capacitor","parameters":{}}')"
t "porkbun deploy_site without go"  deny  live_change_gate.py "$(pre mcp__Porkbun__deploy_site '{}')"
t "edit settings.json without go"   deny  live_change_gate.py "$(pre Edit "{\"file_path\":\"$PWD/.claude/settings.json\"}")"
t "edit user settings without go"   deny  live_change_gate.py "$(pre Write '{"file_path":"/Users/x/.claude/settings.json"}')"
t "cat settings is fine"            allow live_change_gate.py "$(pre Bash '{"command":"cat .claude/settings.json"}')"
t "sed -i settings without go"      deny  live_change_gate.py "$(pre Bash '{"command":"sed -i \"\" s/a/b/ .claude/settings.local.json"}')"
t "edit normal file is fine"        allow live_change_gate.py "$(pre Edit "{\"file_path\":\"$PWD/04_site/index.html\"}")"

prompt "ok go, deploy the review page"
t "ftp upload.js WITH go"           allow live_change_gate.py "$(pre Bash '{"command":"node upload.js"}')"
t "php update_option WITH go"       allow live_change_gate.py "$(pre mcp__novamira-shuiguru-de__mcp-adapter-execute-ability '{"ability_name":"novamira/execute-php","parameters":{"code":"update_option(\"a\",1);"}}')"
t "write go marker always denied"   deny  live_change_gate.py "$(pre Bash '{"command":"echo {} > .claude/go/x.json"}')"
prompt "now the footer too"      # next prompt without go -> marker gone
t "next change needs new go"        deny  live_change_gate.py "$(pre Bash '{"command":"node upload.js"}')"
prompt "let us go through the list"
t "'go through' is not a go"        deny  live_change_gate.py "$(pre Bash '{"command":"node upload.js"}')"

stop() { python3 -c 'import json,sys;print(json.dumps({"session_id":"t","transcript_path":"/nonexistent","stop_hook_active":sys.argv[2]=="1","last_assistant_message":sys.argv[1]}))' "$1" "${2:-0}"; }
t "slop DE block blocks"            block slop_gate.py "$(stop $'Hier:\n```text\nWir bieten ganzheitliche, maßgeschneiderte Lösungen für deine Reise.\n```')"
t "slop EN block blocks"            block slop_gate.py "$(stop $'Here:\n```text\nWe leverage seamless solutions to unlock your journey.\n```')"
t "clean DE block passes"           allow slop_gate.py "$(stop $'```text\nIch habe deinen Google-Eintrag geprüft. Drei Punkte fehlen.\n```')"
t "no text block passes"            allow slop_gate.py "$(stop 'We leverage seamless synergy. No block here.')"
t "retry only warns"                warn  slop_gate.py "$(stop $'```text\nWe leverage seamless solutions.\n```' 1)"

rm -f ".claude/go/$SID.json"
echo "== $pass passed, $fail failed"; [[ $fail == 0 ]]
