# R4-W: Laufplan fuer fuenf 1D-Wellentests (Runde 4, Karten Wellen 1, 2, 3, 12, 13)

Bearbeiter: Agent R4-W (Anthropic, Opus), Auftrag RUNDE-04/AUFTRAG-R4.md. Beginn 2026-09-30 01:25:36 CEST (gemessen),
Ende in der letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ.
Beruecksichtigt: Nachricht der Leitung zum Rechenort (01:31, P4000 ueber kleintest.sh) und zum Fable-Review
(ca. 02:00, kein duennes ruhiges Hintergrundmedium im Ein-Feld-Modell).

## Kurzfassung

- **Code:** wellen/wellen.py (PyTorch, float64 bzw. complex128, nur CUDA). Ein Unterbefehl je Test; jeder rechnet grob
  (dx = 0,1, dt = 0,05) und fein (dx = 0,05, dt = 0,025) und bewertet L2 und L3 selbst.
- **Uebernommen aus QG-1 (RUNDE-01/qg1/qg1.py):** Schiessen, Anker, Gitter, Zeitschritt, Velocity-Verlet, Schwamm,
  Parabelfit, Messung wie dort. Ohne Brechungsfeld (A = B = C = 1).
- **Neu:**
  - Profil-Zwischenspeicher (Schiessen nur einmal)
  - Profil an beliebigen Orten: kubisch nach Hermite, f' aus dem ersten Integral; noetig fuer bewegte Baelle
  - periodischer Rand fuer Monsterwelle und Stokes
- **Laufzeit auf der P4000:** je Test etwa 1 bis 2 min, das Schiessen einmal etwa 2,5 min. Keiner ueber 10 min.
- **Hintergrund:** Nur die Monsterwelle nutzt einen instabilen Hintergrund, mit Absicht.
  - Stokes und Surfen laufen mit freien Wellen um das stabile Vakuum.
  - Brandung laeuft mit dem stabilen dichten See S = 1.
  - Stokes (als Kondensatwelle) und Brandung (als duenne Rampe) sind in ihrer urspruenglichen Form im Ein-Feld-Modell
    nicht umsetzbar (Abschnitt 1).

## 1. Stabilitaet auf Papier (vor dem Code)

**Homogener Hintergrund** psi = sqrt(S0) exp(-i mu t) mit mu^2 = U'(S0) = 1 - 2 S0 + 1,5 S0^2.

- Stoerung ~ exp(i k x - i Omega t) im mitdrehenden System ergibt
  Omega^4 - Omega^2 (2 k^2 + beta + 4 mu^2) + k^2 (k^2 + beta) = 0 mit beta = 2 S0 U''(S0) = -4 S0 + 6 S0^2.
- Die Diskriminante ist (beta + 4 mu^2)^2 + 16 k^2 mu^2 > 0, also ist Omega^2 immer reell.
  - Omega^2 < 0 (Instabilitaet) genau dann, wenn beta < 0 und k^2 < -beta, also fuer 0 < S0 < 2/3.
  - Schall fuer beta > 0: c_s^2 = beta / (beta + 4 mu^2).
- Das stimmt mit Codex' Dispersionsrelation und dem Fable-Review (Z. 39-45) ueberein.

| S0 | beta | mu^2 | Lage | groesste Anwachsrate (von Hand) | bei k | Schall c_s |
|---|---|---|---|---|---|---|
| 0,1 | -0,34 | 0,815 | instabil | 0,094 | 0,40 | - |
| 0,3 | -0,66 | 0,535 | instabil | 0,226 | 0,53 | - |
| 0,8 | +0,64 | 0,36 | stabil | - | - | 0,555 |
| 1,0 | +2,0 | 0,50 | stabil | - | - | 0,707 |

**Folgen fuer die Karten:**

