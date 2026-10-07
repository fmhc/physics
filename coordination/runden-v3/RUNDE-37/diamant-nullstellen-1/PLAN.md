# DIAMANT-NULLSTELLEN-1: Plan (Runde 44, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Arbeitsplatz RUNDE-37/diamant-nullstellen-1/, Rechenort .69
  (/home/fmh/fmhc-physics-remote/diamant-nullstellen-1/), Spuren cpu und cpu11.
- **Zeiten (date):** Start 2026-10-04 23:03:22 CEST. Code ab etwa 23:13, Rauchtest 23:15:55 CEST (nur Laufzeiten und
  Schluessel gesehen, 2,3 s), dieser Plan ab 23:16:07 CEST. Zeitbox bis 23:48 CEST.
- **Kennzeichen:** [M] eigene Mathematik von Hand (ungeprueft), [E] gerechnet, [P] Projektdatei, [S] Quelle, [H] Hypothese,
  [F] Festlegung dieses Plans. Alles ist synthetische Rechnung an einem gedachten Netz, keine Messdaten.

## 0. Gelesen und Projektsuche

- KARTE.md (bindend), diamant-fermion-l/DOSSIER.md ganz, ARBEITSFELD.md Abschnitte 1.1 bis 1.5 (Z. 21-110),
  licht-finn-netz-1/PLAN.md und code/licht_netz.py ganz, runden-v3/README.md, Kopf von kleintest.sh (lokal und .69).
- **Projektsuche** (grep -rl mit allen Ausschluessen der Karte, dazu .git) nach "Knotenlinie", "Nullstellen", "FKM",
  "Fu-Kane", "Fu, Kane", "Kane/Mele", "nodal line", "Knotenschleife":
  - Knotenlinien auf dem Diamant gibt es im Projekt nur fuer andere Operatoren: KITAEV-DIAMANT-1 (Majorana-Spektrum,
    Knotenlinien entlang X-W, ERGEBNIS Z. 32 und 58), QCA-DIAMANT-4 (ERGEBNIS Z. 177, "deutet auf Knotenlinien"),
    QCA-TETRA-1 (Z. 45, 163), TENSOR-EIS-PYRO-1 / KOPPLUNG-TETRA-1 (Nullstellenebenen einer anderen Determinante),
    LICHT-GLEICH-L G6 und WELTMODELL-REVIEW-1 L5 (Fluss 0 gibt keine Dirac-Kegel; Levin/Wen).
  - FKM, Fu-Kane, Kane/Mele: nur DIAMANT-FERMION-L selbst, RUNDE-44.md (Z. 230, 341, 349) und Scout-Cache-Treffer
    (nicht gelesen). Keine Projektrechnung von FKM.
  - Nullstellen: viele fachfremde Treffer (Q-Ball, Kausal-Netze, Regge, Gauntlet-Prompts); SPIN-ZUFALLSNETZ-1 fragt nach
    Dopplern des kubischen Weyl-Operators auf Zufallsnetzen, nicht nach W-D auf dem periodischen Diamant.
  - **Ergebnis:** Kein Projektwert fuer Nullstellen von W-D, W-D+S3 oder FKM. Fuer W-D gibt es nur das Tempo 0,8165,
    a1 = +-0,3536 (110) und a3 = 0,02946 (110) aus LICHT-FINN-NETZ-1 lauf-69/ergebnis.json [P].

## 1. Ableitbarkeitsprobe: Pruefung der Vorab-Ableitungen des feldforschers [M, von Hand, vor jeder Rechnung]

Bezeichnungen: V(k) = sum_s w_s sum_v v e^{ik.(a/4)v} (v ganzzahlig), M = (i/2) sigma.V, R = Re V, I = Im V.

1. **det M und Nullstellen.** (sigma.V)(sigma.V*) = abs(R)^2 + abs(I)^2 + 2 sigma.(R x I). Also
   E^2 = (1/4)[abs(R)^2 + abs(I)^2 +- 2 abs(R x I)], und E = 0 genau fuer V.V = 0 (R senkrecht I, abs(R) = abs(I)).
   Zwei reelle Bedingungen, generisch Linien. **Stimmt** (ARBEITSFELD 1.5).
