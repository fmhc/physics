# REGULAER-V-1: Plan (Runde 49, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Karte KARTE.md bindend; RV0 bis RV3 und ihre Bedeutung unveraendert.
- **Zeiten (date, CEST; die .69 laeuft in UTC = CEST - 2 h):** Start 2026-10-05 12:41:33. Schreibtischrechnung im Kopf
  zwischen dem Lesen und 12:56:23, Plantext ab 12:56:23. Bis zu diesem Text lief keine Rechnung, kein Interpreter, kein
  Rauchtest. Zeitbox 120 min, also bis 14:41:33.
- **Kennzeichen:** [M] eigene Mathematik (Kopf, ungeprueft, kein zweiter Leser), [E] gerechnet, [P] Projektdatei,
  [F] Festlegung dieses Plans, [L] Gedaechtnis-Literatur, [H] Hypothese.
- Alles ist synthetische Rechnung an einem gedachten, unendlich periodischen Netz. Keine Messdaten.

## 0. Gelesen (vor dem Plan)

- KARTE.md; VIERTE-KOORDINATE-L DOSSIER 4.1, 5.2, 6.1; HODGE-L DOSSIER 1a, 4.3 und ARBEITSFELD (Nachtrag 06:31:21);
  TT-ISO-1 code/ew.py (geometrie, baue), code/tp.py (AV, R8); DANZER-NAEHERUNG-2 PLAN.md und code (licht_netz.fit,
  danzer_naeherung.halbkugel, harm, referenzen, zerlegen, dispersion, operator_messen, FENSTER_HAUPT).
- Kein Projekt-grep.

## 1. Schreibtisch (Pflicht, vor jeder Rechnung) [M]

**Koordinaten.** Einheit 1/8 der kubischen Kante a (wie ew.py und HODGE-L). Ein Loch (Stumpftetraeder) mit Mitte C = 0
hat die Ecken = Permutationen von (+-3, +-1, +-1) mit gerader Zahl von Minuszeichen (Kante 2 sqrt2 = Pyrochlorkante
l_P; l_P^2 = 8). Dreieck a (zur Ecke R8[a]) = {2 R8[a] + R8[b], b != a}; Sechseck a = {2 R8[b] + R8[d], b, d != a,
b != d}, Mitte H_a = -R8[a], |H_a|^2 = 3, alle Lochecken |v|^2 = 11. Finn-Tetraeder ueber Dreieck 0: Spitze (3,3,3).
Nachbarloch hinter Sechseck a: C' = 2 H_a - C (H ist Inversionszentrum).

**Bahnen von Fd-3m auf den Ecken von V (je primitive Zelle 10 Ecken):** 3 Bahnen.
- P: 4 Pyrochlor-Ecken (Lagesymmetrie -3m, Ordnung 12; 48/12 = 4),
- C: 2 Lochmitten (Lagesymmetrie -43m, Ordnung 24; 48/24 = 2; C1 und C2 durch die Inversion an einer P-Ecke verbunden),
- H: 4 Sechseckmitten (Lagesymmetrie -3m; 48/12 = 4).
- Die Wyckoff-Namen (8a/8b, 16c/16d) sind [L], nicht geprueft; die Zahl 3 ist [M].
- Bahnweise konstante Gewichte w_P, w_C, w_H; modulo Konstante zwei Unbekannte x = w_C - w_P, y = w_H - w_P.

