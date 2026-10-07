# HOEHE-ISOTROP-1: Plan (Runde 49, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Karte KARTE.md bindend; HI0 bis HI3 und ihre Bedeutung unveraendert.
- **Zeiten (date, CEST; die .69 laeuft in UTC = CEST - 2 h):** Start 2026-10-05 13:19:50. Gelesen bis 13:29:28, Plantext
  ab 13:29:31. Bis zu diesem Text lief keine Rechnung, kein Interpreter, kein Rauchtest. Zeitbox 120 min, also bis
  15:19:50.
- **Kennzeichen:** [M] eigene Mathematik (Kopf, ungeprueft, kein zweiter Leser), [E] gerechnet, [P] Projektdatei,
  [F] Festlegung dieses Plans, [L] Gedaechtnis-Literatur, [H] Hypothese.
- Alles ist synthetische Rechnung an einem gedachten, unendlich periodischen Netz. Keine Messdaten.

## 0. Gelesen (vor dem Plan)

- KARTE.md; REGULAER-V-1: KARTE, PLAN, ERGEBNIS, code/rv.py, code/nachtrag_beta.py, lauf-69 (Logs, Kettenskripte,
  Pruefsummen); LICHT-FINN-NETZ-1: KARTE, ERGEBNIS, NACHTRAG-PHASE-GRUPPE.md, code/licht_netz.py (fit, schranken,
  l_aus_a2, operator_auswerten, richtungen26), code/nachtrag_gruppe.py; danzer_naeherung.py (operator_messen, zerlegen,
  referenzen, halbkugel, maxwell_eigen); KUBISCH-ANKER-L DOSSIER Abschn. 1; VIERTE-KOORDINATE-L DOSSIER 4.1;
  kleintest.sh auf der .69. Kein Projekt-grep.

## 1. Schreibtisch [M] (vor jeder Rechnung)

**1.1 Lesart "Maxwell auf V".** LICHT-FINN-NETZ-1 hat Maxwell als Coulomb-Phase auf den **Diamant-Kanten** mit
Einheitsgewichten gerechnet (M-D: a2 = -1/8 + S4/24 in Tetraederkanten). Das ist ein anderer Operator als Maxwell auf
dem Simplexnetz V. Die Karte meint Maxwell auf V mit gewichteten *1, *2 (DEC auf V). Dieser Operator ist im Projekt neu;
die Zahlen von M-D sind hier nur Vergleich, keine Kontrolle. Die LHAASO-Umrechnung uebernehme ich woertlich (Abschn. 6).

**1.2 Gewichtete Sterne aus dem Potenzdiagramm.** Ecken p_i mit Gewichten w_i, Potenz pi_i(y) = |y - p_i|^2 - w_i.
- Duale Ecke von Tetraeder T: z_T mit gleicher Potenz zu allen vier Ecken (Orthozentrum). Projektion von z_T auf die
  Ebene der Flaeche f ist das Flaechenzentrum c_f (gleiche Potenz zu den drei Ecken, weil die Projektion bei allen drei
  dasselbe h^2 abzieht). Kantenzentrum c_ij im Abstand d_ij = (l^2 + w_i - w_j)/(2 l) von i (de Goes Gl. 2 [S ueber
  VIERTE-KOORDINATE-L]).
- Duale Kante zu f: Strecke z_T z_T', senkrecht auf f; vorzeichenbehaftete Laenge delta_f = h_(f,T) + h_(f,T'),
  h = Abstand c_f -> z_T, positiv zur Seite von T. **\*2_f = delta_f / A_f.**
- Duale Flaeche zu e = ij: Vieleck der z_T um e, senkrecht auf e; Flaeche A*_e = sum_T 1/2 (h_(ij,k) h_(ijk,l) +
  h_(ij,l) h_(ijl,k)) (Formel aus REGULAER-V-1, dort [L] Glickenstein und nur ueber Identitaeten geprueft).
  **\*1_e = A*_e / l_e.** *0_v = Potenzzellen-Volumen = sum_(e an v) A*_e d_(v,e)/3.
- Das ist rv.sterne (unveraendert importiert). Neu ist nur, dass ich *2 = delta / A_f bilde und Maxwell daraus baue.

