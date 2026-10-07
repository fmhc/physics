# M-Theorie und Calabi-Yau: Stand der Forschung und Bezug zu unserem Programm

- **Auftrag:** Finn im Chat, 30.09.2026: "check mal m theory framework und calabi-yau manifold". Weitergegeben von
  claude-primary an einen Feldforscher-Agenten (Anthropic, Claude Opus 5.5).
- **Beginn (gemessen mit date):** 2026-09-30 03:34:47 CEST. **Schreibbeginn (gemessen):** 03:48:42 CEST.
  **Ende (gemessen):** siehe letzte Zeile der Kopfzeilen (nach Abschluss eingetragen).
- **Art:** Literaturcheck, explorativ (v3). Keine Rechnung, kein Vertrag, keine Karte gerechnet.
- **Arbeitsfeld mit allen Erwartungen vor den Abrufen:**
  /tmp/claude-1000/-home-fmh-fmhc-physics/76c41c65-1089-4cc3-bcfe-f088e91d4721/scratchpad/ARBEITSFELD-mtheorie-cy.md
  (Scratchpad dieser Sitzung; Erwartungen E1 bis E31, G1 bis G7, H1 und H2 dort mit Ergebnis).
- **Marken:**
  - **[A]** Abstract bzw. Textstelle an der Quelle gelesen (arXiv-Abstractseite ueber das Abrufwerkzeug oder lokale PDF)
  - **[S]** nur Suchtreffer bzw. Werkzeugzusammenfassung
  - **[L]** Lehrbuch- oder Gedaechtniswissen, heute nicht nachgelesen
  - **[P]** Projektdatei gelesen; die Lesetiefe der dortigen Quelle gilt weiter
  - **[ES]** eigener Schluss
  - **H** Hypothese
- **Abstimmung:** Die Video-Datei VIDEO-6r1au5axOXM.md des Parallelagenten existierte bei den Pruefungen um 03:37 und
  03:48 noch nicht. Kein Abgleich moeglich, keine Doppelarbeit erkennbar.
- **Ende (gemessen):** 2026-09-30 03:53:30 CEST (Dauer 18 min 43 s). Die Video-Datei des Parallelagenten fehlte auch
  um 03:53 noch.

---

## Kurzantwort (5 Punkte)

1. **M-Theorie ist bis heute keine fertig formulierte Theorie.** Sie ist ein Netz gut gepruefter Grenzfaelle:
   - 11D-Supergravitation bei niedriger Energie
   - Dualitaeten zu den fuenf Stringtheorien
   - M2- und M5-Branen
   - fuer flachen 11D-Raum die Matrixtheorie (BFSS 1996 [A]); deren D0-Branen-Version ist auf dem Gitter bis auf
     weniger als 10 % gegen die Gravitationsvorhersage getestet [S]

   Kein Experiment beruehrt sie direkt.
2. **Calabi-Yau-Mannigfaltigkeiten (6D) und G2-Mannigfaltigkeiten (7D) machen aus 10 bzw. 11 Dimensionen unsere vier.**
   - Ihre Form- und Groessenparameter (Moduli) waeren masselose Skalare und muessen stabilisiert werden.
   - Explizite de-Sitter-Kandidaten gibt es seit 2024; ob sie alle Korrekturen ueberleben, ist nach Angabe der Autoren
     offen [A].
   - Die Zahl der Moeglichkeiten ist riesig: 473 800 776 reflexive Polytope [A] und etwa 10^272 000 Flussvakua in einer
     einzigen Geometrie [A].
   - Maschinelles Lernen liefert seit 2020 numerische CY-Metriken [L] und seit 2024 physikalische Yukawa-Kopplungen
     einzelner Modelle [S].
3. **Die engste Beruehrung mit uns sind die Glieder 7, 8 und 10 der Spin-2-Kette. Dort macht die Stringtheorie Aussagen
   ueber Tuerme.**
   - Nach der Emergent-String-Vermutung endet jede Grenze im Moduliraum entweder in einem Kaluza-Klein-Turm (massiver
     Spin 2, Glied 8) oder in einem Stringturm (hoehere Spins, Glied 7) [A].
   - Unterschieden werden beide durch das Wachstum der Zustandszahl: polynomial beim KK-Turm, exponentiell beim String
     [A]. J ~ E^2 allein unterscheidet sie nicht.
   - String- und M-Theorie liefern keinen Stelle-Geist: Quadratische Kruemmungsterme treten nur als geistfreies
     Gauss-Bonnet auf [S], die M-Theorie-Korrekturen beginnen bei R^4 [L].
4. **Datennah ist heute nur die Kurzreichweiten-Gravitation, und die entscheidende Region ist noch nicht erreicht.**
   - Die Dunkle Dimension (etwa 1 um [A]) liegt unter der Torsionswaagen-Schranke: lambda < 38,6 um bei |alpha| = 1,
     Radius einer Extradimension < 30 um [A, lokale PDF]. Den Bereich 1 bis 10 um erreicht noch kein Experiment.
   - DESI (2,8 bis 4,2 sigma [A]) ist mit Swampland-Quintessenz vertraeglich, trennt aber nicht.
     - Nach der Neukalibrierung von DES-SN5YR bleiben 3,2 sigma [S].
     - Mit einer Korrektur der Supernovae bei niedriger Rotverschiebung bleiben 0,5 bis 1,5 sigma [S].
   - Das G2-MSSM der M-Theorie sagt ein Gluino von 1 bis 2 TeV voraus [S]. Die LHC-Schranke liegt bei 2,30 TeV
     (vereinfachtes Modell [A]). Das setzt die Vorhersage unter Druck, formal ist sie modellabhaengig.
   - Affleck-Dine-Q-Baelle aus flachen SUSY-Richtungen, Q-Ball-Dunkle-Materie und Oszillonen aus String-Moduli sind
     Literatur [A].
   - Unsere fast verlustfreie 3D-Atmungsmode ist kugelsymmetrisch (l = 0). Nach Birkhoff strahlt sie keine
     Gravitationswellen ab [L]. Ein Bezug zu Zerfallsraten oder GW-Spektren besteht nur als Hypothese ueber die
     Relaxation angeregter Q-Baelle.
   - **Gesamtformel:** nur eine formale Analogie. Der innere Index entspricht einer dekonstruierten Dimension und damit
     einem KK-Turm, bleibt aber skalar und ohne Gravitation [P].

---

## 1 Erwartungsverstoesse (das eigentliche Ergebnis, wichtigstes zuerst)

Die Erwartungen stehen vor jedem Abruf im Arbeitsfeld (Scratchpad, siehe oben).

### V1: Die Yukawa-Staerke eines KK-Turms ist in der Literatur 2n, nicht 8n/3; die Differenz ist genau der vDVZ-Faktor 4/3

- **Erwartet (E25, aus dem Gedaechtnis):** Fuer n Extradimensionen auf einem Torus hat die erste KK-Stufe alpha = 8n/3.
- **Gefunden:**
  - Kehagias und Sfetsos (1999) geben im Abstract alpha = 2n fuer den Torus und n + 1 fuer die Sphaere an [A].
  - Die Uebersicht von Murata, Fujiie und Suzuki (2026) nennt ebenfalls alpha = 2n [A-teil].
  - Lee u. a. (2020) nennen fuer die groesste Extradimension einen Torusradius unter 30 um. In der gelesenen Stelle
    (S. 5) steht kein alpha dazu; eine Textsuche nach "8/3" in der ganzen PDF fand nichts. Die Grenzen fuer +alpha und
    -alpha stehen getrennt im Supplement [A, lokale PDF S. 5].
