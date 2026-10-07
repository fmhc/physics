# STILLE-GITTER-2: Plan (Code-Agent, Runde 24, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-02 23:49:02 CEST (date).
- Plan geschrieben ab 2026-10-03 00:09:19 CEST (date), nach den Rauchlaeufen R1 bis R3, vor jeder echten Rechnung.
- Karte: KARTE.md (unveraendert). Die Vorhersagen TG0 bis TG3 und ihre Bedeutung gelten wie dort. Dieser Plan legt nur
  Laeufe, Verfahren und die mechanische Auswertung fest.
- Code: code/stille_gitter2.py und code/auswertung2.py; sha256 siehe Abschnitt 7 (lokal = .69).
- .69: /home/fmh/fmhc-physics-remote/runde24-stille-gitter-2/ (Code, lauf/). Lokal nur Lesen, Schreiben, ssh, scp, rsync, jq.
- Zeitbox 120 min ab 23:49:02 CEST.

## 1. Schreibtisch: Pruefung des Karten-Arguments

- **Symbol des 7-Punkt-Sterns** (h = Nachbarabstand, e_1, e_2, e_3 die Gitterrichtungen 0, 60, 120 Grad):
  - (4/(3h^2)) Summe_m (cos(h k.e_m) - 1) mit Summe_m cos^2 = 3/2, Summe_m cos^4 = 9/8,
    Summe_m cos^6 = (30 + 3 cos 6theta)/32.
  - Ergebnis: -k^2 + h^2 k^4/16 - h^4 k^6 (1/576 + cos 6theta/5760) + O(h^6). **Stimmt mit der Karte.**
- **Isotroper Teil wie Stern A:** Der 5-Punkt-Stern hat isotrop h^2 k^4/16 - h^4 k^6/576 (aus (kx^4 + ky^4) und
  (kx^6 + ky^6) = k^6 (5 + 3 cos 4theta)/8).
  - Das ist bis h^4 derselbe isotrope Teil wie beim Dreiecksgitter.
  - [H] Darum sollten Sprossenlage und Re rho des Dreiecksgitters nahe bei Stern A liegen; Abweichungen kommen erst aus
    der Anisotropie von A in zweiter Ordnung (h^4).
  - Der Rauchlauf zeigt bei h = 0,45 einen Abstand von 6,6e-6 (Abschnitt 2). Startwerte unten nutzen das.
- **Fernfeld:** Die anisotrope Dispersion ist dk(theta) ~ (h^4 K^5/11520) cos 6theta ~ 3,1e-3 h^4 cos 6theta (K = 2,05).
  - Phase auf dem Messkreis r = 20: ~0,063 h^4, bei h = 0,5 also 3,9e-3 rad. Der l = 0-Scheinanteil (~beta^2/2) bleibt
    unter 1e-5.
  - Bei Stern A war es 0,0905 h^2 r (RUNDE-23). TG2 ist darum auf dem Dreiecksgitter fast frei von diesem Messartefakt.
- **Symmetrie:** A1 von C6v enthaelt cos(6 m theta), also l = 0, 6, 12, ... Grundgebiet 0 <= j <= i (0 bis 30 Grad).
- **Schaetzung (Karte, [H]):** Anisotropie-Amplitude 1/5760 gegen 1/1440 (Stern B). Gilt die Regel aus RUNDE-23 (Breite
  = Quadrat des anisotropen Symbols bei K), dann Gamma_tri ~ Gamma_B/16. Die Vorhersagen bleiben wie in der Karte.

## 2. Randmethode und Rauchlaeufe (vor dem Einfrieren; h = 0,45, 0,22, 0,21 kommen in keinem echten Lauf vor)

- **Randmethode:** radiale PML durch komplexe Streckung der Knotenkoordinaten, x~ = x r~(r)/r mit
  r~ = r + i sig0 Lpml/(p+1) ((r - Lin)/Lpml)^(p+1) fuer r > Lin, eingesetzt in die P1-FEM-(Kotangens-)Form des Sterns mit
  konzentrierter Masse (Dreiecksflaechen und Kantenvektoren komplex).
  - Ungestreckt ist das exakt der jeweilige Stern: Dreiecksgitter = alle gleichseitigen Dreiecke; Stern A = beide
    Diagonal-Zerlegungen jeder Quadratzelle (Gewicht 1/2); Stern B = (2/3) A + (1/3) Diagonal-Teilgitter (Rauten).
  - Fuer alle drei Sterne derselbe Code und dieselbe Streckung; Gebiet Kreisscheibe r <= Lin + Lpml.
