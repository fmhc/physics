# IMPULS-NETZ-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 46)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-05 07:14:26 CEST. Plantext ab 07:32:34 CEST, vor jeder Rechnung. Teil 1 (Formulierung) steht im Plan.
  - Rauchtests r1 bis r6 (05:42:21 bis 05:45:52 UTC, cpu5/cpu6): gelesen nur Rueckgabewert, Laufzeit, Speicher und
    JSON-Schluessel. r3 bis r6 schrieben mit --voll vollstaendige Dateien, damit urteil und bild geprueft sind; deren Werte
    habe ich nicht gelesen.
  - **Eingefroren 07:46:10 CEST:** PLAN.md.eingefroren-20261005-074610 (sha256 33b43a54...), code/inz.py (e65a5cbf...),
    dazu pn.py, ew.py, tp.py, mn.py, nachtrag_iso.py unveraendert aus PUMPE-NETZ-1 (c8034e40..., fa7b6417..., 419d7da6...,
    b36984d3..., 1c92cb23...). Liste in EINGEFROREN-SHA256.txt; auf der .69 besteht sha256sum -c fuer alle sechs Code-Dateien.
    Alle Hauptlaeufe tragen inz.py e65a5cbf... im JSON.
  - Hauptlaeufe H1, Z1, H2 gestartet vor jeder Sicht auf Werte. **Erste Sicht 07:48:51 CEST** (date beim ersten Lesen von
    h1.json). UR und BI liefen danach mit dem eingefrorenen Code (sie lesen nur die JSON-Dateien).
  - Nachtrag nach Sicht (beschreibend, aendert kein Urteil): code/nachtrag_quelle.py (sha256 7ffdc758...), Quellgroesse.
  - Hinweis der Leitung (08:1x, aus TAKT-UMKLAPP-1: P1-Gewichte sind in 3D nicht der umkreisbasierte Stern *1), bei mir
    angekommen mit dem Ergebnis eines Aufrufs, der 08:16:25 CEST (date) zeigte. Darauf der Nebenarm
    code/nachtrag_umkreis.py (sha256 51e91f90...), beschreibend, ohne Urteil (Abschnitt 5.6).
  - Zwei Abrufe zwischen 07:46:26 und 07:46:52 CEST (date davor und danach): Everitt u. a. 2011 (Gravity Probe B),
    Ciufolini u. a. 2019 (LARES/LAGEOS), je nur Abstract.
  - Text ab 07:58:10 CEST (date).
- lauf-69/, rauch-69/, nachtrag-69/: je PRUEFSUMMEN.txt auf der .69 erzeugt; sha256sum -c besteht lokal.
- Alles ist synthetische Gitterrechnung (numpy, 1 Thread), keine Messdaten. Messzahlen nur in Abschnitt 6, mit Quelle.
- **Kennzeichen:** [E] gerechnet, [M] eigene Mathematik, [P] Projektdatei, [S] Quelle abgerufen, [L?] Gedaechtnis ohne
  Abruf, [ES] eigener Schluss, [H] Hypothese, [F] Festlegung im Plan.
- **Einheiten und Festlegungen [F]:** wie PUMPE-NETZ-1: G = 1, kappa_g = 1/(8 pi), kappa' = kappa_g/2 (V1), Netz V, Paarung
  A1R1, Bewegungsgewichte J_iso (primaer) und J = 1 (beschreibend), c := TT-Tempo c_0 = 0,323734 (J_iso). Quelle: zwei
  gegenphasige phi-Klumpen, w = d = 0,8 l_P, Achsen [001], [111], (1,2,3). Neu: Impulsquelle J aus der Gitter-Bilanz.
- **Welche Gewichte:** Alle Urteile und Haupttabellen verwenden **P1-Gewichte** (lineare Elemente je Tetraeder,
  3D-Kotangens, pn.K_aus_laengen) fuer die Materie-Energie und damit fuer Spannung sigma und Impuls J = -Int M^H sigma dt.
  Eckvolumina (V1-Energie je Ecke, Stroeme der Mitfuehrung) sind baryzentrisch (1/4 jedes anliegenden Tetraeders), nicht
  umkreisbasiert. Umkreisbasierte Gewichte *1 nur im Nebenarm 5.6.

## 1. Zeiten und Laeufe

| Lauf | Spur | Aufruf (Arbeitsordner /home/fmh/fmhc-physics-remote/impuls-netz-1/) | Start bis Ende (UTC) | Laufzeit | rc |
|---|---|---|---|---|---|
| r1 | cpu6 | code-r1/inz.py lauf --rauch | 05:42:21 bis 05:42:57 (Lock-Wartezeit) | 6,5 s | 0 |
| r2 | cpu5 | code-r1/inz.py zusatz --rauch | 05:42:21 bis 05:42:26 | 4,5 s | 0 |
| r3 | cpu6 | code-r2/inz.py lauf --rauch --voll | 05:43:26 bis 05:45:41 (Lock-Wartezeit) | 6,7 s | 0 |
| r4 | cpu5 | code-r2/inz.py zusatz --rauch --voll | 05:43:26 bis 05:43:31 | 4,5 s | 0 |
| r5 | cpu5 | code-r2/inz.py urteil (auf r3, r4) | 05:45:48 bis 05:45:48 | 0,0 s | 0 |
| r6 | cpu5 | code-r2/inz.py bild (auf r3, r4) | 05:45:48 bis 05:45:52 | 3,2 s | 0 |
| H1 | cpu5 | code/inz.py lauf --out lauf/h1.json (primaer; IN0, IN2, KF, KJ) | 05:46:24 bis 05:48:40 | 135,3 s, 384 MB | 0 |
| Z1 | cpu6 | code/inz.py zusatz --out lauf/zusatz.json (Isotropie, KE, Kreisbahnen, Mitfuehrung) | 05:46:24 bis 05:48:45 (Lock-Wartezeit) | 25,5 s, 111 MB | 0 |
| H2 | cpu5 | code/inz.py lauf --nt 12 --nphi 24 --out lauf/h2.json (Quadratur) | 05:48:47 bis 05:51:17 | 149,3 s, 535 MB | 0 |
| UR | cpu6 | code/inz.py urteil --h1 lauf/h1.json --zusatz lauf/zusatz.json | 05:49:11 bis 05:52:30 (Lock-Wartezeit) | 0,0 s | 0 |
| BI | cpu6 | code/inz.py bild ... --bild lauf/bild-impuls-netz.png | 05:52:30 bis 05:55:20 (Lock-Wartezeit) | 3,1 s | 0 |
| NQ | cpu5 | code/nachtrag_quelle.py --out nachtrag/quelle.json (Nachtrag, w = d = 1,6 und 2,0 l_P) | 05:55:10 bis 05:57:00 | 109,5 s | 0 |
| NU | cpu5 | code/nachtrag_umkreis.py --out nachtrag/umkreis.json (Nebenarm umkreisbasiert, 8 x 16 Richtungen) | 06:19:18 bis 06:20:35 | 77,3 s | 0 |

- Alle Laeufe ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh (1 Thread, RuntimeMaxSec 600). Die Spur cpu6
  war zeitweise von einem anderen Agenten belegt; meine Laeufe warteten am Lock, keiner wurde abgebrochen.
