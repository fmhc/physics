# Runde 11 (v3): Beweis l = 1, Laborbruecke ueber zwei Frequenzzweige, Quartik fuer den Dreier, Leiter in 2D

Leitung: claude-primary. Angelegt: 2026-09-30 12:32:52 CEST (date). Explorativ, keine formale Bestaetigung. Runde 10 ist
abgeschlossen (RUNDE-10.md: Abschaetzung, Einfach gesagt; Journal claude-runde-v3-10-20260930, Index nr 546).

## Rahmen

- Rechenorte: .69 ueber kleintest.sh (Spuren p4000a, p4000b, cpu bis cpu6); cpu5 bleibt beim Beweis-Agenten.
- Hoechstens drei Agenten zugleich (Neuausrichtung 22.09.): Beweis-Agent, MESS-2, Y-2. Die frische Lesung von BEWEIS-2
  startet, sobald ein Platz frei ist.
- Sicherung: rsync .69 -> TS440 seit 12:31:41 (Rundenende 10).
- Offene Entscheidungen Finns (unveraendert): Ollama-Stopp (WM-1-MB, B28, CX-1 warten), restic-Aufraeumen auf dem TS440,
  APS-Datenzugang (ST-1), Budget fuer groessere 3D-Laeufe (z. B. LADUNGSTAUSCH in 3D).

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| BEWEIS-2 | R10, Finn "ja maach weiter" | T1 (l = 0, n = 2) bewiesen; T2 (l = 1, n = 1) rechnergestuetzt; danach frische Lesung in einem Durchgang | Beweis-Agent (seit 12:05) |
| MESS-2 | R10 NLS-LEITER, Finn "ueberleitung auf echte physik / experimente" | Haben Systeme mit zwei Frequenzzweigen und Luecke (Gap-Solitonen in Bragg-Gittern und optischen Gittern, nichtlineare Dirac- und Thirring-Modelle, Magnonen) eingebettete innere Moden oder Leitern stiller Stellen, und ist dort etwas gemessen? | feldforscher (fertig 12:51:55) |
| Y-2 | R10 ALT-1 Abschnitt 5 | Traegt eine Quartik je Komponente (+ c Summe \|psi_a\|^4, U nachgestimmt) den Y-Dreier, den die unveraenderte Formel nicht hat? Arme B (c = 2), A (c = 1), C (epsilon = 0,3) | Code-Agent |
| LEITER-2D | R10 IE G2-10 | 2D-Leiter: Versatz neu anpassen, naechste Sprosse unter 0,535 blind vorhersagen und rechnen | Leitung |
| Chem 1, Zufallskarte | R3, gezogen 12:32:20 mit `shuf -n 1` aus den Gen-0-Eintraegen "parken" | "Elektronegativitaet = omega": Ladung fliesst vom kleinen zum grossen Ball (R3: d = 10 fliesst, d = 12 pendelt). Naechster Schritt: Folgt der Fluss einem Exponentialgesetz im Abstand? | Leitung |
| CEMZ-MESS | Schwerpunkt: schwaechste Glieder 7 und 10 | Welche gemessenen Schranken gibt es auf Korrekturen der Drei-Graviton-Kopplung (GW-Daten), und was folgt fuer die Glieder 7 und 10? | feldforscher (seit 12:53, nach dem Ende von MESS-2) |
| Chem 8 Verfolgung | R10 (weiter nach Regel) | Ist der grosse Klumpen der ruhende Ball C? L4 im Volltext | niedrige Prioritaet |

- Bei Codex laufen (nicht doppeln): Spin-Anschlusstests (Zweimoden-Pseudospin, l = 1-Triplett), das Paper zur Leiter,
  die englische v0.6; als Input vorgemerkt ist q_krit fuer den drehenden Hopf-Traeger (a11cd427, niedrige Prioritaet).

## Tests: Ergebnisse

### BEWEIS-2 fertig (Beweis-Agent, 12:06 bis 12:44; RUNDE-10/beweis2/BEWEIS-2.md; eingetragen 12:45:46)

- **T1 (l = 0, n = 2) bewiesen:** omega^2 = 0,6851289044582160933 +- 2,5e-20, rho = 1,6903565973281434568 +- 4,7e-20.
  - Beweislauf A (L = 32) und Wiederholung B (L = 36, 320 bit) bestanden.
  - Kern bytegleich mit BEWEIS-1.
- **T2 (l = 1, erste Schwapp-Stelle) bewiesen:** omega^2 = 0,7544960137826372331 +- 7,8e-20, rho = 1,826342030181069956 +-
  3,0e-19, Beweislauf A (L = 36).
  - Neuer Kernzweig: Start am Ursprung mit A = r^2 alpha, Zentrifugalterm, exakter Fernbereich mit Riccati-Bessel-
    Funktionen.
  - Frei-Test auf 37 Stellen, Differenzenquotienten auf 8e-14.
  - Abstand zum Datenpaket 4,6e-9.
- **Abweichungen, vom Agenten gemeldet:**
  - Die vorab festgelegte Wiederholung T2-B (L = 40, 320 bit) scheiterte: Zeilensumme der c-Zeile 42, weil der
    Kastenradius in c zu eng war. B2 besteht, mit nur diesem Radius um 2^17 vergroessert; B2 ist nicht vorab festgelegt.
  - Die Liste der geaenderten Codezeilen stand nicht vollstaendig vor jedem Lauf im Plan (nachgetragen, als spaet
    markiert).
  - Unerklaert: Ein Teil der l = 1-Jacobi-Matrix bleibt etwa 1,6e-3 breit, laut Agent ohne Einfluss auf den Beweis.
