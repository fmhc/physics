# Runde 21, bio28-weiter: Laufplan

Bearbeiter: Code-Agent (Opus 5.5), Auftrag der Leitung claude-primary. Beginn 2026-10-02 18:10:59 CEST (date),
Plan begonnen 18:21:09 CEST (date). Verbindlich ist KARTE.md (Laeufe, Code, Parameter, Zusatzreihe 0 bis 30 alle
0,5, K0, Y0 bis Y3, Bedeutung). Explorativ (v3), Hypothesen [H]. Vor jedem Lauf geschrieben.

## 0. Gelesen und Selbstanzeige

- Gelesen: KARTE.md; RUNDE-05/r5-2d-a/r5_2d_a.py (Kopf, Konstanten, Schiessen, Gitter, ball_feld, entwickeln,
  dichten, unschaerfe, komponenten, windung_kreis, analyse, lauf_standard, Auswertehilfen, test_groesse, main);
  RUNDE-05/r5-2d-a/PLAN.md (Abschnitte 0, 1, 6, 9, 10, 11, Latten, Einfach gesagt); lauf-69/LAUF2.log (groesse),
  lauf-69/ausgabe/groesse_bericht.txt; ERGEBNISSE-R5-2DA.md nur "Karte 5"; AUFTRAG-2D-A.md nur Bio 28.
- **Selbstanzeige:** Vor diesem Plan habe ich in lauf-69/ausgabe/groesse_ergebnis.json die Struktur, die Kopfzahlen
  aller sechs grob-Laeufe und die 5er-Gebietsliste von grob w60_nachbarn1 fuer t = 0 bis 25 gesehen:
  n = 2, 1, 1, 2, 2, 2; bei t = 5 und 10 ein Gebiet mit Q etwa 152 (Q_box 212,8) und Windung 1; bei t = 15 zwei
  Gebiete (Q 93,4 und 53,7) mit Windung 0 und 0. Meine Sicht auf Y1 und Y3 ist damit nicht mehr blind.

## 1. Ableitbarkeitsprobe (vor dem Lauf)

- **Y1 im Wortlaut folgt schon aus Runde 5, sobald K0 besteht.** r5.ganz_verschmolzen liefert eine Zeit nur bei
  genau einem Gebiet (nach mindestens zwei, Q_box >= 0,9 Q_box(0)). t_verschmolzen = 5 in allen vier gefuetterten
  Laeufen heisst also: n = 1 bei t = 5. Die Teilung liegt bei 10 bzw. 15, also danach. Die Zusatzreihe enthaelt
  t = 5. Y1 kann damit nur scheitern, wenn K0 reisst.
- Die neue Information der Zusatzreihe liegt daher in den beschreibenden Groessen (Abschnitt 4.6): Dauer des
  Ein-Gebiet-Zustands, Windung waehrend dieser Phase (Y3), Ladungsanteil des einen Gebiets, Ladungen und Lage der
  Bruchstuecke. Diese sind keine Kriterien der Karte; ich melde sie nur.
- Y2 (Endzahl 0) ist ebenfalls schon in Runde 5 gemessen (n Ende 0 in allen vier); hier nur Reproduktion.
- Y3 ist offen: Im 5er-Raster hatte das eine Gebiet (w60_nachbarn1) bei t = 10 noch Windung 1; was zwischen 10 und
  15 geschieht, zeigt erst die Zusatzreihe.

## 2. Code und Abweichungen

- **r5_2d_a.py unveraendert** (sha256 4b7a00b2...892bc7b, wie RUNDE-05/r5-2d-a/). Nach
  /home/fmh/fmhc-physics-remote/runde21-bio28-weiter/ kopiert, daneben bio28_weiter.py und r5_groesse_ergebnis.json
  (Kopie der Runde-5-Ausgabe, hilfs/, sha256 a708b364...2a8ecb0) fuer den K0-Vergleich.
- **bio28_weiter.py** importiert r5_2d_a und benutzt unveraendert: profile_holen (Schiessen), Gitter, ball_feld,
  entwickeln (Velocity-Verlet, Randschicht), dichten, unschaerfe, analyse (Gebiete, Schwerpunkt, Windung),
  ganz_verschmolzen, erste_dauerhaft, erhaltung, verlauf_kurz, gebiet_kurz, auswahl und alle Konstanten.
  Aufbau der Felder und Stapel wortgleich zu test_groesse (Zeilen 1282-1306).
