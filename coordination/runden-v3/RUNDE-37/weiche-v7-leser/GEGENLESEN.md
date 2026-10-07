Urteil: nicht weitergabefaehig ohne Berichtigung (3 A, 9 B, 9 C); nach A1 bis A3 weitergabefaehig.

# GEGENLESEN WEICHE-STAND-v7 (Runde 43)

- Leser: pruefer-opus (Haus Anthropic), frisch, kein Fork.
- Beginn: 2026-10-04 19:31:25 CEST (date). Zeitbox 45 min, also bis 20:16:25 CEST.
- Ende des Pruefens: 2026-10-04 19:47:29 CEST (date); Dauer 16 min 4 s. Pruefobjekt waehrend der Pruefung unveraendert
  (mtime 19:30:32.038, per ls --full-time um 19:44:34 und 19:47:29; um 19:31 per ls -la 19:30).
- Arbeitsweise: nur gelesen (sed -n, grep, diff, ls, wc, date); keine Laeufe, kein Interpreter, keine Abrufe. Eine
  Ausnahme beim Schreiben steht unter "Selbstanzeige".
- Auftrag: /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-37/weiche-v7-leser/KARTE.md
- Pruefobjekt: /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-43/WEICHE-STAND-v7.md (108 Zeilen, nicht veraendert)
- Hinweis: Die Leitung nannte keinen sha256 der KARTE; gelesen wurde die Fassung mit mtime 19:30.

## Gesamturteil

**Nicht weitergabefaehig ohne Berichtigung: 3 A-, 9 B-, 9 C-Befunde.** Erst nach A1 bis A3 weitergeben, B1 bis B9 nach
Moeglichkeit mit.

- Schritt 1 haelt: A1 bis A8 des v6-Lesers sind woertlich umgesetzt (A2 in der Zelle sinngemaess). B1 bis B16 sind
  umgesetzt, B5 nur im Kern; B12 ist durch den Nachtrag der Leitung sogar besser belegt.
- Die Zahlen der neuen Stellen sind richtig uebertragen (nachgerechnet: Guertel-Winkel und -Energien, Q-Ball-Ladungen,
  D*-Gesetz).
- Falsch oder zu stark sind drei neue Stellen:
  - A1 Marolf: Der Ausweg verliert seine Bedingung (Eichredundanz) und seinen Preis (Schwerkraft eingesetzt). Aus
    "erlaubt" wird "Schwerewellen ja". Finns Antwort auf die Rueckfrage liegt vor, die Datei nennt sie offen.
  - A2: Das D*-Maximum gilt laut Quelle nur fuer eine Definition, nicht fuer endliche Wuerfel, und war vorab bekannt.
  - A3: Kontinuumsrechnungen (Q-Ball, Stringgas) stehen in der Spalte "feste Nachbarn".
- Die B-Befunde betreffen fehlende Geltungsbereiche (CDT, BDGH, Brandenberger/Vafa, ISO-ATEM, ATEM-NETZ), einen
  verdeckten Gegenbefund beim Guertel, die Vermischung von Raumdimension und innerer Symmetrie und den fehlenden
  Gegenlesestand.
- Die Negativliste ist woertlich und sinngemaess eingehalten.

## Schritt 1: Umsetzung A1 bis A8 und B1 bis B16 des v6-Lesers

Gelesen: weiche-v6-leser/GEGENLESEN.md ganz; Fassung 7 ganz; wortweiser `diff` Fassung 6 gegen 7. Zeilen in Fassung 7
nach `cat -n`.

