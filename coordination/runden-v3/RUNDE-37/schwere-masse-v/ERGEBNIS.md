# SCHWERE-MASSE-V: Ergebnis (Rechen-Agent fuer die Leitung claude-primary, Versuch ohne Karte, GR-Pruefliste Nr. 9)

- **Ablauf (Zeiten per date; die .69 schreibt UTC, CEST = UTC + 2):**
  - Start 2026-10-05 16:51:51 CEST. Ohne Karte, Plan-Einfrieren, Vorhersagetabelle und frischen Leser (Finn, 05.10.).
  - Code kopiert 17:03:22 CEST. Text ab 17:20:15 CEST.
  - Rauchlaeufe r1 bis r3: 15:06:26 bis 15:07:05 UTC (cpu2, cpu3, cpu4), alle rc = 0, Werte gelesen.
  - Zwischenfall "Platte voll" 15:07:47 bis 15:07:48 UTC, ohne Folgen fuer Ergebnisse (Abschnitt 8, Punkt 1).
  - Hauptlaeufe 15:08:56 bis 15:18:27 UTC, Zusammenfassung zf.py bis 15:18:34 UTC.
- 35 Hauptlaeufe und 3 Rauchlaeufe ueber kleintest.sh, nur Spuren cpu2, cpu3, cpu4 (Hauptlaeufe 16 / 10 / 9). Alle
  rc = 0, laengster Lauf 3 min 13 s, hoechstens drei zugleich.
- lauf-69/PRUEFSUMMEN.txt ist auf der .69 erzeugt (75 Dateien, 15:19:03 UTC). Lokal bestehen 35 von 35 JSON, 7 von 7
  Rauchdateien und 9 von 9 Code-Dateien. Die npz-Felder (123 MB) liegen nur auf der .69:
  /home/fmh/fmhc-physics-remote/schwere-masse-v/lauf/.
- Alles ist synthetische Gitterrechnung an einem gedachten periodischen Netz (numpy/scipy, 1 Thread). Keine Messdaten.
- **Kennzeichen:** [E] gerechnet, [M] eigene Mathematik (nicht gegengelesen), [P] Projektdatei, [ES] eigener Schluss,
  [H] Hypothese, [F] Festlegung, [L] Literatur aus dem Gedaechtnis, nicht geprueft.
- **Einheiten:** Q-Ball-Einheiten (Feldmasse m = 1). h = Finn-Kante l_P in Q-Ball-Laengen (h = m l_P), Gitterabstand
  a = l_P. R = Halbenergie-Radius des Kontinuums-Balls, a/R = h/R_Q. Bindungsanteil B = (Q - E)/E (positiv = gebunden;
  das (E - mQ)/E der Aufgabe ist -B).

## 1. Ergebnis zuerst

1. **Mit der Kopplung, die das Projekt rechnet, wiegt die Bindungsenergie genau so viel wie jede andere Energie
   [E, vorab M].** Die Kopplung ist: Quelle des Takts = Energie je Ecke (wie MATERIE-NETZ-1).
   - Gerechnet sind 10 stationaere Gitter-Q-Baelle auf V mit B von -1,2 % bis +29,8 %.
   - Fernfit: M_schwer/E = 0,999999 bis 1,000023; Punktquelle 1,000002 bzw. 1,000010.
   - Das folgt schon aus dem Aufbau: Das Fernfeld haengt nur an der Summe der Quelle, und die Summe ist E. Gemessen ist
     nur die Fit-Genauigkeit.
2. **Koppelt der Q-Ball metrisch (seine Sterne aus den Kantenlaengen, V1), kommt die Spannung dazu: M = E + S [M].**
   - S ist das Integral der Spannungsspur T^i_i. M = E + S ist Tolmans Integral (rho + 3p), wie in der ART.
   - Der Faktor vor S ist 2q = gamma: 1 in V1, 0 in V2.
   - Diese Herleitung ist von mir (Abschnitt 3). Die Statik des Projekts enthaelt den Spannungsterm bisher nicht.
   - Der Takt-Fit liest die Summe der Quelle zurueck [E]: fuer Energie und fuer Energie + Spannung auf hoechstens
     2,3e-5, fuer die Spannung allein auf 6e-5 (eine Ausnahme mit 1,2e-3, Abschnitt 4).
