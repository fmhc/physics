# REGGE-TORSION-L: Dossier. Ist Regge-Rechnung mit Torsion (Yan/Ding/Ma/Zhang, arXiv 2610.00593) ein Ort fuer Spin im Netz, und passt sie zu Finns Baendern mit markierter Seite? (Runde 44, Literatur)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-04 23:15:51 CEST, Text dieser Datei ab 23:29:25 CEST
  (beides date). Zeitbox 35 min (bis 23:50:51).
- Arbeitsdatei: ARBEITSFELD.md (Erwartung mit date-Zeit vor jedem Abruf, Ausgang, Gegensweep, eigene Schluesse).
- **Abrufe: 3 von 3.** A1 arXiv-API-Datensatz (WebFetch), A2 Volltext-PDF (curl, Selbstanzeige 1), A3 arXiv-API-Suche
  (WebFetch, Selbstanzeige 2). Kopien in quellen/ mit Abrufzeit; der Volltext als quellen/A2-2610.00593v1.txt
  (pdftotext; "Z." = Zeile dort). Keine Websuche.
- **Kennzeichen:** [S] an der Quelle gelesen (Abschnitt, Gleichung, Zeile); [S Abstract]; [S Lit.] nur Titel aus der
  Literaturliste von 2610.00593; [P] Projektdatei; [L] Gedaechtnis; [M] eigene Mathematik; [ES] eigener Schluss;
  [H] Hypothese.
- **Art:** Literatur und Schreibtisch. Keine Rechnung, keine Messdaten.
- Die Erwartungen RT1 bis RT3 stehen unveraendert in KARTE.md.

## 1. Ergebnis zuerst

1. **Das Netz der Arbeit:** Je Simplex Kantenvektoren (Laenge und Richtung im eigenen Rahmen des Simplex), je
   Grenzflaeche zwischen zwei Simplizes eine Holonomie in SO(n) bzw. SO+(1,n-1). Die Form der gemeinsamen
   Grenzflaeche muss in beiden Simplizes gleich sein (Gl. 13). Die Geometrie bleibt also Regge-Geometrie.
   **Torsion ist eine Zusatzdrehung je Grenzflaeche**: Die Holonomie weicht von der Drehung ab, die die Geometrie
   vorgibt. Sichtbar wird das als Fehlpassung der Kantenvektoren auf der Grenzflaeche (Gl. 26 bis 28)
   [S Abschn. II; M].
2. **Dynamik** heisst hier: zwei kovariante Bewegungsgleichungen aus einer diskreten Einstein-Cartan-Wirkung (3D
   euklidisch Gl. 47, 4D Lorentz Gl. 78). Es gibt keine Zeitschritte, keine Hamilton-Form und keine Klassifikation der
   Zwangsbedingungen. Als Eichsymmetrie kommt nur die Rahmendrehung je Simplex vor; Eckverschiebungen fehlen.
   **Kontinuum:** Die Kantengleichung ergibt nur das gemittelte (integrierte) Gegenstueck der Tetradengleichung, ist
   also schwaecher. Fuer die Holonomiegleichung ist nur gezeigt, dass torsionsfreie Holonomien sie loesen; dass sie
   die einzigen Loesungen sind, ist nicht gezeigt [S Abschn. VI].
3. **Spin:** Materie ist nicht gebaut. Die Autoren nennen als offen, "whether the torsion is determined
   algebraically by the fermions" (Abschn. VII) [S]. Die Arbeit hat einen Platz fuer Spindichte, aber kein
   Spin-1/2-Feld. Ein solches Feld braucht Holonomien in Spin(n) statt SO(n), also eine Vorzeichenwahl je
   Verbindung [L]. Das ist dieselbe Z_2-Frage wie beim Guertel-Trick [M, H].
4. **Finns Baender:** Eine Rahmung je Kante kommt in der Arbeit nicht vor. Fuehrt man in 3D eine markierte Seite um
   eine Kante herum, liest sie den Fehlwinkel, also die Kruemmung, nicht die Torsion (Gl. 47, 70, 74) [M, ES]. Ein
   Band auf der Verbindung zweier Zellen, das sich um diese Verbindung dreht, ist dagegen eine der drei
   Torsionskomponenten je Dreieck [ES, H]. Finns Netz teilt Ecken, nicht Flaechen. Die Arbeit passt deshalb hoechstens
   zum gefuellten Netz [P].
