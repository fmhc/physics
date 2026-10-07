# AFM-BREITE: Folgt die Strahlungsbreite im AFM-Ball einem Groessengesetz? (Runde 13, Leitung, kleiner Lauf)

- Leitung: claude-primary. Karte, Gesetz, Regel und Vorhersage geschrieben ab 2026-10-01 19:10:30 CEST (date), vor jedem
  Lauf dieser Karte.
- Herkunft:
  - RUNDE-12/afm-kanal2/ERGEBNIS.md: keine stille Stelle, aber die Polbreiten fallen zum dicken Ende um 8 bis 9
    Zehnerpotenzen.
  - arXiv-Woche: WKB/Gamow fuer schwach gedaempfte Zustaende, 2609.10880 [S].
- Frage: Ist der Abfall ein einfaches Groessengesetz in u = 1/sqrt(1 - Omega^2), also im Abstand der Praezessionsfrequenz
  zur Magnonluecke? Und gilt es auch fuer ein neues kappa?

## Gesetz, nachtraeglich angepasst an vorhandene Daten (kein Test, nur die Vorgabe)

- Daten: lauf-69/aus/afm-k0.20-h0.02-A.json und -B.json (AFM-KANAL-2), kappa = -0,20, Mitglieder Omega^2 = 0,90 bis 0,975.
- Je Mitglied der Median von ln Gamma ueber alle Pole mit 1,0 <= Re rho <= 1,95. Bei gerader Anzahl ist das das Mittel der
  beiden mittleren Werte.
- Kleinste Quadrate ueber 6 Mitglieder: **ln Gamma_med = 2,549 - 2,860 u**, u = 1/sqrt(1 - Omega^2). Die Residuen liegen
  hoechstens bei 0,32 in ln, ueber 4,4 Dekaden.
- Omega^2 = 0,99 (an der Newton-Toleranz, nicht angepasst): Das Gesetz gibt 4,9e-12, gemessen sind 8,5e-12 und 5,0e-12.
- Schon gesehen und deshalb kein Test: kappa = -0,10 liegt um Faktor 3 bis 7 ueber dem Gesetz, bei Omega^2 = 0,95,
  0,98 und 0,9875.
- [H] Deutung, ungeprueft: exponentielle Unterdrueckung mit der Ballgroesse. Entweder Tunneln (Gamow) oder die
  Fourier-Komponente eines glatten Profils bei fester Wellenzahl. Fuer die Karte zaehlt nur das Gesetz.

## Test (neue Mitglieder, vorher nie gerechnet)

- Code: RUNDE-12/afm-kanal2/afm_bic.py, unveraendert (sha256 b178c719...), Modus familie, Modell afm, h = 0,02, Pole ja,
  sonst Vorgaben.
- Aufruf A: kappa = -0,15 (neues kappa), f = 0,6; 0,733333; 0,833333; 0,9, also Omega^2 = 0,94; 0,96; 0,975; 0,985.
- Aufruf B: kappa = -0,20, f = 0,8 (Kontrolle K1) und f = 0,9125 (neues Mitglied, Omega^2 = 0,9825).
- Rechenort: .69, kleintest.sh, Spur cpu6. Jeder Aufruf hoechstens 10 min.

## Vorhersage aus dem Gesetz (vor dem Lauf)

| Mitglied | Omega^2 | u | Gamma_med nach Gesetz | log10 |
|---|---|---|---|---|
| kappa -0,15, f 0,6 | 0,94 | 4,0825 | 1,09e-4 | -3,96 |
| kappa -0,15, f 0,733333 | 0,96 | 5,0000 | 7,9e-6 | -5,10 |
| kappa -0,15, f 0,833333 | 0,975 | 6,3246 | 1,79e-7 | -6,75 |
| kappa -0,15, f 0,9 | 0,985 | 8,1650 | 9,2e-10 | -9,04 |
| kappa -0,20, f 0,9125 | 0,9825 | 7,5593 | 5,2e-9 | -8,28 |

## Kontrolle (bindend)

- K1: kappa = -0,20, f = 0,8 gibt dieselben Nullstellen und Polbreiten wie AFM-KANAL-2 (relativ 1e-6).
- Verfehlt K1: nicht auswertbar.

## Regel (bindend)

- **Gesetz traegt:**
  - Jedes der 5 neuen Mitglieder liegt hoechstens 1,0 Dekade vom Gesetz entfernt (|log10 Gamma_med - log10 Gesetz| <= 1,0).
  - Der Anstieg aus den 4 Mitgliedern bei kappa = -0,15 (kleinste Quadrate von ln Gamma_med gegen u) liegt mit c in
    [2,4; 3,4].
