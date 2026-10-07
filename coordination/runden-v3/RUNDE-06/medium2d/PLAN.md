# Runde 6, Agent M2: Medium-Karten in 2D (Laufplan)

Bearbeiter: Anthropic-Agent M2 (Opus 5.5), Auftrag RUNDE-06/AUFTRAG-MEDIUM-UND-2D-B.md, Abschnitt "Agent M2".
Beginn 2026-09-30 02:53:36 CEST (gemessen), Plan begonnen 03:30:23 CEST (gemessen), Ende in der letzten Zeile.
Status: Code geschrieben, **lokaler Formtest (Mini-Gitter, CPU) gelaufen, auf der .69 nicht gerechnet**. Explorativ,
keine formale Bestaetigung. Zahlen in den Vorhersagen sind Papierwerte [S] oder Literatur aus dem Gedaechtnis [L].

## Kurzfassung

- **Code:** medium2d.py (PyTorch, float64/complex128, `--geraet cuda|cpu`). Unterbefehle `profile`, `magnus`,
  `kielwasser`, `wirbel`, `brechung`, dazu `alle --rauch`. Jede Karte rechnet `--stufe grob|fein|beide`.
- **Aufbau:** zwei Felder, psi (Q-Ball, Schiessen und Laplace aus tests2d_r3.py, Schiessregel fuer m != 0 aus
  r5_2d_a.py) und chi (Medium wie r5d.py: C0 = 0,1, g4 = 0,5, lam = 0,1; c_s = 0,2085, Heilungslaenge etwa 3,2).
- **Anfangszustand:** Ball und Medium werden gemeinsam relaxiert (Gradientenfluss, psi bei fester Ladung, chi bei festem
  chemischem Potential). Erst dann wird die Stroemung bzw. der Anschub langsam hochgefahren (sin^2-Rampe, 60 bis 100
  Zeiteinheiten). Gemessen wird danach.
- **Kernvorhersagen:**
  - Magnus: Keine Querdrift ohne gebundene Zirkulation im Medium, egal ob m = +1, -1 oder 0. Es bleibt nur ein kleiner
    fester Querversatz m (Q/E) v_x (Moeller-Verschiebung, bekannt).
  - Mitnahme: Der freie Ball wird beim Anlaufen der Stroemung auf eine feste Geschwindigkeit v_x ~ 0,05 bis 0,17 u
    gebracht und behaelt sie; das ist mitbewegte Mediumsmasse, keine Dauerkraft. Das ist die 2D-Lesart des
    "kreuzen"-Befunds.
  - Kielwasser: Machkegel mit Halbwinkel atan(tan(arcsin(c_s/u))/gamma) im Ruhesystem des Balls, kein Kelvin-Winkel.
  - Wirbelstrasse: Wirbelpaare erst ab etwa 0,55 bis 0,85 c_s, oben negative, unten positive Windung.
  - Brechung: Brechung wie ein Teilchen mit der Ruhemasse M_eff(C) aus der Relaxation. Abweichungen im
    Prozentbereich erwarte ich durch mitgefuehrte Mediumsmasse.
- **Laufzeit (Schaetzung P4000):** je Aufruf 1,5 bis 3,5 min, acht Aufrufe zusammen etwa 20 min. Der GPU-Rauchtest
  (`alle --rauch`) dauert etwa 1,5 min.
- **Lokal gelaufen:** Formtest `alle --rauch --mini --geraet cpu`, 45,8 s, rc 0. Er fand vier Fehler, alle behoben
  (Abschnitt 0.1).

## 0. Hinweise an die Leitung

### 0.1 Lokaler Formtest (Freigabe Finn 30.09. 02:42), gemessen

- **Aufruf** (aus dem Ordner medium2d/):

```
mkdir -p lauf-lokal && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
  nice -n 19 timeout 120 python3 medium2d.py alle --rauch --mini --geraet cpu --out lauf-lokal/mini
```

- **Letzter Lauf:** 03:27:17 bis 03:28:07, gesamt 45,8 s, rc 0, alle fuenf Teile ohne Fehler. Log in
  lauf-lokal/rauch-mini.log.
  - Zusaetzlich `magnus --stufe grob` und dann `--stufe fein` einzeln (je etwa 25 s) als Probe des L3-Abgleichs
    ueber zwei Aufrufe; Ausgaben in lauf-lokal/mini-stufen/. Die .pt-Dateien des Mini-Tests sind geloescht (Zahlen
    ungueltig); Berichte, JSON und Logs bleiben.
- **Mini heisst:** dx 0,6/0,48, dt 0,1/0,08, Laufzeiten x 0,02, 50 Relaxationsschritte, 64 Schiesskandidaten in 9 Runden.
  Die Zahlen gelten nicht, der Test prueft nur Codepfade.
- **Gefundene und behobene Fehler:**
  1. Der harmonische Halter wuchs bis in die Boxecken (V bis 9). Damit wurde der explizite Teil der Relaxation
     instabil (Faktor 1 - dtau V < -1). Jetzt gilt V_h = a R^2 tanh(r^2/R^2) mit R = 12 und periodischem Abstand.
  2. In den brechung-Laeufen fehlte der Schluessel m.
  3. Die chi-Randschicht daempfte gegen die reine Drehfrequenz. Waehrend und nach der Rampe atmet das gleichfoermige
     Medium aber (k = 0). Die Randschicht bremste dieses Atmen nur am Rand, und "Medium allein" wurde ungleichfoermig
     (Spanne 8e-5). Jetzt wird jede Stufe gegen die komplexe Rate chi_t/chi daempft, gemittelt ueber die Randschicht.
     Danach: Spanne 0,0 und Q_chi erhalten.
  4. Der Schaetzer fuer den Machwinkel blieb am Rand des Suchbereichs haengen. Jetzt gilt die RMS-Spitze laengs der
     Strahlen im Bereich 8 bis 87 Grad; die aeussere 50-%-Kante wird mitberichtet.
