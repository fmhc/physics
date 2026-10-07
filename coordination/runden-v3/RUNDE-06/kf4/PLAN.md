
Bearbeiter: Agent KF-4 (Anthropic, Opus). Auftrag: ../AUFTRAG-KF4-KF5.md (gemeinsamer Rahmen, Abschnitt "Agent KF-4"),
Karte KF-4 in ../../REVIEW-FABLE-20260930/KARTEN-FABLE.md (Z. 85 bis 111). Beginn 2026-09-30 02:40:20 CEST
(gemessen), Ende in der letzten Zeile. Explorativ. Code: kf4.py, Version v1, **ungetestet**.

## Kein lokaler Probelauf

Die Leitung schrieb um 02:42, Finn habe lokale CPU-Rauchtests erlaubt. Ich habe keinen gestartet: CLAUDE.md verbietet
lokale Interpreterstarts, und eine weitergeleitete Freigabe ersetzt Finns eigene Zustimmung nicht (so auch R5-C,
RUNDE-05/r5c/PLAN.md). Stattdessen:
- statisch geprueft: Tensorformen in `entwickeln` (B x N, Halbpunkte B x (N-1), Spalten B x 1), `messen` (B x 8),
  Auswertung (M x 8 je Lauf, Lock-in M x 7), Klammerbilanz, Anfuehrungszeichen in f-Strings;
- **Schritt 1 unten ist der Rauchtest auf der .69** (cpu-Spur, etwa 1 min), danach derselbe auf p4000a. Beide geben
  am Ende eine Hochrechnung fuer alle Unterbefehle aus (gemessene Punkt-Schritte je Sekunde).

## Aufbau

- **Modell wie QG-1:** L = A|psi_t|^2 - B|psi_x|^2 - C U(S), A, B, C = 1 + (a, b, c) Phi.
  - Variante C (volle Metrik): (-2, 2, 0).
  - "0": kein Feld (Kontrolle).
- **Feld:** c(x) = 1 + 2 Phi, Phi = (g/2) r(t) sin(2 pi x / lambda), g = 2e-3 (Karte). Fuer die Kontrolle "gleich":
  Phi = -g/2 ueberall.
- **Zeitplan r(t):** 40 feldfrei, 80 sin^2-Rampe hoch, Halten, 80 cos^2-Rampe runter, danach frei (200; resonanz 400).
  - Halten = 20 Gitterperioden (20 lambda / v; Karte), resonanz fest 600, statik 300.
  - Die Rampen verhindern Einschalt-Stoesse. Sie erlauben es, die Anregung **nach** dem Abschalten im feldfreien Raum zu
    messen (eichfrei).
- **Bewegungsgleichung:** A psi_tt = d_x(B psi_x) - C U'(S) psi - A_t psi_t. Der Term A_t kommt aus der Rampe und wirkt
  nur in C; ohne ihn waere die Gleichung nicht die Euler-Lagrange-Gleichung.
- **Numerik wie QG-1:**
  - Integrator: Velocity-Verlet.
  - Gitter: dx/dt = 0,1/0,05 (grob) und 0,05/0,025 (fein).
  - Rand: Dirichlet mit Daempfungsschicht (40 breit, sigma0 = 1).
  - float64 bzw. complex128, alle Laeufe als ein Stapel.
- **Ball:** omega^2 = 0,7 aus dem analytischen 1D-Anker (QG-1: Schuss gegen Anker 1,2e-10); f' in geschlossener Form.
  - Lorentz-Boost wie tests1d.py: psi = f(gamma(x - x0)) e^{i omega gamma v (x - x0)}.
  - Bewegte Baelle starten bei x0 = -v t_ende/2; die Box waechst mit (L = groesste Auslenkung + 100).
- **Antrieb im Ruhesystem:** Omega = gamma k v. Kante 1 - omega = 0,1633, innere Resonanz 1,4937 (RUNDE-02.md: Codex-Pol
  1,49378, Anthropic fein 1,4937).
- **Messung alle 0,25:**
  - Ladungsschwerpunkt X
  - Ladung im Fenster (+-40), im Kern (+-15) und in der Box
  - Ladungsbreite
  - **S_max**: Spitzendichte, parabolisch zwischen den Gitterpunkten
  - Phase an der Spitze
  - flache Energie im Fenster