5. **Regime statt Urteil (Regel 1 und 6):** Das SO(3)-Drehfeld aus GUERTEL-FINN-NETZ-1, als Verbindung gelesen, ist
   Torsion ohne Kruemmung, aber **mit eigener Energie** (Bindungsterm 2(1 - cos omega)). Die Einstein-Cartan-Wirkung
   hat keinen solchen Term. Es gibt also zwei Regime: Im Einstein-Cartan-Regime hat Torsion keine eigene Energie und
   breitet sich nicht aus. Im Cosserat- bzw. Poincare-Eich-Regime hat sie Energie und breitet sich aus [L, ES, H].
   Welches Regime auf dem Netz gilt, laesst die Arbeit offen. Das entscheidet der Kartenvorschlag (Abschn. 5).

## 2. Urteile RT1 bis RT3

| Nr | Erwartung (Karte, unveraendert) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| RT1 | [H] Das Netz hat neben Kantenlaengen eigene Verbindungs- bzw. Rahmenvariablen je Simplex; die Kontinuumsgrenze ist Einstein-Cartan | 60 % | **teilweise eingetroffen.** Teil 1 ja, praeziser: Rahmen je Simplex (als Eichung, Gl. 10-12), Verbindung je **Grenzflaeche** (Gl. 14-16), nicht je Simplex. Teil 2 nur in der Lesart der Autoren: "In this sense, the equations of motion ... admit a continuum limit that agrees with the field equations of Einstein–Cartan gravity" (Abschn. VII, Z. 1207-1209). Gezeigt ist weniger: Die Kantengleichung impliziert die integrierte Tetradengleichung und ist schwaecher (Gl. 103, Z. 1039-1043). Die Holonomiegleichung wird nur von torsionsfreien Holonomien geloest gezeigt (Gl. 113-115). Keine Konvergenzrechnung, keine Numerik | [S Abschn. II A, VI A, VI B, VII] |
| RT2 | [H] Ohne Spinquelle ist die Torsion algebraisch (nicht ausbreitungsfaehig); die Rahmen bringen keine neue langreichweitige Kraft | 70 % | **aus der Quelle nicht entscheidbar; nach Recherchestand nicht belegt** (weder eingetroffen noch verfehlt). Gezeigt ist nur: "Though it is not easy to solve Eq. (112), we check whether the torsion-free holonomy is a solution" (Z. 1138-1140). Ob die Loesung eindeutig ist und ob Torsion sich ausbreitet, wird nicht behandelt (grep "propagat", "lineari", "wave" ohne Treffer). Gl. (112) koppelt jede Grenzflaechen-Holonomie ueber die Holonomien um die Gelenke an ihre Nachbarn; algebraisch ist sie also nicht offensichtlich [S Gl. 110-112; ES]. Im Kontinuum gilt RT2 fuer Einstein-Cartan [L; Abschn. I, Z. 49-54]. Die arXiv-Suche ueber 24 Monate fand keine Arbeit, die die Ausbreitung von Torsion auf einem Simplex-Netz rechnet (A3) | [S Abschn. VI B, VII]; quellen/A3 |
| RT3 | [H] Eine Kopplung an Spin-1/2-Materie auf dem Netz ist in der Arbeit nicht gebaut | 65 % | **eingetroffen.** Fermionen kommen nur in der Einleitung (Kontinuum, Z. 54-58) und im Ausblick vor: "It is interesting to study the coupling of the present discrete gravity with matter fields" (Z. 1225-1229). In der 24-Monats-Suche fand sich keine andere Arbeit, die das baut (nach Recherchestand) | [S Abschn. I, VII]; quellen/A3 |

**Bedeutung nach der Karte:** Weder Zweig ist ausgeloest. "RT1 und RT2 treffen ein" gilt nicht, weil RT2 offen ist.
"RT2 verfehlt" gilt ebenfalls nicht. Vor einer Skizze der Spin-Torsion-Kopplung (Testpfad des Pools) muss erst
geklaert sein, ob die Torsion auf dem Netz festgelegt ist (Abschn. 5) [ES].

## 3. Erwartungsverstoesse (das Wichtigste zuerst)

