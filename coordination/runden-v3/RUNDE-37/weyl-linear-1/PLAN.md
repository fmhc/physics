# WEYL-LINEAR-1: Plan (Runde 42, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Arbeitsplatz RUNDE-37/weyl-linear-1/, Rechenort .69
  (/home/fmh/fmhc-physics-remote/weyl-linear-1/), Spuren cpu8 und cpu9.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 18:12:29 CEST. Zeitbox 90 min, also bis 19:42 CEST.
  - Gelesen bis 18:21 CEST: Karte, DOSSIER Z. 60-100 und 170-200, ARBEITSFELD Abschnitt 4, STRICH-NETZ-1 (ERGEBNIS,
    PLAN, Code), SPIN-ZUFALLSNETZ-1 (KARTE, ERGEBNIS, Code).
  - Code und Rauchlaeufe 18:26 bis 18:31 CEST (Rauch: winzige Netze, nur Rueckgabecodes und Schluessel angesehen).
  - Dieser Plan ab 18:31:31 CEST, vor jeder Sicht auf lambda1-Werte der Auswertung.
- **Kennzeichen:** [M] eigene Mathematik (ungeprueft), [E] gerechnet, [P] Projektdatei, [S] Quelle, [H] Hypothese,
  [F] Festlegung dieses Plans.
- Alles ist synthetische Netzrechnung. Keine Messdaten, keine Messdatenbestaetigung.

## 0. Rohdatenprobe (jq, vor jeder Rechnung)

- **STRICH-NETZ-1 lauf-69/weyl-1-{0,x,d}.json** [P]. Felder: argv, M, modus, N, saat, richtung, laufzeit_gesamt_s,
  rss_mb, protokoll, laeufe[].{theta, a, M, mu_max, sek, sek_kpm, schranke.{a, gershgorin, lanczos_max_betrag,
  lanczos_ok, sek}}, laeufe[].wellen[].{m, theta, k, k_vec, E_zentrum, v, v_halbM, v_max, gewicht_fenster, sigma_E,
  erstes_moment}.
  - Alle drei Dateien: N = 50 000, **nur Saat 1**, M = 4096, a = 3,656.
  - 34 Wellen: 16 Schalenwellen bei theta = 0 (k = 0,171; 0,241; 0,295; 0,341), 9 verdrillt laengs x
    (k = 0,022 bis 0,236), 9 verdrillt laengs der Raumdiagonale (k = 0,022 bis 0,361).
  - **Nur der Ast E > 0** (Helizitaet sigma.k^ = -1; strichnetz.weyl_zentren nimmt U[:, 0]; PLAN Abschnitt 3 (v)).
- **STRICH-NETZ-1 lauf-69/auswertung.json** [P]: urteile.SN5.kennzahlen.fit_weyl (Koeffizienten), se_v0_weyl, rms_weyl;
  **kein Standardfehler des linearen Glieds.** Der Bericht nennt -0,0011 k "ohne Fehler" (ERGEBNIS 2.1).
- **SPIN-ZUFALLSNETZ-1 lauf-69/netz1e4-a.json** (N = 1e4, Saaten 1 bis 4, M = 2048) und **netz1e5-1.json** (N = 1e5,
  Saat 1, M = 1024) [P]. Felder je Saat: kpm.*, op.*, pruefung.*, spektral.{a, M, mu_max_betrag, F_fenster, k[], h[],
  m[], E1[], E2[], G_richtig[], schalen.<s>_<h>.{A[601], anzahl, k_mittel}}. netz1e5-2.json hat keinen Spektralteil.
  - Beide Aeste gibt es nur als **schalengemittelte KPM-Dichte** je Helizitaet auf dem Raster -1,5 bis 1,5 (Schritt
    0,005). Spitzenlagen je Welle sind nicht gespeichert. E1 = <H> und E2 = <H^2> sind exakte Momente (siehe D1).
- **Ergebnis der Probe:** lambda1 samt Fehler steht nirgends. Projekt-grep ("lambda1", "lineares Glied",
  "Teilchen-Loch") fand nur das Dossier, sein ARBEITSFELD und fachfremde Treffer.
- **Kartenfehler:** "zwei Saaten" gilt fuer weyl-1 nicht (nur Saat 1; Saat 2 nur fuer Homogenisierung und
  Zaehlungen). "Beide Aeste" gibt es in SPIN-ZUFALLSNETZ-1 nur schalengemittelt.

## 1. Schreibtisch (vor jeder Auswertung) [M, ungeprueft]

