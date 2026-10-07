# Z2-SCHUTZ-1: Plan (Runde 49; Barriere 360 -> 0 Grad auf Finns Diamant-Netz)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 12:49:07 CEST (date). Plantext ab 13:03:10 CEST (date),
  vor Code und Rauchtest. Zeitbox 120 min ab Start.
- Karte: KARTE.md (Frage, ZS0 bis ZS3, Kontrollen). Daran aendert dieser Plan nichts. Festlegungen [F] machen die Karte
  rechenbar; Zusaetze sind als **Zusatz** markiert und nicht urteilsbildend.
- Kennzeichen: [M] Mathematik; [E] Rechnung im Modell; [L] Literatur oder Gedaechtnis; [H] Hypothese; [F] Festlegung
  dieses Plans; [R] im Rauchtest gesehen; [P] Projektdatei. Alles ist eine synthetische Modellrechnung, keine
  Messdatenbestaetigung.
- Vorwissen [P]: GUERTEL-FINN-NETZ-1 (GFN1) ERGEBNIS und PLAN, Code finn.py. Bekannte Diamant-Werte (12, 24): E(360)
  etwa 5516,38 (Protokollzustand), GF2-Laeufe bei 420 Grad (E_vor 7463,25, E_Ende 3850,0420), theta_max 540 Grad.

## 0. Vorab (Schreibtisch, vor jeder Rechnung)

1. **Eichung [M]:** E = Summe 4(1 - c^2), c = q_a . q_b, ist unter q_a -> -q_a an jedem Knoten einzeln invariant. Das
   Feld lebt also auf SO(3)^N; die Sonde c <= 0 haengt von der stetigen Hebung ab. Der unverdrehte Zustand T (alle
   freien Knoten q = +1, Kern -1, Rand +1) hat E = 0 exakt und Kraft 0 exakt (globales Minimum). Die Kernbindungen
   haben dort c = -1, also einen "Sprung" ohne Energie.
2. **Startzustand [M]:** Bei 360 Grad ist der Kern q = -1 und damit wie der Rand (+1) invariant unter globaler
   Konjugation q -> u q u^-1. Die Drehung der Drillachse (um x und um y) gibt zwei exakte Nullmoden der Hesse-Matrix
   ("Eichmoden" im Sinn der Karte: Symmetrie-Nullmoden). Im Kontinuum ist die Mode sin(psi) (psi = halber Drehwinkel)
   positiv im Inneren, also Grundzustand des Querteils; Erwartung: sonst alles positiv [M, Kontinuum].
3. **Weg [M]:** 360 -> 0 braucht einen Gittersprung (KARTE). Erwartete Form [H, nicht urteilsbildend]: Keimbildung
   einer Z_2-Wirbelschleife (Ring aus Bindungen mit Drehwinkel nahe pi), die die Kugel ueberstreicht. Treibende Kraft
   ist der Drillgradient, am Kern am groessten (proportional 1/r0 bei festem r0/R). Zahlen dazu gebe ich nicht vorab.
4. **Groessenwahl [F, mit Begruendung aus GFN1 P]:** Der Drillgradient am Kern ist theta h'(r0), h'(r0) = R/(r0(R - r0)).
   Bei festem r0/R = 1/2 ist (r0, R) bei 360 Grad so belastet wie (12, 24) bei 360 * 12/r0 Grad. GFN1 sprang auf (12, 24)
   bei 540 Grad; (8, 16) bei 360 entspraeche 540 und ist damit ausgeschlossen, (9, 18) entspraeche 480 (in GFN1 nie
   lang relaxiert). Gewaehlt: G1 = (10, 20) (entspricht 432 Grad), G2 = (12, 24) (GFN1), G3 = (14, 28).
5. **Dimensionen (AGENTS.md):** innere Symmetrie SO(3) (Hauptfrage, ZS0) und SO(2) (Gegenprobe) getrennt gerechnet;
   Raum: 3D-Diamant-Graph, keine Uebertragung auf 1D oder 2D.

## 1. Netz und Zustaende [F]

- **Netz:** finn.Netz("diamant", r0, R), unveraendert aus GFN1 (Zellkante 2, Knotendichte 1, Bindungslaenge 0,866,
  Kern r <= r0, Rand r > R, Profil h harmonisch 3D). **Kerngroesse:** r0 = R/2 bei allen drei Groessen.