3. **Im Kontinuum ist S null, auf dem Gitter nicht [E].**
   - Kontinuum: S/E = -0,9e-8 bis -2,6e-8 (von Laue bzw. Virialsatz, auf Integrationsgenauigkeit).
   - Stationaere Gitter-Baelle, fein (h <= 0,8): S/E = 0,0040 h^2,05 (omega = 0,8, vier h, groesster log-Rest 0,007).
   - Fuer omega = 0,9: S/E = 0,0070 h^1,83 (drei h, log-Rest 0,06).
   - Ueber den Radius: S/E = (0,06 bis 0,15) (a/R)^2 bei h = 0,5. Der groesste Wert gehoert zum duennwandigen,
     staerkst gebundenen Ball.
   - S ist im feinen Bereich immer positiv. Metrisch gekoppelt waere die aktive Masse also etwas groesser als E.
4. **Grob (R bis etwa 5 Gitterabstaende, h >= 1) springt S/E [E].**
   - Werte von -4,4 % bis +3,6 %, mit wechselndem Vorzeichen.
   - S/E haengt dort vom Ort des Balls im Gitter ab: bei h = 1 0,22 % / 0,59 % / 0,68 % (Zentrum P0 / H0 / C1), bei
     h = 2 0,15 % / 0,37 % / 3,1 %. Bei h = 0,64 ist der Ort gleichgueltig (0,159 % bis 0,161 %).
   - Lesart [H]: ein Gitter-Einrasteffekt (wie Peierls-Nabarro), der schneller als jede Potenz verschwindet.
5. **Bindungsanteil [E]:**
   - Bei festem h haengt S/E am Ball, mit Groesse und Wandform; Bindung und Groesse sind in der Q-Ball-Familie nicht
     trennbar.
   - Spanne von M/E zwischen den Baellen bei metrischer Kopplung: h = 2 8 %, h = 1 0,74 %, h = 0,5 0,15 %.
   - Uebertragung [ES, H]: Fuer l < 1,6e-27 m (Pruefliste Nr. 11) und Teilchen von etwa 1e-15 m ist (a/R)^2 < 3e-24,
     also S/E < 1e-24.
   - Das liegt weit unter MICROSCOPE (etwa 1e-15, prueft die passive Masse [L]) und unter den Mondlaser-Grenzen fuer
     die aktive Masse (1e-12 oder besser [L]).
6. **Nebenbefund [E, M nach Sicht]:** Im feinen Bereich gilt S = -2 (E_Gitter - E_Kontinuum) bei festem Q: bei h = 0,5
   fuer alle omega auf 1 bis 4,4 %, fuer omega = 0,8 schon ab h = 0,8 auf 1,2 %. Der Virialrest ist also doppelt der
   Energiefehler des Gitters.

## 2. Was gerechnet ist

- **Netz und Sterne [P, E]:**
  - V aus ew.geometrie('V'), gewichtete Hodge-Sterne an der Kammermitte w_mid = (-23/7, -32/7) (a/8)^2, Marge 12/7.
    Das sind dieselben Sterne wie in LICHT-ABLENKUNG-V (rv.netz_V, rv.topologie, rv.zeilen, rv.lp_symmetrisch,
    rv.sterne, unveraendert importiert).
  - Kontrollen: Summe *0 = Zellvolumen und Summe *1 l^2 t t^T = V I, beides auf 2e-16. Alle *1 > 0 (min 0,0306 a).
  - Tempo des Skalars bei k a = 1e-3: 1 - 1,3e-8 ([100]), 1 + 1,4e-8 ([110]), 1 + 8e-10 ([111]); bei k a = 0,3 0,99960
    bis 0,99968.
  - M(k = 0)^H 1_E = 1,7e-16 (fuer Abschnitt 3).
- **Skalar (Papier I) [P]:** L = Summe *0 |phi'|^2 - Summe *1 |d phi|^2 - Summe *0 U(|phi|^2), U(S) = S - S^2 + S^3/2,
  phi = f e^{i omega t}. Damit K = omega^2 Summe *0 f^2, G = Summe *1 (df)^2, V = Summe *0 U, E = K + G + V,
  Q = 2 omega Summe *0 f^2. Sterne in Q-Ball-Einheiten: *0 h^3, *1 h.
