# VORAB-S5: Gradient-Flow-Skala auf Hyperkubus und Zeltnetz (vor jeder Rechnung)

- Autor: Rechen-Agent fuer die Leitung claude-primary. Zeit (date): 2026-10-07 14:43:22 CEST. Bis hierher nur Lesen, keine Rechnung, kein Lauf.
- Die Erwartungen S5a bis S5c der Karte bleiben unveraendert. Hier stehen Definitionen, Plan und meine eigenen Erwartungen.

## 1. Flussgleichung

- Wilson-Flow nach Luescher (2010): d V_t(l) / dt = Z(V_t) V_t(l), Z = - g0^2 (T^a d^a_l S_w), dabei d^a_l die Lie-Ableitung
  nach dem Link l, g0^2 = 4/beta.
- Flussgenerator ist **dieselbe gewichtete Wilson-Wirkung** wie im Monte Carlo: S_w = beta Summe_f w_f (1 - p0_f), p0_f = Re Tr U_f / 2,
  auf dem Hyperkubus w = 1, auf dem Netz w_f = gwp.npz (Potenz-Dual). Fuer SU(2) in Quaternionen mit U -> e^z U:
  d S_w = -beta p0-Anteil, daraus Z(l) = -(0, Vektorteil von U_l W_l), W_l = Summe_f w_f (Reststaple), exakt der Staple aus su2b.py.
  Die Faktoren beta und g0^2 heben sich weg, der Fluss haengt nur an den Links und den w_f.
- Folge: Z(l) ist die Gradientenrichtung ohne Link-Metrik. Auf dem Hyperkubus ist das der Standard. Auf dem Netz haben die
  Links verschiedene duale Volumina, die naive Form fliesst deshalb nicht exakt mit der kontinuierlichen Rate d_t B = D G
  (die Flussrate eines Links skaliert mit |l|^2 / V_l-dual). Das ist eine **Methodengrenze**, die ich nicht behebe (Auftrag:
  derselbe Generator), aber im Bericht nenne. Eine Link-Metrik waere eine Variante, keine Pflicht.
- Test vor der Auswertung: (i) dS/dt = - beta Summe_l |vec(U W)|^2 gegen endliche Differenz, (ii) epsilon gegen epsilon/2 (Schrittweitenkonvergenz
  von t^2 E), (iii) Einheitsnorm der Links.

## 2. Integrator

- Runge-Kutta 3. Ordnung nach Luescher (arXiv:1006.4518, Anhang C): W0 = V; W1 = exp(Z0/4) W0; W2 = exp(8/9 Z1 - 17/36 Z0) W1;
  V' = exp(3/4 Z2 - 8/9 Z1 + 17/36 Z0) W2, Z_i = eps Z(W_i). Exponential einer reinen Quaternion z: (cos|z|, sin|z| z/|z|).
  Schrittweite fest, eps wird in den Pilotlaeufen gegen eps/2 geprueft.

## 3. Energiedichte, t0, w0

- Plakette (nicht Kleeblatt): E = (4 / V4) Summe_f w_f (1 - p0_f), V4 = L^3 Nt V_c (Zelle V_c = |det A| = 0,25 tau auf dem Netz; 1 auf dem Hyperkubus), alles
  in a = kubische Kante der fcc-Zelle, t in a^2.
  Herleitung: 1 - p0 = a^4 (G^a_{mn})^2 / 8 je Ebene, sechs Ebenen: Summe = a^4 G^a G^a / 16, E = (1/4) G^a G^a = 4 Summe (1 - p0). Auf dem Netz gilt
  Summe_f w_f S_f S_f^T = V_c I_6 (Karte QUANT-2); ich pruefe diese Identitaet im Lauf nach (Spur = 6 V_c).
- E^plaq hat starke Gitterfehler bei kleinem t; t0 und w0 liegen aber bei t ~ 0,1 bis 1 a^2, ausserhalb der unmittelbaren Zone t < 0,05.
- t0: t^2 <E>(t0) = c_t. w0: W(w0^2) = c_w mit W(t) = t d(t^2 <E>)/dt (BMW 2012).
- **SU(2)-Konvention:** Karte verlangt 0,3. Fuehrend gilt t^2<E> = 3 (N^2-1) g^2/(128 pi^2) [L, Luescher 2010, aus dem Gedaechtnis],
  das ist bei gleichem g^2 fuer SU(2) der Faktor 3/8 von SU(3), also 0,1125. Ich nehme **c = 0,3 als Hauptwert** (Vorgabe der Karte; groesseres c = groesseres t0 =
  weiter von der Zellgroesse weg, was fuer das Netz mit kleinen Kanten guenstiger ist) und nenne c = 0,1125 als Empfindlichkeitswert, ebenso c_w gleich c_t. Der Test S5b/S5c ist ein
  Verhaeltnis zwischen zwei Gittern mit gleichem c, die Wahl von c verschiebt beide in gleicher Richtung, nicht die Aussage "Gitter gleich oder nicht" per se
  (Gitterfehler sind bei kleinerem c groesser).
