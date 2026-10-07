# SPROSSEN-L1L2: Vorab gewerteter Sprossentest fuer Dipol (l = 1) und Quadrupol (l = 2) (Runde 21)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 17:56:38 CEST (date), vor jeder Rechnung dieser Karte.
- Herkunft:
  - SPROSSEN-VORAB (Runde 20): Die lineare Sprossenregel sagte 12 neue l = 0-Stellen vorab gewertet richtig voraus, alle
    Abweichungen negativ (der Abstand schrumpft).
  - HUELLEN-DIPOL (R19, 19 Stellen bis R = 19,4) und HUELLEN-QUADRUPOL (R20, 15 Stellen bis R = 19,4) liefern die
    Leitern fuer l = 1 und l = 2.
  - Fast Lane nach v3: Die Karte traegt deutlich, die naechste Runde beginnt sofort.
- Zweck:
  - (a) Die Regel innerhalb jedes l vorab wiederholen, ohne Paarung ueber l hinweg; diese war in HUELLEN-QUADRUPOL das
    Problem.
  - (b) Die Hypothese "schrumpfender Abstand" [H] als zweite, gleichzeitig festgelegte Vorhersage gegen die lineare
    stellen.
- Explorativ (v3), Hypothesen [H].

## Vorgehen

- Code wie HUELLEN-DIPOL (l = 1) und HUELLEN-QUADRUPOL (l = 2), unveraendert bis auf die Startpunkte. Newton auf W in
  (omega^2, rho) an den vorhergesagten R; Hintergruende bis R ~ 24,5 (omega^2 bis etwa 0,78).
- **Annahme einer Stelle** wie in SPROSSEN-VORAB:
  - |W| <= 1e-9 mit Rangabfall
  - Kurve nur ueber Stetigkeit von rho(R) (Abstand zur glatten Fortsetzung kleiner als ein Zehntel des Abstands zur
    Nachbarkurve) und Rang
  - Rechteck-Umlauf von W auf beiden Stufen aufgeloest +-1, Stufen auf 1e-6
  - Nachstarts bei +-0,25 erlaubt; gefunden heisst innerhalb +-0,5 in R
- **Pflicht vor dem Einfrieren (L4):** Testcode samt Kriterium an den letzten zwei bekannten Stellen jeder Kurve unten
  laufen lassen; alle muessen angenommen werden. Sonst nur das Kriterium berichtigen und erneut pruefen.

## Vorhersagen (vor jeder Rechnung dieser Karte)

- **P_lin:** naechste Sprosse = letzte + letzter Abstand, die uebernaechste ebenso.
- **P2 (schrumpfender Abstand):** naechster Abstand = letzter Abstand + 0,85 x (letzter - vorletzter Abstand), danach ebenso.
- Grundlage: die Lagen in RUNDE-19/huellen-dipol/ERGEBNIS.md und RUNDE-20/huellen-quadrupol/ERGEBNIS.md (Stufe 1, drei
  Nachkommastellen).

**Satz A (formal, Kurven mit mindestens 4 bekannten Stellen):**

| l | k | letzte Lagen R | P_lin 1 / 2 | P2 1 / 2 |
|---|---|---|---|---|
| 1 | 0 | 14,161 / 16,593 / 19,02 | 21,447 / 23,874 | 21,443 / 23,862 |
| 1 | 1 | 13,622 / 15,839 / 18,024 | 20,209 / 22,394 | 20,182 / 22,316 |
| 1 | 2 | 14,745 / 17,094 / 19,378 | 21,662 / 23,946 | 21,607 / 23,789 |
| 2 | 0 | 12,694 / 15,172 / 17,63 | 20,088 / 22,546 | 20,071 / 22,498 |
| 2 | 1 | 14,301 / 16,565 / 18,787 | 21,009 / 23,231 | 20,973 / 23,129 |

**Satz B (nur berichtet, junge Kurven):**

| l | k | bekannte Lagen R | P_lin 1 / 2 | P2 1 / 2 |
|---|---|---|---|---|
| 1 | 3 | 15,584 / 18,1 | 20,616 / 23,132 | - |
| 2 | 2 | 12,715 / 15,268 / 17,68 | 20,092 / 22,504 | 19,972 / 22,162 |

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| W0 | L4 bestanden | 85 % |
| W1 | Satz A, P_lin: alle 5 ersten Sprossen innerhalb +-0,06 | 50 % |
| W2 | Satz A, P_lin: mindestens 4 von 5 zweiten Sprossen innerhalb +-0,15 | 60 % |
| W3 | Der Umlauf wechselt entlang jeder Kurve von Satz A weiter | 85 % |
| W4 | P2 hat ueber Satz A (10 Sprossen) eine kleinere mittlere Abweichung als P_lin | 75 % |

**Bedeutung (vorab):**
- W1 bis W3 treffen ein: Die Sprossenregel sagt auch l = 1- und l = 2-Stellen vorab voraus [H, im Modell gestuetzt].
- W4 trifft ein: Der schrumpfende Abstand verbessert die Vorhersage; das stuetzt das Bild Delta R ~ pi/k_innen(R) [H].
- Abweichungen > 0,3 bei Satz A: Die Regel traegt fuer l > 0 nicht.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu bis cpu4 und cpu6, je <= 10 min.
- Plan nach der L4-Pruefung einfrieren; Nachtraege nur eingefroren. Zeitbox 90 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.

- Berichtigung der Leitung (2026-10-02 17:56:55 CEST, vor jedem Lauf und vor dem Agentenstart): P2 fuer l = 1, k = 1, zweite Sprosse
  22,317 -> 22,316. Rundungsfehler beim Nachrechnen gefunden: 20,1818 + 2,13468 = 22,31648.
