# Runde 22, bio28b: Laufplan

Bearbeiter: Code-Agent (Opus 5.5), Auftrag der Leitung claude-primary. Beginn 2026-10-02 19:02:45 CEST (date), Plan
begonnen 19:16:08 CEST (date). Verbindlich ist KARTE.md (Laeufe, Code und Parameter aus R5/R21, Box ohne Randverlust
bis T = 300, K0, Klassifikator aus KF-EICH, D0 bis D2, Bedeutung). Explorativ (v3), Hypothesen [H]. Vor jedem echten
Lauf geschrieben; ein dokumentierter Rauchlauf darf vorher laufen.

## 0. Gelesen und Selbstanzeige

- Gelesen:
  - KARTE.md
  - RUNDE-21/bio28-weiter: KARTE.md, PLAN.md, ERGEBNIS.md, bio28_weiter.py
  - aus lauf-69/ausgabe/bio28_weiter_roh.json: Profile, Schwellen, die n-Listen der dichten Reihe bis t = 20 und die
    5er-Listen der gefuetterten grob-Laeufe bei t = 30, 60, 100, 150, 200
  - RUNDE-05/r5-2d-a/r5_2d_a.py (Kopf, Konstanten, Schiessen, Gitter, ball_feld, entwickeln, dichten, unschaerfe,
    komponenten, windung_kreis, analyse, lauf_standard, Auswertehilfen, test_groesse, main) und PLAN.md (1.1, 1.3, 6)
  - RUNDE-06/kf5/kf5_geburt.py (ganz bis auf vergleich und bericht_text) und familie_2d_m0.json
  - RUNDE-21/kf-eich: ERGEBNIS.md, kf_eich.py (ganz)
  - auf der .69: kleintest.sh
- **Selbstanzeige (nicht blind):**
  - Aus den R21-5er-Listen kenne ich die Bahnen der Stuecke bis t = 200. Sie wandern mit |v| etwa 0,15 bis 0,28 nach
    aussen und behalten bis t = 100 bis 150 fast ihre ganze Ladung im Maskengebiet, z. B. w60_nachbarn1 92,2 und 54,3
    bei t = 100, w75_nachbarn2 2 x 37,4 bei t = 100.
  - Damit ist D1 fuer T bis etwa 150 vorgezeichnet, fuer T = 300 nicht.
  - Ueber Klassifikator-Urteile der Stuecke (D2) weiss ich nichts.

## 1. Ableitbarkeitsprobe (vor dem Lauf)

- **D0 (K0)** ist weitgehend vorab ableitbar.
  - Die neue Box enthaelt die alten Gitterpunkte, und die Startfelder sind dort gleich, bis auf Rundung von etwa 1e-14
    in den Koordinaten.
  - Die Randschicht liegt bis t = 30 weit weg (Abschnitt 2).
  - Die fruehen Zeiten sollten daher wie in R21 herauskommen. K0 kann nur an einem Fehler im Aufbau scheitern. Das ist
    der Zweck von K0.
- **D1** ist bei T = 300 nicht ableitbar. R21 zeigt nur Ladungserhalt bis etwa t = 150, danach kam der Rand.
- **D2** ist nicht ableitbar.
- **Windung 0** der Stuecke ist aus R21 bekannt. Sie wird nur berichtet, nicht gewertet (Karte).

## 2. Box, Modell, Familie (Pruefung vor dem Einfrieren)

- **Box:** r5_2d_a.py nimmt die Box nicht als Aufrufparameter. Die Karte 5 benutzt die Konstante L_STD = 38,4. Die
  Klasse r5.Gitter(L, dx) nimmt L aber als Argument. bio28b.py baut deshalb das Gitter selbst mit groesserem L, wie
  bio28_weiter.py es mit L_STD tat. r5_2d_a.py bleibt unveraendert. Die Randschicht (SPONGE 8, SIGMA0 1) bleibt, wie sie
  ist.
