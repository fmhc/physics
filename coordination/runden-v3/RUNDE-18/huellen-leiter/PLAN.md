# PLAN HUELLEN-LEITER (Runde 18)

- Code-Agent, Start 2026-10-02 13:40:56 CEST (date). Plan geschrieben ab 13:59 CEST (date), vor jedem .69-Lauf.
- Verbindlich aus der Karte: Suchbereich (E1, omega^2 0,74 bis 1,40), Ordnen nach chi-Kurven, Leiterfrage, Kontrollen
  (K1, zwei Gitterstufen, 15 bekannte Stellen), L1 bis L5, Bedeutung. Nichts davon wird nach dem Ergebnis geaendert.
- Gelesen: KARTE; RUNDE-17/stille-zweifeld ERGEBNIS, PLAN, PLAN-NACHTRAG-1, code/stille3.py, hilfs/zeilen-uebersicht-*;
  RUNDE-17/zweifeld-nachbau ERGEBNIS, PLAN, PLAN-NACHTRAG-1 bis 4; RUNDE-18/huellen-uhr ERGEBNIS; RUNDE-16/beutel-1
  ERGEBNIS; kleintest.sh (ssh cat).
- Code: code/huellen_leiter.py (eigen), importiert code/stille3.py und code/beutel.py unveraendert (Code 1, sha256
  1d15a38c... und f831e818..., gleich RUNDE-17).

## 1 Messgroesse (zuerst geklaert)

- **Code 1 (STILLE-ZWEIFELD)** benutzt fuer den Umlauf W = m_ac + i m_bc. Dabei ist G = W[Y_x, Z_y] die 3x2-Wronski-
  Matrix der regulaeren Loesungen Y_a, Y_b, Y_c (Gram-Schmidt-Ordnung c, b, a) gegen die abklingenden Loesungen Z_b,
  Z_c (ohne Welle in a); m_xy sind die 2x2-Minoren aus den Zeilen x, y.
  - Geschlossene Bedingung m_bc = 0. s = m_ac darauf. Stille Stelle <=> Rang G <= 1 <=> m_ac = m_bc = 0 (mit
    sigma2/sigma1-Probe gegen Scheinnullstellen mit Zeile c = 0).
  - W ist ein reelles Paar von Minoren, keine Jost-Determinante. Seine Nullstellen sind einfach und drehen mit +-1.
    Validiert: K1 Umlauf -1, 15 Stellen je +-1 aufgeloest auf zwei Stufen.
- **ZWEIFELD-NACHBAU** benutzt W2 = s~ + i m_a mit m_a = m_bc (gleiche geschlossene Bedingung). s~ ist auf der Kurve bis
  auf einen positiven Faktor s. Gleiche Nullstellen; die Umlaufvorzeichen sind dort global umgekehrt (Konvention:
  NACHBAU S1 = +1, Code 1 Nr 4 = -1 an derselben Stelle).
- **Wahl:** W von Code 1. Grund: derselbe Code und dieselbe Konvention wie fuer die 15 bekannten Stellen, also ist L1 ein
  Vergleich Gleiches mit Gleichem; Newton auf diesem W hat bei allen 15 konvergiert. Die Jost-Determinante (W1 von
  NACHBAU) wird nicht benutzt.
- Kontrolle: L1 verlangt an allen 15 Stellen Umlauf +-1 mit dem Vorzeichen aus Code 1; K1 verlangt -1.

## 2 Hintergrund und Zeilen

- Profile wie Code 1: Numerov-Newton (F = r f, H = r (g - 1)), Saat BEUTEL-1 bei Q = 200, Fortsetzung in omega^2 mit
  Streck-Praediktor zur Duennwand-Seite, Gebiet R_bg = 1,5 r_half + 25/mu + 5. Stufe 1: hp = 0,01; Stufe 2: hp = 0,005
  (Kanalschritt RK4 h = 2 hp).
- **Huellenradius (Definition vorab):** R = Radius, bei dem chi = g des Hintergrunds von innen her 1/2 kreuzt (lineare
  Interpolation auf dem Profilgitter). Je Zeile und je Lokalisierungspunkt.
