# GEGENLESEN WEICHE-STAND-v6 (Runde 43) -- Urteil: haelt nicht ohne Berichtigung (8 A, 16 B, 8 C)

- Leser: pruefer-opus (Haus Anthropic), frisch, kein Fork. Leitung: claude-primary.
- Auftrag: RUNDE-37/weiche-v6-leser/KARTE.md (ohne sha256 uebergeben; Pfad von der Leitung genannt).
- Pruefobjekt: /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-43/WEICHE-STAND-v6.md (76 Zeilen, 1525 Woerter, nicht veraendert).
- Beginn: 2026-10-04 19:07:26 CEST (date). Zeitbox 45 min, also bis 19:52:26 CEST.
- Ende: 2026-10-04 19:23:36 CEST (date); Dauer 16 min 10 s. Gelesene Fassung des Pruefobjekts: mtime 19:06:09, waehrend
  der Pruefung unveraendert (ls um 19:24:00).
- Arbeitsweise: nur gelesen (cat, sed -n, grep, ls, wc, date); keine Laeufe, kein Interpreter, keine Abrufe.

## Gesamturteil

**Haelt nicht ohne Berichtigung: 8 A-, 16 B-, 8 C-Befunde.** Erst nach A1 bis A8 weitergeben.

- Die neuen Zahlen sind richtig uebertragen, nachgerechnet bei KOVARIANZ, STRICH, WEYL und XI. Die Negativliste ist
  woertlich eingehalten.
- Falsch sind ein Gegenstand mit Kennzeichen (A1: "Vorzeichen zu 70 %") und die Lesart Schwerkraft, die der eigenen
  Tabelle widerspricht (A2). Zu stark sind drei Saetze: "gibt es nicht" bei Nachweisgrenze (A3, A7) und "Kausalgraphen"
  ohne "Wolframs" (A6).
- Drei Bedingungen frueherer Leser sind beim Kuerzen ohne Vermerk verschwunden (A4, A5, A8). Dazu kommen weitere
  Vorbehalte (B1 bis B4); der Kopf nennt nur eine Umformulierung.
- Der Dimensionsvergleich nach AGENTS.md fehlt (B15).

## A-Befunde (falsch oder zu stark, vor Weitergabe zu berichtigen)

Datei jeweils RUNDE-43/WEICHE-STAND-v6.md; Zeilen nach `cat -n`.

- **A1 XI-KUGEL: "das Vorzeichen ist zu rund 70 % gitterspezifisch ... [G]" (Z. 42).**
  - Quelle induziert-xi-kugel-1/ERGEBNIS.md Z. 32-35: "Lesart [M, ES]: ... Nimmt man g0 als Reglermoment, stammen rund
    70 % des Einstein-Glieds ... aus gitterspezifischen O(h^2 R)-Anteilen (mit dem Moment der konsistenten Masse 87 %)".
  - Falsch ist der Gegenstand: Die 70 % betreffen den Betrag des Glieds, nicht das Vorzeichen. Ein Vorzeichen hat keine
    Prozentanteile. Rechenweg: Eigenzeit-Regler mit demselben Moment beta(0) = -gamma/6 = -2,905/6 = -0,484, Netz
    -1,613; 0,484/1,613 = 0,30, Rest 0,70, und 1,613/0,484 = 3,3 = 6 x 0,555. Der Vergleichswert -0,484 ist selbst
    negativ, hat also ebenfalls Einsteins Vorzeichen.
  - Falsch ist auch das Kennzeichen: Die Quelle hat [M, ES] unter einer Annahme, die Datei [G].
  - Zu eng ist xi*: 0,555 +- 0,018 gilt fuer konzentrierte Masse, mit konsistenter Masse 1,25 +- 0,04 (Z. 36-38).
  - Ersatz: "Aber: Das Vorzeichen kippt erst bei xi* = 0,555 +- 0,018 statt bei 1/6 (konzentrierte Masse; mit
    konsistenter Masse bei 1,25 +- 0,04). Es ist damit eine Eigenschaft von Netz plus Diskretisierung, nicht der
    Mechanismus des Kontinuums (INDUZIERT-XI-KUGEL-1) [E]. Nimmt man das Netzmoment als Reglermoment, stammen rund 70 %
    des Einstein-Glieds (konsistente Masse: 87 %) aus Eigenheiten des Netzes [M, ES]."