- **Doppelte Kantenlaenge reicht nicht.** Bei L = 76,8 begaenne die Randschicht bei Tiefe 68,8. Hochrechnung aus den
  R21-Bahnen mit fester Geschwindigkeit zwischen t = 60 und 100:
  - w75_nachbarn1, kleines Stueck: (7,5; -24,2) bei t = 100, vy -0,263 → y etwa -77 bei T = 300
  - w60_nachbarn1, kleines Stueck: y -20,7 bei t = 100, vy -0,245 → y etwa -70
  - die anderen Stuecke: Tiefe 46 bis 64
  - Mit einem Maskenradius von etwa 4 reicht das bis Tiefe etwa 81.
- **Gewaehlt: dreifache Kantenlaenge.** L = 3 x 38,4 = 115,2, n = 768 (grob) bzw. 1152 (fein). Die Randschicht beginnt
  bei 107,2, also etwa 26 Einheiten Abstand zur Hochrechnung.
  - Gleiche Gitterpunkte wie R5: x_j = -L + j dx, x = 0 liegt auf dem Gitter.
  - dx und dt unveraendert.
- **Radialtabelle:** Sie reicht bis r = 100 (r5.R_TAB). In der grossen Box liegen Ecken bis etwa r = 172 von einem Ballzentrum.
  r5.hermite setzt dort den letzten Tabellenwert ein, also f(100) kleiner als etwa 1e-21. Das Startfeld ist dort
  1e-21 statt praktisch 0. Vernachlaessigbar, nur vermerkt.
- **Modell gleich:**
  - R5: L = |psi_t|^2 - |grad psi|^2 - U(S), also psi_tt = Lap psi - U'(S) psi.
  - kf5_geburt.py: dieselbe Gleichung mit U = S - S^2 + S^3/2.
  - Gleich sind auch rho = 2 Im(psi conj psi_t), die Energiedichte und das Feldlayout [y, x].
  - kg.Gitter(2 L, dx) hat dieselben Gitterpunkte wie r5.Gitter(L, dx). Das prueft das Skript mit torch.equal, sonst
    Abbruch.
- **Familie gleich:** Die R5-Profile m = 0 liegen auf familie_2d_m0.json (Bio 18, R4).

  | omega^2 | Q R5-Profil | Q Familie | rel. | E R5-Profil | E Familie | rel. |
  |---|---|---|---|---|---|---|
  | 0,60 | 66,616033 | 66,616119 | -1,3e-6 | 56,527231 | 56,527292 | -1,1e-6 |
  | 0,75 | 19,011616 | 19,011678 | -3,3e-6 | 18,390068 | 18,390115 | -2,5e-6 |

  - **Festlegung:** Es gilt RUNDE-06/kf5/familie_2d_m0.json unveraendert (sha256 f3446207...0f806, wie KF-EICH).
  - Eine neue Familiendatei ist nicht noetig, die Pflicht-K-Pruefung entfaellt daher.
  - Als Gegenprobe des Klassifikators auf dem R5-Gitter laeuft trotzdem eine Kontrolle (4.5).
  - Die m = 1-Profile gehoeren nicht zur m = 0-Familie. Die Stuecke tragen nach R21 Windung 0, deshalb ist der Vergleich
    mit m = 0 der vorgesehene.
- **Dateien:** r5_2d_a.py (sha256 4b7a00b2...892bc7b), kf5_geburt.py (9b895c9f...b6bc0) und familie_2d_m0.json werden
  unveraendert nach /home/fmh/fmhc-physics-remote/runde22-bio28b/ kopiert, daneben bio28b.py. sha256 wird beidseitig
  geprueft.

## 3. Parameter (aus R5/R21, nicht geaendert, ausser wo vermerkt)

- **Laeufe:**
  - omega^2 = 0,60 und 0,75, m = 1-Ball im Ursprung
  - k = 1 bzw. 2 m = 0-Nachbarn bei (+D, 0) mit Phase 0 und (-D, 0) mit Phase pi
  - D = R_halb(m=1) + R_halb(m=0) + 3,5
  - Profile durch r5.profile_holen in derselben Reihenfolge wie R5/R21: (0,60; 0), (0,60; 1), (0,75; 0), (0,75; 1)
  - grob dx 0,3, dt 0,05; fein dx 0,2, dt 0,025
  - Nur die vier gefuetterten Laeufe (Karte), grob und fein.
