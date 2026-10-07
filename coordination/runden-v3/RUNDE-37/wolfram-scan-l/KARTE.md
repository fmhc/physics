# WOLFRAM-SCAN-L: Was bietet das Wolfram Physics Project (Modell-Explorer, Registry) fuer ein Weltmodell, das passt? (Literatur- und Werkzeugkarte, Runde 41)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-04 14:08:05 CEST (date), vor jedem Abruf.
- **Auftrag von Finn (04.10., vor 14:08:05, woertlich):** "scan uns wolfram projects da gibts n modell explorer"
- **Zusammenhang:** Finn will "ein Weltmodell, das passt" (WELTMODELL-REVIEW-1 laeuft). Dem Projekt fehlt vor allem eine
  Buehne mit eigener Dynamik: Unsere Netze sind fest oder gequencht gestreut (Zufallsnetze, Kausalmengen, Finns
  Tetraeder-Netz). Wolframs Modelle sind Hypergraphen mit Ersetzungsregeln, also Netze, die aus einer Regel wachsen;
  ihre Kausalgraphen sind Kausalmengen-aehnlich (Ue3).
- **Projekt-grep (Leitung):** "wolfram", "hypergraph", "SetReplace" nur in der Graphen-Uebersicht vom 09.09.
  (coordination/graphen-brief-20260909.md und Begleitdateien) und am Rand in RUNDE-22/geometrie-stand; keine Karte und
  keine Rechnung. Diese Dateien zuerst lesen.
- Kennzeichen: [S] an der Quelle gelesen, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [ES] eigener Schluss, [H]
  Hypothese.

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung |
|---|---|
| E1 | Es gibt eine oeffentliche "Registry of Notable Universe Models" bzw. einen Modell-Explorer auf wolframphysics.org mit Regeln (Signaturen) und Eigenschaften je Regel (Wachstum, geschaetzte Dimension, Kausalinvarianz u. a.) [L?] |
| E2 | Wolframs Ableitungen: spezielle Relativitaet aus Kausalinvarianz, Einstein-Gleichungen aus Grenzwerten von Dimension und Kruemmung (Gorard), Quantenmechanik aus Multiway-Systemen; als Programm veroeffentlicht, nicht als Vorhersage an Messdaten bestaetigt [L] |
| E3 | Kein Modell der Registry ist als unsere Welt identifiziert; Teilchen (persistente lokale Strukturen) und Spin 1/2 sind hoechstens skizziert [L?] |
| E4 | Es gibt fachliche Kritik (z. B. an Kausalinvarianz als Ersatz fuer Lorentz-Invarianz, an fehlenden Vorhersagen) [L?] |
| E5 | Die Kausalgraphen von Wolfram-Modellen lassen sich wie Kausalmengen behandeln (Myrheim-Meyer-Dimension, Links, Intervalle); ob sie Lorentz-gleichverteilt sind wie eine Poisson-Streuung, ist offen [H] |

## Auftrag (feldforscher)

- Gezielte Abrufe, hoechstens 15, keine Websuche (Kontingent erschoepft): zuerst wolframphysics.org (Startseite,
  "universes"/Registry, Technical Introduction, Bulletins, Visual Summary) und, falls verlinkt, der Modell-Explorer;
  danach hoechstens drei Fachartikel bzw. Kritiken (arXiv). Fundstellen nur aus selbst gelesenem Text, lokale Kopien im
  Kartenordner quellen/. Laesst sich der Explorer nur interaktiv bedienen, beschreiben, was die Seite und ihr Quelltext
  davon zeigen, ohne etwas zu erfinden.
- Je Erwartung den Ausgang mit Fundstelle.
- **Projektbezug (je Punkt [S]/[ES]/[H]):**
  - Welche Bausteine eines Weltmodells liefert ein Wolfram-Modell, die uns fehlen (eigene Dynamik der Buehne,
    Kausalinvarianz, Dimension), und welche fehlen dort ebenso (Spin 1/2, chirale Fermionen, Eichgruppe, Zahlen)?
  - Bezug zu unseren Straengen: Kausalmengen (Ue3, "Zahl = Volumen"), Finns Tetraeder-Netz (gibt es Regeln, die
    Tetraeder- bzw. Simplex-Netze erzeugen?), induzierte Schwerkraft, Lichtgeschwindigkeit im Netz.
  - Kandidatenregeln aus Registry bzw. Explorer, deren Eigenschaften zu 3+1 Dimensionen und Kausalinvarianz passen.
- **Kartenvorschlag:** hoechstens zwei kleine Rechenkarten (<= 10 min je Lauf auf der .69, Python, ohne Wolfram
  Language), die scheitern koennen und nicht vorab ableitbar sind, mit Ableitbarkeitsprobe. Beispiel zum Pruefen [H]:
  eine Registry-Regel in Python nachbauen, den Kausalgraphen wie eine Kausalmenge vermessen (Myrheim-Meyer-Dimension,
  Linkzahlen je Element, Verteilung der Links in der Rapiditaet) und gegen eine Poisson-Streuung in 3+1 vergleichen.
- **Abgabe:** RUNDE-37/wolfram-scan-l/DOSSIER.md und ARBEITSFELD.md; Ergebnis zuerst; Erwartungen mit Ausgang;
  Werkzeugbeschreibung (Explorer, Registry: was kann man damit tun); Projektbezug; Kartenvorschlaege; Quellenliste mit
  Abrufstand; Selbstanzeigen; "Einfach gesagt".

## Rahmen

- Zeitbox 60 min. Kein Rechnen; lokal kein python, awk oder perl.