- **Wellen 1 Russell:** braucht keinen Hintergrund (Vakuum). Nicht betroffen.
- **Wellen 2 Monsterwelle:** will die Instabilitaet (S0 = 0,1 und 0,3). Die Gegenprobe ist S0 = 0,8 (stabil).
- **Wellen 3 Stokes-Drift:**
  - Als Welle auf einem Kondensat ist die Karte im Ein-Feld-Modell **nicht umsetzbar**:
    - Ein duennes Kondensat ist instabil.
    - Ein dichtes (S > 2/3) hat mu < 0,8 und damit ein kleineres omega als jeder Ball (> 0,707). Der Ball loest
      sich darin auf.
  - Umgesetzt wird die Karte mit einer **freien laufenden Welle um das Vakuum S = 0**:
    - lineare Dispersion w^2 = 1 + k^2, stabil
    - Die eigene schwache Fokussierung der Welle (aus -S^2 in U) waechst hoechstens mit (3/4) a^2 / w.
    - Bei a = 0,04 und w = 1,42 sind das 8,5e-4, ueber T = 400 ein Faktor 1,4 auf ohnehin winzige Keime.
  - Mit dem Medium als zweitem Feld ginge die Kondensatwelle: Ein zweites Feld mit abstossender Selbstwechselwirkung ist
    bei jeder Dichte stabil.
- **Wellen 12 Surfen:**
  - Ebenfalls nicht als Kondensatwelle; umgesetzt mit einem **freien Wellenpaket um das Vakuum**.
  - Eigene Fokussierung des Pakets: (3/4) A^2 / w = 0,029 bei A = 0,2 und 0,007 bei A = 0,1.
  - Das Paket A = 0,2 veraendert sich also unterwegs selbst ("grosse Welle fokussiert").
    - Es entspricht grob einem NLS-Soliton hoeherer Ordnung, N etwa 4.
    - Die Laeufe "nur Welle" zeigen das.
  - Die A^2-Skalierung wird nur aus A <= 0,1 gelesen.
  - Die Variante "Front" entspricht nach Lorentz-Invarianz der Brandung: ruhender Ball, bewegte Seewand statt bewegtem
    Ball und ruhender Wand. Sie wird deshalb nicht doppelt gerechnet.
