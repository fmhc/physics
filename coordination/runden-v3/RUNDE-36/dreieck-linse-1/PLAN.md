# DREIECK-LINSE-1: Plan (Code-Agent fuer claude-primary, Runde 36)

- Geschrieben ab 2026-10-04 01:45:15 CEST (date). Wird vor der ersten echten Rechnung eingefroren:
  PLAN.md.eingefroren-JJJJMMTT-HHMMSS und code/linse.py.eingefroren-JJJJMMTT-HHMMSS, dazu sha256 von Plan und Code
  (EINGEFROREN-JJJJMMTT-HHMMSS.sha256).
- Karte: KARTE.md. D0 bis D3, ihre Schwellen und ihre Bedeutung gelten unveraendert. Was die Karte offenlaesst, ist
  unten mit **[Festlegung]** gekennzeichnet; alle Festlegungen stehen vor der ersten echten Rechnung fest.
- Code: code/linse.py (neu, aufgebaut auf RUNDE-34/einfang-1/code/einfang.py) und code/kegel_q.py (unveraenderte Kopie
  aus RUNDE-34/einfang-1/code, urspruenglich RUNDE-26; sha256 beginnt mit 4de64b080729204c).
- Rechnen nur auf der .69, Ordner /home/fmh/fmhc-physics-remote/runde36-linse/, jeder Lauf einzeln ueber
  kleintest.sh, Spur p4000a (CUDA, Quadro P4000, float64). Lokal keine Rechnung.

## 1. Netz

- kegel_q.Netz(n, h, R): gleichseitiges Dreiecksnetz aus n Sektoren zu 60 Grad um die Ecke 0.
  - **Hauptnetz n = 5:** Fuenfer-Spitze, Winkelsumme 300 Grad, Fehlwinkel delta = pi/3 = 60 Grad.
  - **Gegenprobe n = 6:** flaches Netz gleicher Bauart, Mitte vom Grad 6.
- h = 0,3, R = 85, Dirichlet phi = 0 am Rand; etwa 243 000 Ecken (n = 5, geschaetzt; der Lauf meldet die Zahl) bzw.
  291 241 (n = 6, Rauchlauf 3).
- **Schwamm** ab r_s = 70 bis R = 85, g_max = 1, quadratisch (wie EINFANG-1, dort r_s = R - 15).
- **Richtungen:** Einlaufstrahl theta0 = 0 (Gitterrichtung, Sektorgrenze). Gegenstrahl = der Strahl hinter der Spitze
  (bei n = 5 die Sektormitte). Das Netz ist spiegelsymmetrisch zur Achse Einlaufstrahl/Gegenstrahl, also ist die Bahn
  -b das Spiegelbild der Bahn +b (Spiegelprobe).
- **Pruefung je Lauf** (Code, Ausgabe im Lauf-JSON):
  - Netzpruefung aus kegel_q: Grade, Defekt an der Spitze, Euler-Charakteristik.
  - Kartenpruefung: Alle Kanten haben in beiden Entwicklungskarten (Abschnitt 3) die Laenge h, ausser den Kanten am
    jeweiligen Schnitt. Diese haben nach dem Kleben mit der Drehung um die Winkelsumme der Spitze wieder die Laenge h.

## 2. Start und Zeitentwicklung

- Modell M1 (U = S - S^2 + S^3/2), Q = 200, Startschnelle v0 = 0,05 (Karte).
- **Start je Bahn:**
  - Statischer Netzball mit Q_lat = Q/gamma_v (kegel_q.loese_ball), harmonischer Schwerpunkt bei z0 = X0 + i b in der
    Einlaufkarte, X0 = 42.
  - Boost mit v0 in Richtung -X: parallel zur Achse, auf die Spitze zu; Phase und Startableitung wie EINFANG-1,
    ohne Lorentz-Kontraktion.
  - Startabstand zur Spitze 43,2 / 46,5 / 51,9 / 58,0 fuer |b| = 10 / 20 / 30 / 40.
- **Stossparameter** (Karte): b = +10, -10, +20, -20, +30, -30, +40, -40.
  - +b laeuft links an der Spitze vorbei (phi > 0), -b rechts.
  - Die 8 Bahnen rechnen als 8 unabhaengige Felder auf demselben Netz in einem Lauf. Die Felder wechselwirken nicht,
    jedes Feld enthaelt genau einen Ball.
