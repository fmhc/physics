# Paket 2D-B (Kollektiv und Kristall): Laufplan

Bearbeiter: Anthropic-Agent B (Opus 5.5), Auftrag RUNDE-06/AUFTRAG-MEDIUM-UND-2D-B.md, Abschnitt "Agent B". Beginn
2026-09-30 02:53:47 CEST (gemessen), Plan begonnen 03:24:33 CEST (gemessen), Ende in der letzten Zeile.
Status: Code geschrieben, **lokale Formprobe gelaufen (CPU, winziges Gitter, alle 8 Karten rc 0), Messlaeufe nicht
gerechnet.** Explorativ, keine formale Bestaetigung. Papierwerte sind [S], Literatur aus dem Gedaechtnis [L].

## Kurzfassung

- **Code:** r5_2d_b.py (PyTorch, float64/complex128, `--geraet cuda|cpu`, cpu nur fuer die Formprobe). Unterbefehle
  `profile`, `paare`, `gitter`, `ringe`, `gluehwurm`, `haendigkeit`, `isomere`, `kollektiv`, dazu `alle --rauch`.
- **Grundlage:** r5_2d_a.py (2D-A), dort aus tests2d_r3.py. Uebernommen ist das **berichtigte Schiessen fuer m != 0**
  (Hinweis der Leitung, Abschnitt 0.2). Neu: Profilcache, Ball-Verfolger, Klumpen mit Mindestladung je Ball,
  "dichte Ladung" fuer die Abstrahlung, Rohdatensicherung je Stufe.
- **Ball:** m = 0 bei omega^2 = 0,70 (R_halb 1,92, Q 24,0). Nachbarabstand d = 2 R_halb + 4 = 7,83. Haendigkeit:
  m = +-1 bei 0,55 (Q 370, R_halb 9,2).
- **Laufzeit P4000 (Schaetzung):** je Aufruf 1,5 bis 4 min, `gluehwurm` etwa 4 min; mit gefuelltem Profilcache. Ohne
  Cache je Aufruf etwa 1,5 min mehr.
- **Kernvorhersagen:**
  - Kein Gitter und kein Ring haelt.
    - Gleichphasige verschmelzen in 5 bis 30 Zeiteinheiten.
    - Wechselphasige laufen auseinander.
    - Eine stabile Anordnung mit gemischten Phasen gibt es nicht (Chemie 13).
  - Gleichphasige Paare binden nicht als Molekuel, sie verschmelzen.
  - Keine Synchronisation (Bio 11), keine Haendigkeit (Bio 47, exakte Spiegelsymmetrie).
  - Kette und Dreieck wandeln sich nicht ineinander um (Chemie 5).
  - Tornado-Auge: Der Kern haengt kaum von Q ab.
  - **Einzige offene Hoffnung:** Der mitdrehende Ring (N6_k1_dreh+) schliesst sich zu einem drehenden Ball mit
    Windung 1.

## 0. Hinweise an die Leitung

### 0.1 Lokale Formprobe (gerechnet auf dem Laptop, Vorschau, kein Ergebnis)

- Freigabe: Auftrag der Leitung und Finn 30.09. 02:42 (Memory "Lokale Laeufe: seit 30.09. kleine erste Runs erlaubt").
  Eingehalten: nur CPU (`CUDA_VISIBLE_DEVICES=`), 1 Thread, nice 19, timeout 120 s, Ausgaben nur in `lauf-lokal/`.
- Aufruf je Karte:

```
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-05/r5-2d-b && mkdir -p lauf-lokal && \
  CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 \
  python3 r5_2d_b.py <karte> --rauch --mini --geraet cpu --out lauf-lokal
```

- Ergebnis 03:22:25 bis 03:22:58 CEST: alle 8 Karten einzeln rc 0, Wandzeit je Karte 3 bis 17 s. Nach der letzten
  Aenderung (Windungsguete) 03:27:54 bis 03:28:48 CEST `alle --rauch --mini` in einem Aufruf: rc 0, 54 s. Davor einmal das Schiessen
  aller 22 Profile: 31 s.
- Dabei gefunden und behoben:
  - Heilungslaenge fuer S_c < 2/3 undefiniert (math domain error)
  - `G_SEED` fehlte
  - Verfolgerfenster ueberlappten, die Verfolger liefen zusammen (Fenster jetzt min(R_halb + 2,5; 0,4 d_NN))
  - Bindungskriterium zu weich (jetzt Hysterese 0,3)
  - Paarabstaende: Spalt 3 ist gleichphasig schon am Start ein Klumpen, deshalb Spalte 4, 5, 7
  - Fitfenster: Gleichphasige Paare verschmelzen in unter 20 Zeiteinheiten, Fenster jetzt [1; 10]
- `--mini`: 256 Schiesskandidaten, dx 0,6/0,4, dt 0,1/0,05, Laufzeiten x 0,02. Die Hochrechnung im CPU-Log gilt nicht
  fuer die GPU.
- **Was ich aus der Vorschau schon gesehen habe** (offengelegt, weil es die Vorhersagen beeinflussen kann):
  - Statik der Paare (Ueberlagerung, dx 0,6): E_bind(Spalt 4) = -0,71 (gleichphasig), +0,39 (gegenphasig).
    Josephson-Amplitude B = 0,55, kappa_fit 0,537 gegen 0,548.
  - Profile m = 1 (256 Kandidaten): Kernradius 2,0 bis 2,5 bei 0,55 bis 0,80; 0,52 ungueltig. Abschnitt 9 nennt die
    Vorhersage vor der Vorschau getrennt.
  - Dynamik nur ueber 8 bis 20 Zeiteinheiten auf grobem Gitter: nicht als Vorhersagegrundlage benutzt, ausser dem
    Hinweis, dass Gleichphasige sehr schnell Bruecken bilden.

### 0.2 Schiessen fuer m != 0