- **Abweichungen (nur Beobachtung, kein Eingriff in die Entwicklung):**
  1. Messtakt 0,5 statt 1: r5.T_MEAS ist waehrend r5.entwickeln 0,5 (grob alle 10, fein alle 20 Schritte).
     Zeitschritt, Schrittzahl (12 000 bzw. 24 000) und Daempfung bleiben. Die Messung liest psi und psi_t nur.
  2. Eigene Messfunktion = r5.lauf_standard.messen ohne die unbenutzten Zweige r_win und radial. Gebietsanalyse an
     allen Vielfachen von 5 (Runde-5-Raster, fuer K0) und zusaetzlich an jedem Messpunkt t = 0; 0,5; ...; 30.
     Begruendung: lauf_standard koppelt den Analysetakt an T_MEAS und ANALYSE_DT fuer den ganzen Lauf; dicht bis
     t = 600 waeren 1201 statt 175 Analysen je Stufe.
  3. Zusammenfassung je Lauf wie test_groesse (Zeilen 1311-1327, dieselben Hilfsfunktionen); Index 10 statt 5 je
     Analyse, weil der Messtakt 0,5 ist.
  4. Eigene Ausgabe: bio28_weiter_roh.json (Rohdaten), bio28_weiter_ergebnis.json (Auswertung),
     bio28_weiter_bericht.txt. Keine .pt-Datei.
- **Erwartung zur Numerik [S]:** Dieselbe Entwicklung auf einer P4000 mit demselben venv sollte bitgleich sein; dann
  sind die 5er-Gebietslisten identisch (wird als "5er-Gebiete identisch" ausgegeben, kein Kriterium).

## 3. Parameter (aus dem Original, nicht geaendert)

- Modell und Numerik wie Runde 5 (PLAN 1.1): Box halbe Laenge 38,4 mit Randschicht; grob dx 0,3, dt 0,05 (n 256),
  fein dx 0,2, dt 0,025 (n 384). T = 600.
- Laeufe: omega^2 = 0,60 und 0,75; m = 1-Ball im Ursprung; k = 0, 1, 2 m = 0-Nachbarn bei (+D, 0) Phase 0 und
  (-D, 0) Phase pi; D = R_halb(m=1) + R_halb(m=0) + 3,5. Grob alle sechs (ein Stapel B = 6), fein die vier
  gefuetterten (B = 4), wie in Runde 5.
- **Gebietsschwelle (Original):** Dichte S mit Gauss Breite 1 (BLUR) geglaettet; Gebiet = geglaettetes S > 0,5 x
  Anfangsmaximum des geglaetteten S, je Lauf (SCHWELLE_REL); 4er-Nachbarschaft, periodisch; Gebiete unter 3 % der
  Anfangsladung zaehlen nicht (Q_MIN_REL).
- **Windungsmessung (Original):** Phasenumlauf auf einem Kreis um den Schwerpunkt (Gewicht S) mit dem S-gewichteten
  mittleren Abstand r_mittel, 128 Punkte, bilinear; S_min_kreis = kleinstes S auf dem Kreis als Guete (nahe null:
  unsicher).
- **Begriffe (Original):** "verschmolzen" = erste 5er-Analyse mit genau einem Gebiet, nachdem es mehrere gab, bei
  Q_box >= 0,9 Q_box(0) (ganz_verschmolzen). "Teilung danach" t_T = erste 5er-Analyse ab t_verschmolzen, ab der
  n >= 2 in drei aufeinanderfolgenden 5er-Analysen gilt (erste_dauerhaft). n_ende = Gebietszahl bei t = 600.
- **Zusatzreihe:** t = 0 bis 30 alle 0,5 (61 Proben je Lauf und Stufe): n; je Gebiet Q, Schwerpunkt X, Y, Windung,
  S_min_kreis, Eigendrehimpuls/Q, r_mittel, Flaeche, E; Q_box; alle paarweisen Schwerpunktabstaende (ohne
  periodisches Bild, wie r5.mittlerer_abstand) und d12 = Abstand der zwei ladungsstaerksten Gebiete.

## 4. Auswertung (vor dem Lauf festgelegt, im Skript so umgesetzt)

### 4.1 K0 (Y0)

- Fuer alle zehn Zeilen (grob sechs, fein vier) gegen lauf-69/ausgabe/groesse_ergebnis.json aus Runde 5:
  t_verschmolzen, t_teilung_danach und Q_box_verlust relativ auf 10 % (None nur gegen None), n_ende gleich.
- K0 bestanden, wenn alle zehn Zeilen alle vier Groessen erfuellen. Wortlaut gilt auch fuer den Rauschwert
  Q_box_verlust = 4,1e-9 (grob w60_nachbarn0); reisst K0 nur dort, melde ich das als "nicht bestanden nach
  Wortlaut" mit Ursache. Y0 = K0 bestanden.

### 4.2 Y1

- Je gefuettertem Lauf: t_T aus dem Nachrechnen (5er-Raster, Regel wie Runde 5). Y1 erfuellt, wenn es in der
  Zusatzreihe eine Probe mit t < t_T gibt mit n = 1, nach einer frueheren Probe mit n >= 2, bei
  Q_box >= 0,9 Q_box(0) (die Regel von ganz_verschmolzen, auf das 0,5-Raster angewandt). Diese Proben heissen
  Ein-Gebiet-Proben; t_1,erst und t_1,letzt sind die erste und die letzte.
- Fehlt t_T (keine Teilung im Nachrechnen): Y1 und Y3 fuer diesen Lauf offen.

### 4.3 Y2

- n_ende = 0 im Lauf.

### 4.4 Y3

