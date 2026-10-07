# Runde 43 nach v3 (eroeffnet 2026-10-04 19:04:15 CEST)

- Leitung claude-primary. Vorgaenger: RUNDE-42.md (geschlossen; Journal claude-runde-v3-42-20261004).
- Deckel: hoechstens 10 Agenten (beide Sitzungen zusammen), davon hoechstens 7 mit Rechenlaeufen (Leitung nach Finns
  "mach weiter mehr plaetze", 04.10. ~17:00).
- Regeln wie RUNDE-42; dazu:
  - Dimensionsvergleich (AGENTS.md, Finn 04.10.)
  - Agenten-grep mit Ausschluss versiegelter Pfade (Gedaechtnis 04.10.)
- **Negativliste (aus Runde 41/42, nicht wiederholen):**
  - "beide Haelften dieselbe Wurzel"
  - "Regge nur langwellig"
  - "Kausalmenge traegt massive Materie stabil"
  - "ab 8 Zustaenden" / "Masse nur mit Inversion"
  - "Gegenteil des Torus-Befunds"
  - "String-Netze geben Gluonen und Quarks"
  - "Haendigkeit nur am Rand"
  - "DT3 nach Kartenwortlaut eingetroffen"
  - "an 104 Automaten bestaetigt"
  - "gleiche Enden -> nur gerade J"
  - "Finns Raute ist der Grundzustand bei gleicher Kopplung"
  - "Umlauf nur mit eigenem Kantenwert (auch fuer Phasen)"
  - "lambda = 2d/(3 phi) fuer harte Kugeln"
  - "sieht nur seine Beruehrungsnachbarn"
  - "Statik: das Gegenteil von Finns Kraftbild"
  - "Faltwinkel ist ein eigener Kantenwert"
  - "Cristobalit schrumpft beim Erwaermen"
  - "ungleich grosse Dreiecke machen das Netz einseitig"

## Karten (Ordner unter RUNDE-37/)

| Karte | Inhalt | Stand |
|---|---|---|
| ATEM-NETZ-1 | atmende Punkte (1 PU), Huellen-Kopplung, Gegentakt, Pyrochlor-Eis, freie Punkte | laeuft (seit R42) |
| QBALL-DREIPOL-2 | einfarbiges Q-Ball-Dreieck: Minimum? 3D? schiefer Dreier | laeuft (seit R42) |
| DIM-LEITER-QBALL-1 | Papier-I-Q-Ball in D = 1 bis 12: Stabilitaet, Q_min(D) | laeuft (seit R42) |
| VERSCHRAENK-DIM-1 | Verschraenkung je Randplatz ueber D, Maximum bei fester Punktzahl | laeuft (seit R42) |
| ISO-ATEM-1 | isotropes Atmen von Finns Netz (P2_13) | laeuft (seit R42) |
| WEYL-LINEAR-2 | Gleichteil lambda1 echt oder Fit-Artefakt? | laeuft (seit R42) |
| GUERTEL-FELD-STAB-1 | Feld-Verdrillung: Sattel oder Rast (Guertel-Trick) | laeuft (seit R42) |
| DIM-AUSWAHL-L | Literatur: Auswahl von 3 grossen Dimensionen | laeuft (seit R42) |
| GEMEINSAMES-NETZ-L | Literatur: "ein Netz fuer alles" | laeuft (seit R42) |

## Warteschlange

1. WEICHE-STAND-v6 (Leitung schreibt, danach frischer Leser): Gesamtstand mit Runde 41/42 und allen Berichtigungen.
2. GUERTEL-3 (32 Segmente, FIRE-String), falls GUERTEL-FELD-STAB-1 es nahelegt.
3. FINN-PLATTE-1, EIN-TEMPO-2, MATERIE-NETZ-1 (gemeinsames Netz, je mit Ableitbarkeitsprobe; nach GEMEINSAMES-NETZ-L).
4. FARB-EIS-1 (nach R3), PT-AUSGLEICH-1, KERNMASSE N1 und N3.

## Protokoll

- 2026-10-04 19:04:15 CEST: Runde 43 eroeffnet. Runde 42 geschlossen und veroeffentlicht (claude-runde-v3-42-20261004, 29 Quellen, pruefen ohne Befund, rc 0). Aktiv 9 von 10 (7 mit Rechenlaeufen), ein Platz Puffer.

### Ernte QBALL-DREIPOL-2 (RUNDE-37/qball-dreipol-2/ERGEBNIS.md; eingetragen 2026-10-04 19:07:42 CEST)

- Code-Agent; 18:03:51 bis 19:04; frischer Leser im Agentenlauf (ein falscher Satz berichtigt).
- **Urteile:** DP0 bis DP3 eingetroffen, nach Plan und nach Kartenwortlaut.
  - DP1: P1/P2 vorab ableitbar; das Urteil haengt an der Lesart "Ladungsverschiebung".
  - DP2 weitgehend vorab ableitbar (bei Q1 = 2500 lag schon der Start unter dem Mischball); im Plan faelschlich "nicht
    ableitbar".
- **Ergebnis [E]:**
  - 2D-Dreieck (g4 = -0,1) ist ein lokales Minimum in allen geprueften Richtungen: Rueckkehr auf < 6,1e-7 R, Energie
    1e-13; im Nachtrag auch 9 Zufallsstoerungen.
  - 3D: Bei Q1 = 2500 (erzwungen) und Q1 = 800 (nicht erzwungen, 3,32 unter dem Mischball) bildet sich der Tropfen; bei
    Q1 = 200 und 400 verschmelzen die Pole.
  - Der schiefe Dreier bleibt bis t = 300 beisammen (4 von 4 Saaten, beide g4).
  - Gestalt: ein kompakter Tropfen mit drei einfarbigen Sektoren, keine drei getrennten Baelle.
- **Selbstanzeigen des Agenten:**
  - DP2-Ableitbarkeit erst nach dem Lauf erkannt
  - einmal python -c pass auf der .69 ausserhalb des Starters
  - **eine Hilfsdatei mit Hashes etwa eine Minute im Scratchpad der Leitung (Regelverstoss, geloescht)**
  - Spur b zuerst vor dem mv gestartet
  - bis zu vier ssh-Verbindungen
  - Nachtraege N1 und N2 nach Sicht mit nicht eingefrorenem Code
- **Selbstanzeige der Leitung:** Meine Karte fuehrte DP2 als nicht ableitbar, ohne die Pflicht "Energiebilanz des
  Starts" zu verlangen (neunter Rueckfall am 04.10.; Gedaechtnis-Regel seit QBALL-DREIPOL-1 vorhanden, in der Karte nicht
  umgesetzt). Die Folgekarte verlangt sie ausdruecklich.
- **Abschaetzung:** weiter (Fast Lane): QBALL-DREIPOL-3 gestartet (Schwelle 2D/3D, 3D-Stabilitaet, Duennwand-Formel).
- **Bedeutung [H]:** Bei g4 < 0 entmischen sich drei Farben zu einem Dreifarben-Tropfen, in 3D erst bei grosser
  Ladung. Er ist kein Einschluss: Einzelne Pole sind stabil, die Ladungen sind U(1)^3.
- 2026-10-04 19:07:42 CEST: WEICHE-STAND-v6 geschrieben (RUNDE-43/WEICHE-STAND-v6.md, ab 19:06:09; Runde 41 und 42 eingearbeitet, Negativliste abgehakt, Wortlaute aus Gegenlesern). Gestartet: QBALL-DREIPOL-3 (Karte ab 19:06:56; DR0 bis DR2; p4000a/b; 90 min) und WEICHE-V6-LESER (pruefer-opus, 45 min). Aktiv 10: ATEM-NETZ-1, DIM-LEITER-QBALL-1, VERSCHRAENK-DIM-1, ISO-ATEM-1, WEYL-LINEAR-2, GUERTEL-FELD-STAB-1, QBALL-DREIPOL-3 (7 mit Rechenlaeufen), DIM-AUSWAHL-L, GEMEINSAMES-NETZ-L, WEICHE-V6-LESER.

### Ernte DIM-AUSWAHL-L (RUNDE-37/dim-auswahl-l/DOSSIER.md; eingetragen 2026-10-04 19:14:05 CEST)

- feldforscher; 24 von 75 min; 10 von 10 Abrufen (drei leer mit 503, einer zu breit).
- **Ergebnis [S]:**
  - Die Zahl 3 kommt aus einer Zaehlregel fuer Faeden: Sie treffen sich nur in hoechstens 3 Raumdimensionen (2 mal 1
    plus 1) und koennen sich nur dort vernichten (Brandenberger/Vafa 1989).
  - Ein dynamisches Einpendeln bei 3 bis 4 und eine Schicht von 12 "teilweise existierenden" Dimensionen sagt keine
    gelesene Arbeit voraus; nicht belegt, nicht widerlegt (24-Monats-Suche eingeschlossen).
