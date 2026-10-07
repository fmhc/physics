# KRAFT-1 Ergebnis: drei Analogkraefte und TET-1

- Runde 9 (v3), Karte KRAFT-1 mit Teilkarte TET-1. Bearbeiter: Code-Agent (Anthropic, Opus).
- Geschrieben ab 2026-09-30 10:02:13 CEST (date). Plan und Vorab: PLAN.md mit Nachtrag 1 (08:27:48) und Nachtrag 2
  (08:34:28).
- Explorativ, Modellaussagen; keine Messdatenbestaetigung.
- Kein Anspruch auf Elektromagnetik oder Gravitation: Alle drei Kraefte kommen aus einem skalaren Feld, ohne Eichfeld
  (Spin 1) und ohne masseloses Spin-2-Feld.
- **K2 und K3 bewertet Codex** (coordination/status-audit-20260930/codex-wm1/KRAFT-KONZEPTPRUEFUNG.txt, Bestand .69
  gesichert 06:57:30 UTC). Hier ist die Bewertung uebernommen, nicht neu gemacht.
- Neu nach der Pause (Laeufe 09:57 bis 10:01 CEST):
  - K1-3D ausgewertet
  - K1-1D gerechnet
  - TET-1 gerechnet
  - zweite K2-Gitterstufe h = 0,15
- Rohdaten und Berichte: lauf-69/ (Kopie von .69:/home/fmh/fmhc-physics-remote/runde9-kraft1/). JSON-Pfade unten gelten
  relativ zu lauf-69/.

## Uebersicht

| Arm | Formel [Hand] | Test | Ausgang | Belegstufe |
|---|---|---|---|---|
| K1 Randkraft (Yukawa) | E_int = -8 pi A^2 cos(Delta theta) e^{-k0 d}/d (3D); -4 k0 A_1^2 cos(Delta theta) e^{-k0 d} (1D) | Endgeschwindigkeit gegenphasiger Paare | 3D: 0,960 (0,76), 0,975 (still); 1D: 0,983 bis 0,996 (d0 = 10 bis 14), 0,921 (d0 = 16); zwei Gitter gleich | numerisch, zwei Gitter; Fenster siehe unten |
| K2 Bjerknes-Typ | F_B = -[sqrt(P_A P_B)/(Omega q d^2)][cos(qd - Delta + 2 delta_1) + qd sin(qd - Delta + 2 delta_1)] | Atmungsphase gleich gegen gegen, vier Abstaende | 0,76: alle Kriterien aus Nachtrag 1 bestanden, jetzt auf zwei Gittern. Still: strenges Schalterkriterium verfehlt (2 von 4 Punkten je Gitter), grobe Widerlegung nicht erreicht | Codex-Bewertung; zweite Stufe neu |
| K3 Kondensat | statisch Yukawa mit M = sqrt(4 g4 C0), nicht \|x\|/ln r/1/r | 1D, zwei Baelle in Fallen | Nullkontrollen bestanden, Kraft im Mittel anziehend, konstante Kraft widerlegt; Yukawa-Rate nicht bestaetigt | Codex-Bewertung |
| TET-1 | Z3-Neutralitaet: nur cos 3m phi; c3 ~ e^{-3 k0 d} | Ueberlagerungsenergie, 5 Abstaende, 12 Phasen, 2 Gitter | (i) bestanden; (ii) Leitung bestanden (3,13 bis 3,34 k0); eigene Zusaetze teils verfehlt | Ueberlagerung, fuehrende Ordnung, keine Dynamik |

## K1: Randkraft (Yukawa-Typ)

### Formel (PLAN Abschnitt 2)

- E_int = -8 pi A^2 cos(Delta theta) e^{-k0 d}/d in 3D; in 1D E_int = -4 k0 A_1^2 cos(Delta theta) e^{-k0 d}, mit
  A_1^2 = 4 k0^2/b0.
- Gleichphasig ziehen sich die Baelle an, gegenphasig stossen sie sich ab.
- Literatur, an der Quelle gelesen (arXiv-Abstract 0809.3895): Bowcock, Foster, Sutcliffe, J. Phys. A 42, 085403 (2009):
  "The asymptotic force between well-separated Q-balls is calculated to show that Q-balls can be attractive or
  repulsive depending upon their relative internal phase". Die Formel ist also im Kern Literatur.
