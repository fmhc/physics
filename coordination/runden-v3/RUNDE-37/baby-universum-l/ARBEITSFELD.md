# BABY-UNIVERSUM-L: Arbeitsfeld (feldforscher fuer claude-primary)

- Start 2026-10-05 08:05:01 CEST (date). Zeitbox 60 min, also bis 09:05:01. Hoechstens 15 Netzabrufe.
- Bindend: KARTE.md (BU1 bis BU6 unveraendert). Diese Datei ist das gemeinsame Feld (Regel 5): vor jedem Schritt neu
  lesen; Gestrichenes bleibt ~~durchgestrichen~~; offene Rueckfragen wandern sichtbar mit.
- Kennzeichen: [E] Messung/Rechnung, [M] Mathematik, [S] Fachquelle an der Stelle gelesen, [S Abstract], [L]
  Lehrbuch/Gedaechtnis, [L?] unsicher, [H] Hypothese, [P] Projektbefund, [ES] eigener Schluss.

## 0. Gelesen vor dem ersten Netzabruf (08:05 bis 08:08, lokal, kein Abruf)

- KARTE.md ganz. WELTKRISTALL-L DOSSIER ganz. UMKLAPP-1 ERGEBNIS ganz. TAKT-UMKLAPP-1 KARTE ganz (nur gelesen).
  HODGE-L DOSSIER Abschn. 1-3. GLIED-10 (25.09.) Kurzfazit und Erwartungsverstoesse; GLIEDER-7-10 Kurzfazit, 2.1, 2.2.
  RUNDE-22 geometrie-stand ERGEBNIS Z. 200-290.
- Projekt-grep "baby univers|minbu|minimal neck" (~~08:06~~ geschaetzt; berichtigt: zwischen den date-Messungen
  08:05:01 und 08:08:49, volle Ausschlussliste): Treffer nur in Quellentexten
  (Loll 2019, AGJL 2012, CDT-review-raw, Catterall 1810.10626), Scout-Cache und Kartentexten. Keine eigene Rechnung.

### 0.1 Lokale Funde (ohne Abrufzaehlung)

- **L1 Loll 2019 (1905.08669), lokal RUNDE-22/geometrie-stand/hilfs/loll-1905.08669.txt, Z. 606-622 [S]:**
  - CDT verbietet Verzweigungen, bei denen das raeumliche Universum seine Topologie aendert und in getrennte Teile
    zerfaellt; in DT seien sie generisch vorhanden, gleich welcher Zeitbegriff (sinngemaess).
  - Kausalitaet scheine fuer einen guten klassischen Limes wesentlich (Heuristik aus Simulationen, kein Satz).
  - **Wichtig:** raeumliche Verzweigungen seien weiter "perfectly allowed ... and will generically occur" (einziges
    Zitat aus L1). -> BU3 ("CDT verbietet sie") gilt nur fuer die Zeitrichtung. Kandidat Erwartungsverstoss.
- **L2 AGJL 2012 (1203.3591), lokal weltkristall-l/quellen/F6-...txt [S]:**
  - Abschn. 5.1 (S. 49-53): In 2D gilt exakt: CDT (g_s = 0) plus zugelassene Baby-Universen mit g_s = 1 ergibt die
    euklidische 2D-Gravitation (Liouville); umgekehrt ergibt Ausintegrieren der Baby-Universen aus der euklidischen
    Summe CDT [64]. Mit g_s = G_s a^3 (GCDT) sind Baby-Universen stark unterdrueckt; euklidisch "completely
    dominate" (einziges Zitat aus L2). -> Im 2D-Fall ist das eine **Rechnung im Modell (exakt loesbar)**, kein
    heuristisches Argument.
  - S. 54 (Z. 2697-2705): Unterschied Onsager- gegen KPZ-Exponenten wird mit Baby-Universen erklaert [67].
  - S. 79, Fussnote 15: 4D-EDT: Baby-Universen mit duennem Hals; Zaehlen misst den Suszeptibilitaetsexponenten [79];
    Baby-Universum-Chirurgie [80] verkuerzte Autokorrelation um Groessenordnungen; in CDT kein Gegenstueck gefunden.
  - S. 83-84: Knaeuel (kappa0 klein, auch 0: nur Entropie) -> 1. Ordnung -> verzweigte Polymere (kappa0 gross).
    Sinngemaess: Uebergang von Entropie-Dominanz zu Dominanz des konformen Faktors. Fn. 21:
    CDT heilt die konforme Krankheit nichtperturbativ (positiver kinetischer Term des Skalenfaktors aus Entropie).
  - [ES] Damit sind die zwei Regime ueber eine gemeinsame Groesse gekoppelt: das Vorzeichen des effektiven
    kinetischen Terms des konformen Faktors (Skalenfaktors). Kontinuum: Coleman-Problem; Gitter: Polymerphase.
- **L3 Scout-Speicher (research-scout-claude-20260913/http-cache, OAI-PMH, nicht von mir abgerufen) [S Abstract]:**
  - Chen 2026 (2609.16116) "Group-averaged baby universe field theory": alpha-Sektoren aus Gaussschem Mass; im
    topologischen Marolf-Maxfield-Modell exakte Fock-Darstellung.
  - Akbarieh 2026 (2609.04191): Axionmasse aus GS-Wurmloch haengt vom Baby-Universum-Zustand ab (alpha-Sektor).
  - Bahiru 2026 (2608.27563): Ultralimits, Ensemble von CFT_p, Baby-Universen und Wurmloecher.
  - Dai/Dong/Peng 2026 (2610.02168): "booklet cosmology", geschlossenes Universum aus mehreren CFTs.
  - -> Strang Marolf-Maxfield/alpha-Sektoren ist im 24-Monats-Fenster aktiv, ohne Entscheidung.

## 1. Plan der Abrufe (hoechstens 15)

| Plan | Ziel | Zweck |
|---|---|---|
| F1 | arXiv-PDF Hebecker/Mikhail/Soler 2018 (1807.00824) | Uebersicht: Coleman, GS, alpha, Einwaende, 3-Form gegen Skalar, negative Moden |
| F2 | arXiv-API id_list (Abstracts) | Primaerabstracts: Marolf/Maxfield, McNamara/Vafa, Hertog u. a., Loges u. a., AJJK 1993, Jain/Mathur, Ambjorn/Loll 1998, Jordan/Loll, Laiho u. a., Ambjorn u. a. 2013, Bassler u. a., Kawai/Okada, Usatyuk u. a. |
| F3 | INSPIRE-API klassische Arbeiten 1988-1989 | Coleman, Giddings/Strominger, Hawking, Polchinski, Fischler/Susskind: Abstract-Lage |
| F4 | arXiv-API Suche Axion-Wurmloch Stabilitaet, neueste zuerst | BU5, 24 Monate |
| F5 | arXiv-API Suche Coleman-Mechanismus / Baby-Universen Lambda, neueste | BU1, 24 Monate |
| F6 | arXiv-API Suche DT/CDT Baby-Universen, neueste | BU3, 24 Monate |
| ~~F7~~ | ~~arXiv-API Suche Baby-Universum-Hilbertraum eindimensional, Kritik~~ | ~~BU2, 24 Monate~~ (08:29: wurde F8; F7 war der McNamara/Vafa-Volltext) |
| F8-F15 | Reserve: Volltextstellen, Gegenarbeiten, 3D-DT-Phasen | |