2. **Schleife durch W und (1; 0,392; 0,392) 2 pi/a.** Auf k = (2 pi/a)(1, u, v) ist V_x rein imaginaer und V_y, V_z
   reell (Paare (p,q,r) und (p,-q,-r) liegen beide in der Schale), also R senkrecht I auf der ganzen Ebene. Nachgerechnet:
   V = (2/sqrt3)(i (cos al + cos be), sin be - sin al, -(sin al + sin be)), Nullbedingung
   2 sin^2 al + 2 sin^2 be = (cos al + cos be)^2. W = (1; 0,5; 0): 2 = 2, **stimmt**. Diagonale u = v: cos al = 1/3,
   u = arccos(1/3)/pi = 0,39183, **stimmt**. Faltung mit G = (1,1,1) 2 pi/a: V(k+G) = -i V(k) (alle A->B-Vektoren haben
   Koordinatensumme 3 mod 4), (0; -0,608; -0,608), abs(k) = 1,91 pro PU, **stimmt**.
3. **W-D+S3, a1 = 0.** Schale 3 (12 Vektoren, Produkt -3): drittes Moment Schale 1 +4, Schale 3 -36; sigma.q-Glied
   ~ 4 w1 - 36 w3 = 0 bei w3 = w1/9. Andere dritte Momente (sum v_x^3, sum v_x v_y^2) sind in beiden Schalen null.
   **Stimmt.** Tempo: 4 w1 + 44 w3 = (80/9) w1, also v = (20/9) 0,8165 = 1,8144 (in W-D-Einheiten).
4. **FKM bei t = 4 lambda.** Aus der Ortsraum-Definition i (8 lambda/a^2) sigma.(d1 x d2) folgt die d-Vektor-Form mit
   Vorfaktor **2 lambda** fuer d3, d4, d5 (abs(d1 x d2) = sqrt2 a^2/8; Hin- und Rueckweg mit entgegengesetztem c; Untergitter
   B mit -c). An X_z: d2 = -t a q_z, d3 = -4 lambda a q_x, d4 = 4 lambda a q_y, d1 und d5 hoeherer Ordnung. Laengs t a,
   quer 4 lambda a: **isotrop bei t = 4 lambda, stimmt**. Spaltung 0 aus P T (jedes Band zweifach): **stimmt** als Argument.
5. **Die "offenen" Groessen sind ebenfalls ableitbar** (Regel "vorab ableitbare Kennzahl ist keine Messung"):
   - **DN1 (Knotenlinien von W-D+S3) [M]:** Auf der Ebene k_x = 2 pi/a gilt R senkrecht I fuer jede Schalenmischung
     (Punkt 2). Dort bleibt eine Bedingung f = abs(R) - abs(I) = 0. An X ist V = i (4 w1 - 4 w3, 0, 0), also f < 0.
     Nahe dem Gitterbild (1,1,1) 2 pi/a von Gamma ist V(G + delta) = I(delta) - i R(delta) mit R(delta) = O(delta^4), also
     f > 0. Die Nullmenge trennt in der Ebene jedes X-Bild von jedem Gamma-Bild: eine Kurve. W ist weiter Nullstelle:
     V(W) = w1 (4 sqrt2/3)(i, 0, -1), V.V = 0. **Vorab: DN1 trifft ein** (Linien in den Ebenen k_i in (2 pi/a) Z).
   - **DN2 (a3 von W-D+S3 laengs 110) [M]:** R = O(k^4) aus dem fuenften Moment, I = (a/4)(80/9) w1 k.
     Relative Spaltung abs(R x n)/abs(I). Laengs (1,1,0)/sqrt2: sum w v_z (v_x + v_y)^4 = (32 - 1056/9) w1 = -85,33 w1,
     daraus **a3 = -+ 0,1 (a/4)^3 = -+ sqrt2/40 = -+ 0,03536** (lo -, hi +). Laengs 100 ist R = 0 exakt, laengs 111
     R parallel n: dort keine Spaltung, a3 = 0. Gemeinsamer Anteil ohne ungerade Glieder. Probe derselben Rechnung fuer
     W-D: a1 = (a/4)/2 = 0,3536 [P stimmt].
   - **DN3 (a2 von FKM an X) [M]:** laengs (q parallel X): E = 4 t abs(sin(a q/4)), a2 = -a^2/96 = **-1/12**; quer laengs
     100: E = 8 lambda abs(sin(a q/2)), a2 = -a^2/24 = **-1/3**. Spannweite mindestens 0,25 bei Mittel zwischen -1/12
     und -1/3: **vorab weit ueber 10 %**.
   - **Wortlaut-Frage [M]:** H^2 = diag(M M^dag, M^dag M); M M^dag = (1/4)[... + 2 sigma.(R x I)],
     M^dag M = (1/4)[... - 2 sigma.(R x I)]. Die A-Komponente des Zweigs hi hat Spin laengs +m, die B-Komponente laengs -m,
     m = (R x I)^ (bei W-D parallel (q x k)^); bei lo umgekehrt. Erwartung: Es trennt die untergitter-gestaffelte
     Querspin-Groesse tau_z sigma.m (+-1), nicht die Helizitaet sigma.k^ und nicht die Weyl-Chiralitaet tau_x (beide ~0).
   - Die Rechnung ist damit fuer DN0 bis DN3 eine **Pruefung von Schreibtisch-Mathematik**, keine Messung. Neu und nicht
     ableitbar ist nur die vollstaendige Nullstellen-Karte (weitere Linien ausserhalb der Ebenen, Punkte, Zahl der Schleifen).