- **Codeproben, die schon im Mini-Test halten** (gelten erst nach dem .69-Lauf):
  - Spiegelprobe |Y(m = +1) + Y(m = -1)| = 6e-14; m = 0: |Y| = 6e-15.
  - lam = 0: Der Ball bleibt auf 1e-6 liegen.
  - M_eff bei lam = 0 trifft die Vakuumenergie des Profils auf 8e-6.
  - Medium allein bleibt gleichfoermig (Spanne 0).
- **Selbstanzeige:** Um etwa 03:20 stand versehentlich `python3 -` (ohne Programm, leere Eingabe, sofort beendet, ohne
  nice und timeout) vor einem grep-Befehl. Gerechnet wurde nichts.

### 0.2 Schiessen fuer m != 0

- Uebernommen ist die berichtigte Coleman-Regel aus r5_2d_a.py (Hinweis der Leitung, 02:55):
  - Ueberschuss: f > f_top oder f < 0.
  - Unterschuss: f' > 0 unterhalb der Talsohle, nachdem die Bahn gefallen ist.
  - Fuer |m| >= 1 wird ln p eingeschachtelt.
- Geschossen wird auf der CPU (kleine Tensoren; auf der GPU kostete es in R3 60 bis 100 s je Aufruf), mit 256 Kandidaten
  in 7 Runden (256^7 > 1e16).
- Der Formtest trifft die 2D-A-Profile:
  - m = 1 bei omega^2 = 0,60: Q 138,757, E 123,074, R_halb 5,957, Virialrest -4e-11.
  - m = 0 bei 0,55, 0,60 und 0,70 wie R3.

### 0.3 Stroemung: Eichrampe statt Phasenwindung

- **Die Stroemung entsteht durch ein gleichfoermiges aeusseres Feld.** chi koppelt an A(t) = (-q r(t), 0) ueber
  (grad - iA). Waehrend der Rampe wirkt das wie eine gleichfoermige Kraft auf die Mediumsladung (ein Windkanal mit
  Druckgefaelle). Danach ist A konstant und lokal reine Eichung.
  - Fuer q = k_n = 2 pi n/(2L) ist das exakt das Modell ohne Eichfeld mit chi ~ exp(i k_n x), also die quantisierte
    Stroemung aus dem Auftrag.
  - Fuer andere q ist es dieselbe lokale Physik mit einer Bloch-Phase am Boxrand (verdrehte periodische
    Randbedingung). Deshalb sind beliebige u/c_s moeglich.
  - Quantisierte Werte in dieser Box (2L = 76,8) waeren n = 1, 2, 3, 4, 6, also u/c_s etwa 0,37 / 0,74 / 1,09 / 1,43 /
    2,0. Wer nur quantisierte Werte will, ersetzt u_cs in den Laeuflisten entsprechend.
- **Die Mediumsdichte sinkt beim Beschleunigen leicht**, denn die Ladungsdichte 2 C w bleibt erhalten:
  C_f = C0 w0/w_f, w_f^2 (1 - u^2) = 1 + 2 g4 C_f.
  - Der Code rechnet u/c_s mit c_s(C_f). Beispiel: 2,5 c_s bedeutet u = 0,492 bei C_f etwa 0,085.
- **Anschub des Balls** (nur brechung): dasselbe mit B(t) an psi. Der Gesamtimpuls (Ball plus Medium) ist danach exakt
  Q |B|. Daraus folgt die traege Masse im Medium M* = Q |B|/v1.

## 1. Festlegungen fuer alle Karten (vor dem Lauf)

- **Modell:**
  - L = |psi_t|^2 - |(grad - iB)psi|^2 + |chi_t|^2 - |(grad - iA)chi|^2 - V
  - V = U(S) + V_h S + C + g4 C^2 + W C + lam S C, mit U = S - S^2 + S^3/2
  - W: aeusseres Potential nur fuer chi (Dichtestufe); V_h: Halter nur fuer psi.
  - Kein eps (Ladungsaustausch); das bleibt bei M1.
- **Warum der Ball ein Hindernis ist:** Im Thomas-Fermi-Bild ist C_innen = C0 - lam S/(2 g4). Bei S etwa 1 und lam = 0,1
  wird das Medium im Ball fast ganz verdraengt. Der Ball ist ein Loch mit Radius R etwa 2 bis 7, also 0,6 bis 2 xi.
