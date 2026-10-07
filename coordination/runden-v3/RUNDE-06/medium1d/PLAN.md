# Runde 6, Agent M1: Medium-Karten in 1D (Wellen 3, 5, 6, 7, 11; Bio 2, 21; Chemie 9)

Bearbeiter: Anthropic-Agent M1 (Opus), Auftrag ../AUFTRAG-MEDIUM-UND-2D-B.md, Abschnitt "Agent M1". Beginn 2026-09-30
02:53:26 CEST (gemessen), Ende in der letzten Zeile. Explorativ. Status: Code geschrieben, lokaler Rauchtest (CPU,
1 Thread, nice 19) fehlerfrei; **Messlaeufe nicht gerechnet**. Alle Vorhersagen stehen vor jeder Messung fest.

## Kurzfassung

- **Code:** medium1d.py (PyTorch, float64/complex128, `--geraet cuda|cpu`), ein Unterbefehl je Karte plus `rauch`.
  Jeder Unterbefehl rechnet alle Laeufe als Stapel, grob (dx 0,1, dt 0,05) und fein (dx 0,05, dt 0,025), sichert die
  Rohdaten nach jeder Stufe (`medium1d_<test>_<stufe>_roh.pt`) und wertet L3 selbst aus.
- **Grundlage:** r5d.py (Medium-Rolle kc = 0, g4 = 0,5, lam; eps fuer Austausch), Anker-Profil und Verlet unveraendert.
  Neu: periodische Box [-300, 300) (Laenge 600, doppelt so lang wie r5d kreuzen), glatte Rampen, Eichfeld zum
  Hochfahren der Stroemung, Falle fuer den Ball, Kraftmessung, Schallpaket, aeusseres Potential des Mediums.
- **Wichtigste Aenderung gegen r5d kreuzen:** Einschwingen und stationaere Kraft sind getrennt (Abschnitt 1).
- **Kernvorhersagen:**
  - Unter einer Schwelle v_c < c_s ist die stationaere Kraft null; v_c/c_s ~ 0,55 bei C0 = 0,1 und ~ 0,75 bei C0 = 0,3.
    Der kreuzen-Drift bei 0,48 c_s ist Mitnahme beim Einschalten, keine Kraft.
  - Die Bremskraft hat ueber der Schwelle ein Maximum (u ~ 0,25 bis 0,45) und faellt bis u = 0,9 unter 10 % davon.
  - Windschatten umgekehrt: Der hintere Ball spuert die volle Kraft, der vordere schwankt mit dem Abstand.
  - Fahrtwind: bewegter und ruhender Ball geben dieselbe Kraft; der Galilei-Aufbau nicht.
  - Stokes: Drift ~ a^2, wenn die Welle von weit her kommt; ~ a, wenn sie beim Start schon auf dem Ball liegt.
  - Osmose und Massenwirkung: Ladung fliesst vom hoeheren zum niedrigeren omega, isoton bei mu_Medium = omega_Ball; das
    Gleichgewicht ist instabil (Reifung statt Massenwirkungsgesetz).
  - Nische: Der Ball laeuft zur duennsten (lam > 0) bzw. dichtesten (lam < 0) Stelle und schwingt dort ungedaempft; nur
    ueber v_c wird er gebremst und bleibt liegen.

## 1. Modell und Einschwingen

### 1.1 Modell

- V = U(S) + mc2 C + g4 C^2 + lam S C + eps (conj(psi) chi + c.c.) + Phi(x, t) S + W(x, t) C, U(S) = S - S^2 + S^3/2.
- **Medium:** chi = sqrt(C0) exp(-i omega0 t), omega0^2 = mc2 + 2 g4 C0; c_s^2 = g/(2 omega0^2 + g), g = 2 g4 C0.
  - C0 = 0,1: c_s = 0,2085; C0 = 0,3: c_s = 0,3216 (mc2 = 1, g4 = 0,5).
  - Heillaenge 1/sqrt(2 g) = 2,24 bzw. 1,29; der Ball (omega^2 = 0,7, FWHM 3,56) ist also mittelgross.
- **Ball:** omega^2 = 0,7: Q = 2,441, E = 2,298, N = Int S = 1,459, S_max = 0,368. Delle im Medium (Thomas-Fermi)
  lam S/(2 g4) = 37 % von C0 = 0,1, 12 % von C0 = 0,3.
- **Stroemung:** gleichfoermiges Eichfeld A(t) auf chi (D = d_x - i A). Es beschleunigt das ganze Medium gleichmaessig und
  laesst den Ball unberuehrt. Am Ende ist das Medium eine Ebene Welle mit Impuls K = -A.
  - Lorentz statt Galilei: K = gamma omega0 u bei Ruhdichte C0. So ist der Endzustand genau das Lorentz-geboostete
    ruhende Medium (C ist ein Skalar, Omega^2 - K^2 = omega0^2).
  - Die Ladung bleibt beim Hochfahren erhalten. Die Anfangsdichte ist deshalb so gewaehlt, dass am Ende C = C0 gilt
    (c_start; bei u = 0,9 und C0 = 0,1 startet das Medium mit C = 0,218).
  - Galilei-Aufbau (nur als Gegenbild in fahrtwind): K = omega0 u. Das ist ebenfalls ein gueltiges Medium mit C0, aber
    es stroemt nur mit u/sqrt(1 + u^2).
