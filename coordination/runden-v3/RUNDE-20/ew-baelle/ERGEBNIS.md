# EW-BAELLE: Ergebnis (Runde 20, Literaturkarte)

- Literatur-Agent fuer die Leitung claude-primary. Start 2026-10-02 17:18:32 CEST, Text begonnen 17:37:23 CEST (date).
- Gegenstand: arXiv:2609.19293v2, Herdeiro, Kunz, Kleihaus, Radu, "Electroweak balls" (v1 16.09.2026, v2 29.09.2026).
  Dazu Ref. [19] (Proca-Higgs-Baelle, arXiv:2301.04172, Volltext in Teilen) und Ref. [59] (arXiv:2609.19273, nur
  Abstract). Das sind zwei der drei erlaubten zitierten Arbeiten.
- Marken: [S] in der Primaerquelle gelesen; [L?] nur Abstract oder Zitat; [H] eigene Schlussfolgerung.
  "Ablesung" heisst: Wert aus einer Abbildung abgelesen (hochaufgeloest gerendert), nicht gerechnet.
- Notation: In der Arbeit heisst der REELLE Skalar des Proca-Higgs-Modells psi. Hier steht psi_M2 fuer unser komplexes
  Feld und psi_PH fuer den reellen Skalar der Arbeit.
- Rohfundstellen, Erwartungsprotokoll und Gegensweep stehen in ARBEITSFELD.md (gleicher Ordner).

## 1 Ergebnis zuerst

1. **Die Arbeit zeigt keinen Beutel.** Das gilt fuer beide gezeigten Profile. Der Higgs-Betrag faellt im Kern der
   e-Kugel nur auf etwa 0,80 (Minimum etwa 0,77 bei endlichem Radius). Beim m-Beispiel liegt das Minimum bei etwa
   0,96 (bei endlichem Radius, im Zentrum etwa 0,996). Der Text
   sagt: phi(0) != 0 "for all solutions obtained so far" (S.18). Auch der ungeeichte Proca-Higgs-Ball in Ref. [19]
   faellt nur auf etwa 0,74. **E1 trifft an den gezeigten Daten nicht ein.** Damit greift der zweite Fall der
   Karten-Bedeutung: M2 ist im Beutelsinn kein Spielzeug dieser Klasse. Die Bruecke Q-Ball/Huelle hat hier keinen
   Literaturanker. Verwandt ist M2 nur ueber Friedberg-Lee-Sirlin (FLS): Ref. [19] nennt Proca-Higgs die
   "vector version of the scalar Friedberg-Lee-Sirlin model".
2. **Intervall und Aeste wie erwartet.** Es gilt w_min < w <= M_W (Gl. (46)). Das gilt in der Eichung A_0, a_0 -> 0
   im Unendlichen (Gl. (22)). Es gibt Massen- und Ladungsluecke, einen Umkehrpunkt bei w_min und zwei Aeste.
   In Abb. 4 erreichen beide Aeste w = M_W mit endlicher Masse. E2 und E4 treffen ein (Ruecklauf, keine Spirale).
   Das SM-Hindernis ist beta (das Verhaeltnis M_H/M_W), nicht der Mischungswinkel (S.19).
3. **Es gibt keinerlei Stoerungs-, Moden- oder Abstrahlungsanalyse.** Lineare Stabilitaet steht nur im Ausblick
   (S.21). E3 trifft ein. Ob die Atmung stille Stellen hat, ist nach Recherchestand nicht untersucht. Eine
   24-Monats-Suche war nicht moeglich, das Suchbudget der Sitzung war verbraucht.
4. **Frage 5: Die Schreibtischaussage gilt fuer die e-Kugelloesungen [H, gestuetzt auf S].** Das gilt in linearer
   Ordnung und in der Eichung von Gl. (22). Die e-Loesung ist unter gewoehnlichen Drehungen invariant (Gl. (20)-(21)). Bei l = 0 hat das masselose Photon nur das Coulomb-Nahfeld,
   also keinen Abstrahlkanal. Offen sind nur W (|w +- Om| > M_W), Higgs (Om > M_H) und Z (Om > M_Z).
   - Unterschied zu M2: ein Kanal mehr (Z), die Schwellen sind getrennt statt gleich (sqrt 2).
   - Ein Fenster mit genau einem offenen Kanal (M_W - w < Om < M_H) gibt es in allen gezeigten Familien [H].
   - Die Arbeit selbst sagt dazu nichts.
   - Bei l >= 1 ist der Photonkanal immer offen [H]. Die l = 1-Leitern von M2 lassen sich also nicht ohne eine
     Zusatzbedingung uebertragen.