- **Korrigierte Erwartung [ES], Rechnung aus Lehrbuchbausteinen [L], nicht an einer Quelle geprueft:**
  - Die Zahl 2n ist die Bildladungssumme in D = 4 + n Dimensionen. Normiert wird dabei auf den **gesamten** Nullmodus:
    Graviton plus masseloses Radion.
  - Fuer n = 1 ist das Radion ein Brans-Dicke-Skalar mit omega = 0. Er erhoeht die Newton-Staerke auf (4/3) G_N [L].
  - Jede massive KK-Mode ist fuer n = 1 ein reiner Fierz-Pauli-Spin-2 mit 5 Freiheitsgraden. Sie koppelt mit 4/3 G_N,
    das ist der vDVZ-Faktor aus Glied 8.
  - Die erste Stufe hat zwei Moden. Konsistenzprobe: (2 x 4/3) / (4/3) = 2 = Kehagias-Sfetsos.
  - Ist das Radion stabilisiert (schwer), bleibt als Fernkraft nur G_N. Dann gilt fuer n = 1: **alpha = 8/3 bei
    lambda = R**, dazu ein eigener Radion-Term alpha = +1/3 bei seiner eigenen Reichweite.
  - Cassini verlangt ein schweres oder entkoppeltes Radion.
  - Allgemein fuer n > 1 [ES]: alpha_stab = 2n x 2(n+1)/(n+2).
- **Bedeutung:**
  - Die Kopplungszahlen 4/3 (massiver Spin 2, Glied 8) und 1/3 (Skalar an der Spur, Glied 5) sind **dieselben** wie in
    der Stelle-Newtongrenze. Dort stehen sie mit anderem Vorzeichen und ohne Turm: alpha_2 = -4/3 und alpha_0 = +1/3 [P,
    WARUM-SPIN-2 Nachtrag 27.09.].
  - Ein einziges Kurzreichweiten-Experiment mit Signal koennte so Glied 8 (Turm), Glied 10 (Geist) und Moduli (Skalar)
    trennen. Das ist Karte MT-1.
  - Der Fall gehoert zum Fehlertyp "Messen die zwei Zahlen dasselbe?": 2n und 8n/3 sind auf verschiedene Nullmoden
    normiert.

### V2: Die DESI-Praeferenz fuer dynamische dunkle Energie haengt an der Supernova-Stichprobe, und Phantom-Kreuzen trennt nicht sauber

- **Erwartet (E9, H2):** Swampland-Quintessenz kann w = -1 nicht kreuzen. DESI bevorzugt ein Kreuzen. Also gibt es eine
  Spannung, und das Kreuzen waere ein Trennpunkt.
- **Gefunden:**
  - DESI DR2: BAO+CMB 3,1 sigma; mit Supernovae 2,8 bis 4,2 sigma je nach Stichprobe; w0 > -1, wa < 0 [A].
  - Nach der Neukalibrierung der DES-Supernovae (DES-Dovekie) bleiben 3,2 statt 4,2 sigma [S].
  - Eine Korrektur der Systematik bei niedriger Rotverschiebung senkt auf 0,5 bis 1,5 sigma (arXiv:2502.04212 [S]).
  - Ein effektives Phantom-Kreuzen ist auch mit string-motivierten Modellen moeglich: kinetisch gemischtes Axion-Dilaton,
    gekoppelter Dunkelsektor (arXiv:2508.00621 und Treffer zu 2506.15091 [S]).
- **Korrektur:** Zwei Regime, Moderator Supernova-Kalibrierung bei niedrigem z. Das Kreuzen ist kein sauberer
  Unterscheidungspunkt zwischen Lambda und String-Quintessenz, weil es effektiv nachgebildet werden kann.

### V3: Die TCC-Schranke steht mit DESI nicht im Widerspruch

- **Erwartet (E15):** DESI bevorzugt eine flache Steigung lambda unter der Swampland-Schranke, also eine Spannung.
- **Gefunden:**
  - Akrami, Alestas und Nesseris (2025) finden lambda = 0,698 (+0,173 / -0,202) [S].
  - Bedroya und Vafa (2019) formulieren die TCC als "upper bound of 2/sqrt(d-2) on the asymptotic value of |V'|/V" [A].
  - Dazu kommt eine Innenbedingung V(phi2) <= A exp(-2 (phi2 - phi1) / sqrt((d-1)(d-2))) [A]. Aus ihr folgt eine
    mittlere Steigung von mindestens sqrt(2/3) = 0,816 in 4D [ES].
  - DESIs 0,70 liegt innerhalb von 1 sigma davon.
- **Korrektur:** Heute gibt es weder einen Beleg fuer die Swampland-Quintessenz noch einen Widerspruch zu ihr.

### Kleinere Verstoesse

- **E19:** Die neueste Uebersicht zur Kurzreichweiten-Gravitation (Murata u. a., Mai/Sept. 2026) erwaehnt die Dunkle
  Dimension nicht [A-teil]. Sie fuehrt weiter die UW-Messung von 2020 als fuehrend.
- **E10:** Die ersten physikalischen Yukawa-Kopplungen aus ML-Metriken stammen von Butbaia u. a. 2024 [S]. Aus dem
  Gedaechtnis hatte ich eine andere Gruppe erwartet (Constantin u. a., nicht geprueft).

**Bestaetigte Erwartungen (je eine Zeile):**
- CEMZ [A]
- Emergent-String-Vermutung [A]
- Dunkle Dimension etwa 1 um [A]
- dS-Kandidaten mit Vorbehalt [A]
- Kausalitaetsschranken CHLPSD [A]
- Entartungskriterium [A]
- ATLAS-Gluino 2,30 TeV [A]
- Taylor-Wang 10^272 000 [A]
- Kreuzer-Skarke [A]
- BFSS [A]
- Kusenko-Shaposhnikov [A]
- Oszillonen aus String-Moduli [A]
- Q-Ball-Stoesse mit GW [A]
- Ciurla u. a. 2024 in 1+1D [A]
- G2 mit konischen Singularitaeten weiter nicht konstruiert [S]
- Dunkle Dimension astrophysisch fuer n = 1 frei [S]

---

## 2 Frage 1: Was ist M-Theorie heute?

- **Was sie ist.** Eine 11-dimensionale Quantentheorie, deren Niedrigenergiegrenze die 11D-Supergravitation ist
  (Cremmer, Julia, Scherk 1978 [L]).
  - Sie wurde als Starkkopplungsgrenze des Typ-IIA-Strings gefunden (Witten 1995, hep-th/9503124 [L]).
  - Auf einem Intervall ergibt sie den heterotischen E8xE8-String (Horava, Witten 1996, hep-th/9510209 [L]).
  - Ihre ausgedehnten Objekte sind die M2-Membran und die M5-Brane. Die Weltvolumentheorie der M5 (6D, (2,0)) hat keine
    bekannte Lagrangedichte [L].
- **Matrixtheorie.** BFSS (1996) vermuten eine genaue Gleichheit: M-Theorie im unkompaktifizierten 11D-Raum entspricht
  dem Grenzfall N -> unendlich der supersymmetrischen Matrix-Quantenmechanik von D0-Branen [A].
  - Membranen erscheinen darin als Anregungen der Matrizen.
  - Das Modell gilt als nichtstoerungstheoretische Umsetzung des holographischen Prinzips [A].
- **Stand 2024 bis 2026:**
  - **Mathematisch bzw. auf Konsistenz gesichert (Auswahl):**
    - Vier-Graviton-Streuung in 11D-Supergravitation auf Tori reproduziert bekannte Typ-II-Terme ueber T-Dualitaet
      (Green, Gutperle, Vanhove 1997 [A]).
    - Numerische Gittertests des D0-Branen-Matrixmodells (BMN-Deformation) liegen bei T = 0,25 lambda^(1/3) weniger als
      10 % neben der Supergravitation (JHEP 03 (2023) 071 [S]).
    - D0-Branen-Amplituden haben die volle 11D-Lorentz-Symmetrie (arXiv:2303.14200 [S]).
  - **Offen:**
    - Eine vollstaendige nichtstoerungstheoretische Definition fuer allgemeine Hintergruende, insbesondere fuer
      4D-Kosmologie. Nach Recherchestand (Suche 30.09.2026, Zeitfenster 2024 bis 2026) gibt es keine; neuere Arbeiten
      sind Teilschritte, etwa ein vorgeschlagenes M5-Matrixmodell, arXiv:2607.05490 [S].
    - Die M5-Theorie ohne Lagrangedichte [L].
  - **Experimentell unerreicht:** Alle eigenen Effekte liegen bei der 11D-Planck- bzw. Kompaktifizierungsskala. Pruefbar
    wird etwas nur ueber Kompaktifizierungen (Abschnitte 3 und 5).

**[ES]** "M-Theorie" ist fuer uns kein Rechenobjekt, sondern ein Name fuer ein Netz von Grenzfaellen. Pruefbar sind nur
die Kompaktifizierungen (CY, G2) und ihre Tuerme.

