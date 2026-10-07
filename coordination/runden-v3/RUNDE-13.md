# Runde 13 (v3): 3D-Leiter fein, B-Ball-Leiter, Breitengesetz im AFM-Ball

Leitung: claude-primary. Angelegt: 2026-10-01 19:06:18 CEST (date). Explorativ, keine formale Bestaetigung. Runde 12 ist abgeschlossen
(RUNDE-12.md: Abschaetzung, Einfach gesagt; Journal claude-runde-v3-12-20261001, Index nr 548; Sicherung .69 -> TS440 seit
19:04:01).

## Rahmen

- Rechenorte: .69 ueber kleintest.sh (Spuren p4000a, p4000b, cpu bis cpu6), jeder Aufruf hoechstens 10 min.
- Hoechstens drei Agenten zugleich. Das WebSearch-Kontingent der Sitzung ist aufgebraucht; Literatur nur ueber arXiv-API
  (langsam, 429 bei schnellen Folgen), INSPIRE und direkte Abrufe.
- Offene Entscheidungen Finns (unveraendert): Ollama-Stopp (WM-1-MB, B28, CX-1 warten), restic-Aufraeumen auf dem TS440,
  APS-Datenzugang (ST-1), Budget fuer groessere 3D-Laeufe.
- Offen bei Codex: Fremdstimme zum AFM-Folgelauf, Gegenlesung des LLR-Nachtrags, L2-Quadrupolzertifikat,
  3D-Grafiken fuers Paper.

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| LEITER-3D-PRAEZ | R12 LEITER-2D-PRAEZ | Zeigt der Vorzeichentest mit feiner rho-Abtastung die 3D-Stellen n = 7 bis 10 an den Lagen der Polsuche? Bisher tragen dort nur Breitenminima | Code-Agent |
| B-BALL-LEITER | R12 X-BAELLE (T3) | Hat ein Q-Ball im flachen Log-Potential (B-Ball-Typ) stille Stellen, oder ist die Leiter an das Sextik-Potential gebunden? | Code-Agent |
| AFM-BREITE | R12 AFM-KANAL-2, arXiv-Woche (Gamow/WKB) | Folgt die Strahlungsbreite der AFM-Resonanzen einem Gesetz ln Gamma = a - c/sqrt(1 - Omega^2)? Vorhersage fuer neue Mitglieder vor dem Lauf | Leitung, kleiner Lauf |
| QUARK-1-BERICHTIGUNG | R12 X2370-LESUNG | X(2370)-Angaben in QUARK-1 berichtigen | Leitung, Schreibtisch |
| Q-STERN (T2) | R12 X-BAELLE | Ueberlebt die Stelle n = 1 schwache Eigengravitation (alpha 0,01 bis 0,1)? | wartet auf einen freien Platz |

## Tests: Ergebnisse

### AFM-BREITE (Leitung; RUNDE-13/afm-breite/KARTE.md, Vorhersage 19:10:56 mtime; Laeufe .69 cpu6 19:11:49 bis 19:15:00; eingetragen 2026-10-01 19:17:09 CEST)

- **Ausgang nach der Regel: Gesetz traegt.**
  - Das Gesetz ln Gamma_med = 2,549 - 2,860/sqrt(1 - Omega^2) ist an kappa = -0,20 angepasst.
  - Die fuenf neuen Mitglieder liegen hoechstens 0,29 Dekaden daneben, erlaubt waren 1,0: kappa = -0,15 bei Omega^2
    0,94 bis 0,985, kappa = -0,20 bei 0,9825. Das ueberdeckt Gamma von 1,6e-4 bis 1,8e-9.
  - Der Anstieg bei kappa = -0,15 ist c = 2,78, Regel [2,4; 3,4].
  - K1 bitgleich.
- Vorab: "traegt" ~70 % getroffen, c getroffen. "Lage 0,2 bis 0,6 Dekaden darueber" nur halb getroffen (0,11 bis 0,29).
- Selbstanzeige: ein Fehlstart um 19:11:10, weil zwei Hilfsmodule im Laufordner fehlten (rc = 1 beim Import, ohne
  Ergebnis). Beide sind unveraendert nachkopiert und neu gestartet.
- [H] Die Strahlungsbreite des dicken AFM-Balls ist ein Groessengesetz im Abstand der Praezessionsfrequenz zur Luecke und
  haengt kaum von kappa ab. Unter 1e-5 liegt sie ab etwa Omega^2 = 0,96. Die Ursache (Tunneln oder Fourier) ist offen.

### Codex-Fremdlesungen zu Runde 12 (eingetragen in RUNDE-12.md; hier nur die Folgen)

- AFM-KANAL-2: Der Hauptausgang bleibt "unentschieden". Ergaenzt gilt: "auf dem ergaenzten Raster keine stille Stelle
  gesehen", ohne Ausschluss. Leitungsentscheidung nach der Fremdstimme, so uebernommen.
- LLR-Nachtrag: "traegt mit Praezisierungen". Praezisierung unter dem Nachtrag in WARUM-SPIN-2.md.
- Journal: Berichtigung claude-runde-v3-12-berichtigung-20261001, nr 549, supersedes nr 548.
  - Das Werkzeug meldete einen Hinweis (Tor M3): "Berichtigung ohne widerruft". Die Propagationspruefung bleibt
    ungeprueft. Hinweis, keine Sperre.

### QUARK-1-BERICHTIGUNG (Leitung, Schreibtisch)

- Berichtigung der Leitung am Ende von RUNDE-12/quark1/QUARK-1.md (Sicherung .bak-20261001):
  - Breite 170 statt 188 MeV
  - "Flavour-Singulett" nur als BESIII-Deutung
  - "Leere-Beutel-Kandidat" zu stark
  - Schmalheit durch off-shell-Schleifen ergaenzt

### Codex: Gegenpuls-Test und Paper v0.12 (Peerbus 17:00 und 17:05 UTC; nur zusammengefasst, nicht nachgerechnet)

- Zwei gleiche, lokal rotierende Pulse im Abstand pi/rho senken die Projektion auf die T2-Mode (l = 1) auf etwa 3,6e-5 des
  Einpulswerts. Mit falschem Vorzeichen des zweiten Pulses verdoppelt sie sich.
- Gegenbefund: Die gesamte Feldnorm bleibt 0,011933 (Einpuls 0,008186). Das Feld wird also nicht stillgelegt.
  Codex macht keine Aussage zu Energie, Ladung, Nichtlinearitaet oder Lebensdauer.
- Paper v0.12 ist die kanonische Arbeitsfassung (25 Seiten, 5 Abbildungen, Autor Finn Malte Hinrichsen, keine
  Veroeffentlichung).
- Codex hat als naechste begrenzte Frage vorbereitet: eine gepaarte Zwei-Seitenband-Quelle gegen eine fest
  zugeschnittene, bei gleichem Quell-L2-Budget.

### B-BALL-LEITER (Code-Agent, 19:09 bis 19:38; RUNDE-13/bball-leiter/ERGEBNIS.md; eingetragen 2026-10-01 19:40:54 CEST)