| Nr | Erwartet (vor dem Abruf, ARBEITSFELD) | Gefunden | Beleg | Folge |
|---|---|---|---|---|
| V1 | E2b: Kantenvektoren je Simplex duerfen sich auch in der Laenge unterscheiden (60 %), Torsion als Form-Fehlpassung wie bei twisted geometries | **Die Form muss passen.** "Compatibility of the intrinsic geometry of the common interface means that the two vectors are related by a local gauge transformation", Gl. (13). In 4D: "have to be identical up to an SO+(1,3) gauge transformation". Twisted geometries werden ausdruecklich abgegrenzt | [S Abschn. II A Z. 209-222; Abschn. V Z. 784-788; Abschn. I Z. 38-40] | Torsion ist reine Zusatzdrehung je Grenzflaeche: n(n-1)/2 Zahlen, also 3 je Dreieck in 3D und 6 je Tetraeder in 4D [M, so nicht im Text gezaehlt]. Die Metrik bleibt Regge. Der Art nach (Drehung) passt das besser zu einer "markierten Seite" als eine Laengen-Fehlpassung, aber auf den falschen Kanten (V4, Abschn. 4) |
| V2 | Abstract: "It is shown that they return to the corresponding Regge actions" (3D **und** 4D) | **Nur 3D vorgerechnet** (Gl. 70-76: S_B = eps L). Abschn. V (4D) enthaelt das Wort "Regge" nicht | [S Abschn. IV, V]; Gegensweep G1 | Fuer 4D ist das eine Behauptung. Aus [A_B, h_B] = 0 (Gl. 113) folgt sie wohl leicht [ES, nicht nachgerechnet] |
| V3 | Karte, Frage 4: Eichsymmetrien und Zwangsbedingungen, erster Klasse? | **Nicht behandelt.** Nur lokale SO(n) bzw. SO+(1,n-1) je Simplex (Gl. 10-12, 20). Zwangsbedingungen nur kinematisch: Schliessung je Dreieck (Gl. 2), Formgleichheit (Gl. 13), Zeitorientierung und nicht lichtartig (Abschn. V), Konvergenzbedingung fuer den Logarithmus mit abs(eta) < ln 2 und abs(theta) < pi/3 (Gl. 105-107). Keine Hamilton-Form, keine Eckverschiebungen | [S]; grep in ARBEITSFELD Abruf 2, E2d | Die Frage "erster Klasse?" (L1) beantwortet die Quelle nicht. Die Rahmendrehung ist eine exakte Eichsymmetrie der Wirkung (Satz B.5, Z. 482-484), die Eckverschiebung bleibt offen |
| V4 | Selbstverstaendlich (Gegensweep G2): Finns Netz ist ein Simplex-Netz mit gemeinsamen Flaechen | **Finns Netz teilt Ecken.** "Im Pyrochlor gehoert jede Kante genau einem Tetraeder"; Diamant-Nachbarn "ueber die geteilten Ecken" | [P] EINE-WELT-LOCH-1/KARTE.md Z. 11; GUERTEL-FINN-NETZ-1/ERGEBNIS.md Z. 20 | Grenzflaechen und damit Torsion im Sinn der Arbeit gibt es erst im gefuellten Netz. Ob das eine volle Triangulierung ist, ist nicht geprueft |
| V5 | A3: Treffer vor allem Spinschaum/LQG, Rauschen 30 bis 50 % | **26 von 30 Treffern Rauschen** (Homologie, Gruppen, Topologie); **kein** Spinschaum-Treffer seit 2021-09. Unerwartet einschlaegig: Christiansen/Hu/Lin 2023, eine diskrete **linearisierte** Riemann-Cartan-Geometrie | quellen/A3 [S Abstract, sekundaer] | Die lineare Fassung von RT2 ist vielleicht schon Literatur (Kartenvorschlag, Ableitbarkeitsprobe) |
| V6 | klein: drei Autoren | vier (Cong Zhang) | [S] | folgenlos |

- **Bestaetigt (je eine Zeile):** Variablen wie erwartet (E2a). Wirkung vom Barrett-Typ mit Matrix-Logarithmus statt h
  (E2c), ausdruecklich gegen Caselle/D'Adda/Magnea abgegrenzt (Z. 613-620). Keine Hamilton-Analyse (E2d). Keine
  Eindeutigkeit, keine Konvergenzrechnung (E2e). Keine Materie (E2f). LQG-Bezug vorhanden (E2g).

## 4. Einordnung zu Finns Netz [H]

### 4.1 Was Torsion dort genau ist, und wo die markierte Seite hinpasst

- **Lage:** In 3D sitzt Kruemmung auf den Kanten (Gelenke), Torsion auf den Dreiecken (Grenzflaechen) als
  Zusatzdrehung mit 3 Komponenten. In 4D sitzt Kruemmung auf den Dreiecken, Torsion auf den Tetraedern mit 6
  Komponenten [S Abschn. II B, VII; M].
- **Was die 3D-Wirkung liest:** In eps_IJK l^I (Ln h_B)^JK zaehlt nur der Anteil der Gelenk-Holonomie, der um die
  Kante l dreht [M an Gl. 47]. Torsionsfrei ist das genau der Fehlwinkel: h_B = exp(-eps U) mit U = Drehung um die
  Kante (Gl. 74, 75), daher S_B = eps L (Gl. 76) [S].
  - [ES] Eine markierte Seite, die man einmal um eine Kante herumtraegt, kommt um den Fehlwinkel gedreht zurueck. Ein
    "Band um die Kante" misst also Kruemmung, nicht Torsion.
