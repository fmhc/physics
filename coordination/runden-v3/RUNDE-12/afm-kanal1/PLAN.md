# AFM-KANAL-1: Plan (vor jedem Lauf)

- Code-Agent, Auftrag AFM-KANAL-1 (Neustart nach Abbruch 30.09. ~20:10, damals keine Datei entstanden).
- Start 2026-10-01 17:12:01 CEST (date); PLAN.md begonnen 2026-10-01 17:29:58 CEST (date), vor dem Rauchtest und vor jedem
  .69-Lauf. Herleitung: HERLEITUNG.md (Formeln gleich MESS-3A K, keine Abweichung; zwei Lesepunkte, s. u.).
- Code: afm_kanal.py (neu). nls2.py wird als unveraenderte Kopie importiert (nur Profile fuer K2 und K4). Hashes in
  ERGEBNIS.md.

## 1 Bindende Regel (woertlich aus KARTE.md)

> - **Massgeblich ist der Wandzustands-Test** (Karte R, Punkt 9):
>   - Wandanteil F_w = Gewicht des Zustands in |r - R_w| < 2 delta. R_w ist der Radius mit Theta = Theta(0)/2, delta die
>     Wandbreite (10-90 %-Abstand von sin^2 Theta).
>   - Wandzustand heisst F_w > 0,5.
>   - **Verworfen:** Fuer die ganze Familie liegt auf beiden Gitterstufen kein Wandzustand im offenen Kontinuum
>     (1 - Omega < rho_c < 1 + Omega). Dann ist der AFM als Leiterkandidat im Sinn von Runde 10 verworfen, auch wenn
>     Regel 8 besteht.
>   - **Weiter:** Mindestens ein Familienmitglied hat auf beiden Gitterstufen einen eingebetteten Wandzustand, und die
>     Lage stimmt zwischen den Stufen auf 1e-3 in rho. Dann folgt als naechste Karte die W-Gitter-Suche mit Kopplung wie
>     in Runde 10.
>   - **Nicht auswertbar:** Eine der Kontrollen K0 bis K3 verfehlt.
> - Regel 8 (MESS-2 woertlich) wird mitgerechnet und berichtet, entscheidet aber nicht.
> - **Beweis, dass die Regel beide Ausgaenge hat:**
>   - Positivkontrolle K2: Im KG-Q-Ball (omega^2 = 0,7977) liegt der nackte Wandzustand bei E = 0,706 im Kontinuum; dort
>     muss derselbe Codepfad "eingebettet, F_w > 0,5" melden.
>   - Negativkontrolle, neu (K4): das kubisch-quintische NLS-Profil aus Runde 10 (RUNDE-10/nls-leiter, Wandzustand
>     ~0,1 ueber der Grenze). Dort muss derselbe Codepfad "kein eingebetteter Wandzustand" melden.
>   - Verfehlt K2 oder K4, ist der Lauf nicht auswertbar.

Regel 8 (MESS-3A R8, woertlich aus MESS-2): "Liegt der tiefste Zustand des geschlossenen Kanals auf zwei Gitterstufen
fuer die ganze Familie nicht im offenen Kontinuum, ist der Kandidat verworfen." Nur berichtet.

## 2 Vorhersagen (woertlich, vor jedem Lauf)

KARTE.md (Leitung):
> - Die Leitung uebernimmt die Vorab-Zahlen des Feldforschers nicht und gibt eigene an:
>   - Regel 8 besteht: ~85 %.
>   - Eingebetteter Wandzustand im Duennwandast (Omega^2 nahe 1 + kappa): ~45 %.
> - Grund der tieferen Zahl [H]: Der zusaetzliche Topf -2 Omega rho (1 - cos Theta) sitzt im Innenraum, nicht in der
>   Wand. Er zieht die tiefen Zustaende eher ins Innere.

MESS-3A Punkt 10:
> 10. Vorab-Vorhersage (vor jeder Rechnung): Regel 8 besteht (~80 %); Wandzustand nahe rho ~ 1 + Omega im
>     Duennwandast eingebettet (~55 %); Dickwandende (Omega -> 1) verhaelt sich NLS-artig (~70 %).