**Flaechenklassen (116 je Zelle) und Insphaeren-Ungleichung.** Hoehe h_i = |p_i|^2 - w_i. Flaeche f = (a, b, c) mit
Gegenecken d (Tetraeder T) und e (Tetraeder T'). Die Gerade d-e schneidet die Ebene von f in q = lambda_d d + lambda_e e
= mu_a a + mu_b b + mu_c c mit lambda_d + lambda_e = 1 = mu_a + mu_b + mu_c. Lokal regulaer heisst: die gehobene Sehne d-e
liegt bei q ueber dem gehobenen Dreieck,

  g_f(w) = lambda_d h_d + lambda_e h_e - (mu_a h_a + mu_b h_b + mu_c h_c) > 0  ("Sehnenabstand", Einheit (a/8)^2).

g_f ist linear in w und translationsinvariant; [M] g_f = delta_f * 2 h_d h_e / (h_d + h_e) mit delta_f = vorzeichenbehaftete
duale Laenge (Abstand der Orthozentren von T und T') und h_d, h_e = Abstaende der Gegenecken von der Ebene von f. Also
sign(g_f) = sign(*2_f). Kontrolle mit HODGE-L: Klasse 3 bei w = 0: delta = -sqrt2/3, h_d = h_e = sqrt2, g = -2/3.

| Klasse | Flaeche | Nachbarn | je Zelle | q, Gewichte | g (Schreibtisch) | bei w = 0 |
|---|---|---|---|---|---|---|
| 1 | P P P (Finn-Dreieck) | Finn-Tetraeder / Kegel | 8 | q = Schwerpunkt; lambda_C = 4/9, lambda_Spitze = 5/9 | 4 - 4x/9 | 4 |
| 2 | C P P, Dreieck-Sechseck-Kante | Kegel / Sechsecktetraeder | 24 | q = (1,1,1/2); lambda = 3/8 (P), 5/8 (H); mu = 1/2 (C), 1/4, 1/4 | 1/2 + x/2 - 5y/8 | 1/2 |
| 3 | C P P, Sechseck-Sechseck-Kante | Sechsecktet. / Sechsecktet. | 12 | q = (1,0,0) = Mitte H_a H_b; mu = 2/3 (C), 1/6, 1/6 | -2/3 + 2x/3 - y | **-2/3** |
| 4 | H P P (in der Sechseckebene) | Sechsecktet. Loch C / Loch C' | 24 | q = H (C, H, C' auf einer Geraden) | 3 - x + y | 3 |
| 5 | C H P | zwei Sechsecktet. desselben Sechsecks | 48 | q = Mitte H v_i = Mitte v_(i-1) v_(i+1) (Raute) | 4 + y/2 | 4 |

- 8 + 24 + 12 + 24 + 48 = 116. Jede Klasse ist eine Bahn (Stabilisator 6, 2, 4, 2, 1; 48/Stab = Anzahl).
- Bei w = 0 ist genau Klasse 3 verletzt (12 je Zelle), wie HODGE-L 1a; Klasse 2 (dort "ungeprueft") ist bei w = 0
  regulaer (g = 1/2).
- Lineare Beziehung: g3 = (4/3) g2 - (1/3) g5 (identisch in x, y).

**Loesung von Hand.** Zulaessig (alle g > 0) ist das offene Dreieck in der (x, y)-Ebene mit den Ecken
(7, 4), (-5, -8), (-11, -8), Flaeche 36 (a/8)^4:
- obere Kante g3 = 0 (von (-11, -8) nach (7, 4)), rechte Kante g4 = 0 (von (-5, -8) nach (7, 4)), untere Kante g5 = 0;
- g2 = 0 beruehrt nur die Ecke (-11, -8) (dort g2 = g3 = g5 = 0); g1 > 0 im ganzen Dreieck (x <= 7 < 9).
- Beispiel: x = 0, y = -2 (nur die Sechseckmitten leichter): g = (4, 7/4, 4/3, 1, 3).
- **Groesste Marge (LP von Hand): t_max = 12/7 = 1,714286 (a/8)^2 = 3/14 l_P^2 bei x = -23/7, y = -32/7.** Aktiv sind
  g2, g3, g4, g5 (alle 12/7); g1 = 344/63. Optimalitaet: 0 = mu3 grad g3 + mu4 grad g4 + mu5 grad g5 mit mu4 = 2 mu3/3,
  mu5 = 2 mu3/3 > 0; die Gradienten spannen die Ebene, das Optimum im Schnitt ist eindeutig.
- **Volle Gewichtsraeume:** Die Kammer {w: g_f(w) > 0 fuer alle f} ist konvex und unter der Raumgruppe (inklusive der
  Translationen der Superzelle L = 2) invariant. Mittelt man einen zulaessigen Punkt ueber die Gruppe, bleibt er
  zulaessig und wird symmetrisch. Also: Kammer nicht leer <=> symmetrischer Schnitt nicht leer, und die groesste Marge
  wird von einem symmetrischen Punkt erreicht. Daraus [M]: **t_max(L = 1) = t_max(L = 2) = t_max(symmetrisch) = 12/7.**
- **Beschraenktheit [M]:** Fuer jede nichtkonstante periodische Richtung dw gibt es eine Flaeche mit Knick < 0 (eine
  periodische, an allen Flaechen konvexe stueckweise lineare Funktion ist konvex und periodisch, also konstant). Die Kammer
  ist modulo Konstante beschraenkt und offen, Dimension 10 L^3 - 1.
- **Wandzuege im symmetrischen Schnitt [M]:**
  - g3 = 0: die 12 symmetrischen 2-3-Zuege von HODGE-L (neue Kante H_a-H_b). w = 0 liegt jenseits dieser Wand.
  - g4 = 0: Die Sechseckebene wird flach; gehobenes H liegt auf der gehobenen Sehne C-C'. Die Potenzzelle von H hat dann
    Volumen 0; dahinter verschwindet H, die Doppelpyramide zerfaellt in 6 Tetraeder um die Achse C-C' (das Netz S aus
    EINE-WELT-LOCH-1).
  - g5 = 0: in der Sechseckebene 4-4-Zuege (Speiche H-v_i gegen Diagonale v_(i-1)-v_(i+1)), symmetrisch alle 6 zugleich;
    auch hier geht das Volumen der Potenzzelle von H gegen 0.
  - g2 = 0 nur in der Ecke (-11, -8): 2-3-Zug Kegel/Sechsecktetraeder (neue Kante P-H). g1 = 0 wird nicht erreicht.