| Befund | Stand in Fassung 7 |
|---|---|
| A1 XI-KUGEL | woertlich (Z. 52) |
| A2 Lesart Schwerkraft und Zelle | Lesart woertlich (Z. 75-78); Zelle sinngemaess ("antwortet keine ... auf konforme Verformung wie Einstein; der Spin-2-Teil ist ungemessen", Z. 52) |
| A3 WEYL "nicht nachweisbar" | woertlich (Z. 51) |
| A4 Tempo | beide Ersatztexte woertlich (Z. 55, Z. 87-89) |
| A5 Lesart Haendigkeit | woertlich (Z. 81-85) |
| A6 Wolframs Kausalgraphen | woertlich (Z. 58) |
| A7 KERNMASSE | woertlich (Z. 53) |
| A8 TWIST-PYRO-1 | woertlich (Z. 54) |
| B1 Kuerzungsliste | umgesetzt (Z. 16-21); die anderen Punkte der B1-Liste sind in die Tabelle zurueck (B2, B3, B4, B14, A4, A8). Rest: Der Lesart-Punkt "Ein Tempo fuer alles" (Z. 87) traegt weiter keine Marke, obwohl er nach Fassung 5 neu ist (C-Befund C1 unten) |
| B2 Tensor-Eis | woertlich (Z. 50) |
| B3 QCA | woertlich (Z. 54) |
| B4 CDT | woertlich (Z. 56) |
| B5 KOVARIANZ | im Kern umgesetzt (KV0 mit Zahlen, KOVARIANZ-KUGEL-1 und -EPS-1 jetzt [E]); WEYL-LINEAR-1 steht weiter als [G], Quelle "Ergebnis [E]" (RUNDE-42.md Z. 831); STRICH-NETZ-1 hat in der Ernte kein Kennzeichen (Z. 182). C-Befund C2 |
| B6 EINE-WELT | woertlich (Z. 50) |
| B7 PACHNER | woertlich (Z. 50 und Z. 56) |
| B8 STRICH | woertlich (Z. 55), 3D auch in Z. 51 |
| B9 TWIST-SPIN | woertlich (Z. 54) |
| B10 TAKT-RAND | woertlich (Z. 54) |
| B11 Auswege | woertlich in der Tabelle (Z. 54); die Lesart (Z. 84) nennt nach A5 nur drei Auswege ohne "quasilokale Nicht-Hamilton-Schritte" (C-Befund C3) |
| B12 BLACKMON | sinngemaess und besser belegt: "[S, Verlagsfassung S. 101 laut Nachtrag der Leitung; der Agent las nur Abstract und Vortragsseite]" (Z. 55). Gedeckt durch blackmon-meow-l/NACHTRAG-LEITUNG.md Z. 1 und Z. 18 ("Postulat (S. 101)") und RUNDE-41.md Z. 680, 784 |
| B13 Tetraeder-Netz-Lesart | umgesetzt (Z. 90-100: GLUONEN-L als "Literatur und Schreibtisch", KOPPLUNG-TETRA-1 genannt, GEMEINSAMES-NETZ-v1 als nicht gegengelesener Entwurf) |
| B14 SWERVE | woertlich (Z. 57) |
| B15 Dimension | umgesetzt (Z. 66-71 und Dimensionsangaben in den Zellen) |
| B16 "ohne Abstimmung" | woertlich, dazu der Faktor 1,13 (Z. 55; siehe C-Befund C4) |

**Ergebnis Schritt 1:** A1 bis A8 sind woertlich bzw. (A2-Zelle) sinngemaess umgesetzt; B1 bis B16 sind umgesetzt, B5
nur im Kern. Kein A-Befund des v6-Lesers ist offen. Von den v6-C-Befunden (nicht verlangt) sind C7 ("Als naechstes" laeuft
schon) und C2 ("TT-Mode" in der Legende) weiter offen.

## Schritt 2: [neu in Fassung 7]-Stellen vorwaerts und rueckwaerts

Gelesen: RUNDE-43.md ganz (Ernten und Protokoll); gemeinsames-netz-l/DOSSIER.md Z. 15-60 und per grep (Marolf, BDGH,
CDT, D-Theorie); dim-auswahl-l/DOSSIER.md Z. 15-52 und Quellenliste; Ergebnis-Abschnitte von guertel-feld-stab-1,
guertel-2 (Z. 18-48, 153), guertel-1 (Z. 14-34), iso-atem-1, atem-netz-1 (per grep), dim-leiter-qball-1,
verschraenk-dim-1 (per grep); schreibtisch-leser A4; AGENTS.md Z. 127-138. Zwischenstand notiert 19:43 (date).

