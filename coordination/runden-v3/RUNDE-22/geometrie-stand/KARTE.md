# GEOMETRIE-STAND: Winkelspannung als Feld und Dimension aus einer Simplex-Suppe, Literaturstand gegen unsere Befunde (Runde 22)

- Leitung: claude-primary. Karte und Erwartungen geschrieben ab 2026-10-02 20:25:52 CEST (date), vor jedem Abruf.
- Anlass, Finns Fragen 02.10. abends:
  - "wie weit waren wir grundsaetzlich mit unseren annahmen gekommen, dass punkte -> striche -> dreiecke ->
    mehrdimensionalitaet - was ist stabil dimensionsmaessig, wie spannt sich der stoff und koennen gekoppelte thetraeder
    in 3d koppeln ueber winkelspannung als feldgroesse?"
  - "und wie weit waren wir mit 1+2+3+4+xD teilchen die eine ursuppe bilden und daraus logik ueber geometrie entsteht?"
- Unsere Befunde [S, eigene Rechnungen R16/R17]:
  - Thomson: 12 und 6 stabil, 8 Sattel, 11 anti-magisch.
  - Nur Dreiecksgitter und fcc sind mit Naechster-Nachbar-Federn starr.
  - Tetraeder lassen um eine Kante 7,36 Grad Luecke; die Frustration je Tetraeder waechst mit der Klumpengroesse; zwei
    Ikosaeder zu koppeln kostet Energie (Delta = +0,0043).
  - Elastische Kopplung von Klumpen: 1/d^4 (rund in rundem Medium, 2D), 1/d^2 (unrund, 2D), 1/d^3 (fcc), mit
    richtungsabhaengigem Vorzeichen.
  - Der Beutelexponent misst die spektrale Dimension.
  - Arbeitsmodell v2.3: Zeit und Einbettung sind vorausgesetzt; die einbettungsfreie Variante B hat keine Dynamik.
- Explorativ (v3), Literatur- und Schreibtischkarte.

## Fragen

1. **Winkelspannung als Feldgroesse:** Wie behandeln Regge-Kalkuel (Fehlwinkel an Kanten als Kruemmung) und die
   geometrische Defekttheorie (Disklinationen als Kruemmungsquellen, Versetzungen als Torsion; z. B. Katanaev/Volovich,
   Kroener, de Wit, Kleman) die Kopplung von Winkeldefekten?
   - Welche Reichweiten haben geschlossene Klumpen (netto ohne Winkelladung) gegenueber offenen Disklinationslinien?
   - Was gilt in 2D, 3D und 4D? Ist es z. B. richtig, dass in reiner 3D-Gravitation bzw. im 3D-Regge-Vakuum ruhende
     Punktdefekte keine Kraft aufeinander ausueben?
2. **Wie spannt sich der Stoff:**
   - Frustration in flachem 3D (Tetraeder) gegen perfekte Packung auf der gekruemmten 3-Sphaere (600-Zeller); Nelson und
     Sethna zu Frustration und Kruemmung.
   - Frank-Kasper-Netze von Disklinationslinien.
   - 2D-Gegenstueck: Fuenfer-Defekte im Dreiecksnetz, Beulen statt Spannung (Seung/Nelson), und die zwoelf Fuenfer jeder
     Kugel-Triangulierung (Euler).
3. **Dimension aus einer Simplex-Suppe:**
   - Was ergeben dynamische Triangulationen ohne und mit Kausalitaet (Ambjorn/Jurkiewicz/Loll; spektrale Dimension ~2
     klein, 4 gross)?
   - Was ergibt "Quantum Graphity" (Konopka/Markopoulou/Severini)?
   - Welche Regeln braucht es, damit eine stabile Dimension herauskommt?
4. **"Logik aus Geometrie":** Gibt es ernsthafte Ansaetze, in denen logische Struktur (Kausalordnung, boolesche
   Verknuepfungen) aus einer Geometrie- oder Graph-Dynamik folgt (z. B. Kausalmengen, Hypergraph-Umschreibung)? Was
   davon ist rechenbar und pruefbar?
5. **Abgleich und naechster Schritt:**
   - Welche unserer Befunde (oben) sind Literatur, welche bestaetigen sie, welche waeren neu?
   - Vorschlag fuer einen kleinen rechenbaren Test (<= 10 min Laeufe, < 1 h neuer Code) je fuer Frage 1 und 3.

## Erwartungen (vor dem Abruf, Leitung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| G1 | Die Defekttheorie sagt: Geschlossene, winkelneutrale Klumpen koppeln wie Punktdefekte (kurzreichweitig); nur offene Disklinationen tragen ein langreichweitiges Winkelfeld | 75 % |
| G2 | In reiner 3D-Gravitation ueben ruhende Punktteilchen keine Kraft aufeinander aus, sie erzeugen nur Kegelraeume | 85 % |
| G3 | Euklidische dynamische Triangulationen ohne Kausalregel ergeben keine 4D-Welt (zerknuellte oder baumartige Phase); mit Kausalregel eine ausgedehnte 4D-Phase mit spektraler Dimension ~2 bei kleinen Abstaenden | 80 % |
| G4 | Zu "Logik aus Geometrie" gibt es keinen pruefbaren physikalischen Ansatz mit Rechnung, der ueber Kausalordnung hinausgeht | 70 % |

**Bedeutung (vorab):** Treffen G1 bis G3 ein, ist Finns Kette "Punkte -> Striche -> Dreiecke -> Tetraeder,
Winkelspannung als Feld" im Kern der Regge-/Defekt-Rahmen [L]. Neu waere dann nur, was unser Modell darauf setzt
(Q-Baelle als Moden auf solchen Netzen). Der vorgeschlagene Test sollte genau dort ansetzen.

## Rahmen

- Literatur-Agent (feldforscher). Das WebSearch-Kontingent ist erschoepft. Abfragen deshalb ueber WebFetch:
  export.arxiv.org/api/query, api.openalex.org, api.semanticscholar.org; Volltexte bei arXiv, Uebersichtsarbeiten
  bevorzugt.
- Jede Aussage mit Fundstelle und Marke ([S], [L?], [H], [E]); Fehlanzeigen nur "nach Recherchestand". Zitate unter 15
  Woertern. Zeitbox 75 min.
