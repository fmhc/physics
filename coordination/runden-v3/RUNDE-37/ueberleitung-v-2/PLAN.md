# UEBERLEITUNG-V-2: Plan (Code-Agent fuer die Leitung claude-primary, Runde 49)

- Karte KARTE.md gelesen; UW0 bis UW4, Messziel, Wortlaut, Wahrscheinlichkeiten und Bedeutung bleiben unveraendert und
  bindend. Die Karte wird nicht geaendert.
- Start des Agenten 2026-10-05 15:19:11 CEST (date). Plantext ab 2026-10-05 15:27:19 CEST (date), vor jedem Rauchtest und
  vor jeder Rechnung dieser Karte. Zeitbox 120 min ab Start.
- Gelesen (nur lesend): ueberleitung-v-1/ (ERGEBNIS, PLAN.md.eingefroren-20261005-143809, code/uv.py, nachtrag_uv.py,
  nachtrag2_uv.py, nachtrag_aw.py, Teile von hm.py, tg.py, dn.py, tti.py); regime-k-2/ (ERGEBNIS, code/rk2.py und rk.py in
  Teilen); ueberleitung-kh-1/ERGEBNIS.md (wird noch gelesen, nur Kontext); aus ueberleitung-v-1/lauf-69 und nachtrag-69 per
  jq nur Laufzeiten, Aufbauzeit und l_mittel (0,35897) fuer die Zeitplanung.
- **Vorwissen (offengelegt):** alle Zahlen in ueberleitung-v-1/ERGEBNIS.md, insbesondere fuer V: 10 negative
  M_eff-Eigenwerte an 591 k, TT-Spanne0 5,1e-10 (Grenzwert quadratisch durch 2^-12 bis 2^-14), keine wachsende Mode,
  Konvergenz M_eff zwischen 2^-13 und 2^-14 bis 6,6e-4 (Raster) bzw. 1,8e-6 (BZ), Polstellen-Intervalle an drei k. Fuer S
  und B1 keine Werte dieser Groessen bekannt.
- Kennzeichen: [M] Mathematik (Schreibtisch), [P] Projektbefund, [F] Festlegung dieses Plans, [H] Hypothese, [E] wird
  gerechnet. Synthetische, linearisierte Gitterrechnung um flach; keine Messdaten, keine Messdatenbestaetigung.

## 1. Netze und Ecken je Grundzelle [F, M]

- **V** (Arm V-A wie UEBERLEITUNG-V-1 PLAN 1): uv.baue_gitter('V', h), 10 Untergitter (ew.geometrie('V'): 4 R8 + C1 + C2 +
  4 Sechseckmitten), fcc-Gitter tp.AV, Hoehen j/10 mal h, Hubfolge A. 3D-Netz hm.netz('V') ueber tg.modell.
- **S** (Arm S-A wie REGIME-K-2): Raum rk2.netz_raum('S'), 6 Untergitter (ew.geometrie('S'): 4 R8 + C1 + C2), Hubfolge A
  (Rang = Code-Index), Hoehen j/6 mal h, Ordnung rk2.ord_rang, Gittervektoren tp.AV. 3D-Netz hm.netz('S') (=
  dn.netz_ew('S'), dieselbe ew.geometrie) ueber tg.modell.
- **B1** (Arm B1-t1 wie REGIME-K-1/-K-2): rk.baue('B1', tau = h), 4 Untergitter (XB_B1: Klassen 0, X, Y, Z),
  kubische Zelle, Klassenhoehen 0, 1/4, 1/2, 3/4 mal h, Ordnung rk.ord_b1. 3D-Netz: tg.modell(eye(3), XB_B1, G, O) mit G, O
  aus rk.b1_raum() (dieselben Tetraeder wie der 4D-Bau).
- **Ecken je Grundzelle (fuer UW1, vor jeder M_eff-Rechnung aus den Netzbauten gezaehlt):** V 10, **S 6, B1 4**.
  Grundzelle = Periodenzelle der Netzbauten. [M] Sollte ein Netz eine kleinere Periode haben, aendert das die Aussage
  "negative Richtungen = Ecken je Zelle" nicht (beide Seiten skalieren mit der Zellgroesse).