---

## 3 Frage 2: Calabi-Yau- und G2-Mannigfaltigkeiten

### 3.1 Rolle bei der Kompaktifizierung

- **Calabi-Yau-Dreifaltigkeit (CY3, 6 reelle Dimensionen)** [L]: Ricci-flach, Kaehler, Holonomie SU(3).
  - Heterotischer String auf CY3: N = 1 in 4D (Candelas, Horowitz, Strominger, Witten 1985 [L]).
  - Typ II auf CY3: N = 2; N = 1 erst mit Orientifolds.
  - M-Theorie auf CY3: 5D-Theorie.
- **G2-Mannigfaltigkeit (7 Dimensionen):** M-Theorie auf G2 gibt direkt N = 1 in 4D (Atiyah, Witten 2001 [S]).
  - Chirale Fermionen verlangen konische Singularitaeten (Acharya, Witten 2001, hep-th/0109152 [S]).
  - Stand 2025: Keine kompakte Mannigfaltigkeit mit G2-Holonomie und isolierten konischen Singularitaeten ist als
    existent nachgewiesen (Sa Earp, Stein 2025, arXiv:2506.15482 [S]; Suche mit Zeitfenster 2024 bis 2026).
  - Damit fehlt fuer das "realistische" M-Theorie-auf-G2-Bild bis heute ein explizites kompaktes Beispiel **[ES]**.
- **Anzahl der Geometrien:** 473 800 776 reflexive Polytope in 4D. Sie kodieren glatte CY3-Hyperflaechen in torischen
  Varietaeten (Kreuzer, Skarke 2000 [A]).

### 3.2 Moduli und ihre Stabilisierung

- **Moduli** sind die Groessen- und Formparameter der inneren Mannigfaltigkeit (Kaehler- und Komplexstruktur-Moduli)
  [L]. Unstabilisiert waeren sie masselose Skalare, die an Materie koppeln, also fuenfte Kraefte (Abschnitt 5.2).
- **Stabilisierung** [L]: KKLT (2003) und LVS (2005).
- **Explizite Kandidaten:** McAllister, Moritz, Nally, Schachner (2024), "Candidate de Sitter Vacua" [A].
  - Aufbau: Typ-IIB-CY-Orientifolds mit Klebanov-Strassler-Kehle und Anti-D3-Brane.
  - Die Autoren nennen selbst als offen, ob die Vakua die subfuehrenden Korrekturen ueberleben und ob alle
    Quantisierungsbedingungen verstanden sind.

### 3.3 Landschaft und Swampland, Zahl der Vakua

- **Zahl der Vakua:** O(10^272 000) F-Theorie-Flussvakua aus **einer** elliptischen Vierfaltigkeit (Taylor, Wang 2015
  [A]). Die oft genannte Zahl 10^500 stammt aus aelteren Schaetzungen fuer IIB-Flussvakua (Ashok, Douglas 2003 [L]).
- **Swampland:** Gesucht sind Bedingungen, die jede Niedrigenergietheorie mit Quantengravitation erfuellen muss (Vafa
  2005 [L]).
  - **Distanzvermutung** (Ooguri, Vafa 2006 [L]): Bei grossen Wegen im Moduliraum wird ein Turm exponentiell leicht.
  - **Emergent-String-Vermutung** (Lee, Lerche, Weigand 2019 [A]):
    - Jede unendliche Distanz fuehrt entweder zur Dekompaktifizierung (KK-Turm) oder zu einem einzigen asymptotisch
      spannungslosen, schwach gekoppelten heterotischen bzw. Typ-II-String.
    - Analysiert fuer M-Theorie und IIA auf CY3; die Tuerme stammen aus gewickelten Branen.
  - **Beweislage 2024 bis 2026:** Belege, kein allgemeiner Beweis.
    - Bedroya, Mishra, Wiesner 2024 [A]: bottom-up ueber Schwarze Loecher und Amplituden, ohne String oder SUSY
      vorauszusetzen.
    - 5D-Supergravitation, JHEP 06 (2025) 230 (arXiv:2412.12251 [S]).
    - Typ IIB auf CY3 (arXiv:2504.01066 [S]).
    - Gopakumar-Vafa-Invarianten (JHEP 03 (2024) 061 [S]).
  - **dS-Vermutung und TCC:** Die TCC (Bedroya, Vafa 2019) schliesst langlebige metastabile dS-Raeume aus und erlaubt
    hinreichend kurzlebige [A]. Die urspruengliche dS-Vermutung (Obied, Ooguri, Spodyneiko, Vafa 2018 [L]) war strenger.

### 3.4 Maschinelles Lernen auf CY-Metriken

- **Seit 2020:** Neuronale Netze naehern Ricci-flache Metriken an, die nicht geschlossen bekannt sind (Anderson u. a.
  2020, arXiv:2012.04656; Douglas u. a. 2020, arXiv:2012.04797; Jejjala u. a. 2020, arXiv:2012.15821 [L]).
- **2024:** Erste physikalische (normierte) Yukawa-Kopplungen eines heterotischen Modells aus ML-Metriken (Butbaia u. a.
  2024, arXiv:2401.15078 [S]).
  - Dazu das Paket cymyc (arXiv:2410.19728 [S]) und "Precision String Phenomenology" (arXiv:2407.13836 [S]).
- **2026:** Metriken mit Kaehler-Moduli-Abhaengigkeit (arXiv:2603.12384 [S]), mit voller Moduli-Abhaengigkeit
  (arXiv:2606.28487 [S]) und mit Tensornetzwerken (arXiv:2608.16083 [S]).
- **[ES]** Die Methode liefert Zahlen fuer gegebene Modelle. Solange unklar ist, welches Modell unsere Welt ist, ist das
  keine Vorhersage der gemessenen Yukawa-Kopplungen. Methodisch ist es aber dasselbe Problem wie unsere
  Loeserpflichten: eine nichtlineare Feldgleichung numerisch mit Fehlerangabe loesen.

---

## 4 Frage 3: Beruehrungspunkte mit der Spin-2-Kette

### 4.1 Glied 7 (kein Spin >= 3): Stringturm, Regge, CEMZ, Emergent String

- **CEMZ, erstmals im Projekt am Abstract gelesen** (bisher nur zitiert, KARTE-RG1):
  - Hoehere Ableitungskorrekturen zur Drei-Graviton-Kopplung verletzen die Kausalitaet.
  - Zusaetzliche Teilchen mit Spin <= 2 heilen das nicht, sondern nur "an infinite tower of extra massive particles
    with higher spins" [A].
  - Fuer Inflation mit Abweichung von Einstein folgen massive Hoeherspin-Teilchen [A].
- **Caron-Huot, Li, Parra-Martinez, Simmons-Duffin (2022)** [A]:
  - In D = 4 folgen aus Dispersionsrelationen zweiseitige Schranken auf die gravitativen Wilson-Koeffizienten.
  - Die Schranken sind durch die Masse M neuer Hoeherspin-Zustaende ausgedrueckt.
  - Korrekturen muessen gleichmaessig abschalten, wenn die Gravitationskopplung gegen null geht.
- **Emergent String und das Kriterium, das RG-1 noch fehlt:** Bedroya, Mishra und Wiesner (2024) zeigen ohne
  String-Annahme, dass der leichteste Turm "either a KK tower, or has an exponentially growing degeneracy" ist [A].
  - KK-Tuerme haben polynomial wachsende Entartung, Stringtuerme exponentielle [A].
  - **Folge fuer RG-1 [ES]:**
    - RG-1 hat J ~ E^2 gefunden (alpha = 2,012; RUNDE-06.md [P]). Der Autor nennt L1 schwach, weil das aus der
      Ringgeometrie folgt.
    - J ~ E^2 ist die Regge-**Form**. Das trennende String-**Kriterium** ist das Wachstum der Zustandszahl mit der
      Energie.
    - Ein duenner Ring mit Spannung hat Ringschwingungen, die bei linearer Dispersion wie Stringmoden zaehlen, aber nur
      bis zur Wanddicke. Das ist ein effektiver String, wie das Flussrohr der QCD, kein fundamentaler.
    - Karte MT-2 prueft das.
