# ARBEITSFELD ATEM-VOLLZAEHLUNG-L (feldforscher fuer claude-primary)

- Start 2026-10-05 09:00:40 CEST (date). Zeitbox 60 min, also bis etwa 10:00:40. Hoechstens 15 Netzabrufe.
- Dieses Feld lese ich vor jedem Schritt neu. Gestrichenes bleibt mit ~~...~~ stehen. Offene Rueckfragen stehen unten
  und wandern mit.
- Kennzeichen: [E] Messung/Rechnung, [M] Mathematik, [S] Fachquelle, [L] Lehrbuch, [H] Hypothese, [P] Projektbefund,
  [ES] eigener Schluss, [L?] Gedaechtnis, ungeprueft.

## 0. Vorgelesen (lokal, kein Netzabruf), 09:00:40 bis 09:04:39

- KARTE.md ganz. AV1 bis AV4 unveraendert uebernommen (siehe Abschnitt 5).
- ISO-ATEM-1 ERGEBNIS Abschnitte 1 bis 4 [P]:
  - P2_13-Schar: lambda = (1 + cos phi_A + cos phi_B)/3 mit cos(phi_A + 60 Grad) + cos(phi_B - 60 Grad) = 1 (Z. 24 bis 25).
  - 222-Form (Z. 119 bis 124): Drehteile E, eine 2_1-Schraube um eine Wuerfelachse, zwei Zweier um die dazu
    senkrechten Flaechendiagonalen mit Verschiebung 1/4 der Diagonale; alle 8 Tetraeder gleich gedreht (17,2539 Grad
    bei lambda = 0,97); halbe kubische Zelle; drei Ausrichtungen; dort schon [H]: "passt zu alpha-Cristobalit
    (P4_12_12) bzw. P2_12_12_1-Familien bei Coh/Vanderbilt, Zuordnung nicht geprueft".
  - Gamma-Ansatz (alle A gleich, alle B gleich) erreicht F = lambda I nie; Teil A (Drehung um eine Achse) gibt
    V/V0 = cos^2 phi, also flaches, anisotropes Atmen.
- EIS-1 Z. 104 bis 105 und 245: RUM-Ebenen (xi, xi, zeta) in beta-Cristobalit (Hammonds u. a. 1996) nur [L?].
- SCHALTER-UND-ATMEN Z. 179: "Die Cristobalit-Waermeaussage ist [L?]." R43 Z. 26: Negativliste "Cristobalit schrumpft
  beim Erwaermen".
- CONNOR-HALL-L N8: Hills Weg = Symmetriebahnen, Polynomsysteme je Untergruppe, Resultanten bzw. Homotopie.
- **Lokale Vorabrufe anderer Agenten (zaehlen nicht als meine Abrufe, Abstract-Ebene):**
  - ISO-ATEM-1 quellen/A2-api-cristobalit-alle.xml Z. 620 bis 637: Coh/Vanderbilt 2008 (arXiv:0806.3737, PRB 78,
    054117) [S Abstract]: P4_12_12- und I-42d-Enantiomorphe bilden drei Cluster, je eine **dreidimensionale
    Mannigfaltigkeit von Strukturen mit P2_12_12_1-Symmetrie**, in der P4_12_12 und I-42d Sonderfaelle hoeherer
    Symmetrie sind; Zhang/Scott: beta sei I-42d.
  - Dieselbe Datei Z. 59 bis 63: Borcea/Streinu 2011 (arXiv:1110.4661), Deformationsraum fuer Quarz-, Cristobalit- und
    Tridymit-Modelle [S Abstract].
  - DREIECK-PUMPE-L ARBEITSFELD Z. 296 bis 312 [P]: BeF2 in alpha-Cristobalit-Struktur (Rechnung, arXiv:2209.10087)
    "giant" positive Ausdehnung ~175e-6/K; Rickwardt/Nielaba/Mueser/Binder (cond-mat/0010315) rechnen beta-Cristobalit,
    Vorzeichen nicht im Abstract. Dort schon Zwei-Regime-Lesart [ES, L]: alpha dehnt sich aus, beta neigt zu NTE.
- Projekt-grep 09:03:20 (Ausschluesse gesetzt) nach ZrW2O8, flexibility window, Wright/Leadbetter, Hatch/Ghose,
  O'Keeffe/Hyde, Swainson, Coh/Vanderbilt, I-42d, P4_12_12, P2_12_12_1: nur Treffer in iso-atem-1, dreieck-pumpe-l,
  schreibtisch-leser (GEGENLESEN Z. 340 bis 342: "nahe null bzw. leicht negativ" nur erinnert). Keine Vollzaehlung,
  keine gemessene Zahl im Projekt.

## 1. Regime (Pflicht)

- **R-inf (linear):** infinitesimale RUM-Zaehlung. Starre Einheitsmoden als Phononen mit omega ~ 0; im
  beta-Cristobalit auf ganzen Ebenen der Brillouin-Zone (EIS-1 [L?]). Aussage: Zahl der Moden je Wellenvektor.
- **R-end (nichtlinear):** endliche Kipp-Varianten mit exakt starren Tetraedern (P2_13, I-42d, P4_12_12,
  P2_12_12_1, ...). Aussage: welche Strukturen und Scharen existieren bei endlichem Winkel.
- **R-Modell gegen R-Material:** ideales Geruest (starre regulaere Tetraeder, Si-O-Si frei) gegen echtes SiO2
  (Tetraeder leicht verformbar, Si-O-Bindung dehnt sich thermisch, Si-O-Si-Winkel hat ein Energieminimum).
- **Im Material zusaetzlich [H]:** alpha-Phase (statische Kippung, unter Tc) gegen beta-Phase (dynamische Kippung,
  ueber Tc). Moderator: Temperatur relativ zu Tc.

## 2. Schreibtisch vor dem ersten Abruf (Bausteine verketten)

- [M] Eine Kipp-Variante mit kubischer Raumgruppe hat ein kubisches Gitter, also F = lambda I automatisch (P2_13).
  Nichtkubische Varianten atmen nur isotrop, wenn Zusatzbedingungen gelten (tetragonal: c = sqrt 2 a; orthorhombisch:
  a = b und c = sqrt 2 a in der halben Zelle).
