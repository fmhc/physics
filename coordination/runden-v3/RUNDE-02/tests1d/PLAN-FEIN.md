# Runde 2, Folgeauftrag: Test 2F (Absorption feiner) und Test 3K (Verschmelzungskarte)

Bearbeiter: Anthropic-Agent (Opus). Auftrag der Leitung 30.09. 01:41 mit Ergaenzungen 01:48 (Codex-Gegenlesung),
01:51 (Finns Frage nach Reflexion) und 02:01 (Fable-Review). Beginn 2026-09-30 01:41:12 CEST (gemessen), Ende in der
letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ. Physik unveraendert.

## Kurzfassung

- **Code:** tests1d_fein.py neben tests1d.py. Die alte Datei bleibt unveraendert und wird importiert: Profile, Baelle,
  Pakete, Zeitschritt, Daempfung, Anker.
- **2F:**
  - Gitterstufen dx = 0,1 / 2^k (k = 0 bis 3), dt mitskaliert, Auslesen bis t = 1500.
  - Ladung getrennt nach Kern und Aussenbereich; Verzoegerungszeit tau aus Phase und Schwerpunkt; Randrueckstrom.
  - Flussbilanz nach Teilchen- und Antiteilchenkanal; Amplitudenprobe; Groessenprobe bei omega^2 = 0,6 und 0,8.
- **3K:** 32 Stoesse (6 Groessen x 4 Geschwindigkeiten, dazu 8 gegenphasige Kontrollen), grob und fein.
- **Aufrufe:** zehn Aufrufe ueber kleintest.sh, je hoechstens etwa 4 min (obere Schaetzung 6 min), zusammen etwa 18 min.
  Vorrang haben die Kernfrequenzen an der Spitze.
- **Kernvorhersage:**
  - Die Spitze ist eine schmale Resonanz bei nu - omega ~ 1,49, gesehen durch das Frequenzfenster des Pakets.
  - Sie konvergiert auf etwa 1,5e-3 bis 2e-3.
  - Die gemessene "Absorption" ist Zwischenlagerung im Ball, keine bleibende Aufnahme.
  - Bleibende Aufnahme gibt es erst oberhalb nu = 1 + 2 omega = 2,673, ueber den Antiteilchenkanal.

## 0. Berichtigung und Begriffe

- **L3 im ersten Lauf:**
  - Fuer dA_Q bestand L3 in 0 von 12 Frequenzen. Die Zeile "L3 fuer R_Q: 4 von 12" in tests1d_bericht.txt betraf R_Q.
  - Die neue Fassung meldet L3 fuer dA getrennt.
- **Was dA misst:** dA ist der Anteil des Einstroms, der zur Auslesezeit noch in |x| < 30 steckt, nach Abzug des freien
  Durchlaufs. Ob Speicherung, Verzoegerung oder Aufnahme vorliegt, entscheiden erst die spaeten Auslesezeiten und die
  Kernladung.
- **Kontinuumskanten bei omega^2 = 0,7** (omega = 0,8367):
  - 1 - omega = 0,163 und 1 + omega = 1,837. Die FFT-Spitzen 0,170 und 1,834 sind diese Kanten, keine Moden.
  - Bei Omega ~ 1,48 bis 1,49 ist ein Kanal offen und einer geschlossen. Dort ist eine Resonanz moeglich, kein
    gebundener Zustand; im Plan heisst sie "**Resonanzkandidat bei nu - omega ~ 1,48**".
  - Der ruhende Ball zeigt sie bei 1,4935, der gestossene bei 1,481; der alte Stoss erhoehte die Ladung um 2 %.
- **Kanaele:**
  - Unter nu = 1 + 2 omega = 2,673 ist nur der Teilchenkanal offen, und in linearer Ordnung gilt |T|^2 + |R|^2 = 1.
  - Darueber ist auch der Partnerkanal bei 2 omega - nu < -1 offen (Antiteilchen).
  - Die im mitrotierenden System erhaltene Energie E - omega Q ergibt (eigene Rechnung, Hypothese): Teilchen aus
    + |Antiteilchen aus| = Einstrom. Der Ball nimmt dann bleibend die Ladung 2 x |Antiteilchen aus| auf.

## 1. Aufbau

