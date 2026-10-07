# BAG-DIM: Plan (Code-Agent, Runde 24, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 00:32:46 CEST (date).
- Plan geschrieben ab 2026-10-03 00:55:03 CEST (date), nach den Rauchlaeufen R1 bis R3, vor jeder echten Rechnung.
- Karte: KARTE.md (unveraendert). Die Vorhersagen BD0 bis BD4 und ihre Bedeutung gelten wie dort. Dieser Plan legt nur
  Graphen, Raster, Starts, Laeufe und die mechanische Auswertung fest.
- Code: code/bagdim.py und code/auswertung.py; sha256 in Abschnitt 7 (lokal = .69).
- .69: /home/fmh/fmhc-physics-remote/runde24-bag-dim/ (code/, lauf/). Lokal nur Lesen, Schreiben, ssh, scp, rsync, jq.
- Zeitbox 120 min ab 00:32:46 CEST.

## 1. Modell und Verfahren (Code bagdim.py)

- Energie bei festem Q wie Karte und Auftrag:
  E = Q^2/(4 S) + f.L f + chi.L chi + Sum_i [(1/4)(chi_i^2 - 1)^2 + chi_i^2 f_i^2], S = Sum f_i^2, omega = Q/(2 S).
  L = Graph-Laplace mit Kantengewicht 1, Knotengewicht 1. Vakuum chi = 1 hat E = 0.
- Minimierung: L-BFGS-B (scipy 1.18.0, numpy 2.4.4 auf der .69), analytischer Gradient, maxcor 20, ftol 1e-16,
  gtol 1e-9 (skaliert), maxiter 20000. Feste Jacobi-Skalierung je Minimierung: f mit 1/sqrt(2 Grad + 2), chi mit
  1/sqrt(2 Grad + 2 f0^2 + 2) (f0 = Startfeld).
- **Konvergiert**, wenn max(|dE/df|, |dE/dchi|) <= 1e-5 max(1, max|f|) (unskaliert).
- **Beutel-Kennzahlen** je Loesung: Beutelknoten B = {chi < 0,5}, nB = |B|, Zusammenhangskomponenten von B, Rg (groesster
  Graphabstand von B zum Mittelknoten), Rs (groesster Startabstand: Gitter euklidisch, sonst Graphabstand), Reff
  (2D sqrt(nB/pi), 3D (3 nB/(4 pi))^(1/3), sonst Rg), Anteil von S in B, Lage des Maximums von |f|.
- **Kompakter Beutel am Mittelknoten** ("kompakt"): nB >= 1, B zusammenhaengend, Abstand Mittelknoten-B <= 2, Maximum
  von |f| hoechstens 3 Schritte vom Mittelknoten, mindestens 50 % von S in B, und **nicht fuellend**: nB <= N/4 und
  Rs + 10 <= d_rand (Graphabstand Mittelknoten zum naechsten Knoten mit kleinerem als dem Hoechstgrad: Gitterrand bzw.
  Sierpinski-Ecke; Zufallsgraph: unendlich).
- **Starts je Q** (Raster Q_k = Q0 r^k):
  - "fort": vorige gewaehlte Loesung, f mal sqrt(Q/Q_vorher) (nicht am ersten k eines Laufs)
  - "frisch": Beutel mit Radius R0 = max(2, a Q^b): chi = clip(tanh((d - R0)/2), 0, 1), f ~ cos(pi d/(2 R0)) innen,
    Normierung S = Q/(2 sqrt(mu)) mit dem Rayleigh-Quotienten mu des Startprofils; d = Startabstand
  - an "pruef-k": zusaetzlich frisch mit 1,5 R0 und R0/1,5
  - an "flach-k" (Zufallsgraph: immer): flacher Start, f^2 = Q/(2N) (1 + 1e-3 Rauschen, feste Saat), chi^2 = 1 - 2 f^2
  - Gewaehlt ("angenommen"): Gitter und Sierpinski: kleinste Energie unter den konvergierten kompakten Beuteln am
    Mittelknoten. Zufallsgraph: kleinste Energie unter allen konvergierten Starts. Die Fortsetzung laeuft nur von einer
    so gewaehlten Loesung weiter.
  - Die tiefste Loesung ueberhaupt wird je Q mitgeschrieben (Randbeutel, ganzer Graph im Beutelzustand,
    delokalisiert).