**Damit vorab entschieden [M] (als Kontrolle gefuehrt):**
- **RV1 (V regulaer, t_max > 0): eingetroffen**, t_max = 12/7 (a/8)^2.
- **RV2 (bahnweise konstante Gewichte genuegen): eingetroffen**; die Kammermitte ist symmetrisch.
- Offen bleiben RV0 (Kontrollen), RV3 (Anisotropie), die volle Kammer (Breite je Koordinate, Wandzuege ausserhalb des
  symmetrischen Schnitts) und L = 2.
- Wenn das LP etwas anderes liefert als 12/7 bei L = 1, L = 2 und symmetrisch, ist entweder diese Handrechnung oder der
  Code falsch. Dann wird das im Ergebnis ausgewiesen und nicht nachtraeglich ausgeglichen.

## 2. Bau [F]

- V aus TT-ISO-1: code/ew.py und code/tp.py sind unveraenderte Kopien (sha256 fa7b6417... und 419d7da6..., gleich
  RUNDE-37/tt-iso-1/code). ew.geometrie('V') liefert die 10 Untergitterlagen (pos8) und die 58 Tetraeder; Zuordnung der
  Ecken mit ew.zerlege. Dort wird nichts geaendert. HODGE-L hat keinen Code und keine Tabellen; die Flaechenliste baue ich
  aus den Tetraedern (jede Flaeche genau zweimal).
- Superzelle L in {1, 2}: Translationen m @ AV8, m in {0..L-1}^3. Globale Ecke = (Untergitter, m mod L). Kanonische
  Schluessel fuer Kanten und Flaechen: Lagen relativ zur Heimlage der kleinsten Eckennummer.
- Pruefungen (mechanisch, Abbruch bei Fehler): 10 L^3 Ecken, 68 L^3 Kanten, 116 L^3 Flaechen, 58 L^3 Tetraeder, Euler 0,
  jede Flaeche in genau 2 Tetraedern, kein Tetraeder mit doppelter Ecke, Volumensumme = 128 L^3 (a/8)^3, Klassenzahlen
  8, 24, 12, 24, 48 je Zelle (Klasse nach Eckbahnen von Flaeche und Gegenecken).

## 3. LP [F]

