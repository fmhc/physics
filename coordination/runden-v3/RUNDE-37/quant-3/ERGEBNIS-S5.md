# QUANT-3, Nachtrag S5: Skala per Gradient Flow (t0, w0, T_c Wurzel(t0)) auf Hyperkubus und Zeltnetz

- Rechen-Agent fuer die Leitung claude-primary, 07.10.2026 14:39 bis 15:25 CEST (date). Synthetisch (SU(2), keine Messdaten, keine Fermionen).
- Vorab-Datei: VORAB-S5.md (Teile 1 bis 6 vor jeder Rechnung; Teil 7 nach den Pilotlaeufen, mit Zeitstempel). Karte unveraendert.
- Code: code/su2flow.py (neu; importiert su2b.py und qu2.py unveraendert), code/flow_bloch.py, code/ana_flow.py, code/zusammen_s5.py, code/es_et_pred.py.
  Rohdaten und Logs: lauf-69-s5/. Pruefsummen: PRUEFSUMMEN-S5.txt.

## Ergebnis zuerst

1. **Der Wilson-Flow ist auf beiden Gittern stabil und liefert ein t0 mit 1 bis 2 % Fehler (S5a).** Hyperkubus 12^4, beta = 2,30, 30 Konfigurationen: t0 = 1,263 +- 0,021 a^2 (1,7 %), Konvention t^2 <E> = 0,3.
   Netz L = 6, Nt = 12, beta = 3,29, 25 Konfigurationen aus zwei Laeufen: t0 = 0,1449 +- 0,0018 a^2 (1,2 %).
2. **T_c Wurzel(t0): Netz 0,2734 +- 0,0017, Hyperkubus 0,2809 +- 0,0024, Abweichung -2,7 +- 1,0 % (S5b, Fenster 15 %).** Das gilt aber nur mit beta_c(Netz) = 3,29 als Annahme; der Wert steigt steil mit beta
   (d ln Wurzel(t0) / d beta = 4,7, das sind 4,7 % je 0,01 in beta), also ist der Befund eine Bedingung an beta_c und kein unabhaengiger Test (Tabelle in Abschnitt 4).
3. **w0 / Wurzel(t0): Netz 1,032 +- 0,004, Hyperkubus 1,034 +- 0,006, Abweichung -0,2 +- 0,7 % (S5c, Fenster 10 %).** Diese Zahl haengt nicht an der Zeitskala kappa (Verhaeltnis zweier Flusszeiten), nur an beta (Tabellen).
4. **Der Fluss mit den Gewichten w_f allein laeuft auf dem Netz nicht in Einheiten a^2.** Er ist zu langsam um den Faktor 1/kappa = 69 (kappa = 0,0145003 = Vc/6, Freifeld-Homogenisierung, isotrop auf 1,6 % in Raum- und Zeitrichtung).
   Die Umrechnung t = kappa t_Lauf steht in allen Netz-Zahlen oben. Ohne sie waere Wurzel(t0) falsch um einen Faktor 8,3. Die DEC-Link-Metrik als Alternative ist nicht verwendbar (26 von 146 Kantenklassen mit h <= 0).
5. **Nur beim Referenzwert c = 0,3 stimmen beide Gitter ueberein.** Bei c = 0,1125 (SU(2)-Wert bei gleichem g^2) ist Wurzel(t0) auf dem Netz 0,123 a, kleiner als die Kanten (0,22 bis 0,52 a), und T_c Wurzel(t0) weicht um 34 %, w0 / Wurzel(t0) um 67 % ab.

## 1. Was gerechnet wurde (Definitionen, wie in VORAB-S5.md)

- Fluss: d V / dt = Z(V) V mit dem Gradienten derselben gewichteten Wilson-Wirkung S = beta Summe_f w_f (1 - p0_f) (Netz: gwp.npz, Hyperkubus: w = 1), Luescher-RK3.
  In Quaternionen Z(l) = -(0, Vektorteil von U_l W_l), W_l der Staple aus su2b.py.