- **Auswertung je Lauf (Haltefenster, ab 20 nach der Rampe):**
  - Lock-in gegen die Gitterphase phi = k X_poly(t): Polynom 2. Grades plus cos/sin von phi und 2 phi.
  - **R_mess** = a1 (k v)^2 / (g k/2) aus dem cos-Anteil der Schwerpunktschwingung (mit Vorzeichen);
    a_com = (k v)^2 |dX| ist die Schwerpunktbeschleunigung.
  - **D1** = Amplitude von S_max bei phi, relativ ("Dehnung").
    - S_max ist ein Lorentz-Skalar. Damit faellt die Scheinschwingung der Laenge durch die Kontraktion weg, ebenso die
      Koordinatenstreckung in C.
    - Die Breite im Ruhesystem (W1) wird nur nebenbei berichtet.
  - **Gamma = D1 / a_com**: Dehnung je Schwerpunktbeschleunigung. So vergleicht der Code A und C "bei gleicher
    Schwerpunktbeschleunigung", siehe Abweichung 1.
  - Ladungsverlust aus dem Kern (dQ_kern), mittlere Bremsung.
  - **Nachschwingen** nach dem Abschalten: Hann-DFT von S_max im Band 0,95 bis 1,05 x 1,4937/gamma (ring_res,
    Frequenz ins Ruhesystem umgerechnet) und im Kantenband (ring_kante).
  - Ruhende Baelle: dS/S (Halten gegen Vorphase), Drehfrequenz aus der entfalteten Phase (domega/omega), Breite.
- **Vorhersage im Code (R_starr):** starrer, geboosteter Ball im Gitter.
  - R_starr = (J - v dJ/dv)/(M gamma^3), J(k, v) = Int cos(k y) j(y; v) dy.
  - j ist die Kopplungsdichte des bewegten Balls: -a|psi_t|^2 + b|psi_x|^2 + c U.
  - Bei k = 0, v = 0 kommt QG-1 heraus (A 0,2227, C 1); der Bericht druckt das als Anker.
- **Rohdaten** jeder Stufe werden sofort gesichert (kf4_roh_grob.pt, kf4_roh_fein.pt). `--roh ORDNER` wertet nur neu
  aus. `--stufe grob|fein` rechnet eine Stufe allein.

### Unterbefehle

| Unterbefehl | Laeufe | Inhalt |
|---|---|---|
| rauch | 14 | alle Codepfade mit kurzen Zeiten (Halten 20): bewegt A/C/0 und 2g, ruhend periodisch und gleich, 5 Resonanzpunkte |
| statik | 13 | v = 0, Ball im Minimum von Phi: lambda 4, 8, 16 und gleichfoermig (A, C); 2g bei 4 und gleich; Kontrolle g = 0 |
| scan-langsam | 25 | (lambda, v) = (4; 0,1), (4; 0,2), (8; 0,1), (8; 0,2), (16; 0,2); je A, C mit g und 2g, Kontrolle g = 0 |
| scan-schnell | 40 | lambda 4 und 8, v = 0,3 / 0,45 / 0,6 / 0,75; je A, C mit g und 2g, Kontrolle |
| resonanz | 37 | lambda 4; Omega = 1,30 / 1,40 / 1,44 / 1,46 / 1,47 / 1,48 / 1,485 / 1,49 / 1,494 / 1,498 / 1,503 / 1,51 / 1,52 / 1,54 / 1,58 / 1,70 (v = 0,637 bis 0,734); A und C; 2g bei 1,494; Kontrollen bei 1,30 / 1,494 / 1,70 |
| kante | 23 | lambda 8; Omega = 0,14 / 0,155 / 0,165 / 0,17 / 0,175 / 0,185 / 0,20 / 0,23 / 0,28 / 0,35 (v = 0,175 bis 0,407); A und C; Kontrollen bei 0,14 / 0,20 / 0,35 |

Omega der Karte fuer den Scan (gamma k v): lambda 4: 0,158 / 0,321 / 0,494 / 0,792 / 1,178 / 1,781; lambda 8: 0,079 /
0,160 / 0,247 / 0,396 / 0,589 / 0,891; lambda 16, v 0,2: 0,080.

## Aufrufe (Remote-Ordner /home/fmh/fmhc-physics-remote/runde6-kf4/, kf4.py dorthin kopieren)

Reihenfolge wie unten. Jeder Aufruf rechnet grob und fein (L3) und schreibt `kf4_<unterbefehl>_bericht.txt`,
`kf4_<unterbefehl>_ergebnis.json` und die Rohdaten in den Ausgabeordner.