| Stelle (Fassung 7) | vorwaerts (Satz zur Quelle) | rueckwaerts (Quelle zum Satz) | Einstufung |
|---|---|---|---|
| Z. 50 BDGH | Kern gedeckt (Dossier Z. 27-33) | fehlt "geisterfrei, mit hoechstens zwei Ableitungen"; Quelle ist "[S Abstract]", Datei "[S laut Agent]" | B2 |
| Z. 52 Marolf | Satz gedeckt (Dossier Z. 17-20, Volltext) | Ausweg heisst in der Quelle "Geometrie mit Zwangsbedingungen bzw. Eichredundanz (Regge, CDT; dann ist die Schwerkraft eingesetzt)" (Z. 24-26, 58-60); "dann ja / dann nein" ist [ES] des Agenten (Z. 21-22, 281); Finns Antwort auf R1 liegt vor (RUNDE-43.md Z. 319) | **A1** |
| Z. 52 CDT mit Materie | Abstract-Lage richtig gekennzeichnet | Quelle: stark nur 2D ab d > 1 bzw. 4D mit Torus-Skalar, sonst "Torus bleibt" (Z. 70, 250); Schwerkraft dort eingesetzt, Fermionen ohne Rueckwirkung (Z. 49) | B1 |
| Z. 54 Guertel | 12/24, 450 -> -270, E(720 - theta) auf 2e-10, Sattel, Zerfall ohne Stoss: gedeckt (ERGEBNIS Z. 18-30). Rechnung: 450 - 720 = -270, 420 - 720 = -300; E(270) = 6161,06, E(300) = 7584,65 | geprueft nur bei 420 und 450 Grad; GS1 war "[M Kontinuum, H Gitter]"; GUERTEL-2 ist auch ein Feldlauf (Teil B), dort sprang das Feld auf groeberen Gittern bei 270 bzw. 450 Grad (guertel-2 Z. 36-39); "Im Fadenmodell (GUERTEL-1, -2)" verschweigt das | B3 |
| Z. 54 SO(2) [M] | gedeckt (ERGEBNIS Z. 40-41) | - | ok |
| Z. 59 Q-Ball | 141,5 / 1705 / 2,6e13 gedeckt (Tabelle: 141,497; 1705,24; 2,61e13). Rechnung: 1705,24 / 141,497 = 12,05 (Quelle 12,1) | "kleinste stabile Ladung" heisst in der Quelle "kleinste Ladung mit E < Q"; Q-Ball ist eine radiale Kontinuumsrechnung, keine Netzrechnung | A3 (Spalte), C |
| Z. 59 VERSCHRAENK | D* ~ 0,53 ln N - 0,5 gedeckt. Rechnung: ln 1000 = 6,908; 0,53 x 6,908 = 3,66; minus 0,5 = 3,16, also D* = 3 bei N = 10^3; ln 10^6 = 13,82, 0,53 x 13,82 - 0,5 = 6,82, Quelle D* = 7 | Quelle: "Das Maximum ist eine Eigenschaft dieser Definition, keine gerechnete Aussage ueber endliche offene Wuerfel" (ERGEBNIS Z. 169-172); das Gesetz "stand vorab im Plan ... keine Entdeckung" (Z. 23-26) | **A2** |
| Z. 59 Brandenberger/Vafa | Zaehlregel gedeckt (Dossier Z. 17-19) | Quelle "generisch"; BV ist [L] ("als Ref. 1 bei ABE gesehen", Z. 19, 431), nicht [S]; "Von selbst pendelt sich nichts bei 3 ein", Glocke ueber 0 bis 9 (EGJK, Z. 24-28); Regel gilt "nur fuer glatte Faeden und eine Topologie mit Schleifen" (Z. 50) | B4 |
| Z. 59 Spaltenwahl | - | Q-Ball (radial, Kontinuum) und Stringgas (Kontinuum, Torus) stehen in Spalte (A) "feste Nachbarn"; nur Z^D ist ein Netz mit festen Nachbarn | **A3** |
| Z. 78-80 Lesart Marolf | - | "Schwerewellen ja" statt "bleiben erlaubt"; Ausnahme ohne Eichredundanz und ohne den Preis "Schwerkraft eingesetzt" | **A1** |
| Z. 85-86 Lesart Guertel | gedeckt | "quasistatisch", "ein einziges Gitter", Gegenbefund GUERTEL-2 fehlen | B3 |
| Z. 95-96 ISO-ATEM-1 | P2_13 vorab ableitbar, 222-Form gefunden: gedeckt (ERGEBNIS Z. 21-30, 53-56) | Quelle: "in der Zelle mit 8 Tetraedern", "im Modell starrer Tetraeder exakt null", kleinste Zelle kann es nicht (Z. 38-40, 60); "zwei Arten" aus 600 Zufallsstarts; Literatur belegt die Schar nicht | B5 |
| Z. 97-98 ATEM-NETZ-1 | "2 + 2" nach ~500 Takten, Eisordnung nur mit Rauschen: gedeckt (ERGEBNIS Z. 20-23, 109-110) | ~3e5 Takte gelten fuer die gemittelte Dynamik; volle Dynamik nur bis 10 000 Takte (P(1) 0,29 bis 0,30); kein frischer Leser (Z. 160, RUNDE-43.md Z. 282); AN1, AN3, AN4 verfehlt | B6 |
| Z. 99-100 D-Theorie | gedeckt (Dossier Z. 34-38; RUNDE-43.md Z. 211-215) | Grenzen "vektorartig, keine Schwerkraft" fehlen | C |
| Z. 105-108 Als naechstes | - | WEYL-LINEAR-2, GUERTEL-FELD-STAB-2, FADEN-DIM-1, QBALL-DREIPOL-3 laufen schon (RUNDE-43.md Z. 225, 319); Finns Antwort liegt vor | A1 (Finn), C |

Zahlen in den neuen Stellen: alle richtig uebertragen. Die Fehler liegen im Geltungsbereich, in Kennzeichen und in einer
Spaltenwahl.

## Schritt 3: Negativliste, zu starke Saetze, Dimensionsvergleich

- **Negativliste woertlich (grep im Rumpf Z. 37-108, Liste der Datei und die laengere Liste in RUNDE-43.md Z. 9-27):**
  kein Treffer fuer Wurzel, "nur langwellig", "traegt massive", "ab 8", "nur mit Inversion", Gegenteil, String-Netz,
  "nur am Rand", DT3, 104, "gerade J", Raute, Grundzustand, Umlauf, Kantenwert, "harte Kugel", Beruehrungsnachbar,
  Kraftbild, Faltwinkel, Cristobalit, Erwaermen. Treffer nur unverfaenglich: "einseitige Randwelle" (Dreiecks-Takt,
  Z. 54, 69, 83), "vierte Richtung" (Z. 85 nach v6 A5; Z. 100 ausdruecklich "keine neue Spur"), "kein Kleber" (Z. 92),
  GLUONEN-L (Z. 91-92).