- **Stationaerer Gitter-Q-Ball [E]:**
  - Minimum von E_Q[f] = Q^2/(4 Summe *0 f^2) + G + V bei festem Q = Q_Kontinuum(omega), mit L-BFGS-B in den
    Variablen sqrt(*0 h^3) f.
  - Start: Kontinuumsprofil (Schiessen wie mn.qball) um die Lochmitte C1.
  - Feldgleichungs-Rest <= 9,3e-7 relativ, keine Zeitgrenze erreicht. Torus-Inkreis 20 bis 30 Q-Einheiten, Energie
    ausserhalb 0,85 L <= 4,3e-6.
  - Gitter-omega weicht hoechstens 4,6 % vom Kontinuum ab (h = 2, omega = 0,9), bei h = 0,5 hoechstens 0,4 %.
- **Spannung [M, F]:**
  - S = dL/dln(lambda) bei gleichfoermiger Streckung aller Laengen. Die Sterne skalieren dabei homogen (*0 ~ lambda^3,
    *1 ~ lambda, Hebehoehen ~ lambda^2), also S = 3K - G - 3V.
  - Im Kontinuum ist das Integral (3 omega^2 f^2 - (grad f)^2 - 3U) = Integral T^i_i.
  - Je Ecke: Energie m_v = K_v + V_v + 1/2 Summe der Kanten-G (wie die Takt-gewichtete Energie in
    LICHT-ABLENKUNG-V). Spannung s_v = 3K_v - 3V_v - 1/2 Summe der Kanten-G; diese Verteilung ist [F]. Fuer das
    Fernfeld zaehlt nur die Summe S.
- **Takt [E]:** wie MATERIE-NETZ-1, mu(k) = -P(k)^{-1} q(k) mit P = -W^H B W (ew.ops, mn.W_of, unveraendert).
  - Gitter: L_T = 48, Band [16; 24] l_P (h = 2) bzw. L_T = 56, Band [18; 28] (h = 1); Q-Ball-Quellen aus dem kleineren
    Torus eingebettet.
  - Fit -A/r - (2 pi/(3 V_tor)) A r^2 + C, M_schwer = A/A_1 mit A_1 = 1/(8 sqrt2 pi).
  - P > 0 an allen k (kleinstes Eigenwertverhaeltnis 2,8e-4 bzw. 3,8e-4).

## 3. Herleitung der Spannungskopplung [M, eigene, nicht gegengelesen]