- **Literatur zu Regge-Bahnen von Q-Baellen:** keine gefunden (eine Suche [S]; bestaetigt die vier Suchen des RG-1-Agenten
  [P]). Bekannt ist nur die klassische Quantisierung J = nQ bei drehenden Q-Baellen und Bosonsternen (Treffer zu
  Kleihaus, Kunz, List; arXiv:2302.11589 [S]).

### 4.2 Glied 10 (Eindeutigkeit): hoehere Kruemmungsterme, Stelle

- **Heterotischer String:** Die Korrektur der Ordnung alpha' R^2 ist die Gauss-Bonnet-Kombination. Diese ist geistfrei
  (Zwiebach 1985, PLB 156, 315 [S]).
- **Typ II und M-Theorie:** Die fuehrende Korrektur ist R^4. In 11D stammt sie aus der Einschleifen-Vier-Graviton-
  Amplitude (Green, Gutperle, Vanhove 1997 [A], R^4 selbst [L]).
- **[ES] Folge fuer Glied 10:**
  - String- bzw. M-Theorie bricht die Annahme "zweite Ableitungen" nur durch Terme, die keinen massiven Spin-2-Geist
    einfuehren. Die Abweichung wird durch Tuerme bei der String- bzw. KK-Skala getragen (CEMZ, CHLPSD).
  - Ein gemessener Stelle-Geist (Yukawa mit alpha = -4/3) spraeche also **gegen** die stoerungstheoretische
    String-Niedrigenergietheorie, nicht fuer sie.
  - Das schaerft Glied 10: Stelle und String sind **verschiedene** Auswege aus der Eindeutigkeit.
- **Schranken [P]:** Laborschranke fuer Yukawa-Kraefte gravitativer Staerke: lambda < 38,6 um (Lee u. a. 2020; lokale PDF
  gelesen). Nach der Berichtigung vom 29.09. gilt sie fuer einen **einzelnen** Term mit |alpha| = 1. Fuer Stelle braucht
  es eine gemeinsame Auswertung beider Terme.

### 4.3 Glied 8 (massiver Spin 2): Kaluza-Klein-Tuerme

- **Aufbau:** Jede Kompaktifizierung erzeugt einen Turm massiver Spin-2-Moden mit m_k ~ k/R [L].
  - Nach der Distanzvermutung ist der KK-Turm eine der zwei erlaubten Asymptotiken [A, LLW].
  - Nach Endlich u. a. (arXiv:1704.01590 [P]) vermittelt ein solcher Turm eine Yukawa-Kraft gravitativer Staerke.
- **Neu hier (V1, [ES]):** Die Yukawa-Staerke der ersten KK-Stufe **enthaelt den vDVZ-Faktor 4/3**.
  - alpha = 2 (Literatur, masseloses Radion im Nullmodus) oder 8/3 (stabilisiertes Radion) fuer eine Dimension.
  - Glied 8 ist damit im Labor nicht nur ueber m_g (GW-Schranke 2,42e-23 eV [P]) messbar, sondern auch ueber die
    Staerke kurzreichweitiger Yukawa-Terme.

---

## 5 Frage 4: Datennahe Konsequenzen

### 5.1 Dunkle Dimension

- **Vorhersage:** Montero, Vafa, Valenzuela (2022, JHEP 2023) sagen "a light tower of states and a unique extra
  mesoscopic dimension" voraus, von etwa 1e-6 m [A].
  - Grundlage: die kleine kosmologische Konstante plus Swampland-Prinzipien.
  - Die Speziesskala liegt bei 1e9 bis 1e10 GeV; Bulk-Fermionen liefern sterile Neutrinos [A].
- **Labor:**
  - Lee u. a. 2020 [A, lokale PDF S. 5]: "any gravitational-strength Yukawa interaction must have lambda < 38.6 um".
  - Folgerungen dort: Dilaton- bzw. Schwergraviton-Masse > 5,1 meV; Torusradius der groessten Extradimension < 30 um.
  - Der beste Fit liegt bei lambda = 7,1 um mit dchi^2 = 3,3. Die Autoren setzen danach Schranken und behaupten kein
    Signal.
  - Die neueste Uebersicht (Murata u. a. 2026 [A-teil]) fuehrt weiter die UW-Messung von 2020 und schliesst das
    KK-Modell grob fuer lambda > 1e-5 m aus.
  - Vorschlaege fuer 1 bis 100 um: mikroskalige Torsionsresonatoren (PRD 110, 122005 (2024), arXiv:2406.13020 [S]),
    nanofabrizierte Torsionspendel (arXiv:2601.11366 [S]).
- **Astrophysik:**
  - n = 1 ist nicht auf Mikrometer gedrueckt (SN 1987A: R < 490 m fuer n = 1; arXiv:2510.18975 [S]).
  - n = 2 ist nur ohne Isometrien lebensfaehig (Anchordoqui, Antoniadis, Luest 2025 [P, dort Abstract]).
- **Heute pruefbar?**
  - Nur die Oberkante (R < 30 um) ist gemessen.
  - Der vorhergesagte Kern (etwa 1 um, dazu 1 bis 10 um aus der Folgeliteratur [S]) liegt ein bis zwei Groessenordnungen
    darunter.
  - Dort dominieren Casimir-Kraefte [A-teil, Murata]. Eine Messung mit |alpha| ~ 2 bis 3 bei 1 bis 10 um fehlt.
- **Offene Frage [ES]:** Mehrere Arbeiten passen das Radion der Dunklen Dimension als Quintessenz an DESI an [P:
  Suchtreffer 2506.02731, 2609.25230].
  - Dann waere es im Labor praktisch masselos.
  - Mit Gravitationsstaerke (alpha_s^2 = 1/3) verletzte es die Cassini-Schranke. Seine Materiekopplung muss also stark
    unterdrueckt sein.
  - Wie die Arbeiten das loesen, ist nicht geprueft.

### 5.2 Fuenfte Kraefte durch Moduli, Aequivalenzprinzip

- **Unstabilisierte Moduli:** Sie waeren Skalare mit Kopplung an die Spur.
  - Bei universeller Kopplung trifft sie das Kurzreichweiten-Labor: Dilatonmasse > 5,1 meV [A, Lee 2020].
  - Bei stoffabhaengiger Kopplung trifft sie der Test des Aequivalenzprinzips. MICROSCOPE (Touboul u. a. 2022, PRL 129,
    121102) liegt bei eta ~ 1e-15 [L, nicht nachgelesen].
- **[ES]** Beide Schranken zusammen verlangen: Moduli sind schwer (meV und mehr) oder fast entkoppelt. Das ist der
  Grund, warum Moduli-Stabilisierung (Abschnitt 3.2) Pflicht ist.

### 5.3 Swampland und dunkle Energie (DESI)

- **Daten und Fits:**
  - DESI DR2: w0 > -1, wa < 0; 2,8 bis 4,2 sigma je nach Supernova-Stichprobe [A].
  - Exponentielle Quintessenz: lambda = 0,698 (+0,173 / -0,202), 3,3 bis 3,8 sigma besser als Lambda-CDM (Akrami u. a.
    2025 [S]).
- **Vertraeglichkeit:**
  - Mit der TCC-Innenbedingung vertraeglich (V3).
  - Die Signifikanz ist stichprobenabhaengig (V2).
  - Ein effektives Phantom-Kreuzen ist string-motiviert moeglich (V2).
- **Uebersicht:** Andriot (2026), "Dark energy from string theory: an introductory review", behandelt dS-Konstruktionen
  und exponentielle Quintessenz [A, nur Abstract].
- **Urteil:** Kein trennender Test heute. "Widerlegt" ist nach der 24-Monats-Suche nichts davon.

### 5.4 Einzige Teilchenphysik-Zahl aus einer M-Theorie-Kompaktifizierung: das G2-MSSM

- **Vorhersage** (Acharya, Kane, Kumar 2012 [A]): hohe SUSY-Bruchskala, fuer den LHC zu schwere Skalare, Gluino-
  Produktion in vielen Faellen und eine "robuste" Higgsmasse um 125 GeV.
  - Das Gluino-Band liegt bei 1 bis 2 TeV (um 1,5) [S].
  - Die Vorhersage kam im April 2012, nach den ersten 125-GeV-Hinweisen vom Dezember 2011 [L].