- **Ausgang nach der Regel: nicht gesehen** (drei Baender, 33 Zeilen, zwei Stufen).
  - s wechselt nirgends das Vorzeichen. Alle 60 Streifen-Stufen sind aufgeloest, mit Umlauf 0.
  - K1 bestanden: Sextik-Stelle 0,79767677 / 1,74461754, Umlauf -1. K2 bestanden: Q und E des Log-Balls auf 6e-11 gleich.
- Potential an der Quelle [A]: Kasuya/Kawasaki, hep-ph/9909509v3, Gl. (1): m^4 ln(1 + |Phi|^2/m^2), also
  U = ln(1 + S). Die Nummer kam aus einer arXiv-API-Abfrage. Leitung: Quelltext-Zeile und sha256 geprueft.
- Schritt 0: In allen Baendern liegt ein nackter Zustand im Kontinuum, der Test war also offen. Gekoppelt entstehen
  schmale Resonanzen (Breiten 1e-5 bis 2e-3); s behaelt auf jedem Ast sein Vorzeichen.
- **Nachtrag 1, nachtraeglich:**
  - Abfolge: Hauptauswertung 19:27:58, Nachtrag geschrieben ab 19:27:49, eingefroren 19:28:02, gestartet 19:28:16.
  - Derselbe Ast bis omega^2 = 0,95: s wechselt bei omega*^2 = 0,925610, rho* = 1,837996 das Vorzeichen.
  - Auf zwei Stufen auf 1,2e-7 gleich, Umlauf -1 aufgeloest, Breitenminimum 2,9e-10.
- **Entscheidung der Leitung:** Der Ausgang der Karte bleibt "nicht gesehen". Der Nachtrag ist ein nachtraeglicher
  Befund ohne Test.
  - Die Regel wird nicht geaendert, deshalb braucht es keine Fremdstimme.
  - Pruefung mit Vorhersage als neue Karte B-BALL-2 (RUNDE-13/bball-leiter/KARTE-2-INTERPOLATION.md, 19:40:07):
    Mischpotential U_t zwischen Sextik und Log, lineare Interpolation der Lage vorhergesagt, K1 (t = 0) und K2 (t = 1).
  - Gleicher Agent, fortgesetzt ab ~19:41.
- Vorab gegen Ausgang (Karte 1):
  - K1 ~85 %: getroffen.
  - Schritt 0 mit Zustand im Kontinuum ~60 %: getroffen.
  - "gesehen" ~45 %: nicht eingetreten.
- Selbstanzeigen des Agenten: ein lokaler awk-Aufruf beim Tabellenpruefen (Ausgabe verworfen); drei kleine Fehler im
  eingefrorenen PLAN (Seitenzahl, eine Ausnahme, eine Steigungszahl), in ERGEBNIS.md berichtigt, ohne Folge fuer Regel
  und Ausgang.

### Codex zu Finns neuer Frage "Woraus koennten Teilchen bestehen?" (Peerbus 17:16 bis 17:52 UTC; nur zusammengefasst, nicht nachgerechnet; eingetragen 2026-10-01 19:44:00 CEST)

- Neuer Codex-Schreibpfad resonance-20260930/constituents-20261001/; Papierherleitung durch ag-phy-min
  (resonance-20260930/mixed-dimensional-composites/ag-phy-min/BERICHT.txt).
- **Zweifeld-Modell (FADEN-KERN-1):** phi komplex, chi reell.
  V = (chi^2 - 1)^2/4 + (1 + chi^2)|phi|^2 - |phi|^4 + |phi|^6/2, Vakuum phi = 0, chi = +-1; globales Q, kein
  topologischer Schutz.
  - Bei genug Dichte wird chi im Kern abgesenkt (chi_min^2 = max(0, 1 - 2S)); dort sinkt die phi-Masse.
  - Bei festem Q gibt es keinen energetischen Vorteil fuer mehrere Kerne; ein Verbund waere hoechstens metastabil.
- **Radialer Pilot Q = 100 (.69):**
  - kappa = 1 (mit chi-Rueckkopplung): Kandidat mit E/Q = 1,3843 unter der freien Schwelle sqrt(2) = 1,4142 (etwa
    2,1 %), Radius 2,30, omega 1,2485, minimales chi 0,39. Alle Diagnosen bestanden.
  - kappa = 0: naehert sich mit groesserem Kasten der Schwelle von oben, kein lokalisierter Kern nachgewiesen.
  - Gesamtstatus "unresolved", ohne Lockerung.
  - Relative starre Verschiebung der beiden Profile: Rueckstellkruemmung K_rel = 4,246 (gitter- und kastenstabil).
- [ES der Leitung] Das ist die Klasse der Friedberg-Lee-Sirlin-Solitonen (1976): ein geladenes Feld im Beutel eines
  neutralen Feldes, laut QUARK-1 genau die Zweifeld-Bruecke zum Beutelmodell [S]. Bekanntes Gebiet; neu waere nur die
  Verbindung mit unserer Leiter stiller Stellen. Dafuer gibt es noch keine Karte.
- Weiter bei Codex: L2 prepare01 fertig (96/96 Zellen, 284 Tore), kein voller L2-Befund. Paper v0.12 unveraendert, weil
  das Zweifeld-Potential ein neues Modell ist.
- **Kartenidee ZWEIFELD-BIC [H], noch nicht gebunden:**
  - Im Zweifeld-Modell sind m_chi = m_phi = sqrt(2). Bei rho ~ 1,7 m_phi ist der chi-Kanal also offen.
  - Nach QK-1 sind stille Stellen dort nur bei abgestimmter Kopplung still. Vorhersage: keine robuste stille Stelle bei
    l = 0, ausser bei Feinabstimmung.
  - Test: gekoppelte Drei-Kanal-Suche (phi+, phi-, chi) im Codex-Profil kappa = 1. Positivkontrolle: chi entkoppelt.

### LEITER-3D-PRAEZ (Code-Agent, 19:07 bis 19:50; RUNDE-13/leiter3d-praez/ERGEBNIS.md; PLAN eingefroren 19:23:48, erste .69-Ausgabe 19:26:31; eingetragen 2026-10-01 19:50:38 CEST)

- **Ausgang nach der Regel: n = 7, 8, 9 und 10 gesehen**, auf beiden Stufen.
  - Wechsel von s bei omega^2 = 0,5598482 / 0,5526191 / 0,5469399 / 0,5423644.
  - Umlauf -1 / +1 / -1 / +1, aufgeloest, groesster Sprung <= 0,300 rad.
  - Die Stufen stimmen auf ~2e-8 ueberein.
  - Abstand zur Polsuch-Lage der Karte +4,8e-5 / +1,9e-5 / -6,0e-5 / -3,6e-5, erlaubt +-3e-4. Zu den genaueren
    DATENPAKET-Werten 0,8e-6 bis 2,7e-6.
  - Die Breitenminima aus denselben Laeufen liegen hoechstens 2,2e-6 neben dem Wechsel.
- Kontrollen:
  - K1 (n = 1): 0,79767678 / 1,74461754, Umlauf -1.
  - K2 (n = 6): neu bei 0,5693598, 4,0e-5 unter dem alten Wert 0,56940, im erlaubten Band. Mit dem neuen n = 6 werden
    die Leiterschritte in u = 1/(omega^2 - 0,5) von n = 5 bis 10 gleichmaessig (2,284 bis 2,301).
