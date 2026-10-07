# PHASE-3D: Bestimmt die ebene Wandphase auch die Lage der 3D-Sprossen (theta_inf)? (Runde 26, Fast Lane)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 04:34:09 CEST (date), vor jeder Rechnung.
- **Herkunft:** PHASE-WAND (RUNDE-26/phase-wand/ERGEBNIS.md). In 1D gilt k_in x_w(eps) + phi = m pi/2.
  - phi ist die ebene Reflexionsphase: 2,553888 bei beta = 1/2, 2,260698 bei beta = 1.
  - x_w ist die Halbhoehen-Wandlage.
  - Die Formel traf eine versiegelte beta-1-Vorhersage auf <= 0,77 %.
- **Schreibtisch der Leitung [H]:**
  - In 3D, l = 0, ist mit u = r psi die Radialgleichung fuer u dieselbe wie in 1D; einen Zentrifugalterm gibt es bei l = 0
    nicht.
  - Die regulaere Innenloesung ist u ~ sin(k r) = cos(k r - pi/2), wie die ungerade 1D-Mode.
  - Daher erwarte ich: k_in R(eps_n) + phi = (n' + 1/2) pi, mit R = Halbhoehenradius des 3D-Profils.
  - Kruemmung und die Verschiebung der Sprossenfrequenz (rho_n - rho_z ~ 1,1 eps) liefern Korrekturen der Ordnung eps.
  - Im Papier-Parameter: theta_inf = 1/2 - phi/pi mod 1, also 0,6871 (beta = 1/2) bzw. 0,7804 (beta = 1).
  - Das Papier fuehrt theta als geeicht ("The coupled planar wall problem has not been solved here").
- **Daten** (vorhanden, nicht angepasst):
  - beta = 1/2: die 3D-Sprossen n = 1 bis 15 aus Tabelle tab:ladder in model-lab/papers/qball-bic-ladder-20260930/main.tex;
    n = 7 bis 10 praezise aus RUNDE-13/leiter3d-praez.
  - beta = 1: die acht Sprossen aus RUNDE-24/leiter-beta (eps 0,031 bis 0,070).
- Ableitbarkeitspruefung:
  - Die Lagen sind bekannt, die Formel nicht; sie wird nicht angepasst.
  - phi stammt nur aus der ebenen Rechnung, R(eps) nur aus den 3D-Profilen.

## Test (Code-Agent)

- **3D-Profile** (M1, l = 0) bei den bekannten Sprossen-omega^2, Halbhoehenradius R(eps): S(R) = S_c/2 mit S_c = 1/(2 beta),
  gleiche Wandkonvention wie PHASE-WAND.
- **Abweichung je Sprosse:** Delta_n = frac([k_in(rho_z) R(eps_n) + phi]/pi - 1/2), auf (-1/2, 1/2] gelegt.
  - Hauptform mit k_in und phi bei rho_z.
  - Als Nebenform mit k_in und phi bei rho_n, wo rho_n bekannt ist (nur berichtet).
- **Verlauf von Delta_n gegen eps:** linearer Ausgleich Delta = a eps + b ueber die kleinsten-eps-Sprossen; b ist die
  Abweichung im Grenzfall.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| P3D-1 | beta = 1/2: Fuer die drei Sprossen mit kleinstem eps (n = 13 bis 15) gilt |Delta_n| < 0,03 | 55 % |
| P3D-2 | beta = 1/2: Der lineare Ausgleich ueber n = 8 bis 15 hat |b| < 0,02, und |Delta_n| faellt mit eps | 50 % |
| P3D-3 | beta = 1: Der lineare Ausgleich ueber die acht Sprossen hat |b| < 0,03 | 45 % |

**Bedeutung (vorab):**
- P3D-1 und P3D-2 treffen ein:
  - Die ebene Wandphase bestimmt theta_inf der 3D-Leiter ohne Eichung.
  - Zusammen mit c_inf = rho_z - omega_min ist die Duennwand-Beschreibung des Papiers im Grenzfall vollstaendig berechnet
    [H].
- P3D-1 trifft nicht ein, aber |Delta_n| faellt gegen 0: Die Annaeherung ist langsamer. Beschreiben.
- |Delta_n| strebt gegen einen festen anderen Wert: Es gibt einen Konventions- oder Kruemmungsversatz. Beschreiben, nicht
  nachtraeglich einrechnen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min, 4 GB).
- Plan vor der ersten echten Rechnung einfrieren. Zielwerte und Lagen nicht als Befehlszeilen-Argumente, sondern ueber
  Dateien.
- Zeitbox 90 min.
