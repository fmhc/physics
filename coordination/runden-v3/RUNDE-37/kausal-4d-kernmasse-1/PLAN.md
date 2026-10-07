# KAUSAL-4D-KERNMASSE-1: Plan (Code-Agent fuer die Leitung, Runde 41, explorativ nach v3)

- Start des Code-Agenten 2026-10-04 14:19:45 CEST (date). Karte ab 14:18:14 CEST (Kartenkopf). Plantext ab 14:50:50 CEST
  (date vor dem Schreiben).
- Vorab-Datei: VORAB.md (Text ab 14:47:26 CEST): Bauweise, Herleitung, erwartetes Mittel, Rauschschaetzung, Bau gegen
  Befund. Dieser Plan verweist darauf und wiederholt nur das Noetige.
- Vorhersagen KM0 bis KM2 und Wahrscheinlichkeiten der Karte unveraendert (Abschnitt 5).
- Kennzeichen wie VORAB.md; dazu [F] Festlegung dieses Plans (von der Karte offengelassen).
- **Code** (code/; sha256 beim Einfrieren in EINGEFROREN-SHA256.txt):
  - kausal4d.py, kontinuum4d.py, schicht2_feld.py, schicht2_kont.py: unveraendert aus KAUSAL-4D-SCHICHT-2 (eingefrorene
    Fassungen, sha256 46311620..., 4462504d..., 99ced10d..., 7b05d976..., wie dort in pruefsummen-einfrieren.txt).
  - kernmasse_feld.py: Teil B. VJ, V0, V00 mit dem Rechenweg von SCHICHT-2, dazu VK (Masse im Kern) aus demselben
    GEMM-Produkt P = C C.
  - kernmasse_kont.py: Teil A. Formelprobe, Pole des Ziels mit Zaehlung, Erwartung von VK durch direkte Faltung.
  - kernmasse_auswertung.py: Urteile nach Abschnitt 5, Bilder, auswertung.json.

## 1. Bauweise (Herleitung VORAB.md Abschnitt 2)

- **VK, Masse im Kern:** phi_K(x) = (1/rho) sum_{y vor x} [a [n = 0] + t(n)] J(y). Ein Schritt, kein Halt.
  - n ist die Zahl der Elemente im offenen Intervall I(y, x); fuer Zuschauerpunkte gilt die Palm-Lesart wie in SCHICHT-2.
  - t(n) = T(sqrt(n/c)), T(sigma) = -a int_0^sigma e^(-c s^2) h_m(sigma - s) ds, h_m(y) = (m/(2 sqrt y)) J1(m sqrt y).
  - Ziel-Mittel: G_K~ = k~(sqrt(Z^2 + m^2)), also Johnstons masseloser Linkkern mit der Masse im Argument (BBL (3.2)).
  - **Begruendung:** VORAB 2. BBL Fussnote 8 fragt nach genau dieser Ortsraumform. Johnstons Form mit b = 0 ist ein
    Ein-Schritt-Kern, und die Bauweise erbt die masselose Stabilitaet von Johnstons Kern. Der BD-Operator mit der Masse im
    Argument erbt dagegen die ASS-Nullstellen.
- **Masse aussen (Kontrolle und Vergleich):** VJ (Johnston), V0 = (2, -2) a, V00 = (3, -7, 4) a, b = -m^2/rho, wie SCHICHT-2.
- Alle vier Varianten laufen je Saat auf derselben Streuung, mit derselben Quelle und denselben Pruefpunkten wie
  SCHICHT-1/-2 (m = 1, sigma_Q = 1, eta = 0 und 0,5, Kappe R_S = 3,5, Gebiet D bis T_TOP = 5).

## 2. Teil A: Mittel per Formel