**1.3 Identitaeten [M].** Fuer jedes w (auch ausserhalb der Kammer, vorzeichenbehaftet) und jedes periodische Netz:
- I1: sum_v *0_v = Vol.
- I2: sum_e *1_e l_e l_e^T = sum_e A*_e l_e n_e n_e^T = Vol I (in REGULAER-V-1 gerechnet).
- **I3 (neu): sum_f *2_f A_f^2 n_f n_f^T = sum_f delta_f A_f n_f n_f^T = Vol I.** Beweisskizze: In jedem Tetraeder T gilt
  der Divergenzsatz fuer x - z_T: Vol_T I = sum_(f von T) A_f n_f (xq_f - z_T)^T (n_f nach aussen, xq_f = Flaechen-
  schwerpunkt). Mit xq_f - z_T = h_(f,T) n_f + (xq_f - c_f) folgt Vol_T I = sum_f A_f h_(f,T) n_f n_f^T + sum_f A_f
  n_f (xq_f - c_f)^T. Der zweite Term hebt sich beim Summieren ueber alle T weg: Jede innere Flaeche kommt zweimal mit
  entgegengesetzter Normale vor, xq_f und c_f haengen nur an der Flaeche. Der erste Term gibt sum_f delta_f A_f n n^T.
- Folge [M]: Ein konstantes Feld E (E_e = E.l_e) erfuellt d0^T *1 E = E . sum A*_e n_e = 0 (geschlossene Potenzzelle);
  ein konstantes B (B_f = B.n_f A_f) erfuellt d1^T *2 B = Umlauf von B entlang des geschlossenen dualen Vielecks = 0.
  Beide brauchen also keinen Korrektor; die langwellige Permittivitaet ist I2/Vol = I, die Permeabilitaet I3/Vol = I.
  **Licht auf V hat fuer jedes w in der Kammer c = 1 in allen Richtungen** (vorab abgeleitet, als Kontrolle gefuehrt).
  Die Gewichte wirken erst in a2.

**1.4 Maxwell auf V (DEC).** A auf Kanten (1-Form), Fluss auf Flaechen (2-Form).
- K(k) = d1(k)^H *2 d1(k), Masse *1; omega^2 = Eigenwerte von *1^(-1/2) K *1^(-1/2) (dicht, numpy eigvalsh).
- Fuer k != 0 klein gilt ker d1(k) = im d0(k) mit Dimension n_V (= 10 L^3); die ersten n_V Eigenwerte sind Eichnullen,
  die naechsten zwei die Photonen (lo, hi), der dritte die erste optische Mode. Bei k = 0 sind es n_V + 2 Nullen (n_V - 1
  Gradienten und 3 harmonische Formen des Torus).
- Bloch-Phasen mit wirklichen Lagen (wie danzer_naeherung): d0[e, v] = -+exp(i k.(x_v - x_e)), d1[f, e] =
  sigma_(f,e) exp(i k.(x_e - x_f)) mit Kantenmitten x_e und Flaechenschwerpunkten x_f im Bezugsrahmen der Flaeche. Dann
  gilt d1(k) d0(k) = 0 exakt.

**1.5 Symmetrie [M].** In der Kammermitte (Fd-3m) und im F-43m-Schnitt hat das Netz kubische Punktsymmetrie (Oh bzw.
Td). Dann:
- a2(n) ist fuer den Mittelzweig (omega_m^2 = (omega_lo^2 + omega_hi^2)/2, Spur, also Polynom) eine quartische Form:
  nur l = 0 und der kubische l = 4-Teil; l = 2, nichtkubisch l = 4 und l = 6 verschwinden. Die einzelnen Zweige lo, hi
  koennen bei Doppelbrechung auch l >= 6 haben.
- Kein lineares Glied: Td und Oh haben Spiegelebenen, also keine optische Aktivitaet [L, Kristalloptik].
- Doppelbrechung in Ordnung (k a)^2 ist bei kubischer Symmetrie nicht verboten (KUBISCH-ANKER-L [L dort]); sie wird
  gemessen, nicht vorausgesetzt.
- Die Inversion an einer P-Ecke vertauscht C1 und C2. Im F-43m-Schnitt ist deshalb beta(u1, u2, v) = beta(u2, u1, v),
  ebenso jede Lichtgroesse.

