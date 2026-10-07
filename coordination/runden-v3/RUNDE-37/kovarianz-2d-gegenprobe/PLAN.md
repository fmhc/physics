# KOVARIANZ-2D-GEGENPROBE: Plan (Code-Agent, Runde 41)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 16:12:18 CEST (date). Lesen und Schreibtisch bis 16:31,
  VORAB.md Abschnitte 1 bis 3 ab 16:31:53 (vor jeder Rechnung), code/kovarianz2d.py bis etwa 16:31, vorab-Lauf
  14:34:15 UTC, VORAB.md Abschnitt 4 ab 16:34:52, Kontrolle und Rauchlaeufe 14:34:48 bis 14:35:48 UTC, Codeprobe
  14:38 bis 14:39 UTC (.69). Letzte Codeaenderung vor dem Rauchlauf: keine; nach dem Rauchlauf nur Auswertung
  (Abschnitt 11). Plantext ab 16:39:34 CEST.
- **Grundlage:** KARTE.md (KG0 bis KG3, Wahrscheinlichkeiten und Bedeutung unveraendert, Abschnitte 6 und 7);
  kovarianz-kugel-1/ (ERGEBNIS, PLAN, VORAB, code/kovarianz.py, kugel2.py); induziert-dichte-2d/ERGEBNIS.md und
  induziert-dichte-2d-grob/ (KARTE, ERGEBNIS: kappa = 1,075 +- 0,071 bzw. 0,924 +- 0,087); induziert-kugel-1/
  (Kugelnetz, 2D-Laeufe N = 4000, 16 000, 64 000, Saaten 0 bis 79).
- **Code:** code/kovarianz2d.py (neu; Modi vorab, kontrolle, messung, auswertung; n als Parameter). Unveraendert kopiert
  (sha256 gleich KOVARIANZ-KUGEL-1): kugel.py (c2a4d790...), kugel2.py (15dcbd85...), dichte4d.py (2881048e...),
  induziert.py (b3867eac...), zufall2d.py (37a0fe8f...), kovarianz.py (bed2c12a..., nur fuer Kontrolle K4D importiert).
- **Vorab-Datei:** VORAB.md (Schreibtisch S1 bis S7, Kartenpunkte K1 bis K6, exakte Kontinuumswerte).
- Kennzeichen: [M] eigene Mathematik, [ES] eigener Schluss, [F] Festlegung dieses Plans, [K] Kartenpunkt (vor dem
  Rechnen festgehalten), [H] Hypothese, [E] in Kontrolle oder Rauchlauf gerechnet (Rauchlauf blind: keine Gamma-Werte).

## 1. Schreibtisch (Kurzfassung; Einzelheiten VORAB.md)

| Nr | Punkt | Befund |
|---|---|---|
| S1 | Polyakov, Normierung | Delta Gamma_P = -(1/(12 pi)) [1/2 Int abs(grad sigma)^2 dOmega + Int sigma dOmega], Flaeche fest (Vorschrift normiert auf N), Nullmode wie im Kontinuum ohne Beitrag; Normierung gegen P = -1/(24 pi) der Torus-Karten geprueft [M, L] |
| S2 | Vorhersagen | M: 0 exakt. K: -0,000332 / -0,001321 / -0,005239 / -0,02065 / -0,08117 bei eps = -0,025 / -0,05 / -0,1 / -0,2 / -0,4 (mal kappa_GROB = 1,075 +- 0,071); eps = +0,05: -0,001346. N-unabhaengig; exakte Polyakov-Steigung 1,975 bis 1,993 [E-v] |
| S3 | Was 2D prueft | Kotangens-Gewichte haengen nur von Winkeln ab: Gamma(QI) = Gamma(CI) exakt (Kontrolle C5: 0,0 fuer alle Verformungen). Geprueft werden Transport, Huelle, Einbettungssehnen, Neuvernetzung, Paarung und der Code des Verformungszweigs; die Volumenzuordnung nur ueber Gamma_M [M, E] |
| S4 | Derselbe Codepfad | kovarianz2d.py mit n = 4 gibt kovarianz.py bitgleich wieder (Kontrolle K4D, live und gegen dessen Laufdatei, Abweichung 0,0) [E] |
| S5 | Erwartung | Kovariante Konstruktion: E[Delta Gamma] glatt und symmetrisch in eps, also quadratisch; mit N wachsend oder linear in abs(eps) nur bei Nicht-Kovarianz oder Codefehler [M] |
| S6 | Rauschen (Rauchlauf) | Std(Delta Gamma) je Saat etwa 0,3 abs(eps) sqrt(N) fuer kleine eps (eps = -0,1: 0,95 / 0,70 / 2,1 / 2,5 bei N = 1000 / 2000 / 4000 / 8000; 10, 10, 4, 4 Saaten). Polyakov-Signal je Saat 0,005: Betrag (KG3) und Steigung bei sauberer Vorschrift (KG1) nicht entscheidbar; ein 4D-artiger Anteil (Delta Gamma/N ~ -0,014) waere je Saat 15- bis 25-fach ueber dem Rauschen [E, ES] |
| S7 | Grobheit | 2D: h^2 K0 = 8 pi/N <= 0,025; 4D: h^2 R ~ 1 bis 2. Die Gegenprobe trennt Code- und Konstruktionsfehler von 4D-Physik, nicht aber einen reinen Grobgitter-Effekt [K4] |

