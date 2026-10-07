# PHASE-3D: Plan (Runde 26, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 04:35:02 CEST (date).
- Plan geschrieben ab 04:57:30 CEST (date), nach den Rauchlaeufen (Abschnitt 8), vor jedem echten Lauf. Kein Profil
  einer gewerteten Sprosse ist bisher gerechnet. Zeitbox 90 min (bis 06:05:02 CEST).
- Ordner: lokal coordination/runden-v3/RUNDE-26/phase-3d/ (code/, lauf-69/); .69:
  /home/fmh/fmhc-physics-remote/runde26-phase-3d/ (phase_3d.py, phase_wand.py, bic2_3d_praez.py, start*.sh, lauf/, rauch/).
- Markierungen: [K] Wortlaut der KARTE, [L] Vorgabe der Leitung im Auftrag, [A] Festlegung des Code-Agenten,
  [H] Hypothese.

## 1. Karte (bindend, unveraendert) [K]

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| P3D-1 | beta = 1/2: Fuer die drei Sprossen mit kleinstem eps (n = 13 bis 15) gilt abs(Delta_n) < 0,03 | 55 % |
| P3D-2 | beta = 1/2: Der lineare Ausgleich ueber n = 8 bis 15 hat abs(b) < 0,02, und abs(Delta_n) faellt mit eps | 50 % |
| P3D-3 | beta = 1: Der lineare Ausgleich ueber die acht Sprossen hat abs(b) < 0,03 | 45 % |

- Bedeutung (vorab, Karte):
  - P3D-1 und P3D-2 treffen ein: Die ebene Wandphase bestimmt theta_inf der 3D-Leiter ohne Eichung. Zusammen mit
    c_inf = rho_z - omega_min ist die Duennwand-Beschreibung des Papiers im Grenzfall vollstaendig berechnet [H].
  - P3D-1 trifft nicht ein, aber abs(Delta_n) faellt gegen 0: Die Annaeherung ist langsamer. Beschreiben.
  - abs(Delta_n) strebt gegen einen festen anderen Wert: Es gibt einen Konventions- oder Kruemmungsversatz. Beschreiben,
    nicht nachtraeglich einrechnen.

## 2. Groessen und Konventionen [A]

### 2.1 3D-Profil (l = 0)

- M1: f'' + (2/r) f' = F(f) = (1 - omega^2) f - 2 f^3 + 3 beta f^5, f'(0) = 0, f -> 0; S = f^2.
- Schiessen in u = t - f wie bic2.profil (RUNDE-13):
  - t = sqrt(S_top), S_top = groessere Wurzel von U'(S) = omega^2, also S_top = (2 + sqrt(4 - 12 beta (1 - omega^2)))/(6 beta).
  - u'' + (2/r) u' = G(u) = -F(t - u) = c1 u - c2 u^2 + c3 u^3 - c4 u^4 + c5 u^5 (Taylor-Koeffizienten exakt wie bic2).
  - Start u(0) = e^(-s); Reihe u = u0 + a r^2 + b r^4, a = G(u0)/6, b = G'(u0) a/20.
  - Ueberschuss: u > t (f < 0). Unterschuss: u' < 0 (f' > 0). Bisektion in s von [-ln(t - 1e-3), 150] (wie bic2) bis
    zur Klammerbreite 1e-13 max(1, s).
- R (Halbhoehenradius) [K]: S(R) = S_c/2 mit S_c = 1/(2 beta), also u(R) = t - sqrt(S_c/2). Gemeldet wird das Mittel
  der beiden letzten Klammerbahnen; ihr Abstand ist die Aufloesung der Bisektion.
- Die Plateauhoehe im 3D-Profil ist S(0) ~ S_top > S_c. Als Halbhoehe gilt trotzdem S_c/2, wie in 1D [L].

### 2.2 Verfahren fuer R

