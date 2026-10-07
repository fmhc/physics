"""Generate standalone schematic SVG research cards; no simulation data implied.
Run: python3 assets/research/generate.py. Text/data: CC BY 4.0; code: Apache-2.0.
"""
from pathlib import Path
from html import escape
import math

OUT=Path(__file__).resolve().parent
C='#60dbc2'; B='#86aaff'; G='#acb8cd'; A='#f6c776'; WHITE='#f2f5fa'
DATA=[
('netz','Netz und Raum',65,'Geometrie als Ausgangspunkt',['Tetraeder, Kanten und Gewichte.','Volumenregel: 3 von 4 Testnetzen stabil.'],['Nichtlineare Dynamik und Netzherkunft.'],'RUNDE-37/volumen-g2-1/ERGEBNIS.md'),
('gravitation','Schwerkraft',55,'Krümmung verändert Wege',['Fernfeld und Lichtablenkung gerechnet.','Perihel aus Netzwerten: PPN-Arithmetik.'],['Nahfeld und dynamischer Kollaps.'],'RUNDE-50/GRUNDGLEICHUNG-v3.md'),
('licht','Licht',55,'Feld auf Kanten und Flächen',['DEC-Maxwell auf dem Netz.','Masseloser Modus in Modellrechnungen.'],['Kopplungsstärke aus dem Modell ableiten.'],'RUNDE-37/quant-2/ERGEBNIS.md'),
('materie','Materiefeld · Q-Bälle',30,'Ein gebundener Feldklumpen',['Klassische Vielteilchen-Objekte.','Für 2–5 Quanten keine belastbare Bindung.'],['Mechanismus für kleine Teilchenmassen.'],'RUNDE-37/quant-1/ERGEBNIS.md'),
('stark','Starke Kraft',40,'Eichfelder auf dem Netz',['SU(2): Einschluss und Flow-Skalen.','S5/S6: Vergleich an zwei Gitterabständen.'],['SU(3), Fadenspannung, größere Netze.'],'RUNDE-37/quant-3/ERGEBNIS-S6.md'),
('hadronen','Mesonen und Baryonen',10,'Gebundene Paare und Dreier?',['Dreipol-Modelle zeigen Bindung.','U(1)³: noch kein Baryonennachweis.'],['Farbeinschluss, Spin und Quantenzahlen.'],'RUNDE-37/qball-dreipol-3/ERGEBNIS.md'),
('spin','Spin ½',20,'Drehung, Vorzeichen, Statistik',['2π-Vorzeichen als zusätzliche Regel.','Spin und Statistik noch nicht vereint.'],['Gemeinsame Dynamik statt Vorgabe.'],'RUNDE-37/gerahmter-faden-1/ERGEBNIS.md'),
('schwach','Schwache Kraft',2,'Gesucht: chirale Wechselwirkung',['Literatur und Modellabgleich vorhanden.','Kein eigener tragender Mechanismus.'],['Chiralität und passende Eichkopplung.'],'RUNDE-20/ew-baelle/ERGEBNIS.md'),
('higgs','Higgs',2,'Gesucht: dynamische Massenerzeugung',['Literaturvorarbeiten vorhanden.','Kein eigener Higgs-Mechanismus.'],['Feld, Symmetriebrechung, Kopplungen.'],'RUNDE-20/ew-baelle/ERGEBNIS.md'),
('generationen','Generationen',2,'Warum drei Teilchenfamilien?',['64 Flussmuster: keine isolierten Knoten.','Einstellbare Massen sind keine Vorhersage.'],['Drei Familien und ihre Hierarchie erklären.'],'RUNDE-37/antigravity-nachbau-1/ERGEBNIS.md'),
('messdaten','Vergleich mit Messdaten',5,'Vom Modell zur prüfbaren Vorhersage',['Bestehende Schranken zusammengestellt.','Bisher keine Messdatenbestätigung.'],['Eigene quantitative Vorhersagen testen.'],'RUNDE-50/GRUNDGLEICHUNG-v3.md'),
('quantengravitation','Quantengravitation',7,'Das Netz selbst wird dynamisch',['CDT-artiges Modell und Dimensionsmessung.','Messverfahren konvergiert langsam.'],['Große Volumina und kontrollierte Grenzfälle.'],'RUNDE-37/ds-eichung-2d-1/ERGEBNIS.md'),
]

def text(x,y,s,size=19,color=WHITE,weight=400,anchor='start'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(s)}</text>'
def line(x1,y1,x2,y2,c=C,w=2,dash=False):
 return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"'+(' stroke-dasharray="7 7"' if dash else '')+'/>'