## 2. Konstruktion (code/kovarianz2d.py) [F]

Schritt fuer Schritt wie kovarianz.py, n = 2 statt 4:
- **Rundes Netz:** k1.kugelnetz(2, N, saat) (Saatschluessel [20261004, 39, 2, N, saat], wie die 2D-Laeufe von
  INDUZIERT-KUGEL-1); Regel Q (Sehnen^2 mal <J>^(2/n), Grundmann-Moeller Grad 5 fuer n = 2) und Regel C (Sehnen).
  Gauss-Bonnet-Pruefung wie kugel.eine_messung.
- **Verformungen** (rotationssymmetrisch um e3, konforme Karte g = e^(2 sigma) g0, Flaeche auf N normiert, sigma als
  kubischer Hermite-Spline auf 8193 Punkten):
  - M: sigma = -ln(cosh t + sinh t cos theta), t = 0,2 (Moebius-Schub, wie 4D).
  - K: sigma = eps (1 - 3 cos^2 theta) + c (zonale l = 2-Funktion von S^2; 4D: 1 - 5 cos^2 theta), eps = -0,025, -0,05,
    -0,1 (Hauptamplitude wie 4D), -0,2, -0,4; dazu eps = +0,05 (Gegenvorzeichen, beschreibend). Alle einbettbar
    (vorab: profil_min >= -2,2e-16).
- **Punkte:** dieselben Zufallspunkte wie das runde Netz; theta' = F_g^-1(F_0(theta)) (F_0 = sin^2(theta/2)), Newton auf
  zellweiser Gauss-Legendre-Quadratur, Rest <= 1e-10 Pflicht; Faserrichtung (Laengengrad) unveraendert. Dichte 1 in g.
- **Netz:** konvexe Huelle der verschobenen Punkte auf der Kugel vom Radius a (konforme Karte), Pruefungen wie
  kugel.kugelnetz (Topologie, Euler 2, Kanten gepaart, leere Kappen, Normalen) und Gauss-Bonnet.
- **Laengen:** Einbettung y = a (s(theta') w, z(theta')), s = e^sigma sin theta, z' = -sqrt(e^(2 sigma) - s'^2); QI:
  Sehnen^2 mal (V_g/V_Sehnen)^(2/n) je Simplex, V_g = flaches Koordinatendreieck mal Grundmann-Moeller-Mittel (Grad 5)
  von J e^(2 sigma). CI: Sehnen^2 unveraendert (Diagnose ohne Volumenzuordnung je Simplex).
- **Gamma:** k1.auswerten (duenne LU wie KUGEL-1/-2 und KOVARIANZ-KUGEL-1), Gamma roh (in 2D korr = 0), dazu Gamma_M.

## 3. Messgroesse und Schaetzer [F]

- Je Saat j, N und Verformung X: Delta Gamma_j(N) = Gamma_QI(X) - Gamma_Q(rund) (Hauptlesart G_QI). Nebenlesarten
  (beschreibend): G_CI (Gamma_CI - Gamma_C; in 2D gleich G_QI), GM_QI (Gamma_M), GM_CI_korr (Gamma_M mit korr_M, Masse
  ohne Volumenzuordnung je Simplex).
