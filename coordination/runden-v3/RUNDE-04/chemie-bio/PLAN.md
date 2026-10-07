# R4-CB: Laufplan fuer die 1D-Tests Chemie/Biologie und die Zufallskarte Artbildung (Runde 4)

Bearbeiter: Agent R4-CB (Anthropic, Opus), Auftrag RUNDE-04/AUFTRAG-R4.md. Beginn 2026-09-30 01:25:43 CEST (gemessen), Ende
in der letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ; alle Aussagen unten sind
Vorhersagen oder Hypothesen, keine Befunde.

## Kurzfassung

- **Code:** chemie_bio.py (PyTorch, float64 bzw. complex128, nur CUDA). Ein Unterbefehl je Test, dazu `rauch`.
- **Rechenort:** Quadro P4000 ueber kleintest.sh (Spur p4000a), laut Nachricht der Leitung von 01:31.
- **Laufzeit:** je Test 0,5 bis 3 min erwartet, hoechstens 5 min; alle zusammen etwa 8 bis 10 min. GPU-Speicher je Test
  unter 0,5 GB.
- **Kernvorhersagen:**
  - Katalyse: Exakt gegenphasige gleiche Baelle verschmelzen bei keinem v (Symmetriesatz). Der dritte Ball ist eher
    Reaktionspartner als Katalysator.
  - Kettenreaktion: Die Front erlischt nach hoechstens einem Paar.
  - Chromatographie: Der grosse Ball (omega^2 = 0,6) braucht laenger. Die Trennung waechst etwa mit eps^2.
  - Neuron: Die Antwort ist glatt, ohne Schwelle.
  - Wundheilung: Die Schiefe heilt in einigen zehn Zeiteinheiten; die Atmung bleibt.
  - Nervenfaser: Ein Stoss laeuft fast ungedaempft wie in einer Toda-Kette; eine Atem-Erregung wird nicht weitergeleitet.
  - Artbildung: Nur die 3D-Familie hat einen Knick (Q_min). Die 2D-Familien sind monoton und kreuzen sich nicht.

## 1. Modell und Uebernahme aus qg1.py