```
cd /home/fmh/fmhc-physics-remote/runde6-kf4 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu kf4-rauch-cpu kf4.py rauch --geraet cpu --out /home/fmh/fmhc-physics-remote/runde6-kf4/rauch-cpu
cd /home/fmh/fmhc-physics-remote/runde6-kf4 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf4-rauch-gpu kf4.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-kf4/rauch-gpu
cd /home/fmh/fmhc-physics-remote/runde6-kf4 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf4-statik kf4.py statik --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-kf4/statik
cd /home/fmh/fmhc-physics-remote/runde6-kf4 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf4-scan-langsam kf4.py scan-langsam --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-kf4/scan-langsam
cd /home/fmh/fmhc-physics-remote/runde6-kf4 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf4-scan-schnell kf4.py scan-schnell --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-kf4/scan-schnell
cd /home/fmh/fmhc-physics-remote/runde6-kf4 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf4-resonanz kf4.py resonanz --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-kf4/resonanz
cd /home/fmh/fmhc-physics-remote/runde6-kf4 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf4-kante kf4.py kante --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-kf4/kante
```

- **Ausweg, falls ein Aufruf nach dem GPU-Rauchtest ueber 8 min geschaetzt wird**, als Beispiel resonanz: zwei Aufrufe
  mit `--stufe grob` bzw. `--stufe fein` und **demselben** `--out`. Danach wertet derselbe Befehl auf der cpu-Spur mit
  `--geraet cpu --roh /home/fmh/fmhc-physics-remote/runde6-kf4/resonanz` beide Stufen gemeinsam aus (Sekunden).
- Die Spur p4000b (zweite P4000) geht genauso, solange WM-1-MB nicht laeuft.

## Laufzeiten (Papierschaetzung, nicht gemessen)

Grundlage:
- Kosten = Laeufe x Gitterpunkte x Zeitschritte, grob plus fein.
- Fuer die P4000 bei grossen Stapeln angenommen: etwa 2e8 Punkt-Schritte/s. Das entspricht etwa 25 elementweisen
  complex128-Operationen je Schritt bei 243 GB/s.
- Messung alle 0,25 kostet etwa 20 Prozent mehr.
- CPU mit einem Kern: etwa 5e6 Punkt-Schritte/s.
- Der Rauchtest misst beides und druckt die Hochrechnung; bitte die gemessenen Zahlen hier nachtragen.

| Aufruf | Box L | t_ende | Punkt-Schritte | Schaetzung P4000 | Schaetzung CPU-Kern |
|---|---|---|---|---|---|
| rauch | 123 | 65 | 2,2e8 | unter 0,5 min (startlastig) | etwa 1 min |
| statik | 112 | 700 | 2,0e9 | etwa 0,5 bis 1 min (startlastig) | 7 bis 8 min, zu knapp, daher p4000a |
| scan-langsam | 300 | 2000 | 3,0e10 | etwa 3 min | nein |
| scan-schnell | 450 | 933 | 3,4e10 | etwa 3 bis 4 min | nein |
| resonanz | 541 | 1200 | 4,8e10 | etwa 4 bis 5 min | nein |
| kante | 367 | 1312 | 2,2e10 | etwa 2 min | nein |

- Speicher auf der GPU unter 0,3 GB; der groesste Stapel ist resonanz fein mit 37 x 21629 complex128.
- Die Grenze der Spur (RuntimeMaxSec 600) haelt jeder Aufruf mit Faktor 2 Abstand ein. Ausnahme ist resonanz: Ist die
  P4000 halb so schnell wie angenommen, wird es knapp; dann den Ausweg mit `--stufe` nehmen.

## Vorhersagen vor dem Rechnen

Kennzeichen: [S] eigene Papierrechnung, [L] Literatur aus dem Gedaechtnis, [A] Projektdatei.