- **In anderer Form:** Die neue Atem-Zeile (Z. 95) beruehrt "Cristobalit schrumpft beim Erwaermen" nicht; sie spricht von
  einem Mechanismus ohne Waerme. Kein Negativ-Satz kehrt sinngemaess zurueck. Der Kopf fasst die acht
  Schreibtisch-Saetze nur noch summarisch, ohne Stichworte (Fassung 6 nannte fuenf); das genuegt, solange die Liste in
  RUNDE-43.md Z. 20-27 gilt.
- **Fruehere A-Befunde:** WEICHE-V6 A1 bis A8 halten (Schritt 1). WEICHE-V3 A4 (Spalten gemischt) ist in neuer Form
  zurueck (A3).
- **Allaussagen:** "nie" und "immer" kommen nicht vor. Neue "nur/kein/nicht"-Saetze:
  - zu stark: Z. 79 "Schwerewellen ja ... ausser" (A1); Z. 59 "3 nur bei rund 1000 Punkten" als Aussage ueber Punkte
    (A2); Z. 52 "Materie veraendert die Geometrie stark" ohne Bereich (B1); Z. 50 "koennen nicht ueber Kreuz koppeln"
    ohne "geisterfrei, hoechstens zwei Ableitungen" (B2); Z. 59 "treffen sich nur in hoechstens 3" ohne "generisch"
    (B4); Z. 95 "auf zwei Arten" ohne Zelle und Startzahl (B5).
  - gedeckt: Z. 52 "kann kein Gauss-Gesetz" mit Gitter- und Lorentz-Angabe; Z. 54 "Gezeigt nur auf einem Gitter" und
    "Im ebenen SO(2)-Feld gibt es keinen Guertel-Trick [M]" (die Gruppe SO(2) hat ganzzahlige Windungen, die sich nicht
    aufheben; SO(3) hat nur zwei Klassen); Z. 59 "keine gelesene Arbeit" (auf Gelesenes begrenzt); Z. 59 "in jeder
    Dimension 1 bis 12" (begrenzt, mit "kein voller Stabilitaetsnachweis").
- **Dimensionsvergleich (AGENTS.md Z. 127-138):**
  - umgesetzt: Liste Z. 66-71, Dimensionsangaben in den Zellen (v6 B15), neue Zeile "Dimensionen".
  - verletzt: Guertel vermischt Raumdimension und innere Symmetrie (B8, AGENTS.md Z. 131); der Q-Ball fehlt in der Liste
    (B8, Z. 135); bei VERSCHRAENK-DIM-1 sind Ableitung und Rechnung nicht getrennt (A2, Z. 134).
- **Lesart gegen Tabelle (KARTE Frage 4):** Schwerkraft Z. 75-78 gedeckt, Z. 78-80 staerker als die Tabelle (A1).
  Haendigkeit Z. 81-85 gedeckt, bis auf die Auswege (C3). Guertel Z. 85-86 schwaecher eingeschraenkt als die Tabelle (B3).
  Tempo Z. 87-89 gedeckt. Tetraeder-Netz Z. 95-98 ohne Tabellenzeile (B7). (B)-Seite Z. 101-102 gedeckt.

## A-Befunde (vor Weitergabe zu berichtigen)

Datei jeweils /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-43/WEICHE-STAND-v7.md; Zeilen nach `cat -n`.