- **dE/dQ = omega** (Konsistenzprobe): an "dq-k" Minimierung bei Q (1 +- 1e-3), warm von der gewaehlten Loesung;
  rel = D/omega - 1 mit D = (E+ - E-)/(2e-3 Q).
- **Profil** (nur Gitter, an "profil-k"): chi und f entlang der +x-Achse vom Mittelknoten.

## 2. Rauchlaeufe (vor dem Einfrieren; alle Q-Raster und Graphgroessen kommen in keinem echten Lauf vor)

- **R1** (22:45:25 bis 22:46:00 UTC, Code bagdim.py.rauch1 9677c088...; lauf/rauch/): Spektren g2:41, g3:21, sg:6,
  zr:4000:6:7; Beutel g2:81, sg:7, g3:31, zr:2000:6:7.
  - Gesehen:
    - L-BFGS konvergiert in 40 bis 170 Iterationen auf max|grad| ~1e-8 bis 1e-6; dE/dQ = omega auf 5e-8 bis 8e-8
    - flache Starts landen auf Gitter und Sierpinski in einem **Randbeutel** (Gitterecke bzw. Sierpinski-Ecke) mit
      tieferer Energie als der Beutel am Mittelknoten
    - Zufallsgraph: auch der Beutelstart zerfliesst in einen delokalisierten Zustand (nB = 0, E ~ Q); ab Q ~ N/2 ist
      der ganze Graph im Beutelzustand (E = N/4)
    - Sierpinski: Beutel rasten auf Teildreieck-Vereinigungen ein (nB = 83 = zwei Stufe-3-Dreiecke, dann 245, ...);
      p_omega = Q omega/E schwankt stark
    - 2D: p_omega 0,686 bis 0,669 (Reff 4,7 bis 12); 3D: 0,773 bis 0,759 (Reff 4,7 bis 7,2)
    - Spektren: g2:41 1,81; g3:21 3,22; sg:6 1,363; zr:4000 kein Plateau; eigvalsh N = 4000 in 14 s
  - Fehler: Die Fortsetzung "fort" lief nie (Variable nie gesetzt).
- **Aenderungen nach R1** (vor dem Einfrieren):
  - Fortsetzung repariert
  - Wahlregel "zentral" (kleinste Energie unter kompakten Beuteln am Mittelknoten), weil Randbeutel tiefer liegen;
    der Zufallsgraph behaelt "alle"
  - Randabstand ueber den euklidischen Radius auf Gittern (der Graphabstand ist dort Manhattan, Diagonale sqrt2 zu
    streng)
  - Optionen --ohne-frisch, --flach-k, --pruef-k alle
- **R2** (22:48:50 bis ~22:53 UTC, Code bagdim.py.rauch2 5ac9e330...; lauf/rauch2/), Zeitmessung:
  - g3:81 bei Q = 2e5 und 2,6e5: 53 s je Start (136 Iterationen, Reff 20,1, p_omega 0,7509)
  - sg:9 bei Q = 5e4: vier Starts 103 s; frisch 1549 Iterationen. **Nebentaeler**: x1,5 und x0,667 enden 11 % bzw.
    19 % hoeher, flach im Beutelzustand des ganzen Graphen (E = N/4)
  - g2:181 bei Q = 1,5e5: Der ganze Graph im Beutelzustand (E = N/4 = 8190) liegt **tiefer** als der Beutel am
    Mittelknoten (8833); flacher Start 7037 Iterationen
  - zr:10000:6:7 Spektrum: eigvalsh 204 s, kein Plateau (Schwankung 0,58)