- **Start S (360 Grad):** q = cos(pi h) + z sin(pi h) auf allen Knoten (Kern -1, Rand +1), kein Rauschen, dann
  finn.fire_feld mit ftol 1e-7, nmax 20000, dtmax 0,1. E_S := E am Ende.
- **Ende T:** alle freien Knoten +1 (exakt, keine Relaxation).
- **Barriere [F, Kartenwortlaut]:** B := E_Sattel - E_S (Sattelenergie minus Startenergie), je Verfahren wie in
  Abschnitt 2.

## 2. Wegverfahren [F] (Fassung nach den Rauchtests 3 bis 5, Begruendung im Abschnitt "Rauchtests")

- **Gemeinsam:** Netz und Energie aus finn.py; Kraefte F = -tang(grad E) (feste Knoten 0); FIRE wie finn.fire_feld
  (dtstart 0,02, Schrittdeckel 0,05 je Knoten) und, bei Weg-Ketten, je Bild.
- **Verfahren A: Bisektion auf der Trennflaeche ("edge tracking")** [L: Skufca, Yorke, Eckhardt 2006, fuer
  Kantenzustaende; hier auf die Energielandschaft angewandt].
  - Familie ebener Startzustaende X(lambda): Halbwinkel psi_i -> psi_i (1 - lambda w_i), w_i = clip((30 Grad + d -
    gamma_i)/d, 0, 1), d = 30 Grad, gamma_i = Winkel zwischen Ortsrichtung und Keimrichtung n_P = (0,92; 0,33; 0,21)
    normiert (allgemeine Richtung, keine Gitterachse). lambda = 0 ist S, lambda = 1 eine entdrillte Kappe.
  - Je lambda: FIRE (Kopie finn.fire_feld, dtmax 0,1) mit Klasse "T", sobald E < E_S - 1 (ausserhalb des Beckens von
    S), Klasse "S", sobald ab Schritt 30 keine Bindung mehr c <= 0 hat (zurueck in der Hebung von S), sonst nach 800
    Schritten "offen" (Abbruch der Bisektion, dieser Zustand gilt als naechster am Sattel).
  - Erst lambda = 1 (muss "T" sein), dann 14 Halbierungen auf [0, 1] (bis 70 % der Wandzeit).
  - Je Bahn wird der Zustand kleinster Knotenkraft ab Schritt 30 gemerkt (Naeherung des Sattels von beiden Seiten).
  - **B_A := max(E_fmin(letzte T-Bahn), E_fmin(letzte S-Bahn)) - E_S.**
  - **Freigabe:** die letzte T-Bahn wird mit FIRE bis E < 1e-3 (T erreicht), 6000 Schritte oder Wandzeit fortgesetzt.
  - **Gueltig**, wenn beide Klassen vorkommen (Klammer), mindestens 10 Halbierungen gerechnet sind, die Freigabe T
    erreicht und dabei unter E_S bleibt, und S die Hesse-Kontrolle besteht. Dann verbindet der Weg S -> Sattelnaehe ->
    T den Startzustand mit dem unverdrehten Feld T.
- **Verfahren B: Nudged Elastic Band mit Kletterbild (CI-NEB)** [L: Henkelman, Uberuaga, Jonsson 2000].
  - Anfangsweg: S -> Klammerzustand S-Bahn -> Klammerzustand T-Bahn -> Endzustand der letzten T-Bahn (E < E_S - 1),
    stueckweise linear, auf M + 2 = 8 Bilder gleicher Bogenlaenge gebracht (g2.reparam_feld); Endpunkte S und
    T-Bahn-Ende fest; innere Bilder mit Rauschen ausserhalb der Ebene wie finn.rauschen (sigma 1e-3, Saat [49, 1, R]).
  - Tangente nach Henkelman und Jonsson (2000, "improved tangent") auf den Tangentialraum projiziert; Feder k_s = 1,0
    entlang der Tangente; senkrechte wahre Kraft; Kletterbild F - 2 (F . tau) tau ohne Feder.
  - **Eichung:** Nach jedem Schritt wird Bild k+1 je freiem Knoten auf das Vorzeichen von Bild k gebracht
    (q -> -q, Geschwindigkeit ebenso). Die Energie aendert sich dabei nicht.
  - Klettern ab Iteration 50; Kletterbild = inneres Bild mit hoechster Energie, nur wenn diese ueber beiden Endpunkten
    liegt.
  - **Konvergenz:** groesste Knotenkraft des Kletterbildes < 5e-3 (Bandkraft nur berichtet). Abbruch bei Konvergenz,
    6000 Iterationen oder Wandzeit 480 s.
  - **B_B := E_Kletterbild - E_S.** Gueltig, wenn konvergiert, geklettert, S besteht die Hesse-Kontrolle und die
    Freigabe aus Verfahren A erreicht T.
