# AFM-KANAL-2: Plan (Runde 12, explorativ)

- Code-Agent, Auftrag AFM-KANAL-2 der Leitung claude-primary. Start 2026-10-01 17:58:40 CEST (date). Plan begonnen
  2026-10-01 18:15:18 CEST (date), vor jedem Lauf. Zeitbox 100 min (bis 19:38 CEST).
- Grundlagen: KARTE.md (dieser Ordner), afm-kanal1/HERLEITUNG.md, afm-kanal1/ERGEBNIS.md, afm-kanal1/afm_kanal.py,
  RUNDE-07/bic2/bic2.py (exakt, kurve, Umlauf-Rechtecke), RUNDE-10/nls-leiter/nls2.py (W-Gitter, qbkontrolle),
  RUNDE-12/leiter2d-praez/ERGEBNIS.md (grobe rho-Abtastung verdeckt kleine s).
- Markierungen: [H] Hypothese/Deutung, [ES] eigener Schluss. Modell ist keine Messung.

## 1 Aus KARTE.md woertlich uebernommen

### Positivkontrolle (bindend)

- Derselbe Codepfad mit dem KG-Q-Ball (U = S - S^2 + S^3/2) muss die bewiesene Stelle omega^2 = 0,797677,
  rho = 1,744618 auf 1e-4 finden, mit Umlauf +-1 auf zwei Gittern.
- Verfehlt sie, ist der Lauf nicht auswertbar.

### Regel (bindend)

- **Stille Stelle gesehen:** Ein Familienmitglied zeigt ein aufgeloestes Umlauf-Rechteck mit +-1 auf zwei Gitterstufen
  (h und h/2), und die Lage stimmt zwischen den Stufen auf 1e-3 in Omega^2 und rho.
- **Auf dem Raster nicht gesehen:** Kein Mitglied zeigt Umlauf ungleich 0 und kein Vorzeichenwechsel von s im Fenster,
  bei bestandener Positivkontrolle.
- **Unentschieden:** alles andere, auch ein nicht aufgeloestes Rechteck.

### Vorhersage (Leitung, vor jedem Lauf)

- Stille Stelle im dicken AFM-Ball gesehen: ~40 %.
- Gruende dafuer: kompakter eingebetteter Zustand wie beim KG-Ball (AFM-KANAL-1); gleiche Kanalstruktur.
- Gruende dagegen: der zusaetzliche Topf -2 Omega rho (1 - cos Theta) und die Sigma-Modell-Nichtlinearitaet aendern die
  Kopplung. Und: In KG hat erst die Duennwandleiter viele Stellen; n = 1 haengt an einer einzigen Phasenbedingung.
- Falls gesehen: Lage rho zwischen 1,65 und 1,80 bei Omega^2 nahe 1 + kappa + 0,9 |kappa| (dickes Ende).

## 2 Gleichungen (HERLEITUNG.md von AFM-KANAL-1, keine neue Herleitung)

- l = 0, y = r w, Zeitfaktor e^{-i rho t}, Kanal 1 geschlossen (w = u + i v), Kanal 2 offen (w~ = u - i v):
  - y1'' = (A + B rho - rho^2) y1 + C y2
  - y2'' = C y1 + (A - B rho - rho^2) y2
- AFM: A = (V_u + V_v)/2, B = 2 Omega cos Theta, C = (V_u - V_v)/2 mit V_u, V_v wie dort (V_v in der Form ohne 0/0).
- KG (Positivkontrolle, beta = 1/2): A = dp - omega^2, B = 2 omega, C = sp, dp = 1 - 4S + 9 beta S^2,
  sp = -2S + 6 beta S^2. Das ist bic2 mit V = geschlossen (omega - rho), U = offen (omega + rho).
- Probe [ES]: aussen A -> 1 - Omega^2, B -> 2 Omega, C -> 0, also geschlossen 1 - (rho - Omega)^2,
  offen 1 - (rho + Omega)^2; Fenster 1 - Omega < rho < 1 + Omega. M ist reell symmetrisch, also ist die
  Wronski-Summe Omega(p, q) = p1 q1' - p1' q1 + p2 q2' - p2' q2 konstant.