**1.6 Der Nullpunkt ist keine Einzelstelle [M].** Der F-43m-Schnitt (w_P, w_C1, w_C2, w_H) hat modulo Konstante drei
Parameter z = (u1, u2, v) = (w_C1 - w_P, w_C2 - w_P, w_H - w_P). beta = 0 ist dort im Allgemeinen eine Flaeche, nicht ein
Punkt. Die Karte spricht von "dem Punkt beta = 0". Ich lege fest [F]: **der beta-Nullpunkt w0\* ist der Punkt auf der
Flaeche beta = 0 (im F-43m-Schnitt, in der Kammer) mit der groessten Marge** min_f g_f(w). Begruendung: koordinatenfrei,
und es ist die isotrope Gewichtung, die am weitesten von jedem Umklappzug entfernt ist. Wegen 1.5 gibt es ihn paarweise
(u1 <-> u2) mit gleichen Werten; ich nehme den mit u1 > u2. Alle uebrigen gefundenen Nullpunkte werden beschreibend
mitgemessen (Abschn. 9, HI1).

## 2. Bau [F]

- Code: code/hi.py (neu). Unveraenderte Kopien aus RUNDE-37/regulaer-v-1/code: rv.py (sha256 237a98e5...), ew.py
  (fa7b6417...), tp.py (419d7da6...), danzer_naeherung.py (0571953e...), licht_netz.py (98d3960a...). Dort wird nichts
  geaendert. rv.netz_V, rv.topologie, rv.zeilen, rv.sterne, rv.messen, rv.lp_symmetrisch, rv.strahl_wand, rv.w_sym
  werden unveraendert benutzt.
- Kanten in der Reihenfolge von topo['kanten'] (wie *1 in rv.sterne), Flaechen in der Reihenfolge von topo['flaechen'].
  Flaechenrand: (v0 -> v1), (v1 -> v2), (v2 -> v0) in der Schluesselreihenfolge; Vorzeichen +1, wenn die Kante im
  kanonischen Schluessel gleich orientiert ist, sonst -1; Versatz der Kante = Translation T aus rv.kanon.
- *2_f = delta_f / A_f (A_f aus den Schluessellagen, Einheit a). Einheit des Operators: a (L_ref = 1 = kubische Kante).

## 3. Messung [F]

- **Licht:** dn.operator_messen('M', fabrik, 3, dn.halbkugel(40), dn.FENSTER_HAUPT, 1.0, dn.referenzen()) mit meiner
  fabrik (Zweige maxwell_lo, maxwell_hi, maxwell_mittel = sqrt((lo^2 + hi^2)/2)). Fenster [0,03; 0,12] pi/a, 8 Punkte,
  gerade Potenzen bis 6. Je Zweig: a2_zerlegung (mittel = l = 0, beta_S4 = kubischer l = 4-Koeffizient, rms_l4, rms_l2,
  nichtkub4_rms, rms_l6, rest_rms), c_mittel, c_spanne_rel, fit_rms_rel_max, a1_voll_max_abs, a2_min, a2_max.
- **Kenngroessen Licht [F]:** "isotroper Anteil" = a2_zerlegung.mittel des Zweigs maxwell_mittel (Kugelmittel);
  "l = 4-Anteil" = beta_L := a2_zerlegung.beta_S4 von maxwell_mittel (Hauptgroesse), daneben rms_l4. Doppelbrechung
  (beschreibend): max ueber die 40 Richtungen von |a2_hi - a2_lo|.
- **Diagnose je Messpunkt** (in der fabrik mitgeschrieben): null_rel = max |lambda_(n_V - 1)| / lambda_(n_V) (Eichnullen
  gegen Photon), luecke = min lambda_(n_V + 2) / lambda_(n_V + 1) (optisch gegen Photon), lam_max.
- **Skalar:** rv.messen (unveraendert), beta = kurz(sk)['beta'] wie REGULAER-V-1.
- **Einheiten:** a2 in a^2. Umrechnung auf die Tetraederkante (Pyrochlorkante l_P = a/(2 sqrt2), Finn-Tetraeder): a2 in
  l_P^2 = 8 a2 in a^2.

## 4. Gewichte und Schnitte [F]