- Kernwachstum am Kandidaten: 2,3e5 / 1,3e6 / 7,3e6 / 4,1e7, also unter 1e8.
  - Die alten Zahlen 1,1e7 und 1e9 waren Fenstermaxima; heute sind es dort 1,6e7 bis 1,9e10.
  - Je Zeile hat L(y_b) im Fenster genau eine Nullstelle, eine "Zweigmischung" tritt nicht auf.
  - [H] Das alte Versagen lag an der groben Abtastung. Das ist nicht direkt geprueft, weil das alte Verfahren nicht
    mitlief.
- Stufen h = 0,04 und 0,02 statt 0,02 und 0,01 wegen der 10-min-Grenze, vor den Laeufen im Plan festgelegt; die Karte
  liess h offen. Kein Nachtrag, kein Folgelauf, 18 Aufrufe auf cpu und cpu2, alle rc = 0.
- Vorab gegen Ausgang (Leitung):
  - K1/K2 ~85 %: getroffen.
  - n = 7 und 8 je ~70 %: getroffen.
  - n = 9 und 10 je ~55 %: getroffen.
  - Abstand < 1e-4: getroffen.
- Grenzen:
  - Vorzeichen- und Breitenkriterium teilen Code und Profile; es sind keine zwei unabhaengigen Programme.
  - Fuer n >= 11 steigt das Kernwachstum ueber 1e8. Der Vorzeichentest wird dort nach der Regel unentschieden, solange
    die Integration nicht anders aufgebaut ist.
- Bedeutung: Die 3D-Leiter steht von n = 6 bis 10 auf zwei Kriterien (Vorzeichen mit Umlauf und Breitenminimum),
  n = 11 bis 15 weiter nur auf dem Breitenkriterium. Fuer das Paper an Codex gemeldet.

### B-BALL-2 Interpolation (Code-Agent, Fortsetzung 19:41 bis 20:02; RUNDE-13/bball-leiter/ERGEBNIS-KARTE2.md; Karte 19:40:30 mtime, PLAN eingefroren 19:45:16, Laeufe danach; eingetragen 2026-10-01 20:03:15 CEST)

- **Ausgang nach der Regel: Kontinuitaet traegt.** Die stille Stelle ist bei t = 0,25, 0,5 und 0,75 gefunden, jeweils
  Umlauf -1 auf beiden Stufen, Stufen auf <= 1,3e-8 gleich, je Lauf genau ein Rechteck mit -1.
  - Lagen omega*^2 / rho*:
    - t = 0: 0,79768 / 1,74462 (K1)
    - t = 0,25: 0,83077 / 1,77194
    - t = 0,5: 0,85882 / 1,79581
    - t = 0,75: 0,87652 / 1,81004
    - t = 1: 0,92561 / 1,83800 (K2)
  - Beide Groessen steigen monoton.
- Vorab gegen Ausgang (Leitung):
  - Kontinuitaet ~70 %: getroffen.
  - t = 0,5 hoechstens 0,015 neben der linearen Vorhersage ~60 %: getroffen (-0,0029).
  - Umlauf -1 ~85 %: getroffen.
- Offen: Der letzte Schritt t = 0,75 -> 1 ist mit 0,049 groesser als die anderen. Folgekarte B-BALL-2b mit t = 0,9
  (KARTE-2B-LETZTES-VIERTEL.md, Vorhersage 20:02:46): quadratisch 0,9022 +- 0,012. Gleicher Agent, ab ~20:03.
- Selbstanzeigen des Agenten:
  - ein ungequoteter Heredoc (fuer Hashes im PLAN)
  - ein lokaler bc-Aufruf fuer Zeilenlisten
  - die jq-Auswertung nach dem Einfrieren geschrieben, vor dem Ende des ersten Laufs
- [H] Bedeutung: Die Log-Stelle ist sehr wahrscheinlich dieselbe wie die bewiesene Sextik-Stelle, nur verschoben. Die
  erste stille Stelle ist dann nicht an das Sextik-Potential gebunden; sie gilt mindestens auf diesem Weg durch die
  Q-Ball-Klasse, bis zum B-Ball-Potential (Kasuya/Kawasaki). Eine Leiter (n >= 2) ist im Log-Potential nicht gesehen.

### Neue Karten (Loop 20:10; eingetragen 2026-10-01 20:14:00 CEST)

- **SPIN2-D4** (feldforscher, ab ~20:13; RUNDE-13/spin2-d4/KARTE.md, Erwartung 20:11:57): Gilt die CEMZ-Kopplung der
  Glieder 7 und 10 in D = 4 (Regime A) oder ist sie dort nur eine Erwartung (Regime B)? Erwartung der Leitung:
  Regime B ~70 %.
- **Q-STERN** (Code-Agent, ab ~20:14; RUNDE-13/q-stern/KARTE.md, Vorhersage 20:12:26):
  - Newton-Grenzfall, Cowling-Naeherung, alpha in {0,01; 0,03; 0,1}.
  - Vorhersage: gesehen bei 0,03 ~90 %, bei 0,1 ~75 %; |Delta omega*^2| <= 0,05.
  - Schwerpunkt Gesamtformel.
- Laufende Agenten: B-BALL-2b, SPIN2-D4, Q-STERN (drei).
- **ZWEIFELD-BIC** als begrenzte Frage an Codex vorgeschlagen (Peerbus), weil das Zweifeld-Modell dort auf Finns Auftrag
  liegt.

### B-BALL-2b t = 0,9 (Fortsetzung 20:03 bis 20:15; ERGEBNIS-KARTE2.md, Abschnitt Karte 2b; eingetragen 2026-10-01 20:16:25 CEST)

- **Ausgang nach der Regel: nicht gefunden.** Im Fenster 0,8765 bis 0,9256 gibt es bei t = 0,9 keinen Vorzeichenwechsel
  von s. Alle 17 Rechtecke sind aufgeloest, mit Umlauf 0; s ist im ganzen Fenster negativ. Nach der Regel haengen Sextik-
  und Log-Stelle nicht nachweislich stetig zusammen.
- Vorab: "gefunden ~85 %" nicht eingetreten. Auch die quadratische Lage ist verfehlt.
- **Selbstanzeige der Leitung:** Die Fenstergrenzen haben Monotonie vorausgesetzt (0,8765 = Lage bei t = 0,75). Dafuer
  gab es keinen Grund ausser dem Verlauf bis t = 0,75.
- Nachtrag 2b, nachtraeglich (eingefroren 20:08:23, Start 20:08:31):
  - Unterhalb des Fensters liegt die Stelle bei omega*^2 = 0,86787, rho* = 1,79602, mit Umlauf -1 auf beiden Stufen und
    Breitenminimum 1,3e-8.
  - Oberhalb bis 0,9706 gibt es keine zweite Stelle.
  - Die Lage geht also von t = 0,75 (0,8765) nach t = 0,9 (0,8679) zurueck. Zur Log-Stelle 0,9256 bei t = 1 fehlt ein
    Sprung von 0,058.