## 3 Verfahren (afm_bic.py, ein Codepfad fuer AFM und KG)

- Profile: AFM aus afm_kanal.afm_profile (Kopie, unveraendert; Schiessen + Numerov-Newton, Gitter h/2); KG aus
  nls2.profile (Kopie, unveraendert; Modell qball, beta = 0,5, d = 3). Danach nur noch A, B, C auf dem Gitter h/2.
- Aussenrand R: erster Gitterpunkt mit Profilamplitude < 1e-6 * Amplitude(0), mindestens 20; Abweichung von A, B, C
  von den Aussenwerten bei R wird je Profil berichtet. Anschlusspunkt r_m = R_w (halbe Amplitude).
- Loesungen: y_a regulaer, offener Start (y2'(0) = 1); y_b regulaer, geschlossener Start (y1'(0) = 1); RK4 mit
  Schritt h von 0 bis r_m. z2 im geschlossenen Kanal abklingend: bei R y1 = 1, y1' = -kappa_c, offen 0, RK4 von R nach
  r_m, je Schritt mit e^{-kappa_c h} skaliert (positiver, glatter Faktor; aendert weder Nullstellen noch Umlauf).
- **W = L(y_a) + i L(y_b), L(y) = Omega(y, z2).** W = 0 <=> z2 liegt in der regulaeren Lagrange-Ebene <=> regulaere,
  in beiden Kanaelen abfallende Loesung bei reellem rho = stille Stelle (bic2, Satz in RUNDE-07/bic2/PLAN.md).
- **s:** s = L(y_a) an den Nullstellen von L(y_b). Raster je Mitglied: 4000 Punkte gleichabstaendig im Fenster
  [1 - Omega + 0,002, 1 + Omega - 0,002] plus 2000 Punkte in [1,6; 1,8] (KARTE: "dicht um 1,6 bis 1,8"), dazu die
  Fensterecken des Nachbarstreifens. Jede Vorzeichenklammer von L(y_b) wird mit 100 Punkten nachgerastert, die Nullstelle
  per Sekante in der Endklammer bestimmt und W dort **exakt neu gerechnet** (keine lineare Interpolation von s ueber das
  Raster; Lehre LEITER-2D-PRAEZ).
- **Aeste und Vorzeichenwechsel:** Zwischen benachbarten Reihen (7 Mitglieder plus 2 Zwischenreihen je Streifen mit 1500
  rho-Punkten) werden Nullstellen gepaart: wechselseitig naechste, gleiche Richtung von dL(y_b)/drho, Abstand < 0,3.
  Vorzeichenwechsel von s auf einem gepaarten Ast = Kandidat. Ungepaarte Nullstellen werden gezaehlt und berichtet.
- **Umlauf je Streifen:** Rechteck [Omega^2_i, Omega^2_{i+1}] x [1 - Omega_i + 0,002, 1 + Omega_i - 0,002] zwischen
  benachbarten Mitgliedern (6 Streifen je kappa). rho-Seiten = dichte Reihen der Mitglieder, bei Spruengen > 0,4 rad
  halbiert; Omega^2-Seiten aus den Zwischenreihen, bei Spruengen > 0,4 rad mit neuen Profilen halbiert (bis 6 Runden).
  Aufgeloest = jeder Phasensprung < 0,4 rad (wie bic2). Der Streifen-Umlauf zaehlt alle Nullstellen von W im Streifen
  (mit Vorzeichen) [ES].
- **Lokalisierung je Kandidat:** Illinois in Omega^2 auf s entlang des Astes (neues Profil je Schritt, rho lokal mit
  401 Punkten plus Nachrastern), bis die Klammer < 1e-7 oder 10 Schritte. Danach **kleines Rechteck**
  Omega^2* +- 4e-4, rho* +- max(2e-3, 3 |drho/dOmega^2| 4e-4) (hoechstens 0,02), 5 Profile auf den Omega^2-Seiten,
  41 rho-Punkte je rho-Seite, adaptiv wie oben.