**Test 2F** (Ball omega^2 = 0,70, sonst wie Test 2: Paket eps = 1e-3, sigma = 8, Start bei x = -65, Ebenen x = -30/+30,
Box [-150, 150], Daempfung ab |x| = 110).
- **Gitterstufen k = 0, 1, 2, 3:**
  - dx = 0,1 / 0,05 / 0,025 / 0,0125, dt = 0,05 / 2^k (dt/dx bleibt 0,5)
  - Punkte je Wellenlaenge bei nu = 2,3 (k = 2,071, Wellenlaenge 3,03): **30 / 61 / 121 / 243**
- **Frequenzsaetze:**
  - kern: 1,5 und 1,9 (Kontrollen), 2,25, 2,325, 2,375 (Spitze und Nachbarn), 2,75 und 2,90 (Partnerkanal offen)
  - raster: 2,10 bis 2,60 in 0,025 plus Kontrollen
  - g06 und g08 fuer die Groessenprobe
- **Laeufe je Stufe:**
  - Ball + Paket und Paket allein je nu
  - Ball allein
  - Stoss bei fester Ladung (psi x 1,01, psi_t / 1,01): Resonanzkandidat beim richtigen omega
  - alter Stoss (Anschluss an den ersten Lauf)
  - mit --probe zusaetzlich eps = 5e-4 an allen nu >= 2 und eps = 2e-3 bei nu = 2,325
- **Messung alle 0,1:**
  - Ladungs- und Energiefluss an beiden Ebenen
  - Ladung in |x| < 30 und im Kern |x| < FWHM/2 + 3 (bei 0,7: 4,78)
  - Breite
  - psi an je drei Punkten um jede Ebene
- **Auswertung je nu:**
  - dA_Q(t) und dA_E bei t = 300, 500, 1000, 1500
  - Kern- und Aussenanteil; Speicherverhaeltnis dA(Ende)/dA(500) und Rate
  - Verzoegerung tau_Schwerpunkt: Schwerpunkt des durchgelassenen Flusses gegen das freie Paket
  - Phase phi_T der durchgelassenen Welle und tau_Phase = d phi_T / d nu (nur bei Rasterabstand <= 0,1)
  - Frequenz und Abklingrate der Wiederabstrahlung an beiden Ebenen ab t = 300
  - Randrueckstrom: nach t = 300 nach innen laufender Fluss, ohne und mit Ball
  - Teilchen- und Antiteilchenfluss: Zerlegung von psi(t) an der Ebene per FFT in e^(-i nu t) und e^(+i nu t), Fluss je
    Anteil
- **Auswertung je Stufe:**
  - Resonanzkandidat Omega_2: FFT der Breite ab T/8, 8-fach aufgefuellt, Parabel; bei T = 1500 Stufe 2 pi/1300 ~ 0,005
  - Abklingrate des Resonanzkandidaten; nu_res = omega + Omega_2
  - Gitterverschiebung der Paketfrequenz bei nu_res
  - Spitzenlage und Hoehe (Parabel durch das Maximum und seine Nachbarn), Linienbreite sigma_nu
- **Stufenvergleich:**
  - Folge dA_Q(t = 500) je nu ueber die Stufen, mit q, beobachteter Ordnung, Richardson und Urteil (Abschnitt 4)
  - Mit --vorher werden die JSON frueherer Aufrufe desselben omega eingelesen.

**Test 3K.**
- Aufbau:
  - grosser Ball 0,55 ruhend bei 0
  - kleiner Ball omega^2 in {0,55; 0,60; 0,65; 0,70; 0,80; 0,90} mit v in {0,02; 0,05; 0,1; 0,2}, Lorentz-Boost
  - Start im Mittenabstand Kontaktabstand + 6, freier Kontakt bei t = 6/v
  - Kontaktphase 0 (Phase fuer den freien Kontakt gesetzt); fuer 0,55 und 0,70 zusaetzlich pi
  - T = 600, Messung alle 0,5, grob und fein
- Messung:
  - hoechstes Maximum von |psi|^2 und das hoechste lokale Maximum in mindestens 3 Abstand
  - Tal dazwischen, Ladung links der Mitte, Ladung +-10 um das hoechste Maximum, Box-Ladung und -Energie, Phasen
