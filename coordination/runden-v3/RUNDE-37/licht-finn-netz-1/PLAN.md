# LICHT-FINN-NETZ-1: Plan (Runde 43, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Arbeitsplatz RUNDE-37/licht-finn-netz-1/, Rechenort .69
  (/home/fmh/fmhc-physics-remote/licht-finn-netz-1/), Spuren cpu4 und cpu11.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 19:48:25 CEST. Letzte eigene Messung vor der Unterbrechung: 19:51:58 CEST (date -u auf der .69,
    17:51:58 UTC). Abbruch durch das Sitzungslimit (laut Leitung gegen 19:53 CEST).
  - Wiederaufnahme laut Leitung 21:44:09 CEST, eigene Messung 21:44:52 CEST. Zeitbox bis 23:09 CEST.
  - Code ab 21:53:14 CEST, dieser Plan ab 21:57:21 CEST. Vor jeder Rechnung: Es gab keinen Rauchlauf und keine
    Ergebniswerte; vor dem Einfrieren laeuft hoechstens eine reine Syntaxpruefung (python -m py_compile ueber
    kleintest.sh, gibt keine Werte aus).
- **Kennzeichen:** [M] eigene Mathematik (ungeprueft), [E] gerechnet, [P] Projektdatei, [S] Quelle, [H] Hypothese,
  [F] Festlegung dieses Plans.
- Alles ist synthetische Rechnung an gedachten Netzen. Keine Messdaten, keine Messdatenbestaetigung.

## 0. Gelesen (vor dem Plan)

- KARTE.md (bindend). WEYL-LINEAR-1 (ERGEBNIS, PLAN: Fitansatz, Umrechnung l = hbar c / (E_QG,2 sqrt(2 kappa))).
  STRICH-NETZ-1 ERGEBNIS (Abschnitte 1 und 2). STRANG-ANKER-L DOSSIER Z. 85 bis 96 (LHAASO-Anker).
  spinnetz.py Kopf und matrix() (Weyl-Operator). QCA-DIAMANT-4 ERGEBNIS und Teile von qca_diamant.py (Problem, W_at,
  isotropie, cplx); Vertreter-Automaten in lauf-69/haupt_A1f.json und haupt_A2w.json (Feld repr: A, freqs).
- Projekt-grep nach QCA-DIAMANT (mit Ausschluss der versiegelten Pfade): einziger Diamant-Automat ist QCA-DIAMANT-4
  (dazu QCA-DIRAC-T-1, SPIEGEL-HAELFTE-1 nicht gelesen).
- Rohdatenprobe [P]: a2/a4 je Richtung fuer Diamant, Pyrochlor oder die QCA-DIAMANT-4-Automaten stehen nirgends.
  QCA-DIAMANT-4 nennt fuer L2:P+P (Fassung 1 frei) eine Richtungsstreuung des Kegeltempos von 7 bis 52 % und fuer den
  Grover-Lauf (Fassung 2 w0) v = 2/sqrt3 mit Streuung ~1e-11 [P].

## 1. Netz und Einheit [F]

- Finns Netz: regelmaessige Tetraeder, die sich an den Ecken beruehren (Pyrochlor). Knoten des Diamant-Graphen =
  Tetraedermitten, Knoten des Pyrochlor-Graphen = Tetraederecken (= Mitten der Diamant-Kanten).
- **Laengeneinheit l = 1 PU = Tetraederkante** (Pyrochlor-Abstand). Daraus kubische Gitterkonstante 2 sqrt2 PU und
  Diamant-Kante b = sqrt(6)/2 = 1,2247 PU. Alle a2, a4 gelten fuer k in 1/PU. In Einheiten der Diamant-Kante waere
  a2 durch b^2 = 1,5 zu teilen (beschreibend mitgenannt).
- Rechnung exakt per Bloch-Matrix je Wellenvektor (unendliches periodisches Netz), keine endliche Box.

## 2. Operatoren und Schreibtisch [M, ungeprueft]