- Gemeinsamer Code: uv.Vier unveraendert; fuer S und B1 wird nur die Netzwahl in uv.baue_gitter in code/uw.py erweitert
  (V und KW laufen ueber die unveraenderte Funktion). Schema "ls" (Hauptschema von UEBERLEITUNG-V-1), Fassung B der
  Schichtkanten (q = raeumlicher Metrikanteil).

## 2. Stetige Grenze, Hauptwert und Konvergenz [F]

- **Hauptwert:** Bloecke S_p bei h = 2^-10 **direkt** (keine Extrapolation), wie die Karte "stetige Grenze (h = 2^-10)"
  festlegt. M_eff = S_2[q,q], V_eff = S_0[q,q], C = S_0[q,n], X = S_1[q,beta], alle in tg-Konvention (U^+ ... U wie
  UEBERLEITUNG-V-1 PLAN 6), M_eff hermitesch symmetrisiert.
- **Kontrollen:** dieselben Bloecke bei h = 2^-8 und 2^-12 (H3 = 2^-8, 2^-10, 2^-12) an jedem k.
- **Konvergenzmass** je Block Q in {M_eff, V_eff, C, X}: r_8(Q) = ||Q(2^-8) - Q(2^-10)||_F / ||Q(2^-10)||_F und
  r_12(Q) = ||Q(2^-12) - Q(2^-10)||_F / ||Q(2^-10)||_F; Ordnung p_h = log2(r_8 / r_12) / 2 (beschreibend; 1 bei O(h), 2 bei
  O(h^2)).
- **k konvergent**, wenn (i) D_0 (L-Block bei omega = 0) bei allen drei h positiv definit ist (kleinster Eigenwert
  > 1e-10 mal groesster Betrag), (ii) r_12(M_eff) <= 1e-2 und (iii) r_12(M_eff) <= max(r_8(M_eff), 1e-10).
- **Traegheit stabil** an k: Die Zahlen (negativ, null, positiv) der M_eff-Eigenwerte (null: Betrag <= 1e-10 mal
  groesster Betrag) sind bei allen drei h gleich.
- Beschreibend: Grenzwert durch quadratische Interpolation durch die drei h, ausgewertet bei h = 0 ("x0"); damit die
  Paarung (a0) unten. Geht in kein Urteil ein.

## 3. Statische Richtungen, Regime H, R1 [F, wie UEBERLEITUNG-V-1 PLAN 5]

- Statische Richtungen u = Eigenvektoren von M_eff mit Betrag <= TOL_NULL mal groesster Betrag, **TOL_NULL = 1e-10**.
  Behandlung bindend wie UEBERLEITUNG-V-1 PLAN 5 (uv.reduktion unveraendert): Gleichung der statischen Richtungen = ihre
  Zeile des Potentials B, Schur-Komplement im Potential (B_p, c_p, M_dp, M_p, A_p = M_p^-1); u^+ B u muss regulaer sein
  (Kondition <= 1e10) und u darf keinen Eichanteil haben (n_ug = 0), sonst ist die Reduktion an diesem k **nicht
  definiert** (Meldung, keine Pseudo-Inverse). Danach R1 (S = Komplement von Bild[M_dp, c_p], A_red, B_red), Spektrum,
  TT-Zweige (zwei betragskleinste omega^2, ok = beide positiv und Luecke < 1e-2), wachsend nach Schwelle 1e-9 s.
- Potential B = 3D-Regge-Form des Netzes (tg.ops), M = Eckverschiebung (tg), c = Code-Regel (tg).
- **Paarungen:** (a) Haupt: M_eff(2^-10), Code-c. (a12) Robustheit: M_eff(2^-12), sonst gleich. (a0) beschreibend: x0.
  (aC) beschreibend: Lapse-Kopplung C(2^-10) statt c.