- Variablen w (10 L^3) und t. Zeile je Flaeche: g_f(w) = G0_f - lambda_d w_d - lambda_e w_e + sum mu_i w_i >= t
  (Koeffizienten bei gleicher Eckennummer addiert). Maximiere t.
- Konstante: sum_i w_i = 0. Damit ist das LP beschraenkt (Abschn. 1). Sicherung: Kasten |w_i| <= 64 (a/8)^2 = a^2;
  liegt eine Kastengrenze am Optimum an (Abstand < 1e-6), steht das im Ergebnis ("kastenbegrenzt").
- Loeser scipy.optimize.linprog, method = 'highs' (scipy 1.18.0 liegt auf der .69 in der ueber .pth eingebundenen
  Umgebung; Versionsausgabe im Rauchtest). Rechnet auf der CPU innerhalb der kleintest-Einheit der Spuren p4000a/p4000b;
  eine GPU braucht ein LP mit 81 Variablen nicht (Auftrag nennt HiGHS ausdruecklich).
- Ausgaben je L: t_max, w_opt, Symmetrisierung (Bahnmittel) und deren Marge, Kastenstatus.
- Symmetrisches LP: w = B z mit z = (w_P, w_C, w_H), w_P = 0; Variablen (x, y, t).
- Werte bei w = 0 (alle Zeilen), Zaehlung g < -1e-12 je Klasse; Werte bei der Handloesung (0, -23/7, -32/7).
- **Breite der Kammer (abgeschlossen, g >= 0):** fuer jede Ecke i min und max von w_i (mit sum w = 0); Zusammenfassung je
  Bahn. Dimension = 10 L^3 - 1, falls t_max > 0. Symmetrischer Schnitt: min/max von x und y (4 LPs) gegen die Ecken des
  Dreiecks.
- **Wandzuege:** Zeilen mit gleicher Halbraum-Normierung (Zeile / Norm, gerundet 1e-9) bilden eine Wandgruppe. Je Gruppe
  ein LP: Gruppe = 0, alle anderen Gruppen >= tau, maximiere tau. Facette, wenn tau > 1e-6 (HiGHS-Toleranz ~1e-7; vor dem
  Einfrieren von 1e-9 auf 1e-6 gesetzt, ohne Werte gesehen zu haben). Je Facette Klasse und Zugart
  aus mu: alle mu > 1e-9 -> "2-3"; ein mu = 0 -> "4-4 (q auf Kante)"; zwei mu = 0 -> "Ecke (q in einer Ecke)"; ein
  mu < -1e-9 -> "nicht konvex".

## 4. Gewichteter Hodge-Stern [F]

- 3D-Gegenstueck zu de Goes Gl. (13) mit Orthozentren (Potenzzentren) statt Umkreismitten, Formel nach Glickenstein
  [L, Formel aus dem Gedaechtnis; Pruefung ueber die Identitaeten unten]:
  - Kantenzentrum c_ij auf der Kante im Abstand d_ij = (l^2 + w_i - w_j)/(2 l) von i (de Goes Gl. 2).
  - Flaechenzentrum c_ijk (gleiche Potenz zu i, j, k in der Ebene), Tetraederzentrum z_T (gleiche Potenz zu allen vier).
  - Anteil von T an der dualen Flaeche der Kante ij: A*_(ij,T) = 1/2 (h_(ij,k) h_(ijk,l) + h_(ij,l) h_(ijl,k)), h = vorzeichen-
    behaftete Abstaende (Kantenzentrum -> Flaechenzentrum in der Flaeche, Richtung zur dritten Ecke; Flaechenzentrum ->
    Tetraederzentrum, Richtung zur vierten Ecke).
  - *1_e = A*_e / l_e; *0_v = sum_(e an v) A*_e d_(v,e) / 3; *2: duale Laenge delta_f = h_(f,T) + h_(f,T') (Vorzeichen wie
    HKV).
