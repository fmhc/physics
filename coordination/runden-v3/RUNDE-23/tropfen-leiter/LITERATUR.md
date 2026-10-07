# TROPFEN-LEITER: Literatur (Runde 23) - Literatur-Agent fuer claude-primary

- Einzige Arbeitsdatei des Literaturteils (Feldregel 5). Vor jedem Schritt neu gelesen. Gestrichenes bleibt mit ~~ ~~
  stehen. Das Arbeitsprotokoll (Vorab-Bilder, Suchplan, Abrufe) steht unveraendert im Anhang.
- Agentenstart 2026-10-02 23:16:53 CEST (date). Datei angelegt 23:19:01 CEST (date). Berichtsteil geschrieben ab
  2026-10-02 23:39:14 CEST (date).
- Zeitbox 60 min ab Start, also bis 2026-10-03 00:16:53 CEST (aus dem Start gerechnet).
- KARTE.md ganz gelesen (eingefroren 23:16:05). E1 bis E5 stehen dort vor dem Abruf fest und sind hier NICHT geaendert,
  nur geprueft.
- Marken:
  - [S] an der Quelle gelesen, mit Abschnitt/Gleichung/Abbildung
  - [L?] nur Abstract, Metadaten, Zitat in einer anderen Arbeit oder Erinnerung
  - [H] Hypothese
  - [ES] eigener Schluss dieses Agenten
- Keine Rechnung, keine Laeufe, kein Journal, kein Peerbus. Drei Kopfrechnungen zur Einordnung von Literaturzahlen sind
  als [ES, Kopfrechnung] markiert (Selbstanzeige S-2).

## Ergebnis zuerst

1. **Zu stillen Moden (BIC) oder einer Transmissionsnullstelle an der Oberflaeche von Bose-Gemisch-Tropfen finde ich keine
   Arbeit (E3 trifft ein).**
   - Gesucht in arXiv-Abstracts, auch im Pflichtfenster Okt. 2024 bis Okt. 2026, und im OpenAlex-Volltext.
   - Der naechste Verwandte stammt aus der He-4-Literatur: Dalfovo u. a. 1995 (cond-mat/9505121, S. 6-7) arbeiten mit
     "resonance states" einer Fluessigkeitsschicht. Darin ist die Atomamplitude ausserhalb null (A_a = 0), "due to
     destructive interference". Das sind nicht verdampfende Zustaende eines endlichen Quantenfluessigkeitskoerpers
     oberhalb der Schwelle, gefunden durch Abstimmen der Schichtdicke.
   - Ihr Mechanismus: Zwei innere laufende Kanaele (R+ und R-) loeschen sich aus. Eine Ein-Kanal-Wand mit Nullstelle ist
     es nicht.
2. **E5 trifft im Wortlaut ein, der Mechanismus ist aber ein anderer als in der Karte.**
   - Bei Normaleinfall faellt die Phonon->Atom-Wahrscheinlichkeit P_pa zwischen dem Rotonminimum (Delta ~ 8,6 K) und dem
     Maxon (Delta* ~ 14 K) von ~1 auf 0 (Dalfovo u. a. 1997, cond-mat/9612042, Eq. (8)-(9), Abb. 2, Tab. I).
   - Die Nullstelle am Maxon ist ein Schwelleneffekt der nicht monotonen Dispersion: Das Phonon geht vollstaendig in ein
     R--Roton ueber. Eine Fano-Interferenz ist es nicht.
   - Im He-4-Fenster mit genau einem offenen Kanal je Seite (|mu| = 7,15 K < hbar omega < Delta) nehmen sie P_pa ~ 1 an;
     gerechnet ist dieses Fenster nicht.
3. **E1 und E2 treffen ein; die Zahlen sind genauer als in der Karte.**
   - Tylutki u. a. 2020 (PRA 101, 051601(R)) rechnen genau das 1D-Kartenmodell.
     - Die Moden eta >= 3 gehen mit fallendem gamma ~ dg N^(2/3) ins Kontinuum, bei N3 = 0,774 bis N7 = 11,447.
     - Die Atmungsmode bleibt immer gebunden.
     - Breiten oberhalb der Schwelle rechnet niemand.
   - Petrov 2015: Im Fenster 20,1 < N~ < 94,2 gibt es keine diskrete Mode (Einheiten: N_i = n_i^(0) xi^3 N~).
     - Als letzte Mode verlaesst die Quadrupolmode l = 2 den diskreten Bereich.
     - Die Atmung liegt grob von N~ ~ 20 bis ~10^3 oberhalb der Schwelle (Abb. 1, abgelesen).
4. **Die Leiterregel steht schon in der Literatur, aber an der Schwelle.**
   - Die Schwellenzahlen N_eta bei Tylutki u. a. haben den konstanten Abstand 2,664. Das ist n0 pi/k(omega = -mu)
     [ES, Kopfrechnung].
   - Ein TR3-Befund muss sich von dieser Schwellenleiter abheben: anderes k, und ein Breitenminimum oberhalb der Schwelle
     statt eines Eintritts an der Schwelle.
5. **Die Datenbruecke ist schwaecher als angenommen.**
   - Selbstverdampfung "has until now defied experimental observations"; der Grund sind Dreikoerperverluste
     (Hirthe/Tarruell 2026, arXiv:2603.17745, S. 13 und S. 22-23).
   - Kollektive Moden von Mischungstropfen sind nach Recherchestand nirgends modenaufgeloest gegen N gemessen
     (Pflichtfenster 24 Monate: nur Theoriearbeiten).
   - Bei dipolaren Tropfen sind die Scherenmode und eine stark gedaempfte Kompressionsmode gemessen
     (Ferrier-Barbut u. a. 2018).
   - "Nicht verdampfende Moden bei diskreten N" sind im Prinzip als Daempfung gegen N messbar. Davon ist der Stand weit
     entfernt [ES].

## Erwartung gegen Befund

| Nr | Erwartung (Karte, unveraendert) | Wahrsch. | Befund | Fundstelle |
|---|---|---|---|---|
| E1 | Tylutki/Astrakharchik/Malomed/Petrov 2020 existiert und zeigt Moden, die mit fallendem N ins Kontinuum laufen | 85 % | **eingetroffen**. Atmungsmode (eta = 2) ausgenommen, sie bleibt gebunden. Breite und Lebensdauer oberhalb der Schwelle behandeln sie nicht. | arXiv:2003.05803, PRA 101, 051601(R) (2020): Abstract; Abb. 1(b) (Kreuze bei gamma > 0, also dg > 0 wie in der Karte); S. 3: N3 ~ 0,774, N4 ~ 3,453, N5 ~ 6,119, N6 ~ 8,783, N7 ~ 11,447; Schwellengesetz -mu - omega ~ (N - N_eta)^2 |
| E2 | Petrov 2015 beschreibt "self-evaporation" fuer 3D-Tropfen unterhalb N ~ 94 (Petrov-Einheiten) | 80 % | **eingetroffen, praezisiert**. Fenster 20,1 < N~ < 94,2; unter 20,1 ist die Monopolmode wieder gebunden; Existenz erst ab N~c ~ 18,65. Das Wort heisst dort "automatically evaporates itself", nicht "self-evaporation". | arXiv:1506.08419, PRL 115, 155302: S. 3-4, Text zu Abb. 1; Einheiten Eq. (9) und Text danach |
| E3 | Keine Arbeit berichtet exakt stille Moden (BIC) von Quantentropfen oder eine Transmissionsnullstelle der Tropfenoberflaeche | 65 % | **eingetroffen** fuer Bose-Gemisch- und dipolare Tropfen (nach Recherchestand nicht belegt, also nicht widerlegt). **Verwandtes**: He-4-"resonance states" mit A_a = 0, entstanden durch Interferenz zweier Innenkanaele. | Negativsuchen C1, C3, C5, F1 (Anhang); cond-mat/9505121 S. 6-7; cond-mat/9603075 S. 15 |
| E4 | Es gibt Theorie zur Phonon-Atom-Umwandlung an der freien He-4-Oberflaeche | 90 % | **eingetroffen** | cond-mat/9505121 (PRL 75, 2510); cond-mat/9603075 (JLTP 104, 367); cond-mat/9612042 (J. Phys.: Condens. Matter 9, L369) |
| E5 | Diese Theorie zeigt eine Nullstelle oder ein scharfes Minimum der Verdampfungswahrscheinlichkeit bei einer Phononenergie | 30 % | **im Wortlaut eingetroffen, Mechanismus anders**. P_pa -> 0 am Maxon (Modenwechsel Phonon -> R-) und an der Schwelle |mu| (Totalreflexion, Atomimpuls -> 0). Ein scharfes Minimum im Inneren eines offenen Fensters gibt es nicht. | cond-mat/9612042 S. 4-8, Eq. (8)-(9), Abb. 2, Tab. I |
| Zusatz | (keine Kartenerwartung) | - | Keine modenaufgeloeste Daempfung gegen N; Selbstverdampfung unbeobachtet | arXiv:2603.17745 S. 13, 20, 22-23; arXiv:1712.06927 S. 3-4, Abb. S3 |

## Erwartungsverstoesse (wichtigste zuerst; Bezug: meine Vorab-Bilder VB-1 bis VB-5 im Anhang und die Karte)

- **V5: Nicht verdampfende Zustaende eines endlichen Quantenfluessigkeitskoerpers gibt es in der He-4-Literatur seit
  1995** (gegen VB-3 und meine erste Lesart von E3).
  - [S] Dalfovo/Fracchetti/Lastri/Pitaevskii/Stringari 1995 (cond-mat/9505121), S. 6-7 nach Eq. (5)-(6):
    - "so called 'resonance' states which are characterized by the absence of the atom signal (A_a = 0) outside the
      slab, due to destructive interference".
    - Gefunden durch Variation von Schichtdicke und Boxgroesse.
    - "the atom wave function is not exactly vanishing, even for the best resonant states".
  - JLTP 1996 (cond-mat/9603075), S. 15: dieselben Zustaende, nur als Rechenhilfe genutzt.
  - Mechanismus nach Eq. (5): S_-a A_- e^(...) + S_+a A_+ e^(...) = 0. Zwei innere laufende Kanaele loeschen sich im
    Atomkanal aus.
  - **[ES]** Das ist der Friedrich-Wintgen-Typ eines BIC (zwei Kanaele interferieren), nicht der Fabry-Perot-Typ mit einer
    Ein-Kanal-Wand. Mit A_a = 0 enthaelt Eq. (5) die Boxlaenge L_a nicht mehr. Deshalb waeren diese Zustaende auch in der
    offenen Schicht nicht abstrahlend (in linearer Ordnung, ohne Mehr-Ripplonen-Prozesse).
