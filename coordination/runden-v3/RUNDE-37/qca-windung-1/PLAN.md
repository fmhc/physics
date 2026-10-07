# QCA-WINDUNG-1: Plan des Code-Agenten (Runde 41)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 15:20:53 CEST (date). Gelesen ab 15:21: KARTE.md,
  chiral-l/DOSSIER.md (V4, Abschn. 7 bis 9), chiral-l/ARBEITSFELD.md (Abschn. 2b bis 7), qca-tetra-1/ERGEBNIS.md und
  code/qca_tetra.py (weyl_A, W_at), qca-bcc-rueck-1/{KARTE, PLAN, ERGEBNIS}.md und code/qca_rueck.py (ganz), Metadaten
  der Laeufe per jq, qca-dirac-t-1/ERGEBNIS.md (Anfang). qca-gegenlesen-2 lese ich vor dem ERGEBNIS-Text (Negativliste).
- Rechnungen nur auf der .69 in /home/fmh/fmhc-physics-remote/runde41-qca-windung/ (code/, rauch/, lauf/, ref_rueck/,
  ref_dirac/), Start nur ueber kleintest.sh, Spuren p4000b und p4000a, je Lauf <= 10 min, 1 Thread.
- **Kennzeichen:** [S] an der Quelle gelesen; [S Abstract] nur Abstract; [L] Gedaechtnis; [L?] unsicher; [M] eigene
  Mathematik, nicht gegengelesen; [P] Projektdatei; [F] Festlegung dieses Plans; [R] im Rauchlauf gesehen; [H] Hypothese.
- Die Vorhersagen WI0 bis WI2 und ihre Wahrscheinlichkeiten stehen unveraendert auf der Karte.

## 0. Literatur (2 von 3 Abrufen, keine Websuche)

- **Erwartungen vor den Abrufen (geschrieben ab 15:29:56 CEST, vor Abruf 1):**
  - F1 (arXiv-Schnittstelle, Autoren Bessho/Sato und Higashikawa/Ueda): Bessho/Sato 2020/21 (arXiv 2006.04204,
    PRL 127, 196404) formulieren einen erweiterten NN-Satz fuer Floquet-Systeme, Gesamtchiralitaet = 3D-Windungszahl
    W3 der Floquet-Unitaeren; Higashikawa/Nakagawa/Ueda 2019 (arXiv 1806.06868, PRL 123, 066403) koppeln W3 an einen
    quantisierten chiralen magnetischen Effekt [L?].
  - F2 (Volltext Bessho/Sato): W3 = (1/24 pi^2) Int tr(U^-1 dU)^3; Aussage je Quasienergie-Luecke bzw. fuer die
    Weyl-Punkte zwischen zwei festen Baendern; Vorzeichen per Konvention [L?].
  - F3 (Reserve): nicht verwendet.
- **F1 (arXiv-API, Abruf 15:30 CEST): bestaetigt.** Nummern und Zeitschriften stimmen. Higashikawa/Nakagawa/Ueda
  [S Abstract]: "A single Weyl fermion, which is prohibited in static lattice systems by the Nielsen-Ninomiya theorem,
  is shown to be realized in a periodically driven three-dimensional lattice system with a topologically nontrivial
  Floquet unitary operator, manifesting the chiral magnetic effect." Das ist das Beispiel mit W3 ungleich 0.