- Uebernommen aus r5_2d_a.py.
- Ueberschuss: f > f_top oder f < 0. Unterschuss: f' > 0 unter der Talsohle nach dem ersten Abstieg. Fuer |m| >= 1 wird
  ln p eingeschachtelt.
- In der Formprobe waren m = 1 bei 0,55 bis 0,80 gueltig, mit Virialrest um 5e-11.

### 0.3 Reihenfolge

1. `alle --rauch` (Rauchtest der GPU, schreibt rauchtest/ mit eigenem Cache)
2. `profile` (fuellt ausgabe/profil_cache.pt fuer alle anderen Aufrufe)
3. die uebrigen sieben in beliebiger Reihenfolge, auch parallel auf p4000a und p4000b

## 1. Festlegungen fuer alle Karten (vor dem Lauf)

### 1.1 Modell und Numerik

- **Modell:** L = |psi_t|^2 - |grad psi|^2 - U(S), U = S - S^2 + S^3/2. Ein Feld, kein Medium, kein V.
- **Unveraendert aus r5_2d_a.py:**
  - Schiessen: RK4, h = 0,01, bis r = 60, 2048 Kandidaten, 5 Runden
  - Radialtabelle bis r = 100, Schwanz K_m(kappa r), Hermite-Interpolation
  - periodische Box mit Randschicht (Breite 8, sigma = (Tiefe/8)^2), spektraler Laplace, Velocity-Verlet
  - grob dx = 0,3, dt = 0,05; fein dx = 0,2, dt = 0,025
  - bewegter Ball durch Lorentz-Boost
- **Startfelder:** Summe der Einzelbaelle (Ueberlagerung), psi_t = -i omega psi je Ball.
  - Phase und Windung jedes Balls sind explizit gesetzt und stehen im Ergebnis-JSON unter "aufbau".

### 1.2 Messgroessen

- **Je Messpunkt** (T_MEAS = 1, bei paare und gluehwurm 0,5):
  - Q_Box, E_Box, J_Box, S_max
  - **Verfolger je Ball** (Fenster r_w = min(R_halb + 2,5; 0,4 d_NN) = 3,13 bei 0,70): Ort (Gewicht S^2), Ladung im
    Fenster, innere Phase arg(Sum psi S), R_rms (Gewicht S), S_max
- **Je Analyse** (alle 5 Zeiteinheiten):
  - **Klumpen:** geglaettetes S (Gauss, Breite 1) > 0,5 x Anfangsmaximum, zusammenhaengend, Ladung >= 0,25 Q_1
  - je Klumpen: Q, E, Ort, v = P/E, Eigendrehimpuls/Q, Phase, bei ringe und haendigkeit die Windung (Kreis mit
    mittlerem Abstand)
  - **dichte Ladung** Q_dicht: Ladung im Gebiet geglaettetes S > 0,1 x Anfangsmaximum
  - **abgestrahlt** f_rad = 1 - Q_dicht/Q_Box(0)
- **Auswertefenster:** endet, sobald ein Klumpenschwerpunkt naeher als Randschicht + 2 am Rand ist (t_rand). Danach
  laeuft Ladung in die Randschicht und wuerde als Verschmelzen oder Zerfall gezaehlt.

### 1.3 Ausgaenge (vorab, fuer alle Mehrball-Laeufe gleich)

Rangfolge von oben nach unten; die erste zutreffende Klasse gilt:

| Klasse | Kriterium (im Auswertefenster, n0 = Klumpenzahl am Start) |
|---|---|
| zerfallen | f_rad am Fensterende >= 0,5 |
| zerbrochen | mehr als n0 Klumpen in 3 aufeinanderfolgenden Analysen |
| verschmolzen (ganz / teilweise k von n0) | weniger als n0 Klumpen in den letzten 3 Analysen |
| auseinander | kein Verschmelzen; Traegheitsradius der Klumpenorte oder mittlerer Naechster-Nachbar-Abstand >= 1,3 x Start |
| halten | stets n0 Klumpen; Traegheitsradius und NN-Abstand stets in [0,85; 1,15] x Start; Fenster >= 0,8 T |
| offen | sonst |

- Paare zusaetzlich **gebunden (schwingt):**
  - kein Verschmelzen, nicht auseinander
  - d(t) der Verfolger mit mindestens 2 Richtungswechseln von je >= 0,3 (Hysterese)
  - 0,5 d0 < d < 1,3 d0, Fenster >= 100
- **Plausibilitaet** (Lehre aus R5, eigene Kontrolle je Lauf):
  - f_rad(0) in [-0,05; 0,25] (`plausibel_start`)
  - Startzerlegung n0 = Ballzahl (`startzerlegung_ok`)
  - Einzelball-Kontrollen "ruhig"
  - Q_Box-Verlust der Einzelball-Kontrollen unter 1e-3
- **Windung** eines Klumpens wird nur mit S_min_kreis > 0,05 gewertet; kleiner heisst "unsicher".
  Umgesetzt als `windung_sicher`; eta (haendigkeit) und `windungen_ende` (ringe) zaehlen nur sichere Windungen.

### 1.4 Aufloesung (L3)

- Je Karte laufen ausgewaehlte Laeufe fein (dx 0,2, dt 0,025).
- Bestanden, wenn die Klasse gleich bleibt und die erste Verschmelzung innerhalb max(20 %, 10) liegt.
- Paare: d'' (Fit) innerhalb 10 %. Gluehwurm: r_Ende innerhalb 0,1.

## 2. Grundlage: Paare (`paare`), macht die offene Paarbindung sichtbar

### 2.1 Aufbau

- **Statik ohne Zeitentwicklung:**
  - Ueberlagerung zweier Baelle bei Spalt 1,0 bis 10,0 (Schritt 0,5) und dphi = 0, pi/2, pi
  - E_bind = E - 2 E_1 - omega (Q - 2 Q_1), Bindung bei fester Ladung in erster Ordnung, Einzelwerte auf demselben
    Gitter
  - Zerlegung E_bind(dphi) = A + B cos dphi + C cos 2 dphi; B ist die Josephson-Amplitude