| Name | Operator | Schreibtisch vorab |
|---|---|---|
| S-D | Skalar, Diamant-Graph, gleiche Gewichte und Massen. Patch-Test: Kantenvektoren je Knoten summieren zu 0, lineare Funktionen sind diskret harmonisch, also kein Zickzack-Korrektor. Akustischer Zweig. | a2(n) = -(3 - 2 S4)/48 mit S4 = sum n_i^4: [100] -0,02083, [110] -0,04167, [111] -0,04861; Mittel ueber die 26 Richtungen -0,03900, Kugelmittel -0,0375; Spannweite 0,02778 = 71 % des Mittels. **LF1 und LF2 sind fuer S-D damit vorab ableitbar.** |
| S-P | Skalar, Pyrochlor-Graph (Tetraederkanten, 6 Nachbarn in +-Paaren), gleiche Gewichte. Akustischer Zweig. | nicht abgeleitet |
| W-D | Weyl-Operator nach spinnetz.py (H0_ij = (i/2) A (sigma.n_ij) e^{ik.d_ij}), Diamant-Graph, gleiche Gewichte (bei gleichen Gewichten patch-test-konsistent). 4x4-Bloch-Matrix, zwei positive Zweige lo, hi. | Fuehrend isotroper masseloser Dirac (zwei Kegel, H(0) = 0). Der Term zweiter Ordnung ist proportional zu i sigma.q mit q = (k_y k_z, k_z k_x, k_x k_y); er spaltet die beiden Zweige **linear** auf: a1 = +-(b/sqrt3) abs(q^ x n) mit q^ = q(n). Also a1 = 0 laengs 100 und 111, +-0,354 laengs 110. |
| Q-W | Weyl-Quantenautomat QCA-DIAMANT-4, Vertreter "d1\|L2:P+P" (Fassung 1 frei), nur kopiert (Zweischritt W(u) = sum_f A_f e^{iu.f}, u = k b n/sqrt3). Zweige: je Kegelcluster von W(0) die m naechsten Eigenphasen, Betrag. | Symmetrie nur L_2 (drei 180-Grad-Drehungen), **nicht kubisch**: Kegeltempo richtungsabhaengig [P]. Die Kartenpraemisse fuer LF0 ([M] kubische Symmetrie) gilt hier nicht. LF0 nach Kartenwortlaut scheitert, wenn Q-W gerechnet wird; das ist vorab bekannt [P]. |
| Q-G | Grover-Lauf QCA-DIAMANT-4, Vertreter "cayley\|T:1+3" (Fassung 2 w0), nur kopiert. Bosonischer Kegel mit zwei flachen Zweigen; flache Zweige (c < 1e-3) zaehlen nicht. | Kegel isotrop in erster Ordnung [P]; a2 nicht abgeleitet. |
| M-D | Maxwell in der Coulomb-Phase (Spin-Eis): A auf den Diamant-Kanten (= Pyrochlor-Ecken), Fluss auf den Sechsringen (4 je Zelle, durch Aufzaehlung), K = C^dag C; 2 Eichnullen, 2 Photonzweige lo, hi. Gleiche Gewichte (alle Kanten und alle Ringe gleichwertig). | Eichinvarianz und kubische Symmetrie erzwingen langwellig K ~ alpha (k^2 - k k^T): Tempo isotrop, beide Polarisationen entartet. a2 nicht abgeleitet. |

- Maxwell auf den Pyrochlor-Kanten mit Dreiecken als Flaechen ist nicht gerechnet: Ohne die Sechsecke (die Hohlraeume
  sind Kegelstumpf-Tetraeder) bleiben flache Nullmoden [M]; mit ihnen braucht es Hodge-Gewichte, die die Karte nicht
  festlegt. Die Coulomb-Phase ist die Lesart "Maxwell auf Kanten" der Karte.
- **Kontrollen und Dimensionsvergleich (AGENTS.md):** Z3-S Skalar (a2 = -S4/24, a4 = S6/720 - S4^2/1152), Z3-W Weyl
  (spinnetz-Kubik H = -sum sigma_a sin k_a: a2 = -S4/6, a4 = S6/45 - S4^2/72), Z3-M Maxwell (Yee: wie Z3-S, beide
  Polarisationen gleich), K1-S Kette 1D (-1/24), Q2-S Quadrat 2D (-S4/24), WB-S Wabe 2D (isotrop -1/32: in 2D macht
  die Sechszaehligkeit den Tensor 4. Stufe isotrop, in 3D kann kubische Symmetrie das nicht).