- Bei w = 0 sind das die umkreisbasierten Sterne von DANZER-NAEHERUNG-2/TAKT-UMKLAPP-1.
- Kontrollen je Auswertung: sum *0 = Zellvolumen; sum_e A*_e l_e n_e n_e^T = Vol I (Divergenzsatz, gilt fuer jedes
  orthogonale Dual); sign(delta_f) = sign(g_f) an allen Flaechen und |g_f - delta_f 2 h_d h_e/(h_d + h_e)| < 1e-10 (bei w = 0,
  in der Kammermitte und an 3 Zufallsgewichten); HODGE-L-Zahl: delta = -sqrt2/3 (a/8) an Klasse 3 bei w = 0.
- In der Kammer erwartet [M]: alle *1, *2, *0 > 0 (Potenzdiagramm ist echtes Dual). Wird im JSON je Stichprobe gezaehlt.

## 5. l = 4-Anisotropie [F] (wie DANZER-NAEHERUNG-2, soweit moeglich)

- Skalar: d0^H *1 d0 phi = omega^2 *0 phi, Bloch mit wirklichen Lagen. omega_0(k) = Wurzel des kleinsten Eigenwerts von
  *0^(-1/2) K(k) *0^(-1/2) (dicht, numpy eigvalsh; n = 10 bzw. 80). Keine Ritz-Naeherung noetig.
- Messung woertlich mit den unveraenderten Kopien danzer_naeherung.py (sha256 0571953e...) und licht_netz.py
  (98d3960a...): dn.operator_messen('S', fabrik, 1, dn.halbkugel(40), dn.FENSTER_HAUPT, L_ref, dn.referenzen()).
  Fenster [0,03; 0,12] pi/L_ref, 8 Punkte, Fit omega/k = c (1 + a2 k^2 + a4 k^4 + a6 k^6), Zerlegung von a2(n).
- **L_ref = 1 = kubische Kante a** (Lagen in Einheiten a; Gewichte durch 64). Bei L = 2 bleibt L_ref = 1, damit dieselben
  physikalischen k gemessen werden.
- **Kennzahl beta = a2_zerlegung.beta_S4** (Koeffizient von S4 = sum n_i^4, Projektion auf K4), Einheit a^2. Nebenzahlen:
  rms_l4 (ganzer l = 4-Anteil), nichtkub4_rms, rms_l2, rms_l6, c_spanne_rel, fit_rms_rel_max.
- Erwartung [M], vorab ableitbar: c = 1 in allen Richtungen fuer jedes w in der Kammer (Identitaet oben und Abschluss der
  Potenzzellen); die Anisotropie steckt in a2.

## 6. Stichproben in der Kammer [F]

- **Kammermitte w_mid:** Bahnmittel der LP-Loesung von L = 1 (erwartet (0, -23/7, -32/7) + Konstante). beta_mid aus L = 1.
- S1 (L = 1, symmetrisch): Ziele = 3 Dreiecksecken und 3 Kantenmitten des Schnitts; Punkte w_mid + s (Ziel - w_mid),
  s in {0,5; 0,9; 0,99}: 18 Punkte.
- S2 (L = 1, voll): 40 Zufallsrichtungen (default_rng([4096, L, 7]), Normalverteilung, sum = 0, normiert); Wandabstand
  s_W = min ueber Zeilen mit kappa < 0 von g(w_mid)/(-kappa); Punkte bei s = 0,5; 0,9; 0,99 s_W: 120 Punkte.
- S3 (L = 1, Kammerecken): die 20 LP-Extrempunkte (min/max je w_i); Punkte w_mid + 0,99 (w_ext - w_mid): 20 Punkte.
- S4 (L = 2): Kontrolle K4 (w_mid kachelweise, beta wie L = 1) und 16 Zufallsrichtungen (default_rng([4096, 2, 7])) bei
  s = 0,5; 0,9; 0,99 s_W: 48 Punkte.
- Beschreibend (kein Urteil): beta bei w = 0 (umkreisbasiert, ausserhalb der Kammer), Probe-Fenster dn.FENSTER_PROBE
  in der Kammermitte.

## 7. Kontrollen fuer RV0 [F]

- (a) V bei w = 0, L = 1 und L = 2: Menge der Flaechen mit g < -1e-12. Bestanden, wenn es genau 12 L^3 sind, alle aus
  Klasse 3 (Sechseck-Sechseck-Kanten, HODGE-L 1a), und alle uebrigen g > 1e-12.
