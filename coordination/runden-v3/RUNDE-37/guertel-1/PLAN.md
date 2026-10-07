# GUERTEL-1: Plan (Runde 41, zusammengelegt mit STRUKTUR-FEDERRING-1)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 14:51:08 CEST; Plantext ab 15:21:50 CEST (date).
- Karte: KARTE.md mit "Berichtigung vor dem Start" (GT2 ersetzt durch GT2a und GT2b, zwei Fadenlaengen, Zeitbox 180 min).
  Vorhersagen und Wahrscheinlichkeiten der Karte bleiben unveraendert.
- Kennzeichen: [M] eigene Mathematik; [S] an der Quelle gelesen (lokale Kopien in quellen/); [L] Gedaechtnis; [ES]
  eigener Schluss; [H] Hypothese; [F] Festlegung dieses Plans; [R] im Rauchlauf gesehen (nur Laufzeit, Sonde,
  Konvergenz). Alles hier ist eine synthetische Modellrechnung, keine Messdatenbestaetigung.
- Reihenfolge (Selbstanzeige): Der erste Rauchlauf (15:16 bis 15:17 CEST) lief, bevor dieser Text geschrieben war. Er
  gab nur Laufzeit, Sonde und Restkraft aus, keine Energien und keine Windungen (code/guertel.py, Modus rauch).

## 1. Schreibtisch und Literatur (vor jeder Hauptrechnung)

Abrufe: 3 von 10 (arXiv:1001.1778v3, arXiv:1409.3232v1, arXiv:math/0501249v1; Volltexte als PDF und Text in quellen/).
Keine Websuche.

### 1.1 Pruefung des Leitungs-Schreibtischs

1. **Phase e^(-i theta/2)** [M]: richtig. In 180-Grad-Schritten 1, -i, -1, +i, 1; Imaginaerteil 0, -1, 0, +1, 0;
   Finns Muster ist sin(theta/2). **Berichtigung:** Das -1 bei 360 Grad ist eine Phase des Zustands. Erwartungswerte
   jeder Messgroesse sind 360-periodisch; die Phase sieht man nur in Interferenz mit einem ungedrehten Teilstrahl
   (Neutroneninterferometrie 1975, Rauch u. a. und Werner u. a.) [L]. Ein Kraftverlauf mit Periode 720 Grad braucht
   deshalb ein klassisches System, das sich die Wickelklasse merkt: den angebundenen Koerper [ES].
2. **Viertakt und Nockenwelle** [L]: richtig (720 Grad Kurbelwinkel je Arbeitsspiel, Nockenwelle mit halber Drehzahl).
   **Berichtigung [M]:** Die Nockenwelle ist eine 2:1-Uebersetzung des Kreises auf sich. In der Ebene ist jede
   Uebersetzung n:1 moeglich und keine erzwungen (pi_1(SO(2)) = Z). Erst bei Drehungen im Raum ist 2:1 topologisch
   erzwungen (pi_1(SO(3)) = Z_2). Die Nockenwelle zeigt also das Halbieren, nicht seinen Grund. Naeheres mechanisches
   Gegenstueck [L]: der "Anti-Twister" (omega-2omega-Antrieb, Adams 1971; Itos Spulenplanetenzentrifuge). Dort dreht die
   Kabelfuehrung mit halber Drehzahl um den Koerper, und das Kabel verdrillt nie. Das ist der Guerteltrick als
   Dauerbewegung.
3. **Feynman-Schachbrett** [L Feynman/Hibbs; Jacobson/Schulman 1984]: Der Faktor je Richtungsumkehr ist i eps m, nicht nur
   i. "i^4 = 1" ist eine Zaehlung der Phasen. In 1+1 Dimensionen gibt es keine Drehungen im Raum; die zwei Komponenten
   sind die zwei Lichtkegelrichtungen, keine Spinzustaende unter Drehung [M]. "Ebenfalls ein Viertakt" ist deshalb eine
   Zaehl-Analogie, nicht derselbe Mechanismus. SCHACHBRETT-KAUSAL-1 hat genau diesen 1+1-Fall gerechnet (Projekt).