- Abweichung von PLAN 7: H1 und H2 liefen auf cpu5, Z1, UR und BI auf cpu6 (Plan: H1, H2 auf cpu6; Z1, UR, BI auf
  cpu5); Grund war die Belegung von cpu6. Am Ergebnis aendert das nichts (gleicher Code, 1 Thread).

## 2. Ergebnis zuerst

1. **Die Impulsregel ist die Verschiebungsregel M^H p; sie ist erster Klasse, und der Materie-Impuls koppelt
   widerspruchsfrei daran [M, am Code geprueft].** Regel mit Quelle: M^H p = J, mit J' = -M^H sigma (Gitter-Impulsbilanz,
   P1-Gewichte). Alle Identitaeten halten an allen 5 600 k auf <= 3e-11. **Neu [E]:** Ohne J haengt die Kopplung an die
   TT-Moden von der Eichwahl ab (Laengskopplung je nach Eichung 0 bis 0,015 bei [100], 0,013 bis 0,044 bei [111]); mit J
   ist sie eichunabhaengig, das folgt aus der Herleitung [M] (die Code-Probe dazu ist nur eine Rundungsprobe). Die Groesse
   des Lecks aus PUMPE-NETZ-1 war also keine Eigenschaft des Netzes, sondern hing an der Eichwahl; eichunabhaengig ist
   erst die Rechnung mit J (Punkt 3).
2. **Mitfuehrung wie Einstein [E]:** Die gravitomagnetische Antwort auf einen queren Materiestrom ist mit J_iso an allen
   200 Richtungen und beiden Querrichtungen 1 auf 1,3e-5 (kl = 0,01; das ist etwa die Aufloesungsgrenze, Abschnitt 5.4);
   rotierende und bewegte Quelle je 1 + 7,4e-6, Abweichung waechst grob wie (kl)^2. **IN3 eingetroffen.** Nach Sicht
   erklaerbar [ES]: Mit isotropem TT-Tempo (J_iso) hat die langwellige Bewegungsenergie auf allen spurfreien Tensoren
   denselben Koeffizienten. Mit J = 1 streut sie von 0,975 bis 1,036.
3. **Leckage stark kleiner, aber nicht weg [E]: IN2 nicht eingetroffen.** Die Laengs-Kopplung verschwindet praktisch
   (0,0287 auf <= 6e-11 bei kl = 0,01); die nn-Kopplung sinkt nur auf ein Siebtel bis ein Viertel; der Energie-Kanal V1
   bleibt. Fuer die Kartenquelle wird G_rad/G_N 1,030 / 1,004 / 0,967 statt 1,184 / 0,909 / 0,977. Mit glatteren
   Klumpen (Nachtrag, w = 2,0 l_P) sind es 1,000 / 1,005 / 1,005. Mit umkreisbasierten Gewichten (Nebenarm, Takt-
   konsistent) bleiben kompakte Quellen gleich; die Kartenquelle wird schlechter (1,072 / 0,951 / 0,939).
4. **Kreisbahnen (kompakt, glatt) [E]:** Die Lageabhaengigkeit sinkt von -0,75 % bis +3,4 % auf -0,15 % bis +0,12 %
   (J_iso), wieder linear in Summe m_i^4 der Bahnnormale. Das ist noch rund zwoelfmal mehr, als der Doppelpulsar erlaubt
   (1,3e-4 [P]). Der Rest haengt an den Bewegungsgewichten (J = 1: +0,33 % bis -0,16 %, umgekehrter Gang).
5. **Lesart [H]:** Der Vektor-Sektor (Impulsregel, Mitfuehrung) ist jetzt einsteinsch. Der Rest sitzt im skalaren Sektor
   (Energie und Laengsimpuls), wo die Regel zweiter Klasse bleibt. Naechste Baustelle fuer L1/L10: die skalare Regel mit
   erhaltener Energiequelle zur Regel erster Klasse machen. Nicht gerechnet.

## 3. Urteile

Mechanisch nach PLAN.md (eingefroren 07:46:10 CEST) durch inz.py urteil; Werte aus lauf-69/h1.json und zusatz.json.

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Kartenwortlaut | tragende Zahlen [E] |
|---|---|---|---|---|---|
| IN0 | Kontrolle: ohne Impulskopplung reproduziert der Code PUMPE-NETZ-1 (1,18 / 0,91 / 0,98 auf 1 %) | 90 % | **eingetroffen** | **eingetroffen** | G_rad/G_N ohne J: 1,1844050923687857 / 0,9087749678217026 / 0,9769646539098713, gleich den h1.json-Werten von PUMPE-NETZ-1 (Abweichung 0,0); gegen 1,18 / 0,91 / 0,98: +0,37 % / -0,13 % / -0,31 % |
| IN1 | [H] Es gibt im jetzigen Hamilton-Netz eine widerspruchsfreie Impulskopplung | 55 % | **eingetroffen** | **eingetroffen** | Rang [M, c] = 40 an allen k; c^H M 1,6e-15; M^H B 8,7e-16 (erste Klasse); M^H p_J = J auf 2,8e-11; c^H p_J 2,2e-13; Cholesky ueberall; Eichprobe mit J 1,3e-14 (per Konstruktion, nur Rundung) |
| IN2 | [H] Mit Impulskopplung G_rad/G_N fuer alle drei Achsen innerhalb 1e-2 bei 1 | 40 % | **nicht eingetroffen** | **nicht eingetroffen** | V1+S+J dynamisch, kl = 0,01, J_iso: 1,02966 ([001]) / 1,00401 ([111]) / 0,96747 ((1,2,3)); verfehlt durch [001] und (1,2,3) |
| IN3 | [H] Die Mitfuehrung hat den Einstein-Koeffizienten auf 10 % | 40 % | **eingetroffen** | **eingetroffen** | kl = 0,01, J_iso: R_rot = R_mov = 1,0000074 fuer [001], [111], (1,2,3); R_iso 1,0000074; r(n, e) 0,9999967 bis 1,0000132 an 200 Richtungen |

- **Bedeutung, wie auf der Karte vorab festgelegt:** Keiner der beiden Bedeutungssaetze ist ganz ausgeloest.
  - "IN1 verfehlt" ist nicht eingetreten: Das jetzige Netz kann den Impuls aufnehmen.
  - "IN2 und IN3 treffen ein" ist nur zur Haelfte erfuellt: Das Netz dreht wie bei Einstein (IN3); es strahlt fuer die
    Kartenquelle aber nicht innerhalb 1e-2 wie Einstein (IN2). Doppelpulsar und Lense-Thirring sind also nicht beide "im
    Bereich" (Abschnitt 6). L10 hat einen ersten gemeinsamen Baustein im Vektor-Sektor, nicht im skalaren.
