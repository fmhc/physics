# Runde 4 (v3): weitere Wellen-, Chemie- und Biologie-Karten, mehr parallel

Leitung: claude-primary. Begonnen: 2026-09-30 01:24:44 CEST (gemessen). Explorativ, keine formale Bestaetigung.

## Rahmen

- Finn: "schön weiter machen noch mehr parallel".
- Runden 2 und 3 laufen noch (drei Code-Agenten). Runde 4 kommt mit zwei weiteren Code-Agenten dazu; zusammen fuenf. Das
  ist der Fan-out-Fall aus Finns globalen Regeln: unabhaengige Karten, je eigener Ordner.
- Jede Rechnung hoechstens 10 min GPU, gerechnet in VS-1-Portionsluecken oder nach VS-1.

## Karten und Tests

| Karte (Quelle) | Test | wer |
|---|---|---|
| Wellen 1 Russell | 1D-Stoss zweier Baelle bei drei Geschwindigkeiten; abgestrahlter Energieanteil | Agent R4-W |
| Wellen 2 Monsterwelle | 1D-Hintergrund mit Rauschen; Statistik der Spitzen gegen die Gauss-Rayleigh-Erwartung | Agent R4-W |
| Wellen 3 Stokes-Drift | Ball in laufender Hintergrundwelle, zwei Amplituden; Drift je Periode, Skalierung mit a^2 | Agent R4-W |
| Wellen 12 Surfen | grosse laufende Welle plus Ball; Energiegewinn | Agent R4-W |
| Wellen 13 Brandung | Ball laeuft in eine Dichterampe; Verformung, Zerfallsschwelle | Agent R4-W |
| Chemie 8 Katalyse | 1D-Dreierstoss; Verschmelzungsschwelle mit und ohne dritten Ball | Agent R4-CB |
| Chemie 16 Kettenreaktion | 1D-Reihe knapp unterkritischer Paare; ersten zuenden, Frontgeschwindigkeit | Agent R4-CB |
| Chemie 20 Chromatographie | Baelle verschiedener omega durch eine raue Zone; Durchlaufzeit gegen omega | Agent R4-CB |
| Bio 13 Neuron | Stossamplitude gegen Antwort; Schwelle ja oder nein | Agent R4-CB |
| Bio 27 Wundheilung | Profil teilweise ausgeschnitten; Heilzeit gegen Schadensgroesse | Agent R4-CB |
| Bio 41 Nervenfaser | Kette aus Baellen, ersten anstossen; Laufgeschwindigkeit und Daempfung | Agent R4-CB |
| **Bio 18 Artbildung (Zufall)** | Familien entlang omega (3D radial m = 0; 2D radial m = 0, 1, 2); Verzweigungen, Q(omega), E(omega) | Agent R4-CB |

- Die Zufallskarte ist Bio 18. Gezogen um 01:24:44 mit `shuf -n 1` aus den noch nicht vergebenen 36 Biologie-Ideen.
- Quellen der Ideen:
  - RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md
  - RUNDE-03/IDEEN-20-QBALL-CHEMIE.md
  - RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md

## Tests: Ergebnisse

Ausgewertet von einem Ernte-Agenten (Anthropic): RUNDE-04/ERGEBNISSE-R4.md, 02:27:59 bis 02:47:08 CEST.
- Alle 13 Aufrufe (inklusive Profil) liefen auf der .69 mit rc 0 (Spur p4000b).
- Von 12 Karten wurden 2 getroffen (Kette, Artbildung), 6 teilweise und 4 verfehlt (Stokes, Brandung, Chromatographie,
  Nervenfaser).
- L3 ist in 10 von 12 bestanden, nicht bei Russell und Nervenfaser.

Kernzahlen (fein):
- **Stokes:**
  - dX 1,44 / 2,92 / 6,01 bei a = 0,01 / 0,02 / 0,04, also linear in a statt a^2.
  - Auch die Anfangsgeschwindigkeit waechst linear in a. Verdacht: Die Welle lag bei t = 0 schon auf dem Ball.
- **Brandung:**
  - Kein Ball wird vom See aufgenommen, 3 von 12 werden durchgereicht.
  - Eine Bilanz ist unlesbar (Seeanteil -2,44), weil nur die linke Seewand gemessen wird.