4. **Guerteltrick** [M, L]: pi_1(SO(3)) = Z_2 ist richtig. Bedingungen:
   - Faeden duerfen sich nicht durchdringen und nicht durch den Koerper gehen.
   - Unverdrehte Faeden (ohne Rahmung) brauchen mindestens drei. Die Kugelzopfgruppe B_2(S^2) ist Z_2 mit sigma_1^2 = 1,
     zwei Faeden lassen sich nach 360 Grad also entwirren. Fuer n >= 3 ist der volle Twist Delta^2 ein Zentralelement der
     Ordnung genau 2 (Fadell/Van Buskirk 1962; Gillette/Van Buskirk 1968) [L]. Diracs Fadenproblem: Newman 1942 [L].
   - Ein Tetraeder-Knoten mit vier Faeden liegt damit im nichttrivialen Bereich.
   - **Quelle [S]** (Staley, arXiv:1001.1778v3, S. 9 f.): "a rotation of 2pi about one axis can be continuously deformed
     into a rotation of 2pi about another axis, or into a rotation of -2pi about the original axis, without changing the
     end points"; fuer 4 pi: "keeping the first 2pi twist intact, deform the second 2pi twist ... The result is a 2pi
     twist followed by a -2pi twist, which cancels the first."
5. **Grundsaetzlich (Paritaet als zweiter Zustand, FR)**: im Ergebnis, Abschnitt "Grundsaetzlich" [H].

### 1.2 Pruefung der Ableitbarkeitsprobe aus der Berichtigung

Definition: E_min(theta) sei das Minimum der Fadenenergie ueber die Klasse c(theta), also alle Fadenzustaende, die sich
ohne Durchdringung in den gedrehten Zustand verformen lassen. Gemessen wird dagegen die kleinste Energie, die
Abkuehlen erreicht (Abschnitt 3).

1. **720-Periodizitaet [M]: gilt fuer E_min.** Die Klasse haengt nur von theta mod 720 ab, die Lage des Koerpers von
   theta mod 360. Im Modell ist jede Energie endlich (harmonische Dehnung). Die Zusammenziehung der 4-pi-Schleife als
   "Schalendrehung" (jede Kugelschale um den Koerper starr gedreht) haelt die Abstaende der Faeden auf gleichem Radius
   fest und ist durchdringungsfrei, solange die Faeden duenn gegen ihren Abstand sind. Also E_min(720) = E_min(0)
   exakt. Nicht ableitbar: ob Abkuehlen dieses Minimum findet (GT1).
2. **Spiegelebenen bei der zweizaehligen Achse [M]: gilt.** T_d hat die Spiegel x = +-y, y = +-z, x = +-z. Die Achse x
   liegt in y = z und y = -z. Probe an den Ecken: y = z laesst (1,1,1) und (1,-1,-1) fest und tauscht (-1,1,-1) mit
   (-1,-1,1); y = -z tauscht (1,1,1) mit (1,-1,-1) und laesst die beiden anderen fest. Zusaetzlich bilden die
   C2-Achsen y und z die Achse x auf -x ab, mit derselben Folge. Daraus E_min(theta) = E_min(-theta) =
   E_min(720 - theta).