- Fehler: Jackknife ueber Bloecke der Konfigurationen (Mittel E(t) je Block-Auslassung, t0 und w0 je Probe neu).

## 4. Einheiten

- Hyperkubus: T_c = 1/(4 a) = 0,25/a. Netz: T_c = 1/(Nt_c tau a), Nt_c = 4, tau = 0,348006576329167, T_c = 0,71836/a. Die Kontrollgroesse ist T_c Wurzel(t0) (dimensionslos).
- Nullte Temperatur: Hyperkubus 12^4 (T = T_c/3), Netz L = 6, Nt = 12 (T = T_c/3, Zeitausdehnung Nt tau = 4,18 a, Raumbox 6 mal Gittervektor 0,707 a = 4,24 a).
  Nt = 8 bei Zeitmangel (T = T_c/2).
- Kopplung: Hyperkubus beta = 2,30 (Karte; Literatur 2,2986). Netz beta = 3,29 (Auftrag; L = 6 aus m5: Anstieg von |L| zwischen 3,25 und 3,30, Leitung nahm 3,30).
  Um den Fehler durch die Lage von beta_c zu sehen, je zwei Nachbarwerte (Hyperkubus 2,25 und 2,35, Netz 3,24 und 3,34); aus der Steigung d ln(Wurzel t0)/d beta
  wird die Unsicherheit von T_c Wurzel(t0) durch beta_c abgeschaetzt (Hyperkubus +-0,01, Netz +-0,03 als Annahme, nicht gemessen).

## 5. Statistik und Ablauf

- Waermebad + Ueberrelaxation wie su2b.py (Original unveraendert, importiert), heisser Start, ntherm 200, danach alle 20 Sweeps eine Konfiguration, die sofort
  im Lauf geflowt wird (E, E_s, E_t je Schritt gespeichert, keine Konfigurationen).
- Hoechstens 10 min je Lauf (zeitlimit 480 s), Spuren p4000a/p4000b fuer die Laeufe, cpu7 fuer die Auswertung. df vorher: .69 hat 17 GB frei.

## 6. Eigene Erwartungen (vor Rechnung, Hypothesen)

- Hyperkubus beta = 2,30: t0(c = 0,3) ~ 0,8 a^2 (Schaetzung aus sigma a^2 = 0,138 und dem SU(3)-Wert Wurzel(t0) Wurzel(sigma) ~ 0,33), T_c Wurzel(t0) ~ 0,22 bis 0,24.
  Fehler von t0 unter 1 %. S5a wahrscheinlich erfuellt (85 %).
- Netz beta = 3,29: Mit sigma a^2 ~ 0,7 aus S4 folgt t0 ~ 0,15 bis 0,2 a^2 und T_c Wurzel(t0) ~ 0,28 bis 0,32, also 20 bis 35 % ueber dem Hyperkubus (S4 lag in dieselbe Richtung).
  Ich halte S5b (unter 15 %) fuer eher nicht erfuellt (35 %), S5c (w0/Wurzel(t0) auf 10 %) fuer ein Muenzwurf (50 %).
- Risiko: Flaechen mit negativem w_f (3 je Zelle, 5184 bei L = 6, Nt = 8 laut s4b-n6t8.json) machen S_w nicht nach unten beschraenkt; der Fluss kann auf dem Netz E nicht-monoton oder instabil machen
  (25 %). Wenn E(t) nicht monoton faellt oder t^2 E die Marke nicht erreicht, melde ich das als Befund und keinen t0-Wert.
- Zu erwartende Fehlerquellen: Plakettendefinition (Gitterfehler), Raumbox des Netzes klein, naiver Fluss ohne Link-Metrik, beta-Lage, Autokorrelation.