- **V4: Die He-4-Verdampfung durch Phononen hat bei Normaleinfall eine Nullstelle, aber ohne Interferenz** (gegen VB-5).
  - [S] Dalfovo/Guilleumas/Lastri/Pitaevskii/Stringari 1997 (cond-mat/9612042), S. 2-8:
    - Vier Kanaele: Atom a, Phonon p, R-, R+.
    - Unitaritaet und Zeitumkehr ergeben S_ij = S_ji.
    - Fuer Delta <= hbar omega <= Delta* gilt P_aa = P_pp = P_-- = P_++ = P_-a = P_+p = 0 (Eq. (8), numerisch bestaetigt)
      und P_pa = P_+- = 1 - P_p- = 1 - P_+a (Eq. (9)).
    - P_pa "decrease[s] from 1 to 0 between Delta and Delta*".
    - Ueber 10 K faellt P_pa "rapidly from 0.5 to 0" (S. 8).
    - Tab. I bei 11 K: P_pa = 0,3236, P_p- = 0,6487, P_+a = 0,6537.
  - Begruendung im Text: Nahe am Maxon dominiert der Modenwechsel Phonon <-> R- (P_p- ~ 1).
  - Die triviale Nullstelle an der Schwelle: "full reflection takes place" (S. 4).
- **V2: Die Leiterregel "Abstand = halbe Innenwellenlaenge" taucht in der Literatur schon auf, an den
  Schwellenkreuzungen** (gegen meine Annahme, die Fabry-Perot-Sicht sei dort neu).
  - Tylutki u. a. beschreiben die diskreten Moden als ebene Bogoliubov-Phononen, "reflected by edges of the droplet"
    (Abstract). Eq. (18): omega_eta ~ 4 pi (eta - 1)/(27 N), Knoten bei x = L/2, also ein "freies Ende".
  - Die Abstaende der N_eta sind 2,679 / 2,666 / 2,664 / 2,664.
  - **[ES, Kopfrechnung]** Mit k^2/2 = sqrt(omega^2 + 1/81) - 1/9 (Text nach Eq. (14)) und omega = -mu0 = 2/9 folgt
    k = 0,5241 und n0 pi/k = 2,664. Je Paritaet sind das 5,33.
- **V1: Im 1D-Tropfen laeuft nicht jede Mode ins Kontinuum** (gegen VB-1).
  - Die Atmungsmode bleibt fuer alle gamma gebunden: Tylutki u. a., S. 3 und Schluss; Astrakharchik/Malomed 2018
    (arXiv:1803.07165), Atmungsabschnitt: "hbar omega_b < |mu| for all parameters", das "autocooling" greift in 1D nicht.
  - Kandidaten fuer stille Moden im 1D-Kartenmodell sind deshalb nur eta >= 3.
- **V3: In 3D ist die letzte gebundene Mode bei N~ = 94,2 die Quadrupolmode, nicht die Atmung** (gegen VB-2).
  - [S] Abb. 1 unten in 1506.08419, vergroessert gelesen.
  - Neue gebundene Moden setzen bei (N~ - N~c)^(1/4) ein: l = 2 bei ~2,95, l = 3 bei ~4,0, l = 4 bei ~4,85, Monopol und
    l = 5 bei ~5,6, l = 6 bei ~6,4, l = 7 bei ~7,1 (abgelesen, grob).
  - Die Monopolmode liegt also grob fuer 20 < N~ < 10^3 ueber der Schwelle.
- **V7: Selbstverdampfung ist nie beobachtet worden.**
  - Das widerspricht der Annahme in IDEEN-LOGIK-TEILCHEN.md, Punkt 2 ("Messdaten moeglich").
  - [S] Hirthe/Tarruell 2026, S. 13: "has until now defied experimental observations". S. 22-23: "three-body losses have
    again prevented its observation".
- **V6 (Nebenbefund): Ein Reflexionselement verschwindet ueber ein ganzes Band.**
  - [S] JLTP 1996, S. 18-19, Eq. (33)-(37): P_++ "practically zero everywhere".
  - Daraus folgt P_-a = (1 - P_+a) P_+a <= 1/4.
  - Das ist eine bandweite Nullstelle, keine isolierte Frequenz.
- Bestaetigungen (je eine Zeile, kein Verstoss):
  - Takahashi 2009: T an einer Kondensat-Stufe steigt monoton.
  - Petrov-Einheiten wie vermutet.
  - Embedded solitons haben Kodimension eins.
  - Keine Modenspektroskopie gegen N bei Mischungstropfen.

## Literaturstand je Frage

### Frage 1 (E1): 1D-Tropfen, Moden ins Kontinuum, Breiten

- [S] Tylutki, Astrakharchik, Malomed, Petrov 2020, arXiv:2003.05803:
  - Eq. (5) ist genau das Kartenmodell "Tropfen 1D": i phi_t = [-phi_xx/2 + sign(dg)|phi|^2 - |phi|] phi mit
    mu0 = -2/9, n0 = 4/9. Der Kink in Eq. (10) ist phi = (2/3)/(1 + exp(2x/3 - 1 - L/3)).
  - Steuergroesse ist gamma = sign(dg) N~^(2/3), Eq. (6).
  - Mit fallendem gamma kreuzen die Moden eta >= 3 nacheinander die Schwelle -mu, bei den Werten N_eta aus der Tabelle
    oben.
  - "Near the crossings the corresponding mode is characterized by a large probability of finding a particle
    (nonvanishing u_eta) outside of the droplet". Der Tropfen wirkt dann als Potentialtopf fuer ein Atom.
  - Die Atmungsmode eta = 2 kreuzt nie. Fuer gamma = 0 gilt omega_2/(-mu) ~ 0,8904; fuer gamma -> -unendlich geht das
    Verhaeltnis gegen 1. Eq. (19): Bindung durch Streulaenge 6/pi.
  - Zu Breite und Lebensdauer oberhalb der Schwelle steht nichts im Text (grep: width, lifetime, decay, damp, resonan).
  - Schluss: "all collective excitations, except the breathing mode, can be pushed into the continuum thus offering a
    way to cool the droplet". Damit ist ungeprueft angenommen, dass Kontinuumsmoden zerfallen.
- [S] Astrakharchik, Malomed 2018, arXiv:1803.07165 (PRA 98, 013631):
  - Atmungsmode in 1D immer unter |mu|.
  - Im Flachkopf-Bereich omega_b ~ 1/N, abgeschaetzt ueber das Phonon mit k ~ pi/L.
- [L?] Ritu, Singh, Gupta, Gautam 2026, arXiv:2603.00987 (PRA 114, 033307): Spinmoden fallen in 1D bei wachsender
  Zwischenkopplung unter die Teilchenemissionsschwelle.
- [L?] Englezos, Charalampidis, Schmelcher, Mistakidis 2026, arXiv:2601.04950: "mode crossings at the particle-emission
  threshold" bei Dreikomponententropfen.

### Frage 2 (E2): Petrov 2015, Selbstverdampfung

- [S] Petrov 2015, arXiv:1506.08419:
  - Eq. (10): i phi_t = (-lap/2 - 3|phi|^2 + 5|phi|^3/2 - mu~) phi. Das ist das Kartenmodell "Tropfen 3D"; fuer
    N~ -> unendlich gilt mu~ = -1/2.
  - Einheiten: xi und tau aus Eq. (9); N_i = n_i^(0) xi^3 N~.
  - Stabilitaet: "metastable (E~ > 0) for N~ < 22.55 and unstable for N~ < N~c ~ 18.65".
  - Moden: "All excitation modes cross the threshold for sufficiently small N~. Only the monopole mode reenters at N~ ~
    20.1. Remarkably, in the interval 20.1 < N~ < 94.2 there are no modes below -mu".
  - Folge laut Text: "exciting the droplet is equivalent to spilling of particles"; "automatically evaporating object".
  - Ripplonen fuer grosse N~ nach Eq. (12): omega_l = sqrt((4 pi/3) l(l - 1)(l + 2) sigma~/N~) mit
    sigma~ = sqrt3 (1 + sqrt3)/35.
  - Abb. 1 zeigt Eq. (12) auch oberhalb der Schwelle (duenn gepunktet). Breiten dort berechnet die Arbeit nicht.
  - 39K-Beispiel (S. 4): xi ~ 1,96 um, tau ~ 2,4 ms. N~ = 30 entspricht N1 = 0,75e5 und N2 = 1,1e5. Lebensdauer
    tau_life ~ 150 ms (K3 = 1e-29 cm^6/s).
- Zum Wort: "self-evaporation" steht nicht bei Petrov (grep). Es erscheint spaeter, etwa bei Ferioli u. a. 2020
  (arXiv:1912.09594) und bei Hirthe/Tarruell 2026. Astrakharchik/Malomed 2018 sagen "autocooling".

### Frage 3 (E3): stille Moden, Transmissionsnullstelle, embedded solitons und embedded eigenvalues

- **Negativbefund zu Tropfen** (nach Recherchestand nicht belegt; Grenzen der Suche im Gegensweep):
  - arXiv-API (Titel, Abstract, Kommentar): "quantum droplet(s)" kombiniert mit "bound state(s) in the continuum",
    "Fano" oder "embedded" ergab 0 Treffer zur Sache.
  - Pflichtfenster 24 Monate: zehn Abfragen, ueber zehn Abstracts gelesen, kein Treffer zur Sache.
  - OpenAlex-Volltext:
    - "quantum droplet" + "bound state in the continuum": 4 Treffer. Alle handeln von optischen BIC
      (Polaritonen-Suprafestkoerper) oder von Dreikoerper-BIC, keiner von Tropfenmoden.
    - "quantum droplet" + "embedded eigenvalue": 0.
    - "quantum droplet" + "total reflection": 8 Treffer. Darin wird der ganze Tropfen an Toepfen und Barrieren
      gestreut; Phononen an der Oberflaeche kommen nicht vor.