- **P0 Anker (Code):** R_starr(k = 0, v = 0) = 0,2227 (A) und 1,0000 (C), wie QG-1 [A].
- **P1 gleichfoermiges c = 1 - g** (statik "gleich", Phi0 = -1e-3) [S]:
  - Herleitung A: B = 1 + 4 Phi0 ist eine Umskalierung x = sqrt(1 + 4 Phi0) y. Bei fester Ladung sitzt der Ball
    danach als Ball mit Q_y = Q (1 - 2 Phi0) auf der 1D-Familie.
    - dS/dQ = 0,26827, aus S_max = 1 - b0 und Q = 2 sqrt(2) omega arcosh(1/b0).
    - dQ/domega^2 = -5,8937.
  - A: dS/S = -3,564 Phi0 = **+3,564e-3**, domega/omega = 0,5918 Phi0 = **-5,92e-4**, je +-3 Prozent. Bei 2g doppelt.
  - C: dS/S = **0** (Betrag unter 1e-4). domega/omega = Phi0 = **-1,000e-3**: Rotverschiebung, fuer jeden Ball gleich.
  - Scheitert, wenn A ausserhalb von 3 Prozent liegt oder C sich staerker als 1e-4 verformt.
  - Bedeutung: In A haengt die innere Uhr des Balls vom Ort und von seiner Zusammensetzung ab (0,59 statt 1). Das ist
    eine Verletzung der lokalen Positionsinvarianz, die Schwester der Universalitaetsverletzung aus QG-1.
- **P2 ruhend im periodischen Feld** (Ball im Minimum, Phi = -g/2, Phi'' = +(g/2) k^2) [S]:
  - C spuert nur die Kruemmung: D_C ~ k^2, also D_C(8)/D_C(16) zwischen 2,8 und 5,2. D_C geht mit lambda gegen null
    (passt zu P1).
  - A = Monopol plus Gezeitenteil: D_A(16) innerhalb 10 Prozent von +3,564e-3. Der Gezeitenteil D_A - D_A(gleich)
    skaliert wie k^2 (dasselbe Band).
  - Kein Vorzeichen fuer die Gezeitenteile vorhergesagt.
  - **P2b** (Handvergleich zweier Berichte): D1_C bewegt bei (8; 0,1) und (16; 0,2) innerhalb eines Faktors 1,5 von
    |D_C statik| bei 8 bzw. 16. In 1+1 Dimensionen ist die Kruemmung ein Skalar, also unabhaengig von v.
- **P3 Schwerpunkt, lambda -> unendlich** [S]:
  - A: R(v) = R0 - (2 + R0) v^2. C: R(v) = 1 - 3 v^2 (PPN gamma = 1, isotrope Koordinaten [L]).
  - Punktgrenze fuer v = 0,1 / 0,2 / 0,3 / 0,45 / 0,6 / 0,75:
    - A: 0,2005 / 0,1338 / 0,0227 / -0,2274 / -0,5775 / -1,0276
    - C: 0,970 / 0,880 / 0,730 / 0,393 / -0,080 / -0,688
  - Nullstellen: A bei v = 0,317, C bei v = 0,577. Der Code rechnet mit Formfaktor (R_starr).
  - P3a: Das Vorzeichen von R_mess stimmt mit R_starr ueberein, wo |R_starr| > 0,1.
  - P3b: |R_mess/R_starr - 1| <= 0,2 fuer Omega < 0,5.
  - Scheitert bei Vorzeichenfehlern oder mehr als 20 Prozent Abweichung auf beiden Gittern.
- **P4 Kernfrage 1, Dehnung bei gleicher Schwerpunktbeschleunigung** [S, Hypothese]:
  - A traegt den Monopol aus P1: S_max folgt dem oertlichen Phi mit 3,56e-3 je g/2, unabhaengig von v.
  - C traegt nur die Kruemmung, ~ (g/2) k^2.
  - Daher Gamma_A/Gamma_C > 3 an allen Punkten unter der Kante: (4; 0,1), (8; 0,1), (8; 0,2), (16; 0,2).
  - Von (8; 0,1) nach (16; 0,2) (gleiches Omega 0,08) waechst Gamma_A/Gamma_C um etwa Faktor 5 (2,5 bis 10).
  - D1_A bei (16; 0,2) zwischen 2,1e-3 und 5,0e-3.
  - Nahe v = 0,32 geht a_com in A gegen null bei endlicher Dehnung: Gamma_A divergiert. Das ist die schaerfste
    Trennung.
  - Scheitert, wenn Gamma_A/Gamma_C unter der Kante auf beiden Gittern zwischen 1/3 und 3 liegt.
