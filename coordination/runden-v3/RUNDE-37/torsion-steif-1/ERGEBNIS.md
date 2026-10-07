# TORSION-STEIF-1: Ergebnis (Runde 45, Code-Agent fuer claude-primary)

- **Zeiten (alle per date):**
  - Start 2026-10-05 04:19:11 CEST.
  - Plan und Code eingefroren 04:38:49, Stempel 20261005-043849. SHA256 lokal und auf der .69 gleich (sha256sum -c: OK).
  - Hauptlauf 04:38:57 bis 04:40:17 (kleintest.sh, Spur cpu, 78 s, rc 0).
  - Auswertung 04:40:17 bis 04:40:18 (Spur cpu11, rc 0).
  - Nachtraege nach Sicht: 04:43:19 und 04:46:13 (Spur cpu11).
  - Text ab 04:46:29.
- **Kennzeichen:** [E] Rechnung, [M] eigene Mathematik, [S] an der Quelle gelesen, [L] Gedaechtnis, [P] Projektdatei,
  [H] Hypothese. **Alles ist synthetisch** (Modellrechnung auf einem idealen Gitter, keine Messdaten).
- **Urteile:** Sie stammen nur aus dem eingefrorenen Code (code/auswertung.py.eingefroren-20261005-043849).
  Abschnitte mit "Nachtrag" kamen nach Sicht und aendern kein Urteil.

## 1. Ergebnis zuerst

1. **Die Torsion ist auf dem flachen Kuhn-Gitter nicht algebraisch festgelegt (TS1 eingetroffen, Klasse "Nullband").**
   - Q(k) hat an allen 3915 ausgewerteten k != 0 Nullmoden: 4 bei allgemeinem k, 5 auf Gamma-X, 6 an X und M, 13 bei
     k = +-(pi/2)(1,1,1) [E].
   - Die Nullen liegen bei <= 1,3e-15 relativ. Die naechste Mode liegt bei 1,3e-4 bis 0,18 (500 Zufalls-k).
2. **Die volle Matrix hat ueber die Eichbahnen hinaus Nullmoden (TS2 verfehlt).**
   - Es sind 25 statt 21 bei allgemeinem k.
   - Die vorab hergeleitete Identitaet "Nullmoden H = 18 + Nullmoden R_ss + Nullmoden Q" gilt an allen 3915 k ohne
     Ausnahme [M, E]. TS1 und TS2 haengen also logisch zusammen.
3. **TS0 (Kontrolle) ist nach der eingefrorenen Regel verfehlt, aber nur wegen meiner Auswerteformel.**
   - Ein Band auf den Linien um eine Gelenkkante dreht sich genau um den Fehlwinkel: Abweichung <= 2,1e-14 in allen 28
     Faellen mit delta != 0, Achse parallel zur Kante auf 1,1e-14, Vorzeichen wie Gl. 74 [E].
   - Die Eichnullmoden (Verschiebung je Ecke und SO(3) je Tetraeder) sind exakt reproduziert (Residuum <= 2,1e-15).
   - Verfehlt wurde allein die Schranke 1e-8 in 6 flachen Faellen (delta = 0). Dort liefert arccos bei psi -> 0 nur
     ~2e-8 Genauigkeit. Mit atan2 (Nachtrag) ist psi <= 8e-16.
4. **Nachtrag (nach Sicht): Woher die 4 Nullmoden kommen** [E, M].
   - Es sind reine Rahmendrehungen omega_i je Tetraeder, und zwar die, deren Summe um jede Kante parallel zu dieser
     Kante liegt. Die Verbindung dazu ist x = D omega: Weitzenboeck-Torsion, krummungsfrei.
   - Zaehlung: 18 Drehungen gegen 14 Bedingungen, also mindestens 4 je Zelle. **Das war vorab ableitbar; ich habe es
     vor der Rechnung nicht gesehen** (Selbstanzeige 1).
   - Ein Logarithmus-Artefakt ist ausgeschlossen [M]. Die Mittelung ist nicht die Ursache: Die Einzelstart-Wirkung hat
     8 statt 4 Nullmoden [E].