- **Einordnung** 250 Zeiteinheiten nach dem freien Kontakt (hoechstens T):
  - zwei Baelle, wenn das zweite Maximum >= 0,3 x kleinste Anfangshoehe und das Tal <= 0,5 x zweites Maximum
  - sonst **verschmolzen**
  - bei zwei Baellen aus den Geschwindigkeiten der letzten 40 Zeiteinheiten:
    - **getrennt** (Abprall): der linke laeuft nach links, schneller als 0,25 v
    - **durchgelaufen**: der rechte laeuft nach rechts, schneller als 0,25 v
    - sonst **gebunden**
- Ladungsuebertrag:
  - M = (Q um das hoechste Maximum - Q_gross)/Q_klein
  - bei Trennung 1 - Q_klein(Ende)/Q_klein(Anfang)
- Kontaktzeit und gemessene Kontaktphase werden mit ausgegeben.

## 2. Aufrufe (Leitung, P4000 ueber kleintest.sh)

Im Ordner /home/fmh/fmhc-physics-remote/tests1d-20260930/ liegen tests1d.py und tests1d_fein.py.
- Abkuerzungen: `K` = `bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a`,
  `D` = /home/fmh/fmhc-physics-remote/tests1d-20260930, `P` = D/rauchtest/profil_1d.pt.
- Jede Zeile beginnt mit `cd D &&`.

| Nr | Kurzname | Aufruf (nach `cd D && K`) | Zweck | P4000 erwartet (obere Schaetzung) |
|---|---|---|---|---|
| R1 | t1f-rauch2f | `t1f-rauch2f tests1d_fein.py --test 2f --stufen 0,1,2 --nu kern --T 1500 --probe --rauch --profil P --out D/fein/rauch2f` | Durchlaufprobe 2F | 0,5 min (1) |
| R2 | t1f-rauch3k | `t1f-rauch3k tests1d_fein.py --test 3k --rauch --out D/fein/rauch3k` | Durchlaufprobe 3K; schiesst 0,55 bis 0,90 und speichert profil_3k.pt | 1,7 min (2,5) |
| A | t1f-kern01 | `t1f-kern01 tests1d_fein.py --test 2f --stufen 0,1 --nu kern --T 1500 --probe --profil P --out D/fein/kern01` | Vorrang: Stufen dx0, dx0/2 an der Spitze, spaete Auslesezeiten | 2,7 min (4,5) |
| B | t1f-kern2 | `t1f-kern2 tests1d_fein.py --test 2f --stufen 2 --nu kern --T 1500 --probe --profil P --vorher D/fein/kern01/fein_ergebnis.json --out D/fein/kern2` | Vorrang: dx0/4 an Spitze und Nachbarn, Urteil | 3,8 min (6) |
| G | t1f-3k | `t1f-3k tests1d_fein.py --test 3k --profil D/fein/rauch3k/profil_3k.pt --out D/fein/3k` | Verschmelzungskarte | 1 min (1,5) |
| F | t1f-g08 | `t1f-g08 tests1d_fein.py --test 2f --w2 0.8 --stufen 0,1 --nu g08 --T 500 --profil P --out D/fein/g08` | Groessenprobe 0,8 | 1,2 min (2) |
| E | t1f-g06 | `t1f-g06 tests1d_fein.py --test 2f --w2 0.6 --stufen 0,1 --nu g06 --T 500 --profil D/fein/rauch3k/profil_3k.pt --out D/fein/g06` | Groessenprobe 0,6 | 1 min (1,5) |
| C | t1f-rast01 | `t1f-rast01 tests1d_fein.py --test 2f --stufen 0,1 --nu raster --T 500 --profil P --out D/fein/raster01` | breiter Scan, nur wenn Zeit | 1,2 min (2) |
| D2 | t1f-rast2 | `t1f-rast2 tests1d_fein.py --test 2f --stufen 2 --nu raster --T 500 --profil P --vorher D/fein/raster01/fein_ergebnis.json --out D/fein/raster2` | breiter Scan dx0/4, nur wenn Zeit | 2,1 min (3,5) |
| H | t1f-kern3 | `t1f-kern3 tests1d_fein.py --test 2f --stufen 3 --nu 2.25,2.325,2.375 --T 500 --profil P --vorher D/fein/kern01/fein_ergebnis.json D/fein/kern2/fein_ergebnis.json --out D/fein/kern3` | dx0/8 an Spitze und Nachbarn (vierte Stufe) | 2,2 min (3,5) |