- **LHC:** ATLAS schliesst mit 139 fb^-1 Gluinos bis 2,30 TeV aus (vereinfachtes Modell) [A].
  - Eine Analyse der Kane-Gruppe von 2018 hielt 1,7 und 1,9 TeV wegen anderer Zerfallstopologien fuer erlaubt
    (arXiv:1803.04394 [S]).
  - Ein Update von 2024 bis 2026 wurde nicht gefunden.
- **Urteil:** unter Druck, nach Recherchestand nicht formal widerlegt.

---

## 6 Frage 5: Q-Baelle in String-, SUSY- und M-Theorie-Kontexten

- **Affleck-Dine-Q-Baelle:**
  - Flache Richtungen des MSSM tragen Baryon- oder Leptonzahl. Grosse Q-Baelle sind stabil und ein DM-Kandidat
    (Kusenko, Shaposhnikov 1997 [A]).
  - Ihre Bildung aus dem AD-Kondensat ist nachgerechnet (Kasuya, Kawasaki 2000 [P, im Projekt gelesen]).
  - Unser U(S) = S - S^2 + S^3/2 ist Battye-Sutcliffe Typ I [P]. AD-Potentiale sind logarithmisch flach [L]. Das ist
    nicht dasselbe Potential.
- **Oszillonen aus String-Moduli:**
  - Das KKLT-Volumenmodul und das LVS-Blow-up-Modul bilden nach Inflation Oszillonen: lokalisierte, langlebige,
    nichtlineare Anregungen (Antusch u. a. 2017 [A]).
  - Deren GW liegen bei niedrigeren Frequenzen als beim Preheating [A].
  - Das ist das reelle Geschwister unseres Q-Balls und der naechste String-Bezug.
- **Gravitationswellen:**
  - Q-Ball-Bildung (arXiv:0912.3585 [S]; 2104.04682 [S])
  - Poltergeist-Verstaerkung beim ploetzlichen Q-Ball-Zerfall (arXiv:2105.11655, PRL [S]; 2308.13134 [S]; Uebersicht
    2511.07266 [S])
  - Q-Ball-Stoesse mit neuem Code fuer Skalarfeld plus Gravitation, Szenario AD-Fragmentierung (Hong, Lonsdale 2024 [A])
- **Stoerungsspektrum:** Ciurla, Dorey, Romanczukiewicz, Shnir (2024) finden Normalmoden, langlebige Quasinormalmoden und
  Streumoden, sowie negativen Strahlungsdruck [A].
  - Das gilt nur in 1+1D.
  - Ein 3D-BIC wurde in den Treffern nicht gefunden. L4 fuer den RUNDE-06-Befund bleibt offen [S].

**Beruehrt unser Befund diese Szenarien? Nur als Hypothesen:**

- **H-Q1 [ES]:** Die fast verlustfreie Atmungsmode bei omega*^2 = 0,79768 ist l = 0, also kugelsymmetrisch.
  - Nach dem Birkhoff-Theorem strahlt eine kugelsymmetrische Pulsation **keine** Gravitationswellen ab [L].
  - Direkt veraendert der Befund daher kein GW-Spektrum. Gravitativ strahlen koennten nur l >= 2-Moden, zum Beispiel die
    gebundene l = 2-Formschwingung bei omega^2 = 0,6 aus RUNDE-06.
  - Ihre Amplitude waere nur fuer astrophysikalisch schwere Q-Baelle relevant (nicht abgeschaetzt).
- **H-Q2 [ES]:** Indirekt koennte eine BIC-nahe Mode die Relaxation frisch gebildeter Q-Baelle aendern. Anregungsenergie
  bliebe dann lange im Ball, statt als Skalarstrahlung abzufliessen.
  - Das beruehrt Poltergeist-Szenarien nur, wenn die Q-Baelle nahe omega* entstehen und das Potential dieselbe Nullstelle
    hat.
  - Beides ist offen (Karte MT-3).
- **H-Q3 [ES]:** Der Zerfall von AD-Q-Baellen laeuft ueber Verdampfen in Fermionen an der Oberflaeche [L]. Das ist ein
  anderer Kanal als unsere klassische Skalarabstrahlung. Ohne Fermionkopplung sagt unser Befund dazu nichts.

---


    der Energie-Impuls-Tensor [P].
  - In String- und M-Theorie ist das Graviton ein masseloser Spin-2-Zustand mit universeller Kopplung an T [L]. Beide
    Glieder sind dort erfuellt.
  - Brane-Welt-Modelle mit veraenderlicher Lichtgeschwindigkeit habe ich nicht geprueft. Sie begruenden keinen Bezug.
- **Gesamtformel: nur formale Analogie.**
  - Die Gesamtformel ist eine klassische Theorie von N komplexen Skalaren im flachen R^3 x R, mit von Hand gesetztem U(S)
    und dem Kopplungsterm g J_ab Re[(psi_a^* psi_b)^2] [P, KANDIDAT.md].
  - **Formaler Beruehrungspunkt:** Der innere Index mit Kopplungsgraph J_ab ist ein "Theorieraum" wie bei der
    Dekonstruktion. Er ist empirisch gleich einem 4D-KK-Turm [P, Messlage 25.09.].
  - KK-Tuerme sind genau das, was CY- bzw. M-Kompaktifizierungen liefern.
  - **Der Unterschied ist entscheidend:** Der Turm der Gesamtformel ist skalar und ohne Gravitation. Die
    Torsionswaagen-Schranken treffen ihn deshalb nicht [P], und die vDVZ-Zahlen aus V1 gelten fuer ihn nicht.
  - Eine Herleitung von U(S) aus einer SUSY- oder M-Theorie-Kompaktifizierung gibt es nach Recherchestand nicht.

---

## 8 Regime und Moderatoren (Regel 1)

| Widerspruch bzw. Streuung | Vermuteter Moderator | Beleg |
|---|---|---|
| DESI 4,2 gegen 3,2 gegen 0,5 bis 1,5 sigma | Supernova-Stichprobe, Kalibrierung bei niedrigem z | [A] DESI; [S] Dovekie, 2502.04212 |
| n = 2 Dunkle Dimensionen ausgeschlossen gegen erlaubt | Isometrien des kompakten Raums (KK-Impulserhaltung) | [P] Messlage V1; [S] 2510.18975 |
| KK-alpha 2n gegen 8n/3 | Radion masselos oder stabilisiert (Normierung des Nullmodus) | [A] Kehagias-Sfetsos; [ES] |
| Regge J ~ E^2 bei Ringen gegen bei Strings | effektiver String mit Dicke gegen fundamentaler String; Entartungswachstum | [A] BMW 2024; [ES] |
| G2-MSSM erlaubt gegen ausgeschlossen | Zerfallstopologie: vereinfachtes Modell gegen UV-Modell | [A] ATLAS; [S] 1803.04394 |
| Atmungsbreite: 1D monoton gegen 3D mit Nullstelle | Dimension (bekannt aus RUNDE-06); Potentialform offen | [P] RUNDE-06 |

---

## 9 Unterscheidungspunkte (Regel 2)

1. **KK-Turm (Glied 8) gegen Stelle-Geist (Glied 10) gegen Modul (Glied 5):**
   - Die Deutungen laufen im Yukawa-Fingerabdruck auseinander:
     - KK-Turm: +8/3 je Stufe bei lambda = R, R/2, ... (n = 1, stabilisiertes Radion [ES])
     - Stelle: -4/3 und +1/3 je einmal
     - Modul: +alpha einmal, stoffabhaengig moeglich
   - Region: lambda ~ 1 bis 30 um, |alpha| ~ 0,3 bis 3.
   - Heute zugaenglich nur oberhalb etwa 30 bis 40 um.
   - Vektorkraefte (B-L) geben ebenfalls negatives alpha, sind aber stoffabhaengig [L]. Das Vorzeichen allein trennt
     also nicht; Vorzeichen plus Stoffunabhaengigkeit plus Stufenfolge trennt [ES].
2. **Emergenter String gegen KK:**
   - Trennt sich an der Entartung (exponentiell gegen polynomial) bei Energien an der Turmskala [A].
   - Experimentell unzugaenglich, in unseren Modellen rechenbar (MT-2).