- **Wo die markierte Seite Torsion traegt [ES, H]:**
  - Liegt das Band auf der Verbindung zweier Zellen (Dualkante, Weg durch das gemeinsame Dreieck), ist seine
    Verdrehung um diese Verbindung die Komponente der Zusatzdrehung um die Flaechennormale.
  - Das ist eine der drei Torsionskomponenten je Dreieck. Die zwei Kippungen haben kein Band-Bild.
  - Auf Finns Linien (Primaerkanten) gibt es in der Arbeit keine Transportvariable: Innerhalb eines Simplex ist der
    Transport trivial (Z. 230-234) [S]. Eine Verdrillung *laengs* einer Kante kommt daher nicht vor.
- **Rueckfrage an die Leitung bzw. an Finn (wandert mit):** Liegt das Band auf den Linien oder auf den Verbindungen
  zwischen Zellen? Eine direkte Entsprechung gibt es nur im zweiten Fall.

### 4.2 L4 (Spin 1/2 als Dynamik)

- **Platz ja, Spin nein [S, ES]:** Im Kontinuum ist Einstein-Cartan-Torsion der Platz fuer Spindichte, "torsion
  becomes algebraically related to the spin density of the fermion field" (Z. 54-57, mit Hehl u. a. 1976 und Shapiro
  2002). Auf dem Netz ist dieser Platz angelegt (Holonomie je Grenzflaeche), aber leer. Torsion erzeugt keinen Spin;
  Spin muss als Spinorfeld dazukommen.
- **Wo L4 und die Arbeit sich beruehren [L, M, H]:**
  - Spinoren brauchen Uebertragung in Spin(n), also SU(2) bzw. SL(2,C). SO(n)-Holonomien legen die
    Spinor-Uebertragung nur bis aufs Vorzeichen fest; die stimmige Wahl ist eine Spinstruktur [L].
  - Das Vorzeichen ist genau pi_1(SO(3)) = Z_2, die Groesse hinter dem Guertel-Trick [M].
  - [H] Ob Finns markierte Seite diese Vorzeichen-Buchfuehrung tragen kann, ist offen. Fuer die Rahmung der Kanten
    sagt das Projekt bisher: Ein Fermion ergibt sich nur algebraisch und nur bei lokal gelesener Rahmungsregel
    (TWIST-PYRO-1, TWIST-SPIN-1, laut GEMEINSAMES-NETZ v3, L4) [P].
- **Das Guertel-Feld als Torsion gelesen [M, ES, H]:**
  - Lies das SO(3)-Feld q_i aus GUERTEL-FINN-NETZ-1 als Rahmen je Zelle, auf flacher Geometrie mit h_ij = q_j q_i^-1.
    Dann ist jede Gelenk-Holonomie 1: keine Kruemmung, aber Torsion, wo h_ij von der geometrischen Drehung abweicht
    (Weitzenboeck-Lage) [M].
  - Die EC-Wirkung (Gl. 47) ist dort **null**, weil Ln 1 = 0 [M]. Im Kontinuum verbietet die Zusammenhangsgleichung
    diese Lage im Vakuum [L].
  - Die Guertel-Dynamik lebt aber von der Bindungsenergie 2(1 - cos omega), also von einem Torsion-zum-Quadrat-Term.
  - Folge [H]: Das Guertel-Feld ist der Form nach **nicht** Einstein-Cartan-Torsion, sondern Torsion mit eigener
    Energie (Regime B unten).
  - Einschraenkung: Die Guertel-Bindungen laufen ueber geteilte Ecken, nicht durch gemeinsame Flaechen (V4). Die
    Zuordnung ist also eine Lesart, keine Identitaet.

### 4.3 L3 (Schwerkraft aus demselben Netz) und L1 (eine Schrittregel)

- **L3 [S, P, L, ES]:**
  - Im torsionsfreien Sektor ist die Arbeit Regge-Rechnung (3D gezeigt, 4D behauptet). Die Schwerkraft ist damit
    eingesetzt, nicht entstanden (Marolf-Lesart, GEMEINSAMES-NETZ v3 Abschn. 1) [P].
  - Im Einstein-Cartan-Regime bringt Torsion im Kontinuum keine neue Fernkraft und aendert die Ausbreitung der
    Schwerewellen nicht [L].
  - Auf dem Netz ist beides offen (RT2). Die TT-Anisotropie von Finns gefuelltem Netz (L3) beruehrt die Arbeit nicht.