- **Reihenfolge:** R1, R2, A, B, G, F, E; danach C, D2, H, soweit Zeit ist.
- **Abhaengigkeiten:** E braucht profil_3k.pt aus R2 (sonst schiesst E omega^2 = 0,6 selbst, etwa 80 s mehr); B und H
  brauchen die JSON aus A (bzw. A und B).
- **Laufzeitgrundlage:**
  - gemessen auf der P4000 im Lauf 23:34Z: etwa 1,0 ms je Verlet-Schritt bei bis zu 26 x 6001 Punkten; Messung alle 2
    Schritte kostet etwa 0,9 ms je Schritt; 1D-Schiessen 83 s
  - Stufe 2 mit 23 Laeufen x 12001 Punkten wird durch die Speicherbandbreite etwa 1,6 bis 2 ms je Schritt kosten
    (120000 Schritte in B)
- **Hochrechnung aus R1:** Stufenzeiten mal 20. Ergibt ein Aufruf mehr als 9 min, nicht starten; die Leitung
  entscheidet (etwa B mit --T 1000).
- **Speicher:** hoechstens etwa 0,3 GB Tensoren (B: Messreihe 15001 x 23 x 19 Werte, zweimal), Deckel 2,5 GB im Code.

## 3. Vorhersagen (vor dem Rechnen)

**2F, Lage und Form der Spitze**
- **V1:** Die Spitze liegt auf allen Stufen bei nu_res = omega + Omega_2 = 2,330 +- 0,015.
  - Omega_2 aus dem Stoss bei fester Ladung ist 1,49 +- 0,01 und aendert sich zwischen den Stufen um weniger als 0,002.
  - Gitterdispersion verschiebt die Paketfrequenz bei nu_res nur um -0,0022 / -0,0005 / -0,00014 / -0,00003
    (Stufe 0 bis 3; Ortsdispersion plus Verlet).
  - Das ist weit unter dem Raster von 0,025. Laeuft die Spitze trotzdem um 0,025 oder mehr mit dx, ist sie keine Resonanz
    des Balls.
- **V2:** Die Linienform ist das Spektrum des Pakets, keine Eigenschaft des Balls: Gauss mit sigma_nu ~ 0,08 bis 0,10
  (Paket: v_g / (sqrt 2 sigma) = 0,080 bei nu = 2,33; aus dem ersten Lauf 0,094). Also ist die Resonanz schmaler als
  0,08.
- **V3 (Anschluss):** Stufe 0 und 1 geben bei t = 500 genau die Werte des ersten Laufs: 2,53e-3 und 1,60e-3 bei 2,25;
  3,24e-3 und 2,11e-3 bei 2,375. Das prueft die neue Fassung gegen die alte.

**2F, Konvergenz (Leitung: dx0 -> dx0/2 -> dx0/4)**
- **Urteile (vorab, im Code urteil_folge):**
  - Mit A0, A1, A2 fuer dA_Q(t = 500) auf drei Stufen gilt q = |A1 - A2| / |A0 - A1| und Richardson A_inf = A2 + (A2 - A1)/3.
  - **konvergiert:** q <= 0,3 und A_inf >= 0,5 A2. Die Leitung nannte 1/5 als Beispiel, aber reine zweite Ordnung gibt
    q = 1/4, deshalb 0,3.
  - **Artefakt:** A_inf <= 0,2 A2 (schrumpft gegen null), oder die Spitze wandert zwischen zwei Stufen um 0,05 oder mehr.
  - **kein Effekt:** A1 und A2 unter 1e-4.
  - **unklar:** alles andere; dann entscheidet Stufe 3 (Aufruf H).
- **V4:** An der Spitze urteile ich "konvergiert" (Wahrscheinlichkeit etwa 60 %). A_inf liegt bei 1,3e-3 (nu = 2,25),
  etwa 1,9e-3 (2,325) und 1,7e-3 (2,375); Richardson aus dem ersten Lauf.
  - Gegenbild (40 %): q >= 0,5 und schrumpfend, also Artefakt oder unklar.
  - Die Kontrollen 1,5 und 1,9 fallen wie dx^2 (erster Lauf: Faktor 4) und bleiben unter 2e-5.