- **Zeilen:** von omega^2 = 1,40 abwaerts, w2_{j+1} = w2_j - min(0,01; 0,5 (w2_j - 0,7281)^2 / 1,3736), letzte Zeile 0,74.
  Das ist gleichmaessig in R mit Abstand 0,5 (Naeherung R ~ 1,3736/(w2 - 0,7281) + 0,55, angepasst an r_half der Runde
  17), oberhalb omega^2 ~ 0,89 gekappt auf 0,01 in omega^2 (feiner als Runde 17). Etwa 266 Zeilen, beide Stufen gleich.
  - Begruendung: In Runde 17 liegen benachbarte Stellen einer Kurve ~ 2,2 bis 2,6 in R auseinander. 0,5 gibt etwa
    vier Zeilen je Abstand; die Unterzeilen (Abschnitt 4) verfeinern auf 0,0625.
- **Konvergenz der Hintergruende (vor der Suche ausgewertet):** Q und E jeder Zeile auf beiden Stufen. "Sauber" heisst
  |dQ/Q| und |dE/E| <= 1e-6 und Newton konvergiert. Bericht: bis zu welchem omega^2 sauber gerechnet ist. Zeilen ohne
  sauberen Hintergrund werden gerechnet, aber getrennt ausgewiesen.

## 3 Zeile (je omega^2, nur E1)

- rho-Gitter: 201 gleichmaessige Punkte in (sqrt2 - w + 1e-4, sqrt2 - 1e-4), dazu ein q-Gitter
  rho = sqrt(m0^2 + (pi q / R)^2), q = 0,2; 0,4; ... (m0^2 = U_chichi in r = 0). Grund: Die inneren chi-Zustaende liegen
  bei q ~ 1, 2, 3, ...; zur Schranke hin sind die untersten nur ~ 12,6/R^2 auseinander (bei R = 116 ~ 1e-3), das
  q-Gitter gibt dort 5 Punkte je Abstand.
- Je Gitterpunkt m_bc, m_ac (Code-1-Kanalrechnung: RK4, Gram-Schmidt alle 0,5, Abgleich bei r_m = r_half auf 0,02).
  Einzige Aenderung: Z startet bei r_m + 25/mu + 5 statt bei R_bg (dort ist der Hintergrund Vakuum auf ~e^-25; spart
  ~30 %). Pruefung: L1 und K1 laufen mit dem unveraenderten Code-1-Weg (Start bei R_bg) und muessen dieselben Lagen
  ergeben.
- Nullstellen von m_bc: jeder Vorzeichenwechsel, Startwert kubisch (Code 1), dann zwei Newton-Schritte in rho
  (Ableitung aus +-1e-4 Zellbreite). s = m_ac an der Nullstelle. Steigung sigma_c = sign(d m_bc / d rho).
  Merker "unsicher", wenn ein Schritt > halbe Zellbreite.
- Knotenzahl n_c: Zahl der Vorzeichenwechsel der c-Komponente von Y_c (regulaere Loesung mit u'(0) = e_c; Gram-Schmidt
  aendert sie nur um einen positiven Faktor) auf (0, r_m].

## 4 chi-Kurven, Kandidaten, Lagen

- **Kriterium chi-Kurve k (vorab):** k = Rang der Nullstelle von m_bc in der Zeile, von unten gezaehlt (k = 0 die
  unterste). Begruendung: Die Nullstellen von m_bc sind die gebundenen Zustaende des chi-Topfs der Huelle (Runde 17:
  16 Nullstellen bei 0,75, Abstaende wie Kastenzustaende; die unterste ~1,02 bis 1,24 ist die Wandmode). Als Eigenwerte
  eines eindimensionalen Problems kreuzen sie sich nicht; neue Kurven entstehen nur oben an der Schwelle rho = sqrt2,
  wenn R waechst. Damit ist der Rang von unten laengs jeder Kurve erhalten = Fortsetzung des Eigenwerts in omega^2.
  - Gegenprobe: Knotenzahl n_c je Nullstelle (berichtet). Merker "Rangsprung", wenn eine Nullstelle mit gleichem Rang in
    benachbarten Zeilen um mehr als die halbe Luecke zu den Nachbarkurven springt; Merker, wenn die Zahl der Nullstellen
    zur Schranke hin abnimmt.
  - Zuordnung Runde 17: Kurven 1 bis 4 von NACHBAU = k = 0, 1, 2, 3.