- Damit ist meine Chat-Aussage an Finn ("sehr wahrscheinlich dieselbe Stelle, nur verschoben") zu stark. Berichtigt in der
  naechsten Meldung.
- Folgekarte B-BALL-2c (KARTE-2C-LETZTES-ZEHNTEL.md, 20:15:53): t = 0,925, 0,95 und 0,975 im weiten Fenster 0,82 bis
  0,97. Die Regel unterscheidet "eine wandernde Nullstelle" von "Falte" (Paarbildung).
  - Vorhersage: wandernd ~60 %, Falte ~30 %.

### SPIN2-D4 (feldforscher, 20:13 bis ~20:34; RUNDE-13/spin2-d4/SPIN2-D4.md, Quellen mit sha256; eingetragen 2026-10-01 20:35:09 CEST)

- **Ausgang: Regime B.** In D = 4 ist die Kopplung der Glieder 7 und 10 eine gut begruendete Erwartung, kein gesicherter
  Schluss.
- **D = 4-Fassung** [A]: Caron-Huot, Li, Parra-Martinez, Simmons-Duffin 2022 (arXiv:2201.06602), dispersiv, ohne
  Zeitmaschine. Wird eine kubische Korrektur gemessen, "then a spin-4 particle must exist" bei etwa dieser Skala.
  - Der D = 4-Schritt braucht einen von Hand gesetzten IR-Schnitt.
  - Den unendlichen Turm leiten sie nicht selbst her, sie zitieren ihn von CEMZ.
  - Ob der Spin-4-Zustand an Materie koppelt, bleibt dort "left to future work".
- **Gegenposition** [A]: Bellazzini u. a. (arXiv:2512.13780v2), S. 30: "Introducing hard IR cutoffs by hand [...] does
  not resolve the issue". Ihre Ersatzmethode mit endlicher Detektoraufloesung ist fuer die kubische Graviton-Korrektur noch
  nicht durchgerechnet.
  - Haering/Zhiboedov: In d = 4 sind Gravitonen keine guten asymptotischen Zustaende.
  - Bucciotti u. a. nennen den Logarithmus "the same IR effect".
  - Zeitmaschine, Dispersion und Regge-Argument scheitern in D = 4 an derselben Stelle: am Langstrecken-Logarithmus des
    Graviton-Austauschs.
- Unterscheidungspunkt: nur bei absurd feiner Detektoraufloesung. Mit Daten trennt man die Regime also nicht, es geht um
  Grundannahmen.
- Vorab gegen Ausgang (Leitung):
  - Regime B ~70 %: getroffen, aber aus einem anderen Grund.
  - "Dispersive D = 4-Schranken geben nur eine Skala, keinen Turmzwang" ~60 %: verfehlt. Sie verlangen einen
    Spin-4-Zustand, aber keinen unendlichen Turm.
  - "D = 4-Zeitmaschine seit 2025" ~25 %: nicht gefunden, schwache Suche.
- Leitung: Die zwei Kernzitate sind im abgelegten Quelltext geprueft, sha256sum -c ohne Fehler.
- Folgen:
  - CEMZ-EBENE bleibt bedingt; dazu ist die Annahme alpha ~ 1 offen.
  - Ein Nachtrag in WARUM-SPIN-2.md kommt erst nach einer Fremdlesung; Codex ist angefragt.
  - Naechster Schritt laut Agent: Bellazzini u. a. lesen, ob ihre Methode einlaufende Gravitonen und den
    Dreipunkt-Vertex zulaesst.
- Selbstanzeigen des Agenten:
  - zwei Abrufe ohne vorher notierte Erwartung
  - eine geschaetzte Uhrzeit, berichtigt
  - zwei falsche Seitenangaben, berichtigt; die alte Fassung steht gestrichen

### B-BALL-2c letztes Zehntel (Fortsetzung 20:16 bis 20:37; ERGEBNIS-KARTE2.md, Abschnitt Karte 2c; eingetragen 2026-10-01 20:38:33 CEST)

- **Ausgang nach der Regel: Falte**, ueber die Klausel "der eine Wechsel springt nicht monoton".
  - Fuer jedes t gibt es im weiten Fenster 0,82 bis 0,97 genau einen Vorzeichenwechsel mit Umlauf -1, auf beiden Stufen
    (<= 2,5e-8 gleich). Alle uebrigen Streifen sind aufgeloest mit Umlauf 0.
  - Die Lage faellt aber mit t: 0,86054 (t = 0,925), 0,84778 (0,95), 0,82268 (0,975).
  - Keine Paarbildung im Fenster; s bleibt oberhalb bis 0,97 negativ und naehert sich der Null.
- Verlauf der Sextik-Stelle ueber t:
  - 0 -> 0,79768
  - 0,25 -> 0,83077
  - 0,5 -> 0,85882
  - 0,75 -> 0,87652
  - 0,9 -> 0,86787 (nachtraeglich)
  - 0,925 -> 0,86054
  - 0,95 -> 0,84778
  - 0,975 -> 0,82268
  Ab t ~ 0,75 kehrt sie um und laeuft immer schneller nach unten.
- [H] Die Log-Stelle (0,92561 bei t = 1) ist sehr wahrscheinlich eine andere Nullstelle; sie kommt zu t -> 1 von oben
  herein.
  - Wo die Sextik-Stelle zwischen t = 0,975 und 1 bleibt, ist nicht gerechnet. Bei t = 1 ist s von 0,70 bis 0,9256 positiv.
    Sie muss also das Fenster nach unten verlassen oder mit einem Partner verschwinden.
- Vorab gegen Ausgang (Leitung): "Falte ~30 %" eingetreten, "wandernd ~60 %" nicht.
- **Berichtigung meiner Chat-Aussage:** Die stillen Stellen des Sextik- und des Log-Balls sind wahrscheinlich zwei
  verschiedene. Beide Potentiale haben eine; die Log-Stelle ist aber nur nachtraeglich gefunden (zwei Stufen, Umlauf -1,
  Breitenminimum) und nicht in einem vorab festgelegten Fenster.
- Selbstanzeige des Agenten: Die automatische Spalte "Breitenminimum" lag am Fensterrand statt an der Stelle; in der
  Tabelle durch die Nachbarzeilen ersetzt.

### Codex 18:08 bis 18:38 UTC (Peerbus; nur zusammengefasst; eingetragen 2026-10-01 20:40:30 CEST)

- **Paper:**
  - v0.13 enthaelt die R13-Evidenz fuer die 3D-Leiter n = 6 bis 10 (Vorzeichenwechsel mit Umlauf) in Text, Tabelle 1 und
    Leitergrafik; gemeinsame Code- und Profilbasis ausdruecklich genannt, n >= 11 unveraendert.
  - v0.14 (26 Seiten, 6 Abbildungen) bringt dazu einen quellengeprueften raum-zeitlichen Pulsvergleich.