- **Ziel G_K~ (KM1):** rho = 4, 8, 16; k = 0 und p = sinh 0,5.
  - Regionen wie SCHICHT-2: A (abs(omega) < 10, Im omega > 0,05), S (Re omega in [0,5; 2], Im omega in [0,002; 1]) und
    S0 (Re omega in [0,5; 2], Im omega in [1e-5; 0,002]). "Nahe der Massenschale" heisst S und S0.
  - Windungszahl W von G_K~ auf dem Rand jeder Region, zwei Aufloesungen (schicht2_kont.zaehle); "stabil" wie SCHICHT-2.
  - Lokalisierte Nullstellen von G_K~: Gitter und Newton in A und S (wie schicht2_kont.suche, aber mit newton_kurz:
    hoechstens 30 Schritte, Abbruch bei abs(omega) > 12 oder Im omega < -0,5), Newton ab x + 0,001 i in S0.
  - **Polzahl je Region [F]: N_pol = N_lok - W** (Argumentprinzip: W = Nullstellen - Pole). G_K~ hat keinen Nenner
    wie 1 + m^2 k~; deshalb wird die Polzahl so bestimmt (Ergaenzung zu "Nullstellenzaehlung wie SCHICHT-1/-2").
  - **Residuumprobe [F]:** R(e) = -2 omega_0 i e G_K~(omega_0 + i e) bei e = 1e-3, 1e-4, 1e-5, mit
    omega_0 = sqrt(k^2 + m^2). Vorab erwartet R -> 1 (Pol auf der reellen Achse, Residuum wie im Kontinuum).
  - Beschreibend: Newton auf 1/G_K~ ab omega_0 + 0,001 i; max abs(G_K~) auf abs(omega) = 10 und 20; tau-Quadratur 128
    gegen 256 Knoten an fuenf Stellen; synthetische Windungsprobe.
- **Formelprobe** (Modus kern): Fourier-Bild von g_K bei reellem Z = 0,5 / 1 / 2 / 4 gegen k~(sqrt(Z^2 + m^2)); Schranke
  abs(t(n)) <= m^2/(8 pi) fuer n <= 2e4 und 200 Werte bis 1e7; T-Quadratur 128 gegen 256 Knoten; Splinefehler von g_bar.
- **KM0 Teil A:** schicht2_kont.py (unveraendert) im Modus pole fuer VJ bei rho = 4, 8, 16 erneut rechnen und mit
  SCHICHT-2 lauf-69/kont/pole-VJ.json (sha256 e7e48961...) vergleichen.
- **Erwartung von VK** an den 9 Pruefpunkten und 19 Achsenpunkten je Konfiguration, durch direkte Faltung im Ortsraum
  (VORAB 2; 96 s-Knoten, 2 x 32 tau-Knoten, 64 x 64 Richtungen, gekappte Quelle):
  - Ziel g_K und Realisierung g_bar (g_bar mit kubischem Spline von sum t(n) Pois(n; u) auf 3 801 tau-Knoten).
  - Laeufe a4, a8, a16 (je eine Dichte). Lauf b: rho = 4 noch einmal, dazu das Ziel bei rho = 1e6 gegen kc.faltung (gekapptes
    Kontinuum K, dieselbe Funktion wie SCHICHT-2) und eine feinere Quadratur (144, 2 x 48, 96 x 96) bei rho = 4.
  - Realisierungsfehler: max abs(g_bar - g_K) auf dem tau-Gitter; Fourier-Bild bei reellem Z = 2, 3, 5.
- **Erwartung von VJ, V0, V00:** aus SCHICHT-2 lauf-69/kont/erwartung.npz (sha256 893dabd1...; rho = 4, 8, 16; nicht
  neu gerechnet). K = quad_kappe aus dem ersten Lauf a (kc.faltung, in allen Laeufen gleich gerechnet); die Gleichheit mit
  SCHICHT-2 und zwischen den Laeufen wird
  beschreibend geprueft.

## 3. Teil B: Felder

- **Saaten [F]:** je Dichte die Saaten 1 bis 12, Tag 141, SeedSequence([20261004, 38, 141, 1000 rho, s]).
  - rho = 16: dieselben Streuungen wie SCHICHT-1/-2. VJ, V0, V00 muessen bitgleich mit SCHICHT-2 lauf sein.
  - rho = 8: dieselben wie SCHICHT-1. VJ, V0 muessen bitgleich mit SCHICHT-1 lauf sein (dort Varianten VJ, V0, VM).
  - rho = 4: neue Streuungen.