- **A1 Marolf: Ausweg ohne Bedingung, "Schwerewellen ja", Finns Antwort fehlt (Z. 52, Z. 78-80, Z. 108).**
  - Quelle gemeinsames-netz-l/DOSSIER.md Z. 20: "Lineare Spin-2-Wellen bleiben erlaubt [S]". Die Lesart macht daraus
    "Schwerewellen ja". Erlaubt heisst nicht gezeigt. Die Verschaerfung stammt aus der Ernte (RUNDE-43.md Z. 223,
    "Bedeutung"), nicht aus dem Dossier.
  - Der Ausweg heisst in der Quelle Z. 24-26: "die Kantenlaengen sind selbst die Geometrie mit Zwangsbedingungen
    (Regge, CDT; dann ist die Schwerkraft eingesetzt)". Z. 58-60 nennt ihn "die Geometrie traegt Eichredundanz". Die
    Ernte Z. 199 hat "mit Eichredundanz" noch, Fassung 7 hat es in Tabelle und Lesart nicht mehr. "ausser das Netz ist
    selbst die Geometrie" liest sich dann wie ein Weg zu Einstein-Schwerkraft. In der Quelle ist es nur der Fall, in dem
    der Satz nicht greift, und die Schwerkraft ist dort eingesetzt.
  - "dann ja / dann nein" ist eine Einordnung des Agenten [ES] (Dossier Z. 21-22, Tabelle G-e Z. 281), kein [S].
  - Finn hat R1 beantwortet: "der raum ist das netz denke ich" (RUNDE-43.md Z. 319, "zwischen 19:28 und 19:31"). Die
    Leitung folgert dort selbst: "Umbauten des Netzes muessen Umbenennungen (Eichredundanz) sein, wie bei Regge/CDT".
    Fassung 7 (mtime 19:30:32) sagt "Rueckfrage an Finn offen" (Z. 52) und fuehrt seine Antwort unter "Als naechstes"
    (Z. 108). Wer die Datei an Finn weitergibt, meldet ihm damit seine eigene Antwort als ausstehend.
  - Ersatz Z. 52 ab "Ob das Finns Netz trifft": "Ob das Finns Netz trifft, ist eine Einordnung des Agenten [ES]: ja,
    wenn seine Kantenlaengen physikalische Groessen auf einem festen Geruest sind; nein, wenn das Netz selbst die
    Geometrie ist und Umbauten nur Umbenennungen sind (Eichredundanz, wie bei Regge oder CDT); dann ist die Schwerkraft
    aber eingesetzt, nicht entstanden. Finn sieht sein Netz als die Geometrie selbst ('der raum ist das netz denke
    ich', 04.10.); ob es diese Eichredundanz traegt, ist offen."
  - Ersatz Z. 78-80: "[neu in Fassung 7] Fuer feste Netze mit lokaler Kinematik (Seite A) gibt es einen Satz (Marolf
    2015): Lineare Schwerewellen bleiben erlaubt, Einstein-Schwerkraft ist ausgeschlossen. Der Satz greift nicht, wenn
    das Netz selbst die Geometrie mit Eichredundanz ist; dann ist die Schwerkraft eingesetzt wie bei Regge oder CDT. Finn
    sieht sein Netz als die Geometrie selbst; ob es diese Eichredundanz traegt, ist offen."
  - Ersatz Z. 108: "- Folge aus Finns Antwort ('der raum ist das netz'): pruefen, ob Umbauten seines Netzes
    Umbenennungen sind (Eichredundanz wie bei Regge/CDT)".
- **A2 VERSCHRAENK-DIM-1: Maximum als Aussage ueber N Punkte (Z. 59).**
  - Quelle verschraenk-dim-1/ERGEBNIS.md Z. 169-172: Am Maximum hat die Kante nur L = 5,6 bis 10; gerechnet ist
    "Dichte im unendlichen Gitter mal Flaeche ... Das Maximum ist eine Eigenschaft dieser Definition, keine gerechnete
    Aussage ueber endliche offene Wuerfel". Dazu Z. 23-26: Das Gesetz "folgt schon aus S_D ~ ln(D)/D^2 und stand vorab
    im Plan ... Es ist keine Entdeckung" (ebenso RUNDE-43.md Z. 144-149).
  - "bei fester Punktzahl N liegt das Maximum bei D* ..., also 3 nur bei rund 1000 Punkten" liest sich als Befund ueber
    ein System aus N Punkten. Genau das schliesst die Quelle aus. Auch die Trennung von Ableitung und Rechnung
    (AGENTS.md Z. 134) fehlt hier.
  - Ersatz: "Freies Feld auf Z^D: Verschraenkung je Randplatz faellt mit D (vorab ableitbar). Rechnet man bei fester
    Punktzahl N mit 'Dichte im unendlichen Gitter mal Schnittflaeche', liegt das Maximum bei D* ~ 0,53 ln N - 0,5, also
    3 bei rund 1000 Punkten; das Gesetz folgt aus S_D ~ ln(D)/D^2 und stand vorab im Plan. Am Maximum hat jede Kante
    nur 6 bis 10 Plaetze; ueber endliche offene Wuerfel sagt das nichts (VERSCHRAENK-DIM-1) [E, M]."
- **A3 Zeile "Dimensionen" in Spalte (A) (Z. 59): Spalten gemischt, Rueckfall der Fehlerart WEICHE-V3 A4.**
  - Spalte (A) heisst "feste Nachbarn" (Z. 39-40, 48). Der Q-Ball ist eine radiale Kontinuumsrechnung
    (dim-leiter-qball-1/ERGEBNIS.md, Gitter h = 0,0125 in r). Brandenberger/Vafa ist ein Stringgas im Kontinuum auf
    einem 9-Torus (dim-auswahl-l/DOSSIER.md Z. 149). Nur das freie Feld auf Z^D ist ein Netz mit festen Nachbarn.
  - In der Weiche liest man die Zelle als Befund fuer Seite (A). Das ist die Fehlerart von WEICHE-V3 A4 (Ergebnis
    einer Art in die Spalte einer anderen); der v6-Leser hatte sie als A4 zurueckgeholt.
  - Ersatz: die Zeile aus der Tabelle nehmen und unter die Tabelle setzen, Kopf woertlich: "**[neu in Fassung 7]
    Dimensionen (keiner Spalte zugeordnet; nur das freie Feld auf Z^D ist ein Netz mit festen Nachbarn, Q-Ball und
    Stringgas sind Kontinuumsrechnungen):**". Darunter die drei Saetze, mit A2 und B4 berichtigt. Falls die Zeile in
    der Tabelle bleibt, soll die Zelle mit diesem Klammertext beginnen.