- Schrittweite eps(t) = min(max(0,02, 0,05 t), 0,1), tmax 2,0 (Hyperkubus) bzw. 15 (Netz, Flusszeit des Laufs; 22 fuer beta = 3,34).
- Energiedichte E = (4 / V4) Summe_f w_f (1 - p0_f), Plakette, V4 = L^3 Nt Vc (Vc = 0,25 tau = 0,087002 auf dem Netz). t0: t^2 <E> = c; w0: W(t) = t d(t^2 <E>)/dt = c, c = 0,3 (Hauptwert; SU(2)-Begruendung in VORAB-S5.md Abschnitt 3).
- Zeit: a = kubische Kante der fcc-Zelle; Netz T_c = 1/(4 tau a) = 0,718356/a, Hyperkubus T_c = 0,25/a. Flusszeit in a^2: t = kappa t_Lauf (Netz kappa = 0,0145003, Hyperkubus 1).
- Statistik: heisser Start, 150 Thermalisierungs-Sweeps, danach alle 20 Sweeps eine Konfiguration, die sofort geflowt wird. Jackknife ueber Bloecke (leave-one-out, bei halber Blockzahl nahezu gleiche Fehler, siehe zusammen.txt).
  t0 je Konfiguration: Lag-1-Korrelation klein (-0,33 bis +0,09), keine Autokorrelationszeit gemessen.
- Kontrollen vor den Produktionslaeufen (Piloten): dS/dt = -beta Summe |vec(UW)|^2 auf 3e-4 (endliche Differenz mit eps = 1e-4); Schrittweite eps gegen eps/2: E aendert sich um hoechstens 2e-5 (Hyperkubus), 5e-6 (Netz, bis t_Lauf = 2);
  Einheitsnorm der Links 2e-16; Summe_f w_f S_f S_f^T = Vc I_6 auf 1,7e-16 nachgerechnet.

## 2. Tabellen (Referenz c = 0,3; Fehler Jackknife, leave-one-out)

### Hyperkubus (kappa = 1, T_c = 0,25/a)

| beta | Gitter | Konfig. | t0 (a^2) | Fehler t0 | w0 (a) | w0/Wurzel(t0) | T_c Wurzel(t0) |
|---|---|---|---|---|---|---|---|
| 2,25 | 12^4 | 30 | 0,9096 | 0,013 (1,4 %) | 1,0265 | 1,0763 +- 0,0054 | 0,2384 +- 0,0017 |
| **2,30** | 12^4 | 30 | **1,2625** | 0,021 (1,7 %) | 1,162 | **1,0342 +- 0,0059** | **0,2809 +- 0,0024** |
| 2,35 | 12^4 | 30 | 1,8447 | 0,034 (1,9 %) | 1,3793 | 1,0156 +- 0,0071 | 0,3395 +- 0,0031 |
| 2,30 | 8^3 x 8 | 40 | 1,2499 | 0,032 (2,6 %) | 1,1644 | 1,0415 +- 0,0105 | 0,2795 +- 0,0036 |

### Zeltnetz (kappa = 0,0145003, T_c = 0,718356/a, Nt = 12, T = T_c/3)

| beta | Gitter | Konfig. | t0 (a^2) | Fehler t0 | w0 (a) | w0/Wurzel(t0) | T_c Wurzel(t0) |
|---|---|---|---|---|---|---|---|
| 3,24 | L = 6 | 9 | 0,09195 | 0,0018 (2,0 %) | 0,3395 | 1,1196 +- 0,0091 | 0,2178 +- 0,0021 |
| 3,29 (Lauf 1) | L = 6 | 12 | 0,14623 | 0,0033 (2,3 %) | 0,3940 | 1,0305 +- 0,0041 | 0,2747 +- 0,0031 |
| 3,29 (Lauf 2) | L = 6 | 13 | 0,14370 | 0,0018 (1,2 %) | 0,3914 | 1,0326 +- 0,0077 | 0,2723 +- 0,0017 |
| **3,29 (beide)** | L = 6 | 25 | **0,14489** | 0,0018 (1,2 %) | 0,3928 | **1,0318 +- 0,0042** | **0,2734 +- 0,0017** |
| 3,34 | L = 6 | 9 | 0,2351 | 0,0088 (3,8 %) | 0,4835 | 0,9973 +- 0,0185 | 0,3483 +- 0,0065 |
| 3,29 | L = 4 | 28 | 0,15235 | 0,0046 (3,0 %) | 0,4004 | 1,0257 +- 0,0102 | 0,2804 +- 0,0043 |

