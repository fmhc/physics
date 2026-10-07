# F-5 schwer und leicht: Laufplan fuer F5-1 bis F5-4 (Code r5d_f5.py)

Bearbeiter: Anthropic-Agent R5-D (Opus). Auftrag: Nachricht der Leitung 30.09. 02:39; Karte
RUNDE-06/FINN-IDEE-F5-SCHWER-LEICHT.md. Beginn 2026-09-30 02:39:09 CEST (gemessen), Ende in der letzten Zeile.

**Status:** Code geschrieben, lokal nur Kompilierung und Rauchtest (Finns Freigabe 02:42). Die Messlaeufe sind nicht
gerechnet. Explorativ.

**Wichtig:** Der lokale Rauchtest hat das lineare Eigenwertproblem von F5-1 schon voll gerechnet, denn der
Laufzeitfaktor gilt dort nicht. Diese Zahlen sind deshalb keine Vorhersage mehr, sondern ein vorlaeufiges Ergebnis
(Kern mit nur einer Schiessrunde). Sie stehen getrennt von meiner Handschaetzung vor dem Rauchtest (Abschnitt 2.1).

## Kurzfassung

- **Code:**
  - r5d_f5.py importiert r5d.py (unveraendert; beide Dateien gehoeren in denselben Ordner).
  - Unterbefehle rauch, f51, f52, f53, f54; `--geraet cuda|cpu`; f54 zusaetzlich `--masse 0.3|0.6` zum Teilen auf
    CPU-Spuren.
  - Jeder Unterbefehl rechnet grob (dx 0,1, dt 0,05) und fein (dx 0,05, dt 0,025) und wertet L3 selbst aus.
- **Uebernommen:**
  - aus tests1d.py unveraendert: radiales Schiessen (Test 4) fuer die 3D-Kerne, Gitter, Zeitschritt, Integrator und
    Daempfung;
  - aus r5d.py: Kopplung, Anker und Hilfen.