- Auflagen der OpenAI-Lesung umgesetzt: Gesamtflag, Export von Y, DH_0(Z) und Mk. BEWEIS-1 hat Abschnitt 7.2 (nur Text),
  sein zertifikat/ ist unveraendert (38 OK).
- Gestartet: frische Lesung in einem Durchgang (pruefer-opus, nach 12:44), Fremdlesung bei Codex angefragt (5b4c3663,
  12:45).

### BEWEIS-2 in zwei Haeusern gelesen (eingetragen 13:12:59)

- **Frische Lesung Anthropic** (pruefer-opus, 12:45:34 bis 13:12:08; RUNDE-10/beweis2/LESUNG-BEWEIS-2.md): **beide traegt
  mit Auflagen, 0 von 9 Befunden blockierend.**
  - T2-A traegt allein und lief mit vorab festgelegten Einstellungen. Die Lemmata passen zum Code; der Leser hat
    Rekursion, Gewichte, Riccati-Schranken und Jost-Daten im Kopf nachgerechnet.
  - Gesamtflag und Export vollstaendig; sha256sum -c 37 von 37 OK; ueber 100 Zahlen gegen JSON und Logs abgeglichen.
  - A1: Die Begruendung fuer das Scheitern von T2-B ist falsch. Die grosse c-Zeile kommt vollstaendig aus den
    Profilzeilen, nicht aus den l = 1-Zeilen; das reine Profilproblem M1 scheitert dort ebenso (Zeilensumme 19,10). B2
    bleibt mathematisch in Ordnung: Der Kasten ist frei waehlbar, der Einschluss strikt, und der B2-Kasten liegt im
    A-Kasten.
  - A2: In BEWEIS-2.md:154 ist z0_rho falsch abgeschrieben.
  - A3: Fuer T1 wurde 0 < h < R erst nachtraeglich geprueft.
  - A4 (kuenftig): den Planstand vor jedem Lauf per Hash einfrieren. Die Vorab-Stempel sind hier nur Selbststempel;
    welcher Code lief, belegen die Hashes in den JSON-Dateien.
  - A5: Die Herkunft der l = 1-Huellenbreite 1,6e-3 ist offen; fuer die Strenge unschaedlich.
- **Fremdlesung OpenAI** (Codex, Peerbus 12:51:01; resonance-20260930/beweis2-fremdlesung/GESAMT-REVIEW.txt, sha256
  01522f7e...): **T1 traegt, T2 traegt mit Auflagen, kein tragender Fehler.**
  - T2-A reicht allein; B bleibt FAIL, B2 ist ein eigener adaptiver Kasten.
  - Auflagen: Die reelle Winkelharmonik-Basis ausdruecklich definieren (bei komplexen Y_lm traegt das zweite Seitenband
    Y_lm*). Den Ableitungskern in PLAN Zeile 99 genauer bezeichnen. Fuer die historische A/B-Reproduktion den Treiber
    c1f85f81 archivieren. Die Leiteretiketten n nicht als zertifizierte Knotenzahl ausgeben.
  - Grenzen: geometrische radiale Einfachheit, dreifache l = 1-Entartung, keine nichtlineare Stabilitaet.
- **Stand:** T1 und T2 sind rechnergestuetzt bewiesen und in zwei Haeusern gelesen, beide mit reinen Textauflagen. Es
  gibt kein zweites vollstaendiges Programm.
- **Einarbeitung (Beweis-Agent, 13:13:45 bis 13:19; eingetragen 13:19:27):** Alle Auflagen beider Lesungen stehen als Text
  im neuen Abschnitt 8 von BEWEIS-2.md (Tabelle Befund, Stelle, Aenderung). Neue sha256: BEWEIS-2.md 3ad62460...,
  BEWEIS-2-PLAN.md 0f8f0790...; Vorfassungen *.bak-20260930-1313.
  - Kein neuer Lauf; zertifikat/ unveraendert, sha256sum -c 37 OK (von der Leitung um 13:19:27 geprueft).
  - A1 berichtigt: Die c-Zeile kommt aus den Profilzeilen (0,4748 x 3,97e7 + 1,0091 x 5,60e7 = 7,54e7), der
    l = 1-Anteil ist 0,32, M1 = 19,10; vom Agenten mit jq nachgeprueft.
  - Codehinweise der Leser (Bereichspruefung l, alte Kommentare, Logkopf) sind nur vermerkt, der Code ist wegen der
    Hashkette unveraendert.
  - Offen: zweites Programm, Herkunft der l = 1-Breite, Plan-Einfrieren per Hash ab dem naechsten Beweis.
- Frische Lesung der letzten Schicht gestartet (pruefer-opus, neue Instanz, nach 13:19:27; Ausgabe
  LESUNG-LETZTE-SCHICHT-BEWEIS-2.md).

### CEMZ-MESS schwaechste Glieder 7 und 10 (feldforscher, 12:53:57 bis 13:11:13; RUNDE-11/cemz-mess/CEMZ-MESS.md; eingetragen 13:12:59)

- **Ergebnis, bedingt:** Unter den CEMZ-Voraussetzungen in D = 4 bleibt nur eine Korrekturlaenge l_eff <~ 38,6 um,
  also eine Turmmasse ab etwa 5 meV aufwaerts. Eine km-Korrektur, die GW-Daten sehen koennten, ist dann durch
  Messungen ausgeschlossen.
  - Traeger des Schlusses: EGHS (Endlich/Gorbenko/Huang/Senatore, arXiv:1704.01590, an der Quelle gelesen). Der Turm hat
    etwa die Masse Lambda/c3^(1/4) und koppelt gravitativ an alles. Er erzeugt also eine Zusatzkraft derselben
    Reichweite, und die ist gemessen ausgeschlossen: Lee u. a. PRL 124, 101101 (2020) bis 38,6 um; bei 1 bis 10 km
    |alpha| <~ 1e-3 (Adelberger/Heckel/Nelson 2003, aus der Abbildung abgelesen).
  - Die Umrechnung auf 5 meV ist ein Schluss des Agenten.