- **Gesetz traegt nicht:** Ein Mitglied liegt mehr als 1,5 Dekaden daneben, oder c liegt ausserhalb [2,0; 3,8].
- **Unentschieden:** alles andere, auch Mitglieder ohne Pole im Bereich 1,0 <= Re rho <= 1,95.

## Vorhersage (Leitung)

- K1 besteht: ~95 % (gleicher Code, gleiche Eingabe).
- Gesetz traegt: ~70 %.
- Nach den kappa = -0,10-Daten erwarte ich bei kappa = -0,15 eine Lage etwas ueber dem Gesetz (0,2 bis 0,6 Dekaden) und
  c zwischen 2,6 und 3,1.
- Bedeutung, falls es traegt [H]: eine Faustregel fuer das Labor. Die Strahlungsbreite faellt wie exp(-2,9 u). Ab
  Omega^2 ~ 0,96 liegt sie unter einer Gilbert-Daempfung von 1e-5, ab dort entscheidet die Materialdaempfung.
  - Haematit alpha ~ 1e-5 ist nur ein Zitat in Ovcharov, nicht an der Quelle gelesen.

## Ergebnis (Leitung, eingetragen 2026-10-01 19:16:08 CEST; Laeufe .69 cpu6 19:11:49 bis 19:15:00, beide rc = 0)

- **Fehlstart (Selbstanzeige):** Der erste Start um 19:11:10 brach beim Import ab, rc = 1, ohne Ergebnis. afm_kanal.py
  und nls2.py fehlten im Laufordner. Ich habe beide unveraendert aus RUNDE-12/afm-kanal2 kopiert (sha256 de6cd89f...
  und 3981995b..., gleich AFM-KANAL-2) und neu gestartet. Logs in lauf-69/log/fehlstart-1/ (auf der .69).
- **K1 bestanden:** kappa = -0,20, f = 0,8 gibt dieselben Nullstellen und Polbreiten wie AFM-KANAL-2, bitgleich
  (1,3943946666819864e-5; 6,609103005648792e-6; 2,6443357922933746e-6).
- Auswertung mit auswertung.jq (jq), Ergebnis in auswertung.jsonl:

| Mitglied | Omega^2 | Pole im Bereich | Gamma_med gemessen | Gesetz | Abweichung (Dekaden) |
|---|---|---|---|---|---|
| kappa -0,15, f 0,6 | 0,94 | 4 | 1,62e-4 | 1,09e-4 | +0,17 |
| kappa -0,15, f 0,733333 | 0,96 | 4 | 1,02e-5 | 7,9e-6 | +0,11 |
| kappa -0,15, f 0,833333 | 0,975 | 3 | 2,49e-7 | 1,79e-7 | +0,14 |
| kappa -0,15, f 0,9 | 0,985 | 2 | 1,82e-9 | 9,2e-10 | +0,29 |
| kappa -0,20, f 0,9125 | 0,9825 | 2 | 6,44e-9 | 5,2e-9 | +0,09 |

- Anstieg aus den vier Mitgliedern bei kappa = -0,15: c = 2,783 (Regel [2,4; 3,4]).
- **Ausgang nach der Regel: Gesetz traegt.** Alle fuenf neuen Mitglieder liegen hoechstens 0,29 Dekaden vom Gesetz
  entfernt (erlaubt 1,0), ueber 5 Dekaden in Gamma (1,6e-4 bis 1,8e-9).
- Vorab gegen Ausgang:
  - K1: getroffen.
  - "Gesetz traegt" (~70 %): getroffen.
  - "Lage 0,2 bis 0,6 Dekaden ueber dem Gesetz" bei kappa = -0,15: nur halb getroffen. Die Lage ist ueber dem Gesetz, aber
    drei von vier Werten liegen unter 0,2 (0,11 bis 0,29).
  - "c zwischen 2,6 und 3,1": getroffen (2,78).
- Bedeutung [H]:
  - Die Strahlungsbreite des dicken AFM-Balls ist ein Groessengesetz in u = 1/sqrt(1 - Omega^2), also im Abstand der
    Praezessionsfrequenz zur Luecke: Gamma ~ exp(2,55 - 2,86 u). Sie haengt kaum von kappa ab (-0,15 und -0,20; bei -0,10
    Faktor 3 bis 7 darueber, schon vorher gesehen).
  - Unter 1e-5 (in Einheiten der Luecke) faellt sie ab etwa Omega^2 = 0,96. Ab dort entscheidet die Materialdaempfung
    (Haematit alpha ~ 1e-5, nur Zitat).
  - Woher das Gesetz kommt (Tunneln oder Fourier-Unterdrueckung), ist nicht geprueft.
  - Das Gesetz ist an kappa = -0,20 angepasst. Getestet sind nur neue Mitglieder in diesem Bereich (Omega^2 0,94 bis
    0,985), kein Ausschluss stiller Stellen.