- **d_j = Mittel ueber N = 1000, 2000, 4000; b_X = Mittel der d_j, SE = Std(d_j, ddof 1)/sqrt(M)** (wie 4D, aber ohne
  Division durch sqrt(N), [K5]). Je N: Mittel, SE, Std, Anteil negativ; beschreibend y = Delta Gamma/sqrt(N) und
  Delta Gamma/N zum Vergleich mit 4D.
- Beschreibend (vorab festgelegt): b(N) = beta + alpha N (gewichteter Ausgleich der N-Mittel inklusive N = 8000);
  b(eps) = A1 abs(eps) + A2 eps^2 ueber die fuenf negativen Amplituden (je Saat und je N; Polyakov-Bezug aus denselben
  Ausgleich der exakten Werte); Steigungen paarweise, ueber alle fuenf und ueber die drei kleinsten Amplituden
  (4D-Bereich); Gegenvorzeichen b(+0,05) gegen b(-0,05).

## 4. Saaten, N, Laeufe [F, nach dem Rauchlauf; Zeitregel vorher notiert]

- **Saaten 0 bis 119** (Nummern und Paarung wie KOVARIANZ-KUGEL-1; Schluessel mit n = 2). N = 1000, 2000, 4000
  (Hauptschaetzer) und N = 8000 (beschreibend). Rauchzeit je Saat 0,65 / 1,22 / 2,32 / 4,74 s, zusammen etwa 1070 s.
- .69, /home/fmh/fmhc-physics-remote/runde41-kovarianz-2d/lauf/, nur ueber kleintest.sh, Spuren cpu und cpu4, je Spur eine
  Kette (ein ssh je Spur):
  - cpu: kontrolle (eingefrorener Code); N = 4000 Saaten 0-119; N = 8000 Saaten 0-59.
  - cpu4: N = 1000 Saaten 0-119; N = 2000 Saaten 0-119; N = 8000 Saaten 60-119.
  - Ausgabe lauf/messung-N<N>-s<saat0>.json; jeder Lauf schreibt nach jeder (Saat, N).
- **Abbruch [F]:** letzter Start spaetestens 17:30 CEST. Nicht fertige (Saat, N) fehlen; Saaten ohne alle drei
  Haupt-N zaehlen als unvollstaendig (nicht ausgeschlossen), N = 8000 wird auf den fertigen Saaten beschrieben.
- Danach: kovarianz2d.py auswertung lauf /home/fmh/fmhc-physics-remote/runde39-induziert-kugel/lauf lauf/auswertung.json.

## 5. Tor [F]

- Je (Saat, N): rundes Netz gueltig (kugel_gueltig mit Gauss-Bonnet <= 1e-8, LU fuer Q und C), jede Verformung
  gueltig (Huellenpruefungen, Gauss-Bonnet, LU fuer QI und CI, Transportrest <= 1e-10, Profil einbettbar). Eine Saat
  mit einem Fehler bei irgendeinem Haupt-N wird ausgeschlossen und gezaehlt.
- Tor bestanden, wenn mindestens 20 Saaten gut sind und hoechstens 10 % der vollstaendigen Saaten ausgeschlossen; sonst
  KG0 bis KG3 "nicht auswertbar (Tor)". Kontrollen (Abschnitt 8) muessen ihre Schwellen erfuellen.

## 6. Vorhersagen der Karte (unveraendert) und Urteilsregeln (mechanisch in kovarianz2d.py auswertung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KG0 | Moebius-Nullprobe innerhalb 3 SE um null oder kleiner als 5 % des l = 2-Signals | 70 % |
| KG1 | [H] Konform l = 2: Antwort quadratisch in der Amplitude (Steigung von ln abs(Delta Gamma) gegen ln Amplitude zwischen 1,8 und 2,2) | 55 % |
| KG2 | [H] Konform l = 2: Antwort unabhaengig von N (Aenderung von N = 1000 auf 4000 innerhalb 2 SE bzw. unter 10 %) | 50 % |
| KG3 | [H] Betrag trifft die Polyakov-Vorhersage innerhalb 30 % | 40 % |