- **P5 Verhaeltnis der Anregung A/C bei gleichem g** (Karte: (4 G/E)^2 = 0,05) [S]:
  - Ich erwarte, dass die Karte hier scheitert: (D1_A/D1_C)^2 >= 0,15 bei lambda 8 und 16 unter der Kante, wachsend
    etwa wie lambda^4.
  - Ueber der Kante (Abstrahlung, dQ-Ueberschuss A/C) wird gemessen, nicht vorhergesagt.
  - Nach der Karte ist eine Abweichung um mehr als Faktor 3 von 0,05 der neue Unterscheidungspunkt fuer das
- **P6 Kernfrage 2, Resonanz** [S; Resonanz selbst Literatur, Ciurla u. a. 2405.06591 [A]]:
  - ring_res hat sein Maximum bei Omega zwischen 1,485 und 1,503, in A und C und auf beiden Gittern.
  - Die Nachschwingfrequenz ist 1,4937 +- 0,01 (Ruhesystem).
  - Spitze gegen den groessten Wert bei |dOmega| >= 0,04: mindestens Faktor 5 in der Amplitude.
  - Halbwertsbreite etwa 0,011, gesetzt durch 600/gamma Antriebszeit.
  - Bei 1,494 gilt ring(2g)/ring(g) zwischen 1,8 und 2,2.
  - Der Ladungsverlust dQ_kern zeigt bei 1,494 hoechstens eine schwache Spitze (unter Faktor 2): Die Resonanz strahlt
    in 600/gamma Zeiteinheiten nur etwa 6 Prozent ihrer Energie ab (2 Gamma = 1,34e-4).
  - Scheitert, wenn auf beiden Gittern keine Spitze erscheint (Karte).
- **P7 Kante** (Karte: Spitze nahe 0,17) [S]:
  - Unter der Kante (Omega 0,14 und 0,155) ist der Ladungsverlust hoechstens dreimal so gross wie in der Kontrolle.
  - Das Maximum von dQ_kern liegt bei Omega 0,165 bis 0,23 und ist mindestens dreimal so gross wie bei 0,35. Grund:
    1D-Schwellenueberhoehung ~ 1/k_r.
  - Scheitert, wenn unter der Kante Abstrahlung auftritt oder das Maximum am oberen Rand liegt.

## Gegenproben (L2)

- **g = 0 (konstantes c = 1)** in jeder Gruppe:
  - D1, R, dQ und ring der Kontrollen sind die Rauschboeden.
  - Ein Effekt zaehlt erst ab dem Fuenffachen der Kontrolle.
  - Die Kontrolle prueft zugleich den Boost: Spitzendichte und Geschwindigkeit bleiben konstant.
- **konstantes c = 1 - g (gleichfoermig):** C darf sich nicht verformen (P1). Fuer A sage ich eine Verformung voraus;
  dort ist das die Messung, keine Gegenprobe.
- **Variante C mit Gezeiten nach der Metrik:**
  - gleichfoermig ohne Verformung, Uhr um Phi0 verstimmt (P1)
  - periodisch D_C ~ k^2 (P2)
  - bewegt wie ruhend bei gleicher Kruemmung (P2b)
  - Schwerpunkt nach 1 - 3 v^2 (P3)
- **Anregung ~ g^2:** 2g-Laeufe; D1 und ring verdoppeln sich, der dQ-Ueberschuss vervierfacht sich (Spalten "lin",
  Soll 2 bzw. 4).
- **lambda -> unendlich gibt QG-1s R:** R_starr(0, 0) im Kopf des Berichts; Punkt (16; 0,2) mit Omega 0,08 und kleinem
  Formfaktor.
- **v = 0:** statik, statische Verformung ohne Abstrahlung. Nach dem Abschalten kehrt S_max auf den Anfangswert zurueck
  (Spalte "S nach Abschalten").

## Aufloesung (L3)

- Zwei Gitter in jedem Aufruf.
- Der Bericht druckt je Paar "L3 D1 A, C" und "L3 R A, C" und je ruhendem Lauf "L3 dS": ok, wenn der Effekt (gegen die
  Kontrolle) mindestens fuenfmal groesser ist als die Aenderung fein gegen grob.
- Die Spitzensuche laeuft fuer beide Gitter getrennt.

## Latten (vorab geschaetzt)