Operator (spinnetz.py, unveraendert): H = V^-1/2 H0 V^-1/2, H0_ij = (i/2) A_ij (sigma.n_ij) e^(i theta.s_ij);
langwellig H ~ -sigma.k, Ast E > 0 hat Helizitaet -1.

| Nr | Frage | Ergebnis | Folge |
|---|---|---|---|
| D1 | Was gibt das erste Moment? | Fuer die ebene Welle (k, h) gilt exakt <H> = -(h/V) sum_Kanten A_e (k^.n_e) sin(k.d_e): ungerade in k, exakt entgegengesetzt fuer h = +-1, **ohne k^2-Glied**. | Aus <H> (Feld erstes_moment, E1) folgt lambda1 = 0 in beiden Aesten; das ist Bauart, keine Aussage. Gemessen werden muss die Spitzenlage (Verschiebung zweiter Ordnung). |
| D2 | Exakte Teilchen-Loch- oder chirale Symmetrie je Netz? | **Nein.** Delaunay ist nicht bipartit (Dreiecke), also kein Untergitter-Operator. Keine 2x2-Matrix antikommutiert mit allen sigma_a. K bzw. i sigma_y K bilden H auf +H ab: Zeitumkehr T, Kramers-Paare. | Je Netz gibt es keine exakte Beziehung E -> -E (passt zur Dichteasymmetrie 0,022 bei N = 1e5 [P]). |
| D3 | Erzwingt das Ensemble etwas? | **Ja, exakt.** Punktspiegelung x -> -x laesst A, d, V gleich und dreht n und s um: H(Pw, theta) = -H(w, -theta). Das Poisson-Ensemble im periodischen Wuerfel ist spiegelinvariant, T bildet k auf -k bei gleichem E ab. | Die Verteilung der Dispersion des Asts E > 0 ueber Netze ist gleich der von abs(E) im Ast E < 0: **E[lambda1(E>0)] = E[lambda1(E<0)]** fuer jeden spiegelsymmetrischen Schaetzer (unserer ist es, Abschnitt 4). |
| D4 | Je Netz, stoerungstheoretisch? | H_k = e^(-ik.x) H e^(ik.x) ist glatt in k, die gleichmaessige Spinorwelle ist Nullmode von H_0. Zweite Ordnung: Sigma(k, E) = k_a k_b P J_a Q (E - QHQ)^-1 Q J_b P mit J = dH_k/dk. T gibt T Sigma T^-1 = Sigma(-k) = Sigma(k), also verschwindet der sigma-Anteil; nur ein Einheitsanteil s0(E) k^2 bleibt. Damit E_+- = +-k + s0 k^2 + O(k^3). | **Je Netz und Richtung lambda1(E>0) = -lambda1(E<0) = s0** in fuehrender Ordnung. Der Gleichteil lambda_S = (lambda1+ + lambda1-)/2 ist in dieser Ordnung null; der symmetrische Teil von v hat nur gerade Potenzen. |
| D5 | D3 und D4 zusammen | E[lambda1] = 0 in beiden Aesten. Je Netz ist lambda1 eine Zufallsgroesse mit Mittel 0 (Volumensumme spiegel-ungerader Beitraege). Grob: Streuung ~ N^(-1/2), weil die Weyl-Greenfunktion ~ 1/r^2 quadratsummierbar ist. | Das Mittel ist Kontrolle. Gemessen werden die Streuung je Netz, ihr N-Exponent, der Gleichteil (Schaetzer, Fitmodell) und ob D4 bei k bis 0,24 numerisch haelt. |
| D6 | Erzwingt Isotropie lambda1 = 0? | Nein. Sie macht nur den Tensor D (lambda1(k^) = k^.D.k^) im Mittel isotrop; die Null im Mittel kommt aus D3. | Mittel ueber die drei Achsen = Spur(D)/3 je Netz. |

- **Folgen fuer die Vorhersage WL1 (Karte, 55 %):** Liest man sigma als Standardfehler des Saatenmittels, ist
  "abs(lambda1) < 3 sigma" fuer den Gegenteil lambda_A aus D5 fast vorab ableitbar. Scheitern kann WL1 dann nur ueber
  den Gleichteil (Fitmodell-Leck eines k^4-Glieds, Linienform, Effekte ausserhalb der Stoerungsrechnung) oder weil D3/D4
  falsch sind. Die Kartenalternative "abs(lambda1) ~ 1e-3 mit entgegengesetztem Vorzeichen je Ast" ist nach D4 die
  erwartete Signatur **eines einzelnen Netzes**, kein Widerspruch zu WL1.