## 2. Operatoren [F; Definitionen aus dem Dossier]

| Name | Definition | Fundstelle |
|---|---|---|
| W-D | H_AB = sum_a (i/2) sigma.n_a e^{ik.d_a}, H_BA = H_AB^dag; d_a = (a/4) t_a; Lage-Eichung | DOSSIER Z. 125; ARBEITSFELD Z. 23 (1.1); licht_netz.py Z. 153 (weyl_matrix) |
| W-D+S3 | dazu 12 Vektoren (+-1, +-1, +-3) a/4 (Koordinatensumme 3 mod 4), Sprung (i/2) w sigma.v unnormiert, w1 = 1/sqrt3 (= W-D), w3 = w1/9 | DOSSIER Z. 126; ARBEITSFELD Z. 70-81 (1.4, Z. 74 und 76) |
| FKM | t auf den 4 naechsten Nachbarn, i (8 lambda/a^2) sigma.(d1 x d2) auf den 12 zweiten Nachbarn (d1, d2 die beiden Bindungen des Weges), t = 1, lambda = 1/4 (t = 4 lambda) | DOSSIER Z. 128 und Z. 75 (V-h) |

- a = 2 sqrt2 PU, b = sqrt6/2 PU, k in 1/PU. Basis (A up, A down, B up, B down). Code: code/diamant_nullstellen.py.

## 3. BZ-Gitter und Kriterium Linie gegen Punkte [F]

- Gitter: k = sum s_i b_i, s_i = j/N, j = 0..N-1, primitive reziproke Vektoren b = (2 pi/a)(-1,1,1), (1,-1,1), (1,1,-1).
  Gamma, X (N gerade) und W (N durch 4 teilbar) liegen auf dem Gitter.
- Groesse je k: E_min = kleinster Betrag der vier Eigenwerte.
- Schwelle tau = 1,5 h v_op, h = V_BZ^(1/3)/N, v_op = Kegeltempo am Bezugspunkt (Gamma fuer W-D und W-D+S3, X_z fuer
  FKM; Mittel E/k bei k = 1e-4 ueber 26 Richtungen).
- Treffer n(N) = Zahl der Gitterpunkte mit E_min < tau. Fuer eine Nullmenge der Dimension D gilt n ~ N^D.
  **D_plan = log2(n(96)/n(48))**. Beschreibend: D aus N = 96 und 144.
- **Linien:** 0,5 <= D_plan < 1,5 und n(96) >= 30. **Punkte:** D_plan < 0,5 (oder n(96) < 30). **Flaechen:** D_plan >= 1,5.
- **Nullstellensuche:** 300 zufaellige Startpunkte (Saat [44, 1]) aus den N = 48-Treffern.
  - W-D, W-D+S3: Gauss-Newton auf (Re V.V, Im V.V) mit Pseudoinverse, Schritt <= 0,2.
  - FKM: Nelder-Mead (scipy) auf E_min^2.
  - Konvergiert, wenn E_min < 1e-9. Faltung in die erste BZ. "Gamma", wenn abs(k) < 0,05; sonst Klassen X, W
    (Abstand < 1e-3 modulo Gitter), "Ebene k_i in (2 pi/a) Z" (eine Koordinate ganzzahlig in 2 pi/a auf 1e-6), sonst.
  - Verschiedene Nullstellen: paarweise Abstand > 1e-3 nach Faltung.
