# Karten: Kann Reflexion Q-Baelle oder ihre Resonanzen stabilisieren? (Finns Frage)

Leitung claude-primary, Zeit vor dem Schreiben gemessen: 2026-09-30 02:22:09 CEST.

Finn woertlich: "wie kann reflexion in diesem kontext ggf auf andere sachen wirken und die stabilisieren?"

## Ausgangslage

- Der Q-Ball hat eine langlebige, ausleckende Resonanz (1D: rho = 1,4938 - 6,7e-5 i; Codex, resonance-20260930/).
- "Ausleckend" heisst: Sie strahlt ab und stirbt deshalb langsam.
- Jeder Mechanismus, der diese Abstrahlung zurueckwirft oder verbietet, kann die Resonanz oder den Ball stabilisieren.
- Das ist bekannte Physik aus Optik und Quantenoptik [L, aus dem Gedaechtnis]:
  - Purcell-Effekt und gehemmte Emission in einer Bandluecke
  - gebundene Zustaende im Kontinuum (Friedrich-Wintgen, Hsu u. a. 2016)
  - optisches Binden und optische Gitter
  - Anderson-Lokalisierung

## Karten (Codex-Format, alle 1D, je hoechstens 10 min)

- **R-1 Bandlueckenschutz (Purcell):**
  - H: Sitzt ein Q-Ball in einer Q-Ball-Kette, deren Bandluecke die Resonanzfrequenz enthaelt, lebt seine Resonanz deutlich
    laenger als allein.
  - Test: linear oder zeitabhaengig; Abklingrate der Resonanz allein, in einer Kette mit Luecke bei rho, in einer Kette
    ohne Luecke bei rho.
  - Gegenprobe: Kette mit gleicher Ballzahl, aber verstimmtem Abstand.
  - Anschluss: W21 (Bragg-Kette).
- **R-2 Dunkler Zustand zweier Baelle (gebundener Zustand im Kontinuum):**
  - H: Bei bestimmten Abstaenden d heben sich die Abstrahlungen zweier gleicher Baelle auf, und die gemeinsame Resonanz
    klingt (fast) nicht mehr ab.
  - Test: Abklingrate gegen d (etwa 10 Werte), linear oder zeitabhaengig.
  - Gegenprobe: ein einzelner Ball; zwei Baelle mit verschiedenem omega (keine Aufhebung erwartet).
- **R-3 Bindung durch Strahlung:**
  - H: Stehende Wellen zwischen zwei Baellen, gespeist aus ihrer Resonanz oder einer schwachen Pumpe, erzeugen eine
    Kraft, die mit dem Abstand schwingt. Deren Minima binden die Baelle bei gequantelten Abstaenden, wie optisches Binden.
  - Test: Kraft bzw. Energie gegen d mit schwacher Pumpe bei rho; gibt es Minima im Abstand ~ halbe Wellenlaenge?
  - Gegenprobe: ohne Pumpe (dort gibt es nur die bekannte kurzreichweitige Phasenkraft).
  - Bedeutung: Das waere ein Weg zur fehlenden Paarbindung (Fable: Chemie 2/3 als Torwaechter).
- **R-4 Methodenwarnung, Randreflexion taeuscht Stabilitaet vor:**
  - H: Mit reflektierendem Rand lebt die Resonanz (und leben Oszillonen) scheinbar ewig; mit absorbierendem Rand nicht.
  - Test: dieselbe Rechnung mit periodischem bzw. reflektierendem gegen daempfenden Rand; Abklingrate.
  - Bedeutung: Kontrolle fuer alle unsere Lebensdauer-Aussagen.
- **R-5 Lokalisierung schuetzt:**
  - H: In einem zufaelligen Q-Ball-Gas wird die Abstrahlung eines angeregten Balls zurueckgestreut (Anderson), und er
    klingt langsamer ab als allein.
  - Test: Abklingrate im Gas gegen allein, mehrere Seeds.
  - Anschluss: W22.

## Einfach gesagt

Der Q-Ball klingt nach wie eine Glocke und verliert dabei langsam Energie nach aussen. Wirft man diesen Schall zurueck,
kann die Glocke viel laenger klingen. Das geht mit einem Spiegel-Kristall, der die Frequenz sperrt, oder mit einem
zweiten Ball im richtigen Abstand, sodass sich die Abstrahlung ausloescht. Vielleicht halten solche Wellen zwei Baelle
sogar in festen Abstaenden zusammen. Ein Stolperstein fuer uns selbst: Wirft der Rand der Rechenbox Wellen zurueck,
sieht alles stabiler aus, als es ist.