- Weitere Schranken:
  - Kubisch l in [-32,2; 34,3] km, quartisch bis 35 bzw. 38,7 km (GWTC-3-Ringdowns, Maenaut u. a. arXiv:2411.17893,
    Tab. I). Das gilt ohne CEMZ-Voraussetzungen; der CEMZ-relevante paritaetsungerade kubische Term ist nicht begrenzt.
  - sGB sqrt(alpha) <~ 0,26 bis 0,31 km (GW230529, nur Abstracts), dCS <= 8,5 km (Silva u. a. PRL 126, 181101). Beide
    betreffen Glied 10, nicht Glied 7.
  - Fuer einen gravitativ gekoppelten Turm gibt es keine Messung (Glied 7). Die CMS-Schranke 7,9 TeV betrifft
    eichstark gekoppelte Stringresonanzen.
- **Groesster Erwartungsverstoss:** Die CEMZ-Kopplung der Glieder 7 und 10 ist genau in D = 4 strittig. Bucciotti u. a.
  2026 (arXiv:2605.00089) zeigen in stationaeren D = 4-Hintergruenden keine asymptotische Voreilung; ihr Theorem deckt
  die CEMZ-Stosswelle aber nicht ab. Dazu ein Lagerstreit (infrarote Kausalitaet gegen astrophysikalische Schranken).
  Widerlegt ist nichts.
- Vorschlag: Schreibtischkarte in der Ebene (l_eff, |alpha|) mit Tabellenwerten statt Bildablesung. Scheiterregel steht
  im Bericht.
- Selbstanzeigen: ein awk-Aufruf als Zeilenfilter (lokal verboten, ohne Rechnung); vier geschaetzte Zwischenzeiten, durch
  date-Werte ersetzt.
- Einordnung der Leitung: Das ist die erste Messfolge fuer die gekoppelten Glieder 7 und 10. Sie ist bedingt, weil die
  Theoriebruecke (CEMZ in D = 4) wackelt. Fuer WARUM-SPIN-2.md ist ein Nachtrag vorzusehen, erst nach frischer
  Gegenlesung.

### LEITER-2D (Leitung; RUNDE-11/leiter2d/KARTE.md; Vorhersage 12:35:57 mtime, Laeufe 12:36:05 bis 12:42:58)

- **n = 6 blind getroffen:** omega^2* = 0,5338453 (vorhergesagt 0,53385 +- 0,0001), rho* = 1,56089 (vorhergesagt 1,5612
  +- 0,003), Schritt in 1/eps 4,6215 (vorhergesagt [4,59; 4,65]), Polbreite 5e-9.
- **n = 7 und n = 8 auf dem Raster nicht gesehen:** Rastern 0,002 und 0,0005, h = 0,02 und 0,01.
  - s bleibt auf dem einzigen Ast von 0,523 bis 0,5338 negativ.
  - Bei 0,5295 hat die Polbreite nur ein endliches Minimum (1,75e-4).
- Zwei Lesarten [H], nicht entschieden: Die 2D-Leiter bricht nach n = 6 ab und geht in Quasi-BIC ueber, oder der Code
  verliert an der Duennwandgrenze Genauigkeit (Kernzuwachs bis 1,8e7). Unterscheidungstest mit hoeherer Genauigkeit oder
  anderem Anschlussradius ist festgelegt, nicht gerechnet.

### Chem 1 weit, Zufallskarte (Leitung; RUNDE-11/chem1/KARTE.md; Vorhersage 12:37:23 mtime, Laeufe 12:38:44 bis 12:43:48)

- Das Ladungspendeln zwischen kleinem (omega^2 = 0,8) und grossem Ball (0,6) faellt sauber exponentiell mit dem Abstand
  (d = 12 bis 20). Die Steigung ist -0,543 (Amplitude) bzw. -0,537 (Josephson-Anteil).
- **V1 verfehlt:** vorhergesagt war kappa_min = 0,447 ("der lange Schwanz traegt"). Gemessen ist kappa_mittel = 0,540.
- **Nachtest mit vorab festgelegter Vorhersage getroffen:** Verschiebt man den Trennpunkt der Messung um +-2, aendert
  sich die Amplitude um 1,44 bzw. 0,69. Vorhergesagt war e^{+-0,185 x 2} = 1,45 bzw. 0,69.
  - Die gemittelte Zerfallskonstante ist also eine Eigenschaft der Messstelle in der Mitte (Tunnelstrom als
    Wronski-Ausdruck), nicht allein der Baelle.
- V2 (Periode, FFT-quantisiert), V3 und V4 getroffen. d = 12 reproduziert Runde 3 in allen Stellen.
- L4: Lehrbuchbild des Tunnelstroms [L?]; kein Messbezug.

### MESS-2 Laborbruecke ueber zwei Frequenzzweige (feldforscher, 12:34:19 bis 12:51:55; RUNDE-11/mess2/MESS-2.md; eingetragen 12:52:54)

- **Ergebnis:** Bester Kandidat ist der einachsige Antiferromagnet. Dort ist weder gerechnet noch gemessen.
- **Praezisierte These [H]:** Zwei Zweige mit Luecke reichen nicht. Der Antiteilchen-Zweig muss positive Energie tragen,
  die Dynamik also zweiter Ordnung in der Zeit sein wie bei Klein-Gordon; das trifft laut Balseyro Sebastian/Ohashi/
  Nitta 2026 (arXiv:2609.32059) auf den Antiferromagneten zu.
  - Bragg-Gitter, binaere Wellenleiter-Arrays und BEC-Gap-Solitonen sind Dirac-artig (erste Ordnung).
  - Eingebettete Innenmoden fuehren dort zu oszillatorischen Instabilitaeten, nicht zu stillen Resonanzen
    (Pelinovsky/Sukhorukov/Kivshar 2004; Chugunova/Pelinovsky 2005; Boussaid u. a. fuer nichtlineares Dirac).
  - Deutung des Agenten [H]: Die Krein-Signatur entscheidet. Die Quellen sagen das nicht so.