- **Wellen 13 Brandung:**
  - Eine duenne, einstellbare Dichterampe ist im Ein-Feld-Modell **nicht umsetzbar**: Sie laeuft durch 0 < S < 2/3
    und zerfaellt.
  - Umsetzbar ist nur die **natuerliche Wand des dichten Sees**:
    - Bei omega^2 = 1/2 koexistieren Vakuum und S = 1 (U(S)/S hat dort sein Minimum 1/2).
    - Die Wand F^2 = 1 / (1 + exp(-sqrt2 (x - x_a))) ist eine exakte Loesung (f' = f (1 - f^2) / sqrt2).
    - Innen gilt beta = 2 > 0, also stabil.
    - Die Wand ist die feste "Rampe": 10 bis 90 Prozent der Dichte auf 3,1 Laengeneinheiten.
    - Der Bereich 0 < S < 2/3 der Wand ist nur etwa 2,3 lang, kuerzer als die kuerzeste instabile Wellenlaenge
      2 pi / sqrt(2/3) = 7,7. Deshalb erwarte ich keine lokale Instabilitaet; der Lauf "See allein" prueft das.
  - Mit dem Medium als zweitem Feld ginge eine frei waehlbare Rampe.

## 2. Aufruf (Leitung, auf der .69, Spur p4000a)

Vorschlag: wellen/wellen.py nach /home/fmh/fmhc-physics-remote/r4-wellen-20260930/ kopieren. Das Programm braucht nur torch.
Es schreibt profil_cache.pt neben sich und die Ergebnisse nach --out (Vorgabe: ausgabe/ neben dem Skript).
kleintest.sh setzt Lock, Unit, CUDA_VISIBLE_DEVICES, RuntimeMaxSec = 600 und das Arbeitsverzeichnis.

```
cd /home/fmh/fmhc-physics-remote/r4-wellen-20260930
# 1. Profil einmal schiessen (wie QG-1), etwa 2,5 min auf der P4000
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4w-profil wellen.py profil
# 2. Rauchtest: alle fuenf Tests mit T = 12, grob und fein, etwa 1 min
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4w-rauch wellen.py rauch --out rauchtest
# 3. Die fuenf Tests einzeln (Reihenfolge beliebig)
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4w-russell  wellen.py russell
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4w-monster  wellen.py monster
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4w-stokes   wellen.py stokes
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4w-surfen   wellen.py surfen
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4w-brandung wellen.py brandung
```

- Ohne Schritt 1 schiesst der erste Test selbst (dann etwa 2,5 min laenger, weiter unter 10 min).
- Der Rauchtest zeigt nur, ob alles durchlaeuft; seine Zahlen gelten nicht.
- Hochrechnung aus dem Rauchtest: Entwicklungszeit mal T / 12, also mal 25 (Monster) bis 42 (Russell). Das Programm
  gibt die Teilzeiten aus. Ergibt ein Test mehr als 9 min, nicht starten; die Leitung entscheidet.
- Ausgaben je Test: <test>_bericht.txt (lesbar, auch auf stdout), <test>_ergebnis.json (alle Zahlen, Kontrollen),
  <test>_reihen.pt (Zeitreihen).
- Grafikspeicher: hoechstens etwa 0,6 GB (Monster fein), die anderen unter 0,1 GB.

## 3. Laufzeit je Test (Schaetzung fuer die P4000, nicht gemessen)

Grundlage ist QG-1 auf der P5000. Dort kostete ein Verlet-Schritt etwa 1,2 ms, begrenzt durch die Zahl der
GPU-Aufrufe, nicht durch die Rechnung. Fuer die P4000 setze ich etwa 2 ms je Schritt an (Faktor 1,7).

| Test | Laeufe x Punkte (grob) | Schritte grob + fein | erwartet | Spanne |
|---|---|---|---|---|
| profil | 3 omega x 4096 Kandidaten | 4 x 8000 RK4 | 2,5 min | 1,5 bis 4 min |
| russell | 9 x 3001 | 10000 + 20000 | 1 min | 0,7 bis 2,5 min |
| monster | 12 x 8000 (periodisch) | 6000 + 12000 | 1 min | 0,7 bis 3 min |
| stokes | 7 x 2560 (periodisch) | 8000 + 16000 | 1 min | 0,5 bis 2 min |
| surfen | 9 x 3001 | 9000 + 18000 | 1 min | 0,6 bis 2,5 min |
| brandung | 16 x 3001 | 9000 + 18000 | 1,2 min | 0,7 bis 3 min |
| rauch | alle fuenf, T = 12 | je etwa 700 | unter 1 min | mit Schiessen bis 4 min |

- Dazu je Aufruf 10 bis 20 s fuer den Start von Python und CUDA.
- **Zusammen:** etwa 9 min fuer Profil, Rauchtest und fuenf Tests. Jeder einzelne Aufruf liegt klar unter 10 min.

## 4. Die Tests: Aufbau, Vorhersage, Gegenprobe, Aufloesung

Gemeinsam: Ball omega^2 = 0,7, geschossen wie QG-1. Profilwerte: f(0)^2 = 0,3675, Q = 2,441, E = 2,297.
K0 prueft das interpolierte Schussprofil gegen den Anker (Grenze 1e-6).
L3 heisst ueberall: Effekt mindestens fuenfmal so gross wie die Aenderung zwischen grob und fein.

### 4.1 Russell (Wellen 1): `russell`

- **Aufbau:**
  - Box [-150, 150], Dirichlet-Rand, Schwamm ab |x| = 110.
  - Zwei Baelle bei x = -20 und +20 mit v = +-0,1, 0,3, 0,5, exakt geboostet (Lorentz).
  - Zwei Phasenlagen:
    - gleichphasig (Spiegelbild, psi_R(x) = psi_L(-x))
    - gegenphasig (psi_R(x) = -psi_L(-x); Knoten bei x = 0)
- **Messung** zur Zeit t_m = 50/v (500, 167, 100), wenn die Baelle wieder bei etwa +-30 sind:
  - Abgestrahlter Energieanteil = 1 - (Energie in Fenstern +-15 um die beiden Ladungsschwerpunkte der Halbraeume)
    / Anfangsenergie.
  - ebenso fuer die Ladung, dazu Lage und Geschwindigkeit danach
  - Langsame Strahlung, die noch im Fenster liegt, zaehlt als Ball; der Wert ist also eine untere Schranke.
- **Gegenprobe:** ein einzelner Ball mit derselben Geschwindigkeit, derselbe Messweg (Fenster um den Schwerpunkt).
- **Vorhersage (vor dem Rechnen):**
  - Einzelball: abgestrahlt unter 1e-5 (Gitterfehler des geboosteten Profils).
  - gleichphasig v = 0,1: Die Baelle verschmelzen zu einem angeregten Klumpen bei x = 0.
    - Der Grundzustand mit Q = 4,88 (omega^2 etwa 0,52) haette E etwa 4,2 statt 4,62.
    - Bis t_m sind 3 bis 9 Prozent der Energie abgestrahlt.
  - gleichphasig v = 0,3 und 0,5: Die Baelle laufen durcheinander hindurch (getrennt). Abgestrahlt 1e-4 bis 1e-2,
    bei 0,5 weniger als bei 0,3.
  - gegenphasig: Sie stossen sich ab und verschmelzen nie. Abgestrahlt unter 1e-3 bei v = 0,1, 1e-3 bis 1e-2 bei 0,3
    und 0,5.
  - Hypothese H der Karte (Anteil haengt von v ab): erwartet ja, am staerksten durch das Verschmelzen bei v = 0,1.
- **Aufloesung (L3):** kleinster Stoss-Anteil mindestens fuenfmal so gross wie die groesste Aenderung grob/fein.
  Erwartet bestanden.
- **Scheitert, wenn:** alle Stoesse weniger als das Fuenffache des Einzelballs abstrahlen (dann waere das Modell
  hier praktisch integrabel), oder wenn der Anteil nicht von v abhaengt.

### 4.2 Monsterwelle (Wellen 2): `monster`

- **Aufbau:**
  - periodische Box der Laenge 800, Hintergrund sqrt(S0) exp(-i mu t)
  - S0 = 0,1 und 0,3 (instabil), dazu die Gegenprobe S0 = 0,8 (stabil)
  - Rauschen: komplex, rms 1e-3, nur Moden 0 < |k| <= 2, fester Seed je Lauf, je S0 vier Seeds.
    Die Moden sind auf beiden Gittern dieselben; grob und fein starten also mit demselben Feld.
  - T = 300, Schnappschuesse von S alle 2 Zeiteinheiten
- **Statistik** je S0 in zwei Fenstern, [50, 150] und [150, 300], gepoolt ueber Seeds, Zeiten und Orte:
  - Mittel M und Varianz V von S.
  - **Gauss-Rayleigh-Erwartung mit gleichem Mittel und gleicher Varianz:** S = |m + z|^2 mit z komplex gauss.
    - Das ist eine Rice-Verteilung, bei m = 0 Rayleigh.
    - Ihre Parameter folgen geschlossen aus M und V: sigma^2 = (M - sqrt(M^2 - V)) / 2 und |m|^2 = M - 2 sigma^2.
    - Ist V >= M^2, gibt es keine Loesung; dann dient die Rayleigh-Verteilung mit gleichem Mittel als Referenz.
      Schon das ist ein schwerer Schwanz.
  - Ueberschreitungen fuer die Schwellen 4 S0 (die Karte: Amplitude ueber dem Doppelten des Hintergrunds), 2, 4 und
    6 M sowie M + 2, 3, 4 und 5 Standardabweichungen: beobachtet gegen erwartet.
  - Persistenz: Anteil der Ueberschreitungen von 4 S0, die 2 Zeiteinheiten spaeter noch bestehen. Kurzlebige
    Spitzen haben kleine Persistenz, Q-Baelle grosse.
  - Erhaltung von E und Q in der periodischen Box.
- **Vorhersage:**
  - S0 = 0,8 (stabil): Das Rauschen bleibt linear und gaussisch.
    - Verhaeltnis beobachtet/erwartet bei M + 2 und M + 3 sd zwischen 0,5 und 2
    - S_max/S0 unter 1,02; keine Ueberschreitung von 4 S0
  - S0 = 0,3: Die Instabilitaet saettigt bei t etwa 30 bis 45. Es entstehen flache Klumpen mit S etwa 0,8 bis 0,95.
    - Kein ruhender Q-Ball erreicht S > 1. Ueberschreitungen von 4 S0 = 1,2 koennen also nur kurzlebig sein.
    - Ich erwarte sie seltener als nach Rice (Verhaeltnis unter 1, leichter Schwanz), weil der S^3-Term hohe Dichten
      abstoesst.
    - S_max/S0 hoechstens 4,3.
  - S0 = 0,1: Die Instabilitaet saettigt bei t etwa 70 bis 100. Es entstehen Q-Baelle mit omega^2 etwa 0,6 bis 0,65
    und S in der Mitte 0,45 bis 0,55, also ueber 4 S0 = 0,4.
    - Ueberschreitungen sind haeufig (Verhaeltnis ueber 3 im Spaetfenster) und bleiben bestehen (Persistenz ueber 0,8).
    - Das sind keine Monsterwellen, sondern die Bildung von Q-Baellen.
  - Hypothese H der Karte (kurzlebige Spitzen haeufiger als Zufall): erwartet in keiner der beiden Dichten bestaetigt.
  - Erhaltung: relative Drift von E und Q unter 1e-5.
- **Gegenprobe:** der stabile Hintergrund S0 = 0,8. Dort muss die Statistik gaussisch sein.
- **Aufloesung (L3):** Logarithmus des Verhaeltnisses bei 4 S0 im Spaetfenster, fein gegen grob, Faktor 5.
  - Die Einzelbahnen sind chaotisch und nicht vergleichbar, die Statistik schon.
  - Bei S0 = 0,1 erwartet bestanden. Bei 0,3 unsicher, falls es nur wenige Ueberschreitungen gibt.

### 4.3 Stokes-Drift (Wellen 3): `stokes`

- **Aufbau:**
  - periodische Box der Laenge 256
  - Ball in Ruhe bei x = 0
  - freie reelle Welle a cos(k x - w t) mit k = 2 pi 41/256 = 1,0063, w = 1,4187 (Periode 4,43). Sie traegt keine
    Ladung.
  - T = 400, Parabelfit des Ladungsschwerpunkts auf [50, 400] wie in QG-1
- **Laeufe:**
  - laufend nach rechts mit a = 0,01, 0,02, 0,04
  - laufend nach links mit a = 0,04 (Spiegelprobe)
  - stehend (zwei laufende Wellen a = 0,04), Bauch am Ball (Gegenprobe)
  - stehend, Knoten am Ball (Diagnose)
  - ohne Welle
- **Messgroessen:**
  - Drift dX ueber das Fitfenster, Drift je Wellenperiode, Beschleunigung, Anfangsgeschwindigkeit
  - Zittern um die Parabel
  - Ladungsaenderung im Fenster
- **Vorhersage:**
  - Der Ball driftet in Laufrichtung der Welle, dX ~ a^2: dX(0,02)/dX(0,01) und dX(0,04)/dX(0,02) je 4 +- 0,8.
  - Mechanismus: vermutlich Strahlungsdruck (Teilreflexion am Ball). Dann waechst die Drift je Periode mit der Zeit
    (Beschleunigung), statt konstant zu sein wie die Stokes-Drift im Wasser.
    - Der Impulsfluss der Welle ist a^2 k^2 = 1,6e-3 bei a = 0,04.
    - Mit einem Reflexionsgrad R von 1e-3 bis 1e-2 folgt dX(0,04) etwa 0,01 bis 1.
  - Ungewiss ist das Vorzeichen: Fuer Kinks ist negativer Strahlungsdruck bekannt. Ich erwarte + (etwa 70 Prozent).
  - Stehende Welle mit Bauch und Lauf ohne Welle: |dX| unter 1e-9 (Symmetrie).
  - Links gegen rechts: dX(links) = -dX(rechts) auf 1e-6.
  - Stehende Welle mit Knoten: |dX| unter einem Zehntel des laufenden Werts, ausser der Knoten ist ein labiles
    Gleichgewicht. Dann rutscht der Ball zum Bauch; das waere ein Hinweis auf eine ponderomotorische Kraft.
  - Ladungsaenderung des Balls unter 1e-3.
- **Gegenprobe:** stehende Welle (Bauch) und ohne Welle, keine Netto-Drift.
- **Aufloesung (L3):** dX(0,04) fein gegen grob, Faktor 5. Erwartet bestanden.
- **Scheitert, wenn:** die Drift nicht mit a^2 geht (Schwelle, Einfang), oder wenn sie gegen die Laufrichtung zeigt.
  Letzteres waere ein echter Befund-Kandidat.

### 4.4 Surfen (Wellen 12): `surfen`

- **Aufbau:**
  - Box [-150, 150] mit Schwamm, Ball ruht bei x = 0.
  - Reelles Wellenpaket A exp(-(x + 60)^2 / 450) cos(0,3 (x + 60) - w t) mit Zeitableitung, sodass es nach rechts
    laeuft.
    - Traeger k = 0,3, w = 1,044, Gruppengeschwindigkeit v_g = 0,287
    - Es erreicht den Ball bei t etwa 200 und hat ihn bei etwa 320 ueberholt.
  - A = 0,025, 0,05, 0,1, 0,2; T = 450
  - Je A ein Lauf "nur Welle", um die Energie des Pakets im Ballfenster abzuziehen.
- **Messgroessen:**
  - Endgeschwindigkeit (Gerade auf [400, 450]); "mitgenommen", wenn sie ueber v_g/2 liegt
  - kleinster und groesster Ort waehrend des Durchgangs
  - Energiegewinn des Balls im Fenster +-15 (Paket abgezogen)
  - Verformung (S_max, Breite)
- **Papierrechnung:**
  - Zeitgemittelt zieht die Welle den Ball an: Wechselwirkungsenergie etwa (A^2/2) Int(-4 S + 4,5 S^2) = -2,2 A^2.
  - Im Paketsystem hat der Ball die Relativenergie (gamma(v_g) - 1) E = 0,10.
  - Eine anziehende, zeitlich feste Mulde kann einen Ball mit positiver Relativenergie nicht einfangen, gleich wie tief
    sie ist. Er laeuft hindurch.
- **Vorhersage:**
  - Kein Mitnehmen bei allen A.
  - Beim Durchgang wird der Ball zuerst zum Paket hin gezogen (X_min < 0), danach bleibt er zurueck.
  - Endgeschwindigkeit klein und positiv (Strahlungsdruck): unter 3e-3 bei A = 0,1 und unter 1e-2 bei A = 0,2.
    Fuer A <= 0,1 skaliert sie mit A^2 (Verhaeltnisse etwa 4).
  - Energiegewinn unter 1 Prozent.
  - Das Paket A = 0,2 fokussiert sich unterwegs selbst: S_max der Welle allein steigt ueber A^2 = 0,04.
- **Gegenprobe:** Ball ohne Welle: |v| unter 1e-6, Energiegewinn unter 1e-5.
- **Aufloesung (L3):** Endgeschwindigkeit fein gegen grob bei A = 0,1 und 0,2, Faktor 5.
  - Bei sehr kleiner Endgeschwindigkeit kann L3 scheitern. Dann lautet die Aussage nur "kein messbarer Gewinn".
- **Scheitert (meine Vorhersage), wenn:** der Ball mitgenommen wird. Dann stimmt die Hypothese der Karte, und die
  Mulde ist nicht zeitlich fest (Fokussierung, Abstrahlung).

### 4.5 Brandung (Wellen 13): `brandung`

- **Aufbau:**
  - Box [-150, 150] mit Schwamm.
  - Der See: S = 1 auf [20, 100] mit zwei exakten Waenden, mu = 1/sqrt2, Ladung etwa 113.
  - Der Ball startet bei x = -5 mit v = 0,1, 0,3, 0,5 nach rechts.
  - Vier Startphasen (0, pi/2, pi, 3 pi/2). Da der Ball schneller dreht als der See, bestimmt die Startphase die
    Phasenlage beim Kontakt. Eine der vier liegt hoechstens pi/4 von gleichphasig entfernt, eine von gegenphasig.
  - T = 450; Kontakt bei t etwa 190, 63, 38.
- **Messgroessen:**
  - Ladung vor dem Strand (x < 16), im See, hinter dem See (x > 104)
  - Schwerpunkt, Breite und S_max vor dem Strand; Wandort (S = 0,5)
  - Ausgang:
    - zurueckgeworfen: mindestens 80 Prozent der Ladung vorn und laeuft zurueck
    - aufgenommen: mindestens 80 Prozent im See
    - durchgereicht: mindestens 50 Prozent hinter dem See
    - sonst zerbrochen oder teilweise aufgenommen
  - Verformung vor dem Kontakt; S_max und Breite eines zurueckgeworfenen Balls am Ende
- **Vorhersage:**
  - Der Ball hat das hoehere omega (0,837 gegen 0,707), also das hoehere chemische Potential. Beim Kontakt fliesst
    seine Ladung in den See.
    - Ueberwiegend "aufgenommen": Zerfall ja in mindestens 9 der 12 Laeufe.
    - Nahe gegenphasig bei v = 0,1 ist "zurueckgeworfen" moeglich, mit mindestens 10 Prozent Ladungsverlust.
  - Nie "durchgereicht" (Anteil hinter dem See unter 0,1).
  - Verformung vor dem Kontakt unter 1e-3; der Schwanz des Sees ist bei x < 13 kleiner als 1e-4.
  - Aufgenommene Ladung verbreitert den See um 2,44/1,414 = 1,7 Laengeneinheiten.
    - Die linke Wand wandert um 0,5 bis 1,7 zum Ball hin (x_wand sinkt), je nachdem, wie sich die Verbreiterung auf
      beide Waende verteilt.
    - Das ist eine scharfe Mengenvorhersage.
- **Gegenproben:**
  - See allein: Wand wandert hoechstens 0,5, Seeladung aendert sich hoechstens um 1e-3. Das prueft die gewaehlte
    stabile Dichte.
  - Ball allein: Verformung vor x = 10 unter 1e-3.
- **Aufloesung (L3):** gleicher Ausgang grob und fein in allen 12 Laeufen, und die Anteile aendern sich hoechstens
  um 0,2. Der Effekt ist die ganze Ballladung (1), also Faktor 5.

## 5. Latten (Vorschlag, die Leitung entscheidet)

Alle Literaturangaben stammen aus dem Gedaechtnis und sind nicht nachgelesen. Vor einer Verwendung ueber L4 hinaus
muessen sie an der Quelle geprueft werden.

| Test | L1 kann scheitern | L2 Gegenprobe | L3 Numerik | L4 schon bekannt | L5 Messbezug |
|---|---|---|---|---|---|
| Russell | ja: Stoesse koennten kaum strahlen oder v-unabhaengig sein | Einzelball, gleicher Messweg | fein/grob, Faktor 5 | weitgehend (Fable: "Nichtintegrabilitaet strahlt, bekannt"; 1D-Q-Ball-Stoesse in der Literatur, nicht gesucht) | mittelbar: Stoesse von Materiewellen-Solitonen im BEC, phasenabhaengig (Nguyen u. a. 2014, aus dem Gedaechtnis) |
| Monsterwelle | ja: S0 = 0,3 kann schwer statt leicht, S0 = 0,1 gaussisch statt schwer ausfallen | stabiler Hintergrund S0 = 0,8 | Statistik fein/grob, Faktor 5 | weitgehend: Modulationsinstabilitaet bildet Q-Baelle (Kusenko, Shaposhnikov 1998; Kasuya, Kawasaki 2000), Monsterwellen der NLS (Akhmediev; Agafontsev, Zakharov 2015) | mittelbar: Monsterwellen-Statistik in Glasfasern (Solli u. a. 2007) und Wellenkanaelen, nur Analogie |
| Stokes | ja: Vorzeichen, a^2-Gesetz | stehende Welle (Bauch), ohne Welle, links gegen rechts | fein/grob, Faktor 5 | teilweise: Strahlungsdruck auf Solitonen, negativer Strahlungsdruck bei Kinks (Forgacs, Lukacs, Romanczukiewicz 2008) | keiner direkt; die Stokes-Drift im Wasser ist ein anderer, kinematischer Mechanismus |
| Surfen | ja: Mitnehmen wuerde meiner Vorhersage widersprechen | Ball ohne Welle, Welle ohne Ball | fein/grob, Faktor 5 (kann bei winzigem Effekt scheitern) | vermutlich: Soliton-Wellenpaket-Wechselwirkung in der NLS | keiner |
| Brandung | ja: Ausgang und Wandverschiebung koennen anders ausfallen | See allein, Ball allein | gleicher Ausgang, Anteile +-0,2 | teilweise: Aufloesung im Medium mit kleinerem chemischen Potential (Fable: Bio 2, Chemie 9) | mittelbar: Tropfen auf einem Bad (teilweise Verschmelzung, Abprallen), nur Analogie |

## 6. Grenzen

- **Ungetestet:** Der Code ist nicht gelaufen; deshalb zuerst der Rauchtest.
- **Ein Kanal, 1D:** Kein duennes stabiles Medium (Abschnitt 1). Drei Karten sind deshalb nur in abgewandelter Form
  gerechnet:
  - Stokes und Surfen mit freien Wellen
  - Brandung mit der natuerlichen Seewand
- **Russell:** Die Strahlung ist eine untere Schranke, weil langsame Strahlung nahe am Ball als Ball zaehlt.
- **Monster:** Die Statistik ist eine Punktstatistik von S (Ueberschreitungswahrscheinlichkeit), keine Statistik
  der Maxima. Die Rice-Referenz passt nur Mittel und Varianz von S an, nicht das Spektrum.
- **Stokes:**
  - Die Welle ist gleich zu Beginn ueberall da; das Einschwingen faellt in [0, 50] und liegt vor dem Fitfenster.
  - Die Gitterdispersion mischt etwa 2e-4 der Gegenwelle bei; das ist vernachlaessigbar.
- **Surfen:** Das Paket A = 0,2 ist stark nichtlinear und aendert sich selbst.
- **Brandung:** Die Rampenbreite ist durch das Modell festgelegt (3,1) und nicht einstellbar.

## Einfach gesagt

Wir testen fuenf Ideen aus der Welt der Wasserwellen an unseren Feldklumpen, den Q-Baellen, in einer Raumdimension. Vorher
haben wir auf Papier geprueft, wann ein ruhiges "Meer" aus Feld ueberhaupt stabil ist: Ein duennes Meer zerfaellt von
selbst in Klumpen, ein stabiles ist so dicht, dass sich ein Ball darin aufloest. Deshalb stossen wir zwei Baelle im leeren
Raum zusammen, lassen ein duennes Meer absichtlich zerfallen und zaehlen, wie oft extreme Spitzen auftreten, schicken
freie Wellen auf einen Ball und lassen einen Ball in einen dichten "See" laufen. Unsere Vorhersagen: Stoesse strahlen
messbar Energie ab, echte Monsterwellen gibt es hier nicht, Wellen schieben den Ball mit einer Kraft, die mit dem Quadrat
der Wellenhoehe waechst, ein Ball kann nicht auf einer Welle surfen, und im See loest er sich meistens auf. Gerechnet
ist noch nichts; alle Tests zusammen brauchen etwa neun Minuten auf einer Grafikkarte.

Ende der Bearbeitung: 2026-09-30 02:12:57 CEST (gemessen mit date).
