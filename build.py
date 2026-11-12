#!/usr/bin/env python3
"""Erzeugt index.html (Design 2, live), design1.html und design2.html aus src/.
Aenderungen am Inhalt gehoeren in src/base.html, Farben in src/theme-*.css.
Aufruf: python3 build.py"""
import re
base=open('src/base.html').read()
FIG='<figure class="heromodel"><img src="images/modell-ueberdachung.jpg" alt="3D-Modell einer Stahlüberdachung" decoding="async"><figcaption>3D-Modell · Stahlüberdachung</figcaption></figure>'
V='b'
K='<div class="fact"><b>Ingenieurkammer-Bau NRW</b><span>Mitglied, bundesweit einreichberechtigt</span></div>'
Y='<div class="fact"><b>13 Jahre</b><span>Berufserfahrung in der Tragwerksplanung</span></div>'
A24='<div class="fact"><b>Antwort in 24 Stunden</b><span>in der Regel auf jede Anfrage</span></div>'
X={'1':'<div class="fact"><b>Statik aus einer Hand</b><span>von der Berechnung bis zur Bestätigung der Ausführung</span></div>','2':'<div class="fact"><b>Neubau und Bestand</b><span>Neubauten, Umbauten und Erweiterungen</span></div>'}
def facts(x='2'): return '    '+K+'\n    '+Y+'\n    '+X[x]+'\n    '+A24
def make(theme,color,noindex,v=None,x='2'):
    v=v or V
    s=base.replace('@FACTS@',facts(x)).replace('@V@',v).replace('@HEROFIG@',FIG if v=='a' else '').replace('/*THEME*/',open(f'src/theme-{theme}.css').read()).replace('/*THEMECOLOR*/',color)
    if noindex: s=s.replace('<meta charset="utf-8">','<meta charset="utf-8">\n<meta name="robots" content="noindex">',1)
    return s
import sys
if len(sys.argv)>1 and sys.argv[1]=='test':
    import os;os.makedirs('../th-bau-test/var',exist_ok=True)
    for x in '12': open(f'../th-bau-test/var/test-b{x}.html','w').write(make(2,'#131a20',True,'b',x))
    print('test ok');sys.exit()
open('index.html','w').write(make(2,'#131a20',False))
open('design1.html','w').write(make(1,'#1b2026',True))
open('design2.html','w').write(make(2,'#131a20',True))
print('ok')