## B-Befunde

- **B1 CDT mit Materie (Z. 52, Spalte C): Geltungsbereich fehlt.** Quelle gemeinsames-netz-l/DOSSIER.md Z. 250: "d <= 1
  bzw. gewoehnliche Skalare: Torus bleibt | d > 1 bzw. Torus-Skalar: Kugel bzw. Topologiewechsel"; Z. 49: "Schwerkraft
  eingesetzt, Fermionen nur ohne Rueckwirkung". In der Zeile "Schwerkraft aus Materie" kann der Satz als
  Sakharov-Beleg gelesen werden; die Schwerkraft ist dort aber eingesetzt. Vorschlag: "[neu in Fassung 7] CDT mit
  Materie (Schwerkraft dort eingesetzt): Materie kann die Geometrie stark veraendern (2D ab d > 1, 4D mit einem
  Skalar, dessen Werte auf einem Kreis liegen); mit d <= 1 bzw. gewoehnlichen Skalaren bleibt der Torus; Fermionen nur
  ohne Rueckwirkung (GEMEINSAMES-NETZ-L) [S Abstract laut Agent]".
- **B2 BDGH (Z. 50): Bedingungen und Kennzeichen.** Quelle Z. 28-31 und Tabelle P1 Z. 82: "no consistent (ghost-free)
  coupling, with at most two derivatives", "[S Abstract]". Vorschlag: "Masselose Gravitonen koennen ohne Geister und mit
  hoechstens zwei Ableitungen, also im langwelligen, Lorentz-invarianten Grenzfall, nicht ueber Kreuz koppeln; erlaubt
  ist nur eine Summe getrennter Einstein-Wirkungen (Boulanger/Damour/Gualtieri/Henneaux 2001; GEMEINSAMES-NETZ-L)
  [S Abstract laut Agent]".
- **B3 Guertel (Z. 54, Z. 85-86): Gegenbefund und Pruefbereich fehlen.**
  - Geprueft sind nur 420 und 450 Grad (guertel-feld-stab-1/ERGEBNIS.md Z. 20), auf einem einzigen Gitter (Z. 141).
    GS1 war "[M Kontinuum, H Gitter]": Im Kontinuum ist der Trick Mathematik, offen war nur das Gitter.
  - GUERTEL-2 ist nicht nur ein Fadenmodell. Teil B rechnete dasselbe Feld, und es sprang "grob bei 270 Grad, fein
    (6, 24) bei 450 Grad, (12, 24) bei 540 Grad" (guertel-2/ERGEBNIS.md Z. 36-39). Nur fuer (12, 24) erklaert
    GUERTEL-FELD-STAB-1 den Sprung mit dem zu schnellen Protokoll, und auch das nur als [H] (Z. 34-35). "Im
    Fadenmodell nicht gezeigt (GUERTEL-1, -2)" verdeckt diesen Gegenbefund.
  - Vorschlag Z. 54: "... (450 -> -270 Grad; geprueft bei 420 und 450 Grad; ...). Im Kontinuum ist der Guertel-Trick
    Mathematik [M]; neu ist, dass dieses Gitter ihn ohne Sprung zulaesst. In den Faden-Knoten nicht gezeigt (GUERTEL-1,
    GUERTEL-2 Teil A) [G]. Im Feld sprang das Drehprotokoll von GUERTEL-2 auf groeberen Gittern bei 270 bzw. 450 Grad;
    ob das am Protokoll lag, prueft GUERTEL-FELD-STAB-2."
  - Vorschlag Z. 85-86: "Den Guertel-Trick hat ein SO(3)-Drehfeld auf einem einzigen 3D-Gitter gezeigt, quasistatisch,
    glatt und ohne Sprung; auf groeberen Gittern sprang das Feld frueher, die Robustheit wird geprueft."
- **B4 Brandenberger/Vafa (Z. 59): "generisch", Kennzeichen, Gegenbefund.**
  - Quelle dim-auswahl-l/DOSSIER.md Z. 17-19: "treffen sich generisch nur in hoechstens 3 Raumdimensionen",
    "Brandenberger/Vafa 1989 [L]" (Z. 431: "als Ref. 1 bei ABE gesehen"). Z. 50: "gilt aber nur fuer glatte Faeden und
    eine Topologie mit Schleifen". Z. 24-28: "Von selbst pendelt sich nichts bei 3 ein", Glocke ueber 0 bis 9 (EGJK).
  - Vorschlag: "Literatur: Glatte Faeden treffen sich in einem Raum mit Schleifen generisch nur in hoechstens 3
    Raumdimensionen (Brandenberger/Vafa 1989 [L]; als Zaehlargument gelesen bei Alexander/Brandenberger/Easson 2000
    [S]). Einen Attraktor bei 3 gibt es dort nicht: Mit zufaelligem Anfang ist die Zahl grosser Dimensionen eine Glocke
    ueber 0 bis 9 (Easther/Greene/Jackson/Kabat 2004 [S Abb.]). Ein Einpendeln bei 3 bis 4 sagt keine gelesene Arbeit voraus
    (DIM-AUSWAHL-L)".