- **Unterzeilen je Zeilenpaar (j, j+1):** fuer jede Kurve, die in beiden Zeilen liegt, 7 Zwischenwerte omega^2 im Abstand
  1/8. Je Zwischenwert: Profil (Fortsetzung auf dem Gitter der unteren Zeile), rho-Startwert linear zwischen den
  Zeilen, ein Newton-Schritt in rho (+-1e-4 Luecke), s linear an die Wurzel. Verworfen, wenn der Schritt > 0,3 Luecke.
- **Kandidat:** jeder Vorzeichenwechsel von s laengs einer Kurve in der Folge (Zeile j+1, 7 Unterzeilen, Zeile j).
  Dann zwei Halbierungen in omega^2 (gleicher Newton-Schritt), Lage durch lineare Interpolation von s:
  Klammer 1/32 des Zeilenabstands (in R ~ 0,016). R der Stelle linear aus R der Klammerenden.
- **Zellen-Umlauf (jede Stelle, beide Stufen):** U_z = sign(s(oberes omega^2) - s(unteres omega^2)) * sigma_c. Herleitung:
  Auf der Kurve ist Im W = 0 und Re W = s; quer dazu dreht Im W mit sigma_c; die Jacobi-Determinante in (omega^2, rho)
  ist das Produkt, Orientierung gegen den Uhrzeigersinn wie Code 1. Merker, wenn sigma_c an den Klammerenden verschieden.
- **Rechteck-Umlauf (aufgeloest, Code 1 unveraendert: newton_E1, umlauf_mit_rueckfall, W = m_ac + i m_bc, Halbbreite
  min(1e-3; 0,4 Abstand zu den Schwellen; 0,25 Luecke; 0,5 Zeilenabstand), 16 Punkte je Kante, Sprung < 0,4 rad,
  hoechstens 24 Runden, Rueckfall 1e-4):**
  - fuer die 15 bekannten Stellen (Start: meine eigene lokalisierte Stelle, nicht die bekannte Lage), beide Stufen;
  - fuer eine Stichprobe neuer Stellen, beide Stufen: je Kurve k = 0 bis 3 die Stelle mit kleinstem omega^2 sowie
    die Stellen mit kleinstem omega^2 auf den Kurven k = 4, 8, 12, ... (so viele die Zeitbox erlaubt, in dieser Reihenfolge).
  - Prueft, dass Zellen-Umlauf = Rechteck-Umlauf.
- **"Stelle" (Zaehlung):** Vorzeichenwechsel von s auf Kurve k, auf beiden Stufen gefunden (gleiche Kurve, gleiches
  Zeilenpaar, Lage in omega^2 auf 1/16 des Zeilenabstands gleich), Zellen-Umlauf +-1 auf beiden Stufen gleich, ohne
  Merker Rangsprung/verworfen. Stellen nur einer Stufe oder mit Merker werden getrennt gelistet.
  - Abweichung von Runde 17 (begruendet): Dort hiess "gefunden" Rechteck-Umlauf aufgeloest. Bei erwartet einigen
    hundert Stellen (Abschaetzung aus den Kurvenabstaenden) passt das nicht in die Zeitbox. Der Rechteck-Umlauf wird
    deshalb an L1 und an der Stichprobe gegen den Zellen-Umlauf geprueft. Stimmen beide dort ueberein, gilt der
    Zellen-Umlauf fuer die Zaehlung. Weicht er an einer Probe ab, wird das berichtet und die Zaehlung als vorlaeufig
    markiert.

## 5 Kontrollen

