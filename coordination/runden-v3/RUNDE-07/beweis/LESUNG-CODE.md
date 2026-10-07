# LESUNG-CODE: Frische Gegenlesung von Code und Zertifikat (BEWEIS-1, M4)

- Leser: frischer Gegenleser (Claude, Haus Anthropic), kein Autor, keine Rechnung, keine Aenderung fremder Dateien.
- Beginn 2026-09-30 07:14:03 CEST (date). Ende: siehe letzte Zeile (date).
- Gelesen (ganz): BEWEIS.md, BEWEIS-PLAN.md, LESUNG-PLAN.md, STAND.md, BRIEF.md, zertifikat/bewkern.py,
  zertifikat/pruef.py, ZERT-A-L40.json, ZERT-B-L44.json, z0.json, z_start.json, SHA256SUMS.txt, LAUF-zertA-L40.log,
  LAUF-zertB-L44.log, LAUF-satzA.log, LAUF-satzB.log, LAUF-kontr1.log, LAUF-frei3.log, LAUF-start.log; in Auszuegen
  LAUF-newton3.log, LAUF-zert1..3.log, LAUF-api.log, LAUF-diag1.log, ZERT-1..3.json. Die Schrittprotokolle
  *-SCHRITTE-KASTEN.json nur mit jq (erster Schritt, Schritte um r = 3, um r = 7, letzte Schritte, Zaehlungen).
- Werkzeuge: Read, grep, sed, jq, sha256sum, date. Kein Interpreter, keine eigene Rechnung; Groessenordnungen nur
  im Kopf zur Plausibilitaet.
- Methode: jede Formel der Lemmata P, J, T, T0, K, Pos, E, R, W gegen den Code gehalten (Vorzeichen, Faktoren,
  Indizes, Reihenfolge der Komponenten); jede Zahl in BEWEIS.md gegen JSON und Log und zurueck; jede Stelle mit
  float, mid(), max(), Vergleich oder Rundung auf Richtung geprueft.

## Gesamturteil: BEWEIS TRAEGT MIT AUFLAGEN

Kein Fehler gefunden, der die strenge Kette bricht: Der Code setzt Lemma P, J, T, T0, K und Pos so um, wie sie in
BEWEIS-PLAN.md bewiesen sind; keine float64-Operation und kein mid() liegt in der strengen Kette; alle 26 Hashes in
SHA256SUMS.txt stimmen (sha256sum -c: OK); die Zertifikatszahlen decken sich mit BEWEIS.md; aus dem Gepruefte folgt
der Satzwortlaut ohne Uebertreibung. Die Auflagen betreffen Dokumentation und Protokoll: eine falsche Zahl in der
Pflichttabelle 3.2 (erster Schritt), drei in die falsche Richtung gerundete Untergrenzen, und ein Zertifikat, das
seine eigenen Laufparameter und den Code-Hash nicht enthaelt. Damit bleibt das Ergebnis "bewiesen (rechnergestuetzt,
linear, l = 0)" unter den zwei genannten Vertrauensannahmen (Software; und nun: diese Lesung statt "nur Selbstpruefung").

## 1. Code gegen Lemmata

### Lemma P (pruef.py tail_E, Zeilen 88-108): stimmt
- phibar := fs0 = 1,01 cab e^{-kappa0 L}/L (Z. 98), K = (2 + 1,5 phibar^2) e^{-2 kappa0 L}/(4 kappa0^2 L^2) (Z. 99),
  eta = 2 K cab^3 (Z. 100), m = cab + eta (Z. 101), Lambda = (6 + 7,5 phibar^2) m^2 e^{-2 kappa0 L}/(4 kappa0^2 L^2)
  (Z. 104): wie im Lemma. Die Bedingungen (i) fstar <= fs0, (ii) K m^3 <= eta, (iii) Lambda < 1, (iv) c.lower() >
  eta.upper() (Z. 103, 105) sind arb-Vergleiche, die nur dann True liefern, wenn die Relation fuer alle Punkte der
  Kugeln gilt (arb_le/arb_lt). Mit cab = obere Schranke von |c| ueber Z sind (i)-(iv) monoton in c, also fuer jedes z
  in Z erfuellt (Zusatz S).
- E_1 = s1 E0 eta0/L (Z. 107) und E_2 = s1 E0 (2 kappa0 eta0/L + eta0/L^2) (Z. 108) mit eta0 = K m^3: entspricht der
  Folgerung nach Lemma P; nachgerechnet ueber f' = (u' - f)/r und die Randwertformeln des Lemmas. Vorzeichen spielen
  keine Rolle, nur Betraege.