- **Embedded solitons, also Solitonen im Kontinuum** [L?]:
  - Yang, Malomed, Kaup 1999, PRL 83, 1958 (Metadaten).
  - Champneys, Malomed, Yang, Kaup 2001, Physica D 152-153, 340, arXiv:nlin/0005056 (Abstract):
    "codimension-one solitons (i.e., those existing at isolated frequency values)". Moeglich, wenn das linearisierte
    Spektrum zwei Zweige hat, einen lokalisierten und einen strahlenden. Ein ES entsteht, "when the latter component
    exactly vanishes in the solitary-wave's tail".
  - Kaup, Malomed 2003, arXiv:math-ph/0204055 (Abstract): Kriterium ist die "orthogonality of the radiation mode in the
    infinite tail to the soliton core".
  - Yang 2003, PRL 91, 143903 (Abstract): stabile ES, in einem Sonderfall auch kontinuierliche Familien.
- **Eingebettete Eigenwerte, also Moden im Kontinuum** [L?]:
  - Cuccagna, Pelinovsky, Vougalter 2005, CPAM 58, 1, DOI 10.1002/cpa.20050 (nur Metadaten, Inhalt nicht gelesen).
  - Soffer, Weinstein 1999, arXiv:chao-dyn/9807003 (Abstract): Generische nichtlineare Hamiltonsche Stoerungen
    zerstoeren gebundene Zustaende durch "slow radiation of energy"; "nonlinear analogue of the Fermi golden rule".
  - Pelinovsky, Kivshar, Afanasjev 1998, Physica D 116, 121: innere Moden, nach Tylutki Ref. [34] auch fuer die
    kubisch-quintische GPE (nur Metadaten und Zitat).
- **Trennung** [ES]:
  - Ein embedded soliton ist der nichtlineare stationaere Zustand selbst, mit Frequenz im linearen Kontinuum.
  - Eine Mode im Kontinuum ist ein Eigenwert der Linearisierung um einen lokalisierten Zustand, eingebettet ins
    kontinuierliche Spektrum. Das ist ein BIC des linearisierten Problems. Die stillen Sprossen gehoeren zu diesem Typ.
  - Gemeinsam ist beiden die Zaehlung: In einem reellen, zeitumkehrsymmetrischen Problem verlangt "Strahlungsamplitude
    = 0" eine einzige reelle Bedingung. Das ergibt isolierte Parameterwerte, wie die Kartenzaehlung annimmt.
- **BIC-Klassen** [L?]:
  - Friedrich, Wintgen 1985, PRA 32, 3231: interferierende Resonanzen.
  - Hsu, Zhen, Stone, Joannopoulos, Soljacic 2016, Nat. Rev. Mater. 1, 16048: Uebersicht, nur Metadaten. Die
    Klassifikation, die den Fabry-Perot-Typ enthaelt, ist Erinnerung.
  - Mai, Lu 2025, arXiv:2501.09207 (Abstract): FP-BIC zwischen zwei total reflektierenden Schichten. "FP-BICs can indeed
    be found near the parameters of total reflections" bei Wellenzahl null oder Spiegelsymmetrie. Ohne diese gilt: "a
    total reflection does not always lead to a FP-BIC even when the parameters of the FP-cavity are tuned".
  - Happ, Naidon 2026, arXiv:2503.02037 (PRA 113, 032203; Abstract): Dreikoerper-Resonanzen lassen sich durch
    Parameterabstimmung zu BIC stabilisieren (Zwei-Kanal-Mechanismus, auch per Magnetfeld). Das ist ein BIC-Vorbild aus
    kalten Atomen, aber kein Tropfen.
- **Phononen an Kondensat- und Tropfenraendern:**
  - [S] Takahashi 2009, arXiv:0909.1068, Abschnitt III, Eq. (62)-(66), Abb. 6:
    - Bogoliubov-Anregung an einer Potentialstufe, hinter der das Kondensat abklingt (U0 > 1).
    - Unter der Schwelle eps = U0 - 1 ist T = 0, darueber steigt T monoton gegen 1; es gibt keine innere Nullstelle.
    - Der Text nennt das "quantum evaporation", "no roton-like dispersion, unlike the superfluid helium 4".
    - Kanalzahl wie in der Karte, aber eine harte Stufe statt einer selbstgebundenen Wand.
  - [S] Holanda Ribeiro, Fischer 2023, arXiv:2111.14153 (SciPost Phys. Core 6, 003), Abschnitt IV.B, Abb. 7, S. 12:
    - Dipolares BEC an einer Schallbarriere.
    - "integrally reflected through the channel k1 (respectively k2) for frequencies close to the roton (respectively
      maxon) frequency".
    - Die Totalreflexion liegt also wieder an Extrema der Dispersion.
  - [L?] Paredes, Guerra-Carmenate, Michinel 2025, arXiv:2507.21376: 2D-Tropfen. Wanderwellen am Rand "emit a small
    outgoing droplet" oder regen innere Moden an. Das ist nichtlinear, kein Phononenstreuproblem.
  - [L?] Hu u. a. 2023, arXiv:2305.09960: Bei der Streuung an einer reflexionsfreien Mulde werden innere Moden unter der
    Schwelle angeregt, deshalb gibt es keine Abstrahlung.

### Frage 4 (E4): He-4 "quantum evaporation", Theorie und Experiment

- [S] Dalfovo, Fracchetti, Lastri, Pitaevskii, Stringari 1995, PRL 75, 2510, arXiv:cond-mat/9505121:
  - Schiefer Einfall, phononfreier Bereich.
  - R+ verdampft deutlich staerker als R-.
  - Rechnung mit "resonance states", siehe V5.
- [S] Dieselben 1996, J. Low Temp. Phys. 104, 367, arXiv:cond-mat/9603075:
  - Linearisierte zeitabhaengige Dichtefunktionaltheorie.
  - Schicht 50 bis 100 Angstroem in einer Box von 100 bis 150 Angstroem, Oberflaechendicke ~6 Angstroem.
  - Nur Eins-zu-eins-Prozesse, keine Mehr-Ripplonen-Prozesse.
  - Bereiche I bis VI in Abb. 1: |mu| = 7,15 K, Maxon "about 14 K" (S. 3-4).
- [S] Dalfovo, Guilleumas, Lastri, Pitaevskii, Stringari 1997, J. Phys.: Condens. Matter 9, L369,
  arXiv:cond-mat/9612042: Normaleinfall, eindimensional, siehe V4.
- [L?] Weitere Theorie, nur Metadaten oder Zitat, Inhalt nicht gelesen:
  - Campbell, Krotscheck, Saarela 1998, J. Low Temp. Phys. 113, 519, DOI 10.1023/A:1022568615857 (Titel fehlt in
    Crossref).
  - Sobnack, Inkson 1997, PRB 56, R14271, und 1999, PRL 82, 3657.
  - Maris 1992, J. Low Temp. Phys. 87, 773, und Mulheran, Inkson 1992, PRB 46, 5454 (semiklassisch; zitiert in
    cond-mat/9612042, Ref. [4, 5]).
- [L?] Experiment:
  - Brown, Wyatt 1990, J. Phys.: Condens. Matter 2, 5025 (Zitat [1] in cond-mat/9612042).
  - Wyatt 1998, Nature 391, 56, DOI 10.1038/34134.
  - Tucker, Wyatt 1996, Czech. J. Phys. 46 S1, 263: P_pa ~ 0,1 fuer hbar omega > 10 K, so zitiert in cond-mat/9612042,
    S. 8.
  - Tucker, Wyatt 1998, J. Low Temp. Phys. 113, 615 (R- relativ zu R+).
- Pflichtsuche 24 Monate: "quantum evaporation" AND phonon ergab 1 Treffer (relativistische Superfluide), keine neue
  Oberflaechentheorie. Neuere Treffer nutzen Quantenverdampfung fuer Detektoren (z. B. arXiv:2201.00738, nur Titel).

### Frage 5 (E5): Nullstelle oder scharfes Minimum

- Ja, aber nur an Schwellen:
  - P_pa -> 0 an der Atomschwelle |mu| (Atomimpuls -> 0, Totalreflexion; S. 4).
  - P_pa -> 0 am Maxon Delta*: Modenwechsel in R-, Eq. (9), Abb. 2. Der Abfall von ~1 bei Delta auf 0 bei Delta* ist
    glatt, nicht scharf.
- Eine isolierte Nullstelle im Inneren eines offenen Fensters gibt es in keiner gelesenen Arbeit.
- Im Fenster |mu| < hbar omega < Delta (nur Phonon und Atom, Kanalzahl wie im Tropfen) argumentiert der Text
  P_pa ~ 1, "since it implies the smallest change of momentum" (S. 4). Abb. 2 beginnt aber erst bei Delta.
- Das Experiment nennt fuer > 10 K P_pa ~ 0,1, die Theorie gibt dort 0,5 bis 0 (S. 8). Schon die Einleitung (S. 2)
  nennt den Vergleich von Theorie und Experiment "still unsatisfactory".

### Frage 6 (Zusatz): Messungen kollektiver Anregungen von Tropfen

- Bose-Gemische:
  - [L?] Cabrera u. a. 2018, Science 359, 301, arXiv:1708.07806: Groesse, Dichte, Mindestatomzahl, Fluessig-Gas-Uebergang.
  - [L?] Semeghini u. a. 2018, PRL 120, 235301, arXiv:1710.10890: Bildung und Gleichgewicht im freien Raum. Das
    Anregungsspektrum nennen sie ausdruecklich als Zukunftsaufgabe.
  - [L?] Ferioli u. a. 2019, PRL 122, 090401: Kollisionen.
  - [L?] D'Errico u. a. 2019, PRR 1, 033155, arXiv:1908.00761: 41K-87Rb, langlebig.
  - [L?] Cavicchioli, Fort, Ancilotto, Modugno, Minardi, Burchianti 2025, PRL 134, 093401, arXiv:2409.16017: Der Tropfen
    startet in einer angeregten Kompressions-Dehnungs-Mode und zerfaellt durch Kapillarinstabilitaet.
  - [S] Hirthe/Tarruell 2026, S. 20: Die Atmungsfrequenz ist nur in der Gasphase gemessen (Aarhus, Skov u. a. 2021,
    PRL 126, 230404).
  - [S] Hirthe/Tarruell 2026, S. 13 und S. 22-23: Selbstverdampfung ist nicht beobachtet. Bei 39K treffen die Verluste
    vor allem eine Spinkomponente, was die Deutung "greatly complicating".