- **A2 Lesart Schwerkraft: "Der 4D-Befund der Fassung 5 haelt der Pruefung nicht stand" und "Verformung" ohne
  Geltungsbereich (Z. 57-59; dazu Z. 42).**
  - Die Messung haelt: beta(0) in 160 von 160 Netzen bitgleich mit KUGEL-2; "Das Einstein-Vorzeichen auf dem S^4-Netz
    (KUGEL-1/-2) ist robust gegen ein Kruemmungsglied bis xi = 1/4, aber es ist kein Abbild des Kontinuums"
    (induziert-xi-kugel-1/ERGEBNIS.md Z. 263-264). Gefallen ist die Lesart als Einsteins Schwerkraft, nicht der
    Befund. Die Tabelle Z. 42 fuehrt den Befund weiter als [E, M]; die Lesart widerspricht ihr.
  - Gemessen ist nur konforme Verformung: "Vorab-Einschraenkung: nur konform flache Verformungen", "TT-Sektor
    ungemessen" (kovarianz-kugel-1/ERGEBNIS.md Z. 50, 279). "keine gerechnete Bauweise antwortet auf Verformung wie
    Einstein" laesst ausserdem "4D" weg.
  - Ersatz Z. 57-59: "Die 4D-Messung der Fassung 5 bleibt (Einsteins Vorzeichen auf dem Kugelnetz, robust bis
    xi = 1/4). Ihre Lesart als Einsteins Schwerkraft haelt der Pruefung nicht stand: Das Vorzeichen ist eine
    Eigenschaft von Netz plus Diskretisierung, und keine gerechnete 4D-Bauweise antwortet auf eine konforme Verformung
    der Kugel wie Einstein; den Spin-2-Teil haben wir nicht gemessen. In 2D bleibt Polyakovs Antwort."
  - Ersatz Z. 42: "Die Antwort auf konforme Verformung hat zwar Einsteins Vorzeichen, ..." und am Ende "Damit gibt
    keine der gerechneten 4D-Bauweisen eine Einstein-Antwort auf konforme Verformung (Spin-2-Teil ungemessen); der
    Strang ist geparkt".
