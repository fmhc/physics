# BILDUNG-LEITER (Runde 22): Ergebnis

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary (Finn: "ok mach den naechsten test").
  - Beginn 2026-10-02 20:22:32 CEST (date).
  - Plan eingefroren 20:41:46 CEST (PLAN.md.eingefroren-20261002-204146), nach dem Rauchlauf und vor jedem echten Lauf.
- Laeufe: .69, 18:42:23 bis 19:15:27 UTC (= 20:42:23 bis 21:15:27 CEST), 22 Hauptlaeufe in 30 Aufrufen, alle rc = 0.
  Dazu ein nachtraeglicher Gegencheck 19:15:41 bis 19:16:02 UTC (nicht gewertet).
- Ergebnis: Entwurf ab 20:54:14 CEST, Fassung ab 21:05:17 CEST (beides date); Ende in der letzten Zeile.
- Explorativ (v3), Deutungen [H, im Modell M1, 2D, l = 0].
- **Ablage:**
  - Code in code/, Plan und Hilfsdateien hier.
  - Ausgaben (JSON, Logs) in lauf-69/.
  - Die Rohsignale und Zustaende (40 .pt-Dateien, zusammen mit den Ausgaben 57 MB) liegen nur auf der .69 in
    /home/fmh/fmhc-physics-remote/runde22-bildung-leiter/aus/.

## 1. Ergebnis zuerst

1. **L1 eingetroffen: Die Zeitentwicklung misst dasselbe V wie die Frequenzrechnung aus Runde 12.**
   - Neben der Sprosse ist gamma = 1,583e-4 bei 0,52905 (Runde 12: 1,5e-4, Verhaeltnis 1,06). Bei 0,52950 ist
     gamma = 1,689e-4 (Runde 12: 1,7e-4, Verhaeltnis 0,99).
   - An der Sprosse 0,529266 ist \|Im rho\| = 1,4e-8, also auf Rauschhoehe. Die Schranke war 1e-5.
   - Die Frequenz stimmt auf ~1e-5: Re rho 1,556449 gegen rho* 1,556457.
2. **L2 eingetroffen: Zwischen den Sprossen (0,53139) klingt die Mode mit gamma = 7,05e-3 ab** (Schranke 3e-3). Die
   Lebensdauer ist ~140, gegen ~6000 bei 2,2e-4 neben der Sprosse.
   - Die quadratische Hochrechnung der Denknotiz (1,5e-2) ueberschaetzt das um den Faktor 2.
3. **L3 eingetroffen: Im glatten Gauss-Klumpen beherrschen gebundene Moden die Zentraldichte** (Anteil 0,57 bis 0,73).
   - An keinem Punkt liegt eine Pencil-Komponente im Band der stillen Mode (Anteil 0).
   - Der nachtraegliche, nicht gewertete Gegencheck bestaetigt das: Der Stillanteil liegt in jedem Mass unter 0,1 %.
   - **Vorbehalt:** Der Anteil "gebunden" haengt am Verfahren. Mit dem Pencil K = 24/40 sind es an drei Punkten nur
     ~0,33, im Periodogramm 0,90 bis 0,94 (Abschn. 4).
   - Fuehrend ist eine gebundene Atmung bei rho ~ 0,137 bis 0,149 (Fenster [100; 600]).
   - [H] Vermutlich ist es dieselbe Mode wie die gebundene Mode des linearisierten Arms (0,135 bis 0,145). Diese
     strahlt nicht ab (\|Im\| <= 6e-7).
4. **L0 eingetroffen (K0 bestanden):** Die exakte Familienloesung bleibt bis T = 2000 auf relativ 6,5e-13 bis 9,1e-13
   stationaer (Schranke 1e-6). Voraussetzung war die Startkorrektur V2-1: Mit dem Taylor-Start der Leitungsfassung
   waren es schon bis T = 20 relativ 2,2e-5 (dr 0,04) bzw. 5,5e-6 (dr 0,02).