Alle Urteile auf der Lesart G_QI; die anderen Lesarten werden beschreibend berichtet.
- **KG0** (M): Plan: eingetroffen, wenn abs(b_M) <= 3 SE_M oder abs(b_M) <= 0,05 abs(pred(K-0.1)) = 0,000282 (das
  vorhergesagte l = 2-Signal der Hauptamplitude). Karte: dieselbe Regel mit dem gemessenen abs(b(K-0.1)) statt der
  Vorhersage. Mitberichtet: GM_QI mit der Planregel (prueft die Volumenzuordnung). Vorab [K2]: fuer Gamma entschieden.
- **KG1** (K): Ausgleichssteigung s von ln abs(b(eps)) gegen ln abs(eps) ueber **eps = -0,1, -0,2, -0,4** (E_FIT), SE
  per Jackknife ueber die Saaten. Auswertbar nur, wenn alle drei b dasselbe Vorzeichen haben und jedes abs(b) >= 3 SE
  ist; sonst Plan und Karte "nicht auswertbar". Plan (Intervallregel): eingetroffen, wenn [s - 2 SE, s + 2 SE] in
  [1,8; 2,2] liegt; nicht eingetroffen, wenn das Intervall [1,8; 2,2] nicht schneidet; sonst "nicht entschieden".
  Karte: eingetroffen, wenn 1,8 <= s <= 2,2 (Punktschaetzer). Polyakov exakt ueber E_FIT: 1,977.
  - E_FIT stand schon vor dem Rauchlauf im Code (Schaetzung VORAB S6); der Rauchlauf hat die Wahl bestaetigt, nur aus
    dem Rauschen: Das Polyakov-Signal/Rauschen ist bei den grossen
    Amplituden am besten (je Saat etwa 0,005 / 0,014 / 0,03 bei -0,1 / -0,2 / -0,4); ein linearer Anteil wie in 4D
    waere dort ebenso sichtbar. Der 4D-Bereich (-0,025 bis -0,1) wird als Steigung "klein3" beschreibend berichtet.
- **KG2** (K, eps = -0,1): Aenderung D = b(N = 4000) - b(N = 1000) (Saatmittel je N), SE_D = Wurzel aus SE_1000^2 +
  SE_4000^2 (unabhaengige Zufallsstroeme je N). Plan = Karte: eingetroffen, wenn abs(D) <= 2 SE_D oder abs(D) <= 0,1
  abs(b(N = 1000)). Mitberichtet (Zusatzzeilen, kein Urteil): alle Amplituden; N = 1000 gegen N = 8000.
  Trennschaerfe aus dem Rauchlauf: SE_D etwa 0,19, also wird ein Wachstum ab etwa 0,4 erkannt; das 4D-Muster je Punkt
  gaebe etwa -32.
- **KG3** (K, **eps = -0,4**): r = b/pred, pred = kappa_GROB Delta Gamma_P = -0,0873; SE_r = Wurzel aus SE_b^2 +
  (b 0,071/1,075)^2, geteilt durch abs(pred). Plan (Intervallregel): eingetroffen, wenn [r - 2 SE_r, r + 2 SE_r] in
  [0,7; 1,3] liegt; nicht eingetroffen, wenn es [0,7; 1,3] nicht schneidet; sonst "nicht entschieden". Karte:
  eingetroffen, wenn abs(r - 1) <= 0,3 (Punktschaetzer). Mitberichtet: alle Amplituden, Verhaeltnis zu kappa = 1.
  - eps = -0,4 stand vor dem Rauchlauf im Code; der Rauchlauf bestaetigt sie nur aus dem Rauschen (bestes
    Polyakov-Signal/Rauschen). Erwartet SE_r etwa 2:
    vorab ist absehbar, dass KG3 nach Plan "nicht entschieden" bleibt [K3].
- Bei nicht bestandenem Tor: alle "nicht auswertbar (Tor)".

## 7. Bedeutung (Karte, unveraendert)

- "KG1 und KG2 treffen ein: Die Vorschrift ist in 2D sauber. Die Anomalie in 4D (Wachstum mit N, lineare Amplitude) ist
  dann 4D- bzw. gitterspezifisch, und KOVARIANZ-KUGEL-1 gilt: auf diesem 4D-Netz nicht Einstein."