- **F2 (Volltext 2006.04204v3, Abruf 15:31 CEST; quellen/bessho-sato-2006.04204v3.pdf, sha256 6a20e340...5d630d369;
  S. 1 bis 5 als Bild gelesen) [S]:**
  - Dualitaet, Eq. (3)/(12): "H(k) = iU_F(k)"; S. 3: "In terms of the Floquet Hamiltonian H_F(k) = (i/tau) ln U_F(k),
    the above relation reads H(k) = sin[H_F(k)tau] + i cos[H_F(k)tau]".
  - Eq. (9): "w3 = -(1/24pi^2) Int_BZ tr[H^-1 dH]^3". Mit H = iU ist H^-1 dH = U^-1 dU, also **w3 = -W3(Karte)**.
  - Theorem 2, Eq. (8): "w3 = Sum_{ImE_p(S_pa)>0} Ch_pa = - Sum_{ImE_p(S_pa)<0} Ch_pa"; Eq. (10) Chern-Zahl auf der
    Fermi-Flaeche S_pa (Re E_p = 0), "the orientation of S_pa is along the direction of the Fermi velocity
    Re(dE_p(k)/dk)", "Ch_pa counts the total chirality of Weyl points inside S_pa". Fuer Floquet ist Re E = 0 bei
    Quasienergie 0 (Im E = +1) und pi/tau (Im E = -1).
  - Theorem 3' (S. 4), Eq. (15): "n = Sum_{eps_a = mu} nu^mu_a, in case (i')"; "(i') gapless fermions in classes A,
    AI, AII appear as band crossing points with arbitrary energies in the quasi-energy spectra"; "alpha labels the
    Fermi surfaces defined by eps = mu, and nu^mu_a is the topological charge of gapless fermions inside the alpha-th
    Fermi surface". n ist die Zahl von iU_F (in 3D Klasse A: w3). Theorem 1' (Eq. 7) ist der 1D-Fall fuer jedes mu.
  - **Was die Quelle sagt:** Fuer jede Quasienergie mu ist die Gesamtladung der Weyl-Punkte innerhalb der
    Fermi-Flaechen bei mu gleich der Volumenzahl w3. Statisch ist w3 = 0 (NN).
  - **Was sie nicht woertlich sagt:** "Netto-Chiralitaet je Luecke zwischen Band n und n+1 = W3". Die Bruecke ist
    meine (Abschn. 3, [M]).
- **1D-Index:** GNVW 2012 (Gross/Nesme/Vogts/Werner, Index fuer 1D-QCA) [L], nur genannt.

## 1. Aufbau von U(k) und Konventionen [F]

- U(u) = Sum_f A_f exp(i u.f), u = k/sqrt3, f aus "freqs" (BCC-Richtungen (+-1, +-1, +-1), Form O/P dazu 0). Das ist
  W_at aus qca_tetra.py und qca_rueck.py. u -> k ist eine positive Streckung; W3 und alle Vorzeichen bleiben.
- Ableitungen analytisch: d_j U = Sum_f i f_j A_f exp(i u.f).
- Periodengitter [M]: g.f in 2 pi Z fuer alle f <=> g in pi*{m in Z^3, Sum m gerade} (FCC), primitive Vektoren
  b1 = pi(1,1,0), b2 = pi(1,0,1), b3 = pi(0,1,1); |det B| = 2 pi^3. Der Wuerfel [0, 2pi)^3 ueberdeckt die Zelle viermal
  (wie CHIRAL-L, Z. 238).
- Phasenkonvention: Eigenwert exp(i phi) von U heisst Quasienergie phi (Eigenphase). Bei Bessho/Sato ist
  U_F = exp(-i eps tau), also eps tau = -phi. Die Fourier-Konvention exp(+i u.f) ist die "Hauptkonvention" von
  QCA-TETRA-1; mit exp(-i u.f) kehrt W3 das Vorzeichen (k -> -k).
- Takt: "im Takt (0)" heisst phi = 0 (U psi = psi), "Gegentakt (pi)" phi = pi (U psi = -psi), sonst "dazwischen";
  Toleranz 1e-6 [F]. **Grenze:** Eine globale Phase exp(i alpha) U aendert nichts Physikalisches, verschiebt aber alle
  phi. Nur die DP-Automaten haben eine natuerliche Eichung (W(0) = I, Eq. 9 der Arbeit von 2017); die gefundenen
  Automaten aus QCA-BCC-RUECK-1 stehen in der Eichung, in der die Suche sie lieferte. Fuer sie ist die Takt-Spalte
  eichabhaengig; ich nenne sie trotzdem (Karte) und vermerke das.
- **Nachbaupruefung (vor allem anderen, je gespeichertem Repraesentanten mit gespeicherter Einordnung):** Phasen der
  Kegel-Cluster bei Gamma (Abweichung <= 1e-9) und chiral_det (relativ <= 1e-6; meine Ableitung nach u, geteilt durch
  sqrt3^3 wie dW_at in qca_rueck.py). DP-Automaten gegen QCA-TETRA-1 Tabelle QT3 (W = +-I an Gamma, P, H, P',
  <= 1e-12). Unitaritaet: max ||U^dag U - I|| auf einem 12^3-Gitter <= 1e-8.

## 2. W3-Integral [F, M]

- W3 = (1/24 pi^2) Int d^3u eps^ijk tr(X_i X_j X_k), X_j = U^dag d_j U; eps^ijk tr(X_i X_j X_k) = 3 tr(X_1 [X_2, X_3]),
  also W3 = (1/8 pi^2) Int tr(X_1 [X_2, X_3]) d^3u [M].
- Rechteckregel ueber die primitive Zelle: u = B t, t auf dem Gitter ((i + 1/2)/N)^3, d^3u = |det B| d^3t
  (Jacobi-Faktor 2 pi^3; Ableitungen nach u, also bleibt die Orientierung von u). N = 16, 24, 32, 48.
- **Probe Jacobi-Faktor:** dasselbe Integral ueber den Wuerfel [0, 2pi)^3 bei N = 16, geteilt durch 4, muss den Wert
  der Zelle bei N = 16 treffen (Abweichung <= 1e-6).
- **Erwartung zur Konvergenz [M]:** Mit U^dag (nicht U^-1) ist tr(X_1 [X_2, X_3]) ein trigonometrisches Polynom mit
  Frequenzen bis 6 je Richtung (in t-Koordinaten bis 6). Die Rechteckregel ist dafuer ab N >= 7 exakt bis auf Rundung.
  Fuer die Projekt-Automaten ist die N-Reihe deshalb eine Probe auf Aliasing und Code, keine echte Konvergenzreihe. Die
  synthetische Abbildung (normiert, kein Polynom) konvergiert spektral; sie prueft die Konvergenz.
- **Ganzzahligkeit (Karte):** abs(W3 - round(W3)) < 0,05 beim feinsten Gitter (N = 48), sonst "nicht konvergiert".
  Gemeldet werden W3 je Gitter, der Imaginaerteil (muss 0 sein) und die Spannweite ueber die Gitter.
- **Zerlegung in Produkte [M], fuer Kontrollen:** W3(UV) = W3(U) + W3(V); W3(U(-u)) = -W3(U(u)); W3(V U V^dag) = W3(U);
  Muenze mal Schiebung X S(u) mit diagonalem S hat W3 = 0 (U^-1 dU = S^-1 dS ist abelsch); konstantes Spektrum gibt
  W3 = 0 (die Abbildung faktorisiert ueber eine Fahnenmannigfaltigkeit ohne H^3).

## 3. Weyl-Punkte, Chiralitaet und die Aussage je Luecke [M]

- **Chiralitaet** eines Zweifach-Clusters bei u_w, Phase phi_w: Q = Schur-Vektoren des Paares, G_l = e^{-i phi_w}
  Q^dag d_l U Q / i, M_lj = Re tr(G_l sigma_j)/2, chi = sign det M (lokaler Abbildungsgrad; basisunabhaengig, weil eine
  Basisdrehung im Cluster die sigma-Koeffizienten mit SO(3) dreht). Dieselbe Groesse ist chiral_det in qca_rueck.py
  (dort mit k-Ableitung, Faktor sqrt3^-3).
- **Vorzeichen fest vorab [M]:** Fuer die synthetische Abbildung (Karte) liegt -I nur bei Gamma: U ~ -I + i k.sigma,
  M = -I, chi = -1. +I hat sieben Urbilder (pi,0,0)-Typ chi = -1 (3x), (pi,pi,0)-Typ +1 (3x), (pi,pi,pi) -1: Summe -1.
  Grad = W3 = -1. Also: Luecke bei 0 netto -1, Luecke bei pi netto -1, **netto je Luecke = +W3** mit chi = lokaler Grad
  und W3 nach der Kartenformel. Das ist die Vorzeichenkonvention von WI2.
- **Bruecke von der Quelle zur Luecke [M, nicht gegengelesen]:** Sind die Baender global beschriftbar (stetige,
  sortierte Hebungen eps_1 <= ... <= eps_N <= eps_1 + 2 pi auf dem ganzen Torus), dann hat jedes Band n als Linienbuendel
  ueber T^3 ohne Weyl-Punkte Gesamtladung 0. An einem Weyl-Punkt zwischen unterem Band l und oberem Band u gilt
  q_u = chi = -q_l. Daraus: netto(Luecke n-1|n) = netto(Luecke n|n+1) fuer alle n; alle Luecken tragen denselben Wert.
  Statisch gibt es unter Band 1 keine Luecke, also 0 (NN). Mit der Quelle (Fermi-Flaechen-Ladung bei jedem mu = w3)
  und dem Grad-1-Beispiel ist der gemeinsame Wert W3 (Konvention oben). Summenform ohne Beschriftung: Summe ueber alle
  Weyl-Punkte = N W3 (Schnittzahl mit dem Entartungsort; beschreibend gemeldet, nicht im Urteil).
- **Globale Beschriftung [M]:** Laeuft man einen Zyklus b_i des Torus ab, verschieben sich die sortierten Hebungen um
  so viele Plaetze, wie det U(k) entlang b_i windet. Beschriftung global <=> Windung von det U entlang b1, b2, b3 alle 0.
  Fuer T- oder L_2-kovariante Automaten ist det U T-invariant, also sind die Windungen 0 [M].
- **Suche:** Zuerst die Zweifach-Cluster an Gamma, H, P, P' direkt (dort erzwingt T Entartungen; nur exakt entartete
  Paare). Dann Eigenphasen auf einem Gitter der Zelle; je Suche ein eigener Schnitt c (Suche 1: c1, Suche 2: c2) und die
  N sortierten Fensterluecken; lokale Minima je Luecke (6 periodische Nachbarn, Luecke < 0,3, hoechstens 400 je Luecke); Newton auf
  b(u) = 0 (sigma-Teil des Paares, Schritt <= 0,3, hoechstens 40 Schritte); Weyl-Punkt, wenn die Paarluecke <= 1e-9;
  Zusammenfassen modulo Periodengitter (t mod 1 bis 1e-6, Phase bis 1e-6). **Bahnergaenzung:** Jeder Fund wird mit den
  12 Drehungen von T abgebildet; ein Bildpunkt zaehlt nur, wenn dort dieselbe Phase mit Paarluecke <= 1e-9 liegt (bei
  T-kovarianten Automaten ist das exakt so, U(Rk) = V U(k) V^dag; bei anderen bestaetigt sich in der Regel keiner).
  Mehr als 400 verschiedene Funde (Knotenflaechen, entkoppelte Bloecke) heissen "nicht einfach"; dann keine
  Bahnergaenzung.