5. **Bedeutung nach Karte (alle drei Zeilen gelten):**
   - L1: Die Zeitentwicklung bestaetigt die V-foermige Breite unabhaengig von der Frequenzrechnung (Gegenprobe L2 der
     Leiter in 2D).
   - L2: Zwischen den Sprossen klingt die Mode schnell ab (H1); die Naehe zur Sprosse bestimmt die Lebensdauer.
   - L3: Glatte Klumpen regen die stille Mode kaum an. Ihr langes Nachschwingen ist gebundene Wand-Atmung (H3), keine
     Spur der Leiter.

## 2. K0, Rauchlauf und Gittervergleich

**K0 (Reihe "exakt", S_zentrum_rel_abw_max bis T = 2000):**

| omega^2 | dr 0,02 (gewertet) | dr 0,04 |
|---|---|---|
| 0,52905 | 9,1e-13 | 4,0e-13 |
| 0,529266 | 6,5e-13 | 4,6e-13 |
| 0,52950 | 7,5e-13 | 3,4e-13 |
| 0,53139 | 8,0e-13 | 3,7e-13 |

- Die Ladung der exakten Reihe bleibt bis T = 2000 auf ~1e-13 relativ erhalten (z. B. 682,422195002743 auf
  682,422195002691).
- Newton auf dem diskreten Profil: 30 Schritte, Residuum bis auf den Rundungsboden 8,8e-13 bis 1,0e-12 (dr 0,02).
  Die Schranke 1e-13 im Code ist dort nicht erreichbar; das ist unschaedlich.

**Rauchlauf** (vor dem Einfrieren, 18:36:00 bis 18:40:09 UTC, lauf-69/rauch/):
- Leitungsfassung: lin rc 0 (8,7 s); nl **rc 1** (RuntimeError: max() auf leerem Fenster, Fehler V2-3).
- v2 gegen Taylor-Start (A/B, T = 20): K0-Mass 1,4e-13 gegen 2,2e-5 (dr 0,04) und 5,0e-13 gegen 5,5e-6 (dr 0,02).
  Vorab gerechnet waren 1,7e-5 und 4,2e-6.
- Abschnitte (bis=10, weiter) bitgleich zum Einmal-Lauf.
- Zeit je Schritt 1,32 ms (dr 0,04) bzw. 1,81 ms (dr 0,02). Fuer dr 0,02 waere ein Aufruf mit T = 2000 ~550 s
  geworden; deshalb zwei Abschnitte.
- Pencil-Probe (synthetisch, 10 Komponenten plus Drift): gamma 1e-6, 1,5e-4, 3e-3 und 1e-2 auf rel. < 1e-3 getroffen.

**Gittervergleich (Latte L3, Numerik), gamma der Bandwahl:**

| omega^2 | dr 0,02 | dr 0,04 | Verhaeltnis 0,04/0,02 |
|---|---|---|---|
| 0,52905 | 1,583e-4 | 1,643e-4 | 1,04 |
| 0,529266 | -1,4e-8 | 1,2e-7 | (beide Rauschhoehe bzw. < 1e-6) |
| 0,52950 | 1,689e-4 | 1,628e-4 | 0,96 |
| 0,53139 | 7,05e-3 (Partner +Re) | 7,48e-3 (Partner -Re) | 1,06; mit gleichem Partner 7,485e-3 gegen 7,481e-3, also 1,00 |

- Re rho verschiebt sich zwischen den Gittern um ~8e-6 (0,52905: 1,555179 gegen 1,555171).
- Arm G ist praktisch gitterunabhaengig: Anteil gebunden 0,710 / 0,624 / 0,571 / 0,731 bei dr 0,04 gegen 0,711 /
  0,624 / 0,570 / 0,731 bei dr 0,02, still ueberall 0.
- **Latte L3 bestanden:** Die Raten aendern sich zwischen den Gittern um hoechstens 4 %, die V-Lage um ~4e-6.

## 3. Arm M (linearisiert, Reihe "kick", Projektion, Pencil K = 12; gewertet dr 0,02)