- (b) Zufaellige periodische Delaunay-Zerlegungen: 3 Saaten (default_rng([4096, 99, s]), N = 40 Punkte im Einheitswuerfel,
  scipy.spatial.Delaunay ueber 27 Bilder, Tetraeder mit Schwerpunkt in der Zelle). Bau-Pruefung (jede Flaeche 2-mal,
  Euler 0, Volumen 1). Bestanden, wenn bei w = 0 alle g > 1e-12 (zulaessig), in allen 3 Saaten. LP-t_max beschreibend.
- (c) "Mother of all examples" als Prisma [L]: aeusseres Dreieck Radius 2, inneres Radius 1, gleiche Winkel (90, 210,
  330 Grad), verdrehte Zerlegung (4,5,6), (1,2,5), (1,5,4), (2,3,6), (2,6,5), (3,1,4), (3,4,6); mal [0, 1] mit
  Treppenzerlegung nach Eckennummer (21 Tetraeder). Endliche Punktmenge: keine Konstante, Normierung |h_i| <= 1 (h = |p|^2 - w).
  Bestanden, wenn t_max <= 1e-9 (keine strikt positive Marge = nicht regulaer). [M] Begruendung: Die Bodenflaeche
  erbte sonst eine regulaere Zerlegung; die drei Trapez-Ungleichungen summieren sich zu 0 < 0.