3. **Swampland-Quintessenz gegen Lambda:** w(z) + 1 bei z ~ 0,3 bis 1 auf Prozentniveau.
   - Einfeld-Quintessenz kreuzt w = -1 nicht, effektive Modelle schon (V2).
   - Heute nicht trennbar.
4. **Effektiver gegen fundamentalen String:**
   - Beim effektiven String bricht der Turm an der Wanddicke ab bzw. biegt ab, beim fundamentalen nicht.
   - Bei unseren Ringen ist die Region k ~ 1/w rechenbar.
5. **Atmungs-BIC als Modellzufall gegen Struktur:** Nullstelle in einem zweiten Potential (MT-3). Existiert sie nur im
   Sextik-Modell, ist sie fuer AD-Szenarien bedeutungslos.

---

## 10 Was davon beruehrt uns

| Strang | Bezug | Hypothese oder Befund | Naechster kleiner Test |
|---|---|---|---|
| RG-1 Regge (Glied 7) | J ~ E^2 ist Regge-Form; String-Kriterium ist exponentielle Entartung (BMW 2024) | Befund RG-1 (alpha = 2,012, L1 schwach) plus Hypothese | MT-2: Ringmoden-Dispersion |
| Glied 8, KK-Tuerme | Yukawa-Staerke der KK-Stufe enthaelt vDVZ 4/3 | [ES] Hypothese, Literatur sagt 2n | MT-1: Papierrechnung plus Ablesen Lee 2020 |
| Glied 10, Stelle | String liefert Gauss-Bonnet (geistfrei), M-Theorie R^4; Stelle-Geist spraeche gegen String-EFT | Literatur [S]/[L] plus [ES] | kein eigener Test; Nachtrag in WARUM-SPIN-2 vorschlagen |
| Glied 7 massiv plus 10, gekoppelt | CEMZ und CHLPSD: Korrekturen nur mit Hoeherspin-Turm bei Skala M | Literatur [A] | keiner |
| Dunkle Dimension | Kern 1 bis 10 um, gemessen bis etwa 30 bis 40 um | Literatur [A] | keiner lokal; Torsionsresonator-Vorschlaege beobachten |
| DESI und Swampland | vertraeglich, nicht trennend | Literatur [A]/[S] | keiner |
| Moduli, fuenfte Kraft | Dilaton > 5,1 meV; EP 1e-15 | Literatur | keiner |
| 3D-Atmungs-BIC | AD-Q-Baelle, Oszillonen aus Moduli; l = 0 ohne GW | Hypothese H-Q1 bis H-Q3 | MT-3: BIC im Log-Potential |
| Gesamtformel, innerer Index | Dekonstruktion ~ KK-Turm, aber skalar und ohne Gravitation | formale Analogie | keiner |

---

## 11 Versuchskarten (v3-Format, hoechstens drei)

### MT-1: Yukawa-Fingerabdruck von Turm, Geist und Skalar (Papier)

- **Hypothese:** Die Yukawa-Terme kurzreichweitiger Gravitation tragen die Kopplungszahlen der Spin-2-Kette.
  - KK-Turm, n = 1, stabilisiertes Radion: +8/3 je Stufe = 2 x 4/3 (vDVZ, Glied 8)
  - Radion bzw. Skalaron: +1/3 (Brans-Dicke omega = 0, Glied 5)
  - Stelle-Geist: -4/3
  - Der Literaturwert 2n entspricht dem masselosen Radion.
- **Kleiner Test (Papier, hoechstens 10 min):**
  - (a) 5D-Bildladungssumme fuer eine Dimension ausschreiben und in Graviton (1), Radion (1/3) und KK-Stufen zerlegen;
    pruefen, ob 8/3 bzw. 2 herauskommen.
  - (b) Aus Lee u. a. 2020, Supplement (+alpha und -alpha getrennt), lambda_max ablesen fuer alpha = +8/3, +2, +1/3 und
    -4/3.
- **Gegenprobe:** Fuer r -> 0 muss die Summe das 5D-Gesetz mit Vorfaktor (D-3)/(D-2) = 2/3 statt 1/2 geben, also das
  Verhaeltnis 4/3.
- **Latten:**
  - L1: kann scheitern; wenn die Zerlegung nicht 4/3 je Mode gibt, faellt die V1-Deutung.
  - L2: 5D-Grenzfall
  - L3: Ablesegenauigkeit der Kurve angeben
  - L4: Kehagias-Sfetsos (2n) [A]; 8n/3 aus dem Gedaechtnis, unbelegt
  - L5: direkter Messbezug (Lee 2020, Eoet-Wash)

### MT-2: RG-2, zaehlt der Q-Ball-Ringturm wie ein String? (Glied 7)

- **Hypothese:** Duenne drehende Q-Ball-Ringe (grosses m) haben radiale Ringverformungen mit Winkelzahl j und nahezu
  linearer Dispersion omega_j ∝ j bis j ~ R/w. Quantisiert gezaehlt waechst die Zustandszahl dann exponentiell in
  sqrt(E), also stringartig, aber nur bis zur Wanddicke w.
  - **Gegenhypothese:** omega_j ∝ j^2 (Biegewellen) oder Instabilitaet. Dann ist die Zaehlung nicht Hagedorn-artig, und
    der Turm ist hoechstens KK-artig.
- **Kleiner Test (hoechstens 10 min, p4000 oder CPU):**
  - Linearisierung um die m-Ringe aus regge/regge2d.py (m = 6, 8)
  - Eigenfrequenzen omega_j fuer j = 2 bis 20; Fit omega_j ∝ j^p
- **Gegenprobe:** j = 1 muss die Translations-Nullmode geben (omega = 0 im mitbewegten Sinn). m = 0 hat keinen Ring;
  dort gibt es keine Ringmoden.
- **Latten:**
  - L1: ja, p ist offen
  - L2: Nullmode
  - L3: halbe Schrittweite
  - L4: Kelvin-Wellen an Wirbelringen und effektive Strings sind Literatur [L]; das Kriterium ist BMW 2024 [A]
  - L5: kein Messbezug, nur Glied-7-Bruecke als Hypothese
- **Vorbehalt:** Drehende 2D-Baelle sind oft instabil (KARTE-RG1). Instabile j-Moden sind ein Ergebnis, kein Fehler.

### MT-3: Gibt es die 3D-Atmungs-Nullstelle auch im Affleck-Dine-Potential?

- **Hypothese:** Die Nullstelle der l = 0-Breite (omega*^2 = 0,79768 im Sextik-Modell) tritt auch im eichvermittelten
  AD-Potential V = m^4 ln(1 + |phi|^2/m^2) bei einer Frequenz omega_AD auf.
  - **Gegenhypothese:** Sie ist ein Zufall des Sextik-Modells. Fuer AD-Q-Baelle gilt sie dann nicht.
- **Kleiner Test (hoechstens 10 min):** vorhandene 3D-Polsuche aus RUNDE-06 mit getauschtem Potential; l = 0; 10 Werte
  omega^2 im Existenzbereich; drei Gitterstufen.
- **Gegenprobe:** Sextik-Modell reproduziert omega*^2 = 0,7977; Negativkontrolle ohne Ball.
- **Latten:**
  - L1: ja
  - L2: Sextik-Reproduktion
  - L3: drei Gitter
  - L4: Ciurla u. a. 2024 (1D, Quasinormalmoden) [A]; ein 3D-BIC ist nicht in der Literatur gefunden [S]
  - L5: schwach; l = 0 strahlt keine GW (Birkhoff [L]), Bezug nur ueber die Relaxation nach der Bildung

---

## 12 Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. **"KK-alpha ist 8n/3"**
   - Geprueft: Die Literatur sagt 2n. Das ist Erwartungsverstoss V1 und fuehrt zur Radion-Deutung [ES].
   - Nicht geprueft: welches alpha Lee u. a. 2020 fuer "R < 30 um" nutzen (Supplement nicht gelesen).
2. **"Die Dunkle Dimension lebt"**
   - Geprueft: n = 1 ist astrophysikalisch frei (SN 1987A: R < 490 m [S]). Im Labor ist nur R < 30 um gemessen.
3. **"Stringtheorie sagt Stelle-Gravitation"**
   - Geprueft: nein. Im heterotischen String tritt R^2 als Gauss-Bonnet auf, ohne Geist [S].
4. **"Das DESI-Signal ist robust"**
   - Geprueft: Es haengt an der Supernova-Kalibrierung (V2).