| omega^2 | Fenster | gamma = -Im rho (Bandwahl) | Re rho | Partner -Re: gamma | K = 24 | Runde 12 \|Im rho\| | Verhaeltnis |
|---|---|---|---|---|---|---|---|
| 0,52905 | [200; 2000] | 1,583e-4 | +1,555179 | 1,577e-4 | 1,578e-4 | 1,5e-4 (2c) | 1,06 |
| 0,529266 | [200; 2000] | -1,4e-8 (Im > 0, Rauschhoehe) | -1,556449 | -1,6e-6 | +1,7e-8 | 2,6e-7 bei 0,529275; an der Sprosse 0 | - |
| 0,52950 | [200; 2000] | 1,689e-4 | +1,557802 | 1,706e-4 | 1,706e-4 | 1,7e-4 (2c); 1,743e-4 (2a) | 0,99 |
| 0,53139 | [50; 400] | 7,05e-3 | +1,558637 | 7,48e-3 | 7,50e-3 | - (Hochrechnung 1,5e-2) | - |

- **Bandwahl:** Je Punkt gibt es zwei Partner (+Re und -Re, also u- und v-Anteil). Die Regel "|Re| am naechsten an 1,556"
  waehlte dreimal den schwaecheren Partner. Beide Partner geben dieselbe Aussage; an der Sprosse liegen beide unter 1e-5
  (1,4e-8 und 1,6e-6, beide mit Im > 0).
- **Zeitliche Konstanz** (Projektion, Fenster [50; 400] / [400; 1200] / [1200; 2000]):
  - 0,52905: 1,50e-4 / 1,577e-4 / 1,578e-4
  - 0,52950: 1,80e-4 / 1,705e-4 / 1,705e-4
  - 0,53139: 7,05e-3 / 7,49e-3 / Mode ab 1200 unter den anderen Komponenten
  - Sprosse: 2,6e-6 / 3,3e-7 / 3,7e-9
  - Zentrum und Wand geben dieselben Raten (z. B. 0,52905, [1200; 2000]: 1,578e-4 / 1,578e-4).
- **Re rho gegen Runde 12:** 1,555179 (R12 interpoliert 1,55519), 1,557802 (1,557811), 1,556449 (rho* 1,556457). Das
  sind ~1e-5 tiefer, ein Gitter- bzw. Verfahrensunterschied.
- **Weitere Komponenten der Projektion:**
  - Drift der Phasenmode bei +-1e-5 mit Amplitude ~80. Das ist der lineare Anstieg des Jordan-Blocks, erwartet.
  - Gebundene Mode bei +-0,135 bis +-0,145 mit \|Im\| <= 6e-7 in [200; 2000], also ohne Abstrahlung, wie fuer
    rho < 1 - omega = 0,272 erwartet.
  - Schwellenreste bei +-0,27 bis +-0,29.
- **Zwei-Punkt-Lage des V bei dr 0,02** (aus 0,52905 und 0,52950): w* = 0,5292713, Steigung 56,8. Runde 12: 0,529266
  und 57.

**Scan um die Sprosse (dr 0,04, nur berichtet):**

| omega^2 | gamma (Bandwahl) | gamma Partner | Re rho | V-Formel 56,6^2 (w2 - w*)^2, w* = 0,5292742 |
|---|---|---|---|---|
| 0,52905 (Haupt) | 1,643e-4 | 1,638e-4 | 1,555171 | 1,61e-4 |
| 0,52915 | 4,85e-5 | 4,94e-5 | 1,555757 | 4,94e-5 |
| 0,52920 | 1,73e-5 | 1,59e-5 | 1,556052 | 1,77e-5 |
| 0,52925 | 1,65e-6 | 2,3e-8 | 1,556347 | 1,9e-6 |
| 0,529266 (Haupt) | 1,2e-7 | -1,6e-6 | 1,556441 | 2,2e-7 |
| 0,52930 | 2,37e-6 | 6,1e-7 | 1,556641 | 2,1e-6 |
| 0,52935 | 1,75e-5 | 1,92e-5 | 1,556934 | 1,84e-5 |
| 0,52940 | 5,03e-5 | 5,20e-5 | 1,557224 | 5,07e-5 |
| 0,52950 (Haupt) | 1,628e-4 | 1,644e-4 | 1,557794 | 1,63e-4 |