- **Spanne0** wie UEBERLEITUNG-V-1 PLAN 7 (uv.spanne unveraendert): je Richtung und TT-Zweig w(kl) = w0 + w2 kl^2 + w4 kl^4,
  kleinste Quadrate ueber kl = 0,005; 0,01; 0,02; 0,05; 0,1; Spanne0 = max w0 / min w0 - 1; "alle Fitpunkte ok" =
  Reduktion definiert und TT-Paar ok an allen Fitpunkten.

## 4. k-Mengen [F]

- **Raster je Netz** (UW0, UW1, UW2, UW3): 13 Richtungen tti.richtungen13 x kl = 0,005; 0,01; 0,02; 0,05; 0,1; 0,2 mit
  l = mittlere Kantenlaenge des 3D-Netzes (tg): 78 k (= die 78 Raster-k des Nachtrags bei V).
- **BZ je Netz** (UW1, UW3): k = (m/8) BVc, BVc = 2 pi inv(LV)^T, m in {0..7}^3 ohne 0 (511 k); Rand = eine reduzierte
  Komponente pi (m_j = 4). S (fcc): dazu K = 2 pi (3/4, 3/4, 0), U = 2 pi (1, 1/4, 1/4) (513 k). B1 (kubisch, LV = Einheit):
  511 k, Rand = k_i = pi (169 k, darunter X, M, R des kubischen Gitters).
- **Neue k fuer UW4 (V), Liste per Regel, 1484 k, keine der 591 Nachtrag-k:**
  - R: 60 neue Richtungen (Fibonacci-Kugel: z_i = 1 - (2 i + 1)/60, phi_i = i pi (3 - sqrt 5), i = 0..59) x die sechs
    Raster-kl: 360 k.
  - W: dieselben 60 Richtungen auf dem Wigner-Seitz-Rand der fcc-BZ: k = t d, t = min ueber G = n BVc
    (n in {-2..2}^3 ohne 0) mit d . G > 0 von |G|^2 / (2 d . G): 60 k (echte BZ-Randpunkte).
  - G16R: k = (m/16) BVc, m in {0..15}^3, mindestens eine Komponente m_j = 8 (reduzierte Komponente pi) und mindestens
    eine ungerade Komponente: 552 k (Rand im Sinn der Nachtrag-Zaehlung).
  - G16I: dasselbe Gitter, alle drei m_j ungerade: 512 k (Inneres).
  - Kontrolle im Code: Keine neue Richtung ist parallel zu einer der 13 (|cos| < 1 - 1e-9), kein neues k stimmt modulo
    reziprokem Gitter mit einem der 591 Nachtrag-k ueberein (reduzierte Koordinaten mod 1, Toleranz 1e-9); sonst Abbruch.
- **Messziel h*(k):** V, Richtungen [100], [111], [321], kl = 0,005; 0,01; 0,02; 0,05; 0,1; 0,2; 0,5; 1; 2; pi (30 k).

## 5. Mechanische Urteilsregeln [F]

Zaehlung negativer Eigenwerte: lambda < -1e-10 mal groesster Betrag (M_eff hermitesch symmetrisiert). n_neg(h) je h.

- **UW0** (V, 78 Raster-k, h = 2^-10):
  - nach Plan **eingetroffen**, wenn (i) Spanne0(a) in [1,7e-10; 1,53e-9] (Faktor 3 um 5,1e-10) bei allen Fitpunkten ok,
    (ii) an allen 78 k (a) definiert ohne wachsende Mode, (iii) an allen 78 k n_neg(2^-10) = 10, k konvergent und
    Traegheit stabil. **nicht eingetroffen**, wenn (i) mit allen Fitpunkten ok verfehlt ist, oder an einem k (a) und (a12)
    wachsend sind, oder an einem konvergenten k mit stabiler Traegheit n_neg != 10. Sonst **nicht entscheidbar**.
  - nach Kartenwortlaut: nur h = 2^-10: Spanne0(a) im Fenster (alle Fitpunkte ok), keine wachsende Mode mit (a) an den 78 k,
    n_neg(2^-10) = 10 an allen 78 k -> eingetroffen; ist ein Teil nicht bestimmbar (Fit nicht ok, Reduktion nicht definiert)
    und keiner verfehlt -> nicht entscheidbar; sonst nicht eingetroffen.