- **Barriere je Groesse:** B(G) := min ueber die gueltigen Verfahren (die Karte fragt nach der kleinsten Barriere).
- **Grenze [M]:** Beide Verfahren pruefen einen Mechanismus (Keim bei n_P, aus einer Familie von Kappen). Die kleinste
  Barriere ueber alle Wege und Orte ist damit nach oben abgeschaetzt, nicht bewiesen. Die Bisektion naehert den Sattel
  nur so gut, wie die letzte Bahn an ihm vorbeilaeuft; der CI-NEB zwischen den Klammerzustaenden prueft das.
- **Fallen gelassen nach den Rauchtests:** Streifweg S -> T, Keimweg S -> K (NEB und Stringmethode) und Zugverfahren an
  einer Bindung (siehe Abschnitt "Rauchtests"); der Code dafuer bleibt in z2.py (Modi keim, zug, weg mit --keim), wird
  aber nicht aufgerufen.

## 3. Lokalisierung (ZS3) [F]

- Je Bindung b: Delta_b = e_b(Sattel) - e_b(S), e_b = 4(1 - c_b^2). Summe aller Delta_b = B. Sattel = Klammerzustand
  mit der hoeheren Energie (Verfahren A) bzw. Kletterbild (Verfahren B).
- **L6 := (Summe der 6 groessten Delta_b)/B.** Beschreibend: n50 (kleinste Zahl Bindungen fuer 50 %), groesstes
  Delta_b, Radius und Winkel zu n_P dieser Bindung, c dieser Bindung am Sattel, Zahl der Bindungen mit c <= 0 am Sattel.

## 4. Kontrollen [F]

- **K-Weg (Karte):** |B_A - B_B| / min(B_A, B_B) <= 0,05 je Groesse (beide gueltig). Sonst "verfehlt" bzw. "nicht
  auswertbar".
- **K-Hesse (Karte):** Riemannsche Hesse-Matrix auf dem Tangentialraum der freien Knoten (duenn, 3 N_frei), vier
  kleinste Eigenwerte (scipy eigsh, which SA).
  - S: lambda_1, lambda_2 in [-1e-5, 1e-5], lambda_3 > 1e-4, und der Raum der zwei kleinsten Eigenvektoren enthaelt
    die zwei analytischen Symmetriemoden (q -> (e_x q - q e_x)/2 bzw. e_y) zu mindestens 0,99 (Normanteil).
  - T: lambda_1 > 1e-4.
  - Beschreibend: Kletterbild des CI-NEB (Zahl der Eigenwerte < -1e-5; erwartet 1), ZS0-Endpunkte.
- **ZS0-Lauf (Karte):** Netz G2 = (12, 24). Endpunkte aus GFN1 lauf-69 (Kopie in eingaben-gfn1/): Zustand "420" aus
  prot-diamant-so3-d10-zust.npz und Endzustand stoss-diamant-so3-T420-e0.01-end.npz. Bezugswerte E_vor und E_end aus
  stoss-diamant-so3-T420-e0.01.json (GF2). Anfangsweg: GFN1-Stoss eps = 0,01 bei 420 Grad (finn.kipp) mit FIRE wie
  GFN1 (nmax 3000), Bild alle 4 Schritte; Weg = [420-Zustand, Bilder..., GFN1-Endzustand], auf M + 2 = 10 Bilder
  gleicher Bogenlaenge gebracht. Wegrechner: CI-NEB (wie B, mit Eichung) und Stringmethode mit Kletterbild
  [L: E, Ren, Vanden-Eijnden 2007; Ren, Vanden-Eijnden 2013] (zentrale Tangente, Umparametrisierung auf gleiche
  Bogenlaenge nach jedem Schritt, getrennt um das Kletterbild). Konvergenz ohne Kletterbild: groesste Knotenkraft aller
  inneren Bilder < 5e-2. Wandzeit je 240 s.