- **Laeufe:** rho = 16 in vier Laeufen zu je drei Saaten (Zeitgrenze 540 s; Rauch: 146 s je Saat, 1,9 GB). rho = 8 und
  rho = 4 je ein Lauf mit 12 Saaten. Fehlende Saaten folgen in weiteren Laeufen mit denselben Nummern.
- Je Saat werden phi an 2 x 26 Zuschauerpunkten (9 Pruefpunkte, 17 Profilpunkte) und die Normsummen je Zeitscheibe fuer alle
  vier Varianten gespeichert.

## 4. Messgroessen und Statistik

- Saatmittel, sd = sqrt(var Re + var Im) mit ddof = 1, SE = sd/sqrt(n).
- **Relative Einzelnetz-Streuung:** s_v(rho) = geometrisches Mittel von sd/abs(K) ueber die 18 Pruefpunkte (9 je
  Konfiguration). K = gekappte direkte Faltung (wie SCHICHT-1/-2).
- **Steigung [F]:** beta_v = Steigung der Ausgleichsgeraden (kleinste Quadrate) von ln s_v gegen ln rho ueber rho = 4, 8, 16.
  - Beschreibend: Zweipunkt-Steigungen; Bootstrap ueber die Saaten je Dichte (4 000 Ziehungen, feste Saat) mit
    Perzentilen 2,5 / 16 / 50 / 84 / 97,5 und dem Anteil beta <= -0,2.
- **Saatmittel gegen eigenes Mittel:** Abstand in SE je Pruefpunkt; VK gegen g_bar (Realisierung), VJ/V0/V00 gegen die
  SCHICHT-2-Erwartung.
- **Beschreibend:**
  - abs(E)/abs(K) fuer Ziel und Realisierung; Realisierung minus Ziel bezogen auf abs(K); Phase.
  - Zuwachs [abs(E)/abs(K)](t = 3,2)/[...](t = 2,0) an den Lagen A, B, C, aus der Erwartung und aus den Saatmitteln.
  - s je Zeitpunkt t = 2,0 / 2,6 / 3,2; sd/abs(E).
  - Norm je Zeitscheibe R und G (Saatmittel und je Saat), wie SCHICHT-2; Steigungen fuer VJ, V0, V00.

## 5. Vorhersagen (Karte, unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| KM0 | Kontrolle: Mit der Masse ausserhalb (V-J) werden die Pole von SCHICHT-2 bitgleich wiedergefunden | 90 % |
| KM1 | [H] Mittel mit der Masse im Kern: kein Pol mit Im omega > 0 nahe der Massenschale bei rho = 4, 8, 16 (Vorab-Datei sagt, ob das ableitbar ist) | 50 % |
| KM2 | [H] Relative Einzelnetz-Streuung faellt mit der Dichte (Steigung in log rho <= -0,2) | 55 % |

- Je KM zwei Urteile: **nach Plan** (Regeln unten) und **nach Kartenwortlaut**.
- "eingetroffen" heisst: Jeder Teil der Regel gilt. Sonst "nicht eingetroffen", ausser in den genannten Faellen
  "nicht auswertbar".
- Alle Urteile rechnet code/kernmasse_auswertung.py mechanisch.

### 5.1 KM0 [F]

- **(a) Pole:** Fuer alle sechs Faelle (VJ; rho = 4, 8, 16; k = 0, p) ist der Eintrag in "ergebnisse" der neuen
  pole-VJ.json gleich dem in SCHICHT-2 (Python-Gleichheit der JSON-Werte ohne "zeit_s"). Das umfasst Schalennullstelle,
  alte Regel, Blatt II, Zaehlungen und Nullstellenlisten.