- **L1 kann scheitern:** ja, P1 bis P7 mit Zahlen und Scheitergrenzen.
- **L2 Gegenprobe:** ja (oben).
- **L3 Numerik:** zwei Gitter.
- **L4 schon bekannt:** teilweise.
  - P0, P1, P3 sind ableitbar: C ist allgemeine Relativitaet in 1+1 Dimensionen, 1 - 3 v^2 ist Lehrbuch [L]. A folgt
    aus dem QG-1-Rahmen.
  - Die Resonanz 1,494 ist Literatur (Ciurla u. a.).
  - Neu fuer uns: die gemessene Dehnung A gegen C, die resonante und die Kanten-Antwort mit Zahlen, und ob der Monopol
    in A die Karte umdreht (P5).
- **L5 Messbezug:** mittelbar.
  - Die Uhrverstimmung in A (0,59 statt 1) ist eine Verletzung der Positionsinvarianz. Rotverschiebungstests mit Uhren
    (Gravity Probe A 1976, etwa 1e-4 [L]) schliessen so etwas fuer gewoehnliche Materie aus. Fuer Q-Ball-artige
    Materie gilt das nur mit derselben Uebertragungsgrenze wie in QG-1.
  - Gezeiten selbst prueft MICROSCOPE nicht (Karte).

## Abweichungen von Karte und Auftrag (mit Grund)

1. **"Gleiche Schwerpunktbeschleunigung"**
   - Umsetzung: Normierung Gamma = D1/a_com, beides gemessen, dazu die Linearitaetsprobe mit 2g. g wird nicht je
     Variante umskaliert.
   - Grund: R_A(v) geht bei v = 0,32 durch null (P3), dort ist Umskalieren unmoeglich. Das Divergieren von Gamma_A ist
     dort selbst das Signal.
2. **Dehnung aus S_max statt aus der Breite.** Die Breite eines bewegten Balls schwingt schon durch die
   Lorentz-Kontraktion mit, und in C ist die Koordinatenbreite eichabhaengig. W1 (Breite im Ruhesystem) steht nur
   nebenbei im Bericht.
3. **Rampen und freies Fenster.** Anregung heisst hier: Nachschwingen nach dem Abschalten im feldfreien Raum, also
   ohne Eichfrage. Die Abstrahlung der Karte ist als Ladungsverlust aus dem Kern (+-15) enthalten.
4. **Resonanz als eigener, feiner Omega-Scan** bei lambda 4. Das Geschwindigkeitsraster der Karte trifft 1,494 nicht:
   v = 0,6 gibt 1,178, v = 0,75 gibt 1,781. Die Spitze ist nur etwa 0,011 breit.
5. **Zusaetzlich statik** (Gegenprobe v = 0 der Karte, dazu P1 und P2) und **kante** (die Spitze nahe 0,17 der Karte).
6. **Karten-Vorhersage A/C = 0,05:** Ich halte dagegen (P5), weil A am Monopol koppelt und C nur an der Kruemmung.
   Beides steht vor dem Rechnen hier.

## Grenzen

  Gradientenabschluss (wie QG-1).
- R_starr ist eine adiabatische Starrkoerper-Rechnung: gut fuer Omega weit unter 0,16, ueber der Kante nur Richtwert.
- Langsame Abstrahlung knapp ueber der Kante verlaesst das Kernfenster spaet und wird eher unterschaetzt.
- Die gleichfoermige Kontrolle in C ist nur nach der Rampe flach. Waehrend der Rampe (80 Zeiteinheiten) gibt es
  eine Kruemmung ~ g/80^2.
- S_max zwischen Gitterpunkten parabolisch: Restfehler etwa 1e-5 gamma^4 (grob). Die Kontrolle g = 0 bei gleichem v
  misst ihn.
- Ungetestet (siehe oben). Der Rauchtest prueft die Codepfade, nicht die Physik.

## Einfach gesagt

Wir lassen einen Q-Ball durch ein Feld laufen, das die Lichtgeschwindigkeit wellenfoermig veraendert, und vergleichen
dass er an einer Stelle mit anderer Lichtgeschwindigkeit ist, und seine innere Uhr geht dort anders als bei anderen
Baellen. Mit Einsteins Regel spuert er nur, wie stark sich das Feld kruemmt. Ausserdem suchen wir, ob der Ball bei der
Frequenz 1,494, bei der er innerlich mitschwingt, wie eine angeschlagene Glocke nachklingt. Gerechnet ist noch nichts;
der Code ist ungetestet und soll zuerst kurz auf der .69 probelaufen.

Ende der Bearbeitung: 2026-09-30 03:10:07 CEST (gemessen mit date).