- **SO(2)-Gegenprobe (Karte):** Netz G2, SO(2)-Feld (finn, feld so2). Endpunkte: SO(2)-Zustand "420" aus GFN1
  prot-diamant-so2-d10-zust.npz; -300-Zustand: phi = 2 atan2(q_z, q_0) des GFN1-SO(3)-Endzustands (Werte in (-2 pi, 0]),
  Kern 420 Grad, dann FIRE (SO(2)) bis ftol 1e-7, nmax 20000. Anfangsweg: phi linear je Knoten. CI-NEB, Wandzeit
  120 s. **Bestanden**, wenn der Endweg eine innere Barriere hat: max_k E_k > E_0 (1 + 1e-6).
- Sprungsonde laufend (Minimum von c ueber alle Bilder und Iterationen; SO(2): Maximum von |dphi|).

## 5. Urteilsregeln [F] (mechanisch in code/auswertung_z2.py)

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| ZS0 | CI-NEB und Stringmethode je: (i) Endweg monoton, E_{k+1} <= E_k + 1e-9 E_0 fuer alle k; (ii) laufende Sonde > 0; (iii) Endpunktenergien gegen GF2 auf 1e-6 relativ; (iv) konvergiert | CI-NEB: (i), (ii), (iii) |
| ZS1 | B(G) gueltig fuer G1, G2, G3 und 2 <= B(G) <= 8 fuer alle drei | dasselbe |
| ZS2 | B(G) gueltig fuer alle drei und (max - min)/min < 0,20 | dasselbe |
| ZS3 | L6 > 0,5 am Sattel des Verfahrens, das B(G) liefert, fuer alle drei Groessen | L6 > 0,5 am Sattel fuer G2 = (12, 24) (das Netz der Karte) |

- Fehlt ein gueltiger Wert, lautet das betroffene Urteil "nicht auswertbar".
- Beschreibend: Bisektionsschritte (lambda, Klasse, kleinste Kraft), Energieprofil des CI-NEB, erstes Bild mit Sonde <= 0, Iterationen, Laufzeit, E_S gegen
  GFN1 (5516,38), Ort der Zugbindung (Radius, Kernbindung ja/nein).

## 6. Laufplan [F]

- Nur .69, ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu und cpu7; je Lauf <= 10 min
  (RuntimeMaxSec 600), 1 Thread. Ordner /home/fmh/fmhc-physics-remote/z2-schutz-1/ (code/, eingaben-gfn1/, rauch*/,
  lauf/).
- **Code:** code/finn.py, guertel2.py, guertel.py, stab.py unveraenderte Kopien aus GFN1 (dort nichts geaendert);
  code/z2.py (neu: Start, Zug, Wege, Hesse); code/auswertung_z2.py (neu).
- **Hauptlaeufe** (eingefrorener Code, je genau einmal):
  - cpu: Start G3; Bisektion G3 (A); CI-NEB G3 (B); ZS0 CI-NEB; ZS0 String; SO(2)-Gegenprobe; Hesse G3.
  - cpu7: Start G1; Start G2; Bisektion G1; Bisektion G2; CI-NEB G1; CI-NEB G2; Hesse G1; Hesse G2 (mit
    ZS0-Endpunkten); danach die Auswertung (wartet auf cpu).
  - Start: ftol 1e-7, nmax 20000, Wandzeit 540 s. Bisektion: 14 Halbierungen, je Bahn hoechstens 800 Schritte,
    Halbierungen bis 70 % der Wandzeit 480 s, Rest Freigabe. CI-NEB Hauptfrage: M = 6, nvor 50, nmax 6000, Wandzeit
    480 s. ZS0: M = 8, nvor 150, Wandzeit 240 s je Verfahren. SO(2): M = 8, Wandzeit 120 s.
- Bricht ein Lauf ab oder konvergiert nicht, kann er als markierter Nachtrag mit Fortsetzung laufen; urteilsbildend
  bleibt der eingefrorene Ablauf.

## Rauchtests und Festlegungen vor dem Einfrieren [R]

- Alle Rauchtests auf der .69 (UTC = CEST - 2 h), je Lauf <= 120 s, nur Groessen (6, 12), (9, 18) und Laufzeitproben auf
  (14, 28). Angesehen habe ich nur Laufzeiten, Iterationszahlen, Kraefte, Abstaende, Kletterindex und Ja/Nein-Felder;
  keine Barrieren- oder Energiewerte der Plangroessen.