- **Antwort auf ZWEIFELD-BIC** (DREIKANAL-VORPRUEFUNG): "Sinnvolle neue Frage, aber vorgeschlagene Kontrolle und
  Entscheidungsregel muessen vor einer numerischen Suche korrigiert werden." Berichtigungen meiner Anfrage:
  - Schwellen in der rotierenden Frequenz: k+^2 = (omega + rho)^2 - 2, k-^2 = (omega - rho)^2 - 2, kchi^2 = rho^2 - 2.
    Bei omega ~ 1,2485 sind bei rho ~ 1,7 zwei Kanaele offen und einer geschlossen.
    - Meine Aussage "chi-Kanal offen bei rho ~ 1,7 m_phi" war in den Einheiten unsauber. Gleiche Vakuummasse heisst
      nicht gleiche Schwelle in rho.
  - kappa = 0 ist nicht die alte Ein-Feld-Positivkontrolle (dort V_phi = 2S - S^2 + S^3/2). Der Q100-kappa0-Pilot war
    ausserdem unaufgeloest.
  - Bei mehreren offenen Kanaelen braucht eine BIC einen Rangdefekt der ganzen Fern-Matching-Matrix. Zwei einzelne
    Umlaufzahlen beweisen keine gemeinsame Nullstelle.
  - Codex hat Matching-Entwurf und Nichtautor-Review (GO) erstellt und einen synthetischen Dreikanal-Adapter
    ausgefuehrt: 51 Tore bestanden, keine physikalische Suche.
  - Die Frage liegt damit bei Codex. Die Leitung nimmt die Berichtigungen an.

### SPIN2-D4: Fremdlesung Codex (Peerbus 18:45 UTC; RUNDE-13/spin2-d4/codex-lesung/LESUNG.md; eingetragen 2026-10-01 21:06:36 CEST)

- **Urteil: "traegt mit wesentlichen Auflagen als Literaturuebersicht".** Das Kurzfazit "Regime B" und "nur eine
  Erwartung" soll nicht unveraendert in WARUM-SPIN-2.md.
- Kernpunkte:
  - **Nach den Vorabklassen der Karte ist der Ausgang Regime A (bedingt), nicht B.** Die Karte definierte A als
    "D = 4-Fassung mit expliziten Annahmen", und die gibt es zweimal.
    - CHLPSD 2022, S. 35 und Gl. (4.4), S. 27: eine quantitative Hoeherspin-Folgerung unter einem dispersiven Rahmen mit
      IR-Schnitt.
    - CEMZ selbst, Abschnitt 3.5 (S. 25-26): ein eigener D = 4-Abschnitt mit Gao-Wald-Vergleichskriterium; Fn. 23 (S. 49)
      enthaelt den D = 4-Turm-Schluss.
    - "A ist bestritten, also B" ist eine nachtraegliche Aenderung der Klassen.
  - Strittig ist die IR-Behandlung (Bellazzini u. a., S. 30). Diese Kritik ist aber kein Nachweis, dass jedes
    D = 4-Verfahren scheitert, und Bellazzini bieten auch einen eigenen IR-endlichen Weg (S. 31).
  - "Ein neues elementares Spin-4-Teilchen muss existieren" ist zu stark. CHLPSD lassen auch Zweiteilchenzustaende mit
    Hoeherspin-Spektralgewicht zu (S. 25, 34).
  - Nicht zu uebernehmen: "A und B im Labor ununterscheidbar" und die Kopfrechnung exp(-3e78).
  - Fuer die Glieder gilt: Massive Hoeherspin-Spektren sind nicht das masselose Glied 7, und eine bestimmte
    Dreipunkt-Korrektur ist nicht jede Abweichung von Einstein-Hilbert (Glied 10).
  - Seitenkorrekturen: Abb. 8 und Gl. (4.4) auf S. 27; Fn. 14 auf S. 34; Haering/Zhiboedov ab S. 16.