- **Nullstellen-Karte:** Bild (Streupunkte der konvergierten Nullstellen, dazu die analytische W-D-Schleife) und Tabelle der
  Klassen.

## 4. Fitverfahren [F, Kopie aus licht_netz.py Z. 283-325]

- 26 Richtungen (+-1, 0)^3 normiert; je Richtung und positivem Zweig (lo, hi) omega/k = c (1 + a1 k + a2 k^2 + a3 k^3 +
  a4 k^4 + ...), alle Potenzen bis Grad g, Kleinste Quadrate auf x = k/k_max.
- Hauptfenster W0: k in [0,01; 0,30], 60 Punkte, Grad 8. Proben (beschreibend): Wk [0,005; 0,15] Grad 6, Wg [0,01; 0,60]
  Grad 10.
- W-D und W-D+S3 um Gamma; FKM um X_z, dazu X_x und X_y (Kontrolle, nur DN3 nach Kartenwortlaut).
- Zusammenfassung je Zweig ueber alle 26 und je Klasse (100, 110, 111): Mittel, min, max, Spannweite, Spannweite relativ =
  (max - min)/abs(Mittel), max abs.

## 5. Kontrollen [F]

- K1: vektorisierte W-D-Matrix gegen Kopie von licht_netz.weyl_matrix (20 zufaellige k), < 1e-12.
- K2: Hermitezitaet aller drei Matrizen. K3: Spektrum periodisch unter den drei b_i.
- K4: W-D-Tempo 0,8165 und a1 (110) = +-0,35355 wie LICHT-FINN-NETZ-1 [P].
- K6: FKM-Spektrum gegen meine d-Vektor-Form mit 2 lambda (Abschnitt 1, Punkt 4).
- K7: Schale 3: 12 Vektoren, alle Produkte -3, Summe 0, zweites Moment 44 delta, drittes -36; Schale 1 drittes +4.
- K8: R senkrecht I auf der Ebene k_x = 2 pi/a fuer W-D und W-D+S3 (50 Punkte).

## 6. Urteilsregeln (mechanisch in code/diamant_nullstellen.py, Funktion urteile)

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| DN0 | (a) W-D: E_min(W) < 1e-10, E_min((1; u*; u*) 2 pi/a) < 1e-10 mit u* = arccos(1/3)/pi, mindestens 32 Punkte der analytischen Schleife (Bisektion, 64 Winkel um X) mit E_min < 1e-10, und W-D-Nullmenge ist Linie (Abschnitt 3); (b) W-D+S3: max abs(a1) ueber 26 Richtungen und beide Zweige < 1e-6 (W0); (c) FKM: groesste Spaltung (Gitter N = 48, 96, 144 und 2000 Zufallspunkte) < 1e-10 und Spannweite relativ des Tempos an X_z < 1e-6 fuer beide Zweige. Alles: eingetroffen, sonst nicht eingetroffen. | wie Plan ohne die Dimensionsbedingung in (a) |
| DN1 | W-D+S3: Linien nach Abschnitt 3 (0,5 <= D_plan < 1,5, n(96) >= 30): eingetroffen; Punkte oder Flaechen: nicht eingetroffen | Nullstellensuche findet mindestens 20 verschiedene Nullstellen ausserhalb Gamma (Kontinuum): eingetroffen, sonst nicht eingetroffen |
| DN2 | W-D+S3, alle 12 Richtungen der Klasse 110, beide Zweige: abs(a3) > 1e-4 (W0). Alle: eingetroffen; keine: nicht eingetroffen; sonst geteilt | dasselbe mit Schwelle max(10 x Rauschboden, 1e-7); Rauschboden = groesstes abs(a3) der Klassen 100 und 111 (dort ist a3 nach Abschnitt 1 exakt 0) |
| DN3 | FKM an X_z: (max a2 - min a2)/abs(Mittel a2) ueber 26 Richtungen > 0,10, je Zweig. Beide: eingetroffen; keiner: nicht eingetroffen; sonst geteilt | dieselbe Groesse ueber alle drei X-Punkte zusammen (78 Kegelrichtungen, beide Zweige) > 0,10 |