- Axenides u. a., Phys. Rev. D 61, 085006 (2000): Abstract gelesen; zur Phasenabhaengigkeit sagt er nichts.

### K1-3D, integral (Nachtrag 2: massgeblich)

- Gegenphasig aus der Ruhe bei d0 = 12. Gemessen wird d'_inf als Steigung auf [225, 300]; Formel
  d'_inf = sqrt(4 E_int/M).
- JSON: aus-k2-{still,076}-{fein,grob}/auswertung_k1_3d.json, Felder .zeilen[4].v_spaet, .v_formel, .verh.

| omega^2 | d'_inf fein | grob | Formel | Verhaeltnis fein / grob |
|---|---|---|---|---|
| still | 0,105059 | 0,105078 | 0,107758 | 0,9750 / 0,9751 |
| 0,76 | 0,107123 | 0,107147 | 0,111545 | 0,9604 / 0,9606 |

- Einordnung des Fensters:
  - Nachtrag 2 hat nur fuer K1-1D ein Zahlenfenster festgelegt: [0,92; 1,07] fuer d'_inf, das entspricht E_int in
    [0,85; 1,15].
  - Fuer K1-3D steht dort nur "massgeblich" mit den Formelwerten 0,1078 und 0,1115.
  - Mit dem uebertragenen Fenster ist K1-3D **bestanden**. Das ist eine Uebertragung, kein woertlich vorab gesetztes
    3D-Kriterium.
  - In Energie ausgedrueckt: 0,951 (still) und 0,922 (0,76) der Formel.
- Beschreibend, laut Nachtrag 2 kein Test (Felder .zeilen[0..3]):
  - 120 Grad: d'_inf das 1,13-Fache (0,76) bzw. 1,18-Fache (still) des Werts bei fester Phase.
  - 90 Grad: Abstossung mit d'_inf = 0,092, obwohl der Wert bei fester Phase 0 ist.
  - 60 Grad: Die Baelle naehern sich erst bis d = 9,5 bis 9,9 (t = 58 bis 60) und laufen dann mit 0,145 bis 0,166
    auseinander.
  - 0 Grad: Sie verschmelzen (d(300) = 3,0 bis 3,9).
  - Deutung [H]: Ladung fliesst zwischen den Baellen, die Phasendifferenz bleibt nicht fest. Das cos-Gesetz gilt nur im
    Augenblick.
- Die d''(0)-Fits (auswertung_bj.json .k1_3d[*]) folgen dem cos-Muster: 0,53 / 0,02 / -0,50 / -0,95 (0,76, fein).
  - Der gleichphasige Absolutwert trifft still mit 0,959 und verfehlt bei 0,76 mit 0,807 die alte 10-%-Latte (Codex).
  - Nach Nachtrag 2 sind diese Werte nur beschreibend.

### K1-1D (PLAN Abschnitt 2 und Nachtrag 2), neu gerechnet

- Lauf: aus-k1vak/medium1d_k1vak_bericht.txt und _ergebnis.json, Feld .ergebnisse.k1vak.ergebnis.{grob,fein}[*].verh.
  Gerechnet auf .69 (Spur cpu2) mit T = 200, dx 0,1 und 0,05.
- Gegenphasig (180 Grad), d'_inf gemessen/Formel, fein (grob):
  - d0 = 10: 0,983 (0,982); gehoert nicht zum Entscheidungsbereich
  - d0 = 12: 0,996 (0,995)
  - d0 = 14: 0,991 (0,991)
  - d0 = 16: 0,921 (0,921); dort ist d(200) = 20,3, und etwa 10 % der Energie stecken noch in E_int
- **Entscheidung nach Nachtrag 2:** Alle drei Werte bei d0 = 12 bis 16 liegen im Formelfenster [0,92; 1,07], 16 knapp.
  Das R3-Fenster [0,67; 0,77] ist ausgeschlossen.
  - Die 1D-Formel gilt. Die R3-t2-Werte (0,52 x Formel) haben eine systematische Abweichung.
  - Die Ursache ist nicht geprueft; vermutlich der Punktzwang der R3-Relaxation [H].