- kappa0, E0, E02 sind Kugeln ueber Z (om als Kugel), nicht Randwerte: keine Monotonie noetig.

### Lemma J (pruef.py 110-127): stimmt
- Q = (6 + 7,5 phibar^2) m^2 e^{-2 kappa0 L}/(2 kappa0 L^2) (Z. 112), mu = max(1/k, 1/(2 kappa_c)) aus oberen
  Schranken (Z. 113; (e^{mu Q} - 1)/mu ist wachsend in mu, also zulaessig), eps = e^{mu Q} - 1 (Z. 114),
  E_A = eps/(mu k), E_B = eps/(2 mu kappa_c), E_A' = (sqrt(1 + kappa_c^2/k^2) + kappa_c/k) eps/mu, E_B' = 1,5 eps/mu
  (Z. 115-118): wie im Lemma, Ableitungsschranken nachgerechnet.
- |E_{2+i}| <= s3 (E_A |A_i'| + E_B |B_i'| + E_A' |A_i| + E_B' |B_i|) (Z. 126-127) entspricht |W(E_J, R_i)| mit
  W = Psi.Phi' - Psi'.Phi. A, A' werden mit khat aus (al, be) zurueckgerechnet (Z. 124-125), passend zur Definition
  A' = khat(-al sin + be cos) in bewkern.py Kopf. Die Zustandswerte sind die Kugeln ueber Z (stZ, Z. 397).