- **(b) Felder:** phi_p und Normsummen bitgleich (numpy array_equal):
  - rho = 16, Saaten 1 bis 12: VJ, V0, V00 gegen SCHICHT-2;
  - rho = 8, Saaten 1 bis 12: VJ, V0 gegen SCHICHT-1.
- **Nach Plan eingetroffen**, wenn (a) und (b) gelten. **Nach Kartenwortlaut** ("die Pole ... bitgleich") genuegt (a).
- **nicht auswertbar**, wenn eine Datei fehlt.

### 5.2 KM1 [F]

- **Bedingungen fuer gueltigen Bau** (sonst "nicht auswertbar", Vermerk Baufehler; VORAB 5):
  - Formelprobe: max relative Abweichung <= 1e-6 bei allen drei Dichten.
  - Schranke abs(t) <= m^2/(8 pi) eingehalten.
  - Alle 18 Zaehlungen (3 Dichten x 2 k x 3 Regionen) stabil.
  - Residuumprobe abs(R(1e-5) - 1) <= 1e-3 in allen sechs Faellen.
- **Nach Plan:** **eingetroffen**, wenn die Baubedingungen gelten und N_pol = 0 in allen 18 Zaehlungen.
  - N_pol != 0 widerspricht der Ableitung (VORAB 3) und zaehlt als Baufehler: "nicht auswertbar".
  - "nicht eingetroffen" kann nach Plan nicht vorkommen: KM1 ist ableitbar (Abschnitt 8).
- **Nach Kartenwortlaut:** k = 0, Regionen S und S0, rho = 4, 8, 16 (sechs Zaehlungen).
  - eingetroffen, wenn alle sechs stabil sind und N_pol = 0;
  - nicht eingetroffen, wenn eine stabile Zaehlung N_pol > 0 zeigt;
  - nicht auswertbar bei instabiler Zaehlung oder N_pol < 0 (nicht lokalisierte Nullstelle).
- Fuer die Realisierung g_bar gilt die Aussage nach VORAB 3 durch die Schranke. Sie wird nicht gezaehlt, weil das
  Fourier-Integral von g_bar nahe der reellen Achse nur langsam konvergiert.

### 5.3 KM2 [F]

- **Gueltigkeit:** je Dichte 12 Saaten mit endlichen Werten.
- **Baubedingung:** Das Saatmittel von VK liegt bei jeder Dichte an mindestens 15 von 18 Pruefpunkten innerhalb 3 SE von
  E[g_bar].
- **Nach Plan:**
  - **eingetroffen**, wenn gueltig, Baubedingung erfuellt und beta_VK <= -0,2;
  - **nicht eingetroffen**, wenn gueltig, Baubedingung erfuellt und beta_VK > -0,2 (Befund);
  - **nicht auswertbar**, wenn die Gueltigkeit fehlt oder die Baubedingung verletzt ist (Baufehler).
- **Nach Kartenwortlaut:** beta_VK <= -0,2 (gueltige Saatzahl vorausgesetzt), ohne Baubedingung. Beschreibend: s faellt
  monoton.

## 6. Bau gegen Befund

- Tabelle in VORAB.md Abschnitt 5 (vorab, vor dieser Planfassung).
- Kurz: Ein Fehlschlag von KM0 oder KM1 ist ein Baufehler. Ein Fehlschlag von KM2 bei gueltigem Bau ist ein Befund
  ueber diese Bauweise.

## 7. Kontrollen (ohne Urteilskraft, ausser wo in 5 genannt)

- Codeprobe (rho = 1,2, Bloecke 256): Blockschleife gegen dichte Rechnung; Zuschauer gegen eine Schleife, die die
  Elemente in I(y, Punkt) zaehlt; Schicht-Indizes gleich schicht2_feld.schichten_gemm; dazu schicht2_feld.lauf_probe.
- Repro (Rauch, rho = 16, Saat 91, Tag 141): VJ und V0 gegen SCHICHT-1 rauch/feld/feld-r16-s91.npz.
- Formelprobe, Schranke, Quadraturproben, Splineprobe (Abschnitt 2).
- Erwartung: rho = 1e6-Ziel gegen kc.faltung; feine gegen grobe Quadratur; Lauf b gegen Lauf a bei rho = 4 (gleich).
- Felder: Endlichkeit, max abs(phi); Saatmittel gegen eigene Erwartung fuer alle Varianten.