- E_0 = 3278 /a^4 auf dem Netz (Hyperkubus 9,54 /a^4), weil die Kanten kuerzer sind (0,22 bis 0,52 a).
- Netz beta = 3,34: ein erster Lauf mit tmax 15 erreichte t^2 E = 0,3 nicht (Maximum 0,289; verworfen, Datei n6t12-b334 bleibt als Beleg); der Wiederholungslauf mit tmax 22 (n6t12-b334b) ist verwendet.
- Wurzel(t0) bei c = 0,3: Hyperkubus 1,124 a (Flussradius Wurzel(8 t0) = 3,18 a gegen Kante a), Netz 0,381 a (Flussradius 1,08 a gegen Kanten 0,22 bis 0,52 a, Raumbox 4,24 a, Zeitausdehnung Nt tau = 4,18 a).

## 3. Abgleich mit den Erwartungen der Karte (beschreibend)

| Nr | Erwartung | Befund | Wahrsch. laut Karte |
|---|---|---|---|
| S5a | Flow stabil, t0 aus t^2 <E> = 0,3 mit Fehler unter 3 % | Hyperkubus 1,7 % (30 Konfig.), Netz 1,2 % (25 Konfig.), beide mit Konfigurationen ohne Divergenz; Fluss stabil fuer eps <= 0,1. Ein Pilotlauf mit eps bis 0,3 ist bei t_Lauf > 9 explodiert (E sprang von 18 auf 2100); das Freifeld-Spektrum gibt eine RK3-Grenze eps < 0,207, der Pilot bestaetigt sie qualitativ | 80 % |
| S5b | T_c Wurzel(t0) Netz weicht um weniger als 15 % vom Hyperkubus ab | -2,7 +- 1,0 % bei beta_c(Netz) = 3,29. Mit der Steigung 4,7 je beta gilt die 15-%-Grenze fuer beta_c im Fenster 3,261 bis 3,325 (Interpolation, Tabelle 4). Ausserhalb (zum Beispiel 3,25: -19 %, 3,33: +18 %) ist sie verletzt | 45 % |
| S5c | w0/Wurzel(t0) auf beiden Gittern auf 10 % gleich | -0,2 +- 0,7 % bei den zentralen beta (2,30 / 3,29). Bei fester beta-Zuordnung ueber die Nachbarwerte bis 10,2 % (Hyperkubus 2,35 gegen Netz 3,24), bei gleichem T_c Wurzel(t0) (beta* = 3,296) 1,03 gegen 1,03 | 55 % |

- Meine Vorab-Erwartungen (VORAB-S5.md Abschnitt 6): S5a 85 %, S5b 35 %, S5c 50 %. Meine Schaetzung, das Netz liege 20 bis 35 % hoeher, kam aus sigma von S4 und war falsch (tatsaechlich -2,7 %).
  Das Risiko "negative Gewichte machen den Fluss instabil" (25 %) ist nicht eingetreten: das Freifeld-K ist positiv semidefinit (kleinster Eigenwert -3e-15), die geflowten Konfigurationen blieben endlich.
- Lesart ohne Starkwoerter: Bei c = 0,3 und beta_c(Netz) = 3,29 fallen Netz und Hyperkubus in T_c Wurzel(t0) und in w0/Wurzel(t0) zusammen. Das ist mit gleichem Kontinuumsverhalten **vereinbar**, belegt es aber nicht (ein Gitterabstand je Gitter, keine Kontinuumsextrapolation).

## 4. beta-Abhaengigkeit und Fenster fuer beta_c (Rechnung aus den Tabellen, code/zusammen_s5.py)

- d ln Wurzel(t0) / d beta: Hyperkubus 3,3 (2,25 bis 2,30), 3,8 (2,30 bis 2,35), gesamt 3,54; Netz 4,55 (3,24 bis 3,29), 4,84 (3,29 bis 3,34), gesamt 4,69. (Asymptotisch waeren es 2,7; die Gitter liegen im Uebergangsbereich.)
- Interpolation von ln(T_c Wurzel(t0)) (Parabel durch drei beta-Werte) auf dem Netz:

| beta_c (Netz) | T_c Wurzel(t0) | Verhaeltnis zum Hyperkubus (2,30: 0,2809) |
|---|---|---|
| 3,25 | 0,2277 | 0,811 |
| 3,27 | 0,2492 | 0,887 |
| 3,29 | 0,2734 | 0,973 |
| 3,30 | 0,2867 | 1,020 |
| 3,33 | 0,3314 | 1,180 |