- Kammermitte w_mid = rv.w_sym(net, x_m, y_m) mit (x_m, y_m) aus rv.lp_symmetrisch (erwartet -23/7, -32/7).
- F-43m-Schnitt: B4 wie nachtrag_beta.py (Untergitter 0..3 -> P, 4 -> C1, 5 -> C2, 6..9 -> H); w(z) = B4 @ (0, u1, u2, v),
  dann Mittel abgezogen. z_mid = (x_m, x_m, y_m).
- Marge m(w) = min_f g_f(w) (G0 + A w aus rv.zeilen, Einheit (a/8)^2). "In der Kammer" heisst m > 0 und alle *0, *1,
  *2 > 0.

## 5. Suche des beta-Nullpunkts im F-43m-Schnitt [F]

- **Stufe 1 (Strahlen):** 128 Richtungen d in z (ln.fib(128), Einheitsvektoren), d_w = B4 @ (0, d) minus Mittel,
  Wandabstand s_W = rv.strahl_wand(A, G0, w_mid, d_w). beta bei s = 0,25; 0,5; 0,75; 0,9; 0,99 s_W. Erster
  Vorzeichenwechsel (beta_mid > 0 bei s = 0) -> brentq auf dem Klammerintervall (xtol 1e-13, maxiter 100): Strahl-
  Nullpunkt. Nur der erste Wechsel je Strahl.
- **Stufe 1b (nur falls Stufe 1 weniger als 3 Strahl-Nullpunkte liefert):** SLSQP minimiert beta(z) unter g_f(z) >= 0,01
  von den 4 Abtastpunkten mit kleinstem beta aus (maxiter 60, ftol 1e-14, Gradient zentral h = 1e-3). Ist das Minimum
  < -1e-9, brentq auf der Strecke z_mid -> z_min.
- **Stufe 2 (groesste Marge):** von den 3 Nullpunkten mit der groessten Marge aus SLSQP mit Variablen (z, t): maximiere t
  unter g_f(z) - t >= 0 (linear, exakter Gradient) und beta(z)/|beta_mid| = 0 (Gradient zentral, h = 1e-3); maxiter
  60, ftol 1e-12. Danach Politur: brentq laengs z + tau grad(beta)/|grad(beta)|, Intervall tau in [-0,05; 0,05], bei
  fehlendem Vorzeichenwechsel bis zu 5-mal verdoppelt.
- **Zeitwaechter (wegen 600 s je Lauf):** nach 400 s Laufzeit keine neuen SLSQP-Starts (im JSON als "uebersprungen");
  nach 540 s keine weiteren Licht-Messungen an Nullpunkten ausser w0* (Zahl der ausgelassenen im JSON).
- **Toleranz:** gueltiger Nullpunkt, wenn |beta| <= 1e-9 a^2 (rund 1e-6 beta_mid), m > 1e-9 und alle Sterne > 0.
- **w0\*** = gueltiger Kandidat (Stufe 2 poliert und alle Strahl-Nullpunkte) mit der groessten Marge; Gleichstand
  (|Delta m| <= 1e-9) -> groesseres u1 - u2.
- Am Ende: Licht (Abschn. 3) an w0* und an allen gueltigen Nullpunkten; Probe-Fenster dn.FENSTER_PROBE an w0*.

## 6. LHAASO-Umrechnung (woertlich wie LICHT-FINN-NETZ-1) [F]

- ln.operator_auswerten('M-V', op_lP, 3, ln.richtungen26()) mit op_lP(k) = op_a(2 sqrt2 k) / (2 sqrt2), also k und omega in
  Einheiten der Tetraederkante l_P (wie dort: l = Tetraederkante). Fenster W0 (k = 0,01 bis 0,30, 60 Punkte, alle Potenzen
  bis 8), dazu Wk und Wg beschreibend.
- ln.schranken(erg): je Zweig (lo, hi, mittel) aus den 26 a2-Werten (W0, voller Fit): konservativ (kleinstes |a2|),
  Mittel (|Mittel der negativen a2|), streng (groesstes |a2|); l = hbar c / (E_QG,2 sqrt(2 |a2|)), E_QG,2 = 6,9e11 GeV
  (subluminal). Nur negative a2 zaehlen (wie dort). Konvention der Quelle (Phasenkoeffizient), NACHTRAG-PHASE-GRUPPE.