Eigene Erwartung des Code-Agenten [H], 17:29:58, aus HERLEITUNG.md Abschnitt 3 und 4 (Schreibtisch, ohne Zahl aus einem
Lauf):
- E-A1: Nach dem Wortlaut der Regel wird der Ausgang "weiter" (~70 %). Grund: Das Fenster |r - R_w| < 2 delta ueberdeckt
  ~4,4 f des Ballradius. Fuer f >= 0,2 erreichen schon gleichmaessig verteilte Innenraumzustaende (Hohlraummoden des
  Spin-Flop-Innern, eingebettet ab rho ~ sqrt((1 + f)|kappa|/2)) F_w > 0,5.
- E-A2: Ein an der Wand lokalisierter Zustand (Wandueberhoehung eta = F_w/L_w > 2, s. u.) im Duennwandast nahe
  1 + Omega: nicht gesehen (~75 %). Der Innenraum ist bei rho ~ 1 + Omega klassisch erlaubt (W ~ -rho^2), der Wandtopf
  nur O(|kappa|) tief.
- E-A3: Regel 8 besteht (~90 %), getragen von Innenraumzustaenden, wie MESS-3A K vorhersagt.

## 3 Rechnung

- Modell, Profil, Kanaele: MESS-3A R1 bis R4 und HERLEITUNG.md. Nackter geschlossener Kanal (C = 0), l = 0, y = r w:
  H(rho) = -d^2/dr^2 + W, W = (V_u + V_v)/2 + 2 Omega rho cos Theta - rho^2, Dirichlet bei 0 und R_max, Differenzen
  2. Ordnung (symmetrisch tridiagonal).