| Name | Rolle | Inhalt |
|---|---|---|
| rk4:0.005 | Hauptrechnung | eigenes klassisches RK4, fester Schritt h = 0,005, R per kubischer Hermite-Interpolation (u, u') |
| rk4:0.01 | Gitterprobe (Regel) | dasselbe mit h = 0,01 |
| bic2:0.01 | Fremdcode-Probe (Regel) | bic2_3d_praez.profil aus RUNDE-13 (unveraendert, sha256 ba86ae6a...), Profilschritt 0,01 = Profil der Leiterstufe h = 0,02; R per Hermite in (f, f') |
| dop853:1e-12 | Integrator-Probe (berichtet) | scipy DOP853, rtol 1e-12; R als Ereignis auf der dichten Ausgabe |
| dop853:1e-10 | berichtet | dasselbe mit rtol 1e-10 |

- DOP853 in zwei Abschnitten: bis u = 1e-3 mit atol = 1e-2 rtol u0, danach atol = 1e-15 (Grund: Abschnitt 8).
- DOP853 startet mit der engen Klammer s_rk4 +- 1e-6 max(1, s_rk4); ist sie ungueltig, mit der vollen Klammer.
- Empfindlichkeit dR/d(omega^2): zentrale Differenz mit rk4:0.005 bei omega^2 +- 1e-6.

### 2.3 Hauptform [K]

- k_in und phi bei rho_z aus PHASE-WAND, unveraendert (lauf-69/phase-b05.json sha256 3d4e1083..., phase-b1.json
  sha256 32bedc3d...; Kopien in lauf/pw-phase-b05.json und lauf/pw-phase-b1.json):
  - beta = 1/2: k_in = 1,9233245912954144, phi = 2,5538882521462405
  - beta = 1: k_in und phi aus phase-b1.json (2,39943212... und 2,26069755...)
- Herleitung (l = 0, u = r psi): Die regulaere Innenloesung ist e1.u = A sin(k r). In der Tiefe d = R - r ist das
  A [sin(kR) cos(kd) - cos(kR) sin(kd)]. Die Wand verlangt e1.u = R_amp cos(kd + phi) (Phasenkonvention PHASE-WAND,
  Abschnitt 2.3 dort). Gleichsetzen gibt tan(kR) = cot(phi), also k R + phi = (n' + 1/2) pi. Das ist die ungerade
  1D-Bedingung cos(k x_w + phi) = 0.
- x = [k_in(rho_z) R + phi]/pi - 1/2, Delta = x - ceil(x - 1/2) in (-1/2, 1/2], n' = ceil(x - 1/2).

### 2.4 Nebenform [K, nur berichtet]

- k_in(rho_n) und phi(rho_n) der ebenen Wand bei omega_min (phase_wand.py unveraendert: MB, innen_moden, phase_satz),
  wo rho_n bekannt ist: beta = 1/2 bei n = 1, 2, 6 bis 10; beta = 1 bei allen acht.
- phi(rho_n) bei d = 20 sqrt(beta) wie PHASE-WAND, Streuung ueber d = 16, 20, 24 sqrt(beta) berichtet.
- Bei rho != rho_z hat die ebene Loesung innen die wachsende e2-Mode; ueber den Wandschwanz speist sie e1, die Phase
  haengt dann von der Tiefe ab (Rauchlauf bei beta = 0,6: Streuung 1e-3 bis 2e-3 rad bei d >= 16 sqrt(beta)). Die
  Nebenform ist darum nur auf etwa 1e-3 rad bestimmt.

### 2.5 Zusatzform [A, nicht in der Karte, nur berichtet, ohne Einfluss auf Urteile]

- k_lok = k(omega_n^2, rho_n, S0) aus der Innenmatrix am tatsaechlichen 3D-Plateau:
  k^2 = omega^2 + rho^2 - D + sqrt(4 omega^2 rho^2 + C^2), D = 1 - 4 S0 + 9 beta S0^2, C = -2 S0 + 6 beta S0^2,
  S0 = S(0) der Hauptrechnung. phi = phi(rho_z). Nur wo rho_n bekannt ist.
- Delta_zusatz = frac([k_lok R + phi]/pi - 1/2). Begruendung: Abschnitt 7.

### 2.6 Sprossen (Eingabedateien, nicht auf der Befehlszeile)

- lauf/sprossen-b05.json: n = 1 bis 15 [K]. omega^2 aus tab:ladder (n = 3 bis 6, 11 bis 15, wie gedruckt), n = 1 und 2
  aus den Einschliessungen C0, C1 (PROOF.tex, auf double gerundet), n = 7 bis 10 aus RUNDE-13 n7..n10-h002
  (ziel_wechsel.x_stern). rho_n aus C0, C1, R13-K2 (n = 6) und R13 n7..n10.
  - n = 6: tab:ladder 0,569360 (Karte), R13-K2 genau 0,56935983; Unterschied 1,7e-7.
- lauf/sprossen-b1.json: die acht Sprossen aus RUNDE-24 auswertung.json (x, rho; sha256 63c07a30...), id = k (eps
  aufsteigend).

## 3. Kommandos (code/phase_3d.py)

- profile: R je Sprosse mit den Verfahren der Konfiguration, dazu dR/d(omega^2).
- phase: ebene Wand bei omega_min fuer rho_z und die bekannten rho_n (Nebenform); Kontrolle phi(rho_z) gegen PHASE-WAND.
- auswertung: Delta je Sprosse (Haupt-, Neben-, Zusatzform), K-Profil, Regeln P3D-1 bis P3D-3, Berichtsausgleiche.
- Urteile beider beta zusammengefasst mit jq in lauf-69/urteile.json.

## 4. Regeln (mechanisch) [A]

- **K-Profil** (je Sprosse):
  - Aufloesung der Bisektion (Hauptrechnung) <= 1e-9
  - abs(R(rk4:0.01) - R(rk4:0.005)) <= 1e-5
  - abs(R(bic2:0.01) - R(rk4:0.005)) <= 1e-5
  - 1e-5 in R sind hoechstens 8e-6 in Delta.
- Faellt K-Profil bei einer Sprosse aus, die eine Regel braucht, ist diese Vorhersage nicht auswertbar
  (= nicht eingetroffen). Das gilt auch, wenn eine Sprosse fehlt.
- **P3D-1:** abs(Delta_n) < 0,03 fuer n = 13, 14 und 15 (jede).
- **P3D-2:** Linearer Ausgleich (kleinste Quadrate, ungewichtet) Delta = a eps + b ueber n = 8 bis 15. Eingetroffen,
  wenn abs(b) < 0,02 **und** abs(Delta_n) streng faellt, wenn eps faellt: abs(Delta_(n+1)) < abs(Delta_n) fuer
  n = 8 bis 14.
- **P3D-3:** derselbe Ausgleich ueber k = 1 bis 8 bei beta = 1, abs(b) < 0,03.
- **Auslegungen [A]:**
  - eps = omega^2 - omega_min^2 (omega_min^2 = 1/2 bzw. 3/4); b ist der Achsenabschnitt bei eps = 0.
  - Abwicklung vor dem Ausgleich: Jedes Delta wird um eine ganze Zahl in (D_ref - 1/2, D_ref + 1/2] gelegt, D_ref =
    Delta der Sprosse mit kleinstem eps der Menge. b wird danach in (-1/2, 1/2] gelegt (b_gewickelt) und geprueft. Ohne
    Sprung ueber +-1/2 aendert das nichts; ob abgewickelt wurde, steht in der Ausgabe.
  - "faellt mit eps" streng wie oben. Die milde Lesart (Spearman-Rang zwischen abs(Delta) und eps > 0) wird nur berichtet.
  - abs(Delta_n) in P3D-1 und in der Monotonie ist das Delta der Karte in (-1/2, 1/2] (nicht abgewickelt).

## 5. Kontrollen und Berichte (keine Regel)

- R - R_tw mit R_tw = 1/(2 sqrt(beta) eps); S0 - S_c - eps (3D-Plateau, erwartet ~ 0 in erster Ordnung).
- DOP853 (1e-12, 1e-10) gegen die Hauptrechnung.
- dDelta/d(omega^2) = k_in dR/d(omega^2)/pi je Sprosse; daraus die Wirkung der gedruckten Rundung von omega^2.
- phi(rho_z) aus phase gegen PHASE-WAND (gleicher Code, gleiche Tiefe: erwartet 0); k_lok(omega_min, rho_z, S_c) - k_in.
- Berichtsausgleiche: Hauptform n = 6 bis 10, 11 bis 15, 6 bis 15 (beta = 1/2) und k = 1 bis 4 (beta = 1); Neben- und
  Zusatzform ueber n = 6 bis 10 bzw. k = 1 bis 8.

## 6. Rahmen

- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4, cpu6 (je 1 Kern, <= 600 s, 4 GB).
- Nach dem Einfrieren keine Aenderung an Plan, Code, Konfigurationen und Startskripten. Abweichungen offen mit Grund und
  Zeit im ERGEBNIS.
- Faellt ein Aufruf aus (rc != 0, 600 s): berichten; ein Nachlauf nur als offen benannte Abweichung.

## 7. Schreibtisch des Code-Agenten [H], vor den Laeufen

- In 1D sind die Korrekturen zur Formel klein, weil x_w ~ ln(1/eps): Eine Aenderung der Innenwellenzahl um O(eps) oder
  O(sqrt(eps)) gibt mal x_w nur O(sqrt(eps) ln(1/eps)).
- In 3D ist R ~ 1/(2 sqrt(beta) eps). Eine Aenderung der Innenwellenzahl um O(eps) gibt mal R eine Phase der Ordnung 1.
- Das 3D-Plateau liegt bei S_top = S_c + eps + O(eps^2), nicht bei S_c. Die Sprosse liegt bei omega_n^2 = omega_min^2 +
  eps und rho_n = rho_z + c eps mit c ~ 1,1 (beta = 1/2) bzw. ~ 0,9 (beta = 1).
- Mit d(k^2) = [dk2/d(omega^2) + dk2/drho c + dk2/dS] eps (Ableitungen am ebenen Punkt):
  - beta = 1/2: 2,955 + 4,331 c - 3,317; mit c = 1,13 sind das 4,53 eps, also dk = 1,18 eps.
  - Mal R_tw = 0,707/eps ergibt das 0,83 rad = 0,27 pi.
  - Schreibtischwert bei n = 10 (k_lok mit S_top): k_lok - k_in = 0,0513, mal R_tw = 16,69 sind 0,86 rad = 0,27 pi.
  - beta = 1: 3,021 + 5,256 c - 4,357; mit c = 0,95 ist dk = 0,76 eps.
  - Mal R_tw = 0,5/eps: 0,38 rad = 0,12 pi; bei k = 1 sind es 0,40 rad = 0,13 pi.
- Erwartung:
  - Die Zusatzform liegt naeher bei 0 (Rest O(eps), z. B. phi(rho_n) - phi(rho_z) ~ 3 c eps rad bei beta = 1/2).
  - Die Hauptform liegt um etwa -0,27 (beta = 1/2) bzw. -0,13 (beta = 1) daneben, wenn die Zusatzform stimmt.
  - Der Versatz bleibt fuer eps -> 0 endlich (c -> c_inf); er ist dann weder Konvention noch Kruemmung, sondern die
    Verschiebung der Innenwellenzahl.
- Eigene Wahrscheinlichkeiten (nicht die der Karte): P3D-1 10 %, P3D-2 10 %, P3D-3 15 %; Zusatzform mit abs(b) < 0,05
  in beiden beta (Bericht) 50 %.
- Wenn die Hauptform doch gegen 0 geht, ist diese Ueberlegung falsch, z. B. weil sich die Verschiebungen von omega, rho
  und Plateau gegen eine Verschiebung von R aufheben, die ich nicht sehe.

## 8. Rauchlaeufe vor diesem Plan (ungueltig fuer jede Wertung; offengelegt)

- .69, 02:48:22 bis 02:57:50 UTC (rauch.sh, rauch2.sh, rauch3.sh, rauch5.sh). beta = 0,6, frei gewaehlte omega^2 = 0,62 und
  0,65 und rho = 1,65 und 1,67; Phase aus der PHASE-WAND-Rauchdatei bei beta = 0,6. Keine gewertete Sprosse, kein beta
  der Karte.
- **Befunde und Aenderungen am Code (alle vor dem Einfrieren):**
  1. DOP853 mit atol = 1e-300 lief sich fest. Die Bahnen nahe der Trennlinie brauchten 5 bis 17 s je Bahn, ein Profil
     ueber 80 s. Ursache [H]: Im Schwanz (u nahe t) ist G(u) eine Differenz von Groessen O(1), das Rundungsrauschen
     ~1e-16 liegt weit ueber atol. Abhilfe: zwei Abschnitte (2.2) und die enge Startklammer. Danach 1,8 s je Profil.
     Die zwei feststeckenden Rauch-Einheiten habe ich per systemctl --user stop (Einheitenname) beendet.
  2. phase: Die Tiefe fuer phi bei rho != rho_z ist einstellbar (streuung_ab, tiefe_gewertet). Bei 12 sqrt(beta) war die
     Streuung groesser (5e-3 bis 2e-2), darum bleibt es bei 20 sqrt(beta) wie PHASE-WAND.
  3. Protokoll je Bahn (nur Rauchlauf), enge Startklammer, dR/d(omega^2) mit beiden Werten.
- Ergebnisse (beta = 0,6, omega^2 = 0,62): R = 17,9400296328 (rk4 0,005), ...336 (rk4 0,01), ...327 (DOP853 1e-12),
  ...333 (DOP853 1e-10). omega^2 = 0,65: DOP853 alt und neu beide 9,9764189096.
- Rauchlauf 5 (neuer Code, alle Verfahren): bic2:0.01 trifft rk4:0.005 auf 1e-10; Laufzeit je Profil 18 s (bic2), sonst
  0,2 bis 1,8 s. Die Auswertung lief durch (Regelpfade, Neben- und Zusatzform, Ausgleiche). Ihre Zahlen bei beta = 0,6
  mit erfundenen rho sind bedeutungslos.

## 9. Laeufe (je Aufruf eine Kleintest-Einheit, 1 Kern, <= 600 s)

| Spur | Inhalt |
|---|---|
| cpu | profile beta = 1/2, n = 1 bis 6 und 15 |
| cpu2 | profile beta = 1/2, n = 7, 8, 9, 14 |
| cpu3 | profile beta = 1/2, n = 10 bis 13 |
| cpu6 | profile beta = 1, k = 5 bis 8 |
| cpu4 | phase beta = 1/2, phase beta = 1, dann profile beta = 1, k = 1 bis 4 |
| cpu4 | danach auswertung beta = 1/2 und beta = 1 |

- kette.sh (ueber start.sh, nohup) wartet auf alle Profile, dann die Auswertungen. start.sh prueft vorher die sha256 der
  PHASE-WAND-Kopien.
- Urteile in lauf/auswertung-b05.json (P3D-1, P3D-2) und lauf/auswertung-b1.json (P3D-3); mit jq zusammengefasst in
  lauf-69/urteile.json.

## 10. Code, Konfigurationen und Skripte (sha256 vor dem Einfrieren; lokal = .69)

```
fcd7a98ad1a52888e2c6a872bd38e161a9d33cb6b1f97ab24a9a6b05c056dc2b  phase_3d.py
c9add78215a755c33fd368ac7d154e190e4b3647dc78246882bb9dedb52f0397  phase_wand.py (Kopie PHASE-WAND, eingefroren dort)
ba86ae6a61eb31b3afbbefcd630771ae627dfcaaa33b9bd7903b768d44838e9b  bic2_3d_praez.py (Kopie RUNDE-13)
8f98074eb0748f671e07e50817493c1718fe0fa5720795e05f34230074ad7f7f  kette.sh
6dcf5422e4753639e8e79d7cc7250e77cee604b97530a35103e975ad48d77fab  start.sh
dc72113fd7be7f0087d33bfba92d257923202f73f165f980fe83f7dc750418ea  lauf/k-auswertung-b05.json
ddfc44023972f8ba8d625d0f1c311383e761b9f68590058d0233833f09409475  lauf/k-auswertung-b1.json
3666c153f585750ccfcb2c7a8869a80fbbaa2101bb8315358e56eaf3212ce0e9  lauf/k-phase-b05.json
63fa3956ba29ccecb16c848ce3bfad10056102110b9f218d6ae0139e13cfc220  lauf/k-phase-b1.json
41a268424fc2a785499cdc0996b2b55c12a9a22ff219aec5548c1881b99de6b1  lauf/k-profile-b05-a.json
3b4c55747531fbd9b5ba90dc687b08ab34543ff96d8c0a32d601355fca9ad980  lauf/k-profile-b05-b.json
3dbd7554ac065eebb528ab14518cdc2d78d69700354f1b786ed6c25e5f6f14f9  lauf/k-profile-b05-c.json
bdd8fd6909614a8195f0d14df1520d395b5c5ba2a58ec4d6012612b94943bac6  lauf/k-profile-b1-a.json
bf92e7ceb1fca9ae0abc235011b7d65ed0bbe74c85e0d4606d517053edaff062  lauf/k-profile-b1-b.json
3d4e10833ae6b37f7216bf2fbb5b556a4b8eba25d34b36c191451147e2857cc6  lauf/pw-phase-b05.json (= PHASE-WAND phase-b05.json)
32bedc3d894a946ffd4a3395b0a0c406b20d75d05110d6c7d88394ac307ba096  lauf/pw-phase-b1.json (= PHASE-WAND phase-b1.json)
ddc778e7e92e254dde37709f62875a98aa49a92910427b667c580b35f60c1ce3  lauf/sprossen-b05.json
d0126655c09d32b9b9d5ea6ca6fbf2b6a7a80bb72365df2d1d61038a7bffa7fc  lauf/sprossen-b1.json
```
