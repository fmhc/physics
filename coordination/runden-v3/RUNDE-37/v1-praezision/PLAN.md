# V-1-PRAEZISION: Plan des Code-Agenten (Runde 37)

- Code-Agent fuer die Leitung claude-primary. Start der Arbeit 2026-10-04 02:28:29 CEST (date), Zeitbox 120 min bis
  04:28 CEST. Plan geschrieben ab 02:56 CEST (date 02:56:06 direkt davor).
- Grundlage: KARTE.md (unveraendert), V-1-WEITER (RUNDE-36/v1-weiter/: KARTE, PLAN, ERGEBNIS, code/v1w.py,
  lauf-69/auswertung.json und Einzellaeufe), Ernte in RUNDE-36.md.
- Kennzeichen: [M] Mathematik, [L] / [L?] Literatur aus dem Gedaechtnis, [H] Hypothese, **[F]** Festlegung des
  Code-Agenten (von der Karte offen gelassen, hier vor dem Einfrieren festgelegt).
- Code: code/v1p.py (Rechnung), code/auswertung.py (Ausgleich, Urteile, Bild). Rechnungen nur auf der .69 ueber
  kleintest.sh, Spuren cpu3 und cpu4, hoechstens zwei Laeufe zugleich.

## 1. Modell und Groessen (wie V-1-WEITER) [M]

- Feld: phi_tt - phi_xx + eps phi_xxxx + U'(abs(phi)^2) phi = 0, U = S - S^2 + beta S^3, beta = 1.
- Hintergrund bei om = om_min = sqrt(3/4): eps f'''' - f'' + (U'(f^2) - om^2) f = 0, f(-inf) = f_c = sqrt(1/2), f(+inf) = 0.
- Schwankungen: eps Z'''' - Z'' + V(x) Z = 0, V = [[W - (rho - om)^2, C], [C, W - (rho + om)^2]], W = 1 - 4S + 9S^2,
  C = -2S + 6S^2, S = f^2.
- Kanaele, Flussform J und Laufrichtungen wie V-1-WEITER PLAN Abschnitt 2. Fuer eps < 0 je Seite drei offene Kanaele
  (aussen B alt, A neu, B neu; innen e1 alt, e1 neu, e2 neu).
- **rho_z(eps):** Nullstelle der Stille-Funktion E(rho) = det[Q_aus | Q_innen] (V-1-WEITER Abschnitt 4).
- **P(eps):** Flussanteil in die neuen Aussenkanaele (A neu + B neu) bei rho_z, bei Einfall mit Fluss 1 im alten
  Innenkanal e1 (V-1-WEITER "P_neu_aus"). Mitberichtet: Einzelkanaele, P_neu_innen, T_alt, Flussbilanz.

## 2. Hintergrund [F]

- **Messproblem [M/H]:** Fuer eps < 0 hat die Hintergrundgleichung an beiden Ruhepunkten zwei rein imaginaere
  Eigenwerte (k0 ~ 1/sqrt(abs(eps))). Eine Wand ohne jeden Schwanz gibt es generisch nicht (Nanopteron, [L?]). Der
  Schwanz ist von der Ordnung exp(-pi k0), also von derselben Ordnung wie das Leck. Er ist damit Teil der
  Modelldefinition.
  - V-1-WEITER legte ihn ungewollt ueber Randbedingungen bei x = 47 bzw. 90 und das FD-Gitter fest. Daher die
    Abhaengigkeit von Rand und Gitter dort.