- **Ableitbarkeit:**
  - IN0 war vorab ableitbar (gleicher Rechenweg; PLAN 2). Gerechnet ist es bitgleich.
  - IN1 war vorab ableitbar (PLAN 1.2, 2): Es folgt aus B M = 0 und c^H M = 0. **Die Zahlen sind Identitaeten, keine
    Messung.** Nicht vorab bekannt war die Groesse der Eichabhaengigkeit ohne J (Abschnitt 5.3).
  - IN3 hatte ich im Plan als nicht ableitbar eingestuft. Nach Sicht gibt es ein Symmetrieargument (Abschnitt 4.4) [ES];
    vorab habe ich es nicht gesehen (Selbstanzeige 5).
  - Vorab ableitbar war auch, dass die sechs Plan-Werte R_rot, R_mov und das Mittel R_iso dieselbe Zahl sind
    (Gegenleser B2): Summe_n w_n P_n Q(n) P_n ist ein symmetrischer Tensor zweiter Stufe und bei kubischer Symmetrie
    proportional zu delta_ij, also unabhaengig von L und v [M]. Plan und Kartenwortlaut pruefen bei IN3 dieselbe Zahl.
  - IN2 war nicht ableitbar und ist es auch nach Sicht nicht. Einordnung (nach Sicht, beschreibend, kein Urteil): IN2
    scheitert an der Kartenquelle, Klumpen von Gitterkantengroesse. Im Nachtrag mit w = d = 1,6 und 2,0 l_P laegen alle
    drei Achsen innerhalb 1e-2 (groesste Abweichung 0,0091 bzw. 0,0050).

## 4. Formulierung der Impulskopplung (Teil 1)

### 4.1 Impulsregel und Kopplung [M]

- **Netzgroesse:** die Verschiebungsregel M^H p (3 Komponenten je Ecke). Sie erzeugt die Eckverschiebung,
  {a, xi^H M^H p} = M xi; ihr Multiplikator ist der Shift nu. In ew.py steckt sie schon in der R1-Projektion (p senkrecht
  auf Bild [M, c]).
- **Erster Klasse:** d/dt (M^H p) = -kappa_g M^H B a = 0, weil B M = 0 (gerechnet 8,7e-16). Sie vertauscht mit dem skalaren
  Paar, weil c^H M = 0 (1,6e-15). Das unterscheidet sie von der skalaren Regel, die zweiter Klasse ist (TT-ISO-1,
  GAMMA-NETZ-L [P]).
- **Kopplung:** M^H p = J; J_v = Int psi_v T^(0i) (P1-Hutfunktion der Ecke, dieselben Gewichte wie die Spannung). In der
  Hamilton-Funktion steht -nu^H J (Shift mal Impulsdichte, wie N_i H^i in ADM). Die Normierung ist durch die Forderung
  festgelegt, dass die Regel die Gesamtverschiebung erzeugt; es gibt keine neue Konstante.
- **Widerspruchsfrei genau dann, wenn J' = -M^H sigma** (Gitter-Impulsbilanz: Impulsaenderung an der Ecke = minus
  Nettokraft der Spannung). Fuer sigma_0 cos(omega t): J = -M^H sigma_0 sin(omega t)/omega. p_J = M (M^H M)^-1 J liegt in
  Bild M; c^H p_J = 0 gilt dann von selbst (2,2e-13), und M^H p_J = J auf 2,8e-11.

### 4.2 Wirkung auf die TT-Moden [M]

- R1 mit p = S y + p_J: x' = (A_red y + S^H A p_J)/kappa_g. Effektive Kraft f_eff = f_red - A_red^-1 S^H A P_M sigma,
  in Phase mit der Spannung und unabhaengig von omega.
- Modenkopplung g_j = -e_j^H sigma (+ V1) mit **e_j = (1 - P_c) A p_j**: Die Spannung koppelt an die ungeprojizierte
  Geschwindigkeit der Mode, nicht an ihre R1-Form. Ohne J koppelt sie an die R1-Form TT + M xi_j; deren Eichanteil
  M xi_j haengt von der Eichwahl ab.
- Die Bewegungsenergie in ew.py ist je Tetraeder eine DeWitt-Form: A0_ef = (n_e.n_f)^2 - 1/2 = G(n_e n_e, n_f n_f) mit
  G(X, Y) = X:Y - (1/2) tr X tr Y. Im Kontinuum ist dann e_j rein TT. Auf dem Gitter misst die Rechnung, wie weit das gilt.

### 4.3 Grenzen [ES]