- **R1** (22:00:43 bis 22:01:50 UTC, lauf/rauch/, Code 55fbee1a..., PML 24/16/1,5/2 = Werte von RUNDE-23 P1 in radialer
  Form; P2 24/22/3/3):
  - Quadrat A 0,45: Gamma_fit 1,29816e-4 gegen RUNDE-23 (Rauch R2) 1,29826e-4 (-7e-5 relativ)
  - Quadrat B 0,45: 1,28079e-7 gegen 1,28184e-7 (-8e-4); P2 1,28163e-7
  - Dreieck 0,45: 7,2319e-9, P2 7,2825e-9 (7e-3 relativ auseinander)
  - Dreieck 0,22 nur Stufe 1 (4 bis 6 s je Punkt) und ein P2-Punkt (7,5 s)
- **R2** (22:03:37 bis ~22:06 UTC, lauf/rauch2/): PML-Diagnose bei h = 0,45, je zehn Einstellungen am Dreiecks-Minimum, an
  einem Dreieckspunkt neben dem Minimum (l = 0, Gamma 4,5e-6) und am Minimum von Stern B.
  - Am Minimum fehlen mit Lin = 24 absolut ~5e-11 (Dreieck) bzw. ~1e-10 (B); neben dem Minimum (l = 0) ~1e-4 relativ.
  - Der Fehler faellt mit glatterem Einsatz (p = 3), groesserem Lpml und stark mit groesserem Lin:
    - Lin 30, 22/3/3: 7,29005e-9
    - Lin 24, 40/2/3: 7,28921e-9
    - Lin 24, 16/1,5/2: 7,23125e-9
  - [H] Lesart: Gitterfehler am komplex gestreckten, abklingenden Schwanz des geschlossenen Kanals u (kappa = 0,56;
    Amplitude ~1e-3 bei r = 24, ~3e-5 bei r = 30). Er ist absolut und haette bei kleinem h den Boden bestimmt.
  - **Aenderung vor dem Einfrieren:** P1 = Lin 30, Lpml 22, sig0 3, p 3 (Rand bei 52); P2 = Lin 34, Lpml 26, sig0 2,
    p 3 (Rand bei 60). P2 aendert Einsatzort und Profil zugleich. Code 70b81d84... (nur Standardwerte und --lin2).
- **R3** (ab 22:07:21 UTC, lauf/rauch3/, Code 70b81d84..., P1/P2 wie oben):
  - Dreieck 0,45: Gamma_fit 7,29076e-9, direkt 7,290053e-9, P2 7,29003e-9 (2e-14 auseinander)
  - Quadrat A 0,45: 1,298285e-4 gegen RUNDE-23 1,298259e-4 (+2,0e-5)
  - Quadrat B 0,45: 1,281885e-7 gegen 1,281843e-7 (+3,3e-5); direkt, DOPPEL und P2 innerhalb 1e-15
  - Dreieck 0,21 (22:07:21 bis 22:11:18 UTC, 236 s fuer 18 Punkte und P2; 11 bis 15 s je Punkt, N = 18729):
    - Gamma_fit 1,2932e-11 (sigma 1,6e-13), direkt 1,28404e-11, DOPPEL 1,28402e-11, P2 1,28431e-11; Boden ~2,9e-15
    - Fit und direkte Rechnung liegen 0,7 % auseinander, innerhalb der Fit-Unsicherheit (wie B015 in RUNDE-23)
    - Lage 0,5294226, Re rho 1,5566865; F6-Anteil am Minimum 1,000
  - Offengelegt: Mit T045 ergibt das einen oertlichen Exponenten von ~8,3 zwischen h = 0,45 und 0,21. Die Vorhersagen
    standen vorher fest. Die Regeln in Abschnitt 5 standen vor dem Ergebnis von T021 im Entwurf (ab 00:09:19 CEST);
    danach geaendert wurden nur dieser Absatz, die Zeile zu T021 und der Wegfall von h = 0,15 (Zeitgrund, Abschnitt 4).
- **Offengelegt:** Die Rauchlaeufe zeigen die Groessenordnung bei h = 0,45 (und 0,21). Die Vorhersagen der Karte standen
  vorher fest und werden nicht angepasst. Die PML-Wahl folgt aus dem Abstand P1/P2 und dem Vergleich mit RUNDE-23, nicht
  aus der Hoehe der Dreiecksbreite.

## 3. Verfahren (Code stille_gitter2.py, eingefroren)