- Weitere Code-Kontrollen: rot grad = 0 (M-D, 50 zufaellige k), Eichnullen, Photon-Eigenwert > 0, Hermitezitaet
  (W-D), Unitaritaet (QCA), Tetraederkante = 1, 6 Pyrochlor-Nachbarn, Kopfprobe kappa 0,117 -> 5,91e-28 m.

## 3. Dispersion und Fit [F]

- Richtungen: die 26 Richtungen (+-1, 0)^3 normiert (6 x 100, 12 x 110, 8 x 111). 2D: 24 Richtungen in der Ebene,
  1D: +-x. Beschreibend: Kugelmittel von a2 ueber 200 Fibonacci-Richtungen (Hauptfenster).
- Je Richtung und Zweig: omega(k)/k an k-Gitter, Polynomfit **mit allen Potenzen** omega/k = c (1 + a1 k + a2 k^2 +
  a3 k^3 + a4 k^4 + ...), dazu das **Kartenmodell nur mit geraden Potenzen** (beschreibend; bei Operatoren mit a1 != 0
  verzerrt).
- **Hauptfenster W0:** k in [0,01; 0,30] 1/PU, 60 Punkte, Grad 8. Proben (nur beschreibend): Wk [0,005; 0,15],
  60 Punkte, Grad 6; Wg [0,01; 0,60], 80 Punkte, Grad 10.
- Je Operator und Zweig: Richtungsmittel (arithmetisch ueber die 26 Richtungen), min, max, Spannweite = max - min,
  Spannweite relativ = Spannweite/abs(Mittel); fuer c, a1, a2, a3, a4. QCA: c ist das Kegeltempo je Richtung, a2 bezieht
  sich auf das eigene c(n).

## 4. Bedingte Maschen-Schranke [F]

- "Wenn das Netz das Licht traegt": Gruppentempo c (1 + 3 a2 (k l)^2) gegen LHAASO c [1 - (3/2)(E/E_QG,2)^2] mit
  E = hbar c k gibt **l = hbar c / (E_QG,2 sqrt(2 abs(a2)))** fuer a2 < 0 (subluminal), E_QG,2 = 6,9e11 GeV, hbar c =
  1,973269804e-16 GeV m. Einheiten: GeV m / GeV = m. Die Formel ist die von WEYL-LINEAR-1/Dossier; die Kopfprobe
  kappa = 0,117 -> 5,91e-28 m rechnet der Code nach.
- Die Ausrichtung des Netzes zum Gammablitz ist unbekannt. Deshalb drei Zahlen: konservativ (kleinstes abs(a2) der 26
  Richtungen, groesstes erlaubtes l), Mittel, streng (groesstes abs(a2)). Haupt-Aussage: konservativ, fuer M-D.
- a2 > 0 (superluminal): LHAASO-Wert fuer n = 2 superluminal steht nicht im Dossier; keine Zahl.
- Lineare Glieder (a1 != 0, erwartet bei W-D): l = hbar c / (2 abs(a1) E_QG,1) mit 1,0e20 GeV (a1 < 0) bzw.
  1,1e20 GeV (a1 > 0), wie WEYL-LINEAR-1. Haengt a1 vom Zweig (Haendigkeit) ab, ist das eine Doppelbrechung; der
  Doppelbrechungsanker des Dossiers (> 1,8e34 GeV [P]) wird nur genannt, nicht umgerechnet.
- l ist die Tetraederkante; die Diamant-Kante ist 1,2247 l.

## 5. Urteilsregeln (mechanisch in code/licht_netz.py, Funktion urteile)