- **Geaendert nach Karte:** Box L = 115,2 (Abschnitt 2), T = 300 statt 600.
- **Gebietsmaske (Original):**
  - geglaettetes S (Gauss Breite 1) > 0,5 x Anfangsmaximum je Lauf
  - 4er-Nachbarschaft, periodisch
  - Gebiete unter 3 % der Anfangsladung zaehlen nicht
  - Windung auf dem Kreis mit r_mittel, 128 Punkte, S_min_kreis als Guete
- **Messtakt** 0,5 wie R21. Gebietsanalyse bei t = 0 bis 30 alle 0,5 (dichte Reihe wie R21), danach alle 5. Je Analyse
  zusaetzlich die groesste Tiefe max(|x|, |y|) aller Maskenpixel.
- **Klassifikator (kf5_geburt.py, wie KF-EICH):**
  - Messfenster [T - 40, T] fuer T = 100, 200, 300, also ab 60, 160 und 260
  - Felder s, rho, e aus kg.dichten (nl = 1)
  - am Fensterbeginn kg.analyse_arm mit S0 = 0,3 (Masken S >= 0,6 und 0,9; Haupt, entscheidet D2) und S0 = 0,1
    (S >= 0,2 und 0,3; Zusatz, nur berichtet)
  - kg.fenster_probe alle 1, die erste Probe am Fensterbeginn, also 41 Proben
  - kg.fenster_auswerten am Fensterende
  - Konstanten unveraendert: FAM_TOL 0,10, KOMPAKT_FAMILIE 1,3, Q_SCHWANK 0,2, A_MIN 2, R_PLUS 6, R_SUCH 2
  - kf5_geburt.py wird nur importiert.

## 4. Auswertung (vor dem Lauf festgelegt, im Skript so umgesetzt)

### 4.1 K0 und D0

- Je Lauf und Gitter aus der dichten Reihe (bis t = 30):
  - t_V = erste Probe mit genau einem Gebiet nach einer Probe mit mindestens zwei, bei Q_box >= 0,9 Q_box(0)
  - t_T = erste Probe danach mit mindestens zwei Gebieten
  - Das ist der Wortlaut von R21 (ERGEBNIS Abschnitt 3).
- **Referenz R21** (dichte Reihe, grob und fein gleich; aus bio28_weiter_roh.json abgelesen):

  | Lauf | t_V | t_T |
  |---|---|---|
  | w60_nachbarn1 | 2,0 | 14,0 |
  | w60_nachbarn2 | 2,0 | 9,0 |
  | w75_nachbarn1 | 1,5 | 12,5 |
  | w75_nachbarn2 | 1,5 | 7,0 |

- K0 je Zeile: |t_V - Ref| <= 1 und |t_T - Ref| <= 1. Fehlt t_V oder t_T, ist die Zeile nicht bestanden.
- K0 ist bestanden, wenn alle acht Zeilen (4 Laeufe x 2 Gitter) bestehen. D0 = K0 bestanden. Fehlen Zeilen, ist D0 offen.

### 4.2 Stuecke und Verfolgung

- **Teilungszeit** = t_T aus 4.1. **Stuecke** = die Gebiete der Maske bei t_T.
- **Rangfolge:** Q absteigend. Bei Gleichstand (Q innerhalb 1 %) steht das Stueck mit groesserem Y vorn. Der Rang
  identifiziert ein Stueck zwischen grob und fein (gleicher Lauf, gleicher Rang).
- **Verfolgung:** In jeder spaeteren Analyse (bis 30 alle 0,5, danach alle 5) gehoert zu jedem Stueck das Gebiet, dessen
  Schwerpunkt dem letzten bekannten Schwerpunkt des Stuecks am naechsten liegt, hoechstens 5 entfernt. Sonst gilt das
  Stueck dort als nicht gefunden und behaelt seine letzte Lage.