- Dipolare Tropfen:
  - [S] Ferrier-Barbut u. a. 2018, PRL 120, 160402, arXiv:1712.06927, S. 3-4 und Abb. S3:
    - Die Scherenmode ist spektroskopisch gemessen (daraus a_bg = 69(4) a0).
    - Nach einem 90-Grad-Quench des Feldes schwingt die Kompressionsmode der langen Achse: "strongly damped", sichtbar
      bis etwa 20 ms.
    - Die Frequenz kommt aus einem "phenomenological damped sinusoid"-Fit; die Daempfung ist kein eigenes Ergebnis.
    - Das Experiment lief in einer Falle (f_z variiert).
  - [S] Hirthe/Tarruell 2026, S. 20 (Innsbruck): Die Quadrupolfrequenz steigt beim Eintritt in den Tropfenbereich;
    Bragg-Spektroskopie.
- Messbarkeit einer "nicht verdampfenden Mode bei diskreten Atomzahlen" [ES]:
  - Messgroesse waere die Daempfung einer gewaehlten Mode gegen N, mit einer Aufloesung feiner als der Sprossenabstand.
  - In echten Atomen ist der 3D-Sprossenabstand gross: Petrovs Beispiel ergibt rund 2,5e3 Atome der Komponente 1 je
    Einheit N~ [ES, Kopfrechnung aus 0,75e5/30].
  - Dagegen stehen drei Hindernisse:
    - Die Atomzahl schwankt von Schuss zu Schuss.
    - Dreikoerperverluste veraendern N waehrend der Messung.
    - Schon die Grundbeobachtung (Selbstverdampfung) fehlt.
  - Im Prinzip ja, praktisch derzeit nicht. Eine Zahlenabschaetzung fehlt; die Leitung muesste sie rechnen.

## Regime und Moderatoren

- **1D gegen 3D:**
  - In 1D bleibt die Atmung immer gebunden, und die Moden eta >= 3 gehen unterhalb N_eta ins Kontinuum.
  - In 3D liegen fuer 20,1 < N~ < 94,2 alle Moden ueber der Schwelle.
  - Moderatoren: die Dimension (Vorzeichen des Beyond-Mean-Field-Terms, Verhaeltnis Oberflaeche zu Volumen) und die
    Steuergroesse (gamma ~ dg N^(2/3) gegen N~).
- **"Glatte Transmission" gegen "Nullstellen":**
  - Glatt: Takahashi-Stufe; He-4-Bereich I, dort nur als Argument.
  - Nullstellen: He-4-Maxon, dipolares Roton und Maxon, He-4-"resonance states".
  - Vermuteter Moderator [ES]: die Zahl der inneren laufenden Kanaele bei der betrachteten Frequenz. Monotone Dispersion
    gibt einen Kanal, Roton und Maxon geben zwei bis drei.
  - Alle gefundenen Nullstellen und stillen Zustaende liegen im Mehrkanal-Regime oder an einer Kanalschwelle.
  - Das Kartenmodell (Bogoliubov, Kontaktwechselwirkung) und M1 liegen im Ein-Kanal-Regime. Dafuer habe ich kein
    Literaturbeispiel einer inneren Nullstelle gefunden.
- **Theorie gegen Experiment (Selbstverdampfung):** Moderator sind Dreikoerperverluste, bei 39K spinselektiv.
- **Skalar gegen Zwei-Komponenten:**
  - Moderator ist die Tropfengroesse im Vergleich zu xi sqrt(g/|dg|).
  - Petrov 2015, S. 3-4: Fuer kleine Tropfen liegen die Spinmoden im Kontinuum.
  - Ritu u. a. 2026 [L?]: In 1D koennen Spinmoden unter die Schwelle fallen.

## Unterscheidungspunkte

- **U1: Ein-Kanal-Wand mit Nullstelle plus Fabry-Perot (Karte [H]) gegen Interferenz zweier Innenkanaele (He-4-Typ).**
  - Die beiden laufen bei der Tropfengroesse L -> unendlich auseinander.
    - [H] sagt: Die stille Frequenz konvergiert gegen eine Eigenschaft der einzelnen Wand (omega_z), unabhaengig von der
      Dimension, mit Leiterabstand pi n0/k_in(omega_z) je Mode, also 2 pi n0/k_in(omega_z) je Paritaet (wie TR3).
    - Der Zwei-Kanal-Typ sagt: Abstand ~ 2 pi/|k1 - k2| (Vernier), ohne Grenzwert einer Einzelwand.
  - Im skalaren Bogoliubov-Tropfen fehlt der zweite Kanal. Die ebene Wandrechnung (TR0 bis TR2) entscheidet direkt.
- **U2: Schwellenleiter (Tylutki) gegen BIC-Leiter (TR3).**
  - Beide geben konstante Abstaende in N.
  - Sie laufen an zwei Stellen auseinander:
    - (i) Bei der Frequenz: -mu gegen omega_z > -mu.
    - (ii) Bei der Breite: An der Schwellenleiter erscheint eine neue gebundene Mode an der Schwelle. An der BIC-Leiter
      hat die Breite V-foermige Minima bei N_k, und die Mode liegt beidseits ueber der Schwelle.
  - Liegt omega_z nahe 2/9, fallen beide Leitern fast zusammen. Dann trennt nur (ii).
- **U3: Fano-Nullstelle (Kopplung ueber den geschlossenen Kanal) gegen Nullstelle an einer Dispersionsschwelle
  (Maxon, Roton).**
  - Sie unterscheiden sich, wo die Dispersion monoton ist: Ohne Maxon ist nur der Fano-Typ moeglich.
  - Fuer M1 liegt rho_z = 1,5275 innen im Fenster (0,293; 1,707), nicht an dessen Rand. Ein Treffer bei TR0 waere also
    vom Fano-Typ.
- **U4: Lineare Stille gegen nichtlineare Abstrahlung.**
  - Am BIC-Punkt verschwindet die lineare Abstrahlung. Hoehere Harmonische, etwa 2 omega, liegen ebenfalls ueber der
    Schwelle und koennen abstrahlen (Soffer/Weinstein-Typ, [ES]).
  - Unterscheidung: Am BIC-Punkt waechst die Daempfung mit dem Amplitudenquadrat, daneben ist sie amplitudenunabhaengig.

## Gegensweep (Was war so selbstverstaendlich, dass ich es nicht geprueft habe?)

- G1, geprueft: Die Kartenmodelle sind die Literaturmodelle. Tylutki Eq. (5), (10) mit dg > 0 (Abb. 1(b): Kreuze bei
  gamma > 0) und Petrov Eq. (10) passen. Ergebnis: ja.
- G2, geprueft an der Quelle: Ist das skalare Modell kanalvollstaendig? Nein.
  - Petrov 2015, S. 3-4: Die Moden der Relativbewegung (E_+,k) sind bei Tropfengroesse ~ 1/xi "all in the continuum".
    Ueberschuessige Atome binden ab dN1/N1 ~ |dg|/g nicht mehr.
  - Im vollen Gemisch gibt es innen zwei laufende Kanaele (Dichte, Spin) und aussen zwei offene (Atome der Sorten 1
    und 2).
  - **[ES, ungeprueft]** Die Zaehlung der Karte (ein offener plus ein geschlossener Kanal je Seite) gilt nur im
    skalaren Modell. Im vollen Modell kann Stille Kodimension zwei haben oder ueber Zwei-Kanal-Interferenz leichter
    entstehen.
- G3, geprueft: Ist Selbstverdampfung beobachtet? Nein (V7).
- G4, geprueft: Steht "self-evaporation" bei Petrov? Nein, dort heisst es "automatically evaporates itself".
- G5, nicht geprueft: Werden 1D-Moden nach dem Schwelleneintritt zu Resonanzen oder zu virtuellen Zustaenden? (O1)
- G6, nicht geprueft: Kennt die Q-Ball-Literatur Fabry-Perot-BIC der Wand schon? Das gehoert zum Literaturteil des
  Papiers, nicht zu dieser Karte.
- G7, teilweise: Bleibt "exakt still" auch nichtlinear still? Nach dem Soffer/Weinstein-Abstract erzeugt Nichtlinearitaet
  generisch Abstrahlung (U4).
- G8, Grenze der Suche:
  - Die arXiv-API durchsucht keinen Volltext.
  - OpenAlex-Volltext deckt nur einen Teil der Arbeiten ab.
  - WebSearch war erschoepft (200 von 200). Semantic Scholar antwortete mit 429.
  - Das Negativurteil zu E3 lautet deshalb "nach Recherchestand nicht belegt".

## Offene Fragen

- O1 (frueher R2): Wird eine 1D-Mode nach dem Eintritt ins Kontinuum zur Resonanz oder zum virtuellen Zustand? Tylutki u. a.
  sagen nichts dazu. [ES: Beim Beruehren der Schwelle eines offenen Kanals entsteht in 1D typischerweise zuerst ein
  virtueller Zustand; ungeprueft.]
- O2: Breite gegen N fuer Tropfenmoden oberhalb der Schwelle hat niemand gerechnet (Petrov, Tylutki, auch die neueren
  Arbeiten nicht, soweit Abstracts reichen). TR3 waere hier neu.
- O3: Kanalzaehlung im Zwei-Komponenten-Modell (G2).
- O4: Campbell/Krotscheck/Saarela 1998 und Sobnack/Inkson habe ich nicht gelesen. Sie koennten Rechnungen im Ein-Kanal-
  Fenster |mu| < hbar omega < Delta enthalten.
- O5: Hat jemand die He-4-"resonance states" als Physik untersucht, etwa nicht verdampfende Moden duenner He-Filme? Nicht
  gefunden.