- **Zeitentwicklung wie EINFANG-1:**
  - A phi'' = -L phi - A U'(|phi|^2) phi - A gamma phi', Stoermer-Verlet mit dt = 0,1 (EINFANG-1: dt = 0,2 stabil),
    float64.
  - Der Schwamm wirkt als exakter Faktor; entzogene Energie und Ladung werden je Feld gezaehlt.
  - T = 2000, Diagnose alle 2 Zeiteinheiten.
  - Bei T = 2000 ist X = 42 - 0,05 T = -58. Jeder Ball hat das Auslauffenster (bis d = 56) ganz durchlaufen; b = 40
    erreicht am Ende gerade r_s = 70.

## 3. Messvorschrift

1. **Ort** = harmonischer Schwerpunkt mit glattem Fenster:
   - W = Sum g q w / Sum g q mit w = r^s exp(i s phi), s = 6/n, q = Ladung je Ecke.
   - g = 1 bis zum geodaetischen Abstand 12 vom letzten Ort, cos^2-Abfall bis 18, dahinter 0.
   - Abstand zur Spitze d = |W|^(1/s).
   - **Begruendung:**
     - W ist auf dem Kegel eindeutig (w ist am Schnitt stetig). W = z_c^s gilt exakt fuer runde Baelle, die die
       Spitze nicht ueberdecken (Mittelwerteigenschaft, KEGEL-Q).
     - Das glatte Fenster ersetzt die harte Schwelle (Lehre aus LICHT-1) und schneidet abgestrahlte Ladung ab.
     - Gemessen wird nur fern der Spitze (d >= 15), wo die Schwerpunktmasse taugen.
   - **Vergleichsmass** (beschreibend): harte Schwelle |phi|^2 > 0,01 wie EINFANG-1.
2. **Entwicklungskarte** [Festlegung]: **Auslaufkarte** = abgerollte Dreiecke mit dem Schnitt auf dem Einlaufstrahl, also
   vor der Spitze. Fuer den Ball z_A = d exp(i arg(-W)/s), fuer Ecken phi_A = phi - 150 Grad (phi > 0) bzw.
   phi + 150 Grad (phi <= 0).
   - **Abweichung vom Hinweis "Schnitt hinter der Spitze":**
     - Mit dem Schnitt auf dem Gegenstrahl liegen die Auslaufstuecke von +b und -b auf verschiedenen Seiten des
       Schnitts, sobald die Baelle den Gegenstrahl gekreuzt haben. Das geschieht im Abstand 2b, bei b = 10 und 20 also
       mitten im Auslauffenster.
     - Ein Verbindungsweg ohne Schnittdurchgang laeuft in dieser Karte vor der Spitze herum, umrundet sie also. Er
       gaebe 0 Grad (vor dem Kreuzen) bzw. 120 Grad (danach) statt delta.
   - **Massgeblich ist die Bedingung der Karte:** Der Verbindungsweg umrundet die Spitze nicht. Er laeuft also hinter
     der Spitze zwischen den Auslaufstuecken hindurch. Das leistet die Auslaufkarte.
     - Beide Bahnen liegen darin ganz ohne Schnittdurchgang, denn kein Ball kreuzt den Einlaufstrahl.
     - Die Einlaufrichtungen von +b und -b erscheinen dort um delta gedreht. Das ist der Schnitt der Karte; die Baelle
       starten parallel in der Einlaufkarte.
   - **Schreibtisch** [M]: Fuer Geodaeten laeuft +b in der Auslaufkarte unter +30 Grad, -b unter -30 Grad zum
     Gegenstrahl. Sie kreuzen sich auf dem Gegenstrahl im Abstand 2b unter 60 Grad.