- **Zeitentwicklung:** T = 400, Box 76,8, Messung alle 0,5.

| Lauf | dphi | Spalt (d) |
|---|---|---|
| gleich_s4 / s5 / s7 | 0 | 4 / 5 / 7 (7,83 / 8,83 / 10,83) |
| quer_s4 | pi/2 | 4 |
| gegen_s4 / s5 | pi | 4 / 5 |
| einzel | - | Kontrolle |

- Fein: gleich_s4, quer_s4, gegen_s4.

### 2.2 Papier [S]

- Asymptotik: E_bind ~ -cos(dphi) K_0(kappa d), kappa = sqrt(1 - omega^2) = 0,548.
- **Phasendynamik** (Q und Phase sind kanonisch konjugiert):
  - dQ_1/dt = -B sin(dphi), d(dphi)/dt = (domega/dQ)(Q_1 - Q_2)
  - Mit domega/dQ < 0 (duennwandiger Ast, 2D-Profile: Q faellt mit omega) ist **dphi = 0 instabil**: Der groessere
    Ball zieht Ladung ab, Wachstumsrate sqrt(2 |omega'| B), etwa 0,07 bei Spalt 4.
  - dphi = pi ist stabil (Schwingung).
  - Das ist der Josephson-Kontakt mit negativer "Ladeenergie" [L: bosonischer Josephson-Kontakt, Smerzi u. a. 1997].
- Ein Minimum von E(d) ist in erster Ordnung nicht zu erwarten (Fable-Review).

### 2.3 Vorhersagen und Kriterien

- **Statik:**
  - E_bind(d, 0) monoton, ohne Minimum (p = 0,9)
  - kappa_fit innerhalb 5 % von 0,548 (p = 0,8)
- **Dynamik:**
  - gleich_s4, s5, s7: **verschmolzen**, p = 0,85. Erste Verschmelzung bei 5 bis 30, 10 bis 60 bzw. 20 bis 200.
  - **gebunden (schwingt)** fuer ein gleichphasiges Paar: p = 0,1. Das waere die sichtbare Paarbindung und ein
    Befund-Kandidat.
  - gegen_s4, s5: **auseinander**, p = 0,9. Die Phasendifferenz bleibt bei pi (Spanne < 1 rad, p = 0,8).
    Endgeschwindigkeit etwa sqrt(E_bind(pi)/M) = 0,13.
  - quer_s4: Anfangsstrom |dQ_1/dt| / |B(Spalt 4)| in [0,7; 1,3] (p = 0,7). Danach Verschmelzen (p = 0,6).
  - einzel: ruhig, Q-Verlust < 1e-3 (p = 0,95).
- **Starrkoerperprobe:**
  - Kriterium: d''_dyn / d''_statik in [0,7; 1,3] heisst "Starrkoerperbild traegt", mit d''_statik = 2 F/M,
    F = -dE_bind/dd.
  - Erwartung, nach der Formprobe formuliert: gleichphasig > 1,5 (p = 0,6; Verschmelzen durch Fluss in den Hals),
    gegenphasig in [0,7; 2] (p = 0,6).
- **Abstandsgesetz:** d''(s4)/d''(s5) etwa e^kappa = 1,73 und d''(s5)/d''(s7) etwa e^{2 kappa} = 2,99, je innerhalb
  30 % (p = 0,5).

## 3. Bio 25/42 und Chemie 13: Gitter (`gitter`)

### 3.1 Aufbau

- Box 96 x 96, T = 400; omega^2 = 0,70; Spalt 4 (d = 7,83), zwei Laeufe mit Spalt 7 (d = 10,83).
- Quadrat k x k.
- Dreiecksgitter aus 16 Baellen: Basis (d, 0), (d/2, d sqrt3/2), 4 Reihen, zentriert.
- **Phasen (explizit):**
  - gleich: alle 0
  - wechsel (Quadrat): pi ((i + j) mod 2), Schachbrett
  - streifen (Dreieck): pi (Reihe mod 2)
  - drei (Dreieck): 2 pi/3 ((i - j) mod 3); jeder Nachbar um +-120 Grad verschoben
  - windung: atan2(y, x) um den Gittermittelpunkt (Plakettenmitte, kein Ball im Zentrum)
  - zufall: gleichverteilt, Saat 20260930

| Lauf | Baelle | Phasen |
|---|---|---|
| Q3_gleich, Q3_wechsel | 9 | gleich, Schachbrett |
| Q4_gleich, Q4_wechsel, Q4_windung, Q4_zufall | 16 | gleich, Schachbrett, Windung 1, zufaellig |
| D16_gleich, D16_streifen, D16_drei, D16_windung | 16 | gleich, Streifen, 120-Grad-Ordnung, Windung 1 |
| Q4_gleich_s7, Q4_wechsel_s7 | 16 | gleich, Schachbrett, weiter Abstand |

- Fein: Q4_gleich, Q4_wechsel, Q4_windung, D16_streifen, D16_drei.
- J/Q am Start (Formprobe): Q4_windung 0,77, D16_windung 0,85. Die Windung traegt Drehimpuls ueber die
  Josephson-Stroeme zwischen den Baellen.

### 3.2 Papier [S]

- Paarenergie E(dphi) = A + B cos dphi + C cos 2 dphi (Statik, Spalt 4: A = -0,11, B = -0,55, C = -0,05).
  - Gleichphasige Nachbarn ziehen an.
  - 120 Grad gibt +0,19 (Abstossung).
  - 180 Grad gibt +0,39 (Abstossung).
- Wechselwirkung faellt mit e^{-kappa d}. Im Schachbrett stossen die naechsten Nachbarn ab; die uebernaechsten
  (gleichphasig, Abstand d sqrt 2) ziehen etwa viermal schwaecher an (E_bind -0,09 gegen +0,39). Netto Abstossung.
- Ein Gleichgewicht aus Abstossung der Nachbarn und Anziehung der Uebernaechsten gibt es nicht, weil die naechsten
  Nachbarn bei jedem Abstand ueberwiegen. **Chemie 13 (Kochsalz-Bild) ist damit schon auf dem Papier unwahrscheinlich.**
- Ein Gitter haelt im konservativen Feld nur, wenn es ein Energieminimum gibt. Die Daempfung aus Bio 25 fehlt, und ein
  Bad gibt es im Ein-Feld-Modell nicht.

### 3.3 Vorhersagen

| Lauf | Vorhersage |
|---|---|
| alle "gleich" (Q3, Q4, D16, Q4_s7) | verschmolzen, p = 0,9; erste Verschmelzung 5 bis 30 (Spalt 4) bzw. 20 bis 150 (Spalt 7); am Ende 1 bis 3 Klumpen |
| Q3_wechsel, Q4_wechsel | auseinander, p = 0,8; Randbaelle zuerst; halten p = 0,1 |
| Q4_wechsel_s7 | auseinander p = 0,6, offen (zu langsam) p = 0,3 |
| D16_streifen | verschmolzen (teilweise), Reihen zu Staeben, Staebe stossen sich ab, p = 0,6; zerbrochen p = 0,15 |
| D16_drei | auseinander p = 0,55; teilweise verschmolzen (120-Grad-Ordnung instabil) p = 0,35 |
| Q4_windung, D16_windung | verschmolzen, p = 0,8; groesster Klumpen mit Windung +-1 (Ring um den Wirbel) p = 0,4 |
| Q4_zufall | verschmolzen (teilweise), einige Baelle werden weggestossen, p = 0,7 |

- **Chemie 13:** kein Lauf mit gemischten Phasen haelt (p = 0,85).
- **Bio 25/42:** kein Gitter haelt; eine Wabe kann ohne Daempfung nicht entstehen (p = 0,9).
- Wird ein Lauf "halten", ist das der Befund-Kandidat. Dann zuerst pruefen:
  - Reicht T?
  - Liegt nur Stillstand wegen schwacher Kraefte vor? Dann muss Spalt 7 dasselbe zeigen.
  - L3

## 4. Bio 46 Kapsid und Chemie 19 Aromatizitaet: Ringe (`ringe`)

### 4.1 Aufbau

- N Baelle auf einem Kreis, Nachbarabstand d = 7,83, Radius R = d/(2 sin(pi/N)).
- Phase von Ball j: 2 pi k j/N, Stufe 2 pi k/N. k = 1 ist das Ringanalogon eines drehenden Balls (Windung 1).
- Drehend ("dreh+"): Tangentialgeschwindigkeit gegen den Uhrzeigersinn mit gamma E v R = Q je Ball, also J_Bahn = Q
  wie beim m = 1-Ball; v = 0,14 bei N = 6. "dreh-" im Uhrzeigersinn.
- T = 500, Box 96.

| Lauf | N | k | Bewegung | cos(Stufe) | Zweck |
|---|---|---|---|---|---|
| N6_k0 | 6 | 0 | ruht | 1 | Chemie 19 gleich |
| N6_k3 | 6 | 3 | ruht | -1 | Chemie 19 wechselnd |
| N6_k1, N6_k2 | 6 | 1, 2 | ruht | 0,5, -0,5 | Stufenreihe |
| N5_k1, N7_k1, N8_k1 | 5, 7, 8 | 1 | ruht | 0,31, 0,62, 0,71 | Kapsid N-Reihe |
| N6_k1_dreh+ | 6 | 1 | mitdrehend | | Ringanalogon |
| N6_k1_dreh- | 6 | 1 | gegendrehend | | Gegenprobe Drehsinn |
| N6_k0_dreh+ | 6 | 0 | drehend | | Gegenprobe ohne Windung |
| N8_k1_dreh+ | 8 | 1 | mitdrehend | | Ringanalogon N = 8 |

- Fein: N6_k0, N6_k1, N6_k3, N8_k1, N6_k1_dreh+.

### 4.2 Papier [S] und Literatur [L]

- Stufe mit cos > 0 zieht zusammen, cos < 0 treibt auseinander (Paarstatik).
- **Boost-Phase:** Ein Ball mit v traegt die Phase omega gamma v x. Beim mitdrehenden Ring verschiebt das die
  Phasendifferenz an der Kontaktstelle um -omega gamma v d, bei N = 6 etwa -50 Grad.
  - Aus 60 Grad werden etwa 10 Grad: Der Ring ist an den Kontakten fast gleichphasig, der Drehimpuls steckt in der
    Bewegung.
  - Formprobe: J/Q = +1,04 (dreh+), +0,56 (ruhend), -0,36 (dreh-). Das passt zu diesem Bild.
- [L] Desyatnikov und Kivshar 2002 (PRL, "Rotating optical soliton clusters"): Ringe aus Solitonen mit Phasenstufe
  drehen sich und koennen in saettigbaren Medien quasi-stabil sein.
- [L] Mihalache u. a. 2003: Solitonhaufen in kubisch-quintischen Medien (unser Modell im Grenzfall omega -> 1).
- [L] Soljacic, Sears, Segev 1998: Halsketten mit Wechselphase dehnen sich langsam aus.
- Hueckel 4n + 2 ist eine fermionische Abzaehlregel. In einem klassischen Feld erwarte ich keine Sonderrolle von N = 6.

### 4.3 Vorhersagen

| Lauf | Vorhersage |
|---|---|
| N6_k0 | verschmolzen (ganz), kompakter Ball, Windung 0, p = 0,9 |
| N6_k3 | auseinander als symmetrische Halskette (alle 6 Klumpen bleiben), p = 0,9 |
| N6_k2 | auseinander, p = 0,7 |
| N5_k1, N6_k1, N7_k1, N8_k1 | verschmolzen, p = 0,8. Am Ende Windung 1 im groessten Klumpen p = 0,35; kompakt mit Windung 0 (Wirbel ausgestossen, J/Q < 1) p = 0,45 |
| N6_k1_dreh+ | ein Klumpen mit Windung +1 und J/Q etwa 1 (Ring schliesst sich zum drehenden Ball) p = 0,45; haelt als drehender Haufen p = 0,2; zerbricht oder fliegt auseinander p = 0,35 |
| N8_k1_dreh+ | wie N6_k1_dreh+, p = 0,45 |
| N6_k1_dreh- | auseinander (effektive Stufe etwa 110 Grad), p = 0,6 |
| N6_k0_dreh+ | verschmolzen, Windung 0, p = 0,7 |

- **Bio 46 Kapsid:** "stabil" heisst halten fuer ein N mit k = 1. Erwartung p = 0,15.
- **Chemie 19:** Der wechselnde Ring ist nur formstabil (Halskette), der gleiche kollabiert. "Deutlich stabiler" im Sinn
  von halten: keiner (p = 0,8). Keine Sonderrolle von N = 6 in der k = 1-Reihe (gleiche Klasse wie N = 5, 7, 8;
  p = 0,85).

## 5. Bio 11 Gluehwuermchen (`gluehwurm`)

### 5.1 Aufbau

- Ring aus 8 Baellen, omega^2 = 0,70 + (-0,005, 0,010, 0, -0,010, 0,005, -0,0025, 0,0075, -0,0075), feste Reihenfolge.
  Spreizung +-0,01 wie im 1D-Test der Runde 2.
- **Phasen:**
  - zufall: (2,39996 j) mod 2 pi, goldener Winkel wie tests1d.py
  - gleich: 0
  - wechsel: pi j
- **Atmung:** r -> r (1 + 0,05 cos beta_j), psi_t = -i omega (1 + 0,05 sin beta_j) psi, mit
  beta_j = (1 + 2,39996 (j + 3)) mod 2 pi.
- Box 115,2 (n = 384 grob), T = 1000, Messung alle 0,5.

| Lauf | Spalt | Phasen | Atmung |
|---|---|---|---|
| nah_zufall_atem | 4 | zufall | ja |
| nah_zufall | 4 | zufall | nein |
| nah_gleich_atem | 4 | gleich | ja |
| nah_wechsel_atem | 4 | wechsel | ja |
| mittel_zufall_atem | 6 | zufall | ja |
| weit_zufall_atem | 22 | zufall | ja (Kontrolle, Kopplung etwa e^{-kappa 18} = 5e-5) |

- Fein: nah_zufall_atem.

### 5.2 Kennzahlen (wie 1D, Runde 2)

- **Fenster:** Anfang [0, T/10], Ende [3T/4, T]. Fuer die Atmung zusaetzlich 5 % Rand weg (FFT).
- **Eigenfrequenz:** omega_j = -Delta Phase/Delta t je Fenster; sigma_omega Anfang und Ende.
- **Kuramoto:** r = |mean e^{i Phase}|.
- **Atmung:** R_rms je Ball linear entzerrt, analytisches Signal; r_Atem, Amplitude, dominante Frequenz.
- **Kriterien** (gegen die weite Kontrolle):
  - phasensynchron: r_Ende >= 0,9 und r_Ende - r_Kontrolle >= 0,3, ohne Verschmelzen
  - frequenzsynchron: sigma_Ende/sigma_Anfang(Kontrolle) <= 0,2, ohne Verschmelzen
  - atemsynchron: r_Atem,Ende >= 0,9 und Effekt >= 0,3, Amplitude Ende >= 0,2 x Anfang, ohne Verschmelzen

### 5.3 Vorhersagen

- **Papier:**
  - Das Feld ist konservativ, also gibt es keinen Attraktor (Liouville). Synchronisation im Kuramoto-Sinn braeuchte
    Dissipation; hier dissipiert nur die Abstrahlung in die Randschicht.
  - Dazu ist Gleichphasigkeit bei domega/dQ < 0 dynamisch instabil (Abschnitt 2.2).
- **Erwartung:**
  - Keine Phasen- und keine Frequenzsynchronisation in keinem Lauf (p = 0,9), wie 1D.
  - nah_gleich_atem: verschmolzen (ganz), p = 0,9.
  - nah_zufall(_atem): teilweise verschmolzen, p = 0,6. Verschmolzene Laeufe sind fuer die Synchronisation nicht
    auswertbar.
  - nah_wechsel_atem: auseinander, p = 0,8.
  - Atmung: Die Amplitude faellt bis zum Endfenster auf unter die Haelfte (p = 0,6), weil der Modus ueber der
    Kontinuumsschwelle 1 - omega = 0,16 liegt und abstrahlt. Atemsynchron in keinem Lauf (p = 0,95).

## 6. Bio 47 Haendigkeit (`haendigkeit`)

### 6.1 Aufbau

- Baelle m = +-1 bei omega^2 = 0,55 (Q 370, R_halb 9,2, Loch 2,5). 3 x 3-Gitter mit d = 2 R_halb + 4 = 22,4.
- Box 115,2, T = 400.
- **Spiegelung x -> -x:** Ball (x, y, m, phi) -> (-x, y, -m, phi + m pi); das Gitter bildet sich auf sich selbst ab.

| Lauf | Aufbau |
|---|---|
| plus9 | 9 x m = +1, alle Phasen 0 |
| plus9_spiegel | exaktes Spiegelbild (9 x m = -1) |
| misch_a | 5 x +1, 4 x -1, Plaetze und Phasen zufaellig (Saat 1) |
| misch_a_spiegel | exaktes Spiegelbild |
| misch_b | andere Mischung (Saat 2) |
| einzel_plus | ein m = +1-Ball (Stabilitaetskontrolle) |

- Fein: plus9, misch_a.

### 6.2 Kennzahlen

- **Haendigkeit:** eta = Sum Q sign(W) / Sum Q ueber Klumpen mit Windung W != 0.
- **Spiegelprobe:** max_t |J_a(t) + J_b(t)| / max|J_a|, gleiche Klumpenzahlen, eta_a + eta_b.

### 6.3 Vorhersagen

- **Papier:** Das Modell ist spiegelsymmetrisch (P und C); ohne einen paritaetsbrechenden Term kann keine Haendigkeit
  bevorzugt werden. Das ist das Curie-Prinzip [L]. Die Karte prueft deshalb vor allem den Code (L2) und zeigt, wie
  Mischungen verschmelzen.
- **Kontaktphase:** Zwei Wirbelbaelle mit gleicher Phase sind am Beruehrpunkt gegenphasig (m pi), fuer jedes
  Vorzeichen von m.
- **Erwartung:**
  - plus9 (und Spiegel): auseinander, p = 0,7.
  - Spiegelprobe bis t_rand unter 1e-6: p = 0,8 bei plus9, p = 0,6 bei misch_a. Chaos kann die Rundung verstaerken;
    die Formprobe hatte 2e-9 schon bei t = 5.
  - misch_a, misch_b: teilweise verschmolzen. +1/-1-Paare verlieren die Windung, +1/+1-Paare geben Windung 2.
  - eta-Drift in zufaelliger Richtung. Keine Bevorzugung, weil die Spiegelbilder exakt gegenlaeufig sind.
  - einzel_plus: ruhig, Windung 1 bleibt, p = 0,85. [L] Wirbelsolitonen der kubisch-quintischen NLS sind oberhalb
    einer Mindestnorm stabil.

## 7. Chemie 5 Isomere (`isomere`)

### 7.1 Aufbau

- Drei Baelle bei 0,70, Bindungslaenge d = 7,83, Winkel am mittleren Ball: Kette 180, Knick 150, Dreieck 60 Grad.
- Phasen jeweils (0, 0, 0) oder (0, pi, 0), der mittlere Ball traegt pi. Box 76,8, T = 400.
- Fein: alle sechs.
- **Statik:** E_bind der Anordnung und Summe der drei Paar-E_bind bei denselben Abstaenden. Dreikoerperanteil
  = (E_bind - Paarsumme)/|Paarsumme|.

### 7.2 Vorhersagen

- **Energie:**
  - E(Dreieck) - E(Kette) < 0 fuer gleiche Phasen (drei Bindungen gegen zwei). Papier aus der Paarstatik etwa -0,7;
    die Formprobe gab -1,03, also etwa 16 % Dreikoerperanteil beim Dreieck.
  - Fuer (0, pi, 0): Formprobe -0,56. Auf dem Messgitter muss das Vorzeichen bleiben (p = 0,9).
- **Dynamik:**
  - Alle gleichphasigen verschmelzen (p = 0,9), das Dreieck zuerst (p = 0,6).
  - kette_wechsel und knick_wechsel: auseinander (p = 0,75).
  - dreieck_wechsel: verschmolzen (teilweise, 2 von 3); der pi-Ball wird ausgestossen (p = 0,6).
- **Umwandlung** Kette -> Dreieck (Winkel <= 75 Grad ohne Verschmelzen): p = 0,05. Isomere im chemischen Sinn (zwei
  langlebige Anordnungen mit Barriere) gibt es nicht.

## 8. Bio 26 Schleimpilz und Bio 40 Schwarm (`kollektiv`), einfache Umsetzung ohne Medium

### 8.1 Aufbau

- 12 Baelle bei 0,70, Zufallsorte in einer Scheibe mit Radius 18, Mindestabstand 2 R_halb + 3 (Saat 26).
- Zufallsphasen und Zufallsrichtungen aus Saat 27. Box 96, T = 400.

| Lauf | Phasen | Bewegung |
|---|---|---|
| schleim_gleich | gleich | ruht |
| schleim_zufall | zufall | ruht |
| schwarm_zufall | zufall | v = 0,05, Zufallsrichtungen |
| schwarm_gleich | gleich | v = 0,05, Zufallsrichtungen |

- Fein: schleim_gleich, schwarm_zufall.

### 8.2 Klassen (vorab)

- aggregiert (Schleimpilz): n_Ende <= n0/3 und groesster Klumpen >= 50 % der Klumpenladung
- vergroebert: n_Ende < n0
- Gas: sonst
- Schwarm (Zusatz): Polarisation |Sum Q v| / Sum Q|v| >= 0,5 am Ende, Zunahme >= 0,3 und mindestens 3 Klumpen

### 8.3 Begruendung und Vorhersagen

- **Bio 26:** Dictyostelium sammelt sich ueber ein Fernsignal (cAMP-Wellen im Medium). Hier gibt es nur die
  Nahkraft (Reichweite 1/kappa etwa 2), ein Fernsignal fehlt.
  - Vorhersage: nur lokales Verschmelzen. schleim_gleich aggregiert p = 0,5, vergroebert p = 0,45; schleim_zufall
    vergroebert p = 0,7.
- **Bio 40:** Swarmalatoren brauchen eine phasenabhaengige Kraft und eine ortsabhaengige Phasenkopplung, die zur
  Gleichphasigkeit zieht. Hier zieht die Josephson-Kopplung nicht zur Gleichphasigkeit (Abschnitt 2.2), und es gibt
  keine Daempfung.
  - Vorhersage: kein Schwarm (p = 0,9). schwarm_gleich vergroebert p = 0,8, schwarm_zufall vergroebert p = 0,6.

## 9. Wellen 19 Auge des Tornados (`profile`)

### 9.1 Aufbau

- m = 1-Profile bei omega^2 = 0,52 / 0,55 / 0,60 / 0,65 / 0,70 / 0,75 / 0,80, dazu m = 0 bei denselben Werten fuer S_c,
  p_c und sigma.
- Kern = innerer Halbwertsradius R_kern_halb (S = S_max/2 von innen).

### 9.2 Vorhersagen (vor der Vorschau festgelegt, so im Code)

- **Regel:** Steigung s von ln R_kern gegen ln Q ueber die vier groessten Q:
  - |s| <= 0,1: "Kern von Q unabhaengig (Saettigung)"
  - s >= 0,35: "waechst wie der Ball" (Idee 19)
  - sonst "schwach"
- Meine Erwartung vorher: Saettigung, p = 0,6.
- Zwei Papierwerte [S]:
  - **Kapillarloch** (2D-A): p a^2 + sigma a = S_c m^2, a etwa 2 bis 2,8
  - **Heilungslaenge** (R3-Plan): sqrt(2) xi = 1/sqrt(S_c U''(S_c)), etwa 0,9; nur fuer S_c > 2/3 definiert
  - Erwartung: naeher am Kapillarloch, p = 0,65.
- **Vorschau** (lokal, 256 Kandidaten, gilt nicht):
  - R_kern_halb 2,54 / 2,13 / 2,01 / 2,02 / 2,11 / 2,28 (0,55 bis 0,80), mit einem Minimum bei 0,65 bis 0,70
  - s(4 groesste Q) = 0,15, also "schwach"; naeher am Kapillarloch
  - 0,52 ungueltig
  - Die Messung mit 2048 Kandidaten entscheidet. Kippt 0,52 zu gueltig, geht sie in die Steigung ein.

## 10. Nicht bearbeitet

- **Bio 21 Nische:** Laut RUNDE-06-Auftrag bei M1 (Medium mit Dichtegefaelle). Die Ein-Feld-Fassung (Ball im
  Potentialgefaelle V(x)|psi|^2) ist der freie Fall a = -g N/E aus 2D-A, Karte 3 (L4). Keine eigene Rechnung.
- Kein Lauf braucht das chi-Medium. Die Daempfung aus Bio 25 ("mit Daempfung ordnen sich...") ist weggelassen: Eine
  Daempfung von psi_t vernichtet Ladung, eine ladungserhaltende Daempfung ist ein Modellwechsel.

## 11. Aufrufe auf der .69 (Leitung; Spur p4000a oder p4000b, je hoechstens 10 min)

- **Vorbereitung:** r5_2d_b.py nach /home/fmh/fmhc-physics-remote/runde5-2d-b/ kopieren.
  - Braucht nur torch.
  - Schreibt nur nach --out: Vorgabe ausgabe/, bei --rauch rauchtest/. Dort liegen auch der Profilcache und die
    Rohdaten je Stufe.
- **Rauchtest** (alle Karten, Laufzeiten x 0,05; etwa 3 bis 4 min, davon etwa 1,5 min Schiessen; druckt je Karte eine
  Hochrechnung):

```
cd /home/fmh/fmhc-physics-remote/runde5-2d-b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2db-rauch r5_2d_b.py alle --rauch
```

- **Hauptlaeufe** (zuerst profile, dann beliebig):

```
cd /home/fmh/fmhc-physics-remote/runde5-2d-b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2db-profile r5_2d_b.py profile
cd /home/fmh/fmhc-physics-remote/runde5-2d-b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2db-paare r5_2d_b.py paare
cd /home/fmh/fmhc-physics-remote/runde5-2d-b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2db-gitter r5_2d_b.py gitter
cd /home/fmh/fmhc-physics-remote/runde5-2d-b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2db-ringe r5_2d_b.py ringe
cd /home/fmh/fmhc-physics-remote/runde5-2d-b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2db-glueh r5_2d_b.py gluehwurm
cd /home/fmh/fmhc-physics-remote/runde5-2d-b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2db-hand r5_2d_b.py haendigkeit
cd /home/fmh/fmhc-physics-remote/runde5-2d-b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2db-iso r5_2d_b.py isomere
cd /home/fmh/fmhc-physics-remote/runde5-2d-b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2db-koll r5_2d_b.py kollektiv
```

- **Hochrechnung ueber 480 s:** grob und fein getrennt, z. B. `ringe --stufe grob` und
  `ringe --stufe fein --out ausgabe-fein`. Die L3-Zeile entsteht dann nicht automatisch; L3 von Hand nach 1.4.
- Laeufe ohne Cache schiessen selbst (etwa 1 bis 1,5 min); der Cache wird atomar geschrieben, parallele Aufrufe sind
  unbedenklich.

## 12. Laufzeit und Speicher (Schaetzung P4000, nicht gemessen)

- **Grundlage:** R3-Tropfen auf der P4000 gemessen, 5,5 bis 6,6 ns je Gitterpunkt und Schritt einschliesslich
  Messung. Hier 6,5 ns angesetzt, plus 20 % bei Messabstand 0,5 und etwa 10 s Klumpenanalyse.

| Aufruf | Arbeit | erwartet |
|---|---|---|
| profile | 22 Profile schiessen | 1,5 bis 2 min |
| paare | Statik 57 Felder; grob 7 x 256^2 x 8000; fein 3 x 384^2 x 16 000 | etwa 1,5 min |
| gitter | grob 12 x 320^2 x 8000; fein 5 x 480^2 x 16 000 | etwa 3,5 min |
| ringe | grob 11 x 320^2 x 10 000; fein 5 x 480^2 x 20 000 | etwa 4 min |
| gluehwurm | grob 6 x 384^2 x 20 000; fein 1 x 576^2 x 40 000 | etwa 4 min |
| haendigkeit | grob 6 x 384^2 x 8000; fein 2 x 576^2 x 16 000 | etwa 2 min |
| isomere | grob 6 x 256^2 x 8000; fein 6 x 384^2 x 16 000 | etwa 2 min |
| kollektiv | grob 4 x 320^2 x 8000; fein 2 x 480^2 x 16 000 | etwa 1,5 min |
| **zusammen** | | **etwa 20 min** |

- Ohne Cache kommt je Aufruf etwa 1 bis 1,5 min Schiessen dazu. Groesster Fall gluehwurm etwa 5,5 min, unter 10 min.
- **Speicher:** groesster Stapel gitter grob (12 x 320^2): etwa 20 MB je Feld, 10 bis 15 Felder, Klumpenanalyse
  int64; zusammen mit dem CUDA-Kontext unter 1 GB.

## 13. Was welches Ergebnis bedeuten wuerde

- **Irgendein Mehrball-Lauf "halten" oder ein Paar "gebunden":**
  - Kandidat fuer echte Q-Ball-Bindung ohne Verschmelzen, gegen Papier und Fable-Review.
  - Zuerst pruefen: L3, Spalt 7, laengeres T.
  - Danach der 1D-Bindungskurve (in Reparatur) gegenueberstellen.
- **Mitdrehender Ring wird zum Ball mit Windung 1:** Ringanalogon traegt. Ein drehender Q-Ball laesst sich aus Einzelbaellen
  zusammensetzen. Das ist neu fuer uns, verwandt mit [L] Battye und Sutcliffe 2000 (drehende Q-Baelle aus Stoessen).
- **Dyn/Statik gleichphasig >> 1:** Das Verschmelzen laeuft ueber Ladungsfluss in den Hals, nicht ueber eine Starrkoerperkraft.
  Das Paarpotential E(d) reicht dann nicht, um Vielball-Dynamik vorherzusagen.
- **Synchronisation gefunden:** gegen Liouville-Argument; zuerst Verschmelzen und Kontrolle pruefen.
- **Spiegelprobe verletzt:** Codefehler, falls schon frueh; spaete Verletzung zeigt nur verstaerkte Rundung (Chaos).
- **Tornado-Kern waechst mit Q:** gegen beide Papierwerte, Befund-Kandidat; zuerst Gueltigkeit bei 0,52 und 0,55.

## 14. Grenzen

- Explorativ; 2D statt 3D. Ein Ballgroesse (0,70) fuer fast alles; duennwandige Baelle koennen anders koppeln.
- **Klumpenschwelle 0,5:** Gleichphasige Baelle bilden schnell Bruecken ueber der Schwelle. "Verschmolzen" heisst dann
  "verbunden"; die Ortsdaten der Verfolger zeigen, ob die Kerne wirklich zusammenlaufen.
- **Verfolger** folgen einem Ball, solange er getrennt ist; nach dem Verschmelzen laufen sie zusammen.
- **Randschicht:** Auswertung endet bei t_rand; auseinanderlaufende Laeufe haben daher kuerzere Fenster.
- **T = 400 bis 1000:** Langsame Prozesse (Raten < 3e-3) sind unsichtbar; "offen" heisst "nicht entscheidbar".
- **Gluehwurm:** Die Anregung der Atmung ist eine Naeherung (Streckung plus Frequenzstoss); die Atemphasen werden
  gemessen, nicht gesetzt.
- **Literatur** aus dem Gedaechtnis, nicht nachgelesen.

## Latten (Vorschlag, die Leitung entscheidet)

| Karte | L1 kann scheitern | L2 Gegenprobe | L3 Numerik | L4 schon bekannt | L5 Messbezug |
|---|---|---|---|---|---|
| Paare (Grundlage) | ja: Bindung, kappa, Josephson-Strom, Starrkoerper | ja: Einzelball, Antisymmetrie, dphi = pi/2 | fein fuer drei Laeufe (10 %) | weitgehend: Phasenkraft und Josephson [L] | nein |
| Bio 25/42 Gitter | ja: Klassen vorab | ja: Spalt 7, Q3 gegen Q4 | fein fuer fuenf | teilweise | nein |
| Chemie 13 Kristall | ja: "haelt nicht" vorab | ja: Schachbrett, Streifen, 120 Grad | fein | Papier sagt nein | nein |
| Bio 46 Kapsid | ja: Ringanalogon, Drehsinn | ja: dreh-, k = 0 drehend | fein fuer fuenf | teilweise: Solitonhaufen [L] | mittelbar (Optik [L]) |
| Chemie 19 Aromatizitaet | ja | ja: N-Reihe | fein | Halskette [L] | mittelbar (Optik [L]) |
| Bio 11 Gluehwurm | ja: Sync vorab nein | ja: weite Kontrolle | fein fuer einen Lauf | Liouville | nein |
| Bio 47 Haendigkeit | schwach: Symmetrie erzwingt das Ergebnis | ja: exakte Spiegelbilder | fein fuer zwei | ja (Curie) | nein |
| Chemie 5 Isomere | ja: Energie, Umwandlung | ja: Knick | fein alle | teilweise | nein |
| Bio 26/40 Kollektiv | ja: Klassen vorab | ja: gleich/zufall, ruhend/bewegt | fein fuer zwei | teilweise | nein |
| Wellen 19 Auge | ja: Steigung, zwei Papierwerte | ja: m = 0 daneben | Klammer, Virialrest | teilweise (Wirbelkern) | nein |

**Vorschlag:**
- Rechnen: profile, paare, gitter, ringe (Kernkarten).
- gluehwurm und isomere rechnen, Erwartung "bekannt".
- haendigkeit vor allem als Codeprobe.
- kollektiv als billige Stichprobe.

## Einfach gesagt

Wir setzen viele kleine Q-Baelle nebeneinander, als Gitter, als Ring oder zufaellig verstreut, und schauen, ob sie wie
ein Kristall zusammenhalten. Jeder Ball hat eine innere Uhr; zeigen die Uhren zweier Nachbarn dasselbe, ziehen sie sich an
und verschmelzen schnell, zeigen sie Entgegengesetztes, stossen sie sich ab. Deshalb erwarten wir, dass kein Gitter haelt:
Gleich gestellte Baelle klumpen zusammen, abwechselnd gestellte fliegen auseinander. Spannend ist ein Ring, dessen Uhren
im Kreis weiterlaufen und der sich zugleich dreht: Er koennte sich zu einem einzigen wirbelnden Ball schliessen. Ausserdem
pruefen wir, dass das Modell links und rechts nicht unterscheidet und dass sich die Uhren nicht wie Gluehwuermchen
gleichtakten.

Ende der Bearbeitung: 2026-09-30 03:29:20 CEST (gemessen mit date). Beginn 2026-09-30 02:53:47 CEST.