- O6: Nichtlineare Abstrahlung ueber Harmonische am BIC-Punkt (U4).

## Was das fuer die Karte heisst [H]

1. **TR1 und TR2 betreten Neuland.**
   - Es gibt weder einen Literaturbefund fuer noch gegen eine Transmissionsnullstelle an einer selbstgebundenen
     Bogoliubov-Oberflaeche.
   - Zwei schwache Gegenhinweise betreffen andere Waende: Takahashis harte Stufe (T monoton) und das He-4-Argument
     P_pa ~ 1 im Ein-Kanal-Fenster.
   - Die 50 % sinken dadurch hoechstens wenig.
   - Findet sich eine Nullstelle, ist sie vom Fano-Typ, nicht vom He-4-Schwellentyp.
2. **Kontrollwerte fuer den 1D-Loeser** vor jeder TR3-Rechnung:
   - N3 ~ 0,774, N4 ~ 3,453, N5 ~ 6,119, N6 ~ 8,783, N7 ~ 11,447 (dg > 0, Kartenmodell).
   - omega_eta ~ 4 pi (eta - 1)/(27 N) fuer grosse N.
   - Quelle: Tylutki u. a. 2020, S. 3 und Eq. (18).
3. **TR3 muss sich von der Schwellenleiter abheben** (U2).
   - Die vorhergesagten 2 pi n0/k_in(omega_z) je Paritaet sind gegen 2 pi n0/k(-mu) = 5,33 abzugrenzen
     [ES, Kopfrechnung].
   - Das trennscharfe Merkmal ist ein Breitenminimum strikt oberhalb der Schwelle.
4. **Die He-4-"resonance states" sind der naechste Vorlaeufer** fuer nicht verdampfende Zustaende eines endlichen
   Quantenfluessigkeitskoerpers. Ein Befund sollte sie zitieren und so einordnen:
   - Im Ein-Kanal-Fall braucht Stille eine Wandnullstelle (dicker Koerper) oder Tunneln ueber den geschlossenen Kanal
     (duenner Koerper).
   - Im Mehrkanal-Fall (He-4-Roton, dipolares Roton, Spinkanal) genuegt Interferenz.
   - Mai/Lu 2025: Totalreflexion fuehrt nur bei Symmetrie verlaesslich zum FP-BIC. Das spricht fuer die symmetrische 1D-
     und Kugelgeometrie der Karte, ist aber kein Beweis.
5. **Die Datenbruecke ist schwach.**
   - Selbstverdampfung ist unbeobachtet, und modenaufgeloeste Daempfung gegen N ist nirgends gemessen.
   - Ein Messvorschlag bleibt Entwurf und sollte von einem "Daempfungsminimum" sprechen, nicht von Null (U4, G2).

## Kalibrierung

- (a) Gemessen:
  - He-4: P_pa ~ 0,1 fuer > 10 K (Tucker/Wyatt, [L?] ueber Zitat).
  - Dy-Tropfen: Kompressionsmode "strongly damped", bis ~20 ms sichtbar.
  - Fuer Bose-Gemisch-Tropfen gibt es keine Daempfungsdaten von Moden.
- (b) Nuetzlich verdichtet: Schwellenwerte und Kurven der Theorie (N_eta, 94,2, P(omega)).
- (c) Gewachsene Gewissheit ohne neue Evidenz:
  - Mein Eindruck "Ein-Kanal-Waende transmittieren glatt" stuetzt sich auf zwei Quellen. Keine davon ist eine
    selbstgebundene LHY-Wand.
  - **Warnzeichen:** Meine Sicherheit, dass E3 eintrifft, stieg, waehrend sich die Frage in "ultrakalte Tropfen" (nichts
    gefunden) und "He-4-Schichten" (gefunden) aufspaltete. Deshalb steht E3 als "eingetroffen mit Verwandtem" da.

## Quellenliste

### [S] an der Quelle gelesen

| Quelle | Fundstelle |
|---|---|
| Tylutki, Astrakharchik, Malomed, Petrov 2020, "Collective excitations of a one-dimensional quantum droplet", PRA 101, 051601(R), arXiv:2003.05803, https://arxiv.org/abs/2003.05803 | Abstract; Eq. (5), (6), (10), (14), (18), (19); Abb. 1(b); S. 3 (N_eta, Schwellengesetz); Schluss |
| Petrov 2015, "Quantum mechanical stabilization of a collapsing Bose-Bose mixture", PRL 115, 155302, arXiv:1506.08419, https://arxiv.org/abs/1506.08419 | Abstract; Eq. (9)-(12); Abb. 1 unten (Bild); S. 3-4 (18,65 / 22,55 / 20,1 / 94,2; Spinmoden; 39K-Zahlen) |
| Astrakharchik, Malomed 2018, "Dynamics of one-dimensional quantum droplets", PRA 98, 013631, arXiv:1803.07165, https://arxiv.org/abs/1803.07165 | Abschnitt "The breathing mode" (S. 9 f.) |
| Dalfovo, Fracchetti, Lastri, Pitaevskii, Stringari 1995, "Rotons and quantum evaporation from superfluid 4He", PRL 75, 2510, arXiv:cond-mat/9505121, https://arxiv.org/abs/cond-mat/9505121 | Eq. (5)-(6), S. 6-7 ("resonance states") |
| Dalfovo, Fracchetti, Lastri, Pitaevskii, Stringari 1996, "Quantum evaporation from the free surface of superfluid 4He", J. Low Temp. Phys. 104, 367, arXiv:cond-mat/9603075, https://arxiv.org/abs/cond-mat/9603075 | Abstract; S. 3-4 (Bereiche, 7,15 K, ~14 K); S. 15; S. 18-19 Eq. (33)-(37); Schluss |
| Dalfovo, Guilleumas, Lastri, Pitaevskii, Stringari 1997, "Quantum evaporation from superfluid helium at normal incidence", J. Phys.: Condens. Matter 9, L369, arXiv:cond-mat/9612042, https://arxiv.org/abs/cond-mat/9612042 | Eq. (1)-(9); S. 4-8; Abb. 2 (Legende); Tab. I |
| Takahashi 2009, "Exact solution of Bogoliubov equations for bosons in one-dimensional piecewise constant potential", arXiv:0909.1068, https://arxiv.org/abs/0909.1068 | Abschnitt III, Eq. (62)-(66), Abb. 6 (Bild), Text S. 7 |
| Holanda Ribeiro, Fischer 2023, "Nonlocal field theory of quasiparticle scattering in dipolar Bose-Einstein condensates", SciPost Phys. Core 6, 003, arXiv:2111.14153, https://arxiv.org/abs/2111.14153 | Abschnitt IV.B, Abb. 7, S. 12 |
| Hirthe, Tarruell 2026, "Bosonic quantum mixtures with competing interactions: quantum liquid droplets and supersolids", arXiv:2603.17745v1, https://arxiv.org/abs/2603.17745 | S. 13 (Abschnitt 2.3); S. 20 (Abschnitt 2.6); S. 22-23 |
| Ferrier-Barbut, Wenzel, Boettcher, Langen, Isoard, Stringari, Pfau 2018, "Scissors mode of dipolar quantum droplets of dysprosium atoms", PRL 120, 160402, arXiv:1712.06927, https://arxiv.org/abs/1712.06927 | S. 3-4, Abb. S3 |

### [L?] nur Abstract, Metadaten oder Zitat

- Champneys, Malomed, Yang, Kaup 2001, "'Embedded solitons': solitary waves in resonance with the linear spectrum",
  Physica D 152-153, 340, DOI 10.1016/S0167-2789(01)00178-6, https://arxiv.org/abs/nlin/0005056 (Abstract)
- Kaup, Malomed 2003, "Embedded solitons in Lagrangian and semi-Lagrangian systems", DOI 10.1016/S0167-2789(03)00219-7,
  https://arxiv.org/abs/math-ph/0204055 (Abstract)
- Yang, Malomed, Kaup 1999, "Embedded solitons in second-harmonic-generating systems", PRL 83, 1958,
  DOI 10.1103/PhysRevLett.83.1958 (Crossref)
- Yang 2003, "Stable embedded solitons", PRL 91, 143903, https://arxiv.org/abs/nlin/0309014 (Abstract)
- Soffer, Weinstein 1999, "Resonances, radiation damping and instability in Hamiltonian nonlinear wave equations",
  https://arxiv.org/abs/chao-dyn/9807003 (Abstract; Zeitschrift Invent. Math. nur aus Erinnerung)
- Cuccagna, Pelinovsky, Vougalter 2005, "Spectra of positive and negative energies in the linearized NLS problem",
  CPAM 58, 1, DOI 10.1002/cpa.20050 (Crossref)
- Pelinovsky, Kivshar, Afanasjev 1998, "Internal modes of envelope solitons", Physica D 116, 121,
  DOI 10.1016/S0167-2789(98)80010-9 (Crossref; Zitat [34] bei Tylutki)
- Hsu, Zhen, Stone, Joannopoulos, Soljacic 2016, "Bound states in the continuum", Nat. Rev. Mater. 1, 16048,
  DOI 10.1038/natrevmats.2016.48 (Crossref)
- Friedrich, Wintgen 1985, "Interfering resonances and bound states in the continuum", PRA 32, 3231,
  DOI 10.1103/PhysRevA.32.3231 (Crossref)
- Mai, Lu 2025, "Relationship between total reflection and Fabry-Perot bound states in the continuum",
  https://arxiv.org/abs/2501.09207 (Abstract)
- Happ, Naidon 2026, "Stabilization of three-body resonances to bound states in a continuum", PRA 113, 032203,
  https://arxiv.org/abs/2503.02037 (Abstract)
- Petrov, Astrakharchik 2016, "Ultradilute low-dimensional liquids", PRL 117, 100401, https://arxiv.org/abs/1605.07585
  (Volltext geladen, nur gegrept, nicht ausgewertet)
- Paredes, Guerra-Carmenate, Michinel 2025, "On the fate of travelling waves at the boundary of quantum droplets",
  https://arxiv.org/abs/2507.21376 (Abstract)