- **UW1** (S und B1, alle gerechneten k: Raster und BZ):
  - nach Plan **eingetroffen**, wenn an jedem k beider Netze: konvergent, Traegheit stabil, n_neg(2^-10) = Ecken je Zelle
    (S 6, B1 4). **nicht eingetroffen**, wenn an einem konvergenten k mit stabiler Traegheit n_neg(2^-10) != Ecken je
    Zelle. Sonst **nicht entscheidbar**.
  - nach Kartenwortlaut: n_neg(2^-10) = Ecken je Zelle an jedem gerechneten k beider Netze -> eingetroffen; Bloecke an
    einem k nicht bestimmbar und sonst keine Abweichung -> nicht entscheidbar; sonst nicht eingetroffen.
- **UW2** (V, 65 Raster-k mit kl <= 0,1). **Definition der oertlichen Dehnungsrichtungen je Ecke (vor jeder Rechnung):**
  - Fuer Ecke v (Untergitter) die Richtung w_v im Raum der Kantenwerte a_e = dl_e / l_e (tg-Konvention, in der M_eff
    hermitesch ist): a_e = 1 an jeder an v haengenden Kante (Startecke: Faktor 1; Endecke: Bloch-Phase exp(i k . T_e) der
    Endecke), sonst 0; bei einer Kante mit beiden Enden im Untergitter v die Summe. Das ist genau die Spalte v der Matrix
    Wh aus tg.ops (die Gewichte der Code-Regel c = -B Wh), also eine gleichmaessige Dehnung aller Kanten an v [M].
  - D = Orthonormalbasis von Bild(Wh) (Rang = Zahl der Ecken je Zelle, sonst Meldung); N = orthonormale Eigenvektoren von
    M_eff(h) zu negativen Eigenwerten (n_neg Stueck). Kennzahl P(k, h) = ||D^+ N||_F^2 / n_neg (gemittelte quadrierte
    Projektion, euklidisches Skalarprodukt der a-Koordinaten; 1 = ganz im Dehnungsraum).
  - nach Plan **eingetroffen**, wenn an allen 65 k: konvergent, P(k, 2^-10) >= 0,9 und P(k, 2^-12) >= 0,9. **nicht
    eingetroffen**, wenn an einem konvergenten k P(k, 2^-10) < 0,9 und P(k, 2^-12) < 0,9. Sonst **nicht entscheidbar**.
  - nach Kartenwortlaut: Lesart (A) P(k, 2^-10) >= 0,9 an jedem der 65 k; Lesart (B) Mittel ueber die 65 k von
    P(k, 2^-10) >= 0,9. Stimmen A und B ueberein, gilt deren Ausgang; sonst "unklar".
  - Beschreibend (ohne Urteil): dasselbe P fuer S und B1 an deren Raster-k mit kl <= 0,1; dazu je k das kleinste Quadrat
    der Hauptwinkel (Kosinus^2).
- **UW3** (S und B1):
  - Je Netz: delta = abs(Spanne0(a) - Spanne0(a12)). Netz **eingetroffen**, wenn alle Fitpunkte ok, Spanne0(a) + delta
    < 1e-8, an allen k (Raster + BZ) (a) und (a12) definiert ohne wachsende Mode und alle k konvergent. Netz **nicht
    eingetroffen**, wenn (alle Fitpunkte ok und Spanne0(a) - delta >= 1e-8) oder an einem k (a) und (a12) wachsend.
    Sonst nicht entscheidbar.
  - nach Plan: UW3 eingetroffen, wenn S und B1 eingetroffen; nicht eingetroffen, wenn eines nicht eingetroffen; sonst
    nicht entscheidbar.
  - nach Kartenwortlaut: nur (a): je Netz Spanne0(a) < 1e-8 mit allen Fitpunkten ok und an allen k (a) ohne wachsende
    Mode; Verknuepfung wie oben; nicht definierte Teile ohne Verfehlung -> nicht entscheidbar.