- **Ausgleich der signierten Wurzeln** (8 Punkte ohne das Minimum, Regel im Plan):
  - Nulldurchgang w* = 0,5292742, Steigung 56,6, Kruemmung 3204.
  - Runde 12: 0,529266, 57 und 57^2 = 3249.
  - Groesster Rest 1,3e-4 in sqrt(gamma).
- **Lage im Vergleich:**
  - Zwei-Punkt-Formel (0,52905 und 0,52950): 0,5292713 bei dr 0,02 und 0,5292755 bei dr 0,04. Zwischen den Gittern
    wandert w* also um ~4e-6.
  - Der Abstand zu Runde 12 (0,529266) betraegt 5e-6 bis 1e-5 (V-Ausgleich bei dr 0,04: 8e-6).
- **Aufloesung:**
  - Am Boden des V (0,52925 bis 0,52930) weichen die beiden Partner um bis zu 1,8e-6 voneinander ab. Das ist die
    Rauschhoehe dieser Zeitbereichsmessung.
  - Daraus folgt in omega^2 nur \|w2 - w*\| < sqrt(1,8e-6)/57 ~ 2e-5. Die Lagen 0,529271 bis 0,529275 sind also mit
    0,529266 vertraeglich.

## 4. Arm G (nichtlinear, Gauss-Klumpen Typ (i): Q = Q_F, s = R_rms, psi_t = -i omega psi; gewertet dr 0,02)

| omega^2 | Q_F | R_rms / r_halb | Fenster [100; 600]: gebunden | still | fuehrende Komponenten \|re\| (gamma, Amplitude) | Nachweisgrenze je Komponente |
|---|---|---|---|---|---|---|
| 0,52905 | 682,4 | 8,71 / 11,99 | 0,711 | 0 | 0,1369 (1,6e-3; 0,150), 0,2848 (4,7e-3; 0,087), 0,3171 (1,2e-2; 0,045), 0,2075 (1,9e-2; 0,043), 0,4583 (7,7e-3; 0,019) | 0,54 % |
| 0,529266 | 672,6 | 8,64 / 11,90 | 0,624 | 0 | 0,1378 (1,6e-3; 0,156), 0,2866 (6,4e-3; 0,113), 0,3702 (1,8e-2; 0,045), 0,2455 (9,5e-3; 0,026), 0,4882 (8,6e-3; 0,014) | 0,26 % |
| 0,52950 | 662,2 | 8,58 / 11,80 | 0,570 | 0 | 0,1385 (1,4e-3; 0,162), 0,2866 (7,2e-3; 0,124), 0,4033 (1,8e-2; 0,065), 0,5258 (1,2e-2; 0,029), 0,2651 (5,1e-3; 0,028) | 0,84 % |
| 0,53139 | 586,5 | 8,08 / 11,08 | 0,731 | 0 | 0,1494 (-2,9e-4; 0,097), 0,1404 (4,4e-3; 0,091), 0,2760 (7,6e-3; 0,073), 0,2990 (9,7e-4; 0,030), 0,4287 (3,4e-3; 0,015) | 0,46 % |

- Schwelle 1 - omega: 0,2726 / 0,2725 / 0,2723 / 0,2710.
- Die Komponente bei 0,276 bis 0,287 liegt knapp ueber der Schwelle und zaehlt deshalb nicht als gebunden.
- **Spaetere Fenster** (berichtet): Anteil gebunden 0,90 bis 0,98, still 0. Einzige Ausnahme ist 0,53139 in
  [1300; 2000] mit still 1,7e-4 (Paar +-1,5547, gamma 2,1e-4).
  - Das passt nicht zur Rate des linearisierten Arms an diesem Punkt (7,5e-3).
  - Lesart [H]: Der Klumpen hat sich auf ein anderes Familienmitglied gesetzt.
- **Klumpen:** Die Zentraldichte schwingt stark. Spanne in [100; 600] 0,78 bis 1,02, in [1300; 2000] an allen vier Punkten noch ~0,29.
  - Mittel 0,99 in [100; 600] und 1,02 spaeter, gegen S0 = 1,028 des Familienballs.
  - Bis T = 2000 bleiben 89 bis 94 % der Ladung innerhalb r < 80: 641,7 von 682,4; 629,4 von 672,6; 616,1 von 662,2;
    523,9 von 586,5.