5. **Rahmenenergie (beschreibend):** Mit der Guertel-Bindungsenergie auf der Holonomie (kappa |x|^2) bekommen die
   Weitzenboeck-Richtungen Energie 2 kappa |D omega|^2 ~ kappa k^2 [E, vorab M].
   - Das ist der Cosserat-Typ.
   - Q + 2 kappa wird dabei zwischen den Gitterpunkten auf Flaechen im k-Raum singulaer (Traegheitswechsel auf den
     Linien).
   - 4 Nullmoden der vollen Matrix bleiben: Rahmen gedreht bei h = 1, die diese Energie nicht sieht.

## 2. Urteilstabelle

| Nr | Vorhersage (Karte, unveraendert) | Wahrsch. | Urteil nach Kartenwortlaut | Urteil nach Plan | Beleg |
|---|---|---|---|---|---|
| TS0 | [Zusatz Leitung] Kontrolle: Arm "Linien" gibt Rahmendrehung = Fehlwinkel auf 1e-8; ohne Torsion reproduziert der Code die Eichnullmoden (Verschiebung je Ecke) | 85 % | **verfehlt.** (b) Eichnullmoden erfuellt: Translation <= 2,1e-15, Drehung <= 2,6e-17, Rang 21 an allen k != 0. (a) In 6 von 35 Faellen ist ||psi| - |delta|| = 2,1e-8 bis 3,0e-8 > 1e-8: flache Faelle mit delta <= 1,8e-15, arccos-Rundung | **verfehlt** (wie Wortlaut). Die Planzusaetze sind erfuellt: Vorzeichen +delta auf 2,1e-14, flacher Stern delta <= 1,8e-15, Drehungseichung <= 2,6e-17 | auswertung.json "TS0"; Nachtrag atan2: psi <= 8,0e-16 |
| TS1 | [H] Q(k) hat fuer k != 0 mindestens eine Nullmode; die Torsion ist auf dem Gitter dann nicht algebraisch festgelegt (woertlich) | 45 % | **eingetroffen.** Nullmoden an 3915 von 3915 k != 0 (Gitter 12^3, 7 Linien, 500 Zufall, 6 kleine k) | **eingetroffen**, Klasse (i) "Nullband": allgemein 4 (Traegheit 15/4/17), Gamma-X 5, X und M 6, (pi/2)(1,1,1) 13; Gamma 12 | auswertung.json "TS1" |
| TS2 | [H] Die volle Matrix hat ausser den Eichbahnen keine Nullmoden (woertlich) | 55 % | **verfehlt.** Nullmoden H: 25, 26, 27 oder 34 bei Eichrang 21. Eichresiduen <= 2,1e-15. Zahl negativer Eigenwerte von H: 18, nur an k = +-(pi/2)(1,1,1) 15 | **verfehlt.** Planzusatz erfuellt: Identitaet an allen k (0 Abweichungen), KX <= 1,9e-15 | auswertung.json "TS2" |

**Bedeutung nach der Karte (woertlich, angewandt):**
- "TS1 trifft ein: Die Torsion ist auf dem Netz unbestimmt. Vor jeder Spin-Kopplung ist dann zu klaeren, ob das ein
  Artefakt der Mittelung bzw. des Logarithmus ist."
- Zum Logarithmus: Ln h und (h - h^T)/2 sind bis zur 2. Ordnung gleich. Fuer diese lineare Frage spielt der
  Logarithmus also keine Rolle [M, vorab, PLAN 1.3].
- Zur Mittelung (Nachtrag 2) [E]: Die folgerichtige Einzelstart-Wirkung hat 8 Nullmoden je Zelle statt 4. Die Mittelung
  halbiert den Kern, erzeugt ihn aber nicht.
- [M] Die Ursache ist eine Zaehlung: Rahmen je Tetraeder gegen Kantenrichtungen (Abschn. 3.3). Sie gilt fuer jede
  Gewichtung der Startpunkte, denn KX gilt je Startpunkt (Nachtrag 2) und damit fuer jede Mischung. Also bleiben
  mindestens 4. Gerechnet [E] sind nur die zwei Faelle "gemittelt" (4) und "Einzelstart" (8).