- **Folgen fuer die Groessen:**
  - 2D auf 241 x 241 vergroessert, damit nB <= N/4 bis Reff ~ 66 haelt
  - Flache Starts nur bei kleinem Q (Gitter und Sierpinski)
  - 3D ohne flachen Start; frische Starts dort nur am Laufanfang und an pruef-k
- **R3** (22:51:30 bis 22:52:42 UTC, Code bagdim.py.rauch3 = eingefrorener Code d6d42765..., auswertung.py.rauch3 =
  eingefrorene Auswertung 76e17980...; lauf/rauch3/): ganze Kette mit g2:81, g3:41, sg:7, zr:2000:6:7 und kleinen
  Spektren, dann die Auswertung. Sie lief fehlerfrei.
  - **Offengelegt (gesehen):**
    - sg:7 (Rg 4 bis 36): Zwei-Perioden-Sekante oben 0,577; Ein-Perioden-Sekanten 0,568 bis 0,583
    - g2:81 (Reff 4,7 bis 9,4): Halbdekaden-Sekante 0,674
    - g3:41 (Reff 4,8 bis 7,5): 0,762
    - zr:2000: 0,914 (delokalisiert)
    - Wandbreite 2D (10-90 %) 3,8 Schritte; dE/dQ auf 5e-8
  - Die Vorhersagen der Karte standen vorher fest und bleiben unveraendert. Die Auswerteregeln (Abschnitt 5) standen als
    Code (auswertung.py) fest, bevor R3 lief; R1 und R2 waren da gesehen.

## 3. Graphen und Raster (echte Laeufe)

| Graph | Code | N | Mittelknoten, d_rand | Raster Q_k = Q0 r^k | k | Startradius R0 = a Q^b |
|---|---|---|---|---|---|---|
| 2D-Gitter 241 x 241, offen | g2:241 | 58081 | (120,120), 120 | 100 x 10^(k/8) | 0..26 (100 bis 1,78e5) | a = 1,152, b = 1/3 (ideales Beutelgesetz) |
| 3D-Gitter 81^3, offen | g3:81 | 531441 | (40,40,40), 40 | 1000 x 10^(k/8) | 0..22 (1e3 bis 5,6e5) | a = 1, b = 1/4 |
| Sierpinski Stufe 9 | sg:9 | 29526 | Seitenmitte (256,0), 256 | 60 x (3 sqrt5)^(k/8), r = 1,268603140 | 0..34 (60 bis 1,94e5) | a = 1,4, b = 0,3642 |
| Zufall 6-regulaer, Saat 1 | zr:10000:6:1 | 10000 | Knoten 0, unendlich | 10 x 10^(k/8) | 0..24 (10 bis 1e4) | R0 = 2 fest |

- Sierpinski: Eine Periode ist Faktor 2 im Radius, also Faktor 3 sqrt5 = 6,708 in Q (Volumen mal 3, sqrt(lambda_1)
  durch sqrt5). Mit 8 Rasterschritten je Periode sind volle Perioden ganze Schrittzahlen.
- Der Mittelknoten des Sierpinski-Dreiecks ist der Seitenmittelpunkt, ein Eckpunkt des zentralen Lochs: Er liegt 256
  Schritte von zwei Ecken und 512 von der dritten entfernt.
- K0-Spektren:
  - g2:241 und g3:81: exakte Produktformel (Pfad-Eigenwerte 2 - 2 cos(pi k/n)), Bauprobe gegen eigvalsh von g2:12 und
    g3:8 aus demselben Code
  - Sierpinski: Stufe 8 (9843 Knoten), volles eigvalsh; Stufe 9 passt nicht in 4 GB
  - Zufallsgraph: zr:10000:6:1, volles eigvalsh
  - Plateau-Regel wortgleich zu URSUPPE-1

