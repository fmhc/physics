# SPLITTER-FREI-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 48)

- Start 2026-10-05 11:20:55 CEST (date). Plantext ab 11:40:28 CEST (date), nach den Rauchtests r1 bis r8 (nur Geometrie,
  Bau, Laufzeiten) und vor jeder Hauptrechnung. Zeitbox 150 min, also bis 13:50:55 CEST.
- Bindend: KARTE.md (SF0 bis SF4, Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Kennzeichen: [M] vorab ableitbar, [E] gerechnet (erst im Ergebnis), [P] Projektdatei, [L] Literatur aus dem
  Gedaechtnis, [F] Festlegung dieses Plans, [H] Hypothese oder Lesart. Alles synthetische Gitterrechnung, keine Messdaten.
- **Code (code/):**
  - Unveraendert kopiert aus lund-regge-masse-1/code (dort identisch mit hodge-masse-1/code und tt-glas-2/code, sha256
    geprueft): tp.py 419d7da6, ew.py fa7b6417, tg.py ec48a258, tti.py 6d6b6f7b, hm.py 0ed5e2ce, lrm.py a6cdd898,
    dn.py 0cd5d13e, nachtrag_kinetik.py fd0d17b9, pn.py c8034e40, inz.py e65a5cbf, nachtrag_iso.py 1c92cb23,
    smi.py 9459838b, mn.py b36984d3.
  - Neu: sf.py (Glasbau, Formmass, Kristallprobe, Laeufe), sf_aw.py (mechanische Auswertung), kette-cpu5.sh,
    kette-cpu6.sh, kette-ende.sh.
  - Gerechnet wird mit hm.punkt (HODGE-MASSE-1) und lrm.punkt (LUND-REGGE-MASSE-1) unveraendert; sf.py baut nur die
    Netze und ruft diese Funktionen auf.

## 0. Rauchbefunde vor dem Plantext (keine Urteilsgroesse angesehen)

- Gelesen wurden nur Geometrie, Bauverlauf, Kristallprobe und Laufzeiten; keine Zahl wachsender Moden, keine
  Lokalisierung, keine Spanne. r6 (Laufzeiten) gab nur Zeiten und Schluessel aus.
- r1 (cpu5, rauch-form):
  - triang (Zerlegung gegebener Punkte) = tg.zufallsnetz in allen vier Saaten (G, O gleich).
  - Formmass der Originalglaeser: q_min 0,0043 bis 0,019; 5-%-Quantil 0,069 bis 0,115; Median 0,36 bis 0,41;
    n(q < 0,1) = 33 bis 70, n(q < 0,2) = 135 bis 196 von T = 850 bis 873.
  - Kristallprobe Originalglas: Q6 (r < 1,35) 0,028 bis 0,046, max S(q) 4,7 bis 10,1, also amorph.
  - Positivkontrolle bcc 4^3 (N = 128): Q6 = 0,511 (Literaturwert fuer 14 Nachbarn [L]), max S(q) = 128, als
    kristallin erkannt; gestoert (0,05): 0,477 und 115,7, ebenfalls kristallin. Q6 einer einzelnen Bindung = 1.
- r2 (cpu6): Bau mit vollem Saum langsam (80 ms je Versuch; Saat 1 nach 90 s noch 42 Tetraeder unter 0,2).
- r3/r4 (Saum 1,5 im Bau): Saat 3 erreicht q_s = 0,2 in 40 s; Saat 1 nimmt keinen Zug an (Umkugel ueber den Saum).
  Daher: Bausaum 2,0 und Rueckfall auf den vollen Saum, wenn eine Umkugel den Bausaum verlaesst (exakt).
- r5, r7, r8 (Bausaum 2,0): Saaten 1, 2, 4 erreichen q_s = 0,2 in 46 / 104 / 72 s; zusammen mit r3 alle vier.
  Mittlere Verschiebung 0,062 bis 0,091 (mittlerer naechster Abstand 0,55 bis 0,59), groesste 0,25 bis 0,39; 100 bis
  110 von 128 Punkten bewegt. Danach Q6 0,029 bis 0,044, max S(q) 6,8 bis 7,8: nicht kristallin. Zerlegung gueltig
  (Volumensumme 3e-16, Diedersumme 2 pi auf 3e-15, keine Selbstkanten).
- r6 (cpu6, Laufzeiten Originalglas s1): hm.punkt 25 s mit TT-Eigenvektoren, sonst 10,5 s; Lokalisierung 7 bis 8,5 s
  je Punkt; lrm.punkt 5,9 s je Punkt.
- r9 bis r14 (09:40 bis 09:42 UTC): Absturzprobe der Kette auf Probedaten (rauch/test: bau mit 5 s, hm und lr je mit
  einer Richtung, aw). Gelesen nur Rueckgabewerte (alle 0) und Schluessel, keine Werte.
- Zwischen r1 und r14 geaendert: Bausaum und Rueckfall (nach r4), Teillaeufe --ridx und --rauch (vor r9).

## 1. Formmass und "die 5 % schlechtesten" [F]

- Je Tetraeder q = 27 V / (8 sqrt(3) R^3), V Volumen, R Umkugelradius. Das ist V/R^3, normiert auf das regulaere
  Tetraeder (q = 1). q geht gegen 0 fuer jede Entartung (Splitter, Nadel, Keil, Kappe).
- "5 % schlechteste" eines Netzes: die ceil(0,05 T) Tetraeder mit kleinstem q (stabile Sortierung). E_q5 = alle Kanten
  dieser Tetraeder. Beschreibend daneben: 1 %, 10 % (q) und 5 % kleinstes Volumen (v5).
- Zufallserwartung fuer SF1: Kantenanteil |E_q5| / E (eine gleich verteilte Mode haette etwa diesen Anteil).

## 2. Splitterarmes Glas [F]

- **Bauweise:** Ausgangspunkte sind die Punkte des Originalglases derselben Saat (Zufallsquelle wie tg.zufallsnetz).
  Wiederholt:
  1. Ein Tetraeder unter der Schranke waehlen (Gewicht q_s - q), eine seiner vier Ecken zufaellig.
  2. Die Ecke um einen zufaelligen Vektor in einer Kugel vom Radius r verschieben (periodisch).
  3. Delaunay neu zerlegen; den Zug nur annehmen, wenn das Formdefizit F = Summe max(0, q_s - q) sinkt.
  - r: Start 0,05; nach je 25 Fehlversuchen x 1,5 (hoechstens 0,4); nach einem Erfolg / 1,2 (nicht unter 0,05).
  - Zufallsquelle der Stoerung [9137, 128, s].
  - Schluss, wenn F = 0, geprueft mit dem vollen Saum von tg (4,0); Bauzeit hoechstens 270 s je Saat.
- **Formschranke q_s = 0,2** fuer alle Tetraeder. Sie liegt ueber dem 5-%-Quantil jedes Originalglases (0,069 bis 0,115)
  und entfernt alle 13 bis 23 % Tetraeder mit q < 0,2.
- **Begruendung:**
  - Die Stoerung derselben Punkte aendert das Glas nur an den schlechten Zellen; der Vergleich bleibt je Saat gepaart.
    Das ist die Splitter-Beseitigung durch Stoerung aus der Netzerzeugung (Li/Teng, Edelsbrunner u. a. [L]).
  - Ein Mindestabstand allein beseitigt Splitter nicht, weil Splitter auch in gut verteilten Punktmengen auftreten [L].
  - Delaunay bleibt die Zerlegungsregel; Punktzahl 128 und Dichte 1 bleiben gleich.
- **Gueltig** ist ein splitterarmes Glas, wenn:
  - die Schranke mit vollem Saum erreicht ist und keine Umkugel den Saum verlaesst,
  - die Zerlegung stimmt (Volumensumme < 1e-12 relativ, Diedersumme je Kante 2 pi auf 1e-9, keine Selbstkanten),
  - es nicht kristallin ist (unten).
  - Ein ungueltiges Glas geht in SF2 bis SF4 nicht ein (vermerkt).
- **Kristallprobe:**
  - Strukturfaktor S(q) = |Summe_j exp(i q r_j)|^2 / N an allen q = 2 pi n / L mit 0 < |n| <= 7 (Halbraum).
  - Steinhardt-Q6 global ueber alle Paare mit Abstand < 1,35.
  - **Kristallin, wenn max S(q) >= 32 (= N/4) oder Q6 >= 0,25.** bcc 4^3 wird so erkannt, das Originalglas nicht (r1).
  - Beschreibend: Q4, Q6 ueber Delaunay-Kanten, g(r), kleinster Paarabstand, Verschiebungen.

## 3. k-Saetze, Reduktionen, Zaehlregeln (woertlich aus den Vorlagen)

- **HM-Satz** (HODGE-MASSE-1, Abschnitt 3, Glas): 13 Richtungen tg.richtungen13w bei |k| = 1e-2, dazu [100], [110],
  [111] bei |k| = 2e-2, also 16 Punkte je Glas.
  - hm.punkt unveraendert, mit_tt wie dort (nur an [100], [110], [111] bei 1e-2). mit_kontr und mit_vert aus: Sie
    haengen nur Gegenproben nach der Zaehlung an.
  - Paarungen: A1R1, A1RH, A2R1, A2RH, A2LR1, A2LRH, A2LR2, A2LRHL (Zielmenge der Karte: A1RH, A2RH, A2LR1, A2LRH).
  - Je Glas zwei Teillaeufe (Richtungen 0 bis 6 und 7 bis 12), zusammengefuehrt in sf_aw.py wie hm_aw.py.
- **Zaehlregel HM (woertlich, hm.z_auswerten):** n_neg = Zahl der Eigenwerte < 0 von Z = L^-1 K_red L^-+
  (K_red = A_red^-1, B_red = L L^+). Je Punkt "wachsende Moden"; der Saatwert in HODGE-MASSE-1 Tab. 4.2 ist das
  Maximum ueber die Punkte.
- **LR-Satz** (LUND-REGGE-MASSE-1, Abschnitt 4): 13 Richtungen tg.richtungen13w, k = (kl / l) d, l = mittlere
  Kantenlaenge des jeweiligen Glases, **kl = 0,005 und 0,2** (Teilmenge wegen der Zeitbox).
  - kl = 0,005 ist der kleinste Wert (die Karte nennt ihn), 0,2 der groesste. Bei 0,2 schwanken die Zahlen in
    LUND-REGGE-MASSE-1 je Richtung (27/28, 30/31, 31 bis 33); das ist die schaerfere Reproduktionsprobe.
  - lrm.punkt unveraendert mit mit_a1 = True, voll = False (wie dessen Stabilitaetslaeufe; die Zaehlung kommt vor allen
    Schaltern).
- **Zaehlregel LR (woertlich, lrm.punkt):** omega^2 = Eigenwerte von L^+ A_red L. Wachsend, wenn
  Re omega^2 < -1e-9 s oder |Im omega^2| > 1e-9 s (s = max |omega^2|). Legendre nur bei regulaerem K
  (|Eigenwert| > 1e-12 max); sonst "Legendre singulaer" und keine Zahl.
- Reduktionen R1 und RH wie HODGE-MASSE-1 (hm.punkt); die Lund-Regge-Masse mit R1 ist dort A2LR1.

## 4. Lokalisierungsmass (SF1) [F]

- An jedem HM-Punkt fuer A1RH und A2RH (beschreibend auch A2LR1, A2LRH): Z wie in hm.punkt (dieselben Operationen),
  Eigenzerlegung mit Vektoren (eigh).
- Wachsende Moden: Eigenwerte < 0. Lage-Eigenrichtung x = L^-+ u (loest K_red x = lambda B_red x).
- Kantenvektor a = S x (Variable a_e = dl_e / l_e wie im Code; senkrecht auf Eichung und skalarer Regel).
- **Lokalisierung f = Summe_{e in E_q5} |a_e|^2 / Summe_e |a_e|^2** (Normquadrat-Anteil).
- Beschreibend: dasselbe fuer E_q1, E_q10, E_v5; Beteiligungszahl PR = (Summe |a|^2)^2 / (E Summe |a|^4).
- Kontrolle: Zahl der Eigenwerte < 0 aus eigh gleich n_neg aus hm.punkt am selben Punkt.

## 5. Kontrollen

- triang der Originalpunkte = tg.zufallsnetz (G, O, Lagen bitgleich), im Bau je Saat.
- Originalglas: A1R1-Spannen und alle TT-Werte w2k2 gegen die Laufdateien von HODGE-MASSE-1 (relativ; erwartet 0).
- Kristallprobe an bcc (positiv) und am Originalglas.
- A1R1 an den LR-Punkten: 0 wachsend (wie LUND-REGGE-MASSE-1).
- Splitterarmes Glas: Gueltigkeit (Abschnitt 2), Q6 und S(q) gegen das Originalglas.

## 6. Bausteine und Erwartungen (vorab, kein Urteil)

- [M] Die Zahl wachsender Moden je Saat war in HODGE-MASSE-1 fast k-unabhaengig (A1RH 10/9/10/9 an allen 16 Punkten).
  Das passt zu oertlichen Moden, beweist aber keinen Splitter-Sitz.
- [M] Splitter haben fast singulaere Phi_t (eine Verzerrung aendert keine Kantenlaenge). A2 (Faktor V_ref/V_t) und A2L
  (Phi^-1) werden dort extrem, A1 bekommt eine fast verschwindende Richtung. Ob daraus negative Richtungen der
  RH-Reduktion werden, ist nicht ableitbar.
- [P] RH-Instabilitaet gibt es auch auf Kristallen (A2LRH auf V, S, A15 je 1 wachsende Mode, HODGE-MASSE-1 4.2), A1RH und
  A2RH dort nicht. Lund-Regge mit R1 waechst auch auf Kristallen kurzwellig (LUND-REGGE-MASSE-1 4.4); auf dem Glas
  liegen die wachsenden Richtungen knapp am Nullkegel der lambda = 1-Form.
- Erwartung des Agenten [H, kein Urteil]: SF2 eher verfehlt (die RH-Instabilitaet ist eine Eigenschaft der
  Dirac-Folgeregel mit indefiniter DeWitt-Form, nicht allein der Form der Zellen), SF3 eher eingetroffen.

## 7. Urteilsregeln (mechanisch in sf_aw.py)

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| SF0 | Originalglas s1 bis s4: n_neg(A1RH) und n_neg(A2RH) an allen 16 HM-Punkten gleich den Laufdateien von HODGE-MASSE-1 (Punkt fuer Punkt), und n_wachsend (LR) an allen 26 LR-Punkten gleich den Laufdateien von LUND-REGGE-MASSE-1 (Punkt fuer Punkt) -> eingetroffen; eine Abweichung -> verfehlt; Lauf fehlt (ohne Abweichung) -> nicht entscheidbar | je Saat die berichteten Zahlen: max n_neg A1RH / A2RH = 10/6, 9/5, 10/7, 9/6 (HODGE-MASSE-1 Tab. 4.2) und Bereich n_wachsend LR = 27-28, 30-31, 31-33, 28-28 (LUND-REGGE-MASSE-1 4.1) |
| SF1 | Originalglas s1 bis s4, alle 16 HM-Punkte, jede wachsende Mode von A1RH und A2RH: f >= 0,5 (Normquadrat-Anteil auf E_q5) -> eingetroffen; eine Mode darunter -> verfehlt; keine wachsende Mode oder Lauf fehlt -> nicht entscheidbar | wie Plan, aber "50 % der Eigenvektornorm" als Norm gelesen: ||a auf E_q5|| >= 0,5 ||a||, also f >= 0,25 |
| SF2 | gueltige splitterarme Glaeser s1 bis s4, alle 16 HM-Punkte: n_neg(A1RH) = 0 und n_neg(A2RH) = 0 -> eingetroffen; ein Punkt mit n_neg > 0 -> verfehlt; Glas ungueltig, Lauf unvollstaendig oder B_red nicht positiv definit (ohne Gegenbefund) -> nicht entscheidbar | wie Plan |
| SF3 | gueltige splitterarme Glaeser, alle 26 LR-Punkte: Legendre regulaer und n_wachsend >= 10 -> eingetroffen; ein Punkt mit n_wachsend < 10 -> verfehlt; Legendre singulaer oder Glas fehlt (ohne Gegenbefund) -> nicht entscheidbar | wie Plan, zusaetzlich an allen 16 HM-Punkten n_neg(A2LR1) >= 10 ("an jedem gerechneten k") |
| SF4 | Mittel ueber s1 bis s4 der Spanne(A1R1, splitterarm) <= 0,5 x Mittel der Spanne(A1R1, Original), beide hier gerechnet (26 Werte bei |k| = 1e-2), alle 16 Punkte beider Glaeser ok -> eingetroffen; sonst verfehlt; nicht alle ok oder Glas ungueltig -> nicht entscheidbar | je Saat: Spanne(splitterarm) <= 0,5 x Spanne(Original derselben Saat), alle vier Saaten |

- "ok" wie HODGE-MASSE-1: zwei positive masselose Werte, Luecke < 1e-2.
- Beschreibend (kein Urteil): A2R1, A2LRH, A2LR2, A2LRHL, Lokalisierung von A2LR1 und A2LRH, Lokalisierung auf dem
  splitterarmen Glas, Formstatistik, Kristallprobe, Verschiebungen.

## 8. Laufliste (.69, kleintest.sh, Spuren cpu5 und cpu6, je Lauf <= 600 s)

- Arbeitsordner /home/fmh/fmhc-physics-remote/splitter-frei-1 (code/, lauf/, rauch/). Ketten code/kette-cpu5.sh und
  code/kette-cpu6.sh, einmal per ssh gestartet; danach code/kette-ende.sh (Auswertung). Logs mit absolutem Pfad.

| Lauf | Spur | Aufruf (code/sf.py ...) | Schaetzung |
|---|---|---|---|
| bau-s13 / bau-s24 | cpu5 / cpu6 | bau --saaten 1,3 bzw. 2,4 --qs 0.2 --zeit 270 --r0 0.05 --rmax 0.4 | 1,5 bis 4 min |
| hm-<art>-s<i>-a / -b | Saaten 1, 3: cpu5; 2, 4: cpu6 | hm --art orig/sf --saat i [--bau lauf/bau-...json] --ridx 0-6 bzw. 7-12 | 3 bis 4 min |
| lr-<art>-s<i> | wie oben | lr --art orig/sf --saat i [--bau ...] | 2,5 bis 3 min |
| aw | cpu5 | aw --lauf lauf --out lauf/auswertung.json | < 1 min |

- Reihenfolge je Saat: hm-orig a/b, hm-sf a/b, lr-orig, lr-sf.
- Schlusszeit: nach 13:20 CEST (11:20 UTC) startet kein neuer Lauf. Fehlende Laeufe werden vermerkt; gewertet wird, was
  vorliegt (Regeln oben).

## 9. Festlegungen und Grenzen [F]

- Ein Bau je Saat (eine Stoerungsfolge); keine zweite Schranke. Andere Bauweisen (Mindestabstand, Relaxation) sind
  nicht gerechnet.
- LR-Satz nur kl = 0,005 und 0,2; der HM-Satz liefert A2LR1 zusaetzlich bei |k| = 1e-2 und 2e-2 (HM-Zaehlregel).
- Lokalisierung im euklidischen Mass der Variablen a = dl/l; andere Gewichtungen (B- oder K-Energie) nicht gerechnet.
- Synthetisch, keine Messdatenbestaetigung.
