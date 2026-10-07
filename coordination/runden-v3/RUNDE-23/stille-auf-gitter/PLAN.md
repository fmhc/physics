# STILLE-AUF-GITTER: Plan (Code-Agent, Runde 23, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-02 22:35:19 CEST (date).
- Plan geschrieben ab 22:55:05 CEST (date), nach dem Rauchlauf, vor jeder echten Rechnung.
- Karte: KARTE.md (unveraendert). Vorhersagen SG0 bis SG3 und ihre Bedeutung gelten wie dort; dieser Plan legt nur
  Laeufe, Verfahren und die mechanische Auswertung fest.
- Code: code/stille_gitter.py, sha256 ab42bce160910308d05697410a70df0571fe0e05863e9081b4fd3f36be7ba1d6 (lokal = .69).
- .69: /home/fmh/fmhc-physics-remote/runde23-stille-auf-gitter/ (Code, lauf/). Lokal nur Lesen, Schreiben, ssh, jq.
- Zeitbox 120 min ab 22:35 (bis etwa 00:35 CEST).

## 1. Schreibtisch: Pruefung des Karten-Arguments

Nachgerechnet (Symbol fuer e^{i(kx x + ky y)}, a = kx h, b = ky h):

- **Stern A:** (1/h^2)(2 cos a + 2 cos b - 4) = -k^2 + (h^2/12)(kx^4 + ky^4) + O(h^4).
  - kx^4 + ky^4 = k^4 (3 + cos 4theta)/4. Anisotroper Anteil (h^2/48) k^4 cos 4theta. **Stimmt.**
- **Stern B:** (1/(6h^2)) [8 cos a + 8 cos b + 4 cos a cos b - 20]
  = -k^2 + (h^2/12) k^4 + h^4 k^6 (-1/288 + cos 4theta/1440) + O(h^6).
  - Der h^2-Term ist (h^2/12) Laplace^2, also isotrop. Der erste anisotrope Term ist (h^4 k^6/1440) cos 4theta.
  - Das ist die Karten-Angabe "(5/2 - (1/2) cos 4theta)" mal -h^4 k^6/720. **Stimmt.**
  - Nuetzliche Zerlegung (fuer die PML): Stern B = D_xx + D_yy + (h^2/6) D_xx D_yy mit D_xx = delta_x^2/h^2.
- **Kopplungsargument:** Die A1-Darstellung von C4v enthaelt alle Kanaele cos(4 m theta), m = 0, 1, 2, ... In 2D sind
  oberhalb der Schwelle alle offen.
  - Ein reeller Parameter (omega^2) kann nur eine Abstrahlamplitude (l = 0) auf null stellen. Die l = 4-Amplitude ist
    erster Ordnung in der Anisotropie, also Gamma_min proportional zum Quadrat: h^4 (A) und h^8 (B). **Stimmt in
    fuehrender Ordnung.**
  - Die Fluesse der Kanaele addieren sich ohne Interferenz. Am Minimum bleibt l = 0 nur in hoeherer Ordnung uebrig.
- **Luecken und Ergaenzungen (Vorhersagen bleiben unveraendert):**
  1. **Zwei Quellen der Ordnung h^2 (A) bzw. h^4 (B):** der Stern, der auf die Mode wirkt, und die anisotrope Verformung
     des Gitter-Q-Balls selbst (Wandradius Achse gegen Diagonale). Beide skalieren gleich, der Exponent aendert sich
     nicht. Der Vorfaktor ist offen.
  2. **Fernfeld-Zerlegung auf dem Gitter:** Die Gitter-Dispersion ist anisotrop.
     - Bei A gilt dk(theta) = (K^3 h^2/96) cos 4theta mit K = 2,05, also 0,090 h^2 cos 4theta.
     - Eine auslaufende l = 0-Welle mischt darum auf dem Weg vom Ball (r ~ 12,5) zum Messkreis (r = 20) l = 4 bei: Phase
       ~0,17 rad bei h = 0,5, Mischanteil ~J1^2 ~ 0,7 %.
     - Der "cos 4theta-Anteil" ist auf dem Gitter nur bis auf diese Groesse definiert. Fuer SG3 ist das klein.
  3. **Form von Gamma(omega^2):** Gamma ist zwischen zwei Sprossen grob Gamma_max sin^2(pi (x - x_r)/Delta), mit
     Delta ~ 4e-3 und Gamma_max ~ 7e-3 (Rauchlauf: Saettigung schon bei +-1e-3).
     - Die Parabel Gamma_min + a (x - x_r)^2 gilt nur nahe am Minimum.
     - Ein Fit ueber +-1e-4 verzerrt Gamma_min um ~1e-7, darum endet die Suche mit einem engen Fenster (Abschnitt 3).
  4. **Schaetzung B gegen A:** Das Amplitudenverhaeltnis ist ~h^2 K^2/30, also Gamma_B/Gamma_A ~ 0,02 h^4 (~1,6e-4 bei
     h = 0,3). Die Bedingung "B < A/30" in SG2 ist danach grosszuegig.
  5. **Der Q-Ball sitzt auf einem Gitterpunkt** (A1 um den Ursprung). Ein bindungszentrierter Ball ist eine andere
     Gitterlage und wird nicht getestet.