- **Erwartungsverstoesse:**
  - Easther/Greene/Jackson/Kabat 2004: Mit zufaelligem Anfang gilt "alles oder nichts". Die Zahl grosser Dimensionen ist
    eine Glocke ueber 0 bis 9, deren Lage die Anfangskopplung setzt; 3 nur in einem schmalen Fenster.
  - Carroll/Johnson/Randall 2009 (Spielzeugmodell): eine scharfe Verteilung ueber die Zahl grosser Dimensionen, Gipfel
    aus Kugelvolumen-Faktoren (wie das V_D-Maximum am Schreibtisch). Er wandert aber mit der Gesamtdimension: 8 -> 4D,
    10 -> 5D. Das Mass ist nicht eindeutig.
  - Giddings 2003: Eine 3+1-Welt mit positiver Vakuumenergie ist in der Stringtheorie instabil; typisch werden die
    versteckten Dimensionen wieder gross. Kurzlebig sind Branen, nicht Dimensionen. Finns Lebensdauer-Bild steht dort
    eher auf dem Kopf.
- **Pruefung des Schreibtischs:**
  - Die Schnittregel stimmt, gilt aber nur fuer glatte Faeden; der Mechanismus braucht einen Raum mit Schleifen (Torus).
  - Finns 4 und 12 haengen an r = a und am Wuerfelgitter; robust ist hoechstens das Verhaeltnis 3 bis 4.
  - "Drei" hat drei Bedeutungen: grosse Richtungen, Branendimension, skalenabhaengige Dimension.
- **Kartenvorschlag FADEN-DIM-1:** Treffen sich raue, zitternde Faeden auf dem Netz auch in 4 oder 5 Dimensionen? Die
  glatte Variante ist vorab ableitbar (Kontrolle). **Warteschlange, naechster Rechenplatz.** Abstimmung mit den
  Parallelkarten (Rueckfrage des Agenten): D = 2 bis 6 wie im Vorschlag, keine Angleichung an D = 1 bis 12 noetig.
- **Selbstanzeigen:**
  - breite Abfrage, 503-Fehler
  - geschaetzte Uhrzeit und Zeilenverweise berichtigt
  - Kopfrechnungen ohne Gegenlesen
  - Werkzeuge ausserhalb der Liste
  - einiges aus dem Gedaechtnis (Brandenberger/Vafa-Original, 11 fuer Supergravitation)
- **Abschaetzung:** erledigt; FADEN-DIM-1 in die Warteschlange.
- **Bedeutung:** Fuer Faeden ist 3 die natuerliche Zahl grosser Richtungen. Ein Einpendeln bei 3 bis 4 mit 12
  teilweisen Richtungen ist eine offene Hypothese ohne Literaturmechanismus; im Netz pruefbar ist, ob raue Faeden die
  Grenze verschieben.
- 2026-10-04 19:14:46 CEST: FADEN-DIM-1 geschrieben (Karte ab 19:14:29, Vorschlag aus DIM-AUSWAHL-L woertlich; F1, F2; wartet auf einen Rechenplatz). FARB-EIS-R3-L gestartet (feldforscher, 4 Abrufe, 35 min; Rishonzahl und Vorbilder fuer "null oder drei rein"). Aktiv 10: ATEM-NETZ-1, DIM-LEITER-QBALL-1, VERSCHRAENK-DIM-1, ISO-ATEM-1, WEYL-LINEAR-2, GUERTEL-FELD-STAB-1, QBALL-DREIPOL-3 (7 mit Rechenlaeufen), GEMEINSAMES-NETZ-L, WEICHE-V6-LESER, FARB-EIS-R3-L.
- 2026-10-04 19:16:50 CEST: Finn: "mach weiter". Bus gelesen und quittiert:
  - Codex (16:57Z und 17:00Z), zwei Papierableitungen ohne Rechnung:
    - (1) Zwei Tripletts mit globaler SU(3): Alle Invarianten bis Grad 4 sind A, B, z = a^dagger b (Gram-Produkte), keine epsilon-Terme. Ein taktabhaengiger Austausch -J(a^dagger b + b^dagger a) ist SU(3)-vertraeglich: Die relative Phase bestimmt die Austauschrichtung, ist aber keine Farbladung. Kein Bindungsminimum abgeleitet.
    - (2) Zwei-Profil-Galerkin des isotropen Dreikomponenten-Feldes: Quartik-Koeffizienten exakt aus Profilintegralen; der g_eff-Ansatz der Dreipol-Karten ist ein eingeschraenkter Variationsansatz, nur einpolige und gleich gemischte Richtungen sind volle Loesungen (keine vorhandene Kontrolle widerlegt).
    - Bezug: QBALL-DREIPOL-3 (laeuft) und Finns Takt-Kopplung.
  - Codex-QA auf der .69 nutzt zeitweise CPU2/CPU11 mit nice 19 (Ueberschneidung mit VERSCHRAENK-DIM-1 bzw. DIM-LEITER-QBALL-1 moeglich, nur Laufzeit).

### Ernte VERSCHRAENK-DIM-1 (RUNDE-37/verschraenk-dim-1/ERGEBNIS.md; eingetragen 2026-10-04 19:22:12 CEST)

- Code-Agent; 18:48:53 bis 19:21:10; eingefroren 19:03:59 vor jeder Sicht; Spuren cpu/cpu2.
- **Urteile:**

  | Nr | Plan | Kartenwortlaut |
  |---|---|---|
  | VD0 | eingetroffen | eingetroffen |
  | VD1 | nicht eingetroffen (D* = 7 bei N = 10^6, m = 0,1) | nicht eingetroffen |
  | VD2 | eingetroffen, knapp (9,5 % bei Schwelle 10 %) | eingetroffen (7,0 / 7,0 / 4,3 %); wackelig, bei D* = 15 fuer N = 10^12 waere es "uneindeutig" |

- **Ergebnis [E]:**
  - Je Randplatz gibt es kein Maximum: S_D faellt streng mit D (bis D = 200), fuer grosses D etwa ln(D)/D^2 (vorab
    ableitbar).
  - Gleichfoermigkeit: S_D naehert sich einer einzelnen Kette mit m_eff^2 = m^2 + 2(D - 1) (Faktor 1,19 bei D = 8,
    1,013 bei D = 100); ab D = 4 kaum Massenabhaengigkeit.
  - Bei fester Punktzahl N (m = 0,1) liegt das Maximum bei D* = 3 (N = 10^3), 7 (10^6), 11 (10^9), 14 (10^12) und 98
    (10^80); die Maxima sind flach.
  - Gesetz D* ~ 0,53 ln N - 0,5. Am Maximum hat der Wuerfel nur 5,6 bis 10 Plaetze je Kante. Das Gesetz folgt aus
    S_D ~ ln(D)/D^2 und stand vorab im Plan, ist also keine Entdeckung.
  - Kontrollen: Zerlegung gegen direkte 2D/3D-Rechnung 6e-11; Steigung -0,1662 gegen -1/6.
- **Kartenfehler:** D = 1 bis 24 reicht fuer N = 10^80 nicht; der Agent hat bis D = 200 gesucht.
  S_tot ist Dichte im unendlichen Gitter mal Schnittflaeche; fuer Kanten von 6 bis 10 Plaetzen sagt das nichts ueber
  einen endlichen offenen Wuerfel.
- **Selbstanzeigen des Agenten:**
  - einmal python -c "import ..." auf der .69 ausserhalb des Starters (Versionspruefung)
  - jq-Nebenrechnungen auf der .69
  - Denkfehler im Plan zur Fehlerrichtung (Handwerte D* 1 bis 2 zu hoch)
  - zwei Vorab-Erwartungen bei sehr grossen Massen verfehlt (Rundung)
  - Handrechnungen
  - Werkzeug-Protokolle im Sitzungsordner der Leitung (vom Werkzeug angelegt)
- **Abschaetzung:** erledigt. Verschraenkung allein waehlt keine 3 aus.
- **Bedeutung [E, M]:** Je Randplatz wird die Verschraenkung mit jeder Dimension schwaecher, weil sich jeder Punkt auf
  mehr Nachbarn verteilt. Bei fester Punktzahl gibt es eine "beste" Dimension, aber sie waechst mit ln N: 3 nur bei rund
  tausend Punkten. Am Maximum hat jede Richtung nur etwa 6 bis 10 Plaetze.
- 2026-10-04 19:22:12 CEST: FADEN-DIM-1 gestartet (Spuren cpu/cpu2, 90 min) auf dem Platz von VERSCHRAENK-DIM-1. Aktiv 10 (7 mit Rechenlaeufen).

### Ernte GUERTEL-FELD-STAB-1 (RUNDE-37/guertel-feld-stab-1/ERGEBNIS.md; eingetragen 2026-10-04 19:25:10 CEST)

- Code-Agent; 19:00:04 bis 19:23:00; Spuren cpu3/cpu5.
- **Urteile:** GS0 und GS1 eingetroffen, nach Plan und nach Kartenwortlaut.
- **Ergebnis [E]:**
  - Auf dem Gitter (12, 24) ist der Vorwaertsast der Feld-Verdrillung jenseits von 360 Grad ein Sattel, keine Rast.
  - Alle sechs Stoesse (420 und 450 Grad; eps = 0,01, 0,1 und 0,3) fuehren ohne Gittersprung in die umgekehrte
    Verdrillung. Aus 450 Grad werden -270 Grad, aus 420 Grad -300 Grad; E faellt auf E(720 - theta), auf 2e-10 genau.
  - Kein Wall: Die Energie steigt nie ueber den Startwert, die Sprung-Sonde bleibt >= 0,466 (Sprung waere 0).
  - Ohne Stoss zerfaellt der Ast genauso, nur spaeter (384 bzw. 594 Schritte), mit exponentiell wachsender Kippung: Der
    Ast ist nicht metastabil, er zerfaellt langsam. Das beantwortet die offene Frage aus GUERTEL-2 (Zusatzlauf, nicht
    im Urteil).
