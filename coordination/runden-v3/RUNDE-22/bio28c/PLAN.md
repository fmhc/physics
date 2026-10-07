# Runde 22, bio28c: Laufplan

Bearbeiter: Code-Agent (Opus 5.5), Auftrag der Leitung claude-primary. Beginn 2026-10-02 19:37:36 CEST (date). Skript
bio28c.py mit Konvention im Kopf geschrieben ab 19:44 CEST, vor jedem Lauf; Plan begonnen 19:46:47 CEST (date).
Verbindlich ist KARTE.md (vier gefuetterte Laeufe wie Bio 28b, Box dreifach, nur grob, bis T = 90; Normierung
"exakter Drehball m = 1 ergibt L_z = Q"; Aufteilung (a), (b), (c) zu 0, 20, 40, 60, 90; K0; J0 bis J2; Bedeutung).
Explorativ (v3), Hypothesen [H]. Ein dokumentierter Rauchlauf darf vor dem Einfrieren laufen.

## 0. Gelesen und Selbstanzeige

- Gelesen: KARTE.md; RUNDE-22/bio28b: KARTE.md, PLAN.md, ERGEBNIS.md, bio28b.py (ganz); RUNDE-05/r5-2d-a/r5_2d_a.py
  (Kopf, Konstanten, Profile, Gitter, ball_feld, ball_bewegt, entwickeln, dichten, analyse, lauf_standard);
  RUNDE-05 PLAN.md nur per grep nach "Drehimpuls"; RUNDE-21 bio28_weiter.py nur Kopf; auf der .69 kleintest.sh.
- Aus Bio 28b (ERGEBNIS) bekannt: zwei Toechter je Lauf ab t = 20, Windung 0, |v| 0,16 bis 0,30, Schwerpunkte bei
  T = 300. Drehimpulszahlen kenne ich nicht (siehe 1).

## 1. Ableitbarkeitsprobe (vor dem Lauf)

- **Befund: Die Karte sagt "Drehimpulse wurden in R5, R21 und R22 nicht ausgegeben". Das trifft fuer Bio 28b nicht ganz
  zu.**
  - bio28b.py speichert je Gebiet und Analysezeit (alle 5) Q, E, X, Y, vx = P_x/E, vy = P_y/E und Jspin_Q (Eigen-
    drehimpuls/Q um den Schwerpunkt, r5.analyse), dazu J_box_start und J_box_ende (grep: 882 bzw. 4 Treffer in
    bio28b/lauf-69/ausgabe/grob_roh.json). R21 (bio28_weiter.py) speichert Jspin_Q ebenfalls.
  - Damit sind (a) und (b) fuer die Maskengebiete bei t = 20, 40, 60, 90 aus den Bio-28b-Rohdaten bis auf Rundung
    ableitbar (P_k = v_k E_k, Bahn = (X_k - X0) x P_k, Eigen = Jspin_Q Q). Ebenso L0 = J_box_start.
  - Nicht ableitbar: (c) und die Erhaltung von L_box bis T = 90 (L_box nur bei 0 und 300 gespeichert).
  - **Ich habe diese Werte nicht angesehen** (nur Schluesselnamen gezaehlt). Nach dem Lauf rechne ich (a) und (b) aus
    den Bio-28b-Rohdaten mit jq nach (Abschnitt 4.6). Das zeigt die Ableitbarkeit und prueft zugleich, dass bio28c
    dieselbe Rechnung ist.
  - Folge fuer L1: J1 und J2 konnten scheitern, waren aber im Prinzip vorab aus vorhandenen Dateien ableitbar.
- K0a ist analytisch vorab bekannt: Fuer f(r) e^{i m theta - i omega t} gilt x P_y - y P_x = m rho punktweise
  (Abschnitt 2). K0a prueft also nur Code und Gitter.

## 2. Konvention (vorab, aus der Lagrangedichte von r5_2d_a.py)