def circle(x,y,r,c=C,fill='#132a35'):
 return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="{c}" stroke-width="2" fill="{fill}"/>'
def path(d,c=C,w=3,dash=False):
 return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}"'+(' stroke-dasharray="7 7"' if dash else '')+'/>'
def mesh(points,edges):
 return ''.join(line(*points[a],*points[b],w=2) for a,b in edges)+''.join(circle(x,y,5) for x,y in points)
def label(s):return text(225,345,s,17,G,anchor='middle')
def diagram(k):
 if k=='netz':
  pts=[(100,270),(215,290),(165,145),(320,240),(275,130)]
  return mesh(pts,[(0,1),(0,2),(1,2),(1,3),(2,3),(2,4),(3,4),(1,4)])+label('Kanten · Flächen · Volumen')
 if k=='gravitation':
  s=''
  for y in range(170,301,26):s+=path(f'M 60 {y} Q 225 {y+55} 390 {y}', '#2c425c',1.5)
  for x in range(85,390,50):s+=path(f'M {x} 150 Q {225+(x-225)*0.45} 235 {x} 320','#2c425c',1.5)
  return s+circle(225,247,25,B,'#263856')+path('M 65 180 Q 190 185 220 200 T 390 225',A,4)+label('Lichtweg im gekrümmten Netz')
 if k=='licht':
  s=''.join(line(x,260,x+45,220,'#2c425c')+line(x+45,220,x+90,260,'#2c425c') for x in range(55,325,90))
  s+=path('M 55 230 C 85 145 110 145 140 230 S 195 315 225 230 S 280 145 310 230 S 365 315 395 230',C,4)
  return s+line(75,305,365,305,B,2)+text(375,311,'→',25,B)+label('Wellenmodus · schematisch')
 if k=='materie':
  s=''
  for r in [92,70,47,22]:s+=circle(225,235,r,C, 'none')
  for x,y in [(195,225),(242,205),(239,258),(204,266),(264,232)]:s+=circle(x,y,5,B,B)
  return s+label('Q: erhaltene Modellladung')
 if k=='stark':
  pts=[(100,165),(225,150),(350,165),(100,280),(225,295),(350,280)]
  s=mesh(pts,[(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)])
  s+=path('M 107 170 Q 145 225 218 154',A,4)+path('M 230 157 Q 290 205 342 170',A,4)
  return s+text(225,236,'SU(2) → SU(3)?',23,WHITE,600,'middle')+label('Getestetes Modell → nächste Variante')
 if k=='hadronen':
  s=line(85,215,170,215,A,4,True)+circle(85,215,19,C)+circle(170,215,19,B)
  pts=[(285,168),(245,285),(365,265)]
  s+=mesh(pts,[(0,1),(1,2),(2,0)])
  for (x,y),c in zip(pts,[C,B,A]):s+=circle(x,y,19,c)
  return s+text(128,287,'Paar?',18,G,anchor='middle')+label('Modellanalogie ≠ Hadronennachweis')
 if k=='spin':
  return path('M 170 167 C 55 200 100 310 215 284 C 355 248 345 125 235 164 C 125 205 190 303 326 266',C,5)+text(124,153,'2π',22,A)+text(318,310,'4π',22,B)+text(226,230,'− / +',29,WHITE,600,'middle')+label('Vorzeichenregel · keine Herleitung')
 if k=='schwach':
  return circle(110,215,33,B)+text(110,223,'L',25,WHITE,600,'middle')+circle(340,215,33,A)+text(340,223,'R',25,WHITE,600,'middle')+line(151,215,298,215,G,3,True)+text(225,205,'?',40,C,600,'middle')+text(225,285,'ungleiche Kopplung gesucht',18,G,anchor='middle')+label('Chirale Dynamik fehlt')
 if k=='higgs':
  return path('M 85 155 C 125 375 167 290 225 220 C 285 290 330 375 367 155',C,4,True)+circle(151,281,9,A,A)+line(151,275,151,210,A,2,True)+text(225,175,'V(φ) ?',27,WHITE,600,'middle')+label('Symbol eines Kandidaten · nicht abgeleitet')
 if k=='generationen':
  s=''
  for x,n in [(90,'I'),(200,'II'),(310,'III')]:
   s+=f'<rect x="{x}" y="165" width="70" height="126" rx="14" fill="#16283e" stroke="{B}" stroke-dasharray="6 6"/>'
   s+=text(x+35,212,n,27,WHITE,600,'middle')+text(x+35,265,'?',26,A,600,'middle')
  return s+label('Ziel: drei Familien, kein Modellresultat')
 if k=='messdaten':
  s=''
  for x,name,c in [(60,'Modell',B),(180,'Prognose',A),(310,'Daten',C)]:
   s+=f'<rect x="{x}" y="192" width="90" height="65" rx="12" fill="#16283e" stroke="{c}"/>'+text(x+45,231,name,17,WHITE,500,'middle')
  return s+line(153,225,175,225,G,2,True)+line(273,225,303,225,G,2,True)+text(225,298,'Abgleich noch offen',20,A,anchor='middle')+label('Schranken → konkrete Vorhersagen')
 if k=='quantengravitation':
  s=''
  for i in range(3):
   y=160+i*57;pts=[(85+i*15,y),(190+i*15,y-20),(325+i*15,y+5)]
   s+=mesh(pts,[(0,1),(1,2),(0,2)])
   if i<2:
    for x,z in pts:s+=line(x,z,x+15,z+57,B,1.5,True)
  return s+label('Zeitschichten · wechselnde Geometrie')
 raise ValueError(k)