- **K1:** Modell K1E1 von Code 1 (chi-Kopplung aus, chi-Potential (1/2)(chi^2 - 1)^2, Masse 1 fuer a, b), Zeilen omega^2
  0,78; 0,79; 0,80; 0,81; 0,82 auf beiden Stufen, ganze E1-Zeile, dieselbe Kette (Zeile, Rang, Unterzeilen, Halbierung),
  dann Newton und Rechteck wie Code 1. Bestanden: bewiesene Stelle 0,797677 / 1,744618 auf 1e-4 getroffen, Umlauf -1
  aufgeloest, beide Stufen; Zellen-Umlauf -1.
- **15 bekannte Stellen (L1):** Zuordnung: Kandidat auf derselben Stufe mit |omega^2 - bekannt| < Zeilenabstand und
  |rho - bekannt| < 0,3 Luecke. Dann Newton (Code 1) ab meiner Lage. Wiedergefunden: Lage auf 1e-6 in omega^2 und rho
  gegen die Tabelle in RUNDE-17 (Stufe 1) und Rechteck-Umlauf aufgeloest mit dem Vorzeichen der Tabelle, beide Stufen.
- **Zwei Gitterstufen je Fund:** Abschnitt 4 ("Stelle"). Zusaetzlich: Zahl und Rang der Nullstellen je Zeile auf
  beiden Stufen gleich (berichtet).

## 6 Wertung L1 bis L5 (vorab operationalisiert)

- L1: eingetroffen, wenn alle 15 wiedergefunden (Abschnitt 5).
- L2: Zahl der Stellen mit omega^2 < 0,819, die nicht zu den 15 gehoeren. Eingetroffen bei >= 10.
- L3: Auf jeder der Kurven k = 0, 1, 2, 3 die Stellen nach fallendem omega^2 ordnen, Abstaende Delta omega^2 bilden.
  Eingetroffen, wenn auf allen vier Kurven die Spearman-Korrelation zwischen Delta omega^2 und dem mittleren omega^2
  des Paares > 0,8 ist (Abstaende nehmen zur Schranke hin ab). Mindestens 4 Abstaende je Kurve, sonst offen.
- L4: Je Kurve mit mindestens 4 Stellen (3 Abstaende): Variationskoeffizient CV = Standardabweichung (n-1) / Mittelwert
  der Abstaende in R. Eingetroffen, wenn CV < 0,25 auf jeder solchen Kurve. Berichtet werden auch die Kurven k = 0..3
  einzeln und der Anteil der Kurven mit CV < 0,25.
- L5: eingetroffen, wenn mindestens eine Kurve mit k >= 4 eine Stelle hat.
- Leiterfrage (Haeufung zur Schranke): beantwortet mit L3, L4 und der Zahl der Stellen je Kurve gegen R.
- Bedeutung: woertlich nach Karte.

## 7 Laeufe (.69, kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4; je <= 10 min)

- V0: py_compile; Zeilenliste (liste). V1: Profile Stufe 1 (cpu) und Stufe 2 (cpu2), dazu K1 Stufe 1/2 (cpu3/cpu4).
- V2: Bloecke "block" (Zeilen i0..i1 rechnen, Paare i0..i1-1 lokalisieren), von omega^2 = 1,40 abwaerts, Stufen getrennt,
  verteilt auf die vier Spuren. Jede Zeile und jedes Paar wird sofort als JSON gespeichert; ein abgebrochener Block wird
  ab der ersten fehlenden Datei wiederholt (bereits vorhandene Dateien werden gelesen, nicht neu gerechnet).
- V3: Auswertung (Kurven, Stellen, Abgleich der Stufen, L1-Zuordnung, Stichprobe) mit code/auswertung.py; dann
  Rechteck-Umlaeufe (umlauf) fuer L1 und Stichprobe; dann Endauswertung und Abbildungen.
- Reihenfolge bei Zeitnot: Stufe 1 und 2 ganz von 1,40 abwaerts; was unten nicht mehr gerechnet ist, wird als
  "nicht erreicht" berichtet (Untergrenze omega^2 genannt).
- Programmfehler werden behoben und mit sha256 dokumentiert; das Verfahren bleibt. Folgelaeufe nur mit eingefrorenem
  PLAN-NACHTRAG-n.md, als nachtraeglich markiert.