- **UW4** (V, die 1484 neuen k): wie ein Netz in UW3, mit Spanne0 ueber die 60 neuen Richtungen (Menge R) und
  "an allen k" = alle 1484 k. Nach Kartenwortlaut nur (a).
- Getrennt berichtet: Rand (Menge W, G16R; bei S und B1 m_j = 4, K, U) und Inneres.

## 6. Messziel h*(k) (ohne Vorhersage, kein Urteil) [F]

- D_0 = L-Block (Schema ls) der Wirkung bei omega = 0, Eigenwerte hermitesch; n_D(h) = Zahl negativer Eigenwerte
  (die Zahl haengt nur vom Unterraum L ab, Sylvester [M]).
- Raster h_j = 2^(-j/8), j = 0..112 (h = 1 bis 2^-14), n_D(h_j) je k.
- **Hauptlesart h*_letzt** (Grenze, unter der D_0 positiv ist; so sind die drei Vorwissen-Punkte der Karte gebildet):
  j* = groesstes j mit n_D(h_j) > 0; Bisektion in log h zwischen h_{j*+1} und h_{j*} (10 Schritte; Test n_D > 0);
  h*_letzt = geometrisches Mittel der Endklammer. j* = 112: "h* < 2^-14"; kein j: "kein negativer Eigenwert bei h <= 1".
- **Woertliche Lesart h*_erst** ("groesstes h, bei dem D_0 einen Eigenwert null hat", gesucht in (2^-14, 1]): kleinstes
  j >= 1 mit n_D(h_j) != n_D(h_{j-1}); Bisektion dazwischen (10 Schritte; Test n_D = n_D(h_{j-1})).
- **Exponent:** Steigung der Ausgleichsgeraden log h*_letzt gegen log kl je Richtung, (i) ueber kl <= 0,1, (ii) ueber alle
  unzensierten kl.
- Grenze: Nulldurchgaenge, die sich zwischen zwei Rasterpunkten paarweise aufheben, sieht das Raster nicht.

## 7. Kontrollen [F]

- K1 Laurent-Form gegen rk.Gitter.H, K2 Eichnullvektoren bei komplexem k_t, K3 rk.Gitter.kontrollen (Fehlwinkel,
  Schlaefli, Volumen, tote Kanten) je h: uv.kontrollen unveraendert, fuer V, S, B1 (K1, K2 bei 2^-8 und 2^-12; K3 bei allen
  drei h); Schwellen 1e-12 (K1, K2), Fehlwinkel <= 1e-12.
- K4 U^+ M_disp(rk) = M(tg) <= 1e-12 an jedem k (prueft die Kantenzuordnung, bei B1 auch Kanten innerhalb einer Klasse).
- K5 Rang B_s = 3 NV und J regulaer an jedem k und h (sonst Schema nicht definiert, Meldung).
- K6 M_eff hermitesch: ||S_2qq - S_2qq^+|| / ||S_2qq|| <= 1e-10.
- K7 3D-Netz: tg-Pruefung (T, E, nV, Diedersumme - 2 pi, Vbox) fuer S und B1.
- Beschreibend (ADM-Form wie Nachtrag UEBERLEITUNG-V-1): ||V_eff - B|| / ||B||, C = kappa c (kappa, Rest), Kreisel
  ||S_1qq|| |k| / ||V_eff||, Lapse-Block ||S_0nn|| / ||C||.

## 8. Laeufe und Rauchtests [F]

- Nur auf der .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu2, cpu3, cpu4, je <= 600 s, Ordner
  /home/fmh/fmhc-physics-remote/ueberleitung-v-2/ (code/, rauch/, lauf/), Logs mit absolutem Pfad.
- Code: code/uw.py (neu; importiert uv.py und die Vorlagen unveraendert, Summen gleich ueberleitung-v-1/code).
- Hauptlaeufe: cpu2: v0 (V Raster), s (S Raster + BZ), b1 (B1 Raster + BZ), vneu Teil 2, hstern [321], dann auswertung;
  cpu3: vneu Teil 0, hstern [100]; cpu4: vneu Teil 1, hstern [111].