- **Gitter:** Knoten (i + j/2, j sqrt3/2) h (Dreieck) bzw. (i, j) h (Quadrat), Kreisscheibe r <= Lin + Lpml, Dirichlet
  ausserhalb.
  - Keilreduktion R L P wie RUNDE-23: C6v mit 0 <= j <= i (1/12), C4v mit 0 <= b <= a (1/8).
  - Exakt, weil Streckung und Dreieckslisten unter der Gruppe invariant sind.
- **Q-Ball:** Newton mit dem ungestreckten Stern; Start radiales Profil, danach Warmstart; max|F| < 1e-11 oder
  Rundungsboden.
- **Linearisierung:** u (geschlossen), v (offen), V1 = U' + U'' f^2, W = U'' f^2 am Knoten.
  - PML P1: Lin 30, Lpml 22, sig0 3, p 3
  - PML P2 (Probe): Lin 34, Lpml 26, sig0 2, p 3
- **Eigenwert:** wie RUNDE-23.
  - Shift-Invert-Arnoldi (tol 1e-13) auf der linearen Einbettung
  - Auswahl l0-Anteil >= 0,5 (Kreise 0,4 R und 0,7 R), naechster an der Vorhersage
  - zweiseitiges Rayleigh-Funktional mit Rechts- und Linksvektor
  - Gamma = -Im rho
- **Suche je (Gitter, Stern, h)** wie RUNDE-23: S1 5 Punkte im Abstand 1e-4 (Randerweiterung hoechstens 6-mal), S2 5
  Punkte im Abstand 4e-5, S3 mit d3 = 1,2 sqrt(Gmin2/a2) in [1e-7; 2e-5], hoechstens eine zweite S3-Runde; MIN = direkte
  Rechnung beim Scheitel; DOPPEL = MIN mit Shift +2e-3; P2 beim Scheitel mit neuem Q-Ball.
- **Rechenboden:** Boden = |Gamma_MIN - Gamma_DOPPEL| + |Gamma_MIN - Gamma_P2|.
  - Ueber dem Rechenboden heisst Gamma_min(Fit) > 0 und Gamma_min >= 10 Boden.
- **Fernfeld:** offener Kanal v am MIN-Punkt, Kreise r_c1 = 20 (gewertet) und r_c2 = 22,5 (Kontrolle).
  - 512 Winkel, kubische B-Splines in den Indexkoordinaten (j, i) des Gitters (beim Dreieck schiefwinklig).
  - Koeffizienten a_j von cos(6 j theta), j = 0 bis 4 (Dreieck), bzw. cos(4 j theta), j = 0 bis 6 (Quadrat).
  - Fluss F_j = N_j r Im(conj(a_j) da_j/dr), N_0 = 2 pi, N_j = pi, dr = 0,25. Anteil l = 6: F_1 / Summe F_j.

## 4. Laeufe (nur .69, kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4, cpu6; je Aufruf --budget 560)

Gemeinsam: `stille_gitter2.py --modus scan --n1 5 --d1 1e-4 --d2 4e-5 --d3max 2e-5 --d3min 1e-7`, PML P1 und P2 wie oben
(Standardwerte des eingefrorenen Codes).

**Schritt 1, K0 (Pflicht, vor jeder Dreiecksrechnung):**

| Lauf | Gitter | Stern | h | x0 | rho0 | Spur |
|---|---|---|---|---|---|---|
| K0A | sq | A | 0,3 | 0,5295910 | 1,556934 | cpu |
| K0B | sq | B | 0,3 | 0,5297012 | 1,557091 | cpu2 |

- x0 und rho0 sind die Minima von RUNDE-23. Die Suche (S1 +-2e-4) prueft die Lage trotzdem neu.
- Faellt K0 durch, folgt keine Dreiecksrechnung mit dieser Randmethode. Der Befund wird dokumentiert; jede Aenderung
  danach waere eine offene Abweichung.

**Schritt 2, Dreiecksgitter (erst nach bestandenem K0):**

| Lauf | h | x0 | rho0 | Spur |
|---|---|---|---|---|
| T050 | 0,5 | 0,5302202 | 1,557865 | cpu |
| T040 | 0,4 | 0,5298558 | 1,557327 | cpu2 |
| T030 | 0,3 | 0,5295897 | 1,556934 | cpu3 |
| T025 | 0,25 | 0,5294890 | 1,556786 | cpu4 |
| T020 | 0,2 | 0,5294079 | 1,556666 | cpu6 |

- Startwerte: x0 = x*_A(h) aus RUNDE-23 minus 6,6e-6 (h/0,45)^4 (Abstand Dreieck gegen A im Rauchlauf, h^4-Skalierung
  nach Abschnitt 1); rho0 = Re rho_A(h) aus RUNDE-23.
