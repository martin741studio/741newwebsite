B='/Users/martindrendel/741website/00_project/assets/stuerzl/cro-b/'
t=open(B+'_build/pool-template.html',encoding='utf8').read()
t=t.replace('{{EXTRA_CSS}}',open(B+'_build/pool-extra.css',encoding='utf8').read()).replace('{{ELEMENTS}}',open(B+'_build/pool-elements.js',encoding='utf8').read())
open(B+'00-element-pool/index.html','w',encoding='utf8').write(t); print('pool built',len(t))