- **[Zusatz Leitung] Fuer Finn:**
  - Baender auf den Linien messen die Kruemmung. Physikalisch ist das bestaetigt; das Urteil TS0 ist wegen der
    Auswerteformel formal verfehlt.
  - Baender zwischen den Zellen tragen Torsion. Die Einstein-Cartan-Wirkung laesst davon 4 Richtungen je Zelle frei,
    und zwar genau Torsion vom Typ "Rahmen gegeneinander verdreht, keine Kruemmung". Das ist der Typ des Guertel-Felds.
  - Eigene Dynamik hat sie in der reinen Wirkung nicht (Energie null). Mit Guertel-Energie bekommt sie eine (Abschn. 5).

## 3. Q(k) ueber k, Nullmoden, volle Matrix gegen Eichbahnen [E]

### 3.1 Spektrum von Q(k) (36 x 36)

- **Allgemeines k** (500 Zufallspunkte, zwei allgemeine Linien, kleine k):
  - Traegheit (negativ, null, positiv) = (15, 4, 17).
  - Q ist spurfrei (|Spur| = 0) und indefinit, wie vorab hergeleitet [M].
  - Das Spektrum ist nicht symmetrisch zu null (Abweichung bis 0,73).
  - Groesster Betrag 2,73205 (= 1 + sqrt 3 auf 6 Stellen; Beobachtung, nicht hergeleitet).
  - Beispiel Zufalls-k Nr. 0: Eigenwerte von -2,08 bis +1,80, vier Nullen, kleinste von null verschiedene Betraege
    0,014 und 0,016.
- **Kleine k** (Richtung (1, 0.37, 0.61)): 4 exakte Nullen, 2 Moden ~ k^2 (0,08 k^2 und 0,23 k^2), 6 Moden ~ k (0,19 k
  bis 0,28 k), dann eine Luecke bei 0,085.
  - Bei Gamma gehen die 2 + 6 gegen null; zusammen mit den 4 sind das die **12 Nullmoden bei k = 0**, Traegheit
    (12, 12, 12).
- **Symmetrielinien** (Nullzahl, je 241 Punkte):

| Linie | Nullmoden von Q |
|---|---|
| Gamma-X | 5 auf der ganzen Linie, 6 an X |
| Gamma-M | 4, an M 6 |
| Gamma-R | 4, an (pi/2)(1,1,1) 13, an R 4 |
| X-M, M-R | 4, an X und M 6 |
| allgemeine Richtungen | 4 durchgehend |

- Gitter 12^3: Traegheiten (15,4,17), (15,5,16), (15,6,15), und (12,13,11) an k = +-(pi/2)(1,1,1).
- **Trennschaerfe:**
  - Groesster als Null gezaehlter Wert ueber alle k != 0: |lambda| / max|lambda| = 1,3e-15. Schranke 1e-9.
  - Fuenfter kleinster Betrag an Zufalls-k: 1,3e-4 bis 0,18. Kein Grenzfall zur Schranke 1e-9.

### 3.2 Volle Matrix H(k) = [[0, M], [M^+, Q]] (61 x 61) gegen die Eichbahnen

- **Eichvektoren:** 18 Drehungen je Tetraeder und 3 Verschiebungen je Ecke, Rang 21 an allen k != 0.
  - Residuum ||H Z|| / (||H|| ||Z||) <= 2,1e-15 (Translation) und <= 2,6e-17 (Drehung).
  - Bei Gamma ist der Rang 18.
- **Nullmoden von H:**
  - allgemein 25 = 21 + 4, Traegheit (18, 25, 18)
  - Gamma-X 26, X und M 27, (pi/2)(1,1,1) 34
  - Gamma 36 = 18 Drehungen + 6 affine + 12 von Q
- **Identitaet** dim ker H = dim ker R + dim ker Q (PLAN 1.4) an allen 3915 k: 0 Abweichungen.
  - R_ss hat ueberall genau 3 Nullmoden (Traegheit 3/3/1).
- **Torsionsfreier Sektor (KR):** R_ss ist die linearisierte Regge-Wirkung in s = l^2.
  - Bei |k| = 1e-3 bis 0,4: Gittermode -3,4999 bis -3,419, zwei negative ~ k^2 (0,41 k^2 und 0,33 k^2), eine positive
    ~ k^2 (0,23 k^2), 3 Nullen.
  - Bei Gamma: 6 Nullen (affin) und -3,5.
  - Das stimmt mit der 3D-Kontrolle von REGGE-4D-1 (Gittermode 3,41 bis 3,50, 2 + 1 k^2-Moden) ueberein, mit
    umgekehrtem Vorzeichen, weil dort H = -Hess gilt [P].