- (c') Positivkontrolle dazu: Delaunay derselben 12 Punkte mit Zitter 1e-2 (default_rng([4096, 98])): t_max > 1e-6.
- RV0 nach Plan: (a) und (b) und (c) bestanden -> eingetroffen; sonst nicht eingetroffen (Einzelergebnisse im Ergebnis).
  (c') ist Werkzeugkontrolle: faellt sie aus, ist (c) nicht aussagekraeftig ("nicht auswertbar").

## 8. Weitere Kontrollen [F]

- K1 Bau (Abschn. 2). K2 Sterne/LP-Zeilen (Abschn. 4). K3 Identitaeten (Abschn. 4).
- K4: beta(L = 2, w_mid gekachelt) = beta(L = 1, w_mid) bis 1e-8 relativ.
- K5: Hand gegen LP: g je Klasse bei w = 0 gleich (4, 1/2, -2/3, 3, 4), bei w_hand gleich (344/63, 12/7, 12/7, 12/7, 12/7),
  je bis 1e-9; t_max(L = 1), t_max(L = 2), t_sym gleich 12/7 bis 1e-7; Ecken des symmetrischen Schnitts bis 1e-6.
- Kartenkontrolle "Ergebnis unabhaengig von L": t_max(1) = t_max(2) bis 1e-7 und RV1/RV2-Urteil gleich.

## 9. Urteilsregeln (mechanisch, Funktion urteilen)

- **RV0:** Abschn. 7.
- **RV1:** t_max(L = 1) > 1e-9 und t_max(L = 2) > 1e-9 -> eingetroffen; beide <= 1e-9 -> nicht eingetroffen; sonst
  "L-abhaengig" (Kartenkontrolle verletzt).
- **RV2:** nur falls RV1 eingetroffen: t_sym > 1e-9 -> eingetroffen (Wortlaut: symmetrische Gewichte genuegen).
  Zusatz nach Plan: |t_sym - t_max| <= 1e-7 (die beste Marge ist symmetrisch). Falls RV1 nicht eingetroffen: "entfaellt".
- **RV3 nach Plan:** Delta = max ueber alle Stichproben S1 bis S4 von |beta - beta_mid| / |beta_mid|. Delta < 0,10 ->
  eingetroffen, sonst nicht eingetroffen. Ist |beta_mid| < 1e-12 a^2: nicht auswertbar. Faellt eine Stichprobe aus der
  Kammer (ein *2 <= 0 oder ein *0 <= 0), zaehlt sie nicht und wird ausgewiesen.
- **RV3 nach Wortlaut** ("l = 4-Anisotropie" als ganzer l = 4-Anteil): dieselbe Regel mit rms_l4 statt beta. Beide Urteile
  werden genannt; bei Abweichung gilt fuer die Karte das Urteil nach Plan, das andere steht daneben.
- Beschreibend: Delta je Stichprobengruppe und je s, Ort des groessten Delta, beta bei w = 0.

## 10. Laufliste [F]

- Nur .69, kleintest.sh, Spuren p4000a und p4000b, je Lauf <= 600 s. Arbeitsordner
  /home/fmh/fmhc-physics-remote/regulaer-v-1/ (code/, lauf/, rauch/).

| Lauf | Spur | Aufruf (code/rv.py ...) | erwartet |
|---|---|---|---|
| H1 | p4000a | lp 1 lauf/lp1.json | < 1 min |
| H2 | p4000b | lp 2 lauf/lp2.json | < 3 min |
| H3 | p4000a | kontrollen lauf/kontrollen.json | < 1 min |
| H4 | p4000a | kammer 1 lauf/kammer1.json | < 3 min |
| H5 | p4000b | kammer 2 lauf/kammer2.json | < 5 min |
| H6 | p4000a | auswerten lauf/auswertung.json lauf/lp1.json lauf/lp2.json lauf/kontrollen.json lauf/kammer1.json lauf/kammer2.json | < 1 min |

- Faellt ein Lauf aus (Fehler, 600 s), steht das im Ergebnis. Eine Codeaenderung nach dem Einfrieren ist eine
  Selbstanzeige mit neuer eingefrorener Fassung.

## 10a. Rauchtests (nach dem Plantext, vor dem Einfrieren)

- Alle ueber kleintest.sh, Ausgaben nach rauch/ (UTC): R1 p4000a rauch (11:03:17 bis 11:03:22), R2 p4000a lp 1
  (11:03:39 bis 11:03:41), R3 p4000b kontrollen (11:03:39 bis 11:03:42), R4 p4000a kammer 1 (11:03:58 bis 11:04:24,
  25,6 s), R5 p4000b kammer 2 (11:03:58 bis 11:04:55, 56,9 s). Alle rc = 0, alle unter 120 s.
- Gelesen habe ich nur die Logs: Bau, Pruefungen, Laufzeiten und Statuszeilen. Keine JSON-Werte, kein t_max, keine
  Verletzungszahl, kein beta.
- Aus R1 gesehen [E]: V L = 1: 10/68/116/58, Euler 0, jede Flaeche 2-mal, Volumen 128 (a/8)^3; L = 2 entsprechend 8-fach;
  Klassenzahlen wie Abschn. 1; alle lambda in (0, 1); K2 bei w = 0: Vorzeichen gleich, |g - delta H| <= 1,5e-16;
  K3: Volumen 2e-16, T1 3e-15. Zufall Saat 0: 40/304/528/264, Euler 0, Volumen 1. Mutter-Prisma: 12/42/52/21,
  32 innere und 20 Randflaechen, Volumen 3 sqrt3; 2D-Zerlegung gleich orientiert, Flaechensumme = aeusseres Dreieck.
- Aus R2 gesehen: "Wandgruppen: 60" bei L = 1. Erwartet hatte ich 72 (8 + 24 + 12 + 4 + 24). Erklaerung [M]: Bei L = 1
  sind gegenueberliegende Sechseckecken dieselbe Ecke (gleiches Untergitter), daher fallen die Zeilen von Klasse 5 fuer
  v_i und v_(i+3) zusammen: 3 statt 6 Gruppen je Sechseck, 12 statt 24 je Zelle, 60 gesamt. Bei L = 2 erwarte ich 72 je
  Zelle nur dann, wenn keine weiteren Zusammenfaelle auftreten; beschreibend.
- Keine Codeaenderung nach den Rauchtests.

## 11. Einfrieren

- Eingefroren werden PLAN.md und code/rv.py als Kopien *.eingefroren-<Zeit>, sha256 in EINGEFROREN-SHA256.txt (dazu die
  vier unveraenderten Kopien). Auf der .69 dieselben Pruefsummen. Danach keine Aenderung an Plan, Code oder Regeln.