**2F, Speicher oder Aufnahme (Codex Punkt 2, Finn 3)**
- **Urteile (vorab):**
  - **Verzoegerung:** dA(1500) <= 0,3 dA(500)
  - **Aufnahme:** dA(1500) >= 0,7 dA(500) und die Kernladung >= 0,7 der Ladung in |x| < 30
  - **langsamer Speicher:** alles dazwischen
- **V5:** unter 2,673 langsamer Speicher oder Verzoegerung, keine Aufnahme.
  - Die Ladung sitzt im Kern (Kernanteil >= 0,7).
  - dA(1500)/dA(500) liegt zwischen 0,3 und 1; die Speicherzeit 1/Rate ist mindestens 500. Die Stossprobe zeigte die
    Schwingung bei 1,48 noch nach 500 Zeiteinheiten.
  - Die Wiederabstrahlung an den Ebenen hat die Frequenz nu_res +- 0,01, nicht die Nennfrequenz des Pakets. Das ist der
    Fingerabdruck einer Resonanz.
  - Die Abklingrate der Wiederabstrahlung (Amplitude) passt auf die halbe Speicherrate und auf die Rate des
    Resonanzkandidaten im Stosslauf, je bis Faktor 2.
- **V6 (Verzoegerungszeit):**
  - tau_Schwerpunkt hat bei nu_res ein positives Maximum; off-resonant ist |tau| < 0,5.
  - tau_Phase = d phi_T/d nu zeigt dasselbe Maximum. Wegen der Paketbreite ist es abgeflacht, nicht 2/Gamma.
- **V7 (Amplitudenprobe):** dA(5e-4)/dA(1e-3) = 1 +- 0,1 und dA(2e-3)/dA(1e-3) = 1 +- 0,1, also linear.
  - Nichtlinearitaet gaebe 0,25 bzw. 4.
  - Eine Stoerung durch die Gitter-Voranregung des Balls (die mit dx^2 faellt) gaebe 2 bzw. 0,5.

**2F, Reflexion (Finns Frage)**
- **Numerische Reflexion und Gitterdispersion:** Das pruefen die Stufen (V1, V4). Bei 30 bis 243 Punkten je
  Wellenlaenge ist die Dispersion klein (V1).
- **V8 (Randreflexion):**
  - Die Daempfungsschicht (40 breit, sigma bis 1) schwaecht eine Welle auf dem Hin- und Rueckweg in der Amplitude um
    exp(-(Int sigma dx)/v_g) = exp(-13,3/v_g), bei v_g = 0,9 um 4e-7, im Fluss um 1e-13.
  - Gemessener Randrueckstrom ohne Ball unter 1e-8 des Einstroms, auch bei t bis 1500. Die Box bleibt deshalb bei
    [-150, 150].
- **V9 (Fabry-Perot gegen Resonanz, Groessenprobe):** Beide Bilder vorab ausgerechnet.
  - Das Potential im Ball ist fuer beide Kanaele V(x) = U' + U'' S = 1 - 4 S + 4,5 S^2.
  - **Bild Resonanzkandidat:**
    - nu_res = omega + Omega_2 = 2 omega + sqrt(E_b), E_b Grundzustand im Topf V fuer den geschlossenen Kanal
    - Kastenmodell (Tiefe V_min, Breite FWHM), geeicht an 0,7 (Modell 2,325 gegen gemessen 2,330):
      **nu_res(0,6) ~ 2,21; nu_res(0,8) ~ 2,53**, je +-0,05
    - Das ergibt Omega_2 = 1,44 bzw. 1,63. Die Spitze **steigt** mit omega^2.
  - **Bild Fabry-Perot:**
    - k_innen L = n pi mit k_innen = sqrt(nu^2 - V_min) und L proportional FWHM
    - Geeicht an 0,7: n = 3, L = 1,15 FWHM = 4,10, k_innen = 2,300 bei nu = 2,33.
    - Daraus **nu(0,6) ~ 2,47** (V_min ~ 0,13, L = 3,87) und **nu(0,8) ~ 2,05** (V_min = 0,33, L = 4,79).
    - Die Spitze **faellt** mit omega^2.
    - Ein Fabry-Perot-Resonator mit glatten Waenden gibt ausserdem Transmissionsmaxima, fast ohne Speicherung (V5
      spraeche dagegen).
  - **Vorhersage:** Die Spitze folgt dem Resonanzbild.
    - Bei 0,6 liegt sie unter 2,33, bei 0,8 darueber.
    - Omega_2 aus dem Stoss erfuellt nu_spitze = omega + Omega_2 auf 0,02.
  - Zu beachten:
    - Bei 0,6 oeffnet der Partnerkanal schon bei 1 + 2 omega = 2,549, deshalb reicht g06 nur bis 2,50.
    - Bei 0,8 oeffnet er bei 2,789.