- Berichtigung 08:29:36 (date): Plan nachtraeglich abgeglichen. Tatsaechlich F7 = McNamara/Vafa-Volltext, F8 =
  H_BU-Suche, F9 = INSPIRE Duff/HT/3D-DT, F10 = Hodge-Vermutung, F11 = BU und Lambda, F12 = CDT-Topologie,
  F13 = Lickorish/AJ 1995, F14 = Egawa-Volltext, F15 = IceCube. In der F2-Erwartung steht "19 IDs"; gesendet wurden 18.

## 2. Erwartungen vor jedem Abruf und Ausgaenge (Regel 3)

(Eintraege folgen; Format: Fn, Zeit (date), Erwartung -> Ausgang, Verstoss ja/nein.)

- **F1, Erwartung 08:09:32 (date):** Hebecker/Mikhail/Soler 2018 (1807.00824, Volltext) sagen: Colemans Lambda -> 0
  haengt am euklidischen Pfadintegral mit exp(+3 pi/(G Lambda)) und gilt nicht als etabliert; Einwaende: konformer
  Faktor (Vorzeichen), Katastrophe grosser Wurmloecher (Fischler/Susskind, Polchinski), fehlende Kontrolle. GS-Wurmloecher
  sind Loesungen mit 3-Form-Fluss; dualisiert zum Axion braucht man ein imaginaeres Axion bzw. falsches Vorzeichen.
  Negative Moden: Rubakov/Shvedov fanden eine, spaeter strittig (Hertog u. a. 2018). WGC-Bezug.
- **F1, Ausgang 08:10:14 (date): im Kern bestaetigt, mit drei Abweichungen (Analysezyklus, weil sie BU1/BU5 schaerfen).**
  Quelle quellen/F1-arxiv-1807.00824-hms-20261005-080942.pdf/.txt (v3, 10.10.2018).
  - Bestaetigt [S, Abschn. 4.1, S. 22]: Colemans Logik ist "nowadays generally not considered a valid solution";
    Gruende: gemessenes Lambda nicht null, Inflation, FKS-Katastrophe, Vorzeichen-/Negativmoden-Problem.
  - **Abweichung A1 (schaerft BU1):** Der Coleman-Peak exp(exp(...)) hat seinen letzten Ursprung im konformen Faktor;
    die Gibbons-Hawking-Perry-Drehung (Heilung des konformen Faktors) dreht das Vorzeichen, dann erklaert nichts mehr die
    Kleinheit [S, Abschn. 5.2, S. 40]. -> Die Heilung des einen Problems toetet den Mechanismus. Das ist kein
    Nebeneinander zweier Probleme, sondern ein Dilemma. [ES]
  - **Abweichung A2 (schaerft BU5):** Hodge-Dualitaet H = f^2 *d theta [S, Abschn. 2.2, Gl. 7-8]: Der GS-Sattel liegt in
    der B2/H3-Form auf der reellen Achse, in der theta-Form auf der imaginaeren Achse. Fn. 4: Die Lesart "falsches
    Vorzeichen" sei begrifflich irrefuehrend; beide Formen haben normale kinetische Terme. -> Die Dualitaet ist
    genau das Werkzeug, an dem der Streit haengt; meine Erwartung "falsches Vorzeichen" war die von HMS abgelehnte Lesart.
  - **Abweichung A3:** Negative Moden 2018: Rubakov/Shvedov eine; Gegenargument Eichmode [196]; Alonso/Urbano [97]
    (lorentzisch identifizierte Moden) keine; noch offen [S, Abschn. 5.2, S. 41].
  - Dazu [S, S. 3], sinngemaess: weder Unphysikalitaet von Wurmloechern/Baby-Universen gezeigt noch ein befriedigendes
    Gesamtbild -> stuetzt BU6 (Stand 2018).
  - FKS [S, Abschn. 5.1]: R^2-Term, alpha3 -> unendlich, dichte Packung auch grosser Wurmloecher; Auswege [18, 27]
    von Polchinski [30] kritisiert; Regularisierung von P(alpha) aendert bevorzugte Werte [37].
  - Lorentzische Neudeutung (Kawai/Okada u. a. [118-121]): Dichtematrix peakt bei Lambda = 0 nur potenzartig, mit
    IR-Abschneider z_IR [S, S. 22].
  - AdS/CFT [S, Abschn. 5.7]: Wurmloecher kollidieren mit Cluster-Zerlegung der Randtheorie (Faktorisierung).
- **F2, Erwartung 08:10:54 (date):** arXiv-API id_list (19 IDs, nur Abstracts). Erwartet je Abstract:
  - Marolf/Maxfield 2002.08950: Baby-Universum-Hilbertraum, alpha-Zustaende als Superauswahlsektoren, Ensemble.
  - McNamara/Vafa 2004.06738: In holographischer/String-Quantengravitation ist der BU-Hilbertraum eindimensional.
  - Hertog/Truijen/Van Riet 1811.12690: Axion-Wurmloecher haben mehrere negative Moden.
  - Loges/Shiu/Sudhir 2203.01956: Mit passenden Randbedingungen (Fluss fest) keine negativen Moden, stabil.
  - Alonso/Urbano 1706.07415: Wurmloecher geben Goldstone-Massen; keine negativen Moden.
  - AJJK hep-th/9303041: 4D-Baby-Universen gezaehlt, Suszeptibilitaetsexponent gamma.
  - Jain/Mathur hep-th/9204017: Minimalhals-Baby-Universen in 2D.
  - Ambjorn/Loll hep-th/9805108: Lorentzisches 2D-Modell ohne Topologiewechsel, andere Universalitaetsklasse.
  - Jordan/Loll 1305.4582: CDT ohne bevorzugte Blaetterung, gleiche Ergebnisse in 3D.
  - Laiho u. a. 1604.02745 und Bassler u. a. 2103.06973: EDT mit Massterm gibt de-Sitter-artige Phase.
  - Ambjorn/Glaser/Goerlich/Jurkiewicz 1307.2270: kein neues Phasenverhalten mit Massterm (Gegenposition).
  - Kawai/Okada 1110.2303: Lorentzisches Multiversum mit Baby-Universen, Feinabstimmung.
  - Usatyuk/Wang/Zhao 2402.00098 und Harlow/Usatyuk/Zhao 2501.02359: Hilbertraum geschlossener Universen eindimensional.
  - AJL hep-th/0505154: raeumliche Schnitte fraktal (d_s ~ 1,5?).
  - Ambjorn/Budd 1302.1763: raeumlicher Topologiewechsel in 2D-CDT gibt Baumstruktur.
  - ALWZ 0709.2784: verallgemeinerte CDT, Kausalitaetsverletzung begrenzt.
  - Einzelne IDs koennen falsch sein; dann steht ein anderer Titel da (Pruefung je Eintrag).