- **Je T = 100, 200, 300 und Stueck:**
  - Q im Gebiet und Anteil = Q / Q(t_T)
  - Schwerpunkt, Geschwindigkeit |P|/E des Gebiets, Windung mit S_min_kreis, r_mittel, Flaeche
- **Verschmolzene Stuecke:** Faellt ein Gebiet mehreren Stuecken zu, zaehlt es als ein Stueck. Sein Anteil ist dann
  Q / (Summe der Q(t_T) dieser Stuecke).

### 4.3 D1

- Je Lauf und Gitter bei T = 300: die verschiedenen Gebiete mit Stuecken zaehlen, deren Anteil >= 0,5 ist.
- Der Lauf erfuellt D1, wenn es mindestens zwei sind. Ohne Teilung bis t = 30 ist er nicht erfuellt.
- Je Gitter: D1 gilt, wenn mindestens 3 von 4 Laeufen D1 erfuellen.
- Gesamt:
  - grob und fein gleich: eingetroffen bzw. nicht eingetroffen
  - verschieden: offen (grob und fein verschieden)
  - fehlt ein Gitter: offen

### 4.4 Klassifikator je Stueck und D2

- **Zuordnung:** Massgeblich ist der Fenstertropfen, der am naechsten an der Lage des Stuecks bei T - 40 startet (x0, y0
  der ersten Probe), hoechstens 5 entfernt. Die Lage bei T - 40 stammt aus der Verfolgung (BALL_SUCH wie KF-EICH).
  Ohne einen solchen Tropfen lautet die Klasse "kein Tropfen".
- **Urteil:**
  - Klasse aus fenster_auswerten: auf, neben, unentschieden, ausserhalb, gestoert oder nicht rund
  - "rund" = rmax/R_A <= 1,3 am Fensterbeginn (KOMPAKT_FAMILIE)
  - gemeldet mit rmax/R_A, Q_net, omega_ruhe +- u, dQ und v
- **D2 je Stueck und Gitter:** Das Stueck ist bei T = 300 gefunden, sein Anteil ist >= 0,5, und es ist bei S0 = 0,3
  "auf" und "rund".
- **D2 eingetroffen,** wenn mindestens ein Stueck (gleicher Lauf, gleicher Rang) das auf beiden Gittern erfuellt.
  - Sonst nicht eingetroffen, wenn beide Gitter vollstaendig sind.
  - Ist die Kontrolle (4.5) nicht bestanden oder fehlt sie: offen.

### 4.5 Kontrolle (Gegenprobe des Klassifikators auf dem R5-Gitter, Zusatz)

- **Aufbau:** Je ein einzelner ruhender m = 0-Ball aus r5.profile_holen, omega^2 = 0,60 (wie die w60-Nachbarn) und 0,70
  (Q 24, wie das kleinere w75-Stueck). Er sitzt im Ursprung der R5-Box (L 38,4, mit Randschicht), grob und fein, T = 300,
  mit denselben Fenstern.
- **Bestanden,** wenn bei S0 = 0,3 alle 12 Urteile (2 Baelle x 2 Gitter x 3 T) "auf" und "rund" sind. Gezaehlt wird der
  Tropfen nahe (0, 0), hoechstens 5 entfernt. S0 = 0,1 wird nur berichtet.
- **Warum:** KF-EICH hat bei dx 0,25 und 0,125 geeicht, R5 rechnet mit 0,3 und 0,2.
  - Nicht bestanden heisst: D2 ist offen.
  - Die R5-Profile 0,60 und 0,70 liegen in der Familie (0,60 oben gezeigt; 0,70 ist ein Knoten der Tabelle).