3. **Fenster des Geradenausgleichs** [Festlegung]:
   - t_n = Zeit des kleinsten Abstands d.
   - Einlauf: t >= 30 (Einschwingen des Boosts), t < t_n, 15 <= d <= 56.
   - Auslauf: t > t_n, 15 <= d <= 56.
   - Die Grenzen bedeuten:
     - d >= 15: Dort ist die Mulde der Spitze abgeklungen (KEGEL-Q: |E(d) - E_flach| < 1 % von B schon ab
       d > R_half + 4/kappa = 12,3), und das Fenster des Schwerpunkts erreicht die Spitze kaum.
     - d <= 56: Der Ball bleibt 14 vor dem Schwamm.
   - Mindestens 50 Diagnosepunkte je Fenster, sonst "nicht auswertbar".
4. **Geradenausgleich** in der Auslaufkarte: x(t) und y(t) je linear (kleinste Quadrate).
   - Richtung theta = atan2(v_y, v_x), Schnelle v = |(v_x, v_y)|.
   - Beschreibend: senkrechte Abweichung von der Geraden; Richtung der ersten und der zweiten Fensterhaelfte
     (Geradheit).
5. **Winkel** (D0, D1, D2): Theta(b) = theta_aus(+b) - theta_aus(-b), gewickelt auf (-180, 180] Grad.
   - Positiv heisst beim Kegel: Die Bahnen laufen hinter der Spitze aufeinander zu.
   - Beschreibend: Einlaufwinkel Theta_ein(b) = theta_ein(+b) - theta_ein(-b) und Zusatzablenkung je Bahn
     epsilon = theta_aus - theta_ein mit Vorzeichen "zur Spitze hin positiv". Es gilt
     Theta(b) - Theta_ein(b) = epsilon(+b) + epsilon(-b).
6. **Endschnelle** (D0, D3): v_aus/v_ein - 1 aus den beiden Geradenausgleichen.
   - [Festlegung] "Startschnelle" = gemessenes v_ein. Der Start ohne Lorentz-Kontraktion liegt 0,06 % unter dem
     Nennwert (EINFANG-1); v_ein/0,05 - 1 wird berichtet.
7. **Schnittprobe** (Buchhaltungskontrolle):
   - Einlaufkarte (Schnitt hinter der Spitze); jede Bahn in ihrer eigenen Abwicklung (Winkel stetig fortgesetzt).
   - Das Auslaufstueck von -b wird ueber den Gegenstrahl an das Blatt von +b geklebt, also um die gemessene
     Winkelsumme der Spitze gedreht.
   - Das muss Theta(b) bis auf Rundung wiedergeben. Beim flachen Netz ist die Winkelsumme 360 Grad, das Kleben also die
     Identitaet (Probe der Unabhaengigkeit von der Schnittwahl).

## 4. Urteile (mechanisch, code: linse.py auswertung)

| Nr | Lauf | Regel (Schwellen aus der Karte) |
|---|---|---|
| D0 | li-F (n = 6) | eingetroffen, wenn \|Theta(b)\| < 0,5 Grad fuer b = 10, 20, 30, 40 und \|v_aus/v_ein - 1\| < 0,01 fuer alle 8 Bahnen |
| D1 | li-K (n = 5) | eingetroffen, wenn \|Theta(b) - 60 Grad\| <= 2 Grad fuer b = 20, 30 und 40 und die Spannweite max - min von Theta ueber diese b < 2 Grad ist |
| D2 | li-K | eingetroffen, wenn Theta(10) - 60 Grad >= 3 Grad |
| D3 | li-K | eingetroffen, wenn \|v_aus/v_ein - 1\| < 0,02 fuer alle 6 Bahnen b = +-20, +-30, +-40 |

- **[Festlegung] Streuung (D1)** = Spannweite max - min ueber b = 20, 30, 40.
- **Nicht auswertbar:** Lauf fehlt oder ist nicht fertig, ein Fenster hat weniger als 50 Punkte, nicht endliche Werte.
- **Konvergenzproben** mit denselben Regeln:
  - li-K-dt: dt = 0,05, alle 8 Bahnen.
  - li-K-h: h = 0,2, dt = 0,05, b = +-10 (also nur D2). Nur wenn die Zeitbox reicht.
  - Gibt eine Probe ein anderes Urteil, bekommt das Urteil den Vermerk "nicht konvergiert"; das Urteil selbst bleibt.
- Laeufe, die bis 03:00 CEST nicht fertig sind, gehen nicht ein.

## 5. Laeufe

