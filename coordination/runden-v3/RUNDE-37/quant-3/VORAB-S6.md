# VORAB-S6: zweiter Gitterabstand (Nt_c = 6) fuer Hyperkubus und Zeltnetz (vor jeder Rechnung)

- Autor: Rechen-Agent fuer die Leitung claude-primary. Zeit (date): 2026-10-07 17:25:38 CEST. Bis hierher nur Lesen von KARTE.md, ERGEBNIS-S5.md, VORAB-S5.md, ERGEBNIS.md, ERGEBNIS-S4.md, AGY-REGELN.md und der Skripte; keine Rechnung, kein Lauf.
- Die Erwartungen S6a bis S6d der Karte bleiben unveraendert. Methode wie S5, unveraendert: Wilson-Flow mit derselben gewichteten Wilson-Wirkung, Luescher-RK3, Plakettenenergie E = (4/V4) Summe w_f (1 - p0_f), t0 und w0 mit c = 0,3 (Hauptwert; c = 0,1125 als Empfindlichkeit), Jackknife (leave-one-out), Flusszeit in a^2: t = kappa t_Lauf mit kappa = 0,0145003 (Netz, Freifeld-Bloch) bzw. 1 (Hyperkubus), T_c = 1/(Nt_c a) (Hyperkubus) bzw. 1/(Nt_c tau a) (Netz), tau = 0,348006576329167. Code: su2b.py/ana.py/su2flow.py/ana_flow.py/ana_s4b.py unveraendert; Aenderungen nur als neue Dateien.

## 1. Plan und Groessen

**A. beta_c(Nt = 6) aus der Polyakov-Suszeptibilitaet** (Regeln A.1 bis A.4 aus VORAB-S4B-AUSWERTUNG.md unveraendert: ana.py tab --nbin 20, ana_s4b.py beta, Teilmenge "beide", Parabel durch Maximum und zwei Nachbarn, signifikant = mindestens 95 % von 4000 Ziehungen konkav und Scheitel im Intervall, Fehler quadratisch mit (heiss - kalt)/2).
- Hyperkubus 18^3 x 6 (Seitenverhaeltnis 3), su2b.py, heisse Starts (beta aufwaerts) und kalte Starts (beta abwaerts) als zwei Replikas, beta = 2,38 / 2,40 / 2,42 / 2,43 / 2,44 / 2,46 / 2,48, ntherm 200 je Stufe, nmess so gross, wie ein Lauf unter 10 min bleibt (Zeitlimit des Programms; die Zahl steht im Ergebnis). Literatur [L, aus dem Gedaechtnis] ~2,43 dient nur als Kontrolle (S6a: 2,40 bis 2,46).
- Netz: L = 9, Nt = 6 (Raumbox 9 mal 0,707 a = 6,36 a, Zeitausdehnung 6 tau = 2,09 a, Verhaeltnis 3,05 wie L = 6/Nt = 4 in S4b), tau = 0,348006576329167, Gewichte gwp.npz. beta = 3,40 bis 3,70 in Schritten von 0,05 (7 Stufen), heiss aufwaerts und kalt abwaerts. Die Lage kommt aus b2-n6t6 (L = 6, Nt = 6: |L| = 0,068 bei 3,5, 0,096 bei 3,6) und dem Verhalten bei Nt = 4 (Anstieg bei 3,3). Ausweichen auf L = 8, wenn L = 9 an GPU-Speicher (frei etwa 2,4 GB auf den P4000) oder Zeit scheitert; das wird dann genannt.
- Ist die Regel A.3 nicht erfuellt, gibt es **kein** beta_c aus chi_L; dann wird nur das Gitterpunkt-Maximum genannt und die Netz-Flussrechnung bei einem beta aus der |L|-Lage gerechnet, mit beta-Abhaengigkeit ueber Nachbarwerte (wie S5). Der Fehler von beta_c geht als Streuung der Teilergebnisse (heiss, kalt, nbin 10 gegen 20) ein, nicht nur als Regelfehler (Lehre aus S4b: Regelfehler 0,0013, Streuung 0,01).