## 7. Nachtrag nach den Pilotlaeufen (date: 2026-10-07 14:52:58 CEST; Pilotlaeufe pilot-k, pilot-n, pilot-nm, pilot-nn und flow_bloch liefen vor diesem Nachtrag; Teile 1 bis 6 oben sind unveraendert)

Was die Piloten gezeigt haben (noch keine Produktionsdaten, nur 2 bis 3 Konfigurationen je Lauf):
- Test (i), dS/dt gegen -beta Summe |vec(UW)|^2: relative Abweichung 3,5e-4 (Hyperkubus) und 2,7e-4 (Netz) bei eps = 1e-4 (ist die Fehlerordnung der endlichen Differenz).
  Test (ii), eps gegen eps/2: relative Abweichung von E 2e-5 (Hyperkubus, eps 0,02) und 3e-6 (Netz). Einheitsnorm 2e-16.
- **Der naive Fluss auf dem Netz laeuft nicht in Einheiten a^2.** E(0) = 3277 /a^4 (Hyperkubus 9,6), die Kantenlaengen liegen bei 0,22 bis 0,52 a, und E faellt in der Flusszeit t des
  Generators nur langsam (E = 18 bei t = 8,5). Ursache: Die Gewichte w_f sind dimensionslose Verhaeltnisse, der Generator ohne Link-Metrik fliesst mit der Rate Vc/6 mal der kontinuierlichen.
- Die DEC-Metrik h_l = |*e|/|e| ist auf dem Netz **nicht verwendbar**: Summe |e||*e| = 4 Vc stimmt (0,34801), aber 26 von 146 Kantenklassen haben h_l <= 0 (h von -0,022 bis 0,164). Die Variante --metrik bricht deshalb ab und wird nicht verwendet.
- Stattdessen Freifeld-Homogenisierung (flow_bloch.py, Bloch-Spektrum von K(k) = D^+ W D mit den Gewichten gwp.npz): K ist positiv semidefinit (kleinster Eigenwert -3e-15, also keine
  negative Mode trotz 3 negativer Gewichtsklassen), 10 Nullmoden (Eichmoden), drei transversale akustische Aeste mit Rate lambda = kappa k^2. kappa = 0,014500 fuer zwei Polarisationen in allen 9 Richtungen
  (x, y, z, 111, 110, t, x+t, 111+t, xyt) und |k| = 0,05 bis 0,4/a; die dritte Polarisation liegt in einigen Richtungen bei 0,01427 (1,6 % tiefer). kappa ist numerisch gleich Vc/6 = 0,0145003.
  Folge: Der Fluss ist auf grosse Wellenlaenge **isotrop in Raum und Zeitrichtung (auf 1,6 %)**; die Flusszeit in Einheiten a^2 ist **t = kappa t_Netz** mit kappa = 0,0145003 (Hyperkubus kappa = 1).
  Das ist eine Annahme der Freifeldnaeherung; ob sie fuer den wechselwirkenden Fluss bei t ~ 0,13 a^2 (Wellenlaenge Wurzel(8t) ~ 1 a gegen Kanten 0,2 bis 0,5 a) traegt, ist Teil des Befundes (S5a/S5c).
  Groesster Eigenwert ueber 60 zufaellige k: 12,09, damit ist RK3 stabil fuer eps < 2,5/12,09 = 0,207 (ein Pilotlauf mit eps bis 0,3 ist bei t > 9 explodiert, E sprang von 18 auf 2100; epsmax = 0,1 verwendet).
- Folge fuer die Erwartungen: Die Zahlenschaetzung der Abschnitte 6 stimmt mit dem Pilot ueberein (t^2 E erreicht 0,3 bei Flusszeit t_Netz ~ 8,6, also t ~ 0,125 a^2); das ist aber aus denselben 2 Pilotkonfigurationen gelesen und noch kein Ergebnis.
- Produktionsplan: Hyperkubus 12^4, beta 2,25 / 2,30 / 2,35, je 30 Konfigurationen, eps 0,02 mit Wachstum 5 % je t bis 0,1, tmax 2,0. Netz L = 6, Nt = 12, beta 3,29 (zwei Laeufe, anderer Seed) sowie 3,24 und 3,34 (kuerzer),
  tmax 15 in Flusszeit t_Netz, eps wie oben, E alle 2 Schritte. Fehlerangabe zusaetzlich: kappa-Unsicherheit 1,6 % in t (0,8 % in Wurzel t).