- Statik wie MATERIE-NETZ-1, aber die Materieenergie haengt von den Kanten a = delta l/l ab (metrische Kopplung):
  H = kappa_g/2 a^T B a + H_m(a) + Summe_v mu_v (m_v - kappa' c_v^T a), mit Eichung M^T a = 0.
- Gleichgewicht: kappa_g B a - kappa' c mu + g + M lambda = 0 mit g = dH_m/da bei festen (phi, pi).
  Eckregel: kappa' c^T a = m.
- Mit c = -B W (MATERIE-NETZ-1, K0) folgt mu = -(kappa_g/kappa'^2) P^{-1} (m - q W^T g), q = kappa'/kappa_g; ohne g
  ist das MATERIE-NETZ-1.
- Fernfeld: Die weiche Richtung von P ist gleichfoermig. Die Staerke ist deshalb proportional zu 1^T (m - q W^T g) =
  E - q (W 1)^T g = E - 2q Summe_e g_e = E - 2q dH_m/dln(lambda).
- Weiter gilt -dH_m/dln(lambda) bei festen (phi, pi) = dL_m/dln(lambda) bei festen (phi, phi') = S. Also M = E + 2q S =
  E + gamma S.
- Der Eichanteil von g faellt im Fernfeld heraus, weil (W 1) = 2 1_E und M(0)^H 1_E = 0 (gerechnet 1,7e-16).
- V1 (q = 1/2) gibt M = E + S = Integral (rho + 3p), wie Tolman und die ART im schwachen Feld. V2 gibt M = E.
- Kontinuum: Die Streckung eines stationaeren Felds ist eine Feldvariation, also S = 0 (Virialsatz, von Laue). Auf dem
  Gitter ist die Streckung der Geometrie keine Feldvariation, also S ungleich 0.
- Effektiv [M, vorab fuer die Ordnung; die Gleichung S = -2 Delta E erst nach Sicht]:
  - G_Gitter = G + h^2 Gamma + ...; der Term O(h) ist eine totale Ableitung und faellt weg.
  - Gamma skaliert unter Dehnung wie lambda^-1. Daraus folgt S = -2 h^2 Gamma, und in erster Ordnung bei festem Q
    Delta E = h^2 Gamma.
  - Also S = -2 Delta E. Gamma < 0, denn Differenzen unterschaetzen Ableitungen; damit S > 0 und S ~ h^2.

## 4. Tabelle: Q-Baelle um C1 [E]

M (Energie)/E: Takt-Fit mit Quelle m_v. M (Energie + Spannung)/E: Takt-Fit mit m_v + s_v; bei h = 0,5 nur aus der
Summe (1 + S/E), kein Takt gerechnet, weil die Baelle fuer den Takt-Torus zu gross sind. Spannung brutto = Summe |s_v|/E.
Q je omega fest: 10 524,9 / 1 172,34 / 365,45 / 174,04 / 115,01.

| omega | h | L | R/a | B = (Q-E)/E | E | M (Energie)/E | M (Energie + Spannung)/E | Spannung brutto | Virialrest S/E |
|---|---|---|---|---|---|---|---|---|---|
| 0,75 | 2 | 12 | 4,78 | 0,2983 | 8 106,90 | 1,000023 | 1,028937 | 0,230 | +2,89e-2 |
| 0,80 | 2 | 10 | 2,37 | 0,1818 | 992,03 | 1,000014 | 1,030943 | 0,325 | +3,09e-2 |
| 0,85 | 2 | 10 | 1,72 | 0,1043 | 330,92 | 1,000011 | 1,035847 | 0,363 | +3,58e-2 |
| 0,90 | 2 | 12 | 1,48 | 0,0311 | 168,79 | 1,000011 | 0,955554 | 0,338 | -4,45e-2 |
| 0,95 | 2 | 15 | 1,56 | -0,0113 | 116,33 | 1,000011 | 0,977183 | 0,213 | -2,28e-2 |
| 0,75 | 1 | 24 | 9,55 | 0,2943 | 8 131,46 | 0,999999 | 1,002251 | 0,231 | +2,25e-3 |
| 0,80 | 1 | 20 | 4,74 | 0,1772 | 995,86 | 1,000006 | 1,006784 | 0,347 | +6,78e-3 |
| 0,85 | 1 | 20 | 3,43 | 0,0861 | 336,49 | 1,000006 | 1,007365 | 0,375 | +7,36e-3 |
| 0,90 | 1 | 24 | 2,96 | 0,0211 | 170,44 | 1,000006 | 1,009009 | 0,322 | +9,00e-3 |
| 0,95 | 1 | 30 | 3,11 | -0,0118 | 116,39 | 1,000004 | 1,009668 | 0,252 | +9,66e-3 |
| 0,75 | 0,5 | 48 | 19,1 | 0,2935 | 8 136,90 | - | (1,000412) | 0,234 | +4,12e-4 |
| 0,80 | 0,5 | 40 | 9,49 | 0,1754 | 997,43 | - | (1,000967) | 0,346 | +9,67e-4 |
| 0,85 | 0,5 | 40 | 6,86 | 0,0832 | 337,38 | - | (1,001538) | 0,367 | +1,54e-3 |
| 0,90 | 0,5 | 48 | 5,92 | 0,0182 | 170,92 | - | (1,001919) | 0,322 | +1,92e-3 |
| 0,95 | 0,5 | 52 | 6,22 | -0,0146 | 116,72 | - | (1,001536) | 0,219 | +1,54e-3 |
| Kontinuum | 0 | - | - | 0,2932 / 0,1748 / 0,0824 / 0,0173 / -0,0153 | 8 138,55 / 997,91 / 337,64 / 171,08 / 116,80 | - | - | - | -9e-9 bis -3e-8 |

- **Punktquelle (Kontrolle wie MATERIE-NETZ-1):** M = 1,000010 (L_T = 48) und 1,000002 (L_T = 56) [E].
- **Nur Spannungsquelle s_v:** M/S = 0,99998 bis 1,00006 [E]. Ausnahme omega = 0,75, h = 1: 1,0012, weil S dort klein
  ist und der Ball bis ins Band reicht. Das Zusatzband [14; 28] gibt dort 1,125.
- **Brutto gegen netto:** Im Kern liegt Druck von +10 bis +20 % von E, in der Wand Zug von 10 bis 19 %. Netto
  bleiben im Kontinuum 1e-8, auf dem Gitter 4e-4 (fein) bis 4 % (grob).

## 5. h-Gang: Wie faellt der Rest? [E]

| h | R/a (0,8) | S/E (0,8) | p lokal | -2 Delta E/S | R/a (0,9) | S/E (0,9) | p lokal | -2 Delta E/S |
|---|---|---|---|---|---|---|---|---|
| 2,0 | 2,37 | +3,09e-2 | - | 0,38 | 1,48 | -4,45e-2 | - | -0,61 |
| 1,6 | 2,97 | +5,33e-3 | 7,9 | 2,62 | 1,85 | +2,26e-2 | - | 1,29 |
| 1,25 | 3,80 | +5,23e-3 | 0,1 | 1,04 | 2,37 | +2,53e-2 | -0,5 | 0,59 |
| 1,0 | 4,74 | +6,78e-3 | -1,2 | 0,61 | 2,96 | +9,00e-3 | 4,6 | 0,84 |
| 0,8 | 5,93 | +2,55e-3 | 4,4 | 0,993 | 3,70 | +4,51e-3 | 3,1 | 1,09 |
| 0,64 | 7,41 | +1,59e-3 | 2,10 | 0,991 | 4,63 | +3,29e-3 | 1,42 | 0,958 |
| 0,5 | 9,49 | +9,67e-4 | 2,02 | 0,988 | 5,92 | +1,92e-3 | 2,18 | 0,989 |
| 0,4 | 11,86 | +6,13e-4 | 2,05 | 0,995 | - | - | - | - |

- **Fein:** omega = 0,8: p = 2,05 aus h = 0,4 bis 0,8. In Radien: S/E = 0,087 bis 0,090 (a/R)^2.
- **omega = 0,9:** p = 1,83 aus h = 0,5 bis 0,8; der Wert schwankt noch (1,42 bzw. 2,18). Der Ball ist dort mit
  R/a <= 5,9 kleiner.
- **Familie von h = 1 nach 0,5:** p = 2,45 / 2,81 / 2,26 / 2,23 / 2,65 (omega = 0,75 bis 0,95). Der Wert bei h = 1
  traegt noch Einrastanteile.
- **Grob:** Unterhalb von etwa 5 Gitterabstaenden folgt der Rest keinem Potenzgesetz.
- **S gegen den Startwert:** Der relaxierte Ball hat im feinen Bereich das 2,48- bis 2,67-fache des Virialrests des
  bloss abgetasteten Kontinuumsprofils (h = 0,5, alle omega; Anmerkung: ein Faktor 2 waere nur mit dem glatten Teil zu
  erwarten [M]). Ohne Relaxation gaebe es also nur rund 40 % des Rests.

## 6. Ortsprobe: Ball um P0 (Finn-Ecke), H0 (Sechseckmitte), C1 (Lochmitte), omega = 0,8 [E]

| h | S/E C1 | S/E H0 | S/E P0 | E C1 / H0 / P0 |
|---|---|---|---|---|
| 2,0 | +3,09e-2 | +3,67e-3 | +1,45e-3 | 992,03 / 990,20 / 987,17 |
| 1,25 | +5,23e-3 | +2,96e-3 | +7,79e-3 | 995,20 / 995,09 / 994,40 |
| 1,0 | +6,78e-3 | +5,94e-3 | +2,16e-3 | 995,857 / 995,868 / 995,982 |
| 0,64 | +1,594e-3 | +1,596e-3 | +1,605e-3 | 997,122 / 997,123 / 997,126 |

- Grob haengt der Virialrest bis zum Faktor 21 vom Ort ab, bei h = 0,64 nur noch auf 0,7 %.
- Bei h = 2 liegt der Ball um P0 energetisch 0,5 % tiefer als um C1; der Ball um C1 ist dort also nicht der
  Grundzustand. Bei h = 1 ist C1 am tiefsten (Unterschiede 1,1e-5 und 1,3e-4 relativ).
- Lesart [H]: Grob misst S vor allem, wie der Ball ins Gitter einrastet. Das ist kein Potenzgesetz in a/R.

## 7. Was vorab aus dem Aufbau folgt und was gerechnet ist

- **Vorab ableitbar:**
  - M (Energie) = Summe m = E fuer jeden Ball, also unabhaengig von der Bindung [M]. Grund: Gauss bzw. die
    gleichfoermige weiche Richtung von P (MATERIE-NETZ-1, Abschnitt 6). Die Fits pruefen nur die Numerik.
  - M (Energie + Spannung) = E + S aus demselben Grund [M].
  - S = 0 im Kontinuum (Virialsatz, von Laue [L]).
  - Der Rest auf dem Gitter ist von fuehrender Ordnung h^2 [M].
- **Gerechnet und vorab nicht festgelegt [E]:**
  - die Groesse des Rests (Koeffizienten 0,0016 bis 0,0077 in h^2 bzw. 0,06 bis 0,15 in (a/R)^2)
  - der Exponent 2,05 (omega = 0,8)
  - das Springen und die Ortsabhaengigkeit unterhalb von etwa 5 Gitterabstaenden
  - S = -2 Delta E auf 1 bis 4 % (die Gleichung habe ich erst nach Sicht hergeleitet)
  - der Faktor 2,5 gegen das abgetastete Profil
  - die Takt-Fits auf 2,3e-5

## 8. Grenzen, Regelabweichungen, Selbstanzeigen

1. **Platte der .69 voll (Hinweis der Leitung, Systemjournal):**
   - Um 15:07:47 bis 15:07:48 UTC schlugen meine Uploads code/kette-cpu2.sh, kette-cpu3.sh und kette-cpu4.sh fehl
     ("No space left on device"). Auf der .69 standen danach 557, 595 und 539 Byte Nullbytes.
   - Ich hatte die drei Ketten um 15:07:49 UTC mit nohup gestartet. bash lief ueber die Nullbytes ohne einen Befehl:
     kein kleintest-Aufruf, keine Rechnung, leere Logs.
   - Bemerkt kurz danach (df: 0 frei, od: nur Nullbytes, keine Prozesse). Die drei Dateien und ihre leeren Logs habe ich
     geloescht (eigene Dateien).
   - Die Ketten laufen seitdem lokal als bash mit ssh (code/lokal-kette.sh, lokal-takt.sh, lokal-zentrum.sh). Die Logs
     liegen lokal in lauf-69/, gerechnet wird weiter nur ueber kleintest.sh auf der .69.
   - Pruefung nach der Warnung der Leitung (15:14:28 UTC): alle 8 Code-Dateien auf der .69 haben dieselbe sha256 wie
     lokal; zf.py kam danach dazu (9 von 9).
   - Alle Rauchausgaben sind bis 15:07:05 UTC geschrieben, alle Hauptausgaben ab 15:08:56 UTC. Alle 35 JSON lassen sich
     lesen; die npz-Dateien haben die Takt-Laeufe geladen. Betroffen ist kein Ergebnis.
   - Neue Dateien habe ich nur unter neuen Namen hochgeladen (sm_z.py, zf.py), nie ueber eine laufende Datei.
2. **Spannungskopplung ist meine Herleitung (Abschnitt 3), nicht Projektstand.** Sie wurde nicht gegengelesen.
   MATERIE-NETZ-1 und LICHT-ABLENKUNG-V koppeln nur die Energie. Die Verteilung s_v ist festgelegt [F]; Nahfeld-Aussagen
   zur Spannung gibt die Rechnung deshalb nicht her.
3. **Nur aktive Masse, statisch, linear.** Passive und traege Masse habe ich nicht gerechnet. MICROSCOPE prueft die
   passive Masse; ob sie im Netz an dieselbe Spannung gebunden ist (in der ART ueber Impulserhaltung), ist offen [H].
4. **Bindung und Groesse:** In der Q-Ball-Familie haengen Bindung, Groesse und Wandform aneinander. Was S/E am Ball
   festlegt, trennt die Rechnung nicht.
5. **Takt-Fits nur fuer h = 1 und 2.** Bei h = 0,5 waeren die Baelle fuer einen Takt-Torus bis L_T = 56 zu gross. Dort
   steht M (Energie + Spannung) nur aus der Summe; das ist durch die Fits bei h = 1, 2 gedeckt, aber nicht gerechnet.
6. **Q-Ball um C1:** Bei h = 2 ist das nicht die tiefste Lage (Abschnitt 6). Die Werte bei h >= 1 sind deshalb nur
   Beispiele fuer die Streuung.
7. **Uebertragung auf echte Materie [ES, H]:** Ein Q-Ball ist kein Kern. Die Zahl 1e-24 setzt voraus, dass der Rest
   auch dort wie (a/R)^2 mit einem Koeffizienten der Ordnung 0,1 faellt.
8. **Literatur [L]:** MICROSCOPE (Endergebnis 2022, eta etwa 1e-15) und die Grenzen fuer aktive Masse (Kreuzer 1968,
   etwa 5e-5; Mondlaser, Bartlett und van Buren 1986, etwa 4e-12; eine neuere Mondlaser-Auswertung um 2023 nennt
   nach meiner Erinnerung etwa 4e-14) sind aus dem Gedaechtnis und nicht nachgeschlagen.
9. **Werkzeuge:** jq lokal nur lesend, zur Anzeige. Alle abgeleiteten Zahlen (Exponenten, Verhaeltnisse) rechnete zf.py
   auf der .69. Lokal liefen nur bash, ssh, scp, grep, sed und sha256sum; kein python, awk oder perl.
10. **Kleinigkeiten:**
    - Der Kopfkommentar von sm_z.py ist der von sm.py; die Datei unterscheidet sich nur durch --zentrum und die
      Pruefsummenliste.
    - Der Status von L-BFGS-B ist 7-mal "ABNORMAL" (Liniensuche am Genauigkeitsende), jeweils mit Rest <= 1,3e-7.
11. Journal, Peerbus und Commit uebernimmt die Leitung.

## 9. Einfach gesagt

Wir haben kugelfoermige Feldklumpen (Q-Baelle) mit verschieden starker Bindung auf Finns Netz gesetzt und aus der
Schwerkraft weit draussen abgelesen, wie schwer sie sind. Zaehlt man, wie bisher im Projekt, nur ihre Energie als
Quelle, wiegen sie genau so viel wie ihre Energie, egal wie stark gebunden; das ist so eingebaut. Zaehlt man, wie in
Einsteins Theorie, auch Druck und Zug im Inneren mit, bleibt auf dem Netz ein kleiner Rest, der mit dem Quadrat von
Maschenweite durch Teilchengroesse schrumpft und fuer echte Teilchen viel zu klein zum Messen waere.

## 10. Dateien

- code/: sm.py (sha256 62cefc60...), sm_z.py (112bac30..., Ortsprobe), zf.py (5a4e8539..., Zusammenfassung),
  lokal-kette.sh, lokal-takt.sh, lokal-zentrum.sh (lokale ssh-Ketten). Unveraendert kopiert aus licht-ablenkung-v/code:
  rv.py, ew.py, mn.py, tp.py, danzer_naeherung.py, licht_netz.py (sha256 wie dort).
- lauf-69/: 35 Logs und JSON; zusammenfassung.json und ZF.log (Tabellen, Exponenten, Takt); PRUEFSUMMEN.txt (75
  Dateien, auch npz); pruef-json.txt (Teilliste fuer die lokale Pruefung).
- rauch-69/: Rauchlaeufe r1 bis r3 mit pruef-rauch.txt.
- Auf der .69: /home/fmh/fmhc-physics-remote/schwere-masse-v/ (code/, rauch/, lauf/, dort auch die npz-Felder).

Abschluss des Textes 2026-10-05 17:24:45 CEST (date). Die Zeitbox von 90 min ab 16:51:51 CEST endet um 18:21:51 CEST; sie ist eingehalten. Kein
Lauf ist mehr aktiv (letzter Lauf 15:18:34 UTC). Journal, Peerbus und Commit uebernimmt die Leitung.
