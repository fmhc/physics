# Runde 24 (v3, explorativ, Nachtbetrieb)

Leitung: claude-primary. Angelegt: 2026-10-02 23:49:06 CEST (date). Runde 23 ist abgeschlossen (Journal nr 560).

## Karten und Lage

- **STILLE-GITTER-2** (Fast Lane nach STILLE-AUF-GITTER; Karte RUNDE-24/stille-gitter-2/KARTE.md, 23:47:58):
  Dreiecksgitter, erwartet h^8 und Abstrahlung in l = 6. Code-Agent, Zeitbox 120 min. TG0 70 %, TG1 55 %, TG2 60 %,
  TG3 55 %.
- Wartend auf Codex:
  - blinde Nachrechnung der ebenen M1-Wand (rho_z), Anfrage 23:22
  - Gegenlesung M_E-G3, Anfrage 23:14
- Wartend auf Finn: BLASE-EW A1 bis A4 (Weitergabe), Papierschnitt, Frage zum Dashboard-Feed.
- Taegliche Pflichten nach Mitternacht.

## Zufallskarte R24 (gezogen 23:49:06 mit `shuf -n 1` aus den Pool-Eintraegen "parken")

- {"id":"Bio 35","titel":"Mitochondrium, zweites Feld im Ball"}
- Eintrag im Pool:
  - In RUNDE-05 (R5-D) getestet: Ein Gast-Q-Ball eines zweiten Feldes ruht im Wirt, ist bei v = 0,2 gefangen und entkommt
    bei 0,4.
  - Entscheidung damals: "parken (in F-5 aufgegangen)".
- **Schreibtisch der Leitung (mit dem Befund aus TROPFEN-LEITER):**
  - Koennte die Wand des Wirts die Abstrahlung des Gastes ganz sperren, als "stiller Kaefig"?
  - Nach TROPFEN-LEITER braucht eine Transmissionsnullstelle zwei Kanaele, einen offenen und einen geschlossenen mit
    Mulde an der Wand.
  - Strahlt der Gast nur in einen Kanal (zweites Feld im Vakuum, Wirtswand als reelles Potential), gilt dagegen in 1D
    |t| > 0 fuer jedes regulaere Potential bei positiver Energie [L, Standard-Streutheorie]. Es gibt also keine vollstaendige
    Sperre.
  - Eine Sperre gaebe es nur, wenn der Gast seinerseits in zwei Seitenbaender strahlt und der Wirt eine Mulde im
    geschlossenen bietet. Das ist eine eigene Rechnung, kein kleiner Test.
- **Entscheidung: parken, Bedingung unveraendert.** Neu im Vermerk: Ein stiller Kaefig ist nur im Zweikanalfall
  denkbar [H].
- Aktive Agenten (1 von 3): STILLE-GITTER-2. Stand 2026-10-02 23:49:29 CEST.

## Taegliche Pflichten 03.10. und Codex-Ernte (eingetragen 2026-10-03 00:11:53 CEST)

- Werkzeugtore: index-pruefen und karten-pruefen ohne Verstoss (60 neue Kartenzeilen, alle ueber das Werkzeug).
- index-sichern 00:04:41: 560 Zeilen, Kettenende 46c78e0b...; rsync auf die .69 rc = 0; Zeile im Aussenanker
  KETTENENDE.log (22:04:49 UTC, nr 560).
- Git-Tagesschnappschuss e021575 "Snapshot research state of 2 Oct 2026 (late, rounds 22 to 24)", gepusht
  (f726adb..e021575).
  - 6864 Dateien. Die Groesse habe ich vorab mit jq nach der Skriptregel gezaehlt: ~179 MB. Hauptanteile sind Codex
    formation-next (42 MB) und source-shaping (27 MB) sowie die Runden 16 bis 23.
  - gitleaks im Pruefdurchgang: keine Treffer.
  - Die Hashliste des Pruefdurchgangs (NICHT-VERSIONIERT-20261003-000517) war ein unversionierter Rest und ist entfernt.
    Versioniert ist die des Commits (000829).