- **Vollstaendig [F]:** zwei unabhaengige Suchen (Gitter 40^3 ohne Versatz, 35^3 mit halbem Versatz) liefern dieselbe
  Menge (Lage, Phase, chi), und alle Punkte sind einfach (|det M| > 1e-10 in u-Einheiten, naechster fremder Eigenwert
  > 1e-6 entfernt). Trivial (keine Suche) ist ein Automat mit konstantem Spektrum (Spannweite < 1e-8) oder mit
  Sprunggewicht Sum_{f ungleich 0} ||A_f||^2 < 1e-10 (wie einordnen() in qca_rueck.py); W3 = 0 ist dort erzwungen [M].
- **Lueckenindex:** Schnitt c in der groessten Luecke der Weyl-Phasen; vom Bezugspunkt u_ref = B (0,1234567;
  0,2345678; 0,3456789) laengs zweier Wege (gerade; ueber B (0,61; 0,27; 0,83)) die Phase von det U stetig fortsetzen
  (1500 Schritte je Teilweg); Verschiebung s = (Theta - N c - Sum psi)/2 pi; Luecke g = (j - s) mod N. Beide Wege muessen
  dieselbe ganze Zahl geben (Abweichung < 0,05), sonst "pfadabhaengig".

## 4. Stufe B: Wiederholungsprotokoll [F]