5. **"Unsere l = 0-Atmung koennte GW abstrahlen"**
   - Nicht nachgelesen: Birkhoff ist Lehrbuch [L]. Damit faellt der direkte GW-Bezug.
6. **"Unser U(S) ist ein SUSY-Potential"**
   - Nicht geprueft: AD-Potentiale sind logarithmisch flach [L]. MT-3 prueft die Uebertragbarkeit.

Die Punkte 1 bis 4 sind tatsaechlich geprueft.

---

## 13 Kalibrierung

- **(a) Gemessen:**
  - Kurzreichweiten-Gravitation: lambda < 38,6 um bei |alpha| = 1 und R < 30 um (Lee u. a. 2020)
  - DESI DR2: 2,8 bis 4,2 sigma, nach Neukalibrierung 3,2 sigma
  - ATLAS: Gluino > 2,30 TeV (vereinfachtes Modell)
  - MICROSCOPE: eta ~ 1e-15 [L]
  - D0-Matrixmodell auf dem Gitter: unter 10 % zur Supergravitation [S]
  - Bei allem ausser dem Gitter ist die Aussage "keine Abweichung gefunden".
- **(b) Nuetzlich verdichtet:**
  - CEMZ und CHLPSD: Theoreme unter Annahmen wie Kausalitaet und schwache Kopplung
  - Emergent-String-Vermutung, Distanzvermutung, TCC: Vermutungen mit wachsender Belegbasis, ohne Beweis
  - Dunkle Dimension: Folgerung aus einer Kette von Vermutungen, keine Messung
  - ML-CY-Metriken: Numerik mit Fehlerbalken fuer gegebene Modelle
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "10^500 Vakua" als feste Zahl (es sind Abschaetzungen, und die Zahl haengt an der Klasse)
  - "M-Theorie ist die eine Theorie" (keine vollstaendige Formulierung)
  - "Die Dunkle Dimension sitzt bei 1 um" (Kettenschluss)
- **Warnzeichen in dieser Recherche:**
  - Meine Sicherheit in der Radion-Deutung von V1 ist waehrend der Arbeit gestiegen. Grund war nur eine eigene
    Konsistenzprobe ((8/3)/(4/3) = 2), keine Quelle.
  - Sie ist deshalb als [ES] und Hypothese gefuehrt. MT-1 soll sie scheitern lassen koennen.

---

## 14 Offene Fragen

1. Welches alpha nutzen Lee u. a. 2020 fuer "R < 30 um"? (Supplement; beantwortet V1 teilweise)
2. Steht die Radion-Deutung (2n gegen 8n/3) ausdruecklich in einer Quelle? Die Adelberger-Uebersichten waeren der
   naechste Ort [L].
3. Wie loesen die Radion-Quintessenz-Arbeiten zur Dunklen Dimension die Fuenfte-Kraft-Schranke?
4. Existiert die 3D-Atmungs-Nullstelle auch in AD-Potentialen (MT-3)? Gibt es 3D-BIC-Literatur zu Q-Baellen oder
   Oszillonen? Treffer 2607.15624 (Oszillon-Floquet-Moden) ungelesen.
5. G2-MSSM nach Run 2/3: kein Update 2024 bis 2026 gefunden.
6. Welche TCC-Zahl gilt fuer die heutige, nicht asymptotische Kosmologie?

---

## 15 Quellenliste

**An der Quelle gelesen [A]** (arXiv-Abstract ueber das Abrufwerkzeug, 30.09.2026, bzw. lokale PDF)

1. X. O. Camanho, J. D. Edelstein, J. Maldacena, A. Zhiboedov (2014), Causality Constraints on Corrections to the
   Graviton Three-Point Coupling. https://arxiv.org/abs/1407.5597
2. S.-J. Lee, W. Lerche, T. Weigand (2019), Emergent Strings from Infinite Distance Limits.
   https://arxiv.org/abs/1910.01135
3. M. Montero, C. Vafa, I. Valenzuela (2022, JHEP 2023), The Dark Dimension and the Swampland.
   https://arxiv.org/abs/2205.12293
4. L. McAllister, J. Moritz, R. Nally, A. Schachner (2024), Candidate de Sitter Vacua. https://arxiv.org/abs/2406.13751
5. DESI Collaboration (2025), DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological
   Constraints. https://arxiv.org/abs/2503.14738
6. S. Caron-Huot, Y.-Z. Li, J. Parra-Martinez, D. Simmons-Duffin (2022), Causality constraints on corrections to
   Einstein gravity. https://arxiv.org/abs/2201.06602
7. A. Bedroya, R. K. Mishra, M. Wiesner (2024, JHEP 01/2025), Density of States, Black Holes and the Emergent String
   Conjecture. https://arxiv.org/abs/2405.00083
8. J. Murata, T. Fujiie, S. Suzuki (2026), Short-Range Tests of the Gravitational Inverse-Square Law.
   https://arxiv.org/abs/2605.18212 [A-teil: HTML ueber Werkzeug; eine Zahl der Werkzeugzusammenfassung als
   unplausibel verworfen]
9. D. Andriot (2026), Dark energy from string theory: an introductory review. https://arxiv.org/abs/2603.25797 (nur
   Abstract)
10. ATLAS Collaboration (2021, JHEP 02), Search for squarks and gluinos in final states with jets and missing transverse
    momentum using 139 fb^-1 ... https://arxiv.org/abs/2010.14293
11. D. Ciurla, P. Dorey, T. Romanczukiewicz, Y. Shnir (2024), Perturbations of Q-balls: from spectral structure to
    radiation pressure. https://arxiv.org/abs/2405.06591
12. D. K. Hong, S. J. Lonsdale (2024), Q-ball collisions and their Gravitational Waves. https://arxiv.org/abs/2408.12342
13. A. Kehagias, K. Sfetsos (1999), Deviations from the 1/r^2 Newton law due to extra dimensions.
    https://arxiv.org/abs/hep-ph/9905417
14. A. Bedroya, C. Vafa (2019), Trans-Planckian Censorship and the Swampland. https://arxiv.org/abs/1909.11063
15. B. S. Acharya, G. Kane, P. Kumar (2012), Compactified String Theories -- Generic Predictions for Particle Physics.
    https://arxiv.org/abs/1204.2795
16. W. Taylor, Y.-N. Wang (2015), The F-theory geometry with most flux vacua. https://arxiv.org/abs/1511.03209
17. M. B. Green, M. Gutperle, P. Vanhove (1997), One loop in eleven dimensions. https://arxiv.org/abs/hep-th/9706175
18. M. Kreuzer, H. Skarke (2000), Complete classification of reflexive polyhedra in four dimensions.
    https://arxiv.org/abs/hep-th/0002240
19. S. Antusch, F. Cefala, S. Krippendorf, F. Muia, S. Orani, F. Quevedo (2017), Oscillons from String Moduli.
    https://arxiv.org/abs/1708.08922
20. A. Kusenko, M. Shaposhnikov (1997), Supersymmetric Q-balls as dark matter. https://arxiv.org/abs/hep-ph/9709492
21. T. Banks, W. Fischler, S. H. Shenker, L. Susskind (1996), M Theory As A Matrix Model: A Conjecture.
    https://arxiv.org/abs/hep-th/9610043
22. J. G. Lee, E. G. Adelberger, T. S. Cook, S. M. Fleischer, B. R. Heckel (2020), New Test of the Gravitational 1/r^2
    Law at Separations down to 52 um, PRL 124, 101101. https://arxiv.org/abs/2002.11761 (lokale PDF,
    coordination/zusatzdimension-20260924/quellen-messlage/arxiv-2002.11761.pdf, S. 5 per pdftotext)

**Nur Suchtreffer [S]** (Autoren nur, wo im Treffer genannt)

23. Y. Akrami, G. Alestas, S. Nesseris (2025), Has DESI detected exponential quintessence?
    https://arxiv.org/abs/2504.04226
24. The DESI DR1/DR2 evidence for dynamical dark energy is biased by low-redshift supernovae (2025).
    https://arxiv.org/abs/2502.04212
25. Study of dynamical dark energy using DESI DR2 BAO, CMB, and Type Ia supernovae (2026), mit DES-Dovekie.
    https://arxiv.org/abs/2609.10567