- **F2, Ausgang 08:12:12 (date):** alle 18 IDs mit passendem Titel (quellen/F2-arxiv-idlist-20261005-081110.xml).
  Bestaetigt (je eine Zeile):
  - Marolf/Maxfield: wie erwartet; dazu Nullzustaende, Dimension des AdS-Hilbertraums als Zufallsgroesse Z.
  - Hertog/Truijen/Van Riet: mehrere negative Moden am Hals; "not relevant saddle points".
  - Loges/Shiu/Sudhir: "in the 3-form picture ... perturbatively stable Euclidean saddle" -> Bild entscheidet (BU5).
  - Alonso/Urbano: quadratische Wirkung "only positive eigenvalues".
  - AJJK 1993: Baby-Universen zaehlen -> Exponent gamma. Jain/Mathur 1992: selbstaehnliche Baby-Universen,
    Halsdicke ~ UV-Abschneider, groesstes ~ A^(1/(1-gamma)).
  - Ambjorn/Loll 1998: 2D exakt; mit Topologiewechsel der Schnitte ("baby universe creation") -> Liouville.
  - ALWZ 2007, Ambjorn/Budd 2013: GCDT exakt loesbar; Baumbijektion.
  - Jordan/Loll 2013: Blaetterung nicht noetig, Kausalitaet ja (3D, numerisch).
  - AJL 2005: "fractal structure of slices of constant time" (raeumliche Schnitte; stuetzt L1).
  - Usatyuk/Wang/Zhao 2024, Harlow/Usatyuk/Zhao 2025: geschlossenes Universum nichtperturbativ eindimensional.
  **Verstoesse (Analysezyklus):**
  - **V-F2a McNamara/Vafa:** nicht "in holographischer QG", sondern "in a consistent theory of quantum gravity", begruendet
    mit Swampland-Bedingungen; "Gauss's law for entropy"; Ausnahmen d <= 3 (JT als Brane). Coleman wird im Abstract nicht
    genannt -> "also kein Coleman-Mechanismus" ist bisher mein Schluss [ES], nicht ihr Satz. Pruefung am Volltext (Plan F8).
  - **V-F2b Laiho u. a. 2017:** EDT mit fein abgestimmtem Massterm: 4D-semiklassisch, und "a cosmological constant that is
    naturally small in the infrared" (RG-Lauf). Bassler u. a. 2021: de-Sitter-(Hawking-Moss-)Instanton aus EDT, ohne
    Kausalitaet. Gegenposition AGGJ 2013: kein Punkt 2. Ordnung, "crinkled phase" ohne Kontinuumsdeutung. -> BU3-Teil
    "erst mit Kausalitaet de Sitter" ist umstritten; Moderator: Massterm plus Feinabstimmung. Lambda-Bezug neu (Glied 10).
  - **V-F2c Kawai/Okada 2011:** Baby-Universen im lorentzischen Multiversum sagen eine Zahl vorher: Higgs-Masse 140 +- 20 GeV
    und theta = 0. Gemessen 125 GeV [L] -> im Band, aber schwach. Ich hatte keine Datenvorhersage aus dem Strang erwartet.
- **F3, Erwartung 08:12:38 (date):** INSPIRE-API, 11 Zeitschriftenstellen (Coleman NPB 310/643 und 307/867, GS NPB 307/854
  und 306/890, Hawking PRD 37/904 und PLB 134/403, Fischler/Susskind PLB 217/48, Polchinski PLB 219/251, Unruh PRD 40/1053,
  Ng/van Dam PRL 65/1972, Rubakov/Shvedov PLB 383/258). Erwartet: die meisten Datensaetze da, Abstracts nur bei einem Teil.
  Inhalt: Coleman: Wurmloecher -> Lambda = 0 mit Wahrscheinlichkeit nahe 1; Hawking 1984: "probably zero"; Ng/van Dam:
  unimodular plus Baum/Hawking -> Lambda = 0 (Bruecke zu Glied 10); Unruh: unimodular, Lambda als Integrationskonstante
  mit Wurmlochbezug; Polchinski: "excluded volume" scheitert; Rubakov/Shvedov: eine negative Mode.
- **F3, Ausgang 08:13:09 (date):** 11 von 11 Datensaetzen mit Abstract (quellen/F3-inspire-klassiker-20261005-081249.json).
  Bestaetigt (je eine Zeile):
  - Coleman 1988 (NPB 310): "if wormholes exist, they have the effect of making the cosmological constant vanish";
    Naeherungen nur an der Wurmloch-Skala, darunter exakt in allen Wechselwirkungen (985 Zitate).
  - Coleman 1988 (NPB 307): kein beobachtbarer Kohaerenzverlust. GS 1988 (NPB 307): Messfolge kollabiert in kohaerente
    (alpha-)Zustaende; alle Kopplungen haengen vom Zustand ab; globale Symmetrien generisch verletzt.
  - GS 1988 (NPB 306): Axion "described by a rank-three antisymmetric tensor field strength" -> Original im 3-Form-Bild.
  - Hawking 1984: "zero is by far the most probable value", Mechanismus "three-index antisymmetric tensor field" oder
    topologische Fluktuationen. Hawking 1988: Abzweigen geschlossener Universen -> gemischter Endzustand.
  - Fischler/Susskind 1989: grosse Wurmloecher "with maximal density". Rubakov/Shvedov 1996: negative Mode, Beitrag
    "purely imaginary", Deutung als Instabilitaet gegen Abgabe von Baby-Universen.
  - Ng/van Dam 1990: unimodular, Lambda Integrationskonstante, Integration ueber Lambda im euklidischen Pfadintegral ->
    Lambda = 0 dominiert; "the two approaches are logically different". -> Bruecke zu Glied 10 an der Quelle.
  **Verstoesse:**
  - **V-F3a Polchinski 1989 (PLB 219, 251) ist nicht die "excluded volume"-Arbeit, sondern "The phase of the sum over
    spheres":** Phase (-i)^(d+2); Colemans Loesung "can work, in its present form, only in dimension d = 2 mod 4".
    -> In d = 4 scheitert die Form des Arguments schon an der Phase. Staerker als erwartet; schaerft BU1.
  - **V-F3b Unruh 1989:** Wurmloecher fuehren doch zu Kohaerenzverlust und "completely destroys the Euclidean quantum
    theory" (nichtlokale, "violently unbounded" Wirkung). Ich hatte Unruh als Unimodular-Arbeit erwartet; hier ist er
    ein Einwand gegen Coleman.
  - Hinweis (aus Hawking 1984 abgeleitet, [L]): Die "three-index"-Variante ist eine 4-Form, Hodge-dual zu einer Zahl;
    Duff 1989 ("The cosmological constant is possibly zero, but the proof is probably wrong", PLB 226, 36) [L] soll ein
    Vorzeichen bei dieser Dualisierung gefunden haben. -> Pruefen (Plan: INSPIRE in einem Sammelabruf). Waere ein
    zweiter Hodge-Bezug neben den Axion-Wurmloechern.
- **F4, Erwartung 08:13:34 (date):** arXiv-API, Abstracts mit wormhole UND axion UND (negative/stability/stable/
  perturbation), neueste zuerst, 25 Treffer. Erwartet: 2024-2026 mehrere Arbeiten (Hertog/Van-Riet-Gruppe,
  Jonas/Lavrelashvili/Lehners, Loges/Shiu); Stabilitaet weiter strittig; Randbedingungen (Fluss fest = 3-Form-Bild
  gegen Axion fest) als Moderator; keine Einigung.