- H_0,3 = s3 (B_1' + kappa_c B_1) = s3 W(J_0, R_1) mit J_0 = (0, 1, 0, -kappa_c): evalH Z. 67-68, Spaltenordnung
  (al, be, B, B') stimmt mit initial_state (Z. 513-514) und M_complex Zeile 3 (B'' = Q B + C A).

### Lemma T, Cauchy-Rest (bewkern.py step 456-501, apriori 350-438): stimmt
- Einschlusstest: rhs(B) = Y0 + Dt F(Dt, B) (Z. 375-414), Test contains_all(B, rhs(B)) (Z. 426) mit acb.contains.
  Suche (Inflation 9/8, hoechstens 14 Runden, Z. 422-435) und Pruefung sind getrennt (Auflage K5).
- Dt = Quadrat mit Halbseite R (Z. 353) enthaelt die Kreisscheibe; sin/cos ueber khat (rj + Dt) (Z. 362-364),
  1/(rj + Dt) (Z. 361), N(B_f), N'(B_f) auf der Huelle (Z. 378, 389).
- 2/r beim Profil: `if not (R < rj): raise Fehler("R >= rj")` (Z. 359) in Kugelarithmetik mit exakten Dyadiken; im
  Gitter R <= r_j/2 (integrate Z. 567, rfrac = 0,5). Zaehlung mit jq: 0 Schritte mit R >= r_j (r_j > 0) in A und B.
- Rest: tailfac = q^N/(1 - q) (Z. 459-460), beta = acb_beta(B) = rad(Re) + rad(Im) (Z. 284-286, obere Schranke fuer
  den groessten Abstand eines Rechteckpunkts zur Mitte), Rest = beta tailfac als Kugel [0 +- ...] zum Horner-Wert
  addiert (Z. 472-473, 486, 495-496). Die Cauchy-Koeffizienten n < N kommen aus den Rekursionen (prof_series 102-123,
  var_series 144-153, lin_recursion 235-263), die Reste decken n >= N. Kugelzuordnung Komponente <-> Rest: Reihenfolge
  [f, g, pa, qa, pw, qw, Y zeilenweise] in apriori (Z. 416) und step (Z. 471-496) gleich.

### Lemma T0, Start bei r = 0 (bewkern.py 126-141, 156-164, 380-381, 390-393, 463-464, 479-481): stimmt
- Integralform: nf = a + Dt2 N(B_f)/6, ng = Dt N(B_f)/3 (Z. 380-381) mit Dt2 = Quadrat der Halbseite R^2 (Z. 356),
  entsprechend f = a + r^2 int tau(1 - tau) N, f' = r int tau^2 N (int tau(1-tau) = 1/6, int tau^2 = 1/3).
  Fuer die Variationen gleich (Z. 391-393) mit Quelle N'(f) phi (+ (-2 om) f fuer phi_om).
- Rekursion f_{n+2} = N_n/((n+2)(n+3)) (Z. 136), g_n = (n+1) f_{n+1} (Z. 140), var_series0 gleich (Z. 162-163).
  Rest fuer g aus B_g (tails[1], Auflage K4).
- Das lineare System ist bei 0 regulaer (keine 1/r-Terme in M_complex, Z. 289-301) und laeuft mit der Standardform
  Y0 + Dt F (Z. 413).
- N0 = 2N (integrate Z. 550), q = h0/R = 1/2 (Z. 553).

### Rekursionen gegen die Gleichungen: stimmt
- Profil: w_n = (-1)^n/r_j^{n+1} (Z. 104-108) als Reihe von 1/(r_j + t); g_{n+1} = (N_n - 2 [g w]_n)/(n+1) (Z. 120);
  N_n = kap0sq f_n - 2 [f S]_n + 1,5 [f T]_n, S = f^2, T = S^2 (Z. 113-118): N(f) = (1 - om^2) f - 2 f^3 + 1,5 f^5.
- Linear: dV = 4,5 T - 4 S (Z. 170), C = 3 T - 2 S (Z. 171), P = dV + khat^2 - k^2 (Z. 172-173, Par Z. 61),
  Q = dV + kappa_c^2 (Z. 174-175): V_+ = dV - k^2 = -khat^2 + P, V_- = dV + kappa_c^2. Variation der Konstanten:
  al' = -(sin/khat)(P A + C B), be' = (cos/khat)(P A + C B) mit A = al cos + be sin: Zeilen 0-1 der Matrix (Z. 184-185,
  M_complex 298-299) stimmen (sc = sin cos, ss = sin^2, cc = cos^2). trig_series (Z. 69-98): Ableitungszyklen von
  cos, sin, sin(2x)/2, (1 - cos 2x)/2, (1 + cos 2x)/2 nachgerechnet.
- Jets (Zusatz J): d_p S = 2 f phi_p (Z. 194-195), d dV = (9S - 4) dS (Z. 198, 200), dC = (6S - 2) dS (Z. 199, 201),
  d_rho P = -2(om + rho), d_rho Q = 2(om - rho), d_om P = -2(om + rho) + ddV, d_om Q = -2(om - rho) + ddV
  (Par Z. 62-65, Z. 205-208): stimmen. lin_recursion mit Zusatz Mps * Yb (Z. 249-260) und Mp_complex (Z. 304-329)
  haben dieselbe Blockstruktur [M_a; M_rho; M_om] (12x4). Anfangswerte der Jets: Spalten 2-7 von Y sind 0, weil
  die Anfangsdaten (0, 1/khat, 0, 0) und (0, 0, 0, 1) nicht von (a, rho, om) abhaengen; phi_a(0) = 1, phi_om(0) = 0
  (Z. 510).
- H_0 und DH_0 (pruef.py evalH 65-83): d_om e^{-kappa0 L} = E0 L om/kappa0 (Z. 71), d_om kappa0 = -om/kappa0 (Z. 72),
  d_rho kappa_c = (om - rho)/kappa_c, d_om kappa_c = -(om - rho)/kappa_c (Z. 73-74), c-Spalte (-s1 E0/L,
  s1 (kappa0 + 1/L) E0/L, 0, 0), rho-Spalte der Profilzeilen 0: alle richtig. Spaltenzuordnung [R1 R2 | d_a | d_rho |
  d_om] in Z. 80-83 passt zu lin_recursion (Z. 260). T2 (kontr1) bestaetigt die Jacobi-Matrix gegen
  Differenzenquotienten mit rel. <= 2e-14 (LAUF-kontr1.log).

### Lemma K, Krawczyk-Brouwer (pruef.py 403-416): stimmt
- Kr = z0 - Y H_0(z0) + (I - Y D)(Z - z0) + |Y| [-eps, eps] (Z. 404-407) mit Y exakt dyadisch (Z. 367-368),
  D = DHZ ueber Z (Z. 391), eps ueber Z (Z. 397), H_0(z0) am Punkt (Z. 357).
- Einschluss je Koordinate: Kr.lower() > z0 - delta und Kr.upper() < z0 + delta (Z. 411), strikt, also Kr im Innern
  von Z. Die rechten Seiten sind Kugeln (Rundung der Differenz z0 - delta bei 256 bit), der arb-Vergleich verlangt
  die Relation gegen jeden Punkt der Kugel: konservativ.
- Kastengewichtete Zeilensumme max_i sum_j |I - Y D|_ij delta_j/delta_i (Z. 408) und Test < 1 (Z. 416): wie Lemma K.
  Perron-Frobenius-Schluss im Lemma nachgerechnet (P delta < delta => rho(P) < 1).
- Der Kasten Zb fuer D und eps (Z. 389) hat den Radius delta als mag (aufgerundet), ist also eine Obermenge von Z:
  konservativ. Der Einschlusstest laeuft gegen das exakte Z.

### Lemma Pos (pruef.py positivity 330-346): stimmt
- f_lo, f_hi je Schritt sind Realteil der A-priori-Huelle (bewkern.py Z. 498-500), gueltig auf [r_j - R, r_j + R]
  und damit auf [r_j, r_j + h]. L_p = Ende des letzten Schritts mit f_lo > 0 (Z. 339-343); der erste Schritt mit
  f_lo <= 0 (A: r_j = 7,04754638671875, f_lo = -0,00349) und alle folgenden werden gegen |f| < thr geprueft
  (Z. 344-345), thr = untere Schranke von sqrt(S_-) mit kap0sq ueber Z (Z. 333-334). jq: ab r_j >= 7,04 ist
  max f_hi = 0,0930, min f_lo = -0,0130 (A); B: L_p = 7,356, max f_hi = 0,0842. Minimumprinzip im Lemma
  nachgerechnet (u = r f, u'' = V u, V > 0 fuer f^2 < S_-).

### Lemma E (BEWEIS-PLAN Abschnitt 4): stimmt
- Nachgerechnet: Phi, Phi' -> 0 aus L^2 und Phi'' = M Phi; Volterra-Kerne der oszillierenden Loesungen mit
  kt(s) = max(1/k, e^{kappa_c (s - L)}/(2 kappa_c)) und Qt endlich wegen 2 kappa0 > kappa_c (Z: >= 0,375);
  W(Psi_c, Psi_s) = k, W(Psi, Psi_c) = W(Psi, Psi_s) = 0, W nichtausgeartet, V3 dreidimensional, W-Komplement
  eindimensional = span{Psi}. Der Green-Kern sinh(kappa_c (s - r))/kappa_c loest B'' - kappa_c^2 B = g
  (nachdifferenziert) und ist derselbe wie in Lemma J (dort in den Tilde-Variablen als (1 - e^{-2 kappa_c (s-r)})/
  (2 kappa_c)).

### Konsistenz der zwei Rechenwege (A-priori-Rechte-Seite gegen Rekursion)
- Die A-priori-Huelle nutzt Nf, Npf, M_complex, Mp_complex; die Koeffizienten nutzen prof_series, var_series,
  lin_M_series, lin_Mp_series. Beide implementieren dieselben Gleichungen (Term fuer Term verglichen). T1 (kontr1)
  bestaetigt das bei r = 3 bis auf 5e-8; siehe K6 zur Deutung "nur Radien".

## 2. Rundung

- Strenge Kette (Punktlauf, Kastenlauf, tail_E, Krawczyk, Positivitaet): nur arb/acb bei ctx.prec = 256 bzw. 320.
  Gitter exakt in Fraction (integrate Z. 544-597), Umwandlung per fr_arb mit Zweierpotenz-Assert (Z. 533-537),
  dyf = exakte Abrundung auf dyadische Zahl (Z. 527-530); Endpunkt exakt (assert rjf == L, Z. 597).
- float nur bei: shoot_float/start_a/c_from_float (Startwerte), consts (Skalen s1, s3; die Parameter kap0_f, kapc_f
  sind floats, werden exakt in arb gewandelt und dann auf feste Dyadiken gerundet; khat_f wird nicht benutzt),
  relw/stepstats/schrittinfo/float(Lp) (Protokoll), Newton (nicht streng). Keine dieser Stellen beeinflusst
  einen Kugelwert der strengen Kette.
- mid() nur bei: Vorkonditionierer Y (Z. 367), Yp fuer M1 (Z. 428-430), delta-Wahl (arb_round Z. 381; beliebiges
  positives delta ist zulaessig), dy_str fuer exakte Werte, inflate_acb in der Huellen-Suche (danach
  Einschlusstest), Kontrollen. Nirgends wird ein mid() genommen, wo eine Huelle gebraucht wird.
- Dyadische Uebergabe: z0, khat als (Mantisse, Exponent) mit assert is_exact (Z. 26-30); delta = arb_round(...)
  exakt, .upper() eines exakten Werts ist der Wert selbst; Z = z0 +- delta im Test exakt; Zb mit mag-Radius
  (aufgerundet) fuer D und eps.
- Vergleiche: alle Bedingungen ueber `bool(arb <op> arb)` (Lemma P (i)-(iv), Lip < 1, rowsum < 1, Kanaele,
  Positivitaet, R < rj): python-flint bildet auf arb_lt/arb_le/arb_gt/arb_ge ab, die nur bei sicherer Relation
  True liefern.
- Einzige nicht saubere Stelle: Python-max ueber Kugeln bei rowsum (Z. 408), rs2 (Z. 438), rs_unw (Z. 474). Bei
  ueberlappenden Kugeln ist die Auswahl nicht die strenge obere Schranke. Hier ohne Folge (Kugelradien ~1e-17
  relativ gegen Werte 5,7e-9 und Schwelle 1): siehe K5.

## 3. Zahlen in beide Richtungen

Geprueft mit sha256sum, jq, grep gegen ZERT-A-L40.json, ZERT-B-L44.json, LAUF-*.log:
- sha256: alle 26 Eintraege von SHA256SUMS.txt stimmen (sha256sum -c, rc = 0); die sieben in BEWEIS.md 4 genannten
  Hashes stimmen mit den lokalen Dateien. Die Gleichheit mit den Kopien auf der .69 (BEWEIS.md: "geprueft 07:09:37")
  konnte ich von hier nicht pruefen.
- Tabelle Z (BEWEIS.md 1) gegen protokoll.Z: alle acht Grenzen nach aussen gerundet, richtig. omega^2, rho, kappa0,
  kappa_c: gegen LAUF-satzA.log richtig (4,74e-22 -> 4,8e-22 usw.). Lauf-B-Kasten gegen LAUF-satzB.log richtig.
- Tabelle 3.1: Laufzeiten 50,6 s (Service 50,552 s), 69,9 s (1 min 9,863 s), 78,2 s, 3,8 s, 297 s: richtig.
- Tabelle 3.2: khat, s1, s3, Schrittzahlen 324/328, R- und h-Bereiche, Reste 3,4e-30 und 7,7e-13, H_0(z0), delta,
  eps_1..4, Lemma-P-Zahlen (i)-(iv), K, m, Lemma-J-Zahlen, Zeilensummen 5,68e-9 und 27253, D-Breite 1,9e-9, M1, M2,
  L_p = 7,0475, Schwelle 0,3320894957: richtig.
- Abweichungen:
  1. "erster Schritt (Reihe um 0) | R0 = 1, h0 = 1/2" (BEWEIS.md 3.2; BEWEIS-PLAN 6 und Lemma T0-Umfeld): Das
     Schrittprotokoll zeigt fuer den angenommenen ersten Schritt in A und B R = 0,203125 = 13/64, h = 0,1015625 =
     13/128 (r_ende "13/128"), Inflationsrunden 10. R0 = 1 war nur der Startversuch (integrate Z. 552-560 verkleinert
     R siebenmal um 4/5 mit dyf(., 8): 1 -> 204/256 -> 163/256 -> 130/256 -> 104/256 -> 83/256 -> 66/256 -> 52/256).
     q = 1/2 und Ordnung 2N stimmen. -> W1.
  2. Drei Untergrenzen in Tabelle 3.2 sind zur naechsten Stelle statt nach unten gerundet: "kappa_c^2 >= 0,274965"
     (Zertifikat 0,274964756794439), "(1 + omega) - rho >= 0,148510" (0,148509986432), "2 omega^2 - 1 >= 0,595354"
     (0,595353574224). Im Satz (Abschnitt 1) stehen die richtig abgerundeten Werte 0,27496 und 0,14850. -> K1.
  3. "K_J <= 1 + 1e-16" (Satz 2 und Tabelle 3.2) ist nur durch die Logzeile gedeckt (K_J = 1,0000000000000000757 in
     LAUF-zertA-L40.log); das JSON traegt K_J nur mit 8 Stellen "[1.0000000 +/- 2e-12]". -> K2.
  4. Das Zertifikat-JSON enthaelt keine Laufparameter (N, Nbox, q, Rmax, kfak, N0) und keinen Hash des erzeugenden
     Codes; q laesst sich nur aus h/R im Schrittprotokoll ablesen (A: 0,3333, B: 0,25), N und Nbox gar nicht. Die
     Bindung Code <-> Zertifikat steht allein in BEWEIS.md 4. -> K3.
  5. BEWEIS.md 4 nennt die Hashes von Interpreter und libflint nur mit 8 Hex-Zeichen ("e50d468e...", "871a4132..."):
     so nicht pruefbar. -> K4.
- Rueckrichtung (JSON -> Text): alle Felder von M3, M1, M2, negativkontrolle, lemma_info, protokoll.kanaele,
  lemma_P, lemma_J, schritte_punkt, schritte_kasten, software finden sich in BEWEIS.md wieder oder sind dort
  zusammengefasst (Lauf B nur als Kasten und Laufzeit; L_p(B) = 7,356 fehlt, ist aber nicht tragend).

## 4. Satz gegen Zertifikat

- Positivitaet auf [0, oo): [0, L_p] aus den Huellen des Kastenlaufs (fuer alle z in Z), [L_p, L] Minimumprinzip mit
  |f| < 0,332 (Protokoll klein_danach = true) und u(L) > 0 aus Lemma P (c - eta > 0), [L, oo) Lemma P: gedeckt.
- Abfall: |A| + |B| <= K_J e^{-kappa_c r} fuer r >= L aus Lemma J; fuer r < L nur Fortsetzung (der Satz behauptet
  den Abfall nur ab L): gedeckt.
- Einfachheit: Lemma E mit 2 kappa0 - kappa_c >= 0,375 ueber Z (Protokoll): gedeckt. Hinweis: Diese Zahl geht nicht in
  das BESTANDEN-Flag ein (zert Z. 423), steht aber im Protokoll; der Satz beruft sich auf das Protokoll. In Ordnung.
- rho strikt im Fenster: k^2 >= 5,9577, kappa_c^2 >= 0,27496 ueber Z (Kugeln, nicht Randwerte): gedeckt.
- Kette H(z*) = 0 => globales Profil und Psi(0) = 0: Lemma W nachgerechnet (W konstant, W(Psi, R_i)(0) = Psi_i(0));
  H_3 = H_4 = 0 heisst nach Lemma W genau Psi(0) = 0. Am Punkt ist zusaetzlich sichtbar, dass beide regulaeren
  Loesungen keinen wachsenden B-Anteil haben (H_0,3, H_0,4 ~ 1e-27): das ist mit der Lagrange-Eigenschaft von
  span{R_1, R_2} vertraeglich und kein Widerspruch.
- Uebertreibung: keine gefunden. "Vollstaendig streng" ist mit den zwei Vertrauensannahmen richtig eingegrenzt;
  "nicht behauptet" deckt Eindeutigkeit von z*, weitere Nullstellen, l > 0, wesentliches Spektrum, nichtlineare
  Strahlung. Die Formulierung "Selbst gegengelesen ... Gegenlesung des Codes durch ein zweites Haus steht aus" ist mit
  dieser Lesung zu aktualisieren (K7).
- Lemma K: E stetig auf Z (Zusatz S nachgelesen, Kugel X' mit |u~| <= m, Kontraktionsschluss richtig), (i)-(iv) fuer
  jedes z in Z durch Monotonie in c und Kugelauswertung in om: gedeckt.

## 5. Negativ- und Kontrolltests

- Negativkontrolle (zert Z. 451-460): Kastenmitte rho + 4 delta, gleiche Matrix Mk, gleicher Kasten; Test verfehlt in
  der rho-Komponente (A und B). Sie beweist, dass der Einschlusstest nicht trivial erfuellt ist. Sie ist nach
  Konstruktion fast sicher verfehlt (Verschiebung 4 delta gegen Innenrand delta/8), prueft also nur die Empfindlichkeit,
  nicht die Strenge. Ausreichend fuer den Zweck; siehe K8 fuer eine schaerfere Variante.
- Frei-Test (f = 0, Z. 226-249): vier Zustandsgroessen bei L = 40 gegen geschlossene Loesungen, Test mit overlaps,
  bestanden; 25 gedruckte Stellen gleich; B_1(L), A_2(L) als reine Nullkugeln (1e-88, 1e-96). Deckt lineare Rekursion,
  Trig-Reihen, (al, be)-Transformation mit khat != k, Reste und Gitter ab. Deckt nicht: Profil, f-abhaengige
  Koeffizienten, Jets.
- T1 (kontrolle Z. 531-561): A-priori-Rechte-Seite gegen Rekursion (Ordnung 0 und 1, inkl. Jets) bei r = 3:
  <= 5,4e-8. Das schliesst Vorzeichen- oder Faktorfehler in den f-abhaengigen Termen aus (dort waeren die Abweichungen
  O(1e-1) bei f ~ 0,5). Ob die Restabweichung "nur Radien" ist, laesst sich aus dem Log nicht pruefen, weil die
  Zustandsradien bei r = 3 nicht ausgegeben werden (im Kastenlauf A liegt die relative Breite von f bei r = 3 bei
  3e-17 bis 1,6e-16; kontr1 rechnet mit N = 32 und q = 1/4, also groeberen Resten; der Wert 5e-8 ist plausibel, aber
  nicht belegt). -> K6.
- T2 (Z. 563-577): Differenzenquotienten gegen Jacobi-Matrix, rel. <= 2e-14 fuer alle nichtstrukturellen Eintraege:
  bestaetigt Variationsgleichungen, Kettenregel-Terme und die expliziten Ableitungen in evalH.
- Wiederholung B (L = 44, 320 bit, q = 1/4, N = 72/44): eigener Punkt- und Kastenlauf, anderes s1, s3, anderes
  Gitter; Kasten im Innern von Z_A. Gute Stuetze, aber derselbe Code (kein zweites Programm; Luecke 3 bleibt).

## Befundliste

Schweregrade wie in LESUNG-PLAN.md: blockierend, wesentlich, klein.

### Blockierend: keiner.

### W1 (wesentlich, Dokumentation; beruehrt die Gueltigkeit nicht): erster Schritt falsch angegeben
BEWEIS.md 3.2 ("R0 = 1, h0 = 1/2") und BEWEIS-PLAN.md 6 beschreiben den Startversuch, nicht den angenommenen Schritt.
Zertifikat (A und B): R = 13/64, h0 = 13/128, Inflationsrunden 10, Rest 1,07e-27 (A) bzw. 2,75e-25 (B).
Anforderung: "In BEWEIS.md 3.2 und BEWEIS-PLAN.md 6 schreiben: 'erster Schritt (Reihe um 0): Startversuch R0 = 1,
angenommen nach sieben Verkleinerungen R = 13/64 = 0,203125, h0 = 13/128, q = 1/2, Ordnung 2N = 96 (A) bzw. 88 (B),
Inflationsrunden 10, Rest 1,07e-27 (A), 2,75e-25 (B); die Reihe um 0 traegt also bis r = 13/128, danach Lemma T.'"

### K1 (klein): drei Untergrenzen in Tabelle 3.2 aufgerundet
Anforderung: "In Tabelle 3.2 schreiben: kappa_c^2 >= 0,274964, (1 + omega) - rho >= 0,148509, 2 omega^2 - 1 >=
0,595353 (oder mehr Stellen, immer abgerundet). Regel im Text: Untergrenzen werden abgerundet, Obergrenzen
aufgerundet."

### K2 (klein): K_J-Schranke nur im Log
Anforderung: "protokoll.lemma_J im JSON mit mindestens 20 Stellen ausgeben (str(20)) oder in BEWEIS.md 3.2 die
Logzeile als Quelle nennen: 'K_J = 1 + 7,6e-17 (LAUF-zertA-L40.log)'."

### K3 (klein): Zertifikat nicht selbstbeschreibend
Anforderung: "pruef.py schreibt in das JSON die Laufparameter (N, N0, Nbox, q, Rmax, kfak, Lz) und die sha256 von
bewkern.py und pruef.py (zur Laufzeit gelesen). Bis dahin: In BEWEIS.md 4 vermerken, dass die Bindung Code <->
Zertifikat nur ueber die Kommandozeilen und die Hashliste besteht." Kein Neulauf noetig fuer das Urteil; bei einem
ohnehin anstehenden Neulauf mitnehmen.

### K4 (klein): Hashes von Interpreter und libflint verkuerzt
Anforderung: "In BEWEIS.md 4 die vollen sha256 von /usr/bin/python3.12 und libflint-6839011d.so.24.0.0 (und
libgmp, libmpfr) eintragen oder eine Datei zertifikat/SOFTWARE-SHA256.txt anlegen."

### K5 (klein): Python-max ueber Kugeln
pruef.py Z. 408, 438, 474: max() ueber arb-Kugeln waehlt bei Ueberlappung nicht die strenge obere Schranke. Ohne
Folge (Abstand zur Schwelle 1 ist acht Groessenordnungen).
Anforderung: "rowsum, rs2, rs_unw als max ueber .upper() der Summanden bilden, oder im Text vermerken, dass die
Zeilensummen exakte obere Schranken je Zeile sind und das max nur der Berichtswert ist."

### K6 (klein): T1-Deutung "nur Radien" nicht belegt
Anforderung: "Im T1-Log die Radien von f, g, Y (max) und der Jets bei r = 3 ausgeben und die Differenz der
Mittelpunkte getrennt von der Summe der Radien nennen; oder in BEWEIS.md 3.1 schreiben: 'T1 <= 5e-8 (Groessenordnung
der Kugelradien; nicht getrennt ausgewiesen)'."

### K7 (klein): Wortlaut zur Gegenlesung
Anforderung: "BEWEIS.md Ergebnis und Lueckenliste 1: 'Code-Gegenlesung durch ein zweites Haus fehlt' ersetzen durch
'Code und Zertifikat frisch gegengelesen (LESUNG-CODE.md, 30.09.): traegt mit Auflagen W1, K1-K8; eine Lesung aus
einem fremden Haus und ein zweites unabhaengiges Programm fehlen weiterhin.'"

### K8 (klein, optional): schaerfere Negativkontrolle
Anforderung: "Zusaetzlich eine Verschiebung um delta/4 und um delta rechnen; erwartet: delta/4 besteht (Innenrand
delta/8 plus Verschiebung), delta verfehlt. Das zeigt, wo der Test kippt, statt nur dass er kippt."