**B. Kalte Gitter und Fluss**
- Hyperkubus: 18^4 (T = T_c/3, Nt = 3 Nt_c), bei beta = beta_c(Hyperkubus) aus A (Rundung auf 0,01) und zwei Nachbarn beta +- 0,05 fuer die beta-Abhaengigkeit, soweit die Zeit reicht. tmax so, dass W(t) = 0,3 erreicht wird (Schaetzung t0 ~ 2,8 a^2 aus T_c Wurzel(t0) = 0,28; tmax 6).
- Netz: L = 6, Nt = 18 (T = T_c/3, Zeitausdehnung 6,26 a, Raumbox 4,24 a), bei beta_c(Netz) aus A (auf 0,01 gerundet). Nachbarwerte beta +- 0,05, soweit die Zeit reicht. Die Raumbox bleibt wegen GPU-Speicher bei L = 6: Der Flussradius Wurzel(8 t0) liegt bei etwa 1,6 a (Verhaeltnis zur Box etwa 0,38, wie im L = 4-Test von S5, dort t0 +5,2 % gegen L = 6). **Das ist eine bekannte Verzerrung des Netz-Werts nach oben, ich kann sie nicht beheben**; ich nenne sie bei jedem Vergleich. Falls der Speicher L = 7 erlaubt (nicht erwartet), wird er genannt.
- Fluss: eps(t) = min(max(0,02, 0,05 t), 0,1), RK3, E alle 2 Schritte, 150 Thermalisierungs-Sweeps, danach alle 20 Sweeps eine Konfiguration (wie S5). tmax Netz: nach der beta_c-Bestimmung, so dass 1,4 t0 abgedeckt ist (Schaetzung t0_Lauf ~ 22).
- Pilot (technisch, vor den Produktionslaeufen): Speicher und Zeit je Konfiguration, dS/dt-Test und eps gegen eps/2 bis t = 2 (--test), 1 bis 2 Konfigurationen; die Pilotdaten gehen nicht in die Ergebnisse.

**C. Vergleich ueber die Abstaende**
- Vergleichsgroessen: R_T = (T_c Wurzel t0)_Netz / (T_c Wurzel t0)_Hyperkubus, R_w = (w0/Wurzel t0)_Netz / (...)_Hyperkubus je Abstand (Nt_c = 4: S5-Werte 0,973 und 0,998; Nt_c = 6: S6), mit Jackknife-Fehlern, dazu die beta-Unsicherheit ueber die Steigung d ln Wurzel(t0)/d beta wie in S5 (Abschnitt 4 von ERGEBNIS-S5).
- Extrapolation in a^2: nur beschreibend, zwei Punkte, a^2 ~ 1/Nt_c^2 (Hyperkubus) bzw. 1/(Nt_c tau)^2 gleiches Verhaeltnis; lineare Extrapolation R(a^2) = R_0 + c a^2 durch die zwei Punkte. Mit zwei Punkten gibt es keinen Test der Linearitaet und keinen Freiheitsgrad; ich nenne den Wert "beschreibend" und gebe die Fehler aus den beiden Einzelfehlern an.

## 2. S6d (Flusszeit-Umrechnung kappa)
- kappa ist in S5 eine Freifeld-Groesse (Bloch-Spektrum von K(k) mit den Gewichten gwp.npz) und haengt nur an Geometrie und Gewichten, nicht an beta, L, Nt oder an Nt_c. **Vorab-Aussage:** Eine Freifeld-Neuberechnung muss denselben Wert liefern, die "Aenderung" ist null per Konstruktion; das ist als Test von S6d wenig aussagekraeftig. Gerechnet wird deshalb (i) flow_bloch.py unveraendert noch einmal (Kontrolle, nur Reproduktion) und (ii) ein wechselwirkender Gegentest: Isotropie E_s/E_t bei t0 gegen die Freifeldvorhersage 0,4568 (es_et_pred.py), sowie der implizite Wert kappa_eff = (t0 aus T_c Wurzel(t0)-Gleichheit)/(t0 Lauf), der aber an beta_c haengt und gross unsichere Fehlerbaender hat. Ich werde S6d nicht als "bestanden" melden, wenn nur (i) vorliegt.