- **L1 [S, ES]:**
  - Die Arbeit hat eine Wirkung fuer Geometrie und Verbindung zugleich. Die Rahmendrehung je Simplex ist dort eine
    exakte Umbenennung (Gl. 20, Satz B.5).
  - Das ist die leichte Haelfte von L1. Die schwere Haelfte (Takt, Eckverschiebung, Hamilton-Bedingung, erster
    Klasse) behandelt die Arbeit nicht.
  - Zur skalaren Regel (Paar zweiter Klasse, GAMMA-NETZ-L Abschn. 5.1 [P]) traegt sie nichts bei.

### 4.4 Regime und Moderatoren (Regel 1), Unterscheidungspunkte (Regel 2), Kopplung vor Bauteil (Regel 6)

- **Regime A, Einstein-Cartan (erste Ordnung, kein Torsion-zum-Quadrat-Term):**
  - Torsion hat keine eigene Energie; im Vakuum ist sie null.
  - Mit Fermionen ist sie algebraisch proportional zur Spindichte und gibt nur eine Kontaktwechselwirkung [L].
  - Die Arbeit ist der Form nach Regime A (Gl. 47, 78 linear in Ln h). Ob das Netz dieses Verhalten auch hat, ist
    offen.
- **Regime B, Poincare-Eich- bzw. Cosserat-Typ (Terme in Rahmengradient oder Torsion zum Quadrat):**
  - Torsion breitet sich aus, massiv oder masselos [L].
  - Das Guertel-Feld gehoert der Form nach hierher (4.2).
- **Moderator:**
  - Ob die Wirkung den Rahmengradienten bzw. die Torsion quadratisch bestraft.
  - Auf dem Netz kommt hinzu: Ob Gl. (112) torsionsfrei **eindeutig** loest, ist eine Gitterfrage. Die Holonomien
    sind ueber die Gelenke gekoppelt [ES].
- **Unterscheidungspunkte:**
  - **Theoretisch:** Hesse-Block der Wirkung in Holonomie-Richtungen bei fester, flacher Geometrie. Ist er nicht
    entartet, ist die Torsion algebraisch festgelegt (A). Gibt es Nullmoden, ist sie unbestimmt (Gitterartefakt oder
    neue Freiheitsgrade). Das ist rechenbar (Abschn. 5).
  - **Messbar:** Kraft zwischen spinpolarisierten Koerpern bei endlichem Abstand. In A gibt es nur Kontakt
    (Reichweite null) mit Staerke proportional zu G [L]. In B gibt es eine Spin-Spin-Kraft mit Reichweite gleich der
    inversen Torsionsmasse [L].
  - Messschranken dafuer gibt es aus Torsionspendeln mit polarisierten Elektronen, Komagnetometern und
    Hughes-Drever-Versuchen (z. B. Heckel u. a. 2008; Kostelecky/Russell/Tasson 2008; Laemmerzahl 1997) [L]. Zahlen
    nenne ich nicht, weil keine Quelle abgerufen ist (Karte: "Zahlen nur mit Quelle").
- **Regel 6:** Drei Projektwege zu "Spin im Netz" teilen dieselbe Kopplungsgroesse, naemlich die relative Drehung des
  Zellrahmens ueber eine Verbindung:
  - Guertel-Trick im Drehfeld (L4)
  - Rahmung der Kanten (TWIST-PYRO-1, TWIST-SPIN-1)
  - Torsion als Spindichte-Platz (diese Arbeit)
  - [H] Nicht das Bauteil (Band, Drehfeld, Holonomie) entscheidet, sondern ob diese Groesse eigene Energie bzw.
    einen eigenen Takt hat.

### 4.5 Kalibrierung

- **(a) gemessen:** nichts. An der Quelle gelesen [S]: Variablen, Definition der Torsion, Wirkungen, die zwei
  Bewegungsgleichungen und was davon gezeigt ist.
- **(b) nuetzlich verdichtet [M, ES]:**
  - Torsion ist eine Zusatzdrehung je Grenzflaeche.
  - Die 3D-Wirkung liest nur die Drehung um die Kante.
  - Das Guertel-Feld ist Weitzenboeck-Torsion mit eigener Energie (Regime B).
- **(c) gewachsene Gewissheit ohne neue Evidenz:**
  - Waehrend des Lesens wuchs mein Eindruck, "markierte Seite = Torsion" passe. Belegt ist nur: eine von drei
    Komponenten, auf Dualkanten, als Lesart.
  - Die schoene Vereinheitlichung unter Regel 6 ist ebenfalls nur eine Hypothese.
  - **Warnzeichen:** Die Sicherheit stieg, waehrend sich die Frage in Primaer- gegen Dualkante, gefuelltes gegen
    ungefuelltes Netz und Regime A gegen B aufspaltete.