- **F4, Ausgang 08:14:11 (date): Erwartung VERLETZT (wichtigster Fund bisher).** 32 Treffer, 25 gelesen
  (quellen/F4-arxiv-axion-wurmloch-stabil-20261005-081342.xml).
  - **Hertog/Maenaut/Missoni/Tielemans 2024 (2405.02072) [S Abstract]:** Stabilitaetsanalyse mit dem Axion als
    Zwei-Form-Eichfeld ist "equivalent to one performed in the Hodge-dual formulation" (Skalar mit falschem Vorzeichen);
    beide Analysen zeigen perturbative Stabilitaet, auch mit Saxion. Dieselbe Gruppe hatte 2018 mehrere negative Moden
    gefunden (1811.12690).
  - **Marolf/Missoni 2025 (2505.21118):** Divergenzen symmetrischer Moden waren ein Artefakt; deren Wirkung positiv;
    fruehere Stabilitaetsaussagen bleiben. **Loveridge/Sun 2025 (2504.10868):** "Recent work has demonstrated that
    Euclidean Giddings-Strominger axion wormholes are stable" (4D flach); AdS3 ebenfalls stabil.
  - **Di Ubaldo/Iliesiu/Lin/Yan 2026 (2605.05305):** Positivitaet der Skalarprodukte plus perturbativ stabile Wurmloecher
    -> nichtperturbative Instabilitaet noetig, die die Shift-Symmetrie bricht -> scharfe axionische WGC mit Zahlen.
  - **Held/Kaplan/Marolf/Wang 2026 (2601.02507):** Relevanz des Wurmloch-Sattels fuer das Faktorisierungsproblem haengt an
    der Kontur; fuer reelles positives chi_E liegt der Sattel auf einer Stokes-Linie, "a matter of choice".
  - Jonas/Lavrelashvili/Lehners 2023: masselose Axion-Dilaton-Wurmloecher stabil; Zweige ab Verzweigungspunkt mit
    negativer Mode. Lavrelashvili/Lehners 2026: Null-Ladungs-Grenze = No-Boundary-Instanton (Hals schnuert ab).
  - **Korrektur der Erwartung (protokolliert):** Nicht "Stabilitaet weiter strittig", sondern: Die perturbative
    Stabilitaet gilt im 24-Monats-Fenster als gezeigt (drei Gruppen), und die Hodge-Dualitaet ist das Werkzeug, mit dem die
    Gleichwertigkeit beider Bilder gezeigt wurde. Strittig ist jetzt die **Relevanz** (Kontur, Stokes-Linien, UV-Vollendung,
    WGC), nicht die Stabilitaet. -> BU5 Teil 2 verfehlt (vorlaeufig; Gegensuche nach 2025/26-Dissens folgt im Gegensweep).
- **F5, Erwartung 08:14:35 (date):** arXiv-API, Abstracts mit Coleman UND (wormhole(s) / baby universe(s)), neueste
  zuerst, 25 Treffer. Erwartet: im 24-Monats-Fenster 2 bis 6 Arbeiten, die Colemans Mechanismus neu deuten (lorentzisch,
  JT, alpha-Zustaende, unimodular); keine zeigt ihn als gueltige Loesung des Lambda-Problems; eher Varianten mit
  Feinabstimmungs-Anspruch (Kawai-Linie) oder Kritik.
- **F5, Ausgang 08:15:31 (date): Anzahl im Fenster bestaetigt (eine Arbeit), Inhalt teils VERLETZT** (Analysezyklus).
  27 Treffer (quellen/F5-arxiv-coleman-wurmloch-20261005-081444.xml).
  - Im 24-Monats-Fenster nur **McNamara/Wang 2026 (2607.01322)**: Rekonstruktionssatz fuer QFT (unitaere QFTs durch
    Partitionsfunktionen geschlossener Mannigfaltigkeiten bestimmt; jede reflexionspositive Partitionsfunktion stammt
    aus einer unitaeren QFT); gravitativ gedeutet: scheinbarer Bruch der Hilbertraum-Faktorisierung ist "a red herring".
    Satz [M] im QFT-Teil; die Gravitationsdeutung ist Heuristik. Kein Lambda-Bezug.
  - **V-F5a (Regime-Bruecke, nicht erwartet): Hamada/Kawai/Kawana 2022 (2210.05134):** 2D euklidische QG (c <= 1),
    direktes Zaehlen der Zufallsflaechen aller Topologien: Baby-Universen "too small to realize the Coleman mechanism".
    4D lorentzisch mit nicht-hermiteschem Hamilton: Coleman erfuellt, Lambda fast null. -> **Dieselbe Aussage gilt im zaehlbaren 2D-Regime nicht**, im 4D-Modell nur mit Zusatzannahme.
  - **V-F5b (gegen BU3-Lesart): Loll/Westra/Zohren 2005/2006 (hep-th/0507012, hep-th/0603079):** 2D-CDT MIT Summe ueber
    Topologien (infinitesimale Wurmloecher), exakt per Doppelskalierung: Lambda_eff sinkt, "reminiscent of the
    suppression mechanism considered by Coleman"; endliche Dichte mikroskopischer Wurmloecher; Bedingung sind geeignete
    Kausalitaetsschranken. -> CDT verbietet Topologiewechsel nicht grundsaetzlich; kausal
    eingeschraenkte Wurmloecher sind rechenbar und senken Lambda_eff (Rechnung im 2D-Modell).
  - **V-F5c Ambjorn/Sato/Watabiki 2021 (2101.00478):** 2D, Summe ueber alle Wurmlochkonfigurationen -> eine Art
    Coleman-Mechanismus, bei dem Lambda fuer grosse Universen keine Rolle spielt; Beobachter deuten das als
    "fluctuating cosmological constant". -> Bezug Glied 10 (everpresent-artige Schwankung aus Topologie). [H]
  - Blommaert/Iliesiu/Kruthoff 2022: alpha-Zustaende in JT konkret gebaut; Nullzustaende muessen herausgeteilt werden;
    Ensemble-Mittel <-> Wurmloecher konkret verknuepft.
  - D'Agnolo/Mangini/Rigo 2024 (April, knapp ausserhalb 24 Monate): Baby-Universen durch Aufwaerts-Tunneln in ewiger
    Inflation; Multiversum erklaert Lambda und Schwache Skala (anthropisch, nicht Coleman).
- **F6, Erwartung 08:15:56 (date):** arXiv-API, Abstracts mit dynamical triangulation(s) UND (baby / branched polymer(s)
  / minimal neck / measure term), neueste zuerst, 30 Treffer. Erwartet: im Fenster 2 bis 5 Arbeiten (EDT mit Massterm
  von der Laiho-Gruppe; CDT-Phasenstruktur), keine neue Aussage, dass CDT Baby-Universen enthaelt; der
  EDT-de-Sitter-Anspruch bleibt umstritten; 3D-Minimalhals-Definition evtl. in alten Treffern.
- **F6, Ausgang 08:16:43 (date): teils bestaetigt, ein harter VERSTOSS** (quellen/F6-arxiv-dt-baby-polymer-20261005-081606.xml,
  30 Treffer).
  - **V-F6a (gegen BU3 "CDT verbietet sie"): Ambjorn/Jurkiewicz/Loll 2002 (hep-lat/0201013), 3D-Lorentz-DT (= 3D-CDT)
    [S Abstract]:** zwei Phasen; schwache Kopplung semiklassisch, starke Kopplung: "'classical' space disintegrates into a
    foam of baby universes." -> Auch in CDT gibt es eine Phase aus (raeumlichen) Baby-Universen. Zusammen mit L1 (Loll
    2019) und V-F5b: Kausalitaet verbietet nur das Verzweigen in der Zeit.
  - **Bestaetigt (BU4 Teil 2): Egawa/Tsuda/Yukawa 1997/1998 (hep-lat/9709099, hep-lat/9802010):** MINBU-Analyse in 3D-DT
    mit S^3-Topologie; gamma_st(3) ~ gamma_st(4) ~ 0 am kritischen Punkt; gemeinsame Skalierung der Minbu-Verteilung in
    3D und 4D in der Starkkopplungs-(Knaeuel-)Naehe. -> Minimale Haelse sind in 3D-DT definiert und gemessen.
  - Catterall/Kogut/Renken/Thorleifsson 1995 (hep-lat/9509004): Baby-Universen auch in der **Knaeuel**phase von 4D-DT
    gemessen (nicht nur in der Polymerphase); Daten vertraeglich mit exponentieller Schranke.
  - **Im 24-Monats-Fenster nur Budd/Nemeth 2025 (2507.01604):** 3D-DT mit zwei aufspannenden Baeumen; neue
    "triple-tree phase" neben Knaeuel- und Polymerphase; Hinweise, dass der Uebergang Polymer -> triple-tree stetig ist.
    -> 3D-Phasenstruktur ist reicher als "Knaeuel oder Polymer" (betrifft BU4 Teil 3).
  - Asaduzzaman/Catterall 2022 (2207.12642): EDT mit Massterm: Linie 1. Ordnung, latente Waerme sinkt fuer kappa -> oo,
    D_H -> 4, D_s ~ 3/2 kurz; "broadly in agreement" mit frueheren EDT-Arbeiten (stuetzt Laiho-Linie, ohne Entscheidung).
  - Ambjorn/Anagnostopoulos/Loll 1999 (hep-lat/9909129): Belege, dass die KPZ-Exponenten der 2D-euklidischen QG
    "entirely due to the presence of baby universes" sind -> messbarer Unterschied der Regime im Modell (Exponenten).
  - Ambjorn/Barkley/Budd 2011: Jain/Mathur-Vermutung zur Skalierung von Haelsen auf Geschlecht-g-Flaechen verbessert.
  - Noch offen fuer BU3 Teil 1: Quelle, die die Polymerphase ausdruecklich als Baum aus Baby-Universen beschreibt
    (AGJL Fn. 20 sagt nur "tree graph"). -> Plan: Volltext AJJK 1993 oder Ambjorn/Jurkiewicz 1995.