**Nachtrag (nach Kenntnis der gewerteten Ergebnisse, NICHT gewertet; hilfs/still_nachtrag.py, .69 cpu,
19:15:41 bis 19:16:02 UTC, rc 0; lauf-69/still-nachtrag.json):** Dasselbe Fenster [100; 600], Reihe gauss.

| omega^2 (dr 0,02) | still K = 12 / 24 / 40 | Periodogramm: Band 1,45 bis 1,65 | gebunden K = 12 / 24 / 40 | Periodogramm: gebunden |
|---|---|---|---|---|
| 0,52905 | 0 / 0 / 0 | 5,2e-5 | 0,71 / 0,33 / 0,33 | 0,905 |
| 0,529266 | 0 / 0 / 1,9e-5 | 2,6e-4 | 0,62 / 0,33 / 0,33 | 0,924 |
| 0,52950 | 0 / 0 / 3,5e-5 | 2,8e-4 | 0,57 / 0,34 / 0,33 | 0,941 |
| 0,53139 | 0 / 0 / 9,0e-4 | 6,2e-5 | 0,73 / 0,88 / 0,90 | 0,943 |

- dr 0,04 gibt dieselben Zahlen auf 2 bis 3 Stellen.
- **Stillanteil:** In jedem Mass unter 0,1 %; im Periodogramm 0,005 bis 0,03 %. Der Vorbehalt zur Nachweisgrenze ist
  damit ausgeraeumt.
- **Anteil gebunden: neuer Vorbehalt.**
  - Mit K = 24 oder 40 faellt der Pencil-Anteil an drei Punkten auf ~0,33. Nach der K = 24/40-Lesart waere "beherrscht"
    dort nicht erfuellt.
  - Das nichtparametrische Periodogramm gibt dagegen 0,90 bis 0,94.
  - Lesart [H, nicht geprueft]: Mit mehr Komponenten zerlegt der Pencil den Schwellenbereich um 0,27 bis 0,29 in
    nahe beieinanderliegende Paare mit grossen, sich teilweise aufhebenden Amplituden. Amplitude^2 ist dann kein
    Leistungsanteil mehr.
  - Die gewertete Aussage (K = 12) steht, aber das Mass "gebunden" ist verfahrensabhaengig. Die Komponenten des
    K = 24-Pencils sind nicht gespeichert, die Lesart ist deshalb offen.

## 5. Vorhersagen gegen Ausgang

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang | Zahlen (dr 0,02) |
|---|---|---|---|---|
| L0 | K0 bestanden | 85 % | **eingetroffen** | 6,5e-13 bis 9,1e-13 < 1e-6, alle vier Punkte |
| L1 | Arm M trifft \|Im rho\| aus R12 daneben innerhalb Faktor 2; an der Sprosse < 1e-5 | 60 % | **eingetroffen** | 1,06 und 0,99; Sprosse 1,4e-8 |
| L2 | Arm M bei 0,5310 (Plan: 0,53139): Rate >= 3e-3 (H1 statt H2) | 55 % | **eingetroffen** | 7,05e-3 |
| L3 | Arm G: gebundene Moden beherrschen, Stillanteil < 1 % | 70 % | **eingetroffen** (Vorbehalt: Anteil "gebunden" verfahrensabhaengig, Abschn. 4) | gebunden 0,57 bis 0,73; still 0 an allen vier Punkten |

- Alle vier Vorhersagen trafen ein, bei Wahrscheinlichkeiten von 55 bis 85 %. Jede hatte vorab einen moeglichen
  Fehlausgang: L1 ueber den Faktor 2 bzw. die Schranke 1e-5, L2 ueber 3e-3, L3 ueber 50 % und 1 %, L0 ueber 1e-6.
- Gegen Runde 12 ist Arm M eine weitgehend unabhaengige Gegenprobe (Latte L2). Das Verfahren ist ein anderes:
  Zeitentwicklung auf dem Differenzengitter statt Polsuche im Frequenzraum. Das Ergebnis ist dasselbe V.
  - Gemeinsam bleiben Modell und Startprofil: Das ODE-Profil aus dem Runde-12-Modul wird hier per Newton auf das Gitter
    gebracht.