## 2. Rauchlauf (vor dem Einfrieren; h = 0,45, 0,35, 0,22, kommen in keinem echten Lauf vor)

- R1 (20:49 bis 20:50 UTC, lauf/rauch/; Code-Fassung 6a2348c9...):
  - nur Stufe 1, A und B bei h = 0,45 und 0,35
  - Befund: Im rho < 0 (abklingend), l0-Anteil 0,98 bis 1,00, Rechenzeit 1 bis 4 s je Punkt
  - Die Sprosse liegt deutlich hoeher: A ~ +3,8e-3 h^2, B ~ +5,0e-3 h^2.
  - **Fehler gefunden:** Die Nachverfeinerung nutzte die LU bei sigma fuer die inverse Iteration. Beim quadratischen
    Problem fuehrt das auf den falschen Vektor (Residuum ~1e-3). Behoben: Die LU wird jetzt beim komplexen
    Arnoldi-Wert gebildet; Residuen jetzt ~5e-15.
  - **Verfahren geaendert:** Ein breites Parabelfenster (+-9e-4) ist wegen der sin^2-Form unbrauchbar (Luecke 3). Jetzt
    Zoom: Minimum der Stichprobe, 3-Punkt-Scheitel, dann enge Fenster.
- R2 (20:53 bis ~20:59 UTC, lauf/rauch2/; Code ab42bce1..., die eingefrorene Fassung): volle Suche A und B bei h = 0,45,
  dazu A und B bei h = 0,22.
  - A 0,45: Gamma_min = 1,298e-4 bei 0,5300311. Direkt, Doppelrechnung und P2 stimmen auf 2e-9. F4-Anteil 0,879.
  - B 0,45: Gamma_min = 1,282e-7 bei 0,5302998. P2 weicht um 3e-12 ab. F4-Anteil 1,000.
  - A 0,22: ~9 s je Punkt; B 0,22: ~13 s je Punkt.
  - **Offengelegt:** Diese Rauchwerte zeigen schon die Groessenordnung. Die Vorhersagen der Karte standen vorher fest
    und werden nicht angepasst.
- Startwerte der echten Laeufe aus R1/R2:
  - A: x0 = 0,5292654 + 3,78e-3 h^2, rho0 = 1,556457 + 5,5e-3 h^2
  - B: x0 = 0,5292654 + 5,1e-3 h^2, rho0 = 1,556457 + 7,3e-3 h^2

## 3. Verfahren (Code stille_gitter.py, eingefroren)

- **Gitter:** x_i = i h, |i| <= M, M = ceil(40/h), Dirichlet ausserhalb.
  - A1-Achtelgebiet 0 <= y <= x; Operator R L P (voller Kronecker-Operator, eingeschraenkt auf symmetrische
    Funktionen; exakt, weil L mit C4v vertauscht).
- **Q-Ball:** Newton auf dem Gitter mit dem ungestreckten Stern.
  - Start: radiales Kontinuumsprofil (dr = 0,02); danach Warmstart vom naechsten omega^2.
  - Residuum max|F| < 1e-11 oder Rundungsboden.