- "KG1 oder KG2 verfehlt: Die Vorschrift oder der Code erzeugt die Anomalie auch dort, wo die Physik sie verbietet. Dann
  ist das 4D-Ergebnis nicht als Physik lesbar; der Bau muss vor jeder Deutung berichtigt werden."
- Vorab-Einschraenkung [K3, K4]: Ist KG1 "nicht auswertbar" (Signal unter dem Rauschen), loest formal keiner der beiden
  Saetze aus. Ich berichte dann die Schranken (b je N, A1 je Punkt, Steigung "klein3" falls auswertbar) gegen die
  4D-Groesse und benenne, was daraus folgt, getrennt vom Kartenurteil.

## 8. Kontrollen (Schwellen vor dem Lauf; Rauchwerte .69)

- **C1 (sigma = 0, N = 1000, Saat 991):** 0 neue Dreiecke; Gamma_QI - Gamma_Q und Gamma_CI - Gamma_C <= 1e-8.
  Rauch: 0; 1,1e-13; 0,0. Rundes Netz gueltig, Gauss-Bonnet -2,5e-13 [E].
- **C2 (Moebius):** Transport gegen exakte Moebius-Abbildung <= 1e-10, Netz gleich, Punkte gleich <= 1e-10,
  Gamma_CI - Gamma_C <= 1e-8. Rauch: 1,4e-14; gleich; 2,1e-14; 0,0 (QI ebenfalls 0,0) [E].
- **C3 (LU gegen dicht, N = 400, Saat 990, M, K-0.1, K-0.4, QI):** <= 1e-8. Rauch: <= 4,0e-13 [E].
- **C5 (Skaleninvarianz, N = 1000, Saat 991, alle Verformungen):** Gamma_QI - Gamma_CI <= 1e-9. Rauch: 0,0 fuer alle;
  rund Q - C 0,0 [E].
- **K4D (n = 4, Saat 0, N = 1000, rund Q/C, M und K, QI/CI, Gamma und Gamma_M):** generischer Code gegen kovarianz.py
  live und gegen lauf/messung-N1000-s0.json von KOVARIANZ-KUGEL-1: <= 1e-8. Rauch: bitgleich (0,0) [E].
- **Vorab-Proben:** Polyakov(M) <= 1e-9 (8,9e-16), kleines eps gegen -8/15 <= 1e-3 relativ (1,9e-4), M-Profil <= 1e-9
  (4,6e-15), Flaeche <= 1e-12 (3e-15) [E-v].
- **K0:** Gamma_C rund bitgleich mit INDUZIERT-KUGEL-1 (n = 2, N = 4000, Saaten 0 bis 79).
- **In jedem Netz:** Transportrest <= 1e-10, Huellenpruefungen, Gauss-Bonnet <= 1e-8, LU; M: Netz gleich und Punkte
  gleich (beschreibend je Netz).

## 9. Kartenpunkte (vor dem Rechnen offengelegt; Einzelheiten VORAB.md S7)

- **[K1]** Volumenzuordnung wirkt in 2D nicht auf Gamma; Diagnose-Variante fuer Gamma identisch, nur Gamma_M sieht sie.
- **[K2]** KG0 fuer Gamma vorab entschieden (exakt null); Codekontrolle, kein Test.
- **[K3]** KG3 und (bei sauberer Vorschrift) KG1 voraussichtlich nicht entscheidbar; Regeln "nicht entschieden" bzw.
  "nicht auswertbar" vorab festgelegt. KG2 bei sauberer Vorschrift fast sicher erfuellt, kann aber scheitern.
- **[K4]** 2D-Netz relativ zur Kruemmung viel feiner als das 4D-Netz; ein reiner Grobgitter-Effekt in 4D bleibt offen.
- **[K5]** 2D-Antwort ist Delta Gamma (N-unabhaengige Vorhersage), nicht Delta Gamma/sqrt(N).
- **[K6]** KG3 gegen kappa_GROB Delta Gamma_P; kappa = 1 mitberichtet.
- **[K7]** Seeds wie in der Karte (0 bis 119); mehr Saaten wuerden KG3 nicht entscheidbar machen (dafuer etwa 10^4
  Saaten noetig) und sind fuer die Anomaliefrage nicht noetig.