- **F7, Erwartung 08:17:08 (date):** Volltext McNamara/Vafa 2020 (arXiv-PDF 2004.06738). Erwartet: Sie nennen Colemans
  alpha-Parameter; mit eindimensionalem BU-Hilbertraum sind die alpha festgelegt, Kopplungen nicht zufaellig, kein
  Ensemble. Den Lambda-Mechanismus nennen sie hoechstens am Rand (eher gar nicht). Begruendung ueber Swampland
  (keine globalen Symmetrien, Vollstaendigkeit, Cobordismus-Vermutung) und Eichredundanz zwischen Topologien.
- **F7, Ausgang 08:17:36 (date): bestaetigt, mit zwei Praezisierungen** (quellen/F7-arxiv-2004.06738-mcnamara-vafa-20261005-081717.pdf/.txt).
  - Sinngemaess [S, S. 3]: Baby Universe Hypothesis: fuer unitaere QG in d > 3 gilt dim H_BU = 1. Einziger eichinvarianter Zustand =
    Hartle-Hawking-Wellenfunktion. Status: **Hypothese als Swampland-Bedingung**, kein Satz.
  - Begruendung [S, Abschn. 3.2]: alpha-Parameter definieren eine globale (-1)-Form-Symmetrie und sind freie Parameter;
    beides verbietet das Swampland-Programm in d > 3; Cobordismus-Trivialitaet verbietet Superauswahlsektoren im endlichen
    Raum.
  - **Praezisierung 1 (gegen BU2-Wortlaut):** nicht "holographische QG", sondern jede unitaere QG in d > 3; Holographie ist
    Motivation (Ensemble nur d = 2, evtl. 3; JT als Brane-Weltvolumen).
  - **Praezisierung 2:** "cosmological" kommt im Volltext 0-mal vor (grep 08:17). "Also kein Coleman-Mechanismus" ist
    nicht ihr Satz, sondern ableitbar [ES]: ohne alpha-Verteilung nichts, worauf Colemans Mass P(alpha) wirken koennte.
  - **Hodge-Fund (nicht erwartet):** Gl. (9)-(10): Ein freier Parameter lambda koppelt an eine Top-Form L_lambda; der
    erhaltene 0-Form-Strom ist J_lambda = *L_lambda (Hodge-Stern). Fuer Lambda ist L = Volumenform. -> Dritter
    Hodge-Bezug neben Axion<->2-Form (HMS Gl. 7-8) und Lambda<->4-Form-Fluss (Hawking 1984). [ES]
- **F8, Erwartung 08:18:03 (date):** arXiv-API, Abstracts mit "baby universe(s)" UND (Hilbert space / one-dimensional /
  alpha), neueste zuerst, 30 Treffer. Erwartet: 2024-2026 viele Arbeiten; Mehrheit stuetzt "eindimensional" fuer
  geschlossene Universen (UWZ, HUZ, Folgearbeiten), daneben Gegenstimmen bzw. Einschraenkungen (Beobachter, de Sitter,
  nichttriviale alpha in 2D-Modellen; Engelhardt/Gesteau "against a semiclassical baby universe"?). Kein Beweis fuer d = 4.
- **F8, Ausgang 08:18:41 (date): bestaetigt, ein Moderator-Fund (Analysezyklus)** (quellen/F8-arxiv-bu-hilbertraum-20261005-081814.xml,
  37 Treffer; Engelhardt/Gesteau nicht unter den 30 neuesten, nicht weiter gesucht).
  - Mehrheit im Fenster: geschlossenes Universum nichtperturbativ eindimensional, "within each superselection sector"
    bzw. "for each alpha-sector" (Nomura/Ugajin 2025, 2026); Vorhersagen ueber Teilbeobachtbarkeit.
  - Gegen- bzw. Einschraenkung: Abdalla/Antonini/Iliesiu 2025: mit Beobachter "not one-dimensional", Dimension ~
    exp(1/G_N); HUZ 2025: Beobachter-Hilbertraum ~ e^(S_Ob). Kumar 2026: Folgen haengen daran, ob H_BU eindimensional ist.
  - Di Ubaldo/Iliesiu/Lin 2026 (2609.16113): notwendige und hinreichende Bedingungen, wann das Pfadintegral ein
    Skalarprodukt bzw. ein statistisches Mittel ist; Positivitaet beschraenkt Wurmloch-Amplituden (Bootstrap).
  - **V-F8a (Moderator, Glied 10): Gielen 2026 (2606.17163) [S Abstract]:** geschlossenes Minisuperraum-Universum; die
    Potentialenergie ist Integrationskonstante, "equivalent to the cosmological constant as it appears in unimodular
    gravity". Konstante fest -> physikalischer Hilbertraum eindimensional; Konstante frei -> unendlichdimensional
    (Energieeigenzustaende). -> Ob der Hilbertraum eines geschlossenen Universums eindimensional ist, haengt daran, ob
    Lambda fest oder (unimodulare) Integrationskonstante ist. Das ist genau unser Glied-10-Bruch. [ES]
- **F9, Erwartung 08:19:04 (date):** INSPIRE-Sammelabruf (Duff PLB 226/36; Henneaux/Teitelboim PLB 222/195;
  Brown/Teitelboim PLB 195/177 und NPB 297/787; Ambjorn/Varsted NPB 373/557; Agishtein/Migdal MPLA 6/1863;
  Boulatov/Krzywicki MPLA 6/3005; Polchinski NPB 325/619; Banks NPB 309/493; Klebanov/Susskind/Banks NPB 317/665).
  Erwartet: Duff: Hawkings 4-Form-Argument hat ein Vorzeichenproblem (richtig behandelt kehrt sich der Peak um).
  Henneaux/Teitelboim: Lambda konjugiert zur kosmischen Zeit (4-Volumen). Brown/Teitelboim: Membranen neutralisieren
  Lambda ueber 4-Form-Fluss. 3D-DT: zwei Phasen (heiss/knaeuel gegen kalt/gestreckt), Uebergang 1. Ordnung (spaetestens
  Boulatov/Krzywicki). Polchinski NPB 325: "excluded volume" rettet nicht. Abstracts nicht bei allen.