- **Folgen fuer die Netzweite [H]:** Ein Photon ueber kosmische Wege tastet ein riesiges Netzstueck ab. Gilt D5 mit
  Exponent -1/2, faellt sein wirksames lambda1 gegen null; dann bliebe nur der quadratische Anker. Das wird nur bedingt
  gesagt und an den gemessenen N-Exponenten gebunden.

## 2. Netzweiten-Formeln des Dossiers (nachgerechnet am Schreibtisch, Zahlen in Teil K des Codes) [M]

- LHAASO Gl. 2 [S-lokal laut Dossier]: v(E) = c [1 - s (n+1)/2 (E/E_QG,n)^n] (Gruppentempo).
- Netz, k in Einheiten 1/l mit l = n^(-1/3) (Code: Dichte 1): E = hbar c k (1 + lambda1 k l). Gruppentempo
  c (1 + 2 lambda1 k l). Gleichsetzen mit n = 1: 2 abs(lambda1) k l = E/E_QG,1, k = E/(hbar c), also
  **l = hbar c / (2 abs(lambda1) E_QG,1)**; Einheiten GeV m / GeV = m. Subluminal heisst lambda1 < 0; nach D4 ist ein
  Ast sub-, der andere superluminal (LHAASO superluminal 1,1e20 GeV, fast gleich).
- Quadratisch: Phasentempo 1 - kappa k^2 gibt Gruppentempo 1 - 3 kappa k^2; gleich (3/2)(E/E_QG,2)^2 gibt
  **l = hbar c / (E_QG,2 sqrt(2 kappa))**. Beide Formeln stimmen mit dem Dossier ueberein.
- Kopfprobe: 1,97327e-16 / (2 x 0,0011 x 1e20) = 8,97e-34 m = 55,5 l_P; mit 1,22e19 GeV (JLM "order unity", nur
  Groessenordnung) 7,35e-33 m = 455 l_P; quadratisch 0,117: 5,91e-28 m. Teil K rechnet sie auf der .69 nach.

## 3. Altdaten-Auswertung (Teile A und S von code/auswertung.py)

- **A, STRICH-NETZ-1, Ast E > 0, N = 50 000, Saat 1:** Fit v - 1 = lambda1 k + lambda2 k^2 (Kartenansatz,
  Achsenabschnitt 1, ungewichtet) an alle Wellen mit Fenstergewicht >= 0,5 [F].
  - Hauptfenster W0: k <= 0,25 [F]. Probefenster (nur beschreibend): Wk k <= 0,15, Wg k <= 0,37 (alle).
  - Bootstrap ueber Richtungs-Cluster (13 Richtungen, Vorzeichen egal; B = 2000; default_rng([42, 1])). Bei weniger
    als 3 Clustern (Wk: nur x und Diagonale) nur beschreibend. **Mit einer Saat ist kein Saaten-Bootstrap moeglich;
    dieser Fehler misst nur die Richtungsstreuung in einem Netz.**
  - Beschreibend: Fit mit freiem Achsenabschnitt, Fit an den M/2-Zentren, Residuen-Standardfehler.
- **S, SPIN-ZUFALLSNETZ-1, beide Aeste:** Zentrum je Schale und Ast auf dem gespeicherten Raster (Maximum in
  [0,3 k; 1,7 k], Fenster +-4 sigma_E mit sigma_E = pi a/M, Trapez); Ast E < 0 als gespiegelte Dichte A(-E) mit
  derselben Routine. lambda_A = (E_plus - abs(E_minus))/(2 k^2) je Schale; Hauptmenge k <= 0,30 (N = 1e4: Schale 1,
  vier Saaten; N = 1e5: Schalen 1 bis 4, eine Saat). Nur der Gegenteil ist so messbar.

## 4. Neue Laeufe (die Altdaten tragen den Fehler nicht: eine Saat, ein Ast, ein N)

- **Code:** code/weyllinear.py (neu; Zentrumsroutine woertlich aus strichnetz.weyl_zentren, STRICH-NETZ-1) mit
  code/spinnetz.py (unveraendert, sha256 460c0af6). Netz: spinnetz.zufallsnetz(N, saat), dieselbe Saatkonvention wie
  STRICH-NETZ-1 (default_rng([39, N, saat])).
- **Wellen [F]:** m = 0, Verdrillung theta = k L e, e in {x, y, z}; k in K = {0,06; 0,12; 0,18; 0,24}; beide
  Helizitaeten in einem KPM-Block. Ast E < 0: Momente mu_n -> (-1)^n mu_n, dann dieselbe Routine (spiegelsymmetrischer
  Schaetzer).