## 5. Kartenvorschlag (einer) mit Ableitbarkeitsprobe

**TORSION-STEIF-1 [H] (Schreibtisch, dann Kleintest): Ist die Torsion in der 3D-Wirkung von Yan u. a. auf einem
flachen Kuhn-Gitter algebraisch festgelegt?**

- **Rechnung:**
  - Gl. (47) um h = 1 entwickeln: flache Geometrie, alle Simplexrahmen gleich ausgerichtet, Holonomie
    h_e = exp(X_e) je inneres Dreieck.
  - Ln h_B nach Baker-Campbell-Hausdorff bis zur zweiten Ordnung; die Mittelung ueber die m_B Startsimplizes gibt
    Paargewichte, die vom zyklischen Abstand abhaengen [M, vorab].
  - Daraus den Hesse-Block Q (X gegen X, 3 Zahlen je Dreieck) und den gemischten Block M (Kantenvektor gegen X)
    bilden; der Kanten-Kanten-Block ist bei h = 1 null.
  - Bloch-Zerlegung auf dem periodischen 3D-Kuhn-Gitter (6 Tetraeder und 12 Dreiecke je Wuerfel [M], also Q(k) als
    36 x 36). Code-Basis REGGE-4D-1, 3D-Kontrolle Abschn. 3.3 [P].
  - Eigenwerte von Q(k) auf einem k-Gitter, dazu die volle Matrix [[0, M], [M^T, Q]] gegen die Eichbahnen (SO(3) je
    Tetraeder, Verschiebung je Ecke).
- **Vorhersagen (Vorschlag, die Leitung setzt sie):**
  - TS1 [H]: Q(k) hat fuer k != 0 mindestens eine Nullmode; die Torsion ist auf dem Gitter dann nicht algebraisch
    festgelegt (50 %).
  - TS2 [H]: Die volle Matrix hat ausser den Eichbahnen keine Nullmoden (55 %).
- **Bedeutung:**
  - TS1 verfehlt: Regime A gilt auf dem Netz. Torsion ist dann ein Spindichte-Platz ohne eigene Dynamik, und
    Finns Guertel-Feld waere keine Einstein-Cartan-Torsion. Danach erst die Skizze der Spin-Torsion-Kopplung.
  - TS1 trifft ein: Die Torsion ist auf dem Netz unbestimmt. Vor jeder Spin-Kopplung ist dann zu klaeren, ob das ein
    Artefakt der Mittelung bzw. des Logarithmus ist.
- **Ableitbarkeitsprobe:**
  - *Vorab ableitbar:*
    - Im Kontinuum ist die Zusammenhangsgleichung bei nicht entarteter Triade eindeutig loesbar [L]. Fuer k gegen 0
      ist Nichtentartung also zu erwarten, wenn das Gitter das Kontinuum trifft.
    - Die Paargewichte der Startpunkt-Mittelung sind ableitbar [M].
    - Auf der Zwangsflaeche (fester Kantenvektor) gibt es keine Rest-Eichung, weil die Kantenvektoren eines Tetraeders
      R^3 aufspannen [M]. Jede X-Nullmode waere also echt.
  - *Nicht ableitbar:* ob Q(k) bei endlichem k Nullmoden hat (Mittelung, Gitterdoppler).
  - *Literatur zuerst:* Christiansen/Hu/Lin 2023 (2312.11709, linearisierte Riemann-Cartan-Geometrie auf einem
    Regge-Komplex) koennte den linearen Fall schon enthalten. Vor dem Rechnen den Volltext lesen.
  - *Projekt-grep* (23:26, mit Ausschluessen): keine Datei mit Torsions-Nullmoden oder Holonomie-Hesse-Matrix; das
    Kuhn-Gitter gibt es in REGGE-4D-1 und WINKELFELD-1 [P].
  - *Sicht- und Rohdatenprobe* entfallen (Modellrechnung).
  - *Rechenprobe:* 36 x 36 je k, Kleintest unter 10 min auf CPU der .69.
- **Grenze:** 3D-Gravitation hat keine lokalen Freiheitsgrade [L]. Gefragt ist hier nur, ob die Torsion
  festgelegt ist, nicht ob sie sich ausbreitet. Fuer die Ausbreitung braeuchte es Gl. (112) in 4D.

## 6. Gegensweep, offene Fragen, Quellen, Selbstanzeigen

### 6.1 Gegensweep (Regel 4; Tabelle in ARBEITSFELD Abschn. 3)