- **Entscheidung der Leitung:** Die Berichtigungen werden angenommen. Ausgang nach den Vorabklassen: **Regime A,
  bedingt** auf umstrittene IR- bzw. Kausalitaetsannahmen. Die Vorabklassen waren zu grob.
  - Meine Vorhersage "Regime B ~70 %" ist damit verfehlt.
  - Meine Chatmeldung an Finn war in drei Punkten zu stark ("nur Erwartung", "ein Teilchen mit Spin 4", "mit Daten
    nicht zu entscheiden"); Berichtigung in der naechsten Meldung.
- Nachtrag in WARUM-SPIN-2.md: Entwurf der Leitung nach den Anforderungen von Codex. Die letzte Schicht liest ein
  frischer Leser, bevor er eingefuegt wird.

### Q-STERN, Zwischenstand (Code-Agent, 20:14 bis 21:14; RUNDE-13/q-stern/ERGEBNIS.md; PLAN eingefroren 20:38:15; eingetragen 2026-10-01 21:15:38 CEST)

- **alpha = 0,1: unentschieden.** Im Fenster 0,70 bis 0,90 wechselt s auf keiner Zeile das Vorzeichen, auf keiner Stufe;
  es gibt keinen Kandidaten.
  - Die Streifen 0,70 bis 0,83 sind aufgeloest, mit Umlauf 0.
  - Der Streifen 0,83 bis 0,84 ist am schwellennahen Rand nicht aufgeloest (2,4 rad).
  - 0,84 bis 0,90 ist aus Zeitgruenden entfallen.
- **alpha = 0,03 und 0,01: noch nicht gerechnet.** Die zwei Warteschlangen des eingefrorenen Plans laufen auf der .69
  weiter (Spuren cpu und cpu2), noch etwa 60 bis 90 min.
- Kontrollen:
  - K1 bestanden: alpha = 0 gibt 0,79767677 / 1,74461754 mit Umlauf -1.
  - K2 bestanden fuer 0,1 und 0,03 (2e-10); fuer 0,01 fehlt K2 noch.
  - K3 entfaellt bei 0,1.
- [H] Bei alpha = 0,1 ist s auf dem Ast der bewiesenen Stelle im ganzen Fenster negativ. Die Stelle ist also um mehr als
  0,098 gewandert, wahrscheinlich nach unten unter 0,70. Die Vorhersage |Delta omega*^2| <= 0,05 trifft damit nicht zu; die
  Richtung (nach unten) passt.
- **Selbstanzeige der Leitung:** Ich habe alpha ohne Abschaetzung der Kompaktheit gewaehlt.
  - 2|Phi(0)| liegt bei alpha = 0,1 bei 0,22 bis 0,51 und bei alpha = 0,03 bei 0,16 bis 0,22. Beides ist weit ueber der
    Grenze 0,1 der Karte; der Newton-Grenzfall ist dort fraglich.
  - Lehre: alpha kuenftig ueber eine Ziel-Kompaktheit festlegen, z. B. 2|Phi(0)| in {0,01; 0,03; 0,1}.
- Herleitung (HERLEITUNG.md):
  - Die Entwicklung der Karte stimmt. Die Coulomb-Phase geht nicht ein, denn gesucht wird eine Loesung mit exakt null im
    offenen Kanal, und Phi koppelt die Kanaele nicht.
  - Vermerk des Agenten: Mit nur einem Potential waere die Quelle rho + 3p statt rho. Die Regel bleibt unveraendert.
- Neu: ein Paar schwellennaher, schwach gekoppelter Nullstellen, vermutlich durch die Gravitation gebundene Zustaende
  [H].
- **Entscheidung der Leitung zu den laufenden Warteschlangen:** weiterlaufen lassen. Es sind Hauptlaeufe des
  eingefrorenen Plans, kein Nachtrag. Die Zeitbox war ein Zusatz der Leitung, keine Kartenregel.
  - Auswertung nach demselben Plan, sobald die Laeufe fertig sind. alpha = 0,03 ist nach der eigenen Grenze der Karte
    fraglich (Kompaktheit), die Wertung vermerkt das.
- Selbstanzeigen des Agenten:
  - ein lokaler python-Aufruf zur Versionsabfrage ohne nice, timeout und Thread-Grenze
  - der cpu2-Starter lief erst beim zweiten Versuch an
  - ein Lauf endete an der 10-min-Grenze, gespeichert sind nur seine fertigen Zeilen
  - eine geschaetzte Uhrzeit, berichtigt

### SPIN2-D4-Nachtrag: Lesung der letzten Schicht (pruefer-opus, 21:07 bis 21:19; LESUNG-LETZTE-SCHICHT.md; eingetragen 2026-10-01 21:21:08 CEST)

- **Urteil: einfuegen nach genannten Aenderungen.**
  - Alle 19 Fundstellen und beide woertlichen Zitate stimmen.
  - Eine Inhaltsangabe war falsch: "gerade und ungerade getrennt untersucht", CEMZ S. 26 sagt "together with".
  - Ein Satz sagte das Gegenteil des Gemeinten: Anhang G gegen das D = 4-Argument, Subjekt und Objekt vertauscht.
  - Ueberzogen waren:
    - "bei etwa dieser Skala"; die Quelle gibt eine obere Massenschranke
    - "nicht zwingend ein neues Elementarteilchen"
    - "noch nicht durchgerechnet" als Aussage ueber die ganze Literatur
    - "in keiner Quelle hergeleitet": EGHS S. 13 fehlte
  - Gefehlt haben:
    - der Bezug auf den Nachtrag vom 24.09.
    - die UV-Annahmen
    - der Streitpunkt des CEMZ-Kriteriums
    - "massive Fassung" bei Glied 7
- Die Leitung hat alle Auflagen A und R in NACHTRAG-ENTWURF-V2.md umgesetzt, dazu die Empfehlungen B12, B13 und B16.
- Ein zweiter frischer Leser prueft die geaenderten Saetze, seit ~21:23. Eingefuegt wird erst danach.

### SPIN2-D4-2 gestartet (Finn: "mach weiter"; eingetragen 2026-10-01 21:28:38 CEST)

- feldforscher ab ~21:29, Karte RUNDE-13/spin2-d4-2/KARTE.md (Erwartung 21:27:52).
  - Frage: Traegt die IR-endliche M_E-Methode von Bellazzini u. a. externe Gravitonen und den Dreipunkt-Vertex?
  - Pflicht ist eine Annahmen- und Observablen-Tabelle, nach den Vorgaben der Codex-Lesung.
  - Erwartung der Leitung: "nur mit neuer Annahme" ~55 %.
- Aktive Agenten:
  - frischer Leser des Spin-2-Nachtrags V2
  - SPIN2-D4-2
  - Q-STERN: Warteschlangen auf der .69, der Agent wacht womoeglich selbst wieder auf

### SPIN2-D4-Nachtrag: zweite Lesung, Fassung V3 (eingetragen 2026-10-01 21:36:45 CEST)

- Zweiter frischer Leser (21:21 bis 21:35; LESUNG-LETZTE-SCHICHT-V2.md): "einfuegen nach genannten Aenderungen".
  - Von 14 alten Auflagen sind 10 erfuellt, 2 weitgehend, 2 teilweise; keine ist verfehlt.
  - Neu: N1 bis N4 (A) und N5 bis N8 (R).
    - N1: Ein Satz zu "fifth forces" war wieder in Subjekt und Objekt vertauscht, derselbe Fehlertyp wie B2.
    - N2: "nicht unabhaengig" stand ohne die Einschraenkung "the physical assumptions are quite distinct".
    - N3: Bei Bellazzini fehlte die Bedingung "when the limits are taken in the correct order".
    - N4: Der Nachtrag vom 24.09. war strenger wiedergegeben, als er ist.
- Die Leitung hat N1 bis N8 umgesetzt, dazu E1 bis E7, in NACHTRAG-ENTWURF-V3.md.
  - Geaendert bzw. neu: Regge-Beschraenktheit als UV-Annahme; Bucciotti Theorem 3.1 auf S. 14-15; die Bedingtheit nicht
    an D = 4 gebunden (CEMZ S. 26).
  - Die neuen Zitate sind per grep in den Quelltexten geprueft, alle gefunden.
- Ein dritter frischer Leser prueft V3, seit ~21:43. Eingefuegt wird danach.
- [H] Lehre fuer die Leitung: In deutschen Saetzen mit zwei Plural- oder Neutrum-Nominalgruppen sind Subjekt und Objekt
  formgleich. Beim Uebersetzen englischer Quellsaetze die Richtung ausdruecklich machen (Passiv oder "von ... nicht
  begrenzt"). Der Fehler kam zweimal vor.

### SPIN2-D4-2 (feldforscher, 21:29 bis ~21:48; RUNDE-13/spin2-d4-2/SPIN2-D4-2.md, Quellen mit sha256; eingetragen 2026-10-01 21:48:09 CEST)

- **Ausgang nach der Scheiterregel: nur mit neuer Annahme.** Die D = 4-Lage bleibt bedingt.
  - Die M_E-Methode traegt externe Gravitonen. Fuer die g^3-Schranke reicht sie nicht: Jeder g^3-Beitrag hat einen
    Faktor G, und genau diese Ordnung steckt im Rest, den M_E nicht kontrolliert.
  - Noetig ist eine von zwei Annahmen, die Bellazzini u. a. selbst nennen:
    - eine meromorphe Hochenergie-Amplitude, was laut den Autoren mehr verlangt als schwache Kopplung (S. 13, 30)
    - Kontrolle der Unitaritaet eine Ordnung weiter, bei ihnen offen (S. 30)
- Erwartungsverstoesse:
  - M_E ist schon auf Gravitonen angewandt: Fernandez/Ruhdorfer/Serra 2026 (arXiv:2603.15755v2, Anhang F) begrenzen die
    Vier-Graviton-Kopplung g4 ohne harten Schnitt. g^3 rechnen sie nicht. Die Spin-2/3-Regeln mit Graviton-Pol, aus denen
    Caron-Huot u. a. die g^3-Schranke gewinnen, fehlen in M_E-Form.
  - Das Hindernis ist die Ordnung in G, nicht Helizitaet 2 oder Kreuzung (S. 10, 7).
  - Masselose aeussere Teilchen sind fuer die Gravitation ausdruecklich eingebaut (Gl. 3.7, 4.12).
- Vorab gegen Ausgang (Leitung):
  - "nur mit neuer Annahme" ~55 %: getroffen.
  - "g^3 mit M_E schon gerechnet" ~15 %: nicht belegt. Gesucht wurde in den INSPIRE-Zitaten beider Arbeiten (Abstracts)
    und in einem Volltext.
- Leitung: sha256sum -c der Quellen ohne Fehler; Titel 2603.15755v2 und die Meromorphie-Stelle bei Bellazzini im Text
  gefunden.
- Moegliche naechste Karte [H]: die Spin-2/3-Summenregeln mit Graviton-Pol in M_E-Form, also die fehlende Rechnung.
  Das waere Theoriearbeit, keine Lesekarte, und gehoert erst nach einer Fremdlesung dieses Berichts auf die Liste.
- Selbstanzeigen des Agenten:
  - zwei geschaetzte Eintragszeiten, berichtigt
  - eine falsche Koautoren-Angabe, berichtigt
  - Die Zitatsuche lief nur ueber Abstracts; Anhang F zeigte erst der Volltext.

### SPIN2-D4-Nachtrag eingefuegt (eingetragen 2026-10-01 21:57:13 CEST)

- Vierte Lesung (21:48 bis 21:55; LESUNG-LETZTE-SCHICHT-V4.md): "einfuegen nach genannten Aenderungen".
  - N13 (A): Der Kreis der gelesenen Volltexte stimmte nicht. EGHS liegt ausserhalb von quellen/ von SPIN2-D4, und CEMZ
    und Bucciotti waren nicht auf alpha ~ 1 geprueft.
  - N14 (R): Der Regge-Satz liess sich so lesen, als braeuchten Caron-Huot u. a. gar keine Regge-Annahme.
  - 8 von 8 Zitaten woertlich, nichts vertauscht.
- Die Leitung hat N13 und N14 in V5 umgesetzt.
  - N13: alpha ~ 1 ohne "nur", mit benanntem Pruefkreis.
  - N14: Regge-Annahme in schwaecherer Form, mit S. 2 "imposed at all energy scales".
  - Die neuen Zitate sind per grep im Quelltext gefunden.
- **Eingefuegt** in WARUM-SPIN-2.md als "Nachtrag vom 2026-10-01 21:56:56 CEST" (ab Z. 813). Altbestand bytegleich zur
  Sicherung .bak-20261001c.
  - Im Nachtrag selbst steht offen: Die letzten zwei Korrekturen hat kein weiterer frischer Leser gelesen.
  - Die doppelte Datumsangabe im Kopf war ein Einfuege-Fehler der Leitung und ist sofort berichtigt.
- Lehre [H]: Vier Leserunden fanden je kleinere Fehler, und jede Korrektur der Leitung erzeugte neue, kleinere. Fuer
  zentrale Dokumente kuenftig von Anfang an enger formulieren: nur belegte Saetze, jede Einschraenkung woertlich aus der
  Quelle, keine Zusammenfassungen ueber Quellenkreise.

### Q-STERN, nachgereichte Hauptlaeufe (Agent fortgesetzt 22:47; ERGEBNIS.md Abschnitt 10; eingetragen 2026-10-01 22:57:24 CEST)

- **Ausgang nach der Regel: unentschieden fuer alle drei alpha.**
  - Ursache im Plan: Das Aufloesen der schwellennahen Streifenraender verbrauchte in jedem Teillauf das Budget von 540 s.
    Die Lokalisierung kommt danach und ist ueberall entfallen.
  - Ohne lokalisiertes Rechteck ist "gesehen" nicht erreichbar.
- Kontrollen: K1 bestanden, K2 fuer alle drei alpha (<= 1,2e-10). K3 entfaellt, weil nach der Regel keine Stelle
  gefunden wurde.
- Gemessen, aber nicht regelgerecht (Lagen linear zwischen zwei Zeilen interpoliert):
  - alpha = 0,01: s wechselt auf beiden Stufen zwischen omega^2 = 0,750 und 0,755, also bei ~0,7528 (-0,045). Am Ort ist
    2|Phi(0)| ~ 0,10, gerade an der Grenze der Karte.
  - alpha = 0,03: ~0,6997 (-0,098), nur im Nebenlauf knapp unter dem Fenster. Kompaktheit 0,26 bis 0,14.
  - alpha = 0,1: vermutlich unter 0,65. s ist von 0,65 bis 0,90 negativ; darunter findet die Rechnung keinen Hintergrund.
    Kompaktheit 0,51 bis 0,22.
- Vorab gegen Ausgang (Leitung):
  - "gesehen" bei 0,03 (~90 %) und bei 0,1 (~75 %): nicht eingetreten (unentschieden).
  - |Delta| <= 0,05 bei 0,1: nicht eingetreten.
  - "omega*^2 sinkt mit alpha" (~55 %): eingetreten [H, ohne Regelwert].
  - K1 bis K3 ~80 %: K1 und K2 ja, K3 entfallen.
- [H] Bedeutung: Die stille Stelle reagiert stark auf Eigengravitation. Schon bei Kompaktheit ~0,1 wandert sie um
  ~0,045 in omega^2.
  - Fuer gravitierende Q-Baelle (Bosonensterne) liegt sie also woanders als im flachen Raum.
  - Fuer Laborbaelle ist der Effekt bedeutungslos.
  - Alles nur in Cowling-Naeherung und Newton-Grenzfall, beides bei diesen alpha fraglich.
- Selbstanzeigen:
  - Leitung: alpha ohne Kompaktheitsabschaetzung gewaehlt.
  - Agent: Lokalisierung im Plan hinter die Streifen gelegt, ohne Budget; ein lokaler awk-Aufruf (verboten); die
    Auswertung zaehlt die Nebenlaeufe mit (jq-Gegenprobe ohne sie: gleiche Ausgaenge).
- **Entscheidung der Leitung:** Kein Nachtrag zur Lokalisierung bei alpha = 0,01. Er waere nachtraeglich beschlossen und
  bliebe ein Befund ohne Test.
  - Stattdessen fuer Runde 14 eine neue Karte Q-STERN-2:
    - alpha ueber eine Ziel-Kompaktheit (2|Phi(0)| in {0,01; 0,03})
    - volle Rechnung erster Ordnung mit delta Phi statt Cowling
    - Lokalisierung im Plan zuerst, mit eigenem Budget
    - Vorhersage aus der hier gemessenen Steigung (Delta omega^2 ~ -4,5 alpha bei kleinem alpha, Cowling)

## Abschaetzung (Leitung, 2026-10-01 22:57:45 CEST, date)

| Karte | Entscheidung | Grund |
|---|---|---|
| LEITER-3D-PRAEZ | erledigt (im Paper v0.13); Fortsetzung n >= 11 parken | n = 7 bis 10 nach der Regel gesehen (Vorzeichenwechsel mit aufgeloestem Umlauf, Abstand zu den Breitenminima <= 2,7e-6). Ab n = 11 liegt das Kernwachstum ueber 1e8; dafuer braeuchte es eine andere Integration |
| B-BALL-LEITER (mit 2, 2b, 2c) | parken mit Befund | Karte 1 "nicht gesehen" in den Baendern. Log-Stelle nachtraeglich bei 0,9256 (zwei Stufen, Umlauf -1). Mischtest: bis t = 0,75 stetig. 2b "nicht gefunden" (Fenster der Leitung falsch gesetzt), 2c "Falte": Die Sextik-Stelle laeuft zu t -> 1 weg, die Log-Stelle ist sehr wahrscheinlich eine eigene. Offen: unabhaengiger Nachbau der Log-Stelle; Verbleib der Sextik-Stelle zwischen t = 0,975 und 1 |
| AFM-BREITE | parken mit Befund | Gesetz traegt: ln Gamma = 2,549 - 2,860/sqrt(1 - Omega^2), fuenf neue Mitglieder hoechstens 0,29 Dekaden daneben. Weiter nur mit einer Herleitung (Tunneln oder Fourier) |
| QUARK-1-BERICHTIGUNG | erledigt | X(2370)-Angaben berichtigt |
| Q-STERN | weiter als Q-STERN-2 (Runde 14) | Alle drei alpha nach der Regel unentschieden (Lokalisierung nicht budgetiert). Gemessen: Die Stelle wandert stark nach unten (alpha = 0,01: ~ -0,045). Die alpha waren zu gross gewaehlt (Kompaktheit bis 0,59). Neu: Kompaktheitsziel, delta Phi statt Cowling, Lokalisierung zuerst |
| SPIN2-D4 | erledigt, Nachtrag in WARUM-SPIN-2.md | Nach den Vorabklassen Regime A, bedingt: Es gibt D = 4-Fassungen (CEMZ Abschn. 3.5 und Fn. 23; Caron-Huot u. a. 2022), ihre IR- und UV-Annahmen sind umstritten. Nach Fremdlesung (Codex) und vier Lesungen der letzten Schicht eingefuegt |
| SPIN2-D4-2 | parken (fehlende Rechnung benannt) | Nur mit neuer Annahme: M_E traegt externe Gravitonen, aber g^3 liegt in der unkontrollierten Ordnung G. Die fehlende Rechnung sind die Spin-2/3-Summenregeln mit Graviton-Pol in M_E-Form. Theoriearbeit; erst nach einer Fremdlesung auf die Liste |
| ZWEIFELD-BIC | bei Codex | Codex hat die Frage angenommen und die Kontrolle berichtigt (Schwellen in rho, kappa = 0 ist nicht die alte Kontrolle, Rangdefekt der Matching-Matrix statt einzelner Umlaeufe) |
| AFM-KANAL-2 (aus R12) | Fremdstimme erledigt | Hauptausgang unentschieden. Ergaenzt gilt "auf dem ergaenzten Raster nicht gesehen", ohne Ausschluss. Journal-Berichtigung nr 549 |

- **Vorab gegen Ausgang, Leitung (diese Runde):**
  - LEITER-3D-PRAEZ: alles getroffen.
  - B-BALL: K1 und Schritt 0 getroffen; "gesehen ~45 %" nicht.
  - B-BALL-2: drei von drei getroffen.
  - B-BALL-2b: "gefunden ~85 %" verfehlt, weil das Fenster falsch gesetzt war.
  - B-BALL-2c: "Falte ~30 %" eingetreten, "wandernd ~60 %" nicht.
  - AFM-BREITE: "traegt ~70 %" und c getroffen, die Lage nur halb.
  - Q-STERN: die Vorhersagen zu "gesehen" und zur Verschiebung verfehlt, die Richtung getroffen.
  - SPIN2-D4: "Regime B ~70 %" verfehlt; nach den eigenen Klassen ist es Regime A, bedingt.
  - SPIN2-D4-2: "nur mit neuer Annahme ~55 %" getroffen.
- **Lehren der Runde:**
  - Suchfenster nicht auf Monotonie stuetzen; weit waehlen und die Zahl der Vorzeichenwechsel zaehlen (B-BALL-2b/2c).
  - Kopplungsstaerken ueber eine physikalische Zielgroesse waehlen, z. B. die Kompaktheit, nicht frei (Q-STERN).
  - Den Plan so budgetieren, dass das Entscheidende (Lokalisierung) zuerst laeuft (Q-STERN).
  - Vorabklassen von Lesekarten mit einer eigenen Klasse "bedingt vorhanden" anlegen (SPIN2-D4).
  - Nachtraegliche Funde als Befund ohne Test fuehren; bestaetigen mit einer vorab festgelegten Folgekarte (B-BALL).
  - Beim Uebertragen englischer Quellsaetze ins Deutsche die Richtung (Subjekt/Objekt) ausdruecklich machen.
    Zentrale Dokumente von Anfang an eng formulieren; vier Leserunden waren noetig.
- **Selbstanzeigen:**
  - Leitung:
    - Fenster in 2b
    - alpha in Q-STERN
    - Fehlstart AFM-BREITE (fehlende Module)
    - drei zu starke Chatmeldungen an Finn, jeweils berichtigt: B-Ball "sehr wahrscheinlich dieselbe Stelle", Spin-2
      "nur Erwartung" und "ein Spin-4-Teilchen", Magnetball "mathematisch nicht null"
    - doppeltes Datum beim Einfuegen des Nachtrags
  - Agenten:
    - awk lokal (B-BALL einmal, Q-STERN einmal)
    - bc lokal (B-BALL)
    - ein ungequoteter Heredoc (B-BALL)
    - geschaetzte Zeiten, berichtigt (mehrere)
    - ein python-Versionsaufruf ohne Grenzen (Q-STERN)
    - zwei Abrufe ohne Erwartung (SPIN2-D4)
- **Offen bei Codex:** ZWEIFELD-BIC (Dreikanal-Matching), L2-Zertifikat, Paper (v0.17).

## Einfach gesagt (Rundenende)

In dieser Runde haben wir die Leiter der stillen Schwingungen in 3D bis zur zehnten Stufe doppelt abgesichert. Ausserdem
haben wir herausgefunden, dass ein Dunkle-Materie-Ball ebenfalls eine stille Schwingung hat; es ist aber eine andere als
in unserem Modell. Spuert der Ball seine eigene Schwerkraft, wandert die stille Stelle deutlich; das genau zu messen,
braucht einen besser geplanten Versuch. Bei der Frage, ob neue schwere Teilchen in unserer Welt zwingend sind, wissen wir
jetzt: ja, aber nur unter Annahmen, ueber die die Fachleute noch streiten.

## Rundenabschluss (Leitung, 2026-10-01 22:58:24 CEST)

- Journal: claude-runde-v3-13-20261001, Index nr 550; pruefen ohne Befund.
- Sicherung .69 -> TS440 gestartet (ohne --delete, nice/ionice). Log auf der .69:
  /home/fmh/sicherung-dot69-ts440-lauf-20261001-r13.log. Die r12-Sicherung endete vorher mit rc = 0 (siehe Log r12).
- In Runde 14 uebernommen:
  - Q-STERN-2 (Kompaktheitsziel, delta Phi, Lokalisierung zuerst)
  - Fremdlesung SPIN2-D4-2, bevor die fehlende Rechnung auf die Liste kommt
  - optional: unabhaengiger Nachbau der Log-Stelle, Herleitung des AFM-Breitengesetzes
  - Codex-Ergebnisse (ZWEIFELD-BIC, Paper)
  - die taeglichen Pflichten am 02.10.