for i,(slug,title,pct,subtitle,known,missing,source) in enumerate(DATA,1):
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="480" viewBox="0 0 1000 480" role="img" aria-labelledby="title desc"><title id="title">{escape(title)} — Forschungsschema</title><desc id="desc">{escape(subtitle+". Befunde: "+" ".join(known)+" Offen: "+" ".join(missing)+f". Subjektiver Entwicklungsstand {pct} Prozent, kein Messwert.")}</desc>'
 s+='<rect width="1000" height="480" rx="22" fill="#0b1423"/><rect x="1" y="1" width="998" height="478" rx="21" fill="none" stroke="#2d3a4e"/><g font-family="DejaVu Sans, sans-serif">'
 s+=text(35,43,f'FORSCHUNGSATLAS / {i:02d}',13,C,600)+text(35,90,title,31,WHITE,600)+text(35,120,subtitle,18,G)
 s+=text(960,67,f'{pct} %',31,C,600,'end')+text(960,92,'subjektive Schätzung',13,G,anchor='end')
 s+=f'<rect x="790" y="108" width="170" height="5" rx="2" fill="#26374c"/><rect x="790" y="108" width="{170*pct/100}" height="5" rx="2" fill="{C}"/>'
 s+=diagram(slug)+line(454,160,454,360,'#26374c',1)
 s+=text(490,181,'BEFUNDE / VORARBEITEN',13,C,600)
 for j,t in enumerate(known):s+=text(490,217+j*29,t,18)
 s+=text(490,291,'OFFENE FRAGE',13,A,600)
 for j,t in enumerate(missing):s+=text(490,323+j*26,t,18)
 s+=line(35,391,965,391,'#26374c',1)+text(35,423,'SCHEMA · keine Messdaten · keine maßstäbliche Darstellung',14,G)+text(35,449,'Stand 07.10.2026 · Befunde und Grenzen: verlinkte Projektberichte',13,G)
 s+='</g></svg>'
 (OUT/f'{slug}.svg').write_text(s)

lines=['## Forschungsbereiche in Bildern','','Die Grafiken sind schematische Erklärbilder, keine Simulationsergebnisse oder Messdaten. Prozentwerte sind subjektive Entwicklungsschätzungen zum Stand 07.10.2026. Durch Anklicken lassen sich die Grafiken vergrößern; die Berichte darunter liefern Befunde und Grenzen.','','| | |','|---|---|']
for a,b in zip(DATA[::2],DATA[1::2]):
 cells=[]
 for slug,title,pct,subtitle,known,missing,source in [a,b]:
  cells.append(f'[![{title}: {subtitle}. {pct} % subjektive Schätzung.](assets/research/{slug}.svg)](assets/research/{slug}.svg)<br>**{title}** · [Befunde](coordination/runden-v3/{source})')
 lines.append('| '+' | '.join(cells)+' |')
lines+=['','Modellideen werden auf Passung zum Netz, bekannte Befunde und prüfbare Vorhersagen untersucht. Die Bilder behaupten insbesondere keine Herleitung von Hadronen, Higgs oder Teilchenfamilien.','','<!-- END RESEARCH GRAPHICS -->','']
(OUT/'gallery.inc').write_text('<!-- BEGIN RESEARCH GRAPHICS -->\n'+'\n'.join(lines))
print(f'Generated {len(DATA)} SVGs and gallery fragment')