### 3.3 Nachtrag (nach Sicht): Herkunft der Nullmoden [E, M]

- **Gerechnet:** 47 Punkte (nachtrag-69/nachtrag_kern.json).
- **Befund:**
  - ker Q(k) = J(ker M^+) an allen 47 Punkten. Die Dimensionen sind gleich (4, bzw. 5 auf Gamma-X). Q J N = 1,4e-16.
    Der Hauptwinkel ist <= 4e-8; das ist die sqrt(eps)-Grenze der cos-Formel.
  - ker M^+ hat Dimension 7: 3 Translationen + 4.
  - Die 4 liegen nach Abzug der Translationen **vollstaendig in den Rahmendrehungen Omega**, ihr ds-Anteil ist 0.
- **Erklaerung [M]:**
  - M^+ g = 0 heisst: Die ueber die Tetraeder um jede Kante gemittelte Kantenvektor-Stoerung ist geschlossen.
  - Fuer reine Rahmendrehungen heisst das: (Summe der omega_i um Kante B) x l_B = 0 fuer alle 7 Kantentypen. Das sind
    14 Bedingungen fuer 18 Drehungen, also **mindestens 4 je Zelle**.
  - Wegen M^+ = -Q J (KX) liegt dann J g = D omega im Kern von Q. D ist bei k != 0 injektiv.
  - Physikalisch sind das Weitzenboeck-Konfigurationen: Die Rahmen sind gegeneinander verdreht, die Holonomie um jede
    Kante bleibt 1 (keine Kruemmung). Die mittlere Kantengeometrie bleibt unveraendert, die Wirkung merkt es zur
    2. Ordnung nicht.
  - Allgemein [M, H]: 3T - 2E = T - 2V je Ecke (mit E = V + T aus Euler und F = 2T). Kuhn: 6 - 2 = 4. Fuer jede
    3D-Triangulierung mit T > 2V waere die Zahl positiv; das ist nicht an einer zweiten Triangulierung gerechnet.
- **Nachtrag 2: folgerichtige Einzelstart-Wirkung** (Start je Gelenk in T[0], Q und M passend; 31 Punkte,
  nachtrag-69/nachtrag_einzelstart.json):
  - KX gilt auch hier (<= 9,1e-16). Damit ist die Behauptung "torsionsfrei ist je Startpunkt stationaer" bestaetigt.
  - Eichresiduum 1,6e-17.
  - dim ker Q = **8**, dim ker M^+ = 9, Rang J(ker M^+) = 6; Nullmoden H = 29 = 21 + 8.
  - Die Mittelung verkleinert den Kern also, erzeugt ihn aber nicht.

## 4. Arm "Linien" (Baender auf den Kanten) [E]

- **Aufbau:** alle 7 Kantentypen (m = 6 oder 4) mit je 5 Einstellungen:
  - flach
  - Gelenkquadrat mal (1 +- 0,05)
  - dazu 1 % bzw. 2 % Zufallsstoerung der uebrigen Sternkanten
  - jeder Tetraeder einzeln eingebettet und zufaellig gedreht (Eichung)
  - Holonomie je Grenzflaeche nach Gl. 28
- **Fehlwinkel:** delta von -0,267 bis +0,474. Laengeres Gelenk gibt delta < 0, wie erwartet, weil die Diederwinkel
  wachsen.
- **Ergebnis:**
  - Rahmendrehung psi_signed = delta auf <= 2,1e-14 in allen 28 Faellen mit delta != 0.
  - Achse parallel zur Gelenkkante auf <= 1,1e-14, Orthogonalitaet der Holonomien <= 2,5e-15.
  - Bandwinkel = |delta|.
  - Vorzeichen wie Gl. 74: Drehung um +delta um l^ bei Umlauf nach der Rechten-Hand-Regel.
- **Flache Faelle:** delta <= 1,8e-15. Gemessenes |psi| (arccos) 2,1e-8 bis 3,0e-8, weil 1 - cos psi = 2 bis 4 ulp.
  Das ergibt TS0 "verfehlt". Mit atan2 (Nachtrag 1) ist psi <= 8,0e-16.