| Name | Rolle | n | h | dt | b | T | Kosten (Rauchlauf) |
|---|---|---|---|---|---|---|---|
| li-K | D1, D2, D3 | 5 | 0,3 | 0,1 | +-10, +-20, +-30, +-40 | 2000 | ca. 5 min |
| li-F | D0 | 6 | 0,3 | 0,1 | +-10, +-20, +-30, +-40 | 2000 | ca. 5,5 min |
| li-K-dt | Konvergenz dt | 5 | 0,3 | 0,05 | +-10, +-20, +-30, +-40 | 2000 | ca. 9 min, 2 Abschnitte |
| li-K-h | Konvergenz h (wenn Zeit), nur D2 | 5 | 0,2 | 0,05 | +-10 | 2000 | ca. 9 min, 2 Abschnitte |

- Alle mit Q = 200, v0 = 0,05, X0 = 42, R = 85, r_s = 70, g_max = 1, Diagnose alle 2.
- Jeder Abschnitt startet einzeln ueber kleintest.sh p4000a. Nach 520 s Wandzeit sichert der Lauf seinen Zustand; der
  naechste Abschnitt setzt mit --fortsetzen fort.
- Reihenfolge: li-K, li-F, li-K-dt, li-K-h, dann auswertung und bild (ebenfalls ueber kleintest.sh p4000a).

## 6. Beschreibend (nicht gewertet)

- Bild der Bahnen in der Auslaufkarte fuer alle b (Kegel und flach) und Bild Winkel gegen b (lauf-69/bahnen.png,
  lauf-69/winkel.png).
- Je Bahn: Zusatzablenkung epsilon, Spiegelprobe epsilon(+b) - epsilon(-b), Geradheit (Fensterhaelften), senkrechte
  Abweichung.
- b = 10: Ablenkung, Verlangsamung, E_ball und Q_ball vor und nach, max |phi|^2 (Atmung).
- Vergleich mit dem Schwellen-Schwerpunkt; Energie- und Ladungsbilanz je Bahn.

## 7. Rauchlaeufe vor dem Einfrieren (offengelegt; Parameter kommen in keinem echten Lauf vor)

- **rauch1:** n = 5, h = 0,35, R = 50, r_s = 38, Q = 150, v = 0,1, X0 = 24, b = +-16, T = 450.
  - Winkel der Auslaeufe 60,0015 Grad, der Einlaeufe 59,9969 Grad; Zusatzablenkung je Bahn +0,0023 Grad zur Spitze.
  - v_aus/v_ein - 1 = -4,7e-6, Schnittprobe 0; beide Bahnen exakt spiegelgleich.
  - Kartenpruefung: Kanten isometrisch auf 9e-14, geklebt auf 7e-14; Winkelsumme der Spitze 5 pi/3 auf 9e-16.
  - **Damit war die Tendenz von D1 vor dem Einfrieren sichtbar (Selbstanzeige).**
- **rauch2:** dasselbe mit n = 6: Winkel -0,0001 Grad, v_aus/v_ein - 1 = -5,9e-6. **Tendenz von D0 sichtbar.**
  - Energie und Ort stimmen mit rauch1 auf alle gedruckten Stellen ueberein (der Ball sieht dort dasselbe Gitter).
- **rauch3** (Zeitmessung): n = 6, h = 0,3, R = 85, r_s = 70, Q = 150, v = 0,1, b = +-12, +-22, +-32, +-42, T = 100.
  - 12,85 ms je Schritt fuer 8 Felder, Aufbau 60 s (8 statische Baelle zu 5 bis 9 s).
- **rauch4** (Zeitmessung h = 0,2): n = 5, h = 0,2, R = 85, Q = 150, v = 0,1, b = +-11, dt = 0,05, T = 20.
  - 546 001 Ecken, Aufbau 16 s, 2 statische Baelle zu 16 bis 17 s, 10,6 ms je Schritt fuer 2 Felder; rc = 0 unter
    MemoryMax 4G. Deshalb rechnet li-K-h nur b = +-10.
- **Code nach den Rauchlaeufen geaendert** (ohne Einfluss auf Regeln oder Schwellen): Option --b-liste fuer die
  Auswertung der Rauchdaten; robuster Zugriff in den Urteilsfunktionen.