- **F9, Ausgang 08:19:41 (date): bestaetigt, zwei Datenbezuege neu** (quellen/F9-inspire-duff-ht-3ddt-20261005-081916.json,
  10 von 10 mit Abstract).
  - Bestaetigt: **Duff 1989** [S Abstract]: Einsetzen in die Wirkung und Variieren ist nicht dasselbe wie Einsetzen in die
    Feldgleichungen; beim Tensorpotential vom Rang drei unterscheiden sich Wirkungskoeffizient und gemessenes Lambda im
    Vorzeichen; Hawkings Beweis damit ungueltig, und es "casts doubt on similar attempts". -> Hodge-dualer 4-Form-Sektor
    kippt das Vorzeichen; trifft Hawking 1984 direkt, Coleman indirekt.
  - Bestaetigt: Henneaux/Teitelboim 1989: Lambda Integrationskonstante; globaler Mode "cosmic time canonically conjugate
    to the cosmological constant". Polchinski NPB 325: KFS-Katastrophe bleibt, Coleman/Lee-Ausweg kritisiert.
    Brown/Teitelboim 1987/88: Membranbildung senkt Lambda schrittweise (4-Form-Fluss).
  - Bestaetigt (3D-DT): Ambjorn/Varsted 1992: Uebergang von "crumpled, of essentially zero radius" zu ausgedehnten
    Objekten; Boulatov/Krzywicki 1991: Entropie sichert ein Vakuum "in spite of the Einstein action being bottomless".
    Agishtein/Migdal 1991 (fruehe Daten): keine "collapse to the branched polymer phase" bis 60000 Tetraeder.
  - **V-F9a (Daten): Klebanov/Susskind/Banks 1989:** Colemans Argument fuer andere Parameter "applied to the mass of the
    pion. A discouraging result is found that the pion mass is driven to zero." -> Gegen Messung (Pionmasse > 0) [L].
  - **V-F9b (Daten): Banks 1988:** Bifurkierende Universen bestimmen Lambda bei starker Inflation als "negative and very
    small". -> Vorzeichen gegen die Beobachtung Lambda > 0 [L].
  - [ES] Damit hat der euklidische Strang mindestens drei Datenkontakte: Lambda = 0 exakt (Coleman) gegen Lambda > 0;
    m_pi -> 0 (KSB) gegen m_pi > 0; Lambda < 0 (Banks) gegen Lambda > 0. Plus Kawai/Okada Higgs 140 +- 20 GeV (im Band).
- **F10, Erwartung 08:20:01 (date):** arXiv-API, Abstracts mit "Hodge conjecture" UND (gravity / wormhole(s) / baby
  universe / flux / vacua / string), neueste zuerst. Erwartet: einige Treffer aus Stringkompaktifizierung (Hodge-Loci,
  Fluss-Vakua, Endlichkeit, Swampland; Grimm-Umfeld), keiner zu Baby-Universen oder Wurmloechern. Dann gilt fuer die
  Hodge-Vermutung: kein Baby-Universum-Bezug nach Recherchestand; ein indirekter Lambda-Bezug ueber die Landschaft.
- **F10, Ausgang 08:20:19 (date): bestaetigt** (quellen/F10-arxiv-hodge-vermutung-physik-20261005-082012.xml). Ein
  einziger Treffer (alle Jahre): Grimm 2020 (2010.15838): Endlichkeit selbstdualer Fluss-Vakua; "a striking connection of
  the finiteness result for supersymmetric flux vacua and the Hodge conjecture". Kein Treffer zu Wurmloechern oder
  Baby-Universen (die 2 grep-Treffer sind der Suchstring). -> Hodge-Vermutung beruehrt Lambda nur ueber die
  Stringlandschaft (Zahl der Vakua), nicht ueber Baby-Universen. Nach Recherchestand kein Bezug.
- **Herleitung D1 [M], ~~08:21~~ (geschaetzt; berichtigt: zwischen den date-Messungen 08:20:19 und 08:23:06)
  (Schreibtisch, kein Abruf): 2-3-Zuege erzeugen keine minimalen Haelse.**
  - Minimaler Hals (3D) = vier Dreiecke pqr, pqs, prs, qrs vorhanden, Tetraeder pqrs fehlt.
  - 2-3-Zug: abcd + abce -> abde, bcde, acde; neu sind Kante de und Dreiecke ade, bde, cde; entfernt wird nur abc.
  - Enthaelt eine Schale ein neues Dreieck, etwa ade, so braucht sie ein zweites Dreieck mit Kante de, also bde oder cde;
    dann ist ihr Tetraeder abde bzw. acde vorhanden -> kein Hals.
  - Enthaelt sie kein neues Dreieck, existierten alle vier Dreiecke vorher. Fehlte ihr Tetraeder vorher, war sie schon ein
    Hals. War es vorhanden, ist es abcd oder abce, dann gehoert abc zur Schale und wurde entfernt -> keine Schale mehr.
  - **Also: Unter 2-3-Zuegen nimmt die Zahl minimaler Haelse nie zu.** Ein 3-2-Zug kann einen erzeugen (Beispiel: Ecke p
    mit Doppelpyramiden-Umgebung, 3-2 an Kante px -> p hat nur noch 4 Tetraeder; Schale abcy umschliesst p).
  - Folge fuer UMKLAPP-1 [M, P]: Die Netze mit f = 0,2 (nur 2-3-Zuege) haben hoechstens so viele Haelse wie ihre
    Delaunay-Ausgangsnetze. Die gefundene Instabilitaet ist also kein Minimalhals-Baby-Universum-Effekt, sofern die
    Ausgangsnetze keine Haelse hatten (nicht gezaehlt).
- **F11, Erwartung 08:23:06 (date):** arXiv-API, Abstracts mit (baby universe(s) / alpha parameters / wormhole(s)) UND
  (cosmological constant / dark energy), neueste zuerst, 30 Treffer (Regel 7 fuer BU1 ohne das Stichwort Coleman).
  Erwartet: im 24-Monats-Fenster 3 bis 8 Treffer; Lorentz-/Multiversum-Varianten (Kawai-Umfeld), de-Sitter-Wurmloecher,
  ggf. dunkle Energie aus Wurmloechern; keine Arbeit, die Lambda -> 0 (oder den beobachteten Wert) als gezeigt ansieht.
- **F11, Ausgang 08:23:24 (date): Anzahl bestaetigt, Inhalt VERLETZT (Datenkontakt, Analysezyklus)**
  (quellen/F11-arxiv-bu-lambda-20261005-082317.xml, 21 Treffer).
  - **V-F11a: Ambjorn/Watabiki-Linie (CDT-Gruender!)**: 2017 (1709.06497): W3-Modell mit Baby-Universen und Wurmloechern,
    exponentielle Expansion ohne Lambda, "predicts that w = -1.2" (4D, vereinfachende Annahmen). 2024 (2401.06931):
    Absorption von Baby-Universen -> modifizierte Friedmann-Gleichung, Beschleunigung ohne Lambda, bevorzugt lokales H0.
    **2026 (2605.15045, im Fenster):** dasselbe Modell, w(z) < -1 fuer genuegend grosses z (Bezug DESI-z-Abhaengigkeit).
  - **Datentest Muralidharan/Cline 2024 (2408.13306, 23.08.2024, knapp 2 Monate vor dem Fenster) [S Abstract]:** Planck +
    DESI 2024 + weitere: "the pure baby universe model gives a poor fit to current data". Mit Lambda dazu zwei erlaubte
    Gebiete: nahe LCDM, oder Lambda < 0 plus exotische Komponente; je nach SN-Datensatz deutlich besser als LCDM;
    Hubble-Spannung bis 2 sigma gemildert; w(a) mit Polsingularitaet frueh.
  - Trivedi/Khlopov 2024: keine Rips/Singularitaeten im Verschmelzungsmodell (theoretisch).
  - **Korrektur der Erwartung:** Es gibt einen Baby-Universum-Strang mit Daten (DESI, Planck, SN), aber nicht Coleman,
    sondern Absorption (Verschmelzung) als dunkle Energie. Fuer Glied 10 [P] ist das ein vierter Weg zu Lambda_eff(z)
    (neben unimodularer Diffusion, wechselwirkendem Vakuum, everpresent Lambda). Regel 6: gemeinsame Groesse w(z) bzw.
    die Austauschrate. [ES]
  - Kein Treffer im Fenster, der Colemans Lambda -> 0 als gezeigt ansieht (Regel 7 fuer BU1 erfuellt, zusammen mit F5).