- **Falle:** Phi = kappa R^2/2 prod_i tanh^2(gamma d_i/R) mit kappa = 0,02 und R = 8.
  - Fallenperiode ~56, Hoechstkraft ~0,09. Beim Ziehen (fahrtwind B) ist die Falle Lorentz-kontrahiert (gamma der
    momentanen Fallengeschwindigkeit).
  - Die Falle verformt den Ball etwas; alle Laeufe einer Karte haben dieselbe Falle.
- **Kraftmessung:** F_med = -lam Int_{Fenster} S dC/dx dx, also die Kraft des Mediums auf den Ball (Fenster +-12 um den
  mitgefuehrten Ball; bei zwei Baellen gehoert jeder Punkt zum naeheren Ball). Zur Kontrolle auch die Fallenkraft F_Falle.
  Im stationaeren Zustand muss F_med + F_Falle = 0 sein (im Mittel).

### 1.2 Einschwingen: wie es gemacht wird

Der Anfangszustand "Ball im Medium" ist keine Loesung des gekoppelten Systems. Statt imaginaerer Zeit nutze ich
adiabatisches Einschalten im echten Zeitschritt. Dafuer braucht es keinen zweiten Loeser, und es funktioniert in jedem
Bezugssystem.

1. **t = 0:** ruhender Ball (geschlossenes Profil) und ruhendes, homogenes Medium, lam = eps = kappa = 0. Das ist bis auf
   Gitterfehler eine exakte Loesung.
2. **[0, 100]:** lam, eps und die Falle glatt einschalten (C2-Rampe 6s^5 - 15s^4 + 10s^3). Das Medium graebt seine Delle
   langsam. Alles ist spiegelsymmetrisch, darum kann kein Stoss entstehen. Der schwache Schall laeuft nach beiden
   Seiten weg.
3. **[120, 320]:** die Stroemung glatt hochfahren (Eichfeld). In fahrtwind B statt dessen die Falle mit dem Ball auf -u
   beschleunigen ([120, 370]).
4. **[320, 370]:** abklingen lassen.
5. **[370, T]:** messen. Die Kraft ist ein Hann-gewichtetes Mittel, das Restschwingungen der Falle (Periode ~56) fast
   ganz herausnimmt.
- Rampenzeit gegen Zeitskalen: Dellenaufbau ~ Heillaenge/c_s ~ 11, Fallenperiode 56, Rampe 200 (3,6 Fallenperioden).
- Box 600: Schall, der bis zum Messende von der Delle ausgeht, erreicht den Ball nicht wieder (Umlauf braucht bei
  u + c_s <= 0,93 mindestens 645 Zeiteinheiten).

### 1.3 Woran man sieht, dass es gelungen ist (Kriterien vorab)

- **E1 Plateau:** Die mittlere Kraft der ersten und zweiten Fensterhaelfte stimmt auf 10 % ueberein, bei |F| < F_MIN auf
  F_MIN = 2e-6.
- **E2 Ruhe bei u = 0:** |F| < 1e-10 (Symmetrie); S_max nach dem Einschalten innerhalb 1 % konstant (Spalte "S gehalten").
- **E3 Rampe egal:** landau "langsam" (Rampe 300 statt 200) gibt bei u = 0,10 dieselbe Kraft wie die normale Rampe (auf
  F_MIN).
- **E4 Weg egal:** fahrtwind A (Medium hochgefahren) und B (Ball gezogen) geben dieselbe Kraft. Zwei ganz verschiedene
  Einschwingwege fuehren dann in denselben stationaeren Zustand.
- **E5 Ploetzlich gegen adiabatisch (einschwingen):** Beide freien Baelle bewegen sich nach dem Einschwingen gleichfoermig
  (|a| < 1e-7 unter v_c). Nur die Anfangsgeschwindigkeit unterscheidet sich; das ist der Stoss bzw. die Mitnahme.
- **E6 Einschwing-Spitze:** Die groesste Kraft waehrend der Rampen (Spalte "Einschwing-Spitze") steht neben der
  stationaeren. Unter v_c ist sie > 0 (Mitnahme), stationaer ~0.
- **E7 Medium allein:** Beim hochgefahrenen Medium ist C raeumlich exakt gleich (Spanne 0; alle Punkte rechnen dasselbe)
  und am Ende C0 auf 1e-3 (Adiabatik der Amplitudenmode, Frequenz ~2). Beim ploetzlichen Medium bleibt C auf 1e-9
  konstant (exakte Gitterloesung wie r5d).

## 2. Karten: Aufbau, Vorhersage, Gegenprobe

Alle Laeufe haben die periodische Box, sind grob und fein gerechnet und nutzen den Ball omega^2 = 0,7 bei x = 0, sofern
nicht anders angegeben. Mediumparameter C0 = 0,1, g4 = 0,5, mc2 = 1, lam = 0,1.