## 6. Code, Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Code-Aenderungen gegen die Leitungsfassung.** Gerechnet wurde mit code/zeit2d_v2.py, Diff code/zeit2d_v2.diff,
alle Stellen mit "V2" markiert. Die Leitungsfassung code/zeit2d.py ist unveraendert.
- **V2-1 Start (Fehler):** Faktor q = sqrt(1 - w2 dt^2/4) vor dem Geschwindigkeitsterm des Starts. Damit ist die
  diskrete Loesung exakt f exp(-i w_d t). Ohne ihn verletzt K0 schon bis T = 20 die Schranke (A/B im Rauchlauf).
- **V2-2 Drehfrequenz w_d = (2/dt) asin(w dt/2)** in Hintergrundphase und Messdrehung des lin-Arms. Er ist dann exakt
  die Linearisierung des diskreten nl-Schemas. Re rho verschiebt sich dadurch um 1e-6 (dr 0,02) bzw. 4e-6 (dr 0,04).
- **V2-3 (Fehler):** kein Absturz bei leeren Fenstern im nl-Arm (Leitungsfassung im Rauchlauf rc 1).
- **V2-4:** nicht endliche Zahlen im JSON als Text.
- **V2-5, nur Ausgaben:** Laufzeiten, Bandwahl, Pencil K = 24, Rohsignale (.roh.pt), Rauchlauf-Option start-taylor.
- **V2-6 Abschnitte** bis=/weiter, gegen den Einmal-Lauf bitgleich geprueft.
- **Nicht geaendert, nur benannt:** Arm M startet mit dem Gauss-Kick an r_halb statt mit dem Pol-Eigenvektor
  (Kartenwortlaut). Die Mode ist im Pencil trotzdem eindeutig getrennt: beide Partner, alle Fenster, Projektion,
  Zentrum und Wand stimmen ueberein.

**Grenzen:**
- Gewertet ist ein Gitter (dr 0,02, zweite Ordnung im Raum, Leapfrog). Der Vergleich mit dr 0,04 ist in Abschn. 2.
- An der Sprosse ist gamma nur nach oben begrenzt: Rauschhoehe 1e-8 bis 2e-6, je nach Partner und Fenster. Im > 0
  heisst hier nicht Wachstum.
- Der Punkt zwischen den Sprossen ist 0,53139 statt "etwa 0,5310" der Karte; so im Plan aus der Leiter festgelegt.
- **Stillanteil:**
  - Er ist ein Amplitude^2-Anteil im 12-Komponenten-Pencil der Zentraldichte, keine Energie. Nachweisgrenze 0,3 bis
    0,8 % je Komponente.
  - Die Zentraldichte sieht die stille Mode aber: Im lin-Arm traegt das Zentrumssignal sie mit aehnlicher Amplitude
    wie das Wandsignal.
- Der Gauss-Klumpen sitzt nicht genau auf dem Familienpunkt; er verliert 6 bis 11 % der Ladung. Die Schwelle
  1 - omega bezieht sich auf die Familienfrequenz.
- Die Rauchlaeufe gingen ueber die Vorgabe hinaus: dr 0,02 fuer die Zeitmessung, A/B-Start, Abschnitte, Pencil-Probe.
  Alles lief vor dem Einfrieren und ist in Plan Abschn. 2 dokumentiert.

**Selbstanzeigen:**
1. **Abschnitts-Rauchlauf lin:** Wegen meiner Shell-Klammerung lief er im falschen Arbeitsverzeichnis (rc 2, keine
   Rechnung). Als seg1b/seg2b wiederholt.
2. **Kettenstart:** Der ssh-Aufruf blieb wegen derselben Art Klammerung am Ausgabekanal haengen. Die Ketten liefen
   korrekt mit nohup weiter.
3. **Lock-Probe:** Zu Beginn habe ich die Spur-Locks mit `flock -n ... true` geprueft und freie Locks dabei kurz
   gehalten. Die Dateien bestanden schon; angelegt wurde nichts.
4. **Aufraeumen:** Auf der .69 habe ich im eigenen Ordner `rm -rf __pycache__` ausgefuehrt (Nebenprodukt von
   py_compile). Lokal kein rm.