## 10. Agenten-Vorhersagen (nach Kontrolle und Rauchlauf, vor den Hauptlaeufen; ohne Kenntnis von Messwerten)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Tor besteht ohne Ausschluss | 95 % |
| A2 | K0 bitgleich | 95 % |
| A3 | KG0 (Plan) eingetroffen | 99 % |
| A4 | KG0-Nebenlesart Gamma_M (QI) mit Planregel eingetroffen | 35 % |
| A5 | KG1 "nicht auswertbar" | 80 % |
| A6 | KG2 eingetroffen | 85 % |
| A7 | KG3 nach Plan "nicht entschieden" | 90 % |
| A8 | Kein 4D-artiger Anteil: abs(b(K-0.1)) <= 0,3 und abs(D) <= 0,5 bei eps = -0,1 | 80 % |

## 11. Rauchlaeufe und Kontrolle (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC)

- **vorab** (14:34:15 bis 14:34:31, cpu, rc 0): VORAB.md Abschnitt 4.
- **kontrolle** (14:34:48 bis 14:35:03, cpu, rc 0): C1 bis C5 und K4D wie Abschnitt 8; Anteil neuer Dreiecke bei
  N = 1000: 0,048 / 0,083 / 0,141 / 0,235 / 0,341 (eps = -0,025 bis -0,4), 0,066 (+0,05), M 0.
- **rauch-a** (14:34:50 bis 14:35:12, cpu4, rc 0): N = 1000, 2000, Saaten 900 bis 909, blind; alle Netze gueltig;
  0,65 / 1,22 s je Saat (rund und sieben Verformungen); RSS 95 MB.
- **rauch-b** (14:35:18 bis 14:35:48, cpu, rc 0): N = 4000, 8000, Saaten 900 bis 903, blind; alle gueltig; 2,32 / 4,74 s je
  Saat; RSS 116 MB; neue Dreiecke 0,03 bis 0,32 (wie bei N = 1000).
- **Blinde Streuung** (Std von Delta Gamma ueber die Saaten, keine Mittel; N = 1000 / 2000 / 4000 / 8000):
  - eps = -0,025: 0,27 / 0,24 / 0,51 / 0,56; -0,05: 0,51 / 0,44 / 0,97 / 1,18; -0,1: 0,95 / 0,70 / 2,09 / 2,50;
    -0,2: 1,51 / 1,48 / 3,13 / 4,46; -0,4: 1,68 / 3,19 / 4,10 / 2,04; +0,05: 0,50 / 0,39 / 0,87 / 1,26.
  - M: 2,8e-13 bis 2,4e-12 (Gamma); Gamma_M: 0,015 / 0,016.
- **Blindheit geprueft (jq):** In rauch-a.json und rauch-b.json hat kein Objekt ein Feld gamma oder gamma_M.
- **Codeprobe** (14:38 bis 14:39 UTC, cpu, rc 0): nicht blind auf N = 300, 600, 1200 (Saaten 950 bis 979) und N = 2400
  (Saaten 950 bis 954), dann Auswertung mit Haupt-N 300, 600, 1200; nur Struktur geprueft (jq keys: Tor, K0, Urteile
  KG0 bis KG3 mit allen Feldern, 28 Messgroessen, 28 Steigungen, Zusatz A1/A2, Netze). Werte und Urteile der Probe
  nicht gelesen.
- **Codeaenderungen nach dem Rauchlauf (vor dem Einfrieren, ohne Kenntnis von Messwerten):** nur Auswertung: Zusatz
  A1/A2-Ausgleich, KG2 mit allgemeinen Haupt-N und Zusatzzeile bis N = 8000, optionaler Haupt-N-Parameter fuer die
  Codeprobe. Rauch- und Kontrollwerte stammen aus dem Code vor dieser Aenderung (Messteil unveraendert).
- **Zeitfolge der Festlegungen:** Verformungen, Amplituden, Regel QI/CI, Huelle, Transport, Messgroesse, Tor, die
  Urteilsregeln samt E_FIT und EPS_KG3 standen vor der Kontrolle im Code (16:31 CEST); nach Kontrolle und Rauchlauf
  festgelegt: Saatzahl und Laufaufteilung (aus den Zeiten), Zusatzauswertungen (Abschnitt 3), Agenten-Vorhersagen,
  Text. Der Rauchlauf hat E_FIT und EPS_KG3 nur ueber das Rauschen bestaetigt.