- Profil: Schiessen (RK4, Schritt 0,02; Runde 0 logarithmisch im Abstand zu pi/2, dann linear) als Startwert, dann
  Numerov-Newton fuer y = r Theta auf dem Rechengitter (MESS-3A R2 erlaubt Newton-Relaxation). Grund: In doppelter
  Genauigkeit trennt sich das Klammerpaar beim Duennwandball schon an der Wand (R10: "Klammer auf dem Plateau
  auseinander"); Newton auf dem ganzen Gitter hat diese Grenze nicht.
- Gitter (MESS-3A R7, "wie R10"): h = 0,02 und h = 0,01; wie im R10-Befehl "kanal" ist das Rechengitter das
  Profilgitter mit Schritt hp = h/2 (0,01 bzw. 0,005). K2 prueft damit auch die R10-Zahl E = 0,706247 (h = 0,02).
- Familie (MESS-3A R6): kappa in {-0,017; -0,05; -0,10; -0,19; -0,20}, Omega^2 = 1 + kappa + f |kappa|,
  f in {0,1; 0,2; 0,35; 0,5; 0,7; 0,85; 0,95} (35 Profile).
- R_max = max(3 R_w, R_w + 25/sqrt(1 - Omega^2)); Mitglieder mit R_max > 3000 werden ausgeschlossen und benannt.
  Vorab-Abschaetzung [ES]: groesster Wert bei kappa = -0,017, f = 0,95: R_w + 25/0,029 ~ R_w + 858, also kein Ausschluss
  erwartet. Massgeblich ist die Zahl aus dem Lauf.
- Suche (MESS-3A R4 "Raster in rho, dann Bisektion"): Sturm-Zaehlung der negativen Eigenwerte von H(rho) auf 3000
  rho-Punkten in (1e-6, 1 + Omega), zwei Verfeinerungen mit je 30 Teilpunkten (Aufloesung ~2,5e-7). Jede Aenderung der
  Zahl ist eine Nullstelle lambda_k(rho_c) = 0 mit k = min(Zahl links, Zahl rechts). Eigenvektor mit
  eigh_tridiagonal. Gleichzeitige Nullstellen in Gegenrichtung innerhalb einer Feinzelle wuerden sich aufheben
  (Grenze, benannt).
- Lesepunkt 1 (HERLEITUNG 4.1), **Zusatz der Code-Agenten, getrennt markiert**: R4 sagt "fuer die untersten k <= 5".
  Massgeblich (bindende Auswertung) ist die Menge **R4 = alle Nullstellen mit k <= 5**. Zusaetzlich berichtet, nicht
  entscheidend: die Menge **alle** (jedes k). Weicht der Ausgang der Menge "alle" ab, wird das als Befund gemeldet.
- Definitionen (vorab festgelegt):
  - R_w: erster Radius mit Theta = Theta(0)/2; delta = r_10 - r_90 mit sin^2 Theta = 0,1 bzw. 0,9 sin^2 Theta(0).
  - F_w = sum y^2 ueber |r - R_w| < 2 delta / sum y^2 (Mass dr fuer y = r w). Wandzustand: F_w > 0,5.
  - Eingebettet: 1 - Omega < rho_c < 1 + Omega.
  - Tiefster Zustand (Regel 8): Nullstelle mit dem kleinsten rho_c der Menge (erste Nullstelle bei steigendem rho; so
    liest MESS-3A K "Volumenzustaende beginnen bei rho ~ sqrt(|kappa|/2)"). Tiefster Wandzustand: kleinstes rho_c mit
    F_w > 0,5.
  - Regel 8 verworfen, wenn bei keinem Mitglied auf keiner Stufe der tiefste Zustand eingebettet ist; berichtet wird
    auch, bei welchen Mitgliedern er auf beiden Stufen eingebettet ist.
  - Bindende Regel: "weiter", wenn ein Mitglied auf beiden Stufen je einen eingebetteten Wandzustand hat und zwei davon
    auf 1e-3 in rho uebereinstimmen; "verworfen", wenn kein gueltiges Mitglied auf irgendeiner Stufe einen hat; sonst
    "unentschieden (Regel-Luecke)", benannt. "Nicht auswertbar", wenn K0, K1, K2, K3 oder K4 verfehlt.
- Lesepunkt 2 (HERLEITUNG 4.2), **Zusatz, nicht entscheidend**: je Zustand die Wandueberhoehung eta = F_w/L_w mit
  L_w = (R_w + 2 delta - max(0, R_w - 2 delta))/(R_w + 2 delta) (Anteil des Fensters am Bereich [0, R_w + 2 delta]),
  dazu F_innen, F_aussen, Beteiligungslaenge P = (sum y^2)^2/sum y^4 * hp, r_spitze. Ein gleichmaessig verteilter
  Innenraumzustand hat eta ~ 1; ein an der Wand sitzender eta >> 1 (hoechstens 1/L_w). Gezaehlt wird "eingebettet,
  Wand, eta > 2".

## 4 Kontrollen (vorab, Kriterien)

- K0 (kappa = 0, Omega^2 = 0,90 / 0,95 / 0,99): Schiessen meldet "keine Loesung" (kein Ueberschuss in Runde 0) fuer
  alle drei.
- K1 (Theta = 0, Omega aus kappa = -0,10, f = 0,5; R = 500): keine Nullstelle in (0, 1 + Omega); lambda_0(rho) gleich
  4/hp^2 sin^2(pi/(2J)) + 1 - (rho - Omega)^2 auf 1e-8 bei rho = 0,5 / 1,0 / 1,9.
- K2 (KG-Q-Ball, nls2-Profil beta = 0,5, omega^2 = 0,7977; A = dp - omega^2, B = 2 omega, c2 = 1, Suche in
  (0, 1 + omega), eingebettet fuer 1 - omega < rho_c < 1 + omega): eine Nullstelle mit |rho_c - (omega + sqrt(0,706247))|
  < 0,01 (Ziel 1,7335), eingebettet und F_w > 0,5, auf beiden Stufen. Zusatz: (rho_c - omega)^2 gegen R10 0,706247.
- K3 (je gueltiges Mitglied, beide Stufen): max |(-Lap + V_v) sin Theta| / max|sin Theta| < 1e-6 und
  max |(-Lap_{l=1} + V_u) Theta'| / max|Theta'| < 1e-6, Laplace mit Differenzen 4. Ordnung, Bereich ohne die drei
  Randpunkte je Seite.
- K4 (kubisch-quintisches NLS 3D, nls2-Profil, Omega = 0,16 und 0,17; A = 2 D, B = 1, c2 = 0, Spektralparameter nu,
  Suche in (-Omega, 1,0), eingebettet fuer nu_c > Omega): keine Nullstelle, die eingebettet ist und F_w > 0,5 hat, auf
  beiden Stufen. Abweichung vom AFM-Suchbereich (0, ...) benannt: Der R10-Wandzustand liegt bei nu_c = -2 E_0 ~ -0,04 und
  waere sonst gar nicht im Bereich; so prueft K4, dass der Codepfad einen echten Wandzustand findet und als nicht
  eingebettet meldet. Zusatz: -nu_c/2 gegen R10 E_0 = +0,021274 (0,16) bzw. +0,0236 (0,17).

## 5 Aufrufe

- Rauchtest lokal (ungueltig, Zahlen zaehlen nicht): `timeout 120 nice -n 19 env OMP_NUM_THREADS=1
  OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 CUDA_VISIBLE_DEVICES= python3 afm_kanal.py familie --kappa -0.2 --f 0.1,0.95
  --h 0.04 --m1 600 --aus lauf-lokal --name rauch-fam` und ein Kontrollen-Rauchtest mit h = 0,04 (Ausgaben in
  lauf-lokal/).
- .69, Ordner /home/fmh/fmhc-physics-remote/runde12-afm-kanal1/ (Kopien afm_kanal.py, nls2.py), je Aufruf
  `bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <name> afm_kanal.py <kommando> ... --aus
  /home/fmh/fmhc-physics-remote/runde12-afm-kanal1/aus --name <name>`, Log nach .../runde12-afm-kanal1/log/<name>.log
  (absoluter Pfad). Spuren cpu, cpu2, cpu3, cpu4, cpu6; je Spur nur ein Aufruf zugleich (keine Wartezeit am Lock).
  - fam-k<kappa>-h0.02 und fam-k<kappa>-h0.01 je kappa (10 Aufrufe, 7 Mitglieder je Aufruf; bei Bedarf geteilt in
    f-Teilmengen, Name mit Zusatz -a/-b).
  - kon-h0.02, kon-h0.01 (K0, K1, K2, K4).
  - auswertung (liest aus/fam-*.json und aus/kon-*.json, wendet die Regel aus Abschnitt 3 an).
- Jeder Aufruf hoechstens 10 min Wanduhr (RuntimeMaxSec 600 in kleintest.sh); Ergebnisse nach lauf-69/ kopiert.

## 6 Nachtrag nach dem Rauchtest (vor dem Einfrieren, Kriterien unveraendert)

- Rauchtests lokal 17:30:58 bis 17:31:44 (date), h = 0,04, M1 = 600, Zahlen ungueltig: lauf-lokal/rauch-fam.*,
  rauch-kon.*. Code laeuft (4,3 s und 3,9 s). Gesehen, ohne Folgen fuer Regel oder Kriterien:
  - K3-Translationsresiduum beim Dickwandmitglied (kappa = -0,2, f = 0,95) 1,4e-5 auf dem Rauchgitter hp = 0,02. Bei
    h^4-Skalierung erwartet ~9e-7 fuer h = 0,02 (knapp) und ~5e-8 fuer h = 0,01. Kriterium 1e-6 bleibt; verfehlt es
    ein Mitglied, ist der Lauf nach der Regel "nicht auswertbar". Ergaenzt: Ort des groessten Residuums (Diagnose).
  - Menge R4 (k <= 5) und Menge "alle" unterscheiden sich schon im Rauchtest beim Duennwandmitglied. Die Festlegung
    "R4 massgeblich, alle als Zusatz" stand vorher (17:29:58) und bleibt.
- afm_kanal.py danach nur um die Residuums-Orte ergaenzt; sha256 der Laufversion in ERGEBNIS.md.