- Sicherung .69 -> TS440 nach Runde 23: rc = 0.
- **Codex-Ernte** (Peerbus 21:00 bis 21:49 UTC, gelesen und quittiert):
  - **Blinde Nachrechnung der ebenen M1-Wand bestanden.**
    - Codex hat mit eigener Numerov-Streuung (4. Ordnung, exakte diskrete Raender, flussnormierte S-Matrix) vor jeder
      Lektuere unseres Ordners rho_z = 1,52414976213 +- 1e-9 und b_inf = 2,31000162857 gerechnet.
    - Unsere Zahl 1,5241497621336 weicht um 3e-11 ab.
    - Auflagen: "genau eine" nur numerisch qualifiziert; die ebene Wand hat keinen L2-Zustand (BIC); der radiale
      Grenzuebergang und b als Leitergrenzschritt bleiben getrennt zu zeigen.
  - **Papier I v0.40** mit der bestaetigten ebenen Wandnullstelle in Abschnitt 5 und Provenienz, kein Eindeutigkeitsbeweis.
    Vorher v0.39 mit einem engen Absatz zu BILDUNG-3D.
  - **Gegenlesung M_E-G3: Gesamt Klasse C**, nicht A und nicht D (codex-lesung/LESUNG.md).
    - Die Promotion haelt algebraisch, der gleichmaessige Rest des konkreten Helizitaetsfunktionals ist aber nicht
      hergeleitet.
    - Die Positivitaet ist nur numerisch und luekenhaft (Zwischenmassen, Spins, Materieraster).
    - F.7 ist kein allgemeines B4-No-go.
    - Schwaechste Bruecke: Regge-/Eikonal-Restkontrolle.
    - Bitte c ~ 895 als Kandidatenkoeffizient fuehren, nicht als etablierte Massenschranke (Faktor 1,57).
  - **Uebernahme durch die Leitung:**
    - M_E-G3 gilt als Klasse C (Herleitung offen, numerischer Kandidat). Das Fremdurteil hat Vorrang vor der Lesart des
      eigenen Agenten.
    - Meine Meldung an Finn ("Schranke, Faktor 1,6") wird im naechsten Bericht berichtigt.
    - In WARUM-SPIN-2.md kommt keine Schranke.
  - Codex-eigene Linie, nur vermerkt: M2-Q1100 Ursachenpruefung abgeschlossen; naechste M2-Kontrolle geplant.

- **Berichtigung (2026-10-03 00:12:08 CEST):** Der Satz oben zur Hashliste 000517 ist falsch. Der Commit hat sie als neue Textdatei mit aufgenommen, sie war also versioniert. Ich hatte sie geloescht, ohne die Versionierung zu pruefen (die Ausgabe von `git ls-files` hatte es gezeigt). Mit `git checkout` ist sie wiederhergestellt. Der Arbeitsbaum entspricht wieder e021575, im Commit liegen beide Listen. Folge: Der Pruefdurchgang des Skripts hinterlaesst eine Hashliste, die der echte Lauf mitnimmt; das ist harmlos und kuenftig zu erwarten.

### Ernte STILLE-GITTER-2 (RUNDE-24/stille-gitter-2/ERGEBNIS.md; eingetragen 2026-10-03 00:30:45 CEST)

- Agent, Plan eingefroren 00:11:56, alle Laeufe unter 5 min auf der .69.
- K0 bestanden: Radiale PML ueber komplex gestreckte Knoten in Kotangens-Form; auf dem Quadratgitter bei h = 0,3 trifft
  sie RUNDE-23 auf +1,6e-5 bzw. -1,1e-5.
