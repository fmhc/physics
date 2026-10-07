# Runde 7, Karte RING: Laufplan

Bearbeiter: Anthropic-Agent (Opus 5.5) im Auftrag der Leitung claude-primary. Beginn 2026-09-30 04:02:10 CEST (gemessen),
Ende in der letzten Zeile. Explorativ (v3), keine formale Bestaetigung. Literatur aus dem Gedaechtnis [L], nicht
nachgelesen; Papierwerte [S].

Status: **Code geschrieben, lokale Formprobe gelaufen (CPU, 1 Thread, nice 19, timeout 120, Mini-Gitter, alle
Unterbefehle rc 0). Messlaeufe nicht gerechnet.**

## Kurzfassung

- **Code:** ring.py (PyTorch, float64/complex128, `--geraet cuda|cpu`, cpu nur mit `--rauch --mini`). Unterbefehle
  `profile`, `wirbel`, `teilung`, `vierer`, dazu `alle --rauch`. Rohdaten je Stufe sofort nach der Zeitentwicklung
  (`<karte>_<stufe>_roh.pt`), danach Bericht und JSON je Stufe; L3 entsteht, sobald grob und fein im selben Ordner liegen.
- **Grundlage:** Bausteine aus r5_2d_b.py (Schiessen mit berichtigter Regel fuer m != 0, Profilcache, Baelle, Boost,
  Verlet, Klumpen, Windung, Verfolger, Ringaufbau) und r5_2d_a.py (Stoerfaktor, A_l, Vieleck), unveraendert uebernommen.
  Neu: Messabstand 0,5 mit Verlustraten der Randschicht (Bilanz), Klumpenfenster, Windung auf acht Kreisen,
  Wirbelzaehlung, Radialprofil, C4-Projektion, Saat auf einem Ball (Liste im Kopf von ring.py).
- **Laufzeit P4000 (Schaetzung):** je Aufruf 2 bis 4,5 min, neun Aufrufe, zusammen etwa 30 min.
- **Ausgangslage (Berichtigung der Leitung, eingegangen etwa 04:35):**
  - J/Q ~ 1,04 (N6_k1_dreh+) bzw. 1,03 (N8_k1_dreh+) sind Startwerte, per Aufbau gesetzt.
  - J faellt waehrend des Laufs um 11 bis 12 % (181,6 -> 159,1 bzw. 242,1 -> 214,4). J/Q des Klumpens am Ende steht in
    keinem Bericht.
  - Belegt ist nur: ein Klumpen mit Windung 1 am Ende (N6 grob und fein, N8 nur grob). Auch der ruhende Ring N8_k1 endet
    mit Windung 1. Ein ruhiger m = 1-Ball ist nicht belegt.
  - ring.py misst J/Q des Klumpens selbst: Fenster um den Schwerpunkt, J um den Schwerpunkt, je Messung.
- **Kernvorhersagen:**
  - (a) Der Klumpen aus dem mitdrehenden Ring hat Windung 1 und J/Q etwa 1. Frequenz und Profil liegen nahe am
    m = 1-Ball gleicher Ladung. Ob er bis T = 3000 haelt, ist offen; die Vorschau deutet auf eine l = 3-Instabilitaet
    (offengelegt in 0.2).
  - (b) Der Vierer-Ring ist kein stabiler Verbund. Erwartet: im symmetrischen Sektor schwingt er gebunden (p = 0,55). Ohne erzwungene Symmetrie
    bricht die Symmetrie durch Ladungstausch zwischen den Diagonalpaaren mit Rate etwa 0,07; das beginnt schon im
    R5-Lauf kurz vor T = 500.

## 0. Hinweise an die Leitung

### 0.1 Lokale Formprobe (Laptop, Vorschau, kein Ergebnis)