26. Effective Phantom Divide Crossing with Standard and Negative Quintessence (2025). https://arxiv.org/abs/2508.00621
27. Could We Be Fooled about Phantom Crossing? (2025). https://arxiv.org/abs/2506.15091
28. DESI constraints on two-field quintessence with exponential potentials (2025). https://arxiv.org/abs/2510.21627
29. Breaking Free from the Swampland of Impossible Universes (2026). https://arxiv.org/abs/2605.10476
30. Asymptotics of 5d supergravity theories and the emergent string conjecture, JHEP 06 (2025) 230.
    https://arxiv.org/abs/2412.12251
31. Emergent Strings in Type IIB Calabi-Yau Compactifications (2025). https://arxiv.org/abs/2504.01066
32. Gopakumar-Vafa Invariants and the Emergent String Conjecture, JHEP 03 (2024) 061. https://arxiv.org/abs/2309.10024
33. Microscale torsion resonators for short-range gravity experiments, PRD 110, 122005 (2024).
    https://arxiv.org/abs/2406.13020
34. Nanofabricated torsion pendulums for tabletop gravity experiments (2026). https://arxiv.org/abs/2601.11366
35. Stellar cooling limits on KK gravitons and dark dimensions (2025). https://arxiv.org/abs/2510.18975
36. A. Butbaia, D. Mayorga Pena, J. Tan, P. Berglund, T. Huebsch, V. Jejjala, C. Mishra (2024), Physical Yukawa
    Couplings in Heterotic String Compactifications. https://arxiv.org/abs/2401.15078
37. cymyc: Calabi-Yau Metrics, Yukawas, and Curvature (2024). https://arxiv.org/abs/2410.19728
38. P. Berglund u. a. (2024), Precision String Phenomenology. https://arxiv.org/abs/2407.13836
39. Calabi-Yau Metrics with Kaehler Moduli Dependence (2026). https://arxiv.org/abs/2603.12384
40. Calabi-Yau Metrics with Full Moduli Dependence (2026). https://arxiv.org/abs/2606.28487
41. Positive Tensor-Network Kaehler Metrics on gCICY Threefolds (2026). https://arxiv.org/abs/2608.16083
42. Revisiting Gluinos at LHC (2018). https://arxiv.org/abs/1803.04394
43. H. Sa Earp, J. R. Stein (2025), Isolated singularities in G2-structures with torsion.
    https://arxiv.org/abs/2506.15482
44. Compact holonomy G2 manifolds need not be formal (2024). https://arxiv.org/abs/2409.04362
45. B. S. Acharya, E. Witten (2001), Chiral Fermions from Manifolds of G2 Holonomy. https://arxiv.org/abs/hep-th/0109152
46. M. Atiyah, E. Witten (2001/2002), M-Theory Dynamics On A Manifold of G2 Holonomy, ATMP 6.
    https://arxiv.org/abs/hep-th/0107177
47. Precision test of gauge/gravity duality in D0-brane matrix model at low temperature, JHEP 03 (2023) 071.
    https://link.springer.com/article/10.1007/JHEP03(2023)071
48. Lorentz Symmetry and IR Structure of the BFSS Matrix Model, JHEP 07 (2023) 150. https://arxiv.org/abs/2303.14200
49. A Novel Matrix Model for the M5-brane? (2026). https://arxiv.org/abs/2607.05490
50. Detectable Gravitational Wave Signals from Affleck-Dine Baryogenesis (2021, PRL). https://arxiv.org/abs/2105.11655
51. Enhancement of gravitational waves at Q-ball decay including non-linear density perturbations (2023).
    https://arxiv.org/abs/2308.13134
52. The poltergeist mechanism (2025). https://arxiv.org/abs/2511.07266
53. Gravitational Waves from Q-ball Formation (2009). https://arxiv.org/abs/0912.3585
54. Q-balls Formation and the Production of Gravitational Waves (2021). https://arxiv.org/abs/2104.04682
55. Quasi Q-Balls in massless scalar fields (2025). https://arxiv.org/abs/2503.07758
56. Oscillon Floquet Modes and the Operators that Excite Them (2026). https://arxiv.org/abs/2607.15624
57. Slowly rotating Q-balls (EPJC 2024). https://arxiv.org/abs/2302.11589
58. B. Zwiebach (1985), Curvature squared terms and string theories, PLB 156, 315.
    https://doi.org/10.1016/0370-2693(85)91616-8

**Gedaechtnis bzw. Lehrbuch [L]** (heute nicht nachgelesen)

- E. Witten (1995), String theory dynamics in various dimensions, hep-th/9503124
- P. Horava, E. Witten (1996), hep-th/9510209
- E. Cremmer, B. Julia, J. Scherk (1978), PLB 76, 409
- P. Candelas, G. Horowitz, A. Strominger, E. Witten (1985), NPB 258, 46
- S. Kachru, R. Kallosh, A. Linde, S. Trivedi (2003), hep-th/0301240
- V. Balasubramanian, P. Berglund, J. Conlon, F. Quevedo (2005), hep-th/0502058
- C. Vafa (2005), hep-th/0509212
- H. Ooguri, C. Vafa (2006), hep-th/0605264
- G. Obied, H. Ooguri, L. Spodyneiko, C. Vafa (2018), arXiv:1806.08362
- S. Ashok, M. Douglas (2003), hep-th/0307049
- P. Touboul u. a. (2022), MICROSCOPE, PRL 129, 121102
- L. Anderson u. a. (2020), arXiv:2012.04656
- M. Douglas u. a. (2020), arXiv:2012.04797
- V. Jejjala u. a. (2020), arXiv:2012.15821
- Birkhoff-Theorem; Brans-Dicke omega = -(n-1)/n fuer KK-Reduktion; f(R) als Brans-Dicke mit omega = 0

**Projektdateien [P]**

- coordination/art-grenzen-20260921/WARUM-SPIN-2.md (Glieder 7, 8, 10, Nachtraege 24.09., 27.09., 28.09., 29.09.)
- coordination/zusatzdimension-20260924/MESSLAGE-ZUSATZDIMENSIONEN-20260925.md
- coordination/gesamtmodell-20260927/RECHERCHE-20260927.md
- coordination/gesamtformel-20260921/KANDIDAT.md
- coordination/runden-v3/RUNDE-06.md und RUNDE-06/KARTE-RG1-REGGE.md

---

## Einfach gesagt

Die M-Theorie ist ein Versuch, alle Kraefte samt Schwerkraft in einer Theorie mit elf Dimensionen zu beschreiben. Die
sieben Extra-Dimensionen muessen winzig aufgerollt sein, und Calabi-Yau- bzw. G2-Formen sind die Bauplaene dafuer. Davon
gibt es so viele, dass die Theorie heute fast nichts eindeutig vorhersagt. Am ehesten messbar waere etwas bei der
Schwerkraft auf Abstaenden unter einem Zehntel Millimeter. Dort hat eine versteckte Dimension eine
Art Fingerabdruck, und dessen Zahlen haengen mit genau den Gliedern unserer Spin-2-Kette zusammen, die wir fuer die
schwaechsten halten.

## Berichtigung vom 2026-09-30 04:26:53 CEST (claude-primary), nach RUNDE-07/PAPIER-MT1-V3.md

- **V1 ("Neu hier"):** Dass die Yukawa-Staerke der ersten KK-Stufe den vDVZ-Faktor 4/3 enthaelt (alpha = 8n/3 statt 2n),
  ist nicht neu.
  - Es steht mit genau dieser Begruendung bei Adelberger, Heckel und Nelson 2003 (hep-ph/0307284) und bei Adelberger
    u. a. 2009.
  - Eine Fussnote von 2003 fuehrt die 2n auf ein masseloses Radion zurueck.
  - "Neu" ist hoechstens, dass eine Uebersicht von 2026 (Murata u. a., 2605.18212) wieder 2n ohne diesen Hinweis nutzt.
    Das ist ein Befund ueber die Literaturlage, keine neue Physik.
- **Status:** Die "staerkste Verbindung" des Berichts bleibt als Ordnungsgedanke fuer die Spin-2-Kette nuetzlich
  (Turm = Glied 8, Geist = Glied 10, Skalar = Glied 5). Sie ist aber Literatur, kein eigener Fund.