3. **Berichtigung zur "Nullstelle bei 360" [M]:** Aus 2. folgt nur M(360 + x) = -M(360 - x), ein Vorzeichenwechsel bei
   360 Grad, aber keine stetige Nullstelle.
   - **Schreibtisch in fuehrender Ordnung [M, Naeherung]:** Schalendrehung mit Winkelgeschwindigkeit w(r) und
     harmonischer Energie. Der Laengenzuwachs eines Fadens in Richtung v ist proportional zu |w x v|^2, und
     Summe_i |w x v_i|^2 = (8/3) |w|^2, weil vier Tetraederrichtungen ein sphaerisches 2-Design sind
     (Summe v_i v_i^T = (4/3) I). Die Energie haengt dann nur vom Drehweg in SO(3) ab, isotrop.
   - Kleinste Energie in c(theta) proportional zu dist(theta, 720 Z)^2. Das gibt einen **Knick bei 360 Grad**: Das
     Moment springt von +M_max auf -M_max, die Kraftspitze liegt kurz vor 360 Grad, nicht bei 180 Grad.
   - Bei genau 360 Grad bilden die kleinsten Vertreter die entartete Familie der 2-pi-Drehungen um jede Achse (Staley
     [S]), in fuehrender Ordnung ein flaches Tal.
   - Finns Sinus sin(theta/2) entspraeche einer glatten Energie auf SU(2), etwa 1 - Re q = 1 - cos(theta/2) (Sehne statt
     Bogen). Der Schreibtisch erwartet also eher eine Saege als einen Sinus. Das ist eine Vorhersage, kein Befund. Die
     Kartenwahrscheinlichkeit fuer GT2a bleibt unveraendert.
4. **Allgemeine Achse [M, Naeherung]:** In fuehrender Ordnung (2-Design) haengt die Energie nur von |w| ab, also gleich
   fuer +theta und -theta um jede Achse. Dann liegt der Wechsel auch ohne Spiegel bei 360 Grad. Eine Verschiebung kaeme
   nur aus hoeheren Ordnungen (Kontakte, Wickeln, Biegung). GT2b ist damit in fuehrender Ordnung erwartet, aber nicht
   streng ableitbar.
5. **Existenz und "endlich" [M]:** Der Entwirrungsweg existiert (1.1 Punkt 4). "Endlich" in GT3 ist im Modell leer.
   - Zusatz [M, Naeherung]: In fuehrender Ordnung ist der vorwaerts ueber 360 Grad hinaus gewickelte Zustand gar kein
     lokales Minimum. Die Geodaete mit Drehwinkel > 2 pi in SO(3) hat bei 2 pi einen konjugierten Punkt (Morse-Index
     2).
   - Truege das, waere die Entwirrung vom 720-Grad-Zustand aus sperrfrei, und schon das Drehprotokoll wuerde bei 360
     Grad von selbst umklappen. Fuer dicke Faeden mit Kontakten nicht ableitbar, also gemessen.
6. **Die eigentliche Messung (nicht ableitbar):** ob Abkuehlen den Entwirrungsweg findet (GT1); Energien und Sperre
   (GT3); Zwischenrasten und Lage der Kraftspitze (GT2a); Verhalten ohne Spiegel (GT2b); die Form bei 360 Grad (Sprung
   oder glatte Nullstelle, Formmass 3.5); dazu die Grenze bei kurzer Fadenlaenge.
7. **GT0 (Ebene)** ist in der idealen Rechnung topologisch ableitbar. In der Ebene geht die Drehachse durch den
   Koerper, die Windung ist ganzzahlig und erhalten. GT0 prueft deshalb nur, ob der Ausschluss haelt.

### 1.3 Literatur zu Federring und Drehungs-Cluster

Steht in RUNDE-37/struktur-federring-1/BERICHT.md (Quellen dort und hier in quellen/).

## 2. Modell [F]

- **Einheiten:** Koerperradius 1, Energie-Einheit eps = 1 (WCA).
- **Koerper:** starre Kugel vom Radius A = 1,0 als Ausschlussform. Die vier Ecken des Tetraeders auf ihr geben die
  Ansatzrichtungen u_i = (+-1, +-1, +-1)/sqrt(3) mit gerader Zahl von Minuszeichen. Die Faeden beginnen bei
  R_ATT = 1,1 entlang R(theta) u_i, also im Kontaktabstand.
  - Warum eine Kugel statt eines Tetraeders als Ausschlussform: glatte Wand, exakte Durchdringungsprobe. Die
    T_d-Symmetrie kommt allein aus den Ansatzpunkten.