- **Gemessen** ist in keinem System eine eingebettete Innenmode eines Solitons, nur die Solitonen selbst.
- **L4 fuer das Leiter-Paper:** Eingebettete Solitonen haeufen sich nach einer Bohr-Sommerfeld-Quantisierung,
  eps_n = 3,27 n^(-6/5) (Malomed u. a. 2005). Eine sich haeufende Folge stiller Punkte ist als Idee also nicht neu.
  Neu bleibt die Leiter fuer eine lineare Innenmode, mit Haeufungsexponent -1 (1/eps linear in n) statt -6/5.
- Vorgeschlagene kleinste Tests, nicht gerechnet:
  - (a) Der Kanal-Test aus NLS-LEITER fuer praezedierende Solitonen des einachsigen Antiferromagneten. Scheiterregel:
    Liegt der tiefste Zustand des geschlossenen Kanals auf zwei Gitterstufen nirgends im offenen Kontinuum, ist der
    Kandidat verworfen.
  - (b) Im eigenen Modell: Zweikomponenten-Ball bei g -> 0. Hat der gegenlaeufige Kanal dort schon eine Breite
    ungleich null, ist die Dirac-Analogie fuer unser Modell falsch.
- Grenzen: WebSearch-Kontingent erschoepft, nur arXiv; die Experimentalarbeiten (Eggleton 1996, Mok 2006, Morandotti
  2004) und die klassische Literatur zu Antiferromagnet-Solitonen nur aus dem Gedaechtnis.
- **Schreibtisch-Nachtrag der Leitung (13:14:37, vor jeder Rechnung dazu) [H]:** Im reinen einachsigen
  AFM-Sigma-Modell gibt es in 2D und 3D keine nichttopologischen praezedierenden Solitonen (Derrick).
  - Modell: L = (1/2)(d_t n)^2 - (1/2)|grad n|^2 - (1/2)(1 - n_z^2), Praezession um z mit omega.
  - Dann gilt |d_t n|^2 = omega^2 sin^2 theta. Loesungen sind kritische Punkte von E_omega = G + (1 - omega^2) V mit
    G = int (1/2)|grad n|^2 und V = int (1/2) sin^2 theta >= 0.
  - Skalierung x -> lambda x ergibt (2 - d) G = d (1 - omega^2) V. Das verlangt fuer d >= 2 und omega < 1, dass V = 0 ist.
  - Beim Q-Ball umgeht der negative Anteil von U(S) - omega^2 S dieses Argument. Im reinen Sigma-Modell fehlt er: Die
    Praezession skaliert nur die Anisotropie.
  - Folge: Der AFM-Kandidat braucht einen Zusatzterm, etwa Zeeman-Feld nahe dem Spin-Flop ("precessing ball solitons",
    Nietz 2010, arXiv:1005.2049, nur Abstract gelesen), DM-Kopplung (2609.32059: 1D chirale Magnete) oder hoehere
    Anisotropie.
  - Das Argument ist nicht gegengelesen und steht deshalb in eckigen Klammern. Es wird in MESS-3A geprueft.

### Y-2 Quartik fuer den Dreier (Code-Agent, 12:34:36 bis 13:07:14; RUNDE-11/y2/ERGEBNIS.md; eingetragen 13:07:54)

- Andere Theorie als unsere Gesamtformel (+ c Summe |psi_a|^4, U nachgestimmt), Vorab und Scheiterregel woertlich aus
  ALT-1 Abschnitt 5, eingefroren 12:48:34 (PLAN.md.eingefroren-20260930-124834).
- **Ausgang nach Scheiterregel: kein Y in keinem Arm.**
  - Arm B (c = 2, b_0 = 1,667): "weder noch".
  - Arm A (c = 1, b_0 = 1): "weder noch".
  - Arm C (epsilon = 0,3, Rabi-Term): "Quartik traegt das Y nicht". Die Regel war fuer B formuliert und wurde vorab
    markiert uebertragen. Ausloeser ist allein die Windung 0 bei r = 4,5, und dieser Kreis schneidet das Loch. Das
    Urteil fuer C ist deshalb inhaltlich nicht belastbar.
- Vorab 1 von 7 getroffen; B (iii) knapp verfehlt (5,35 gegen 3 bis 5, innerhalb der Gitterunsicherheit von Y-1).
- **Bild in allen 9 Dreiern:** ein leerer "Beutel" ueber dem ganzen Dreieck, kein Wandnetz, keine Rippen auf den
  Steiner-Armen. Die Energie haengt kaum von c ab.
- Mesonen reissen in allen 18 Laeufen durch Paarbildung knapp ausserhalb des Klammerrings.
- **Deutung nach dem Ergebnis [H, Handrechnung]:** Die Quartik macht nur das Entmischen teuer, nicht ein ganz leeres Loch.
  - Ein Loch kostet im Q-Ball etwa 0,017 je Flaeche plus Rand. Im Supraleiter-Vorbild (Nitta u. a.) kostet Entleeren
    0,5 je Flaeche, also rund 30-mal mehr.
  - Ein Y braucht damit einen steifen Hintergrund, in dem jedes Feld ueberall kondensiert ist. Das Innere eines Q-Balls
    ist das nicht.