- **A3 WEYL-LINEAR: "Ein lineares Glied gibt es im Mittel nicht" (Z. 41).**
  - Quelle RUNDE-42.md Z. 831: "In keinem Ast ist ein lineares Glied nachweisbar"; Z. 839-840: Gleichteil
    +0,0010 +- 0,0006 (1,7 sigma) offen; nur 4 Netze bei N = 32 000. Der eigene Nachsatz der Zelle ("Gleichteil ...
    wird nachgeprueft") ist genau die Frage, ob es im Mittel ein lineares Glied gibt.
  - Ersatz: "Ein lineares Glied ist im Mittel nicht nachweisbar: lambda1 = +0,0010 +- 0,0007 (E > 0) bzw.
    +0,0010 +- 0,0009 (E < 0) bei N = 32 000 auf 4 Netzen; ..."
- **A4 Tempo: Rueckfall von WEICHE-V4 B4 und Spaltenmischung (Z. 45, Z. 63-64).**
  - Fassung 5 hatte nach WEICHE-V4 B4: "offen bleibt, ob bei einem zusammengesetzten Photon (Finns Fall)
    Quantenkorrekturen die Tempi von selbst schnell genug angleichen (seit 2013 offen)" und "Fuer ein gemeinsames Tempo
    braucht es nach heutigem Stand Abstimmung; offen ist nur der Weg ueber Quantenkorrekturen". Fassung 6 streicht beides
    ohne Vermerk; "Pfeil-Eis braucht weiter Abstimmung" ist damit zu stark.
  - "Auf Zufallsnetzen" verallgemeinert STRICH-NETZ-1 (3D-Poisson-Netz mit aeusserer Uhr, Spalte A) auf alle
    Zufallsnetze; fuer (B-eukl.) steht in der Tabelle "nicht gerechnet", fuer (B) "offen". Das ist die Fehlerart von
    WEICHE-V3 A4. "nicht der Punktlage" ist nur ueber Saaten und Punktzahl eines Poisson-Netzes geprueft
    (RUNDE-42.md Z. 188-190).
  - Ersatz Z. 45 (nach "(LICHT-GLEICH-L) [S]"): "; offen bleibt, ob bei einem zusammengesetzten Photon (Finns Fall)
    Quantenkorrekturen die Tempi von selbst schnell genug angleichen (seit 2013 offen)".
  - Ersatz Z. 63-64: "Auf raeumlichen Zufallsnetzen mit aeusserer Uhr (3D, Spalte A) ist es bei langen Wellen eine
    Frage der Kopplungsregel (Patch-Test); Saat und Punktzahl aendern daran nichts. Fuer die (B)-Seiten ist das nicht
    gerechnet. Fuer Pfeil-Eis braucht es nach heutigem Stand Abstimmung; offen ist nur der Weg ueber Quantenkorrekturen."
- **A5 Lesart Haendigkeit: Geltungsbereich gekuerzt (Z. 60-61).**
  - Die Tabelle Z. 44 hat den Wortlaut von WINDUNG-LESER ("unitaerer, streng lokaler, translationsinvarianter Takt
    freier Teilchen"). Die Lesart sagt nur "lokal, verlustfrei" und laesst "translationsinvariant" und "freie Teilchen"
    weg. Das ist WINDUNG-LESER B2 (windung-leser/GEGENLESEN.md Z. 354-358: "Raender und Wechselwirkung deckt der Satz
    nicht ab"). Als "keine"-Aussage ist der Satz so zu breit.
  - "gilt auch fuer Finns Dreiecks-Takt" laesst die Dimension weg: In 2D gibt derselbe Takt eine einseitige Randwelle
    (RUNDE-42.md Z. 234-236), der Satz betrifft das 3D-Volumen.
  - Naeherer Rueckfall: Direkt danach nennt die Lesart als einzigen Weg "Eine vierte Richtung mit Rand traegt sie".
    Zusammen gelesen ist das die gestrichene Aussage "Haendigkeit nur am Rand" (Negativliste Z. 15) in anderer Form;
    die Tabelle nennt drei Auswege, die Lesart einen.
  - Ersatz Z. 60-62 bis "gesetzt vom ganzen Netz.": "Im Volumen eines streng lokalen, verlustfreien,
    translationsinvarianten Takts freier Teilchen gibt es keine Netto-Haendigkeit. Das ist ein bekannter Satz (Read
    2017) und gilt auch fuer Finns Dreiecks-Takt in 3D; in 2D gibt derselbe Takt eine einseitige Randwelle (bekannt,
    Kitagawa u. a. 2010). Bekannte Auswege sind abgetrennte Baender, Verluste oder ein Rand; Wechselwirkung ist nicht
    untersucht. Den Rand bietet zum Beispiel eine vierte Richtung; den Drehsinn setzt dort das ganze Netz."
- **A6 "Kausalgraphen sind mikroskopisch Seite (A) ... [S]" (Z. 48).**
  - Quelle RUNDE-41.md Z. 298-300: "Die Kausalgraphen haben im Kleinen feste, wenige Nachbarn [M, Herleitung des Agenten
    aus Wolframs Definition]. Gorard raeumt das ein ... [S]. Mikroskopisch also Seite (A) mit verstecktem Ruhesystem;
    ob sie im Grossen (B)-artig werden, ist offen."
  - Ohne "Wolframs" liest sich der Satz als Aussage ueber Kausalgraphen allgemein, also auch ueber die Kausalmenge in
    Spalte (B). Das Kennzeichen ist [M, Agent] plus [S] fuer Gorard, nicht [S]. Der Vorbehalt "im Grossen offen" fehlt.
  - Ersatz: "Wolframs Kausalgraphen haben im Kleinen feste, wenige Nachbarn, sind mikroskopisch also Seite (A)
    [M, Herleitung des Agenten]; Gorard raeumt das ein und rettet die Lorentz-Invarianz nur durch Vergroeberung [S]. Ob
    sie im Grossen (B)-artig werden, ist offen (WOLFRAM-SCAN-L)."
- **A7 KERNMASSE: "eine Gleichung auf der Kausalmenge dazu gibt es nicht" (Z. 43).**
  - Der Leser schrieb: "Eine Gleichung auf der Kausalmenge, deren Green-Funktion VK ist, ist weder angegeben noch
    untersucht. Mit Diagonalterm gaebe es formal (I + W)^-1; dessen Eigenschaften (Lokalitaet, Stabilitaet) sind offen"
    (kernmasse-leser/GEGENLESEN.md Z. 268-270), im Vorschlag: "eine Bewegungsgleichung auf der Kausalmenge fehlt"
    (Z. 295). "gibt es nicht" behauptet Nichtexistenz. Die Verschaerfung stammt aus RUNDE-42/BERICHTIGUNG-R41-KERNMASSE.md
    (Leitung), nicht vom Leser.
  - Ersatz: "gebaut ist ein vorgegebener Propagator aus der Kontinuumsformel; eine Gleichung auf der Kausalmenge, deren
    Green-Funktion er ist, ist weder angegeben noch untersucht".
- **A8 TWIST-PYRO-1: Bedingung frueherer A-Befunde gestrichen (Z. 44).**
  - Fassung 6: "Pfeil-Eis algebraisch mit Rahmungsregel (TWIST-PYRO-1) [G]". Fassung 5 hatte nach WEICHE-V3 A3 und
    WEICHE-V4 B3: "Nur im Austauschvorzeichen (algebraisch) kann ein Fadenende in beiden Lesarten ein Fermion sein, wenn
    man die Rahmungsregel von Levin/Wen lokal liest ... [G, vorab ableitbar]; nicht gezeigt: Spin 1/2, Licht
    (Coulomb-Phase), Kopplung ans Licht". Die woertliche Lesart der Rahmungsregel scheitert schon auf Levin/Wens
    Wuerfelgitter (WEICHE-V3 A3). "mit Rahmungsregel" ohne "lokal gelesen" ist damit zu stark; die Liste "nicht
    gezeigt" ist ohne Vermerk weg.
  - Ersatz: "Pfeil-Eis: Ein Fadenende kann nur im Austauschvorzeichen (algebraisch) ein Fermion sein, und nur wenn man
    die Rahmungsregel von Levin/Wen lokal liest (TWIST-PYRO-1) [G, vorab ableitbar]; nicht gezeigt: Licht
    (Coulomb-Phase), Kopplung ans Licht."

## B-Befunde

- **B1 Kopf (Z. 6-7, 25-26): Nicht alle Aenderungen sind gekennzeichnet.** Laut Kopf ist neu nur, was [neu in
  Fassung 6] traegt, und umformuliert nur "nur langwellig". `diff` gegen Fassung 5 zeigt mehr:
  - ohne Marke neu: die Lesart-Punkte "Ein Tempo fuer alles" (Z. 63-64) und "Finns Tetraeder-Netz (A)" (Z. 65-69);
  - ohne Vermerk gestrichen, mit Bedingungen, die fruehere Leser verlangt hatten: Tensor-Eis-Positivbefunde und
    Gegenlesestand (V4 B1, C10), QCA-Bedingungen (V3 A2, V4 B2), TWIST-PYRO-Bedingung (A8), Tempo-Vorbehalt (A4),
    CDT-Vorbehalt (B4), Torus-Widerspruch mit 5,7 SE (V3 A1) und INDUZIERT-G-L, "vorab berechnet" bei KAUSAL-SWERVE,
    KAUSAL-4D-SCHICHT-Preis (Rauschen 1,6 bei V-00, l nahe l_P), SPIN-ZUFALLSNETZ-1, LADUNG-MONOPOL-1, DYON-STATISTIK-L,
    FLUSS-1 (klassisches Licht).
  - Vorschlag: eine Zeile "Gegenueber Fassung 5 gekuerzt (Inhalt gilt weiter, siehe Fassung 5): ..." mit dieser Liste;
    A4 und A8 zurueckholen (dort Ersatz), die uebrigen Vorbehalte mindestens als Verweis.
- **B2 Tensor-Eis (Z. 40): Rueckfall von WEICHE-V4 B1.** Ohne "je Welt zwei Helizitaet-2-Moden ... und Newtons 1/r
  innerhalb einer Welt" stehen wieder nur die Nachteile da. Vorschlag: nach "(zwei getrennte Welten)" einfuegen "; je
  Welt zwei Helizitaet-2-Moden und Newtons 1/r" und das Kennzeichen "[G; gegengelesen nur vom eigenen Leser des Agenten]"
  zurueck.
- **B3 QCA (Z. 44): Bedingungen von WEICHE-V3 A2 / V4 B2 fehlen.** In der Zeile "halber Spin" fehlt "dass sich die
  Zustaende wie Spin 1/2 drehen, ist eingegeben" und "ohne Inversion ist Masse nicht verboten". Vorschlag: "QCA auf BCC
  mit Tetraeder-Symmetrie (QCA-BCC-RUECK-1; Spin-1/2-Drehverhalten eingegeben), Masse mit Inversion gefunden, ohne
  Inversion nicht verboten (QCA-DIRAC-T-1)".
- **B4 CDT (Z. 46): Vorbehalt von WEICHE-V4 B6 fehlt.** Vorschlag: "(CDT-HORAVA-L) [S; Tagungsarbeit mit zwei uneinigen
  Methoden]".
- **B5 KOVARIANZ-KUGEL-1 (Z. 42):** KV0 (Moebius-Nullprobe) nicht eingetroffen, b_M = -0,0017 +- 0,0002 (-8,9 SE,
  3 % des Signals; RUNDE-41.md Z. 600-601); fehlt. Quelle [E], Datei [G] (ebenso KOVARIANZ-EPS-1, STRICH-NETZ-1,
  WEYL-LINEAR-1).
- **B6 EINE-WELT-LOCH-1 (Z. 40):** Stabilitaet braucht ausser skalaren Regeln auch eine passende Paarung (3 von 6
  wachsen, RUNDE-42.md Z. 153); das Tempo ist auch modellabhaengig (> 30-fach, Z. 156). Vorschlag: "die Stabilitaet
  braucht skalare Regeln und eine passende Paarung, und das Tempo ist richtungs- und modellabhaengig".
- **B7 PACHNER-TAKT-1 (Z. 40, 46):** Es fehlen "nach drei Takten faellt der Rang unter die Schwelle (Daempfung [H])" und
  "gegenueber dem Zeltstangen-Takt nichts Neues" (RUNDE-42.md Z. 558, 569). Vorschlag Z. 40 nach "koppeln nicht": "; nach
  drei Takten faellt der Rang (Daempfung [H]); gegenueber dem Zeltstangen-Takt nichts Neues". Z. 46: "waechst linear mit
  der Kruemmungsamplitude und faellt wie (a/L)^2,25" statt "von der Groessenordnung der Kruemmung".
- **B8 STRICH-NETZ-1 (Z. 41, 45):** "vorab ableitbar" fuer den Grenzwert 1 fehlt (Z. 185); "0,937 bis 0,972" gilt nur
  fuer Delaunay, auf Gabriel 0,887 bis 0,952 (Z. 188-189); Dimension 3D nicht genannt. Vorschlag Z. 45: "Auf raeumlichen
  3D-Zufallsnetzen ... genau 1 (vorab ableitbar) nur mit patch-test-konsistenten Kopplungen ...; naive Regeln sind
  langsamer, 0,937 bis 0,972 auf Delaunay, 0,887 bis 0,952 auf Gabriel".
- **B9 TWIST-SPIN-1 (Z. 44):** "sind spinlos" ohne Bereich. Quelle: bei fester Teilchenzahl, ein Zustand je Knoten, am
  Diamant-Knoten vorab ableitbar; halber Spin braeuchte einen zweiten Zustand je Knoten oder eine Bandstruktur
  (RUNDE-41.md Z. 144-151). Vorschlag: "Im gerechneten Modell (ein Zustand je Knoten) ist das Fadenende ein spinloses
  Fermion (T statt 2T; vorab ableitbar; TWIST-SPIN-1) [G]".
- **B10 TAKT-RAND-4D-1 (Z. 44, 61):** "rund nur als Dreiergruppe" -> "rund bisher nur als Dreiergruppe" (Quelle: "bisher";
  ein einzelner runder Kegel mit anderem Plan ist offen). Es fehlt "vorab ableitbar (Qi/Hughes/Zhang 2008); neu ist nur
  die streng lokale Ausfuehrung" und "der Gegenrand traegt die umgekehrte Haendigkeit" (RUNDE-42.md Z. 586-600, 612).
- **B11 Auswege der Haendigkeit (Z. 44):** "Auswege sind abgetrennte Baender, Verluste oder ein Rand" liest sich als
  vollstaendige Liste. WINDUNG-LESER nennt dazu quasilokale Nicht-Hamilton-Schritte und "Wechselwirkung ist nicht
  untersucht" (windung-leser/GEGENLESEN.md Z. 305-309). Vorschlag: "Bekannte Auswege sind ...; Wechselwirkung ist nicht
  untersucht."
- **B12 BLACKMON (Z. 45):** [S] gilt nur fuer Vortragsseite und Abstracts; der Aufsatz war nicht lesbar, "Ob der
  Haupttext doch einen Grund nennt, ist ungeprueft" (RUNDE-41.md Z. 573). Vorschlag: "[S, nur Abstract und
  Vortragsseite]"; "dort" durch "bei Blackmon" ersetzen.
- **B13 Lesart "Finns Tetraeder-Netz (A)" (Z. 66, 69):** GLUONEN-L steht in keiner Tabellenzeile; "kein Kleber" stuetzt
  auch KOPPLUNG-TETRA-1. GEMEINSAMES-NETZ-v1.md ist ein nicht gegengelesener Entwurf der Leitung (RUNDE-42.md Z. 926-930);
  so kennzeichnen.
- **B14 KAUSAL-SWERVE (Z. 47):** "vorab berechnet" ist gestrichen; die Varianz 1/4 ist damit als Befund lesbar.
  Vorschlag: "Varianz 1/4 je Schritt (vorab berechnet)".
- **B15 Dimensionsvergleich (AGENTS.md Z. 127-138):** Die Datei weist nicht aus, was allgemein gilt und was sich mit der
  Dimension aendert. Unbeschriftet: STRICH-NETZ-1 (3D; der 2D-Wert waere ein anderer, SN7), Wolframs R2 (2D-Regel,
  1+1), Dreiecks-Takt (2D Randwelle, 3D W3 = 0), GUERTEL (Ebene ~ k^2, Raum springt). Vorschlag: je Zelle die Dimension
  nennen und unter der Legende eine Zeile "Dimension: ..." mit den vier Faellen.
- **B16 "genau 1 nur mit patch-test-konsistenten Kopplungen" (Z. 45) [M, Leser, nicht gerechnet]:** Das "nur" gilt bei
  der Normierung der Karte. Skaliert man die Gewichte einer naiven Regel um einen festen Faktor, etwa ungewichtet
  1/0,939^2 = 1/0,882 = 1,13, ist ihr langwelliges Tempo ebenfalls 1; das waere Abstimmung je Feld. Vorschlag: "genau 1
  ohne Abstimmung nur mit patch-test-konsistenten Kopplungen".

## C-Befunde

- **C1 (Z. 41, Spalte B):** "Rauschen statt Vorzugsrichtung [G]" nennt weiter keine Karte (WEICHE-V4 C6); der Vermerk
  "Karte schon in Fassung 1 nicht genannt" ist jetzt auch weg.
- **C2 Legende (Z. 50-53):** "TT-Mode" kommt in der Tabelle nicht mehr vor. Unerklaert sind u. a. FEM, Voronoi,
  Poisson-Delaunay, Patch-Test, W3, E - G, xi*, sigma, Flip-Flop/Zeltstangen, T und 2T, Isotacheia, Horava.
- **C3 WOLFRAM-RUHE-1 (Z. 48):** "vorab ableitbar" gilt fuer die Kette; "nicht kausalinvariant" ist gemessen (5 von 8
  Reihenfolgen, [E]; RUNDE-42.md Z. 416-422). "in der staerksten Form" ist Zusatz der Leitung [ES].
- **C4 1/5 (Z. 46):** TAKT-UMBENENNUNG-L hat die 1/5 nachgerechnet ("arithmetisch richtig", DOSSIER Z. 119). Den
  Wegfall von "nicht gegengelesen" deckt das; die Fundstelle sollte dabeistehen: "[M, Annahmen; nachgerechnet in
  TAKT-UMBENENNUNG-L]".