- **Anker:** bei R_ANK = 2,9 entlang u_i; Aussenwand bei R = 3,0. Die Faeden bleiben in der Schale; das ist die
  Topologie S^2 x I. Die Aussenwand steht fuer das uebrige Netz.
- **Faeden:** Ketten aus Kapselsegmenten, Dicke sigma = 0,2. Gerader Abstand d = 1,8.
  - Konturlaenge 1,3 d = 2,34 mit 12 Segmenten (b0 = 0,195).
  - Konturlaenge 1,8 d = 3,24 mit 16 Segmenten (b0 = 0,2025).
- **Energie:**
  - Dehnung (k_s/2)(l - b0)^2 mit k_s b0^2 = 20.
  - Biegung k_b Summe (1 - t_k . t_k+1) mit k_b = 2.
  - Einspannung an beiden Enden: k_b (1 - t_erst . R(theta) u_i) und k_b (1 - t_letzt . u_i).
  - Faden-Faden: WCA im Mittellinienabstand der Segmente, Kontakt bei sigma. Gleicher Faden erst ab Segmentabstand 3.
  - Faden-Koerper: WCA in (Abstand Segment-Mittelpunkt minus A), Kontakt bei sigma/2.
  - Aussenwand: WCA auf Perlen in (R - r), Kontakt bei sigma/2.
- **Achsen:**
  - Zweizaehlig: x = (1,0,0).
  - Allgemein: n_G = (4,2,1)/sqrt(21), vorab festgelegt. Keine Spiegelebene von T_d enthaelt n_G (Betraege der
    Komponenten paarweise verschieden). Keine C2-Achse steht senkrecht auf n_G (alle Komponenten ungleich null).
    Winkel zu den Ecken: 28,1, 82,8, 112,2 und 129,1 Grad.
- **Ebene (Kontrolle GT0):**
  - Vier Richtungen (0, +-1, +-1)/sqrt(2) in der Ebene senkrecht zu x (Projektionen der Ecken).
  - Drehung um x; alle Kraefte und das Rauschen ohne x-Anteil. Die Faeden bleiben exakt in der Ebene.
- **Startzustand:** gerade, gestauchte Faeden mit kleiner Stoerung (Saat fest je Fadenlaenge). Sie knicken beim ersten
  Relaxieren aus; die Faeden sind schlaff.

## 3. Protokoll und Messgroessen [F]

### 3.1 Drehprotokoll

- Alle drei Systeme (zweizaehlig, allgemein, Ebene) in einem Stapel je Fadenlaenge.
- Ablauf:
  - Start mit FIRE (hoechstens 5000 Schritte, Restkraft-Ziel 1e-3).
  - Drehen in Schritten von 1 Grad bis 1440 Grad, nach jedem Schritt FIRE mit hoechstens 80 Schritten.
  - Auf den Gitterwinkeln 0, 30, ..., 720, 1080, 1440 FIRE mit hoechstens 1500 Schritten; dort E_prot, Moment M_prot
    und Windungen W_i speichern, ebenso den Zustand.
  - Moment und Energie werden zusaetzlich nach jedem 1-Grad-Schritt gespeichert (Protokollweg, beschreibend).
- Rauchlauf 1 hatte 4-Grad-Schritte. Dabei schlug die Sonde in der Ebene an (Abschnitt 7), daher 1 Grad.

### 3.2 Drehmoment

- M(theta) := dE/dtheta bei festgehaltenen freien Perlen (zentrale Differenz, h = 1e-4 rad).
- Das ist das Moment der Fadenkraefte und der Einspannmomente um die Drehachse, das man zum Halten aufbringen muss.
- Am relaxierten Zustand ist es nach dem Einhuellendensatz gleich dE/dtheta entlang des glatten Asts. Einheit Energie
  je rad.