## 4. Laeufe (nur .69, kleintest.sh; Spuren cpu, cpu2, cpu3, cpu4, cpu6; je Aufruf --budget 560)

Gemeinsam: Standardwerte des eingefrorenen Codes (maxiter 20000, gtol 1e-9, gok 1e-5, dq-delta 1e-3).

| Lauf | Aufruf (Auszug) | Starts |
|---|---|---|
| S-g2 | spektrum g2:241 --klein 12 | |
| S-g3 | spektrum g3:81 --klein 8 | |
| S-sg | spektrum sg:8 | |
| S-zr | spektrum zr:10000:6:1 | |
| D2a / D2b | g2:241, k 0..15 / 16..26 | fort + frisch je k; pruef-k 0,8,16,24,26; flach-k 4,12; dq-k 8,16,24; profil-k 14,26 |
| D3a ... D3e | g3:81, k 0..6 / 7..11 / 12..15 / 16..19 / 20..22, --ohne-frisch | fort (frisch am Laufanfang); dq-k 8,16; profil-k 22 |
| D3p1 / D3p2 | g3:81, k = 10 / k = 21, pruef-k 10 / 21 | frisch, x1,5, x0,667 |
| SGa ... SGf | sg:9, k 0..13 / 14..20 / 21..25 / 26..29 / 30..32 / 33..34 | fort, frisch, x1,5, x0,667 bei jedem k (pruef-k alle); flach-k 8,16; dq-k 12,24,32 |
| Z | zr:10000:6:1, k 0..24, --wahl alle --flach-immer | fort, frisch, flach je k; pruef-k 8,16; dq-k 8,16 |

- Spurbelegung (je Spur nacheinander): cpu S-g2, S-g3, D3a, D3b, D3p1, SGf; cpu2 S-sg, D3c, SGa, SGe; cpu3 S-zr, D3d,
  SGb; cpu4 Z, D2a, D2b, D3p2; cpu6 D3e, SGc, SGd.
- **Restlaeufe:** Stoppt ein Lauf ueber das Budget (der Code bricht vor einem k ab, wenn verbraucht + 1,3 x letzter
  Punkt > 560 s), laeuft der Rest als neuer Lauf ab dem ersten fehlenden k mit sonst gleichen Argumenten. Bricht ein
  Lauf mit Fehler ab, wird er einmal unveraendert wiederholt. Beides wird offen vermerkt.
- Die Auswertung legt alle Starts eines Graphen je k aus allen Dateien zusammen.

## 5. Mechanische Auswertung (code/auswertung.py, laeuft auf der .69 ueber kleintest.sh)

- **Oertlicher Exponent:** p_FD = ln(E_k+1/E_k)/ln(Q_k+1/Q_k) zwischen Nachbarn; daneben p_omega = Q omega/E (gleich
  d ln E/d ln Q, wenn dE/dQ = omega). Gewertet wird nur mit Sekanten von E.
- **Beutelbereich** (Gitter, Sierpinski): laengste zusammenhaengende Folge von k mit gewaehltem kompakten Beutel (bei
  Gleichstand die obere). Berichtet: Spanne in Dekaden (Karte: mindestens 1,5) und Reff bzw. Rg an den Enden.
- **BD0:** Plateau (Regel URSUPPE-1: Fenster [t, 4t], kleinste relative Schwankung, P(t) > 2 c/N, t >= 0,5; Plateau,
  wenn Schwankung < 0,2).
  - Eingetroffen, wenn alle drei gelten:
    - Sierpinski (Stufe 8): Plateau und |d_s - 1,365| <= 0,08
    - g2:241: Plateau und |d_s - 2| <= 0,15
    - g3:81: Plateau und |d_s - 3| <= 0,15
  - Zufallsgraph nur berichtet.