- **C5 Horava (Z. 46):** Die Quelle sagt "locally the two theories are equivalent" (BPS S. 8, DOSSIER Z. 61-62), der
  A1-Vorschlag "ist in der Literatur das projizierbare Horava-Modell". Vorschlag: "ist lokal gleichwertig zum
  projizierbaren Horava-Modell".
- **C6 "laufen ... durch" (Z. 40)** neben "laeuft" im Sinn von "Rechnung laeuft" (Z. 41, 44): der Doppelsinn aus
  WEICHE-V4 B9. Vorschlag: "dann bleiben fuer zwei Takte genau E - G = 3 Groessen je Zelle erhalten".
- **C7 "Als naechstes" (Z. 72-76):** Alle sechs genannten Karten laufen laut RUNDE-42.md Z. 932-933 schon. Vorschlag:
  "Laufen und werden als naechstes geerntet".
- **C8 XI-KUGEL-Bezug:** Die Quelle liest das Ergebnis ueber INDUZIERT-G-L ("bei freien Feldern setzt der Regler das
  Vorzeichen"); Fassung 6 strich diesen Literaturbezug. Er gehoert in Z. 42 zurueck.

## Frage 1: Neue Aussagen gegen ihre Quellen (vorwaerts und rueckwaerts)

Gelesen: diff Fassung 5 gegen 6; die Ernten aller in Fassung 6 neu genannten Karten in RUNDE-41.md und RUNDE-42.md
(dazu Abschluss R42); BERICHTIGUNG-R41-KERNMASSE.md; kernmasse-leser, windung-leser, schreibtisch-leser (A-Liste),
takt-umbenennung-l/DOSSIER.md (A1), weiche-v3- und weiche-v4-gegenlesen (A, B, C, Negativliste); Ausschnitte aus
induziert-xi-kugel-1/ERGEBNIS.md, kovarianz-kugel-1/ERGEBNIS.md, kovarianz-eps-1/ERGEBNIS.md, pachner-takt-1/ERGEBNIS.md.

**Vorwaerts gedeckt (Zahlen nachgerechnet):**
- KOVARIANZ-KUGEL-1 11,3 und 20,8 -> "11- bis 21-mal"; KOVARIANZ-EPS-1 eps^1,31 und -11,2 +- 0,4 -> "11-mal, falsches
  Vorzeichen"; KOVARIANZ-2D "4D-spezifisch".
- STRICH-NETZ-1 Dispersion: (0,117 - 0,022) x 0,171^2 = 0,095 x 0,0292 = 0,0028 (Quelle 0,26 %) und
  0,095 x 0,341^2 = 0,095 x 0,1163 = 0,011 (Quelle 1,1 %); die Zahlen passen zueinander.
- WEYL-LINEAR-1 Streuung 0,0070 / 0,0023 / 0,0013 bei N = 2000 / 8000 / 32 000: ueber den 16-fachen Bereich Faktor
  0,0070/0,0013 = 5,4, Exponent ln 5,4 / ln 16 = 1,69/2,77 = 0,61; "etwa N^(-1/2)" traegt.
- EINE-WELT-LOCH-1 Kern, PACHNER-TAKT-1 Kern (Zeltstangen, E - G = 3, Welten getrennt, globaler Takt), SPIEGEL-HAELFTE-1
  (44 %; Saaten 0,444 bis 0,450), Foster/Jacobson [S], GUERTEL-1/-2 "nicht gezeigt", TAKT-UMBENENNUNG-L (A1 sinngemaess),
  WOLFRAM-RUHE-1, Windungs-Satz in der Tabelle (Wortlaut WINDUNG-LESER), KERNMASSE (Wortlaut der Berichtigung).
- Journal-IDs im Kopf: alle drei stehen in research-journal/INDEX.jsonl.

**Nicht gedeckt oder zu eng (Einstufung oben):** A1, A2, A3, A6, A7; B5 bis B12.

**Rueckwaerts (wichtige Quellsaetze, die fehlen):** XI "robust bis xi = 1/4" und "xi* haengt an der Massendiskretisierung";
KOVARIANZ "TT-Sektor ungemessen", KV0; EINE-WELT "Paarung", "Tempo modellabhaengig"; PACHNER "Rang nach drei Takten",
"nichts Neues"; STRICH "vorab ableitbar", Gabriel-Werte; WEYL "nur 4 Netze"; TWIST-SPIN "ein Zustand je Knoten";
TAKT-RAND "vorab ableitbar (Qi/Hughes/Zhang 2008)", "bisher"; BLACKMON "Haupttext ungeprueft"; WOLFRAM-SCAN "im Grossen
offen"; DREIECK-TAKT 2D-Randwelle.

Arbeitsnotizen 19:16 (Grundlage der Einstufung):

- Z. 42 XI-KUGEL: "das Vorzeichen ist zu rund 70 % gitterspezifisch ... [G]". Quelle induziert-xi-kugel-1/ERGEBNIS.md
  Z. 32-35: "Lesart [M, ES] ... Nimmt man g0 als Reglermoment, stammen rund 70 % des Einstein-Glieds ... aus
  gitterspezifischen O(h^2 R)-Anteilen (mit dem Moment der konsistenten Masse 87 %)". Gegenstand ist der Betrag des
  Glieds, nicht das Vorzeichen; Kennzeichen [M, ES] unter Annahme, nicht [G]. Rechenweg: Eigenzeit-Regler -0,484, Netz
  -1,613; 0,484/1,613 = 0,30, Rest 0,70 (stimmt); -0,484 ist selbst negativ, das Vorzeichen bliebe also auch ohne den
  Netzanteil. Zudem Z. 263: "robust gegen ein Kruemmungsglied bis xi = 1/4". xi* = 0,555 gilt nur fuer konzentrierte
  Masse (konsistent 1,25 +- 0,04; Z. 36-38).
- Z. 42 KOVARIANZ-KUGEL-1: 11,3 und 20,8 -> "11- bis 21-mal" stimmt. Geltungsbereich fehlt: nur konform flache
  Verformung, "TT-Sektor ungemessen" (kovarianz-kugel-1/ERGEBNIS.md Z. 50, 70, 279). KV0 (Moebius-Nullprobe) nicht
  eingetroffen, fehlt.
- Z. 42 KOVARIANZ-2D-GEGENPROBE: "4D-spezifisch" gedeckt (RUNDE-42 Z. 110-112); Volumenzuordnung prueft der 2D-Test nicht.
- Z. 42 KOVARIANZ-EPS-1: Zahlen stimmen (eps^1,31; -11,2 +- 0,4 mal Einstein); Quelle [E], Datei [G].
- Z. 40 EINE-WELT-LOCH-1: Stabilitaet haengt auch an der Paarung (3 von 6 wachsen), Tempo modellabhaengig (> 30-fach);
  beides fehlt.
- Z. 40 PACHNER-TAKT-1: Rangabfall nach drei Takten (PT1 nicht eingetroffen) und "nichts Neues gegenueber dem
  Zeltstangen-Takt" fehlen.
- Z. 41 WEYL-LINEAR-1: "Ein lineares Glied gibt es im Mittel nicht" gegen Quelle "In keinem Ast ist ein lineares Glied
  nachweisbar" (RUNDE-42 Z. 831); widerspricht dem eigenen Nachsatz (Gleichteil 1,7 sigma offen). Nur 4 Netze bei N = 32 000.
- Z. 45 STRICH-NETZ-1: Grenzwert 1 war vorab ableitbar (RUNDE-42 Z. 185), fehlt. "0,937 bis 0,972" ist nur Delaunay;
  Gabriel 0,887 bis 0,952 (Z. 188).
- Lesart Z. 57: "Der 4D-Befund der Fassung 5 haelt der Pruefung nicht stand" gegen XI-KUGEL Z. 263 (Vorzeichen robust,
  bitgleich reproduziert); gefallen ist die Einstein-Lesart, nicht die Messung.
- Lesart Z. 63: "Auf Zufallsnetzen" mischt Spalten (STRICH-NETZ-1 ist Spalte A, 3D mit aeusserer Uhr); "nicht der
  Punktlage" nur ueber Saaten eines Poisson-Netzes geprueft.

## Frage 2: Negativliste und A-Befunde frueherer Leser

- **Negativliste (Z. 9-20), grep im ganzen Text:** Keiner der Saetze steht woertlich im Rumpf; Treffer nur im Kopf
  (Wurzel, nur langwellig, traegt massive, ab 8, nur mit Inversion, Gegenteil, String-Netz, nur am Rand, DT3, 104,
  gerade J, Raute, Faltwinkel, Sicht, Phase, Cristobalit). Die A-Punkte von SCHREIBTISCH-LESER (Raute, Sichtlaenge,
  Umlauf mit Kantenwert, ATEM-NETZ-1) kommen im Rumpf nicht vor.
- **In anderer Form zurueck:** "Haendigkeit nur am Rand" in der Lesart Z. 60-62 (einziger genannter Weg; A5).
- **Fruehere Befunde:**

| Befund | Stand in Fassung 6 |
|---|---|
| V3 A1 Torus "Gegenteil" | nicht zurueck; der Torus-Widerspruch (5,7 SE) ist ganz gestrichen (B1) |
| V3 A2 "ab 8", "nur mit Inversion" | nicht woertlich zurueck; Gegenstuecke "eingegeben", "ohne Inversion nicht verboten" fehlen (B3) |
| V3 A3 TWIST-PYRO-1 Bedingung | **zurueck**: "mit Rahmungsregel" ohne "lokal gelesen", Liste "nicht gezeigt" weg (A8) |
| V3 A4 Spalten gemischt | **zurueck** in der Lesart Tempo, "Auf Zufallsnetzen" (A4) |
| V3 A5 TENSOR-EIS-Stand | erledigt |
| V4 A1 drei Bauweisen | haelt in Z. 40 |
| V4 B1 Tensor-Eis-Positivbefund | **zurueck** (B2) |
| V4 B2 QCA-Bedingung | teilweise ("mit Tetraeder-Symmetrie" steht, Rest fehlt; B3) |
| V4 B3 Fermionen-Bedingung | **zurueck** (A8) |
| V4 B4 Tempo offen ueber Quantenkorrekturen | **zurueck** (A4) |
| V4 B5 "nicht belegt, nicht gibt es nicht" | Satz gestrichen; damit auch der Vorbehalt (A4) |
| V4 B6 CDT-Vorbehalt | **zurueck** (B4) |
| V4 B7 euklidisches Gegenstueck [H] | haelt (Z. 31-33) |
| V4 B9 Doppelsinn "laeuft" | leicht zurueck (C6) |
| V4 C5 1/5-Kennzeichen | durch TAKT-UMBENENNUNG-L gedeckt (C4) |
| V4 C6 Karte fuer "Rauschen" | weiter offen (C1) |
| V4 C10 Gegenlesestand TENSOR-EIS | **zurueck** (B2) |
| WINDUNG-LESER A1, A2, B2, B6 | A1 in anderer Form (A5), A2 haelt, B2 in der Lesart zurueck (A5), B6 nicht umgesetzt |
| KERNMASSE-LESER B1 | umgesetzt, aber "gibt es nicht" staerker als der Leser (A7) |

## Frage 3: Zu starke Saetze und Dimensionsvergleich

- "nur", "kein(e)", "gibt es ... nicht" im Rumpf (grep und Lesen): Z. 40, 41, 42, 43, 44, 45, 58, 60, 66, 68; dazu
  Z. 46 und 48 (Allaussagen ohne diese Woerter). "nie" und "immer" kommen nicht vor.
  - gedeckt: Z. 40 und 68 Flip-Flop "nur ... mitruecken" (feste Ecken scheitern geometrisch, Quelle "nur mit
    Zeltstangen"); Z. 42 "nur Gitterterme", "nur konforme Mode"; Z. 43 "nur mit Feinabstimmung"; Z. 44 "nur im
    Mittel" (SPIEGEL) und "keine Netto-Haendigkeit" mit vollem Geltungsbereich; Z. 46 "hebt ihn nicht auf"; Z. 66 "kein
    Kleber" (GLUONEN-L, KOPPLUNG-TETRA-1 KT3).
  - zu stark: Z. 41 "gibt es im Mittel nicht" (A3); Z. 42 und 58 "keine ... Bauweise" ohne Verformungsart (A2); Z. 43
    "gibt es nicht" (A7); Z. 48 "Kausalgraphen sind" (A6); Z. 60 "keine" ohne vollen Geltungsbereich (A5); Z. 44 "rund nur
    als Dreiergruppe" ohne "bisher" (B10); Z. 45 "genau 1 nur mit" ohne "ohne Abstimmung" (B16); Z. 44 Liste der Auswege
    als vollstaendig gelesen (B11).
- **Dimensionsvergleich:** nicht umgesetzt (B15). Allgemein gilt laut Quellen nur der Windungs-Satz unter seinen
  Voraussetzungen; dimensionsabhaengig sind Haendigkeit (2D Randwelle, 3D W3 = 0, 4D-Rand Weyl), Induzierte Schwerkraft
  (2D Polyakov, 4D Anomalie), STRICH (3D-Werte), Wolfram R2 (1+1), Guertel (Ebene gegen Raum).

## Frage 4: Lesart der Leitung gegen die Tabelle

- Schwerkraft (Z. 57-59): widerspricht Z. 42 (Befund dort weiter [E, M]); "ueberwiegend gitterbedingt" folgt aus der
  falschen 70-%-Lesart (A1, A2).
- Haendigkeit (Z. 60-62): breiter als Z. 44 (A5); Guertel-Satz gedeckt.
- Tempo (Z. 63-64): "Auf Zufallsnetzen" breiter als Z. 45, Spalten B-eukl. und B sind dort nicht gerechnet bzw. offen
  (A4).
- Finns Netz (Z. 65-69): Graviton-Welt und Flip-Flop gedeckt (Z. 40); Gittereichtheorie (GLUONEN-L) und
  GEMEINSAMES-NETZ-v1 stehen in keiner Tabellenzeile (B13).
- (B)-Seite (Z. 70-71): gedeckt.

## Einfach gesagt

Die neue Fassung bringt die Rechnungen der letzten zwei Runden richtig in Zahlen, aber an einigen Stellen klingt sie
sicherer als die Quellen. Ein Beispiel: Dass man eine Abweichung nicht messen konnte, heisst noch nicht, dass es sie
nicht gibt. Beim Kuerzen sind ausserdem Vorbehalte verloren gegangen, die fruehere Pruefer ausdruecklich verlangt
hatten, etwa dass beim Pfeil-Eis der Weg ueber Quanteneffekte noch offen ist. Die Schwerkraft-Messung auf dem Kugelnetz
ist nicht falsch geworden, falsch war nur die Deutung als Einsteins Schwerkraft. Mit acht kleinen Textaenderungen
ist die Datei weitergabefaehig.