## 3. Eigene Erwartungen (Hypothesen, vor der Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| S6a | beta_c(Hyperkubus, Nt = 6) aus chi_L im Bereich 2,40 bis 2,46 (eine Spitze wird sichtbar; 18^3 x 6 hat grobe chi_L-Fehler) | 70 % |
| S6a' | beta_c(Netz, Nt = 6) mit Regel A.3 signifikant bestimmbar | 40 % |
| S6a'' | beta_c(Netz, Nt = 6) liegt zwischen 3,45 und 3,65 | 65 % |
| S6b | w0/Wurzel(t0) Netz gegen Hyperkubus (6) auf 2 % | 50 % (S5 hatte 0,2 %, aber bei diesem Abstand koennen Endvolumen und beta_c-Lage 3 bis 5 % bringen) |
| S6c | Abweichung in T_c Wurzel(t0) wird kleiner oder bleibt unter 5 %: von beta_c abhaengig. Ich erwarte einen Wert zwischen -15 % und +15 % wegen der beta_c-Unsicherheit (+-0,03 gleicht 14 %) | 35 % fuer unter 5 % |
| S6d | kappa gleich auf 3 % (per Konstruktion Freifeld) | 95 % fuer das Freifeld, wechselwirkend nicht gerechnet |
| E1 | Hyperkubus T_c Wurzel(t0) bei Nt_c = 6 liegt um 0 bis 8 % ueber dem Nt_c = 4-Wert 0,2795 bis 0,2809 (Gitterfehler wachsen mit Nt_c) | 60 % |
| E2 | Netz-Fehler von t0 (L = 6, Nt = 18, 10 bis 20 Konfigurationen) 2 bis 5 % | 60 % |

- Risiken: Netz L = 6 zu klein (Endvolumen +5 %); GPU-Speicher knapp (Fremddienste belegen 5,5 GB von 8 GB je P4000); Netz-Kosten pro Konfiguration etwa 90 bis 120 s, also nur etwa 3 bis 5 Konfigurationen je 10-min-Lauf, damit Fehler 3 bis 5 %; beta_c(Netz) nur auf etwa +-0,03 (wie S5), das groesste Fehlerbudget.
- Nicht erwartet, aber moeglich: kein Maximum von chi_L im Netz-Scan (Nt = 6, L = 9 mit 7 Stufen und kurzer Statistik).
- Auswerteregeln wie in S5: Zahlen aus den Tabellen, Fehler Jackknife; keine Staerkewoerter; kein Verschieben der Erwartungen nach Sicht.

## 4. Laufbegrenzung
- Je Lauf hoechstens 10 min (zeitlimit unter 560 s), nur Spuren p4000a/p4000b (GPU) und cpu/cpu7 (Auswertung), df vorher (.69 hat 17 GB frei, Abbruch unter 10 GB), Ausgabe nach /home/fmh/fmhc-physics-remote/quant-3/lauf-s6/, lokal nach lauf-69-s6/.

## 5. Nachtrag nach den Pilot- und ersten Scanlaeufen (date: 2026-10-07 17:51:06 CEST; Teile 1 bis 4 oben sind unveraendert)

