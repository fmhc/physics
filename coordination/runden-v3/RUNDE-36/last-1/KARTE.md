# LAST-1: Ziehen sich gleiche Lasten in einem Stabnetz an, und warum ist das trotzdem keine Schwerkraft? (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 22:41:18 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finns Frage "Kraefte in den Staeben -> Schwerkraft?" (RUNDE-34/tetra-konzept/; Finn ~22:30 zur Spin-2-Kopplung).
  - Gegenleser-Befund B2 (RUNDE-35/GEGENLESEN-R35.md, Abschnitt 3.2): Vorgegebene Lasten, die Arbeit leisten, ziehen sich
    an (Gummituch); Zwangsbedingungen (Eis) stossen ab.
  - Bezug von Laue (RUNDE-29): Fuer einen ruhenden, abgeschlossenen Koerper ist das Integral der Spannungen null.
- Kennzeichen: [M] Mathematik (vorab ableitbar), [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Punktlasten** [M, L: Kelvin-Loesung]:
  - Im elastischen Medium ist das Gesamtpotential Pi = U_el - W = -(1/2) sum f.u.
  - Wechselwirkung zweier Lasten: Pi_12 = -f1 . G(r) . f2.
  - Isotrop: G_ij(r) = [(3 - 4 nu) delta_ij + r_dach_i r_dach_j]/(16 pi mu (1 - nu) r).
  - **Gleich gerichtete Lasten ziehen sich an, mit 1/r wie die Schwerkraft.**
  - Haken: Die Lasten tragen eine Nettokraft, die von aussen kommen muss (beim Gummituch die Erdschwere). Die
    Schwerkraft steckt also schon drin.
- **Selbsttragende Quellen ohne Nettokraft** (ein zu langer Stab wie in EIS-1, ein aufgeweiteter Knoten bzw.
  Dilatationszentrum, ein Einschluss mit geaenderten Ruhelaengen): Das ist der Fall eines abgeschlossenen Koerpers (von
  Laue).
  - Ihr Fernfeld faellt eine Ordnung schneller; die Wechselwirkung geht wie 1/r^3 [L: Eshelby 1956].
  - Im unendlichen isotropen Medium wechselwirken zwei isotrope Dilatationszentren gar nicht [L?: Satz nach Bitter bzw.
    Crum].
  - Im kubisch-anisotropen Gitter geht es wie 1/r^3, mit richtungsabhaengigem Vorzeichen [L].
- **Isotrope Abstimmung** (Gegenleser B1, Rechnung aus Tabelle A1 von NETZ-C-1): fcc mit Zentralfedern 1 und
  normierten Winkelfedern wird bei k_theta = 1/18 elastisch isotrop (Zener-Verhaeltnis 1). Das wird hier mitgeprueft.

## Test (Code-Agent)

- **Netz:** fcc-Stabnetz, Kantenlaenge 1, Masse egal (statisch), Zentralfedern 1, Winkelfedern wie in NETZ-C-1
  (normiert ueber cos theta; Code RUNDE-35/netz-c-1/code/).
  - Zwei Fassungen: k_theta = 0 (anisotrop, Zener 2) und k_theta = 1/18 (isotrop laut Gegenleser).
- **Loeser:** periodisches Gitter, L^3 kubische Zellen, Gitter-Greensche Funktion per FFT.
  - Nettokraft: q = 0 entfaellt, entspricht einem gleichmaessigen Gegenkraft-Hintergrund. Hintergrundkorrektur bzw.
    Groessenreihe offenlegen (Lehre aus TENSOR-EIS-0: Scheinanziehung auf zu kleinen Tori).
- **Quellen:**
  - (a) zwei gleich gerichtete Punktlasten f auf Knoten
  - (b) zwei Dilatationszentren (alle 12 Staebe um einen Knoten mit Ruhelaenge 1 + delta)
  - (c) zwei zu lange Einzelstaebe (Fehlpass wie EIS-1), parallel
- **Gemessen:** Wechselwirkung Pi_12(r, Richtung) = Pi(Paar) - Pi(einzeln) - Pi(einzeln) fuer r = 2 bis 16 und
  [100], [110], [111] plus mindestens 12 weitere Richtungen. Daraus der Abfallexponent.
- Groessen L = 32 und 64 (bzw. so gross wie in 10 min moeglich).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| L0 | Kontrolle: elastische Konstanten aus dem Gitter treffen fuer k_theta = 0 die Form C11 = 2 C44, C12 = C44 auf 1e-6; bei k_theta = 1/18 ist das Zener-Verhaeltnis 1 innerhalb 1 % | 85 % |
| L1 | Gleich gerichtete Punktlasten ziehen sich an (Pi_12 < 0) fuer alle r >= 3 und alle Richtungen; Abfallexponent 1 +- 0,1; im isotropen Netz innerhalb 5 % der Kelvin-Formel fuer r >= 6 (nach Hintergrundkorrektur) | 75 % |
| L2 | Isotropes Netz, isotrope Dilatationszentren (b): Bei r = 8 ist der Betrag von Pi_12 hoechstens 5 % des Betrags im anisotropen Netz in derselben Richtung, und er faellt mindestens wie r^-3 | 60 % |
| L3 | Anisotropes Netz (k_theta = 0), Dilatationszentren (b): Pi_12 ~ r^(-3) (Exponent 3 +- 0,4), Vorzeichen laengs [100] und [111] entgegengesetzt | 60 % |
| L4 | Selbsttragende Quellen (b, c): Die Verschiebung faellt fern wie r^-2, nicht wie r^-1 (keine Nettokraft) | 85 % |

**Bedeutung (vorab):**
- L1 bis L4 treffen ein: Kraefte in Staeben geben eine schwerkraftartige 1/r-Anziehung nur fuer Lasten mit Nettokraft,
  und die muss von aussen kommen (Gummituch-Zirkel).
  - Abgeschlossene Klumpen (ohne Nettokraft, von Laue) wechselwirken ueber das Netz nur kurzreichweitig (1/r^3) oder,
    im isotropen Netz, gar nicht.
  - Elastizitaet allein macht also keine Schwerkraft; die Quelle muss an die Energie und an die Zeit (h_00) koppeln
    (LAPSE-0).
- L2 verfehlt: Auch im isotropen Netz wechselwirken Dilatationszentren merklich; das waere ein Gittereffekt.
  Beschreiben.
- L0 verfehlt: Die isotrope Abstimmung des Gegenlesers stimmt nicht; B1 dann neu fassen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6 (nicht cpu2, cpu3, cpu4, cpu5, p4000a,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