- **B5 ISO-ATEM-1 (Z. 95-96): Geltungsbereich fehlt.** Quelle iso-atem-1/ERGEBNIS.md Z. 21, 38-40, 60: "in der Zelle mit 8
  Tetraedern", "im Modell starrer Tetraeder exakt null", "keiner existiert in der kleinsten Zelle"; die zwei Arten
  stammen aus 600 Zufallsstarts (Z. 26-27); die Literatur belegt die Schar nicht (Z. 54-55). Vorschlag: "Im Modell
  starrer Tetraeder kann es in der Zelle mit 8 Tetraedern ohne Energie in alle Richtungen gleich schrumpfen und
  zurueck; aus 600 Zufallsstarts fanden sich zwei Arten (P2_13-Schar, vorab ableitbar; zweite Form mit Punktgruppe
  222, gefunden); die kleinste Zelle kann es nicht (ISO-ATEM-1) [E]."
- **B6 ATEM-NETZ-1 (Z. 97-98): gemittelte Dynamik und Gegenlesestand.** Quelle atem-netz-1/ERGEBNIS.md Z. 20-23 und
  109-110: Die volle Dynamik lief bis 10 000 Takte (P(1) 0,29 bis 0,30); "~3e5 Takte" und "nur mit Rauschen" gelten fuer
  die gemittelte Dynamik. Z. 160: "Kein frischer Leser hat diese Datei gegengelesen." Vorschlag: "Atmende Punkte an
  seinen Ecken ordnen sich nach etwa 500 Takten je Tetraeder 'zwei so, zwei gegen'; eine gemeinsame Eisordnung
  entsteht in 10 000 Takten nicht, in der gemittelten Dynamik erst mit Rauschen nach rund 300 000 Takten (ATEM-NETZ-1)
  [E; kein frischer Leser]."
- **B7 Lesart ohne Tabelle (Z. 95-98):** ISO-ATEM-1 und ATEM-NETZ-1 stehen nur in der Lesart, in keiner Tabellenzeile
  (Fehlerart v6 B13). Vorschlag: eine Zeile "[neu in Fassung 7] Atmen des Netzes" in Spalte (A) mit dem Wortlaut aus
  B5 und B6; die Lesart verweist dann nur darauf.
- **B8 Dimensionsliste, Guertel (Z. 70): Raumdimension und innere Symmetrie vermischt.**
  - AGENTS.md Z. 131: "Räumliche Dimensionen von Feldkomponenten und inneren Symmetrien unterscheiden."
  - GUERTEL-2 rechnete SO(2) auf Z^2 und SO(3) auf Z^3 (guertel-2/ERGEBNIS.md Z. 153). Beides wechselte zugleich.
    Der Trick haengt an der Gruppe der Feldwerte, also an der inneren Symmetrie (SO(2) ohne, SO(3) mit [M]).
    "Ebene ... Raum" unter der Ueberschrift "Dimension" legt eine Raumdimension als Grund nahe. Ausserdem waechst die
    Energie wie k^2, nicht die Verdrillung (Z. 34: 175; 695; 1550; 2718; Rechnung: 695/175 = 3,97, 1550/175 = 8,86,
    2718/175 = 15,5 gegen 4, 9, 16).
  - Vorschlag: "- Guertel: entscheidend ist die innere Symmetrie der Feldwerte, nicht die Raumdimension. SO(2)-Werte
    (gerechnet auf Z^2): Energie waechst etwa wie k^2, kein Guertel-Trick [M]. SO(3)-Werte (gerechnet auf Z^3, ein
    Gitter): 720 Grad werden glatt abgelegt. SO(2) auf Z^3 und SO(3) auf Z^2 sind nicht gerechnet."
  - Dazu fehlt in der Liste der Q-Ball. Vorschlag: "- Q-Ball D = 1 bis 12: radial, also weder ein 1D-Modell noch ein
    voller Stabilitaetsnachweis (AGENTS.md Z. 135)".
- **B9 Gegenlesestand der neuen Quellen fehlt (Kopf Z. 14):** Laut Ernten ist GEMEINSAMES-NETZ-L "nicht gegengelesen"
  (RUNDE-43.md Z. 191). DIM-AUSWAHL-L hat "Kopfrechnungen ohne Gegenlesen" (Z. 110), ISO-ATEM-1 "Handrechnung nicht
  gegengelesen" (Z. 273), ATEM-NETZ-1 "kein frischer Leser" (Z. 282). Fuer TENSOR-EIS fuehrt die Datei den Stand
  (Z. 50). Vorschlag fuer den Kopf: "Die Quellen GEMEINSAMES-NETZ-L, DIM-AUSWAHL-L, ISO-ATEM-1 und ATEM-NETZ-1 hat
  kein frischer Leser gegengelesen."

## C-Befunde