- Rauchtests (nach diesem Plantext, je <= 120 s): r1 technisch je Netz (K1 bis K5, K7, Netzgroessen, Laufzeit je k und h;
  keine Spektren, keine Spannen, keine Zaehlungen negativer Eigenwerte); r2 Codeprobe der ganzen Kette mit --probe (2 bis
  4 k je Lauf, auch hstern mit einem k und grobem Raster) und Auswertung: nur rc, Laufzeit, Schluessel ansehen.
- Einfrieren vor dem ersten Hauptlauf: PLAN.md.eingefroren-<JJJJMMTT-HHMMSS>, code/*.eingefroren-<...>, sha256 in
  EINGEFROREN-SHA256.txt; auf der .69 dieselben Summen pruefen.

## 9. Agenten-Vorhersagen (vor jeder Rechnung; gehen in kein Urteil ein)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | UW0 nach Plan eingetroffen (Risiko: Spanne bei h = 2^-10 direkt statt extrapoliert) | 45 % |
| A2 | UW1 nach Plan eingetroffen | 55 % |
| A3 | UW2 nach Plan eingetroffen | 45 % |
| A4 | UW3 nach Plan eingetroffen | 30 % |
| A5 | UW4 nach Plan eingetroffen | 40 % |
| A6 | Exponent von h*_letzt gegen kl (kl <= 0,1) liegt fuer alle drei Richtungen zwischen 0,2 und 1,0 | 50 % |
| A7 | Konvergenzordnung p_h von M_eff ist an den meisten Raster-k nahe 1 (O(h), Kreiselterm) | 55 % |

## 10. Rauchtests vor dem Einfrieren (Nachtrag ab 15:34:46 CEST, date)

- Alle ueber kleintest.sh, .69-Zeiten UTC (CEST = UTC + 2).
- **r1** (code/rauch.sh, 13:33:33 bis 13:33:38 UTC; cpu2 V, cpu3 S, cpu4 B1): alle rc 0 (Service runtime 4,9 / 2,3 /
  1,8 s). Gelesen nur Technik: NV = 10 / 6 / 4, NE = 146 / 86 / 60, nq = 68 / 40 / 28, keine tote Kante, alle
  Diagonalen dt = -1; K1 <= 4,5e-16, K2 <= 1,3e-14, K3 Fehlwinkel <= 4,4e-13 (alle drei h), Schlaefli <= 5,1e-13,
  Volumensumme <= 8,9e-16; K4 <= 1,8e-16 an je 6 Proben-k (B1 mit 4 Kanten innerhalb einer Klasse); K8 (bloecke2 gegen
  uv.Vier.bloecke) 0 exakt; Rang B_s = 30 / 18 / 12, n_L = 38 / 22 / 16, J regulaer, D_0 regulaer (nur ja/nein) an den
  Proben-k; 3D-Pruefung: T = 58 / 34 / 24, E = 68 / 40 / 28, Diedersumme - 2 pi <= 1,8e-15, Vbox 0,25 / 0,25 / 1;
  l_mittel 0,35897 / 0,39811 / 0,74895; Laufzeit punkt2 je k 0,26 / 0,08 / 0,04 s. Keine Spektren, Spannen oder
  Zaehlungen angesehen.
- **r2** Codeprobe (code/probe.sh, 13:34:01 bis 13:34:21 UTC, cpu2): v0, s, b1, vneu Teil 0/1/2 je 3 k, hstern 100 mit
  einem kl und grobem Raster (j <= 16, 2 Bisektionsschritte), auswertung: alle rc 0. Gelesen nur rc, Laufzeiten,
  Schluessel und die Mengen-Information der neuen k (1484 k: R 360, W 60, G16R 552, G16I 512; groesster abs(cos) einer
  neuen Richtung gegen die 13 = 0,99966; kleinster Abstand zu den 591 Nachtrag-k in reduzierten Koordinaten 3,8e-5).
- Keine Aenderung an Plan oder Code nach den Rauchtests. Hinzu kommen nur die Laufketten code/kette-cpu2.sh,
  kette-cpu3.sh, kette-cpu4.sh (PLAN 8).