- **Bewusst nicht gewaehlt: der m = 0-Ball bei 0,75.** Er hat S_max = 0,6955. Seine Maske S >= 0,6 haette nur einen
  Radius von etwa 0,8, das sind etwa 21 Gitterpunkte bei dx 0,3, also Flaeche 1,9 < A_MIN 2 [S, Schaetzung aus der
  Krummung im Zentrum]. Dort gaebe es "kein Tropfen". Das waere ein Schwellenbefund des Werkzeugs und keine
  Uebertragungsfrage.

### 4.6 Box-Pruefung

- **Bestanden,** wenn in allen acht Laeufen die groesste Tiefe max(|x|, |y|) aller Maskenpixel bis T = 300 unter
  L - 8 = 107,2 bleibt.
- Zusaetzlich gemeldet: Q_box(300) / Q_box(0) und die Tiefe der Stueckschwerpunkte.
- **Reisst die Box-Pruefung:** Dann werden D1 und D2 trotzdem nach Wortlaut ausgewertet. Die Verletzung wird gemeldet,
  und die Bedeutung erhaelt den Vorbehalt "Rand erreicht".

### 4.7 Bedeutung (Wortlaut der Karte, Skript gibt sie aus)

- D1 und D2 eingetroffen: Der gefuetterte Drehball zerfaellt in Q-Ball-Toechter ohne Windung. Das ist eine Teilung,
  aber keine Groessengrenze im Sinn von Bio 28 [H].
- D1 nicht eingetroffen: Die Toechter zerfliessen auch ohne Rand.
- Sonst: Die Karte ordnet keine Bedeutung zu. Ich berichte die Ausgaenge ohne Deutung.

### 4.8 Beschreibend (kein Kriterium)

- Je Stueck berichtet: Windung und S_min_kreis bei T (nur berichtet), Jspin/Q, alle Gebiete bei T (auch Nebenstuecke),
  S0-0,1-Urteile und Q_box-Reihe alle 5.

## 5. Aufrufe (.69, kleintest.sh)

- **kleintest.sh** (gelesen 19:09 CEST):
  - Spur p4000b = GPU-8fab62d5, gesperrt, solange WM-1-MB laeuft; p4000a = GPU-a5689af6
  - systemd-run mit CPUQuota 100 %, MemoryMax 4G, RuntimeMaxSec 600, PYTHONDONTWRITEBYTECODE=1
- **GPU-Speicher um 19:09:** p4000a 6,5 von 8 GB belegt, p4000b 6,4 von 8 GB, durch fremde Dienste. Frei sind etwa
  1,6 bis 1,8 GB. Der Rauchlauf misst den eigenen Hoechstwert.
- **Vorbereitung:**
  - rsync von bio28b.py, r5_2d_a.py, kf5_geburt.py und familie_2d_m0.json
  - py_compile auf der .69
  - sha256 beidseitig
- **Rauchlauf** (vor dem Einfrieren erlaubt, dokumentiert):
  - Aufruf `bash kleintest.sh p4000b r22-bio28b-rauch bio28b.py --gruppe rauch`
  - grob, volle Box, B = 4, T = 6, ein Fenster [2, 6]
  - dazu der Selbsttest der Auswertung mit einer erfundenen Reihe
  - Zahlen ungueltig. Gemessen werden ms je Schritt, Analysezeit, Fensterzeit und GPU-Speicher.
- **Hauptlaeufe** nach dem Einfrieren, Spur p4000b, bei Belegung p4000a:
  1. `--gruppe grob`
  2. `--gruppe fein-w60`
  3. `--gruppe fein-w75`
  4. `--gruppe kontrolle`
  5. `--auswerten lauf-69/ausgabe`, Spur cpu, ohne GPU, nur JSON
- **Laufzeit-Schaetzung** (nicht gemessen; R21: 5,2 ns je Gitterpunkt und Schritt):
  - grob: 2,36 Mio. Punkte x 6000 Schritte etwa 74 s, dazu Schiessen 63 s, Analysen etwa 30 s und Fenster, zusammen
    etwa 190 s
  - fein je Paar: 2,65 Mio. Punkte x 12 000 Schritte etwa 165 s, zusammen etwa 270 s
  - Kontrolle: etwa 100 s