- **Festlegung (Kartenmodell, gewertet):** Hintergrund = Loesung auf der instabilen Mannigfaltigkeit von f_c, also
  innen ohne Schwanz. Start bei x = -L mit f = f_c - a0 e^{lam1 (x + L)}, lam1^2 = (1 - sqrt(1 - 4 eps))/(2 eps),
  a0 = (f_c/2) e^{-lam1 L}. Taylor-Integration ueber das ganze Gebiet bis x = +L.
  - Aussen entsteht dann ein Schwanz der Groesse T. Da H = 0 erhalten ist und der Schwanz H > 0 traegt, waechst
    zusaetzlich ein Anteil ~ T^2 e^{x/2} [M].
  - Beides wird berichtet (Zerlegung des Zustands bei x = +L in die vier Moden bei f = 0).
  - Rauchlauf r2 (eps = -1,2e-2): T = 3,3e-12, Anteil e^{x/2} bei x = 70: 7,8e-6. Fuer abs(eps) <= 1e-2 erwartet
    <= 1e-8 bei x = 70 und darunter [H]. Das wird je Lauf berichtet.
- **Diagnosereihe D (beschreibend, kein Urteil):** Hintergrund f0 = sqrt(S_c/(1 + e^x)), eps nur in den
  Schwankungen, wie V-1-WEITER D_*. Sie dient dem Gleichwert-Nachweis gegen V-1-WEITER (gleiches Modell, dort
  sauber).
- **eps > 0 (Kontrolle +3e-3) [F]:** Der Kartenhintergrund ist fuer eps > 0 mit Schiessen nicht berechenbar. Die
  schnelle instabile Richtung e^{x/sqrt(eps)} bei f_c verstaerkt jeden Rundungsfehler um e^{18 * 140} (Rauchlauf r3 abgebrochen).
  - Die Kontrolle laeuft deshalb mit dem f0-Hintergrund.
  - [M] Fuer eps > 0 gibt es je Seite genau einen offenen Kanal. Dann gilt T = 0 genau bei E = 0, fuer jedes glatte
    reelle Profil (V-1-WEITER PLAN Abschnitt 4). Die Kontrolle prueft also Verfahren und Genauigkeit, nicht die Form
    des Hintergrunds.
  - "Leck" bei eps > 0 := T_aus(rho_z), der gesamte durchgelassene Flussanteil. Neue offene Kanaele gibt es dort
    nicht; P_neu ist per Konstruktion 0.

## 3. Verfahren: Taylor-Reihen in Festkomma (Weg (a) der Karte, ohne mpmath.odefun)

- Gleiches Randwert- und Streuproblem wie V-1-WEITER, gleiche Kanalbasen, gleiche Endblock-Auswertung der
  Dreiecksmatrix. Anders sind Integrator und Zahlformat:
  - Taylor-Verfahren der Ordnung N mit fester Schrittweite h fuer Hintergrund (nichtlinear) und Schwankungen (linear).
    Die Koeffizienten folgen exakt aus den Rekursionen der Differentialgleichungen (Cauchy-Produkte), normiert
    z_j = Z_j h^j.
  - Alle Koeffizienten sind Ganzzahlen mit Skala 2^-P, P = bits + 20 (Festkomma, Python-Ganzzahlen). QR, Determinante
    und Gleichungssysteme laufen in mpmath mit derselben Stellenzahl.
  - QR (Gram-Schmidt, zweimal, positive Diagonale): eps < 0 alle 10 Schritte, eps > 0 jeden Schritt.
- Schrittweite: h = L/n mit n = ceil(L K_max/kh), K_max = groesste Wellenzahl der neuen Kanaele bei rho_start.
  Abbruchfehler je Schritt ~ kh^N/N! (kh = 3,2, N = 64: ~1e-57).
- Gebiet: [-L; L] mit L = 70; Anpassung im Wandmittelpunkt x = 0.
  - Startfehler der asymptotischen Moden ~e^{-70} = 4e-31 relativ.
  - Erwartetes Signal bei -2e-3: Amplitude ~1e-25 [H, Hochrechnung V-1-WEITER].
- Nullstelle: Klammer rho_start -+ 5e-8 (bei fehlendem Vorzeichenwechsel bis dreimal x8), dann Illinois-Verfahren bis
  Klammerbreite < 1e-22 (eps < 0) bzw. < 2^-(bits-10) (eps > 0).