- code/qca_rueck.py ist eine **unveraenderte** Kopie von qca-bcc-rueck-1/code/qca_rueck.py.eingefroren-20261004-095059
  (sha256 a42239a2...f767da17, gleich EINGEFROREN-SHA256.txt von RUECK-1).
- **Einziger Zusatz:** code/wiederholung.py importiert qca_rueck und umhuellt zwei Funktionen: rueck_pruefung(A, s, rng)
  merkt sich A und ruft das Original mit denselben Argumenten (derselbe rng, also dieselben Zufallszahlen); fall(...)
  ruft das Original und haengt die gemerkten A als "A_zusatz" (Format cplx wie "repr") an die Treffer. Begruendung:
  Das Original speichert A nur fuer den Repraesentanten (Z. 778-780); W3 braucht A je Treffer. Die Huelle aendert
  keinen Rechenschritt. sha256 der Huelle in EINGEFROREN-SHA256.txt.
- **Saaten:** main() von qca_rueck.py, Modus haupt (saat_basis 399): seed = 399*10000 + 2000 + 100*Form + 10*Variante +
  Fall (Form N = 0, O = 1; Variante frei = 0, r50 = 1; Fall K1..K5 = 0..4). Die Kartenformel seedbase*10000 + 10*vi ist
  die von Teil 0. Die Saat haengt nicht davon ab, welche Faelle ein Aufruf rechnet; ich rechne nur die neun Faelle
  mit Treffern (8Nb hatte keine) plus K5|N|r50, der im selben Aufruf anfaellt.