- **Pole:** je Mitglied an jeder Nullstelle von L(y_b): D(rho) = det[y_a, y_b, j1, j2](r_m) bei komplexem rho,
  Jost-Ebene (j1 abklingend geschlossen, j2 auslaufend offen) alle 4 Schritte orthonormiert, 2D-Newton wie bic2
  (Start rho_b - 1e-6 i). Gamma = -Im rho. Polbreiten-Minima je Ast ueber die Mitglieder. Nur soweit die Zeit reicht.
- Zwischenergebnisse: JSON nach jedem Mitglied, jeder Zwischenreihe, jedem Streifen, jedem Kandidaten; Abtastungen als
  npz am Ende.

## 4 Familie und Gitter

- kappa in {-0,10, -0,19, -0,20}; je 7 Mitglieder Omega^2 = 1 + kappa + f |kappa| mit
  f in {0,5; 0,575; 0,65; 0,725; 0,8; 0,875; 0,95} (gleichabstaendig im dicken Teil, Grenzen wie AFM-KANAL-1).
  Das ist meine Lesart von "je 7 Omega aus dem dicken Teil des Fensters (f in {0,5 ... 0,95})".
- Positivkontrolle: KG mit 7 Mitgliedern omega^2 in {0,785; 0,79; 0,795; 0,80; 0,805; 0,81; 0,815}.
- Gitterstufen h = 0,02 und h/2 = 0,01 (Profilgitter h/2 = 0,01 bzw. 0,005), wie AFM-KANAL-1.
- Ein Aufruf je (Modell, kappa, h): 6 AFM-Aufrufe + 2 KG-Aufrufe, dann ein Auswertungsaufruf.

## 5 Auswertung nach der Regel (Umsetzung in afm_bic.py auswertung)

- Positivkontrolle bestanden: auf beiden Stufen ein lokalisierter Kandidat mit |Omega*^2 - 0,797677| < 1e-4,
  |rho* - 1,744618| < 1e-4 und aufgeloestem kleinem Rechteck mit Umlauf +-1.
- "gesehen": fuer ein kappa auf beiden Stufen je ein lokalisierter Kandidat mit aufgeloestem kleinem Rechteck +-1,
  Lagen auf 1e-3 gleich.
- "auf dem Raster nicht gesehen": Positivkontrolle bestanden, alle Streifen auf beiden Stufen aufgeloest mit Umlauf 0,
  kein Vorzeichenwechsel von s, kein Rechteck ungleich 0, alle Profile gueltig.
- Sonst "unentschieden" (auch: ein Streifen nicht aufgeloest oder ein Streifen fehlt).
- Lesart [ES]: "Mitglied" ist ein (kappa, Omega)-Paar; die Rechtecke und Streifen liegen zwischen Mitgliedern. Ein
  Streifen-Umlauf ungleich 0 zaehlt als "Mitglied zeigt Umlauf ungleich 0" (fuer beide Nachbarn).

## 6 Eigene Vorhersagen (Code-Agent, vor jedem Lauf)

- E-1 Positivkontrolle besteht auf beiden Stufen: ~80 %.
- E-2 Ausgang: "gesehen" ~45 %, "nicht gesehen" ~20 %, "unentschieden" ~35 %.
  - [H] Begruendung: Am dicken Ende wandert der kompakte geschlossene Zustand (AFM-KANAL-1: rho_c 1,05 bis 1,74) ueber
    einen weiten rho-Bereich; die Phase q R_w des offenen Kanals aendert sich dabei um mehrere rad. Ein
    Vorzeichenwechsel der Kopplung entlang des Astes ist darum eher wahrscheinlich als nicht.
  - Unentschieden-Risiko: Astpaarung bei grobem Omega-Abstand, nicht aufgeloeste Streifen nahe den Schwellen.