- **Lesart:**
  - Das Ergebnis war vorab ableitbar (Karte: "Kontrolle [vorab ableitbar]").
  - Es zeigt nur, dass der Code die torsionsfreie Holonomie und den Fehlwinkel richtig baut.
  - Ein Band auf den Linien liest die Kruemmung, nicht die Torsion.

## 5. Arm "Rahmenenergie" (beschreibend) [E; Teile vorab M]

- **Modell:** Guertel-Bindungsenergie auf der Holonomie, sum_t 2 kappa (1 - cos |x_t|), zur 2. Ordnung Q -> Q + 2 kappa.
  kappa in {0; 0,25; 1}, auf 5 Linien ab Gamma und 6 kleinen k.
- **Weitzenboeck-Richtungen x = D omega** (18 je Zelle):
  - kappa = 0: Energieform P^+ Q P = 0 auf <= 2,2e-16. Ohne Zusatzenergie haben diese Rahmenverdrehungen keine Energie
    (vorab [M]).
  - kappa > 0: P^+ Q_kappa P = 2 kappa P^+ P auf <= 1,3e-15. Die kleinste Mode waechst wie k^2 (kappa = 1: 6,0e-7 bei
    k = 1e-3, 0,096 bei 0,4), die groesste ist 12 kappa.
  - Damit ist das ein ausbreitungsfaehiges Rahmenfeld vom Cosserat-Typ (statisch, k^2-Steifigkeit), so wie das
    Guertel-Feld. Das war vorab ableitbar.
- **Nicht vorab ableitbar:**
  - kappa = 0,25: An keinem ausgewerteten k ist Q + 2 kappa exakt singulaer (kleinster Betrag 4,8e-5). Auf allen
    Linien wechselt aber die Zahl negativer Eigenwerte, 2 bis 4 Mal je Linie (6 bis 12 negative). Eigenwerte
    durchlaufen also zwischen den Punkten null, und Q + 2 kappa ist auf Flaechen im k-Raum singulaer. Statisch heisst
    das: Die Antwort der Verbindung auf eine Quelle hat dort Anteile grosser Reichweite.
  - kappa = 1: Fast positiv definit (0 oder 1 negative), ein Wechsel auf 3 von 5 Linien, kleinster Betrag 5e-6 bzw.
    4,8e-8 bei k = 1e-3.
  - Die volle Matrix mit Energie hat allgemein 7 Nullmoden: 3 Translationen + die 4 Moden (Omega in ker M^+, x = 0).
    Diese Rahmendrehungen bei h = 1 sieht eine Energie auf der Holonomie nicht. Auf Symmetrielinien sind es 8, 9 oder
    13.
- **Lesart [H]:**
  - In der reinen Einstein-Cartan-Wirkung hat das Guertel-Feld (Weitzenboeck-Torsion) keine Energie. 4 Richtungen je
    Zelle sind sogar ganz unbestimmt.
  - Erst eine eigene Rahmenenergie macht es ausbreitungsfaehig (Regime B im Dossier).
  - Die gerechnete Energie auf der Holonomie laesst aber 4 Nullmoden je Zelle uebrig. Eine Energie auf den
    Rahmendrehungen selbst ist nicht gerechnet.

## 6. Was Christiansen/Hu/Lin 2023 (arXiv 2312.11709) schon enthaelt [S]

- **Abrufe:** B1 Datensatz (WebFetch, vor 04:26:17) und B2 Volltext-PDF (WebFetch, vor 04:26:30).
  - Die Modell-Zusammenfassung von B2 war unlesbar. Das PDF hat das Werkzeug gespeichert; ich habe es nach
    quellen/B2-2312.11709v1.pdf kopiert (SHA256 06532f1a...) und lokal per pdftotext gelesen.
  - Erwartung vorher: quellen/ERWARTUNG-vor-Abruf.md (04:26:02).
- **Enthalten:**
  - Ein diskreter linearisierter Riemann-Cartan-Komplex (FEEC/BGG) auf jeder Triangulierung.
  - Verbindung in Wh1 = Flaechendeltas c tensor n_f (3 je Flaeche), Torsion in Vh2 (3 je Flaeche).
  - Der algebraische Operator dazwischen ist bijektiv: "S^-1 maps Vh2 to Wh1 (as S is bijective)", Abschn. 4, Z. 550.
  - Kohomologie = de Rham tensor infinitesimale Starrkoerperbewegungen (Abstract; Satz 4.1, 5.1).
  - Das ist der **kinematische** Teil unserer Frage: Torsionsfrei legt die Verbindung je Flaeche algebraisch fest.
    Bei uns entspricht das J(k), lokal und eindeutig, Konsistenz <= 8,5e-16.