- **Bedeutung** (woertlich aus der Karte) wird nur zitiert, nicht umgedeutet. DN1 nein haette nur dann die Bedeutung
  "symmetrischer Einzel-Dirac-Operator", wenn die Suche ausser Gamma gar keine Nullstelle findet; das wird angegeben.

## 7. Wortlaut-Frage (beschreibend, ohne Urteil)

- Fuer W-D und W-D+S3 bei abs(k) = 0,1/PU in den 12 Richtungen der Klasse 110 und 20 Fibonacci-Richtungen: Eigenvektoren
  von lo und hi; Erwartungswerte aller 16 Produkte tau_a (x) sigma_b mit tau_a in {1, x, y, z} (Untergitter) und sigma_b in
  {1, sigma.k^, sigma.m, sigma.(k^ x m)}, m = (R x I)^ aus V(k). Entartete Richtungen (Luecke < 1e-9) zaehlen nicht.
- Helizitaet = 1 (x) sigma.k^. Weyl-Chiralitaet (gamma5-artig, vertauscht mit der fuehrenden Ordnung tau_x sigma.k)
  = tau_x (x) 1. Untergitter-Operator = tau_z (x) 1.
- "Trennt" heisst: lo und hi haben in jeder nicht entarteten Richtung entgegengesetztes Vorzeichen und abs(hi - lo) > 0,5.
- Dazu cos(m, (q x k)^) fuer W-D. FKM: alle Baender zweifach entartet, Frage nicht anwendbar.

## 8. Laeufe (nach dem Einfrieren; je <= 600 s, 1 Thread, Logs mit absolutem Pfad)

- Vorab Kopie von code/ nach /home/fmh/fmhc-physics-remote/diamant-nullstellen-1/code/ (Pruefsummen gleich).
- L1 (cpu): `diamant_nullstellen.py rechnen lauf/ergebnis.json`.
- L2 (cpu11): `diamant_nullstellen.py bild lauf/ergebnis.json lauf/bild-diamant-nullstellen.png`.
- L3 (cpu11, beschreibend): Wiederholung von L1 nach lauf/ergebnis-wdh.json (Reproduktion; Zahlen gleich erwartet).
- **Laufzeitschaetzung:** Rauchtest (N = 8, 16, 24, 10 Starts) 2,3 s. Gitter 48^3 + 96^3 + 144^3 = 4,0 Mio. k je Operator,
  etwa 2 Mikrosekunden je k, also etwa 25 s fuer alle drei; Suche etwa 30 s (FKM) und je etwa 6 s; Fits und Rest < 20 s.
  Zusammen etwa 1 bis 3 min je Lauf.
- Faellt ein Teil mit Fehler aus, wird das im Ergebnis vermerkt; eine Codeaenderung danach waere eine Selbstanzeige mit
  neuer eingefrorener Fassung.

## 9. Agenten-Erwartung (vor jeder Rechnung; aus Abschnitt 1, also keine unabhaengige Vorhersage)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| E1 | DN0 eingetroffen (alle drei Teile) | 85 % |
| E2 | DN1 eingetroffen nach Plan und Kartenwortlaut; die W-D+S3-Linien liegen in den Ebenen k_i in (2 pi/a) Z | 80 % |
| E3 | DN2: a3 (110) = -+0,0354 auf 1e-4, a3 (100, 111) = 0 | 80 % |
| E4 | DN3: a2 an X: -1/12 laengs, -1/3 quer (100); Spannweite > 100 % | 75 % |
| E5 | Wortlaut: trennend ist tau_z sigma.m; Helizitaet und tau_x mitteln auf abs < 0,05 | 70 % |

## 10. Einfrieren

- Eingefroren werden PLAN.md und code/diamant_nullstellen.py als Kopien *.eingefroren-<Zeit>; sha256 in
  EINGEFROREN-SHA256.txt, auf der .69 dieselben Pruefsummen. Danach keine Aenderung an Plan, Code oder Regeln; alles nach
  Sicht ist ein gekennzeichneter Nachtrag in neuen Dateien.