- **Aufrufe (wie die Originale laut ERGEBNIS RUECK-1 und Log):** Starts 12; Form N maxit 600, Form O maxit 300.
  - B-N: --teil 8 --modus haupt --formen N --varianten frei,r50 --faelle 3,4 --starts 12 --maxit 600
  - B-Oa: --teil 8 --modus haupt --formen O --varianten frei --faelle alle --starts 12
  - B-Ob: --teil 8 --modus haupt --formen O --varianten r50 --faelle 3 --starts 12
- **Reproduktionsprobe (Karte):** je wiederholtem Fall D_min, D_median, D_max und je Treffer D, D_poliert, D_voll
  relativ <= 1e-10 gleich den gespeicherten, gleiche Trefferzahl, gleiche log10D-Liste. Vermerke: nur Werte >= 1e-20;
  A des Repraesentanten (max. Abweichung). **Misslingt die strikte Probe:** neue Saaten (Modus rauch, saat_basis 3990,
  sonst gleich), als neue Stichprobe gekennzeichnet, die alte Zaehlung wird nicht verwendet (Karte).
- Zahl "17 Treffer ohne Inversion" (CHIRAL-L) wird an den wiederholten Treffern geprueft (Kategorien, Inversion).

## 5. Rauchlauf und Sichtregel [F]

- Rauch 1 (Kontrollen, Modus rauch): synthetische Abbildungen und DP-Automaten mit allen Ausgaben (Kontrollen duerfen
  vor dem Einfrieren gesehen werden).
- Rauch 2 (Stufe A, Modus rauch): fuer Projekt-Automaten nur Laufzeit, Unitaritaet, Inversion, Nachbaupruefung; W3,
  Weyl-Punkte und Chiralitaeten werden gerechnet, aber nicht geschrieben.
- Rauch 3: wiederholung.py im Modus rauch (andere Saaten) mit einem Start, nur Mechanik und Zeit.
- Danach Plan und Code einfrieren; keine W3-Werte von Projekt-Automaten vorher.
- **Ergebnisse der Rauchlaeufe [R] (13:43 bis 13:55 UTC, alle rc = 0; Ordner rauch-69/):**
  - Rauch 1 (Kontrollen, p4000b, 36 s): K-S1 W3 = -0,999859 / -0,999999 / -1,000000 / -1,000000 (N = 16/24/32/48),
    Imaginaerteil 0; 8 Weyl-Punkte (7 bei 0 mit netto -1, Gamma bei pi mit -1), Luecken netto (-1, -1), beide Suchen
    gleich. K-S1m +1, Luecken (+1, +1). K-S1q -2 (Suche nicht vollstaendig: Knotenflaeche bei -I, wie fuer U^2 zu
    erwarten). K-S1inv 0, Inversion erkannt (Suche nicht vollstaendig: entkoppelte Bloecke kreuzen auf Flaechen). K-MS8
    0 (Wuerfelprobe -4,6e-16); Suche mit ~100 Weyl-Punkten nicht vollstaendig. DP A+ und A-: W3 ~ 1e-17, je 4 Weyl-Punkte
    (2 bei 0, 2 bei pi, je +1 und -1), Luecken (0, 0), Tabelle QT3 getroffen (<= 2,2e-16), keine Inversion.
  - Rauch 2 (Stufe A ohne Ausgabe von W3 und Weyl-Daten, p4000a, 233 s): Nachbaupruefung bei Gamma fuer alle 31
    RUECK-Repraesentanten bestanden; 8 Zustaende 5 bis 25 s je Automat. Die "trivialen" Repraesentanten haben
    Sprunggewicht ~1e-14 (nicht exakt 0); mein erstes Trivialkriterium (nur Spektrum) erkannte sie nicht -> Kriterium um
    das Sprunggewicht ergaenzt (wie qca_rueck.py).
  - Rauch 2b (nur Zahl und Gleichheit der Weyl-Funde, keine Phasen oder Chiralitaeten): 2 Zustaende je 4 Punkte, beide
    Suchen gleich; 8 Zustaende 70 bis 120 Punkte, die zwei Suchen ungleich (z. B. 93 gegen 87); 4 Zustaende (einseitig)
    teils nicht einfach. -> Suche verstaerkt (Gitter 36/31 statt 32/27, 64 statt 32 Kandidaten) und Bahnergaenzung unter
    T eingefuehrt (Abschn. 3). Rauch 1c/2c pruefen das.
  - Rauch 1c (Kontrollen) habe ich nach 2 min 38 s selbst gestoppt (eigene Unit, systemctl --user stop): Das
    Zusammenfassen war quadratisch in der Punktzahl und lief bei K-S1inv (Knotenflaechen) zu lange. -> vektorisiert und
    Obergrenze 400 Punkte.
  - Rauch 2c (36/31, 64 Kandidaten, mit Bahnergaenzung): 8 Zustaende weiter ungleich (96/91, 80/88). Rauch 2d/2e (40/35,
    alle lokalen Minima < 0,3 bis 400, zwei Schnitte je Suche): K4_gemischt_0 104/104 gleich, Bahnen vollstaendig, 84 s;
    8Na K4|N|frei 64/63 ungleich, Bahnen vollstaendig, 97 s: Der Unterschied ist ein einzelner T-Fixpunkt. -> Gamma, H,
    P, P' direkt gepruefter Startsatz, je Suche nur ein Schnitt (halbe Zeit, unabhaengigere Suchen). Rauch 1d/2f pruefen
    das (Abschn. 5, Nachtrag im ERGEBNIS).
  - Rauch 3 (Wiederholung, Modus rauch, andere Saaten): Mechanik laeuft; mit 3 Starts in K4|N|frei ein Treffer,
    "A_zusatz" angehaengt und gleich dem gespeicherten "repr"-A desselben Treffers.

