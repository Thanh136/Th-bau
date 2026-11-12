#!/usr/bin/env python3
"""Erzeugt index.html (Design 2, live), design1.html und design2.html aus src/.
Aenderungen am Inhalt gehoeren in src/base.html, Farben in src/theme-*.css.
Aufruf: python3 build.py"""
import re
base=open('src/base.html').read()
def make(theme,color,noindex):
    s=base.replace('/*THEME*/',open(f'src/theme-{theme}.css').read()).replace('/*THEMECOLOR*/',color)
    if noindex: s=s.replace('<meta charset="utf-8">','<meta charset="utf-8">\n<meta name="robots" content="noindex">',1)
    return s
open('index.html','w').write(make(2,'#131a20',False))
open('design1.html','w').write(make(1,'#1b2026',True))
open('design2.html','w').write(make(2,'#131a20',True))
print('ok')