5. **E5 trifft nicht ein.** Zwei Feldrollen und eine Massenluecke tragen, die Absenkung nur schwach.
   - Der Hauptunterschied ist nicht die Gauss-Bedingung, sondern die Massenerzeugung: W-Masse ~ phi, kein Gegenstueck
     zu 1*S und -S^2 + S^3/2. Dazu kommen der fehlende Beutel und das enge Existenzgebiet: leichtes Higgs, w nahe M_W.
   - Die Eichkopplung q aendert im gPH-Modell die Profile bei festem w nur quantitativ (S.6, Abb. 1). Die globale
     Aststruktur aendert sie wohl doch: Ref. [19] ungeeicht zeigt Spirale und M -> unendlich, die EW-Arbeit zwei Aeste
     mit endlicher Masse [H].

### 1a Erwartungsverstoesse (eigene Abruf-Erwartungen, das Wichtigste zuerst)

Die Erwartungen der Leitung (E1 bis E5) werden in Abschnitt 3 gewertet. Hier stehen die Verstoesse gegen meine eigenen,
vor jedem Abruf notierten Erwartungen (EA-1 bis EA-8 in ARBEITSFELD.md).

1. **VS-a/VS-g: Kein Beutel, weder bei EW noch bei Proca-Higgs (PH).** Ich erwartete beim PH-Ball mit sehr kleinem
   lambda = 0,005 ein phi(0) von 0,2 bis 0,5. Abgelesen: 0,74 (Ref. [19] Abb. 2 links, Einschub).
   - [H] Moegliche Ursache, aus den Gleichungen hergeleitet und nicht geprueft: Ref. [19] S.5 [S] sagt, phi = 0 ist
     eine konsistente Abschneidung mit "complex (massless) vector", also eine "Einstein-(double)Maxwell" Theorie.
   - Ein masseloser Vektor hat bei l = 0 keinen eigenen Freiheitsgrad. In einem quellfreien phi = 0-Kern waere die
     l = 0-Feldstaerke null. Ein l = 0-Vektorkondensat kann einen Beutel also nicht fuellen.
   - Das ist dieselbe Eigenschaft, die in Frage 5 das Photon bei l = 0 stumm macht (Feldregel 6: eine Kopplungsgroesse
     statt zweier Bauteile).
2. **VS-b: Die SM-Huerde ist beta, nicht Coulomb.** Ich hatte g' (Coulomb-Abstossung) vermutet.
   - S.19 [S]: theta_W laesst sich bei grossem w und kleinem beta annaehern; bei beta^2 = 0,3029 gibt es bisher keine
     Loesung.
   - Abb. 4 [Ablesung]: w_min rueckt mit wachsendem beta rasch an M_W, z. B. e-Familien 0,935 / 0,975 / 0,988 fuer
     beta = 0,0894 / 0,1096 / 0,1183.
