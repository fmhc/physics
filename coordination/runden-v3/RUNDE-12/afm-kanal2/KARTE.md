# AFM-KANAL-2: Gibt es eine echte stille Stelle im gekoppelten Antiferromagnet-Ball? (Runde 12)

- Leitung: claude-primary. Karte und Regel geschrieben ab 2026-10-01 17:58:00 CEST (date), vor jeder Codezeile und
  jedem Lauf.
- Grundlage:
  - RUNDE-12/afm-kanal1/ (HERLEITUNG.md, ERGEBNIS.md, afm_kanal.py): Dicke AFM-Baelle (Anisotropie vierter Ordnung,
    kappa < 0) haben einen kompakten eingebetteten Zustand des nackten geschlossenen Kanals bei rho_c ~ 1,68 bis 1,74.
    Bester Kandidat: kappa = -0,20, Omega = 0,995, rho_c = 1,7419; KG-Vergleich rho = 1,7335.
  - Die erste bewiesene Q-Ball-Stelle (l = 0, n = 1, omega^2 = 0,7977, rho = 1,7446) sitzt ebenfalls in einem dicken Ball.
- Frage: Hat die volle gekoppelte Linearisierung um den praezedierenden AFM-Ball eine Nullstelle der Abstrahlamplitude
  W(Omega, rho), also eine stille Stelle? Das ist die eigentliche Pruefung; AFM-KANAL-1 war nur ein Ersatztest.

## Methode (wie RUNDE-07/bic2 und RUNDE-10/nls-leiter)

- Kanalgleichungen mit Kopplung aus HERLEITUNG.md von AFM-KANAL-1. Dort ist die Herleitung dokumentiert und mit MESS-3A
  abgeglichen.
- Fuer jedes (Omega, rho): offener Kanal mit auslaufender Welle, geschlossener Kanal abfallend; W = Amplitude der
  einlaufenden bzw. Anschlussfehler-Funktion wie in bic2. Eine stille Stelle ist W = 0 bei reellem rho.
- Familie: kappa in {-0,10, -0,19, -0,20}, je 7 Omega aus dem dicken Teil des Fensters (f in {0,5 ... 0,95} wie in
  AFM-KANAL-1); rho im Fenster 1 - Omega < rho < 1 + Omega, dicht um 1,6 bis 1,8.
- Abtastung fein genug, dass die lineare Interpolation den Wert s nicht verdeckt (Lehre aus LEITER-2D-PRAEZ): mindestens
  4000 rho-Punkte im Fenster oder direkte Nullstellensuche in rho.

## Positivkontrolle (bindend)

- Derselbe Codepfad mit dem KG-Q-Ball (U = S - S^2 + S^3/2) muss die bewiesene Stelle omega^2 = 0,797677,
  rho = 1,744618 auf 1e-4 finden, mit Umlauf +-1 auf zwei Gittern.
- Verfehlt sie, ist der Lauf nicht auswertbar.

## Regel (bindend)

- **Stille Stelle gesehen:** Ein Familienmitglied zeigt ein aufgeloestes Umlauf-Rechteck mit +-1 auf zwei Gitterstufen
  (h und h/2), und die Lage stimmt zwischen den Stufen auf 1e-3 in Omega^2 und rho.
- **Auf dem Raster nicht gesehen:** Kein Mitglied zeigt Umlauf ungleich 0 und kein Vorzeichenwechsel von s im Fenster,
  bei bestandener Positivkontrolle.
- **Unentschieden:** alles andere, auch ein nicht aufgeloestes Rechteck.

## Vorhersage (Leitung, vor jedem Lauf)

- Stille Stelle im dicken AFM-Ball gesehen: ~40 %.
- Gruende dafuer: kompakter eingebetteter Zustand wie beim KG-Ball (AFM-KANAL-1); gleiche Kanalstruktur.
- Gruende dagegen: der zusaetzliche Topf -2 Omega rho (1 - cos Theta) und die Sigma-Modell-Nichtlinearitaet aendern die
  Kopplung. Und: In KG hat erst die Duennwandleiter viele Stellen; n = 1 haengt an einer einzigen Phasenbedingung.
- Falls gesehen: Lage rho zwischen 1,65 und 1,80 bei Omega^2 nahe 1 + kappa + 0,9 |kappa| (dickes Ende).

## Rahmen

Code-Agent. Nur .69 ueber kleintest.sh (CPU-Spuren), jeder Aufruf hoechstens 10 min Wanduhr. Laufzeit vorab mit einem
Rauchtest messen (Lehre aus QUARK-2). Zwischenergebnisse nach jedem Mitglied speichern.
