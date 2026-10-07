# QBALL-HADRON-1, Teil 1: Was ist logisch? (vor jeder neuen Rechnung)

- Code-Agent mit Literaturteil fuer die Leitung claude-primary. Start 2026-10-05 05:54:51 CEST (date). Abschnitte 1 bis 5
  geschrieben ab 06:08:56 CEST (date), nach den sechs Abrufen und vor jeder Rechnung. Abschnitte 6 und 7 (Rohdatenprobe,
  Entscheidung) folgen nach der Auswertung der Altdaten, ebenfalls vor jeder neuen Rechnung.
- Finn (05.10., vor 05:50:21), woertlich: "Angeregte qballs hadronen probier auch aus aber überleg was logisch ist".
  Zusatz der Leitung 06:02: "Prüfe mal 3d bzw 4d q Balls auch dazu"; Teil 2 laeuft deshalb in jedem Fall.
- Modell (wie RG-1, HAGEDORN, DIM-LEITER): L = |phi_t|^2 - |grad phi|^2 - U(S), S = |phi|^2, U(S) = S - S^2 + S^3/2,
  Masse der freien Quanten 1, Q = 2 omega Int f^2, E = Int [omega^2 f^2 + |grad f|^2 + U]. Ein komplexes Skalarfeld,
  sonst nichts.
- "Stabil" heisst hier wie in DIM-LEITER-QBALL-1: E < Q bzw. VK-stabil (dQ/domega < 0), nicht nichtlinear stabil.
  Ausnahme: Die 2D-Ringaussagen aus HAGEDORN-1/-2 sind lineare Stabilitaet (Eigenwerte) im Modell.
- Kennzeichen: [S] an der Quelle gelesen, [S Abstract] nur Abstract, [P] Projektdatei, [M] eigene Rechnung oder
  Kopfrechnung, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## 1. Was Hadronen verlangen

- Mesonen haben Baryonenzahl B = 0, Baryonen B = 1 und halbzahligen Spin (Nukleon J = 1/2) [L].
- Fuehrende Mesonbahn rho - a2 - rho3 - a4, J = 1, 2, 3, 4. Massen PDG 2024 (mass_width_2024.txt) [S]:
  rho(770)^0 0,77526(23) GeV; a2(1320) 1,3182(6); rho3(1690) 1,6888(21); a4(1970) 1,967(16). Alle vier haben
  neutrale Mitglieder (Ladungszustaende "0" bzw. "0,+" in der Datei) [S].
- M^2 = 0,6010 / 1,7377 / 2,8520 / 3,8691 GeV^2; Schritte 1,137 / 1,114 / 1,017 GeV^2 je Spineinheit, also
  alpha' ~ 0,88 bis 0,98 GeV^-2 [M aus S].
- **Hadron-Pruefzahlen [M aus S]:** R2 = (M_rho3^2 - M_rho^2)/(M_a2^2 - M_rho^2) = 1,980 (+- 0,007);
  R3 = (M_a4^2 - M_rho^2)/(M_a2^2 - M_rho^2) = 2,875 (+- 0,056, fast nur aus dem a4-Fehler). Die echte Bahn ist also
  leicht konkav, R3 liegt 2,2 Standardabweichungen unter 3. (Wird auf der .69 nachgerechnet.)
- Der Spin steigt laengs der Bahn in Schritten von 1 (je Signatur in Schritten von 2).

## 2. Was Q-Baelle mitbringen

- **Ein bosonisches Feld.** Alle Zustaende haben ganzzahligen Spin. Spin 1/2 ist mit der unveraenderten Formel
  unmoeglich: Der Konfigurationsraum ist zusammenziehbar, es gibt kein Finkelstein-Rubinstein-Vorzeichen [P, Gedaechtnis
  "Spin 1/2 nicht moeglich"; M].
- **Drehung bei festem Q ist an die Ladung gekoppelt.** Jede stationaere drehende Loesung hat genau J = m Q
  [S Volkov/Woehnert Gl. (23), (30); S Kleihaus/Kunz/List Gl. (27); P RG-1 Abschn. 1.2]. In hbar-Einheiten ist Q die
  Zahl der Quanten. Der Drehimpuls springt also in Schritten von Q, nicht von 1.