3. **VS-f: Ungeeicht gegen EW unterscheiden sich qualitativ in der Aststruktur.**
   - Ref. [19] S.11-12 [S]: M -> unendlich fuer w -> mu, die M(w)-Kurve schneidet sich selbst ("for all computed
     lambda"), mindestens drei Aeste. Ein w_min liess sich "so far" nicht bestimmen.
   - EW (S.18 [S]): M und Q bleiben bei w -> M_W endlich, zwei Aeste.
   - Die Arbeit fuehrt den Umkehrpunkt auf "charged non-topological solitons" zurueck (S.18).
4. **VS-h [L?]: Mit Gravitation geht es bei physikalischen Massenverhaeltnissen.** Ref. [59] (Abstract) haelt die
   Newton-Konstante und die elektroschwachen Massenverhaeltnisse auf physikalischen Werten. Die flache Arbeit findet
   dort keine Loesungen. [H] Das beta-Hindernis waere dann eine Eigenschaft der flachen Familien, nicht des
   Feldinhalts.
5. **VS-d: Die Huelle gibt es, aber anders.** Bei der e-Kugel ist T_tt im Zentrum etwa 0,0012 und hat sein Maximum
   (etwa 0,0022) bei log10 r etwa 1,1. Dort liegt auch das Higgs-Minimum (Abb. 3, Ablesung).
   - Beim PH-Ball ist die Ladungsdichte j^t im Zentrum null, ihr Maximum liegt bei r etwa 4 (Ref. [19] Abb. 2 [S]).
   - [H] Das folgt aus der Vektorstruktur: Die Ladungsdichte enthaelt die Radialkomponente, und die verschwindet bei
     r = 0 (EW: Gl. (42), H(r) ~ r).
   - Das ist eine Ladungsschale, keine Beutelwand.
6. **Kleiner Verstoss EA-1:** Die Karte nennt den 29.09. als Einreichung. Das ist v2 ("references added"), v1 ist vom
   16.09.2026.

## 2 Antworten auf die Fragen

### Frage 1: Higgs-Betrag im Kern, Beutelenergie

- [S, S.18] Higgs knotenfrei, phi(0) != 0 "for all solutions obtained so far"; lokales Minimum bei endlichem Radius
  moeglich.
- [S, Ablesung Abb. 3] e-Beispiel (w/M_W = 0,98, g'/g = 0,14, beta = 0,0632): phi(0) etwa 0,80, Minimum etwa 0,77 bei
  log10 r etwa 1,1 (r in Einheiten 1/(g v), Gl. (23)).
- [S, Ablesung Abb. 2] m-Beispiel (w/M_W = 0,998, g'/g = 0,01, beta = 0,124): phi(0) etwa 0,996, Minimum etwa 0,962
  bei theta = pi/2, r etwa 40.
- [S, Ref. [19] Abb. 2] PH-Ball ungeeicht (w = 0,80, lambda = 0,005): phi(0) etwa 0,74, Minimum etwa 0,63 bei r etwa 4.
- Beutelenergie: [S, Fehlanzeige] Die Arbeit gibt keine an, das Wort "bag" kommt nicht vor (Volltextsuche).
  - [H aus Gl. (38) und (12)] Formales Gegenstueck ist die Potentialdichte (lambda v^4/4)(1 - phi^2)^2. Bei phi = 0
    waere sie lambda v^4/4 = M_H^2 v^2/8.
  - [H, Kopfrechnung] Bei phi etwa 0,8 wird nur etwa ein Achtel davon erreicht.
- [S, S.3 Fussnote 1] Baelle mit Higgs etwa null im Inneren nennt die Arbeit nur fuer eine andere Klasse: Ponton, Bai,
  Jain [40], Dunkelmaterie-Baelle mit Zusatzskalar. Fuer einen Beutel-Anker im elektroschwachen Umfeld waere [40] der
  Kandidat (nicht gelesen).

### Frage 2: Frequenzintervall, Massenluecke, zwei Aeste

- Oberes Ende [S]: w <= M_W, "bound-state condition" (S.11, Gl. (46)). Fuer das gPH-Modell gilt w <= mu (S.6).
  - Vorbehalt [S, Gl. (22)]: w ist eichabhaengig. Es ist festgelegt durch A_0, a_0 -> 0 im Unendlichen.
  - Laut S.18 verbindet der Grenzfall w -> M_W nicht mit dem Vakuum.
  - Abfall des W-Feldes: sqrt(M_W^2 - w^2) (S.12, Gl. (44)).
- Unteres Ende [S, S.19]: w_min > 0, festgelegt durch (theta_W, beta). Ablesung Abb. 4:

  | Sektor | tan theta_W | beta | w_min/M_W |
  |---|---|---|---|
  | e | 0,04 | 0,0894 | etwa 0,935 |
  | e | 0,04 | 0,1096 | etwa 0,975 |
  | e | 0,04 | 0,1183 | etwa 0,988 |
  | m | 0,01 | 0,1096 | etwa 0,944 |
  | m | 0,01 | 0,1342 | etwa 0,982 |
  | m | 0,01 | 0,1523 | etwa 0,998 |

- Massenluecke [S, S.18]: M und Q bleiben fuer w -> M_W endlich ("mass and charge gap"). Ihr Minimum liegt zwischen
  w_min und M_W.
  - Einen Zahlenwert nennt der Text nicht.
  - Ablesung Abb. 4: Der untere e-Ast endet bei w = M_W mit etwa 20 bis 45 M_0, wobei M_0 = v/g.
  - [H] In Einheiten von M_W skaliert die Masse wie 1/g^2, denn M_0 = 2 M_W/g^2.
- Zwei Aeste [S, S.18-19]: Bei w_min kehrt die Familie auf einen zweiten Ast um. Bei gleicher Frequenz gibt es dann
  zwei Baelle mit verschiedener Masse, Ladung und Profil. Das gilt in beiden Sektoren und fuer alle betrachteten
  (theta_W, beta).
  - Ablesung Abb. 4: Der obere Ast laeuft mit wachsender Masse zurueck bis w = M_W (e: etwa 340 bzw. 700 M_0).
- Standardmodell [S, S.19]: Bei gleichzeitig gemessenem g'/g und lambda/g^2 gibt es keine Loesung.
  - Die Autoren betonen: "should not be interpreted as a general non-existence result".
  - Moegliche Gruende laut S.19 und S.21: echtes Ende der Familien, Grenze der Fortsetzung oder eingeschraenkter
    Ansatz.
  - [H, aus Gl. (23)] Die gezeigten beta <= 0,152 heissen M_H/M_W <= 0,43; im SM ist es 1,56.

### Frage 3: Stabilitaets- oder Stoerungsanalyse

- [S] Keine. Es gibt keine linearen Moden, keine Atmung, keine Abstrahlung und keine stillen Stellen.
  - Die Virialidentitaeten (Gl. (33)-(34) fuer m, Gl. (45) fuer e) dienen nur als Genauigkeitstest. Sie helfen laut
    S.16 nicht, die Existenz zu verstehen.
  - Volltextsuche: "breath", "quasinormal", "oscillat" und "photon" kommen nicht vor. "radiat" steht nur in
    "superradiant" (S.2 und S.22, Proca-Haar an Schwarzen Loechern) und in einem Literaturtitel. "stabil" steht nur im
    Ausblick und in Literaturtiteln.
- [S, S.21] Ausblick: Lineare Stabilitaet und nichtlineare Dynamik seien "equally important". Als Suchrichtungen
  nennt die Arbeit radial und winkelmaessig angeregte Loesungen. Statische l = 1-e-Loesungen und rotierende Loesungen
  seien gefunden, aber noch nicht veroeffentlicht.
- [S, Ref. [19]] Dort gibt es nur ein energetisches Spaltungskriterium (Abb. 1 unten rechts: Q/(M/v) < 1 heisst
  instabil gegen Spaltung). Fuer PH-Sterne steht dort: "rigorous stability analysis is beyond the scope" (Abschn. 4).
- [L?, Ref. [59]] Das Abstract erwaehnt weder Stabilitaet noch Moden noch Abstrahlung.

### Frage 4: Abbildung auf M2

Die vollstaendige Tabelle steht in Abschnitt 4. Kurz:

- Tragend: psi_M2 entspricht W (geladen, harmonisch in der Zeit), chi entspricht phi (Vakuum 1), S entspricht dem
  W-Quadrat, die Schwelle sqrt 2 des psi-Kanals entspricht M_W. Die Massenluecke traegt ebenfalls.
- Brechend:
  - Die Massenerzeugung (W-Masse ~ phi, Gl. (16); kein expliziter Anteil wie 1*S, kein -S^2 + S^3/2).
  - Der fehlende Beutel.
  - Das Massenverhaeltnis: In M2 ist m_chi/m_psi = 1, das entspricht beta = 1/sqrt 8, etwa 0,354. Gezeigt sind nur
    beta <= 0,152.
  - Die Vektorstruktur (V und H, Gl. (39)/(41)).
  - Zusaetzliche Felder: Z, Photon mit Coulomb-Schwanz, Gauss.
  - Duennwand: In M2 ist w0/m_psi etwa 0,60; die EW-Familien liegen alle bei w/M_W >= 0,935 [H].

### Frage 5: masseloses Photon bei l = 0

- Was in der Arbeit steht [S]:
  - e-Ansatz (Gl. (20)-(21)): geladenes W nur mit dt- und dr-Komponente (V(r), H(r)); neutrale Felder nur mit
    Zeitkomponente (A_0(r) tau3, a_0(r)); phi(r). Alles haengt nur von r ab, die tau-Richtungen sind fest.
  - Klassifikation (S.5-6, nach [41]): Die e-Familie enthaelt die Kugel-Proca-Sterne als l = 0-Glied. Der allgemeine
    e-Ansatz hat drei Vektorpotentiale, das l = 0-Glied nur zwei. Die m-Familie hat kein Kugelgegenstueck und
    beginnt bei l = 1.
  - Asymptotik (Gl. (44), S.14 und S.16): Higgs und Z fallen nach Yukawa mit M_H bzw. M_Z ab, W mit
    sqrt(M_W^2 - w^2). Einziger langreichweitiger Anteil ist der Coulomb-Schwanz Q/r ("the only long-range
    contribution"); die Ladung ist Q/e (Gl. (32)).
  - Randbedingungen (S.16): r = 0: H = V' = A_0' = a_0' = phi' = 0; r -> inf: H = V = A_0 = a_0 = 0, phi = 1.
  - Ueber Abstrahlung oder Kanaele sagt die Arbeit nichts.
- Eigene Schlussfolgerung [H]:
  1. Die e-Loesung ist unter gewoehnlichen Drehungen invariant; anders als beim Sphaleron gibt es keine
     Isospin-Verdrehung. Damit ist l fuer Stoerungen ein guter Index, und l = 0 meint das Uebliche.
  2. Bei l = 0 hat ein Vektorfeld nur Zeit- und Radialkomponente, also keine transversale Mode. Fuer das masselose
     Photon bleibt nur ein radiales E-Feld. Ausserhalb der Quellen ist es durch die eingeschlossene Ladung festgelegt
     (Gauss). In linearer Ordnung ist die Stromstoerung an das exponentiell abfallende Hintergrund-W gebunden. Die
     Ladung im Fernfeld ist dann fest, und es gibt keine Abstrahlung.
  3. Das Photon ist auch im Inneren masselos. Laut Gl. (16) enthalten die Massenterme nur W und g'a - gV^3
     (Z-Richtung); die Photonkombination aus Gl. (13) kommt nicht vor. Das gilt, solange phi != 0, und phi ist
     knotenfrei (S.18). Das Photon bleibt aber kein Zuschauer: Es traegt die Coulomb-Abstossung im Nahfeld,
     verschiebt also Frequenzen, nur ohne Verlustkanal.
  4. Offene l = 0-Kanaele: Higgs (Om > M_H), Z (longitudinal, Om > M_Z) und W (longitudinal, Seitenbaender:
     w + Om > M_W ab Om > M_W - w, und |w - Om| > M_W ab Om > M_W + w). Die Schwellen gelten in der Eichung von
     Gl. (22). Der Coulomb-Schwanz verzerrt die auslaufenden W-Wellen, verschiebt aber die Schwelle nicht.
  5. Vergleich mit M2:
     - M2 hat drei Schwellen: sqrt 2 - w (psi oben), sqrt 2 (chi), sqrt 2 + w (psi unten).
     - EW hat vier: M_W - w, M_H, M_Z, M_W + w.
     - Ein-Kanal-Fenster: in M2 sqrt 2 - w < Om < sqrt 2; in EW M_W - w < Om < min(M_H, M_Z). In allen gezeigten
       Familien ist M_H < M_Z, denn M_Z/M_W = sqrt(1 + tan^2 theta_W) ist ungefaehr 1.
     - Im e-Beispiel liegt das Fenster etwa bei 0,02 < Om/M_W < 0,18; es ist also schmal und liegt tief.
     - Die Kanalstruktur ist also gleichartig, nicht gleich: ein Kanal mehr (Z), getrennte Schwellen.
     - Stille Atmungsstellen sind damit moeglich, aber nicht gezeigt. Ob Atmungsmoden in das Fenster fallen, weiss
       niemand, denn es gibt keine Modenanalyse.
  6. Bei l >= 1 ist das Photon immer offen (transversal, ab Om > 0). Eine stille Stelle braeuchte dort zusaetzlich
     eine verschwindende Photonkopplung, also zwei Bedingungen statt einer.

## 3 Erwartungen der Leitung E1 bis E5

| Nr | Erwartung (unveraendert) | Ausgang | Beleg |
|---|---|---|---|
| E1 | Higgs-Betrag im Kern mindestens 30 % abgesenkt (70 %) | **nicht eingetroffen** (an allen gezeigten Profilen; Rest der Familien offen) | Abb. 3: phi(0) etwa 0,80 (20 %); Abb. 2: etwa 0,996, Minimum 0,962; S.18 phi(0) != 0. Oberer Ast ohne Profil. |
| E2 | Oberes Ende = Masse des geladenen Vektors (75 %) | **eingetroffen** (mit Eichvorbehalt) | Gl. (46), S.11 w <= M_W; gPH S.6 w <= mu; Gl. (22) legt w ueber A_0, a_0 -> 0 fest. |
| E3 | Keine Analyse linearer Moden oder Abstrahlung (85 %) | **eingetroffen** | Volltext; S.16 (Virial nur Test); S.21 Stabilitaet als Ausblick. |
| E4 | M(w) mit Ruecklauf oder Spirale (60 %) | **eingetroffen** (Ruecklauf, keine Spirale) | S.18 Umkehr bei w_min, zweiter Ast; Abb. 4. Spirale nur beim ungeeichten PH-Ball (Ref. [19] S.11-12). |
| E5 | Abbildung traegt fuer l = 0, Hauptunterschied Gauss (55 %) | **nicht eingetroffen** (erster Teil weitgehend, zweiter nicht) | Feldrollen und Luecke tragen. Eichkopplung im gPH-Modell fuer Profile nur quantitativ (S.6, Abb. 1); groesser sind Massenerzeugung (Gl. (16), Ref. [19] Gl. (10)), fehlender Beutel und Existenzgebiet (S.19). |

Bedeutung gemaess Karte: Der erste Fall (E1, E3 und E5 treffen ein) tritt nicht ein. Der zweite Fall (E1 trifft nicht ein)
greift: M2 ist kein Beutel-Spielzeug dieser Klasse, und die Bruecke Q-Ball/Huelle bleibt hier ohne Literaturanker.

[H] Davon getrennt: Nach Frage 5 waere "Hat die l = 0-Atmung der e-Baelle stille Stellen im Fenster
M_W - w < Om < M_H?" eine eigenstaendige, rechenbare Frage an ein Literaturmodell. Sie waere aber keine
Uebertragung von M2.

## 4 Abbildungstabelle M2 <-> elektroschwacher Ball (e-Sektor, l = 0)

| M2-Groesse | Gegenstueck in 2609.19293 | traegt / bricht | Grund |
|---|---|---|---|
| psi_M2 komplex, traegt Q | W = V^1 + i V^2 (Gl. (15)); e-Ansatz V(r), H(r), Phase w t (Gl. (20)) | traegt in der Rolle, bricht in der Form | Vektor: zwei Radialfunktionen, algebraische Gl. (39) und Zwang (41) [S]; V mit einem Knoten (S.18) [S]; Ladungsdichte im Zentrum null [H, wie Ref. [19] Abb. 2] |
| chi reell, Vakuum 1, im Ball -> 0 | phi(r), Vakuum phi = 1 (Gl. (21)) | Rolle traegt; "-> 0" bricht | phi(0) etwa 0,80 (Abb. 3), nie 0 (S.18) |
| S = abs(psi)^2 | W-Quadrat; im e-Sektor (V^2 - H^2) in Gl. (38) | traegt teilweise | Kopplung phi^2 mal W-Quadrat wie chi^2 S [S, Gl. (16)]; Lorentz-Norm nicht positiv definit [H]; zusaetzlich Z-Term (a_0 - A_0)^2 phi^2 [S, Gl. (38)] |
| (1 + chi^2) S: psi-Masse^2 von 1 (Kern) bis 2 (Vakuum) | (g^2/8) phi^2 W Wbar: W-Masse = M_W phi (Gl. (16)) | bricht | kein expliziter Massenanteil; W waere bei phi = 0 masselos. FLS-Typ, Ref. [19] Gl. (10) [S] |
| -S^2 + S^3/2 (Selbstanziehung, Duennwand) | kein direktes Gegenstueck; effektiv -(A Abar)^2/M_rho^2 nach Ausintegrieren des Higgs (Ref. [19] Gl. (17)) und nichtabelsche W-Terme (EW-Arbeit Gl. (17)) | bricht | Kein eigenes Duennwandregime gefunden (Ref. [19] S.11-12: kein w_min mit divergenter Masse) |
| Beutelkonstante 1/4 | lambda v^4/4 = M_H^2 v^2/8 (Gl. (38) bei phi = 0) [H] | formal traegt, physikalisch bricht | nicht erreicht; bei phi etwa 0,8 nur etwa 1/8 [H] |
| Kanalmasse sqrt 2 (psi im Vakuum) | M_W (Gl. (12)) | traegt | gleiche Rolle als Bindungsschwelle (Gl. (46)) |
| Kanalmasse sqrt 2 (chi) | M_H = v sqrt(2 lambda) | Rolle traegt, Verhaeltnis bricht | M2: m_chi/m_psi = 1, das waere beta etwa 0,354; gezeigt beta <= 0,152, also M_H/M_W <= 0,43 [H]; SM 1,56 |
| Kanalmasse 1 (psi im Kern, Lesart R2) | M_W phi_innen, im e-Beispiel etwa 0,8 M_W [H] | traegt qualitativ | Masse innen kleiner als aussen in beiden Modellen |
| (fehlt) | Z, Masse M_Z (Gl. (12), (44)) | bricht | zusaetzlicher massiver l = 0-Kanal [H] |
| (fehlt) | Photon, Coulomb-Schwanz Q/r, Gauss (Gl. (32), (44)) | bricht | kein M2-Gegenstueck; bei l = 0 kein Verlustkanal, bei l >= 1 immer offen [H] |
| Ladung Q (global) | Q/e (Gl. (32)), zugleich Quelle des Coulombfelds | bricht teilweise | Q-Ball-Ladung und Eichladung fallen zusammen |
| w0^2 etwa 0,728 (Duennwand, w0/m etwa 0,60) | w_min (Umkehrpunkt), w_min/M_W >= 0,935 (Abb. 4) | bricht | Umkehrpunkt bei endlicher Masse statt Divergenz; schwellennahes Regime [H] |
| Massenluecke | Massen- und Ladungsluecke (S.18) | traegt | |
| Huelle (Beutelwand, Huellenradius) | Higgs-Minimum und T_tt-Maximum bei endlichem Radius (Abb. 3) | anderer Mechanismus [H] | Ladungsschale aus der Radialkomponente, keine Beutelwand |
| stille Stellen l = 0 / l = 1 | nicht untersucht | offen | S.21 nur Ausblick |

## 4a Regime, Moderatoren, Unterscheidungspunkte

- Regime "Beutel" gegen "kein Beutel" (Feldregel 1):
  - M2 hat chi -> 0 und eine Duennwand mit w0/m etwa 0,60. In den gezeigten EW- und PH-Profilen liegt das
    phi-Minimum zwischen etwa 0,63 (PH) und 0,96 (EW, m); die EW-Loesungen liegen nahe der Schwelle.
  - [H] Drei Wege fuehren zu "kein Beutel":
    1. fehlende Eigen-Anziehung (kein -S^2);
    2. die l = 0-Vektorstruktur (bei phi = 0 masselos, also im Kern reine Eichung, vgl. Ref. [19] S.5 [S]);
    3. die Coulomb-Abstossung (geeichte Q-Baelle, S.18-19 zitiert [48-51]). Dass sie die Ladung deckelt, ist mein
       Vorwissen und steht nicht in der Arbeit.
  - Nach Feldregel 6 ist die gemeinsame Groesse dann: Gibt es eine Duennwandfrequenz w0 deutlich unter der
    Vakuummasse?
  - Unterscheidungspunkt: m-Familien und l = 1-e-Familien bei kleinem w, also dort, wo transversale W-Komponenten
    existieren.
    - Die Vektorstruktur-Hypothese sagt voraus, dass phi(0) dort gegen 0 gehen kann.
    - Bei den l = 0-e-Familien sagt sie voraus, dass das nie geschieht.
    - In der Arbeit ist das nicht gezeigt; das m-Beispiel liegt bei w/M_W = 0,998.
- Regime "Spirale" (PH ungeeicht) gegen "zwei Aeste" (EW): Die Arbeit ordnet ihren Umkehrpunkt den geladenen
  Solitonen zu ("charged non-topological solitons", S.18). Den Vergleich mit der PH-Spirale zieht sie selbst nicht.
  - [H] Vermuteter Moderator ist die Ladung (Gauss). An dieser Stelle wirkt die Gauss-Bedingung wirklich.
  - Unterscheidungspunkt: gPH bei wachsendem q ueber die ganze Familie. Abb. 1 zeigt nur ein festes w = 0,495.
- SM-Hindernis: Die Arbeit nennt drei Lesarten (S.19, S.21): echtes Ende, Numerik, Ansatz.
  - Unterscheidungspunkt fuer "echtes Ende": w_min laeuft mit wachsendem beta gegen M_W, das Intervall schrumpft.
    Abb. 4 zeigt das fuer beide Sektoren und stuetzt damit [H] das echte Ende dieser Familien.
  - Unterscheidungspunkt fuer "Ansatz": l = 1-e- oder rotierende Familien bei beta^2 = 0,3029. Nicht berichtet.
  - Gravitierende Loesungen bei physikalischen Verhaeltnissen gibt es laut [59] [L?].
- Frage 5, Behauptung gegen Alternative "Photon verliert ueber Z-Mischung im Kern":
  - [H] Beide laufen nur bei Om < M_W - w auseinander, wo alle massiven Kanaele zu sind. Die Behauptung sagt dort
    eine ungedaempfte Mode voraus, die Alternative eine Daempfung.
  - Der Bereich Om < M_W - w ist in den gezeigten Familien hoechstens 0,065 M_W breit (w_min/M_W >= 0,935), praktisch
    also schwer zugaenglich.

## 4b Gegensweep (Was war selbstverstaendlich und ungeprueft?)

- G1: "e" heisst nicht "elektrisch geladen". e/m ist die Proca-Multipolklasse; auch m-Loesungen tragen Ladung
  (S.14). Geprueft.
- G2: w ist nicht eichinvariant (Gl. (22)). "Oberes Ende = M_W" und die Kanalschwellen gelten in der Eichung
  A_0, a_0 -> 0. Geprueft.
- G3: l ist ein guter Index fuer Stoerungen (keine Isospin-Verdrehung, Gl. (20)-(21)). Geprueft.
- G4: Das Photon ist auch im Kern masselos (Gl. (16)). Geprueft.
- G5: Die SM-Huerde ist beta, nicht theta_W (S.19). Geprueft und ein eigener Verstoss.
- G6: v2 = v1 bis auf Referenzen ist nicht geprueft, nur die Kommentarzeile.
- G7: "Transversale Moden ab l = 1" stuetzt die Arbeit nur indirekt (S.6). Als Lehrbuchaussage ist es in dieser Karte
  ohne eigene Quelle [H].
- G8: Die 24-Monats-Suche (Feldregel 7) lief nicht; das Websuch-Budget der Sitzung war verbraucht (200 von 200).
  Deshalb heisst jede Literatur-Fehlanzeige hier "nach Recherchestand nicht belegt".

## 4c Offene Fragen und Rueckfragen

- R1: Was meint "unser E1/E2" in Frage 5 der Karte? Ich vergleiche mit der M2-Kanalstruktur aus dem Auftrag.
- R2: "Kanalmassen 1 und sqrt 2": Ich lese das als psi_M2-Masse im Kern (chi = 0) gleich 1, Vakuummassen gleich
  sqrt 2. Bitte bestaetigen.
- O1: phi(0) und die Profile auf dem oberen Ast (schwere Loesungen bei w -> M_W) sind nicht gezeigt. E1 ist dort
  offen.
- O2: Wo liegt beta_max je theta_W? Eine analytische Grenze fehlt laut S.19; die Extrapolation aus Abb. 4 ist [H].
- O3: Haben die l = 0-e-Baelle im Fenster M_W - w < Om < M_H gebundene Zustaende im Kontinuum? Es gibt keine Analyse.
- O4: Das FLS-Original (in Ref. [19] als [100] zitiert, Friedberg, Lee, Sirlin) ist hier nicht gelesen. Gleiches gilt
  fuer Ponton, Bai, Jain [40]. Beide waeren Kandidaten fuer einen Beutel-Anker.

## 4d Kalibrierung

- (a) Gemessen, also in den Quellen gerechnet und gezeigt:
  - zwei Profile (e, m), sechs M(w)-Familien, Asymptotik und Randbedingungen;
  - die beta/theta_W-Aussage (S.19);
  - ein PH-Profil (Ref. [19]).
- (b) Nuetzlich verdichtet: die Abbildungstabelle, die Kanalstruktur aus Frage 5 und "kein Beutel". Die letzte Aussage
  stuetzt sich auf zwei Profile plus einen Satz. Der Satz (phi(0) != 0) schliesst nur phi(0) = 0 aus, keine starke
  Absenkung.
- (c) Gewachsene Gewissheit ohne neue Evidenz:
  - die Begruendung "l = 0-Vektor kann keinen Beutel fuellen";
  - "Photon bei l = 0 stumm" (Lehrbuch, hier nicht belegt);
  - "die Familien enden knapp ueber dem groessten beta".
- Warnzeichen: Meine Sicherheit bei Frage 5 stieg beim Lesen der Klassifikation (S.6). Gleichzeitig zerfiel die Frage
  in Kanaele, Seitenbaender und Eichwahl. Die Ja-Antwort gilt in linearer Ordnung und in der Eichung von Gl. (22),
  nicht allgemein.

## 5 Grenzen und gelesene Quellen

- Grenzen:
  - Literaturkarte ohne Rechnung; Zahlen nur aus Abbildungen abgelesen.
  - Ref. [19] nur in den Abschnitten 2.1, 2.2, 2.4, 3.2 und Abb. 1-2 gelesen; Ref. [59] nur im Abstract.
  - Keine Websuche (Budget erschoepft), also keine Pruefung auf Folgearbeiten.
  - Keine Projektdateien ausser der Karte.
- Lokale Kopien der Quellen (nur zum Lesen) liegen in `quelle/`: PDF, pdftotext-Text und gerenderte Abbildungsseiten.
- Quellen:
  1. Herdeiro, C., Kunz, J., Kleihaus, B., Radu, E. (2026): Electroweak balls: non-topological solitons in the
     Weinberg-Salam theory. arXiv:2609.19293, **Fassung v2** (29.09.2026; v1 16.09.2026).
     - Abstract-Seite https://arxiv.org/abs/2609.19293, abgerufen zwischen 17:18:32 und 17:20:08 CEST.
     - PDF https://arxiv.org/pdf/2609.19293v2, geladen 2026-10-02 17:20:10 CEST.
     - Gelesen: S.1-22 vollstaendig, Literaturliste in Auszuegen.
  2. Herdeiro, C., Radu, E., dos Santos Costa Filho, E. (2023): Proca-Higgs balls and stars in a UV completion for Proca
     self-interactions. JCAP 05 (2023) 022, arXiv:2301.04172 **v1**. Ref. [19] der Arbeit.
     - PDF https://arxiv.org/pdf/2301.04172, geladen 2026-10-02 17:26:16 CEST.
  3. dos Santos Costa Filho, E., Gervalle, R. (2026): Bosonic stars with dark electroweak fields. arXiv:2609.19273
     **v1** (16.09.2026). Ref. [59] der Arbeit, nur Abstract [L?].
     - https://arxiv.org/abs/2609.19273, abgerufen zwischen 17:31:08 und 17:33:45 CEST.

## 6 Einfach gesagt

Die Forscher haben im Computer "Kugeln" aus W-Teilchen gebaut, die von selbst zusammenhalten, aehnlich wie unsere
Q-Baelle. Wir hatten gehofft, dass das Higgs-Feld innen fast verschwindet, wie bei unserem Modell (dem "Beutel").
Das tut es aber nicht: Es sinkt nur um etwa ein Fuenftel. Auch Schwingungen der Kugeln hat niemand untersucht. Unsere
Frage nach "stillen Stellen" ist dort also ganz offen. Nach unserer Ueberlegung kann Licht eine gleichmaessig atmende
Kugel nicht abstrahlen; dafuer gibt es dort einen Abstrahlweg mehr als bei uns.