- **Modell:** L = |psi_t|^2 - |psi_x|^2 - U(S) - V(x) S mit S = |psi|^2 und U = S - S^2 + S^3/2, also
  psi_tt = psi_xx - (U'(S) + V) psi. V ist nur in der Chromatographie ungleich null.
- **Ladung und Energie:** Ladungsdichte rho = 2 Im(psi conj(psi_t)), Ladung Q = 2 omega Int f^2, Energie
  E = Int |psi_t|^2 + |psi_x|^2 + U.
- **Unveraendert aus qg1.py:**
  - Schiessen (rhs, rk4, schiessen, profil_bahn) und der analytische Anker mit anker_wgv
  - Gitter mit x = 0 auf einem Punkt
  - dx/dt grob 0,1/0,05 und fein 0,05/0,025
  - Velocity-Verlet mit Dirichlet-Rand und quadratischer Daempfungsschicht (sigma0 = 1, Breite 40), Messabstand 1
- **Aenderungen (bitte pruefen):**
  1. Die Boxlaenge haengt vom Test ab: 120, fuer Kette und Nervenfaser 180. Die Daempfung beginnt jeweils 40 vor dem Rand.
  2. Die Anfangsdaten kommen aus dem **analytischen Anker** f^2 = 2 a0 / (1 + b0 cosh(2 sqrt(a0) x)) samt f'.
     - Grund: Verschobene und Lorentz-geboostete Baelle brauchen f an beliebigen Stellen.
     - In qg1 stimmte der Schuss auf 1,2e-10 mit dem Anker ueberein.
     - Der Schuss laeuft als Kontrolle K0 (Unterbefehl `profil`). K0b prueft f' gegen zentrale Differenzen.
  3. **Bewegte Baelle:** exakter Lorentz-Boost psi = f(gamma(x - x0 - vt)) exp(-i omega gamma (t - v(x - x0)) + i phi).
     Das Modell ist Lorentz-invariant (c = 1). Die Ladung bleibt dabei Q0.
  4. **Artbildung:** radiales Schiessen nach demselben Einschachtelungsschema, mit drei Anpassungen:
     - logarithmischer Parameter
     - 256 Kandidaten, 6 Runden
     - Klammer = erster Klassenwechsel zwischen entschiedenen Nachbarn
     Fuer m = 0 wird die Abweichung g = f - f_t vom oberen Gipfel integriert, mit W'(f_t) = 0 exakt. Nur so sind duenne
     Waende (3D-Radius etwa 70 bei omega^2 = 0,51) in float64 erreichbar.
  5. Die 89 Zufallszahlen der Chromatographie zieht der CPU-Generator (torch, fester Seed, geraeteunabhaengig). Gerechnet
     wird alles auf CUDA.
- **Hintergrundkondensat:** Kein Test braucht eines. Die Chromatographie nutzt ein kleines Massenpotential, kein
  Kondensat; eine Stabilitaetsbegruendung entfaellt deshalb.

## 2. Aufruf (Leitung, .69, Spur p4000a)

Vorschlag: chemie_bio.py nach /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930/ kopieren. Das Programm braucht nur torch
und schreibt nur in --out. kleintest.sh setzt Lock, Unit, CUDA_VISIBLE_DEVICES, RuntimeMaxSec 600 und das
Arbeitsverzeichnis.

Zuerst der Rauchtest. Er rechnet alle Teile ausser dem K0-Schuss mit T = 20 und kleinem Schiessen; Dauer unter 1,5 min.

```
cd /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4cb-rauch chemie_bio.py rauch --out rauchtest
```

Nur bei rc = 0 weiter, je Test ein Aufruf (Reihenfolge beliebig):

```
cd /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4cb-profil chemie_bio.py profil --out ausgabe
cd /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4cb-kat chemie_bio.py katalyse --out ausgabe
cd /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4cb-kette chemie_bio.py kette --out ausgabe
cd /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4cb-chrom chemie_bio.py chromatographie --out ausgabe
cd /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4cb-neuron chemie_bio.py neuron --out ausgabe
cd /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4cb-wunde chemie_bio.py wunde --out ausgabe
cd /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4cb-nerv chemie_bio.py nerv --out ausgabe
cd /home/fmh/fmhc-physics-remote/r4-chemie-bio-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r4cb-art chemie_bio.py artbildung --out ausgabe
```

- **Ausgaben je Test in --out:** `<test>.json` mit allen Zahlen, `<test>_bericht.txt` mit lesbaren Tabellen (auch auf
  stdout); im Rauchtest mit dem Praefix `rauch_`.
- **Abbruch:** Jeder 1D-Test prueft, ob alle Messwerte endlich sind, und bricht sonst ab.
- **Spur p4000b:** kleintest.sh kennt auch p4000b. Die Leitung hat p4000a genannt; p4000b nur, wenn sie es freigibt.

## 3. Laufzeit je Test (Schaetzung fuer die P4000, nicht gemessen)

- **Grundlage:** qg1 auf der P5000 brauchte 1,2 ms je Verlet-Schritt und 2,1 ms je Schiess-Schritt.
- **Engpass:** die Zahl der GPU-Aufrufe, nicht die float64-Arithmetik. Der P4000-Faktor 1,7 wirkt deshalb nur auf die
  groessten Stapel; die Obergrenze unten rechnet ihn trotzdem ganz ein.

| Test | Arbeit (grob + fein) | erwartet | Obergrenze |
|---|---|---|---|
| rauch | alle Teile, T = 20, kleines Schiessen | 0,5 min | 1,5 min |
| profil (K0) | qg1-Schiessen 4 omega (40 000 RK4-Schritte) | 1,5 min | 3 min |
| katalyse | 64 Laeufe, T = 300: 6 000 + 12 000 Schritte | 0,6 min | 1,5 min |
| kette | 10 Laeufe, Box 180, T = 600: 12 000 + 24 000 Schritte | 0,8 min | 2 min |
| chromatographie | 39 Laeufe, T = 420: 8 400 + 16 800 Schritte | 0,6 min | 1,5 min |
| neuron | 25 Laeufe, T = 300: 6 000 + 12 000 Schritte | 0,5 min | 1 min |
| wunde | 10 Laeufe, T = 400: 8 000 + 16 000 Schritte | 0,6 min | 1,5 min |
| nerv | 12 Laeufe, Box 180, T = 400: 8 000 + 16 000 Schritte | 0,6 min | 1,5 min |
| artbildung | 196 Zeilen x 256 Kandidaten, 6 Runden, h = 0,04 und 0,08 (etwa 39 000 RK4-Schritte) | 2,5 min | 5 min |

Jeder Test bleibt unter der 10-Minuten-Grenze der Unit; zusammen sind es etwa 8 bis 10 min.

## 4. Tests: Aufbau, Vorhersage, Gegenprobe, L3

Alle 1D-Tests laufen grob und fein im selben Aufruf. **L3** heisst: Der gemessene Effekt ist mindestens fuenfmal groesser als
seine Aenderung von grob zu fein; der Bericht gibt beide Zahlen aus. Eichwerte des Ankers bei omega^2 = 0,6 / 0,7 / 0,8:

- Q = 3,163 / 2,441 / 1,886
- E = 2,878 / 2,299 / 1,818
- S_max = 0,553 / 0,368 / 0,225

### 4.1 Katalyse (Chemie 8)

- **Aufbau:**
  - A (Phase 0) startet bei -12 mit +v, B (Phase dphi) bei +12 mit -v; alle drei Baelle haben omega^2 = 0,7.
  - C ruht bei 0: Phase dphi/2 (`bruecke`) oder dphi/2 + pi (`sperre`).
  - Kontrollen: `ohne` (kein C) und `nur_AC` (kein B).
  - dphi in {pi, 3pi/4}, v in {0,05; 0,1; 0,15; 0,2; 0,3; 0,4; 0,5; 0,6}; 64 Laeufe, T = 300.
- **Messung:**
  - Klumpen = zusammenhaengend S > 0,05 in |x| < 75.
  - "Verschmolzen" heisst: Der groesste Klumpen traegt im Mittel der letzten 50 Zeiteinheiten mindestens 1,5 Q0.
  - Schwelle = kleinstes v mit Verschmelzung.
- **Warum ein v-Raster statt "knapp unter der Schwelle":**
  - Die Schwelle ist noch nicht gemessen; Chemie 7 in Runde 3 laeuft noch.
  - Das Raster liefert die Schwelle mit und ohne C im selben Lauf.
- **Vorhersage:**
  1. **dphi = pi, ohne: keine Verschmelzung bei irgendeinem v** (Muster `........`). Begruendung:
     - Die Anfangsdaten sind exakt ungerade, psi(-x) = -psi(x), und die Gleichung erhaelt das.
     - Also gilt psi(0, t) = 0, und keine Ladung kann x = 0 passieren.
     - In 1D gibt es keinen ungeraden stationaeren Ball: Das erste Integral f'^2 = 2 W(f) mit W(0) = 0 erzwingt
       f'(0) = 0 bei f(0) = 0, also f = 0.
     - Eine Verschmelzung bei exakt gegenphasigen gleichen Baellen waere ein Codefehler oder eine Instabilitaet, die
       Rundungsfehler aufblaeht. Beides waere ein Befund-Kandidat.
     - Folge: Eine "Verschmelzungsschwelle" gibt es hier nicht; die Frage "senkt C die Schwelle" wird zu "macht C eine
       Verschmelzung erst moeglich".
  2. **dphi = 3pi/4, ohne:** offen.
     - Hypothese (Chemie 7): Verschmelzung hoechstens in einem mittleren v-Fenster.
     - Mechanismus: Der Ladungsaustausch dreht die relative Phase ins Anziehende.
     - Bei kleinem v prallen die Baelle weit vorher ab, bei grossem v laufen sie durch.
  3. **bruecke:** Bei kleinem v (<= 0,2) entsteht mindestens ein Klumpen mit etwa 2 Q0. Dieselbe Verschmelzung zeigt aber
     schon `nur_AC`: **C wirkt als Reaktionspartner, nicht als Katalysator.** Ein Katalysator im strengen Sinn ist in 1D
     kaum pruefbar, weil C im Weg liegt.
  4. **sperre bei 3pi/4:** C stoesst A und B ab (cos(5pi/8) < 0); weniger Verschmelzung als `ohne`.
- **Codeprobe:** Bei dphi = pi sind `bruecke` und `sperre` Spiegelbilder (x -> -x, globale Phase pi). Beide Muster
  muessen gleich sein; sonst liegt ein Fehler vor.
- **Gegenproben:** `ohne`, `nur_AC`, `sperre`.
- **L3:**
  - Effekt: groesster Unterschied |q1(bruecke) - q1(ohne)|/Q0 ueber alle v und dphi.
  - Aenderung: groesste Abweichung von q1/Q0 zwischen grob und fein.
  - Zusaetzlich meldet der Bericht, ob die Klassen gleich bleiben.

### 4.2 Kettenreaktion (Chemie 16)

- **Aufbau:**
  - Fuenf Paare, omega^2 = 0,7, innen gleichphasig im Abstand d_in; Nachbarpaare gegenphasig im Abstand d_in + 4.
  - Die Gegenphase verhindert, dass die Produkte ineinander laufen.
  - `zuend`: Paar 0 steht mit Abstand 8 und verschmilzt fast sofort.
  - `kalt`: dieselbe Reihe ohne Zuendung.
  - `paar`: ein einzelnes Paar (natuerliche Verschmelzungszeit); `zuendpaar`: einzelnes Paar mit Abstand 8.
  - d_in in {16, 20, 24}; T = 600, Box 180.
- **"Knapp unterkritisch":**
  - Das Paar verschmilzt von selbst erst nach der Laufzeit.
  - Handrechnung aus den Schwaenzen: V(d) = -4 kappa A^2 e^{-kappa d} mit A^2 = 4 a0/b0 = 1,897 und kappa = 0,548.
  - Fallzeit aus der Ruhe: t_f = 2,13 e^{kappa d/2}, also 19 / 171 / 510 / 1520 fuer d = 8 / 16 / 20 / 24.
  - Damit ist d_in = 16 ueberkritisch (verschmilzt allein), 20 kritisch (knapp vor T) und 24 unterkritisch.
  - Die Laeufe `paar` messen die Zeiten direkt.
- **Messung:**
  - Paar k gilt als verschmolzen, sobald die Ladungs-RMS-Breite im Paarfenster unter 3 faellt.
  - "Gezuendet" heisst: t_zuend < 0,8 t_kalt.
  - Reichweite = Zahl der aufeinanderfolgend gezuendeten Paare.
  - Frontgeschwindigkeit = Strecke / Zeit ab Paar 0.
- **Vorhersage:**
  - Die Front erlischt; Reichweite 0, hoechstens 1.
  - Grund: Die Fusion setzt etwa 0,4 Energie frei, grossteils als Atmung und Strahlung. Beim naechsten Paar kommt
    hoechstens ein Stoss von etwa 0,01 bis 0,02 in der Geschwindigkeit an.
  - Bei d_in = 16 verschmelzen `zuend` und `kalt` fast gleichzeitig (etwa 170, Faktor 2), also ohne Front.
  - Bei d_in = 24 verschmilzt in `kalt` nichts, in `zuend` nur Paar 0.
- **Gegenproben:** `kalt` und `paar`. Eine Front zaehlt nur, wenn die Paare der Reihe nach frueher verschmelzen als in
  `kalt`.
- **L3:**
  - Effekt: groesster Zeitgewinn |t_zuend - t_kalt| der Paare 1 bis 4.
  - Aenderung: groesste Abweichung einer Verschmelzungszeit zwischen grob und fein.
  - Ohne Front ist der Effekt etwa 0 und L3 gegenstandslos; das ist dann kein Numerikproblem.

### 4.3 Chromatographie (Chemie 20)

- **Aufbau:**
  - Baelle mit omega^2 = 0,6 / 0,7 / 0,8 starten bei x = -60 mit v = 0,3.
  - Raue Zone |x| < 40 mit Massenpotential V(x) = eps Sum_j a_j exp(-(x - x_j)^2/2) im Abstand 1, weich eingeblendet.
  - eps in {0,01; 0,02; 0,03}, Seeds 1 bis 4, dazu `glatt` (eps = 0); 39 Laeufe, T = 420.
- **Messung:**
  - Durchlaufzeit = Zeit von X = -40 bis X = +40, linear interpoliert; X ist der Ladungsschwerpunkt.
  - Trennung = t(0,6) - t(0,8) je Seed, dazu Ordnung, Reflexionen und Ladungsverlust.
- **Vorhersage (Handrechnung):**
  - **Kopplung:** Der Ball spuert V gemittelt ueber f^2. Die Kopplung relativ zur Masse ist I/E = 0,71 / 0,64 / 0,58.
  - **Mittelung:** Die RMS-Breite des Profils ist etwa 1,5 / 1,7 / 2,1; der Mittelungsfaktor ist 0,56 / 0,51 / 0,43.
  - **Mittlere Verzoegerung** (zweite Ordnung) bei eps = 0,02: etwa 3,7 / 2,7 / 1,9 Prozent. Sie waechst mit eps^2.
  - **Trennung t(0,6) - t(0,8):** etwa +1 / +5 / +11 Zeiteinheiten bei eps = 0,01 / 0,02 / 0,03.
  - **Streuung je Seed:** Der Mittelwert von V ueber die Zone ist je Seed ungleich null (erste Ordnung) und streut die
    Trennung um etwa +-1 / +-2 / +-3.
  - **Ordnung** 0,6 > 0,7 > 0,8: bei eps = 0,03 in mindestens 3 von 4 Seeds; bei 0,01 zufaellig.
  - **Reflexion:** Bei eps = 0,03 kann der Ball mit omega^2 = 0,6 in 1 bis 2 Seeds zurueckprallen (Buckel bis etwa 0,14
    gegen 0,13 Bewegungsenergie); 0,8 kommt durch.
  - **Kurz:** Der grosse Ball wird zurueckgehalten.
  - **Strahlung:** Ladungsverlust unter 1e-3.
- **Gegenprobe:** `glatt` muss fuer alle omega dieselbe Durchlaufzeit 80/0,3 = 266,7 liefern (Spannweite unter 0,1).
  Bestanden, wenn die Spannweite hoechstens ein Fuenftel der groessten mittleren Trennung ist.
- **L3:**
  - Effekt: groesste mittlere Trennung.
  - Aenderung: groesste Aenderung einer Durchlaufzeit zwischen grob und fein.

### 4.4 Neuron (Bio 13)

- **Aufbau:** Ein ruhender Ball (omega^2 = 0,7) bekommt bei t = 0 einen Stoss.
  - `dehnung`: psi_t += -eps x f'(x). Die Ladung bleibt gleich; die zugefuehrte Energie ist eps^2 Int x^2 f'^2.
    eps = +-0,01 ... +-1,0 (16 Werte).
  - `amplitude`: psi = (1 + eps) f bei gleichem omega, also Ladung mal (1 + eps)^2. eps = +-0,03 ... +-0,5 (8 Werte).
  - `null` ohne Stoss als Bezug; 25 Laeufe, T = 300.
- **Messung:**
  - Spitze = max |S_max - S_max(null)|/S_max(0) bis t = 50 (die "Antwortamplitude").
  - Spaete Atmung, abgestrahlte Ladung, omega^2 am Ende aus S_max.
  - Klumpenzahl mit Schwelle S > 0,01.
  - **Sprung** (vorab festgelegt): Zwischen benachbarten |eps| aendert sich Spitze/|eps| um mehr als den Faktor 3, oder
    die Klumpenzahl aendert sich.
- **Vorhersage:**
  - **Kein Sprung.** Kleine Stoesse: Spitze ~ |eps|, Spitze/|eps| auf 20 Prozent konstant fuer |eps| <= 0,1. Darueber
    wird die Antwort unterlinear und glatt.
  - Abgestrahlte Ladung etwa ~ eps^2, bei eps = 1 einige Prozent.
  - **Keine Spaltung, kein Zerfall:** In 1D gibt es kein Q_min; auch ein Ball mit 25 Prozent der Ladung (amplitude -0,5)
    entspannt sich zu einem breiten Ball mit omega^2 etwa 0,98.
  - Ein Sprung waere ein Befund-Kandidat, zuerst gegen die Schwellenwahl zu pruefen.
- **Gegenprobe:** `null` (Spitze 0) und der lineare Bereich bei kleinem eps.
- **L3:**
  - Effekt: groesste Spitze.
  - Aenderung: groesste Abweichung einer Spitze zwischen grob und fein.
  - Zusaetzlich meldet der Bericht, ob die Klumpenzahl gleich bleibt.

### 4.5 Wundheilung (Bio 27)

- **Aufbau:**
  - Baelle mit omega^2 = 0,7 und 0,55, rechts weich beschnitten mit psi = f w, w = (1 - tanh((x - x_c)/0,5))/2.
  - x_c wird so gesucht, dass 10 / 25 / 50 Prozent der Ladung wegfallen (Int f^2 w^2 auf einem Hilfsgitter mit
    dx = 0,001; auf grobem und feinem Gitter derselbe Schnitt).
  - Gegenproben: `null` (ungeschnitten) und `symmetrisch` (je Seite 12,5 Prozent); 10 Laeufe, T = 400.
- **Messung:**
  - Schiefe = drittes standardisiertes Moment der Ladung um den Schwerpunkt (+-8).
  - Formfehler = L2-Abstand von |psi| zum Gleichgewichtsprofil derselben Fensterladung.
  - Heilzeit = ab wann Schiefe bzw. Formfehler dauerhaft unter 10 Prozent des Anfangswerts bleibt.
  - Dazu abgestrahlte Ladung und omega^2 am Ende (aus Q und aus S_max).
- **Vorhersage:**
  - **Heilzeit der Schiefe:** einige zehn Zeiteinheiten (wenige Innenperioden 2 pi/omega = 7,5), mit dem Schaden
    wachsend.
  - **Heilzeit der Form:** oft nicht erreicht, weil eine Atmung bleibt. Der Ball wird schnell symmetrisch, aber nicht
    schnell ruhig.
  - **Abgestrahlte Ladung:** unter 1 Prozent bei 10 Prozent Schnitt, einige Prozent bei 50 Prozent.
  - **Neues omega^2 bei 0,7:** etwa 0,743 / 0,81 / 0,91 fuer 10 / 25 / 50 Prozent, falls kaum Ladung abgestrahlt wird.
  - **Neues omega^2 bei 0,55:** etwa 0,575 / 0,636 / 0,797.
  - Der geheilte Ball ist ein kleinerer Ball, kein reparierter alter.
- **Gegenproben:**
  - `symmetrisch`: Die Schiefe bleibt auf Rundungsniveau, obwohl Atmung und Abstrahlung aehnlich sind wie beim
    einseitigen 25-Prozent-Schnitt.
  - `null`: Formfehler nur auf Gitterniveau (etwa 1e-4).
- **L3:** Fuer jeden einseitigen Schnitt aendern sich abgestrahlte Ladung und Heilzeit der Schiefe von grob zu fein um
  hoechstens ein Fuenftel ihres Werts.

### 4.6 Nervenfaser (Bio 41)

- **Aufbau:**
  - Sechs Baelle mit omega^2 = 0,7 und wechselnder Phase (0, pi, ...), also abstossende Nachbarn. Gleichphasig wuerde die
    Kette zusammenfallen.
  - Abstand d in {9, 12, 15, 40}.
  - `stoss`: Ball 0 laeuft mit v = 0,2 auf die Kette zu.
  - `atem`: Ball 0 bekommt den Dehnungsstoss eps = 0,3.
  - `ruhe`: ungestoert, als Bezug; 12 Laeufe, T = 400.
- **Messung:**
  - Das Signal ist die Differenz zu `ruhe`. Dadurch faellt die langsame Ausdehnung der offenen Kette heraus.
  - `stoss`: Geschwindigkeit des Schwerpunkts; `atem`: |Delta S_max|.
  - Ankunft = erstes Erreichen von 10 Prozent der Amplitude von Ball 0.
  - Tempo je Glied = d / Laufzeit; Daempfung je Glied = Amplitude(k+1) / Amplitude(k).
- **Vorhersage `stoss`:**
  - **Bild:** Die Kette verhaelt sich wie eine Kugelkette mit weicher exponentieller Abstossung, fast eine Toda-Kette.
  - **Uebergabe:** Der Impuls wird auf Abstand uebergeben. Bei v = 0,2 kommen sich zwei Baelle nur bis etwa 9,5 nahe.
  - **Tempo je Glied:** etwa 0,5 / 0,4 / 0,33 / 0,25 fuer d = 9 / 12 / 15 / 40, also stets schneller als v = 0,2.
  - **Daempfung je Glied:** mindestens 0,9 fuer d >= 12 (nahezu verlustfrei).
  - **Achtung, Abweichung vom Auftrag:** Bei d = 40 wird der Stoss trotzdem weitergeleitet, nur ballistisch (Tempo gegen
    v). Die Gegenprobe "grosser Abstand, keine Weiterleitung" gilt nur fuer die Atem-Erregung.
- **Vorhersage `atem`:**
  - Keine Weiterleitung bei allen d: Ball 1 bleibt unter 10 Prozent von Ball 0.
  - Grund: Die Kopplung ueber die Schwaenze ist ~ e^{-kappa d}, also 7e-3 bei d = 9. Die Atmung zerfliesst eher als
    Strahlung.
- **Gegenproben:** `ruhe` (Signal 0) und d = 40 (keine Atem-Weiterleitung).
- **L3:**
  - `stoss`: kuerzeste Laufzeit je Glied gegen die groesste Aenderung einer Ankunftszeit.
  - `atem`: Amplitude von Ball 1 gegen ihre Aenderung.

### 4.7 Zufallskarte Bio 18, Artbildung (nur Schiessen)

- **Aufbau:**
  - Familien 3D m = 0 und 2D m = 0, 1, 2, je omega^2 = 0,51 bis 0,99 in Schritten von 0,01 (196 Zeilen).
  - Radialgleichung f'' = -((d-1)/r) f' + (m^2/r^2) f + (a0 - 2 f^2 + 1,5 f^4) f.
  - Q = 2 omega Int f^2 dV, E = Int (omega^2 f^2 + f'^2 + m^2 f^2/r^2 + U) dV, Simpson.
- **Gueltig** heisst:
  - Klammer gefunden
  - Bahn ohne Nulldurchgang und Umkehr bis 1e-3 f_max
  - Derrick-Virialrest |(d-2) G + d (V - W)|/E < 1e-3
- **Weitere Ausgaben:**
  - Q_min je Familie und Vorzeichenwechsel von dQ/domega (Knick, Vakhitov-Kolokolov)
  - omega^2 mit E = Q
  - Probe dE = omega dQ
  - **Artgrenzen:** Schnitte der Kurven (ln Q, E/Q) zwischen den 2D-Familien. Gleiches (Q, E) heisst Schnittpunkt.
- **Vorhersage:**
  - **3D m = 0:** Q(omega) ist U-foermig, mit Q gegen unendlich an beiden Enden.
    - Duenne Wand: Radius etwa 0,71/(omega^2 - 0,5), also etwa 70 bei 0,51.
    - Dicke Wand: Q etwa 18,9 omega/sqrt(1 - omega^2).
    - **Einziger Knick:** Q_min innen, grob bei omega^2 = 0,8 bis 0,93 und Q_min etwa 40 bis 150. Dort liegt die Spitze
      von E(Q); daneben ist der Ast mit dQ/domega > 0 instabil.
    - E = Q wird bei kleinerem omega^2 als Q_min gekreuzt (E/Q > 1 bei dicker Wand).
  - **2D m = 0:** keine Verzweigung.
    - Q faellt monoton von unendlich (duenne Wand) auf etwa 11,7 bis 11,9 bei 0,99 (Townes-Wert 11,70 plus Korrektur).
    - Begruendung: Pohozaev-Rechnung im NLS-Grenzfall, dQ/da0 = -N_T/2 + P6/4 > 0 mit P6 = Int R_T^6 etwa 60 bis 76.
    - Alle Punkte sind stabil nach Vakhitov-Kolokolov. E/Q liegt nahe 1 fuer omega -> 1; die Abweichung ist ~ a0^2 mit
      offenem Vorzeichen.
  - **2D m = 1, 2:** ebenfalls monoton.
    - Q bei 0,99 nahe den Wirbel-Townes-Werten der kubischen NLS, etwa 48 bzw. 89. Diese Zahlen sind aus dem Gedaechtnis
      und nicht nachgeschlagen.
    - Nahe der duennen Wand (etwa omega^2 < 0,52) werden die Zeilen ungueltig, weil float64 lange Ringplateaus nicht
      traegt.
  - **Artgrenzen:** keine. Bei gleichem Q gilt E_0 < E_1 < E_2 (Drehung kostet Energie).
  - **3D gegen 2D** ist nicht vergleichbar (andere Raumdimension; in 2D ist Q eine Ladung je Laenge).
  - **Numerik:** Virialrest unter 1e-4 bei h = 0,04. Probe dE = omega dQ im Median unter 1e-3, nahe der duennen Wand bis
    etwa 1e-2 (Differenzenfehler).
- **Gegenproben:**
  - Virial- und dE/dQ-Probe
  - Townes-Grenzwert 11,70 fuer 2D m = 0
  - h gegen 2h
- **L3:** relative Aenderung von Q und E zwischen h = 0,04 und 0,08, gegen die kleinste relative Q-Variation einer
  Familie ueber omega.

## 5. Was welches Ergebnis bedeuten wuerde

- **Katalyse, dphi = pi ohne C, mit Verschmelzung:** Symmetriesatz verletzt. Zuerst den Code verdaechtigen:
  - Spiegelprobe bruecke = sperre
  - Rundung
  - Klumpenschwelle
  Danach eine Instabilitaet des ungeraden Zustands pruefen (Befund-Kandidat).
- **Katalyse, bruecke verschmilzt, nur_AC nicht:** echter Dreikoerper-Effekt; C bringt A und B zusammen. Das waere die
  interessanteste Wendung, weil es die Katalyse-Hypothese stuetzt.
- **Kette mit Reichweite >= 2 und gleichmaessigen Abstaenden der Fusionszeiten:** Die Front laeuft, gegen die Vorhersage.
  Dann Frontgeschwindigkeit gegen d_in pruefen.
- **Chromatographie mit Ordnung umgekehrt (0,8 langsamer):**
  - Die Mittelung ueber die Ballbreite ist schwaecher als angenommen, oder die Strahlungsreibung dominiert.
  - Eine vollstaendige Trennung durch Reflexion nur des grossen Balls waere die staerkste Form der Chromatographie.
- **Neuron mit Sprung:** Schwelle im 1D-Q-Ball, zum Beispiel eine Spaltung ab einem bestimmten eps. Befund-Kandidat,
  zuerst die Klumpenschwelle variieren.
- **Wunde, symmetrischer Schnitt mit Schiefe ueber Rundungsniveau:** Symmetriebruch; Codefehler oder Instabilitaet.
- **Nervenfaser, atem wird bei d = 9 oder 12 weitergeleitet:** Die Atem-Mode koppelt resonant ueber die Schwaenze.
  Befund-Kandidat mit Messbezug zu Solitonenketten.
- **Nervenfaser, stoss mit starker Daempfung:** Die Stoesse sind inelastisch (innere Moden, Strahlung); das Toda-Bild
  traegt dann nicht.
- **Artbildung mit innerem Q_min in 2D oder mit Schnitt zweier E(Q)-Kurven:** neue Verzweigung bzw. Artgrenze, gegen die
  Vorhersage. Zuerst Virial, h gegen 2h und die Klassenwahl pruefen.

## 6. Latten (Vorschlag, die Leitung entscheidet)

| Test | L1 kann scheitern | L2 Gegenprobe | L3 Numerik | L4 schon bekannt | L5 Messbezug |
|---|---|---|---|---|---|
| Katalyse | ja (Symmetriesatz; Rolle von C) | ja: ohne, nur_AC, sperre, Spiegelprobe | geplant, Faktor 5 | teilweise: 1D-Q-Ball- und Solitonenstoesse (Battye und Sutcliffe 2000, kubisch-quintische NLS) | nein |
| Kettenreaktion | ja (Front laeuft oder nicht) | ja: kalt, paar | geplant; ohne Effekt gegenstandslos | wahrscheinlich (Mehrsolitonen-Wechselwirkung) | nein |
| Chromatographie | ja (Vorzeichen und Groesse der Trennung) | ja: glatt | geplant | teilweise: Solitonen in Zufallspotentialen | mittelbar (BEC-Solitonen in Unordnung), nicht fuer Q-Baelle |
| Neuron | ja (Sprung oder glatt) | ja: null, linearer Bereich | geplant | wahrscheinlich (innere Moden von Solitonen, Kivshar und Pelinovsky) | nein |
| Wundheilung | ja (Heilzeit, abgestrahlte Ladung, omega am Ende) | ja: null, symmetrisch | geplant | wahrscheinlich (Relaxation gestoerter Solitonen) | nein |
| Nervenfaser | ja (Tempo, Daempfung, Atem-Weiterleitung) | ja: ruhe, d = 40 | geplant | teilweise: Toda-Kette, Solitonen-Newton-Wiege | mittelbar (Solitonenketten in BEC/Optik), nicht fuer Q-Baelle |
| Artbildung | ja (Q_min nur in 3D, keine Artgrenze in 2D) | ja: Virial, dE = omega dQ, Townes-Wert | geplant: h gegen 2h | weitgehend: Q_min, VK-Kriterium, drehende Q-Baelle (Volkov und Woehnert 2002), Wirbelsolitonen der kubisch-quintischen NLS | nein |

Literatur aus dem Gedaechtnis, nicht nachgelesen. Mehrere Vorhersagen (Symmetriesatz, Townes-Grenzwert, Fallzeiten,
Vorzeichen der 2D-Steigung) sind vorab ableitbar; bestaetigt der Lauf sie, ist das eine Code- und Endlichkeitsprobe, kein
neuer Befund.

## 7. Grenzen

- **Ungetestet:** Der Code ist nicht gelaufen, deshalb zuerst der Rauchtest. Seine Zahlen gelten nicht, weil die Laufzeit
  nur 20 betraegt.
- **Nur 1D:** Zeitentwicklung nur in einer Raumdimension, ohne Querbewegung. Die Chemie-Analogien (Katalysator "daneben")
  sind in 1D nur eingeschraenkt abbildbar.
- **Ein Kanal, keine Eichfelder, keine Quantenkorrekturen.** Stabilitaet in der Artbildung nur nach Vakhitov-Kolokolov,
  keine Zeitentwicklung.
- **Festgelegte Schwellen** (Klumpen S > 0,05 bzw. 0,01, Fusion bei Breite < 3, Ankunft 10 Prozent): Sie sind Wahl. Die
  JSON-Dateien enthalten die vollen Zeitreihen-Kennzahlen, damit man nachtraeglich pruefen kann, ob ein Ergebnis an der
  Schwelle haengt.

## Einfach gesagt

Wir testen am Rechner, ob sich Q-Baelle, also kleine stabile Feldklumpen, wie Stoffe in der Chemie und Zellen in der
Biologie verhalten: ob ein dritter Ball zwei andere zum Verschmelzen bringt, ob eine Verschmelzung eine Kettenreaktion
ausloest, ob eine raue Strecke grosse und kleine Baelle trennt, ob ein Ball auf einen Stoss mit "Alles oder nichts"
antwortet wie eine Nervenzelle, wie er nach einer Verletzung wieder rund wird und ob eine Kette von Baellen ein Signal
weitergibt. Dazu kommt die Frage, ob die Ball-"Arten" (rund oder drehend) irgendwo ineinander uebergehen. Unsere Erwartung
ist nuechtern: Vieles verlaeuft glatt und ohne Schwelle, eine Kettenreaktion erlischt, und nur ein Schubs wird entlang der
Kette sauber weitergereicht. Spannend wird es genau dort, wo der Rechner anders antwortet. Gerechnet ist noch nichts; alle
Tests zusammen brauchen etwa zehn Minuten auf einer Grafikkarte.

Ende der Bearbeitung: 2026-09-30 02:12:58 CEST (gemessen mit date). Beginn war 01:25:43 CEST; Budget 90 min eingehalten
(47 min).