- **Nicht enthalten:**
  - keine Wirkung, keine Hesse-Matrix, keine Bewegungsgleichung (grep action/variational/energy/functional: nur ein
    Literaturtitel)
  - keine Startpunkt-Mittelung, kein Logarithmus, kein Bloch, kein Kuhn-Gitter, keine Nullmoden
  - Torsion in Regge-Rechnung "beyond the scope of this paper" (Z. 140-144)
- **Der lineare dynamische Fall (TS1, TS2) steht dort also nicht.** Erwartungen E1 bis E3 eingetroffen, E4 soweit
  pruefbar.

## 7. Kontrollen, Ableitbarkeit, Selbstanzeigen

### 7.1 Kontrollen (eingefrorene Regeln PLAN 6) [E]

| Kontrolle | Schranke | Wert | erfuellt |
|---|---|---|---|
| KN: Gl. 47 exakt (expm/Log, Mittelung, 3^3-Torus) gegen Bloch-Quadratform, 3 Zufallsvektoren | <= 1e-6 | 7,2e-12; 8,3e-12; 4,2e-12 | ja |
| KG: erste Ordnung = 0, Verhaeltnis t^2 | 0,25 +- 0,01 | 0,2500 / 0,2500 / 0,2500 | ja |
| KH: Q hermitesch | <= 1e-12 | 1,4e-16 | ja |
| KT: Spur Q | <= 1e-12 | 0 | ja |
| KE: Eichresiduen, Rang | <= 1e-9, 21 | 2,1e-15, 21 | ja |
| KJ: torsionsfreie Abbildung konsistent | <= 1e-9 | 8,5e-16 | ja |
| KX: M^+ + Q J = 0 | <= 1e-9 | 1,9e-15 | ja |
| R hermitesch, R = -J^+ Q J, Omega-Zeilen von R | (beschreibend) | 2,6e-15; 2,1e-15; 1,6e-15 | ja |
| KR: Regge-Sektor wie REGGE-4D-1 3D | beschreibend | 3 Null, 2 neg., 1 pos. ~ k^2, Gittermode -3,50 | ja |

- KN prueft Paargewichte, Umlaufrichtungen, M-Block und Bloch-Zusammenbau zugleich gegen die exakte Formel.

### 7.2 Ableitbarkeit

- **Vorab im Plan hergeleitet [M]:**
  - Paargewichte w(d) = 1 - 2d/m mit Eigenwerten i cot(pi q/m)
  - Q spurfrei und indefinit
  - Logarithmus auf 2. Ordnung belanglos
  - KX und die Identitaet dim ker H = dim ker R + dim ker Q, also TS2 genau dann, wenn nicht TS1, an jedem k
  - Weitzenboeck-Form P^+ Q P = 0
  - Arm "Linien"
- **Selbstanzeige 1 (die wichtigste):** Auch die **Existenz** von mindestens 4 Nullmoden je k war vorab ableitbar:
  18 Rahmendrehungen gegen 14 Kantenbedingungen, zusammen mit KX.
  - Karte und Plan (1.8) nannten das "nicht ableitbar". Ich habe die Zaehlung erst nach Sicht gefunden.
  - TS1 "eingetroffen" und TS2 "verfehlt" sind damit im Kern **vorab ableitbare Kennzahlen, keine Messung**.
  - Gemessen ist nur: genau 4 bei allgemeinem k (nicht mehr), 5, 6 und 13 auf Sonderlinien, 12 bei Gamma, die k-Skalen
    und der Einzelstart-Vergleich (8).

### 7.3 Weitere Selbstanzeigen

2. **TS0 verfehlt wegen meiner Regel.** Die Regel ||psi| - |delta|| <= 1e-8 mit arccos war bei psi = 0 zu streng
   fuer die Formel (arccos bei 1 - 2 ulp gibt 2e-8). Das Urteil bleibt "verfehlt". Die Physik der Kontrolle ist
   erfuellt (Abschn. 4).