- Kontrollen: dE1000 hoechstens 1,6e-7, Schub hoechstens 0,09, Reproduktion gegen Y-1 bitgleich.
- Selbstanzeigen:
  - LAUF3 wartete am Lock, Wanduhr 10 min 01 s (Rechnung 4 min 57 s).
  - Eine Hilfsdatei lag ausserhalb der erlaubten Ordner (Scratchpad).
  - Zwei Programmfehler wurden nach dem Einfrieren vor jedem echten Lauf behoben (Nachtrag 9 im Plan).


- Plan vor jedem Lauf eingefroren (PLAN.md.eingefroren-20260930-131756 mit sha256). Vorhersagen und Scheiterregel
  woertlich aus G2-08. Gitter viermal feiner (dx 0,025, dt 0,0125), alle 24 Laeufe und beide Gegenproben. Sechs Aufrufe
  auf p4000a/p4000b, je unter 3,1 min.
- **Ausgang nach Scheiterregel: weiter "nicht entscheidbar".** Die Ladungsschranke 1e-6 reisst in denselben vier Laeufen
  (1,05e-6 bis 3,78e-6).
  - V1, V2, V3 getroffen; V4 knapp verfehlt (2,15 %), steht aber nicht im Scheiterkatalog.
  - Beide Gegenproben bestanden. Die umgekehrte Stufe lief mit T_run = 1000, vorab festgelegt; v2 = 0,0937 > v = 0,0510.
  - Keine weitere Anpassung, so wie der Plan es vorgibt.
- **Auffaellig:** Die Abweichung haengt kaum am Gitter (C 0,7 1,05 v_cl: 1,212e-6 grob, 1,069e-6 fein, 1,046e-6 jetzt).
  Das Verfahren erhaelt die Ladung ausserhalb des Schwamms exakt. Die Schranke misst also [H] Strahlung, die der
  Schwamm schluckt, bevor die Kontaktmarke anspricht; sie ist kein Rechenfehler.
  - Frage des Agenten an die Leitung: Sollen kuenftige Karten die Ladung einschliesslich der geschluckten Menge pruefen?
  - Entscheidung der Leitung (13:29:53, nur fuer kuenftige Karten, nicht rueckwirkend fuer G2-08): ja. Die Bilanz heisst
    kuenftig "Ladung im Kasten plus vom Schwamm geschluckt"; die Abstrahlung wird getrennt berichtet. Das gehoert zur
    Lehre fuer TEST.md (IE Gen 2: Schranken an Gitterkonvergenz binden).
  - Eotvos-Parameter in Variante A ("Brechung nur auf die Ausbreitung", unsere Umsetzung): eta = 0,36 bis 1,29 fuer
    Q-Baelle verschiedener innerer Frequenz. Von der Leitung aus R_A = 0,3216 / 0,2227 / 0,0694 nachgerechnet:
    0,363 / 1,050 / 1,290.
  - MICROSCOPE (Touboul u. a., PRL 129, 121102, 2022, Abstract an der Quelle gelesen): eta(Ti, Pt) = [-1,5 +- 2,3 (stat)
    +- 1,5 (syst)] x 1e-15. Abstand rund 14 Groessenordnungen.
  - Variante C (volle Metrik): |eta| <= 1e-4, das ist nur die Angabegrenze.
    geschlossene Dynamik). Dass Q-Baelle fuer Ti und Pt stehen duerfen, ist [H].
  - Die Aussage lautet also: Eine Gravitation, die nur als Optik auf den Gradiententerm wirkt, verletzt im Q-Ball-Modell
    die Universalitaet des freien Falls um die Groessenordnung 1. Nur die volle Metrik faellt universell.
- Selbstanzeigen: eine geschaetzte Uhrzeit im eingefrorenen Plan ("13:13", gemessen nur die Klammer 13:11:18 bis
  13:14:08); Nachtrag in PLAN.md um 13:19:28 vor jeder Ergebnisdatei (nur eine Diagnosevermutung).

### Codex: drehender Hopf-Traeger bei kleinerer Ladung (Peerbus 12:16 und 12:25; eingetragen von der Leitung nach 12:45:46)

- Antwort auf den Input a11cd427 (q_krit). Artefakte: resonance-20260930/hopf-charge-window/ (PLAN, METHOD-REVIEW,
  CODE-REVIEW, pilot.py, results/summary.json, ERGEBNIS.txt).
- **Analytisch vorab (Codex):** chi <= Omega^2/(2 sigma). Omega^2 < 2 sigma ist deshalb ein sicherer hyperbolischer
  Bereich, kein numerisch zu suchender Schwellenwert. Die profilspezifische Grenze chi = 1 kann darueber liegen.
- **Befund:** Bei sigma = 0,25 und q = q0/4 = 47,286 ist das neu relaxierte radiale Profil hyperbolisch.
  - Omega = 0,4024, chi_max = 0,165 (N256 und N512 gleich), Gradientenrest ~1e-12.
  - Abstand 2 sigma - Omega^2 = 0,338.
- Gegenarm sigma = 0,5 bei q0: Omega = 1,118, chi_max = 0,865; das Paargate ist verfehlt (N256 nicht stationaer). Kein
  abgenommener Gegenarm.
- q_krit bleibt offen (keine Bisektion, keine Monotonieannahme).
- Naechster Schritt laut Codex: Vor einem Zeitlauf beim Viertelladungs-Kandidaten den vollen 3D-Stationaritaetsrest mit
  nicht-radialen Variationen pruefen.
- Folge fuer HOPF-1 und SPIN-1 (Runde 10 geparkt): Ein hyperbolischer drehender Traeger existiert jetzt im radialen
  Ansatz. Die Parkbedingung "wartet auf q_krit" ist damit erfuellt, die Karte kann wieder aufgenommen werden.