- **LF0 nach Plan:** (i) Spannweite relativ des Tempos c ueber die 26 Richtungen < 1e-6 fuer jeden Zweig der Operatoren
  mit kubischer bzw. tetraedrischer Symmetrie (S-D, S-P, W-D, Q-G, M-D, Z3-S, Z3-W, Z3-M), und (ii) Z3-S laengs der
  6 Achsen abs(a2 + 1/24) < 1e-6. Beides: eingetroffen, sonst nicht eingetroffen. Q-W ist ausgenommen, weil die
  Kartenpraemisse ([M] kubische Symmetrie) fuer ihn nicht gilt (Abschnitt 2).
- **LF0 nach Kartenwortlaut:** (i) fuer alle gerechneten Operatoren und Zweige (auch Q-W, auch 1D/2D), dazu (ii).
- **LF1 nach Plan:** "Licht" ist M-D (Maxwell, Licht im engeren Sinn der Karte). Eingetroffen, wenn fuer beide
  Photonzweige 0,01 <= abs(Richtungsmittel a2) <= 0,2 (Hauptfenster, k in 1/PU); keiner: nicht eingetroffen; einer:
  geteilt. M-D nicht rechenbar: nicht auswertbar.
- **LF1 nach Kartenwortlaut:** dieselbe Bedingung fuer alle Zweige aller Operatoren auf Finns Netz (S-D, S-P, W-D, Q-W,
  Q-G, M-D): alle: eingetroffen, keiner: nicht eingetroffen, sonst geteilt.
- **LF2 nach Plan:** M-D, beide Photonzweige: (max a2 - min a2)/abs(Mittel a2) > 0,10 ueber die 26 Richtungen.
  Gleiche Auswertung wie LF1 (eingetroffen / nicht eingetroffen / geteilt).
- **LF2 nach Kartenwortlaut:** dieselbe Bedingung fuer alle Zweige auf Finns Netz.
- Je Zweig stehen die Einzelurteile im Ergebnis (urteile.LF1.je_zweig, LF2.je_zweig).
- Beschreibend, ohne Urteil: Proben Wk und Wg, Kartenmodell (gerade Potenzen), Kugelmittel, Schreibtischvergleich,
  Werte in Diamant-Kanten-Einheiten.

## 6. Laeufe (nach dem Einfrieren; je <= 600 s, 1 Thread, Logs mit absolutem Pfad)

- Vorab auf der .69: Kopie von code/ nach /home/fmh/fmhc-physics-remote/licht-finn-netz-1/code/, Kopie der beiden
  QCA-DIAMANT-4-Dateien (haupt_A1f.json, haupt_A2w.json; Pruefsummen gleich den lokalen) nach .../alt/.
- L1 (cpu4): `licht_netz.py rechnen alt/haupt_A1f.json alt/haupt_A2w.json lauf/ergebnis.json`.
- L2 (cpu11): `licht_netz.py bild lauf/ergebnis.json lauf/bild-licht-finn-netz.png`.
- L3 (cpu11, beschreibend): Wiederholung von L1 in lauf/ergebnis-wdh.json (Reproduktion, sha256 gleich erwartet).
- Faellt ein Teil mit Fehler aus, wird das als Fehler im Ergebnis vermerkt; eine Codeaenderung danach waere eine
  Selbstanzeige mit neuer eingefrorener Fassung.

## 7. Agenten-Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | S-D trifft die Schreibtischformel auf 1e-6 | 85 % |
| A2 | W-D: a1 != 0 laengs 110 (abs > 0,1), = 0 laengs 100 und 111 | 65 % |
| A3 | M-D: abs(Mittel a2) in [0,01; 0,2] fuer beide Zweige | 60 % |
| A4 | M-D: Spannweite > 10 % | 70 % |
| A5 | M-D: die beiden Polarisationen unterscheiden sich in a2 in mindestens einer Richtung um > 1e-3 (Doppelbrechung bei k^2) | 50 % |
| A6 | LF0 nach Plan eingetroffen, nach Kartenwortlaut nicht (Q-W) | 70 % |

## 8. Einfrieren

- Eingefroren werden PLAN.md und code/licht_netz.py als Kopien *.eingefroren-<Zeit>; sha256 in EINGEFROREN-SHA256.txt,
  auf der .69 dieselben Pruefsummen. Danach keine Aenderung an Plan, Code oder Regeln.