**2F, Kanaele (Fable KF-1)**
- **V10:**
  - Unter 2,673: Antiteilchenfluss aus unter 1e-6 des Einstroms, Teilchen durch + reflektiert = 1 - dA.
  - Bei 2,90 (Paket fast ganz ueber der Schwelle) ist der Antiteilchenfluss > 0, geschaetzt 1e-5 bis 1e-2.
  - Teilchen aus + |Antiteilchen aus| = Einstrom (keine Verstaerkung).
  - Der Ball nimmt bleibend dA ~ 2 x |Antiteilchen aus| auf; dA faellt dort nicht mit der Auslesezeit.
  - 2,75 liegt nur etwa 1 sigma ueber der Schwelle; dort ist die Lage gemischt.
  - Scheitert die Bilanz (Verstaerkung, oder dA nicht ~ 2 x Antiteilchen), ist meine Kanalrechnung falsch.

**3K, Verschmelzungskarte**
- Frequenzabstand zum grossen Ball (omega = 0,7416): 0 / 0,033 / 0,065 / 0,095 / 0,153 / 0,207.
- Papierbild: Verschmelzen braucht Phasengleichheit waehrend der Verschmelzung (Dauer ~ 20 bis 40), also
  Delta omega x 30 < pi/2, Delta omega < ~0,05.
  - Bei kleinem v verschiebt Anziehung und Abstossung im Vorlauf den Kontaktzeitpunkt, die Kontaktphase wird dann zufaellig.
  - Bei grossem v bleibt sie nahe der gesetzten 0.
- **V11:** gleiche Frequenz (0,55), Phase 0: verschmolzen bei v = 0,02 / 0,05 / 0,1; bei 0,2 offen.
- **V12:** Phase pi (0,55 und 0,70): nie verschmolzen. Bei 0,55 getrennt (Abprall) bei allen v, weil die Abstossung
  (~1) weit ueber der Bewegungsenergie (<= 0,07) liegt.
- **V13:** 0,60 verschmilzt bei mindestens zwei der vier v, 0,65 hoechstens bei grossem v, 0,70 hoechstens bei einem v.
  0,80 und 0,90 verschmelzen nie. Der Ladungsuebertrag bleibt dort unter 0,1 von Q_klein, bei v = 0,1 und 0,90 wie im
  ersten Lauf etwa 0,003.
- **V14:** Beim Verschmelzen liegt M zwischen 0,7 und 1; die Box verliert 1 bis 10 % der Ladung.
- Also nicht "kleines v hilft", sondern "kleiner Frequenzabstand hilft". Bei Delta omega > 0 erwarte ich eher Verschmelzen
  bei groesserem v (unsicher).

## 4. Gegenproben

| Test | Gegenprobe | wo |
|---|---|---|
| 2F | Paket ohne Ball (freier Durchlauf, abgezogen), Ball ohne Paket (abgezogen) | jede Stufe |
| 2F | Kontrollfrequenzen 1,5 und 1,9 (Rauschniveau, faellt wie dx^2) | kern, raster |
| 2F | Amplitudenprobe 5e-4 / 1e-3 / 2e-3 | kern mit --probe |
| 2F | Randrueckstrom ohne Ball | jede Stufe |
| 2F | zwei Frequenzen oberhalb 2,673 (anderes Kanalbild) | kern |
| 2F | Groessenprobe 0,6 und 0,8 gegen zwei vorab gerechnete Bilder | F, E |
| 2F | Anschluss an den ersten Lauf (V3) | A |
| 3K | gegenphasig (pi) bei 0,55 und 0,70; grob gegen fein | G |