- **Relaxation (Gradientenfluss, halbimplizit spektral, dtau = 0,4, bis 2500 Schritte oder Residuum < 1e-8):**
  - psi_tau = Lap psi - (U' + lam C + V_h - omega^2) psi mit omega = Q/(2N): Abstieg von E bei fester Ladung.
  - chi_tau = Lap chi - (1 + 2 g4 C + lam S + W - w0^2) chi mit w0^2 = 1 + 2 g4 C0: Fernfeld C0.
  - Waechter: Waechst der Quadrupol c2 eines Balls ueber 1e-2 (Teilungsmode), bricht die Relaxation mit Warnung ab.
- **Start:** psi_t = -i (sin th/dt) psi mit cos th = 1 - dt^2 omega^2/2. Das ist die exakte diskrete Kreisbahn des
  Velocity-Verlet, also kein O(dt^2)-Atmen wie in R5 ("Medium allein" 6e-4). Fuer chi entsprechend.
- **Numerik:**
  - Laplace spektral in der periodischen Box [-38,4, 38,4)^2.
  - grob: dx = 0,3, dt = 0,05 (256^2); fein: dx = 0,2, dt = 0,025 (384^2).
  - Randschicht 8 breit, sigma0 = 0,5. psi: psi_t wird gedaempft. chi: gedaempft wird nur die Abweichung
    chi_t - lambda chi, wobei lambda die mittlere Rate in der Randschicht ist. Gleichfoermige und stationaere
    Stroemung, auch um den Ball herum, bleibt dadurch unberuehrt.
- **Messung alle 1,0:**
  - Schwerpunkt (Gewicht S^2, periodisch)
  - Kraft des Mediums auf den Ball F = -Int lam S grad C dA
  - Q_psi, Q_chi
  - Windung von psi auf einem Kreis um den Ball (m bleibt erhalten?)
  - Zirkulation von chi auf einem Kreis mit R_halb + 6 bzw. + 4 (gebundene Wirbel)
  - **chi-Wirbel Plakette fuer Plakette:** Phasensumme der vier Kanten / 2 pi, gegen den Uhrzeigersinn positiv. Getrennt
    nach Vorzeichen, oberhalb/unterhalb des Balls, ausserhalb des Kreises, ohne Randschicht.
  - Quadrupol c2 von S (Teilung), C-Spanne im Innenbereich, sechs Dichtebilder je Lauf.
  - Kielwasser: zusaetzlich das Zeitmittel von C.
- **Rohdaten:** <karte>_<stufe>_roh.pt und .json werden sofort nach jeder Stufe gesichert, vor der Auswertung. Eine
  abgestuerzte Auswertung steht im Bericht, ohne die Rechnung zu kosten.

## 2. Rechenzeit (Schaetzung aus dem Tropfentest)

- **Grundlage:** tests2d_r3 tropfen auf der P4000 (lauf-69/R3-2D.log):
  - grob: 4 Laeufe, 320^2, 20 000 Schritte in 45,3 s, also 5,5 ns je Punkt und Schritt
  - fein: 2 Laeufe, 480^2, 40 000 Schritte in 114,2 s, also 6,2 ns
  - Ein Feld mit 2 FFT und etwa 17 Elementoperationen je Schritt.
- **Hier je Schritt:** 4 FFT und etwa 40 Operationen (zwei Felder, chi-Randschicht mit Rate), dazu alle 20 Schritte
  Messungen mit 3 FFT, Plaketten und etwa 60 Operationen. Faktor etwa 2,4 x 1,15, also **etwa 17 ns je Punkt und
  Schritt**. Relaxation etwa 10 ns je Punkt und Schritt. Schiessen auf der CPU 10 bis 20 s je Aufruf.

| Aufruf | Arbeit | Schaetzung |
|---|---|---|
| alle --rauch | 4 Profile, alles x 0,05 | etwa 1,5 min |
| magnus --stufe grob | 8 Laeufe x 256^2 x 8000 Schritte, Relaxation | etwa 1,8 min |
| magnus --stufe fein | 3 x 384^2 x 16 000 | etwa 2,5 min |
| kielwasser (beide) | 6 x 256^2 x 5600 und 3 x 384^2 x 11 200 | etwa 2,5 min |
| wirbel --stufe grob | 6 x 256^2 x 14 000 | etwa 2 min |
| wirbel --stufe fein | 2 x 384^2 x 28 000 | etwa 2,6 min |
| brechung --stufe grob | 8 x 256^2 x 8400, dazu 10 Massenrelaxationen | etwa 2 min |
| brechung --stufe fein | 3 x 384^2 x 16 800, 10 Massenrelaxationen fein | etwa 3,2 min |

- Unsicherheit etwa Faktor 1,5, zum Beispiel wenn Ollama die Karte teilt. Alle Aufrufe bleiben unter 6 min.
- Der GPU-Rauchtest druckt je Karte "Hochrechnung Hauptlauf"; ueber 540 s: Stufen einzeln (so schon geplant).
- **Speicher:** hoechstens etwa 0,3 GB (fein, 10 Massenrelaxationen). Die .pt-Dateien sind 5 bis 20 MB je Stufe
  (Dichtebilder float32).

## 3. Karten: Aufbau, Vorhersage, Gegenproben

### 3.1 magnus (Wellen 8/9, Magnus und Flettner)

- **Aufbau:**
  - Freier Ball bei (-8, 0), omega^2 = 0,60. m = +-1: Q 138,8, E 123,1, R_halb 6,0; m = 0: Q 66,6, E 56,5, R_halb 3,4.
  - Stroemung in +x, Rampe 100, T = 400.
- **Laeufe:**
  - m = +1 / -1 bei u = 0,4 c_s (0,083) und 0,8 c_s (0,166)
  - m = 0 bei 0,8 c_s
  - m = +1 ohne Stroemung (Stabilitaet des drehenden Balls)
  - m = +1 bei 0,8 c_s mit lam = 0
  - Medium allein bei 0,8 c_s
  - fein: die drei Laeufe bei 0,8 c_s.
- **Warum keine Magnuskraft zu erwarten ist [S]:**
  - Das Medium sieht vom Ball nur S = |psi|^2 (Dichtekopplung). S eines stationaeren m = +-1-Balls ist
    achsensymmetrisch und zeitunabhaengig. Die Drehung von psi ist fuer chi unsichtbar; es gibt keine Haftbedingung,
    die das Medium mitdreht.
  - Die Zirkulation von chi um den Ball ist gequantelt (2 pi n/w) und am Anfang null. Aendern kann sie sich nur, wenn
    ein chi-Wirbel die Messschleife kreuzt.
  - Kutta-Joukowski (gilt auch unterschallig kompressibel): Auftrieb = rho u Gamma = 0. Der Widerstand ist null
    (d'Alembert, Suprafluid).
  - Symmetrie: psi -> conj(psi) laesst S gleich und macht (m, Q) zu (-m, -Q); die Spiegelung y -> -y macht (m, Q) zu
    (-m, Q). Eine Querkraft ist also nur proportional zu J = m Q erlaubt, nicht verboten. Deshalb ist das hier eine
    echte Probe (L1).
  - Naive Gegenerwartung: Wuerde der Ball das Medium mitdrehen (Gamma ~ 2 pi m/omega), dann waere
    a_y ~ rho Gamma u/M ~ 1e-3, also Delta y ~ 50 in 300 Zeiteinheiten. Das waere nicht zu uebersehen.
- **Vorhersagen (vor dem Lauf):**
  - **V-M1 (Kern):** Fuer m = +-1 bei 0,4 und 0,8 c_s gilt, solange die chi-Zirkulation um den Ball null bleibt:
    |dY - dY_Moeller| < 0,05 und |v_y| < 1e-4 (p = 0,8). Urteil im Code: "keine Querdrift ohne Zirkulation".
    Befund-Kandidat bei |dY - dY_Moeller| > 0,15 oder |v_y| > 3e-4.
  - **V-M2 (bekannt, ableitbar, keine Messung):** fester Querversatz dY = m (Q/E) v_x, gleiches Vorzeichen wie m bei
    Bewegung in +x. Das ist der Moeller-Versatz des Schwerpunkts eines drehenden Koerpers (J v/M). Mit v_x etwa 0,01 bis
    0,03 ist er etwa 0,01 bis 0,03.
    - Im Mini-Test gemessen: 2,53e-4 gegen m Q v_x/E = 2,28e-4.
    - Der Code zieht ihn vor dem Urteil ab.
  - **V-M3 (Mitnahme):** Nach der Rampe laeuft der freie Ball mit fester Geschwindigkeit v_x weiter (a_x etwa 0).
    - v_x/u = m_a/(M + m_a) mit m_a = rho pi R^2, rho = 2 w^2 C etwa 0,22 (Enthalpiedichte).
    - Starres Hindernis: m = 1: 0,17; m = 0: 0,12. Weil der Ball weich und durchlaessig ist, erwarte ich 0,3 bis 1,0
      davon, also m = 1: 0,05 bis 0,17 und m = 0: 0,04 bis 0,12.
    - Das ist reversible Mitnahme beim Anlaufen, keine Dauerkraft unter c_s. Das ist meine Lesart des 1D-"kreuzen"-
      Befunds (v_Ende = 5,2e-3, a spaet 4e-6). M1 klaert ihn in 1D.
  - **V-M4:** Bei 0,8 c_s entstehen chi-Wirbel mit p = 0,5 (m = +-1, groesser) bzw. p = 0,3 (m = 0).
    - Bindet ein Wirbel (Zirkulation n != 0), dann gibt es Auftrieb F_y = -4 pi w C u n, etwa -0,2 n (Kutta-Joukowski
      mit rho = 2 w^2 C). Der Code prueft das Vorzeichen.
    - Ob das Vorzeichen von n mit m zusammenhaengt: erwartet nein (p = 0,6). Nur die Spin-Kippung der Dichte koennte
      es koppeln.
  - **Stabilitaet (Lauf m+1_ruhe):** Der m = 1-Ball bleibt heil (Windung 1, c2 < 0,05) ueber T = 400 mit p = 0,7.
    Teilt er sich, sind die m = +-1-Laeufe ohne Aussage (Code: "Ball nicht heil").
- **Gegenproben:**
  - Spiegel |Y(+1) + Y(-1)| < 1e-10 (exakt, Gittersymmetrie)
  - m = 0: |Y| < 1e-12
  - lam = 0: |dX|, |Y| < 1e-5
  - Medium allein: C-Spanne < 1e-12, Q_chi konstant
- **L3:** v_x, dY, v_y grob gegen fein.

### 3.2 kielwasser (Wellen 4)

- **Aufbau:**
  - Ball m = 0, omega^2 = 0,60, gehalten (V_h = 2e-3 r^2 innen) bei (-12, 0).
  - Medium stroemt in +x, Rampe 80, T = 280. Dichtebild gemittelt ueber die letzten 60 Zeiteinheiten.
  - Ausgewertet wird ein Winkelprofil im Ring r = 10 bis 24 hinter dem Ball.
- **Bezugssystem:** Der Auftrag sagt "Ball bewegt durch ruhendes Medium". Beide Felder sind relativistisch; ein
  stroemendes Medium der Dichte C ist die Lorentz-Transformierte des ruhenden. Also ist das Ruhesystem des Balls
  gleichwertig, und das Muster steht dort still, was die Messung sehr vereinfacht.
  - Der Winkel transformiert sich: tan a' = tan(arcsin(c_s/u))/gamma.
  - Die Gleichwertigkeit selbst prueft M1 in 1D (Wellen 11).
  - Ein Lauf "Ball bewegt" waere mit dem B-Anschub moeglich, braucht aber eine laengere Box: naechste Runde.
- **Laeufe:**
  - u/c_s = 0,5 / 1,3 / 1,8 / 2,5 (u = 0,104 / 0,267 / 0,364 / 0,492)
  - u/c_s = 1,8 mit lam = 0
  - Medium allein bei 1,8
  - fein: 1,3 / 1,8 / 2,5
- **Warum kein Kelvin-Winkel [S]:**
  - Kelvins feste 19,47 Grad folgen aus der Tiefwasser-Dispersion omega ~ sqrt(k). Dort faellt die Phasengeschwindigkeit
    mit k, und die Gruppengeschwindigkeit ist halb so gross.
  - Bogoliubov ist umgekehrt: Die Phasengeschwindigkeit ist mindestens c_s und steigt mit k, die Gruppengeschwindigkeit
    ist groesser als die Phasengeschwindigkeit.
  - Folgen:
    - Unter c_s gibt es gar keine stehenden Wellen (Landau).
    - Ueber c_s bilden die langen Wellen den Machkegel. Sein Winkel haengt von u ab.
    - Kurze Wellen liegen ausserhalb des Kegels, vor dem Ball [L: Carusotto u. a., PRL 97, 260403 (2006); Gladush u. a.
      2007].
    - Im Kegel koennen schraege dunkle Solitonen stehen, konvektiv stabil etwa ab 1,44 c_s [L: El, Gammal, Kamchatnov,
      PRL 97, 180405 (2006)].
- **Vorhersagen:**
  - **V-K1:** RMS-Spitze des Winkelprofils (8 bis 87 Grad) innerhalb 6 Grad von a' = 49,2 / 31,9 / 20,8 Grad (u = 1,3 /
    1,8 / 2,5 c_s; Mediumswinkel 50,3 / 33,7 / 23,6).
    - Erwartet ist eher ein etwas groesserer Winkel (dispersive Wellen aussen), also 0 bis +6 Grad (p = 0,55).
    - Die 50-%-Kante wird mitberichtet, ohne Kriterium.
  - **V-K2:** Bei 0,5 c_s ist die RMS-Amplitude im Ring kleiner als 10 % der Amplitude bei 1,3 c_s (p = 0,75).
  - **V-K3:** Widerstand F_x(0,5 c_s) kleiner als 10 % von F_x(1,3 c_s) (p = 0,7). Unter c_s koennte nur
    Wirbelbildung bremsen; die ist bei diesem kleinen Ball (R etwa xi) unwahrscheinlich.
  - Der Widerstand steigt ueber c_s mit u.
- **Gegenproben:** lam = 0 (kein Muster, Amplitude < 1e-6); Medium allein (Spanne 0); oben/unten symmetrisch.
- **L3:** Winkel (2 Grad), Amplitude, F_x.

### 3.3 wirbel (Wellen 18, Wirbelstrasse)

- **Aufbau:**
  - Grosser Ball m = 0, omega^2 = 0,55 (Q 238,4, R_halb 6,9, D = 13,8, also etwa 4 xi).
  - Gehalten mit V_h = 5e-4 r^2 innen, bei (-14, 0,05). Die 0,05 sind ein kleiner Anstoss gegen die exakte
    Spiegelsymmetrie.
  - Rampe 100, T = 700.
- **Laeufe:**
  - u/c_s = 0,4 / 0,55 / 0,7 / 0,85 / 1,0
  - 0,85 mit lam = 0
  - fein: 0,7 und 0,85
- **Messung:**
  - Wirbel ausserhalb des Kreises R_halb + 4 je Vorzeichen und Seite
  - "Ereignisse" = Zunahmen dieser Zahlen, mit Zeiten
  - mittlerer Abstand der Ereignisse und Strouhal-Zahl St = f D/u
  - Auftrieb F_y(t) mit Periodogramm (eine wechselnde Abloesung erzeugt einen schwingenden Auftrieb, eine symmetrische
    keinen)
- **Literatur [L, aus dem Gedaechtnis]:**
  - Frisch, Pomeau, Rica, PRL 69, 1644 (1992): Wirbelpaare hinter einer Scheibe in 2D-NLS ab v_c etwa 0,4 c fuer
    R >> xi.
  - Huepe und Brachet (2000): Schwelle bei kleineren Hindernissen hoeher.
  - Sasaki, Suzuki, Saito, PRL 104, 150404 (2010): Karman-Strasse in BEC-Simulationen fuer genuegend grosse
    Hindernisse und ein schmales Geschwindigkeitsfenster.
  - Kwon u. a., PRL 117, 245301 (2016): im Experiment beobachtet.
  - Klassisch ist St etwa 0,2.
- **Vorhersagen:**
  - **V-W1:** Bei 0,4 c_s kein Wirbel. Die Schwelle liegt zwischen 0,55 und 0,85 c_s (p = 0,6).
  - **V-W2:** Wirbel entstehen paarweise (Gesamtwindung 0). Oben mit negativer, unten mit positiver Windung (Stroemung in
    +x; p = 0,8).
  - **V-W3:** Die Abloesefrequenz steigt mit u; St zwischen 0,05 und 0,3 (p = 0,6).
    - Wechselnde Abloesung (Karman-artig, schwingender Auftrieb): p = 0,3.
    - Symmetrische Paarabloesung: p = 0,5.
    - Der Ball ist mit D etwa 4 xi eher klein.
  - **V-W4:** lam = 0: kein Wirbel, keine Kraft.
- **Achtung:**
  - Der Halter hat die Eigenperiode 2 pi sqrt(M/(2 a N)), etwa 214. Einrasten der Abloesung auf diese Periode
    (wirbelerregte Schwingung) ist moeglich. Deshalb wird die X-Spanne berichtet.
  - Wirbel koennen am Rand liegen bleiben; gezaehlt wird nur ausserhalb der Randschicht.
- **L3:** Zahl der Ereignisse (+-1), erster Zeitpunkt (+-20), F_x.

### 3.4 brechung (Wellen 14, Brechung im Medium)

- **Aufbau:**
  - Dichtestufe C0 -> C0 + dC bei x = 0, Breite 2. Erzeugt durch W = -2 g4 dC s(x) nur fuer chi; periodisch
    geglaettet, die zweite Stufe liegt in der Randschicht.
  - Ball m = 0, omega^2 = 0,70 (Q 24,0, klein wie in R3), Start bei (-16, -16 tan th1).
  - Anschub mit B: Soll v1 = 0,12 (0,58 c_s) unter th1, Rampe 60, T = 420. Fits fuer |X| >= 9.
- **Ruhemasse im Medium vorab:**
  - M_eff(C) = F(Ball + Medium) - F(Medium) mit F = E - w Q_chi (Medium als Reservoir, festes w), durch Relaxation in
    gleichfoermigen Medien fuer jedes dC der Laeufe.
  - Mini-Test (dx 0,6, nur zur Groessenordnung): M(0,10) = 22,755; M(0,14) = 22,810; M(0,16) = 22,838;
    M(0,06) = 22,701; Vakuum 22,626.
  - Die Stufe verschiebt die Masse um etwa 1,37 dC, also 0,24 % bei dC = 0,04. In R3 waren es 1,3 %.
- **Vorhersage P1 (bindend, wie R3):** E = gamma1 M1 und p_y erhalten, p2^2 = E^2 - M2^2, sin th2 = p_y/p2.
  - Der Code rechnet sie aus dem gemessenen v1 und th1.
  - Handwerte fuer v1 = 0,11 (erwartet etwas unter 0,12 wegen der Mitnahme):

| Lauf | dC | th1 | P1: th2 | P1: v2 | Ausgang |
|---|---|---|---|---|---|
| abst20 | +0,04 | 20 | 26,1 | 0,086 | durch (Grenzwinkel etwa 51 Grad) |
| abst40 | +0,04 | 40 | 55,7 | 0,086 | durch |
| abst50 | +0,06 | 50 | - | - | reflektiert (Grenzwinkel etwa 40 Grad) |
| anz20 | -0,04 | 20 | 16,9 | 0,130 | durch |
| anz40 | -0,04 | 40 | 33,1 | 0,130 | durch |
| senkrecht | +0,04 | 0 | 0 | 0,086 | durch |
| ohne40 | 0 | 40 | 40 | 0,11 | gerade |
| lam0_40 | +0,04, lam = 0 | 40 | 40 | 0,11 | gerade |

- **Variante P2 (nicht bindend):**
  - Mitgefuehrte Mediumsmasse: M* = Q|B|/v1 wird gemessen, m_a = M* - gamma1 M1. m_a waechst proportional zu C.
  - p_y erhalten, K = p^2/(2 M*).
- **Vorhersagen:**
  - **V-B1:** P1 haelt fuer alle sechs Stufenlaeufe (1 Grad, 2 %, Ausgang); p = 0,35.
    - Ich erwarte Abweichungen von einigen Prozent in v2, weil die mitgefuehrte Masse (m_a/M etwa 0,02 bis 0,15) in P1
      fehlt.
  - **V-B2:** Die Ausgaenge stimmen, einschliesslich der Reflexion bei abst50 (p = 0,8).
  - **V-B3:** m_a/M zwischen 0,02 und 0,15. Kontrolle: bei lam = 0 ist M*/(gamma M) = 1 auf 1e-3.
  - **V-B4:** Kein Ladungsverlust (< 1e-3). In R3 verloren die steilen anziehenden Laeufe an der Potentialstufe 92 bis
    94 % ihrer Ladung. Hier ist die Stufe fuenfmal schwaecher und wirkt nur ueber das Medium.
  - **V-B5:** Kein Wirbel (Ball unter c_s aller Medien der Laeufe: 0,166 bei C = 0,06 bis 0,254 bei C = 0,16).
- **Gegenproben:** ohne Stufe (Knick < 0,2 Grad), lam = 0 (gerade), senkrecht (nur Geschwindigkeit), vy2/vy1, M_eff bei
  lam = 0 gegen die Vakuumenergie.
- **L3:** th2 (0,3 Grad), v2.

### 3.5 Linse (Wellen 15): nur Papier, kein Code

- **Umsetzbar mit derselben Maschine:**
  - W(x, y) als Scheibe (Radius R_L = 10) mit dC = -0,04.
  - Fuenf Laeufe mit je einem Ball bei y0 = 2 / 4 / 6 / 8 / 10, parallel in +x.
  - Getrennte Laeufe statt einer Reihe, damit sich die Baelle nicht beruehren.
- **Brennweite [S]:** n = p_innen/p_aussen etwa 1,18 (v1 = 0,11). Kugellinse paraxial f = n R/(2 (n - 1)), etwa 33 vom
  Mittelpunkt.
  - Das passt nicht in diese Box (die Randschicht beginnt bei 30).
  - Loesungen: eine laengere Box oder ein langsamerer Ball (v1 = 0,08 und dC = -0,06: n etwa 1,45, f etwa 16). Der
    Ball ist dann innen nahe c_s(0,04) = 0,137.
  - Kugelaberration: f faellt mit y0. Mit Strahlverfolgung in M_eff(C(x, y)) vorab rechenbar.
- **Vorschlag:** naechste Runde, wenn brechung P1 oder P2 traegt.

### 3.6 Kelvin-Helmholtz (Wellen 17): nur Papier, Karte parken

- **Grenzflaeche:** zwischen psi-Tropfen und Medium.
  - Tropfen: sigma etwa 0,38 aus R3, Dichte rho1 = 2 omega^2 S etwa 1,06.
  - Medium: rho2 = 2 w^2 C etwa 0,22.
- **KH ohne Schwere [S]:** instabil fuer k < rho1 rho2 U^2/((rho1 + rho2) sigma), also etwa 0,48 U^2.
  - Auf einem Tropfen mit Radius R ist die kleinste Mode l = 2 (k = 2/R). Instabil ab U^2 > 4,2/R.
  - Beim groessten bezahlbaren Tropfen (omega^2 = 0,52, R = 17,5) heisst das U > 0,49, also 2,3 c_s. Dort ueberdecken
    Wellenwiderstand und Machkegel alles.
  - Suprafluid-KH [L: Blaauwgeers u. a., PRL 89, 155301 (2002), 3He A-B; Takeuchi u. a., PRB 81, 094517 (2010),
    zwei BEC-Komponenten] aendert die Schwelle nur um Faktoren der Ordnung 1.
- **Vorhersage:** Unter c_s kein KH-Wachstum. Parken, bis ein dichteres Medium (groesseres rho2) oder kleineres sigma
  (omega^2 naeher an 1/2) ansteht.

## 4. Gegenproben im Ueberblick

| Probe | Karte | Erwartung |
|---|---|---|
| lam = 0 | alle | keine Kraft, kein Muster, kein Wirbel, Ball bleibt bzw. laeuft gerade |
| Medium allein | magnus, kielwasser | Stroemung exakt: C-Spanne 0, Q_chi konstant (im Mini-Test schon so) |
| m -> -m | magnus | Y(+1) = -Y(-1) exakt (Gitterspiegel); die Physik steckt im Betrag |
| m = 0 | magnus | Y = 0 exakt |
| ohne Stufe | brechung | gerade, v unveraendert |
| M_eff(lam = 0) | brechung | Vakuumenergie des Profils (Mini-Test: 8e-6) |
| zwei Aufloesungen | alle | L3-Tabelle im Bericht, automatisch auch ueber zwei Aufrufe |

## 5. Aufrufe fuer die .69 (Leitung)

- **Vorbereitung:** medium2d.py nach /home/fmh/fmhc-physics-remote/runde6-medium2d/ kopieren. Das Programm braucht nur
  torch und schreibt nur in --out (Vorgabe: `ausgabe/` bzw. `rauchtest/` neben dem Skript).
- **Reihenfolge:** zuerst der Rauchtest, dann die grob-Aufrufe, dann die fein-Aufrufe.
  - Ein fein-Aufruf liest das grob-Ergebnis aus demselben Ordner und schreibt die L3-Tabelle.
  - Parallel geht p4000b, wenn WM-1-MB ruht; die Spur p4000b prueft das selbst.

```
cd /home/fmh/fmhc-physics-remote/runde6-medium2d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m2-rauch medium2d.py alle --rauch
cd /home/fmh/fmhc-physics-remote/runde6-medium2d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m2-magnus-g medium2d.py magnus --stufe grob
cd /home/fmh/fmhc-physics-remote/runde6-medium2d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m2-brechung-g medium2d.py brechung --stufe grob
cd /home/fmh/fmhc-physics-remote/runde6-medium2d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m2-kielwasser medium2d.py kielwasser
cd /home/fmh/fmhc-physics-remote/runde6-medium2d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m2-wirbel-g medium2d.py wirbel --stufe grob
cd /home/fmh/fmhc-physics-remote/runde6-medium2d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m2-magnus-f medium2d.py magnus --stufe fein
cd /home/fmh/fmhc-physics-remote/runde6-medium2d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m2-brechung-f medium2d.py brechung --stufe fein
cd /home/fmh/fmhc-physics-remote/runde6-medium2d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m2-wirbel-f medium2d.py wirbel --stufe fein
```

- **Laufzeiten:** siehe Abschnitt 2, je 1,5 bis 3,5 min, zusammen etwa 20 min. Keiner der Aufrufe braucht mehr als
  0,3 GB GPU-Speicher.
- **Ausgaben je Aufruf:**
  - `<karte>[_<stufe>]_bericht.txt` (auch auf stdout) und `_ergebnis.json`
  - `<karte>_<stufe>_roh.pt` und `.json` (Rohdaten mit Zeitreihen, Dichtebildern, Wirbelkarten, Endfeldern)
- **Ohne CUDA** bricht das Programm ab (kein stiller CPU-Ausweg). `--geraet cpu` rechnet mit einem Thread, ist aber fuer
  Messlaeufe etwa 10- bis 30-mal zu langsam.
- **Lokaler Formtest** zum Wiederholen: Abschnitt 0.1.

## 6. Latten (Vorschlag, die Leitung entscheidet)

| Karte | L1 kann scheitern | L2 Gegenprobe | L3 Numerik | L4 schon bekannt | L5 Messbezug |
|---|---|---|---|---|---|
| Wellen 8/9 Magnus | ja: Querdrift > 0,15 ohne Zirkulation widerlegt V-M1; Symmetrie verbietet sie nicht | ja: m -> -m, m = 0, lam = 0, Medium allein, Ruhe | geplant, 3 Laeufe | ja: Kutta-Joukowski, Kelvin, Magnus nur mit Zirkulation (Suprafluid-Lehrbuch), Moeller-Versatz | schwach: Mitnahme = mitbewegte Masse (Blasen, Suprafluid), Bezug zu "kreuzen" |
| Wellen 4 Kielwasser | ja: Winkel 6 Grad, kein Muster unter c_s | ja: lam = 0, Medium allein, u unter c_s | geplant, 3 Laeufe | ja: Machkegel, Bogoliubov-Cherenkov (Carusotto 2006) | nein (BEC-Experimente nur Analogie) |
| Wellen 18 Wirbelstrasse | ja: Schwelle, Vorzeichen je Seite, Frequenz steigt | ja: lam = 0, u = 0,4 | geplant, 2 Laeufe | ja: Frisch-Pomeau-Rica, Sasaki 2010, Kwon 2016 | nein |
| Wellen 14 Brechung | ja: P1 mit 1 Grad und 2 %, Reflexion | ja: ohne Stufe, lam = 0, senkrecht | geplant, 3 Laeufe | teilweise: korpuskulare Brechung ableitbar; neu sind M_eff(C) und die mitgefuehrte Masse | nein |
| Wellen 15 Linse | ja (Brennweite vorab rechenbar) | - | - | ja (Kugellinse) | nein; Papier |
| Wellen 17 KH | ja | - | - | ja | nein; Papier, parken |

**Vorschlag:**
- Magnus und Brechung zuerst: Sie koennen am klarsten scheitern.
- Kielwasser als Bekannt-Probe des Zwei-Feld-Codes (L4).
- Wirbel ist explorativ.
- Linse erst nach Brechung, KH parken.

## 7. Grenzen

- **Nur Dichtekopplung:** Mit eps (Ladungsaustausch) koppeln die Phasen von psi und chi. Dann koennte die Windung von psi
  Zirkulation ins Medium tragen. Weil die Frequenzen (0,77 gegen 1,05) nicht passen, ist das nicht resonant. Das ist
  eine eigene Karte.
- **Periodische Box:** Die Stroemung durch Nachbarbilder (Abstand 76,8) blockiert etwas: Das Dipolfeld faellt wie
  R^2/r^2, bei m = 1 etwa 3 %. Die Randschicht nimmt Stoerungen auf, aber nicht perfekt.
- **Halter** (kielwasser, wirbel): Er veraendert den Ball leicht (innen hoechstens a r^2, etwa 0,02 bis 0,05) und hat
  eine Eigenschwingung.
- **Relaxation:** Ist der m = 1-Ball ein Sattel (Teilungsmode), kann der Gradientenfluss dorthin laufen. Der Waechter
  stoppt bei c2 > 1e-2.
- **Heilungslaenge:** etwa 3,2, vergleichbar mit den Baellen (R 2 bis 7). Die Hindernisse sind "klein und weich"; die
  Literaturschwellen fuer grosse harte Scheiben gelten nur ungefaehr.
- **Kielwasser** nur im Ruhesystem des Balls gerechnet. Die Gleichwertigkeit mit "Ball bewegt" ist Lorentz-Invarianz
  (Codeprobe bei M1 in 1D).
- **Literatur** nur aus dem Gedaechtnis [L], nicht nachgeschlagen.

## Einfach gesagt

Wir setzen einen Q-Ball in ein duennes, stabiles "Wasser" aus einem zweiten Feld und lassen es an ihm vorbeistroemen. Der
drehende Ball bekommt vermutlich keinen Magnus-Seitenschub, weil das Wasser seine Drehung gar nicht spuert: Es sieht nur,
wo der Ball ist, nicht wie er sich dreht. Beim Anlaufen der Stroemung wird er aber ein Stueck mitgenommen und rollt dann
gleichmaessig weiter, wie eine Blase im Wasser; so erklaere ich auch den 1D-Befund von gestern. Ist die Stroemung
schneller als der Schall im Wasser, erwarten wir hinter dem Ball ein V wie beim Ueberschallknall, dessen Winkel mit der
Geschwindigkeit enger wird. Ausserdem pruefen wir, ob der Ball Wirbel abloest und an einer Dichtestufe wie ein
Lichtstrahl gebrochen wird.

Ende der Bearbeitung: 2026-09-30 03:33:48 CEST (gemessen mit date). Beginn 2026-09-30 02:53:36 CEST.