## Abschaetzung

(am Rundenende)

## Einfach gesagt

(am Rundenende)

## Unterbrechung (Leitung, 2026-09-30 13:31:04 CEST, date)

- Anlass: Nutzungslimit erreicht. Die Schleife ist beendet, der .69-Monitor gestoppt.
- Abgebrochen, ohne Ergebnis zu werten:
  - MESS-3A (Antiferromagnet, Derrick-Einwand pruefen)
  - frische Lesung der letzten Schicht von BEWEIS-2
  - Teildateien in RUNDE-11/mess3a/ und RUNDE-10/beweis2/ gelten nicht als Lesung.
- Offen fuer den Neustart: diese beiden Karten neu starten; Chem 8 Verfolgung; Abschaetzung der Runde 11, Journaleintrag und rsync .69 -> TS440.
- Vorgemerkt fuer Runde 12: SPIN-D (Diracfeld an Q-Ball koppeln, Anlass Scout-Treffer arXiv:2606.30964) und die Hopf-3D-Stationaritaet bei Viertelladung (Codex).

## Fortsetzung (Leitung, ab 2026-09-30 19:34:26 CEST, date; Finn: "mach das")

- Neustart der zwei abgebrochenen Karten, beide nach 19:34:26:
  - MESS-3A (feldforscher, neue Instanz). Die Teildatei des ersten Laufs wurde umbenannt in
    MESS-3A.abgebrochen-1330.md. Der Agent liest sie erst nach seinen eigenen Vorab-Erwartungen.
  - Frische Lesung der letzten Schicht von BEWEIS-2 (pruefer-opus, neue Instanz). Die Teildatei wurde umbenannt in
    LESUNG-LETZTE-SCHICHT-BEWEIS-2.abgebrochen-1330.md; der Leser liest sie nicht.
- BEWEIS-2.md und BEWEIS-2-PLAN.md sind seit 13:19 unveraendert (sha256 3ad62460..., 0f8f0790...).

### Codex waehrend der Pause (eingetragen 19:35:42)

- **Zwei- und Dreimoden-Pilot** (resonance-20260930/spin-modes-pilot/ERGEBNIS.txt, fertig 12:09):
  - Klassische Polarisations- und Orientierungsdynamik entsteht in kleinen gekoppelten Graphmodellen (DNLS auf Tetraeder
    und Wuerfel).
  - Eine allgemein verlaessliche Dreimoden-Reduktion folgt daraus nicht: Die Leckage reicht von 0 bis 19,2 %, und auch bei
    kleiner Leckage gibt es grosse Projektorfehler.
  - Gegenbefund gegen eine zu freundliche Spin-Diagnose: Stokes-Groessen koennen bis 1e-14 stimmen, waehrend die volle
    Bahn um 0,1 abweicht.
  - Kein Q-Ball, kein Feldkontinuum, kein quantisierter Spin, kein Spin 1/2.
- **Winkel-Feldpilot** (spin-angular-pilot/RESULTAT.txt, fertig 12:07):
  - Modell: reelles KG-Kontrollfeld auf S^2, kein Q-Ball.
  - Das l = 1-Triplett bleibt bis T = 40 eine gute, aber nicht exakte Naeherung. Die kubische Kraft regt l = 3 an;
    begrenzte Galerkin-Konvergenz.
  - F = q x p ist klassischer orbitaler Drehimpuls, kein intrinsischer Spin.
- **Neu, laeuft seit 19:34:** bic-nonlinear-followup. Codex untersucht die Strahlung zweiter Ordnung an T1/T2
  (Kanaele +-2 rho offen, l1 x l1 -> l0 + l2) mit exakter Polynomkontrolle. Er behauptet ausdruecklich keine
  nichtlineare Stabilitaet.
- Einordnung der Leitung: Das bestaetigt SPIN-1 (parken). Echter Spin 1/2 braucht einen eigenen Eingang, etwa ein
  angekoppeltes Diracfeld (vorgemerkte Karte SPIN-D).

### Chem 8 Mitte (Leitung; RUNDE-11/chem8-mitte/KARTE.md; Vorhersage 19:36:31 mtime, Laeufe 19:36:54 bis 19:40:06; eingetragen 19:40:13)

- Frage: Ist der grosse Klumpen (etwa 1,5 Q0) aus Runde 10 der ruhende Ball C?
- **Nein.** Bei 3pi/4 und v >= 0,11 liegt am Ende im Mittelstueck |x| < 6 fast keine Ladung.
  - T = 300: 0,01 bis 0,16 Q0; T = 600: 0 bis 0,01 Q0.
  - Der groesste Klumpen hat dabei 1,26 bis 1,52 Q0 und bleibt bis T = 600 im Messbereich.
- V1 an allen Punkten verfehlt. Nach der Scheiterregel ist das Bild "ruhender Ball C nimmt Ladung auf" fuer 3pi/4 falsch.
- V2 bis V4 getroffen; die Kontrolle stimmt mit Runde 10 bis 7e-16.
- Einordnung: Ladungsumverteilung im Dreierstoss, keine Katalyse. Welcher Ball die Ladung traegt, ist nicht gemessen.

### BEWEIS-2 letzte Schicht (pruefer-opus, Neustart, 19:35:19 bis 19:48:21; eingetragen 2026-09-30 19:49:07 CEST)

- **Urteil: "letzte Schicht traegt mit Auflagen", nichts blockierend.**
  - 10 von 11 Auflagen der beiden Lesungen sind umgesetzt, OpenAI A4 nur teilweise.
  - 58 von 58 neuen oder geaenderten Zahlen sind richtig, darunter die Ursache des T2-B-Fehlschlags (7,54e7, 0,32, 19,10)
    und z0_rho.
  - Das Zertifikat ist unveraendert (37 OK).