- **Wachter im Skript:** Bei t = 40 rechnet das Skript die Gesamtdauer hoch. Liegt die Prognose ueber 570 s, bricht es
  ab, bevor RuntimeMaxSec greift.
- **Teilungsregel:** Ist die Hochrechnung aus dem Rauchlauf fuer einen Aufruf groesser als 480 s, teile ich die
  fein-Paare in Einzellaeufe. Das waere eine neue Gruppe, Nachtrag vor dem Lauf.
- **Ergebnisse:** per rsync nach lauf-69/ (lokal), Log je Aufruf nach lauf-69/*.log.
- **Technischer Abbruch** (Speicher, Zeit, Absturz): denselben Aufruf unveraendert wiederholen, Vermerk im Ergebnis.
  Kein Wechsel von Parametern.

### 5.1 Rauchlauf (vor dem Einfrieren, Zahlen ungueltig)

- **Lauf:** p4000b, 17:17:46 bis 17:19:39 UTC (19:17:46 bis 19:19:39 CEST), rc 0. Der Lock war etwa 40 s belegt, die
  Unit lief 71 s. Log: lauf-69/RAUCH.log.
- **Gemessen:**
  - Schiessen 63,6 s
  - grob, n 768, B 4: 14,62 ms je Schritt
  - 13 Analysen in 1,7 s (0,13 s je Analyse)
  - 5 Fensterproben in 1,0 s, mit analyse_arm am Fensterbeginn
  - GPU hoechstens 570 MB
  - Selbsttest der Auswertung: ok, alle Sollwerte getroffen
  - Rauch-K0: grob w60_nachbarn1 hat t_V 2,0 wie R21; t_T fehlt, weil T nur 6 ist
- **Hochrechnung:**
  - grob: 64 + 6000 x 14,6 ms (88 s) + 115 Analysen (15 s) + 123 Fensterproben (etwa 25 s), also etwa 190 s
  - fein je Paar: Gitterpunkte x 1,125, FFT-Groesse 1152 vorsichtig mit 18 ms je Schritt: 64 + 216 + 20 + 25, also
    etwa 330 s; GPU etwa 650 MB
- **Entscheidung:** Alle Aufrufe liegen unter 480 s, also bleibt es bei den Gruppen aus Abschnitt 5, ohne weitere
  Teilung.
- **Eine Zahl habe ich gesehen:** die Rauch-Fensterklassen bei T = 6, waehrend des Verschmelzens ("ausserhalb",
  "neben", "unentschieden"). Sie betreffen keine Vorhersage.

## 6. Grenzen

- Das R5-Modell bleibt: 2D, ein Feld, Futter statt Bad.
- Der Klassifikator ist im Vakuum und fuer m = 0 geeicht. "auf" heisst "Q passt zu omega" innerhalb 10 %, nicht
  "unangeregt" (KF-EICH, Satz A).
- Die Maske zaehlt verbundene Lappen als ein Gebiet. Die Verfolgung ueber den naechsten Schwerpunkt kann bei
  Teilungen der Stuecke dem groesseren Teil folgen.
- Q im Maskengebiet erfasst den Schwanz unter der Schwelle nicht. Der Anteil vergleicht deshalb Gleiches mit Gleichem
  (Maske bei t_T und bei T).
- Die Ableitbarkeit von D0 steht in Abschnitt 1.

## Einfach gesagt

In Runde 21 sind die Bruchstuecke des gefuetterten Drehballs am Rand der Box verschluckt worden, bevor wir sehen
konnten, ob sie als Baelle weiterleben. Jetzt rechnen wir denselben Versuch in einer dreimal so breiten Box bis zur
Zeit 300. So kommen die Stuecke nicht an den Rand. Wir verfolgen jedes Stueck, messen seine Ladung und fragen das in
KF-EICH gepruefte Messgeraet, ob es wie ein echter ruhiger Q-Ball aussieht. Zur Sicherheit pruefen wir das Messgeraet
vorher an perfekten Baellen auf demselben Gitter.