- **h = 0,15 entfaellt** (nicht in der Karte): Bei h = 0,21 dauert ein Punkt 12 bis 15 s (N = 18729). Bei h = 0,15 waere
  N ~ 37000, geschaetzt ~35 s je Punkt; schon 15 Punkte ohne P2 lagen damit ueber 10 min.
- Bricht ein Lauf ab (Zeit oder Fehler), wird er einmal mit unveraenderten Argumenten wiederholt und das offen vermerkt.
  Fehlen dann DOPPEL oder P2, folgen getrennte Rechnungen im Modus punkt bei x* (`--punkt-sigoff 2e-3` bzw. mit
  `--lin 34 --lpml 26 --sig0 2 --pexp 3`). Fehlt dann noch etwas, bleibt der Punkt offen.

## 5. Mechanische Auswertung (Skript code/auswertung2.py, laeuft auf der .69)

- **K0:** Quadratgitter A und B bei h = 0,3, Gamma_min (Fit) gegen RUNDE-23: 2,3375e-5 (A) und 3,9974e-9 (B).
  - **Bestanden**, wenn fuer beide |Gamma/Ref - 1| <= 0,05.
- **TG0** (Dreieck, die fuenf Karten-h):
  - q aus dem nichtlinearen Fit omega_r^2(h) = w0 + c h^q ueber alle fuenf h
  - w0' aus dem linearen Fit omega_r^2 = w0' + c' h^2 ueber h <= 0,3 (0,3; 0,25; 0,2)
  - **Eingetroffen**, wenn |q - 2| <= 0,4 und |w0' - 0,529266| <= 3e-5.
- **TG1:** p = Steigung der Ausgleichsgeraden log Gamma_min gegen log h ueber alle Karten-h ueber dem Rechenboden;
  Unsicherheit = Standardfehler.
  - **Eingetroffen**, wenn mindestens 3 h ueber dem Rechenboden liegen und 6,5 <= p <= 9,5 (Punktschaetzer).
- **TG2:** F6-Anteil (r_c1 = 20) am MIN-Punkt fuer alle Karten-h <= 0,4 (0,4; 0,3; 0,25; 0,2), nach dem Wortlaut der
  Karte unabhaengig vom Rechenboden.
  - **Eingetroffen**, wenn alle >= 0,80.
  - **Nicht eingetroffen**, wenn einer < 0,80 ist (mit Angabe der h).
  - **Offen**, wenn ein h fehlt und keiner unter 0,80 liegt.
- **TG3:** Gamma_min(Dreieck, h = 0,3). Liegt er unter dem Rechenboden, gilt max(Gamma_min, 10 Boden).
  - **Eingetroffen**, wenn < 4,0e-9.
- Zusaetzlich berichtet, ohne Wertung:
  - oertliche Exponenten zwischen Nachbar-h
  - F0- und F12-Anteile, Kontrollkreis r_c2
  - Wandradius Achse gegen 30 Grad
  - Verhaeltnisse Gamma_B/Gamma_tri und Gamma_A/Gamma_tri je h (Werte aus RUNDE-23)
  - Re rho, Kruemmung a, h = 0,15 falls gerechnet
- Passt ein Ausgang nicht in die Bedeutungszeilen der Karte, wird er beschrieben, nicht umgedeutet.

## 6. Grenzen

- Keine Journaleintraege, keine Peerbus-Nachrichten, keine Aenderungen an Karten oder anderen Runden.
- Code und Plan nach dem Einfrieren unveraendert. Abweichungen werden offen mit Grund und Zeit notiert.
- Prozesse nur per PID bzw. Unit, Skripte nie in place ueberschreiben (Upload als .neu, dann mv), Zeiten per date.

## 7. Pruefsummen beim Einfrieren

- code/stille_gitter2.py: 70b81d84e24af9a747854e1db9d862ded72c36a925e1b8eb1aca174e3d6f05e7 (lokal = .69)
- code/auswertung2.py: 3e487ed48ef2d6f997dd510f71685c29c164e284fe73b9017e680865628398a1 (lokal = .69; an den
  Rauchdaten lauf/rauch3 einmal fehlerfrei gelaufen, 22:10:28 UTC)
- code/stille_gitter2.py.rauch1: 55fbee1ae7e856ef7995a182ae2d62a7cbdc452ef2861be128a4b03039c82134 (Fassung von R1/R2)
- Eingefroren 2026-10-03 00:11:56 CEST (date, unmittelbar vor dem Kopieren).