- Hu, Li, Guo, Chen, Luo 2023, "Scattering of one-dimensional quantum droplets by a reflectionless potential well",
  https://arxiv.org/abs/2305.09960 (Abstract)
- Ritu, Singh, Gupta, Gautam 2026, "Spin and density excitations of one-dimensional self-bound Bose-Bose droplets",
  PRA 114, 033307, https://arxiv.org/abs/2603.00987 (Abstract)
- Englezos, Charalampidis, Schmelcher, Mistakidis 2026, "Stability and mixed phases of three-component droplets in one
  dimension", https://arxiv.org/abs/2601.04950 (Abstract)
- Yuan, Xiao, Chen 2026, "Sound propagation in one-dimensional quantum droplets", https://arxiv.org/abs/2608.28028
  (Abstract)
- Weitere Abstracts aus dem Pflichtfenster, alle ohne Bezug zu Stille oder Breiten: arXiv:2607.29292, 2601.16808,
  2607.01863, 2511.02394, 2606.29370
- De Rosi, Astrakharchik, Massignan 2021, PRA 103, 043316, https://arxiv.org/abs/2011.14353 (Abstract; thermische
  Verdampfung einer 1D-Fluessigkeit)
- Papoular, Pitaevskii, Stringari 2016, PRA 94, 023622, https://arxiv.org/abs/1510.02618 (Abstract)
- Campbell, Krotscheck, Saarela 1998, J. Low Temp. Phys. 113, 519, DOI 10.1023/A:1022568615857 (Crossref, Titel fehlt)
- Sobnack, Inkson 1997, PRB 56, R14271; 1999, PRL 82, 3657 (Crossref)
- Brown, Wyatt 1990, J. Phys.: Condens. Matter 2, 5025 (Zitat in cond-mat/9612042)
- Wyatt 1998, "Evidence for a Bose-Einstein condensate in liquid 4He from quantum evaporation", Nature 391, 56,
  DOI 10.1038/34134 (Crossref)
- Tucker, Wyatt 1996, Czech. J. Phys. 46 S1, 263 (Zitat in cond-mat/9612042); 1998, J. Low Temp. Phys. 113, 615
  (Crossref)
- Cabrera u. a. 2018, Science 359, 301, https://arxiv.org/abs/1708.07806 (Abstract)
- Cheiney u. a. 2018, PRL 120, 135301, https://arxiv.org/abs/1710.11079 (nur Titel)
- Semeghini u. a. 2018, PRL 120, 235301, https://arxiv.org/abs/1710.10890 (Abstract)
- Ferioli u. a. 2019, PRL 122, 090401, https://arxiv.org/abs/1812.09151 (Titel)
- Ferioli u. a. 2020, PRR 2, 013269, https://arxiv.org/abs/1912.09594 (Abstract)
- Fort, Modugno 2021, Appl. Sci. 11, 866, https://arxiv.org/abs/2012.10347 (Abstract)
- D'Errico u. a. 2019, PRR 1, 033155, https://arxiv.org/abs/1908.00761 (Abstract)
- Cavicchioli u. a. 2025, PRL 134, 093401, https://arxiv.org/abs/2409.16017 (Abstract)
- Skov u. a. 2021, PRL 126, 230404 (Zitat [20] bei Hirthe/Tarruell)

## Einfach gesagt

Wir haben gefragt, ob die Oberflaeche eines Quantentropfens bei einer bestimmten Tonhoehe gar keine Atome mehr abgibt.
Dafuer hat noch niemand eine Rechnung oder Messung veroeffentlicht. Bei fluessigem Helium kennt man aber seit 1995
Zustaende einer duennen Schicht, die genau so still sind. Dort entsteht die Stille, weil sich zwei verschiedene
Wellenarten im Inneren gegenseitig aufheben, nicht weil die Wand selbst dicht ist. Ob die Tropfenwand allein dicht sein
kann, muss die Rechnung der Leitung zeigen; messen kann man es heute noch nicht, weil die Tropfen dafuer zu schnell
Atome verlieren.

## Selbstanzeigen

- S-1 (23:19): In einem Bash-Aufruf habe ich `python3 -` mit LEEREM Heredoc als Ausweich-Parser gestartet. Es lief kein
  Code (leere Eingabe, keine Ausgabe), aber es war ein Python-Interpreterstart entgegen "keine Python-Laeufe". Danach nur
  curl/grep/sed/pdftotext/pdftoppm.
- S-2: Drei Kopfrechnungen zur Einordnung von Literaturzahlen, alle als [ES, Kopfrechnung] markiert und von der Leitung
  nachzurechnen:
  - n0 pi/k(-mu) = 2,664
  - 2 pi n0/k(-mu) = 5,33
  - ~2,5e3 Atome je Einheit N~ aus Petrovs Beispiel
  Dazu Abszissen aus Abb. 1 bei Petrov abgelesen (grob).
- S-3: Beim Einfuegen des Abrufprotokolls ging die Ueberschrift "## 3. Erwartungsverstoesse" durch ein Edit verloren. Es
  ging kein Inhalt verloren; im Anhang ist die Ueberschrift als [nachgetragen] markiert.
- S-4: Eine Zuordnung stammt aus der Erinnerung: Dass Hsu u. a. 2016 eine Klasse "Fabry-Perot-BIC" fuehren, ist nicht an
  der Quelle gelesen ([L?]). Die Aussage zum FP-BIC stuetzt sich auf den Abstract von Mai/Lu 2025.

---

## Anhang: Arbeitsprotokoll (unveraendert aus der Arbeitsphase)

### 0. Meine Vorab-Bilder (vor dem ersten Abruf, aus Gedaechtnis; damit Verstoesse sichtbar werden)

- VB-1 (E1): Tylutki/Astrakharchik/Malomed/Petrov existiert, vermutlich PRA 101 (2020), Rapid Communication. Inhalt:
  Bogoliubov-Spektrum des 1D-Tropfens gegen N; mit fallendem N laufen die Moden ueber die Schwelle -mu ins Kontinuum;
  im Grenzfall kleiner N wird der Tropfen ein NLS-Soliton ohne innere Moden. Zu Breiten oberhalb der Schwelle erwarte
  ich hoechstens einen Satz ("Resonanzen", keine Rechnung).
- VB-2 (E2): Petrov 2015 nennt drei Zahlen: Existenz ab N~ = 18,65, Stabilitaet (E < 0) ab ~22,55, und eine
  Selbstverdampfungsgrenze bei N~ ~ 94, unterhalb der die Atmungsmode (l = 0) oberhalb von -mu liegt. Einheiten:
  N~ = N / (n0 xi^3) mit Gleichgewichtsdichte n0 und Laenge xi aus dem Petrov-Funktional (genaue Form unsicher).
- VB-3 (E3): Keine Arbeit zu exakt stillen Moden von Quantentropfen. "Embedded solitons" (Yang/Malomed/Kaup 1999) sind
  Solitonen mit Frequenz im Kontinuum, die nur bei isolierten Parametern existieren (Strahlungsschwanz verschwindet).
  "Embedded eigenvalues" der Linearisierung um NLS-Solitonen (Cuccagna/Pelinovsky/Vougalter 2005) sind nicht generisch
  und werden unter Stoerung zu Resonanzen (Fermis Goldene Regel, Soffer/Weinstein 1999).
- VB-4 (E4): Dalfovo/Fracchetti/Lastri/Pitaevskii/Stringari 1995 (PRL) und 1996 (JLTP), Campbell/Krotscheck/Saarela
  1998 (PRL), Sobnack/Inkson 1997; Experimente Brown/Wyatt 1990, Wyatt 1998 (Nature).
- VB-5 (E5): Die DFT-Rechnungen zeigen glatte Verdampfungswahrscheinlichkeiten; die einzige Nullstelle ist die triviale an
  der Schwelle (Phononenergie = Bindungsenergie 7,15 K). Kein scharfes Minimum erwartet; unsicher.

### 1. Suchplan (vor dem ersten Abruf)

Kanaele: WebSearch (vielleicht erschoepft), arXiv-API (export.arxiv.org/api/query), arXiv-Abstract- und HTML-/PDF-Seiten
(WebFetch), Verlagsseiten, Semantic Scholar/OpenAlex fuer Zitate.

| Block | Frage | Ziel |
|---|---|---|
| A | E1 | Tylutki u. a. 2020 finden, Volltext; Astrakharchik/Malomed 2018 |
| B | E2 | Petrov 2015 Volltext (arXiv 1506.08419?) - Nummer erst pruefen, nicht raten |
| C | E3 | BIC/embedded bei Tropfen; embedded solitons; embedded eigenvalues NLS; Pflicht-Suche letzte 24 Monate (Regel 7) |
| D | E4/E5 | He-4 quantum evaporation, Theorie (Dalfovo u. a., Campbell/Krotscheck) und Experiment (Wyatt) |
| E | Zusatz | Messungen kollektiver Moden von Tropfen (K-39, K-Rb, dipolar) |
| F | Gegensweep | Selbstverstaendliches pruefen |

### 2. Abrufprotokoll (Erwartung vor jedem Abruf; Bestaetigung = eine Zeile; Verstoss = voller Zyklus)

- A1 (23:19, arXiv-API au:Tylutki AND au:Petrov). Erwartung: Treffer "Collective excitations of a one-dimensional
  quantum droplet", PRA 101 (2020). Befund: arXiv:2003.05803, PRA 101, 051601(R) (2020), DOI 10.1103/PhysRevA.101.051601.
  Bestaetigt.
- A2 (23:20, Volltext 2003.05803v2, pdftotext). Erwartung: Quantisierungsbedingung mit Randphase, Abbildung omega(gamma)
  gegen -mu, nichts zu Breiten oberhalb der Schwelle. Befund: teils VERSTOSS, siehe V1 und V2 in Abschnitt 3.
  [S] Eq. (5) ist genau das Kartenmodell "Tropfen 1D" (mu0 = -2/9, n0 = 4/9, Kink Eq. (10)). Abb. 1(b): omega_eta/(-mu)
  gegen gamma = sign(dg) N~^(2/3), rote Kreuze = Eintritt ins Kontinuum. S. 3: Atmungsmode (eta = 2) bleibt immer unter
  der Schwelle; alle eta >= 3 kreuzen sie mit fallendem gamma; Schwellengesetz -mu - omega ~ (N - N_eta)^2;
  N3 ~ 0,774, N4 ~ 3,453, N5 ~ 6,119, N6 ~ 8,783, N7 ~ 11,447. Eq. (18): omega_eta ~ 4 pi (eta - 1)/(27 N) im
  Flachkopf-Grenzfall, Knoten des Phononfelds bei x = L/2 ("freies Ende"). Breiten/Lebensdauern oberhalb der Schwelle:
  kein Wort (grep width/lifetime/decay/damp/resonan leer); Schlusssatz: alle Moden ausser der Atmung lassen sich ins
  Kontinuum schieben, "a way to cool the droplet".