- **Klassisch heisst Q >> 1.** Es gibt eine Mindestladung: 2D Q > 11,70 (Townes-Grenze, nicht angenommen) [P RG-1,
  DIM-LEITER]; 3D Q_min = 111,9, E < Q erst ab Q_s = 141,5; 4D Q_min = 1034, Q_s = 1705 [P DIM-LEITER]. Drehende
  Baelle brauchen mehr: Q_min(n = 1) > Q_min(n = 0) [S KKL, flacher Raum]; 2D Q_min(m) ~ 43,5 m [P RG-1].
- **Der Turm bei festem Q ist endlich.** Gebunden ist ein Ball nur fuer E < m_B Q (hier m_B = 1). Mit wachsendem m
  steigt E_m(Q) gegen Q; in 2D endet der Turm bei m_max ~ Q/43,5 [P RG-1, M]. In KKL (3D, anderes Potential) liegt
  n = 2 bei Q = 410 schon bei 96 % der Schwelle (414,7 gegen sqrt(1,1) * 410 = 430,0) [M aus S].
- **Vier Arten von Anregung** [S VW, S KKL, P HAGEDORN-1, M]:
  - (a) Windung m: J = m Q, Ring bzw. Torus (gerade Paritaet: Energiedichte torusartig; ungerade: Doppeltorus [S KKL]).
  - (b) Radiale Knoten n: J = 0 [S VW].
  - (c) Kleine Schwingungen bzw. Oberflaechenwellen mit Drehimpuls l: J = l (hbar-Einheiten), Energie hbar Omega_l.
    l = 1 ist die Verschiebung (Omega = 0). Die 2D-Scheibe m = 0 hat Omega ~ l^1,53, fast Kapillarwellen
    sqrt(l (l^2 - 1)) [P HAGEDORN-1].
  - (d) Paritaetspartner (gerade/ungerade) bei gleichem m [S VW, KKL].
- **Stabilitaet (2D, linear) [P HAGEDORN-1/-2]:** lange Ringe zerfallen (l = 2, Ellipse); stabil sind nur dicke
  Ringe nahe der Duennwandgrenze, Seitenverhaeltnis A = mittlerer Radius/Dicke <= 1,79 (bei omega^2 <= 0,55); bei
  omega^2 >= 0,70 ist jeder Ring m >= 1 instabil. In 3D/4D ist die Stabilitaet drehender Baelle hier nicht bekannt.

## 3. Die Zuordnungen

### (i) Q = Baryonenzahl
- Ein Baryon waere ein Q-Ball mit Q = 1. Bei Q = 1 gibt es keinen klassischen Ball (Mindestladung 11,7 / 112 / 1034
  in 2D / 3D / 4D); "Q-Ball mit Q = 1" ist ein einzelnes freies Quant.
- Spin 1/2 fehlt (Abschnitt 2).
- Mesonen haetten Q = 0, und bei Q = 0 gibt es keinen Q-Ball (omega = 0 heisst statisch, das verbietet Derrick ab
  D = 2 [M]).