- **Katalyse:**
  - Mit Bruecke verschmilzt ein gegenphasiges Paar an je einem v-Punkt, knapp ueber der Schwelle (1,52 bzw. 1,53 Q0 bei
    Schwelle 1,5 Q0).
  - Ohne Bruecke und nur mit dem Partner A-C verschmilzt nichts.
- **Russell:**
  - Gleichphasige Stoesse strahlen 3,6 bis 6,8 % der Energie ab, gegenphasige hoechstens 5,8e-5.
  - L2 und L3 sind gerissen.
- **Nervenfaser:**
  - Die "Stossgeschwindigkeiten" reichen bis 3,97, also ueber c = 1.
  - Die Messgroesse ist damit keine Signalgeschwindigkeit; L3 ist gerissen.
- **Chromatographie:** Bis 52,6 % Ladungsverlust, 14 von 36 Durchlaufzeiten fehlen; die Trennung ist negativ.
- **Artbildung:** 3D Q_min = 111,9 bei omega^2 = 0,93; die 2D-Familien sind monoton; es gibt keine Artgrenze.

## Abschaetzung

Leitung claude-primary, 2026-09-30 02:54:37 CEST (gemessen vor dem Schreiben).

| Karte | Entscheidung | Grund |
|---|---|---|
| Wellen 3 Stokes | **weiter** | Die lineare Drift in a ist vermutlich ein Starteffekt. Neu im stabilen chi-Medium mit einlaufender Welle (RUNDE-06, Agent M1, Karte 5) |
| Wellen 13 Brandung | parken | Befund "durchgereicht statt aufgenommen" ist sichtbar, die Bilanz aber ohne zweite Seewand unlesbar; bei Gelegenheit mit beiden Waenden |
| Chemie 8 Katalyse | parken | nur je ein v-Punkt knapp ueber der Schwelle, kein Klumpen nahe 2 Q0; kein tragender Katalyseeffekt |
| Wellen 1 Russell | parken | L2 und L3 gerissen; gegenphasig fast verlustfrei ist bekanntes Solitonverhalten (L4) |
| Wellen 12 Surfen | parken | kein Mitnehmen; v_Ende ~ A^2 ist Kraft zweiter Ordnung, ohne Messbezug |
| Chemie 20 Chromatographie | parken | Messung unbrauchbar (Ladungsverlust bis 53 %, fehlende Zeiten) |
| Bio 13 Neuron | parken | keine Schwelle, glatte Antwort |
| Bio 27 Wunde | parken | heilt, grosser Schaden schneller, aber mit bis 68 % Abstrahlung; nichts Tragendes |
| Bio 41 Nervenfaser | parken | Messgroesse falsch definiert (Werte ueber c); L3 gerissen |
| Wellen 2 Monsterwelle | verwerfen | Ein-Feld-Hintergrund ist instabil, das stabile chi-Medium ist defokussierend: keine Monsterwellen moeglich |
| Chemie 16 Kette | verwerfen | wie vorhergesagt Reichweite 0; nichts Neues |
| Bio 18 Artbildung (Zufall) | verwerfen | bekannt (L4): monotone Familien, Q_min wie in Runde 2 |

- Bilanz: 1 weiter, 8 parken, 3 verwerfen.
- Urteil gegen Zufall: Die Zufallskarte (Artbildung) ging wie erwartet aus und wird verworfen. Von den gewaehlten Karten
  traegt nur Stokes weiter, und auch nur als Umbau ins Medium.
- Lehre: Karten, die ein Medium brauchen (Stokes, Brandung, Chromatographie), waren im Ein-Feld-Modell schlecht
  gestellt. Das bestaetigt Fables Befund und die Umleitung in das Zwei-Feld-Medium.

## Einfach gesagt

Von zwoelf kleinen Versuchen zu Wellen, Chemie und Biologie traegt keiner fuer sich allein weiter. Der interessanteste,
die Drift eines Balls in einer Welle, wird neu gerechnet, diesmal in einem ruhigen zweiten Feld als "Wasser" und mit einer
Welle, die von weit her kommt. Einige Messungen waren selbst fehlerhaft, etwa Geschwindigkeiten ueber der
Lichtgeschwindigkeit; diese Karten liegen auf Eis. Die Runde zeigt vor allem: Unser Ein-Feld-Modell hat kein ruhiges
"Wasser", deshalb gehen Wasser-Bilder dort schief.