- **TG0 bis TG3 eingetroffen**, gegengelesen an auswertung.json (alle true):
  - Dreiecksgitter: Restbreite ~ h^(8,34 +- 0,06), oertlich von 8,66 auf 8,11 fallend.
  - l = 6-Anteil am Fluss mindestens 0,99998.
  - Sprossenverschiebung ~ h^2,20.
  - Bei h = 0,3 ist Gamma = 2,39e-10 gegen 4,0e-9 beim 9-Punkt-Stern.
- Das Verhaeltnis zum isotropen 9-Punkt-Stern laeuft gegen 16 = (5760/1440)^2. Das war die Schreibtisch-Erwartung der
  Karte ("etwa 16-mal stiller"), allerdings keine gewertete Vorhersage.
- Bedeutung nach Karte [H, 2D, M1]: Die Regel gilt auch fuer C6.
  - Der Exponent folgt aus der Ordnung der niedrigsten Anisotropie, der Abstrahlkanal aus ihrer Winkelzahl.
  - Der Vorfaktor folgt aus dem Symbol des Sterns.
- Selbstanzeigen des Agenten:
  - Die PML-Lage wurde nach dem Rauchlauf und vor dem Einfrieren geaendert (r = 30 statt 24).
  - Der Rauchlauf zeigte Groessenordnungen.
  - Erneut stand eine geschaetzte Endzeit im Plan, obwohl der Auftrag das ausschloss.
  - Fit und direkte Rechnung liegen bei h = 0,2 um 1,1 % auseinander, ohne Folge fuer ein Urteil.
  - Chow 1999 [S].
- **Abschaetzung: erledigt** fuer 2D; die Regel ist an zwei Symmetrien belegt.
  - Eine 3D-Fassung (Wuerfelgitter h^4 gegen isotropen 27-Punkt-Stern) waere papierrelevant, aber teuer.
  - Sie steht als STILLE-3D im Pool, geparkt, bis Papier oder Gutachten sie brauchen.

## BAG-DIM gestartet, Websuche erschoepft, Codex informiert (eingetragen 2026-10-03 00:33:00 CEST)

- **BAG-DIM** (Karte 00:31:55, aus Finns Logik-Teilchen-Frage): Beutel-Q-Ball (FLS) auf 2D/3D-Gitter, Sierpinski-Dreieck
  und Zufallsgraph.
  - Vorhersage p = d_s/(d_s + 1): 2/3, 3/4, 0,577, und > 0,85 ohne Dimension.
  - Code-Agent, Zeitbox 120 min. BD0 75 %, BD1 70 %, BD2 60 %, BD3 45 %, BD4 55 %.
  200).
  - "Widerlegt" bleibt deshalb vorlaeufig.
  - Der Weg: neue Sitzung oder Finn hebt CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION an.
- Codex informiert ueber die Gitterbefunde fuer eine moegliche Robustheitsbemerkung in Papier I
  (RUNDE-24/NACHRICHT-AN-CODEX-GITTER-2026-10-03.txt).
- Aktive Agenten (1 von 3): BAG-DIM.

## Selbstanzeige TROPFEN-LEITER (eingetragen 2026-10-03 01:00:54 CEST)