- E-3 Falls gesehen: auf dem oberen Ast (rho 1,3 bis 1,8) bei f >= 0,8 fuer kappa = -0,19/-0,20: ~60 %.
- E-4 Streifen-Umlauf und gepaarte s-Wechsel stimmen je Streifen ueberein (wo beide definiert): ~85 %.

## 7 Budget und Ablauf

- Lokaler Rauchtest (CPU, 1 Thread, nice 19, timeout 120 s): KG mit 2 Mitgliedern (0,795; 0,80) und AFM kappa = -0,20
  mit 2 Mitgliedern (f = 0,875; 0,95), h = 0,04, kleine Raster. Daraus Laufzeit je Mitglied hochrechnen (Nachtrag
  unten, vor dem Einfrieren).
- .69 nur ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4, cpu6;
  jeder Aufruf < 10 min (Budget im Code 540 s, danach entfallen Teile mit Vermerk). Skripte nie in place ueberschreiben.
- Vor dem ersten echten Lauf: PLAN.md.eingefroren-<JJJJMMTT-HHMMSS> plus sha256.

## 8 Nachtrag nach dem Rauchtest (vor dem Einfrieren, vor jedem echten Lauf; geschrieben ab 18:22:08 CEST, date)

- Rauchtests lokal (python3 des Systems, numpy 1.26.4, OMP/OPENBLAS/MKL 1 Thread, nice 19, timeout), h = 0,04, kleine
  Raster (800 + 300 rho-Punkte, 1 Zwischenreihe), Ausgaben in lauf-lokal/ (ungueltig fuer die Regel):
  - rauch-kg 2,3 s (Budget 55 s liess Lokalisierung und Pole aus), rauch-kg2 9,0 s, rauch-kg3 7,7 s (nach Code-Aenderung),
    rauch-afm 48,0 s (kappa = -0,20, f = 0,875 und 0,95), rauch-afm2 45,8 s (nach Code-Aenderung). Summe 112,8 s.
  - KG (h = 0,04): s wechselt zwischen 0,795 und 0,80 das Vorzeichen, Streifen-Umlauf -1 (aufgeloest), lokalisiert
    0,79767659 / 1,74461748 (Ziel 0,797677 / 1,744618), kleines Rechteck Umlauf -1, aufgeloest (0,359 rad).
  - AFM (h = 0,04): f = 0,95 hat bei rho = 1,74224 eine Nullstelle von L(y_b) mit s/median|W| = -6e-7 und
    Polbreite 8,5e-12; f = 0,875 Breiten 3e-7 bis 4e-8. Die eingebetteten Zustaende sind also aeusserst schmal.
    Folge fuer das Verfahren: Der Rand laeuft dort sehr nahe an W = 0 vorbei; die erste Fassung loeste den Streifen
    nicht auf (Sprung 3,04 rad).
- Code-Aenderungen nach dem Rauchtest (Regel, Kontrolle, Raster und Schwellen unveraendert):
  1. Omega^2-Seiten: je schlechtem Intervall 3 neue Profile statt 1, bis 8 Runden, hoechstens 60 neue Profile je
     Rechteck; rho-Seiten bis 40 Halbierungsrunden statt 16. Danach war der AFM-Streifen aufgeloest (0,391 rad, Umlauf 0).
  2. Ecken neuer Profile gemeinsam in einem Stapel (W_multi): gleiche Gleichungen, gemeinsamer Aussenrand (A, B, C mit
     den Aussenwerten verlaengert) und gemeinsamer Anschluss; W aendert sich dadurch nur um einen positiven Faktor
     (gleiche Phase). KG-Rauchtest danach gleich (rauch-kg3).
  3. Zusatzausgaben: groesster Sprung je Seite; Umlauf zusaetzlich aus der Kreuzungszaehlung
     (1/2) sum sgn L(y_a) sgn(Delta L(y_b)) als Gegenprobe (nicht entscheidend).
  4. Pole: hoechstens 15 Newton-Schritte, Nullstellen mit rho < 1 - Omega + 0,02 ausgelassen (dort lief Newton im
     Rauchtest weg).
  5. Lokalisierung: Klammer < 1e-7 oder 10 Schritte; Nullstellenverfeinerung mit einem Feinraster (Klammer/100), dann
     W exakt an der Nullstelle.