## 8. Hinweise zur Karte (vor dem Einfrieren)

1. **Kartenfehler: keinen gefunden.** Wahrscheinlichkeiten und Wortlaut bleiben stehen.
2. **KM1 ist nach VORAB 3 ableitbar** (die Karte fragt danach): Fuer das Ziel k~(Z_m) und fuer jede beschraenkte
   Realisierung gibt es keinen Pol mit Im omega > 0. Die Karte nennt 50 %, meine Vorab-Erwartung ist 97 %; der Rest ist
   Baurisiko der Zaehlung. Die Rechnung prueft den Bau, nicht die Kausalmenge.
3. **Ergaenzung, keine Berichtigung:** G_K~ hat keinen Nenner 1 + m^2 k~. Die "Nullstellenzaehlung wie SCHICHT-1/-2"
   wird deshalb als Polzahl N_lok - W gefuehrt. Regionen, Aufloesungen und Stabilitaetsregel bleiben gleich.
4. **Offen gelassen und festgelegt [F]:**
   - Bauweise VK; Saaten und Tag; K als Bezug; Steigung per Ausgleichsgerade ueber drei Dichten
   - Baubedingungen (VORAB 5); Residuumprobe
   - KM0 nach Plan mit Feldern, nach Wortlaut nur Pole
5. **Auftrag der Leitung:** "Kontrolle KM0 (Masse ausserhalb, bitgleich mit SCHICHT-2 auf denselben Saaten)". Das deckt
   5.1 (b) ab; rho = 8 wird zusaetzlich gegen SCHICHT-1 geprueft.

## 9. Rauch (vor dem Einfrieren)

Ordner rauch-69/ (Kopien aus /home/fmh/fmhc-physics-remote/runde41-kausal-kernmasse/rauch/); .69-Zeiten in UTC, alle rc = 0.

- **Codeprobe** (cpu6, 12:43:58 bis 12:45:22 UTC; rho = 1,2, N = 1 511):
  - Schicht-Indizes gleich schicht2_feld: ja, ja, ja. Kausalitaet gleich Koordinaten: ja.
  - VK Block gegen dicht 3,0e-16; Zuschauer gegen Schleife 3,4e-16.
  - schicht2_feld-Probe wie in SCHICHT-2 (<= 4,1e-15).
  - max abs(t) 0,028 bei rho = 1,2.
- **Formelprobe** (cpu6, 12:45:22 bis 12:45:35 UTC; Modus kern, rho = 4, 8, 16):
  - Fourier-Bild von g_K gegen k~(Z_m): <= 1,9e-11 relativ.
  - Schranke eingehalten (0,032 / 0,034 / 0,035 <= 0,0398).
  - T-Quadratur 128 gegen 256 <= 3,9e-16; Splinefehler g_bar <= 2,8e-13.
  - Gesehen habe ich dabei auch die Werte k~(Z_m) und k~(Z) bei reellem Z (VORAB 3, grobe Erwartung).
- **Repro und Zeit** (cpu7, 12:44:00 bis 12:46:27 UTC; rho = 16, Saat 91):
  - N = 20 385, L0 = 2 140 832, L1 = 942 371, L2 = 657 207 wie SCHICHT-2.
  - VJ und V0 bitgleich (phi_p und Normsummen, Abweichung 0,0).
  - 146 s je Saat (Links und VK 130 s), 1,88 GB.
  - Ausgabe ohne VK-Werte.