- **Rauchtest 1 (11:10 bis 11:12 UTC):** alle Modi rc = 0. Laufzeit des Weges auf (14, 28) mit 12 inneren Bildern
  2,3 s je Iteration (Bildanordnung (N, P, 4) mit Spaltenschnitten). Hesse (14, 28): rund 30 s je Zustand.
- **Rauchtest 2 (11:15 bis 11:16 UTC):** Bildanordnung (P, N, 4), Endpunkte nur einmal gerechnet: 1,2 s je Iteration
  auf (14, 28), M = 12.
- **Rauchtest 3 (11:16 bis 11:18 UTC, (9, 18), 110 s):** Streifweg S -> T. NEB nach 400 Iterationen Kraefte 1,8
  (Band) und 1,9 (Kletterbild), keine Abnahme; Stringmethode ohne Kletterbild (kein inneres Bild ueber E_S: Der Sattel
  liegt so nah an S, dass der lange Weg ihn nicht aufloest). Folge: Keimweg S -> K, M = 8, FIRE je Bild.
- **Rauchtest 4 (11:22 bis 11:25 UTC, (9, 18)):** Keim bei 30 Grad sofort unter E_S - 1, K -> T erreicht T. NEB und
  String weiter mit Kraeften 1 bis 4. Befund: zwischen Nachbarbildern Skalarprodukte q_k . q_k+1 bis -1, also
  Vorzeichenwechsel einzelner Knoten (Eichsprung; E haengt nur von c^2 ab). Folge: Eichung nach jedem Schritt,
  Mindestrelaxation 100 Schritte fuer K.
- **Rauchtest 5 (11:27 bis 11:29 UTC, (9, 18)):** Eichung wirkt (q_k . q_k+1 >= 0), aber nur knapp ueber 0: einzelne
  Knoten drehen zwischen Nachbarbildern um fast 180 Grad (SO(3)). Der Weg besteht aus vielen kleinen Gittersprungen;
  8 Bilder loesen ihn nicht auf, die Kraefte bleiben bei 1 bis 12. Folge: Verfahren A = Zugverfahren an der
  staerksten Bindung (einzelner Sprung, voll relaxiert, FIRE ohne Ketten), Verfahren B = CI-NEB auf dem glatten Zugweg.
  Der Ablauf weicht damit vom Plantext ab (dort NEB und Stringmethode auf einem Streifweg); ZS0 behaelt beide
  Kettenverfahren.
- **Rauchtest 6 (11:32 bis 11:34 UTC, (9, 18)):** Zugverfahren an der staerksten Bindung (Kernbindung, r = 9,4): 17
  Zwangsminima je etwa 150 bis 200 Schritte bis ftol 1e-4, aber das Energiemaximum liegt am Ende (j = 16), und die
  Freigabe laeuft zurueck nach S. Ein einzelner Bindungssprung ist also unterkritisch; der kritische Keim ist groesser.
  Folge: Verfahren A = Bisektion auf der Trennflaeche in einer Kappenfamilie, Verfahren B = CI-NEB auf dem Weg
  S -> Klammerzustaende -> T-Bahn.
- **Rauchtest 7 (11:36 bis 11:40 UTC, (9, 18)):** erster Versuch rc = 1 (Klammerzustand fehlte, wenn eine Bahn vor
  Schritt 30 entschieden war; Klasse "S" schon bei Schritt 0). Korrigiert (Zustand am Ende als Ersatz, "S" erst ab
  Schritt 30). Zweiter Versuch: Klammer, NEB nur zwischen den Klammerzustaenden ohne inneres Maximum, also kein
  Klettern. Folge: Weg S -> Klammer -> T-Bahn-Ende, M = 6, 14 Halbierungen. Dritter Versuch (7c): Bisektion 14
  Halbierungen, Klammerbreite 6e-5 in lambda, kleinste Kraefte 0,14 (S-Bahn) und 0,28 (T-Bahn), Freigabe erreicht T;
  CI-NEB konvergiert nach 184 Iterationen (Kraft des Kletterbildes 4,8e-3). Laufzeit 53 s und 28 s auf (9, 18).
- **Gesehen:** nur die genannten Ja/Nein-Felder, Kraefte, Iterationen und Laufzeiten; keine Barrieren- oder
  Energiewerte. Auf (9, 18) habe ich auch keine Barriere angesehen.