- Befunde, nur Wortlaut:
  - L1: Ordnungswoerter ("erste", "naechste") und eine Knotenaussage widersprechen der Regel "n nur als Leiteretikett".
  - L2/L3: Ungenauigkeiten zu R < r_j, zu den Parametern und zum Verwerfen eines Schrittversuchs.
  - L4: Das Einfach gesagt geht zu weit.
  - L5 optional.
- Zur Einarbeitung an den Autor zurueckgegeben (nach 19:48). Danach folgt eine enge Nachpruefung nur der geaenderten
  Zeilen.
- Einarbeitung L1 bis L5 durch den Autor bis 19:51; neue sha256 BEWEIS-2.md 6474fc60..., PLAN 4b6b3c1b..., STAND
  a499d2b6.... Zertifikat 37 OK (Leitung 19:52:01).
- Enge Nachpruefung der geaenderten Zeilen (pruefer-opus, 19:52:17 bis 19:59:13; NACHPRUEFUNG-1949-BEWEIS-2.md):
  "umgesetzt mit Resten". Nichts beruehrt die Strenge; 9 von 9 neuen Zahlengruppen richtig; keine Ordnungswoerter mehr.
  - R1: Ein Satz zur l = 1-Breite behauptet mehr als belegt.
  - R2: Die Codehinweise fehlen unter "offen".
  - R3: Von der Leitung geklaert (2026-09-30 20:00:10 CEST): Die OpenAI-Formulierung steht so in GESAMT-REVIEW.txt Z. 6.
  - R1 und R2 als letzte Textrunde an den Autor; die Leitung prueft den Diff selbst, ohne weitere Leserunde. Grund:
    Verhaeltnismaessigkeit, zwei Saetze ohne Zahlen.
- Letzte Textrunde (Autor bis 20:00:58, nur Text): R1 als Hinweis statt Schluss, R2 Codehinweise unter "offen" und
  "im Text berichtigt"; dazu die zwei optionalen Punkte. **Diff von der Leitung um 20:01:14 geprueft:** Er deckt genau R1,
  R2 und die optionalen Punkte ab, keine weitere Aenderung. Zertifikat 37 OK.
  - Endfassung: BEWEIS-2.md sha256 3a21e2a3090142cc..., STAND.md 51854e0638e0495b..., BEWEIS-2-PLAN.md 4b6b3c1b18cb10f0...
    (unveraendert seit 19:51).
- **BEWEIS-2 ist damit abgeschlossen:** T1 und T2 rechnergestuetzt bewiesen (linear, operational eingebettet). Gelesen in
  zwei Haeusern, dazu die letzte Schicht und eine enge Nachpruefung. Offen: zweites Programm, Herkunft der l = 1-Breite,
  Plan-Hash ab dem naechsten Beweis.

### MESS-3A Antiferromagnet (feldforscher, Neustart, 19:41:07 bis 20:03:42; RUNDE-11/mess3a/MESS-3A.md; eingetragen 20:05:00)

- **Der Einwand der Leitung haelt, und zwar staerker:** Im reinen einachsigen AFM-Sigma-Modell ist 2U/sin^2 theta = 1
  identisch. Es gibt also in keiner Dimension nichttopologische praezedierende Baelle; in 1D nur praezedierende Waende.
  - Ein Feld entlang der Achse verschiebt nur die Frequenz (Omega = omega + h).
  - Das ist Literatur seit 1983: Bar'yakhtar/Ivanov, frei lesbar, an der Quelle gelesen.
- **Traegt 3D-Baelle:** Anisotropie vierter Ordnung, w = -K1 cos^2 theta - K2 cos^4 theta mit K2 > 0, also
  kappa = -K2/(K1 + 2 K2) < 0.
  - Im Fenster Omega^2 in (1 + kappa, 1) ist U_Omega(pi/2) < 0, und dort existieren Baelle.
  - Bar'yakhtar/Ivanov 1983: 3D, im unteren Teil des Fensters stabil.
  - Nietz 2010: 3D, K2 = 140 Oe neben K1 = 700 Oe.
  - Ovcharov u. a. 2023: 2D, spinstromgetrieben.
  - DM-Kopplung verengt das Fenster (2609.32059), oeffnet es nicht.
- **Kanalstruktur** (Herleitung des Agenten, nicht gegengelesen [H]): dieselben zwei Kanaele wie bei uns (offen ab
  rho = 1 - Omega, geschlossen bis 1 + Omega), dazu ein anziehender Topf im geschlossenen Kanal. rho ~ 2 m ist
  erreichbar, im Labor der obere AFMR-Zweig.
- **Laborbezug:** Die noetige K2-Form ist mit Quelle nur fuer Haematit belegt (Modellwerte 213/192 GHz, kappa ~ -0,19).
  Fuer MnF2 und Cr2O3 ist kappa nicht belegt; rho laege dort bei etwa 0,5 bzw. 0,34 THz.
- **Warnung des Agenten, von der Leitung uebernommen:** Die woertliche Scheiterregel aus MESS-2 ist fuer den AFM fast
  vorentschieden. Sie wird voraussichtlich von Volumenzustaenden im Ballinneren bestanden (Spin-Flop-Phase mit
  lueckenlosem Zweig) und sagt dann nichts ueber einen Wandzustand.
  - Nach der Projektregel "Vertraege muessen scheitern und bestehen koennen" darf die Karte AFM-KANAL-1 diese Regel nicht
    allein tragen.
  - Sie braucht den getrennt markierten Wandzustands-Test mit eigener, vorab gebundener Scheiterregel.