- [M, ES] Gitterzuordnung zur Elternzelle Fd-3m (kubische Kante a_c):
  - I-42d: innenzentriert tetragonal, a_t = a_c/sqrt 2, c = a_c, gleiche Translationen wie Fd-3m, also k = 0
    (Gamma). Das ist der Gamma-Ansatz bzw. Teil A von ISO-ATEM-1 (Drehung um eine Wuerfelachse, nur a und b schrumpfen).
  - P4_12_12 (alpha): primitiv tetragonal, gleiche Kanten, Volumen a_c^3/2, also ein Arm des X-Punkts.
  - P2_13: primitiv kubisch, Volumen a_c^3, also alle drei X-Arme.
  - Die 222-Form von ISO-ATEM-1: halbe Zelle, drei 2_1-Schrauben (Wuerfelachse; 1/4 Flaechendiagonale = a_t/2 laengs
    a_t und b_t). **[H] Das ist P2_12_12_1 in der halben Zelle**, gemeinsame Untergruppe von P4_12_12 und I-42d.
  - [ES] Zaehlprobe: Ist die Coh/Vanderbilt-Mannigfaltigkeit (dreidimensional) die der starren Tetraeder samt
    Gitter, dann geben die zwei Isotropiebedingungen (a = b, c = sqrt 2 a) und festes lambda zusammen 3 Bedingungen,
    also isolierte Punkte bei festem lambda. Genau das fand ISO-ATEM-1 (Nullitaet 0 bei festem lambda, 1 mit freiem
    lambda). Drei Cluster dort = drei Ausrichtungen hier. Pruefen am Volltext.
- [L?] Geschichte: Barth 1932 P2_13; Nieuwenkamp 1937 Fd-3m mit ungeordnetem O; Wright/Leadbetter 1975 eher Domaenen
  aus I-42d, nicht P2_13. Falls das stimmt, ist AV1 in der Zuschreibung falsch. Pruefen.

## 3. Abrufplan (15 hoechstens)

1. Coh/Vanderbilt Volltext (arXiv 0806.3737v2): Geschichte, Mannigfaltigkeit, starr oder nicht, isotrop?
2. Suche: gemessene Waermeausdehnung beta-Cristobalit (Primaerquelle finden).
3. Primaerquelle Ausdehnung lesen.
4. ZrW2O8: Mary u. a. 1996 (Zahl).
5. RUM-Deutung der NTE (Pryde u. a. 1996 oder Tucker u. a. 2005).
6. Gegensweep: Kritik am RUM-Bild (Cao/Bridges u. a.).
7. Gegensweep 24 Monate (arXiv-API mit submittedDate oder Websuche).
8. Hatch/Ghose 1991 Abstract (Isotropie-Untergruppen).
9. O'Keeffe/Hyde 1976 Abstract (Cristobalit-Ableitungen mit regulaeren Tetraedern).
10. Suche nach vollstaendiger Abzaehlung (Glazer-Analogon fuer Tetraedergerueste).
11. Dove 2019 Uebersicht (RUM-Modell, offen zugaenglich).
12 bis 15. Reserve fuer Erwartungsverstoesse.

## 4. Abrufprotokoll mit Erwartungen (vor jedem Abruf)

(folgt)

## 5. Vorhersagen der Karte (unveraendert)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| AV1 | [L?] Die P2_13-Schar aus ISO-ATEM-1 entspricht dem Cristobalit-Modell von Wright/Leadbetter (P2_13) | 70 % |
| AV2 | [L?] Die 222-Form ist in der Literatur als Kipp-Variante des Cristobalits bekannt (gleich welcher Name) | 45 % |
| AV3 | [H] Eine vollstaendige Abzaehlung der endlichen Kipp-Varianten mit starren Tetraedern gibt es in der Literatur nicht; bekannt sind nur einzelne Varianten und die infinitesimale RUM-Zaehlung | 55 % |
| AV4 | [L?] Beta-Cristobalit hat einen kleinen bzw. negativen Waermeausdehnungskoeffizienten, und die negative Waermeausdehnung verwandter Gerueste wird durch RUM erklaert | 60 % |

## 6. Erwartungsverstoesse (laufend)

(noch keine)

## 7. Offene Rueckfragen (wandern mit)

- Q1: Ist die 222-Form P2_12_12_1 (Schreibtisch [H])? Am Volltext Coh/Vanderbilt pruefen.
- Q2: Wer hat P2_13 vorgeschlagen (Barth 1932 oder Wright/Leadbetter 1975)?
- Q3: Gemessener Koeffizient beta-Cristobalit mit Temperaturbereich und Stelle.

### A1 (Erwartung vor Abruf)
- Erwartung geschrieben 09:05:34 (date): Coh/Vanderbilt Volltext arXiv 0806.3737v2. Ich erwarte: (a) Einleitung nennt Barth 1932 fuer P2_13 und Wright/Leadbetter 1975 fuer I-42d-Domaenen (nicht P2_13); (b) die P2_12_12_1-Mannigfaltigkeit wird ueber Drehungen (fast) starrer Tetraeder parametrisiert, drei Parameter; (c) kein Wort zu isotropem Atmen F = lambda I; (d) P2_13 nur in der Geschichte, nicht gerechnet.
- **A1 ausgefuehrt 09:05:38 (date, quellen/A1-zeit.txt), curl arXiv-PDF, Text quellen/A1-coh-vanderbilt-0806.3737v2.txt
  (pdftotext). Gelesen bis zur Zeit unten.**
  - (a) Wright/Leadbetter 1975 = **I-42d** (tetragonal, alle Tetraeder um z gedreht), nicht P2_13 [S, Txt Z. 53 bis 55
    und 115 bis 124]. Barth wird nicht zitiert, **P2_13 kommt im ganzen Aufsatz nicht vor** (grep ohne Treffer).
    -> Erwartung (a) halb, (d) verletzt.
  - (b) Starke Bestaetigung, staerker als erwartet: "an entire three-dimensional subspace of rigid-unit structures
    " (Starrheit exakt erfuellt; Zitat gekuerzt, Urheberrecht) mit P2_12_12_1 [S, Z. 502 bis 507]. Drei
    solche Mannigfaltigkeiten, je X-Punkt eine (Z = 4-Zelle), Treffpunkt nur die kubische Ideallage [S, Z. 507 bis 513].
    Inhalt je Mannigfaltigkeit: alpha1, alpha1' (X-Punkt, P4_12_12 bzw. P4_32_12) und beta1 (Gamma, I-42d) [S].
  - (c) Kein Wort zu isotropem Atmen (grep "isotrop" ohne Treffer) -> wie erwartet.
  - **Unerwartet 1 (gross):** Drehungen aus zwei verschiedenen der drei Mannigfaltigkeiten lassen sich
    nicht starr kombinieren (Paraphrase statt Zitat, Urheberrecht) [S, Abschnitt IV, Z. 750 bis 757]. P2_13 braucht aber alle drei
    X-Punkte (kubische P-Zelle, Z = 8) und ist in ISO-ATEM-1 exakt starr (Handformel, Rest 1e-16) [P].
    Schreibtisch [M, ES]: Bei P2_13 (Wyckoff 4a: (x,x,x), (1/2-x,-x,1/2+x), (-x,1/2+x,1/2-x), (1/2+x,1/2-x,-x)) ist die
    x-Komponente der Drehachsen ueber die vier fcc-Plaetze (+,-,-,+), also mit X_z moduliert; y mit X_x, z mit X_y.
    Jede Komponente ist eine Drehung senkrecht zu ihrem k, also vom alpha-Typ der jeweiligen Mannigfaltigkeit.
    P2_13 ist damit linear eine Dreierkombination aus allen drei Mannigfaltigkeiten. Lesart: Coh/Vanderbilt schliessen
    Paare aus und rechnen nur Z = 4-Zellen; die kubische Dreierkombination behandeln sie nicht. Kein Widerspruch, aber
    ihr Satz ist ohne die Einschraenkung "Paare, Z = 4" zu stark. **Moderator: Zellgroesse (Z = 4 gegen Z = 8).**
  - **Unerwartet 2:** Kippungen starrer Tetraeder koennen das Idealvolumen nur verkleinern (Paraphrase) [S, Z. 254
    bis 256]. Fuer Finns Atmen: starres Atmen geht nur nach unten (Schrumpfen ab der Ideallage) und zurueck, nie
    darueber. Passt zu ISO-ATEM-1 (V/V0 <= 1) [P].
  - Weitere Funde [S]: Hatch/Ghose 1991: beta schwankt zwischen 12 alpha-Domaenen (3 X-Punkte x 2 Enantiomorphe x
    +-phi) (Z. 711 bis 719). O'Keeffe/Hyde 1976 diskutieren einen Weg alpha -> beta ueber zwei verschiedene
    Mannigfaltigkeiten (Z. 727 bis 735). Messung (Sekundaerzitat, Ref. 53 = Schmahl/Swainson/Dove/Graeme-Barber 1992):
    beta etwa 5 % groesser als alpha (Z. 696 bis 699). DFT: beta-tilde 2,2 % groesser als alpha-tilde.
  - Jedes Modell nur ueber Si-O-Si-Winkel gibt einen Weg ohne Barriere alpha1 -> beta1 (Z. 669 bis 680) [S].