- **BD1 / BD2:** p_end = Sekante ueber die obere halbe Dekade des Beutelbereichs, ln(E(k_o)/E(k_o - 4))/ln(10^0,5),
  k_o = oberstes k des Bereichs.
  - Eingetroffen, wenn |p_end - 2/3| <= 0,03 (2D) bzw. |p_end - 3/4| <= 0,03 (3D).
  - Offen, wenn der Bereich kuerzer als eine halbe Dekade ist.
- **BD3:** p_mittel = Sekante ueber zwei volle Perioden am oberen Ende des Beutelbereichs,
  ln(E(k_o)/E(k_o - 16))/ln(45).
  - Ist der Bereich kuerzer, gilt eine Periode (8 Schritte), markiert; unter einer Periode: offen.
  - Eingetroffen, wenn |p_mittel - 0,577| <= 0,03 und |p_mittel - 0,577| < |p_mittel - 0,613|.
  - Berichtet ohne Wertung: alle gleitenden Ein- und Zwei-Perioden-Sekanten im Bereich.
- **BD4:** Bereich = zusammenhaengende Folge ab dem kleinsten k, in der die gewaehlte Loesung nicht fuellend ist
  (nB <= N/4). p_end = Sekante ueber die obere halbe Dekade dieses Bereichs.
  - Eingetroffen, wenn p_end > 0,85.
  - Berichtet: ob es ueberhaupt einen kompakten Beutel gibt, und die Beutelstarts allein.
- **Kontrollen (Plan, nicht Karte):**
  - dE/dQ = omega: bestanden, wenn |rel| <= 1e-4 an allen dq-Punkten
  - Beutelbild 2D (K0 Teil 2), am groessten k mit Profil: bestanden, wenn chi(0) < 0,05 und die Wandbreite
    (chi 0,1 bis 0,9 entlang +x, linear interpoliert) <= 6 Gitterschritte
  - Bauproben der Graphen (Knotenzahl, Kanten, Grade; Produktformel gegen eigvalsh <= 1e-9)
  - Nebentaeler: Zahl der k, an denen ein anderer Beutelstart als fort/frisch tiefer lag, und groesste
    Energieabstaende der Starts
  - Randbeutel und Fuellzustand aus den flachen Starts, mit Energie gegen den zentralen Beutel
- Passt ein Ausgang nicht in die Bedeutungszeilen der Karte, wird er beschrieben, nicht umgedeutet.

## 6. Grenzen

- Keine Journaleintraege, keine Peerbus-Nachrichten, keine Aenderungen an Karten oder anderen Runden.
- Code und Plan nach dem Einfrieren unveraendert. Abweichungen offen mit Grund und Zeit.
- Prozesse nur per PID bzw. Unit; Skripte nie in place ueberschreiben (Upload unter neuem Namen, dann mv); Zeiten per
  date. Lokal kein Interpreter.

## 7. Pruefsummen beim Einfrieren

- code/bagdim.py: d6d4276511eae6d5ec99a1940cbef9a93a1d890223c362c1373ff2838c0fa53c (= .69 bagdim.py.rauch3)
- code/auswertung.py: 76e1798043e4f23c39e96daa4e3bb6da312e2c382f3b603ca77236d0682eee19 (= .69 auswertung.py.rauch3;
  in R3 einmal fehlerfrei an den Rauchdaten gelaufen)
- code/start_haupt.sh: e6802ca8d32a57fdb3c2a4901a7e0be4e9d795598e71098aee58060968f57643 (Startskript der Laeufe aus
  Abschnitt 4, lokal = .69, auf der .69 mit bash -n geprueft)
- code/bagdim.py.rauch1: 9677c088724061ae0f610b6b505cfcb2f29334b0a27ca7decbe3cba10c3de6a7 (Fassung von R1)
- .69 bagdim.py.rauch2: 5ac9e330cdd4c4da25b20544a8b313f5b996728b93ecee55e1582001f4e200a4 (Fassung von R2)
- Eingefroren 2026-10-03 00:56:57 CEST (date, unmittelbar vor dem Kopieren).