- **Pfadprobe der ganzen Kette** auf Nicht-Plan-Dichten rho = 1,5, 2, 3 (Saaten 1 bis 3; rauch/pfad/, ab 12:50:20 UTC):
  - Felder (je Saat 0,7 / 1,1 / 2,7 s), VJ-Pole mit schicht2_kont.py (288 s fuer sechs Faelle), VJ-Erwartung mit
    schicht2_kont.py (113 s), VK-Modi kern (7 s) und erwartung a (411 s fuer drei Dichten), erwartung b und die
    Auswertung mit rhos = 1,5,2,3.
  - **VK-Pole, erster Versuch:** 141 s je Fall, weil Newton aus Gitterkandidaten am Rand von A ohne Nullstelle 80 Schritte
    lief. Ich habe die eigene Unit nach zwei Faellen gestoppt (systemctl --user stop, 12:55:25 UTC); sie haette die
    600-s-Grenze gerissen. Danach newton_kurz/suche_kurz (Abschnitt 2) und Zeitmessung je Teil; zweiter Versuch nur bei
    rho = 1,5: 22 bis 24 s je Fall, Kandidaten A 70, S 0, alle Zaehlungen stabil.
  - erwartung b (rho = 1,5 mit Kontrollen): 407 s; feine gegen grobe Quadratur 2,7e-4, Ziel bei rho = 1e6 gegen
    kc.faltung 1,4e-3 (beide unter 1e-2).
  - Auswertung (cpu7, 13:10:39 bis 13:10:49 UTC, rc = 0) mit rhos = 1,5,2,3 und n_soll = 3; KM0-Feldvergleich gegen
    die eigenen Pfadfelder (Selbstvergleich, nur Codepfad).
  - **Gesehen vor dem Einfrieren:** Die Auswertung druckte ihre Urteile fuer die Pfaddaten: KM0 eingetroffen
    (Selbstvergleich), KM1 nicht auswertbar (nur rho = 1,5 gerechnet), **KM2 nicht eingetroffen** fuer rho = 1,5/2/3 mit
    je 3 Saaten. Das ist ohne Urteilskraft (andere Dichten, 3 Saaten). Regeln, Schwellen, Dichten und Saatzahl standen
    vorher fest und bleiben unveraendert; meine Vorab-Wahrscheinlichkeit (VORAB 4) bleibt stehen.
  - Zweck: Laufzeiten und Codepfade vor dem Einfrieren pruefen. Von ihren Werten nehme ich nur Laufzeiten, rc,
    Abbrueche und die Stabilitaetsangabe zur Kenntnis; ihre Urteile zaehlen nicht.
- **Nicht gerechnet vor dem Einfrieren:** Pole, Erwartung oder Felder von VK bei rho = 4, 8, 16.

## 10. Laeufe nach dem Einfrieren

- **cpu7:** feld rho = 16, Saaten 1 bis 3; dann 4 bis 6; dann 7 bis 9; dann rho = 8, Saaten 1 bis 12.
- **cpu6:** kont pole (rho = 4, 8, 16; pole-VK.json), dann schicht2_kont pole VJ (KM0), dann kont erwartung a4, a8, a16,
  dann kont kern (rho = 4, 8, 16; Wiederholung der Formelprobe mit dem eingefrorenen Code), dann kont erwartung b; dann
  feld rho = 16, Saaten 10 bis 12; dann rho = 4, Saaten 1 bis 12.
- Je Spur ein ssh-Aufruf mit einer Folge von Starteraufrufen; hoechstens zwei Laeufe zugleich.
- Danach kernmasse_auswertung.py auf lauf/ (12 Saaten je Dichte; Bezug SCHICHT-2: runde39-kausal-schicht2/lauf und
  lauf/kont/pole-VJ.json, erwartung.npz; SCHICHT-1: runde38-kausal-schicht/lauf).
- Fehlende Saaten (Zeitgrenze) werden mit denselben Nummern nachgerechnet und offengelegt.

## 11. Einfrieren

- Kopien PLAN.md.eingefroren-JJJJMMTT-HHMMSS und VORAB.md.eingefroren-... (Zeit per date), Code-Kopien mit derselben
  Endung, sha256 in EINGEFROREN-SHA256.txt.
- Danach aendern sich Plan, Vorab-Datei, Urteilsregeln und Code nicht mehr.