Gelaufen vor diesem Nachtrag (Pilotdaten gehen nicht in die Ergebnisse): pilot-k, pilot-n, pilot-n2, pilot-n3; Hyperkubus-Scan h1 (18^3 x 6, beta 2,38 / 2,42 / 2,44 / 2,48, 1000 Messungen je Stufe); Netz-Scan n1 (L = 9, Nt = 6); Netz-Scans n2a und n2b (L = 8, Nt = 6, beta 3,40 bis 3,65).
- **L = 9 verworfen:** n1 (L = 9) lief mit der GPU-Speichergrenze (Mess-Graph nicht erfassbar, eager) 411 s je Stufe, nur eine Stufe (beta 3,40 heiss / 3,70 kalt). Das Netz wechselt auf L = 8 (Ausweichgroesse laut Abschnitt 1.A, Seitenverhaeltnis 2,7), mit su2b_s6.py (su2b.py unveraendert, nur PYTORCH_CUDA_ALLOC_CONF=expandable_segments). n1 geht nicht in beta_c ein.
- **Grund Zeit:** Die P4000 rechnet in float64 langsam; L = 8, Nt = 6 braucht rund 0,35 s je Sweep samt Messung (2 Replikas), also etwa 520 Schritte je 180 s. Ein 10-min-Lauf traegt drei beta-Stufen mit 400 Messungen. Das ist knapp (tau_int(|L|) 3 bis 9 Messungen, 20 Bins zu 20); der Regelfehler von beta_c wird deshalb wie in S4b nur mit der Streuung der Teilergebnisse als Fehler genannt.
- **Lage der Spitze:** Im Bereich 3,40 bis 3,65 liegt das chi_L-Maximum am untersten Punkt (3,40: chi 2,19 kalt, 1,21 heiss; Binder U4 0,33 / -0,24, also der Uebergang selbst), |L| steigt von 0,02 auf 0,06 zwischen 3,40 und 3,45. Der Uebergang liegt somit bei oder unter 3,40, nicht im vorab geschaetzten Bereich 3,45 bis 3,65 (S6a'': eingetroffen waere 3,45 bis 3,65, wird verfehlt, falls beta_c unter 3,40 bleibt). Neuer Lauf n3: beta 3,30 / 3,35 / 3,375 (L = 8, Nt = 6). Zusammen mit n2: Gitter 3,30 bis 3,65. Sonst gelten die Regeln A.1 bis A.4 unveraendert (Teilmengen ueber alle Laeufe zusammengefuehrt mit code/merge_tab_s6.py, Gewichte wie "beide").
- **Hyperkubus:** h1 zeigt chi_L-Spitze zwischen 2,42 und 2,44 (chi 5,3 / 5,8 / 4,4 / 5,7); Lauf h2 (2,40 / 2,43 / 2,46, 1200 Messungen) folgt, dann gemeinsame Parabel ueber h1 + h2.
- **Netz-Fluss:** Pilot (L = 6, Nt = 18, beta 3,55) zeigt t^2 E in Flusszeit t_Lauf = 30 erst bei 525 (Zielwert 0,3/kappa^2 = 1427): bei beta 3,55 ist t0 groesser als 0,44 a^2, also T_c Wurzel(t0) groesser als 0,32, ein Hinweis, dass beta 3,55 ueber beta_c liegt. Speicher mit su2flow_s6.py (Staple in Bloecken, gleiche Rechnung): 1540 MB; Kosten etwa 100 s je Konfiguration bei tmax 30. epsmax fuer die Produktion: 0,15 statt 0,1 (spart Zeit; Stabilitaetsgrenze Freifeld 0,207); eps gegen eps/2 bis t = 10 als Kontrolle im ersten Produktionslauf (--test --ttest 10).
- Eigene Erwartung ergaenzt (vor n3): beta_c(Netz, Nt = 6, L = 8) liegt zwischen 3,33 und 3,42 (65 %).

## 6. Nachtrag nach den beta_c-Auswertungen, vor den Produktionslaeufen des Flusses (date: 2026-10-07 18:01:23 CEST; Lauf fh-a (Hyperkubus 18^4, beta 2,43) war schon gestartet, kein Ergebnis gelesen ausser dem Pilot-Test und cfg 0; Teile 1 bis 5 unveraendert)

Ergebnis der beta_c-Auswertung nach den festen Regeln A.1 bis A.4 (Details in ERGEBNIS-S6.md):
- Hyperkubus 18^3 x 6 (h1 + h2, 7 Stufen): Regel A.3 fuer "beide" **nicht erfuellt** (Anteil konkav 0,935 < 0,95); Gitterpunkt-Maximum 2,43. Querprobe 5-Punkt 2,437 +- 0,008 (signifikant), heiss 2,431, kalt 2,457. Es gibt kein Regel-beta_c; Produktion bei **beta = 2,43** (Gitterpunkt-Maximum), Nachbarn 2,38 und 2,48. S6a (2,40 bis 2,46) ist damit fuer Maximum und Querproben erfuellt.
- Netz L = 8, Nt = 6 (n2a + n2b + n3, 9 beta-Stufen von 3,30 bis 3,65): Regel A.3 erfuellt, **beta_c = 3,411 +- 0,014** (Regelfehler 0,0015, heiss 3,386, kalt 3,414, 5-Punkt 3,430). Produktion bei **beta = 3,41**, Nachbarn 3,36 und 3,46. Die Streuung der Teilergebnisse ist 0,03; ich rechne die Folge fuer T_c Wurzel(t0) mit +-0,03 (wie S5) und nenne die Regelzahl nicht allein.
- Eigene Erwartung vor den Fluss-Ergebnissen: Netz bei 3,41 hat t0 zwischen 0,25 und 0,5 a^2 (T_c Wurzel(t0) 0,24 bis 0,34); Hyperkubus bei 2,43 hat t0 zwischen 2,0 und 3,8 a^2 (T_c Wurzel(t0) 0,24 bis 0,33). Das Verhaeltnis R_T liegt zwischen 0,85 und 1,15 (60 %). Produktionsparameter: Hyperkubus 18^4, tmax 8, epsmax 0,1, 150 Thermalisierungs-Sweeps; Netz L = 6, Nt = 18, tmax 45, epsmax 0,15, 150 Thermalisierungs-Sweeps; ntherm, mabst 20, Jackknife wie S5.