- **F12, Erwartung 08:24:16 (date):** arXiv-API, Abstracts mit "causal dynamical triangulation(s)" UND (topology /
  baby / branching / wormhole), neueste zuerst, 25 Treffer (Regel 7 fuer BU3, Gegensweep CDT). Erwartet: im Fenster 1
  bis 4 Arbeiten (Topologie der Schnitte, Torus-CDT, raeumlicher Topologiewechsel in 2D/3D); keine 4D-Arbeit, die
  zeitliches Verzweigen in CDT zulaesst und trotzdem de Sitter findet.
- **F12, Ausgang 08:24:34 (date): bestaetigt** (quellen/F12-arxiv-cdt-topologie-20261005-082426.xml, 48 Treffer, 25 gelesen).
  Im Fenster: Fuji/Manabe/Watabiki 2025 (2D: multikritische DT "lacks a causal time direction", CDT "possesses";
  topologische Rekursion loest beide), Barouki/Laurenzano 2025 (Ising auf CDT), Clemente/D'Elia/Nemeth 2024 (Yang-Mills-
  Topologie). Keine 4D-CDT-Arbeit mit zeitlichem Verzweigen. Davor: AGG 2022 (Ordnung des Uebergangs haengt an der
  Raumzeittopologie, 3-Torus), Brunekreef/Nemeth 2022 (3D-CDT: hoeheres raeumliches Geschlecht und gelockerte
  Mannigfaltigkeitsbedingungen aendern Phasenstruktur nicht), Ambjorn/Hiraga/Ito 2021 (2D: Wurmloch-Wechselwirkung =
  Spalten/Verbinden in der CDT-Stringfeldtheorie).
- **F13, Erwartung 08:24:41 (date):** arXiv-API id_list math/9911256 (Lickorish), hep-th/9503006 (Ambjorn/Jurkiewicz
  1995), hep-lat/9809131 (Thorleifsson 1998). Erwartet: Lickorish nennt Pachners Satz (geschlossene PL-Mannigfaltigkeiten
  PL-homoeomorph genau dann, wenn durch endlich viele bistellare Zuege verbunden); AJ 1995: gamma aus Minbu-Verteilung,
  gestreckte Phase gamma ~ 1/2 (verzweigte Polymere); Thorleifsson: Uebersicht DT inkl. Baby-Universen.
- **F13, Ausgang 08:25:02 (date): bestaetigt, eine Abweichung** (quellen/F13-arxiv-idlist-pachner-minbu-20261005-082454.xml).
  - Lickorish 1999 [S Abstract]: Beweise nach Pachner; Zuege aus einer endlichen Sammlung genuegen, um zwei
    Triangulierungen einer PL-Mannigfaltigkeit zu verbinden. -> Gegensweep G1 bestaetigt: Pachner-Zuege verbinden genau die
    Triangulierungen derselben PL-Mannigfaltigkeit; sie aendern die Topologie nicht [S + M].
  - AJ 1995 [S Abstract]: gestreckte Phase (grosses kappa0): innere Hausdorff-Dimension zwei, Kontinuum "branched
    polymers"; Knaeuel (kleines kappa0): Dimension "seems to be infinite"; Algorithmus "baby universe surgery".
    **Abweichung:** 1995 hiess es "the transition is continuous"; spaeter 1. Ordnung (AGJL Fn. 19, lokal L2).
  - Thorleifsson 1998: Abstract ohne Baby-Universen; nicht weiter genutzt.
  - BU3 Teil 1 ("Polymerphase von Baby-Universen beherrscht") an der Quelle bisher nur indirekt: Baum (AGJL Fn. 20),
    d_H = 2 (AJ 1995), 2D-Rauigkeit = selbstaehnliche Baby-Universen (Jain/Mathur). Ausdruecklicher Satz fehlt noch.
- **F14, Erwartung 08:25:21 (date):** Volltext Egawa/Tsuda/Yukawa 1997 (hep-lat/9709099, PDF). Erwartet: 3D-Minbu als
  geschlossene Flaeche aus 4 Dreiecken (Rand eines Tetraeders), die selbst kein Tetraeder des Netzes ist und das Netz in
  zwei Teile trennt; in 4D entsprechend 5 Tetraeder. Dazu: Minbu-Verteilung n(B) ~ B^(gamma-2); in der gestreckten Phase
  gamma ~ 1/2 (Baum aus Baby-Universen).
- **F14, Ausgang 08:25:41 (date): teilweise VERLETZT** (quellen/F14-arxiv-hep-lat-9709099-egawa-20261005-082530.pdf/.txt,
  3 Seiten Proceedings).
  - Keine Definition im Text; Verweis auf Jain/Mathur [4] ("standard MINBU algorithm"). Die 4-Dreiecke-Definition bleibt
    [L] (Gedaechtnis), an keiner Quelle gelesen.
  - Bestaetigt: 3D-DT (S^3, N3 = 16K, kappa0 = 4,09, kappa3 = 2,20, Wirkung kappa3 N3 - kappa1 N1) Minbu-Verteilungen
    gemessen, gamma_st(3) ~ 0 nahe dem kritischen Punkt (Starkkopplungsseite); 4D ebenso ~ 0.
  - Kein Satz zur Polymerphase. -> BU3 Teil 1 bleibt indirekt belegt.
- Lokal (kein Abruf, 08:25:58): Alvey/Escudero 2020 (2009.03917, aus F4-Datei) [S Abstract]: Wurmloecher brechen globale
  Symmetrien; "the axion has a quality problem within non-perturbative Einstein gravity". -> Datenkontakt ueber die
  Strong-CP-Schranke (Neutronen-EDM, |theta| < ~1e-10 [L]); Zahl nicht an der Quelle.
- **F15, Erwartung 08:26:03 (date):** arXiv-API, Abstracts mit IceCube UND decoherence UND gravity, neueste zuerst.
  Erwartet: IceCube-Kollaboration 2023/24 (Nature Physics): keine Dekohaerenz gefunden; Schranken auf
  Dekohaerenzparameter fuer mehrere Energieabhaengigkeiten (n = 0 bis 3), weit unter frueheren; Motivation
  "Raumzeitschaum"/virtuelle schwarze Loecher; Baby-Universen bzw. Wurmloecher hoechstens am Rand genannt. Das waere die
  Datenschranke fuer den Hawking-Informationsverlust (nicht fuer alpha-Zustaende, die keinen Verlust zeigen).