- Danach Streuung bei rho_z, in H zusaetzlich bei rho_z + 1e-8 (Empfindlichkeit, beschreibend).
- rho_start: V-1-WEITER-Werte (A-Laeufe) fuer -1e-2, -7e-3, -3e-3; sonst die V-1-WEITER-Formel
  rho_z(0) - 3,7486e-3 eps + 5,32e-3 eps^2. Reihe D: aus D_*-Laeufen angepasst.

### Konfigurationen (Karte: zwei Genauigkeiten, Schrittweite)

| Name | bits (Stellen) | N | kh | L | Zweck |
|---|---|---|---|---|---|
| H | 200 (~60) | 64 | 3,2 | 70 | Hauptlauf |
| G | 133 (~40) | 64 | 3,2 | 70 | zweite Genauigkeit (PR0) |
| S | 200 | 64 | 2,2 | 70 | Schrittweite x0,69 |
| R | 200 | 64 | 3,2 | 85 | Gebietsprobe, nur eps = -2e-3 |

- Punkte (Kartenmodell): eps = -1e-2, -7e-3, -5e-3, -4e-3, -3e-3, -2e-3, je H, G, S. Kontrolle +3e-3 (f0) in H und G.
  Reihe D: dieselben sechs eps in H.

## 4. Aufloesung eines Punkts [F]

- Ein Punkt gilt als gemessen (aufgeloest), wenn
  - H und G in ln P auf 1e-6 relativ uebereinstimmen und
  - H und S in ln P auf 1e-6 relativ uebereinstimmen und
  - die Flussbilanz in H unter 1e-40 liegt.
- Gewertet wird der Wert aus H.

## 5. Ausgleich [F, wo nicht von der Karte vorgegeben]

- Ungewichtete kleinste Quadrate in ln P ueber alle aufgeloesten Punkte des Kartenmodells.
- **F1 (q frei):** ln P = a + q ln abs(eps) - c/sqrt(abs(eps)).
- **F0 (q = 0):** ln P = a - c/sqrt(abs(eps)).
- **FK (genaues Kanal-k, q frei):** ln P = a + q ln abs(eps) - 2 d K_B(eps). Dazu FK0 mit q = 0 (beschreibend).
  - K_B(eps) = sqrt((1 + sqrt(1 + 4 abs(eps) mu_B))/(2 abs(eps))), mu_B = 1 - (rho_z(eps) + om)^2. Das ist die
    Wellenzahl des neuen Aussenkanals B neu, des Hauptkanals des Lecks: V-1-WEITER bei -1e-2 traegt er 88 % von P,
    Amplituden B neu 4,61e-9 gegen A neu 1,56e-9.
  - **Begruendung der Abweichung von der Kartenformel [F]:** Die Karte setzt omega = rho_z in die Vakuum-Dispersion
    omega^2 = 1 + k^2 + eps k^4 ein. Im mitrotierenden System haben die Aussenkanaele aber die Frequenzen rho -+ om,
    also mu_A = 1 - (rho - om)^2 und mu_B = 1 - (rho + om)^2. Ausserdem folgt aus der Dispersion fuer eps < 0
    k^2 = (1 + sqrt(1 - 4 abs(eps)(omega^2 - 1)))/(2 abs(eps)); die Karte hat "+" unter der Wurzel.
  - Beschreibend (ohne Urteil) berichtet: d mit der Kartenformel woertlich, mit Vorzeichen-berichtigter Kartenformel,
    mit K_A und mit 1/sqrt(abs(eps)) (= F1, d = c/2).
- Bild: ln P gegen 1/sqrt(abs(eps)) mit F1 und FK, darunter die Reste. Reihe D zusaetzlich (offen).

## 6. Urteilsregeln (mechanisch, Schwellen der Karte unveraendert)