- Hochrechnung je Aufruf (.69 etwa wie Laptop angenommen): Mitglied 2,5 s (h = 0,02) bzw. 5 s (h = 0,01), Zwischenreihe
  1,5 bzw. 2,5 s, Streifen ~40 s (vor allem Profile), Kandidat ~80 s, Pole ~6 s je Mitglied (h = 0,02).
  Darum Aufteilung je kappa und Stufe in zwei Haelften: A = f {0,5; 0,575; 0,65; 0,725} (Streifen 0 bis 2),
  B = f {0,725; 0,8; 0,875; 0,95} (Streifen 3 bis 5); f = 0,725 in beiden. Erwartet 3 bis 6 min je Aufruf, Budget im
  Code 540 s, RuntimeMaxSec 600 s.
- Pole nur auf h = 0,02 (Polbreiten-Minima sind Zusatz, nicht Teil der Regel); h = 0,01 mit --pole nein.
- Aufrufe: kg-h0.02, kg-h0.01, afm-k{0.20,0.19,0.10}-h{0.02,0.01}-{A,B} (14), dann auswertung. Starter start.sh auf der
  .69 (einmalig per nohup, nur freie Spuren, kein Dienst).
- Auswertung fasst die Haelften je (kappa, h) zusammen: 7 gueltige Mitglieder, 6 Streifen.

## 9 Nachtrag 2 (nach Kenntnis der Hauptlaeufe, vor dem Folgelauf; geschrieben ab 2026-10-01 18:31:22 CEST, date)

- Stand der Hauptlaeufe (v1, Auswertung 16:30:51 UTC): Positivkontrolle auf beiden Stufen bestanden. AFM: 0
  Vorzeichenwechsel von s, 35 von 36 Streifen aufgeloest mit Umlauf 0. Nicht aufgeloest auf **beiden** Stufen:
  kappa = -0,10, Streifen 5 (Omega^2 0,9875 .. 0,995), groesster Sprung 0,755 rad auf der oberen Seite
  (rho = 1,99173, 0,002 unter der geschlossenen Schwelle), Umlauf -0,0000, Kreuzungszaehlung 0. Grund nach Ausgabe: der
  oberste Ast (L(y_b) = 0, Richtung -1, s/median|W| ~ 1e-8 bis 1e-7) kreuzt die obere Seite; dort laeuft W sehr nahe an
  0 vorbei, und die 8 Verfeinerungsrunden in Omega^2 reichten nicht.
- **Der vorab festgelegte Ausgang bleibt "Unentschieden"** (eingefrorener PLAN Abschnitt 5: ein nicht aufgeloester
  Streifen). Der Folgelauf aendert ihn nicht; die Leitung entscheidet ueber die Wertung.
- Folgelauf (nachtraeglich festgelegt): afm_bic_v2.py (nur --runden-x und --max-prof neu, Diff afm_bic_v2.diff), kappa =
  -0,10, Mitglieder f = 0,875 und 0,95 (genau dieser Streifen, gleiche Ecken, gleiche Zwischenreihen), h = 0,02 und
  0,01, --runden-x 30 --max-prof 240 --pole nein, Ausgabe in aus-nachtrag/ (nicht in aus/, damit die Auswertung der
  Hauptlaeufe unberuehrt bleibt).
- Vorhersage vor dem Folgelauf: Streifen auf beiden Stufen aufgeloest ~75 %; falls aufgeloest, Umlauf 0 auf beiden
  ~95 %; dieselben Werte von s und dieselben Nullstellen wie im Hauptlauf (bitgleich bis auf die Rechteck-Verfeinerung)
  ~95 %.