- An w_mid und an w0*. Beschreibend dazu: Schranke aus dem Kugelmittel (8 a2_mittel in l_P^2).

## 7. Stichproben fuer HI2 (L = 1, alle in der 9-dimensionalen Kammer) [F]

- M: Kammermitte.
- S1 (symmetrisch, 18): wie REGULAER-V-1 (3 Dreiecksecken, 3 Kantenmitten; s = 0,5; 0,9; 0,99).
- S2 (120): 40 Zufallsrichtungen default_rng([4096, 1, 7]) wie REGULAER-V-1; s = 0,5; 0,9; 0,99 s_W.
- S3 (20): LP-Extreme je w_i, Punkt w_mid + 0,99 (w_ext - w_mid).
- F43 (640): die Strahlpunkte aus Stufe 1 (128 x 5), mit Licht. Zwei Laeufe zu je 64 Richtungen.
- N (Nullpunkte): alle gueltigen Nullpunkte aus Abschn. 5.
- G (325): Fd-3m-Schnitt, baryzentrisches Gitter m = 24, um 0,99 zur Mitte geschrumpft (wie nachtrag_beta N1).
- L2 (beschreibend, nur Wortlaut-Lesung von HI2): L = 2, w_mid gekachelt (Kontrolle K7) und die ersten 4 Richtungen aus
  default_rng([4096, 2, 7]) bei s = 0,9 s_W. Faellt dieser Lauf aus, steht das im Ergebnis.
- Fuer S1, S2, S3 und M wird der Skalar gegen REGULAER-V-1 kammer1.json verglichen (beschreibend, gleiche Reihenfolge).
- **Gueltig** ist eine Stichprobe, wenn sie in der Kammer liegt (Abschn. 4), null_rel <= 1e-8, luecke >= 1,5 und
  fit_rms_rel_max(maxwell_mittel) <= 1e-6. Ungueltige werden gezaehlt, genannt und nicht gewertet.

## 8. Kontrollen [F]

- K1 Bau: V L = 1 mit 10/68/116/58 (wie rv); d1(k) d0(k) = 0 (max <= 1e-12) an 3 Zufalls-k; Zahl der Eigenwerte
  <= 1e-11 lambda_max (an w_mid): n_V + 2 bei k = 0, n_V bei 3 kleinen Zufalls-k (|k| = 0,05/a).
- K2 Identitaeten I1, I2, I3 (relativ <= 1e-12) an w_mid, w0* und 3 Zufallsgewichten w_mid + 0,5 N(0,1)
  (default_rng([4096, 77])); dort auch rv.stern_kontrolle (Vorzeichen *2 = Vorzeichen g).
- K3 Skalar aus meinem d0, *1, *0 gleich rv.fabrik_skalar (kleinster Eigenwert, relativ <= 1e-12) an 3 Zufalls-k.
- K4 c = 1 fuer Licht: |c_mittel - 1| <= 1e-8 und c_spanne_rel <= 1e-8 an w_mid und w0* (alle drei Zweige).
- K5 Fit: Probe-Fenster gegen Hauptfenster an w_mid und w0* (beta_L, a2_mittel; beschreibend). LHAASO-Fenster W0, Wk, Wg
  (beschreibend).
- K6 Symmetrie: an w_mid und w0* fuer maxwell_mittel rms_l2, nichtkub4_rms, rms_l6 <= 1e-8 a^2 (beschreibend, Boden).
- K7 L = 2: w_mid gekachelt gibt beta_L und a2_mittel wie L = 1 (relativ <= 1e-6; beschreibend).

## 9. Urteilsregeln (mechanisch, Funktion urteilen)

- **HI0 nach Plan:** (a) drei Stichpunkte aus REGULAER-V-1 neu gerechnet: Kammermitte (kammer1.json 'mitte'), w = 0
  (kammer1.json 'w0'), F-43m-Punkt mit kleinstem beta aus nachtrag-beta.json (N2 'ort_min', w aus w_P_C1_C2_H);
  |beta_neu - beta_alt| <= 1e-6 |beta_alt| an allen dreien. (b) w0* existiert (gueltig nach Abschn. 5). Eingetroffen,
  wenn (a) und (b); sonst nicht eingetroffen.
  **Nach Wortlaut:** "auf 1e-6" auch absolut (1e-6 a^2) gelesen; eingetroffen, wenn (b) und (a) in mindestens einer der
  beiden Lesungen.