- A3 (23:21, Volltext 1803.07165v2). Erwartung: Atmung, Kollisionen, Zerfall von 1D-Tropfen; nichts zu stillen Moden.
  Bestaetigt. [S] Abschnitt "The breathing mode" (S. 9 f.): in 1D gilt hbar omega_b < |mu| fuer alle Parameter, das
  "autocooling" aus 3D greift in 1D nicht.
- B1 (23:20, Volltext 1506.08419v2). Erwartung: N~c = 18,65; Selbstverdampfung unter N~ ~ 94; N~ = N/(n0 xi^3).
  Bestaetigt mit Verfeinerung: [S] S. 3: metastabil fuer N~ < 22,55, instabil fuer N~ < N~c ~ 18,65; "Only the monopole
  mode reenters at N~ ~ 20.1"; "in the interval 20.1 < N~ < 94.2 there are no modes below -mu"; "automatically
  evaporating object". Einheiten Eq. (9) und Text danach: N_i = n_i^(0) xi^3 N~. Eq. (10) ist genau das Kartenmodell
  "Tropfen 3D" (mu~ = -1/2 fuer N~ -> unendlich). Eq. (12): Ripplonen omega_l = sqrt((4 pi/3) l(l-1)(l+2) sigma~/N~),
  sigma~ = sqrt3 (1 + sqrt3)/35. Das Wort "self-evaporation" steht nicht im Text (grep), sondern "automatically
  evaporates itself"; Astrakharchik/Malomed 2018 nennen es "autocooling".
- B2 (23:21, Abb. 1 unten von 1506.08419 als Bild gelesen). Erwartung: die Atmungsmode kreuzt als letzte bei 94,2.
  VERSTOSS (V3): Nach dem Bild kreuzt bei (N~ - N~c)^(1/4) ~ 2,95 (N~ = 94,2) die Quadrupol-Oberflaechenmode
  omega~_2 als letzte; die Monopolmode omega~_0 erscheint erst bei (N~ - N~c)^(1/4) ~ 5,5 bis 5,7 (grob abgelesen,
  N~ ~ 10^3) unter der Schwelle. Reihenfolge abgelesen: l = 7, 6, dann Monopol, dann l = 5, 4, 3, 2.
  Nachtrag 23:37 (vergroessertes Bild): Monopol und l = 5 setzen beide bei ~5,6 ein; l = 4 bei ~4,85, l = 3 bei ~4,0.

- C0 (23:23, WebSearch). Erwartung: Budget erschoepft. Bestaetigt ("200 of 200"). Weiter nur arXiv-API, PDFs, Verlage.
- C1 (23:23, arXiv-API: "quantum droplet(s)" AND "bound state(s) in the continuum"; "quantum droplets" AND Fano;
  "quantum droplet" AND embedded). Erwartung: 0 Treffer zu BIC/Fano. Bestaetigt: 0 / 0 / 0; "embedded" nur im Sinn
  "embedded vorticity" o. ae. Grenze: arXiv-API durchsucht Titel, Abstract, Kommentar, nicht Volltext.
- C2 (23:24, arXiv-API: Yang/Malomed/Kaup, embedded eigenvalue, Pelinovsky, flat-top internal modes). Erwartung:
  Champneys/Malomed/Yang/Kaup als Uebersicht; Kodimension eins. Bestaetigt [L?, Abstract nlin/0005056]: "codimension-one
  solitons (i.e., those existing at isolated frequency values)", moeglich, wenn das linearisierte Spektrum zwei Zweige
  hat (lokalisiert und Strahlung); ES entsteht, wenn die Strahlungskomponente im Schwanz exakt verschwindet.
  Kaup/Malomed (math-ph/0204055, Abstract): Kriterium = Orthogonalitaet der Strahlungsmode zum Solitonkern.
  Neu und relevant: 2507.21376 (Paredes/Guerra-Carmenate/Michinel 2025, 2D-Tropfen: Wanderwellen am Tropfenrand
  stossen kleine Tropfen aus oder regen innere Moden an; Abstract). 2305.09960 (Hu u. a. 2023): Streuung an
  Poeschl-Teller-Mulde regt innere Moden UNTER der Schwelle an, deshalb keine Abstrahlung (Abstract).
- C3 (23:24, arXiv-API, Pflicht-Zeitfenster 2024-10-01 bis 2026-10-03, sieben Abfragen zu Tropfen + evaporation /
  particle emission / excitation spectrum / collective excitations / phonon reflection / breathing mode). Erwartung:
  keine Arbeit zu stillen Moden oder Transmissionsnullstellen. Bestaetigt auf Abstract-Ebene; acht Abstracts gelesen
  (2608.28028 Schall in 1D-Tropfen; 2603.00987 Spin- und Dichtemoden, Spinmoden fallen unter die Schwelle;
  2601.04950 Dreikomponenten, "mode crossings at the particle-emission threshold"; 2607.29292; 2601.16808;
  2607.01863; 2511.02394; 2606.29370). Keines erwaehnt Breiten, BIC, Fano oder Totalreflexion.
- D1 (23:25, arXiv-API "quantum evaporation", au:Dalfovo, au:Krotscheck, au:Wyatt). Erwartung: Dalfovo u. a. 1995/96
  auf arXiv, Campbell/Krotscheck nicht. Bestaetigt: cond-mat/9505121 (PRL 1995), cond-mat/9603075 (JLTP 104, 367,
  1996), dazu cond-mat/9612042 (J. Phys.: Condens. Matter 9, L369, 1997, NORMALEINFALL). Campbell/Krotscheck/Saarela
  nicht auf arXiv gefunden.
- D2 (23:26, Volltext cond-mat/9612042, Normaleinfall). Erwartung (VB-5): glatte Kurven, nur die triviale Nullstelle an
  der Schwelle |mu| = 7,15 K. VERSTOSS (V4), siehe unten.
- D3 (23:27, Volltext cond-mat/9505121 und cond-mat/9603075). Erwartung: Slab-Rechnung, keine Zustaende ohne
  Abstrahlung. VERSTOSS (V5), siehe unten.

- C4 (23:29, arXiv-API Soffer/Weinstein, Cuccagna/Pelinovsky, FP-BIC). Erwartung: Fermis Goldene Regel macht
  eingebettete Eigenwerte generisch zu Resonanzen; zur "Totalreflexion -> Fabry-Perot-BIC" nur Photonik. Bestaetigt.
  [L?, Abstract chao-dyn/9807003] Soffer/Weinstein: gebundene Zustaende werden durch generische nichtlineare
  Stoerungen zerstoert, "nonlinear analogue of the Fermi golden rule". [L?, Abstract 2501.09207] Mai/Lu 2025: FP-BIC
  zwischen zwei periodischen Schichten im Abstand h; "FP-BICs can indeed be found near the parameters of total
  reflections" bei Wellenzahl null oder Spiegelsymmetrie; sonst "a total reflection does not always lead to a FP-BIC
  even when the parameters of the FP-cavity are tuned". Crossref-Metadaten [L?]: Hsu u. a., Nat. Rev. Mater. 1, 16048
  (2016), DOI 10.1038/natrevmats.2016.48; Friedrich/Wintgen, PRA 32, 3231 (1985); Pelinovsky/Kivshar/Afanasjev,
  Physica D 116, 121 (1998); Cuccagna/Pelinovsky/Vougalter, CPAM 58, 1 (2005), DOI 10.1002/cpa.20050;
  Yang/Malomed/Kaup, PRL 83, 1958 (1999).
- C5 (23:32, Pflicht-Zeitfenster 24 Monate: "embedded soliton"; BIC AND Bose-Einstein; BIC AND soliton;
  quantum evaporation AND phonon). Erwartung: nichts zu Tropfen. Bestaetigt: 0 / 2 (Exzitonen, allgemein) / 4
  (Polaritonen in BIC-Mikrokavitaeten, also BIC der Optik, nicht des Solitons) / 1 (relativistische Superfluide).
- D4 (23:32, Volltext 0909.1068, Takahashi 2009, Bogoliubov an Potentialstufe). Erwartung: Phonon -> Atom an einer
  Kondensatkante, T glatt, keine Nullstelle. Bestaetigt [S]: Abschnitt III, Eq. (62)-(66), Abb. 6: fuer U0 > 1 (Kondensat
  klingt hinter der Stufe ab) T = 0 unter der Schwelle eps = U0 - 1, darueber monoton steigend gegen 1; der Text nennt
  das "quantum evaporation" und betont "no roton-like dispersion, unlike the superfluid helium 4". Kanalzahl wie in der
  Karte (innen Phonon + abklingend, aussen u offen + v geschlossen), aber harte Stufe statt selbstgebundener Wand.
  Weitere Abstracts [L?]: Papoular/Pitaevskii/Stringari, PRA 94, 023622 (2016), arXiv:1510.02618 (Leitwert ueber
  Kondensation in eine Anregung und Quantenverdampfung); Duine/Stoof cond-mat/0204529 (anderer Sinn: Emission nach
  schneller Aenderung der Streulaenge).
- D5 (23:28, Crossref). Erwartung: Campbell/Krotscheck/Saarela 1998, Sobnack/Inkson, Wyatt 1998 vorhanden. Bestaetigt
  [L?, nur Metadaten]: Campbell/Krotscheck/Saarela, J. Low Temp. Phys. 113, 519 (1998), DOI 10.1023/A:1022568615857
  (Titel fehlt in Crossref); Sobnack/Inkson, PRB 56, R14271 (1997) und PRL 82, 3657 (1999); Wyatt, Nature 391, 56
  (1998), DOI 10.1038/34134; Tucker/Wyatt, J. Low Temp. Phys. 113, 615 (1998) (R- relativ zu R+); Brown/Wyatt,
  J. Phys.: Condens. Matter 2, 5025 (1990) nur als Zitat [1] in cond-mat/9612042. Keine dieser Arbeiten im Volltext.