- **KPM [F]:** M = 2048, feste Skala a = 4,0 fuer alle N (sigma_E = pi a/M = 0,0061 ueberall gleich); zulaessig nur,
  wenn a >= 1,02 x Lanczos-Betrag (sonst Rueckfall auf die Code-Skala, Feld a_fest_ok). M/2 = 1024 wird mitgefuehrt.
- **Netzgroessen und Saaten [F]:** N = 2000 (Saaten 1 bis 12), N = 8000 (1 bis 6), N = 32 000 (1 bis 4).
- **Kontrollen:**
  - KG: kubisches Gitter L = 20, M = 2048, a = 4, k in K laengs x: abs(E) gegen sqrt(sum sin^2 k_a) und
    E_plus - abs(E_minus) = 0.
  - KR (Reproduktion): N = 50 000, Saat 1, theta = 0,8 e_x, M = 4096, Code-Skala: v des Asts E > 0 muss dem Altwert
    (weyl-1-x, erste Welle) auf <= 1e-9 gleichen. Der Ast E < 0 an derselben Stelle ist beschreibend.
- **Laufliste (je Lauf <= 600 s, 1 Thread, 4 GB; Logs mit absolutem Pfad in lauf/):**
  - cpu8: L1 kontrolle (Gitter), L2 zweig 2000 Saaten 1-12, L3 zweig 8000 Saaten 1-3, L4 zweig 32000 Saat 1,
    L5 zweig 32000 Saat 3.
  - cpu9: L6 auswertung nur Teile A, S (Altdaten), L7 repro 50000 Saat 1, L8 zweig 8000 Saaten 4-6, L9 zweig 32000
    Saat 2, L10 zweig 32000 Saat 4.
  - Danach L11 auswertung alle Teile mit Bild. Zeit je Lauf geschaetzt aus Rauchlauf R3 (N = 8000: 4,8 s je Wellenpaar).

## 5. Auswerteregeln (mechanisch in code/auswertung.py, Teil N)

- Je Saat und Ast: Fit v - 1 = lambda1 k + lambda2 k^2 an alle 12 Punkte (4 k x 3 Richtungen) -> lambda1+(s),
  lambda1-(s); lambda_A = (lambda1+ - lambda1-)/2 (Gegenteil), lambda_S = (lambda1+ + lambda1-)/2 (Gleichteil).
- Je N: Mittel, Streuung (SD ueber Saaten), SE = SD/sqrt(n), RMS; zweistufiger Bootstrap (Saaten mit Zuruecklegen,
  darin die drei Richtungen mit Zuruecklegen; B = 4000; default_rng([42, 2, N])).
- N-Exponent: Gerade durch log SD gegen log N (N mit >= 3 Saaten), beschreibend.
- Proben (nur beschreibend): Fenster k <= 0,18; M/2-Zentren; freier Achsenabschnitt; direkter Gegenteil-Schaetzer
  mittel((v+ - v-)/(2k)); Korrelation lambda1+ gegen lambda1-.
- **WL1 (Karte) [F: Lesart]:** bei der groessten N (32 000) je Ast abs(Mittel lambda1) < 3 x Bootstrap-SE des Mittels.
  Eingetroffen, wenn beide Aeste das erfuellen; sonst nicht eingetroffen; weniger als 3 Saaten: nicht auswertbar.
- Netzweite: nur bedingt ("wenn das Netz das Photon traegt"), mit den Formeln aus Abschnitt 2.

## 6. Agenten-Vorhersagen (geschrieben vor jeder Sicht auf lambda1-Werte)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Je Netz entgegengesetzt (D4): Korrelation lambda1+ gegen lambda1- ueber alle Saaten und N < -0,5 | 70 % |
| A2 | Streuung von lambda_A faellt mit N, Exponent in [-0,8; -0,2] | 60 % |
| A3 | abs(Mittel lambda_A) < 3 Bootstrap-SE bei jedem N (Kontrolle aus D5) | 85 % |
| A4 | WL1 eingetroffen | 50 % |
| A5 | Altdaten W0: abs(lambda1) < 0,003 | 65 % |
| A6 | abs(Mittel lambda_S) < 1e-3 bei N = 32 000 | 55 % |
| A7 | Kontrollen: Gitter abs(E) auf <= 1e-4 und plus - minus <= 1e-12; Reproduktion <= 1e-9 | 80 % |

## 7. Einfrieren

- Eingefroren werden PLAN.md, code/weyllinear.py, code/auswertung.py und code/spinnetz.py als Kopien
  *.eingefroren-<Zeit> mit Pruefsummen in EINGEFROREN-SHA256.txt (lokal und auf der .69).