- **Linearisierung:**
  - u (omega - rho, geschlossen) und v (omega + rho, offen), Potentiale V1 = U' + U'' f^2 und W = U'' f^2, am Gitterpunkt.
  - **PML P1:** s(x) = 1 + 1,5 i ((|x| - 24)/16)^2 fuer 24 < |x| <= 40, gleich in y. Im Stern B wird jeder D_xx gestreckt,
    auch im Mischterm.
  - **PML P2 (Probe):** Dicke 22 (Rand bei 46), Staerke 3,0, Exponent 3.
- **Eigenwert:**
  - Shift-Invert-Arnoldi (eigs, tol 1e-13) auf der linearen Einbettung [[0, I], [K, C]] mit sigma = Re rho_vorher;
    erster Punkt nev = 6, danach nev = 3.
  - Auswahl: l0-Anteil (u und v auf Kreisen 0,4 R und 0,7 R) >= 0,5, dann naechster an der Vorhersage.
  - Danach zweiseitiges Rayleigh-Funktional mit Rechts- und Linksvektor aus der LU beim komplexen Arnoldi-Wert.
- **Gamma = -Im rho** (Konvention RUNDE-12: Breite = |Im rho|, ohne Faktor 2).
- **Suche je (Stern, h)**, x = omega^2:
  - S1: 5 Punkte im Abstand 1e-4 um x0. Liegt das Minimum am Rand, wird um je 1e-4 erweitert (hoechstens 6-mal).
    Scheitel x1 der Parabel durch die 3 Punkte um das Stichprobenminimum.
  - S2: 5 Punkte im Abstand 4e-5 um x1, Parabel-Fit (kleinste Quadrate) -> x_r2, Gamma_min2, a2.
  - S3: d3 = 1,2 sqrt(max(Gamma_min2, 0)/a2), begrenzt auf [1e-7; 2e-5]. 5 Punkte im Abstand d3 um x_r2, Fit.
    Liegt der Scheitel ausserhalb des Fensters, folgt eine zweite S3-Runde um den neuen Scheitel.
- **Ergebnis je (Stern, h):** Fit der letzten S3-Runde.
  - omega_r^2(h) = Scheitel x*, Gamma_min(h) = Fit-Minimum, a = Kruemmung, sigma aus den Fit-Residuen.
  - MIN: direkte Rechnung bei x*.
- **Doppelrechnung (DOPPEL):** bei x* mit sigma um +2e-3 verschoben (anderer Krylov-Weg).
- **PML-Probe (P2):** bei x* auf dem P2-Gitter, Q-Ball neu per Newton.
- **Rechenboden:** Boden(h) = |Gamma_MIN - Gamma_DOPPEL| + |Gamma_MIN - Gamma_P2|.
  - **Ueber dem Rechenboden** heisst Gamma_min(Fit) > 0 und Gamma_min >= 10 Boden.
  - **Unter dem Rechenboden** (SG2) heisst nicht ueber dem Rechenboden.
- **Fernfeld (SG3):** offener Kanal v am MIN-Punkt, auf den Kreisen r_c1 = 20 (gewertet) und r_c2 = 22,5 (Kontrolle).
  - 512 Winkel, kubische Spline-Interpolation; Koeffizienten a_j von cos(4 j theta), j = 0 bis 6.
  - Fluss F_j = N_j r Im(conj(a_j) da_j/dr), N_0 = 2 pi, N_j = pi; da/dr zentral mit dr = 0,25.
  - Anteil l = 4: F_1 / Summe F_j.

## 4. Laeufe (nur .69, kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4, cpu6; je Aufruf --budget 560)

Gemeinsam: `stille_gitter.py --modus scan --n1 5 --d1 1e-4 --d2 4e-5 --d3max 2e-5 --d3min 1e-7`, PML P1 und P2 wie oben.