- Lagrangedichte (r5_2d_a.py, Kopf): L = |psi_t|^2 - |grad psi|^2 - U(S), S = |psi|^2.
- Noether fuer Verschiebungen: T^0_i = (dL/d psi_t) d_i psi + (dL/d psi_t*) d_i psi* = 2 Re(psi_t* d_i psi).
  Impulsdichte P_i = -T^0_i = -2 Re(psi_t* d_i psi) = -(psi_t* d_i psi + c.c.), wie in der Karte.
  Vorzeichenprobe: geboosteter Ball mit v > 0 in x hat P_x = 2 v (f'^2 + omega^2 f^2) > 0 (kleines v).
- Ladung rho = 2 Im(psi psi_t*) (r5.dichten); fuer psi ~ e^{-i omega t} ist rho = 2 omega |psi|^2 > 0.
- Drehimpuls um den Ursprung: L_z = Int (x P_y - y P_x). Fuer psi = f(r) e^{i m theta - i omega t}:
  x P_y - y P_x = -2 Re(psi_t* d_theta psi) = -2 Re((i omega psi*)(i m psi)) = 2 m omega |psi|^2 = m rho, also L_z = m Q.
  theta zaehlt gegen den Uhrzeigersinn von der x-Achse; m = +1 (r5.ball_feld(g, p1, 1)) gibt L_z = +Q.
- Das ist genau r5.dichten (px, py, jz); bio28c.py benutzt r5.dichten unveraendert. Spektrale Ableitungen, Layout
  [Stapel, y, x].
- Bahnvorzeichen: Ein Koerper bei +y, der sich in +x bewegt, laeuft im Uhrzeigersinn um den Ursprung, L_z < 0.

## 3. Laeufe und Messung (bio28c.py)

- **Laeufe:** w60_nachbarn1, w60_nachbarn2, w75_nachbarn1, w75_nachbarn2, aufgebaut wie Bio 28b (r5.profile_holen in
  derselben Reihenfolge, m = 1-Ball im Ursprung, k Nachbarn m = 0 bei (+D, 0) Phase 0 und (-D, 0) Phase pi,
  D = R_halb(1) + R_halb(0) + 3,5), Box L = 115,2 (n 768), grob dx 0,3, dt 0,05, Randschicht wie R5 ab Tiefe 107,2,
  T = 90, ein Stapel B = 4. r5_2d_a.py unveraendert importiert (sha256 4b7a00b2...892bc7b).
- **Je Messpunkt (Takt 0,5):** Q_box, E_box, L_box, P_box, Q/E/L in der Randschicht (Tiefe >= 107,2),
  Ladungsschwerpunkt der Box.
- **An allen Vielfachen von 5** (darin die Kartenzeiten 0, 20, 40, 60, 90): Gebiete wie Bio 28b (geglaettetes S >
  0,5 x Anfangsmaximum des Laufs, 4er-Nachbarschaft, Gebiete unter 3 % der Anfangsladung zaehlen nicht, r5.analyse
  mit Windung). Schwerpunkt X_k wie Bio 28b (Gewicht S, r5.analyse).
- **Zerlegung** (je Lauf und Zeit; Summe ueber alle gezaehlten Gebiete k):
  - X0 = Sum Q_k X_k / Sum Q_k: gemeinsamer Ladungsschwerpunkt der Gebiete
  - P_k = Gebietsintegral der Impulsdichte (in r5.analyse als v_k E_k gespeichert, hier mit voller Genauigkeit)
  - (a) Bahn = Sum_k (X_k - X0) x P_k (x: 2D-Kreuzprodukt, A x B = A_x B_y - A_y B_x)
  - (b) Eigen = Sum_k Int_k ((x - X_k) P_y - (y - Y_k) P_x) (r5.analyse: Jspin)
  - (c) Rest = L_box - Sum_k Int_k (x P_y - y P_x): alles ausserhalb der gezaehlten Gebiete (Abstrahlung, Schwaenze
    unter der Maskenschwelle, Gebiete unter 3 %)
  - s = X0 x Sum_k P_k: Schliessglied, damit L_box = a + b + c + s exakt. Es misst zugleich, wie stark (a) von der
    Wahl von X0 abhaengt. Erwartung klein, weil die Toechter entgegengesetzte Impulse tragen.
  - Anteile: jeweils / L0 mit L0 = L_box(t = 0) des Laufs.
- **Zusatz (kein Kriterium):** dieselbe Zerlegung mit Zonen statt Masken. Jeder Gitterpunkt gehoert zum naechsten
  Gebietsschwerpunkt, wenn er hoechstens R_ZONE = 12 entfernt ist. Zweck: (c) trennen in "Schwanz nahe den Toechtern"
  und "ferne Abstrahlung". Grund: Bio 28b fand 21 bis 43 % mehr Ladung in Scheiben als in der Maske.
- **Konventionspruefung bei t = 0 auf demselben Gitter** (Kontrollfelder, keine Zeitentwicklung, eigene Maskenschwelle):
  - m1_w60, m1_w75: exakter Drehball m = 1 allein im Ursprung (Profile wie in den Laeufen)
  - m0_w60_ruhend: ruhender m = 0-Ball bei (10, -7)
  - paar_w60, paar_w75: zwei m = 0-Baelle bei (0, +12) mit v = 0,2 in +x und (0, -12) mit v = 0,2 in -x
    (r5.ball_bewegt). Erwartung: L < 0, a/L zwischen 0 und 1 (Anteil des Impulses in der Maske), b/L nahe 0.
  - Die Kontrollen zeigen zugleich, welchen Teil eines reinen Eigen- bzw. Bahndrehimpulses die Maske in (b) bzw. (a)
    erfasst (beschreibend).

## 4. Auswertung (vor dem Lauf festgelegt, im Skript so umgesetzt)

### 4.1 K0 und J0

- **K0a:** m1_w60 und m1_w75: |L_box/Q_box - 1| <= 0,01.
- **K0b:** m0_w60_ruhend: |L_box| <= 0,01 Q_box (Hinweis der Leitung: ruhender m = 0-Ball, L_z = 0).
- **K0c** je Lauf: max ueber alle Messpunkte t <= 90 von |L_box(t)/L0 - 1| <= 0,01.
  - "Solange nichts den Rand erreicht": Erreicht die Energie in der Randschicht 1e-4 E_box(0) vor T = 90, endet das
    Fenster dort (t_rand wird berichtet). Erwartung: kein t_rand, Wellenfront bei t = 90 hoechstens bei Tiefe ~105.
  - Fehlt der Lauf bis 90, ist K0c offen.
- **K0** bestanden = K0a und K0b und K0c in allen vier Laeufen. **J0** = K0 bestanden (eingetroffen / nicht /
  offen bei fehlenden Daten).
- **Vorzeichenprobe (Bedingung, nicht Teil von K0):** paar_w60 und paar_w75: L < 0, a/L > 0, |b/L| < 0,05, genau zwei
  Gebiete.

### 4.2 J1 und J2

- Je Lauf bei T = 60: a/L0 und b/L0 aus 3.
- **J1** je Lauf erfuellt, wenn a/L0 >= 0,5 (mit Vorzeichen; L0 > 0). Eingetroffen bei mindestens 3 von 4 Laeufen,
  nicht eingetroffen bei hoechstens 2 von 4 (alle vier vorhanden).
- **J2** je Lauf erfuellt, wenn |b/L0| < 0,10.
  - **Festlegung der Bearbeitung (nicht Karte):** Die Karte nennt fuer J2 keine Laufzahl. Ich lese J2 als Aussage
    ueber alle vier Laeufe: eingetroffen, wenn alle vier erfuellen; nicht eingetroffen, sobald einer nicht erfuellt.
  - **Festlegung der Bearbeitung:** Betrag |b|, damit ein starker Gegendrall nicht als "klein" zaehlt. Das Vorzeichen
    wird berichtet.
- **Sind K0 oder die Vorzeichenprobe nicht bestanden, sind J1 und J2 offen.** Die Zahlen werden trotzdem berichtet.

### 4.3 Bedeutung (Wortlaut der Karte, Skript gibt sie aus)

- J1 und J2 eingetroffen: "Der innere Drehimpuls des Drehballs geht beim Zerfall in die Bahnbewegung der Toechter
  ueber, wie bei einem sich teilenden rotierenden Tropfen [H, im Modell]."
- J1 nicht eingetroffen: "Der Drehimpuls geht ueberwiegend in Abstrahlung (c)"; Groesse von (c) je Lauf angeben.
  Zusatz im Bericht: (c) nach Zonen getrennt (Schwanz nah / fern), ohne die Bedeutung zu aendern.
- Sonst: keine Bedeutung nach Karte, Ausgaenge ohne Deutung.

### 4.4 Tabelle

- Je Lauf und t = 0, 20, 40, 60, 90: L_box/L0, (a), (b), (c), s, je / L0; dazu Zahl der Gebiete, X0 und je Gebiet Q,
  Lage, Bahn- und Eigenanteil, Jspin/Q, Windung. Zusatz: Zonenwerte a_Z, b_Z, c_Z.

### 4.5 Beschreibend (kein Kriterium)

- L0/Q_m1 je Lauf (Ueberlapp der Anfangsfelder), Q_box- und E_box-Erhaltung bis 90, Energie in der Randschicht.
- Zerlegung an allen Vielfachen von 5 (in der Rohdatei).

### 4.6 Nachtraegliche Rechenprobe gegen Bio 28b (vorab festgelegt, kein Kriterium)

- Mit jq aus bio28b/lauf-69/ausgabe/grob_roh.json bei t = 20, 40, 60, 90 je Lauf: Gebiete (Q, X, Y) mit bio28c
  vergleichen. Erwartung: gleich bis auf die Rundung der Bio-28b-Ausgabe (Q 4, X/Y 3 Stellen).
- Daraus (a) und (b) bei T = 60 nachrechnen (P_k = v_k E_k, Eigen = Jspin_Q Q). Erwartung: gleich bis auf Rundung. Das
  ist der Nachweis der Ableitbarkeit (Abschnitt 1), keine neue Messung.

## 5. Aufrufe (.69, kleintest.sh)

- kleintest.sh (gelesen 19:41 CEST): systemd-run, CPUQuota 100 %, MemoryMax 4G, RuntimeMaxSec 600.
- GPU-Speicher 19:41: P4000 Nr. 0 6,5 von 8 GB, Nr. 1 6,4 von 8 GB durch fremde Dienste; Bio 28b brauchte grob 570 MB.
- Vorbereitung: rsync von bio28c.py und r5_2d_a.py nach /home/fmh/fmhc-physics-remote/runde22-bio28c/, py_compile auf
  der .69 (ok, 19:46), sha256 beidseitig gleich.
- **Rauchlauf** (vor dem Einfrieren, Zahlen ungueltig ausser den t = 0-Kontrollen): `--gruppe rauch`, T = 6,
  Selbsttest der Auswertung mit erfundenen Zahlen, Auswertungsdurchlauf.
- **Hauptlauf** nach dem Einfrieren: `bash kleintest.sh p4000b r22-bio28c-grob bio28c.py --gruppe grob` (bei
  Belegung p4000a), dann `--auswerten lauf-69/ausgabe/bio28c_roh.json` auf Spur cpu.
- Laufzeit-Schaetzung aus Bio 28b (14,6 ms je Schritt, Schiessen 63 s): 1800 Schritte etwa 26 s, Analysen etwa 5 s,
  zusammen etwa 100 s. Waechter bei t = 20: Abbruch bei Prognose > 570 s.
- Technischer Abbruch: denselben Aufruf unveraendert wiederholen, Vermerk im Ergebnis.

## 6. Grenzen

- Nur grob (Karte), keine Gitterpruefung grob/fein. K0c ist die numerische Pruefung.
- Die Maske erfasst die Schwaenze nicht. (c) enthaelt deshalb auch die Schwaenze der Baelle, schon bei t = 0. Die
  Kontrollen und die Zonen-Zerlegung zeigen, wie gross dieser Teil ist.
- X0 und X_k sind Schwerpunkte verschiedener Art (Ladung bzw. S-Gewicht wie Bio 28b). Das Schliessglied s zeigt die
  Wirkung.
- 2D, ein Feld, Futter statt Bad (R5-Modell).

### 5.1 Rauchlauf (vor dem Einfrieren, Zahlen ungueltig)

- p4000b, 17:46:45 bis 17:47:53 UTC (19:46:45 bis 19:47:53 CEST), rc 0, Unit 68 s. Log lauf-69/RAUCH.log.
- Selbsttest der Auswertung (drei erfundene Faelle): ok, alle Sollwerte getroffen.
- Gemessen: Schiessen 63,0 s, 14,63 ms je Schritt (n 768, B 4), 2 Analysen in 0,2 s, GPU hoechstens 573 MB,
  Gesamtdauer 65,4 s.
- **Gesehen (Selbstanzeige):** nur die Wahrheitswerte K0a true, K0b true, Vorzeichenprobe true (t = 0-Kontrollen, wie
  im Hauptlauf) und J offen. Keine Zahlen der Kontrollen oder der Zerlegung angesehen.
- Hochrechnung Hauptlauf: 63 s + 1800 x 14,6 ms (26 s) + 19 Analysen (2 s), etwa 95 s. Keine Teilung noetig.
- Keine Aenderung am Skript nach dem Rauchlauf.