### Nicht beanstandet, aber notiert
- Schrittprotokoll enthaelt nicht die Huelle B und keinen expliziten Testausgang je Schritt (K5 der Plan-Lesung
  verlangte beides); der Testausgang folgt daraus, dass der Lauf ohne Fehler endete (jeder Schritt wird nur mit
  bestandenem Test angenommen, bewkern.py Z. 426-427, 577-583).
- consts() hat einen unbenutzten Parameter khat_f (pruef.py Z. 51). Ohne Wirkung.
- L_p des Laufs B (7,356) steht nicht in BEWEIS.md. Nicht tragend.

## Gepruefte Stellen (Datei:Zeile)

bewkern.py: 18-20 (Konstanten 3/2, 9/2, 15/2); 27-50 (conv, sqc, pmul; Nullauffuellung); 53-66 (Par: kap0sq, ksq,
kapcsq, Pc, dPr, dQr, dPw, dQw, src_w); 69-98 (trig_series); 102-123 (prof_series, w_n, Rekursion); 126-141
(prof_series0); 144-164 (var_series, var_series0); 168-188 (lin_M_series); 191-232 (lin_Mp_series); 235-263
(lin_recursion, Jet-Zusatz, Yb-Fortschreibung); 271-287 (inflate_acb, contains_all, acb_beta); 289-329 (M_complex,
Mp_complex); 332-339 (Nf, Npf); 350-438 (apriori: 353 Dt, 356 Dt2, 359 R < rj, 361 WD, 362-364 sin/cos, 375-414 rhs,
416-420 Start, 422-435 Suche, 426 Test); 442-453 (horner, horner_mat); 456-501 (step: 459-460 q, tailfac; 463-469
Reihen; 471-473 Reste f, g; 476-489 Jets; 493-496 Y mit Restmatrix; 498-500 Realhuelle); 504-516 (initial_state);
519-537 (relw, dyf, fr_arb); 540-598 (integrate: 544-546 Fraction, 549-563 erster Schritt, 566-597 Gitter, 597 assert).