- **F15, Ausgang 08:27:14 (date): bestaetigt** (quellen/F15-arxiv-icecube-dekohaerenz-20261005-082615.xml, 7 Treffer).
  IceCube 2023 (2308.00105, Nature Phys. 20 (2024) 913): keine Dekohaerenz; Gamma_0 <= 1,17e-15 eV (energieunabhaengig),
  30-mal besser als frueher; fuer E^2-Skalierung mehr als sechs Groessenordnungen besser; "significantly surpassing
  expectations from natural Planck-scale models". IceCube 2025 (2507.12316, Proceedings): 10,7 Jahre, nur Empfindlichkeit.
  Baby-Universen/Wurmloecher nicht genannt. -> Eine Abbildung dieser Schranke auf Baby-Universum-Emission habe ich nicht
  gesucht: nach Recherchestand nicht belegt.
- **Abrufbudget erschoepft (15 von 15), 08:27:14.** Ab hier nur Schreibtisch und lokale Dateien.

## 2a. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- **G1 Pachner-Zuege erhalten die Topologie.** GEPRUEFT (F13, Lickorish 1999 [S Abstract]): endlich viele Zugtypen
  verbinden Triangulierungen derselben PL-Mannigfaltigkeit. Bestanden.
- **G2 "Baby-Universum" heisst ueberall dasselbe.** GEPRUEFT (Lesen): Nein, drei Bedeutungen. (a) Topologiewechsel:
  abgeschnuertes geschlossenes S^3 (Hawking 1988, GS 1988, HMS 2018). (b) DT: Auswuchs hinter einem duennen Hals bei
  FESTER Topologie (AGJL Fn. 15; AJJK; Jain/Mathur). (c) Holographie: Zustand eines geschlossenen Universums im
  Hilbertraum H_BU (MM 2020, MV 2020, HUZ 2025). Der Moderator heisst "aendert sich die Topologie?".
- **G3 CDT verbietet Baby-Universen.** GEPRUEFT: nur zeitliches Verzweigen (Loll 2019 lokal; AJL 2002: 3D-CDT-Phase
  "foam of baby universes"; LWZ 2005: 2D-CDT mit Wurmloechern rechenbar).
- **G4 Zufallszuege in UMKLAPP-1 = DT-Zufallszuege.** GEPRUEFT (Schreibtisch): Nein. UMKLAPP-1: feste Ecken, eingebettet,
  flach (UK0), nur 2-3. DT: abstrakte Triangulierungen, alle Zugtypen, Gleichgewicht. Gemeinsam nur die Zaehlrichtung:
  2-3 bei festem N0 senkt N0/N3, das ist in DT die Knaeuel-Richtung (AGJL S. 83 [S]); Polymere brauchen viele Ecken.
- **G5 Delaunay-Netze haben keine minimalen Haelse.** NICHT geprueft (nur grobe Abschaetzung [ES]: vier leere Kugeln
  noetig, sehr selten). Kein Satz: Gegenbeispiel moeglich (Punkt nahe der Mitte eines Tetraeders, sonst leer).
- **G6 3D-Minimalhals = vier Dreiecke ohne Tetraeder.** VERSUCHT (F14), an keiner Quelle gelesen -> bleibt [L].
- **G7 Hertog 2024 ersetzt Hertog 2018.** Nicht am Volltext geprueft; nur Autorenueberschneidung und Abstracts.
- **G8 Kein Dissens 2025/26 zur Axion-Wurmloch-Stabilitaet.** Teilweise geprueft (F4); Arbeiten ohne "axion" im Abstract
  koennten fehlen.

## 3. Strangnotizen und Urteilsentwuerfe (ab 08:29:36 date, Schreibtisch; Ausarbeitung im DOSSIER)

- BU1 eingetroffen (Kern; beide genannten Probleme an der Quelle; Liste unvollstaendig: Daten, Phase).
- BU2 teilweise (eindimensional und keine alpha: ja; "holographisch" zu eng; "kein Coleman" nicht ihr Satz; Hypothese).
- BU3 teilweise (Teil 1 indirekt; Teil 2 nur zeitlich; Teil 3 umstritten).
- BU4 teilweise (Teil 1 ja; Teil 2 ja, aber nur ueber 3-2/1-4, nicht 2-3; Teil 3 nicht entscheidbar).
- BU5 teilweise (Teil 1 ja; Teil 2 verfehlt).
- BU6 eingetroffen (Regel-7-Suchen F5, F8, F11).
- Warnzeichen (Kalibrierung): Die Delaunay-Zuege in TAKT-UMKLAPP-1 enthalten auch 3-2-Zuege (UMKLAPP-1 4.1: 2-3 und 3-2
  etwa gleich oft [P]). D1 deckt diese Netze also NICHT ab; dort koennen Haelse entstehen, auch wenn das Endnetz
  Delaunay ist. Meine wachsende Sicherheit "Baby-Universen spielen fuer Finns Netz keine Rolle" gilt nur fuer reine
  2-3-Folgen.

## 4. Offene Rueckfragen (wandern mit)

- R1: Ist die Kausalitaet die einzige Regel, die in 4D eine de-Sitter-Phase gibt? (Gegenlinie: EDT mit Massterm,
  Laiho u. a.) -> F2. **Stand 08:29:** nicht entschieden (Laiho 2017, Bassler 2021, Asaduzzaman/Catterall 2022 dafuer;
  AGGJ 2013 dagegen; im Fenster nichts Neues gefunden). Bleibt offen.
- R2: Gilt "CDT verbietet Baby-Universen" auch fuer raeumliche Verzweigungen? Lokal L1: nein (Loll 2019).
  **Beantwortet 08:29:** nein (Loll 2019; AJL 2002).
- R3 (neu): Hatten die Delaunay-Ausgangsnetze von UMKLAPP-1 und TT-GLAS-1 minimale Haelse? Nicht gezaehlt (G5).
- R4 (neu): Wie lautet die Ambjorn/Watabiki-Friedmann-Gleichung genau, und wie schneidet sie mit DESI DR2 ab? Nicht
  gelesen (nur Abstracts).
- R5 (neu): Hat jemand die IceCube-Dekohaerenzschranke auf Baby-Universum-Emission (Hawking 1988, GS 1988) abgebildet?
  Nicht gesucht.
- R6 (neu): Steht die 3D-Minimalhals-Definition (4 Dreiecke) so bei Jain/Mathur oder AJJK? Nicht an der Quelle gelesen.

## 4a. Berichtigungen

- ~~08:41~~ (geschaetzt; berichtigt: 08:40:50 date): Lange Zitate (HMS S. 3, McNamara/Vafa S. 3, AGJL S. 83, Duff, HKK, Lickorish) und mehrere
  Zweitzitate je Quelle in diesem Arbeitsfeld auf Umschreibung umgestellt (Urheberrechtsregel: hoechstens ein kurzes
  Zitat je Quelle). Inhalt und Zeiten unveraendert.
- 08:36: Regelverstoss awk in einer lokalen Pipe (Ausgabe verworfen); siehe DOSSIER, Selbstanzeige 12.

## 5. Gestrichen (bleibt sichtbar)

- ~~F4-Erwartung: "Stabilitaet weiter strittig; keine Einigung"~~ (08:14, durch F4 widerlegt; siehe dort).
- ~~F3-Erwartung: "Polchinski PLB 219: excluded volume scheitert"~~ (08:13: falsche Zuordnung; das ist NPB 325, F9).
- ~~F1-Erwartung: "dualisiert braucht man ... falsches Vorzeichen"~~ (08:10: HMS Fn. 4 nennt diese Lesart irrefuehrend;
  Hertog u. a. 2024 benutzen sie aber weiter. Beide Lesarten gelten als gleichwertig.)