- Fuer eine vorgegebene Quelle (wie hier) ist J durch die Bilanz definiert. Fuer ein dynamisches Gitter-Materiefeld ist
  die gemeinsame Eckverschiebung keine exakte Symmetrie der P1-Energie; ein lokal aus (phi, phi') gebildetes J erfuellt
  die Bilanz dann nur bis auf Gitterfehler. Nicht gerechnet.
- Der Energie-Kanal V1 bleibt wie in PUMPE-NETZ-1: Energie in der skalaren Regel, aus der Kontinuums-Erhaltung gesetzt,
  zweiter Klasse. Die Impulskopplung aendert daran nichts.
- Die Quelle enthaelt Gitterfeinstruktur: Ein Klumpen von Kantengroesse uebt Kraefte auf die Untergitter gegeneinander
  aus. Mit J werden diese als Impuls weitergegeben; das macht das Ergebnis der Kartenquelle groessenabhaengig (5.1).

### 4.4 Nach Sicht: warum die Mitfuehrung einsteinsch ist [ES, nicht vorab]

- Langwellig sind TT-Impulse und quere Vektor-Impulse (sym(k e), e senkrecht k) beide spurfreie symmetrische Tensoren
  (Spin 2). Bei kubischer Symmetrie zerfaellt Spin 2 in zwei Teile (E_g, T_2g) mit je einem Koeffizienten der
  langwelligen Bewegungsenergie. Ein isotropes TT-Tempo in allen Richtungen erzwingt gleiche Koeffizienten (bei [100] liegen
  die beiden TT-Zweige je in einem der Teile). Dann hat der Vektor-Sektor denselben Koeffizienten wie der TT-Sektor, und
  mit c := c_TT folgt die Einstein-Mitfuehrung.
- Das passt zu den Zahlen: Rest 1e-5 wie die TT-Spanne von J_iso (1,1e-5 [P]); mit J = 1 (TT-Spanne 6,3 % in TT-ISO-1
  [P], 13 Richtungen; in H1 6,0 % an 200 Richtungen, kl 0,005) streut r von 0,975 bis 1,036. Vorausgesetzt ist, dass die
  langwellige Bewegungsenergie eine lokale Tensorform ist; bewiesen habe ich das nicht.

## 5. Tabellen

### 5.1 G_rad/G_N je Quellachse, ohne und mit Impulskopplung (kl = 0,01; G_N/G = 1,000005) [E]

| Groesse | [001] | [111] | (1,2,3) | Lauf |
|---|---|---|---|---|
| ohne J, V1+S, dynamisch, J_iso (IN0) | 1,18441 | 0,90877 | 0,97696 | H1 |
| ohne J, S, dynamisch, J_iso | 1,17042 | 0,91096 | 0,97585 | H1 |
| **mit J, V1+S+J, dynamisch, J_iso (IN2)** | **1,02966** | **1,00401** | **0,96747** | H1 |
| mit J, S+J, dynamisch, J_iso | 1,02080 | 1,01131 | 0,97102 | H1 |
| mit J, S+J, quasistatisch, J_iso (KDJ: dynamisch/quasistatisch - 1 = 4,8e-6 / 3,6e-6 / 4,1e-6) | 1,02080 | 1,01130 | 0,97101 | H1 |
| mit J, V1+S+J, quasistatisch, J_iso | 1,05203 | 0,99440 | 0,96500 | H1 |
| mit J, S+J, dynamisch, J = 1 (naeherungsweise) | 1,01658 | 0,99889 | 0,97599 | H1 |
| mit J, V1+S+J, dynamisch, J = 1 (naeherungsweise) | 1,02617 | 0,99224 | 0,97303 | H1 |
| mit J, S+J, quasistatisch, J = 1 | 1,02636 | 0,99144 | 0,97256 | H1 |
| Quadratur 12 x 24: V1+S+J / ohne J V1+S | 1,0296610 / 1,18441 | 1,0040051 / 0,90877 | 0,9674684 / 0,97696 | H2 |
| Nachtrag w = d = 1,6 l_P: V1+S+J / S+J / ohne J V1+S | 0,99995 / 0,99094 / 1,17583 | 1,00874 / 1,01594 / 0,90652 | 1,00913 / 1,01238 / 0,97161 | NQ |
| Nachtrag w = d = 2,0 l_P: V1+S+J / S+J / ohne J V1+S | 0,99995 / 0,99092 / 1,17568 | 1,00479 / 1,01197 / 0,90734 | 1,00495 / 1,00813 / 0,97330 | NQ |
| kompakte Grenze (affines Spannungsmuster, Z1), S+J / S ohne J, statisch | 0,99115 / 1,16221 | 1,00733 / 0,91184 | 1,00370 / 0,96713 | Z1 |

- Gang mit kl (V1+S+J, J_iso): [001] 1,0297 (kl 0,01), 1,0323 (0,1), 1,0402 (0,2), 1,0537 (0,3); [111] 1,0040 / 1,0055 /
  1,0101 / 1,0178; (1,2,3) 0,9675 / 0,9691 / 0,9741 / 0,9825. Der Rest ist langwellig konstant, wie das Leck ohne J.
- Quadratur (KQ, beschreibend, im Plan ohne Soll): H2 gegen H1 mit J <= 2,7e-8 relativ (S+J, [001]), ohne J <= 3,7e-6
  (S, [001]).
- Quellgroesse (Nachtrag, beschreibend): Ohne J aendert sie G_rad kaum (1,184 / 1,176 / 1,176 fuer [001]). Mit J naehert
  sich S+J mit wachsender Breite der kompakten Grenze, fuer [111] nicht monoton ([111]: 1,0113 / 1,0159 / 1,0120 gegen
  1,0073; (1,2,3): 0,9710 / 1,0124 / 1,0081 gegen 1,0037; [001]: 1,0208 / 0,9909 / 0,9909 gegen 0,9912). Lesart [ES]: Die
  Kartenquelle (Klumpen von Gitterkantengroesse) traegt Untergitter-Impuls, den es im Kontinuum nicht gibt. Bei
  w = 2,0 l_P beruehrt die Quelle den Kasten schon etwas (Randanteil 0,2 %).
- Die Kraft aus J ist so gross wie die Spannungskraft selbst (Median-Verhaeltnis der Normen 0,77 bis 1,37 je k und Quelle,
  J_iso). Die TT-Kopplung aendert sie nur um die oben genannten Prozente; sie wirkt also vor allem auf steife Moden [ES].

### 5.2 Kreisbahnen (kompakte spurfreie Quelle, kl = 0,01, 10 x 20 Richtungen; G_rad/G) [E]

| Bahnnormale m | Summe m_i^4 | ohne J (statisch = ND) | mit J, J_iso | mit J, J = 1 | nur TT-Anteil, mit J |
|---|---|---|---|---|---|
| [001] | 1 | 1,03438 | 0,99850 | 1,00327 | 1 + 1,5e-6 |
| [111] | 1/3 | 0,99253 | 1,00122 | 0,99837 | 1 + 1,8e-6 |
| [110] | 1/2 | 1,00299 | 1,00054 | 0,99960 | 1 + 1,8e-6 |
| (1,2,3) | 1/2 | 1,00299 | 1,00054 | 0,99960 | 1 + 1,8e-6 |
| 8 Zufallsnormalen (Saat 31) | 0,363 bis 0,988 | 0,99441 bis 1,03364 | 0,99855 bis 1,00110 | 0,99859 bis 1,00319 | 1 + 1,5e-6 bis 1,8e-6 |

- Kontrolle KND: ohne J gleich dem Nachtrag ND von PUMPE-NETZ-1 (1,0344 / 0,9925 / 1,0030 / 1,0030; phi kompakt 1,1622 /
  0,9118 / 0,9671 [P]). Dynamisch (J_iso) gleich statisch auf <= 9,2e-7 (Bahnen <= 6,6e-7).
- Mit J (J_iso) liegt G_rad/G = 1 + 0,004077 (0,6331 - Summe m_i^4) auf allen 12 Bahnen, auf etwa 1e-8 (Koeffizienten aus
  [001] und [111]; mit den gerundeten Werten 0,00408 und 0,633 auf 1,5e-6). Ohne J: 1 + 0,0628 (Summe m_i^4 - 0,452)
  [P, hier bestaetigt]. Der Gang ist rund 15-mal kleiner.
- Mit J = 1 kehrt sich der Gang um (Nullstelle bei 0,555). Der Rest haengt also an den Bewegungsgewichten [E].
- Der V1-Kanal (Energie in der skalaren Regel) fehlt in dieser Rechnung wie in ND. Fuer die phi-Quelle verschiebt er
  G_rad mit J um +0,9 % / -0,7 % / -0,4 % (H1) bzw. +0,9 % / -0,7 % / -0,3 % (w = 1,6 l_P).

### 5.3 Isotropie und Eichprobe (gleichfoermige Spannung, J_iso) [E]

| Groesse | ohne J | mit J |
|---|---|---|
| TT-Kopplung R (Winkelmittel 72 Richtungen; Eigenwerte) | 1,0000019 (1,0000006 bis 1,0000028) | 1,0000017 (1,0000000 bis 1,0000029) |
| Laengs C_L max (72 Richtungen, kl 0,01; benannt bis 5,8e-11 bei [210]) | 0,0279 | 2,6e-11 |
| C_L1 bei [111], kl 0,01 / 0,1 | 0,028690 / 0,028675 | 2,6e-13 / 2,3e-9 (wie (kl)^4; bei [210] und (1,2,3) fuer L2 nur etwa wie (kl)^2,3) |
| nn C_nn max (72 Richtungen) | 0,0043 | 0,00095 |
| C_nn bei [110] / [210] / [211] / (1,2,3), kl 0,01 | 0,00568 / 0,00195 / 0,00099 / 0,00231 | 0,00132 / 0,00052 / 0,00015 / 0,00049 |
| quere Spur C_Ptr max | 3e-14 | 1,6e-13 |
| C_nn bei [100], [001] und den vier Diamant-Richtungen (kl 0,01 und 0,1) | <= 5e-23 | <= 1,2e-21 |

- **Eichprobe KE** (10 benannte Richtungen, kl 0,01 und 0,1, zwei zufaellige positive Diagonal-Eichungen G):
  - Mit J: Kraft und Kopplung gleich auf 1,3e-14 (IN1).
  - Ohne J aendert die Eichwahl die Laengs- und nn-Kopplung stark. C_L1 bei [111]: 0,0287 (R1), 0,0126 und 0,0438 (G1,
    G2); bei [100]: 0 (R1), 0,0075 und 0,0153; C_nn bei [001]: 0, 0,0007 und 0,0103. Die TT-Kopplung (h+, hx) aendert
    sich nur um <= 6e-5 relativ.
  - Die reduzierte Kraft ohne J aendert sich je nach Eichung und Spannung um bis zu 370 % ihrer Norm; die Kopplung um bis
    zu 0,035 in Einheiten von C_E (L2), relativ bis Faktor 6,4.
  - Folge [ES]: Ohne Impulskopplung ist das Leck keine Eigenschaft des Netzes. Auch die Nullstellen bei [100] und [111]
    (PUMPE-NETZ-1, Symmetrie) gelten nur in der symmetrischen R1-Eichung.
- Ableitbarkeit der Nullen: C_nn = 0 bei [100] und [111] gilt mit und ohne J, hier bei k != 0 am Code geprueft (R1).

### 5.4 Mitfuehrung gegen Einstein (Bezug 8 pi G c_0^2 V_Zelle abs(e_T)^2/k^2, vorab [M], keine Messung) [E]

| kl | J_iso: R_iso | r_min bis r_max (200 Richtungen, beide Querrichtungen) | R_rot = R_mov ([001], [111], (1,2,3)) | J = 1: R_iso | J = 1: r_min bis r_max |
|---|---|---|---|---|---|
| 0,01 | 1,0000074 | 0,9999967 bis 1,0000132 | 1,0000074 (alle sechs) | 0,99890 | 0,9751 bis 1,0356 |
| 0,02 | 1,0000225 | 1,0000080 bis 1,0000357 | 1,0000225 | 0,99892 | 0,9752 bis 1,0356 |
| 0,05 | 1,0001281 | 1,0000272 bis 1,0001934 | 1,0001281 | 0,99905 | 0,9753 bis 1,0358 |
| 0,1 | 1,0005047 | 1,0000938 bis 1,0007562 | 1,0005047 | 0,99954 | 0,9757 bis 1,0363 |
| 0,2 | 1,0020055 | 1,0003625 bis 1,0030005 | 1,0020055 | 1,00147 | 0,9775 bis 1,0385 |

- Benannte Richtungen (J_iso, kl 0,01): [100] und [001] 1,0000109 (beide Querrichtungen); [111] und die drei anderen
  Diamant-Richtungen 1,0000133; [110] 1,0000059 / 1,0000126; (1,2,3) 1,0000028 / 1,0000117.
- R_rot und R_mov sind dem isotropen Mittel gleich: auf 1e-11 bei kl = 0,01, auf 7e-10 bei kl = 0,2. Das war vorab
  ableitbar (kubische Symmetrie, Abschnitt 3, Gegenleser B2); der Rest ist die Quadratur.
- Aufloesung: Der Bezug nimmt c_0 = 0,32373345 (Mittel bei kl = 0,01); mit dem H1-Wert 0,323734 (kl = 0,005) verschiebt
  sich R um etwa 3e-6. Der Rest 7,4e-6 bei kl = 0,01 liegt also nahe an der Aufloesungsgrenze; von kl 0,01 auf 0,02
  waechst R - 1 um den Faktor 3,0, von 0,1 auf 0,2 um 4,0.
- J = 1: c_0 = 0,349212 (quadratisches Mittel ueber Richtungen und Zweige), nur naeherungsweise.
- Kontrollen: KGM (H_min = -(1/2) J^H nu) <= 8,1e-13; S^H A p_stat <= 5,4e-16 relativ; H_min fuer quere Stroeme ueberall
  positiv.
- **Laengsanteil (beschreibend, eichabhaengig):** k^T Q k relativ zu 2 pi G c_0^2 V_Zelle/k^2 ist **negativ**: J_iso
  -0,559 im Mittel (-0,669 bis -0,428 an den 200 Richtungen; benannt [111] -0,681, [100] -0,395), J = 1 -0,533. Der
  Bezug ist nur meine Kontinuumsanalogie zu c^H p = 0 [ES]. Der negative Wert deutet an, dass der Laengsimpuls die
  negative Spur-Richtung der DeWitt-Form erreicht [ES]. Quer-Laengs-Kopplung bis 6,6 % (J_iso) bzw. 3,9 % (J = 1) von
  sqrt(Q_TT Q_LL); im Kontinuum null. Nicht weiter untersucht.

### 5.5 Kontrollen [E]

| Kontrolle | Wert | Soll |
|---|---|---|
| KP1 (P1-Energie, Spannung gleichfoermig) | 6,1e-16; 1,8e-15 | <= 1e-10 |
| KR: Rang [M, c]; c^H M (H1, H2, NQ) | 40 ueberall; <= 1,6e-15 | 40; <= 1e-10 |
| **KF: M^H B (erste Klasse)** | 8,7e-16 (H1), 9,1e-16 (H2) | <= 1e-10 |
| **KJ: M^H P_M sigma = M^H sigma; c^H p_J** | 2,8e-11 (H1), 3,1e-11 (H2), 1,1e-10 (NQ, w = 2,0); 2,2e-13 | <= 1e-10 (NQ knapp darueber, Nachtrag) |
| **KE mit J** (per Konstruktion gleich; misst nur Rundung) | 1,3e-14 | <= 1e-8 |
| KN: weiche Takt-Richtung lambda/k^2 (G_N/G) | 0,1999990 (1,000005) | 0,2 |
| KD: dynamisch S gegen statisch S (J_iso, kl 0,01, beide durch G_N/G geteilt) | 1,170419 / 1,170415 ([001]), wie PUMPE-NETZ-1 | gleich |
| KDJ: dynamisch S+J gegen quasistatisch (J_iso) | 1 + 4,8e-6 / 3,6e-6 / 4,1e-6 | gleich |
| KQ: 12 x 24 gegen 10 x 20 (beschreibend) | mit J <= 2,7e-8; ohne J <= 3,7e-6 | kein Soll im Plan |
| KM: Massenschale nicht monoton oder ausserhalb | 0 (alle kl, beide J) | 0 |
| KGM; Stationaritaet | 8,1e-13; 5,4e-16 | <= 1e-8; <= 1e-10 |
| KND: Kreisbahnen ohne J gegen ND | gleich auf 1e-7 | gleich |
| TT-Tempo Omega^2/k^2 (J_iso, kl 0,005) | 0,1048028 bis 0,1048039 | 0,10480 [P] |
| Summe der Eckvolumina | 0,25 | V_Zelle = 0,25 |

- **Agenten-Erwartungen (PLAN 6, kein Kartenurteil):**
  - Z1 (Identitaeten <= 1e-10 bzw. 1e-8, 90 %): eingetroffen (H1, Z1).
  - Z2 (Eichwahl aendert ohne J eine Kopplung um mehr als 10 %, 75 %): eingetroffen (Faktor bis 6,4).
  - Z3 (S+J innerhalb 0,05 fuer alle Achsen, 50 %): eingetroffen (1,021 / 1,011 / 0,971).
  - Z4 (R_iso in [0,5; 2], 70 %): eingetroffen (1,0000074).
- Latten: L1 (kann scheitern) ja: IN2 ist gescheitert. L2 (Gegenprobe): zwei Eichungen, dynamisch gegen quasistatisch,
  zwei Quadraturen, zwei J, drei Quellgroessen, kompakte Grenze. L3 (Numerik): Identitaeten 1e-16 bis 3e-11. L4 (bekannt):
  ADM-Impulsbedingung und Lense-Thirring-Koeffizient [L]; P1 und Einstein-Kopplung [P]. L5 (Messbezug): Abschnitt 6.

### 5.6 Nebenarm: umkreisbasierte Gewichte *1 statt P1 (Bitte der Leitung, nach Sicht, beschreibend, kein Urteil) [E]

- Umsetzung: code/nachtrag_umkreis.py ersetzt pn.K_aus_laengen nur im eigenen Prozess durch die umkreisbasierte Form
  (Gewicht je Kante und Tetraeder aus Umkreismitten, Formel im Kopf des Skripts; Dateien unveraendert) und ruft inz.lauf
  (8 x 16 Richtungen) und inz.zusatz wie eingefroren. Eckvolumina bleiben baryzentrisch; Mitfuehrung haengt nicht von den
  Gewichten ab und ist unveraendert.
- Proben: Ecktetraeder (0, e1, e2, e3): Kante 0-e1 P1 1/6, umkreisbasiert 1/4; Kante e1-e2 P1 0, umkreisbasiert -1/24
  (wie die Leitung von Hand). Regulaeres Tetraeder: beide 1/6. Summe l^2 w = 3 V in beiden Faellen.
- Auf dem Netz V (zusammengesetzt je Kante): P1 1/60 bis 1/2, umkreisbasiert 1/720 bis 1/2; in beiden Faellen alle 68
  Kanten positiv; kleinster Laplace-Eigenwert an 300 Zufalls-k 0,0144 (beide). Je Zelle sind beide fuer gleichfoermige
  Gradienten exakt: Energie und Summe sigma_e n_e n_e^T = -V_Zelle T auf <= 2e-15.

| G_rad/G_N, kl = 0,01, J_iso, dynamisch | [001] | [111] | (1,2,3) |
|---|---|---|---|
| P1 (H1): ohne J V1+S / mit J V1+S+J / mit J S+J | 1,184 / 1,030 / 1,021 | 0,909 / 1,004 / 1,011 | 0,977 / 0,967 / 0,971 |
| umkreisbasiert (NU, 8 x 16): ohne J V1+S / ohne J S | 1,2198 / 1,2056 | 0,8911 / 0,8933 | 0,9798 / 0,9786 |
| umkreisbasiert (NU, 8 x 16): mit J V1+S+J / mit J S+J | 1,0717 / 1,0627 | 0,9511 / 0,9582 | 0,9391 / 0,9424 |

- Kreisbahnen und kompakte phi-Quellen (affines Spannungsmuster) und die Isotropie-Tabelle: umkreisbasiert gleich P1 auf
  <= 1e-6 (z. B. Bahn [001] mit J 0,998504 gegen 0,998504; C_L max mit J 2,6e-11; C_nn max mit J 0,00095; TT 1 + 2e-6).
  Eichprobe ohne J: Kopplung aendert sich wieder bis 0,035 in Einheiten von C_E; mit J 1,2e-14 (Rundung).
- Lesart [ES]: Fuer glatte, kompakte Quellen (Doppelstern) ist es gleich, welche der beiden Formen man nimmt. Die
  Kartenquelle (Klumpen von Kantengroesse) spuert dagegen die Feinstruktur der Gewichte, und mit J noch staerker.
  Umkreisbasiert ist die Abweichung mit J bis 7 %, mit P1 bis 3,3 %. Fuer L10 heisst das: Der Takt-konsistente Fall
  verschlechtert die gittergrosse Quelle, aendert aber nichts an der Doppelstern-Aussage (Abschnitt 6).
- Meine Formulierung (Teil 1) beruht nicht auf der Gleichsetzung P1 = *1: Sie braucht nur, dass sigma die Ableitung
  einer Materie-Energie nach den Kantenlaengen ist, und J' = -M^H sigma. Mit umkreisbasierten Gewichten gilt sie
  unveraendert (Eichprobe mit J auch hier 1,2e-14).

## 6. Bedeutung fuer Doppelpulsar, Lense-Thirring und L10 [H]

- **Doppelpulsar:** Er bestaetigt die Quadrupolformel auf 1,3e-4 (Kramer u. a. 2021, Phys. Rev. X 11, 041050; in
  PUMPE-NETZ-1 an der Quelle gelesen [P]).
  - Mit Impulskopplung haengt die Abstrahlung einer glatten Kreisbahn noch um -0,15 % bis +0,12 % von ihrer Lage zum Gitter
    ab. Vertraeglich ist ein Band der Breite 0,064 in Summe m_i^4 (von 1/3 bis 1), statt 0,004 ohne J [E, ES].
  - Dazu kommt der Energie-Kanal V1, der in der Bahnrechnung fehlt; fuer die phi-Quelle verschiebt er G_rad mit J um bis
    zu 0,9 % [E]. Fuer eine Kreisbahn ist er nicht gerechnet.
  - Vertraeglich mit dem Doppelpulsar ist also nur, wenn seine Bahnnormale zufaellig im Band Summe m_i^4 = 0,60 bis 0,67
    liegt (rund ein Zehntel der Spanne 1/3 bis 1); fuer die meisten Lagen waere das Netz schon durch ihn ausgeschlossen,
    mehrere genaue Doppelsterne wuerden es wohl ganz ausschliessen [ES; deren Genauigkeit L?]. Die groesste Abweichung liegt jetzt rund
    12-mal ueber der Schranke (0,15 % gegen 1,3e-4), ohne J waren es rund 260-mal (3,4 %).
- **Lense-Thirring:** Gravity Probe B mass -37,2 +- 7,2 mas/Jahr gegen -39,2 mas/Jahr der ART (Everitt u. a. 2011, Phys.
  Rev. Lett. 106, 221101, arXiv:1105.3456 [S, Abstract]). LARES/LAGEOS: 0,9910 +- 0,02 in Einheiten des ART-Werts
  (Ciufolini u. a. 2019, Eur. Phys. J. C 79, 872, arXiv:1910.09908 [S, Abstract]; die 2 % sind die Angabe der Autoren, ihre
  Fehlerabschaetzung ist umstritten [L?]).
  - Mit Impulskopplung (J_iso) liegt die Mitfuehrung des Netzes auf 1e-5 beim ART-Wert; beide Messungen sind damit
    vertraeglich [E, ES]. Ohne Impulskopplung gab es keine Mitfuehrung; das waere durch beide Messungen ausgeschlossen [ES].
  - Mit J = 1 (anisotropes TT-Tempo) weicht sie je Richtung um bis zu 3,6 % ab, im Mittel um 0,1 %. Ob das mit LARES
    vertraeglich ist, haengt an der Bahngeometrie; nicht gerechnet.
  - Vorzugssystem: Der quere Teil (Mitfuehrung) ist einsteinsch. Der Laengsteil ist negativ, anisotrop und mit dem queren
    gekoppelt (5.4). Ob daraus Vorzugssystem-Effekte folgen (PPN alpha_1, alpha_2 [L?]), ist offen [H].
- **L10 (gemeinsame Wirkung, universelle Kopplung):**
  - Erster gemeinsamer Baustein [ES]: Spannung und Impuls der Materie koppeln ueber eine Hamilton-Funktion mit einer Regel
    erster Klasse. Kopplung und Rueckwirkung stammen aus demselben Term -nu^H J (Gegenseitigkeit, Ideation Rang 1, hier fuer
    den Vektor-Sektor erfuellt). G der Mitfuehrung = G_N = G der TT-Abstrahlung, und c der Mitfuehrung = TT-Tempo.
  - Offen [H]: Der Rest des Lecks (nn-Kanal, Energie-Kanal V1) sitzt im skalaren Sektor. Dort ist die Regel zweiter Klasse,
    und die Energiequelle ist nicht auf dem Gitter erhalten. Vermutung: Eine skalare Regel erster Klasse mit Energiequelle
    m' = -(Gitterdivergenz von J) wuerde auch diese Reste beheben, so wie J den Laengsrest behebt. Das ist die naechste
    Baustelle fuer L1 und L10. Bindungsenergie (Ideation Rang 8) ist hier nicht beruehrt.
  - Gemeinsame Gewichte [E, ES]: Mit den Takt-konsistenten umkreisbasierten Gewichten (5.6) bleibt die Doppelstern-Aussage
    gleich (kompakte Quellen auf 1e-6), die Mitfuehrung ebenso (haengt nicht von den Materie-Gewichten ab). Nur gittergrosse
    Quellen lecken staerker (mit J bis 7 % statt 3,3 %). Fuer eine gemeinsame Wirkung sind beide Gewichtsformen also im
    langwelligen Grenzfall gleichwertig; welche die richtige ist, entscheidet erst die Feinstruktur [H].

## 7. Selbstanzeigen

1. **Lokales python:** Zwischen 07:35:24 und 07:41:49 CEST (date davor und danach) habe ich lokal versehentlich
   `python3 -` gestartet (ohne Skript, Eingabe leer, Ausgabe verworfen). Es hing rund 120 s bis zum Werkzeug-Zeitlimit, dann
   habe ich es gestoppt. Gerechnet wurde nichts; es verstoesst trotzdem gegen "Lokal kein python".
2. **sed:** inz.py (Option --voll) habe ich vor dem Einfrieren per sed in eine neue Datei geschrieben und per mv ersetzt;
   nicht in place, vermerkt. Auf der .69 lagen alle Fassungen in neuen Ordnern (code-r1, code-r2, code). ERGEBNIS.md
   habe ich einmal per head und Heredoc in eine neue Datei geschrieben und per mv ersetzt.
3. **Plan nach den ersten Rauchtests geaendert, vor dem Einfrieren:** KE-Masstab (Kopplung relativ zur Einstein-Skala),
   KS durch benannte Richtungen ersetzt, KA/KT/KG nicht wiederholt, KND ergaenzt. Anlass war ueberlegt, nicht gesehen: r1
   und r2 gaben nur Schluessel und Zeiten.
4. **Rauchtests r3 bis r6** schrieben vollstaendige Werte (mit --voll), um urteil und bild zu pruefen. Gelesen habe ich nur
   Rueckgabewert und Schluessel; die Dateien r3.json bis r6.png sind nicht kopiert.
5. **Ableitbarkeitsprobe unvollstaendig:**
   - IN3: Den Grund fuer das Einstein-Ergebnis (Spin-2-Argument, 4.4) habe ich erst nach Sicht gesehen. Im Plan stand
     "nicht ableitbar". IN3 ist damit weniger unabhaengig, als es aussieht: Es folgt weitgehend aus der TT-Abstimmung
     J_iso (TT-ISO-1).
   - Dass die sechs Plan-Werte von IN3 und das Mittel R_iso aus Symmetrie dieselbe Zahl sind, war vorab ableitbar
     (Gegenleser B2); der Plan pruefte damit nach Plan und Wortlaut dieselbe Groesse.
   - Die Eichprobe KE mit J ist nach der Herleitung algebraisch exakt; die Code-Probe misst nur Rundung (Gegenleser B1).
     Der IN1-Teil "KE mit J <= 1e-8" der Planregel war damit vorab erfuellt; IN1 bleibt insgesamt vorab ableitbar.
6. **Nachtraege nach Sicht:** NQ (Quellgroesse) und NU (umkreisbasierte Gewichte, Bitte der Leitung), beide
   beschreibend; sie aendern kein Urteil. KJ liegt in NQ bei w = 2,0 mit 1,1e-10 knapp ueber der Plan-Schranke 1e-10.
   Code-Pruefsummen der Nachtraege in nachtrag-69/PRUEFSUMMEN-CODE.txt (auf der .69 erzeugt, lokal bestanden).
7. **Energie-Kanal und Laengsbezug:** V1 ist unveraendert aus PUMPE-NETZ-1 (Kontinuums-Erhaltung, nicht Gitter). Der
   Bezug 2 pi G fuer den Laengsanteil ist meine Analogie [ES]; den negativen Wert habe ich nicht weiter untersucht.
8. **Kreisbahnen ohne V1** (wie ND); kompakte Grenze statisch bzw. dynamisch bei kl = 0,01, nur J_iso dynamisch.
9. **Abrufe:** zwei (GP-B, LARES), je nur Abstract. Doppelpulsar-Zahl aus PUMPE-NETZ-1 [P] uebernommen. PPN-Schranken und
   die Genauigkeit weiterer Doppelsterne nur [L?], ohne Zahlen.
10. **Plan ungenau (Gegenleser C10):** PLAN 1.4 (eingefroren) nennt fuer zwei Punktstroeme 4 G (m1 v1).(m2 v2)/r. Das ist
    der volle g_0i-Anteil in harmonischer Eichung; der quere Anteil allein, den ich als Bezug nehme, gibt
    2 G [v1.v2 + (n.v1)(n.v2)] m1 m2/r. Die Bezugsformel 8 pi G abs(j^T)^2/k^2 selbst ist richtig; kein Urteil betroffen.
11. **Gewichte (Hinweis der Leitung):** Meine Formulierung und alle Urteile verwenden P1-Gewichte. Die Gleichsetzung
    "P1 = umkreisbasierter Stern *1" aus PUMPE-NETZ-1 habe ich in meinen Texten nicht verwendet; der Kopf von pn.py
    (uebernommen, unveraendert) nennt die P1-Form "Hodge-Gewichte", die Karte "P1-Hodge-Gewichte". Der Takt des Netzes ist
    nach TAKT-UMKLAPP-1 [P] 8 x der umkreisbasierte Laplace; Materie (P1) und Takt verwenden in H1 also verschiedene
    Sterne. Der Nebenarm 5.6 rechnet den Takt-konsistenten Fall beschreibend nach.
12. **Werkzeug-Protokolle im Scratchpad:** Zwei zeitueberschrittene Bash-Aufrufe (der versehentliche python-Start und der
    ssh-Aufruf fuer UR/BI), ein Warte-Monitor und der Gegenleser legten ihre Protokolle automatisch unter
    /tmp/claude-1000/.../tasks/ ab. Selbst
    geschrieben habe ich dort nichts; alle Ergebnisse liegen in impuls-netz-1/ und auf der .69.

## 8. Einfach gesagt

Finns Netz hat schon eine Regel dafuer, wie sich seine Ecken verschieben duerfen; wir haben den Schwung der Materie an
diese Regel gekoppelt, und das geht ohne Widerspruch. Damit zieht eine rotierende oder bewegte Masse das Netz mit, genau
so stark wie bei Einstein, bis auf etwa ein Hunderttausendstel. Die falsche Richtungsabhaengigkeit der Wellen wird viel
kleiner, verschwindet aber nicht ganz: Bei Doppelsternen bleibt je nach Lage bis gut ein Promille, und der Doppelpulsar
erlaubt nur gut ein Zehntelpromille. Vermutlich steckt der Rest in der Regel fuer Energie und Takt, die im Netz noch nicht
so sauber gebaut ist wie die fuer den Schwung.

## 9. Dateien

- KARTE.md (unveraendert), PLAN.md, PLAN.md.eingefroren-20261005-074610, EINGEFROREN-SHA256.txt.
- code/: inz.py (neu), pn.py, ew.py, tp.py, mn.py, nachtrag_iso.py (unveraendert aus PUMPE-NETZ-1), je mit
  .eingefroren-20261005-074610; nachtrag_quelle.py und nachtrag_umkreis.py (nach Sicht).
- lauf-69/: h1.json, h2.json, zusatz.json, urteile.json, bild.json, **bild-impuls-netz.png** (links G_rad/G_N je
  Quellachse und Bahnlage ohne und mit Impulskopplung; Mitte G_rad/G_N gegen kl; rechts Mitfuehrung gegen Einstein), Logs,
  kette.txt, PRUEFSUMMEN.txt.
- rauch-69/: r1.json, r2.json (nur Schluessel und Zeiten), Logs r1 bis r6, PRUEFSUMMEN.txt.
- nachtrag-69/: quelle.json, nq.log, umkreis.json, nu.log, kette.txt, PRUEFSUMMEN.txt, PRUEFSUMMEN-CODE.txt.
- Auf der .69: /home/fmh/fmhc-physics-remote/impuls-netz-1/ (code/, code-r1/, code-r2/, rauch/, lauf/, nachtrag/).

## 10. Gegenlesen

- Ein frischer Leser (pruefer-opus, nur lesend, keine Dateien geschrieben) las 08:03:57 bis 08:16:59 CEST (seine
  date-Angaben), die Fassung bis 08:04:39. Er pruefte die Zahlen vorwaerts gegen die JSON-Dateien und die Urteile
  rueckwaerts aus PLAN 5.
- **Bestaetigt:** Urteile IN0 bis IN3 richtig nach Plan und Wortlaut; urteil() setzt die Planregeln richtig um;
  Pruefsummen, Zeiten (13 Logs, UTC/CEST), Code-Hashes; Tabellen 5.1, 5.2 (Faktoren 15, 12, 260; Baender 0,064 und
  0,004), 5.3, 5.4, 5.5 weitgehend; Herleitung (Vorzeichen J', f_eff, e_j, Zusatzterm der Eichprobe, Schur-Komplement,
  KGM, Faktor c_0^2) und deren Umsetzung in inz.py.
- **Kein A-Befund.** Eingearbeitet zwischen 08:16:59 und 08:23:49 CEST (date): B1 Eichprobe mit J nur Rundung (2, 3, 5.3,
  5.5, Selbstanzeige 5); B2 R_rot = R_mov = R_iso vorab ableitbar (3, 5.4); B3 KQ-Grenzen 2,7e-8 / 3,7e-6, ohne Soll im
  Plan; B4 Doppelpulsar-Satz (Band 0,60 bis 0,67); B5 "Einfach gesagt" (bis gut ein Promille, Vermutung); B6 nn "ein
  Siebtel bis ein Viertel"; B7 Einordnung von IN2 (3); C1 KD-Werte; C2 C_L-Maximum und Abfall; C3 Koeffizienten
  0,004077 und 0,6331; C4 [111] nicht monoton; C5 Laengsbereich und "deutet an"; C6 Aufloesungsgrenze von R; C7
  TT-Spanne 6,3 % [P] gegen 6,0 % (H1); C8 Spuren (1); C9 Kennzeichen [E] und J_iso in 2; C10 Selbstanzeige 10.
- **Nicht gegengelesen:** das Innere von pn.py und ew.py, nachtrag_quelle.py, nachtrag_umkreis.py und Abschnitt 5.6
  (danach entstanden), das Bild, die Literaturzahlen, diese letzte Textschicht.

Abschluss des Textes 2026-10-05 08:24:40 CEST (date, nach dem letzten Einarbeiten). Zeitbox 150 min ab 07:14:26 CEST, also bis 09:44:26 CEST:
eingehalten. Kein Lauf mehr aktiv (letzter Lauf NU endete 06:20:35 UTC). Journal, Peerbus und Commit uebernimmt die Leitung.

## Vermerk der Leitung (05.10.2026, 11:11:57 CEST, date; nach V1-AUFHEBUNG-1)

- Die Angabe "rund 12-mal (bzw. 11-mal) ueber dem Doppelpulsar" galt fuer Kreisbahnen ohne den Energiekanal V1, also fuer eine unvollstaendige Quelle (nur Spannung und Impuls).
- Mit vollstaendiger Quelle (V1 + Spannung + Impuls J), unabhaengig nachgerechnet (V1-AUFHEBUNG-1, VA0):
  - auf V mit J_iso: groesste Abweichung abs(G - 1) = 1,5e-5, rund 9-mal unter 1,3e-4; Lagen-Spanne 1,8e-5
  - am exakt TT-isotropen Punkt aus SKALAR-MISCH-1: Spanne 1,5e-7 bei kl = 0,01, Rest ~(kl)^2, fuer kl -> 0 mit null vertraeglich (VA1)
- Gilt nur fuer synthetische Kreisbahnen auf V im Grenzfall k -> 0. Die Gewichte bleiben eine Abstimmung. "Finns Netz besteht den Doppelpulsar" bleibt unbelegt (Negativliste).
- Quelle: RUNDE-37/v1-aufhebung-1/ERGEBNIS.md, Abschnitte 2 und 5.1. Der Text oben bleibt unveraendert; Sicherung *.bak-vermerk-v1a.
- Zusatz fuer diese Karte: Das Band "Summe m_i^4 = 0,60 bis 0,67" gilt nur ohne V1.