- **HI1 nach Plan:** R = |beta_L(w0\*)| / |beta_L(w_mid)| (maxwell_mittel). R < 1e-3 -> eingetroffen, sonst nicht
  eingetroffen. Nicht auswertbar, wenn w0* fehlt oder |beta_L(w_mid)| < 1e-9 a^2.
  **Nach Wortlaut** ("l = 4-Anteil von a2 beim Licht"): rms_l4 statt beta_S4, fuer beide Photonzweige lo und hi am
  Punkt w0*: beide < 1e-3 ihres Werts bei w_mid -> eingetroffen; keiner -> nicht eingetroffen; sonst geteilt.
  Beschreibend: Bereich von R ueber alle gueltigen Nullpunkte.
- **HI2 nach Plan:** ueber alle gueltigen L = 1-Stichproben (M, S1, S2, S3, F43, N, G): a = a2_mittel(maxwell_mittel),
  r = a(w)/a(w_mid). Eingetroffen, wenn alle a < 0 und max_w max(r, 1/r) <= 2; sonst nicht eingetroffen.
  **Nach Wortlaut:** dazu die L2-Punkte; "aendert sich um hoechstens den Faktor 2" als Spanne max|a| / min|a| <= 2 ueber
  alle Stichproben; "negativ" fuer alle drei Zweige.
- **HI3 nach Plan:** Mittel-Schranke von maxwell_mittel (Abschn. 6); F = max(l(w0\*)/l(w_mid), l(w_mid)/l(w0\*)).
  F < 3 -> eingetroffen, sonst nicht eingetroffen. Faellt eine Schranke weg (kein negatives a2), zaehlt F = unendlich.
  **Nach Wortlaut** (die Karte nennt die Schranke als Achsen- bzw. Raumdiagonalen-Wert): konservativ und streng, je
  Photonzweig lo und hi (4 Faktoren): alle < 3 -> eingetroffen; alle >= 3 -> nicht eingetroffen; sonst geteilt.
- Bei Abweichung zwischen den Lesungen gilt fuer die Karte das Urteil nach Plan; das andere steht daneben.
- Beschreibend (kein Urteil): Vorzeichenwechsel von beta_L im F-43m-Schnitt (Strahlpunkte) und im Fd-3m-Gitter G; wo
  beta_L klein wird; Doppelbrechung; Schranken in m und in Planck-Laengen.

## 10. Laufliste [F]

- Nur .69, kleintest.sh, Spuren p4000a und p4000b, je Lauf <= 600 s. Arbeitsordner /home/fmh/fmhc-physics-remote/
  hoehe-isotrop-1/ (code/, alt/, lauf/, rauch/). alt/ enthaelt Kopien von REGULAER-V-1 lauf-69/kammer1.json und
  nachtrag-beta.json (Pruefsummen gegen lauf-69/PRUEFSUMMEN-69.txt).

| Lauf | Spur | Aufruf (code/hi.py ...) | Inhalt |
|---|---|---|---|
| H1 | p4000a | mitte lauf/mitte.json alt/kammer1.json alt/nachtrag-beta.json | HI0 (a), K1 bis K6 an w_mid, Licht und LHAASO an w_mid |
| H2 | p4000b | proben lauf/proben.json alt/kammer1.json | S1, S2, S3 mit Skalar und Licht |
| H3 | p4000a | strahlen 0 lauf/f43-0.json | F43, Richtungen 0..63 |
| H4 | p4000b | strahlen 1 lauf/f43-1.json | F43, Richtungen 64..127 |
| H5 | p4000a | null lauf/null.json | Abschn. 5, Licht an allen Nullpunkten, LHAASO an w0*, K2/K4/K5/K6 an w0* |
| H6 | p4000b | gitter lauf/gitter.json | G |
| H7 | p4000b | l2 lauf/l2.json | L2 (beschreibend) |
| H8 | p4000a | auswerten lauf/auswertung.json lauf/mitte.json lauf/proben.json lauf/f43-0.json lauf/f43-1.json lauf/null.json lauf/gitter.json [lauf/l2.json] | Urteile |