- Je gefuettertem Lauf: Die Windung des einen Gebiets bei t_1,letzt (letzte Ein-Gebiet-Probe vor t_T) ist 0.
  Gleichwertig: Die Windung faellt im Ein-Gebiet-Zustand auf 0 und kehrt bis zur Teilung nicht zurueck.
  S_min_kreis wird mitgemeldet, aber nicht zum Ausschluss benutzt.
- Ohne Ein-Gebiet-Probe: Y3 offen.

### 4.5 Zusammenfassen (Zusatz der Ausfuehrung, nicht in der Karte)

- Jede Y gilt fuer "alle vier gefuetterten Laeufe" (wie Y1 in der Karte). Ausgewertet wird grob (wie die Kennzahlen
  in Runde 5); fein ist die L3-Probe:
  - grob und fein gleich: eingetroffen bzw. nicht eingetroffen
  - verschieden: offen (grob und fein verschieden)
  - ein Lauf offen: offen
- Bedeutung genau nach Karte (Y1 und Y2 / Y1 ohne Y2 / nicht Y1). Mein Skript gibt den Kartentext aus.

### 4.6 Beschreibende Groessen (Zusatz der Ausfuehrung, kein Kriterium)

- Zahl der Ein-Gebiet-Proben und laengste zusammenhaengende Folge (Proben und Zeitspanne).
- Windung und S_min_kreis an jeder Ein-Gebiet-Probe; erste Ein-Gebiet-Probe mit Windung 0.
- Ladungsanteil Q_Gebiet / Q_box an den Ein-Gebiet-Proben.
- d12 bei t = 0 und kleinstes d12 vor dem ersten Ein-Gebiet-Zustand.
- Erste Probe nach t_1,letzt und erste Probe danach mit n >= 2 ("Bruchstuecke"): Q, Windung, Lage je Gebiet;
  Q / Q_m1 und Q / Q_nachbar. Ein Bruchstueck mit Q nahe Q_nachbar und Windung 0 neben einem mit Q nahe Q_m1 und
  Windung 1 spraeche fuer unverschmolzene Nachbarn; das ist eine Lesart [H], keine Regel.

## 5. Aufrufe (.69, kleintest.sh)

- kleintest.sh (gelesen 18:14 CEST): Spur p4000a = GPU-a5689af6, p4000b = GPU-8fab62d5 (gesperrt, solange WM-1-MB
  laeuft); Python /home/fmh/fmhc-physics-gpu-venv/bin/python; systemd-run mit CPUQuota 100 %, MemoryMax 4G,
  RuntimeMaxSec 600; flock wartet bis 3600 s auf den Spur-Lock.
- Runde 5 lief auf p4000b. Ich nehme p4000b; ist sie gesperrt oder belegt, p4000a (gleiche Karte, Quadro P4000).
- Vorbereitung: rsync von r5_2d_a.py, bio28_weiter.py, r5_groesse_ergebnis.json; py_compile auf der .69; sha256
  beidseitig.
- Rauchlauf (nach dem Einfrieren): `bash kleintest.sh p4000b r21-bio28-rauch bio28_weiter.py --rauch`. Nur grob,
  t_end = 1 (vor jedem Verschmelzen), dazu Selbsttest der Auswertung mit erfundener Reihe. Zahlen ungueltig.
- Hauptlauf: `bash kleintest.sh p4000b r21-bio28-haupt bio28_weiter.py` (grob und fein in einem Aufruf, wie Runde 5).
- Laufzeit-Schaetzung (nicht gemessen): Runde 5 groesse 194 s (Schiessen 63, grob 27, fein 100). Zuschlag fuer den
  doppelten Messtakt und 2 x 54 zusaetzliche Analysen geschaetzt 10 bis 60 s; erwartet 200 bis 260 s, unter 600 s.
  Liegt die Hochrechnung aus dem Rauchlauf ueber 480 s, teile ich in `--stufe grob` und `--stufe fein` (zwei
  Aufrufe, je mit eigenem Schiessen), Nachtrag vorher.
- Ergebnisse per rsync nach lauf-69/ (lokal), Log je Aufruf nach lauf-69/*.log.

## 6. Grenzen

- Y1 im Wortlaut ist vorab ableitbar (Abschnitt 1).
- Gebietsschwelle 0,5 und Windung auf dem Kreis wie im Original; bei verformten Gebieten ist die Windung unsicher
  (S_min_kreis). Keine Anpassung nach dem Lauf.
- 2D, ein Feld, kein Bad (wie Runde 5). Explorativ.

## Einfach gesagt

Wir rechnen den Versuch aus Runde 5 noch einmal genau gleich, schauen aber in den ersten 30 Zeiteinheiten zehnmal
so oft hin. So sehen wir, ob die Nachbarbaelle wirklich zu einem Ball verschmelzen und der dann zerfaellt, oder ob
sie nur kurz aneinanderkleben und wieder auseinandergehen. Wir zaehlen die Klumpen, messen ihre Ladung und pruefen,
ob der Drehwirbel im verschmolzenen Ball bleibt.