## 5. Latten (Vorschlag, die Leitung entscheidet)

| Latte | 2F Absorption | 3K Verschmelzung |
|---|---|---|
| L1 kann scheitern | ja: Spitze schrumpft gegen null oder wandert (Artefakt); dA bleibt stehen (Aufnahme statt Speicher); Groessenprobe folgt Fabry-Perot; Kanalbilanz verletzt | ja: V11 bis V13 koennen scheitern (etwa Verschmelzen bei 0,90 oder kein Verschmelzen bei 0,55) |
| L2 Gegenprobe | ja: ohne Ball, Kontrollfrequenzen, Amplitudenprobe, Rand | ja: Phase pi, gleiche Frequenz |
| L3 Numerik | ist der Test selbst: drei bis vier Stufen, Urteil nach Abschnitt 3 | grob gegen fein: gleiche Klasse, M-Latte |
| L4 schon bekannt | teilweise: Fano- und Feshbach-Resonanzen an Solitonen, eingebettete Moden (Literatur aus dem Gedaechtnis, nicht nachgelesen) | weitgehend: phasenabhaengige Q-Ball-Stoesse (Battye/Sutcliffe 2000; Axenides u. a. 2000) |
| L5 Messbezug | nein (Analogie: Streuung an optischen Solitonen im Prinzip messbar) | nein |

## 6. Grenzen

- **Ungetestet:** zuerst R1 und R2. Wahrscheinlichste Fehlerstellen:
  - Spaltenzuordnung der Ebenenwerte, FFT-Masken der Kanalzerlegung
  - JSON-Einlesen mit --vorher (nur Stufen desselben omega^2 werden uebernommen)
- **Paketbreite:** Das Paket ist 0,08 breit in nu. Eine Resonanz schmaler als das bleibt eine Faltung; ihre Breite
  liefert nur die Abklingrate.
- **Spaete Auslesezeit:** dA(1500) enthaelt bei kleinem nu noch langsame Paketanteile. Der Abzug des freien Pakets
  entfernt sie in erster Ordnung.
- **Kanalzerlegung:** per FFT ueber die ganze Zeitreihe. Kreuzterme mitteln nur weg, wenn beide Anteile lange genug
  laufen; der Bilanzrest wird gemeldet.
- **3K:**
  - Die Einordnung haengt an Schwellen (0,3 Hoehe, 0,5 Tal, 0,25 v). Bei v = 0,02 bleiben nach 250 Zeiteinheiten nur
    etwa 5 Laengeneinheiten Abstand, die Unterscheidung von "gebunden" ist dort knapp.
  - Kontaktphasen bei ungleicher Frequenz sind nur Sollwerte; die gemessene steht daneben.
- **Kastenmodell der Groessenprobe:** nur eine Schaetzung (+-0,05). Entscheidend ist die Richtung, nicht der Wert.

## Einfach gesagt

Im ersten Lauf schien der Q-Ball Wellen einer bestimmten Frequenz zu schlucken, aber bei feinerem Rechengitter wurde der
Effekt um ein Drittel kleiner. Jetzt rechnen wir auf noch feineren Gittern, schauen viel laenger hin und pruefen, ob die
geschluckte Ladung im Ball bleibt oder spaeter wieder herauskommt, ob sie vom Rand der Rechenbox zurueckkommt und ob die
Frequenz mit der Ballgroesse wandert. Meine Erwartung: Der Ball haelt die Welle eine Weile fest wie eine Glocke, die
nachklingt, und gibt sie dann wieder ab; wirklich behalten kann er Ladung erst bei noch hoeheren Frequenzen, wenn er
dabei eine "Anti-Welle" aussendet. Beim Verschmelzen erwarte ich, dass vor allem gleich tickende Baelle zusammengehen und
nicht die langsamen. Gerechnet ist noch nichts; die Laeufe brauchen zusammen etwa eine Viertelstunde Grafikkarte.

Ende der Bearbeitung: 2026-09-30 02:06:35 CEST (gemessen mit date).