- Variante "grosse Baryonenzahl" (baryonische Q-Baelle der Supersymmetrie [S Titel F2, z. B. Selipsky "Baryon Q balls:
  A new form of matter?"]): Das sind Klumpen mit B >> 1, keine Hadronen; ungerades B mit halbzahligem Spin geht auch dort
  nicht.
- **logisch: nein.**

### (i-M) Mesonen ueberhaupt als Q-Baelle
- rho^0, a2^0, rho3^0, a4^0 haben alle additiven Ladungen null (B, elektrische Ladung, Strangeness, I3) [S PDG
  Ladungszustaende; L Quantenzahlen]. Keine erhaltene U(1)-Ladung kann fuer diese Bahn Q spielen.
- Ausweg Q-Ball plus Anti-Q-Ball (wie q qbar): Ein umlaufendes Paar haette ein kontinuierliches J-Spektrum
  [S VW Fussnote 9: "the spectrum of J would then probably be continuous"]; Q und Anti-Q vernichten sich [L Battye/
  Sutcliffe 2000]; eine fadenartige Bindung, die eine Regge-Gerade braeuchte, hat das Skalarmodell nicht.
- **logisch: nein** (der Paar-Ausweg nur bedingt und ohne Faden).

### (ii) Sack-Lesart (Friedberg/Lee)
- Der Ball ist der Sack, die Quantenzahlen tragen Quarks darin: "color quarks q, scalar gluon sigma, color gauge field
  V_mu, and color Higgs field phi"; statische Hadroneigenschaften auf 10 bis 15 % [S Abstract FL II 1977]. Spin 1/2,
  B und Mesonen kommen von den Fermionen; quasiklassisch gut "when the fermion number N is large" [S Abstract FL I].
- Regge-Geraden kommen dann aus Farbflusslinien in einem langgezogenen, drehenden Sack: "bags made of colored quarks
  and gluons have an asymptotically linear Regge trajectory whose structure is dominated by colored flux lines ...
  alpha' = 0.88 GeV^-2" [S Abstract Johnson/Thorn 1976].
- Ein kugelfoermiger Sack gibt keine Gerade [M]: ein Quark mit hohem l hat Energie x_l/R mit x_l ~ l, dazu
  (4 pi/3) B R^3; Minimum E ~ x^(3/4), also J ~ E^(4/3).
- Uebersicht: Lee/Pang 1992 behandeln nichttopologische Solitonen "in any space-dimension" mit Anwendung auf
  "hadron structures" [S Abstract]. Die Suche F2 (Titel, 22 Treffer) fand Hadronmodelle nur in dieser Sack-Form (Quarks
  an ein Skalarfeld gekoppelt: Celenza/Shakin 1986 "Mesons as nontopological solitons", ohne Confinement; chirales
  Quark-Soliton-Modell) und keine Arbeit, die drehende Q-Baelle selbst als Hadronen auf Regge-Bahnen fuehrt
  [S Titel und Abstracts; Volltext nicht durchsucht].
- **logisch: ja, aber nicht im unveraenderten Modell.** Es braucht Fermionen und ein einschliessendes Eichfeld. Die
  Hadronanregungen sind dann Quark- und Fadenanregungen des Sacks, nicht der m-Turm des Balls.

### (iii) Turm bei festem Q mit J = m Q (Karte)
- Verlangt: Q fest und klassisch (Q >> 1), m = 0, 1, 2, 3, nur stabile Mitglieder.
- Schliesst aus: die Gleichsetzung m = Hadronspin. Der Drehimpuls springt um Q, nicht um 1; eine Bahn J = 1, 2, 3, 4
  braeuchte Q = 1, und dort gibt es keinen Ball. Ebenso ausgeschlossen: Spin 1/2 und jeder Vergleich absoluter
  Steigungen. Vergleichbar sind nur dimensionslose Formzahlen (R2, R3).
- Der Turm ist endlich (E_m < Q); eine schmale Regge-Bahn endet nicht. Echte Hadronbahnen saettigen vielleicht
  [P DOSSIER 6.1 (ii)].
- Literatur: "the energy increases (but not very rapidly) with the angular momentum" [S VW]. Die Zahlen der VW-Tabellen
  sind laut KKL inkonsistent (Faktor 2 am Potential, KKL Fussnoten 18, 19) [S], ich nutze sie nicht. KKL Tabelle III
  (3D, Potential phi^6 - 2 phi^4 + 1,1 phi^2, Q = 410, gerade Paritaet): M = 293,8 / 363,4 / 414,7 fuer n = 0 / 1 / 2
  [S], daraus R2 = 1,873 [M aus S]; R3 gibt es dort nicht.
- **logisch: nur bedingt**, als Formprobe des Modellspektrums ohne Hadronbezug.

### (iv) Schwingungen des Balls mit J = l (zusaetzlich)
- Die einzige Q-Ball-Anregung mit Spinschritt 1 [M]. Energie hbar Omega_l klein gegen E0; Tropfenmoden laufen
  asymptotisch wie l^(3/2), nicht linear [P HAGEDORN-1; M].
- Spin 1/2 fehlt auch hier; der Grundzustand hat J = 0, und J = 1 ist nur die Verschiebung. Eine Zuordnung zur Bahn
  J = 1, 2, 3, 4 passt also nicht einmal in den Etiketten.
- **logisch: nur bedingt** (Kern- bzw. Tropfenbild, nicht Regge).

### (v) Radiale Anregungen (Knoten)
- J = 0, also keine Bahn. Hoechstens Gegenstueck zu Radialanregungen (rho', rho'') [S VW; M].
- **logisch: nur als Tochter- bzw. Radialfolge, nicht fuehrende Bahn.**

### Gegenmodell (nicht gefragt, zur Einordnung)
- Das widerspruchsfreie Soliton-Bild der Baryonen ist topologisch: Skyrmion, B = Windungszahl, Spin 1/2 aus der
  Quantisierung der Drehkoordinaten bei ungeradem N_c [L Skyrme 1961, Witten 1983; S VW zitiert Adkins/Nappi/Witten als
  Ref. 1]. Ein Q-Ball hat keine topologische Ladung.

### 3D und 4D (Zusatz Finn)
- Logisch aendert sich nichts: J = m Q bleibt, der Spin bleibt ganzzahlig. Neu sind nur die Formen (3D: Tori [S KKL];
  4D: zwei Drehebenen).
- **4D: zwei Drehimpulse** J1 = m1 Q, J2 = m2 Q (Drehung in zwei zueinander senkrechten Ebenen). "Regge-artig" heisst
  dann [M]: E^2 haengt nur von J1 + J2 ab, und zwar linear. Grund: Ein offener Faden, der in zwei Ebenen zugleich dreht
  (X = cos(sigma) (a1, a2) e^(i tau), Virasoro kappa^2 = a1^2 + a2^2), hat E^2 = (J1 + J2)/alpha'. Pruefzahl
  K = (E^2(1,1) - E0^2)/(E^2(2,0) - E0^2): Regge 1, kleiner starrer Rotor (E - E0 ~ m1^2 + m2^2) 0,5.

## 4. Logischer Pruefstein

- Karte [M]: R2 = (E(2)^2 - E(0)^2)/(E(1)^2 - E(0)^2) = 2 und R3 = 3 fuer eine Regge-Gerade; kleiner starrer Rotor
  R2 ~ 4. Hadronen: R2 = 1,980, R3 = 2,875 (Abschnitt 1).
- **Erweiterung 1, Q-Unabhaengigkeit [M]:** Ein Regge-Gesetz im Modell verlangt R2 ~ 2 bei jedem Q des stabilen
  Bereichs, nicht bei einem Q. Fuer Q -> unendlich bei festem m sitzt der Wirbel als kleiner Kern in einer grossen
  Scheibe; dann gilt Delta E_m ~ 2 pi m^2 [ln(R/R_kern) + O(1)], also R2 -> 4 (langsam, logarithmisch). Grobe
  Abschaetzung mit duenner Wand (Kern R_h ~ m^2/sigma, sigma = sqrt(2)/4): R2 ~ 4 (L - ln 4)/L mit L = ln(e sigma R);
  R2 = 2 bei R ~ 17, also Q ~ 1200; darunter R2 < 2. Gueltig erst fuer R >> m^2/sigma, also nur Richtung, keine Zahl.
- **Erweiterung 2, Tropfenfalle [M]:** Der Vier-Punkt-Test trennt eine Regge-Gerade nicht von Tropfenmoden.
  2D-Kapillarwellen Omega ~ sqrt(l (l^2 - 1)) geben fuer l = 2, 3, 4 die Verhaeltnisse 2,00 und 3,16; 3D-Rayleigh-Moden
  Omega ~ sqrt(l (l - 1)(l + 2)) geben 1,94 und 3,00 (mit E^2 - E0^2 ~ 2 E0 hbar Omega). Beide wachsen asymptotisch wie
  l^(3/2). R2 = 2 +- 0,2 (QH1) ist deshalb schwacher Beleg, in beide Richtungen.
- **Erweiterung 3, 4D:** K = 1 (Regge) gegen 0,5 (Rotor), dazu R2 entlang (m, 0).
- **Vorab ableitbar [M]:** J = m Q (Identitaet, also kein Turm mit Spinschritt 1); E_m < Q (Turm endlich); R2 -> 4
  fuer Q -> unendlich (2D, Richtung). Offen und nur rechnerisch zu klaeren sind R2 und R3 bei endlichem Q.

## 5. Literatur (6 Abrufe, Kopien in quellen/, Zeiten in quellen/ABRUFE.log)

| Nr | Was | Ergebnis |
|---|---|---|
| L0 | Volkov/Woehnert 2002, hep-th/0205157 (lokale Kopie aus REGGE-HADRON-REF-L, kein eigener Abruf) | J = N Q; "energy increases (but not very rapidly)"; Tabellen laut KKL inkonsistent |
| F1 | INSPIRE: Friedberg/Lee 1977 I und II, Lee/Pang 1992, Johnson/Thorn 1976 | Abstracts gelesen (oben) |
| F2 | INSPIRE-Titelsuche Q-Ball/nichttopologisches Soliton und Regge/Hadron/Meson/Baryon | 22 Treffer; Hadronen nur als Sack mit Quarks; kein Treffer zu Regge-Bahnen drehender Q-Baelle |
| F3 | arXiv-API Kleihaus/Kunz/List (gr-qc/0505143, 0712.3742) | HTTP 429, nichts erhalten (gezaehlt) |
| F4 | PDG mass_width_2024.txt | Massen rho, a2, rho3, a4 (Abschnitt 1) |
| F5 | INSPIRE: Kleihaus/Kunz/List 2005 und 2008 | Abstracts; "Their flat space limits represent spinning Q-balls" |
| F6 | arXiv-PDF gr-qc/0505143 (KKL 2005) | Tabelle III (Q = 410, n = 0 bis 2); Tori; Q_min(n = 1) > Q_min(n = 0); "stable along the lower branch, when ... M < m_B Q" |

- Erwartungen standen vor jedem Abruf in quellen/ABRUFE.log. Getroffen: F1, F2, F4 und F6 (Tori, Q_min-Ordnung).
  Nicht erwartet: die Inkonsistenz der VW-Tabellen (KKL Fn. 18, 19).

## 6. Rohdatenprobe (Altdaten RG-1, nur ausgewertet; geschrieben ab 06:13 CEST, date 06:12:45 davor)

- **Ja, die RG-1-Daten enthalten E(m) bei festem Q** (bahn/bericht.txt, "Rotorprobe": Q = 300 mit m = 0 bis 6,
  Q = 1000 mit m = 0 bis 8). Die Werte sind aber keine Rechnung bei festem Q, sondern Interpolation (ln E gegen ln Q,
  linear) zwischen den Tabellenzeilen (25 Werte omega^2).
- Auswertung auf der .69 (code/rohdaten.py, Spur cpu, 04:12:21 UTC, rc = 0, 0,2 s; lauf-69/rohdaten/), dazu von Hand
  aus dem Bericht nachgerechnet (gleich auf 1e-4). **Das ist Auswertung vorhandener Daten, keine Messung.**
- **QH0 (Datenweg):** Exponent 0,89887 (Q = 300) und 0,92403 (Q = 1000) aus derselben Tabelle, gegen 0,899 / 0,924
  im Bericht. Das ist bei gleicher Tabelle und gleicher Formel zwangslaeufig; der Codeweg folgt in Teil 2.
- **R2, R3 aus den Altdaten haengen an der Interpolation:**

| Q | Interpolation | R2 | R3 | E0 | E1 | E2 | E3 |
|---|---|---|---|---|---|---|---|
| 300 | A wie RG-1 (ln E gegen ln Q linear) | 2,207 | 3,305 | 232,13 | 245,62 | 260,97 | 274,19 |
| 300 | B Hermite in Q, Steigung dE/dQ = omega | 2,218 | 3,320 | 231,45 | 245,10 | 260,77 | 274,17 |
| 300 | C Hermite in ln Q | 2,070 | 3,035 | 229,35 | 245,03 | 260,76 | 274,17 |
| 1000 | A | 2,126 | 2,997 | 744,24 | 764,67 | 787,04 | 803,90 |
| 1000 | B | 2,339 | 3,616 | 741,99 | 759,09 | 781,41 | 802,12 |
| 1000 | C | 2,856 | 5,136 | 736,37 | 749,46 | 773,18 | 801,35 |

- Grund: Bei Q = 1000 liegen m = 0 bis 3 alle zwischen den Zeilen omega^2 = 0,52 und 0,55, und dort springt Q um den
  Faktor 4 bis 6 (m = 1: 370 auf 1798). Die drei Interpolationen trennen sich bei E1 um bis zu 15 Einheiten, bei einer
  Anregung E1 - E0 von etwa 20. Bei Q = 300 ist die Spanne kleiner (R2 2,07 bis 2,22), aber dort liegt m = 0 ebenfalls
  in dieser Luecke. h0005 gibt dieselben Zahlen (die Luecke liegt im omega-Raster, nicht in der Schrittweite).
- **Lage und Stabilitaet (beschreibend, lineare Interpolation in omega^2):**
  - Q = 300: m = 0 / 1 / 2 / 3 bei omega^2 ~ 0,548 / 0,560 / 0,588 / 0,623; Seitenverhaeltnis A = - / 0,92 / 1,70 /
    2,66. Fuer 0,55 < omega^2 < 0,70 gibt es keine HAGEDORN-Rechnung; die A-Regel ist nur fuer omega^2 <= 0,55 belegt.
    Stabilitaet von m = 1 bis 3 bei Q = 300 also unbekannt.
  - Q = 1000: m = 0 bis 3 bei omega^2 ~ 0,531 / 0,537 / 0,545 / 0,549, A = - / 0,74 / 1,24 / 1,93; m = 4 bei 0,560 mit
    A = 2,73. Nach der A-Regel [P HAGEDORN-2, H]: m = 1 und 2 stabil, m = 3 im Zwischenbereich 1,79 bis 1,99, m = 4
    instabil.
- **Ergebnis der Rohdatenprobe:** R2 bei festem Q ist in den Altdaten **nicht beantwortet**. Die Spanne der
  Interpolationen (Q = 1000: R2 2,13 bis 2,86) ist groesser als das Fenster von QH1 (+- 0,2). Die Rotorprobe 0,899 /
  0,924 ist selbst nur so gut wie diese Interpolation.

## 7. Entscheidung fuer Teil 2

- Logisch traegt nur (iii), und nur als Formprobe des Modellspektrums (Abschnitt 3). Diese Probe ist nicht in den
  Altdaten beantwortet (Abschnitt 6). Teil 2 laeuft ausserdem auf Finns Zusatzwunsch (3D, 4D) in jedem Fall.
- Gerechnet wird E(m) direkt bei festem Q, ohne Interpolation ueber grosse Luecken:
  - 2D, Weg A (Karte): RG-1-Code (Kopie), dichte omega^2-Zeilen 0,52 bis 0,60, Hermite mit dE/dQ = omega auf kurzen
    Intervallen.
  - 2D, Weg B (neu, unabhaengig): E bei festem Q als Minimum von E_Q[f] = G[f] + Q^2/(4 N[f]) (omega eliminiert),
    radial. Dazu ein Q-Raster fuer R2(Q) (Pruefstein, Erweiterung 1).
  - 3D: achsensymmetrisch phi = f(rho, z) e^(i(omega t + m theta)), m = 0 bis 3, gleiche Methode auf einem
    (rho, z)-Gitter; Torusform und E < Q je m.
  - 4D: phi = f(rho1, rho2) e^(i(omega t + m1 theta1 + m2 theta2)), (0,0), (1,0), (1,1), (2,0); K wie in Abschnitt 3.
- Vorab festgehalten: Ein Ausgang R2 ~ 2 bei einem Q waere nach Abschnitt 4 kein Regge-Beleg (Tropfenfalle,
  Q-Abhaengigkeit). Gewicht bekaeme erst R2 ~ 2 und R3 ~ 3 ueber das ganze stabile Q-Band.
