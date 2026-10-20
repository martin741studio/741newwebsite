import re
B='/Users/martindrendel/741website/00_project/assets/stuerzl/cro-b/'
t=open(B+'_build/pool-template.html',encoding='utf8').read()
t=t.replace('Element-Pool STÜRZL Track B','Element-Pool 2 STÜRZL Track B').replace('Element-Pool: STÜRZL Steuerstrafrecht, Track B','Element-Pool 2: STÜRZL Steuerstrafrecht, Track B')
t=t.replace("stuerzl-pool-votes-v1","stuerzl-pool2-votes-v1").replace("fetch('save',","fetch('save?f=votes-pool2.json',")
t=t.replace('Alle Elemente sind in den Farben','Pool 2 zeigt nur NEUE Elemente aus der erweiterten Recherche (Award-Seiten, Kanzlei-Seiten, Notfall-Muster, Typografie). Deine Stimmen aus Pool 1 gelten weiter. Alle Elemente sind in den Farben')
t=t.replace('https://fonts.googleapis.com/css2?family=Manrope','https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;1,6..96,400&family=Fraunces:ital,opsz,wght@0,9..144,350;1,9..144,350&family=Hanken+Grotesk:wght@400;600&family=Instrument+Sans:wght@400;600&family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;600&family=Geist+Mono&family=Mrs+Saint+Delafield&family=Manrope')
t=t.replace('{{EXTRA_CSS}}',open(B+'_build/pool-extra.css',encoding='utf8').read()).replace('{{ELEMENTS}}',open(B+'_build/pool2-elements.js',encoding='utf8').read())
open(B+'00-element-pool/pool2.html','w',encoding='utf8').write(t); print('pool2 built',len(t))