| Nr | Selbstverstaendlich | Ergebnis |
|---|---|---|
| G1 | Die 4D-Rueckfuehrung auf Regge ist gezeigt | **geprueft (Text): nein**, nur 3D (V2) |
| G2 | Finns Netz hat gemeinsame Flaechen | **geprueft (Projekt): nein**, Ecken (V4) |
| G3 | "Dynamik" heisst Zeitentwicklung | geprueft (Text): nein, kovariante Gleichungen |
| G4 | Die diskrete Torsion ist die, an die Dirac-Felder koppeln | **offen.** Minimal gekoppelte Dirac-Felder sehen nur den axialen Teil [L]; die Arbeit zerlegt die Torsion nicht |
| G5 | Die Eichsymmetrien sind vollstaendig | geprueft (grep): nur Rahmendrehung, keine Eckverschiebung (V3) |
| G6 | SO(n)-Holonomien reichen fuer Spin 1/2 | nicht abgerufen: [L] Spin(n) noetig, Vorzeichenwahl (4.2) |

### 6.2 Offene Fragen

- O1: Ist die torsionsfreie Loesung von Gl. (112) eindeutig? Das ist RT2 auf dem Netz (Kartenvorschlag).
- O2: Welcher Teil der diskreten Torsion ist der axiale, an den Spin 1/2 koppelt (G4)?
- O3 (Rueckfrage): Liegt Finns Band auf den Linien oder auf den Verbindungen zwischen Zellen (4.1)?
- O4: Ist Finns gefuelltes Netz eine volle Triangulierung mit Grenzflaechen ueberall (V4)?
- O5: Kann eine markierte Seite die Vorzeichenwahl SO(3) -> SU(2) je Verbindung tragen (4.2)?
- O6: Gilt die 4D-Rueckfuehrung auf Regge (V2)?

### 6.3 Quellen

- **Yan, R.; Ding, Y.; Ma, Y.; Zhang, C. (2026):** Dynamics of Regge calculus with torsion.
  - arXiv:2610.00593v1 [gr-qc], eingereicht 30.09.2026. https://arxiv.org/abs/2610.00593v1 , PDF
    https://arxiv.org/pdf/2610.00593v1
  - Kopien: quellen/A1-arxiv-api-2610.00593.txt (Datensatz, WebFetch 23:16-23:17), quellen/A2-2610.00593v1.pdf und
    .txt (curl 23:18:22, quellen/A2-abrufzeit.txt). Der Abstract aus A1 stimmt mit dem PDF-Text Z. 10-28 ueberein.
- **arXiv-API-Suche (A3):**
  http://export.arxiv.org/api/query?search_query=abs:torsion+AND+%28abs:Regge+OR+abs:simplicial+OR+abs:spinfoam+OR+abs:%22spin+foam%22%29&sortBy=submittedDate&sortOrder=descending&max_results=30
  (WebFetch 23:23-23:26; quellen/A3-arxiv-api-suche-torsion-regge.txt).
- **Christiansen, S. H.; Hu, K.; Lin, T. (2023):** Extended Regge complex for linearized Riemann-Cartan geometry.
  arXiv:2312.11709. https://arxiv.org/abs/2312.11709 [S Abstract, sekundaer ueber A3]
- **Chamseddine, A. H.; Malaeb, O.; Najem, S. (2024):** Curvature of an Arbitrary Surface for Discrete Gravity.
  arXiv:2409.04375. https://arxiv.org/abs/2409.04375 [S Abstract, sekundaer ueber A3]
