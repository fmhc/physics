# V-1-PRAEZISION: Stimmt das Leck der stillen Wandschwingung mit exp(-2 pi/sqrt(abs(eps))), und wie sieht der Vorfaktor aus? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 02:26:47 CEST (date), vor jeder Rechnung.
- **Anlass:** V-1-WEITER (RUNDE-36/v1-weiter/ERGEBNIS.md, Ernte in RUNDE-36.md).
  - Die stille Wandfrequenz der ebenen Q-Ball-Wand (M1, beta = 1) leckt bei eps < 0 in einen neuen Kanal mit k ~ 1/sqrt(abs(eps)).
  - Beschreibend ln P ~ a - c/sqrt(abs(eps)) mit c = 6,31 bzw. 6,295, aufgeloest aber nur bei eps = -1e-2. Bei -3e-3 und
    -1e-3 lag das Leck unter der float64-Grenze.
  - Herleitung der Leitung [M]: Bei omega_min^2 = 3/4 ist die Wand logistisch, S = (1/2)/(1 + e^-x). Die naechsten Pole
    liegen bei x = +-i pi, also c = 2 pi.
- Schwerpunkt: Q-Baelle (Papier I, stille Schwingung).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Exponent:** Eine Kopplung, die ein glattes Wandprofil mit einer Welle e^{ikx} faltet, ist fuer grosses k ~ e^{-k d},
  d = Polabstand [M]. Die Leistung ist ~ e^{-2 k d}. Mit k = 1/sqrt(abs(eps)) (fuehrend) und d = pi folgt c = 2 pi.
- **Vorfaktor [H]:** Einfache Pole geben keine Potenzkorrektur im Fourier-Integral; Ableitungen in der Kopplung geben
  Potenzen von k. Also P ~ A abs(eps)^q exp(-2 pi/sqrt(abs(eps))) mit einem festen q.
  - Ausserdem verschiebt sich der genaue Kanal-Wellenvektor: k^2 = (1 + sqrt(1 + 4 abs(eps)(omega^2 - 1)))/(2 abs(eps))
    statt 1/abs(eps) [M]. Das gibt eine Korrektur im Exponenten von relativer Ordnung abs(eps).
- **Messproblem:** P liegt bei -3e-3 um 1e-39 [H, Hochrechnung]. Noetig ist Rechnen mit erweiterter Genauigkeit
  (z. B. mpmath mit 40 und 60 Stellen) oder ein exaktes Verfahren ueber die komplexe Ebene.

## Test (Code-Agent)

- **Modell und Groessen** wie V-1-WEITER (Code RUNDE-36/v1-weiter/code/v1w.py, PLAN.md, ERGEBNIS.md): ebene Wand, M1,
  beta = 1, Zusatzterm eps d^4 in Hintergrund und Schwankung. Leistung P im neuen Kanal bei der stillen Frequenz rho_z(eps)
  bzw. die dortige Lecktiefe nach derselben Definition.
- **Punkte:** eps = -1e-2, -7e-3, -5e-3, -4e-3, -3e-3; wenn machbar dazu -2e-3.
- **Kontrollen:**
  - zwei Genauigkeiten (Stellenzahl)
  - Gitter- bzw. Schrittweite
  - eps = -1e-2 gegen das float64-Ergebnis aus V-1-WEITER
  - eps > 0 (+3e-3), wo das Leck exakt verschwinden soll
- **Auswertung:**
  - Ausgleich ln P = a + q ln abs(eps) - c/sqrt(abs(eps)), einmal mit q = 0 fest und einmal mit q frei.
  - Dazu die Variante mit dem genauen Kanal-k statt 1/sqrt(abs(eps)).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| PR0 | Kontrollen: Zwei Genauigkeiten stimmen in ln P auf 1e-6 relativ ueberein; eps = -1e-2 trifft V-1-WEITER auf 5 % in P; bei eps = +3e-3 liegt das Leck unter 1e-60 (bzw. an der Rechengenauigkeit) | 75 % |
| PR1 | Ausgleich mit q frei ueber alle Punkte: c = 2 pi auf 1 % (6,22 bis 6,35) | 65 % |
| PR2 | Mit dem genauen Kanal-k (k d statt pi/sqrt(abs(eps))): c auf 0,3 % gleich 2 pi | 50 % |
| PR3 | [H] Der Vorfaktor ist ein Potenzgesetz: Die Reste des Ausgleichs mit q frei bleiben unter 0,05 in ln P | 55 % |

**Bedeutung (vorab):**
- PR1 und PR2 treffen ein: Das Leck ist vollstaendig verstanden. Der Polabstand pi der logistischen Wand legt es fest, ohne
  Anpassung. Fuer Papier I gibt das einen sauberen Robustheitsabsatz: Die stille Schwingung ist bei gitterartigen
  Aenderungen nur exponentiell klein undicht, mit bekannter Formel.
- PR1 verfehlt: Der beschreibende Wert 6,3 war ein Zufall des einen Punkts, oder es gibt naehere Singularitaeten
  (z. B. aus der Schwankungsgleichung selbst). Die Herleitung waere dann unvollstaendig.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