- Freigabe: weitergeleitet von der Leitung (Finn 30.09. 02:42; Memory "Lokale Laeufe: seit 30.09. kleine erste Runs
  erlaubt"). Eingehalten: nur CPU (`CUDA_VISIBLE_DEVICES=`), 1 Thread, nice 19, timeout 120 s, Mini-Gitter, Ausgaben nur
  in `lauf-lokal/`.
- Aufruf je Unterbefehl:

```
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-07/ring && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  nice -n 19 timeout 120 python3 ring.py <karte> --rauch --mini --geraet cpu --out lauf-lokal --cache lauf-lokal/profil_cache_mini.pt
```

- Gerechnet (Zeiten gemessen, rc je 0):
  - profile 04:24:33 bis 04:24:57 (39 Profile in 21,5 s)
  - wirbel 04:25:04 bis 04:25:16
  - teilung 04:25:29 bis 04:25:41
  - vierer 04:26:14 bis 04:26:23
  - Nach den Aenderungen unten nochmals teilung, vierer und wirbel: 04:28:42 bis 04:29:20.
  - wirbel mit `--laeufe` (Saatlaeufe): 04:30:08 bis 04:30:12.
  - Nach der L3-Aenderung (Bruchzeit nur mit Saat) wirbel: 04:34:54 bis 04:35:11. Nach Einbau von N8_ruhend die
    Saatlaeufe mit N8_ruhend: 04:35:40 bis 04:35:46.
  - Zusatzvorschau vierer, laenger: Kopie im Scratchpad mit Rauchfaktor 0,15 statt 0,02 (T = 300, dx 0,6), Laeufe
    n4_windung, _sym, _s1e-3, _s1e-6, Ausgabe lauf-lokal/vierer-lang/: 04:36:48 bis 04:37:07, rc 0. Gerechnet nach dem
    Niederschreiben der Vorhersagen in 4.3.
- Dabei gefunden und behoben:
  - Sektorprobe: Der Rand der periodischen Box bricht die C4-Symmetrie des Startfelds auf dem Niveau des Feldschwanzes
    am Rand (etwa 3e-9). Grund: Zeile x = -L hat kein Gegenstueck bei x = +L. Die Schranke steht jetzt bei 1e-7 statt
    1e-12. Fuer die Dynamik ist das belanglos; die Stoerung sitzt in der Randschicht und klingt nach innen wie
    e^{-kappa d} ab.
  - Wachstumsratenfit der Ladungsspreizung erfasste die Anfangsschwingung der Saat. Das Fenster beginnt jetzt beim
    10-fachen Startwert, bis 3e-2, und verlangt einen Faktor 20.
  - Teilung der Ringklumpen: Die Klumpenschwelle haengt am Anfangsmaximum, und die Saat hebt dieses Maximum. Dazu kommt
    eine schwellenfreie Probe: Die Fensterladung faellt unter die Haelfte ihres Werts bei t_ref.
  - Selbstprobe des Profilvergleichs (stationaerer m = 1-Ball gegen sein eigenes Profil) als Schranke eingebaut.
- Die Rechenzeit im CPU-Log gilt nicht fuer die GPU.

### 0.2 Was ich vor und nach der Vorschau wusste (Offenlegung)

- **Vor den Vorhersagen gelesen** (vorhandene Daten aus Runde 5):
  - Zeitreihe von n4_windung in r5-2d-a/lauf-69/ausgabe/vielzeller_ergebnis.json
  - Ringradius: schwingt zwischen 5,53 und 6,17 mit etwa 150 Zeiteinheiten Periode.
  - Das Quadrat dreht sich im Uhrzeigersinn, gegen die Phasenwindung, um etwa 100 Grad in 500 Zeiteinheiten.
  - Die vier Klumpenladungen laufen ab t = 415 auseinander: Spreizung 4e-4, bei t = 470 1,7e-2, bei t = 500 0,31,
    Diagonalpaar gegen Diagonalpaar. Das ergibt von Hand eine Rate von etwa 0,07.
  - Die Vorhersagen zu (b) bauen darauf auf.
- **Vorhersagen** (Abschnitte 2.3, 3.3, 4.3):
  - Vor der Vorschau im Kopf festgelegt, aber erst danach niedergeschrieben; deshalb nur mit Vorbehalt L1.
  - Wo die Vorschau eine Zahl beeinflusst hat, steht "nach Vorschau".
- **Vorschau** (Mini-Gitter dx 0,6, T = 40 bis 60; nicht als Ergebnis zu werten):
  - teilung: 0,65 teilt sich bei t = 50 mit gamma 0,0925 (R5: 0,0926). Bei 0,625 waechst A_2 mit etwa 0,063.
    0,55 bis 0,60 sind bis T = 60 ruhig.
  - Selbstprobe: Profil-L2 0,008 bis 0,016; omega_eff trifft omega_m1(Q) auf 0,1 %.
  - wirbel: Die Ringe verschmelzen bei t = 5 zu einem Klumpen mit Windung 1 auf allen Kreisen.
    - J/Q im Fenster 0,97 bis 0,98, E/Q etwa 5 % ueber dem m = 1-Ball gleicher Ladung.
    - **Mit Saat 1e-2 zerfallen beide Ringklumpen bis t = 60 in 3 Klumpen mit Windung 0 (Dreieck, l = 3).**
    - Mit Saat 1e-3 bzw. 1e-4 waechst A_3 bis t = 60 auf 0,065 bzw. 0,007, also etwa mit Rate 0,08.
    - Ohne Saat bleibt A_3 bei 0: Die gemeinsame Symmetrie von Gitter und Ring (C2 bei N6, C4 bei N8) verbietet l = 3.
      l = 3 waechst dann nur aus Rundung.
  - N8_ruhend (nach der Berichtigung eingebaut): ein Klumpen ab t = 10 mit W = 1 auf allen Kreisen; J/Q im Fenster
    0,65 bei t = 30 bis 60 (Start 0,61).
  - vierer: Das Quadrat dreht sich mit -5,2e-3 (im Uhrzeigersinn, wie in R5). Die Spiegelprobe (n4_gegen) stimmt auf
    3e-16.
  - vierer lang (T = 300, nach 4.3 gerechnet): s1e-3 Ladungstausch bei t = 81,5, verschmolzen bei 115; s1e-6 bei
    195,5 bzw. 230, gamma 0,059; Saatprobe dt x gamma / ln 1000 = 0,98. n4_windung ohne Saat und _sym bis 300 ganz;
    _sym: Radius 5,55 bis 6,20, Mittel 5,91, Drift +1,5 % ueber das Fenster, Umkehrpunkte ergeben Periode etwa 200.

### 0.3 Verstoss (Selbstanzeige)

Zwischen 04:02 und 04:13 CEST (nicht genau gemessen) stand vor einer jq-Abfrage versehentlich `python3 -c "print('x')"`.
Das ist ein lokaler Interpreterstart ohne Zweck, genau das Muster aus der Memory-Notiz. Gerechnet wurde nichts. Bitte ins
Arbeitsfeld und in den Fehlerkasten uebernehmen; ich schreibe dort nicht selbst.

### 0.4 Reihenfolge

1. `alle --rauch` (GPU-Rauchtest; schiesst zuerst alle 39 Profile und fuellt `profil_cache.pt` neben dem Skript; der
   Cache gilt auch fuer die Hauptlaeufe, Schluessel enthaelt alle Schiessparameter)
2. `profile` (Bericht; aus dem Cache in Sekunden)
3. die uebrigen Aufrufe in beliebiger Reihenfolge, auch parallel auf p4000a und p4000b (Abschnitt 6)

## 1. Festlegungen fuer alle Unterbefehle (vor dem Lauf)

### 1.1 Modell und Numerik

- Modell wie Runde 5: L = |psi_t|^2 - |grad psi|^2 - U(S), U = S - S^2 + S^3/2, ein Feld.
- Unveraendert: Schiessen (RK4, h = 0,01, bis r = 60, 2048 Kandidaten, 5 Runden), Radialtabelle bis 100, Randschicht
  (Breite 8, sigma = (Tiefe/8)^2), spektraler Laplace, Velocity-Verlet, grob dx 0,3 / dt 0,05, fein dx 0,2 / dt 0,025.
- Profilgitter: m = 1 bei omega^2 = 0,540 bis 0,660 (Schritt 0,005), m = 0 bei 0,54 bis 0,66 (Schritt 0,01) und 0,70.
  "m = 1-Ball gleicher Ladung" = lineare Interpolation in ln Q zwischen den zwei Nachbarzeilen, ohne Extrapolation.

### 1.2 Messgroessen

- **Je Messung** (T_MEAS = 0,5):
  - Q_Box, E_Box, J_Box (um den Ursprung), S_max
  - Verlustraten der Randschicht: L_Q = Int sigma rho, L_J = Int sigma j_z, L_E = Int 2 sigma |psi_t|^2
- **Klumpenfenster** (wirbel r_win = 15, teilung R_halb + 12) um den verfolgten Schwerpunkt (Gewicht S^2):
  - Q_w, E_w, N_w = Int S
  - J_w um den Schwerpunkt, Impuls
  - omega_eff = Q_w/(2 N_w); fuer einen stationaeren Ball exakt omega
  - omega_loc = Int S rho/(2 Int S^2)
  - S_max, A_l (l = 1..6)
- **Je Analyse** (alle 5):
  - Klumpen wie r5_2d_b.py, mit Windung
  - im Fenstermodus: Windung auf Kreisen r = 1, 2, 3, 4, 5, 6, 8, 10 um den Schwerpunkt, mit S_min je Kreis
    ("sicher" ab S_min >= 0,05)
  - Wirbelzaehlung ueber den Phasenumlauf je Gitterplakette: +1 und -1 in r < 4 und r < 8, Abstand des naechsten Wirbels
  - Radialprofil S(r) in Ringen der Breite 0,25 bis r = 16
- **Vierer:** Verfolger je Ball wie r5_2d_b.py (Fenster 3,13). Daraus:
  - Ringradius r(t): mittlerer Abstand vom gemeinsamen Mittelpunkt
  - mittlerer Paarabstand, wie der "Abstand" in R5
  - Ladungsspreizung (max - min)/Mittel der vier Ballladungen
  - Drehwinkel von Ball 0

### 1.3 Bilanz und Schranken (Kontrolle c)

- **Bilanz je Lauf:** Rest(t) = X_Box(t) + X_geschluckt(t) - X_Box(0), X_geschluckt aus der Trapezregel der Raten.
  - Toleranz (vorab): max |Rest| <= 1e-3 Q_Box(0) fuer Q, 3e-3 Q_Box(0) fuer J, 1e-3 E_Box(0) fuer E.
  - Q ist im Verlet-Verfahren exakt erhalten (Formprobe ohne Randverlust: Rest 3e-16). Der Q-Rest misst also nur den
    Quadraturfehler der Verlustrate.
  - Der J-Rest misst zusaetzlich die Gitteranisotropie.
- **Schranken je Lauf:**
  - Startzerlegung (n Klumpen = Ballzahl)
  - 0 < omega_eff < 1 (gebundener Klumpen)
  - Q_w <= 1,01 Q_Box(0)
  - Profilvergleich eingeschachtelt (keine Extrapolation)
  - teilung: Selbstprobe; ein stabiler m = 1-Ball passt zu seinem eigenen Profil mit L2 < 0,05. Damit ist die
    Vergleichsmethode von (a) geeicht.
  - vierer: Sektorprobe des Startfelds. Ohne Saat <= 1e-7 (Randartefakt), mit Saat eps = 0,433 eps auf 5 %.

### 1.4 L3

- wirbel: N6_dreh+, N8_dreh+ und N6_dreh+_s1e-2 fein bis T = 1000. Bestanden, wenn:
  - ein Klumpen ab gleicher Zeit (auf 10 genau)
  - nur mit Saat: Bruch ja/nein gleich, Bruchzeit innerhalb max(10 %, 10). Bruch = Teilung nach dem Verschmelzen oder
    Fensterladung unter 1/2. Ohne Saat waechst jede Stoerung aus Rundung; die Bruchzeit ist dort nicht vergleichbar.
  - |dJ/Q| <= 0,01 und |d omega_eff/omega_eff| <= 0,005 an den Reihenzeiten 100, 250, 500, 1000, soweit sie 50 vor dem
    frueheren Bruch liegen
- teilung: 0,59 und 0,625 fein bis T = 1500. Bestanden bei gleichem Ausgang, t_teilung innerhalb max(10 %, 10) und gamma
  innerhalb 20 %.
- vierer: n4_windung_sym und n4_windung_s1e-6 fein bis T = 1000. Bestanden, wenn:
  - Radius an den Reihenzeiten innerhalb 1 %
  - t_Bruch innerhalb max(10 %, 10)
  - gamma innerhalb 10 %

## 2. Frage (a): Wirbelball aus dem Ring (`wirbel`)

### 2.1 Aufbau

- Wie `ringe` in r5_2d_b.py: Baelle m = 0 bei omega^2 = 0,70 (Q 24,0, R_halb 1,92), Abstand d = 7,83, Radius
  R = d/(2 sin(pi/N)), Phase 2 pi j/N.
- Tangential gegen den Uhrzeigersinn mit gamma E v R = Q je Ball (v = 0,134 bei N6, 0,103 bei N8). Box L = 48.
- T = 3000 grob, 1000 fein.

| Lauf | N | Saat (Stoerfaktor l = 1..6 am Ringradius) | Zweck |
|---|---|---|---|
| N6_dreh+ | 6 | 0 | = N6_k1_dreh+ aus ringe, lang |
| N8_dreh+ | 8 | 0 | = N8_k1_dreh+ aus ringe, lang |
| N6_dreh+_s1e-2, N8_dreh+_s1e-2 | 6, 8 | 1e-2 | Robustheit gegen Asymmetrie |
| N6_dreh+_s1e-3, N6_dreh+_s1e-4 | 6 | 1e-3, 1e-4 | Saatreihe: waechst eine Mode mit fester Rate? |
| N8_ruhend | 8 | 0 | = N8_k1 aus ringe: Phasenstufe ohne Drehung; entsteht derselbe Wirbelball? |

### 2.2 Papier [S]

- Ladung und Drehimpuls **am Start**, per Aufbau (wie ringe; Berichtigung der Leitung):
  - N6: Q_Box 174,3, J 181,6 (J/Q 1,042)
  - N8: Q_Box 235,3, J 242,1 (J/Q 1,029)
  - N8_ruhend: J/Q 0,615
- Box bei T = 500, von Hand aus J_Ende und Q-Verlust im ringe-Bericht. Das sind Werte der Box (Klumpen plus Strahlung
  in der Box), nicht des Klumpens:
  - N6_k1_dreh+: J/Q 159,1/165,1 = 0,96
  - N8_k1_dreh+: 214,4/215,3 = 1,00
  - N8_k1 ruhend: 200,5/201,0 = 1,00; J stieg dort von 136,7 auf 200,5, also muss Strahlung negativen Drehimpuls
    abgefuehrt haben.
  - Q ist groesser als N x 24, weil die Boost-Phase die Kontaktphase auf etwa 15 Grad drueckt. Die Ueberlappung zaehlt
    dann fast gleichphasig.
- m = 1-Ball gleicher Ladung (Profiltabelle der Formprobe; gleiche Werte wie R5 bei 0,55/0,60/0,65):
  - Q = 160: omega^2 = 0,589, E/Q 0,873
  - Q = 208: omega^2 = 0,573, E/Q 0,85
  - m = 0 bei Q = 160: omega^2 = 0,562. Die Frequenz trennt m = 1 und m = 0 gleicher Ladung also nur um etwa 2,4 %.
    Das Profil trennt stark (Loch gegen Kuppe).
- R5 teilung: m = 1 bei 0,55 (Q 370) stabil bis 600; bei 0,65 (Q 94) Teilung bei t = 50 in 2 Toechter, l = 2. Die
  Ringklumpen (Q etwa 160 bis 210) liegen genau in der ungeprueften Luecke.
- Symmetrie: Das Gitter ist nur unter 90 Grad symmetrisch.
  - N6-Ring und Gitter teilen C2. Dichtemoden mit ungeradem l (l = 3) entstehen nur aus Rundung.
  - N8 teilt C4. l = 2 und l = 3 entstehen nur aus Rundung; bei N6 saet die Diskretisierung l = 2 und l = 4.
  - Deshalb die Saatlaeufe.

### 2.3 Vorhersagen

| Nr. | Groesse | Vorhersage |
|---|---|---|
| A1 | Windung | Solange ein Klumpen: W = 1 auf allen sicheren Kreisen r = 2 bis 8 in mindestens 95 % der Analysen ab T/2; genau ein +1-Wirbel in r < 4, kein Gegenwirbel; p = 0,85 |
| A2 | J/Q (Fenster) | bei t = 250 bis 500 zwischen 0,95 und 1,05, p = 0,8; spaet 1,00 +- 0,02, falls ein Klumpen bleibt, p = 0,7 |
| A3 | Frequenz | omega_eff innerhalb 2 % von omega_m1(Q_w) und naeher an m = 1 als an m = 0, p = 0,6 |
| A4 | Profil | spaetes Mittel: L2 gegen m = 1 unter 0,15 und mindestens 30 % kleiner als gegen m = 0, p = 0,55; E/Q hoechstens 3 % ueber m = 1, p = 0,5 |
| A5 | Dauer ohne Saat | vor Vorschau: N6 bleibt bis T = 3000 ein Klumpen mit W = 1 (p = 0,6), teilt sich (p = 0,3). N8 bleibt (p = 0,65). **Nach Vorschau:** N6 zerfaellt nach t = 350 bis 700 in 3 Klumpen (Rundungssaat, Rate etwa 0,08), p = 0,45; N8 bleibt laenger ganz als N6, p = 0,6 |
| A6 | Saatreihe (nach Vorschau) | s1e-2: Zerfall in 3 Klumpen vor t = 100 (p = 0,7). Zerfallszeit (Fensterladung < 1/2 oder 3 Klumpen) waechst je Dekade Saat um ln(10)/gamma, also 25 bis 40 (p = 0,5) |
| A7 | N8_ruhend (nach Berichtigung, nach Vorschau) | ein Klumpen ab t = 5 bis 15 mit W = 1 (p = 0,85); Klumpen-J/Q steigt von 0,61 und liegt bei t = 500 zwischen 0,95 und 1,05, weil Strahlung negativen Drehimpuls abfuehrt (p = 0,6); danach wie N8_dreh+ (p = 0,5) |

### 2.4 Kriterien (im Bericht)

- "Wirbelball" (Frage a beantwortet mit ja), wenn gleichzeitig:
  - A1 erfuellt
  - J/Q spaet 1,00 +- 0,03
  - omega_eff innerhalb 2 % von omega_m1
  - Profil-L2(m = 1) < 0,15 und < 0,7 x L2(m = 0)
  - kein Zerfall bis T
- "Wirbelball auf Zeit": dasselbe bis zu einem Zerfall, dessen Zeit mit ln(1/Saat) waechst. Dann schuetzt nur die
  Symmetrie des Startfelds den Wirbel.

## 3. Frage (a), Anschluss Teilung (`teilung`)

### 3.1 Aufbau

- Ruhender m = 1-Ball bei omega^2 = 0,55 / 0,575 / 0,59 / 0,60 / 0,625 / 0,65 (Q 370 / 199 / 157 / 139 / 110 / 94).
- Stoerfaktor wie r5_2d_a.py (l = 1..6, je 0,01 bei r_s = max(R_max, 0,7 R_halb), Phase 2,4 l). Box L = 38,4.
- T = 3000 grob, 1500 fein (0,59 und 0,625).
- 0,55 und 0,65 sind die R5-Kontrollen: 0,55 stabil bis 600; 0,65 geteilt bei 50, gamma 0,093.

### 3.2 Messung

- Wie R5:
  - Teilung = mindestens 2 Klumpen in 3 Analysen; Toechter 30 nach der Teilung
  - l_dom, gamma aus ln A_l
- Neu:
  - schwellenfreie Probe (Fensterladung < 1/2 von Q_w(0))
  - A_l-Maxima ueber T
  - fuer stabile Baelle J/Q, omega_eff, Windungen und Selbstprobe des Profils

### 3.3 Vorhersagen (vor Vorschau; die Vorschau bis T = 60 aendert daran nichts ausser dem Hinweis auf 0,625)

- 0,55 ruhig bis 3000 (p = 0,85); 0,65 Teilung bei 40 bis 60, gamma 0,08 bis 0,11, l = 2, zwei Toechter mit W = 0
  (p = 0,9).
- 0,575 ruhig (p = 0,65); 0,59 ruhig (p = 0,6); 0,60 ruhig (p = 0,5); 0,625 geteilt (p = 0,6).
- Schwelle zwischen 0,60 und 0,625 (p = 0,4), zwischen 0,575 und 0,60 (p = 0,25), anderswo (p = 0,35).
- Wo geteilt: l_dom = 2, Toechter W = 0 (p = 0,8); gamma faellt zur Schwelle hin monoton (p = 0,7).
- Selbstprobe: stabile Baelle Profil-L2 < 0,05 und J/Q = 1,000 +- 0,005 (p = 0,9).

## 4. Frage (b): Vierer-Ring (`vierer`)

### 4.1 Aufbau

- Wie n4_windung in r5_2d_a.py: vier Baelle m = 0 bei 0,70, Quadrat (Ecken bei 45 Grad + k 90 Grad, gegen den
  Uhrzeigersinn), Seite 2 R_halb + Luecke, Phase w k pi/2. Box L = 38,4.
- T = 2000 grob, 1000 fein.
- C4-Projektion (nur *_sym):
  - vor jeder Messung P = (1/4) Sum_k conj(lam)^k R^k mit lam = e^{-i w pi/2}, angewandt auf psi, psi_t und Kraft
  - Das Gitter geht unter 90 Grad exakt in sich ueber. Die Projektion haelt die exakte Dynamik des symmetrischen
    Startfelds fest und nimmt nur die aus Rundung wachsenden asymmetrischen Anteile heraus.

| Lauf | Luecke | Windung w | C4-Sektor | Saat (Ball 0 x (1 + eps)) | Zweck |
|---|---|---|---|---|---|
| n4_windung | 4 | +1 | nein | 0 | R5 lang |
| n4_windung_sym | 4 | +1 | ja | 0 | gebunden im symmetrischen Sektor? |
| n4_windung_s1e-3, _s1e-6 | 4 | +1 | nein | 1e-3, 1e-6 | ln-eps-Probe der Instabilitaet |
| n4_gegen | 4 | -1 | nein | 0 | Windung gegenlaeufig |
| n4_gleich | 4 | 0 | nein | 0 | ohne Windung (verschmilzt) |
| n4_windung_l6, _l6_sym | 6 | +1 | nein / ja | 0 | groesserer Startabstand |
| n4_windung_l8_sym | 8 | +1 | ja | 0 | noch groesser |

- Die Gegenprobe "gegenlaeufig" ist exakt das Spiegelbild von n4_windung (mal globaler Phase). Sie kann nur durch einen
  Codefehler abweichen (L2 schwach), prueft aber Aufbau und Drehimpulsvorzeichen.

### 4.2 Papier [S]

- Nachbarn stehen 90 Grad auseinander. Die Paarenergie erster Ordnung ist null (2D-B-Statik: -0,064 bei Spalt 4, zweite
  Ordnung). Diagonalen (180 Grad, Abstand 11,1) stossen schwach ab.
- Der Josephson-Strom sin(90 Grad) ist maximal. Im Quadrat laeuft er im Kreis (Drehimpuls ohne Nettotransport).
- Im Paar (2D-B quer_s4) frisst ein Ball den anderen (max |dQ|/Q 0,93). Im Quadrat unterdrueckt die Symmetrie das,
  solange sie haelt.
- R5-Daten (0.2): Rate etwa 0,07 fuer den Tausch zwischen den Diagonalpaaren. Aus Rundung 1e-15 folgt der Bruch bei etwa
  t = ln(1e14)/0,07, also 450 bis 500. Das passt zu R5.

### 4.3 Vorhersagen und Klassen

- **Klassen** (vorab, im Code), frueheste zutreffende:
  - verschmolzen: weniger als 4 Klumpen in 3 Analysen
  - Ladungstausch: Spreizung >= 0,3
  - auseinander: r >= 1,3 r0
  - Danach, ohne Ereignis:
    - offen (Rand)
    - driftend: |Drift x Fenster| >= 0,1 r0
    - gebunden: 4 Baelle, Spreizung < 0,1, r in [0,8; 1,25] r0, Fenster >= 0,8 T
    - sonst offen
  - Zeiten: t_Bruch = Spreizung 0,1; gamma aus ln Spreizung.
- **Vorhersagen:**
  - n4_windung: Symmetriebruch mit gamma 0,05 bis 0,10 und t_Bruch 380 bis 600 (p = 0,7). Klasse Ladungstausch oder
    verschmolzen (p = 0,75), gebunden (p = 0,1).
  - n4_windung_sym: gebunden im Sektor (p = 0,55), driftend (p = 0,3), verschmolzen (p = 0,15).
    - Periode 120 bis 200 (p = 0,6); Drehung im Uhrzeigersinn, Rate -3e-3 bis -8e-3 (p = 0,7).
  - Saaten: t_Bruch(1e-3) < t_Bruch(1e-6) < t_Bruch(0), und dt_Bruch(1e-6 minus 1e-3) x gamma/ln 1000 zwischen 0,7 und
    1,3 (p = 0,6).
  - n4_gegen: r(t) bis t = 300 gleich n4_windung auf 1e-10, J entgegengesetzt, Drehrate entgegengesetzt (p = 0,97).
  - n4_gleich: verschmolzen bis t = 10 (p = 0,95).
  - Luecke 6: kleinere Kopplung. l6 bricht spaeter als n4_windung, mit kleinerem gamma (p = 0,6); l6_sym gebunden
    (p = 0,45).
  - l8_sym: fast ruhend, "gebunden" nach Kriterium (p = 0,6).
    - Das Kriterium unterscheidet dort aber nicht zwischen gebunden und kaum wechselwirkend (Grenze, Abschnitt 8).
- **Antwort auf "gebundener Verbund?"** Der symmetrische Zustand ist gebunden, aber instabil (p = 0,5). Nicht einmal
  im Sektor gebunden (p = 0,3).

## 5. Kontrollen (c): Vorhersagen

- Bilanz in allen Laeufen unter Toleranz (p = 0,9). Q-Rest unter 1e-4 (p = 0,8).
- L3 bestanden: wirbel (p = 0,75), teilung (p = 0,85), vierer (p = 0,8).
- Schranken: alle erfuellt (p = 0,85). Am ehesten reisst "Profil eingeschachtelt", falls ein Ringklumpen spaet unter
  Q = 89 (omega^2 0,66) faellt.

## 6. Aufrufe auf der .69 (Leitung; je hoechstens 10 min, Spur p4000a oder p4000b)

- Vorbereitung: `ring.py` nach /home/fmh/fmhc-physics-remote/runde7-ring/ kopieren. Das Skript braucht nur torch.
- Es schreibt nach `--out` (Vorgabe `ausgabe/`, bei `--rauch` `rauchtest/`), den Profilcache neben das Skript.

```
cd /home/fmh/fmhc-physics-remote/runde7-ring && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r7-ring-rauch ring.py alle --rauch
cd /home/fmh/fmhc-physics-remote/runde7-ring && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r7-ring-profile ring.py profile
cd /home/fmh/fmhc-physics-remote/runde7-ring && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r7-ring-wirbel-a ring.py wirbel --stufe grob --laeufe N6_dreh+,N8_dreh+,N6_dreh+_s1e-2,N8_dreh+_s1e-2
cd /home/fmh/fmhc-physics-remote/runde7-ring && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b r7-ring-wirbel-b ring.py wirbel --stufe grob --laeufe N6_dreh+_s1e-3,N6_dreh+_s1e-4,N8_ruhend --out ausgabe-saat
cd /home/fmh/fmhc-physics-remote/runde7-ring && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b r7-ring-wirbel-fein ring.py wirbel --stufe fein
cd /home/fmh/fmhc-physics-remote/runde7-ring && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r7-ring-teilung-grob ring.py teilung --stufe grob
cd /home/fmh/fmhc-physics-remote/runde7-ring && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b r7-ring-teilung-fein ring.py teilung --stufe fein
cd /home/fmh/fmhc-physics-remote/runde7-ring && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r7-ring-vierer-grob ring.py vierer --stufe grob
cd /home/fmh/fmhc-physics-remote/runde7-ring && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b r7-ring-vierer-fein ring.py vierer --stufe fein
```

- p4000b nur, wenn WM-1-MB nicht laeuft (kleintest.sh prueft das selbst, Ausgang 3). Sonst alles nacheinander auf
  p4000a.
- `wirbel-b` schreibt nach `ausgabe-saat/`, damit der Bericht von `wirbel-a` nicht ueberschrieben wird. L3 fuer wirbel
  entsteht in `ausgabe/` aus `wirbel-a` und `wirbel-fein`, gleich in welcher Reihenfolge.
- Der Rauchtest druckt je Unterbefehl eine Hochrechnung (Entwicklung x 20). Ueber 480 s: `--laeufe` weiter teilen.
- `wirbel` ohne `--laeufe` rechnet alle sieben Laeufe grob (etwa 6 bis 7 min); deshalb oben geteilt.

## 7. Laufzeit und Speicher (Schaetzung P4000, nicht gemessen)

- **Grundlage:** gemessene Entwicklungszeiten auf der P4000 aus den R5-Logs:
  - ringe: grob 11 x 320^2 x 10 000 Schritte in 79,1 s (7,0 ns je Punkt und Schritt); fein 5 x 480^2 x 20 000 in
    148,8 s (6,5 ns)
  - vielzeller: grob 7 x 256^2 x 10 000 in 28,0 s (6,1 ns); fein 6 x 384^2 x 20 000 in 92,1 s (5,2 ns)
  - teilung: grob 8 x 256^2 x 12 000 in 37,3 s (5,9 ns)
  - Hier 8,5 ns angesetzt: Messabstand 0,5 statt 1 bedeutet doppelt so viele Dichteberechnungen, dazu die Fenstersummen.
    Pro Analyse kommen etwa 50 ms dazu.
  - Start des Interpreters etwa 3 s. Profile aus dem Cache: unter 1 s; ohne Cache etwa 100 s (R5: 82 bis 96 s fuer 13
    bis 22 Profile).

| Aufruf | Arbeit | erwartet |
|---|---|---|
| alle --rauch | 39 Profile schiessen + 5 % aller Laeufe | etwa 3 min |
| profile | aus dem Cache | unter 0,5 min |
| wirbel-a | 4 x 320^2 x 60 000 | etwa 4 min |
| wirbel-b | 3 x 320^2 x 60 000 | etwa 3 min |
| wirbel-fein | 3 x 480^2 x 40 000 | etwa 4,5 min |
| teilung-grob | 6 x 256^2 x 60 000 | etwa 4 min |
| teilung-fein | 2 x 384^2 x 60 000 | etwa 2,7 min |
| vierer-grob | 9 x 256^2 x 40 000 | etwa 4 min |
| vierer-fein | 2 x 384^2 x 40 000 | etwa 2 min |
| **zusammen** | | **etwa 30 min** |

- Groesster Aufruf etwa 4,5 min, also mindestens Faktor 2 unter RuntimeMaxSec 600.
- Speicher: groesster Stapel vierer grob mit 9 x 256^2 complex128 = 9,4 MB je Feld, etwa 15 Felder. Mit CUDA-Kontext
  unter 1 GB (p4000a hatte 3,0 GB frei, p4000b 1,7 GB). Rohdaten je Aufruf unter 20 MB.

## 8. Was welches Ergebnis bedeuten wuerde

- **Wirbelball (2.4) ohne Zerfall, auch mit Saat 1e-2:**
  - Ein Ring aus Einzelbaellen schliesst sich robust zu einem stationaeren drehenden Q-Ball (m = 1).
  - Neu fuer uns; verwandt mit [L] Axenides u. a. 2000 und Battye/Sutcliffe 2000 (drehende Q-Baelle aus Stoessen).
- **Wirbelball auf Zeit:**
  - Der Wirbel lebt nur, solange die Symmetrie des Startfelds haelt; die Saat bestimmt die Lebensdauer (ln-Gesetz).
  - Der R5-Befund bei T = 500 waere dann dieselbe Symmetrieschutz-Falle wie beim Vierer.
  - Vergleich mit teilung zeigt, ob der Klumpen zerfaellt, weil er zu leicht ist (Q unter der Schwelle) oder weil er
    zu stark angeregt ist (E/Q ueber dem m = 1-Ball, Q ueber der Schwelle).
- **teilung-Schwelle:** Sie ordnet die Ringklumpen ein und ist fuer spaetere Wirbelkarten die Stabilitaetsgrenze in
  omega^2 bzw. Q.
- **Vierer:**
  - im Sektor gebunden, ohne Symmetrie gebrochen: Ein "Molekuel" existiert als symmetrische Loesung, ist aber instabil
    gegen Ladungstausch. Kein Verbund im biologischen Sinn.
  - im Sektor driftend: Es gibt gar keine Bindung.
  - ohne Symmetrie gebunden: widerspricht dem Paarbild. Zuerst L3, Saatprobe und laengeres T pruefen.

## 9. Grenzen

- Explorativ; 2D; eine Ballgroesse (0,70) fuer die Ringe; ein Stoerfaktor-Muster (l = 1..6, feste Phasen).
- Klumpenschwelle am Anfangsmaximum (wie R5), daher zusaetzlich die schwellenfreie Fensterprobe.
- omega_eff trennt m = 1 und m = 0 gleicher Ladung nur um etwa 2,4 %; Windung und Profil tragen die Unterscheidung.
- Der Profilvergleich nimmt das zeitliche Mittel ab T/2; ein angeregter Klumpen verschmiert das Profil. Die Selbstprobe
  in teilung zeigt, was ein stationaerer Ball erreicht.
- "gebunden" nach dem Driftkriterium unterscheidet bei grossem Abstand (l8) nicht zwischen Bindung und schwacher
  Wechselwirkung; dafuer waere ein Stossversuch noetig (nach aussen gerichtete Anfangsgeschwindigkeit), naechste Runde.
- C4-Projektion ist ein numerisches Mittel (invarianter Unterraum), kein physikalischer Zustand, der sich von selbst
  einstellt.
- Die Wachstumsraten der Symmetriebrueche (vierer, wirbel ohne Saat) haengen am Rundungsniveau; nur die Saatlaeufe geben
  kontrollierte Anfangsamplituden.
- Literatur aus dem Gedaechtnis:
  - kubisch-quintische Wirbelsolitonen stabil oberhalb einer Leistungsschwelle (Quiroga-Teixeiro und Michinel 1997;
    Towers u. a. 2001)
  - Solitonhaufen (Desyatnikov und Kivshar 2002)
  - Q-Ball-Stoesse (Axenides u. a. 2000; Battye und Sutcliffe 2000)
  - Vor einer Verwendung an der Quelle lesen.

## Latten (Vorschlag, die Leitung entscheidet)

| Teil | L1 kann scheitern | L2 Gegenprobe | L3 Numerik | L4 schon bekannt | L5 Messbezug |
|---|---|---|---|---|---|
| (a) wirbel | ja: Windung, J/Q, Frequenz, Profil, Dauer vorab (mit Vorbehalt 0.2) | ja: m = 0-Profil gleicher Ladung, Saatreihe 1e-4 bis 1e-2 | fein N6/N8 bis 1000; Bilanz | teilweise: Wirbelsolitonen und Solitonhaufen [L], drehende Q-Baelle aus Stoessen [L] | mittelbar (Optik, Kondensat-Wirbel [L]) |
| (a) teilung | ja: Schwelle vorab | ja: 0,55 und 0,65 als R5-Kontrollen; Selbstprobe des Profils | fein 0,59 und 0,625 | ja: Stabilitaetsschwelle von Wirbelsolitonen (CQ-NLS) [L] | mittelbar |
| (b) vierer | ja: Bruch, Rate, Klasse vorab | ja: ohne Windung, gegenlaeufig (schwach, Spiegelbild), Abstand 6 und 8, C4-Sektor, Saat 1e-3/1e-6 | fein sym und s1e-6 | teilweise: Josephson-Tausch im Paar (2D-B quer_s4) | nein |
| (c) Kontrollen | ja: Toleranzen vorab | Q-Rest eicht die Quadratur | - | - | - |

**Vorschlag:** alle neun Aufrufe rechnen. Wenn die Zeit knapp ist, zuerst wirbel-a, teilung-grob und vierer-grob.

## Einfach gesagt

Sechs oder acht kleine Q-Baelle, die im Kreis laufen und deren innere Uhren einmal rundherum weiterzaehlen,
verschmelzen zu einem einzigen Ball, der sich wie ein Wirbel dreht. Wir pruefen jetzt, ob dieser Ball wirklich derselbe
drehende Q-Ball ist, den man auch direkt ausrechnen kann: gleiche Drehung, gleicher Takt, gleiche Form. Ausserdem schauen
wir, ob er lange haelt oder, wie kleine drehende Baelle, wieder zerfaellt. Bei den vier Baellen im Quadrat, die in R5
zusammenblieben, sieht es nach einem Kartenhaus aus: Solange alles perfekt symmetrisch ist, halten sie. Der kleinste
Unterschied waechst aber, bis ein Ball den anderen die Ladung abnimmt.

Ende der Bearbeitung: 2026-09-30 04:37:37 CEST (gemessen mit date). Beginn 2026-09-30 04:02:10 CEST.