- **Neu:**
  - 3D radial mit u = r psi und w = r chi: u_tt = u_rr - [U'(S) + ...] u mit S = |u|^2/r^2, Dirichlet bei r = 0 und
    r = 150, Daempfung ab r = 110.
  - lineares Eigenwertproblem -u'' + [lam S + l(l+1)/r^2] u = e u mit omega^2 = m^2 + e (dichte Matrix, eigh).
- **Rauchtest lokal** (Laptop, 1 CPU-Thread, alle vier Karten x 0,05): 60,9 s, keine Fehler.
- **Kernvorhersagen:**
  - Q-Atom: nur ein gebundenes Niveau im stabilen Fenster.
  - Huelle: haelt auf dem stabilen Kern, rettet den instabilen nicht.
  - Mischung: Pendeln nach der Neutrino-Formel; ein stabiler gemischter Ball nur, wenn seine Frequenz unter beiden
    Massen liegt.
  - Unsichtbarer Kern: Reflexion nach Born, bei grossem k unabhaengig vom Vorzeichen von lam; kein Einfang.

## 1. Modell und Wahl der Geometrie

- **Felder:** psi schwer (Masse 1, U(S) = S - S^2 + S^3/2, bildet Q-Baelle), chi leicht (Masse m < 1) mit
  V_chi = m^2 C + g4 C^2 (g4 = 0,1).
- **Kopplungen:** Dichtekopplung C (lam S + lam2 S^2), Mischung eps (conj(psi) chi + c.c.). Die Formeln stehen in
  PLAN.md 1.1 und 1.2.
- **Warum g4 > 0:** Ohne Selbstabstossung ist V bei lam < 0 nach unten unbeschraenkt. Bei festem S > m^2/|lam| gilt
  U(S) + m^2 C + lam S C -> -oo fuer C -> oo. Mit g4 C^2 ist V beschraenkt, weil der Term S^3/2 gewinnt.
- **Warum 3D radial fuer F5-1 und F5-2:**
  - In 1D bindet jede anziehende Mulde mindestens ein Niveau. Die Frage "gibt es Schwebezustaende?" waere dort
    vorab mit ja beantwortet.
  - In 3D gibt es eine Bindungsschwelle, Drehimpuls-Niveaus (s, p, d) und Radien wie beim Atom.
  - Die Huelle sitzt auf einer gekruemmten Wand. Q_min und die VK-Grenze gibt es nur in 3D; in 1D sind alle Baelle
    VK-stabil.
  - Das 3D-Profil kommt aus dem geprueften Schiessen von Test 4 (Virial 1,3e-6, Q_min = 111,84 bei omega^2 = 0,927).
- **Warum 1D fuer F5-3 und F5-4:**
  - Die Mischung ist lokal; die Dimension aendert nur Faktoren, und in 1D ist es billiger.
  - Streuung ist in 1D durch R und T vollstaendig beschrieben und genau als Fluss messbar. 3D braeuchte Partialwellen;
    das ist ein spaeterer Schritt.

## 2. Die vier Karten

Kernzahlen (Test 4, 4 Runden):

| omega^2 | Q | E | S(0) | Bemerkung |
|---|---|---|---|---|
| 0,70 | 473,4 | 428,6 | 1,135 | stabil |
| 0,95 | 115,8 | 117,6 | 0,408 | VK-instabil, E/Q > 1 |

1D-Kern omega^2 = 0,7: Q 2,44, S(0) = 0,3675, Int S dx = 1,46.

### 2.1 F5-1 Q-Atom (3D radial, `f51`)

- **Aufbau:**
  - Kern psi omega^2 = 0,7.
  - Linear: e_n(lam, l) fuer lam = -0,1 bis -1,0 und l = 0, 1, 2; grob dr = 0,1, fein dr = 0,05, Kasten (0, 60].
  - Dynamik (l = 0, T = 300, 8 Laeufe): das unterste Niveau mit Q_chi = 1 bzw. 20 gefuellt, Frequenz aus dem
    Eigenwert.
    - m = 0,3: lam = -0,25; -0,35 (dazu Q = 20)
    - m = 0,6: lam = -0,3; -0,6 (dazu Q = 20)
    - Gegenprobe lam = 0 (Start wie m = 0,6, lam = -0,6)
    - "tief": m = 0,3, lam = -0,8 mit g4 = 1 und nur Keimladung Q = 0,01
      - Nach dem Rauchtest geaendert: Bei Q = 1 und der Hilfsfrequenz 0,03 startete die Wolke schon nahe der Saettigung.
        Das Kriterium "C_max waechst dreifach" waere dann nicht pruefbar.
- **Messung:**
  - Q_psi und Q_chi in r < 40, Radien (rms von |u|^2 bzw. |w|^2), C_max, S bei r = 1.
  - omega_chi und omega_psi aus Phasensteigungen auf [T/2, T]; Bindung m - omega_chi.
  - Klassen: Atom stabil (Q_chi >= 0,9 und Q_psi >= 0,98 gehalten, C_max < 3-fach), zerlaeuft (Q_chi < 0,5),
    Kondensation (C_max >= 3-fach), sonst unklar.
- **Handschaetzung vor dem Rauchtest** (Kasten-Mulde, Radius 3,5, Tiefe |lam| 1,13):
  - Bindungsschwelle |lam| ~ 0,18.
  - Tachyonisch (m^2 + e0 < 0, chi kondensiert statt zu schweben) ab |lam| ~ 0,38 fuer m = 0,3 und ab ~0,70 fuer
    m = 0,6.
  - p-Niveau erst ab |lam| ~ 0,7.
  - Folgerung: Im stabilen Fenster gibt es nur ein Niveau (s).
- **Rauchtest-Zahlen (vorlaeufig, Kern mit 1 Schiessrunde; grob = fein auf 1e-4):**
  - s-Niveau:

| lam | -0,2 | -0,3 | -0,4 | -0,5 | -0,6 | -0,8 | -1,0 |
|---|---|---|---|---|---|---|---|
| e0 | -0,0032 | -0,036 | -0,089 | -0,152 | -0,224 | -0,380 | -0,548 |
| Radius | 13,3 | 5,5 | 4,2 | 3,6 | 3,3 | 2,9 | 2,7 |

  - p-Niveau: gebunden ab lam = -0,8 (e = -0,032). d-Niveau: bis lam = -1,0 keines.
  - Stabiles Fenster:
    - m = 0,3: lam von -0,2 bis -0,4 (omega0^2 = 0,0014 bei -0,4; tachyonisch ab -0,5)
    - m = 0,6: lam bis -0,6; tachyonisch bei -0,8
  - Die Handschaetzung trifft das Bild, die Grenzen liegen etwas anders.
  - **Befund-Kandidat (nach Vollrechnung):** Ein stabiles Q-Atom hat genau ein Schwebeniveau. Bevor ein zweites (p)
    gebunden ist, kondensiert das erste.
- **Vorhersagen fuer die Dynamik (vor dem Lauf):**
  - **V1a:** Die vier Laeufe im stabilen Fenster sind "Atom stabil".
    - omega_chi liegt fuer Q = 1 auf 0,01 bei sqrt(m^2 + e0).
    - Bei Q = 20 liegt omega_chi durch g4 hoeher, um weniger als 0,03.
  - **V1b:** Die Wolke ist nahe der Schwelle groesser als der Kern (R_chi/R_psi > 1,2 bei m = 0,3, lam = -0,25) und
    bei tiefer Bindung hoechstens so gross (R_chi/R_psi <= 1 bei m = 0,6, lam = -0,6).
  - **V1c (Gegenprobe lam = 0):** zerlaeuft, Q_chi gehalten < 0,5.
  - **V1d (tief):** Kondensation. C_max waechst mehr als dreifach und saettigt bei C ~ |lam| S/(2 g4) ~ 0,45; Q_chi
    bleibt erhalten (eps = 0).
- **Vorab ableitbar, keine Messung:** Jedes gebundene Niveau hat omega < m, also E_Bindung = -(m - omega) Q_chi < 0.
  "Gebunden" beantwortet schon das lineare Problem.
- **L3 im Code:** Bindung m - omega_chi und R_chi je Lauf; e0 je gebundenem Niveau grob gegen fein.

### 2.2 F5-2 Huelle auf der Wand (3D radial, `f52`)

- **Aufbau:**
  - Kerne 0,7 (stabil) und 0,95 (VK-instabil), beide mit Faktor 1,01 angestossen.
  - chi Masse 0,6, g4 = 0,1.
  - Wandkopplung -a 4 S (S0 - S)/S0^2 C: Tiefe a bei S = S0/2, null in der Mitte und aussen.
  - Huelle als Gauss-Schale (Breite 1) am Wandradius, Amplitude A, Startfrequenz 0,54.
  - 8 Laeufe, T = 400:

| Kern | Laeufe (a, A) |
|---|---|
| 0,7 | nackt; a = 0, A = 0,2; a = 0,2, A = 0,2; a = 0,4, A = 0,2; a = 0,4, A = 0,05 |
| 0,95 | nackt; a = 0, A = 0,2; a = 0,4, A = 0,2 |

- **Messung:**
  - Q_psi gehalten; groesste relative Aenderung von S(r = 1); omega_psi.
  - Wandanteil von |w|^2 in |r - R_Wand| < 1,5; Q_chi gehalten.
  - Der Code gibt auch das lineare Huellen-Niveau (l = 0) je Kopplung aus.
- **Vorhersagen:**
  - **V2a:** Die Huelle traegt bei a = 0,4 auf dem Kern 0,7: Wandanteil >= 0,5 auf [T/2, T], Q_chi gehalten >= 0,5.
    - a = 0,2 ist knapp gebunden, Wandanteil 0,3 bis 0,6.
    - a = 0 zerlaeuft (Wandanteil < 0,2). Die freie Schale laeuft erst nach innen (Fokussierung, C_max steigt) und
      dann hinaus.
  - **V2b:** Der Kern 0,7 bleibt in allen Laeufen stabil (Q_psi >= 0,98, S-Aenderung < 0,3).
  - **V2c:** Der Kern 0,95 nackt zerfaellt oder wandelt sich innerhalb T = 400 (Q_psi < 0,9 oder S-Aenderung > 0,5).
    Das ist unsicher, weil die Wachstumsrate der VK-Mode unbekannt ist.
  - **V2d:** Die Huelle rettet ihn nicht: "0,95 a = 0,4" hat dieselbe Klasse wie "0,95 nackt" und ein Q_psi auf 0,05
    gleich.
    - Grund: Die Bindungsenergie der Huelle ist ~(m - omega_b) Q_chi ~ 0,1 bis 0,3, verglichen mit E ~ 118 des Kerns.
    - Die VK-Grenze haengt an dQ/domega des Kerns.
- **Q_min selbst ist so nicht messbar:** Das braucht zweifaches Schiessen in (f, h) bei festem omega_chi. Das ist die
  kleinste sinnvolle Form und nicht in dieser Runde. Die Dynamik des Kerns 0,95 ist die Ersatzprobe.
- **Gegenprobe:** a = 0 (Kopplung aus) und die nackten Kerne.
- **L3 im Code:** Wandanteil und Q_psi gehalten je Lauf mit Huelle.

### 2.3 F5-3 Mischung und Oszillation (1D, `f53`)

- **(a) Pakete:**
  - Ruhendes Paket (A = 1e-3, sigma = 10) im leichten Feld chi (frei, Masse m), psi leer.
  - m = 0,6 / 0,9 / 0,97 mit eps = 0,02 und 0,05; Kontrolle eps = 0.
  - P(t) = Q_psi(t)/Q.
- **Formel (Neutrino-Mischung, vorab):** Massenmatrix [[1, eps], [eps, m^2]], sin^2 2theta = 4 eps^2/((1 - m^2)^2 +
  4 eps^2), P(t) = sin^2 2theta sin^2(dM t/2), dM = M+ - M-.

| m, eps | 0,6; 0,02 | 0,6; 0,05 | 0,9; 0,02 | 0,9; 0,05 | 0,97; 0,02 | 0,97; 0,05 |
|---|---|---|---|---|---|---|
| sin^2 2theta | 0,0039 | 0,024 | 0,042 | 0,217 | 0,314 | 0,741 |
| Periode 2 pi/dM | 15,7 | 15,5 | 61,5 | 55,6 | 173 | 106 |

- **V3a:** P_max auf 10 % bei sin^2 2theta, Periode auf 5 % bei der Formel. Die Korrekturen der Ordnung eps^2
  (relativistische Ladungsgewichtung) und die Dephasierung durch die k-Breite (Zeit ~2000 > T) sind klein.
- **V3b:** eps = 0: P = 0.
- **(b) Baelle** (omega^2 = 0,7, omega = 0,837):
  - **V3c (schwerer Ball, leichtes chi m = 0,6 < omega):** Es gibt keinen stabilen gemischten Ball; er verdampft in
    das leichte Feld.
    - Gamma = eps^2 f~(k)^2/k mit k = sqrt(omega^2 - M-^2). Formel im Code: 1,06e-3 (eps = 0,02) und 6,48e-3
      (eps = 0,05), Lebensdauer ~2300 bzw. ~380.
    - Gemessen/Formel zwischen 0,5 und 2; Gamma(0,05)/Gamma(0,02) zwischen 4 und 9 (Formel 6,1).
  - **V3d (schwerer Ball, chi schwerer als omega, m = 1,2):** stabil, |Gamma| < 1e-5; p (schwerer Anteil) ~0,996
    bleibt auf 0,002.
  - **V3e (leichter chi-Ball, Kopie mit m = 0,6, omega = 0,502 < 1):** stabil; p ~0,004 (Beimischung des schweren
    Feldes) bleibt auf 0,002.
  - **V3f:** eps = 0: Gamma = 0, p = 1.
- **Antwort auf die Karte (vorab):** Ein stabiler gemischter Ball mit festem p existiert genau dann, wenn seine
  Frequenz unter beiden Massen liegt.
  - p wird dann von eps/(M^2 - omega^2) des beigemischten Feldes bestimmt, also von einem "gebundenen
    Mischungswinkel", nicht vom freien.
  - Liegt die Frequenz ueber der leichten Masse, ist die Mischung ein Zerfallskanal wie bei Bio 48.
- **Code-Korrektur nach dem Rauchtest:** Die lokale Bekleidung eps f/(U'(S) - m^2) hat bei leichtem chi einen fast
  verschwindenden Nenner (U' - m^2 = 0,11 in der Ballmitte), 8 % der Ladung waeren kuenstlich in chi gelandet. Bei
  m^2 < omega^2 startet chi jetzt leer.
- **L3 im Code:** P_max und Periode; Gamma und p.

### 2.4 F5-4 unsichtbarer Kern (1D, `f54`)

- **Aufbau:**
  - 1D-Kern omega^2 = 0,7, eps = 0 (nur lam).
  - Paket im leichten Feld (A = 1e-3, sigma = 12, von x = -70), m = 0,3 und 0,6, lam = -0,3 und +0,3, Bezug lam = 0.
  - k = 0,25 / 0,4 / 0,6 / 0,9 / 1,3; Fluesse bei x = -+30; T = 400.
  - Zusammen 30 Laeufe.
- **Messung:** T, R, A = 1 - T - R gegen den Einstrom des Bezugslaufs; Einfang = chi-Ladung in |x| < 10 am Ende
  (minus Bezug); Aenderung der Kernhoehe S_max.
- **Papierbild:**
  - Gleichung fuer chi bei fester Frequenz: h'' + k^2 h = lam S(x) h, also Schroedinger mit Potential lam S.
  - Die 1D-Mulde (lam = -0,3) bindet ein Niveau mit kappa ~ 0,22. Es ist stabil fuer beide Massen
    (m^2 - kappa^2 > 0).
  - Born: R = lam^2 S~(2k)^2/(4k^2). Code-Werte: 0,374 / 0,054 / 4,1e-3 / 7,1e-5 / 1,4e-7 fuer k = 0,25 bis 1,3.
  - Born haengt nicht vom Vorzeichen von lam ab und nicht von m.
- **Vorhersagen:**
  - **V4a:** Fuer k >= 0,6: R_mess/R_Born zwischen 0,7 und 1,3, und R(+lam) = R(-lam) auf 20 % (Vorzeichen
    unsichtbar).
  - **V4b:** Bei k = 0,25 unterscheiden sich R(-lam) und R(+lam) um mehr als 30 %; Born ist dort ungueltig
    (R ~ 0,4). Anziehung und Abstossung sind nur bei kleinem k unterscheidbar.
  - **V4c:** Einfang < 1e-4 des Einstroms und |A| < 1e-3. Ein ruhender Kern streut nur elastisch; Einfang in das
    gebundene Niveau braeuchte eine Abgabe von Energie.
  - **V4d, vorab ableitbar:** R(m = 0,3, k) = R(m = 0,6, k); die Gleichung haengt nur von k ab. Nur eine Codeprobe.
    Ebenso lam = 0: R = 0.
- **Bedeutung:** Der schwere Kern ist nur ueber R(k) ~ |S~(2k)|^2 sichtbar, seinen Formfaktor. Aus R(k) liesse sich
  seine Groesse ablesen, wie bei der Elektronenstreuung an Kernen (Hofstadter).
- **L3 im Code:** R je gekoppeltem Lauf.

## 3. Latten (Vorschlag, die Leitung entscheidet)

| Latte | F5-1 Q-Atom | F5-2 Huelle | F5-3 Mischung | F5-4 unsichtbarer Kern |
|---|---|---|---|---|
| L1 kann scheitern | ja: Zerfall im stabilen Fenster; zwei stabile Niveaus zugleich | ja: Huelle zerlaeuft bei a = 0,4; Huelle aendert das Schicksal von 0,95 | ja: stabiler Ball ueber der leichten Masse; Gamma weit neben der Formel | ja: R weit neben Born; Vorzeichen bei grossem k sichtbar; Einfang |
| L2 Gegenprobe | lam = 0 | a = 0, nackte Kerne | eps = 0 | lam = 0 |
| L3 Numerik | im Code: Bindung, R_chi, e0 | im Code: Wandanteil, Q_psi | im Code: P_max, Periode, Gamma, p | im Code: R |
| L4 bekannt | teilweise: gebundene Zustaende in Solitonen-Mulden, Bindungsschwelle in 3D (Lehrbuch); Q-Ball-"Atome" nicht nachgesehen | teilweise: Oberflaechenzustaende, Tenside | ja: Neutrino-Mischung (Formel Lehrbuch), Zerfall ueber Mischung | ja: Born-Streuung, Formfaktor (Hofstadter) |
| L5 Messbezug | nein (Analogie; Q-Ball-Dunkle-Materie als Bild [L]) | nein | teilweise: Mischungsformel ist die der Neutrinos, aber klassisch | nein |

Literatur aus dem Gedaechtnis, nicht nachgelesen. Schwellen und Klassen stehen im Code fest und werden nach dem Lauf
nicht gelockert.

## 4. Aufruf (Leitung, .69, kleintest.sh)

Remote-Ordner /home/fmh/fmhc-physics-remote/runde5-r5d/ mit **r5d.py und r5d_f5.py** (r5d_f5 importiert r5d). CPU-Spuren
brauchen `--geraet cpu`.

```
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5d-f5rauch r5d_f5.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5d/f5-rauch-cuda
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5d-f51 r5d_f5.py f51 --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5d/f51
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5d-f52 r5d_f5.py f52 --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5d/f52
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5d-f53 r5d_f5.py f53 --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5d/f53
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5d-f54 r5d_f5.py f54 --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5d/f54
```

f54 alternativ auf CPU in zwei Haelften:

```
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5d-f54a r5d_f5.py f54 --geraet cpu --masse 0.3 --out /home/fmh/fmhc-physics-remote/runde5-r5d/f54-m03
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5d-f54b r5d_f5.py f54 --geraet cpu --masse 0.6 --out /home/fmh/fmhc-physics-remote/runde5-r5d/f54-m06
```

## 5. Laufzeit: Rauchtest gemessen, Hochrechnung

**Gemessen** (Laptop, 1 CPU-Thread, nice 19, alle vier Karten mit Laufzeit x 0,05, Kern mit 1 Schiessrunde):
- 1. Rauchtest 02:49: 60,9 s, keine Fehler.
- 2. Rauchtest 02:53 nach den Korrekturen (Bekleidung F5-3, Tachyon-Lauf, Laeufe mit nicht endlichen Werten einzeln
  markiert): 67,8 s, keine Fehler.
- 3. Rauchtest 02:57 nach dem kleineren Keim im Tachyon-Lauf: 57,1 s, keine Fehler. Der Lauf "tief" meldet jetzt, wie
  beabsichtigt, "Kondensation" (C_max 200-fach); das zeigt nur die Form, es ist keine Messung.
- Die Streuung der Einzelzeiten (f54 fein 15,9 s bzw. 27,7 s) kommt von der Last auf dem Laptop.

| Karte | gesamt (1. / 2.) | davon (1. Lauf) |
|---|---|---|
| f51 | 26,2 / 19,8 s | linear 15,7 s, Dynamik grob 0,6 s + fein 2,3 s |
| f52 | 6,2 / 6,7 s | Dynamik 0,6 + 2,2 s |
| f53 | 8,6 / 8,6 s | 1,8 + 6,9 s |
| f54 | 19,8 / 32,7 s | 3,8 + 15,9 s (2. Lauf 4,9 + 27,7 s) |

**Hochrechnung fuer die vollen Aufrufe:** Dynamik mal 20, Schiessen mal ~4 (4 Runden), linearer Teil unveraendert.

| Aufruf | Laptop-Kern | .69-Kern (x 1 bis 2) | P4000 (startbegrenzt, ~3 ms je Schritt) |
|---|---|---|---|
| f51 | ~1,5 min | 1,5 bis 3 min | 1,5 bis 2,5 min |
| f52 | ~1,2 min | 1,2 bis 2,5 min | ~1,5 min |
| f53 | ~3 min | 3 bis 6 min | ~1,5 min |
| f54 | 6,6 bis 11 min | **zu knapp, nicht auf einem CPU-Kern** | ~1,5 min |
| f54 mit --masse (je Haelfte, CPU) | 3,3 bis 5,5 min | 3,3 bis 11 min (nur wenn der Rauchtest auf der .69 dort unter 16 s je Haelfte bleibt) | – |

Empfehlung: f54 auf p4000a. Regel wie in Runde 2: jede Stufenzeit des Rauchtests auf der .69 mal 20; ergibt ein Aufruf
mehr als 9 min, ihn nicht starten.

Speicher unter 0,2 GB (groesste dichte Eigenmatrix 1199^2 x 8 B = 11 MB).

## 6. Ausgabe und Grenzen

- **Ausgabe:** r5d_f5_<unterbefehl>_bericht.txt, _ergebnis.json, _reihen.pt im --out-Ordner.
- **Rauchtest-Zahlen gelten nicht:** Ausnahme sind die linearen Niveaus von F5-1 (siehe oben, vorlaeufig).
- **Lauf mit nicht endlichen Werten:** Er wird gemeldet (WARNUNG) und bekommt NaN; die anderen Laeufe desselben
  Aufrufs bleiben gueltig.
- **Klassische Felder:** "Verschraenkung" im quantenmechanischen Sinn ist nicht Teil dieser Rechnung (Karte, Hinweis
  der Leitung).
- **Anfangszustaende sind nicht exakt stationaer:** Huelle als Gauss-Schale; Wolke aus dem linearen Niveau ohne
  Rueckwirkung.
- **Q_min mit Huelle** braucht zweifaches Schiessen und ist nicht in dieser Runde.

## Einfach gesagt

Finns Bild stimmt zum Teil: Ein schwerer Q-Ball ist fuer leichte Teilchen wie eine Mulde, in der sie schweben koennen,
fast wie Elektronen um einen Atomkern. Nach unserer Rechnung passt aber nur ein einziges Schwebeniveau hinein; macht
man die Mulde tiefer, kippt das leichte Feld und sammelt sich als Brei statt zu schweben. Mischt man die beiden Felder,
pendelt die Ladung wie bei Neutrinos hin und her, und ein gemischter Ball haelt nur, wenn er fuer beide Sorten zu
wenig Energie hat, sonst verdampft er in die leichte Sorte. Ein unsichtbarer schwerer Ball verraet sich nur dadurch,
dass er leichte Wellen ein wenig zurueckwirft, und daran kann man seine Groesse ablesen.

Ende: 2026-09-30 02:58:28 CEST (gemessen mit date). Lokal nur Kompilierung und drei Rauchtests; Messlaeufe nicht gerechnet.