### 2.1 landau (Wellen 5): stationaere Kraft gegen u, zwei Dichten

- **Aufbau:** Ball in der Falle, Medium adiabatisch auf u, T = 570, Messfenster [370, 570].
  - C0 = 0,1: u = 0 / 0,05 / 0,08 / 0,10 / 0,12 / 0,14 / 0,16 / 0,18 / 0,21 / 0,25 / 0,30 / 0,40
  - C0 = 0,3: u = 0,10 / 0,15 / 0,19 / 0,23 / 0,27 / 0,31 / 0,36 / 0,45
  - Kontrollen: Spiegel u = -0,25; lam = 0 bei 0,25; Medium allein bei 0,25; langsame Rampe bei 0,10
  - 24 Laeufe
- **Schwelle im Code:** u_c liegt zwischen dem groessten u mit |F| < F_MIN = 2e-6 und dem kleinsten u mit |F| >= F_MIN.
- **Papierbild:**
  - Landau fuer ein schwaches Hindernis: v_c = c_s.
  - Fuer ein breites Hindernis (hydraulische Grenze, nichtrelativistisch): Die Stroemung wird in der Delle lokal
    schallschnell. Mit x = Dichte in der Delle/C0, M = u/c_s und beta = Tiefe der ruhenden Delle gilt Bernoulli
    1 + M^2/2 = 3x/2 + beta und Fluss x^3 = M^2. Daraus v_c = 0,30 c_s bei C0 = 0,1 (beta = 0,37) und 0,58 c_s bei
    C0 = 0,3 (beta = 0,12).
  - Unser Ball ist so breit wie 1,6 bzw. 2,8 Heillaengen, liegt also dazwischen.
  - Hinweis aus r5d kreuzen (Vorwissen, kein Blindtest): Bei 0,48 c_s lief der Ball mit a = 4e-6 fast gleichfoermig, bei
    0,76 c_s beschleunigte er zehnmal staerker.
- **Vorhersagen:**
  - **V5a:** Unter der Schwelle ist die stationaere Kraft null: |F| < F_MIN bei u <= 0,05 (C0 = 0,1) und u <= 0,15
    (C0 = 0,3).
  - **V5b:** u_c/c_s = 0,55 +- 0,2 bei C0 = 0,1 (u_c = 0,07 bis 0,16) und 0,75 +- 0,15 bei C0 = 0,3 (u_c = 0,19 bis
    0,29). Die Schwelle waechst mit C0 staerker als c_s (Faktor 1,5 bis 2,5 statt 1,54), weil die Delle relativ zum
    Medium flacher wird.
  - **V5c:** Ueber der Schwelle ist F > 0 in Stroemungsrichtung, bei u = 0,30 und C0 = 0,1 zwischen 5e-4 und 2e-3 (aus
    r5d kreuzen n = 16: E a ~ 1e-3). Zwischen v_c und c_s schwankt F stark (Dunkelsolitonen, F_std gross).
  - **V5d (unsicherste, beste Schaetzung):** u = 0,10 (0,48 c_s): |F| < F_MIN. Der kreuzen-Drift war dann keine
    Kraft (Klaerung in 2.3). Liegt u_c doch unter 0,10, war er zum Teil eine echte Kraft.
- **Gegenproben:** lam = 0: F = 0 exakt; Spiegel: F(-u) = -F(u) auf Rundung; Medium allein: E7; langsame Rampe: E3.
- **L1:** Findet der Code bei 0,48 c_s eine stationaere Kraft >= F_MIN, oder liegt u_c/c_s bei C0 = 0,3 nicht hoeher
  als bei 0,1, ist die Vorhersage verfehlt.

### 2.2 gleiten (Wellen 6): Kraft bis u = 0,9

- **Aufbau:** wie landau, C0 = 0,1. lam = 0,1: u = 0,25 / 0,30 / 0,35 / 0,40 / 0,50 / 0,60 / 0,70 / 0,80 / 0,90;
  lam = 0,3: u = 0,30 / 0,50 / 0,70 / 0,90; Spiegel u = -0,50. 14 Laeufe.