- E1x (23:30, arXiv-API Experimente). Erwartung: Mischungstropfen: Groesse, kritische Zahl, Lebensdauer, Kollisionen;
  keine Modenspektroskopie gegen N; dipolar: Scherenmode. Bestaetigt, und verschaerft durch [S] Hirthe/Tarruell 2026
  (arXiv:2603.17745v1, Varenna-Skript), S. 13 Abschnitt 2.3: Selbstverdampfung "has until now defied experimental
  observations"; S. 22-23: "three-body losses have again prevented its observation", bei 39K verschaerft, weil die
  Verluste vor allem eine Spinkomponente treffen; S. 20 Abschnitt 2.6: Atmungsfrequenz nur in der GASphase gemessen
  (Aarhus, Skov u. a. PRL 126, 230404 (2021)); Innsbruck: Quadrupolfrequenz steigt beim Eintritt in den Tropfenbereich,
  Bragg-Spektroskopie. Abstracts [L?]: Cabrera 2018 (Groesse, Dichte, Mindestzahl, Fluessig-Gas-Uebergang); Semeghini
  2018 (Bildung und Gleichgewicht, Anregungsspektrum ausdruecklich Zukunft); D'Errico 2019 (41K-87Rb, langlebig);
  Ferrier-Barbut 2018 (Scherenmode eines Dy-Tropfens, Spektroskopie per Feldmodulation); 41K-87Rb 2025 (PRL 134, 093401:
  Tropfen startet in angeregter Kompressions-Dehnungs-Mode, zerfaellt per Kapillarinstabilitaet); Ferioli u. a. 2020
  und arXiv:2012.10347 (Theorie: Selbstverdampfung gegen Dreikoerperverlust, Parameterbereich zur Beobachtung).
- F1 (23:34, OpenAlex-Volltextfilter). Erwartung: keine Tropfen-BIC. Bestaetigt: "quantum droplet" + "bound state in the
  continuum" 4 Treffer (PRL 134, 056002 Polaritonen; Happ/Naidon Dreikoerper-BIC; arXiv:2604.21353 und ein Preprint zu
  Polaritonen-Suprafestkoerpern); + "embedded eigenvalue" 0; + "total reflection" 8 (Tropfen an Toepfen/Barrieren,
  Holanda Ribeiro/Fischer, Gutachten); + "Fano" 54 (nicht ausgewertet, meist vermutlich Fano-Feshbach); "quantum
  evaporation" + BIC 1 (cond-mat/0210544, Feshbach-Theorie). Semantic-Scholar-Snippetsuche: HTTP 429.
- F2 (23:35, Volltext 2111.14153). Erwartung: Totalreflexion nur in Bereichen ohne laufenden Kanal. Teils bestaetigt:
  Totalreflexion "for frequencies close to the roton (respectively maxon) frequency" (Abschnitt IV.B, Abb. 7, S. 12),
  also an Dispersionsextrema; "Fano" dort nur als mathematische Zerlegung (Anhang B).
- E2x (23:36, Volltext 1712.06927). Erwartung: Frequenz und Daempfung der Scherenmode. Teils: Scherenmode
  spektroskopisch; Kompressionsmode "strongly damped", ~20 ms sichtbar, Fit mit "phenomenological damped sinusoids"
  (S. 3-4, Abb. S3); Daempfung kein eigenes Ergebnis.
- A4 (23:39, Abb. 1(b) von 2003.05803 als Bild). Erwartung: Kreuze bei gamma > 0. Bestaetigt (gamma ~ 0,85 / 2,3 /
  3,35 / 4,25 / 5,05 / 5,8 / 6,55 fuer eta = 3 bis 9), also dg > 0 wie im Kartenmodell.

### 3. Erwartungsverstoesse [Ueberschrift nachgetragen, siehe S-3]

- V4 (gegen VB-5; fuer E5 entscheidend): Die He-4-Theorie bei Normaleinfall hat eine Nullstelle der
  Phonon-Verdampfung, aber nicht durch Interferenz. [S] Dalfovo/Guilleumas/Lastri/Pitaevskii/Stringari 1997
  (cond-mat/9612042), S. 4-5 und Eq. (8)-(9), Abb. 2, Tab. I: vier Kanaele (Atom a, Phonon p, R-, R+);
  S symmetrisch (Unitaritaet + Zeitumkehr); fuer Delta <= hbar omega <= Delta* gilt P_pa = P_+- = 1 - P_p- = 1 - P_+a.
  "they decrease from 1 to 0 between Delta and Delta*"; fuer hbar omega > 10 K faellt P_pa "rapidly from 0.5 to 0".
  Bei 11 K: P_pa = 0,3236, P_p- = 0,6487 (Tab. I). Mechanismus: am Maxon Delta* (~14 K, JLTP 1996 S. 4) gehen Phonon
  und R- ineinander ueber, die Modenwechsel-Reflexion Phonon -> R- wird vollstaendig (P_p- ~ 1). Dazu die triviale
  Nullstelle an der Schwelle |mu|: "full reflection takes place" (S. 4). Zwischen |mu| und Delta (nur Phonon und Atom,
  also EIN offener Kanal je Seite wie im Tropfen) argumentieren sie P_pa ~ 1 (kleinster Impulsuebertrag); gerechnet
  ist dort nichts (Abb. 2 beginnt bei Delta).
- V5 (gegen VB-3 und gegen meine Lesart von E3): In der He-4-Literatur gibt es nicht abstrahlende Zustaende eines
  endlichen Fluessigkeitskoerpers oberhalb der Verdampfungsschwelle. [S] Dalfovo/Fracchetti/Lastri/Pitaevskii/
  Stringari 1995 (cond-mat/9505121), S. 6-7 nach Eq. (5)-(6): "so called 'resonance' states which are characterized
  by the absence of the atom signal (A_a = 0) outside the slab, due to destructive interference"; gefunden durch
  Variation der Slab-Dicke und der Boxgroesse; "the atom wave function is not exactly vanishing, even for the best
  resonant states". JLTP 1996 (cond-mat/9603075), S. 15: dieselben Zustaende, "vanishing amplitude outside the liquid,
  due to destructive interference", nur als Rechenhilfe. Mechanismus nach Eq. (5): zwei INNERE laufende Kanaele (R+ und
  R-) loeschen sich im Atomkanal aus (S_-a A_- e^(...) + S_+a A_+ e^(...) = 0). **[ES]** Das ist eine Interferenz zweier
  offener Innenkanaele (Friedrich-Wintgen-Typ), keine Transmissionsnullstelle einer Ein-Kanal-Wand. Im
  Bogoliubov-Tropfen gibt es innen nur EINEN laufenden Kanal; dort muesste eine stille Mode eines dicken Tropfens aus
  einer Nullstelle der Wandtransmission kommen (oder aus Tunneln durch den geschlossenen Kanal bei duennen Tropfen).
- V6 (Nebenbefund): JLTP 1996, S. 18-19, Eq. (33)-(37): P_++ ist "practically zero everywhere" (Normalreflexion von R+
  verschwindet ueber das ganze Band, Impulsuebertrag ~ 4 1/Angstroem passt nicht zur glatten Oberflaeche). Das ist eine
  bandweite Nullstelle eines Reflexionselements, keine isolierte Frequenz.
- V1 (gegen VB-1, nicht gegen E1): Im 1D-Tropfen laeuft NICHT jede Mode ins Kontinuum. Die Atmungsmode bleibt fuer alle
  gamma gebunden (Tylutki u. a. 2020, S. 3 und Schluss; Astrakharchik/Malomed 2018, Atmungsabschnitt). Folge: Der
  1D-Tropfen hat in der Atmung keine Kandidatin fuer eine stille Mode im Kontinuum; Kandidaten sind nur eta >= 3.
- V2 (gegen meine Annahme, die Literatur kenne kein Fabry-Perot-Bild): Tylutki u. a. beschreiben die diskreten Moden
  ausdruecklich als ebene Bogoliubov-Phononen, "reflected by edges of the droplet" (Abstract) und loesen sie per
  Anpassung an die Kink-Gleichungen (15)-(18). Die Schwellen N_eta haben fast konstanten Abstand: 2,679 / 2,666 /
  2,664 / 2,664. **[ES, Kopfrechnung, keine Rechnung im Sinn der Karte]** Das ist n0 pi/k(omega = -mu) mit
  k^2/2 = sqrt(omega^2 + 1/81) - 1/9 aus dem Text nach Eq. (14): k = 0,5241, n0 pi/k = 2,664. Die Leiterregel
  "Abstand = halbe Wellenlaenge der Innenwelle" ist in der Literatur also fuer die SCHWELLEN-Kreuzungen schon da, aber
  bei omega = -mu, nicht bei einer Transmissionsnullstelle.
- V3 (gegen meine Erwartung zu E2-Details): In 3D ist die Atmungsmode ueber einen grossen Bereich (grob N~ ~ 20 bis
  10^3) ueber der Schwelle; die letzte gebundene Mode bei N~ = 94,2 ist die Quadrupol-Oberflaechenmode (Abb. 1,
  abgelesen).

### 4. Offene Rueckfragen (wandern mit)

- ~~R1: Welche Einheiten nutzt Petrov 2015 fuer N~ genau? (E2)~~ erledigt in B1: N_i = n_i^(0) xi^3 N~, xi aus Eq. (9).
- R2: Ist das, was oberhalb der Schwelle aus einer gebundenen 1D-Mode wird, eine Resonanz (endliche Breite) oder ein
  virtueller Zustand? Tylutki u. a. sagen nichts dazu. [ES: in 1D wird ein Zustand, der die Schwelle eines offenen
  Kanals beruehrt, typischerweise zuerst virtuell, nicht resonant; ungeprueft.] -> wandert als O1 in "Offene Fragen".