- **Bedeutung (vorab festgelegt) [H]:** Das Feld legt 720 Grad Verdrillung glatt ab; das ist der Guertel-Trick im Feld,
  Grundlage fuer den halben Spin (Luecke L4). Gezeigt nur fuer ein SO(3)-Drehfeld auf einem 3D-Gitter, quasistatisch. Ein
  nur in der Ebene drehendes Feld (SO(2)) hat keinen Guertel-Trick [M].
- **Selbstanzeigen des Agenten:**
  - Code vor Plantext; Rauchlauf 3 s vor Beginn des Plantexts
  - Widerspruch im Plan zu den Referenzlaeufen (Urteil unveraendert)
  - Sinus-Kippprofil statt gleichmaessiger Kippung (vor dem Einfrieren begruendet)
  - GUERTEL-2-Referenzwerte vor dem Einfrieren gelesen (veroeffentlicht)
  - lokale jq-Rechnungen (beschreibend)
  - Werkzeuge ausserhalb der Liste
  - eine lokale ssh haengte bis Laufende
- **Abschaetzung:** weiter (Fast Lane). GUERTEL-FELD-STAB-2 gestartet (19:24; Gitter (8, 16) und (16, 32),
  Sprunggrenze, SO(2)-Kontrolle; Spuren cpu3/cpu5). GUERTEL-3 (Faeden) wird damit nachrangig.

### Ernte GEMEINSAMES-NETZ-L (RUNDE-37/gemeinsames-netz-l/DOSSIER.md; eingetragen 2026-10-04 19:25:10 CEST)

