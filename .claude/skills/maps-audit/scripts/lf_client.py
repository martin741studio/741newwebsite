import os, sys, json, urllib.request
env={}
for l in open('/Users/martindrendel/741website/.env'):
    if '=' in l and not l.startswith('#'):
        k,v=l.strip().split('=',1); env[k]=v.strip().strip('"')
KEY=env['LF_API_KEY']
URL='https://mcp.localfalcon.com/mcp?local_falcon_api_key='+KEY
H={'Content-Type':'application/json','Accept':'application/json, text/event-stream','Authorization':'Bearer '+KEY}
def rpc(method, params=None, sid=None, id_=1):
    h=dict(H)
    if sid: h['Mcp-Session-Id']=sid
    body={'jsonrpc':'2.0','id':id_,'method':method}
    if params is not None: body['params']=params
    req=urllib.request.Request(URL, json.dumps(body).encode(), h)
    r=urllib.request.urlopen(req, timeout=90)
    txt=r.read().decode()
    sid2=r.headers.get('Mcp-Session-Id') or sid
    # SSE or json
    if txt.startswith('event:') or 'data:' in txt[:20]:
        for line in txt.splitlines():
            if line.startswith('data:'):
                txt=line[5:].strip(); break
    return json.loads(txt), sid2
def session():
    r,sid=rpc('initialize',{'protocolVersion':'2025-03-26','capabilities':{},'clientInfo':{'name':'maps-audit','version':'0.1'}})
    return sid
def call(name,args,sid):
    r,_=rpc('tools/call',{'name':name,'arguments':args},sid,2)
    return r
if __name__=='__main__':
    sid=session()
    if sys.argv[1]=='tools':
        r,_=rpc('tools/list',{},sid,3)
        print(json.dumps([t['name'] for t in r['result']['tools']]))
    else:
        r=call(sys.argv[1], json.loads(sys.argv[2]), sid)
        print(json.dumps(r,ensure_ascii=False)[:int(sys.argv[3]) if len(sys.argv)>3 else 6000])