- Nicht blind: Der Rauchtest (Nachtrag 2) zeigte das Ergebnis schon.
- Beschreibend:
  - 120 Grad: 1,10 bis 1,25 x Formel bei fester Phase.
  - 90 Grad: Abstossung (d'_inf 0,02 bis 0,13).
  - Ladungsverhaeltnis rechts/links am Ende bis 1,44.
  - Einzelball: Drift 0.
- Literatur zum Ladungsaustausch zwischen Q-Baellen verschiedener Phase: [L?], nicht gelesen.

## K2: Bjerknes-Typ ueber die Abstrahlung, Kraftschalter

### Formel (PLAN Abschnitt 3)

- F_B(d) = -[sqrt(P_A P_B)/(Omega q d^2)] [cos(qd - Delta + 2 delta_1) + qd sin(qd - Delta + 2 delta_1)].
  - P: Einzelball-Leistung; delta_1: l = 1-Streuphase des Partners, gerechnet +0,2568 (0,76)
  - Fernfeld: ~ sin(...)/d
  - Grenzfall qd << 1: -sqrt(P_A P_B)/(Omega q d^2), die klassische Form
- Literatur, an der Quelle gelesen (archive.org, V. Bjerknes, "Fields of force", 1906, Vorlesung 2, Abschnitte 3 und 4):
  - "Between bodies pulsating in the same phase there is an apparent attraction; between bodies pulsating in the
    opposite phase there is an apparent repulsion, the force being proportional to the product of the two intensities
    of pulsation, and proportional to the inverse square of the distance".
  - Dazu: "... the direction of the force in the hydrodynamic field is opposite to that of the corresponding force in
    the electric or magnetic field."
  - Unsere Formel geht fuer qd << 1 in diese Form ueber.
- Getestet ist nur das Fernfeld qd ~ 72 bis 78. Die 1/d^2-Form ist damit **nicht** geprueft (Codex).

### Bewertung: von Codex uebernommen (KRAFT-KONZEPTPRUEFUNG.txt, Abschnitte 1 und 2)

- **0,76:** Vorzeichen, normierte Amplitude und Streuphase treffen die Kriterien aus Nachtrag 1 an allen vier Abstaenden.
  - Felder: .paare[i].verhaeltnis 1,008 / 0,972 / 1,092 / 1,053; .fit.chi 0,524 gegen 0,514; .fit.alpha 1,013.
  - Das ist ein begrenzter positiver Dynamikbefund, kein konservatives Paarpotential und kein Bindungsnachweis.
- **still:** Das strenge Schalterkriterium (alle |Delta d(300)| < 5e-4) ist **verfehlt**:
  - d_1 -6,12e-4 und d_4 -1,25e-3 liegen darueber, d_2 und d_3 bestehen.
  - Die grobe Widerlegungsgrenze (> 10 % des 0,76-Signals) ist **nicht erreicht**.
  - alpha = 0,216 ist ein Formfit-Parameter mit schlechtem Fit, keine Restkraftquote.

### Neu: zweite Gitterstufe h = 0,15

- Laeufe: aus-k2-{076,still}-grob/auswertung_bj.json, Felder .paare[i].Delta_d_Ende, .verhaeltnis, .fit.
- 0,76, Delta d(300) fein / grob:

| d | fein | grob | Verhaeltnis fein / grob |
|---|---|---|---|
| 30 | +0,01879 | +0,01533 | 1,008 / 0,831 |
| 30,654 | +0,06181 | +0,06107 | 0,972 / 0,945 |
| 31,309 | -0,01790 | -0,01548 | 1,092 / 1,005 |
| 31,9635 | -0,06392 | -0,06012 | 1,053 / 1,019 |

- Fit grob: alpha 0,976, chi 0,496; die Vorhersage fuer chi ist 0,514.
- Die Kriterien aus Nachtrag 1 bestehen auch auf dem groben Gitter: Vorzeichen d_2 positiv, d_4 negativ; Verhaeltnis in
  [0,7; 1,3]; chi +-0,4.
- Gitteraenderung an den Baeuchen 1 % und 6 %, nahe den Knoten 14 % und 18 %.
  - Die Latte "Effekt (grob) >= 5 x Aenderung" (wie medium1d) besteht an drei von vier Punkten; d_1 verfehlt sie
    (0,0153 < 5 x 0,0035).
  - Fuer K2 war sie nicht als Zahl vorab gesetzt.
- still, Delta d(300) fein / grob:
  - d_1: -6,12e-4 / -5,23e-4
  - d_2: +1,24e-4 / +3,68e-4
  - d_3: -2,52e-4 / +9,99e-4
  - d_4: -1,25e-3 / -1,9e-5
- Schalterkriterium auf grob: ebenfalls verfehlt (d_1 und d_3 ueber 5e-4).
- Die Reste bei still sind **nicht gitterstabil**: Bei d_3 wechselt zwischen den Gittern das Vorzeichen, bei d_4 aendert
  sich der Betrag um das 66-Fache.
- Groesster Rest: 2,0 % (fein) bzw. 1,6 % (grob) des 0,76-Bauchwerts. Das ist ein direkter Vergleich derselben
  Messgroesse, keine Restkraftquote.
- Einzelball still: P(50) = 7,92e-5 (fein) / 7,97e-5 (grob), also 0,7 % von P(0,76). Dieser Rest ist gitterstabil.
  - Ob er in der ersten Harmonischen liegt (dann traegt er zur Kraft bei) oder in der zweiten (dann faellt er in der
    Differenz heraus), ist nicht zerlegt: **fehlt**.
- alpha still grob 0,479 gegen fein 0,216: Der Formfit ist nicht stabil. Das bestaetigt Codex' Lesart.

## K3: Schall im Kondensat (Goldstone)

### Formel (PLAN Abschnitt 4)

- Statisch regt eine Delle die Phase nicht an. Die Antwort laeuft ueber die massive Dichtemode:
  F_B = -lam^2 C0 s~^2 e^{-M d} (1D) mit M = sqrt(4 g4 C0). Weit reichende Kraefte gibt es nur mit Quellfluss,
  Bewegung, Schwingung, Wirbeln oder Fluktuationen [H].
- Literatur, an der Quelle gelesen (arXiv-Abstract 1607.04507): Naidon, J. Phys. Soc. Jpn. 87, 043002 (2018): "the two
  impurities form two polarons that interact through a weak Yukawa attraction mediated by virtual excitations".
  - Die Reichweite steht nicht im Abstract [L?].
  - Camacho-Guardian und Bruun (2018): nicht gelesen [L?].

### Bewertung: von Codex uebernommen (KRAFT-KONZEPTPRUEFUNG.txt, Abschnitte 3 und 4)

- Nullkontrollen bestanden (Einzelbaelle, lam = 0).
- Alle 15 Mittelwerte sind anziehend.
- Die Regel "konstante Kraft" ist widerlegt: Die Kraft faellt mehr als zehnfach ueber Delta d = 6.
- 13 von 15 bestehen nur die eingebaute Gitterlatte; beide d = 10-Faelle bei C0 = 0,1 verfehlen.
- **Die Yukawa-Abklingrate ist nicht bestaetigt:**
  - C0 = 0,1: 1,81 / 0,57 / 0,53 / 0,83 gegen M = 0,447
  - C0 = 0,3: gegen M = 0,775 ebenfalls verfehlt
  - Nur das Paar 14-18 bei lam = -0,1 passt (0,472).
- Vorfaktor: bei d = 14 bis 18 innerhalb Faktor 2, bei d = 12 und 20 nicht.
- Der Vorzeichenvergleich lam = +-0,1 verfehlt bei d = 10.
- Fallen halten die Baelle: keine Aussage ueber freie Bindung.
- Die Halbfenster zeigen, dass die Stationaritaet nicht gesichert ist.
- Kein eigener Widerspruch zu dieser Bewertung.

## TET-1: Tetraeder mit 120-Grad-Dreieck (PLAN Abschnitt 5, Nachtrag 2)

### Lauf und Werte

- .69 p4000a (fein: h = 0,08, N_alpha = 384) und p4000b (grob: h = 0,12, N_alpha = 240); omega^2 = 0,76, k0 = 0,48990.
- JSON: aus-tet1-{fein,grob}/tet1.json, Felder .laeufe[i].neutral_E.harm, .neutral_F.harm, .gleich_E.harm,
  .gleich_F.harm, .c3_paar, .steigungen[j].

| d | c3 (120 Grad) | 6 beta J33 (Paaranteil) | c3/Paar | \|c1\|, \|c2\| (120 Grad) | c1 0/0/0, F = E - omega Q |
|---|---|---|---|---|---|
| 8 | 8,315e-2 | 1,801e-1 | 0,462 | < 1,1e-14 | -31,04 |
| 10 | 3,858e-3 | 6,820e-3 | 0,566 | <= 3,0e-15 | -8,874 |
| 12 | 1,511e-4 | 2,420e-4 | 0,625 | < 1,8e-14 | -2,458 |
| 14 | 5,729e-6 | 8,684e-6 | 0,660 | < 1,1e-14 | -0,7488 |
| 16 | 2,187e-7 | 3,208e-7 | 0,682 | < 2,6e-14 | -0,2411 |

- Fein und grob stimmen in c3/Paar auf 1e-4 und in den Steigungen auf 1e-3 k0 ueberein.
- c3 aus E und aus E - omega Q ist gleich (auf 1e-7 relativ), wie vorab hergeleitet.

### Kriterien

| Kriterium | Herkunft | Ausgang |
|---|---|---|
| (i) \|c1\|, \|c2\| < 1e-9 \|c0\| | Vorgabe der Leitung | **bestanden**: <= 1,2e-14 relativ auf beiden Gittern |
| (ii) Steigung c3 in [2,5; 3,5] k0 | Vorgabe der Leitung | **bestanden**: 3,134 / 3,307 / 3,340 / 3,333 k0 (8-10, 10-12, 12-14, 14-16) |
| (ii') Steigung = 3 k0 + 3 ln(d2/d1)/(d2 - d1) +- 0,3 k0; c3 > 0 | eigene Vorhersage | c3 > 0 bestanden. Steigung: 8-10 **verfehlt** (3,134 gegen 3,683); 10-12, 12-14, 14-16 bestanden (-0,25 / -0,13 / -0,08). Nach dem Rauchtest nicht mehr blind |
| (iii) Gegenprobe 0/0/0, Steigung der ersten Harmonischen "nahe k0" | Vorgabe der Leitung | ohne Zahlenfenster nicht entscheidbar. E: 0,83 / 0,89 / 0,93 / 0,96 k0; F = E - omega Q: 1,28 / 1,31 / 1,21 / 1,16 k0 |
| (iii') Steigung = k0 + ln(d2/d1)/(d2 - d1) +- 0,1 k0 | eigene Vorhersage | Der Plan hat E oder F nicht festgelegt. Mit F (die Paarformel meint F): 3 von 4 bestanden, 10-12 verfehlt (+0,12). Mit E: 0 von 4 |
| Zusatz: c3/Paar in [0,7; 1,3] bei d >= 10 | eigene Vorhersage | **verfehlt** (0,57 bis 0,68, mit d steigend). Echte Dreikoerperterme senken c3 um 32 bis 43 % |

### Was das heisst [H]

- Beim 120-Grad-Dreieck heben sich die erste und zweite Harmonische exakt auf.
- Die verbleibende Phasenabhaengigkeit der Spitze faellt wie e^{-3,3 k0 d}, die erste Harmonische beim nicht neutralen
  Dreieck wie e^{-1,2 bis 1,3 k0 d} (F).
- Bei d = 10 ist c3 das 4,3e-4-Fache von |c1(0/0/0)|, bei d = 16 das 9,1e-7-Fache.
- Die Energie ist am kleinsten bei phi = pi/3 (mod 2 pi/3), also wenn die Spitze gegenphasig zu einer Ecke steht.
- Grenzen:
  - Die Analogie zu Farbneutralitaet und kurzreichweitiger Restkraft ist strukturell.
  - Es gibt keine SU(3)-Ladung, keine Eichfelder und keinen Einschluss (wie FA-1).
  - Ueberlagerung in fuehrender Ordnung: kein Stabilitaets- oder Bindungsnachweis (Codex).
  - Zeitlauf der Spitze: **fehlt**.

## Einordnung (Zusatz der Leitung 08:04)

- **Teilchen-Wirbel-Dualitaet in 2+1D** [L?]:
  - Ambegaokar, Halperin, Nelson, Siggia 1980; Dasgupta und Halperin 1981; Fisher und Lee 1989. Nicht an der Quelle
    gelesen: Die Websuche war erschoepft, APS-Seiten sind nicht abgerufen.
  - Einordnung [H]: Sie braucht eine masselose Phase, also einen Kondensat-Hintergrund, bei uns das chi-Medium. Dann
    wechselwirken Wirbel ueber ln r, und die Magnus-Kraft entspricht der Lorentz-Kraft.
  - Das waere die sauberste abgeleitete Eichkraft im Modell, aber nur in 2+1D.
  - Wirbel in einem Q-Ball im Vakuum (ROT-1) haben aussen kein masseloses Phasenfeld und daher keine ln r-Kraft.
  - In 3+1D koppeln Wirbellinien an ein 2-Form-Feld (Kalb-Ramond): Die "Ladungen" sind Linien, keine Punktteilchen.
    Das ist keine Elektrodynamik mit Punktladungen.
- **Akustische Metrik:**
  - Unruh, Phys. Rev. Lett. 46, 1351 (1981), Abstract gelesen: "a thermal spectrum of sound waves should be given out
    from the sonic horizon in transsonic fluid flow".
  - Barcelo, Liberati, Visser, Living Rev. Rel. 8, 12 (2005), Abstract gelesen: Uebersicht ueber Analogmodelle.
  - Die Aussage "Kinematik ja, Dynamik nein (keine Einstein-Gleichungen, kein Spin 2)" steht nicht in den Abstracts;
    sie ist unsere Einordnung [L?].
  - Bezug [H]:
      Bewegung, nicht das statische K3.
    - K3 zeigt im gemessenen Fenster keine konstante weitreichende Kraft statischer Dellen.
    - Glied 7/10 der Spin-2-Kette bleibt davon unberuehrt.

## Fehlerkasten

- 08:24: lokal ein leerer Aufruf `python3 -` (Heredoc ohne Inhalt); schon in PLAN Nachtrag 2 vermerkt.
- 08:35: Start mehrerer Laeufe mit einer Befehlskette `R=... && K=... && nohup ... &`. Damit lief die ganze Kette im
  Hintergrund, nur K3 startete. K1-1D, TET-1 und K2-grob fehlten deshalb in Codex' Bestand (06:57 UTC). Nachgeholt ab
  09:57.
- 08:37: Der Neustart wurde abgelehnt (Nutzungspause der Leitung bis ~09:51).
- 09:59: eigene wartende kleintest-Instanz (Spur cpu, K1-3D-Auswertung still) per PID beendet, weil die Spur belegt
  war, und auf p4000a neu gestartet; kein pkill -f.
- Methodenwechsel K1 nach dem Rauchtest (Nachtrag 2): Die d''(0)-Fits sind nur noch beschreibend. Das K1-3D-Fenster ist
  aus der K1-1D-Regel uebertragen.
- TET-1 (iii'): E oder F war im Plan offen; beide sind berichtet.
- __pycache__ im Ordner kraft1/ (lokaler Rauchtest) entfernt.

## Einfach gesagt

Wir haben geprueft, ob unser Feldmodell ausser der Randkraft noch andere Kraefte hervorbringt. Die Randkraft stimmt:
Gegenphasige Baelle fliegen fast genau so schnell auseinander, wie die Formel sagt (die alte Abweichung aus Runde 3
kommt wohl von der damaligen Messmethode). Atmende Baelle, die Wellen aussenden, schieben oder ziehen sich je nach
Takt und Abstand so, wie die Bjerknes-Formel es vorhersagt; an der stillen Stelle schrumpft dieser Effekt auf 1 bis
2 %, aber nicht nachweislich auf null. Im Kondensat fanden wir keine weitreichende Kraft ruhender Dellen. Drei Baelle
im 120-Grad-Muster heben ihre Wirkung auf die Phase eines vierten Balls fast ganz auf; es bleibt nur ein Rest, der mit
dem Abstand dreimal schneller abfaellt.