3. **Variante E1 im Hauptlauf ist ein Zwitter.** Nur Q kam vom Einzelstart, M blieb gemittelt.
   - Ihr Q-Kern (8 an allen k) gilt fuer den Einzelstart, denn Q haengt nicht von M ab.
   - Der Vergleich "Q_E1 J N" im Nachtrag 1 (Residuum 0,135) ist dagegen sinnlos. Richtig gerechnet ist es in
     Nachtrag 2.
4. **Code vor dem Plantext geschrieben.** Zwei Rauchtests liefen vor dem Einfrieren; gesehen habe ich nur Laufzeiten,
   Schluessel und Rueckgabecodes. Fuer den zweiten Rauchtest kam ein Modus "rauchvoll" hinzu.
5. **Nachtraege nach Sicht** (code/nachtrag_kern.py, code/nachtrag_einzelstart.py) sind nicht eingefroren.
   - Der erste Start von nachtrag_kern.py brach am Modul-Lader ab; die neue Fassung kam per mv.
   - Sie aendern kein Urteil.
6. **"Q_max = 1 + sqrt 3"** ist nur eine Zahlbeobachtung (2,7320506). Die 13 Nullmoden bei (pi/2)(1,1,1) sind nicht
   weiter untersucht.
7. **Allgemeine Triangulierungen (T - 2V > 0):** nur hergeleitet, nicht gerechnet [H].
8. **Abruf B2:** Die WebFetch-Zusammenfassung war leer. Gelesen ist der lokale pdftotext-Text des vom Werkzeug
   gespeicherten PDFs; das zaehlt als Abruf 2 von 2. Keine weiteren Abrufe. pdftotext lief lokal; kein python, awk oder
   perl lokal.
9. **Rahmenenergie nur auf der Holonomie** (wie im Plan). Eine Energie auf den Rahmendrehungen Omega ist nicht
   gerechnet; sie wuerde die 4 verbleibenden Moden betreffen.
10. **Keine Schreibzugriffe ausserhalb** von torsion-steif-1/ und /home/fmh/fmhc-physics-remote/torsion-steif-1/. Kein
    Journal, kein Peerbus, kein Commit. Nichts Versiegeltes geoeffnet; jeder grep mit allen Ausschluessen.
11. **Zeitbox:** Start 04:19:11, letzter Lauf 04:46:13, Ende 05:49:11. Kein Lauf nach der Zeitbox.

## 8. Einfach gesagt

- Wir haben geprueft, ob die Regeln von Yan und Kollegen die "Zusatzverdrehung" zwischen zwei Nachbarzellen eines
  Tetraeder-Gitters eindeutig festlegen, wenn der Raum flach ist.
- Das tun sie nicht ganz: Je Gitterzelle bleiben 4 Arten, die Zellen gegeneinander zu verdrehen, ohne dass die Rechnung
  das merkt. Diese Luecke ist eine Abzaehlfolge (mehr Zellen-Drehungen als Kanten-Bedingungen); man haette sie vorher
  ausrechnen koennen.
- Ein Band, das man auf den Kanten um eine Kante herumfuehrt, kommt genau um den Kruemmungswinkel verdreht zurueck. Es
  misst also Kruemmung, nicht Verdrehung.
- Gibt man den Zellen-Verdrehungen eine eigene Energie wie beim Guertel-Feld, koennen sie sich ueber das Gitter
  ausbreiten wie eine Welle. Ein Teil der Luecke bleibt aber offen.

## Dateien

- KARTE.md (unveraendert), PLAN.md, PLAN.md.eingefroren-20261005-043849, EINGEFROREN-SHA256.txt
- code/torsion_steif.py und code/auswertung.py, je mit .eingefroren-20261005-043849
- code/nachtrag_kern.py und code/nachtrag_einzelstart.py (Nachtrag, nicht eingefroren)
- lauf-69/: haupt.json (11,6 MB), auswertung.json, Logs, PRUEFSUMMEN.txt (gegen die .69 geprueft: OK)
- nachtrag-69/: nachtrag_kern.json, nachtrag_einzelstart.json, Logs, PRUEFSUMMEN.txt
- quellen/: ERWARTUNG-vor-Abruf.md, B-abrufzeit.txt, B2-2312.11709v1.pdf und .txt
- .69: /home/fmh/fmhc-physics-remote/torsion-steif-1/ (code/, lauf/, nachtrag/, rauch/)