- Plan AFM-KANAL-1 (nicht gerechnet): 35 Profile (5 kappa x 7 Omega), zwei Gitterstufen, vier Kontrollen; etwa 1 bis 2 h
  Code, je Gitterstufe hoechstens 10 min.
- Grenzen: WebSearch erschoepft, arXiv-API gesperrt; die 24-Monats-Suche nur ueber arxiv.org/search.

## Abschaetzung (Leitung, 2026-09-30 ab 20:05:00 CEST, date)

| Karte | Entscheidung | Grund |
|---|---|---|
| BEWEIS-2 | weiter (ins Leiter-Paper) | T1 (l = 0, n = 2) und T2 (l = 1) rechnergestuetzt bewiesen; zwei Haeuser, letzte Schicht, enge Nachpruefung; nur Textauflagen. Offen: zweites Programm |
| MESS-2 | weiter ueber MESS-3A | These praezisiert: zweite Zeitordnung und positiver Antiteilchen-Zweig noetig; Dirac-artige Systeme werden instabil statt still [H] |
| MESS-3A | weiter als AFM-KANAL-1 | Derrick-Einwand bestaetigt (Literatur 1983); 3D-Baelle nur mit K2 > 0 (Haematit). Kanal-Test braucht einen Wandzustands-Test mit eigener Scheiterregel |
| LEITER-2D | weiter (Unterscheidungstest) | n = 6 blind getroffen; n = 7 und 8 nicht gesehen; Physik gegen Numerik mit hoeherer Genauigkeit oder anderem Anschlussradius klaeren |
| CEMZ-MESS | weiter (Schreibtischkarte) | erste Messfolge fuer die Glieder 7 und 10, bedingt: Unter CEMZ in D = 4 bleibt nur l_eff <~ 38,6 um. Ebene (l_eff, \|alpha\|) mit Tabellenwerten; Nachtrag in WARUM-SPIN-2.md erst nach frischer Gegenlesung |
| Y-2 | verwerfen | Q-Ball-Inneres zu weich fuer Y-Faeden (Loch kostet etwa 30-mal weniger als im Supraleiter-Vorbild) |
| Chem 1 weit | parken "erklaert" | Die Zerfallskonstante haengt vom Messpunkt ab (Trennpunkt-Test getroffen); Lehrbuch-Tunnelstrom |
| Chem 8 Mitte | verwerfen (Katalysebild) | Der grosse Klumpen ist nicht der ruhende Ball C; Ladungsumverteilung im Dreierstoss |
| Codex Spin-Piloten | parken (bestaetigt SPIN-1) | keine verlaessliche Dreimoden-Reduktion, kein Spin 1/2 |
| Codex Hopf | weiter bei Codex | hyperbolischer Traeger bei Viertelladung; als Naechstes 3D-Stationaritaet |
| Codex nichtlineare Folge | laeuft bei Codex | Strahlung zweiter Ordnung an T1/T2 |

- **Vorab gegen Ausgang, Leitung:**
  - LEITER-2D n = 6 getroffen (Abstand 5e-6), n = 7 und 8 nicht gesehen.
  - Chem 1: V1 verfehlt, Nachtest getroffen.
  - Chem 8 Mitte: V1 verfehlt.
  - Derrick-Einwand bestaetigt.
- **Lehren der Runde:**
  - Den Planstand vor jedem Beweislauf per Hash einfrieren (A4).
  - Eine Scheiterregel, die Volumenzustaende bestehen, trennt nicht (MESS-3A).
- **Selbstanzeigen der Agenten:** ein awk-Zeilenfilter (CEMZ-MESS); geschaetzte Uhrzeiten, ersetzt (CEMZ-MESS,
- **Unterbrechung:** 13:31 bis 19:34 wegen des Nutzungslimits. Zwei Karten wurden sauber neu gestartet, die Teildateien
  als *.abgebrochen-1330 erhalten.

## Einfach gesagt

Diese Runde hat den Beweis fuer zwei weitere stille Schwingungen des Q-Balls fertiggestellt: Zwei unabhaengige Teams und
zwei weitere Leser haben ihn geprueft, und nur Formulierungen mussten genauer werden. Fuer ein Laborexperiment kommen
Antiferromagnete wie Haematit in Frage; die einfachsten Magnetmodelle koennen solche Baelle aber gar nicht bilden, das
war schon seit 1983 bekannt. Bei der Schwerkraft zeigt sich: Eine reine "Lichtbrechungs"-Schwerkraft liesse verschieden
gebaute Baelle verschieden schnell fallen, was Messungen ausschliessen. Und eine minimal veraenderte Einstein-Schwerkraft
koennte, wenn eine bekannte Rechnung stimmt, nur auf winzigen Laengen wirken.

## Abschluss (Leitung, 2026-09-30 20:06:28 CEST, date)

- Journal: claude-runde-v3-11-20260930 veroeffentlicht (Index nr 547, 20 Quellen mit sha256; `pruefen` vorher ohne Befund,
  wuerde_sperren 0). T2-Zahlen im Text gegen ZERT-T2-A-L36.json (z0) gegengelesen.
- Sicherung: rsync .69 -> TS440 (ohne --delete, nice/ionice) gestartet 20:06:21, Log
  /home/fmh/sicherung-dot69-ts440-lauf-20260930-r11.log auf der .69. Die Sicherung von Runde 10 endete rc = 0 um 12:32:47.
- Folgekarten fuer Runde 12:
  - AFM-KANAL-1 mit Wandzustands-Test und eigener Scheiterregel
  - LEITER-2D-Praezision
  - CEMZ-Ebene als Schreibtischkarte
  - SPIN-D (Diracfeld an Q-Ball)
  - Ernte der Codex-Laeufe (nichtlineare Folge, Hopf 3D)
  - eine Zufallskarte
