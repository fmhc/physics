# NETZ-C-1: Plan des Code-Agenten (Runde 35)

- Code-Agent fuer die Leitung claude-primary. Start 20:48:56 CEST (date). Plan geschrieben ab 21:09:30 CEST (date).
- Reihenfolge:
  - Rauchlauf 1 lief ab 19:08:48 UTC, vor diesem Plan. Er zeigt keine Ergebnisgroessen: Netzbau (Grad, Zahl der
    Staebe und Winkelpaare), Zeit je Matrix, Zeitmessung der Kette bis t = 20, Fortsetzungstest.
  - Rauchlauf 2 (Teil A klein, Auswertepfad) startet erst, wenn die Abschnitte 1 bis 6 stehen.
  - Was ich dabei sehe, steht in Abschnitt 8. Danach friere ich ein.
- Spuren: nur cpu3 und cpu4 (Aenderung der Leitung vom 03.10. waehrend der Vorbereitung; cpu6 nie benutzt).
- Kennzeichen: [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese,
  [F] von der Karte offengelassen und hier vor dem Einfrieren festgelegt.

## 1. Vorhersagen (aus KARTE.md, unveraendert)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| P0 | Kontrolle: fcc-Geschwindigkeiten treffen die Tabelle auf 1e-4 relativ; Zahl der Nullmoden passt zur Maxwell-Zaehlung | 95 % |
| P1 | In jedem steifen Netz (alle akustischen Geschwindigkeiten > 0) gibt es in jeder Richtung mindestens zwei verschiedene Geschwindigkeiten, Verhaeltnis groesster zu kleinster >= 1,15 | 90 % |
| P2 | Pyrochlor nur mit Zentralfedern: mindestens ein akustischer Ast hat in einigen Richtungen Geschwindigkeit 0 (< 1e-6) | 60 % |
| P3 | Mit Winkelfedern sind alle Netze steif, und jeder Querast schwankt ueber die Richtungen um mindestens 10 % (keine zufaellige Isotropie) | 70 % |
| K0 | Kontrolle: ohne Kraft und Reibung Energie auf 1e-6 erhalten; groesste Gruppengeschwindigkeit der Kette < 1 | 95 % |
| K1 | h = 0,1: Endgeschwindigkeit innerhalb 2 % von gamma v = pi F/(4 eta) (Sollwerte v = 0,287; 0,707; 0,949; 0,995) | 80 % |
| K2 | h = 0,1, v <= 0,95: gamma aus der Steigung innerhalb 3 % von 1/sqrt(1 - v^2) | 75 % |
| K3 | Kein Kink ist je schneller als 1 (Kinkort-Schnelle <= 1 + 1e-3, alle Laeufe) | 95 % |
| K4 | [H] Ohne Reibung waechst gamma bis zu einer Grenze, die mit kleinerem h steigt; gamma_max h liegt fuer alle drei h zwischen 0,3 und 5 | 55 % |
| K5 | [H] h = 1: Endgeschwindigkeit bei pi F/(4 eta) = 10 mindestens 10 % unter dem Kontinuumswert (Gitterabstrahlung) | 50 % |

- Berichtigung der Leitung vor dem Start gilt: Teil B (1) rechnet mit eta = 0,01.

## 2. Teil A: Modell und Messvorschrift

### 2.1 Netze (Kantenlaenge 1, Masse 1 je Knoten)

| Netz | Bravais | kubische Kante a | Knoten je primitiver Zelle | Staebe je Zelle | Grad | Maxwell 3n - b |
|---|---|---|---|---|---|---|
| fcc | fcc, (a/2)(0,1,1) usw. | sqrt 2 | 1 | 6 | 12 | -3 |
| Pyrochlor | fcc | 2 sqrt 2 | 4: (a/8)(0,0,0), (0,2,2), (2,0,2), (2,2,0) | 12 | 6 | 0 |
| Diamant | fcc | 4/sqrt 3 | 2: 0 und (a/4)(1,1,1) | 4 | 4 | 2 |
| srs | bcc, (a/2)(-1,1,1) usw. | 2 sqrt 2 | 4: (a/8)(1,1,1), (5,3,7), (3,7,5), (7,5,3) (FLUSS-1) | 6 | 3 | 6 |

- Nachbarn: alle Knotenpaare im Abstand 1 (Toleranz 1e-9), gesucht ueber Zellversaetze -3..3. Geprueft und berichtet:
  Grad je Knoten, kleinster Abstand (muss 1 sein), Winkelhaeufigkeit je Knoten.
- Das optionale Tetraeder-Oktaeder-Fachwerk mit Zusatzdiagonalen rechne ich nicht (Zeitbox).

### 2.2 Federn [F]

- **Z:** Zentralfedern, Steifigkeit 1, Ruhelaenge = Kantenlaenge. Zeile je Stab: e_b = n_b . (u_j e^{i k.R} - u_i).
- **W1 (Hauptmodell mit Winkelfedern):** Z plus je Paar von Kanten an einem Knoten die Zeile
  d(cos theta) = d(r^_ij . r^_il) (Skalarprodukt der Einheitsvektoren, linearisiert), Steifigkeit k_theta = 0,1,
  Energie (k_theta/2) Summe d(cos theta)^2.
  - Fuer kollineare Paare (180 Grad) ist die Zeile exakt null; sie liefern keinen linearen Term. Das betrifft fcc (6 von
    66 Paaren je Knoten) und Pyrochlor (3 von 15).
  - Das ist die Form, fuer die der Hinweis der Leitung "kollineare Paare liefern keinen linearen Term" zutrifft. Sie
    ist eine reine Winkelfeder ohne Laengsanteil.
- **W2 (Variante, nur Vermerk):** Z plus Keating-Form d(r_ij . r_il) mit unnormierten Kantenvektoren, gleiche
  Steifigkeit 0,1.
  - Fuer kollineare Paare ist diese Zeile nicht null, sondern n . (u_l - u_j). Das ist eine Laengsfeder zum
    uebernaechsten Nachbarn laengs der Geraden, keine Biegung. Bei anderen Winkeln mischt W2 Winkel und Dehnung:
    d(r.r) = d(cos theta) + cos theta (dl_ij + dl_il).
  - W2 wird voll gerechnet und berichtet. Weicht ein Urteil P1 oder P3 unter W2 ab, steht das als Vermerk; das Urteil
    traegt W1.
- Die Energien sind unter starren Drehungen invariant (Skalarprodukte). Damit gibt es keine kuenstliche
  Drehsteifigkeit.

### 2.3 Dynamische Matrix und Geschwindigkeiten

- **Bloch-Matrix A(k):** Zeilen = Staebe (Gewicht 1) und Winkelpaare (Gewicht sqrt k_theta), Spalten = 3n
  Verschiebungen. Zellphase e^{i k.R} (Zellgauge), D(k) = A(k)^H A(k) (Masse 1).
  - Die Frequenzen sind die Singulaerwerte s_i von A(k). Ich nehme sie statt sqrt(Eigenwert von D), weil
    Singulaerwerte bis ~1e-15 absolut genau sind; Eigenwerte von D erst nach Wurzel (~3e-8).
  - Damit gilt c < 1e-6 bei |k| = 1e-3 als sauber messbar.
- **Geschwindigkeit:** c_i(k^) = s_i(|k| k^)/|k| bei |k| = 1e-3 (Hauptwert) und |k| = 2e-3 (Probe), Laenge in
  Kantenlaengen, Zeit in sqrt(m/k).
  - Linearitaet: Verhaeltnis c(2e-3)/c(1e-3) je Ast, berichtet als Minimum und Maximum ueber alle Richtungen.
- **Aeste [F]:** je Richtung nach Singulaerwert sortiert (Vorgabe der Leitung). Die drei kleinsten heissen die
  akustischen Aeste 1 <= 2 <= 3.
  - Queraeste = Aeste 1 und 2, Laengsast = Ast 3.
  - Entartung und Kreuzung: Die sortierten Werte sind stetig in der Richtung, eine Zuordnung ueber Kreuzungen hinweg
    findet nicht statt. Die Anisotropie wird je sortiertem Ast gemessen.
  - Berichtet je Ast: Laengsanteil lambda_L = |p . k^|^2/|p|^2 der mittleren Verschiebung p. Damit sieht man, ob der
    schnellste Ast wirklich laengs schwingt.
  - Berichtet je Ast: Translationsanteil tau = n |mittlere Verschiebung|^2 (1 = reine Verschiebung aller Knoten der
    Zelle, kleiner = Beimischung innerer Bewegung).
  - Ein Ast mit c = 0, der aus einer optischen Nullmode kommt (kleines tau), zaehlt nach dieser Regel als
    akustischer Ast. Sein tau steht als Vermerk dabei.
  - Berichtet wird auch die Luecke c4/c3 (vierter Singulaerwert gegen dritten) als Mass, wie sauber die drei
    akustischen Aeste vom Rest getrennt sind.
- **Nullschwelle:** c < 1e-6, also Eigenwert < 1e-12 |k|^2, gilt als null (Karte P2).
- **Steif:** In allen Richtungen des Satzes sind alle drei akustischen Geschwindigkeiten >= 1e-6, beim jeweils
  betrachteten |k|.
- **Richtungssatz:**
  - Hauptwert: [100], [110], [111] und 400 Fibonacci-Richtungen auf der ganzen Kugel.
  - Probe 1: dieselben drei und 800 Fibonacci-Richtungen.
  - Probe 2: |k| = 2e-3 mit 400.
  - Probe 3 (Verfeinerung, nur steife Modelle):
    - Nelder-Mead in (theta, phi), Start an den 5 (P1) bzw. 3 (P3) besten Richtungen des 800er Satzes,
      xatol 1e-7, hoechstens 600 Schritte
    - gesucht werden das kleinste Verhaeltnis Ast 3/Ast 1 und je Querast Minimum und Maximum

### 2.4 Nullmoden auf dem k-Gitter

- **Gitter:** k = sum (m_i/N) b_i, m_i = 0..N-1, N = 12 (Probe) und N = 16 (Hauptwert), b_i reziproke primitive Basis.
- **Nullschwelle:** Singulaerwert < 1e-6 |k|_min; |k|_min ist der Abstand zum naechsten reziproken Gittervektor.
  Bei k = 0 gilt die absolute Schwelle 1e-9.
- **Berichtet je Netz und Modell:**
  - Histogramm der Nullmodenzahl N0(k) fuer k ungleich 0, und N0(0)
  - Zahl der Punkte mit N0 > 0 und Summe der Nullmoden
  - Abstand der Schwelle zu den Werten: groesster als null gezaehlter s/|k| und kleinster nicht null gezaehlter s/|k|
- **Lage im k-Raum:** Fuer Pyrochlor und fcc zaehle ich die <110>-Richtungen e mit k . T_e in 2 pi Z (T_e kuerzester
  Gittervektor laengs e), also die Ebenen senkrecht zu geraden Stablinien.
  - Berichtet: Zahl der Nullpunkte auf mindestens einer solchen Ebene, und Zahl der Punkte mit N0 = Ebenenzahl.
- **Generisch:** 64 zufaellige k-Punkte (Seed 20261003). Gezaehlt werden N0 = 3n - Rang und Ns = Zeilen - Rang.
  - Maxwell-Zaehlung: generisch N0 = max(0, 3n - b) fuer die Zentralfedern.
  - Die Indexzahl N0 - Ns = 3n - b gilt immer (Rang-Satz) und ist keine Pruefung.

### 2.5 fcc-Kontrolle [F]

- Bei Kantenlaenge 1 ist a = sqrt 2 und c0 = (a/2) sqrt(k/m) = 0,70711.
- Sollwerte in c0, sortiert:

  | Richtung | Soll in c0 (Ast 1, 2, 3) |
  |---|---|
  | [100] | 1, 1, sqrt 2 |
  | [110] | 1/sqrt 2, 1, sqrt 2,5 |
  | [111] | sqrt(2/3), sqrt(2/3), sqrt(8/3) |

  - Die Werte sind die geschlossenen Formen aus C11 = 2k/a, C12 = C44 = k/a der Karte.
  - Die dreistelligen Tabellenwerte der Karte sind deren Rundungen. Schon ihr Rundungsfehler (bis 6e-4 bei 0,816)
    liegt ueber 1e-4. Verglichen wird deshalb mit den geschlossenen Formen.
- Polarisation laengs [110], wie in der Tabelle der Karte:
  - Ast 1 (1/sqrt 2) muss auf [1-10] stehen: |p . [1-10]/sqrt 2| >= 0,99
  - Ast 2 (1) muss auf [001] stehen: |p_z| >= 0,99

## 3. Teil B: Kette und Messvorschrift

### 3.1 Gleichung, Integrator, Start

- **Gleichung:** u_n'' = (u_{n+1} - 2 u_n + u_{n-1})/h^2 - sin u_n - eta u_n' + F, x_n = n h, freie Enden.
  - Hamilton-Funktion H = sum h [p^2/2 + 1 - cos u - F u] + sum (u_{n+1} - u_n)^2/(2h).
- **Integrator [F]:** Yoshida 4. Ordnung (symplektisch, drei Kraftauswertungen je Schritt) fuer den Hamilton-Teil.
  - Reibung exakt als p -> p exp(-eta dt/2) vor und nach jedem Schritt (Strang).
  - Zeitschritt, nach Rauchlauf 2 festgelegt (Abschnitt 8):
    - Hauptwert dt1 = 0,0125 fuer h >= 0,125, also dt = h/80, h/40, h/20, h/10 fuer h = 1; 0,5; 0,25; 0,125
    - h = 0,1: dt1 = 0,01 (h/10)
    - Probe dt2 = dt1/2
  - Laufnamen: Endung _dt1 = Hauptwert, _dt2 = Probe.
  - Zuerst geplant war dt = h/10 und h/20. Bei h = 1 verfehlt dt = h/10 die K0-Kontrolle; Abschnitt 8 nennt die
    Zahlen.
- **Start [F]:** Kontinuums-Antikink u = arcsin F + 4 arctan exp(-gamma0 (x - X0)), p = 2 v0 gamma0 sech(gamma0 (x - X0)).
  - Links 2 pi + arcsin F, rechts arcsin F. F > 0 schiebt ihn nach rechts, mit der Kraft 2 pi F.
  - Ich nehme den Antikink statt des Kinks, damit die Bewegung in die lange Seite der Kette geht. Physikalisch ist das
    gleichwertig.
  - X0 = 50. Teil B (1) und K4 starten ruhend (v0 = 0). K0 startet geboostet mit v0 = 0,9.
  - Die Kontinuumsform ist auf dem Gitter nicht exakt statisch. Der kleine Anfangsstoss bleibt drin und wird nicht
    entfernt.

### 3.2 Laeufe

| Gruppe | h | F | eta | v0 | t_end | Kettenlaenge L | Knoten |
|---|---|---|---|---|---|---|---|
| K0 | 0,1 und 1 | 0 | 0 | 0,9 | 300 | 400 | 4001 / 401 |
| (1) | 0,1 und 1 | (4 eta/pi) q, q = 0,3; 1; 3; 10 | 0,01 | 0 | 1000 | 1150 | 11501 / 1151 |
| K4 | 0,5 / 0,25 / 0,125 | 0,02 | 0 | 0 | 828 / 1656 / 3312 | 930 / 1760 / 3420 | 1861 / 7041 / 27361 |

- Jeder Lauf mit dt1 und dt2 (Abschnitt 3.1).
- Laufende von K4 [F]: t_end = 414/h. Bis dahin wuerde gamma im Kontinuum gamma h = 6,5 erreichen. Ein Wachstum ohne
  Grenze ueber gamma h = 5 hinaus waere also sichtbar.
- Die Kette ist so lang, dass der Kink den Rand nicht erreicht. Abbruch, falls der Kinkort naeher als 30 am rechten
  Ende ist; dann steht der Status "rand" im Kopf.
- Lange Laeufe setzen sich ueber Checkpoints fort (Wandzeit 520 s je Aufruf, hoechstens 4 Aufrufe).

### 3.3 Messungen (alle 0,5 Zeiteinheiten)

- **Kinkort X:**
  - Kreuzung von u = pi + arcsin F, linear interpoliert.
  - Bei mehreren Kreuzungen gilt die naechste am vorigen Ort.
  - Daneben der Schwerpunkt Xcm von -u_x im Fenster [X - 4, X + 4], nur berichtet.
- **Fenster:** |x - X| <= 4.
- **gamma aus der Steigung:**
  - gamma_s = (groesster Differenzenquotient (u_n - u_{n+1})/h im Fenster)/2 (roh).
  - gamma_sp: Scheitel der Parabel durch den groessten Quotienten und seine zwei Nachbarn, halbiert.
- **gamma aus der Energie:** gamma_E = E_win/8.
  - E_win ist die Energie im Fenster ohne den F u-Term: Summe h [p^2/2 + 1 - cos u - (1 - cos arcsin F)] plus die
    Federenergie der Staebe im Fenster.
- **Weitere Energien:**
  - E0 = dieselbe Summe ueber die ganze Kette
  - E_hinten, E_vorn = ausserhalb des Fensters
  - Energie ausserhalb des Kinks = E0 - E_win
  - H (die volle Hamilton-Funktion) fuer die Erhaltung
- **ncross:** Zahl aller Kreuzungen der Niveaus pi + arcsin F + 2 pi m (m ganz) laengs der Kette. Fuer einen Kink
  ist ncross = 1.
- **Zerstoerung [F]:** erster Messzeitpunkt mit einer dieser Bedingungen. Alle Groessen, die "vor der Zerstoerung"
  heissen, enden dort.
  - ncross ungleich 1 (Paarbildung oder Ueberschlag)
  - kein Kinkort
  - Sprung des Kinkorts > 2 zwischen zwei Messungen (scheinbare Schnelle > 4)
  - E_win < 4 (der Kink hat mehr als die Haelfte seiner Ruheenergie verloren)
- **Endgeschwindigkeit:** Steigung der Ausgleichsgeraden X(t) ueber t in [800, 1000]. Nach 8/eta ist der
  Einschwingrest e^-8 = 3e-4.
  - Ist der Kink vor t = 1000 zerstoert, gibt es keine Endgeschwindigkeit.
- **gamma fuer K2 [F]:** Mittel von gamma_sp ueber [800, 1000]; die Karte schreibt fuer K2 gamma aus der Steigung vor.
  - Daneben berichtet: gamma_s roh und gamma_E.
- **Schnelle fuer K3 [F]:**
  - Fensterschnelle = Steigung der Ausgleichsgeraden von X ueber gleitende Fenster von 20 Zeiteinheiten (41 Punkte),
    nur vor der Zerstoerung.
  - Der Hoechstwert ueber alle Fenster und alle Laeufe traegt das Urteil.
  - Berichtet werden auch die Zweipunkt-Schnelle (X-Differenz je 0,5) und die Fensterschnelle von Xcm.
  - Begruendung: Ist der Kink schmaler als h, springt der interpolierte Ort stufig. Die Zweipunkt-Schnelle schwankt
    dann auch bei gleichmaessiger Bewegung ueber 1.
- **gamma_max und Grenze fuer K4 [F]:**
  - gamma_max = Hoechstwert des gleitenden Mittels (20 Zeiteinheiten) von gamma_E vor der Zerstoerung oder bis
    Laufende.
  - Begruendung, warum die Energie das K4-Urteil traegt und nicht die Steigung [M]:
    - Zwei Nachbarknoten unterscheiden sich in einem intakten Kink um hoechstens 2 pi. Daher ist gamma_s = (u_x,max)/2
      <= pi/h, also gamma_s h <= pi.
    - Diese Groesse liegt damit vorab im Band [0,3; 5] nach oben begrenzt und saettigt von selbst. Sie ist fuer K4
      keine Messung.
    - gamma_E hat keinen solchen Deckel. gamma_s wird trotzdem berichtet.
  - Grenze erreicht heisst:
    - Zerstoerung vor t_end, oder
    - Saettigung: Steigung der Ausgleichsgeraden des gleitenden Mittels von gamma_E im letzten Viertel von
      [0, t_stop] < 0,25 pi F/4. Das ist ein Viertel der Kontinuumsrate d gamma/dt -> pi F/4 fuer v -> 1.
  - Berichtet werden auch Stichproben gamma_E, gamma_s und gamma Kontinuum = sqrt(1 + (pi F t/4)^2) bei
    t = 100, 200, 400, 800, 1600, 3200, sowie die Energie ausserhalb des Kinks.
- **Groesste Gruppengeschwindigkeit:** v_g = sin(kh)/(h omega), omega^2 = 1 + 4 sin^2(kh/2)/h^2, auf 10^6
  Punkten in (0, pi/h], fuer h = 0,1; 1; 0,5; 0,25; 0,125.
  - [M]: sin^2(kh)/h^2 = 4 sin^2(kh/2) cos^2(kh/2)/h^2 < omega^2, also v_g < 1 immer. Das ist eine Kontrolle, keine
    Messung.

## 4. Urteilsregeln (mechanisch, code/auswertung.py)

- **P0:** eingetroffen, wenn alle Bedingungen gelten:
  - fcc-Z bei |k| = 1e-3: alle 9 Geschwindigkeiten in [100], [110], [111] liegen relativ <= 1e-4 an den Sollwerten
    (Abschnitt 2.5).
  - Beide [110]-Polarisationen >= 0,99.
  - Fuer alle vier Netze mit Zentralfedern: generisch (64 Zufallspunkte) ist N0 = max(0, 3n - b) an jedem Punkt.
  - fcc-Z auf dem Gitter 16^3: N0 = 0 an jedem k ungleich 0 und N0(0) = 3.
  - Probe: |k| = 2e-3 und Gitter 12^3.
- **P1:**
  - Menge S = alle Paare (Netz, Modell) mit Modell Z oder W1, die steif sind (Hauptsatz, |k| = 1e-3).
  - Eingetroffen, wenn S nicht leer ist und fuer jedes Paar in S das kleinste Verhaeltnis Ast 3/Ast 1 ueber alle
    Richtungen >= 1,15 ist. Dann gibt es auch mindestens zwei verschiedene Geschwindigkeiten.
  - Proben: 800er Satz, |k| = 2e-3, und die Verfeinerung (kleinerer Wert von Gitter und Verfeinerung).
  - W2 steht als Vermerk dabei.
- **P2:**
  - Eingetroffen, wenn Pyrochlor-Z im Hauptsatz in mindestens einer Richtung einen akustischen Ast mit c < 1e-6 hat.
    Eine Symmetrierichtung steht wegen der kubischen Symmetrie fuer mindestens drei gleichwertige Richtungen.
  - Proben: 800er Satz und |k| = 2e-3.
  - Vermerk: tau der Nullaeste in den Symmetrierichtungen.
- **P3:**
  - Eingetroffen, wenn alle vier Netze mit W1 steif sind (Hauptsatz) und fuer jedes Netz beide Queraeste
    (Ast 1 und 2) ueber die Richtungen max/min - 1 >= 0,10 erreichen.
  - "Schwankt um mindestens 10 %" lese ich als max/min >= 1,10 [F]. Berichtet wird auch (max - min)/Mittel.
  - Proben: 800er Satz, |k| = 2e-3, Verfeinerung (groesserer Wert).
  - W2 als Vermerk.
- **K0:** eingetroffen, wenn
  - in beiden K0-Laeufen (h = 0,1 und 1, dt1) max |H(t) - H(0)|/|H(0)| <= 1e-6 gilt, und
  - die groesste Gruppengeschwindigkeit fuer alle fuenf h < 1 ist.
  - Probe: dt2.
- **K1:** eingetroffen, wenn fuer alle vier h = 0,1-Laeufe |v_end - v_soll|/v_soll <= 0,02 gilt, mit
  v_soll = q/sqrt(1 + q^2).
  - Ein vor t = 1000 zerstoerter Kink zaehlt als nicht eingetroffen.
- **K2:** eingetroffen, wenn fuer die drei h = 0,1-Laeufe mit v_soll <= 0,95 (q = 0,3; 1; 3; Auswahl nach Sollwert)
  |gamma_sp/gamma_v - 1| <= 0,03 gilt, mit gamma_v = 1/sqrt(1 - v_end^2) aus der gemessenen Endgeschwindigkeit.
- **K3:** eingetroffen, wenn die groesste Fensterschnelle aller Laeufe (K0, (1), K4; jeweils vor der Zerstoerung)
  <= 1,001 ist.
- **K4:**
  - Teil a: Alle drei h erreichen eine Grenze (Abschnitt 3.3).
  - Teil b: gamma_max(0,125) > gamma_max(0,25) > gamma_max(0,5).
  - Teil c: 0,3 <= gamma_max h <= 5 fuer alle drei h.
  - Eingetroffen bei a und b und c. Nicht eingetroffen bei a ohne (b und c).
  - Erreicht ein h keine Grenze:
    - nicht eingetroffen, wenn der Verstoss endgueltig ist: gamma_max h > 5 bei irgendeinem h, oder gamma_max h < 0,3
      bei einem h mit Grenze, oder b verletzt zwischen zwei h mit Grenze
    - sonst nicht auswertbar
- **K5:**
  - Eingetroffen, wenn im Lauf h = 1, q = 10 v_end <= 0,9 v_Kontinuum = 0,9 x 0,99504 = 0,89554.
  - Nicht auswertbar, wenn der Kink vor t = 1000 zerstoert ist.

## 5. Konvergenzproben und Vermerke

- Jede Vorhersage wird mit Hauptwert und Probe(n) ausgewertet. Das Urteil traegt der Hauptwert.
  - Gibt eine Probe ein anderes Urteil, steht "nicht konvergiert" als Vermerk.
  - Teil A: |k| = 2e-3, 800er Richtungssatz, Verfeinerung, Gitter 12^3.
  - Teil B: dt2 = dt1/2.
- h selbst ist in Teil B eine physikalische Groesse (Gitterabstand der Kette), keine numerische. Die zwei h je
  Gruppe sind Teil der Fragestellung.

## 6. Erwartungen vor der Rechnung (nicht gewertet, zur spaeteren Lesart)

- **P0 und P1 fuer fcc-Z sind vorab ableitbar [M].**
  - Die Christoffel-Gleichung mit C11 = 2, C12 = C44 = 1 legt alle Geschwindigkeiten fest.
  - In den Symmetrierichtungen ist Ast 3/Ast 1 = sqrt 2, sqrt 5 und 2.
  - Die Rechnung prueft hier den Code, nicht die Physik.
- **P2 ist weitgehend vorab ableitbar [M].**
  - EIS-1 fand Eigenspannungen laengs gerader <110>-Linien. Eine solche Linie traegt bei Bloch-Wellenvektor k eine
    Eigenspannung, wenn k . T_e in 2 pi Z liegt.
  - Pyrochlor ist isostatisch (3n = b). Nach dem Indexsatz (Maxwell-Calladine) ist dann N0(k) = Ns(k) an jedem k.
  - Auf den Ebenen k senkrecht zu e, die durch k = 0 gehen, gibt es also fuer jedes |k| eine Nullmode.
  - [100], [110] und [111] liegen auf 2, 1 und 3 solchen Ebenen.
  - Offen ist nur, ob die Rechnung das zeigt und welchen Translationsanteil der Nullast hat.
- **Pyrochlor-Z bei kleinem k [H, Schreibtisch]:**
  - Bei k = 0 gibt es 6 Nullmoden: 3 Verschiebungen und 3 Gegendrehungen der oberen und unteren Tetraeder.
  - Meine Schreibtischrechnung im Nullraum ergibt keine gemeinsame Nullrichtung abseits der Ebenen. Die Gegendrehungen
    sollten dann bei kleinem k ebenfalls linear werden: sechs lineare Aeste statt drei.
  - Laengs [110] mischt die Nullmode eine Verschiebung laengs [1-10] mit der Gegendrehung (tau ungefaehr 1/3).
- **Diamant-Z [M, L: Keating 1966 mit beta = 0]:**
  - C11 = C12, C44 = 0. Zwei Queraeste sind ueberall null (das sind die 2 Maxwell-Nullmoden).
  - Der Laengsast ist isotrop. Diamant-Z ist nicht steif.
- **srs-Z [H]:** 6 Nullmoden je k. Ich erwarte alle akustischen Geschwindigkeiten null oder fast alle; nicht steif.
- **K1 [L: McLaughlin/Scott 1978]:** Kontinuum gamma v(t) = (pi F/(4 eta))(1 - e^{-eta t}) ab Ruhe. Bei h = 0,1 und
  q = 10 ist gamma h ~ 1, dort sind Gitterabweichungen moeglich; v_soll = 0,995 ist aber unempfindlich.
- **K4 [H]:**
  - Abstrahlung durch Resonanz mit Gitterwellen (Peierls-Nabarro, [L?: Peyrard/Kruskal 1984]) waechst ungefaehr wie
    exp(-pi^2/(gamma h)).
  - Ein Gleichgewicht mit der Kraftleistung 2 pi F v kann bei gamma h von einigen Einheiten liegen, also auch ueber 5.

## 7. Rauchlaeufe

- **Rauchlauf 1** (code/rauch1.sh, vor diesem Plan, ohne Ergebnisgroessen):
  - Netzbau aller Netze mit Zeit je Singulaerwertzerlegung
  - Kette h = 0,1 und h = 0,125 bis t = 20 (Zeitmessung)
  - Fortsetzungstest: h = 0,5 bis t = 40 mit Wandzeit 0,5 s, verglichen mit einem ununterbrochenen Lauf
- **Rauchlauf 2** (code/rauch2.sh, nach diesem Plan):
  - Teil A mit 20/40 Fibonacci-Richtungen fuer alle Netze und Modelle
  - drei Kettenlaeufe bis t = 30 unter Hauptnamen
  - auswertung.py auf diesem Ordner, um den Auswertepfad zu pruefen
  - Die Urteile daraus zaehlen nicht.

## 8. Beobachtungen aus den Rauchlaeufen (vor dem Einfrieren nachgetragen)

- Nachgetragen ab 21:16 CEST. Rauchlauf 1: 19:08:48 bis 19:08:56 UTC. Rauchlauf 2: 19:12:31 bis 19:13:34 UTC.
  Zeitschritt-Rauch: 19:15 UTC. Daten in rauch-69/.
- **Netzbau:**
  - Grad 12/6/4/3, kleinster Abstand 1, Staebe je Zelle 6/12/4/6.
  - Winkel je Knoten:
    - fcc 24 x 60, 12 x 90, 24 x 120, 6 x 180 Grad
    - Pyrochlor 24 x 60, 24 x 120, 12 x 180 Grad (je Zelle)
    - Diamant 12 x 109 Grad
    - srs 12 x 120 Grad
  - Das stimmt mit Abschnitt 2.1 ueberein.
- **Fortsetzung ueber Checkpoints:** 10 Abschnitte gegen einen ununterbrochenen Lauf, alle Zeitreihen bitgleich
  (max. Differenz 0,0).
- **Zeit je Schritt:** h = 0,1 (11501 Knoten) 0,75 ms; h = 0,125 (27361 Knoten) 2,3 ms. Daraus die Verteilung der
  Laeufe auf die Spuren.
- **Zeitschritt [Selbstanzeige, vor dem Einfrieren]:**
  - K0-Rauch h = 1, v0 = 0,9, t = 30. Energieabweichung bei dt = h/10, h/20, h/40, h/80: 9,7e-5; 6,0e-6; 3,7e-7;
    2,3e-8. Das ist die saubere dt^4-Skalierung des Yoshida-Verfahrens.
  - h = 0,1 mit dt = h/10: 1,9e-9. h = 0,5 mit dt = h/10: 4,4e-8 (mit F = 0,02, ohne Reibung).
  - Deshalb dt1 = 0,0125 fuer h >= 0,125 (Abschnitt 3.1). Das ist eine numerische Festlegung, keine Aenderung einer
    Schwelle der Karte. Die Regel K0 (1e-6) bleibt.
- **Teil A klein (20/40 Fibonacci-Richtungen; diese Werte zaehlen nicht):**
  - **P0-Pfad:** fcc-Z trifft die Sollwerte auf 3,5e-8. Die [110]-Polarisationen liegen bei 1,000. Generische
    Nullmoden 0/0/2/6 = Maxwell. fcc-Gitter ohne Nullmoden ausser k = 0 (3).
  - **Keating-Pruefung [L]:** Diamant-W2 ist das Keating-Modell.
    - Mit alpha = k/3 und beta = (4/3) k_theta (Keatings Normierung, Summe ueber Atome und Nachbarn) ergeben
      C11 = (alpha + 3 beta)/a und C44 = 4 alpha beta/(a (alpha + beta)) die Werte 0,31754 und 0,16496.
    - Die Rechnung gibt rho c_L^2 = 0,31754 und rho c_T^2 = 0,16495 laengs [100].
    - Die Winkelzeilen sind damit richtig gebaut; W1 unterscheidet sich nur im Koeffizienten.
  - **Steifheit:**
    - nicht steif: Pyrochlor-Z, Diamant-Z, srs-Z, und auch srs-W1 und srs-W2
    - steif: alle uebrigen
    - srs-W1 hat laengs [110] einen exakten Nullast (c = 1,8e-13, tau = 0,57). Auf dem Gitter 16^3 haben 91 von 4095
      Punkten eine Nullmode; bei k = 0 gibt es 4 Nullmoden.
    - Das ist kein Codefehler. In einem ebenen Dreierstern sind die drei Winkel linear abhaengig, und das Kippen aus der
      Ebene aendert sie erst in zweiter Ordnung.
    - Damit wird P3 nach der Regel nicht eintreffen. Das sehe ich vor dem Einfrieren; die Regel bleibt.
  - **Kleiner Satz, P1:** kleinstes Verhaeltnis Ast 3/Ast 1 bei fcc-Z 1,414, fcc-W1 1,315, Pyrochlor-W1 1,275,
    Diamant-W1 1,487.
  - **Kleiner Satz, P3:** Schwankung der Queraeste bei fcc-W1 5,9 % und 8,7 %, Pyrochlor-W1 30 % und 17 %, Diamant-W1
    8,1 % und 5,2 %.
  - **Kleiner Satz, P2:** Pyrochlor-Z hat Nullaeste in [100] (2), [110] (1) und [111] (3), wie in Abschnitt 6 vorab
    abgeleitet.
    - tau = 1/3 in [100] und [110], wie meine Schreibtischrechnung fuer [110]; in [111] 0,34 bis 0,49.
    - Gitter 16^3: Alle 1365 Punkte mit Nullmode liegen auf <110>-Ebenen, und an allen ist N0 = Zahl der Ebenen.
- **Kette, Auswertepfad:** Kurzlaeufe bis t = 30 durchliefen auswertung.py ohne Fehler.
  - Fehlende Laeufe werden als "nicht auswertbar" bzw. "Lauf fehlt" gemeldet.
  - Die Urteile aus dem Rauch zaehlen nicht.
- **Codeaenderungen nach dem Rauch, vor dem Einfrieren:**
  - netz_a.py: (max - min)/Mittel gibt bei Mittel 0 None statt NaN.
  - auswertung.py: Laufnamen _t10/_t20 umbenannt in _dt1/_dt2.
  - laeufe.sh: neue Zeitschritte und Spurverteilung.

## 9. Einfrieren

- Eingefroren werden diese Datei und code/netz_a.py, kette.py, auswertung.py, laeufe.sh. Je Datei liegt eine Kopie
  *.eingefroren-JJJJMMTT-HHMMSS daneben, schreibgeschuetzt.
- sha256 und Zeit stehen in code/pruefsummen-einfrieren.txt; der Zeitstempel kommt aus date im selben Befehl.
- Danach aendere ich Plan und Urteilsregeln nicht mehr. Code nur bei echten Fehlern, offengelegt in ERGEBNIS.md.