## 6. Urteilsregeln (mechanisch in code/auswertung.py)

- **Moegliche Urteile:** "eingetroffen", "nicht eingetroffen", "nicht auswertbar".
- **Vorbedingung Numerik (fuer alle drei):** alle Laeufe Modus haupt; Unitaritaet aller Automaten <= 1e-8; Probe
  Jacobi-Faktor <= 1e-6; Nachbaupruefung aller gespeicherten RUECK-Repraesentanten und wiederholten Treffer mit
  gespeicherter Gamma-Einordnung bestanden; DP-Tabelle QT3 getroffen. Sonst alle drei "nicht auswertbar".
- **WI0:** eingetroffen genau dann, wenn | |W3(K-S1)| - 1 | < 0,05, |W3(DP A+)| < 0,05, |W3(DP A-)| < 0,05 und fuer jeden
  untersuchten Automaten mit Inversion |W3| < 0,05 (je bei N = 48). "Mit Inversion": fester invertierbarer V mit
  V U(u) = U(-u) V, numerisch aus 32 Zufallspunkten (relativer Singulaerwert <= 1e-9, Kondition < 1e6, Rest an 16
  neuen Punkten < 1e-8). Die Menge umfasst die synthetische Kontrolle K-S1inv, die RUECK-Repraesentanten und -Treffer
  und den Zusatz aus QCA-DIRAC-T-1 (Form P mit Inversion, Abschn. 7). Vermerk: Zahl und Herkunft.
- **WI1:** nicht auswertbar, wenn WI0 nicht eingetroffen ist. Menge M = RUECK-Repraesentanten (Stufe A) und wiederholte
  Treffer (Stufe B, nur bei bestandener Reproduktionsprobe; sonst die neue Stichprobe, gekennzeichnet), jeweils ohne
  Inversion. Eingetroffen genau dann, wenn ein Automat in M konvergiert ist und |round(W3)| >= 1 hat; nicht eingetroffen,
  wenn alle in M konvergiert sind und round(W3) = 0; sonst nicht auswertbar. Vermerke: nur Repraesentanten; nur
  Treffer; mit dem DIRAC-T-1-Zusatz; Haeufigkeit der W3-Werte.