- Gelesen bis 09:08:21 (date).

### A2 (Erwartung vor Abruf, geschrieben 09:08:45 date)
- WebSearch nach gemessener Waermeausdehnung von beta-Cristobalit (Gitterkonstante gegen T). Erwartung: Treffer auf
  Schmahl u. a. 1992 (Z. Krist. 201, 125) und/oder Bourova/Richet 1998 (GRL); im beta-Feld Koeffizient nahe null
  (Betrag unter 5e-6/K, Vorzeichen eher negativ bis null); alpha-Feld stark positiv (Groessenordnung 1e-5 bis 1e-4/K
  linear), Sprung etwa +5 % Volumen bei 490 bis 540 K. Suchtreffer sind keine Quelle; Zahl danach an der
  Primaerquelle lesen.
- **A2 ausgefuehrt** (WebSearch, Treffer gelesen bis 09:09:16 date). Suchtreffer-Zusammenfassung, **keine Quelle**:
  - Schmahl u. a. 1992: Ausdehnungskoeffizient von beta faellt beim Erwaermen, ueber 1000 Grad C Zellparameter
    "virtually constant" (Treffer epub.ub.uni-muenchen.de/18597, offenbar LMU-Repositorium).
  - Bourova/Richet 1998: Volumen von beta steigt bis 1300 K, **faellt dann bis zum Schmelzpunkt 2000 K** auf den Wert
    von 750 K (27,4 cm^3/mol) (Treffer earthref.org/ERR/18636).
  - **Erwartungsverstoss (vorlaeufig, an Primaerquelle pruefen):** Ich hatte im beta-Feld "nahe null, eher negativ"
    erwartet, einheitlich. Der Treffer zeigt **zwei Regime innerhalb von beta**: erst positiv (bis 1300 K), dann
    negativ (1300 bis 2000 K). Moderator: Temperatur innerhalb von beta.

### A3 (Erwartung vor Abruf, geschrieben 09:09:16 date)
- curl epub.ub.uni-muenchen.de/18597 (Seite, dann ggf. PDF als A4). Erwartung: Eintrag Schmahl/Swainson/Dove/
  Graeme-Barber 1992 mit Abstract; Abstract nennt Tc um 500 K bis 545 K, erste Ordnung, Volumensprung einige Prozent,
  Koeffizient von beta klein und fallend; keine Zahl fuer alpha_V im Abstract.
- **A3 ausgefuehrt 09:09:30 (date, quellen/A3-zeit.txt)**, curl LMU-epub 18597, gelesen bis 09:09:57 (date).
  - Schmahl/Swainson/Dove/Graeme-Barber 1992, Z. Krist. 201, 125-145, DOI 10.1524/zkri.1992.201.1-2.125 [S Abstract,
    auf der Seite abgeschnitten]: Uebergang Fd-3m -> P4_12_12 "strongly first order" **nahe 533 K**, latente Waerme
    1256 J/mol, **grosser Volumensprung von 5 %** (Paraphrase), ein aktiver Ordnungsparameter, keine Kopplung der sechs
    Komponenten. Volltext auf LMU nicht frei.
  - Erwartung bestaetigt (Tc, erste Ordnung, 5 %). Der Satz zum fallenden beta-Koeffizienten aus dem Suchtreffer steht
    auf dieser Seite **nicht**; bleibt unbelegt.
  - Folge [ES]: Beim Erwaermen durch Tc **waechst** Cristobalit sprunghaft um etwa 5 % Volumen (P4_12_12 -> kubisch).
    In ISO-ATEM-1-Sprache: Die statische Kippung loest sich, das Geruest atmet "aus" zur groesseren Form.

### A4 (Erwartung vor Abruf, geschrieben 09:09:57 date)
- OpenAlex-Suche "Quartz and cristobalite: high-temperature cell parameters and volumes of fusion" (Bourova/Richet
  1998, GRL). Erwartung: Abstract bestaetigt den Suchtreffer (beta-Volumen steigt bis ~1300 K, faellt bis 2000 K auf
  27,4 cm^3/mol wie bei 750 K); keine Koeffizientenzahl im Abstract; DOI fuer den Volltext.