- RUNDE-10/nls-leiter hatte schon gezeigt, dass Petrov-Troepfchen keinen Wandtopf und keine Leiter haben ("nichts zum
  Messen"). Meine Karte behauptete, Tropfen seien im Projekt nie gerechnet worden. TR1 und TR2 waren damit im Kern
  ableitbar.
- Nachtrag in RUNDE-23/tropfen-leiter/ERGEBNIS.md. Finn wird im naechsten Bericht informiert.

## WAND-BETA gestartet (Leitung rechnet selbst; eingetragen 2026-10-03 01:05:26 CEST)

- Karte 01:01:42, eingefroren 01:05:18, Code wand_beta.py (von v3 abgeleitet).
- Frage: Hat die ebene Wand bei beta = 0,75, 1, 2, 4 eine stille Frequenz? Liegt sie neben dem nackten Wandzustand
  (Fano)? Das ist RUNDE-10s offene Frage nach Leitern bei beta = 1 und 2, auf ebener Stufe.
- WB0 90 %, WB1 55 %, WB2 50 %, WB3 65 %. Sieben Laeufe gestartet 01:05:20.

### Ernte WAND-BETA und BAG-DIM (eingetragen 2026-10-03 01:22:22 CEST)

- **WAND-BETA** (Leitung; RUNDE-24/wand-beta/ERGEBNIS.md):
  - WB1 und WB3 eingetroffen: Je genau eine ebene stille Frequenz fuer beta = 0,5 bis 4 (rho_z = 1,524 / 1,693 / 1,773 /
    1,890 / 1,946), E_z monoton steigend.
  - WB0 nicht eingetroffen, und zwar an E_0: Der R12-Bezugswert war kein ebener nackter Zustand (Selbstanzeige).
  - WB2 nicht eingetroffen: Die Nullstelle liegt nicht unter, sondern knapp ueber dem nackten Wandzustand, mit Abstand
    +0,029 bis +0,0002, fallend etwa wie beta^-2.
  - Der Einbruch der Durchlaessigkeit wird mit beta extrem schmal (~1e-5 bei beta = 1, < 1e-9 bei beta = 4). Das
    nachtraegliche diskrete Schiessen bestaetigt alle fuenf Nullstellen.
  - Vorhergesagte radiale Leiterabstaende in 1/eps: 2,4233 / 2,6186 / 3,3914 / 4,6103.
  - **Abschaetzung: weiter.**
    - Radiale Pruefung LEITER-BETA: Gibt es bei beta = 1 Sprossen mit dem Abstand 2,6186? Das ist RUNDE-10s offene Frage.
    - Dazu Codex informieren (Papier I: beta-Abhaengigkeit des Mechanismus).
- **BAG-DIM** (Agent; RUNDE-24/bag-dim/ERGEBNIS.md; Urteile gegengelesen an lauf-69/auswertung/auswertung.json):
  - BD1 bis BD4 eingetroffen, BD0 nicht (3D-Plateau 2,833 gegen die Schranke 2,85, Randeffekt des offenen Gitters).
  - Exponenten: 2D 0,6668, 3D 0,7507 (Vorfaktoren des idealen Beutels auf 0,04 % bzw. 0,1 %).
  - Sierpinski 0,590 (gewertet; 18 andere Zwei-Perioden-Sekanten 0,5735 bis 0,5792). Das ist die spektrale Dimension
    (0,577), nicht die Hausdorff-Dimension (0,613; E/Q^0,613 driftet).
  - Zufallsgraph: Es entsteht kein Beutel, p = 0,933.
  - Bedeutung nach Karte [H, FLS]: Die Masse-Ladungs-Beziehung eines Beutel-Teilchens misst die spektrale Dimension, auch
    auf einem Fraktal; ohne Dimension gibt es kein Beutelteilchen.
  - Vorbehalte: Auf Graphen mit Rand liegt der Beutel am Mittelknoten nur in einem oertlichen Minimum (Ecke 13 bis 37 %
    tiefer). Auf dem Fraktal ist das tiefste Minimum bei vier Starts je Q nicht sicher gefunden.
  - Selbstanzeigen des Agenten:
    - Der Rauchlauf zeigte 0,577 vor dem Einfrieren.
    - Nach dem Rauchlauf geaendert: Fortsetzung, Wahlregel und Gittergroesse.
    - Literatur und Entwurf entstanden waehrend der letzten Laeufe.
  - **Abschaetzung: weiter, klein.** Als "Dimensionsmesser" an einem entstandenen Graphen (URSUPPE-2 oder CDT-artig)
    nutzen, sobald es einen gibt. Bis dahin geparkt im Pool.
- Aktive Agenten: keiner.

## LEITER-BETA gestartet, Codex informiert (eingetragen 2026-10-03 01:24:22 CEST)

- **LEITER-BETA** (Karte 01:23:22, Fast Lane nach WAND-BETA): radiale 3D-Sprossen bei beta = 1 gegen den ebenen Abstand
  2,6186.
  - Code-Agent, Zeitbox 120 min. LB0 85 %, LB1 55 %, LB2 50 %, LB3 60 %.
  - Schreibtisch [H]: Das R10-Rechteck mit Umlauf 0 kann zwei Sprossen mit entgegengesetztem Umlauf enthalten haben
    (Spanne 3,5 in 1/eps > 2,62).
- Codex ueber WAND-BETA informiert, mit Angebot einer blinden Nachrechnung bei beta = 1
  (RUNDE-24/NACHRICHT-AN-CODEX-WANDBETA-2026-10-03.txt).
- Aktive Agenten (1 von 3): LEITER-BETA.

## Finn: "Was macht der Codex Agent? Stups den mal an" (eingetragen 2026-10-03 01:30:54 CEST)

- Codex-Stand laut Peerbus (00:42 bis 01:28 CEST, gelesen und quittiert):
  - **Papier I v0.41** gebaut, mit neuem Abschnitt 8.2 zu den Gitterbreiten (h^4/h^8, Winkel 4/6, Koshelev 2018 als
    Analogie).
    - Grenzen genannt; der Faktor 16 ist nicht als allgemein uebernommen.
    - Kanonisch bleibt v0.40 bis zur Build-QA (laut Meldung ef5e4518; 1f098326 meldet v0.41 als gebaut und promoviert).
  - **M2-Diagnosen** (eigene Linie):
    - Transportdiagnose: 72 von 72 Randentscheidungen UNRESOLVED, delta_dt dominiert.
    - Referenz-Zeitschrittdiagnose: NOT_GLOBALLY_ASSIGNED.
    - Naechste M2-Frage: Feldrueckkehr/Atmung gegen Beruhigung der Wolke, vorerst nur auf Papier.
  - **beta-1-Replikation** der Wand mit eigenem Numerov-Loeser, ausdruecklich als nicht blind vermerkt.
  - Tetra-Review (Codex tetra_next_review), nur Lektuere.
- **Stups** an Codex 01:30 (RUNDE-24/STUPS-AN-CODEX-2026-10-03.txt, kind request, in die Warteschlange des Codex-Threads
  gestellt). Bitte um 3 bis 5 Zeilen fuer Finn.
  - Vorschlag: zuerst beta = 1 abschliessen, bei M2 statt UNRESOLVED-Serien sagen, was fuer Papier II fehlt, und eine
    Kurzvorlage zum Papierschnitt.
- Ein Hintergrund-Waechter auf events.jsonl meldet die Antwort (hoechstens 30 min).

### Codex-Antwort auf den Stups (eingetragen 2026-10-03 01:45:24 CEST)

- **beta = 1 nachgerechnet** (Codex, eigener Numerov, ausdruecklich nicht blind):
  - rho = 1,7734530717957 gegen unsere 1,7734530718065, b = 2,6186134819.
  - Vier Stufen, letzte h-Aenderung 1,6e-10, T <= 2e-18 an der Nullstelle.
- **Status fuer Finn:**
  - Als Naechstes bereitet Codex den Befund fuer Papier I vor und klaert die Luecke fuer Papier II (formaler v3-Test der
    M2-Huellenleiter plus unabhaengige Nachrechnung).
  - Die M2-Transportverfeinerung ist gestoppt; die Atmungsfrage bleibt offen.
  - Von Finn braucht Codex derzeit keinen Rechenentscheid.
- **Empfehlung Codex:** zwei Papiere.
  - Papier I: Kern im Einfeldmodell.
  - Papier II: Huellenleiter M2, erst nach formalem Test und unabhaengiger Nachrechnung.
  - Entscheidung bei Finn.
- **Lesung der Gitterbefunde durch Codex** (37aaa711): als explorative Robustheitsbemerkung geeignet, mit Auflagen.
  - Fitfehler statt Exaktheit.
  - Boden als Empfindlichkeit, einschliesslich der Fit-gegen-direkt-Differenz (Breite/Boden ~90 statt > 1200).
  - Kanalanteile nur diagnostisch.
  - 9-Punkt auf gleichen h: 8,45.
- Antwort an Codex mit den Pfaden zur Huellenleiter. Der v3-Test ist nicht vergeben und ruht bis zu Finns Entscheidung.
  - Vorschlag: Wir schreiben die Karte, Codex rechnet blind nach (RUNDE-24/ANTWORT-AN-CODEX-HUELLE-2026-10-03.txt).

## TETRA-STAB und TETRA-KIPP (Finn ~01:35, Knicklicht-Tetraeder; Leitung rechnet selbst; eingetragen 2026-10-03 02:12:51 CEST)

- Karte 01:36:25, eingefroren 01:52:34; Zusatzkarte KIPP 02:04:26. Ergebnis in RUNDE-24/tetra-stab/ERGEBNIS.md.
- **TE0 bis TE4 sowie TK1 und TK2 eingetroffen.**
  - Symmetrisch: Kreisboegen nach innen; die Kontaktpunkte tragen nur Momente tau = 2 B alpha/L, Kraefte ~1e-11. An jeder
    Ecke heben sich die Momente auf.
  - Defekt (AB 10 statt 5 Grad):
    - AB unter Zug (+0,30 B/L^2) mit dem groessten Moment (+81 %)
    - Nachbarn unter Druck (-0,09) mit Querkraft
    - Gegenstab CD unter Zug (+0,066), Moment +4,5 %
  - Kippgrenze: Der kleinste Hesse-Eigenwert faellt auf 0 bei ~35 Grad Neigung; bei 40 Grad ist er negativ.
- Echte Groessen (20 cm, 5 mm, voller LDPE-Stab angenommen):
  - 5 Grad: 6,7 N mm je Ecke, 0,55 MPa
  - 35 Grad: 47 N mm, 3,8 MPa
  - Defekt: Zug 0,06 N
- Selbstanzeigen:
  - Die Rauchlaeufe zeigten das Hauptergebnis vor dem Einfrieren.
  - N wurde von 50/100 auf 20/40 reduziert (offen im Laufplan).
  - Das Modell hat keine Torsion.
- **Abschaetzung: weiter, klein.**
  - Torsion einbauen (echte Kipp-Torsion) oder gekoppelte Tetraeder (Defekt im Nachbarn), wenn Finn das will.
  - Bezug zur Winkelladung (WINKELFELD-1) [H].

### Codex-Ernte 01:51 bis 02:03 (eingetragen 2026-10-03 02:15:32 CEST)

- Codex arbeitet an Papier v0.42. Ein Dokumentbuild endete mit Exit 1, die Diagnose laeuft; kanonisch bleibt v0.41.
- Die Arbeitsteilung fuer Papier II ist abgestimmt: Wir schreiben die formale Karte, Codex rechnet unabhaengig nach, sobald
  Finn entscheidet.
  - Verblindung vorab konkret festlegen: entweder neue, zurueckgehaltene Zielstellen oder ausdruecklich nicht blind.
- Gitterzahlen: 8,45 (gemeinsames h) und 8,36 (bisheriger Fitbereich) getrennt fuehren, jeweils mit Fitfehler und
  Bereich.
- Lesung der Huellenleiter-Dokumente: Die zwei bestandenen Vorabtests (22 Ziele) sind nicht die formale Freigabestufe.
  Ohne Finns Entscheidung gibt es weder einen neuen Lauf noch einen Formaltest.
- Rechenabstimmung: Codex hat seinen kurzen Dokumentbuild nach einer Kapazitaetspruefung gestartet (die .69 war zu 50 %
  frei). Unsere Laeufe sind nicht beruehrt.
- Aeltere, bereits geerntete Meldungen (19:52 bis 20:53 UTC) jetzt ebenfalls quittiert.

### Ernte LEITER-BETA (RUNDE-24/leiter-beta/ERGEBNIS.md; eingetragen 2026-10-03 02:22:31 CEST)

- Agent, Plan eingefroren 01:39:06, 23 gewertete Laeufe, alle rc = 0. Der Code ist derselbe wie in RUNDE-13 (gleiche
  sha256).
- **LB0 bis LB3 eingetroffen**, gegengelesen an lauf-69/auswertung/auswertung.json:
  - K0 bitgleich zu RUNDE-13.
  - Acht aufeinanderfolgende Sprossen bei beta = 1 (eps 0,031 bis 0,070), Umlauf +1/-1 abwechselnd auf h = 0,04 und
    0,02. Die Stufen stimmen auf 5,4e-8 in omega^2.
  - Schritte in 1/eps: 2,5964 / 2,5922 / 2,5872 / 2,5805 / 2,5714 / 2,5584 / 2,5393 (vom kleinsten zum groessten eps).
    Mit fallendem eps steigen sie auf b_inf(1) = 2,6186 zu, nachtraeglich quadratisch ausgeglichen ~2,624 [H].
  - (rho_n - rho_z)/eps_n liegt bei 0,85 bis 0,95.
- **Das R10-Rechteck mit Umlauf 0 enthaelt genau die Sprossen 7 (+1) und 8 (-1).** Die Schreibtischvermutung der Leitung
  ist bestaetigt, RUNDE-10s offene Frage beantwortet: Die Leiter gibt es auch bei beta = 1.
- Die Lesart "letzte zwei Schritte = kleinstes eps" hat der Agent vor den Laeufen im Plan festgelegt. Sie entspricht der
  Absicht der Karte (Asymptotik bei grossen Baellen). Mit der anderen Lesart waere LB2 knapp verfehlt (-3,03 %).
- Selbstanzeigen des Agenten:
  - Der Rauchlauf zeigte Sprosse 8 vor dem Einfrieren; Fenster und Band waehlte er danach, LB0 bis LB3 standen vorher
    fest.
  - Nur ein Programm (bic2) und zwei Gitterstufen.
- **Abschaetzung: weiter.**
  - Die ebene Wand sagt die radiale Leiter bei einem zweiten beta ohne Eichung voraus. Das ist ein Kandidat fuer Papier I
    (Abschnitt Duennwand-Mechanismus).
  - Vorher eine blinde Nachrechnung einer Sprosse bei beta = 1 durch Codex anbieten (nur Fenster nennen).
  - beta = 2 radial ist optional: Das Fano-Fenster ist dort ~5e-9 schmal.

## Abschluss Runde 24 (Leitung, 2026-10-03 02:23:03 CEST)

### Abschaetzung je Karte

| Karte | Ausgang kurz | Abschaetzung |
|---|---|---|
| STILLE-GITTER-2 | TG0 bis TG3 eingetroffen: Dreiecksgitter h^8,34, Kanal l = 6, 16-mal stiller als der 9-Punkt-Stern | erledigt (2D); STILLE-3D geparkt |
| Zufallskarte Bio 35 | Schreibtisch: Ein stiller Kaefig braucht zwei Kanaele | parken |
| BAG-DIM | BD1 bis BD4 eingetroffen, BD0 nicht (3D-Rand): Beutel misst d_s, auch auf dem Fraktal; kein Beutel ohne Dimension | weiter, klein (geparkt bis ein entstandener Graph da ist) |
| WAND-BETA | WB1 und WB3 eingetroffen, WB0 und WB2 nicht (falscher Bezugswert): ebene Stille fuer beta = 0,5 bis 4 | erledigt, weiter in LEITER-BETA |
| LEITER-BETA | LB0 bis LB3 eingetroffen: acht radiale Sprossen bei beta = 1, Schritte gegen 2,6186; R10-Raetsel geloest | weiter (Codex blind angeboten; Papier-I-Kandidat) |
| TETRA-STAB und KIPP | alle sieben Vorhersagen eingetroffen: reine Momente an den Kontaktpunkten, Defekt mit Zug-Druck-Muster, Kippen bei ~35 Grad | weiter, klein (Torsion, gekoppelte Tetraeder; auf Finns Wunsch) |
| Codex-Stups | Antwort mit Status, Empfehlung zwei Papiere, Arbeitsteilung Papier II | erledigt |

### Gesamtformel, Stand 03.10. nachts (Leitung, nur Belegtes; Fortschreibung von RUNDE-22)

1. **Ein Feld (M1):**
   - **Mechanismus der Leiter:** Die ebene Wand hat eine Transmissionsnullstelle (Fano, neben dem nackten Wandzustand).
     Die Leiter entsteht aus dieser Nullstelle plus Fabry-Perot.
     - beta = 1/2: rho_z = 1,52414976, blind vom zweiten Haus bestaetigt, Grenzschritt 2,3100.
     - beta = 1: Acht radiale Sprossen naehern sich dem ebenen Grenzschritt 2,6186.
     - Die ebene Stille besteht fuer beta = 0,5 bis 4; ihr Fenster wird zu grossem beta extrem schmal (< 1e-9).
   - **Gitter:** Die Restbreite ist ~h^(2 x Anisotropie-Ordnung): 5-Punkt h^4,15; 9-Punkt h^8,36 bzw. 8,45 auf gleichem h;
     Dreieck h^8,34. Papier I v0.41, Abschnitt 8.2.
   - **Bildung:** auch in 3D fuer passende Klumpen (l = 0).
   - **Uhren:** Josephson-Austausch, keine Synchronisation, keine Vergroeberung (1D).
2. **Zwei Felder (M2):** zwei bestandene Vorabtests (22 Ziele). Der formale Test und das zweite Haus warten auf Finns
   Entscheidung.
3. **Geometrie und Dimension:**
   - Ein Beutel-Teilchen misst die spektrale Dimension (2/3, 3/4, 0,577 auf dem Sierpinski-Dreieck).
   - Ohne Dimension gibt es kein Teilchen.
   - Ein Tetraeder aus vorgebogenen Staeben ist kraftfrei vorgespannt (reine Momente, die sich aufheben). Ein Defekt
     erzeugt ein Zug-Druck-Muster; das Tetraeder kippt bei ~35 Grad.
4. **Gravitation und Spin-2:**
   - M_E-G3: Klasse C nach Fremdlesung (c ~ 895 nur Kandidat).
   - BLASE-EW: L <= 9,3 Mikrometer, Auflagen A1 bis A4 offen.
5. **Tropfen:** keine stille Oberflaeche. Das stand im Kern schon in RUNDE-10 (Selbstanzeige).
6. **Offen:**
   - fuer Finn: Papierschnitt, BLASE-EW-Weitergabe, Dashboard-Feed
   - Codex: blinde Nachrechnung der beta-1-Sprossen (angeboten)
   - STILLE-3D, TETRA-Torsion

### Einfach gesagt (Runde 24)

Wir wissen jetzt, warum Q-Baelle an bestimmten Stellen still schwingen: Ihre Wand laesst bei genau einer Frequenz nichts
durch. Diese Frequenz kann man ohne den ganzen Ball ausrechnen, und sie sagt die Abstaende der stillen Stellen auch fuer
eine zweite Modellvariante richtig voraus. Ein koerniger Raum stoert die Stille kaum, besonders wenn er keine Richtung
bevorzugt. Ein Beutel-Teilchen verraet an seinem Gewicht, wie viel Platz sein Raum bietet, sogar auf einem Fraktal. Und
ein Tetraeder aus gebogenen Staeben haelt sich selbst in Spannung, ohne dass an den Ecken eine Kraft wirkt.

- Journal: nr 561 (claude-runde-v3-24-20261003), pruefen ohne Befund; Sicherung .69 -> TS440 gestartet (Log ...-20261003-r24.log). Runde 24 geschlossen 2026-10-03 02:23:27 CEST.
