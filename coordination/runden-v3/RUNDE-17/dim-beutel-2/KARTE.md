# DIM-BEUTEL-2: Misst der Beutelexponent auf Fraktalen die spektrale Dimension? (gewertete Wiederholung, Runde 17)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 10:49:36 CEST (date), vor jeder Rechnung
  dieser Karte.
- Herkunft: DIM-BEUTEL (RUNDE-16/dim-beutel/ERGEBNIS.md). Auf Kette, Quadrat- und kubischem Gitter misst der
  Beutelexponent p die Dimension (d = p/(1 - p) = 1,001 / 2,002 / 3,02).
  - Beim Sierpinski-Dreieck blieb der Fortsetzungsast haengen; Ausgang offen.
  - Ein nicht gewerteter Nachtrag mit frischen selbstaehnlichen Starts gab p = 0,575 bis 0,594, naeher an d_s.
  - Diese Karte macht genau dieses Verfahren vorab zur Regel und fuegt ein zweites Fraktal mit groesserem Abstand
    d_s/d_H hinzu.
- Explorativ (v3). Hypothese der Leitung [H]: p = d_s/(d_s + 1), mit der spektralen statt der Hausdorff-Dimension
  (Herleitung in RUNDE-16/dim-beutel/KARTE.md).

## Graphen

- **F1 Sierpinski-Dreieck**, Generation 10 (wie DIM-BEUTEL), Kontrolle g = 9.
  - d_s = 1,3652 (in DIM-BEUTEL direkt gemessen), d_H = ln3/ln2 = 1,5850.
  - Soll: p_s = 0,5772 bzw. p_H = 0,6131.
- **F2 Vicsek-Fraktal** (Kreuz-/Plus-Fraktal, Baumstruktur), Generation so gross wie in 10 min rechenbar, Kontrolle eine
  Generation kleiner.
  - d_H = ln5/ln3 = 1,4650; d_s = 2 ln5/ln15 = 1,1887 [L?].
  - Soll: p_s = 0,5431 bzw. p_H = 0,5943, Abstand 0,051.
  - **Kontrolle vorab:** d_s direkt messen, ueber Laplace-Zaehlung oder Random Walk wie in DIM-BEUTEL. Weicht sie um mehr
    als 0,03 von 1,1887 ab, gilt der gemessene Wert als Soll.

## Verfahren (vorab festgelegt)

- Modell und Energie wie DIM-BEUTEL (Code in RUNDE-16/dim-beutel/code/ darf genutzt werden).
- **Frische Starts** je Ladungsstufe, keine Fortsetzung ueber viele Stufen.
  - Startform A: Kugel im Graphabstand R0 um einen Mittelpunkt hoher Generation.
  - Startform B: zweiter Mittelpunkt bzw. andere Anfangsradien.
  - Je Stufe gilt die tiefere Energie von A und B.
- **Ladungsstufen:** je selbstaehnlicher Periode mindestens 4 Stufen, ueber mindestens 3 Perioden im Beutelbereich.
  - Beutelradius gross gegen die kleinste Zelle und klein gegen den Graphen; beides berichten.
- **Gewertete Groesse:** p_per = ln(E(Q_k+P)/E(Q_k)) / ln(Q_k+P/Q_k), ueber volle Perioden, damit die Gitterwelligkeit
  sich weghebt.
  - Gewertet wird das Mittel ueber alle vollen Perioden im Beutelbereich, Fehlerband aus deren Streuung.
- **Kontrollen:**
  - dE/dQ = omega an jeder Stufe
  - zwei Generationen
  - zwei Startformen
  - Regulaere Gitter nicht wiederholen; sie sind in DIM-BEUTEL bestanden.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| E1 | Sierpinski: p_per = 0,577 +- 0,015, also naeher an p_s (0,577) als an p_H (0,613) | 70 % |
| E2 | Vicsek: d_s-Direktmessung 1,19 +- 0,03 | 80 % |
| E3 | Vicsek: p_per naeher an p_s (0,543) als an p_H (0,594) | 65 % |
| E4 | Bei beiden Fraktalen liegt p_per innerhalb +- 0,02 um d_s/(d_s + 1) | 55 % |

**Bedeutung (vorab):**
- Treffen E1 und E3 ein: Der Beutelexponent misst die spektrale Dimension, also wie sich Wellen und Diffusion
  ausbreiten, nicht die Raumfuellung. Er taugt dann als Dimensionsmesser fuer Graphen ohne vorgegebene Dimension.
- Trifft eines nicht ein: Die Herleitung p = d_s/(d_s + 1) ist zu einfach. Dann den Grund suchen (Lokalisierung auf
  Fraktalen, Randeffekte).

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu2, je <= 10 min. Plan vorab einfrieren.
  Nachtraege nur eingefroren, nach Laufbeginn als nachtraeglich markiert. Zeitbox 90 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