- Gleichheit bei beta* = 3,296. Fenster 15 %: 3,261 bis 3,325; 10 %: 3,273 bis 3,316; 5 %: 3,285 bis 3,306.
- beta_c(Netz) aus den frueheren Lauefen: L = 6: Anstieg von |L| zwischen 3,25 und 3,30 (Leitung: 3,30), L = 4: 3,33. Beides liegt im 15-%-Fenster, der untere Rand des L = 6-Anstiegs (3,25) liegt knapp ausserhalb.
- Hyperkubus: T_c Wurzel(t0) bei dem Literaturwert beta_c = 2,2986 ist 0,2795 (statt 0,2809 bei 2,30), der Unterschied ist 0,5 %.

## 5. Kontrollen und Nebenbefunde

- **Endvolumen:** Netz L = 4 gegen L = 6: t0 um 5,2 % hoeher (1,5 Sigma); Hyperkubus 8^3 x 8 gegen 12^4: -1,0 % (0,3 Sigma). Das Netz ist bei L = 6 (Flussradius 1,08 a gegen Box 4,24 a, Verhaeltnis 0,25) nicht frei von Endvolumen-Einfluss, der Trend ist aber klein gegen die beta_c-Unsicherheit.
- **E_s / E_t (Scheibenanteil gegen Rest der Energie):** Hyperkubus 1,00 bei jeder Flusszeit (Euklid-Symmetrie, die drei Raum- gegen drei Zeitebenen). Netz 0,419 bei Flusszeit 0 und **0,459 bei t0**; das Freifeld-Verhaeltnis aus den Gewichten und Dreiecksklassen (es_et_pred.py)
  ist 0,4568 fuer isotropes F. Die Aufspaltung ist beim Netz rein geometrisch (Scheiben-Dreiecke liegen nicht in einer echten Zeitscheibe) und stimmt bei t0 mit dem isotropen Wert auf 0,5 % ueberein.
- **kappa:** Freifeld-Bloch-Spektrum (flow_bloch.py): drei transversale akustische Aeste mit lambda / k^2 = 0,014500 (zwei Polarisationen, alle 9 Richtungen inkl. Zeitrichtung, |k| = 0,05 bis 0,4/a), dritte Polarisation bis 0,01427 (1,6 % tiefer). Systematik fuer Wurzel(t0): +- 0,8 %.
  w0/Wurzel(t0) ist davon unabhaengig.
- **DEC-Metrik:** Summe |e||*e| = 0,348007 = 4 Vc stimmt, aber h_l = |*e|/|e| liegt zwischen -0,022 und 0,164, 26 von 146 Kantenklassen sind nicht positiv. Das Netz ist fuer die Kanten nicht umkreismittig wohlzentriert; die Metrik-Variante (--metrik) wurde nicht gerechnet.
- **Vergleich mit S4:** S4 gab auf dem Netz T_c/Wurzel(sigma) = 0,85 +- 0,15 (L = 4, Nt = 10, mit ERGEBNIS-S4-Hinweis: Spannweite 0,71 bis 0,86; Hyperkubus 0,673), das heisst Wurzel(sigma t0)(Netz) ~ 0,32 gegen 0,42 auf dem Hyperkubus. S5 sagt T_c Wurzel(t0) gleich.
  Beide zusammen ergaeben ein um etwa 23 % kleineres Wurzel(sigma t0) auf dem Netz; das ist bei einer S4-Fehlergrenze von 15 % in Wurzel(sigma) etwa 1,5 Sigma. Offen, nicht aufgeloest.

## 6. Was aus dem Aufbau folgt und was gerechnet ist

- **Folgt aus Aufbau:** Der Flussgenerator ist exakt die Wirkung des Monte Carlo. Wegen Summe_f w_f S_f S_f^T = Vc I_6 (nachgerechnet) ist die Kontinuumsnormierung des Generators richtig; die **Zeit** ist es nicht (Faktor 1/kappa), weil
  die Gewichte dimensionslose Verhaeltnisse sind und der Generator keine Link-Metrik hat. Das ist aus der Freifeldrechnung abgeleitet, nicht aus dem wechselwirkenden Fluss gemessen.