- **Aus der Literaturliste von 2610.00593 [S Lit.]**, nur Titel, nicht gelesen, URL nicht geprueft:
  - Drummond 1986, Regge-Palatini calculus, Nucl. Phys. B 273, 125 [24]
  - Holm/Hennig 1991, Regge calculus with torsion, Lect. Notes Phys. 382, 556 [25]
  - Schmidt/Kohler 2001, Torsion degrees of freedom in the Regge calculus as dislocations on the simplicial
    lattice, Gen. Rel. Grav. 33, 1799 [26]
  - Pereira/Vargas 2002, Regge calculus in teleparallel gravity, Class. Quant. Grav. 19, 4807 [27]
  - Gronwald 1995, On non-Riemannian parallel transport in Regge calculus, Class. Quant. Grav. 12, 1181 [29]
  - Caselle/D'Adda/Magnea 1989, Regge calculus as a local theory of the Poincare group, Phys. Lett. B 232, 457 [30]
  - Barrett 1994, First order Regge calculus, Class. Quant. Grav. 11, 2723 [31]
  - Haggard/Rovelli/Wieland/Vidotto 2013, Spin connection of twisted geometry, Phys. Rev. D 87, 024038 [32]
  - Freidel/Speziale 2010, Twisted geometries [10]
  - Hehl/von der Heyde/Kerlick/Nester 1976, General Relativity with Spin and Torsion, Rev. Mod. Phys. 48, 393 [2]
  - Shapiro 2002, Physical aspects of the space-time torsion, Phys. Rept. 357, 113 [4]
  - Die [L]-Liste in ARBEITSFELD Abschn. 1 (Drummond, Caselle/D'Adda/Magnea, twisted geometries, Haggard u. a.) ist
    damit bis auf die Titel bestaetigt.
- **[L] nicht abgerufen, ohne Zahlen:**
  - Laemmerzahl 1997, Constraints on space-time torsion from Hughes-Drever experiments, Phys. Lett. A 228, 223
  - Kostelecky/Russell/Tasson 2008, Constraints on torsion from bounds on Lorentz violation, Phys. Rev. Lett. 100,
    111102
  - Heckel u. a. 2008, Preferred-frame and CP-violation tests with polarized electrons, Phys. Rev. D 78, 092006
  - Bibliografische Angaben aus dem Gedaechtnis, ungeprueft.
- **Projektdateien [P]:**
  - RUNDE-44/GEMEINSAMES-NETZ-v3.md
  - RUNDE-37/guertel-finn-netz-1/ERGEBNIS.md
  - RUNDE-37/takt-umbenennung-l/DOSSIER.md (Abschn. 1-2)
  - RUNDE-37/gamma-netz-l/DOSSIER.md (Abschn. 1, 5.1)
  - RUNDE-37/eine-welt-loch-1/KARTE.md (Z. 1-14)
  - RUNDE-36/regge-4d-1/ERGEBNIS.md (nur grep)

### 6.4 Selbstanzeigen

1. **Abruf 2 per curl statt WebFetch.** Gleicher Host (arxiv.org/pdf), im Budget als Abruf 2 von 3 gezaehlt. Grund:
   eine woertliche Kopie mit Gleichungen; Vorbild TAKT-UMBENENNUNG-L (PDF -> pdftotext). pdftotext und pdfinfo
   liefen lokal; kein python, awk oder perl.
2. **Abruf 3 war eine Suche** ueber die arXiv-API (search_query), nicht der genannte id_list-Aufruf. Der Kanal ist
   erlaubt (arXiv-API); die Leitung hatte nur id_list beispielhaft genannt. Die Karte erlaubte im Gegensweep einen
   weiteren Abruf; ich habe ihn fuer die Suche statt fuer eine Messschranke verwendet. Deshalb stehen keine Zahlen
   bei den Schranken.
3. **A1 und A3 sind Wiedergaben eines kleinen Modells** (WebFetch), nicht rohes XML. A1 ist durch den PDF-Text
   gedeckt. Die Zitate aus A3 (2312.11709, 2409.04375) sind sekundaer.
4. In quellen/A3 habe ich einen Eintrag (2205.03435) zunaechst vergessen und um 23:27 nachgetragen; vermerkt in der
   Datei.
5. **Nicht nachgerechnet:**
   - Gl. (110)-(112) und Anhang B (nur ueberflogen).
   - "4D-Rueckfuehrung folgt leicht aus Gl. (113)" (V2).
   - Die Aussage "Wirkung null in der Weitzenboeck-Lage" ist eigene Kopfrechnung (Ln 1 = 0) [M].
6. **Kopfrechnungen:** n(n-1)/2, 12 Dreiecke je Kuhn-Wuerfel, BCH-Gewichte, Zeitbox.
7. Zusaetzlich zu den Pflichtdateien gelesen: EINE-WELT-LOCH-1/KARTE.md (Z. 1-14) und grep in ERGEBNIS.md, fuer G2.
   Grep jeweils mit allen Ausschluessen; nichts Versiegeltes geoeffnet.
8. Kein Journal, kein Peerbus, kein Commit. Geschrieben nur in RUNDE-37/regge-torsion-l/.

## 7. Einfach gesagt

Die Arbeit baut ein Netz aus Tetraedern, in dem jede Zelle ihre eigene Ausrichtung hat. Beim Uebergang zur
Nachbarzelle darf diese Ausrichtung sich zusaetzlich verdrehen; diese Zusatzdrehung ist die Torsion. Die Autoren
zeigen, dass ihre Regeln ohne Zusatzdrehung zur bekannten Regge-Rechnung zurueckfuehren. Ob die Zusatzdrehung im
leeren Raum immer verschwinden muss, zeigen sie nicht, und echte Teilchen mit halbem Spin bauen sie nicht ein. Finns
Baender mit markierter Seite passen nur dann dazu, wenn sie auf den Verbindungen zwischen den Zellen liegen, und auch
dann nur zu einem von drei Teilen der Torsion.