- **PR0** (alle drei Teile noetig, sonst nicht eingetroffen):
  - (a) Genauigkeiten: fuer jeden gerechneten eps < 0 abs(ln P_H - ln P_G) <= 1e-6 abs(ln P_H).
  - (b) eps = -1e-2: abs(P_H/P_ref - 1) <= 0,05 mit P_ref = 9,378187e-17 **[F]**. Das ist der gewertete V-1-WEITER-Wert
    (A_m1e-2x, Tabelle 2). B dort: 8,81e-17, berichtet.
  - (c) eps = +3e-3: T_aus(rho_z) < 1e-60 in H; G berichtet.
  - "nicht auswertbar", wenn ein Teil nicht gerechnet werden konnte.
- **PR1:** c aus F1 im Bereich 6,22 bis 6,35: eingetroffen, sonst nicht eingetroffen.
- **PR2:** d aus FK mit abs(d/pi - 1) <= 0,003: eingetroffen, sonst nicht eingetroffen.
- **PR3:** groesster Betrag der Reste von F1 < 0,05: eingetroffen, sonst nicht eingetroffen.
- PR1 bis PR3 brauchen mindestens fuenf aufgeloeste Punkte des Kartenmodells, sonst nicht auswertbar. Nicht
  aufgeloeste Punkte fallen aus dem Ausgleich und werden genannt.
- **Gebietsprobe R:** weicht ln P bei -2e-3 um mehr als 1e-6 relativ von H ab, folgt ein Vermerk und eine
  Selbstanzeige. Die Urteilsregeln bleiben.

## 7. Rauchlaeufe vor dem Einfrieren (offengelegt)

Alle bei eps ausserhalb der Hauptliste.

| Lauf | eps, Modell | Konfiguration | Ergebnis | Dauer |
|---|---|---|---|---|
| r1 | -1,5e-2, f0 | 100 bits, N 40, kh 2,5, L 50 | rho_z = 1,77316666423873398555 (V-1-WEITER D: ...734); P = 4,30302997e-12 (V-1-WEITER D float64: 4,30303006e-12, relativ 1,9e-8); Bilanz -2,6e-28 | 7 s |
| r2 | -1,2e-2, Karte | H | rho_z = 1,77349883952891; P = 1,82437e-14 (V-1-WEITER r4, FD Ende 47: 1,878e-14); P_neu_innen = P; Bilanz -1e-52; bei rho_z + 1e-8 P relativ -1,7e-6, T_alt 1,8e-6; Schwanz T = 3,3e-12, Anteil e^{x/2} bei x = 70: 7,8e-6 | 32 s |
| r3 | +2e-3, Karte | H | im Hintergrund haengengeblieben (Ueberlauf der schnellen Richtung), nach ~3 min gestoppt | - |
| r4 | +2e-3, f0 | H | rho_z = 1,77349069560607 (Klammer 1e-63); T_aus(rho_z) = 1,4e-114; Bilanz -2,1e-57 | 95 s |

- Nach den Rauchlaeufen: eps > 0 mit f0-Hintergrund (Abschnitt 2). Am Code (v1p.py) seit r1 keine Aenderung.
- Was die Rauchlaeufe vorwegnehmen:
  - r1: Das Verfahren trifft V-1-WEITER im sauberen Modell D auf 2e-8.
  - r4: Die Kontrolle bei eps > 0 wird sehr wahrscheinlich bestehen (PR0 Teil c).
  - r2: Das Kartenmodell liegt nahe am FD-Wert von V-1-WEITER (3 % bei -1,2e-2, dort FD mit Ende 47). Fuer PR0 Teil b
    sagt das wenig, weil sich die Schwanzwahl unterscheidet.
  - Die Schwellen der Karte bleiben unveraendert.

## 8. Laufplan und Abbruch

- Ketten je Spur (cpu3, cpu4), jeder Lauf ein eigener kleintest-Aufruf (<= 600 s), Ergebnis-JSON laufend
  geschrieben.
- Danach code/auswertung.py ueber kleintest (lauf/auswertung.json, Bild), dann ERGEBNIS.md.
- Abbruch: Laeuft ein Punkt in 600 s nicht durch, wird er mit groesserem kh oder kleinerem L nicht nachgerechnet.
  Er gilt als "nicht gerechnet", mit Grund.