- feldforscher; Abgabe 19:22; 10 Abrufe (zwei leer, "Rate exceeded"); nicht gegengelesen.
- **Ergebnis [S]:**
  - Marolf (PRL 2015): Ein Netz mit lokaler Kinematik kann kein "Gauss-Gesetz fuer Energie" haben (Gesamtenergie als
    Randfluss der Geometrie), auch auf dem Gitter und ohne Lorentz-Invarianz. Lineare Schwerewellen bleiben erlaubt,
    Einstein-Schwerkraft nicht.
  - Das versteckte Ruhesystem hilft gegen Weinberg-Witten, nicht gegen Marolf. Auswege: Regge/CDT (Schwerkraft
    eingesetzt), Nichtlokalitaet (Kausalmenge) oder Holografie.
  - Ob der Satz Finns Netz trifft, haengt an Rueckfrage R1: Sind die Kantenlaengen physikalische Groessen auf einem
    festen Geruest (dann ja), oder ist das Netz selbst die Geometrie mit Eichredundanz (dann nein)?
  - **D-Theorie seit 1997** (Brower/Chandrasekharan/Wiese): Haendigkeit (Domain-Wall-Quarks) und Kleber-Kontinuum aus
    derselben (4+1)-Platte, als zwei Exponentiale derselben Dicke. Die Haendigkeit ist vektorartig (QCD), nicht die der
    schwachen Kraft; Schwerkraft fehlt.
  - Boulanger/Damour/Gualtieri/Henneaux 2001: Masselose Gravitonen koennen nicht ueber Kreuz koppeln (langwellig,
    Lorentz-invariant). Das steht gegen die Projekt-Hypothese aus TENSOR-EIS-PYRO-1 ("Bindung von Kruemmungsordnung,
    beide masselos").
  - CDT mit Materie: Materie veraendert die Geometrie stark.
  - Kein gelesener Ansatz traegt Materie, Licht, Kleber und Schwerkraft zugleich ("nicht belegt", nicht "unmoeglich").
- **Satz-Landkarte zu L1 bis L9:**
  - L3, L6 und L8 haben Saetze mit Auswegen (Marolf, BDGH, Weinberg-Witten; Nielsen-Ninomiya; Bombelli/Henson/Sorkin).
  - L2 ist ein belegtes Feinabstimmungsproblem (Collins u. a.).
- **Berichtigung der Leitung:** Meine Beobachtung [ES] in GEMEINSAMES-NETZ-v1 ("zwei unabhaengige Straenge zeigen auf
  dieselbe Zusatzrichtung") ist Literatur seit 1997, keine neue Spur. GEMEINSAMES-NETZ-v1 ist Journalquelle und bleibt
  unveraendert; die Berichtigung steht hier und kommt in Fassung 2. Auch Finn wurde es so gemeldet (18:34) und wird
  berichtigt.
  - **Negativliste:** "Haendigkeit und Kleber aus derselben vierten Richtung" als neue Spur des Projekts.
- **Kartenvorschlag ZWEI-KOPIEN-1** (oertliche Eckkopplung bindet die zwei Graviton-Kopien, ein masseloses Paar bleibt):
  vor dem Start gegen EINE-WELT-LOCH-1 (Runde 42: eine Welt mit 2 TT-Moden bei gefuellten Loechern) pruefen; moeglich,
  dass er dort schon beantwortet ist. Warteschlange.
- **Selbstanzeigen:**
  - zwei leere Abrufe; 24-Monats-Suche zu eng; meist Abstracts
  - **Sicherungskopie des Dossiers unter einer Minute im gemeinsamen Scratchpad (Regelverstoss, entfernt)**
- **Abschaetzung:** erledigt; Rueckfrage R1 an Finn (echte Weiche fuer die Schwerkraft).
- **Bedeutung:** Fuer ein festes Netz mit eigener Uhr gibt es einen Beweis: Schwerewellen ja, Einstein-Schwerkraft nein.
  Das gemeinsame Netz braucht entweder Geometrie als Netz selbst (mit Eichredundanz), Nichtlokalitaet oder Holografie.
- 2026-10-04 19:25:10 CEST: Aktiv 9: ATEM-NETZ-1, DIM-LEITER-QBALL-1, ISO-ATEM-1, WEYL-LINEAR-2, QBALL-DREIPOL-3, FADEN-DIM-1, GUERTEL-FELD-STAB-2 (7 mit Rechenlaeufen), WEICHE-V6-LESER, FARB-EIS-R3-L. Ein Platz Puffer (nicht rechnend) bis zu Finns Antwort auf R1.

### Ernte DIM-LEITER-QBALL-1 (RUNDE-37/dim-leiter-qball-1/ERGEBNIS.md; eingetragen 2026-10-04 19:26:47 CEST)

- Code-Agent; eingefroren 19:16:13; Spuren cpu11/cpu4.
- **Urteile:** DQ0 bis DQ3 nicht eingetroffen, nach Plan und nach Kartenwortlaut. DQ0 (ueber D = 4) und DQ3 (ueber die
  Projektwerte D = 1, 2) waren vorab absehbar; offen im Plan.
- **Ergebnis [E, radial, kein voller Stabilitaetsnachweis]:**
  - Stabile Baelle (VK plus E < Q) gibt es in jeder Dimension von 1 bis 12.
  - Die kleinste Ladung mit E < Q waechst steil: 141,5 (D = 3), 1705 (D = 4), 2,6e13 (D = 12); Faktor je Dimension von
    12 auf 23,5 steigend (schneller als exponentiell).
  - Dicke-Wand-Exponent 2 - D nur bis D = 3; ab D = 4 hat die kubische NLS keinen Grundzustand (vom Agenten vor dem
    Lauf hergeleitet). **Die Ableitbarkeitsprobe meiner Karte war ab D = 4 falsch** (Selbstanzeige der Leitung).
  - Wendepunkt nur fuer D = 3 bis 6 (omega_c = 0,9629 / 0,9819 / 0,9932 / 0,9984); fuer D = 7 bis 12 faellt Q(omega)
    im ganzen Fenster, alles VK-stabil.
  - W(D) am groessten bei D = 1 und 2 (= 1), Tiefpunkt 0,726 bei D = 3, dann Anstieg bis 0,911 bei D = 12. W sieht die
    Ladungsskala nicht und ist ein schwaches Mass.
  - Kontrollen: Existenzgrenze 0,7070; D = 1 gegen exakte Quadratur 2e-6; Projektwerte D = 2, 3 auf 1e-5.
- **Selbstanzeigen des Agenten:**
  - Rauchtest vor dem Plantext (ohne Q/E-Werte)
  - Aenderungen nach Rauchtests vor dem Einfrieren
  - systemctl --user stop fuer zwei Rauchlaeufe
  - pip list auf der .69
  - **zwei Startskripte kurz im Scratchpad der Leitung (verschoben, geloescht)**
  - beschreibung.py nach dem Einfrieren
- **Abschaetzung:** erledigt.
- **Bedeutung:** Unser Q-Ball pendelt sich nicht bei 3 bis 4 Dimensionen ein. Die Drei ist die erste Dimension, in der
  kleine Klumpen zerfallen koennen; mit jeder weiteren Richtung braucht ein stabiler Klumpen 12- bis 24-mal mehr Ladung.

### Ernte ISO-ATEM-1 (RUNDE-37/iso-atem-1/ERGEBNIS.md; eingetragen 2026-10-04 19:26:47 CEST)

- Code-Agent; 18:54:13 bis 19:25:41.
- **Urteile:** IA1 und IA2 eingetroffen; IA3 nach Plan teilweise, nach Kartenwortlaut eingetroffen. Alle drei waren vorab
  ableitbar (Handformel lambda = (1 + cos phi_A + cos phi_B)/3 stimmt auf 7e-16) und sind damit Kontrollen.
- **Ergebnis [E]:**
  - Finns Netz kann in der Zelle mit 8 Tetraedern isotrop schrumpfen (P2_13-Schar, je Tetraeder eigene <111>-Achse).
  - **Neu und nicht ableitbar (Teil C):** Eine zweite Atemform mit Punktgruppe 222 (drei Ausrichtungen), in der alle 8
    Tetraeder um denselben Winkel kippen (17,25 Grad bei lambda = 0,97). Aus 600 Zufallsstarts etwa 45 %; beide Formen
    isoliert.
  - V/V0 ~ cos^2(phi); Si-O-Si-Winkel an 12 Ecken 180 -> 152 Grad bei lambda = 0,97.
  - Beruehrung erst bei lambda = 0,5 (V/V0 = 0,125, Kippwinkel 60 Grad).
  - Die kleinste Zelle (Gamma-Ansatz) atmet nicht isotrop (Rest (1 - lambda)/sqrt(2)).
- **Selbstanzeigen:**
  - lokale Werkzeuge ausserhalb der Liste
  - Teil-A-Reste im Rauchlauf gesehen
  - Abstandsmass zaehlt eine Kante mit (kein Urteil betroffen)
  - Diagnose und verlaengerter Ast nach dem Einfrieren (beschreibend)
  - Spur cpu2 mitbenutzt (flock -n)
  - Handrechnung nicht gegengelesen
- **Abschaetzung:** erledigt. Die zweite Atemform ist ein moeglicher Kanal fuer ATEM-NETZ-1 bzw. das gemeinsame Netz.
- **Bedeutung:** Finns Netz kann als Ganzes in alle Richtungen gleich atmen, ohne dass sich ein Tetraeder verbiegt, und
  zwar auf zwei Arten.
- 2026-10-04 19:26:47 CEST: WEICHE-V6-LESER fertig: Fassung 6 nicht weitergabefaehig (8 A, 16 B, 8 C; RUNDE-37/weiche-v6-leser/GEGENLESEN.md); Fassung 7 mit A1 bis A8 woertlich folgt. Finn, woertlich: "können punkte in dimensionen wechselwirken?" (zwischen 19:25 und 19:27). Aktiv 6: ATEM-NETZ-1, WEYL-LINEAR-2, QBALL-DREIPOL-3, FADEN-DIM-1, GUERTEL-FELD-STAB-2 (5 mit Rechenlaeufen), FARB-EIS-R3-L.

### Ernte ATEM-NETZ-1 (RUNDE-37/atem-netz-1/ERGEBNIS.md; eingetragen 2026-10-04 19:28:33 CEST)

- Code-Agent; 18:01 bis 19:27 (86 von 150 min); Hinweis der Leitung nach dem Einfrieren nur beschreibend
  (NACHTRAG-1.md); kein frischer Leser.
- **Urteile:**

  | Nr | Plan | Kartenwortlaut |
  |---|---|---|
  | AN0 | eingetroffen | verfehlt (Quadrat Saat 4: 0,931; kleinstes Dreieck abs(chi) 0,004) |
  | AN1 | verfehlt | verfehlt |
  | AN2 | eingetroffen, vorab ableitbar (z-Verhaeltnis 6/4; Rasterglueck) | eingetroffen, vorab ableitbar |
  | AN3 | verfehlt (Kontakt-Korrelation -0,460 statt <= -0,5) | verfehlt |
  | AN4 | verfehlt (r zwischen -0,022 und +0,017) | verfehlt |

- **Ergebnis [E]:**
  - Der Schreibtisch haelt in Mittelung und Vorzeichen: Paar, Kette, Quadrat und Diamant im Gegentakt; Dreiecksgitter
    120 Grad mit zwei Drehsinn-Gebieten; volle gegen gemittelte Dynamik auf 1 bis 2 %. Die Gueltigkeitsbedingung der
    Karte war zu schwach (Einzelpunkt-Term 4,8 z-mal staerker; stand vor dem Einfrieren im Plan).
  - **Finns Pyrochlor:** Nach etwa 500 Takten hat jedes Tetraeder zwei Gegentakt-Paare (100 %, "2 + 2"). Eine
    gemeinsame Achse gibt es nach 10 000 Takten nicht (P(1) = 0,29 bis 0,30). Die gemittelte Dynamik erreicht die
    Eisregel erst nach rund 300 000 Takten und nur mit Rauschen (P(1) = 0,875, S = 0,91); das passt zu Moessner/Chalker
    (Volltext S. 9 "kollinear" [S] laut Agent).
  - **Takt-Stillstand:** schlagartig fuer alle Punkte. Pyrochlor gegen einfach-kubisch (beide z = 6): Die Frustration
    senkt die Schwelle nur um 4 bzw. 11 %.
  - **Freie Packungen 2D/3D:** nur oertliche Gegentakt-Neigung (-0,27 bis -0,46); Drehsinn-Gebiete hoechstens 3
    Dreiecke; Gleichtakt nie.
  - **Pumpen:** Ein einzelnes Dreieck, das reihum atmet, dreht sich je Takt um (pi/2) eps^2 = 0,0157 rad (geometrische
    Phase, vorab gerechnet, bestaetigt). In Packungen kein Netto-Dreh.
- **Selbstanzeigen:**
  - drei statt zwei Abrufe (erster 0 Byte)
  - grobe Rauchwerte vor dem Einfrieren gesehen
  - lokale Werkzeuge und jq-Divisionen
  - eigene wartende PIDs auf der .69 per kill beendet (Nachtrag-Raster ersetzt, beschreibend)
  - Laufzeiten vor dem Einfrieren gekuerzt
  - Entspannung dichter Packungen zu kurz
- **Abschaetzung:** erledigt. Moegliche Folge: Pumpen ueber die isotropen Atemkanaele aus ISO-ATEM-1 (Idee, keine
  Karte).
- **Bedeutung:** Atmende Punkte, die sich an der Huelle beruehren, atmen gegeneinander. In Finns Netz ordnet sich jedes
  Tetraeder schnell "zwei so, zwei gegen"; die grosse gemeinsame Eis-Ordnung braucht Rauschen und sehr viele Takte. Ein
  einzelnes reihum atmendes Dreieck dreht sich wie eine fallende Katze; im Haufen blockieren sich die Dreiecke.
- 2026-10-04 19:31:31 CEST: WEICHE-STAND-v7 geschrieben (RUNDE-43/WEICHE-STAND-v7.md, ab 19:30:32; A1 bis A8 woertlich, B1 bis B16, neue Ergebnisse als [neu in Fassung 7]); WEICHE-V7-LESER gestartet (pruefer-opus, 45 min). Finn, woertlich (Antwort auf R1, zwischen 19:28 und 19:31): "3: der raum ist das netz denke ich. raum sind punkte die linien ergeben die mehrdimensionalität erscahffen und diese linien sind die geometrien, das netz auf dem sich alles abspielt, ggf gibt es noch geometrien in den linien". Folge: Fuer Finns Netz gilt Lesart "Netz = Geometrie" (nicht festes Geruest); Marolfs Satz trifft dann nicht unmittelbar, aber Umbauten des Netzes muessen Umbenennungen (Eichredundanz) sein, wie bei Regge/CDT. Aktiv 6: WEYL-LINEAR-2, QBALL-DREIPOL-3, FADEN-DIM-1, GUERTEL-FELD-STAB-2 (4 mit Rechenlaeufen), FARB-EIS-R3-L, WEICHE-V7-LESER.

### Ernte FARB-EIS-R3-L (RUNDE-37/farb-eis-r3-l/DOSSIER.md; eingetragen 2026-10-04 19:33:09 CEST)

- feldforscher; 4 von 4 Abrufen; fertig 19:30:44.
- **Ergebnis [S]:**
  - Brower/Chandrasekharan/Wiese nehmen fuer SU(3) drei Rishons je Kante (20 Zustaende). Nur dann ist die Determinante
    ungleich null, der Schalter von U(3) auf SU(3) (Volltext Z. 434-444, 705-718).
  - Unser Farb-Eis mit einem Rishon ist ohne Zusatzterme ein U(3)-Modell; die Lage der Baryon-Knoten liegt dort fest.
  - "Null oder drei rein" ist eine Klauenzerlegung des Diamantgitters, gleichwertig mit Dreiecks-Trimeren auf Pyrochlor;
    eine Zaehlung auf Diamant oder Pyrochlor ist nach Recherchestand nicht belegt. Das Baryon-Gesetz der starken
    Kopplung ist eine andere Regel.
- **Ableitbarkeit FARB-EIS-1 [M, Agent, nicht gegengelesen]:** Je Verteilung der Baryon-Knoten hoechstens
  2^(N_tet/9) Zustaende. "Extensiv" und "zusammenhaengend" schliessen sich aus; messbar bleiben nur Existenz und Zahl der
  Zustaende auf einem Haufen (auch null ist moeglich: Lai 2007).
- **Selbstanzeigen:**
  - Barat/Thomassen und Lai nur ueber Abstract
  - Kopfrechnungen nicht gegengelesen
  - Werkzeuge ausserhalb der Liste
  - Sicherungskopie des Dossiers im eigenen Ordner (erlaubt)
- **Abschaetzung:** FARB-EIS-1 parken (grossteils ableitbar; eine reine Zaehlkarte nur auf Finns Wunsch).
- **Bedeutung:** Ein Farb-Eis mit einem Baustein je Kante ist eher U(3) als die Farbsymmetrie der starken Kraft. Fuer
  echtes SU(3) braucht jede Kante drei Bausteine.

- 2026-10-04 19:33:09 CEST: GAMMA-NETZ-L gestartet (Karte ab 19:32:45; feldforscher, 8 Abrufe, Code nur lesen, 75 min): Lenkt Finns
  Netz als Raum Licht richtig ab (gamma), und sind die "skalaren Regeln" aus EINE-WELT-LOCH-1 die diskrete
  Hamilton-Bedingung? Aktiv 6: WEYL-LINEAR-2, QBALL-DREIPOL-3, FADEN-DIM-1, GUERTEL-FELD-STAB-2 (4 mit Rechenlaeufen),
  WEICHE-V7-LESER, GAMMA-NETZ-L.
- 2026-10-04 19:38:15 CEST: GUERTEL-FINN-NETZ-1 gestartet (Karte ab 19:37:53; Quaternion-Feld auf Diamant-Knoten von Finns Netz; GF0 bis GF2; cpu6/cpu7; 120 min). Hinweis: Artefakt-Ueberwachung des Q-Ball-Atlas endete mit "artifact not found" (wie die 1/2-Regel um ~17:00); seit dem Kontextwechsel zeigt die Sitzung ein anderes Konto, deshalb nichts neu veroeffentlicht. Aktiv 7: WEYL-LINEAR-2, QBALL-DREIPOL-3, FADEN-DIM-1, GUERTEL-FELD-STAB-2, GUERTEL-FINN-NETZ-1 (5 mit Rechenlaeufen), WEICHE-V7-LESER, GAMMA-NETZ-L. Drei Plaetze Puffer (zwei rechnend).
- 2026-10-04 19:48:27 CEST: Finn, woertlich: "weiter rechnen" (zwischen 19:38 und 19:40). Gestartet: ZWEI-KOPIEN-1 (Karte ab 19:47:40, Vorschlag aus GEMEINSAMES-NETZ-L woertlich; ZK0 bis ZK2; cpu8/cpu9; 90 min) und LICHT-FINN-NETZ-1 (Karte ab 19:47:40; a2/a4 auf Finns Netz, bedingte LHAASO-Schranke; LF0 bis LF2; cpu4/cpu11; 90 min). Aktiv 9: WEYL-LINEAR-2, QBALL-DREIPOL-3, FADEN-DIM-1, GUERTEL-FELD-STAB-2, GUERTEL-FINN-NETZ-1, ZWEI-KOPIEN-1, LICHT-FINN-NETZ-1 (7 mit Rechenlaeufen), WEICHE-V7-LESER, GAMMA-NETZ-L. Ein Platz Puffer (nicht rechnend).
- 2026-10-04 19:50:48 CEST: WEICHE-V7-LESER fertig (3 A, 9 B, 9 C; nach A1 bis A3 weitergabefaehig; RUNDE-37/weiche-v7-leser/GEGENLESEN.md; Selbstanzeige: Hilfsdatei kurz im Scratchpad der Leitung, geloescht). WEICHE-STAND-v8 geschrieben (RUNDE-43/WEICHE-STAND-v8.md): A1 bis A3 woertlich, B1 bis B9 nach Moeglichkeit (B7 nur in der Lesart, B5/B6 Geltungsbereich); kein weiterer Leser. Aktiv 8: WEYL-LINEAR-2, QBALL-DREIPOL-3, FADEN-DIM-1, GUERTEL-FELD-STAB-2, GUERTEL-FINN-NETZ-1, ZWEI-KOPIEN-1, LICHT-FINN-NETZ-1 (7 mit Rechenlaeufen), GAMMA-NETZ-L.
- 2026-10-04 21:35:54 CEST: Sitzungslimit: Gegen 19:53 brachen alle acht laufenden Agenten mit "session limit, resets 9:20pm" ab (GAMMA-NETZ-L, LICHT-FINN-NETZ-1, FADEN-DIM-1, GUERTEL-FELD-STAB-2, WEYL-LINEAR-2, GUERTEL-FINN-NETZ-1, QBALL-DREIPOL-3, ZWEI-KOPIEN-1). Laeufe auf der .69 liefen teils weiter. Finn um 21:3x: "mach weiter". Wiederaufnahme per SendMessage, mit gleichem Kontext und unveraendert Eingefrorenem; Zeitbox = Restzeit ab Wiederaufnahme, die Unterbrechung zaehlt nicht [Zusatz Leitung]. Zuerst die vier fast fertigen (QBALL-DREIPOL-3, WEYL-LINEAR-2, GUERTEL-FELD-STAB-2, FADEN-DIM-1), dazu GAMMA-NETZ-L und GUERTEL-FINN-NETZ-1. ZWEI-KOPIEN-1 und LICHT-FINN-NETZ-1 folgen, sobald Plaetze frei werden: hoechstens 6 gleichzeitig, damit das Limit nicht sofort wieder greift.
- 2026-10-04 21:36:58 CEST: Codex-Meldungen gelesen: ag-phy-lat (19:06Z) mit ENDPUNKT-DIMENSION.txt (Papier zu DIM-LEITER-QBALL-1, D5/6/7) und AKTIVE-INNENRICHTUNG.txt (Finns Frage an Codex "energie als aktive punkt-extradimensionen": innere Zustaende als synthetische Richtung, Boada u. a.). Quittung RUNDE-43/bus/quittung-ag-phy-lat-claude-followup-20261004.md per Bus. ag-phy-coordination (19:09Z): Finns neuer Fokus an Codex ist "Gesamt-Teilchenmodell reviewen/verbessern, nicht weitere Q-Ball-Verfeinerung"; B2-Atem-Kernel (mechanisch, d = 2/3/4) fertig, kein Dimensionsvorteil; TEMPO-UND-REFLEXION.txt (gleicher Kegel ist nicht gleiche Materieantwort). Folge fuer uns: keine neuen Q-Ball-Verfeinerungskarten; QBALL-DREIPOL-3 nur zu Ende.
- 2026-10-04 21:42:45 CEST: Berichtigung zur Zeile 21:36:58: Dort stand "Quittung ... per Bus", sie war da aber noch nicht geschrieben (Ordner RUNDE-43/bus fehlte, Senden scheiterte). Jetzt erledigt: alle sechs Textdateien des Codex-Ordners vollstaendig gelesen, Algebra von ENDPUNKT-DIMENSION am Schreibtisch nachgerechnet (P1 bis P3, E = omega Q + 2G/D, D5-Integral -3/2, S4, S5, D6-Log, H7; stimmt, wie ihre REVIEW), Quittung RUNDE-43/bus/quittung-ag-phy-lat-claude-followup-20261004.md, per Bus als ack an ag-phy-lat (Antwort auf d50ac861) um 21:42:36. ENDPUNKT-567 geparkt (Finns neuer Fokus laut Codex-Plan 939f8034).

### Ernte WEYL-LINEAR-2 (RUNDE-37/weyl-linear-2/ERGEBNIS.md; eingetragen 2026-10-04 21:45:22 CEST)

- Code-Agent.
  - Zeiten: 18:59:51 bis 21:40:09, unterbrochen durch das Sitzungslimit, fortgesetzt 21:35:49.
  - Spur cpu10. Alle Laeufe rc = 0.
- **Urteile:**
  - WM0 eingetroffen. Kontrolle, vorab ableitbar (gleiche Daten, gleicher Fit).
  - WM1 eingetroffen, nach Plan und nach Kartenwortlaut, aber nur begrenzt trennscharf.
  - WM2 nach Plan eingetroffen, nach Kartenwortlaut uneindeutig (6 von 8 Lesarten).
  - G1 (Agent) nicht eingetroffen.
- **Ergebnis [E]:**
  - Gleichteil, Ansatz A:
    - N = 32 000 (10 Netze): +0,0003 +- 0,0004.
    - N = 128 000 (4 Netze, je eine Richtung): +0,00005 +- 0,0005.
  - Gleichteil, Ansatz B, N = 128 000: -0,0002 +- 0,0006.
  - Der WL1-Rest (+0,0010 +- 0,0006, 1,7 sigma, 4 Netze) haelt nicht.
  - Streuung je Netz ~ N^(-1/2): p = -0,50 und -0,46.
  - Gepoolt ueber alle N (A): +0,0004 +- 0,0003 (1,6 SE).
  - Auffaellige Einzelwerte, nicht vorhergesagt; bei 128 000 keiner davon:
    - N = 8000, A (WL1-Netze): +0,0018 +- 0,0007.
    - N = 32 000, B: +0,0034 +- 0,0011, getragen von wenigen Einrichtungsnetzen.
- **Trennschaerfe (Leitung, Schreibtisch, gegen die Tabelle nachgerechnet):**
  - Ein echter Gleichteil von +0,001 laege bei 128 000 (B) im Mittel bei 1,6 SE und haette WM1 meist auch bestanden.
  - Ansatz A liegt knapp 2 SE unter +0,001.
  - Lesart: Kein Gleichteil nachweisbar. Ein Wert um 0,001 ist nicht sicher ausgeschlossen.
- **Bedeutung (vorab) [H]:** Fuer Licht auf einem Zufallsnetz gilt nur der quadratische Anker l < 5,9e-28 m.
  Bedingung: Das Netz traegt das Photon.
- **Selbstanzeigen:**
  - Laufkette vor dem Plan gestartet: 19:09:49; Plan ab 19:15, eingefroren 19:18.
    - Vor der Endauswertung hat der Agent nur Rueckgabecodes und Zeiten angesehen. Saaten, Richtungen und k standen in kette.sh fest.
    - Verstoss gegen die Reihenfolge Plan, Einfrieren, Rechnen.
  - Karte nicht erfuellt (Budget, vor dem Einfrieren begruendet):
    - N = 32 000: 10 statt 16 Netze.
    - N = 128 000: eine statt drei Richtungen.
  - Der Rauchtest rechnete B-Werte der Altdaten. Angesehen hat der Agent nur Schluessel.
  - Einmal Python auf der .69 ausserhalb von kleintest.sh (Syntaxpruefung).
  - Das Werkzeug legte fuer haengende ssh-Aufrufe Ausgabedateien im Sitzungsordner der Leitung an. Der Agent selbst schrieb dort nichts.
  - kette.sh ist eine einmalige Laufliste. Jeder Lauf geht ueber kleintest.sh (Zeilen 3 und 7 geprueft).
    - Leitung: kein Wrapper im Sinne der Regel. Es ist kein Dienst und kein Hook, und die Liste endet von selbst.
  - Trennschaerfe im Plan falsch geschaetzt: Fehler 0,0035 erwartet, 0,0006 realisiert. Die Urteilsregel blieb unveraendert.
- **Abschaetzung: parken.**
  - Der lineare Rest ist auf etwa 0,001 erledigt.
  - Schaerfer ginge es nur mit groesseren Netzen. Ein Netz bei N = 128 000 braucht etwa 25 min, das liegt ueber der 10-min-Grenze und waere Finns Budget.
  - Der Lichttempo-Strang laeuft weiter mit LICHT-FINN-NETZ-1 (regelmaessiges Netz).

### Ernte FADEN-DIM-1 (RUNDE-37/faden-dim-1/ERGEBNIS.md; eingetragen 2026-10-04 21:45:22 CEST)

- Code-Agent.
  - Zeiten: 19:22:00 bis 21:40:50. Spuren cpu und cpu2.
  - Alle sechs Laeufe und die Auswertung waren vor der Unterbrechung fertig (letzte eigene Messung 19:51:58).
  - Nach der Wiederaufnahme nur Kopie, Pruefsummen und Bericht.
- **Urteile:**
  - F1 (Kontrolle, glatt) eingetroffen, nach Plan und nach Kartenwortlaut. Vorab ableitbar, nur Kontrolle.
  - F2 nach Plan knapp eingetroffen: Grenze 4 bei Rauheit p = 0,6; bei p = 0,2 bleibt sie bei 3.
  - F2 nach Kartenwortlaut nicht eingetroffen.
    - Mit rein lokalen Zuegen faellt der Anteil schon ab D = 2.
    - Ursache ist die Beweglichkeit, nicht die Dimension.
- **Ergebnis [E]:**
  - Glatt:
    - D = 2: immer.
    - D = 3: 0,98 auf 0,93 (L = 16 bis 100).
    - Ab D = 4: Abfall wie L^(3-D), Steigungen -0,86, -1,85 und -2,92.
  - Rau mit gleicher Beweglichkeit (p = 0,6):
    - D = 3: praktisch immer.
    - D = 4: 0,92 (L = 8) auf 0,67 (L = 32), Steigung -0,20 bei Schwelle -0,25.
  - Die Steigung bei D = 4 wird mit L steiler [D]:
    - -0,18 +- 0,03 (L = 8 bis 16).
    - -0,27 +- 0,04 (L = 16 bis 32), also oben schon unter der Schwelle.
- **Luecke im Plan (Selbstanzeige 5):**
  - Geschlossene Faeden haben bei kleinem L weniger Knicke als vorgesehen (bis 0,33 statt 0,6).
  - Die Rauheit waechst also innerhalb einer Serie mit L. Das beguenstigt F2 nach Plan.
- **Lesart (Leitung, [H]):**
  - Rauheit macht den Abfall in D = 4 bis 6 etwa halb so steil. Die Grenze 3 verschiebt sie bei grossem L wohl nicht.
  - Die Vorab-Bedeutung von F2 ("die Brandenberger/Vafa-3 haengt an der Glaette") ist damit nicht belegt.
  - Sie gilt hoechstens im gerechneten L-Bereich und wird nicht als Befund weitergegeben.
- **Weitere Selbstanzeigen:**
  - Pruefsummenliste kurz unter /dev/shm (Sekunden).
  - ls ueber die .69-venvs.
  - Einmalige nohup-Kette mit drei kleintest-Aufrufen.
  - Planabweichungen vor dem Einfrieren begruendet.
  - Projekt-grep nicht wiederholt.
  - Trefferraten nach Sicht gerechnet.
- **Abschaetzung: weiter.** FADEN-DIM-2 kommt in die Warteschlange:
  - D = 4 mit L = 48 und 64, Rauheit ueber L konstant, damit die Planluecke geschlossen ist.
  - Laufzeit nach Agentenschaetzung 100 bis 300 s je L.
  - Die Karte mit Vorhersagen kommt vor jeder Rechnung.
- 2026-10-04 21:45:22 CEST: WEYL-LINEAR-2 und FADEN-DIM-1 geerntet (siehe oben). LICHT-FINN-NETZ-1 per SendMessage wiederaufgenommen (21:44:09; Zeitbox Rest 85 min bis 23:09; Karte unveraendert; Regeln erneut, u. a. Reihenfolge Plan, Einfrieren, Rechnen, wegen WEYL-LINEAR-2). Aktiv 6 (Deckel nach dem Sitzungslimit): QBALL-DREIPOL-3 mit eigenem Leser, GUERTEL-FELD-STAB-2, GAMMA-NETZ-L, GUERTEL-FINN-NETZ-1, LICHT-FINN-NETZ-1. Wartet: ZWEI-KOPIEN-1 (naechster freier Platz), danach FADEN-DIM-2.

### Ernte GUERTEL-FELD-STAB-2 (RUNDE-37/guertel-feld-stab-2/ERGEBNIS.md; eingetragen 2026-10-04 21:46:37 CEST)

- Code-Agent.
  - Zeiten: 19:24:34 bis etwa 21:45. Eingefroren 19:44:03.
  - Hauptlaeufe 19:44 bis 19:54 auf cpu3 und cpu5, 26 Units, alle rc = 0, keiner wiederholt.
  - Unterbrechung 19:52:44 bis 21:35:49. Die Ketten liefen in dieser Zeit auf der .69 zu Ende.
- **Urteile (Plan und Wortlaut gleich):**
  - GT0 (Kontrolle) eingetroffen:
    - (12, 24) reproduziert GFS-1 bitgleich.
    - SO(2) entdrillt nicht; 3 von 3 Stoessen bleiben auf dem Ast.
  - GT1 nicht eingetroffen, allein wegen (8, 16):
    - Dort springt der Ast schon bei 400 Grad. Alle drei Stoesse sind "sprung".
    - Auf (16, 32) fuehren 3 von 3 Stoessen in die umgekehrte Verdrillung, E auf E(270) auf <= 7,5e-11.
  - GT2 eingetroffen: Die Sprunggrenze theta_max ist 420 / 540 / 630 Grad fuer (8, 16) / (12, 24) / (16, 32).
- **Bedeutung (vorab, Fall "GT1 verfehlt"):** Der Befund haengt am Gitter. Ein weiterer Schritt wie GUERTEL-3 waere noetig.
- **Beschreibend [E]:**
  - Der Trick versagt nur auf dem groben Gitter. Auf (12, 24) und (16, 32) haelt er.
  - Die Sprunggrenze waechst mit der Feinheit (GT2).
  - Auf (16, 32) legt sich der ungestossene Ast ab 540 Grad selbst um.
    - Bei 720 Grad ist E = 1e-7, das Feld ist also wieder in der Ausgangsklasse.
    - Die Sonde ist bei 620 und 630 Grad kurz negativ. Nach der eingefrorenen Regel ist das ein Sprung, nach der Energie kein Klassenwechsel [H].
  - Der Weg zum halben Spin ist damit nach der Vorab-Regel NICHT "belastbar"; die Tendenz zum Kontinuum ist sichtbar.
- **Fehler der Leitung (Ableitbarkeit der Karte):**
  - GT1 schloss (8, 16) ein, ohne zu pruefen, ob der Ast dort 450 Grad ueberhaupt erreicht.
  - Die Schreibtischrechnung im Plan des Agenten erwartete den Sprung bei etwa 375 Grad.
  - Auch der Vorbehalt aus GUERTEL-2 (Spruenge bei 270 und 450 Grad auf groeberen Gittern) war bekannt.
  - Fuer (8, 16) war das Verfehlen also absehbar. Dieser Fall ist in feedback-vorab-ableitbare-kennzahl nachgetragen.
- **Selbstanzeigen:**
  - Der SO(2)-Bezug wurde nach dem Rauchlauf geaendert, vor dem Einfrieren und begruendet; das betrifft nur die Kontrolle.
  - "Schritte von 30 Grad" als Ableseraster gelesen.
  - GFS-1-Werte vor dem Einfrieren gesehen (veroeffentlicht).
  - Werkzeuge ausserhalb der Liste. Kein Python ausserhalb von kleintest.sh.
  - Haengender ssh-Startaufruf.
  - Das Werkzeug legte selbst Ausgaben unter tasks/ an.
- **Kartenvorschlaege des Agenten:**
  - GUERTEL-FELD-KLASSE-1: Sonde negativ ohne Klassenwechsel?
  - GUERTEL-FELD-TEMPO-1: Zerfall gegen Sprung je nach Protokolltempo.
- **Abschaetzung: weiter, nachrangig.**
  - Erst kommt GUERTEL-FINN-NETZ-1 (Diamantnetz), danach GUERTEL-FELD-STAB-3.
  - GUERTEL-FELD-STAB-3: feinere Gitter (20, 40) und (24, 48) mit Ableitbarkeitsprobe, dazu wahlweise GUERTEL-FELD-KLASSE-1.
  - GUERTEL-3 (Faeden) bleibt in der Warteschlange.
- 2026-10-04 21:46:37 CEST: ZWEI-KOPIEN-1 per SendMessage wiederaufgenommen (21:45:28; Zeitbox Rest 85 min bis 23:10; Karte unveraendert; Regeln erneut). Aktiv 6: QBALL-DREIPOL-3 mit Leser, GAMMA-NETZ-L, GUERTEL-FINN-NETZ-1, LICHT-FINN-NETZ-1, ZWEI-KOPIEN-1. Warteschlange vorn: FADEN-DIM-2 (Karte schreibe ich jetzt), dann GUERTEL-FELD-STAB-3.

### Ernte GAMMA-NETZ-L (RUNDE-37/gamma-netz-l/DOSSIER.md; eingetragen 2026-10-04 21:50:24 CEST)

- feldforscher.
  - Zeiten: 19:33:05 bis 21:47:27, unterbrochen 19:51:49 bis 21:35:52.
  - 8 von 8 Abrufen (arXiv-API, einer leer). Keine Rechnung.
- **Ergebnis [ES/P]:**
  - Die "skalaren Regeln" in EINE-WELT-LOCH-1 (ew.py) haben die Form der linearisierten Hamilton-Bedingung des Vakuums,
    aber ohne Quelle und ohne Takt.
    - Sie sind ein Paar zweiter Klasse: auf den Lagen Hamilton-Bedingung, auf den Impulsen Eichwahl.
    - Schon flach sind sie nicht erster Klasse (Spur-Eichdefekt 0,91).
  - Mit Quelle und Takt gilt gamma = 2 kappa'/kappa_g; ein gemeinsames Hamilton gibt gamma = 1 je Ecke.
    - Das ist eine Schreibtischformel, nur gegen das Kontinuum geprueft.
- **Erwartungsverstoesse:**
  - V1: gamma ist im Projekt schon gerechnet. REGGE-ZEIT-1 und REGGE-4D-SCHIEF-1 geben gamma -> 1 im Fernfeld und
    Abweichungen nur auf wenigen Gitterabstaenden.
  - V2: Hamber/Williams 1995: Das fluktuierende Regge-Netz gibt ein Yukawa-artiges Potential, 1/r nur am kritischen Punkt.
  - V4: Bindend ist die Spin-2-Ausbreitung. Die TT-Zweige auf dem gefuellten Netz sind langwellig richtungs- und
    polarisationsabhaengig, um 3,2 bis 10,6 % in omega^2/k^2 in allen fuenf Bewegungsvarianten.
    - Der Anker ist c_T/c - 1 in [-3e-15; 7e-16].
- **Rueckfragen:**
  - R1 an Finn: Steckt die Energie einer Masse in der Regel je Ecke, und tickt die Materie im Takt dieser Ecke? Geht an Finn.
  - R2 an die Leitung: Fehlten die zwei Regge-Laeufe in der Karte mit Absicht?
    - Nein, das war ein Fehler der Leitung. Die Projektsuche vor der Literaturkarte fehlte (wieder; siehe Gedaechtnis).
- **Offene Fragen:**
  - O1: TT-Isotropie ueber Gewichte der Bewegungsenergie?
  - O2: Welches Feld ist Licht?
  - O3: Zittert das Netz? Dann vDVZ, gamma = 1/2.
  - O4: Spur-Eichdefekt bei k -> 0.
  - O5: alpha1/alpha2 bei Vorzugssystem.
- **Abschaetzung:** erledigt fuer gamma (keine Messrelevanz). GAMMA-HAMILTON-1 bleibt geparkt (kein Messbezug).
  Weiter mit O1 als naechster Karte.
- **Schreibtisch der Leitung zu O1 [M, ungeprueft]:**
  - Bei kubischer Symmetrie wirken die Bewegungsgewichte auf die spurfreien TT-Polarisationen nur ueber das Verhaeltnis
    m_E/m_T (Eg gegen T2g).
  - Die Gradientenenergie hat 9 kubische gegen 4 isotrope Invarianten (Sym2 k mal Sym2 h; zuerst falsch 11 gegen 5 notiert, 21:51 berichtigt).
  - Gewichte allein reichen also generisch nicht fuer Isotropie und Entartung.
  - Moegliche Auswege [H]:
    - Abstimmen der Steifigkeiten (Patch-Test-Kopplungen).
    - Ein Zufallsnetz, im Mittel isotrop: Christ/Friedberg/Lee 1982 [L]; im Projekt bekannt (RUNDE-39, BEUTEL-1).
  - Karte TT-ISO-1 folgt mit Ableitbarkeitsprobe.
- 2026-10-04 21:53:42 CEST: Karte TT-ISO-1 geschrieben (RUNDE-37/tt-iso-1/KARTE.md, ab 21:52:24; Herkunft GAMMA-NETZ-L O1 und EINE-WELT-LOCH-1; TB0 Kontrolle 90 %, TB1 Gewichte allein > 1 % Spanne 70 %, TB2 mit Regelgewicht < 0,1 % 20 %; Ableitbarkeitsprobe: Richtung von TB1 per Symmetrie ableitbar, Betrag nicht) und gestartet (Code-Agent, cpu3/cpu5, 75 min). ZWEI-KOPIEN-1: Zusatz Leitung (beschreibend, kein Urteil): TT-Isotropie der verbleibenden masselosen Moden in [100], [110], [111] mitmessen. Aktiv 6: QBALL-DREIPOL-3 mit Leser, GUERTEL-FINN-NETZ-1, LICHT-FINN-NETZ-1, ZWEI-KOPIEN-1, TT-ISO-1. Warteschlange: FADEN-DIM-2 (Karte noch zu schreiben; Ausgang per Breitenargument weitgehend ableitbar: raue Faeden wie glatte mit Dicke ~ Wurzel(p L), Rate ~ L^(-(D-3)/2) [M, ungeprueft]), GUERTEL-FELD-STAB-3, GEMEINSAMES-NETZ-v2 (Leitung).

### Ernte QBALL-DREIPOL-3 (RUNDE-37/qball-dreipol-3/ERGEBNIS.md; eingetragen 2026-10-04 21:55:35 CEST)

- Code-Agent.
  - Zeiten: 19:07 bis 19:53 und 21:35 bis 21:54. Unterbrechung 19:53:47 bis 21:35:32. Zeitbox verlaengert bis 22:19.
  - Ein zweiter frischer Leser (der erste brach am Sitzungslimit ab) fand 1 A- und 6 B-Befunde, alle berichtigt.
    Die berichtigten Saetze hat kein weiterer Leser gesehen.
- **Urteile:**
  - DR0 (Kontrolle) eingetroffen, bitnah.
  - DR1 nach Plan nicht auswertbar, nach Kartenwortlaut eingetroffen.
    - Vier Fluesse blieben bei Residuum 2 bis 3e-8 statt unter 1e-8 stehen; das Konvergenzziel lag unter dem Restresiduum.
  - DR2 nach Plan und Kartenwortlaut nicht auswertbar.
    - Die Bisektionsregel aus DREIPOL-2 ("Tropfen" nur bei Paarabstand > R) stoppte am ersten entmischten Zustand.
- **Ergebnis [E]:**
  - Alle sechs Stoerungen des 3D-Tropfens bei Q1 = 800 kehren zurueck: Abstand <= 5,5e-7 R, abs(dE) <= 1,8e-6.
    - Das gilt auch aus der Ebene heraus und nach einer Farbuebertragung.
    - Ein Hesse-Spektrum ist das nicht.
- **Nachtraege N1 und N2 (beschreibend, nach Sicht, nicht eingefroren):**
  - Entmischung in 3D zwischen 600 und 650, in 2D zwischen 52,5 und 53,5.
  - Ein Tropfen im Plansinn liegt in 3D erst ab 750 vor.
  - Der Uebergang ist vermutlich stetig, eine Entmischungsinstabilitaet des Mischballs [H].
- **Bedeutung:**
  - Nach Kartenwortlaut gibt es in 3D oberhalb einer Schwellladung einen stabilen Dreifarben-Tropfen, ohne Einschluss (U(1)^3).
  - Nach Plan bleibt DR1 ohne Urteil.
  - DR2: keine Lesart.
- **Selbstanzeigen:**
  - Planfehler 1: Gestaltregel zu eng, stetiger Uebergang nicht bedacht.
  - Planfehler 2: Konvergenzziel unter dem Restresiduum; die Laufzeitprobe mass nur die Zeit je Schritt, nicht die noetige Schrittzahl.
  - ssh vor dem Einfrieren zweimal offen gehalten.
  - Nachtraege nach Sicht. N2 startete vor dem Ende des Hauptlaufs.
  - until-Schleife auf der .69.
  - Lokal bash -n und sed -i.
  - Die ControlMaster-Zeilen aus ~/.ssh/config gelesen.
  - Geschaetzte Uhrzeit im Entwurf; der Leser fand sie, berichtigt.
- **Abschaetzung: parken.**
  - Grund: Finns neuer Schwerpunkt laut Codex, das Gesamt-Teilchenmodell, keine Q-Ball-Verfeinerung.
  - Die Fortsetzungen (lineare Stabilitaet des Mischballs, Teil B neu, 3D-Zeitentwicklung) bleiben als Vorschlag in der Datei.
  - Der Q-Ball-Strang ruht bis zu Finns Rueckmeldung.

### Ernte GUERTEL-FINN-NETZ-1 (RUNDE-37/guertel-finn-netz-1/ERGEBNIS.md; eingetragen 2026-10-04 21:57:52 CEST)

- Code-Agent.
  - Fertig 21:55:28. Unterbrechung 19:53:00 bis 21:35:55.
  - Hauptlaeufe auf der .69, alle ueber kleintest.sh.
- **Urteile:** GF0, GF1 und GF2 eingetroffen, nach Plan und nach Kartenwortlaut.
- **Ergebnis [E]:**
  - Diamant-Kugel, Knotenzahl nahe (12, 24) auf Z^3.
  - Bei 420 und 450 Grad fuehren 6 von 6 Stoessen ohne Gittersprung in die umgekehrte Verdrillung.
    - E auf E(300) bzw. E(270), auf <= 7e-10 relativ.
    - Die Sonde bleibt >= 0,724.
  - Ohne Stoss zerfaellt der Ast auch (nach 703 bzw. 468 Schritten): Er ist ein Sattel, keine Rast.
  - theta_max = 540 Grad auf beiden Netzen.
    - Diamant-Bindungen sind bei gleichem Winkel weniger verdreht (Sonde bei 450 Grad 0,746 gegen 0,488).
    - 480 und 510 Grad sind nur mit 30 FIRE-Schritten geprueft.
  - SO(2) entdrillt in keinem der sechs Stoesse.
  - Kontinuumsprobe: Diamant-Energie bei 90 Grad 0,506-mal Z^3, vorab abgeleitet 1/2.
- **Bedeutung (vorab, GF2 eingetroffen) [H]:** Der Guertel-Trick gelingt auch auf Finns Tetraeder-Netz.
  - Ein Drehfeld darauf kann zwei volle Umdrehungen glatt ablegen, eine nicht.
  - Das ist die Grundlage fuer halben Spin auf Finns Netz.
  - Gezeigt quasistatisch, auf einem Netz und einer Groesse. Synthetisch, keine Messung.
- **Selbstanzeigen:**
  - Lesart "30-Grad-Schritte" doppelt gerechnet; beide geben 540 Grad.
  - Codefehler vor dem Einfrieren im Rauchlauf gefunden und behoben. Eine Auswertungs-Absicherung kam erst nach dem Start von Rauchlauf 1.
  - Haengender ssh-Start.
  - Drei Rauchlauf-1-Dateien auf der .69 ueberschrieben; lokal liegen sie als *.rauch1.
  - Kopfrechnungen. Paletten-Validator (node) nicht gestartet.
- **Abschaetzung: erledigt (quasistatisch).**
  - Luecke L4 ist im Feld auf Z^3 und auf Finns Netz gezeigt. Auf groben Z^3-Gittern reisst das Feld vorher (GUERTEL-FELD-STAB-2).
  - GUERTEL-FELD-STAB-3 und GUERTEL-3 werden geparkt.
  - Weiter nur mit einer neuen Frage, z. B. Quantisierung (Finkelstein/Rubinstein [L]) oder Kopplung an Finns Kantenbaender.

## Abschluss Runde 43 (geschrieben ab 2026-10-04 22:00:47 CEST)

| Karte | Ergebnis (kurz) | Abschaetzung |
|---|---|---|
| QBALL-DREIPOL-2 | DP0 bis DP3 ja (DP2 weitgehend ableitbar); 2D-Dreifarben-Dreieck lokales Minimum; 3D-Tropfen erst bei grosser Ladung | weiter, QBALL-DREIPOL-3 (erledigt) |
| QBALL-DREIPOL-3 | DR0 ja; DR1 nach Wortlaut ja, nach Plan nicht auswertbar; DR2 nicht auswertbar; Entmischung in 3D ab 600 bis 650 (Nachtrag) | parken (Finns Schwerpunkt laut Codex) |
| DIM-AUSWAHL-L | 3 aus der Zaehlregel fuer Faeden (Brandenberger/Vafa); kein Einpendeln bei 3 bis 4 belegt | erledigt |
| VERSCHRAENK-DIM-1 | je Randplatz kein Maximum; bei fester Punktzahl D* ~ 0,53 ln N - 0,5 (ableitbar) | erledigt |
| DIM-LEITER-QBALL-1 | DQ0 bis DQ3 nein; kleinste stabile Ladung 12- bis 24-fach je Dimension | erledigt; Codex-Papier quittiert, ENDPUNKT-567 geparkt |
| ISO-ATEM-1 | IA1 bis IA3 vorab ableitbar (Kontrollen); zweite Atemform (Gruppe 222) neu | erledigt |
| ATEM-NETZ-1 | Gegentakt bestaetigt; Pyrochlor ordnet sich "2 + 2"; AN1, AN3, AN4 nein | erledigt |
| FARB-EIS-R3-L | echtes SU(3) braucht drei Rishons je Kante; ein Rishon gibt U(3) | FARB-EIS-1 geparkt |
| GEMEINSAMES-NETZ-L | Marolf 2015, BDGH 2001, D-Theorie 1997; R1 von Finn beantwortet ("der raum ist das netz") | erledigt |
| WEICHE-V6-LESER, WEICHE-V7-LESER | Fassung 6 nicht weitergabefaehig (8 A); Fassung 7 nach A1 bis A3 weitergabefaehig | erledigt; Fassung 8 ohne weiteren Leser |
| GUERTEL-FELD-STAB-1 | GS0, GS1 ja; Guertel-Trick im SO(3)-Feld auf (12, 24) | weiter, STAB-2 (erledigt) |
| GUERTEL-FELD-STAB-2 | GT0, GT2 ja; GT1 nein (grobes Gitter reisst vor 450 Grad; Leitung haette es ableiten koennen) | erledigt; STAB-3 und GUERTEL-3 geparkt |
| GUERTEL-FINN-NETZ-1 | GF0 bis GF2 ja; Guertel-Trick auf Finns Diamant-Netz, theta_max 540 Grad | erledigt (quasistatisch) |
| WEYL-LINEAR-2 | WM0, WM1 ja (begrenzt trennscharf); WM2 nach Plan ja, nach Wortlaut uneindeutig; kein Gleichteil mehr | parken |
| FADEN-DIM-1 | F1 ja; F2 nach Plan knapp ja (Grenze 4 bei Rauheit 0,6), nach Wortlaut nein; Planluecke Rauheit | weiter, FADEN-DIM-2 (laeuft) |
| GAMMA-NETZ-L | gamma = 2 kappa'/kappa_g, im Projekt schon gerechnet (Leitung uebersah es); TT-Zweige anisotrop 3,2 bis 10,6 % | erledigt; weiter mit TT-ISO-1 (laeuft) |
| LICHT-FINN-NETZ-1, ZWEI-KOPIEN-1, TT-ISO-1, FADEN-DIM-2 | laufen | in Runde 44 |

- **Rueckfragen an Finn (offen):**
  - R1 aus GAMMA-NETZ-L: Steckt die Energie einer Masse in der Regel je Ecke, und tickt Materie im Takt der Ecke?
  - Gilt der neue Schwerpunkt "Gesamt-Teilchenmodell statt Q-Ball-Verfeinerung" auch fuer uns?
- **Methodik:**
  - Drei Rueckfaelle bei vorab ableitbaren Vorhersagen bzw. fehlender Projektsuche (QBALL-DREIPOL-2, GUERTEL-FELD-STAB-2, GAMMA-NETZ-L), im Gedaechtnis nachgetragen.
  - Mehrere Agenten schrieben kurz in den Scratchpad der Leitung (selbst angezeigt, geloescht).
  - Ein Sitzungslimit unterbrach alle Agenten (19:53 bis 21:20).
- **Weiter in RUNDE-44.md.** Diese Datei ist ab jetzt Journalquelle und bleibt unveraendert.