| Lauf | Stern | h | x0 | rho0 | Spur |
|---|---|---|---|---|---|
| A050 | A | 0,5 | 0,5302104 | 1,557832 | cpu2 |
| A040 | A | 0,4 | 0,5298702 | 1,557337 | cpu6 |
| A030 | A | 0,3 | 0,5296056 | 1,556952 | cpu6 |
| A025 | A | 0,25 | 0,5295017 | 1,556801 | cpu4 |
| A020 | A | 0,2 | 0,5294166 | 1,556677 | cpu2 |
| B050 | B | 0,5 | 0,5305404 | 1,558282 | cpu6 |
| B040 | B | 0,4 | 0,5300814 | 1,557625 | cpu3 |
| B030 | B | 0,3 | 0,5297244 | 1,557114 | cpu4 |
| B025 | B | 0,25 | 0,5295842 | 1,556913 | cpu3 |
| B020 | B | 0,2 | 0,5294694 | 1,556749 | cpu |

- **h = 0,15 (optional, nur wenn nach allen zehn Laeufen noch mindestens 30 min Zeitbox bleiben):**
  - A015 mit x0 = 0,5293505, rho0 = 1,556581, `--n1 3 --ohne-p2`
  - B015 mit x0 = 0,5293802, rho0 = 1,556621, `--n1 3 --ohne-p2`
  - P2 jeweils getrennt im Modus punkt bei x* mit `--lpml 22 --sig0 3 --pexp 3`. Fehlt DOPPEL aus Zeitgruenden, folgt
    eine getrennte Rechnung im Modus punkt mit `--punkt-sigoff 2e-3`.
  - Zaehlt nur, wenn Boden vollstaendig ist.
- Bricht ein Lauf ab (Zeit oder Fehler), wird er einmal mit unveraenderten Argumenten wiederholt und das offen vermerkt.
  Fehlt dann noch etwas, bleibt der Punkt offen.

## 5. Mechanische Auswertung (Skript code/auswertung.py, nach diesem Plan; laeuft auf der .69)

- **SG0** (je Stern, alle h mit S3-Fit):
  - Exponent q aus dem nichtlinearen Fit omega_r^2(h) = w0 + c h^q ueber alle h; Unsicherheit aus der Kovarianz.
  - Extrapolation w0' aus dem linearen Fit omega_r^2 = w0' + c' h^2 ueber h <= 0,3 (0,3; 0,25; 0,2, dazu 0,15 falls
    vorhanden).
  - **Eingetroffen**, wenn fuer beide Sterne |q - 2| <= 0,4 und |w0' - 0,529266| <= 3e-5.
- **SG1** (Stern A):
  - p = Steigung der Ausgleichsgeraden log Gamma_min gegen log h ueber alle h ueber dem Rechenboden; Unsicherheit =
    Standardfehler der Steigung.
  - **Eingetroffen**, wenn mindestens 3 h ueber dem Rechenboden liegen und 3,2 <= p <= 4,8 (Punktschaetzer).
- **SG2** (Stern B):
  - (a) mindestens 3 h ueber dem Rechenboden und 6 <= p_B <= 10, oder (b) Gamma_min fuer alle h <= 0,3 unter dem
    Rechenboden.
  - Und (c): Gamma_min,B(0,3) < Gamma_min,A(0,3)/30. Fuer B unter dem Rechenboden wird dort max(Gamma_min,B, 10 Boden_B)
    eingesetzt.
  - **Eingetroffen**, wenn ((a) oder (b)) und (c).
- **SG3** (Stern A):
  - F4-Anteil am MIN-Punkt auf r_c1 = 20, fuer jedes h ueber dem Rechenboden.
  - **Eingetroffen**, wenn er bei allen diesen h >= 0,80 ist. Sonst nicht eingetroffen, mit Angabe der h.
- **K0:** w0' gegen 0,529266 (wie SG0). Dazu berichtet: Kruemmung a(h) gegen 57^2 = 3249, Re rho(x*) gegen 1,556457
  und der Rechenboden je h.
- Zusaetzlich berichtet, ohne Wertung:
  - oertliche Exponenten zwischen Nachbar-h
  - Wandradius Achse gegen Diagonale
  - F0- und F8-Anteile
  - Kontrollkreis r_c2

## 6. Grenzen

- Keine Journaleintraege, keine Peerbus-Nachrichten, keine Aenderungen an Karten oder anderen Runden.
- Code und Plan nach dem Einfrieren unveraendert. Abweichungen werden offen mit Grund und Zeit notiert.
- Prozesse nur per PID, Skripte nie in place ueberschreiben, Zeiten per date.