- **A4 ausgefuehrt 09:10:02 (date)**, OpenAlex, Abstracts rekonstruiert (jq, nur Lesen), gelesen bis 09:10:58 (date).
  - Bourova/Richet 1998, GRL, DOI 10.1029/98gl01581 [S Abstract]: Synchrotron-Roentgenbeugung bis zum Schmelzpunkt.
    beta-Cristobalit: Volumen steigt gleichmaessig bis 1300 K, **faellt dann stetig bis 2000 K** und ist dort wieder beim
    Wert von 750 K, **27,4 cm^3/mol**. Quarz ueber 1400 K mit leicht negativem Ausdehnungskoeffizienten (Paraphrase).
    Schmelzvolumen beta-Cristobalit -0,1 cm^3/mol.
  - **Erwartungsverstoss bestaetigt (an der Primaerquelle, Abstract):** Im beta-Feld gibt es zwei Regime, positiv bis
    1300 K, negativ darueber. Erwartet hatte ich ein einheitliches "nahe null, eher negativ".
  - [E aus S] Mittlerer Volumenkoeffizient 750 bis 2000 K = 0 (gleiches Volumen an beiden Enden). Rundung der Angabe
    (+-0,05 cm^3/mol) gibt |alpha_V| <= 0,05/27,4/1250 K = 1,5e-6/K (Rechnung von Hand: 0,05/27,4 = 1,82e-3;
    /1250 = 1,46e-6), linear |alpha_L| <= 0,5e-6/K. Lokale Koeffizienten (Vorzeichenwechsel bei 1300 K) nur im
    Volltext.
  - Beifang (24-Monats-Fenster): Stokes 2024, J. Am. Ceram. Soc., DOI 10.1111/jace.20214, "beta-Cristobalite thermal
    expansion and stability in EBC systems" [S Abstract]: Abstract ohne Zahl; modifikator-stabilisiertes SiO2.