- Faellt ein Lauf aus (Fehler, 600 s), steht das im Ergebnis; ein Lauf zum Aufteilen wird dann mit derselben
  eingefrorenen Fassung wiederholt (z. B. halbe Richtungszahl ueber ein Argument, das schon im eingefrorenen Code steht).
- Eine Codeaenderung nach dem Einfrieren ist eine Selbstanzeige mit neuer eingefrorener Fassung.

## 11. Rauchtests und Einfrieren

- Rauchtest (<= 120 s, ueber kleintest.sh, nach diesem Plantext): code/hi.py rauch: Bau, K1, K2 an w_mid, K3, Laufzeit
  einer Licht-Messung (L = 1 und L = 2), Laufzeit einer Skalar-Messung. Der Rauchtest gibt keine a2-, beta- oder
  Schrankenwerte aus; ich lese nur das Log.
- Dazu Pfadtests mit verkleinerten Mengen (Schalter --rauch, im eingefrorenen Code): proben (6 Punkte), strahlen (2
  Richtungen), null (6 Richtungen, SLSQP maxiter 2 bzw. 3), gitter (m = 2), l2 (nur Mitte), mitte (voll, ~10 s) und
  auswerten auf diesen Dateien. Ich lese davon nur Laufzeiten, Fortschrittszeilen und rc; die JSON-Dateien und das Log
  von auswerten (es druckt Urteile der verkleinerten Mengen) lese ich nicht, ausser Fehlermeldungen (grep Traceback).
- Eingefroren werden PLAN.md und code/hi.py als Kopien *.eingefroren-<Zeit>, sha256 in EINGEFROREN-SHA256.txt (dazu die
  fuenf unveraenderten Kopien). Auf der .69 dieselben Pruefsummen.

## 11a. Rauchtests (gelaufen nach dem Plantext, vor dem Einfrieren; Text ab 13:42:39 CEST)

- Alle ueber kleintest.sh, Ausgaben nach rauch/ (UTC), alle rc = 0, alle unter 120 s:
  R1 p4000a rauch (11:40:21 bis 11:40:28); R2 p4000a mitte (11:41:01 bis 11:41:15); R3 p4000a null --rauch (11:41:15
  bis 11:41:33); R4 p4000a gitter --rauch (11:41:33 bis 11:41:40); R5 p4000b proben --rauch (11:41:01 bis 11:41:07);
  R6 p4000b strahlen 0 --rauch (11:41:07 bis 11:41:18); R7 p4000b l2 0 (11:41:18 bis 11:42:06, 47 s); R8 p4000a
  auswerten auf den Rauchdateien (11:42:32 bis 11:42:33).
- Gelesen habe ich nur R1 ganz (Kontrollen, Zeiten; keine Licht- oder beta-Werte) und von R2 bis R8 die Fortschritts-,
  Zeit- und Statuszeilen. Keine JSON-Datei, kein Urteil aus R8.
- Aus R1 [E]: Bau 10/68/116/58, Euler 0; K1 d1 d0 = 4e-16, Nullen 12 bei k = 0 (soll 12) und 10 bei kleinem k (soll
  10); K3 Skalar 9,5e-15; K2 I1/I2/I3 <= 7,8e-16 an Mitte und 3 Zufallsgewichten, Vorzeichen *2 = g; Diagnose an der
  Mitte null_rel 3e-11, luecke 514 (L = 1) bzw. 130 (L = 2). Zeiten: Licht-Messung L = 1 0,74 s, Skalar 0,15 s, Licht-op
  L = 2 0,13 s je k (Messung ~43 s). I3 ist damit auch numerisch bestaetigt.
- Aus R3 gesehen (Fortschrittszeile): Bei 6 Strahlen lief Stufe 1b (weniger als 3 Strahl-Nullpunkte); Stufe 2 und die
  Politur wurden im Rauchtest nicht durchlaufen. Ein Fehler dort wird im Hauptlauf abgefangen und im JSON ausgewiesen
  (try/except); die Strahl-Nullpunkte bleiben Kandidaten.
- Laufzeiten fuer die Hauptlaeufe daraus: H3/H4 je ~320 Proben x ~0,95 s ~ 5 min; H5 ~5 bis 9 min (Zeitwaechter);
  H6 ~5 min; H7 ~4 min.
- Keine Codeaenderung nach den Rauchtests.