pruef.py: 20-47 (dy_str, dy_arb mit is_exact, arb_round); 51-54 (consts); 57-84 (evalH: 61-63 kappa0, kapc, E0; 65-68
H_0; 71-74 Ableitungen; 76-83 DH); 88-133 (tail_E: 92-96 L, kappa0, E0, E02, cab; 98-108 Lemma P; 110-118 Lemma J;
119-127 W-Schranke; 128-133 Protokoll); 137-191 (float-Startwerte, nicht streng); 194-202 (Newton-Hilfen); 205-317
(main: 223 prec, 226-249 frei, 250-266 start, 267-271 z laden, 272-296 newton, 303-317 satz); 321-327; 330-346
(positivity); 349-520 (zert: 351-354 L, s1, s3; 357 Punkt; 364-368 Y; 372-386 delta; 389-391 Kasten; 397-401 eps;
403-416 Krawczyk; 418-426 M3; 428-442 M1; 443-450 M2; 451-460 Negativkontrolle; 462-509 Protokoll; 510-520 Ausgabe);
523-578 (kontrolle T1, T2).

Zertifikate/Logs: ZERT-A-L40.json und ZERT-B-L44.json (alle Felder), z0.json, z_start.json, SHA256SUMS.txt,
LAUF-zertA-L40.log, LAUF-zertB-L44.log, LAUF-satzA.log, LAUF-satzB.log, LAUF-kontr1.log, LAUF-frei3.log,
LAUF-newton3.log (Radien H, Zeiten), LAUF-zert1..3.log (Parameter, Ergebnisse), ZERT-1..3.json (delta, rowsum, eps),
*-SCHRITTE-KASTEN.json per jq (Schritt 0; Schritte mit r_j in (2,7; 3,3), (6,5; 7,6); letzte zwei; Zaehlung R >= r_j;
max Inflationsrunden 13, max Fehlversuche 4, Summe 186 (A); Positivitaetsgrenzen).

## Was ich nicht getan habe

Keine Rechnung, kein Interpreter, keine Aenderung an BEWEIS.md, BEWEIS-PLAN.md, STAND.md, Code oder Zertifikaten,
kein git, kein Journaleintrag, kein Zugriff auf die .69 (die Gleichheit der dortigen Kopien mit den lokalen Dateien
bleibt Aussage des Autors). Die Korrektheit von python-flint/FLINT (Kugelarithmetik, acb_contains, arb_poly-Produkte)
bleibt Vertrauensannahme, wie in BEWEIS.md 5.2 gefuehrt.

- Ende 2026-09-30 08:03:32 CEST (date). Dauer 49 min 29 s.