- **Gerechnet:** t0, w0, T_c Wurzel(t0) auf den Gittern der Tabellen mit Jackknife-Fehlern; Freifeld-Spektrum; Test-Identitaeten. Nicht gerechnet: T_c auf dem Netz (beta_c(Nt = 4) ist aus den frueheren Laeufen uebernommen), Kontinuumsextrapolation,
  Kleeblatt-Definition von E, zweiter Gitterabstand je Gitter.

## 7. Grenzen

- Ein Gitterabstand je Gitter. Gitterfehler von t0 und w0 mit der Plakette sind nicht abgeschaetzt; sie sind bei c = 0,1125 gross (siehe unten) und bei c = 0,3 unbekannt.
- **c = 0,1125:** T_c Wurzel(t0) Netz 0,0885 gegen Hyperkubus 0,1338 (Verhaeltnis 0,66), w0/Wurzel(t0) Netz 2,49 gegen Hyperkubus 1,49. Wurzel(t0) = 0,123 a liegt unter den Kantenlaengen, also im Gitterbereich. Mit diesem Referenzwert waere S5b und S5c nicht erfuellt.
  Die Uebereinstimmung bei c = 0,3 haengt damit an der Wahl der Referenz, die die Karte vorgab.
- beta_c(Netz) nur auf etwa +- 0,03 bekannt (L = 6 gegen L = 4: 3,28 gegen 3,33), damit +- 14 % in T_c Wurzel(t0). Das ist das groesste Fehlerbudget, nicht der statistische Fehler.
- Statistik beim Netz: 9 bis 28 Konfigurationen je Punkt, zwei unabhaengige Laeufe nur bei beta = 3,29; die Autokorrelationszeit ist nicht gemessen (Lag-1 von t0 klein). beta = 3,34 mit 3,8 % Fehler.
- Netz L = 6 hat Endvolumen-Einfluss im Prozentbereich (Abschnitt 5). Hyperkubus 12^4 mit Flussradius 0,27 L.
- kappa aus der Freifeldnaeherung; der wechselwirkende Fluss auf dem Netz bei Flussradius 1,08 a (2 bis 5 Kantenlaengen) kann davon abweichen. Ein Hinweis auf Konsistenz ist E_s/E_t = 0,459 gegen 0,457 (nur Isotropie, nicht der Wert von kappa).
- Synthetisch: SU(2) ohne Fermionen. T_c Wurzel(t0) = 0,28 ist nicht mit QCD-Zahlen vergleichbar.

## 8. Regelabweichungen

- Zwei Startbefehle (`ssh -f ... nohup bash ... < /dev/null &`) leiteten die Standardeingabe aus /dev/null um (AGY-REGELN: nichts nach /dev/null). Keine Ausgabe oder Datei dorthin; kein Einfluss auf Daten.
- Ein `pkill -f` mit dem Muster "s5-pilot" (nur meine Pilotlaeufe) beendete versehentlich die eigene ssh-Sitzung; fremde Prozesse nicht betroffen. Der Erststart der beiden Piloten war ein Skriptfehler (Variable nicht gesetzt) und lief nach Neustart durch.
- Die Pilotdatei pilot-n.json stammt von der ersten Fassung von su2flow.py (code/su2flow.py.v1, ohne --metrik/Schrittplan); alle Produktionsdaten von der Fassung mit der Pruefsumme in PRUEFSUMMEN-S5.txt.
- Sonst keine: lokal kein python, awk oder perl; Rechnen nur ueber kleintest.sh (Spuren p4000a, p4000b, cpu7); df vor jedem Start (17 GB frei); je Lauf unter 10 min (laengster 484 s); nichts in /tmp oder /dev/shm; Original su2.py, su2b.py, qu2.py unveraendert;
  keine Commits, keine Nachrichten.

## Einfach gesagt

Man misst die Groesse des Gitters nicht mehr mit der Spannung eines Fadens, sondern damit, wie schnell man die Zacken im Feld glaetten muss, bis eine bestimmte Energie erreicht ist. Mit dieser Messlatte liegen Finns Netz und das normale Wuerfelgitter bei der gewaehlten Kopplung nur etwa 3 Prozent auseinander, und das Verhaeltnis der beiden Glaettungsmasse ist praktisch gleich. Das hat aber einen Haken: Die Kopplung am Uebergang ist auf dem Netz nur auf etwa 0,03 genau bekannt und die Zahl reagiert darauf stark, und mit einer feineren Messlatte (kleinerer Referenzwert) passen die beiden Gitter nicht zusammen.