### A5 (Erwartung vor Abruf, geschrieben 09:10:58 date)
- OpenAlex search=cristobalite, Jahre 1932, 1975, 1976, 1991 (Barth, Wright/Leadbetter, O'Keeffe/Hyde, Hatch/Ghose).
  Erwartung: O'Keeffe/Hyde 1976 Abstract nennt Ableitungen des idealen Cristobalits mit regulaeren Tetraedern
  (P2_13, I-42d, P4_12_12 und weitere), keine Vollstaendigkeitsbehauptung; Hatch/Ghose 1991 Abstract: X-Punkt-
  Ordnungsparameter, beta dynamisch, P4_12_12; Wright/Leadbetter 1975: I-42d-Domaenen, P2_13 als verworfenes Modell
  erwaehnt; Barth 1932 vermutlich ohne Abstract.
- **A5 ausgefuehrt 09:11:04 (date)**, OpenAlex (500 Treffer, gefiltert per grep/jq), gelesen bis 09:11:33 (date).
  - **Wright/Leadbetter 1975**, Phil. Mag. 31, DOI 10.1080/00318087508228690 [S Abstract]: 16 O je Zelle statistisch
    ueber die 96 Lagen (h) von Fd-3m verteilt; gedeutet als **Domaenen von "ideal cristobalite" (I-42d) in sechs
    Orientierungen** (eine Art Mikro-Verzwillingung, Paraphrase); statische Unordnung (U_x^2)^1/2 = 0,18 A fuer Si. **Kein P2_13.**
    -> Bestaetigt A1: AV1-Zuschreibung falsch. Erwartung "P2_13 als verworfenes Modell erwaehnt": im Abstract nicht.
  - Leadbetter/Wright 1976, Phil. Mag., DOI 10.1080/14786437608221095 [S Abstract]: Gitterparameter je Phase "smooth
    and slow variation with temperature", Phasensprung mit Volumenunterschied etwa 4 % (Paraphrase), erste Ordnung, Hysterese,
    ~20 Grad C Koexistenz.
  - Barth 1932 "The cristobalite structures" (Am. J. Sci., DOI 10.2475/ajs.s5-23.136.350) und Barth/Posnjak 1932
    (Z. Krist. 81, alpha-Carnegieit, Beziehung zu Hoch-Cristobalit) existieren; **kein Abstract-Text**, P2_13 bei Barth
    bleibt [L?].
  - O'Keeffe/Hyde 1976 (DOI 10.1107/s0567740876009308) und Hatch/Ghose 1991 (DOI 10.1007/bf00202234): in OpenAlex
    **ohne Abstract**.

### A6 (Erwartung vor Abruf, geschrieben 09:11:33 date)
- IUCr-Seite O'Keeffe/Hyde 1976 (journals.iucr.org, DOI 10.1107/S0567740876009308). Erwartung: Abstract beschreibt
  Cristobalit-Ableitungen durch Drehung regulaerer Tetraeder, nennt P2_13 (Barth) und P4_12_12 bzw. I-42d mit
  Formeln Zellparameter gegen Drehwinkel; keine Vollstaendigkeitsbehauptung; nichts zu isotropem Atmen ausser
  implizit bei P2_13 (kubisch).
- **A6 ausgefuehrt 09:11:38 (date): HTTP 403 (Cloudflare-Abfrage), kein Inhalt.** Abruf verbraucht. O'Keeffe/Hyde
  1976 bleibt [L?]. Gelesen bis 09:11:48 (date).

### A7 (Erwartung vor Abruf, geschrieben 09:11:48 date)
- Springer-Seite Hatch/Ghose 1991 (DOI 10.1007/BF00202234). Erwartung: Abstract: Ordnungsparameter am X-Punkt
  (Irrep X_4 o. ae.), alpha = P4_12_12 als Isotropie-Untergruppe, beta dynamisch ungeordnet (Mittel ueber Domaenen),
  Domaenenzahl; Liste weiterer Isotropie-Untergruppen (z. B. P2_13, P2_12_12_1) nur im Volltext; keine starren
  Tetraeder als Rechnung.
- **A7 ausgefuehrt 09:11:53 (date): Springer "Client Challenge" (JavaScript), kein Inhalt.** Abruf verbraucht.
  Hatch/Ghose 1991 nur als Sekundaerzitat bei Coh/Vanderbilt [S, A1 Z. 711 bis 719]. Gelesen bis 09:12:37 (date).
- **Kurskorrektur:** Verlagsseiten (IUCr, Springer) sind fuer curl gesperrt. Rest nur ueber arXiv, OpenAlex,
  PubMed, Websuche. Noch 8 Abrufe (A8 bis A15).

### A8 (Erwartung vor Abruf, geschrieben 09:12:37 date)
- OpenAlex filter=doi fuer Mary u. a. 1996 (Science 272, 90), Swainson/Dove 1993 (PRL 71, 193), Cao u. a. 2002
  (PRL 89, 215902), Tucker u. a. 2005 (PRL 95, 255501), Bridges u. a. 2014 (PRL 112, 045505). Erwartung: Mary:
  isotrope NTE von 0,3 K bis 1050 K, alpha_L etwa -9e-6/K (alpha-Phase) und etwa -5e-6/K (beta-Phase); Swainson/
  Dove: beta-Cristobalit dynamisch ungeordnet durch RUM; Tucker: RUM-Bild fuer ZrW2O8 aus Totalstreuung bestaetigt;
  Cao: WO4-Einheiten nicht starr, Zr-O-W-Bewegung korreliert, gegen reines RUM; Bridges 2014: lokale Schwingungen
  statt starrer Einheiten. APS/Science-Abstracts koennen in OpenAlex fehlen.
- **A8 ausgefuehrt 09:12:42 (date)**, OpenAlex, 5 von 5 mit Abstract, gelesen bis 09:13:19 (date).
  - Mary/Evans/Vogt/Sleight 1996, Science 272, 90 [S Abstract]: NTE von 0,3 K bis zur Zersetzung bei etwa 1050 K;
    kubisch im ganzen Bereich, also isotrop; HfW2O8 gleich. **Keine Koeffizientenzahl im Abstract** -> Erwartung
    (Zahl -9e-6/K im Abstract) verletzt; Zahl bleibt offen bis A9.
  - Tucker/Goodwin/Dove/Keen/Wells/Evans 2005, PRL 95, 255501 [S Abstract]: RMC aus Neutronen-Totalstreuung;
    WO4 und ZrO6 bewegen sich quantitativ wie von der RUM-Theorie vorhergesagt; "We suggest that rigid unit modes are
    associated with the NTE"; gegen die XAFS-Deutung mit steifer Zr-O-W-Bruecke. -> erwartet.
  - Cao/Bridges/Kowach/Ramirez 2002, PRL 89, 215902 [S Abstract]: XAFS; NTE-Moden = korrelierte Schwingung eines WO4
    mit seinen drei naechsten ZrO6, **Translation des WO4 als starre Einheit laengs der vier <111>-Achsen**;
    "frustrated soft mode". -> erwartet, aber: auch hier starre Einheit, nur andere Bewegung.
  - Bridges u. a. 2014, PRL 112, 045505 [S Abstract]: XPDF + EXAFS 10 bis 500 K; Zr-O-W-Bruecke "relatively stiff",
    kein Biegen; NTE aus korrelierten Drehungen der ZrO6, die grosse <111>-Translationen der WO4 erzeugen, statt
    Querbewegung des O. -> erwartet.
  - Swainson/Dove 1993, PRL 71, 193 [S Abstract]: inelastische Neutronenstreuung + MD: niederfrequente "floppy modes"
    in beta-Cristobalit, wie in Netzwerkglaesern, aehnlich orientierungsungeordneten Kristallen. -> erwartet.
  - [ES, Regel 6] Drei Wege zur NTE in ZrW2O8 (RUM mit Biegen an O; korrelierte starre Translation mit steifer
    Bruecke; ZrO6-Drehung mit WO4-Translation). Gemeinsame Groesse: **niederfrequente Moden mit negativem
    Grueneisen-Parameter** (Querschwingung zieht die Bruecke zusammen). Streit ist um das Bauteil (welche Bindung
    biegt), nicht um die Kopplung. [H, nicht an einer Quelle geprueft]

### A9 (Erwartung vor Abruf, geschrieben 09:13:19 date)
- OpenAlex search "ZrW2O8 negative thermal expansion coefficient", 25 Treffer, in Abstracts nach Zahl suchen.
  Erwartung: mindestens ein Primaer-Abstract (Evans u. a. 1996 Chem. Mater. oder Ernst u. a. 1998 Nature) nennt
  alpha_L etwa -9e-6/K (bzw. -8,7e-6/K) fuer alpha-ZrW2O8 und etwa -5e-6/K ueber dem Ordnungsuebergang bei ~430 K.
- **A9 ausgefuehrt 09:13:26 (date)**, OpenAlex (15 Treffer, 11 mit Abstract), gelesen bis 09:13:52 (date).
  - **Evans/David/Sleight 1999**, Acta Cryst. B, DOI 10.1107/s0108768198016966 [S Abstract]: Pulverbeugung an 260
    Temperaturen 2 bis 520 K; a = 9,18000(3) A bei 2 K; **alpha = -9,07e-6/K (2 bis 350 K)** fuer alpha-ZrW2O8.
  - Evans 2000, JJAP 39 S1, 535, DOI 10.7567/jjaps.39s1.535 [S Abstract]: alpha_l = -9,1e-6/K (2 bis 300 K);
    Ursache "low energy phonon modes with negative Gruneisen parameters"; Uebergang bei 448 K zu beta-ZrW2O8 mit
    dynamisch ungeordnetem O. -> stuetzt meine [ES]-Kopplungsgroesse (negativer Grueneisen-Parameter) an einer
    Quelle.
  - **Pryde/Hammonds/Dove/Heine/Gale/Warren 1997**, Phase Transitions, DOI 10.1080/01411599708223734 [S Abstract]:
    RUM-Phononen in komplizierter Verteilung im reziproken Raum; kollektive Drehungen von ZrO6 und WO4 "enable ZrW2O8
    to contract upon heating"; NTE isotrop, nicht unterbrochen vom Uebergang bei 430 K. -> RUM-Erklaerung an der
    Primaerquelle.
  - Erwartung (-9e-6/K) bestaetigt, eine Zeile. Uebergangstemperatur in den Quellen 430 K bzw. 448 K (verschieden
    angegeben, nicht aufgeloest).

### A10 (Erwartung vor Abruf, geschrieben 09:13:52 date) - Gegensweep, 24-Monats-Fenster
- arXiv-API: (abs:cristobalite OR abs:"rigid unit") AND submittedDate 2024-10-05 bis 2026-10-05. Erwartung: wenige
  Treffer (unter 30); ML-Potentiale oder DFT zu beta-Cristobalit (anharmonische Stabilisierung, dynamische Unordnung),
  eventuell NTE-Arbeiten an Geruesten (ScF3, Cyanide, MOFs) mit RUM-Bezug; keine Arbeit, die das RUM-Bild fuer
  beta-Cristobalit grundsaetzlich verwirft; eher "quasi-RUM" oder "RUM plus Tetraederverformung".
- **A10 ausgefuehrt 09:13:57 (date): HTTP 301 (http -> https), curl ohne -L, kein Inhalt.** Mein Fehler; als Abruf
  gezaehlt (Selbstanzeige). Erwartung unveraendert fuer A11 (gleiche Abfrage ueber https). Notiert 09:14:06 (date).
- **A11 ausgefuehrt 09:14:12 (date): HTTP 503 der arXiv-API, kein Inhalt.** Gezaehlt. Notiert 09:15:12 (date).
- **Kurskorrektur:** Gegensweep 24 Monate ueber OpenAlex (Datumsfilter, Abstracts im selben Abruf) statt arXiv-API.
  Noch 4 Abrufe (A12 bis A15): A12 Gegensweep, A13 Vollzaehlungs-Suche (AV3), A14 Borcea/Streinu-Volltext,
  A15 Reserve.

### A12 (Erwartung vor Abruf, geschrieben 09:15:12 date) - Gegensweep, 24-Monats-Fenster
- OpenAlex search = cristobalite OR "rigid unit mode(s)", from_publication_date 2024-10-05. Erwartung wie A10:
  ML/DFT zu beta-Cristobalit (anharmonisch, dynamische Unordnung), NTE-Gerueste mit RUM; keine grundsaetzliche
  Verwerfung des RUM-Bildes; moeglich: Arbeiten, die Tetraederverformung oder Bindungsdehnung als gleichwertig
  zeigen.
- **A12 ausgefuehrt 09:15:18 (date)**, OpenAlex 2136 Treffer, erste 100 nach Relevanz, Abstracts gegrept, gelesen
  bis 09:16:23 (date).
  - **Erwartungsverstoss (gross, fuer AV3):** Campbell/Eggers/Stokes 2025, "Large-angle rigid unit modes in
    crystalline frameworks", DOI 10.1063/4.0000587 (Struct. Dyn., Tagungsabstract) [S Abstract]: Es gibt schon einen
    algebraischen Weg, die **kleinwinkligen RUM systematisch und vollstaendig** (Paraphrase) vorherzusagen, geordnet nach
    irreduziblen Darstellungen der Elterngruppe. Manche kleinwinkligen RUM verformen bei grossem Winkel die Einheiten,
    sind also keine grosswinkligen RUM. Vorgestellt wird "the first systematic search algorithm for large-angle RUMs";
    der Kleinwinkel-Grenzwert des Raums grosswinkliger RUM ist **eine Vereinigung von Unterraeumen** des Raums
    kleinwinkliger RUM. Beispiele im Abstract nicht genannt (Cristobalit unbekannt).
  - Eggers/Stokes/Campbell 2024, Acta Cryst. A, DOI 10.1107/s205327332401163x [S Abstract]: kleinwinklige RUM, die
    eine **linear mitwachsende Gitterverzerrung** brauchen, wurden von den bisherigen Werkzeugen nicht gefunden; jetzt
    systematisch eingeschlossen ("any geometrically possible small-angle RUM can be detected").
  - Kastis/Kitson 2026, J. Math. Anal. Appl., DOI 10.1016/j.jmaa.2026.131029 [S Abstract]: RUM-Spektrum symmetrischer
    Gerueste (abelsche Symmetrie, lineare Nebenbedingungen), Mathematik, nur infinitesimal.
  - Gegensweep-Fund (Glas, nicht Kristall): "Vibrational spectrum of vitreous silica ... ROSA", DOI 10.1103/lnlg-ldlk
    (2026-06-15) [S Abstract]: im Niederfrequenzbereich sind starre Tetraederdrehungen **keine unabhaengigen
    Freiheitsgrade**, sondern "kinematically enslaved to bending coordinates by no-stretch constraints". Das widerspricht
    dem RUM-Bild nicht, verschiebt aber die Steuergroesse auf die Biegung an der Bruecke (Si-O-Si). Passt zu Coh/
    Vanderbilt Gl. 7 [S, A1] und zur [ES]-Kopplungsgroesse. Autoren in dieser Datei nicht ausgelesen.
  - Kein Abstract unter den 100 verwirft das RUM-Bild fuer beta-Cristobalit. "Microstructural insights into the
    stabilization of beta-cristobalite" (Ceram. Int. 2025) ohne RUM-Bezug im Titel, nicht weiter gelesen.
  - Folge fuer AV3 [ES]: Infinitesimal ist die Zaehlung **systematisch und vollstaendig** (Campbell/Stokes-Werkzeuge,
    seit 2024 auch mit linearer Verzerrung); endlich gibt es seit 2025 einen ersten systematischen Suchalgorithmus.
    Ob er auf Cristobalit angewandt wurde, ist offen. Coh/Vanderbilt geben fuer die Z = 4-Zellen die starren
    Mannigfaltigkeiten an. "Nur einzelne Varianten" ist also zu schwach.

### A13 (Erwartung vor Abruf, geschrieben 09:16:23 date)
- WebSearch "large-angle rigid unit modes" Campbell Stokes cristobalite (Anwendung auf Cristobalit? Volltext?).
  Erwartung: Treffer auf BYU/ISOTROPY-Seiten oder Acta Cryst. A 2018 "algebraic approach to cooperative rotations";
  Cristobalit als Beispiel eher nicht genannt; kein veroeffentlichter Volltext zum Grosswinkel-Algorithmus.
- **A13 ausgefuehrt** (WebSearch; Zeitklammer 09:16:23 bis 09:16:52 date, Suchzeitpunkt nicht einzeln gemessen).
  Suchtreffer-Zusammenfassung, **keine Quelle**: BYU-Seiten (iso.byu.edu "2018 Campbell.pdf", stokes.byu.edu
  "2021 Campbell a.pdf", ISOTILT-Werkzeug), Acta Cryst. A 2018 (me6016). Kein Treffer zeigt eine Anwendung des
  Grosswinkel-Algorithmus auf Cristobalit. -> Erwartung bestaetigt, eine Zeile.

### A14 (Erwartung vor Abruf, geschrieben 09:16:52 date)
- Borcea/Streinu 2011, arXiv 1110.4661 Volltext (curl PDF). Erwartung: periodische Stab-Gelenk-Gerueste, Cristobalit
  als Beispiel mit lokaler Dimension des Deformationsraums (endlich, nichtlinear) fuer eine feste Periodizitaet
  (wohl die kleinste Zelle); keine Abzaehlung isolierter Formen, nichts zu F = lambda I; eventuell "auxetische" Wege.
- **A14 ausgefuehrt 09:16:57 (date)**, curl arXiv-PDF, Text quellen/A14-borcea-streinu-1110.4661v1.txt, gelesen bis
  09:18:04 (date).
  - **Erwartungsverstoss (fuer AV3):** Borcea/Streinu 2011, **Theorem 2** [S, Txt Z. 161 bis 163]: Der Deformationsraum
    des idealen Hoch-Cristobalit-Geruests ist "naturally parametrized by the open set in SO(3)", solange die
    gezeichneten Erzeuger linear unabhaengig bleiben (Zitat gekuerzt, Urheberrecht). Periodizitaet = alle Translationen des Idealkristalls, n = 4
    Eckbahnen, m = 12 Kantenbahnen (Z. 114 bis 118), also die **primitive Zelle mit 2 Tetraedern**. Ein Tetraeder fest,
    das andere beliebig um O gedreht. Damit ist fuer die kleinste Zelle der **endliche** Deformationsraum vollstaendig
    bekannt: dreidimensional, SO(3). Erwartet hatte ich "lokale Dimension", nicht eine geschlossene globale Form.
  - Einleitung [S, Z. 28 bis 31]: bisher sei nur eine eng begrenzte Auswahl geometrischer Moeglichkeiten untersucht,
    meist Ein-Parameter-Familien; allgemein sei eine reiche, vielfaeltige Geometrie zu erwarten (Paraphrase).
  - Nichts zu isotropem Atmen (grep "isotrop" ohne Treffer), keine groesseren Zellen.
  - **Bausteine verkettet [M]:** Ideal ist das zweite Tetraeder das am Punkt O gespiegelte erste (t_i^0 = -s_i). Mit
    t_i = R t_i^0 werden die Gittervektoren gamma_i = t_i - s_i = -(R + I) s_i, also F = (R + I)/2. F = lambda I
    verlangt R = (2 lambda - 1) I; das ist nur fuer lambda = 1 eine Drehung. **ISO-ATEM-1 Abschnitt 1 Punkt 5 (die
    kleinste Zelle kann nicht isotrop atmen) folgt also in einer Zeile aus Theorem 2.** Deckt sich mit ISO-ATEM-1
    IA1 (F = (R_A + R_B)/2) [P].
  - [ES] Bild der Zellgroessen: Z = 2: SO(3), 3D, Tangente (beta1, beta2, beta3) [S BS]. Z = 4 (ein X-Punkt): dazu
    die P2_12_12_1-Mannigfaltigkeit (alpha1, alpha1', beta1), 3D [S CV]; die Tangentenkegel sind Vereinigungen von
    Unterraeumen, wie Campbell u. a. 2025 allgemein sagen [S Abstract]. Z = 8 (kubisch, ISO-ATEM-1): 9 lineare RUM
    (3 Gamma + 3 x 2 X), endliche Varietaet **nicht in der Literatur gefunden**; bekannt darin mindestens: SO(3)-Schar,
    drei 3D-Mannigfaltigkeiten, P2_13-Kurve.

### A15 (Erwartung vor Abruf, geschrieben 09:18:04 date) - letzter Abruf
- OpenAlex search "rigid unit modes thermal expansion" (1995 bis 2021, Abstracts), grep nach cristobalite/quartz.
  Erwartung: Welche/Heine/Dove 1998 (beta-Quarz: NTE durch RUM) und eine Dove-Uebersicht nennen RUM als Ursache
  kleiner bzw. negativer Ausdehnung der beta-Phasen; fuer beta-Cristobalit selbst keine Zahl im Abstract.
- **A15 ausgefuehrt 09:18:11 (date)**, OpenAlex (6873 Treffer, erste 100), gelesen bis 09:19:58 (date). **Budget 15/15
  verbraucht.**
  - **Heine/Welche/Dove 1999**, J. Am. Ceram. Soc., DOI 10.1111/j.1151-2916.1999.tb02001.x [S Abstract]: Starre
    Drehung der Einheiten verkleinert Volumen oder Gitterkonstante als rein geometrischer Effekt (Paraphrase); das gibt einen
    **negativen Beitrag** zum Ausdehnungskoeffizienten, **zusaetzlich** zum ueblichen positiven aus der Anharmonizitaet;
    am staerksten bei tiefen Frequenzen; das Vorzeichen des Koeffizienten "may be reversed above a soft mode
    phase transition". -> erwartet (Theorie), und genau die Zwei-Regime-Lesart (unter/ueber dem Kipp-Uebergang).
  - **Huang/Kieffer 2003**, J. Chem. Phys., DOI 10.1063/1.1529684 [S Abstract, **Simulation**, keine Messung]: MD mit
    Dreikoerperpotential; konsistent mit dem RUM-Modell; alpha-Cristobalit positiver Koeffizient, beta-Cristobalit
    **"almost zero ... up to 2000 K and slightly negative at higher temperatures"**, bestaetige Roentgendaten.
    -> Verstoss gegen meine Erwartung "keine beta-Aussage im Abstract": doch, aber als Simulation.
  - **Dove/Du/Wei/Keen/Tucker/Phillips 2020**, PRB 102, 094105 [S Abstract], ScF3, Gegensweep: NTE haengt **nicht nur
    an RUM**, sondern auch an Moden, die die Oktaeder verformen; quasiharmonisch mit anharmonischer Renormierung
    beschreibt es gut, "in contrast with previous predictions". -> Gegenstimme aus der RUM-Schule selbst (ausserhalb
    des 24-Monats-Fensters).
  - Welche/Heine/Dove 1998 (beta-Quarz) unter den 100 nicht als eigener Treffer geprueft.

## 8. Gegensweep (Regel 4), ab 09:20:30 (date), ohne Netz (Budget 15/15 verbraucht)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- **G1 "Die 222-Form ist P2_12_12_1" (mein Schreibtisch-[H]). GEPRUEFT** an ISO-ATEM-1 nachtrag-69/diag-c.json [P]
  (lokal, jq): Klasse mit Achse [0,0,1] (n = 49): 2[0,0,1] mit Laengsanteil 0,5 (= c/2, also 2_1); 2[1,1,0] mit
  Laengsanteil 0,35355 = a_c/(2 sqrt 2) = a_t/2 (also 2_1 laengs a_t); 2[1,-1,0] ebenso (0,6464 = 1 - 0,3536, Kosmetik
  der Modulo-Rechnung, Selbstanzeige 9 dort). Gitter primitiv mit halber Wuerfelzelle, (1/2,0,1/2) fehlt, also keine
  Innenzentrierung. Drei senkrechte 2_1 in primitivem Gitter: **Drehteil-Gruppe P2_12_12_1** [ES, an Daten geprueft].
  Drei Ausrichtungen = X_x, X_y, X_z = die drei Mannigfaltigkeiten bei Coh/Vanderbilt. Grenze: Uneigentliche
  Operationen hat ISO-ATEM-1 nicht getestet; eine hoehere Gruppe mit gleichem Drehteil ist nicht ausgeschlossen.
- **G2 "Der 5-%-Sprung ist ein Wachsen beim Erwaermen."** Geprueft (A1, Coh/Vanderbilt Z. 696 bis 699: beta ist im
  Experiment etwa 5 % groesser, Paraphrase) [S]. Bestaetigt.
- **G3 "750 K liegt im beta-Feld."** Geprueft am Schreibtisch: Tc nahe 533 K (Schmahl, A3) < 750 K. Bestaetigt.
- **G4 "Die Tetraeder bleiben beim Atmen im echten SiO2 starr."** Teilgeprueft (A1, Coh/Vanderbilt Z. 247 bis 252,
  DFT): fuer V < V0 bleiben O-Si-O-Winkel und Si-O-Laengen fast konstant (Paraphrase), Si-O-Si aendert sich um ~35 Grad [S].
  Nicht geprueft: thermische Dehnung der Si-O-Bindung selbst (der positive Beitrag nach Heine u. a. 1999).
- **G5 "Die P2_13-Schar ist Barths Modell."** Nicht geprueft (Barth 1932 ohne Abstract, kein Abruf mehr). Bleibt [L?].
- **G6 "OpenAlex-Abstracts sind woertlich die Verlagsabstracts."** Nicht geprueft; Stichprobe moeglich nur mit
  weiterem Abruf. Risiko: Rekonstruktion aus dem invertierten Index kann Woerter verlieren (z. B. Formeln bei Tucker
  2005: "the and polyhedra" - dort fehlen offenbar WO4/ZrO6). Zahlen (Evans 1999, Bourova/Richet) sind lesbar.
- **G7 "Coh/Vanderbilts Mannigfaltigkeit ist die vollstaendige starre Menge der Z = 4-Zelle."** Nicht bewiesen; sie
  sagen sinngemaess, es gebe eine ganze dreidimensionale Schar, nicht, es gebe nur diese (Paraphrase). Meine Zuordnung der
  222-Form haengt daran nur schwach (Symmetrie und Zaehlung passen).
- **Zusatzfund im Gegensweep (Tabelle I bei Coh/Vanderbilt, A1 Z. 196 bis 222) [S]:** DFT-Idealzelle a_c = 7,444 A;
  beta-tilde (I-42d) relaxiert a = 7,1050 A, c = 7,4061 A, also a/a_c = 0,9545, c/a_c = 0,9949 [E aus S]: **die
  Wright/Leadbetter-Form schrumpft nur quer zur Drehachse** = ISO-ATEM-1 Teil A (flaches Atmen). Experiment (Refs. 3,
  10): beta a = 7,131 A ("average cubic"), alpha a = 4,9570 A, c = 6,8903 A, also c/(sqrt 2 a) = 0,983 [E aus S]: alpha
  ist nicht isotrop. Gemischter Vergleich Experiment/DFT-Ideal: 7,131/7,444 = 0,958 = lambda des echten beta
  [E aus S, Methoden gemischt, DFT-Gitter meist ~1 % zu gross].
- Notiert 09:21:22 (date).

## 9. Stand der Rueckfragen und Erwartungsverstoesse (Nachtrag 09:23:40 date; Abschnitte 6 und 7 oben bleiben stehen)

- ~~Q1: Ist die 222-Form P2_12_12_1?~~ Drehteil-Gruppe ja (G1, an Daten geprueft); ob sie in der CV-Mannigfaltigkeit
  liegt: [ES], nicht gerechnet -> bleibt offen als Q1'.
- ~~Q2: Wer hat P2_13 vorgeschlagen?~~ Nicht Wright/Leadbetter [S]. Barth 1932 [L?] -> bleibt offen als Q2'.
- ~~Q3: Gemessener Koeffizient beta-Cristobalit.~~ Mittel 750 bis 2000 K = 0 [E aus S]; lokale Werte nur im Volltext
  -> offen als Q3'.
- Neu Q4: Wurde der Grosswinkel-Algorithmus (Campbell u. a. 2025) auf Cristobalit angewandt?
- Neu Q5: Ist die CV-Mannigfaltigkeit die ganze starre Menge der Z = 4-Zelle?
- Neu Q6: Hatch/Ghose 1991 Untergruppenliste (gesperrt).
- Neu Q7: Direkte Messung des RUM-Anteils an der beta-Ausdehnung (Totalstreuung) nicht gelesen.
- Erwartungsverstoesse, geordnet: E1 mehr als Einzelvarianten (BS-SO(3), CV-3D, Campbell 2025); E2 CV-"inkompatibel"
  gegen exaktes P2_13 (Moderator Zellgroesse); E3 zwei Regime in beta (Vorzeichenwechsel 1300 K); E4 W/L = I-42d;
  E5 starres Atmen nur nach unten; E6 keine Zahl bei Mary 1996; E7 Huang/Kieffer-Grenze 2000 K gegen 1300 K.
- Kalibrierung, Warnzeichen: Meine Sicherheit "222 = isotroper Ast der CV-Mannigfaltigkeit" stieg von [H] auf "sehr
  wahrscheinlich" nur durch Symmetrie und Zaehlung, ohne Rechnung. Gehoert so in den Bericht.

## 10. Praezisierung zu E2 (P2_13-Zerlegung), 09:24:49 (date), Schreibtisch [M]

- Abschnitt A1 "Unerwartet 1" nannte nur das A-Teilgitter. Vollstaendig (B-Plaetze (1/4,1/4,1/4), (1/4,3/4,3/4),
  (3/4,3/4,1/4), (3/4,1/4,3/4), Achsen [111], [-1,-1,1], [-1,1,-1], [1,-1,-1]):
  - Anteil bei X_z: A dreht um x (z = 0: +x, z = 1/2: -x), B dreht um y (z = 1/4: +y, z = 3/4: -y). Folge der Schichten
    +x, +y, -x, -y: das ist das 4_1-Muster von alpha-Cristobalit, also ein alpha-Typ-Modus bei X_z.
  - Zyklisch: X_x mit A um y, B um z; X_y mit A um z, B um x. Kein Gamma-Anteil (Summen je Komponente null).
  - Also: **P2_13 = je ein alpha-Typ-Modus an allen drei X-Punkten mit gleicher Amplitude** (linear). Das bleibt im
    Widerspruch zum woertlich allgemeinen Satz bei Coh/Vanderbilt, wenn man ihn ueber Paare hinaus liest; logisch
    zwingend ist der Widerspruch nicht (Paare koennen scheitern, wo das kubische Tripel gelingt).
- Rechnung nur von Hand, nicht gegengelesen.

## 11. Urheberrecht, Nachtrag 09:31:17 (date)

- Mehrfach- und Langzitate (ueber eine Quelle hinaus bzw. ab 15 Woertern) habe ich in den Abschnitten A1, A3, A4, A5,
  A12, A14, A15 und 8 durch Paraphrasen ersetzt, markiert mit "(Paraphrase)" bzw. "(Zitat gekuerzt)". Inhalt und
  Zeilenangaben sind unveraendert. Die Fassung davor liegt unveraendert in quellen/ARBEITSFELD-vor-Paraphrase.bak
  (statt Loeschen, Regel 5).
- Abgabe Dossier 2026-10-05 09:32:10 CEST (date). Ende.