- **WI2:** nicht auswertbar bei verletzter Numerik-Vorbedingung. Auswertbar ist ein Automat, wenn er nicht trivial ist,
  die Suche vollstaendig ist (Abschn. 3), die Beschriftung global ist (Windungen von det U < 0,05, Schritt < 1 rad), der
  Lueckenindex pfadunabhaengig ist und W3 konvergiert ist. Eingetroffen genau dann, wenn es mindestens einen
  auswertbaren Automaten gibt und bei allen die Netto-Chiralitaet jeder der N Luecken gleich round(W3) ist; nicht
  eingetroffen, wenn bei einem auswertbaren Automaten eine Luecke abweicht; nicht auswertbar ohne auswertbaren
  Automaten. Kontrollen zaehlen mit (die Karte nennt WI2 eine Kontrolle der Formel). Vermerke: nur RUECK-Automaten;
  Summenregel Sum chi = N W3; Liste der ausgeschlossenen Automaten mit Grund.
- **Urteil nach Kartenwortlaut:** WI0 und WI1 wie oben (die Karte nennt dieselben Mengen; der DIRAC-T-1-Zusatz zaehlt
  bei WI0 mit, weil die Karte "alle Automaten mit Inversion" sagt, bei WI1 nur als Vermerk, weil die Karte
  "Repraesentant oder wiederholter Treffer" aus RUECK meint). WI2: Die Karte sagt "jede Quasienergie-Luecke"; ohne
  globale Beschriftung ist eine Luecke nicht definiert, deshalb dieselbe Regel; Abweichung keine.
- **Beschreibend:** W3 je Gitter, Imaginaerteile, Weyl-Punkte je Automat (Lage, Phase, chi, Luecke, Takt), Tabelle
  "Takt (0) / Gegentakt (pi) / dazwischen", det-Windungen, Summenregel, Laufzeiten.

## 7. Umfang Stufe A [F]

- RUECK-1 (Hauptmenge): alle Objekte "repr" mit "A" und "freqs" in lauf-69/haupt_{0,4N,4O,8Na,8Nb,8Oa,8Ob}.json:
  Teil 0 (L2:Pauli frei und r50; sechs Konstruktionen R3), 4 Zustaende (4N: 4, 4O: 10), 8 Zustaende (9).
- DP-Automaten A+ und A- (Eq. 24 der Quelle 2014, Funktion weyl_quelle wie in qca_rueck.py/qca_tetra.py).
- Zusatz QCA-DIRAC-T-1 (lauf-69/haupt_*.json, alle "repr"): Form P (mit Inversion) als Inversionskontrollen; die
  uebrigen nur beschreibend und als Vermerk bei WI1.
- Synthetische Kontrollen: K-S1 (Karte, m = 2), K-S1q = K-S1^2 (W3 = -2 erwartet), K-S1m = K-S1(-u) (+1), K-S1inv =
  K-S1(u) + K-S1(-u) (Inversion, 0), K-MS8 = X1 S X2 S mit 8 Zustaenden (0, Dichte nicht 0).

## 8. Laufplan

- Hauptlaeufe nach dem Einfrieren, je ein Starteraufruf, hoechstens zwei zugleich (p4000b, p4000a); Teillaeufe wegen
  der 10-min-Grenze, Inhalt wie oben:
  - H-K (p4000b, zuerst): Kontrollen -> lauf/kontrollen.json
  - H-A1, H-A2, H-A3 (p4000b): Stufe A RUECK in Teilen (haupt_0; haupt_4N + haupt_4O; haupt_8*) ->
    lauf/stufeA_rueck_{1,2,3}.json
  - H-BN, H-BOa, H-BOb (p4000a): Wiederholung -> lauf/wiederholung_{N,Oa,Ob}.json
  - H-B1, H-B2, H-B3: windung.py --teil B je Wiederholungsdatei -> lauf/stufeB_{N,Oa,Ob}.json
  - H-D (p4000a, zuletzt): Stufe A DIRAC-T-1 ohne Weyl-Suche (--weyl 0; Zusatz fuer WI0 und Vermerk WI1) ->
    lauf/stufeA_dirac.json
  - Auswertung: auswertung.py --dir lauf (Referenzen lauf/ref/haupt_8{Na,Oa,Ob}.json = Kopien der RUECK-1-Dateien);
    Teildateien werden per Muster zusammengefuehrt.
- Faellt ein Lauf aus (rc ungleich 0, Zeitabbruch), sind die betroffenen Urteile "nicht auswertbar"; ein zweiter
  Versuch nur bei einem Fehler ausserhalb des Codes, offengelegt.