- Vorzeichen: Finns "0 +1 0 -1 0" entspricht M > 0 in (0, 360) und M < 0 in (360, 720).

### 3.3 Abkuehlen

- Start: der gespeicherte Protokollzustand je Gitterwinkel. Je Winkel 5 Saaten, alle Winkel eines Systems in einem
  Stapel (27 x 5 = 135).
- Ebene (nur Kontrolle GT0): nur die Winkel 0, 180, 360, 540, 720, 1080, 1440 (7 x 5 = 35), um Rechenzeit zu sparen.
- Ueberdaempftes Langevin, T von T0 = 0,5 linear auf 0 in nL = 6000 Schritten. dt0 = 2e-4; Drift hoechstens 0,01 je
  Schritt; Gesamtschritt je Perle hoechstens 0,02.
- Danach FIRE mit hoechstens nF = 2500 Schritten, Restkraft-Ziel 1e-3.
- Endenergie E_end je Saat. Bei 720 Grad werden alle 25 Schritte Rahmen fuer die Sperrbestimmung gespeichert.

### 3.4 Messgroessen

- **E_min(theta)** := kleinste E_end ueber die gueltigen Saaten (Sonde bestanden, 4.2); dazu Mittel E_quer, SE =
  sd/sqrt(n).
- **Weg kleinster Energie:** je Gitterwinkel die gueltige Saat mit kleinster E_end; M_best(theta) ist ihr Moment.
- **Verdrillungsenergie:** dE_360 := E_quer(360) - E_quer(0).
- **Sperre S (GT3)**, in dieser Reihenfolge:
  - (a) Ist der Protokollzustand bei 720 Grad schon entwirrt (Mittel |W_i| < 0,5), gilt S := 0 ("Entwirrung beim
    Drehen ohne Sperre").
  - (b) Sonst Stringmethode (vereinfachte Fassung, E/Ren/Vanden-Eijnden 2007 [L]) zwischen dem Protokollzustand bei 720
    Grad (Start des Abkuehlens) und dem gueltigen entwirrten Endzustand bei 720 Grad mit kleinster Energie.
    - Anfangspfad: die Langevin-Rahmen dieser Saat.
    - 61 Bilder, 1500 Iterationen, Schritt 1e-4, Verschiebung je Perle hoechstens 0,005, Umverteilung alle 5
      Iterationen.
    - S := max_k E_k - E_0.
    - Gueltig nur bei bestandener Pfadpruefung: jedes Bild in den Grenzen; zwischen Nachbarbildern
      d_min - 2 delta > 0 und rho_min - delta - A > 0.
  - (c) Entwirrt keine Saat, ist S "nicht bestimmt".
- **Lesart H (berichtet, nicht urteilsbildend):** H := max_k E_k - E_min(0), die Hoehe ueber dem Grundzustand.
- **Topologie-Probe:** Windung W_i jedes Fadens um die Drehachse, vom Anker zum Ansatz, vor und nach dem Abkuehlen.
  - Vorwaertsast: W_i ~ theta/360. Entwirrt bei 720 Grad: Mittel |W_i| < 0,5.
  - In 3D ist W_i keine Invariante, weil Faeden die Achsenlinie kreuzen duerfen; genau so sieht man die Entwirrung. In
    der Ebene ist W_i invariant.

### 3.5 Formmass bei 360 Grad (beschreibend, vorab festgelegt)

- Auf dem Weg kleinster Energie: J := min(|M_best(330)|, |M_best(390)|) / max |M_best| ueber 30 bis 690 Grad.
  - "Sprung", wenn J >= 0,5 und M(330) > 0 > M(390).
  - "glatt", wenn J <= 0,25.
  - Sonst "unklar".
- Dazu die Korrelation von M_best (30 bis 690 Grad) mit sin(theta/2) und mit der Saege (theta fuer theta < 360,
  theta - 720 fuer theta > 360).

## 4. Kontrollen [F]

1. **Ebene (GT0):** wie Abschnitt 2, gleiche Laeufe und Regeln.
2. **Durchdringungsprobe** je System und Schritt, ueber Drehen, Abkuehlen und Relaxieren:
   - (i) Mittellinienabstand der Faden-Faden-Paare mit Energie >= 0,5 sigma = 0,1 (Ausschlussgrenze).
   - (ii) Fuer alle Segmentpaare ohne gemeinsame Perle (auch Abstand 2 im selben Faden): Abstand vor dem Schritt minus
     2 delta > 0, mit delta = groesste Perlenverschiebung im Schritt. Bei linearer Bewegung kann sich dann waehrend
     des Schritts nichts kreuzen.
   - (iii) Segmentabstand zum Koerpermittelpunkt >= A = 1, dazu rho_vor - delta - A > 0.
   - (iv) Perlen bei r <= R = 3.
   - Folgen:
     - Eine Saat, die (i) bis (iv) verletzt, ist ungueltig ("Durchtunneln moeglich") und faellt aus E_min.
     - Sind weniger als 80 % der Saaten eines Winkels gueltig (oder weniger als 2), ist der Winkel "nicht auswertbar".
     - Im Protokoll wird die Sonde je Intervall zwischen Gitterwinkeln gefuehrt und berichtet.
3. **Topologie-Probe:** W_i vor und nach dem Abkuehlen; in der Ebene muss W_i = k bei k mal 360 Grad bleiben
   (berichtet).
4. **Gegenprobe der Sonde:**
   - Ebene und zweizaehlige Achse mit ausgeschaltetem Faden-Faden- und Faden-Koerper-Ausschluss: Drehen bis 720 Grad,
     dann Abkuehlen.
   - Erwartung: Die Sonde schlaegt an, und die Windungen der Ebene gehen verloren. Sonst taugt die Sonde nicht.

## 5. Urteilsregeln [F] (mechanisch in code/auswertung.py)

Allgemein:
- Nur gueltige Saaten.
- Urteil fuer die Konturlaenge 1,8 d (Karte: "das Urteil zaehlt fuer den groesseren Wert"). 1,3 d wird mit
  denselben Regeln als Grenze berichtet.
- GT1 und GT3 urteilen auf der zweizaehligen Achse; die allgemeine Achse wird berichtet.
- "Innerhalb 10 %" heisst relativ zu E_min(0).
- "SE ueber Saaten": SE_komb = sqrt(SE_a^2 + SE_b^2) aus der Streuung der Endenergien je Winkel.

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| GT0 (Ebene) | fuer k = 1, 2: E_quer(k 360) - E_quer((k-1) 360) > 3 SE_komb, und E_min(720) > 1,10 E_min(0); 1080 und 1440 nur berichtet (Grund 7.3) | E_min streng steigend ueber 0, 360, 720, 1080, 1440 und E_min(k 360) > 1,10 E_min(0) fuer k >= 1 |
| GT1 (zweizaehlig) | (a) E_min(720) <= 1,10 E_min(0); (b) E_quer(360) - E_quer(0) >= 3 SE_komb; (c) bester 720-Zustand entwirrt (Mittel abs W_i < 0,5) | abs(E_min(720) - E_min(0)) <= 0,10 E_min(0) und E_min(360) - E_min(0) >= 3 SE_komb |
| GT2a (zweizaehlig) | M_best > 0 auf 30..330 Grad; E_min nicht fallend bis auf 2 % von abs(E_min(360) - E_min(0)) je Schritt (0..360); argmax M_best (30..330) in [135, 225] | wie Plan, aber E_min streng steigend |
| GT2b (allgemein) | genau ein Vorzeichenwechsel von M_best auf 30..690 Grad (+ vorher, - nachher); Nullstelle (linear zwischen den Nachbarpunkten) in [330, 390]; Spitze vor der Nullstelle in [135, 225] ("dasselbe Muster") | gleich (Nullstelle und "dasselbe Muster"); zusaetzlich berichtet: nur Nullstelle |
| GT3 (zweizaehlig) | S (3.4) < dE_360: eingetroffen; S >= dE_360: nicht eingetroffen; S nicht bestimmt: nicht auswertbar | gleich ("endlich" ist leer) |

- Eingangsbedingung: Fehlt ein benoetigter Winkel oder ist er nicht auswertbar (4.2), lautet das Urteil "nicht
  auswertbar".

## 6. Laufplan [F]

- Nur .69, Spur cpu, ueber kleintest.sh; je Lauf <= 10 min, 1 Thread, 4 GB. Ordner:
  /home/fmh/fmhc-physics-remote/runde41-guertel/ (code/, rauch/, lauf/).
- Hauptlaeufe, nacheinander:
  - Protokoll L = 1,8 und L = 1,3 (dtheta 1 Grad, nrelax 80, ngitter 1500, tmax 1440).
  - Abkuehlen fuer (L, System) mit L in {1,8, 1,3} und System 0, 1, 2 (sechs Laeufe; nL 6000, nF 2500, T0 0,5,
    5 Saaten; Ebene nur auf den Winkeln aus 3.3).
  - Sperre fuer (L, System) mit System 0, 1 (61 Bilder, 1500 Iterationen).
  - Gegenprobe L = 1,8 (bis 720 Grad, nL 2000, nF 1000).
  - Auswertung (code/auswertung.py).
- Saatbasis 0. Die Zufallsfolge ist je (System, L) fest (numpy default_rng([41, System, 10 L, 0])).
- Ein Hauptlauf je Teil. Muss ein Lauf wegen Zeitueberschreitung oder Absturz wiederholt werden, steht das als
  Nachtrag mit Grund in Abschnitt 8. Die Werte des abgebrochenen Laufs werden nicht angesehen.

## 7. Rauchlauf (Laufzeit, Stabilitaet, Sonde) [R]

Gesehen wurden nur Laufzeiten, Sondenwerte und Restkraefte. Energien und Windungen standen nicht in den Ausgaben.

### 7.1 Rauchlauf 1 (13:16:15 bis 13:17:41 UTC)

- Protokoll bis 720 Grad, 4-Grad-Schritte, 100 FIRE-Schritte je Schritt.
- Abkuehlen B = 6 mit nL = 1000, nF = 500 bei 720 Grad. String als Maschinenprobe (21 Bilder, 50 Iterationen).
- Laufzeit je Energieauswertung: B = 3: 1,8 bis 2,1 ms; B = 135: 27 bis 36 ms. String mit M = 21: 4 bis 5 ms je
  Iteration.
- **Sonde:**
  - 3D-Systeme bestanden (kleinster Kreuzungsrand 0,016 bei L = 1,3, allgemeine Achse).
  - Ebene schlug in beiden Laengen an (Rand < 0). Ursache: Die Ansatzperle springt je 4-Grad-Schritt um 0,077 in eng
    gewickelte Lagen; Restkraft danach bis 6e4.
- Folge: 1-Grad-Schritte und 80 FIRE-Schritte je Schritt (Code-Vorgaben geaendert, vor jedem Hauptlauf).

### 7.2 Rauchlauf 2 (13:20:04 bis 13:24:23 UTC; 1-Grad-Schritte bis 720 Grad, nL = 1000, nF = 1000)

- **L = 1,8:** alle drei Systeme bestehen die Sonde im Protokoll (min Faden-Faden 0,139 bis 0,181, Raender > 0,08) und
  im Abkuehlen.
- **L = 1,3:**
  - 3D-Systeme bestehen.
  - Die Ebene verletzt die Ausschlussgrenze: min 0,080 < 0,1 im Protokoll, 0,077 im Abkuehlen bei 720 Grad. Die
    Kreuzungsraender bleiben > 0. Restkraft bis 2e6 nach Schritten und 2e5 nach FIRE.
- Laufzeit: Protokoll bis 720 Grad 108 bzw. 128 s. Langevin B = 6: 3,3 bzw. 4,6 ms je Schritt. B = 135: 27 bzw. 40 ms
  je Auswertung.
- Daraus geschaetzt:
  - Protokoll bis 1440 Grad etwa 6 min je Laenge.
  - Abkuehlen B = 135 mit nL = 6000 und nF = 2500 hoechstens 6 min.
  - Unter 10 min je Lauf.
- Gegenprobe-Code (Kurzlauf bis 90 Grad) laeuft (rc = 0); Werte nicht angesehen.

### 7.3 Folgerung fuer GT0 (vor jedem Hauptlauf)

- **Packungsgrenze [M]:** In der Ebene kreuzt eine Linie vom Koerper zur Wand bei W Windungen 4 W Faeden. Bei
  Kontaktabstand sigma braucht das 4 W sigma <= etwa 2,0 (Schale 1,1 bis 2,9 plus sigma), also W <= 2,5.
- 1080 und 1440 Grad (W = 3, 4) gehen in der Ebene nur mit Zusammendruecken unter den Kontaktabstand. Bei L = 1,3
  zwingt schon 720 Grad die Dehnung so weit (Faktor etwa 6 bis 9 bei 12 Segmenten), dass die Ausschlussgrenze reisst.
- Deshalb urteilt GT0 nach Plan ueber 360 und 720 Grad. 1080 und 1440 werden mit Sondenstatus berichtet. Das
  Wortlaut-Urteil verlangt weiter alle Vielfachen und lautet "nicht auswertbar", wenn einer fehlt.
- Keine Aenderung an Modell oder Sonde.

## 8. Nachtraege nach dem Einfrieren

### Nachtrag 1 (2026-10-04 15:45:27 CEST, nach Sicht auf abkuehlen-L1.8-s0 und sperre-L1.8-s0)

- **Befund:**
  - Bei 720 Grad endet die zweizaehlige Achse (L = 1,8) in allen Saaten im Zustand W = (1, 0, 1, 0): zwei Faeden
    entwirrt, zwei mit einer Windung.
  - Exakt ist dort Mittel |W_i| = 0,5, also nach Abschnitt 3.4 "nicht entwirrt" (Regel: < 0,5).
  - Der eingefrorene Code vergleicht aber den Gleitkomma-Mittelwert. Fuer Saat 0 ergibt er 0,49999999999999994 und
    zaehlt die Saat als entwirrt. Daraufhin rechnete der Sperrlauf einen String zwischen zwei Zustaenden derselben Art
    (beide W = (1, 0, 1, 0)), der kein Entwirrungsweg ist (S = 0,24).
- **Pruefung:** Bei 720 und 1440 Grad sind alle W_i bis auf hoechstens 3,3e-16 ganzzahlig (Anfangs- und Endpunkt jedes
  Fadens haben dort denselben Azimut).
- **Berichtigung, nur in der Auswertung; Code unveraendert:**
  - Bei 720 und 1440 Grad wird die Regel "Mittel |W_i| < 0,5" auf die auf ganze Zahlen gerundeten W_i angewandt.
  - Betroffen sind GT1 Teil (c), GT3 (Pfad (a) Protokoll und Pfad (b) Kandidatenwahl) und die Zahl der entwirrten
    Saaten.
  - Im Ergebnis stehen das mechanische Code-Urteil und das berichtigte Urteil nebeneinander. Gueltig ist das
    berichtigte, weil es die Regel des Plans so anwendet, wie sie geschrieben ist.
- **Keine Lockerung:** Die Berichtigung entfernt ein falsch positives "entwirrt"; sie macht kein Urteil leichter.