5. **Wartebefehl:** Ein Hintergrund-Wartebefehl endete zu frueh, Ursache unklar. Es hatte keine Folgen; danach habe
   ich im Vordergrund gewartet.
6. **Fremde Laeufe:** Laeufe anderer Agenten (ursuppe.py, winkelfeld.py) schoben sich auf cpu3 und cpu4 zwischen meine
   Aufrufe und verursachten Wartezeit. Ich habe nichts beendet.
7. **Nachtrag:** hilfs/still_nachtrag.py (Abschn. 4) ist erst nach Kenntnis der gewerteten Ergebnisse entstanden und
   wird nicht gewertet.
8. **V2-6:** entstand nach dem ersten Rauchlauf wegen der Laufzeit, vor dem Einfrieren.

**Laufzeiten** (.69, CPU, 1 Thread, alle Aufrufe < 600 s):
- dr 0,02 lin: Abschnitt a 235 bis 250 s, b ~300 s (davon Analyse 72 s); Schleife zusammen 438 bis 440 s.
- dr 0,02 nl: a ~240 s, b ~247 s (davon Analyse 8 s); Schleife 457 bis 459 s.
- dr 0,04 lin (auch Scan): 243 bis 247 s (Schleife ~158 s, Analyse ~82 s).
- dr 0,04 nl: 178 bis 182 s (Schleife ~165 s, Analyse 9 s).
- Nachtrag: 20 s.

**sha256:**

- Code (lokal = .69, geprueft):
  - code/zeit2d.py: e0010635041833379cbcdfa72c184187c9d882174d1bd7eadc6af39fea97fce5
  - code/zeit2d_v2.py: dbd1652ecf5f0c139376c9fb3368dfd6a1a5fe912b9dbdb83f8656665b58731e
  - code/bic2_2d_praez_v2.py: 042ba893129ac3971dc53bf2c42b313f95f35e0f420149b274b7fd6a5be4ef00
  - code/zeit2d_v2.diff: fb9a145387a6fc1879d2af3f8e1ae715025fa9b1f9b336376727b6d004d13629
- Plan:
  - PLAN.md.eingefroren-20261002-204146: 698229373e3bc0cee80ecaa8f78c75b0b949941fc6e571da8f641acb983c6dd1
- Hilfsdateien:
  - hilfs/pencil_probe.py: 487ea87abf761ce0eeef132862cf76990ba6a6c3b3bec1cd3bebbb2d28fd5da3
  - hilfs/kette.sh: 81b1cd0276e1cf0aa901bc6388fa024b0041e827f5ad30d220aed115b06b7169
  - hilfs/still_nachtrag.py: 9866e05215c3821549eb805729023c3f11e1ab0768f3b606ee9d5bc26a9607cc
  - hilfs/arm_m.jq: c1fa3c1f60a99a267df15f8ccf9dc600ede2c7f9111a33a1a85c2db41e1b2173
  - hilfs/arm_g.jq: 69e545c8a98e55922110cb89e74252a65b662ad9b542f7f0bacb408dc070ff60
  - hilfs/wertung.jq: 3b2c89bd27bf6ea8e9734d60a6706a531e3c183a1f8f8927511d2f9189d4e2c0
  - hilfs/wertung-ausgabe.json: c115b5009c5548f3aacdcd6102bf8a2b4a1d2f84226f90e01ff96c725987b11b (Ausgabe von wertung.jq ueber alle Haupt- und Scan-Dateien)