- **Papierbild:**
  - Ueber c_s strahlt der Ball eine stehende Bugwelle ab. Ihre Wellenzahl im Ballsystem ist k' (Code: kielwelle); sie
    waechst mit u (0,64 bei u = 0,35; 4,3 bei u = 0,9).
  - Die Kraft geht in erster Naeherung mit |S^(k')|^2. Fuer ein glattes Profil der Breite ~2 faellt das bei grossem k'
    exponentiell. Also steigt F ueber der Schwelle, hat ein Maximum und faellt wieder.
  - [L, aus dem Gedaechtnis] Astrakharchik und Pitaevskii 2004 sowie Pavloff 2002: Bremskraft auf ein Hindernis in einem
    1D-Kondensat.
- **Vorhersagen:**
  - **V6a:** Maximum der Kraft bei u = 0,25 bis 0,45 (lam = 0,1).
  - **V6b:** F(0,9)/F_max < 0,1 bei lam = 0,1 und < 0,2 bei lam = 0,3. "Gleiten" gibt es also, als Abfall ueber der
    Rumpfgeschwindigkeit.
  - **V6c:** Das Maximum bei lam = 0,3 liegt nicht unter dem bei lam = 0,1 (staerkeres Hindernis, mehr nichtlineare
    Abstrahlung bei mittlerem u).
- **Gegenprobe:** Spiegel; L3 je Lauf.
- **L1:** F monoton bis 0,9 oder F(0,9)/F_max > 0,3 widerlegt V6a/b.

### 2.3 einschwingen (Klaerung des kreuzen-Befunds)

- **Aufbau:** freier Ball (ohne Falle), C0 = 0,1, lam = 0,1. u = 0,0994 / 0,1578 / 0,3044, also genau die r5d-kreuzen-Werte
  n = 5 / 8 / 16. In der doppelt langen Box sind das n = 10 / 16 / 32.
  - "ploetzlich": ungekleideter Ball in der stroemenden Ebenen Welle, lam ab t = 0 (Wiederholung von r5d kreuzen)
  - "adiabatisch": Einschwingen nach 1.2, Ball frei
  - Kontrollen: ploetzlich lam = 0; Medium allein (n = 32); ploetzlich, aber in der Falle gehalten (n = 10)
  - 9 Laeufe, T = 570
- **Papierbild:** Mitnahme. Beim Hochfahren schiebt das beschleunigte Medium den Ball an ("Auftrieb" der fehlenden
  Mediummasse in der Delle, 2 omega0^2 |Int dC| ~ 0,32 gegen E = 2,3). Der Ball erreicht v_b ~ 0,14 u und rollt dann
  kraeftefrei weiter.
- **Vorhersagen:**
  - **V-E1 (Reproduktion):** ploetzlich n = 10 gibt x(300) = 1,27 +- 0,05 und v[100, 300] = 5,2e-3 +- 5 % wie r5d.
  - **V-E2:** adiabatisch u = 0,0994: nach dem Hochfahren gleichfoermig, |a| < 1e-7 auf [370, 570] (kreuzen: 4e-6), und
    v_b = (0,07 bis 0,21) u.
  - **V-E3:** ploetzlich u = 0,0994 spaet ebenfalls |a| < 1e-6 (der Stoss ist abgeklungen); ploetzlich gehalten:
    F_med spaet < F_MIN.
  - **V-E4:** u = 0,3044 (1,46 c_s): a > 1e-4 in beiden Faellen (echte Kraft).
  - **V-E5:** u = 0,1578 (0,76 c_s) folgt landau: ist dort u_c < 0,16, beschleunigt auch der adiabatische Ball.
- **Gegenproben:** lam = 0 (v = 0 exakt), Medium allein (C konstant auf 1e-9).

### 2.4 windschatten (Wellen 7)

- **Aufbau:** zwei Baelle in eigenen Fallen bei -d/2 (vorn, stromauf) und +d/2 (hinten), Stroemung in +x.
  - d = 6 / 10 / 16 / 24 und u = 0 / 0,05 / 0,35 (0,24 bzw. 1,68 c_s), dazu je ein einzelner Ball: 15 Laeufe
  - dF = F(u) - F(u = 0, gleiches d); damit fallen die statischen Kraefte (Mediums-Anziehung der Dellen, direkte
    psi-Ueberlappung) heraus
- **Papierbild:**
  - Bei der Bogoliubov-Dispersion laeuft die Gruppengeschwindigkeit der Bugwelle schneller als der Ball. Die stehende
    Welle liegt deshalb **stromauf**; stromab ist das Medium ungestoert (nur abklingende Auslaeufer der Delle).
  - Also sieht der hintere Ball ungestoertes Medium. Der vordere steht in der Bugwelle des hinteren; seine Kraft haengt
    mit cos(k' d) vom Abstand ab (k' = 0,644, Wellenlaenge 9,8).
- **Vorhersagen:**
  - **V7a:** u = 0,05: alle dF < F_MIN (keine Bremsung, also auch kein Windschatten).
  - **V7b:** u = 0,35, d >= 10: hinten/allein = 1,00 +- 0,15 (kein Windschatten fuer den hinteren).
  - **V7c:** vorn/allein weicht bei mindestens zwei der vier Abstaende um mehr als 0,2 von 1 ab und folgt dem Vorzeichen
    von cos(k' d) oder seinem Gegenteil (Korrelation |r| > 0,7; das Vorzeichen lege ich nicht fest).
  - Kurz: umgekehrter Windschatten, der Vordermann spuert den Hintermann.
- **L1:** hinten/allein < 0,7 bei d >= 10 waere echter Windschatten und widerspraeche dem Bild.

### 2.5 fahrtwind (Wellen 11): Lorentz-Codeprobe

- **Aufbau:** u = 0,05 / 0,35 / 0,60, je drei Laeufe, dazu Spiegel A(-0,35): 10 Laeufe, T = 620, Fenster [420, 620].
  - A: Ball ruht in der Falle, Medium adiabatisch auf u (Lorentz-Impuls K = gamma omega0 u, C = C0).
  - B: Medium ruht (C0), die Falle zieht den gekleideten Ball glatt auf -u ([120, 370]) und ist Lorentz-kontrahiert.
    Die Laengskraft ist Lorentz-invariant (F = Int f'^1 dx', Kraftdichte transformiert mit gamma, Laenge mit 1/gamma).
    Im Ballsystem ist B also dasselbe wie A.
  - C: wie A, aber mit Galilei-Impuls K = omega0 u; das Medium stroemt dann nur mit u/sqrt(1 + u^2) (0,330 bzw. 0,514).
- **Vorhersagen:**
  - **V11a:** |F_B - F_A| <= max(0,05 |F_A|, 5e-7) bei allen drei u (Codeprobe und zugleich E4).
  - **V11b:** F_C - F_A ist bei 0,35 und 0,60 deutlich (> 10 % von F_A) und hat das Vorzeichen der Steigung von F(u)
    aus gleiten zwischen u_G und u. Bei 0,05 sind alle ~0.
- **Gegenprobe:** Spiegel F_A(-0,35) = -F_A(0,35).

### 2.6 stokes (Wellen 3)

- **Aufbau:** freier, gekleideter Ball bei 0.
  - Bei t = 150 wird ein Schallpaket eingesetzt: linearisierte Bogoliubov-Welle mit k = 0,42 (Wellenlaenge 15, gut
    4 Ballbreiten), Om = 0,116 (Periode 54), v_g = 0,39, Gauss-Huelle sigma = 25, Mitte bei x = -130, laeuft nach +x.
  - Relative Dichteamplitude a = 0,05 / 0,1 / 0,2.
  - Kontrollen: ohne Welle; Spiegel (von +130 nach -x, a = 0,2); lam = 0; Medium allein.
  - Dazu die Welle **auf dem Ball** (Mitte x = 0) mit a = 0,1 und 0,2 als Nachbau des Runde-4-Befunds.
  - 9 Laeufe, T = 900. Das Paket hat den Ball bis t ~ 680 ganz passiert; v_Ende wird auf den letzten 150 gemessen.
- **Papierbild:** Kommt die Welle von weit her, mittelt sich die lineare Antwort (Hin- und Herschaukeln) weg. Uebrig
  bleiben Strahlungsdruck (teilweise Reflexion an der Delle) und die mittlere Stroemung des Pakets. Beides geht ~ a^2.
- **Vorhersagen:**
  - **V3a:** Exponent aus v_Ende und aus x nach Durchgang (a = 0,2 gegen 0,05): 2,0 +- 0,3; Richtung +x.
  - **V3b:** Welle auf dem Ball: Verschiebung ~ a (Verhaeltnis a = 0,2/0,1 zwischen 1,7 und 2,3). Das erklaert Runde 4.
  - **V3c:** Spiegel kehrt das Vorzeichen um; lam = 0 gibt 0 exakt.

### 2.7 osmose (Bio 2)

- **Aufbau:** Medium mit mc2 = 0,5, also mu_Medium^2 = 0,5 + C (mu = omega0). Ball omega^2 = 0,7, lam = 0 (reiner Austausch).
  - eps = 0,01 glatt eingeschaltet [0, 100]. Das Vakuum ist stabil (mc2 >= eps^2).
  - C = 0 (leeres chi-Vakuum) / 0,10 / 0,15 / 0,20 / 0,25 / 0,30 / 0,35
  - eps = 0,02 bei C = 0,10 und 0,30; Kontrollen eps = 0 und Medium allein
  - 11 Laeufe, T = 800
  - Rate = d/dt (Ladung psi + chi im Ballfenster minus Hintergrund) auf [300, 800]
  - C ist hoechstens 0,35, damit mu weit unter der psi-Masse 1 bleibt; sonst wird die psi-Beimischung des Mediums gross
    (Rauchtest mit C = 0,45: Ballfrequenz verfaelscht).
- **Papierbild:**
  - Ueber eps wandelt ein psi-Quant (Energie omega_Ball) in ein Kondensatquant (mu) plus ein Phonon (omega_Ball - mu) um.
    Das geht nur, wenn die Phonon-Energie positiv ist. Ladung fliesst also vom hoeheren zum niedrigeren
    chemischen Potential, und das Medium traegt die Differenz als Schall weg.
  - Isoton ist mu = omega_Ball, naiv C = 0,7 - 0,5 = 0,20.
  - Ohne Medium (C = 0) strahlt der Ball freie chi-Wellen ab (chi-Masse 0,707 < omega = 0,837). Rate
    -eps^2 ft(k)^2/k mit k = sqrt(omega^2 - mc2); der Code druckt den Wert.
- **Vorhersagen:**
  - **V2a:** Vorzeichenwechsel der Rate zwischen C = 0,15 und 0,25 (gemessen im Code), mit C_iso = 0,20 +- 0,03. Darunter
    verliert der Ball Ladung, darueber waechst er.
  - **V2b:** C = 0: Rate/Formel zwischen 0,67 und 1,5.
  - **V2c:** Rate(eps = 0,02)/Rate(eps = 0,01) zwischen 3 und 5 bei C = 0,10 und 0,30.
  - **V2d:** Das isotone Gleichgewicht ist instabil: Ein wachsender Ball senkt sein omega und waechst weiter (dQ/domega
    < 0). Es gibt also einen isotonen Punkt, aber kein stabiles "Zellvolumen".
- **Gegenprobe:** eps = 0: Rate < 1e-7 (nur Messrauschen); Q_psi + Q_chi bleibt auf Rundung erhalten.

### 2.8 massenwirkung (Chemie 9)

- **Aufbau:** drei Baelle omega^2 = 0,6 / 0,7 / 0,8 (Q = 3,16 / 2,44 / 1,89) bei -100 / 0 / 100, Medium wie osmose.
  - C = 0,1 / 0,2 / 0,3: mu^2 = 0,6 / 0,7 / 0,8, bei jeder Dichte ist genau ein Ball isoton
  - Kontrollen: eps = 0 bei C = 0,2; C = 0 (Vakuum)
  - 5 Laeufe, T = 800
- **Vorhersagen:**
  - **VC9a:** Bei allen 6 nicht-isotonen Baellen (|mu - omega| > 0,01) hat die Rate das Vorzeichen von mu - omega.
    Beispiel C = 0,2: der grosse Ball waechst, der kleine schrumpft.
  - **VC9b:** Kein Massenwirkungsgesetz mit stabilem Verhaeltnis, sondern Reifung: Der Abstand der Ladungen waechst mit
    der Zeit, bei C = 0,2 auseinander.
  - **VC9c:** Vakuum: alle drei verlieren Ladung.

### 2.9 nische (Bio 21)

- **Aufbau:** Medium C0 = 0,15 mit aeusserem W, glatt eingeschaltet [0, 150]. Im Thomas-Fermi-Bild wird daraus
  C = 0,15 + dC sin(2 pi x/lambda); die Delle liegt bei -lambda/4, der Buckel bei +lambda/4.
  - Ball in der Falle bei x = 0 (Nulldurchgang), Falle geloest auf [200, 250], danach frei bis T = 1300.
  - Laeufe: lam = +0,1 sanft (dC = 0,02, lambda = 30); lam = -0,1 sanft; lam = +0,2 steil (dC = 0,05, lambda = 60);
    lam = 0; Spiegel (dC -> -dC); Medium allein. 6 Laeufe.
- **Papierbild:**
  - Die Energie des Balls ist lam N C(x); er laeuft also zur duennsten Stelle (lam > 0) bzw. zur dichtesten (lam < 0).
  - Harmonisch T0 = 2 pi/sqrt(|lam| N dC k^2/E) = 842 (sanft) bzw. 753 (steil). Der Start im Nulldurchgang ist ein Pendel
    mit 90 Grad Ausschlag: Periode x 1,18.
  - Hoechstgeschwindigkeit sanft ~0,06: unter der hydraulischen Schwelle 0,09 an der Delle, also keine Reibung. Steil
    ~0,13, wobei lam = 0,2 die Delle fast leert (v_c klein): Bremsung durch Solitonen.
- **Vorhersagen:**
  - **V21a:** lam = +0,1 sanft: Umkehr bei x = -15 +- 2, Halbperiode 500 +- 150, zweiter Ausschlag >= 0,9 x der erste.
    Er bleibt nicht stehen; die Nische ist nur die Mitte der Schwingung.
  - **V21b:** lam = -0,1 sanft: dasselbe Bild zum Buckel (+x); Spiegel: nach +x.
  - **V21c:** lam = +0,2 steil: gedaempft, zweiter Ausschlag <= 0,7 x der erste. Der Ball bleibt bei der Delle x = -15
    +- 5 liegen. Das ist unsicher (haengt an v_c, siehe landau).
  - **V21d:** lam = 0: Ball bleibt auf 1e-6; Medium allein: Profil bleibt nach dem Einschalten stehen.

## 3. Aufloesung (L3) und Latten (Vorschlag, die Leitung entscheidet)

- **L3 im Code:** Jede Hauptkenngroesse wird grob (dx 0,1, dt 0,05) und fein (dx 0,05, dt 0,025) gerechnet. Bestanden,
  wenn der Effekt mindestens fuenfmal so gross ist wie die Aenderung grob -> fein (wie r5d).
  - landau: F je Lauf und u_c je Dichte
  - gleiten: F
  - einschwingen: v und a spaet
  - windschatten: dF vorn und hinten bei u = 0,35
  - fahrtwind: F_A
  - stokes: v_Ende und x nach Durchgang
  - osmose, massenwirkung: Rate
  - nische: x_min, x_max
  - Bei Effekt ~0 (unter der Schwelle) ist L3 nicht bestehbar; das ist dort das Ergebnis, kein Mangel.
- Mit `--stufen grob|fein` laesst sich ein Aufruf in zwei teilen; L3 dann aus beiden Berichten von Hand.

| Latte | landau / gleiten | einschwingen | windschatten | fahrtwind | stokes | osmose | massenwirkung | nische |
|---|---|---|---|---|---|---|---|---|
| L1 kann scheitern | ja: Kraft bei 0,48 c_s; u_c/c_s faellt mit C0; kein Maximum | ja: adiabatisch a >= 1e-7 unter v_c | ja: hinten/allein < 0,7 | ja: F_B != F_A | ja: Exponent != 2 | ja: kein Vorzeichenwechsel, C_iso weit von 0,2 | ja: Vorzeichen falsch | ja: keine Bewegung zur Delle; Daempfung bei sanft |
| L2 Gegenprobe | lam = 0, Spiegel, Medium allein, langsame Rampe | lam = 0, Medium allein, gehalten | u = 0, einzelner Ball | Spiegel, Galilei-Gegenbild | ohne Welle, lam = 0, Spiegel, Medium allein | eps = 0, Medium allein | eps = 0, Vakuum | lam = 0, Spiegel, Medium allein |
| L3 Numerik | im Code | im Code | im Code | im Code | im Code | im Code | im Code | im Code |
| L4 bekannt | ja: Landau; 1D-Hindernis (Hakim 1997, Pavloff 2002, Astrakharchik/Pitaevskii 2004) [L] | teilweise: Mitnahme, "Auftrieb" im beschleunigten Superfluid | teilweise: Zwei-Hindernis-Interferenz in 1D-Stroemungen [L] | ja: Lorentz-Invarianz | teilweise: Strahlungsdruck von Phononen auf Dunkelsolitonen/Verunreinigungen [L] | teilweise: Verdampfung und Einfang bei Q-Baellen; Kondensat als Bad | ja: Ostwald-Reifung; Q-Ball-Thermodynamik | teilweise: Soliton im Dichtegefaelle (Busch-Anglin 2000 fuer Dunkelsolitonen) [L] |
| L5 Messbezug | nein (Analogon: Kritische Geschwindigkeit in BEC-Experimenten) | nein | nein | nein | nein | nein | nein | nein |

Literatur [L] aus dem Gedaechtnis, nicht nachgelesen. Vorab ableitbar und deshalb nur Kontrollen: F = 0 bei lam = 0
und bei u = 0; Spiegelsymmetrie; Q_psi + Q_chi erhalten; C_iso naiv = 0,20. Schwellen (F_MIN, 10 %, 0,15, 0,01) stehen
fest und werden nach dem Lauf nicht gelockert.

## 4. Aufrufe (Leitung, .69, ueber kleintest.sh)

Remote-Ordner /home/fmh/fmhc-physics-remote/runde6-medium1d/ mit medium1d.py darin (nur torch noetig, schreibt nur in
--out).
- Alle Messlaeufe auf den P4000-Spuren. CPU-Spuren sind fuer die Messlaeufe zu langsam: lokal gemessen 250 bis 300 ns je
  Punkt und Schritt auf einem Kern, das ergaebe 8 bis 20 min je Unterbefehl.
- `--geraet cpu` setzt einen Thread.

**Rauchtest zuerst** (alle neun, Zeiten x 0,05, beide Stufen):

```
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m1-rauch medium1d.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/rauch-cuda
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu m1-rauchcpu medium1d.py rauch --geraet cpu --faktor 0.02 --stufen grob --out /home/fmh/fmhc-physics-remote/runde6-medium1d/rauch-cpu
```

- **Hochrechnung:** jede gedruckte Stufenzeit des CUDA-Rauchtests x 20, plus 15 s Start.
- Ergibt ein Unterbefehl mehr als 9 min, ihn mit `--stufen grob` und `--stufen fein` in zwei Aufrufe mit getrennten
  --out-Ordnern teilen (Rohdaten je Stufe bleiben ohnehin erhalten).

**Messlaeufe** (nur nach rc = 0 im Rauchtest; Spurvorschlag, jede P4000-Spur geht):

```
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m1-landau medium1d.py landau --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/landau
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m1-einschw medium1d.py einschwingen --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/einschwingen
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m1-fahrtwind medium1d.py fahrtwind --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/fahrtwind
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m1-osmose medium1d.py osmose --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/osmose
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a m1-nische medium1d.py nische --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/nische
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b m1-gleiten medium1d.py gleiten --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/gleiten
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b m1-windsch medium1d.py windschatten --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/windschatten
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b m1-stokes medium1d.py stokes --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/stokes
cd /home/fmh/fmhc-physics-remote/runde6-medium1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b m1-massenw medium1d.py massenwirkung --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-medium1d/massenwirkung
```

- Ist p4000b gesperrt (WM-1-MB laeuft), laufen alle nacheinander auf p4000a.
- Reihenfolge nach Nutzen: landau und einschwingen zuerst (Klaerung kreuzen), dann fahrtwind (Codeprobe), dann der Rest.

## 5. Erwartete Laufzeit (Schaetzung, nicht gemessen auf der .69)

- **Grundlage:**
  - r5d auf der P4000: 2,2 bis 2,6 ms je Schritt bei 9 x 3000 bis 6000 Punkten (Kernelstarts begrenzen).
  - medium1d hat etwa 1,5-mal so viele Operationen je Schritt (Falle, Eichfeld, Messung mit Ballfenstern).
  - Schaetzung 3 bis 5 ms je Schritt.
- **Lokaler Rauchtest (Laptop-CPU, ein Thread, nice 19):**
  - rauch --faktor 0,02 --stufen grob, alle neun: 33,3 s und 25,2 s
  - massenwirkung beide Stufen: 6,2 s
  - nische fein: 12,6 s
  - landau beide Stufen: 45,4 s
  - Alle rc = 0, keine Fehler. Die Zahlen darin gelten nicht (Rampen von 2 bis 4 Zeiteinheiten sind nicht adiabatisch).

| Unterbefehl | Laeufe | T | Schritte grob + fein | P4000 (geschaetzt) |
|---|---|---|---|---|
| rauch | alle | x 0,05 | 5 % von allem | 1 bis 2 min |
| landau | 24 | 570 | 11400 + 22800 | 2 bis 3,5 min |
| gleiten | 14 | 570 | 11400 + 22800 | 1,5 bis 3 min |
| einschwingen | 9 | 570 | 11400 + 22800 | 1,5 bis 3 min |
| windschatten | 15 (2 Baelle) | 570 | 11400 + 22800 | 2 bis 4 min |
| fahrtwind | 10 | 620 | 12400 + 24800 | 1,5 bis 3 min |
| stokes | 9 | 900 | 18000 + 36000 | 2,5 bis 4,5 min |
| osmose | 11 | 800 | 16000 + 32000 | 2,5 bis 4 min |
| massenwirkung | 5 (3 Baelle) | 800 | 16000 + 32000 | 2,5 bis 4 min |
| nische | 6 | 1300 | 26000 + 52000 | 4 bis 6,5 min |

- Speicher: groesster Stapel 24 x 12000 complex128 = 4,6 MB je Feld; Zeitplaene bis 60 MB; zusammen unter 0,5 GB.
- Torch-Deckel 1,5 GB wie r5d.

## 6. Ausgabedateien (im --out-Ordner)

- `medium1d_<test>_<stufe>_roh.pt`: Rohdaten sofort nach jeder Stufe, also Zeitreihen je Lauf und Ball, x, Endprofile
  S und C, Laufliste und Spaltennamen.
- `medium1d_<unterbefehl>_bericht.txt` und `_ergebnis.json`: Tabellen je Stufe, L3-Zaehlung, Rechenzeiten.
  - Nach jedem Test neu geschrieben.
  - Faellt eine Auswertung aus, steht der Fehlertext im JSON; die Rohdaten bleiben.

## 7. Grenzen

- **Nur 1D:** Die Kraefte sind 1D-Hindernisphysik (keine Umstroemung, kein Wirbelabloesen).
- **Falle:** Sie verformt den Ball leicht (Potential 0,03 am Ballrand gegen Bindung 0,3). Alle Laeufe einer Karte haben
  dieselbe Falle; die freien Baelle (einschwingen, stokes, osmose, massenwirkung, nische) sind unverformt.
- **Adiabatik:** Unter v_c gibt es keinen Energiesatz-Schutz gegen Restschwingungen der Falle. Das Hann-Mittel und E1
  (Haelftenvergleich) fangen das ab, pruefen aber nicht jede denkbare langsame Mode.
- **Bogoliubov-Paket:** Es ist nur in erster Ordnung eine Loesung. Bei a = 0,2 entstehen beim Einsetzen Fehler der Groesse
  a^2 = 4 %, weit vom Ball; sie laufen als Teil der Welle mit.
- **Osmose:** Die isotone Dichte verschiebt sich um O(eps^2) durch die psi-Beimischung des Mediums. Die Frequenzmessung
  am Ballzentrum enthaelt diese Beimischung (Fehler ~1e-4).
- **Vorwissen:** Die Schwellen-Schaetzung (V5b, V5d) kennt das Ergebnis von r5d kreuzen; das ist kein Blindtest.
- **Formeln:** Bernoulli-Schwelle und Vakuumrate sind Naeherungen (nichtrelativistisch bzw. erste Ordnung in eps).

## Einfach gesagt

Wir schieben einen Q-Ball durch eine duenne, ruhige "Suppe" aus einem zweiten Feld und messen, wie stark sie bremst.
Wichtig ist diesmal, dass wir alles ganz langsam einschalten, denn ein ploetzlicher Start gibt dem Ball einen Schubs,
der wie eine Kraft aussieht. Unsere Vorhersage: Unter einer Grenzgeschwindigkeit, etwas unter der Schallgeschwindigkeit
der Suppe, bremst gar nichts; darueber bremst es stark, und bei sehr hohem Tempo wieder weniger. Hinter einem anderen
Ball hat man keinen Windschatten, eher spuert der Vordermann den Hintermann. Tauscht der Ball Stoff mit der Suppe, fliesst
er immer zu dem mit dem niedrigeren "chemischen Druck", wie bei der Osmose.

Ende der ersten Fassung: 2026-09-30 03:46:23 CEST (gemessen mit date vor dem Schreiben dieser Zeile). Code lokal
rauchgetestet (Rohdaten der Rauchtests geloescht, Berichte und Logs in lauf-lokal/); Messlaeufe nicht gerechnet.