- **C1 (Z. 87):** Der Lesart-Punkt "Ein Tempo fuer alles" ist seit Fassung 6 neu und traegt weiter keine Marke (Rest von
  v6 B1). Vorschlag: "[neu in Fassung 6, berichtigt nach A4]".
- **C2 Kennzeichen [G] statt [E]:** WEYL-LINEAR-1 (Quelle "Ergebnis [E]", RUNDE-42.md Z. 831; Rest von v6 B5). Ebenso alle
  neuen Rechenkarten: GUERTEL-FELD-STAB-1, ISO-ATEM-1, ATEM-NETZ-1 und DIM-LEITER-QBALL-1 haben in Quelle und Ernte
  [E], VERSCHRAENK-DIM-1 [E, M].
- **C3 (Z. 84):** Die Lesart nennt drei Auswege, die Tabelle (Z. 54) nach v6 B11 vier ("quasilokale
  Nicht-Hamilton-Schritte"). Angleichen.
- **C4 (Z. 55) "etwa 1,13":** Der Faktor gilt nur fuer eine Regel mit Tempo 0,939 (v6 B16: 1/0,939^2 = 1/0,882 = 1,13).
  Fuer die genannte Spanne 0,887 bis 0,972: 0,972^2 = 0,945, 1/0,945 = 1,06; 0,887^2 = 0,787, 1/0,787 = 1,27.
  Vorschlag: "(je nach Regel etwa 1,06 bis 1,27)".
- **C5 (Z. 103-107) "Als naechstes":** WEYL-LINEAR-2, GUERTEL-FELD-STAB-2, FADEN-DIM-1 und QBALL-DREIPOL-3 laufen schon
  (RUNDE-43.md Z. 225 und 319; v6 C7). Vorschlag: "Laufen und werden als naechstes geerntet".
- **C6 (Z. 59) "kleinste stabile Ladung":** Die Quelle sagt "kleinste Ladung mit E < Q" (dim-leiter-qball-1/ERGEBNIS.md,
  Ergebnis 1). Der VK-Wendepunkt liegt tiefer (D = 3: Q_min 111,9 gegen Q_s 141,5). Vorschlag: "die kleinste Ladung mit
  E < Q".
- **C7 (Z. 99-100) D-Theorie:** Es fehlen die Grenzen aus der Quelle (Dossier Z. 38, 236; RUNDE-43.md Z. 201-202): Die
  Haendigkeit ist vektorartig (QCD, nicht die schwache Kraft), Schwerkraft fehlt, die Geometrie ist fest. Ein
  Halbsatz genuegt.
- **C8 Legende:** Neue Begriffe ohne Erklaerung: SO(3)-Drehfeld, P2_13, Punktgruppe 222, Gauss-Gesetz fuer Energie,
  lokale Kinematik, Z^D, D*, VK. "TT-Mode" kommt in der Tabelle weiter nicht vor (v6 C2).
- **C9 ausserhalb des Pruefobjekts, nur zur Kenntnis:** RUNDE-43.md Z. 264-265 nennt "V/V0 ~ cos^2(phi)" und
  "lambda = 0,5 (V/V0 = 0,125, Kippwinkel 60 Grad)". Rechnung: cos 60 Grad = 0,5, cos^2 = 0,25, nicht 0,125; dagegen
  0,5^3 = 0,125. Die Quelle (iso-atem-1/ERGEBNIS.md Z. 31-32) sagt nur "fast genau cos^2" und belegt das bis 50 Grad
  (cos^2 50 Grad = 0,413 gegen 0,394). Bei grossen Winkeln gilt die Faustregel nicht. Fassung 7 uebernimmt die Zahl
  nicht.

## Selbstanzeige

- Um etwa 19:40 habe ich eine Hilfsdatei (Kopie der Zeilen 37 bis 108 des Pruefobjekts, keine Geheimnisse, keine
  gesperrten Daten) im Scratchpad der Leitung angelegt, um den grep zu vereinfachen. Das verstoesst gegen "nichts in den
  Scratchpad der Leitung". Ich habe sie um 19:41:05 (date) wieder geloescht. Sonst habe ich nur in diesen Ordner
  geschrieben.
- Den Inhalt der Kopie habe ich nur fuer den Negativlisten-grep genutzt.

## Einfach gesagt

Die Leitung hat alle Korrekturen des letzten Pruefers sauber eingebaut, und die neuen Zahlen stimmen. Bei den neuen
Literaturstellen fehlt aber oft das Kleingedruckte. Ein Beispiel: Ein Satz von Marolf sagt, dass ein festes Netz keine
echte Einstein-Schwerkraft hervorbringen kann. Die Ausnahme "das Netz ist selbst die Geometrie" hilft nur, wenn
Umbauten des Netzes blosse Umbenennungen sind, und dann ist die Schwerkraft hineingesteckt, nicht entstanden. Ausserdem
hat Finn die Rueckfrage schon beantwortet, und zwei Ergebnisse stehen in der falschen Spalte oder klingen allgemeiner,
als die Rechnung hergibt; mit drei kurzen Textaenderungen ist die Datei weitergabefaehig.