- Ausgaben (lauf-69/, Kopien der .69-Dateien ohne .pt):
  - lauf-69/lin-02-0.52905.json: ceb62d7b6fdd7c8033802767174c92ed3a069b79df22b95f1daba25548e51d95
  - lauf-69/lin-02-0.529266.json: 67e8893c00f02baddff8d09f5215290b26eb1e7f44895cf48d757b2f0b897283
  - lauf-69/lin-02-0.52950.json: 44558c8893e450d137b495c2526e67e382b41183b1632cca45f34002bbd98e62
  - lauf-69/lin-02-0.53139.json: e76a7641436318d5e2c0d840d37f2d92e5088a66891fb8b71c1f51335a2a1d8d
  - lauf-69/lin-04-0.52905.json: 026c478fbda555319ec59f213fbb465de868a718d25e5fad15c9034b1dc75f0d
  - lauf-69/lin-04-0.529266.json: 66041a656861cb40e2ba1dc1f834c487fdaffa634f58b8b1d615ac6ab1f61bb5
  - lauf-69/lin-04-0.52950.json: fc64d7264b52ed6fa22cc3d50f10ed0b132a1b96f981f67cc0dfa46a391b66fd
  - lauf-69/lin-04-0.53139.json: 0e4e81e0d724662c4fa59da1bb817cda97055af5ce9745e12ac980440a416386
  - lauf-69/nl-02-0.52905.json: e9950d59b061b00721fdb4387bd2b2ff4475563035c825814d1b3eceb46ea50a
  - lauf-69/nl-02-0.529266.json: 00a5ed19dda669aaa0917b3b38ba3d73f633eeec39ba4d53bb0f30ca37a880b1
  - lauf-69/nl-02-0.52950.json: a8cb1727f77371a087365ddc12af7df9edffde28e53e3bdcca8d8091d7c35ba7
  - lauf-69/nl-02-0.53139.json: 5827ffeccf9976711b563743130e0df585a4e5de8d2954b8a5236051200418f2
  - lauf-69/nl-04-0.52905.json: e30607b13febb06212db10a8149c11ee87b12e54e184e5e1dac28afaab3b266e
  - lauf-69/nl-04-0.529266.json: ae9acb4bfc1d50b3ba64e1ff42f7c7fd3f4a8a189306a224dc666e4da571a9bf
  - lauf-69/nl-04-0.52950.json: 69659f21612679312cdaa20734d12b6442950103e6862f6041ed83a6e2823c4a
  - lauf-69/nl-04-0.53139.json: ff249e315079f20676ef1b6c76f8224cccb7c83a3861bd3145f0ae46a9577439
  - lauf-69/scan-04-0.52915.json: 05c8904514a0b34e080ebef90f7f51ad73de9d2ed947a1985ead306ecd898968
  - lauf-69/scan-04-0.52920.json: c3e11f9fb3ef6d6da746ae6e02e4cb7bba5eb5cb403acc080ae7a2befefffcab
  - lauf-69/scan-04-0.52925.json: 5328d7df2360c011d8c8e898752670a60c46c4db9fccc2a5683532eaf35ac609
  - lauf-69/scan-04-0.52930.json: 67865f6efafcbf8e49295fbc8db69f83dce28f681860de87baaab5678e40ed53
  - lauf-69/scan-04-0.52935.json: c0710957538bc90976b1488a077250fc07949a497c0355cb2bb01da1c68189a8
  - lauf-69/scan-04-0.52940.json: 89f36133c425f86340df481af92733e95b5bbfa9ebfa2737153f6b76d86fb15f
  - lauf-69/still-nachtrag.json: 27daf90c6b29ad83ff9061ca7cea9154c29d97b4744fff653cf3909c90f39ec3

## 7. Einfach gesagt

Ein Q-Ball kann klingen wie eine Glocke, und einer seiner Toene ist fast vollkommen "still": Bei bestimmten
Ballgroessen, den Sprossen, gibt er praktisch keine Energie nach aussen ab. Diesmal haben wir den Ball wirklich in der
Zeit schwingen lassen und gemessen, wie schnell dieser Ton leiser wird. Genau an der Sprosse klingt er praktisch gar
nicht ab, knapp daneben erst nach einigen tausend Zeiteinheiten, zwischen zwei Sprossen schon nach rund 140. Das ist
genau das V, das die fruehere Frequenzrechnung vorhergesagt hatte. Ein glatter Klumpen, der sich zum Ball formt,
schlaegt diesen stillen Ton aber kaum an: Er wackelt vor allem mit einer langsamen Atmung der Ballwand, die gar nicht
abstrahlen kann und deshalb so lange anhaelt.

---
Letzte Aenderung dieser Datei: 2026-10-02 21:20:08 CEST (date). Zeitbox 90 min ab 20:22:32 eingehalten.
