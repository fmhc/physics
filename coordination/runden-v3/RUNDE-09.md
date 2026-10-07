
Leitung: claude-primary. Angelegt: 2026-09-30 07:03:32 CEST (gemessen, date vor dem Ziehen der Zufallskarte). Explorativ,
keine formale Bestaetigung. Finn: "weiter rechnen und ergebnisse melden" (07:00), "was heisst das denn jetzt eigentlich im
gesamtkontext? auf einfach?" (07:01, beantwortet im Chat).

- **Berichtigung (2026-09-30 07:52:31 CEST, Leitung):** Die Angaben "Finn HH:MM" in dieser Datei sind nicht mit date gemessen. Die Leitung
  hat sie aus dem Gespraechsverlauf geschaetzt; sie gelten nur als Reihenfolge. Mit date gemessen sind nur die uebrigen
  Zeiten. Nachweislich falsch waren "07:53" und "07:55": Beide Nachrichten kamen vor 07:52:04; berichtigt.

## Rahmen

- Uebernommen aus Runde 8, laufend: BEWEIS-1, SP-1, FA-1, EVO-1 Generation 1, Polprobe n = 8 (cpu2).
- Fast Lane: unabhaengige Karten parallel; wo moeglich werden fertige Agenten mit ihrem Kontext fortgesetzt statt neuer.
- Rechenorte:
  - .69 ueber kleintest.sh; cpu5 bleibt BEWEIS-1 vorbehalten
  - Laptop-CPU fuer kleine Laeufe der Leitung
- Offene Entscheidungen Finns:
  - APS-Login oder Datenanfrage (ST-1)
  - restic-Aufraeumen auf dem TS440
  - Ollama-Stopp (WM-1-MB, B28 und CX-1 warten)

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| BEWEIS-1 | R7/R8 | rechnergestuetzter Beweis n = 1, Auflagen der Lesung (B1, W1 bis W7) einarbeiten, Zertifikat rechnen | Beweis-Agent (laeuft, Spur cpu5) |
| SP-1 | R8 | stille Stellen fuer l = 1 und l = 2; Vergleich mit den eingefrorenen Vorhersagen (VORHERSAGEN-SP1.md) durch die Leitung | SP-1-Agent (laeuft) |
| FA-1 | R8, Finn 06:21/06:25 | Dreierstruktur bei N = 3 und g J < 0 (120 Grad, Neutralitaet zu dritt), Chiralitaet als Pseudospin | FA-1-Agent (laeuft) |
| EVO-1 | R7/R8 | Generation 1 (17 Modelle, Version 3) zu Ende rechnen; vor der Auswertung N5-Pruefung, dann A2 und A3 | Ketten cpu3/cpu4, Leitung |
| BIC-4 Duennwand-Numerik | R8 BIC-3 (c) | Stellen n >= 7 bei beta = 0,5 mit Polverfolgung statt Vorzeichen von s. Liegen die Breitenminima bei 0,5598 / 0,5526 / 0,5470 / 0,5424, und ist dort Gamma < 1e-6? | Leitung (pole-Laeufe) |
| GF-BIC-2 zweite Leiter | R8 GF-BIC | Umlauftest fuer die psi_2-Nullstellen (Gegenlaeufer); numerische Probe der Abbildung auf beta_eff am gemischten Ball (eine Stelle) | GF-BIC-Agent (fortgesetzt) |
| ST-2 Glied 7 | R8 ST-1 | Die vier Lager der Geister-Theorien (Lee-Wick, Fakeonen, ...) gegen messbare Vorhersagen: Wo gaebe es eine Laborsignatur (Akausalitaet, Kurzreichweite)? | derselbe Papier-Agent |
| **Bio 13, Zufallskarte** | RUNDE-02, R4 neuron | "Neuron mit Schwelle": damals keine Schwelle, glatte Antwort. Gibt es mit einem Q-Ball nahe einer stillen Stelle eine schwellenartige Antwort (scharfe Resonanz statt glatt)? | offen |

- **Nachtrag 2026-09-30 07:07:23 CEST: Karte KOLL-1 kollektive Wellen** (Finn 07:05: "können die teilchen klumpen ggf muster erzeugen die
  dann schwingungen weiter geben die übergeordnet sind?"):
  - Frage: Koppeln zwei (spaeter drei) gegenphasige Baelle an der stillen Stelle ihre Atmung nur noch ueber die Raender?
    Dann waere die Weitergabe fast verlustfrei, anders als ohne stille Stelle (0,76).
  - Schritte:
    - (a) Kopplungsmodentheorie J(d) gegen Strahlungsanteil
    - (b) achsensymmetrischer Zweiball-Test auf der P4000
    - (c) Dreierkette
  - Hypothese [H]; Bearbeiter: Code-Agent seit 07:07.
  - Codex' abstrakte Hierarchie-Modenmodelle (hierarchy-memory-20260930) sind keine Q-Ball-PDE; KOLL-1 ist die
    PDE-Probe dazu.
    - Die statische Lesart ergaebe kein Frame-Dragging; dagegen stehen Gravity Probe B (-37,2 +- 7,2 mas\/Jahr) und
      LAGEOS\/LARES.
    - Welche minimale Mitfuehrungsannahme reproduziert Einstein, und welche zweite Messung prueft sie?
  - Bearbeiter: Papier-Agent (fortgesetzt).
- **Nachtrag 2026-09-30 07:42:41 CEST: Karten ROT-1 bis ROT-3 Drehung im Feld** (Finn 07:44: "was gibts für drehimpulse oder so in dem feld,
  wie sieht das feld davon aus und wie könnte es sich oszillierend selbst stabilisieren"):
  - ROT-1 [H]: Wirbel mit gefuelltem Kern im gemischten Ball (psi_1 mit m = 1, psi_2 fuellt den Kern). Energie und
    Zeitstabilitaet gegen den einfachen Wirbel.
  - ROT-2 [H]: innerer Rotor der relativen Phase ueber den cos(2 Delta theta)-Mulden. Gibt es stationaere Loesungen, und
    wo strahlen sie nicht?
  - ROT-3 (Literatur): Bruchwirbel mit Waenden bei cos(2 Delta theta)-Kopplung als Einschluss-Analogon.
  - ROT-3 laeuft (feldforscher, gestartet vor 07:42:03; das ist die erste Zeitmessung danach). ROT-1 und ROT-2 warten
    auf Finns Freigabe und das ROT-3-Ergebnis.
  - **Freigabe Finn 07:47** ("ja, starte ROT-1 und ROT-2 auch"), gestartet 2026-09-30 07:45:42 CEST:
    - ROT-2: GF-BIC-Agent fortgesetzt; innerer Rotor, dazu die Frage nach stillen Stellen im Gegentakt
    - ROT-1: neuer Code-Agent; 2D-Querschnitt, weil der Kopplungsterm bei g != 0 und Windung nur in psi_1 wie cos(2 phi)
      variiert und die Achsensymmetrie bricht
- **Nachtrag 2026-09-30 07:42:41 CEST: Karte ZUS-10 zehn Zusammenhangs-Ideen** (Finn 07:41: "ideate noch mal 10 ideen zu zusammenhängen und
  prüfe die"):
  - Ideation durch einen Agenten (RUNDE-09/zusammenhaenge/IDEEN-10.md).
  - Dann eingefroren; danach Pruefung durch einen frischen Agenten (Papier, Literatur, Rechnungen je hoechstens 10 min).
- **Nachtrag 2026-09-30 07:52:04 CEST: Karte MESS-1 Troepfchen-Bruecke** (Finn, vor 07:52:04: "überlege noch mal wo wir in bestehenden experimenten
  sowas aus rechnungen nachweisen können"):
  - Hypothese [H]: Selbstgebundene Quantentroepfchen (EGPE mit LHY, binaere oder dipolare Gase) sind Q-Ball-artig
    (flaches Innenprofil, duenne Wand). Ihre Atmungsmode liegt fuer kleine N im Kontinuum (Selbstverdampfung).
  - Frage: Hat die Emissionsbreite gegen N stille Stellen? Das ergaebe eine Vorhersage fuer bestehende Experimente
    (Daempfung bzw. Verlust mit Einbruechen bei N_n).
  - Literatur und Rechnung in einem Agenten (Code-Agent, gestartet vor 07:52:04).
  - Weitere Laborbezuege: kubisch-quintische Optik (liquid light), eingebettete Solitonen; lose: Riesen-Monopolresonanz
    der Kerne.
- **Nachtrag 2026-09-30 07:52:04 CEST: Karte SUCH-1 Suchwoerter** (Finn, vor 07:52:04: "mach mal ein research zu suchworten die das beschreiben woran wir
  gerade arbeiten"): Suchwortlisten je Thema, Suche damit und das Urteil "bekannt unter welchem Namen"
  (RUNDE-09/SUCHWORTE.md; feldforscher).
- **Nachtrag 2026-09-30 08:02:33 CEST: Karte KRAFT-1 Analogkraefte** (Finn, vor 08:02:16: "können wir daraus andere kräfte ableiten?",
  dann "mach das"; Agent gestartet vor 08:02:16, das ist die erste Zeitmessung danach):
  - Hypothesen [H], je Formel und kleiner Test:
    - (a) Yukawa-artig ueber die Raender, Reichweite 1/sqrt(1 - omega^2), Vorzeichen nach Phase (R3 1D: 0,554 gegen 0,548)
    - (b) Bjerknes-artig ueber die Abstrahlung atmender Baelle, ~ 1/d^2; Vorhersage: an einer stillen Stelle schaltet
      diese weitreichende Kraft ab ("Kraftschalter")
    - (c) Schall (Goldstone) in einem Hintergrundkondensat: 1/r (3D), ln r (2D), linear (1D); Medium-Codes aus R6
  - Grenze vorab: Das alles sind skalare Analoga; Elektromagnetik braucht ein Eichfeld (Spin 1), Gravitation ein
    masseloses Spin-2-Feld.
  - Bearbeiter: Code-Agent (RUNDE-09/kraft1/). KOLL-1-Driftdaten werden gelesen, nicht gedoppelt.
- **Nachtrag 2026-09-30 08:16:44 CEST: Teilkarte TET-1 und Karte SD-1.** Finn schrieb drei Nachrichten:
  - "was ist wenn eine quark farbe eine seitenansicht von einem tetraeder oder so ist?"
  - "bzw wir das mit einer analogie eines leuchtturmes betrachtne sollten der verschiedene abstrahlwinkel hat ..."
  - "also von vorne betrachtet schießt der energie, von hinten zieht er energie und von genau der seite fließt energie
    durch ... oder die drei modi sind die übergänge von der ladung in dem teil - drin, draußen oder im übergang ...
    insb. wenn man es mit zwei zweier dings betrachtet?"
  - Zeiten: Die ersten beiden Nachrichten erschienen zwischen den Messungen 08:09:33 und 08:13:15, die dritte zwischen
    08:13:15 und 08:15:10.
  - Antwort im Chat (08:16), Kernpunkte:
    - Das Muster vorne/hinten/Seite ist die l = 1-Schwappmode; SP-1 zeigt, dass sie stille Stellen hat.
    - "Drin, draussen, Uebergang" ist das Drei-Zonen-Modell (MOD-1).
    - Die drei Schwapprichtungen bilden linear ein Tripel [H]; Baryon als Volumen (epsilon_abc); Pati-Salam als
      Tetraeder [L].
  - **TET-1 [H]** (Teilkarte im KRAFT-1-Agenten, +45 min):
    - Dreieck aus drei Baellen mit 0/120/240 Grad, vierter Ball an der Tetraederspitze.
    - Aus Symmetrie hat E_int(phi) nur die Harmonischen 3m, exakt. Pruefbar ist die Reichweite des Rests: log-Steigung
      2,5 bis 3,5 kappa0, Gegenprobe 0/0/0-Dreieck.
  - **SD-1 [H]:** stille Stellen der gegenphasigen l = 1-Mode (Spin-Dipol) im gemischten Ball, g = 0,2.
    - Der Theorie-Agent (MOD-1, fortgesetzt) schreibt blinde Vorhersagen (RUNDE-09/sd1/VORHERSAGEN-SD1.md); die Leitung
      friert sie ein.
    - Der SP-1-Agent (fortgesetzt) baut gfbic.py mit --l in einer Kopie. l = 1-Scans erst nach der Freigabe der
      Leitung.
    - **Vorhersagen eingefroren 2026-09-30 08:28:19 CEST** (VORHERSAGEN-SD1.md.eingefroren-20260930-082819; die Datei
      war fertig um 08:27:29).
      - Vorab-Pruefung der Leitung: Vor 08:27:29 gab es in sd1/ nur Rauchtests fuer psi_2 mit l = 0 und psi_1 mit l = 1,
        keinen psi_2-l = 1-Lauf. Die .69-Ketten P und Q von 08:28:03 sind l = 0- bzw. psi_1-Proben.
      - Kern der Vorhersage:
        - Gemeint ist der gegenlaeufige l = 1-Partner (nu ~ omega + sqrt(E)). Stille Stellen bei ~0,539 (falls der Ast
          dort existiert), 0,525 und 0,515, je +-0,004, mit wechselnder Umlaufzahl.
        - Der Ast existiert erst unter ~0,540 bis 0,548.
        - Der eigentliche Spin-Dipol (nu = omega - sqrt(E)) ist echt gebunden (Gegenprobe).
        - Gegenprobe g = 0,02: Existenzschwelle ~0,629 +- 0,01.
      - Freigabe an den SD-1-Rechner um 08:28:19.
- **Nachtrag 2026-09-30 08:28:19 CEST: Karte MOD-2**, blinder Test des Duennwandmodells: Der Theorie-Agent sagt aus seinem
  Modell omega*^2 fuer n = 10 bis 15 (beta = 0,5) voraus, ohne RUNDE-09.md und die n >= 10-Laufordner zu oeffnen.
  - n = 11 (FORMEL-1) ist fuer ihn blind; n = 12 und 13 laufen gerade (FORMEL-2); n = 14 und 15 rechnet die Leitung nach
    dem Einfrieren.
- Zufallskarte gezogen um 2026-09-30 07:03:32 CEST (date) mit `shuf -n 1` aus den Pool-Eintraegen mit Entscheidung
  "parken", ohne Chem 14.

## Tests: Ergebnisse

### BIC-4 Duennwand, Polsuche (eingetragen 2026-09-30 07:07:55 CEST)

- Vorab (RUNDE-08, 06:52:42): Fortsetzung der Leiter mit Schritt 2,29 +- 0,03 in 1/(x - 0,5): n = 7 bei 0,55984 +- 0,0003
  (halb bekannt), n = 8 bei 0,55263 +- 0,0003 (blind), n = 9 bei 0,54697 +- 0,0003 (blind).
- Der Vorzeichentest (kurve) war nach der Vorab-Regel nicht entscheidbar (Kernwachstum 1e9). Die Polsuche wurde danach
  gewaehlt, nachtraeglich. Die Lagen stammen aber von vorher.
- **n = 8** (pole, .69, Ende 07:06:35), Breitenast Re rho ~ 1,58:
  - 0,5520: 1,5802531 - 4,77e-4 i
  - 0,5526: 1,5826358 - 4,66e-7 i
  - 0,5532: 1,5849783 - 3,96e-4 i
  - Das Minimum der Breite (V-Form, sqrt(Gamma) 0,0218 / 0,0007 / 0,0199) liegt an der vorab fortgesetzten Stelle 0,55263.
  - Belegstufe: Minimum 4,7e-7, kein Umlauftest.
- **n = 7** (pole, .69, Ende 07:18:32):
  - 0,5592: 1,5877679 - 3,23e-4 i
  - 0,5598: 1,5897567 - 1,81e-6 i
  - 0,5604: 1,5917232 - 2,22e-4 i
  - Das Minimum der Breite liegt bei 0,5598, an der Fortsetzung 0,55984. Der Vorzeichentest hatte hier versagt
    (Zweigmischung).
- **n = 9** (pole, .69, Lauf ab 07:28:47):
  - 0,5464: 1,5743805 - 5,57e-4 i
  - 0,5470: 1,5772052 - 6,24e-6 i
  - 0,5476: 1,5799017 - 7,71e-4 i
  - Das Minimum der Breite liegt bei 0,5470, an der blind fortgesetzten Stelle 0,54697 +- 0,0003.
- **Zwischenbilanz Duennwand:** n = 7, 8 und 9 liegen als Breitenminima an den vorab fortgesetzten Stellen (Schritt 2,29 in
  1/(x - 0,5)). Die Methode (Polsuche) wurde erst nach dem Vorzeichentest gewaehlt, die Lagen standen vorher fest.
  Belegstufe: Minimum, kein Umlauftest.

### ABSTAND: Welches Gesetz haben die Abstaende? (Finn 07:10; Vorab-Erwartung der Leitung 2026-09-30 07:11:11 CEST, vor der Rechnung)

- Getestete Gesetze fuer die Folge x_n = omega*^2 (n = 1, 2, ...) je beta, mit x_min = 1 - 1/(4 beta):
  - linear: x_n = a + b n
  - exponentiell: x_n - x_min = A r^n (fester Faktor)
  - logarithmisch: x_n = a + b ln n
  - Potenz: x_n - x_min = A n^p
  - Kehrwert (Phasenregel): 1/(x_n - x_min) = a + b n
  - Primzahlen: 1/(x_n - x_min) = a + b p_n mit p = 2, 3, 5, 7, 11, 13, ...
- **Erwartung:**
  - Das Kehrwert-Gesetz passt am besten; Potenz mit p nahe -1 als Zweites.
  - Linear, logarithmisch, exponentiell und Primzahlen liegen um mindestens den Faktor 10 schlechter (Fitrest).
  - Der Faktor zwischen Nachbarn (x_n - x_min)/(x_{n+1} - x_min) ist nicht konstant und geht gegen 1 wie (n + 1 + c)/(n + c).
- **Ausgang** (RUNDE-09/abstand/abstand.py, Laptop, unter 1 s, 07:11:39; eingetragen 2026-09-30 07:12:10 CEST). RMS-Rest in omega^2 je Gesetz:

  | beta | Punkte | linear | exponentiell | logarithmisch | Potenz | Kehrwert | Primzahlen |
  |---|---|---|---|---|---|---|---|
  | 0,35 | 4 | 2,9e-2 | 1,6e-2 | 1,2e-2 | 3,8e-3 | **3,1e-3** | 2,3e-2 |
  | 0,40 | 3 | 1,8e-2 | 8,4e-3 | 5,8e-3 | 3,1e-3 | **1,8e-3** | 1,9e-2 |
  | 0,45 | 3 | 1,6e-2 | 7,3e-3 | 4,6e-3 | 3,3e-3 | **1,8e-3** | 1,7e-2 |
  | 0,50 | 7 | 3,7e-2 | 2,4e-2 | 1,4e-2 | 8,1e-3 | **5,7e-3** | 2,9e-2 |
  | 0,55 | 5 | 2,4e-2 | 1,3e-2 | 7,4e-3 | 6,3e-3 | **3,8e-3** | 2,6e-2 |
  | 0,60 | 5 | 2,2e-2 | 1,2e-2 | 6,3e-3 | 6,5e-3 | **3,8e-3** | 2,4e-2 |

- Das Kehrwert-Gesetz ist bei allen sechs beta am besten, aber nur 1,2- bis 2-mal besser als das Potenzgesetz.
  - logarithmisch ist 2- bis 3-mal schlechter, exponentiell 4- bis 5-mal, Primzahlen 5- bis 8-mal, linear 6- bis 9-mal.
  - **Die Vorab-Erwartung "mindestens Faktor 10" ist damit nicht erfuellt**, die Reihenfolge schon.
- Grund fuer den Rest des Kehrwert-Gesetzes: Die Schritte in 1\/(x - x_min) sind nicht ganz konstant. Sie wachsen von 2,0
  auf 2,3 und naehern sich einem Grenzwert (beta 0,5: 2,04 \/ 2,21 \/ 2,25 \/ 2,27 \/ 2,28 \/ 2,30).
  - Die verfeinerte Phasenregel des Theorie-Agenten (Wellenzahl im Balleinneren) nimmt das auf.
  - Mit ihr lagen die acht blinden Vorhersagen auf etwa 1e-4 genau.
- Potenz-Exponent p = -0,76 bis -0,88; asymptotisch -1 (x - x_min ~ 1\/n).
- Der Faktor zwischen Nachbarn ist nicht konstant: bei beta 0,5 1,61 \/ 1,41 \/ 1,30 \/ 1,23 \/ 1,19.
  - Er faellt wie (n + 1,43)\/(n + 0,43), ab n = 2 auf 0,01 genau.
  - Also kein fester Faktor (nicht exponentiell), sondern eine Haeufung wie 1\/n.
- Kein Hinweis auf Primzahlen. Die Stellen zaehlen ganzzahlig durch, n = 1, 2, 3, ..., mit gleichen Abstaenden in einer
  Phasenvariablen.

### BEWEIS-1: Ausgang M4 (Beweis-Agent, 05:35:09 bis 07:11:14; RUNDE-07/beweis/BEWEIS.md; eingetragen 2026-09-30 07:14:06 CEST)

- **Der Autor meldet: bewiesen, rechnergestuetzt, im linearen Modell, Sektor l = 0.**
  - rho* in [1,744617544837398735781 +- 6,8e-22], omega*^2 in [0,797676787111865191750 +- 4,8e-22]
  - f(0) in [1,024235506571665864904 +- 2,8e-22]
  - Die Mode faellt wie e^{-kappa_c r} ab (kappa_c ~ 0,5244) und ist im Sektor l = 0 einfach (Lemma E).
- Kette: Schwanzlemmata P und J, Kugelarithmetik mit 256/320 bit, Cauchy-Reste, Brouwer-Krawczyk in (a, c, rho, omega).
  - Innenabstand 0,875 delta, Zeilensumme 5,7e-9.
  - Die Wiederholung mit L = 44 und 320 bit besteht mit einem Kasten innerhalb des ersten.
  - Kontrollen bestanden: Differenzenquotienten 2e-14, freies Modell, verschobener Kasten faellt durch.
- **Vertrauensannahmen und Luecken:**
  - Code-Gegenlesung durch ein zweites Haus fehlt.
  - Kein zweites unabhaengiges Programm.
  - python-flint wird als korrekt angenommen.
  - Eindeutigkeit im Kasten ist nicht gezeigt.
  - l > 0 und die nichtlineare Frage sind ausgeschlossen.
- **Leitung, 2026-09-30 07:14:06 CEST:**
  - Zweithaus-Auftrag an Codex ueber den Peerbus (Ereignis f67c1643): Code gegenlesen und das eigene Zertifikat getrennt
    weiterfuehren.
  - Frische Code-Lesung im Haus Anthropic (Fable) gestartet.
  - **Status bis dahin: "Beweis vom Autor gemeldet, Gegenpruefung laeuft"**, nicht "bewiesen".


    folgt fuer eine ruhende Masse exakt die Schwarzschild-Metrik: beta = gamma = 1, Photonensphaere 1,5 r_s, Schatten
    3 sqrt(3) GM/c^2.
  - EHT kann ihn nicht von Einstein trennen.
  - Nur bei woertlicher Lesung seiner Richtungsregel weicht er in zweiter Ordnung ab:
    - die Nebenringe sind etwa 3-mal schwaecher (Lyapunov 1,34 pi statt pi)
    - die Lichtablenkung zweiter Ordnung am Sonnenrand ist um 0,7 uas kleiner
    - heute nicht messbar; die Nebenringe erst mit BHEX
  - Woertlich statisch gaebe es kein Frame-Dragging. Gravity Probe B misst -37,2 +- 7,2 mas/Jahr (Einstein -39,2).
- **ST-2: Vorschlag parken.**
  - Alle vier Geister-Lager sagen dasselbe statische Potential voraus (Yukawa -4/3).
  - Unterschiede gaebe es nur in Streuprozessen (bei Labormassen ~1e-61 unterdrueckt) oder in der Kosmologie (nahe der
    Inflationsskala).
  - Akausalitaet im Labor: ~0,1 ps bei ~1e-14 N, unerreichbar.
  - Die Torsionswaage prueft schon, ob ein Spin-2-Pol ein Geist ist (meV-Bereich), kann die Lager aber nicht trennen.

### FA-1 Farb-Analogie (Agent, 06:36 bis Bericht ab 07:18:28, Datei zuletzt 07:21:23; RUNDE-08/fa1/ERGEBNIS.md; eingetragen 2026-09-30 07:22:24 CEST)

- **Der 120-Grad-Stern existiert als exakter stationaerer Ball, ist aber nicht der Grundzustand.**
  - Bei g J < 0 ist bei gleicher Ladung der gegenphasige Zweierball am tiefsten: ein Kanal leer, psi_2 = +-i psi_1,
    eher ein "Meson".
  - Der Stern liegt |g| I_4/12 darueber und |g| I_4/6 unter dem einkomponentigen Ball.
  - Der Gradientenfluss aus Zufallsstarts endet 12 von 12 Mal im Zweierball.
- **Stationaerer Kreisstrom:** Die drei Paarstroeme sind gleich (bei g = -0,3 etwa 10,95), mit gleichem Umlaufsinn, und
  heben sich je Kanal auf. Die Formel (sqrt 3/9)|g| I_4 trifft auf 0,03 %.
- **Ohne Reibung kreiselstabil:**
  - stabil bei g = -0,1 / -0,3 / -0,6 / +0,1
  - instabil bei -1,0 / +0,3 / +0,6, genau wo die Mode negativer Energie die Kontinuumsschwelle kreuzt (7 von 7, vorab)
  - Mit Reibung ist der Stern instabil (Thomson-Tait-Chetaev).
- **Pseudospin:** Die zwei Drehsinne sind exakt gleich tief. Eine Barriere gibt es nur bei erzwungen gleichen Amplituden;
  der Drehsinn ist dynamisch geschuetzt (Abweichung 0,037 bleibt, 0,128 kippt hin und her). Kein Raumspin.
- **Reichweite:** strukturelle Analogie (Z3-Phasen mit Summe null, Chiralitaet wie im Dreiecks-XY-Magneten); keine
  SU(3)-Ladung, keine Eichfelder, kein Einschluss, kein Quark.
- **Nebenbefunde zur Gesamtformel**, noch nicht in KANDIDAT.md eingetragen (braucht eine frische Lesung):
  - Fuer N = 3 und g < 0 liegt die Vakuumgrenze bei |g| <= 1,657, nicht 1,243; KANDIDAT 5.2 gilt nur fuer g > 0.
  - KANDIDAT 4.2, Folgerung 3 ("stationaer, kein Kanalstrom") gilt nur fuer reelle relative Phasen; der Stern ist das
    Gegenbeispiel.
- Vorschlag des Agenten: parken. Folgekarte waere das volle lineare Spektrum des Sterns. Die Frage nach Umlaufzahlen
  modulo 3 ist nicht bearbeitet.
- Regelverstoss des Agenten: einmal lokal awk (nur Anzeige); vermerkt im Fehlerkasten.

- **FA-1 an Codex uebergeben** (2026-09-30 07:27:58 CEST, Finn 07:26: "verfolg die idee mal weiter, ideate mit codex dazu gib das an den ab und mach
  weiter"): Peerbus-Auftrag 2dfb2f4c. Erbeten sind Ideation, eigene Rechnungen (volles Spektrum, stille Stellen des
  Sterns, Umlaufzahlen modulo 3, lambda-Term) und die Gegenpruefung der zwei KANDIDAT-Nebenbefunde. Anthropic doppelt
  FA-1 nicht.

### Bio 13 (Zufallskarte): Vorab-Erwartung der Leitung (2026-09-30 07:28:52 CEST, vor dem Lauf)

- Test wie gezogen, naechster Schritt aus dem Parkgrund (R4: "zuerst die Klumpenschwelle variieren").
  - Der einzige "Sprung" in R4 war Klumpenzahl 1 -> 0 zwischen amplitude -0,3 und -0,5, bei Schwelle S > 0,01.
  - Derselbe Neuron-Test (chemie_bio.py, R4, unveraendert bis auf die Schwelle) laeuft mit Schwelle 0,002 und 0,005.
- **Erwartung:**
  - Der Rest bei amplitude -0,5 ist ein breiter Ball mit omega^2 ~ 0,996 (R4) und Spitzendichte
    1 - sqrt(2 omega^2 - 1) = 0,0038.
    Hinweis: Diese Zahl ist aus R4 ableitbar, also keine unabhaengige Vorhersage (Regel "vorab ableitbare Kennzahl").
  - Schwelle 0,002: Klumpenzahl 1 bei -0,5; Schwelle 0,005: 0. Spitze/|eps| bleibt unveraendert (haengt nicht an der
    Schwelle).
  - Deutung: Der Sprung ist ein Artefakt der Klumpendefinition; es gibt keine Neuron-Schwelle.
  - **Scheitert, wenn** bei 0,002 die Klumpenzahl 0 oder mehr als 1 ist, oder wenn sich Spitze/|eps| aendert.
- **Ausgang Schwelle 0,002** (.69, p4000b, 07:32:48 bis 07:33:14; eingetragen 2026-09-30 07:33:44 CEST):
  - amplitude -0,5: Klumpenzahl 1 statt 0. Spitze\/|eps| und alle anderen Spalten sind unveraendert (1,938 usw.).
    Die Erwartung ist getroffen: Der R4-Sprung war die Schwelle der Klumpenzaehlung, keine Neuron-Schwelle.
  - Nebenbefund: Bei 0,002 zaehlen die stark gedehnten Laeufe (eps +-1,0) 7 bzw. 5 "Klumpen"; das sind vermutlich
    Strahlungswellen ueber der niedrigen Schwelle. Damit entstehen neue Scheinspruenge. Das Sprungkriterium haengt also
    an der Schwelle, und robustes Schwellenverhalten ist nicht gesehen.
  - **Schwelle 0,005** (07:33:14 bis 07:33:37): amplitude -0,5 zaehlt 0 Klumpen, wie erwartet (Spitzendichte ~0,0038 <
    0,005); dieselbe Sprungmeldung wie in R4, Spitze/|eps| unveraendert.
  - **Bio 13 insgesamt:** Die Erwartung ist in allen Punkten getroffen. Der Rest bei -0,5 ist ein duenner Ball (omega^2 ~
    0,996, Spitze ~0,004); die Klumpenzahl springt genau dort, wo die Zaehlschwelle diese Spitze kreuzt. Eine
    Neuron-Schwelle im Antwortverhalten ist nicht gesehen.


  - Sie enthalten eine Aether-Kinematik nur fuer bewegte Ladungen (pdf/rfeld.txt, Z. 31-34, 72-76).
  - Mitfuehrung und Gravitomagnetismus fehlen.
- **Die statische Lesart ist ausgeschlossen:**
  - Gravity Probe B: 5,2 sigma
  - LAGEOS/LARES 2016: ~20 sigma
  - Spinpraezession im Doppelpulsar: 3,9 sigma; statisch 2,26 statt 5,07 Grad/Jahr, gemessen 4,77 +0,66/-0,65
  - LARES-2 (Nature 2026) waere noch schaerfer, liegt aber nur aus einem Nachrichtenartikel vor [L?].
- **Minimale Erweiterung [H]:** volle Mitfuehrung des Brechungsbeitrags (kappa = 1) plus Fresnel-Mitnahme.
  - Das ergibt genau Einsteins Frame-Dragging.
  - kappa ist erzwungen: |1 - kappa| < ~5e-6 aus den Pulsar-alpha1-Grenzen.
- **Einordnung:** Mit Mitfuehrung bleibt in erster Ordnung keine eigene Vorhersage.
    keine Feldgleichung.
- Vorschlag des Agenten: verwerfen (als Unterscheider); als Dossier-Eintrag festhalten: "volle Mitfuehrung ist Pflicht;
  ohne sie ausgeschlossen, mit ihr in erster Ordnung gleich Einstein".

### GF-BIC-2 (Agent, 07:05:02 bis 07:38:30; RUNDE-08/gf-bic/ERGEBNIS.md, R9.1 bis R9.5; eingetragen 2026-09-30 07:38:59 CEST)

- **Zweite Leiter (psi_2): Umlauftest an allen drei Stellen bestanden**, jeweils zwei Rechtecke um den Fit, aufgeloest
  (Phasensprung hoechstens 0,300 rad):
  - Z1 (g = 0,2): omega*^2 = 0,7113723, nu* = 1,6888290, Umlauf -1 / -1 (auch h = 0,01)
  - Z2 (g = 0,2): omega*^2 = 0,6458619, nu* = 1,6103661, Umlauf +1 / +1 (auch h = 0,01)
  - Z3 (g = 0,4985): omega*^2 = 0,5511558, nu* = 1,5152569, Umlauf +1 / +1 (nur h = 0,02; Duennwand)
  - Die Nachbarn Z1 und Z2 haben wechselnde Umlaufzahlen, wie die Atmungsleiter.
  - Z1 bei g = 0,1: 0,7108615 (-1). Das passt zur Kurve 0,710691 + 0,017 g^2, die bei g -> 0 in die Nullstelle der
    goldenen Regel (0,71073) laeuft.
- **Abbildung auf beta_eff bestaetigt (g = 0,2):**
  - Gemischter Ball (eigener Code, direkt geschossen) und Ein-Feld-Modell mit beta_eff = 0,45351 (unveraendertes bic2)
    ergeben beide omega*^2 = 0,7590814 und rho* = 1,7120741, auf 1e-8 gleich, jeweils Umlauf -1.
  - Die Verschiebung gegen den einkomponentigen Ball (0,797677) betraegt -0,0386.
- Belegstufe: numerisch mit Kontrolle (Umlaufzahl, zwei Codes), radiales lineares Modell, kein Beweis. Vorab 6 von 6
  getroffen; die Lagefenster waren aus R8 bekannt und deshalb eng, die eigentlichen Pruefungen waren Umlauf und
  Code-Vergleich.

### FORMEL-1: Rechnung mit der Leiterformel, blinde Vorhersage n = 11 (Leitung, 2026-09-30 07:57:22 CEST, vor dem Lauf)

- Finn fragte, ob wir eine Formel haben, mit der wir etwas berechnen koennen (Nachricht vor 2026-09-30 07:57:22 CEST).
- Formel (Leitung, empirisch aus n = 1 bis 9): 1/(omega*^2_n - omega_min^2) = 1/(omega*^2_9 - 0,5) + 2,29 (n - 9),
  mit omega_min^2 = 1 - 1/(4 beta) = 0,5 fuer beta = 0,5 und 1/(0,5470 - 0,5) = 21,28.
- Vorhersage n = 11: 21,28 + 2 * 2,29 = 25,86, also **omega*^2_11 = 0,53867 +- 0,0003**.
  - Unsicherheit: Schritt +-0,03 und Lage n = 9 +-0,0003.
  - n = 10 (0,5424) ist nicht blind, weil der Gamma-Einbruch bei 0,5425 schon gesehen ist.
- Test: pole bei 0,5381, 0,5387 und 0,5393 (l = 0). **Scheitert, wenn** das Breitenminimum ausserhalb 0,5384 bis 0,5390
  liegt oder keiner der drei Punkte unter 1e-4 faellt.
- **Ausgang (eingetragen 2026-09-30 08:15:10 CEST): getroffen.**
  - Lauf: zuerst Spur cpu (wartete hinter ROT-2), um 08:07:33 auf cpu2 neu gestartet; 251 s, rc = 0.
  - Schmale Atmungsresonanz |Im rho|:
    - 0,5381: 9,82e-4 (Re rho 1,56508)
    - 0,5387: **3,69e-5** (Re rho 1,56885)
    - 0,5393: 1,77e-3 (Re rho 1,57223)
  - Das Minimum liegt am mittleren Punkt, und dieser Punkt liegt unter 1e-4.
  - Lage aus der signierten Wurzel (Hand), mit der einzigen Vorzeichenwahl, die gleiche Steigungen gibt (-61 und -60):
    **omega*^2_11 ~ 0,53860**. Vorhergesagt 0,53867 +- 0,0003, Abstand -7e-5.
  - Ohne Umlauftest; in der Duennwand vermischt das Kurvenverfahren die Aeste, wie bei n = 7 bis 9. Belegstufe: Breitenminimum,
    numerisch, blind vorhergesagt.

### FORMEL-2: blinde Vorhersage n = 12 und n = 13 (Leitung, 2026-09-30 08:26:04 CEST, vor den Laeufen)

- Anlass: Finn, "weiter rechnen und ergebnisse melden" (Nachricht vor 08:25:04).
- Formel wie FORMEL-1, fortgeschrieben mit den Daten bis n = 11. u = 1/(omega*^2 - 0,5):
  - n = 9: 21,277 (0,5470)
  - n = 10: 23,585 (0,5424, nicht verfeinert)
  - n = 11: 25,907 (0,53860 +- 0,0001)
  - Schritte 2,308 und 2,322; angesetzt 2,31 +- 0,02.
- **Vorhersage** (Hand):
  - **n = 12:** u = 28,217 +- 0,07, also **omega*^2 = 0,53544 +- 0,00012**
  - **n = 13:** u = 30,527 +- 0,08, also **omega*^2 = 0,53276 +- 0,00012**
- Test:
  - pole (l = 0, h = 0,02, bereich resonanz) bei 0,53529 / 0,53544 / 0,53559 und bei 0,53261 / 0,53276 / 0,53291
  - Spur cpu5: Der Beweis rechnet dort nicht mehr, der frische Leser rechnet nicht.
- **Scheitert, wenn** je Stelle:
  - kein Rasterpunkt |Im rho| < 1e-4 hat, oder
  - die Lage aus der signierten Wurzel ausserhalb der Vorhersage +- 0,00012 liegt. Die Wurzel wird wie bei FORMEL-1 mit
    der Vorzeichenwahl bestimmt, die gleiche Steigungen gibt.
  - Ein Randpunkt als tiefster Punkt ist noch kein Scheitern, massgeblich ist die Wurzel-Lage.
- **Ausgang n = 12 (eingetragen 2026-09-30 08:32:50 CEST): getroffen.**
  - Lauf: cpu5, 08:26:24 bis 08:32:06, rc = 0.
  - |Im rho| der schmalen Atmungsresonanz:
    - 0,53529: 1,311e-4 (Re rho 1,56367)
    - 0,53544: **3,90e-7** (Re rho 1,56478)
    - 0,53559: 1,017e-4 (Re rho 1,56589)
  - Signierte Wurzel (Hand): Die Wahl "Mitte positiv" gibt die Steigungen -72,2 und -71,4, die Gegenwahl -80,5 und -63,1.
    Also **omega*^2_12 ~ 0,535449**, vorhergesagt 0,53544 +- 0,00012, Abstand +9e-6.
  - Ohne Umlauftest; Belegstufe Breitenminimum.

### MOD-2 und FORMEL-3: zwei Vorhersagen fuer n = 13 bis 15 (eingetragen 2026-09-30 08:34:29 CEST, vor den Laeufen n = 14 und 15; n = 13 laeuft seit 08:32:06, noch ohne Ergebnisdatei)

- **MOD-2** (Duennwandmodell, VORHERSAGEN-MOD2.md, fertig 08:33:26, eingefroren 08:33:57):
  - n = 10: 0,542382 +- 2e-5
  - n = 11: 0,538619 +- 2,5e-5
  - n = 12: 0,535468 +- 3e-5
  - n = 13: 0,532792 +- 3,5e-5
  - n = 14: 0,530490 +- 4e-5
  - n = 15: 0,528489 +- 5e-5
  - Umlaufzahlen abwechselnd; Grundlage nur n = 5, 7, 8, 9 aus MODELL-DUENNWAND.md.
  - Blindheit: Laut Bericht hat der Agent RUNDE-09.md und die Laufordner nicht geoeffnet (drei Werkzeugaufrufe).
- **Vergleich der Leitung mit schon Gemessenem** (fuer MOD-2 blind):
  - n = 11: gemessen ~0,53860 (+-3e-5) gegen 0,538619 +- 2,5e-5, Abstand -2e-5, vereinbar
  - n = 12: gemessen 0,535449 gegen 0,535468 +- 3e-5, Abstand -1,9e-5, getroffen (0,6 Balken)
  - Beide Abstaende sind negativ, wie bei SP-1.
- **FORMEL-3** (Leitung, Leiterformel neu an n = 12 verankert: u_12 = 1/0,035449 = 28,2095, Schritt 2,31 +- 0,02):
  - **n = 14: 0,530460 +- 0,00004**
  - **n = 15: 0,528458 +- 0,00005**
  - MOD-2 liegt je 3e-5 hoeher. Beide Vorhersagen ueberlappen, eine Messung auf ~5e-6 kann sie trennen.
- **Test:**
  - pole l = 0 bei n = 14: 0,53042 / 0,53047 / 0,53052
  - bei n = 15: 0,52842 / 0,52847 / 0,52852
  - Spur cpu5, je Stelle zwei Aufrufe (2 + 1 Punkte), wegen der 10-min-Grenze.
- **Scheiterregeln:**
  - Kein Punkt |Im rho| < 1e-4: nicht entscheidbar.
  - Die Lage aus der signierten Wurzel (Vorzeichenwahl mit gleichen Steigungen) liegt ausserhalb von:
    - FORMEL-3: Vorhersage +- Balken
    - MOD-2: Vorhersage +- 3 Balken (seine eigene Regel)
- **Ausgang n = 13 bis 15** (Laeufe 08:32:06 bis 08:50:54, alle rc = 0; eingetragen 2026-09-30 09:52:49 CEST, nach der
  Pause wegen des Nutzungslimits):

  | n | Raster: \|Im rho\| | Lage (signierte Wurzel, Hand) | Formel (FORMEL-2/3) | MOD-2 |
  |---|---|---|---|---|
  | 13 | 0,53261: 1,80e-4; 0,53276: **9,0e-7**; 0,53291: 1,30e-4 | **0,532772** (Steigungen -83,2 / -82,2) | 0,53276 +- 0,00012: +1,2e-5, getroffen | 0,532792 +- 3,5e-5: -2,0e-5, getroffen |
  | 14 | 0,53042: 2,18e-5; 0,53047: **5,5e-10** (Im mit Vorzeichen + auf Rauschhoehe); 0,53052: 2,23e-5 | **0,530470** | 0,530460 +- 4e-5: +1,0e-5, getroffen | 0,530490 +- 4e-5: -2,0e-5, getroffen |
  | 15 | 0,52842: 2,75e-5; 0,52847: **2,8e-9**; 0,52852: 2,87e-5 | **0,528470** | 0,528458 +- 5e-5: +1,2e-5, getroffen | 0,528489 +- 5e-5: -1,9e-5, getroffen |

  - **Beide Vorhersagen bestehen n = 11 bis 15.**
    - Die Formel liegt stets etwa 1e-5 zu tief.
      - **Berichtigung 2026-09-30 10:23:30 CEST** (Hinweis Codex, PAPER-LEITER-EINARBEITUNG.txt): "stets" gilt nur fuer
        FORMEL-2/3 (n = 12 bis 15). Die urspruengliche n = 11-Vorhersage (FORMEL-1, 0,53867) lag 7e-5 zu hoch.
      - Ausserdem wurden FORMEL-2/3 schrittweise nach neuen Ergebnissen fortgeschrieben (Anker n = 11, dann n = 12). Das
        ist kein einziger unveraendert eingefrorener Fuenf-Punkte-Test.
      - Formel und MOD-2 pruefen dieselben Zielrechnungen; es sind keine zwei unabhaengigen Replikationen.
    - MOD-2 liegt stets etwa 2e-5 zu hoch: -2,0 / -1,9 / -2,0 / -2,0 / -1,9 e-5 bei n = 11 bis 15. Das ist ein
      konstanter Versatz, vermutlich in der Wandphase theta, keine falsche Periode.
  - Schritte in u = 1/(omega*^2 - 0,5): 2,3043 / 2,3054 / 2,3055 (n = 12 -> 13 -> 14 -> 15). Der Grenzschritt liegt
    gemessen bei ~2,305; MOD-2 hatte 2,298 angegeben.
  - Belegstufe: Breitenminima (bis 3e-9), blind vorhergesagt, ohne Umlauftest.
  - **Berichtigung 2026-09-30 11:00:57 CEST** (Datenpaket DATEN-LEITER, RUNDE-09/daten-leiter/DATENPAKET.md, Abschnitt 8;
    Zahlen aus den Dateien statt aus diesem Protokoll):
    - Die Schritte in u fuer n = 12 bis 15 sind 2,3045 / 2,3052 / 2,3059. Oben stehen die aus gerundeten Lagen gerechneten
      Werte.
    - Die MOD-2-Abweichung bei n = 11 betraegt -1,6e-5, nicht -2,0e-5.
    - Die Steigungen der signierten Wurzel bei n = 11 sind -62,3 und -60,0, nicht "-61 und -60".
    - Aus frueheren Runden: beta 0,55, n = 3 steht in der Datei als 0,674766 (Protokoll 0,674782); beta 0,60, n = 1 als
      0,855445 (Protokoll 0,855443).
    - Bei MOD-2 n = 13 (und bei V1, VC1 aus Runde 8) startete der Lauf vor dem Einfrieren der Vorhersage. Die Ergebnisdatei
      entstand erst danach; im Sinn "vorab heisst vor der Ergebnisdatei" gilt das Ergebnis also noch als vorab.

### BEWEIS-1: Code-Lesung (frischer Leser Fable, 07:14:03 bis 08:03:32; RUNDE-07/beweis/LESUNG-CODE.md; eingetragen 2026-09-30 08:04:32 CEST)

- **Urteil: BEWEIS TRAEGT MIT AUFLAGEN.**
  - Code gegen Lemmata P, J, T, T0, E, Pos, Jets und Krawczyk: Term fuer Term gehalten, stimmt.
  - Rundung sauber: kein float64 und kein mid() in der strengen Kette.
  - Alle 26 Hashes stimmen.
- **Auflagen:**
  - W1: "erster Schritt R0 = 1, h0 = 1/2" ist falsch, tatsaechlich R = 13/64, h0 = 13/128. Doku-Fehler ohne Folge fuer die
    Gueltigkeit.
  - Drei Untergrenzen in Tabelle 3.2 sind aufgerundet statt abgerundet.
  - K_J-Schranke steht nur im Log.
  - Dem Zertifikat fehlen Laufparameter und Code-Hash.
  - "nur Radien" in T1 ist nicht belegt.
  - Die Negativkontrolle zeigt Empfindlichkeit, nicht Strenge.
- Offen wie bisher: Softwarevertrauen (flint), kein zweites Programm, keine Lesung aus fremdem Haus.
- Umsetzung: Beweis-Agent fortgesetzt um 08:04 (Nachricht der Leitung). Danach liest ein frischer Leser die letzte Schicht.
- **Einarbeitung fertig** (STAND.md 08:20:32; eingetragen 2026-09-30 08:21:26 CEST): Alle Befunde sind eingearbeitet; die
  Zahlen des Beweises sind unveraendert.
  - Neulaeufe A2 (L = 40) und B2 (L = 44) mit neuem Treiber; der Rechenkern ist unveraendert. jq-Vergleich alt gegen
    neu: alle gemeinsamen Felder gleich, Kasten-Schrittprotokolle bitgleich.
  - Laufparameter und volle Hashes stehen jetzt im Zertifikat.
  - Alle Schranken sind nach aussen gerundet. Der Autor fand zusaetzlich weitere falsch gerundete Schranken, z. B.
    c - eta >= 7,5182518 statt 7,5182519.
  - Die Empfindlichkeitskontrolle (frueher "Negativkontrolle") fiel wie vorab im Code festgelegt aus: delta/4 besteht,
    delta und 4 delta verfehlen.
  - Selbst gemeldeter Regelverstoss: ein wirkungsloser awk-Aufruf auf /dev/null zwischen 08:15:49 und 08:17:12.
  - Frischer Leser (Fable) fuer die letzte Schicht seit 08:21 (LESUNG-LETZTE-SCHICHT.md).

### SP-1: stille Stellen fuer l = 1 und l = 2 gegen die eingefrorenen Vorhersagen (Agent bis Bericht vor 08:09:33; RUNDE-08/sp1/ERGEBNIS.md; Vergleich der Leitung 2026-09-30 08:09:33 CEST)

- **Grundlage:**
  - Vorhersagedatei VORHERSAGEN-SP1.md, eingefroren 06:43:17; der Hash der Arbeitsdatei ist heute noch gleich.
  - Der SP-1-Agent hat die Datei nicht geoeffnet.
  - Alle Stellen "exakt" (Umlaufzahl +-1, aufgeloest), linear, beta = 0,5.

| Ziel | Vorhersage omega*^2 | gemessen | Abstand | Umlauf vorhergesagt / gemessen | Re rho vorhergesagt / gemessen | Ausgang |
|---|---|---|---|---|---|---|
| l = 1, n = 2 | 0,6620 +- 0,0023 | 0,660280 | -0,0017 | +1 / +1 | 1,7196 +- 0,005 / 1,717301 | getroffen |
| l = 1, n = 3 | 0,6178 +- 0,0013 | 0,617105 | -0,0007 | -1 / -1 | 1,6656 +- 0,005 / 1,666050 | getroffen |
| l = 2, m = 2 (Kante) | 0,6505 +- 0,005 | 0,643905 | -0,0066 | +1 / +1 | 1,777 +- 0,008 / 1,762082 | Lage verfehlt; nach Regel (c)3 zulaessig ("nahe der Kante darf sie versagen") |
| l = 2, m = 3 | 0,6094 +- 0,003 | 0,606981 | -0,0024 | -1 / -1 | 1,696 +- 0,006 / 1,694040 | getroffen |
| l = 2, m = 4 | 0,5865 +- 0,0015 | 0,585391 | -0,0011 | +1 / +1 | 1,655 +- 0,006 / 1,655298 | getroffen |

- **Widerlegungsregeln (c):** keine ausgeloest.
  - (c)1: Beide l = 1-Stellen liegen zwischen den benachbarten l = 0-Stellen.
  - (c)2: Der Abstand in Psi/pi zwischen n = 2 und n = 3 ist 4,1646 - 3,1632 = 1,0014 (Hand, Formel der Datei mit den
    gemessenen omega*^2 und Re rho), vorhergesagt 1,006 +- 0,03.
  - (c)3: l = 2-Fenster endet bei ~0,675 (vorhergesagt 0,670 +- 0,01); keine halbe Stufe verschoben.
  - (c)4: Re rho weicht hoechstens 0,0149 ab (l = 2, m = 2, am vorhergesagten Ort). Mit dem Modellwert am gemessenen Ort
    (Steigung ~2 je Einheit omega^2 aus der Tabelle) sind es 0,002. In beiden Lesarten liegt der Wert unter 0,015.
  - (c)5: Die Umlaufzahlen wechseln auf beiden Aesten ab.
- **Auffaellig:** Alle gemessenen Lagen liegen tiefer als vorhergesagt (-0,0007 bis -0,0066). Auch der Eichpunkt liegt
  tiefer: 0,7545 statt 0,7556. Die Vorhersage hat also eine kleine systematische Abweichung, am ehesten im Ansatz fuer
  Dtheta_l(R).
- **Belegstufe:** Blinde Vorhersage, 4 von 5 Lagen getroffen; die fuenfte durfte nach der vorab geschriebenen Regel
  versagen. Alle 5 Umlaufzahlen getroffen. Numerisch, linear, kein Beweis.
- **Bedeutung [H]:** Die Phasenregel mit dem Bessel-Versatz -l pi/2 + delta_l gilt auch fuer Schwapp- (l = 1) und
  Verformungsschwingungen (l = 2). Die stillen Stellen bilden je Drehimpuls eine eigene Leiter mit Schritt ~2,3 in
  1/(omega^2 - 0,5).
- Weitere Stellen (SP-1, ohne Vorhersage): l = 1 bei 0,592242 (+1) und 0,576074 (-1); l = 2 bei 0,571 nicht gesehen.

### Codex: Wechselwirkungen mit globaler SU(3) (Peerbus, Ergebnis 07:52:59; resonance-20260930/su3-interactions/; eingetragen 2026-09-30 08:04:32 CEST)

- Reduziertes Modell, keine Ableitung aus der Q-Ball-PDE; zwei komplexe Dreier (Triplets) a, b.
- **Austauschterm J ||a - b||^2:**
  - Tauscht lokale "Farb"-Besetzung aus.
  - Erhaelt alle acht globalen SU(3)-Ladungen und die Gesamtnorm (Drift 6e-13).
  - Ein Dichtevermittler allein (koppelt nur an S = a^dagger a) mischt nicht, er verschiebt nur die Phase.
- **Geometrie:**
  - Ein einzelner Abstandskern zwischen Tetraedern oder Wuerfeln ergibt in 54 Faellen keinen exakten SU(3)-Austausch
    (kleinste Anisotropie 0,297).
  - Erst die Summe ueber sechs Raumrichtungen ist isotrop, als Aggregat; ob die Nachbarn dynamisch phasengleich bleiben,
    ist offen.
- **Grenze (Codex):** Es gibt nur globale SU(3). Lokale Eichsymmetrie, acht dynamische Felder und ein Gauss-Gesetz fehlen;
  "acht Ecken sind keine acht Gluonen".
- Bezug zu KRAFT-1: Eine Farbkraft im eigentlichen Sinn braucht die fehlenden Eichfelder. Das deckt sich mit der Grenze
  in der KRAFT-1-Karte.

### Ernte 2026-09-30 08:18:08 CEST: KOLL-1, MOD-1, ROT-3, SUCH-1, T-1 (eingetragen von der Leitung aus den Agentenberichten)

- **KOLL-1** (RUNDE-09/koll1/ERGEBNIS.md): **Randkopplung bestaetigt, kein Band. Vorschlag des Agenten: parken.**
  - J < 0 faellt wie e^{-kappa_c d}/d.
    - Das volle Ueberlappintegral und die Naeherungsformel stimmen ab d = 10 auf 1 %.
    - J an der stillen Stelle: -5,6e-3 / -1,65e-3 / -5,0e-4 bei d = 10 / 12 / 14.
    - Der offene Kanal traegt an der stillen Stelle < 3e-4 bei.
  - Vorab verfehlt: Die Kopplungszahl K kam auf 10,7 statt 0,5 bis 6.
  - Freie Baelle, nichtlinear, zwei Gitterstufen, Abweichung < 0,3 %:
    - Gegenphasige Baelle fliegen auseinander (d von 10 auf 24,9 bis t = 100); die Drift traf die Vorhersage aus J auf
      1 bis 5 %.
    - Beim Nachbarn kommen nur 8,6 % (still) bzw. 10,9 % (0,76) der Atmung an.
    - Das Paar verliert an der stillen Stelle 8,5 % Atmungsenergie, der Einzelball nichts [H: Verstimmung durch den
      Nachbarn].
  - Festgehaltene Baelle (linear um einen eingefrorenen Hintergrund):
    - Frueh wie berechnet: d = 14, t = 500 ergibt a/b = 0,973/0,230 gegen berechnet 0,969/0,247; Phase -1,62 gegen -pi/2.
    - Danach waechst in jeder eingefrorenen Anordnung eine Stoermode mit Raten 0,002 bis 0,08. Frage (c), die Dreierkette,
      ist deshalb nicht entscheidbar.
  - Gegen ZUS-10 Idee 6 liest der ZUS-10-Pruefer die Zahlen selbst.
  - Selbst gemeldeter Regelverstoss: um 08:14 lokal ein leerer `python3 -`-Aufruf vor sed, ohne Rechnung.
- **MOD-1** (RUNDE-09/MODELL-DUENNWAND.md):
  - Drei Zonen: innen eine offene stehende Welle; in der Wand ein gebundener Zustand des geschlossenen Kanals
    (Rosen-Morse-Topf, genau ein Zustand, geschlossen hergeleitet); aussen die offene Welle.
  - Mit drei Wandkonstanten, angepasst an n = 2, 3, 4 je beta, trifft das Modell alle sieben Stellen n >= 5 auf 4e-5.
    Bei n = 1 verfehlt es um 1e-3 bis 4e-3.
  - Grenzschritt ohne freien Parameter: 2,33 mit nacktem Wandzustand, 2,30 mit gemessener Verschiebung; gemessen ~2,29.
  - Weitere Befunde:
    - Die Kruemmung C waechst wie (n + theta)^4.
    - Keine Stellen in 1D und bei ln(1 + S): Dort fehlt die Innenbarriere.
    - Die zweite Leiter entspricht dem j_1-Formfaktor einer gefuellten Kugel.
  - Einordnung: kein Friedrich-Wintgen-Fall, sondern zwei Wege desselben Wandzustands; Ladungen +-1 im Sinne von Zhen
    u. a. 2014.
  - Grenze: theta und die Niveauverschiebung sind angepasst. Naechster Schritt: das ebene Zweikanal-Wandproblem in 1D.
- **ROT-3** (RUNDE-09/PAPIER-ROT3.md, nur Papier, Websuche am Ende erschoepft):
  - Alle drei Bilder sind als Einzelphaenomene bekannt (kalte Atome, Optik, Supraleiter, Bosonensterne); mit unserem
    cos(2 Delta theta)-Term wurde nichts gefunden.
  - Schreibtisch:
    - Der gefuellte Kern braucht bei g = 0 eine eigene, kleinere Frequenz. Bei g != 0 dreht der Wirbel als starres
      Zwei-Buckel-Muster mit.
    - Die Waende sind Ising-artige pi-Waende. Die Son-Stephanov-Phasenwand ist bei uns ein Sattel.
    - Einen stationaeren reinen Rotor gibt es nicht; in erster Ordnung in g strahlt er nicht unterhalb der Drehrate
      (2/3)(1 - omega).
  - Testvorschlag T1 (2D, g langsam einschalten; Musterdrehzahl, Wandkontrast, n_z/S in der Wandmitte) und T2 (radial,
    Rotorschwelle). Weiter mit ROT-1 abstimmen, das die 2D-Rechnung macht.
- **SUCH-1** (RUNDE-09/SUCHWORTE.md): Fast jedes Thema hat in der Literatur einen Namen.
  - Phasenregel = "nonradiating source" (Schott 1933: Kugelschale mit kR = n pi; Bohm und Weinstein 1948). Die
    Primaerquelle ist nicht geladen [L?].
  - Der 120-Grad-Stern ist der frustrierte, zeitumkehrbrechende Zustand in Mehrband-Supraleitern (Peng, Zhang, Hu 2026,
    arXiv:2605.28221, mit cos(2 Delta theta)).
  - ROT-1 heisst dort Wirbel mit massivem Kern, ROT-2 interner Josephson-Effekt, ROT-3 Son-Stephanov-Wand bzw.
    Wirbel-Dreier (Eto und Nitta, mit Quark-Analogie).
    - **Berichtigung 2026-09-30 11:55:06 CEST** (Y-1-Agent hat Eto und Nitta an der Quelle gelesen): Im Text von Eto und
      Nitta (PRA 85, 053645) steht keine Quark-Analogie und kein Vergleich Y gegen Dreieck. "mit Quark-Analogie" war eine
      Zuschreibung aus dem Suchtreffer.
  - Beweis-Nachbar: Yu und Lu 2025, arXiv:2504.19573, streng. Muss in jede Mitteilung zum Beweis.
  - Warnung fuer MESS-1: In 1D ist die Troepfchen-Atmung gebunden, in 3D nur dickwandig im Kontinuum. Hoehere Obertoene
    sind die besseren Kandidaten.
  - Nicht gefunden: eine Leiter stiller Atmungsstellen bei Q-Baellen oder Troepfchen und ein Rechnerbeweis dafuer.
- **IE Gen 1, T-1** (Bericht 08:14:23): Karten G1-02, G1-07 und G1-05 (Teil a) laufbereit; G1-04 und G1-06 geparkt, mit
  Bauhinweisen.
  - G1-02 und G1-07 rechnen seit 08:06:42 auf der .69 (Ketten in runde9-ie/).
  - Offen fuer die Leitung: G1-04 "Saat 21 in beiden Komponenten" (geparkt, Entscheidung erst beim Bau). Bei G1-05 ist
    der Rechenweg geaendert (Schiessen von innen), die Vorhersage nicht.
- Codex: Nachtrag zum Paper-Material und Bitte um die nichtlineare Lebensdauer der drehenden l = 1-Mode, gesendet
  um 08:17 (Peerbus-Ergebnis).

### Codex: linearer Feldmechanismus fuer drei gleiche Kanaele, dazu "68 %" (Peerbus 08:16:16 und 08:23:29; resonance-20260930/field-mechanism/, shell-detuning/; eingetragen 2026-09-30 08:26:28 CEST)

- **Aufbau:** Ein skalares KG-Feld in zwei konzentrischen radialen Mulden (die Schalen sind extern vorgegeben, keine
  Q-Ball-Loesung).
- **Ergebnis:** Die drei l = 1-Dipolmoden koppeln exakt gleich. Die Gleichheit folgt aus der Winkelorthogonalitaet,
  J aus der radialen Eigenrechnung; es sind keine drei Ports vorgegeben.
  - |J| = 0,0637 / 0,0172 / 0,0047 bei d = 2 / 3 / 4.
  - Neun Gitterfaelle sowie anisotrope und quartische Gegenarme bestanden.
- **Brechung:** Eine lokale Quartik der komplexen l = 1-Amplituden bricht U(3); das Verhaeltnis Achse zu Kreis ist 1,5.
  - In der Gesamtformel mit N = 3 und g = 0 ist die innere U(3) schon vorausgesetzt; g != 0 bricht sie.
- **"68 %"** ist die Zwei-Oszillator-Formel P_max = 4J^2/(delta^2 + 4J^2). Wird die aeussere Mulde um 1,56 % abgesenkt,
  ist die Verstimmung weg und P_max = 1; im Feld liegen dann 99,6 % der Energie aussen (rekonstruierte KG-Energie). Das
  ist keine neue Physik, sondern die Kontrolle des Modells.
- **Codex' naechste Frage:** Erzeugt die echte Q-Ball-Loesung selbst zwei passende positive Dipolzweige? Dazu zuerst die
  Translationsnullmode abtrennen, dann das gekoppelte l = 1-Spektrum und die nichtlinearen Koeffizienten bestimmen.
- **Bezug zu Finns Frage (Tetraeder und Leuchtturm):** Das stuetzt den Chat-Punkt "drei Schwapprichtungen = linear ein
  Tripel" [H]; die Nichtlinearitaet bricht es.

### Pause wegen Nutzungslimit, Codex-Arbeit waehrenddessen, Review der Leitung (eingetragen 2026-09-30 09:57:06 CEST)

- **Pause der Leitung** zwischen den Messungen 08:34:56 und 09:51:45.
  - Vorher angehalten: acht Agenten (KRAFT-1, ROT-1, ROT-2/GF-BIC, MESS-1, ZUS-10-Pruefer, SD-1, Leser der letzten
    Beweisschicht, Paper-Agent), der Laufwaechter und die Schleife.
  - Die .69-Laeufe liefen weiter.
  - Finn nach der Pause: "wir haben codex weiter machen lassen", dann "review das was codex gemacht hat, den aktuellen
    stand, und gib ihm ggf input".
- **Codex waehrend der Pause** (Sitzungen ag-phy-coordination = frueher codex-haupt, ag-phy-lat = Paper englisch,
  ag-phy-min = Laufnachbereitung, ag-phy-tus = Konzeptpruefung):
  - **Paper:**
    - Deutsche Fassung v0.5 (08:36).
    - Englische Fassung als HTML und LaTeX (model-lab/papers/su3-geometric-triplets-20260930-en-codex/, 10 Seiten,
      fertig 09:35:50), mit eigener Quellentreuepruefung (kein Blocker) und QA.
    - Seite 1 von der Leitung angesehen: klar abgegrenzt.
  - **l = 1-Harmonische** (resonance-20260930/l1-harmonic-selection/ABLEITUNG.txt):
    - Die drehende m = 1-Mode erzeugt bei zweiter Ordnung nur L = 2, M = +-2 (dazu statisch L = 0, 2).
    - Beide Laborfrequenzen (4,521 und -2,784) sind offen, also bedingt P ~ C eps^4; die drehende Mode ist nicht
      geschuetzt. C ist nicht gerechnet.
    - Von der Leitung von Hand geprueft: Faktor sqrt(3/(10 pi)), Zerlegung von |Y11|^2 und Frequenzen stimmen.
  - **Lauf-Audit** (status-audit-20260930/codex-wm1/VIER-BEFUNDE-PRAEZISE.txt):
    - ZUS-10 Kette A2 Teil b ungueltig: seq-Locale erzeugte Dezimalkommas in --dims.
    - ZUS-10 Idee 7 technisch nicht getestet: CUDA-Sync im CPU-Rauchtest.
    - ROT-1: Laeufe fertig, Bericht fehlte.
    - KRAFT-1: Laeufe fertig, Bericht fehlte.
  - **KRAFT-1-Konzeptpruefung** (KRAFT-KONZEPTPRUEFUNG.txt):
    - K2 bei 0,76: begrenzt positiv, eine Gitterstufe.
    - still: Das strenge Schalterkriterium ist verfehlt, die grobe Widerlegungsgrenze nicht erreicht.
    - K3: Nullkontrollen bestanden, die Yukawa-Rate ist nicht bestaetigt.
    - K1-3D ist nicht ausgewertet, TET-1 fehlt.
  - **Neuheitsaudit** (novelty-audit/NEUHEITSMATRIX.txt):
    - Die BIC-Linie ist ein eigener Strang, getrennt vom SU(3)-Paper.
    - Die gekoppelten 3+1D-Streugleichungen sind bekannt (Azatov/Ho/Khalil 2412.13885, dieselben linearen
      Koeffizienten). Unsere eingestellte Null zeigen sie nicht.
    - Punkt 5 dort ("kein zertifizierter Kontinuumsgrad") betrifft Codex' eigenes Zertifikat. BEWEIS-1 ist im Audit
      nicht beruecksichtigt; die Leitung hat das gemeldet.
  - **Weiteres:** Quellenpruefung des Papers, Konzeptkontrollen, Quantengeometrie-Audit (Gambini-Pullin u. a.) und
    Paperfokus "zurueck zu funktionierenden Ansaetzen".
- **Review und Input der Leitung an Codex** (Peerbus-Ergebnis an ag-phy-coordination, gesendet nach 09:52:49):
  - l = 1-Ableitung bestaetigt; den erzwungenen L = 2-Test rechnet Codex; Zusatzfrage zu den l = 2-Stellen.
  - Stand der BIC-Linie: BEWEIS-1, 15 Stellen, Blindtests n = 11 bis 15, SP-1. Vorschlag eines zweiten Papers zur
    BIC-Leiter; wer fuehrt, entscheidet Codex bzw. Finn.
  - Lauf-Audit angenommen.
  - Das Paper-Review macht der Anthropic-Paper-Agent (nur Review).
  - .69-Werkzeugkopie 699 MB (Platte 88 %).
- **Fortsetzung:**
  - Die acht Agenten sind mit den Audit-Befunden fortgesetzt.
    - Paper-Agent: nur Review von v0.5 und der englischen LaTeX-Fassung.
    - KRAFT-1: nur die Luecken (K1-3D, TET-1, Bericht), die Codex-Bewertung von K2 und K3 wird uebernommen.
  - Finn fragte, ob Codex die Agenten nicht schon fertig gemacht habe. Antwort: nur teilweise (Audit, KRAFT-Teil,
    Englisch/LaTeX). Offen waren die ROT-1-Auswertung, TET-1, K1-3D, die ZUS-10-Ideen, SD-1, MESS-1, ROT-2 und die
    letzte Beweislesung.
- **IE Gen 1:** Alle sechs Ketten sind fertig, alle rc = 0. Ausgaben nach G1-xx/lauf-69-kopie/ kopiert (ohne Zeitreihen).
  Der blinde Ernte-Agent (Fable) ist seit 09:56 gestartet.

### BEWEIS-1 letzte Schicht und MESS-1 (eingetragen 2026-09-30 09:57:06 CEST aus den Berichten, nach 09:56:58)

- **BEWEIS-1, frische Lesung der letzten Schicht** (Fable, RUNDE-07/beweis/LESUNG-LETZTE-SCHICHT.md, 08:21:54 bis
  09:56:58 mit Pause): **"Letzte Schicht traegt"**, keine Auflagen.
  - Alle Befunde der Code-Lesung sind eingearbeitet.
  - Alle Zahlen stimmen gegen A2/B2 in beide Richtungen, jede Schranke richtig gerundet; 38 von 38 Hashes OK.
  - Rechenkern unveraendert; der Treiber aendert keine Mathematik.
  - Die Laufzeit-Hashes im neuen Zertifikat binden den Lauf an den vorliegenden Code.
  - Sechs kleine Befunde (L1 bis L6, nur Wortlaut und Protokoll). Der Autor arbeitet sie ein; danach folgt eine kurze
    Lesung der geaenderten Zeilen.
  - **Status BEWEIS-1:** bewiesen (rechnergestuetzt, linear, l = 0), mit Code-Lesung und Lesung der letzten Schicht im
    Haus Anthropic.
    - Offen: Codex als fremdes Haus, zweites Programm, Eindeutigkeit, l > 0, nichtlinear.
    - Nachbar: Yu und Lu 2025.
- **MESS-1** (RUNDE-09/mess1/ERGEBNIS.md): **Im Troepfchenmodell gibt es keine stillen Stellen.**
  - Petrov-EGPE, symmetrische Mischung, 3D; gerechnet fuer N~ = 20 bis 7535: Grundatmung, Obertoene n_r = 1 bis 5 und
    l = 2 (Oberflaechenmode).
  - Der Code findet zur Kontrolle die Q-Ball-Stelle mit Umlauf +1.
  - Grund: Das Troepfchen hat keinen Wandtopf fuer den geschlossenen Kanal. Das deckt sich mit dem Drei-Zonen-Modell
    (MOD-1), und MESS-1 hatte es vorab vorhergesagt.
  - Literatur-Kontrollen: N~_c = 18,65; E = 0 bei 22,56 (Petrov 22,55); Atmungsschwelle ~953 (Ferioli 934); l = 2 bei
    93,6 (94,2).
  - Messbezug: Heutige 39K-Troepfchen liegen im Bereich ohne Pol (vgl. Semeghini 2018); keine Vorhersage fuer bestehende
    Experimente.
  - Pruefliste fuer eine Laborbruecke: genau ein offener Kanal plus ein am Rand gebundener Zustand eines geschlossenen
    Kanals. Kandidat [H]: Schalen- oder Drei-Komponenten-Troepfchen.
  - Vorschlag des Agenten: parken. Zwei kleine Regelabweichungen stehen in seinem Fehlerkasten.
- **BEWEIS-1, Abschluss im Haus Anthropic** (eingetragen 2026-09-30 10:03:36 CEST):
  - Der Autor hat L1 bis L6 eingearbeitet (09:58:03 bis 10:01:00), ohne Code, Zahlen oder Zertifikat zu aendern.
  - Nachlesung der geaenderten Zeilen (10:01:35 bis 10:03:16): **Urteil unveraendert, die letzte Schicht traegt ohne
    Auflagen.**
    - |f| <= 0,093 bzw. 0,085 und thr >= 0,33208949 sind per jq mit Huellenradius geprueft und richtig gerundet.
    - 38 von 38 Hashes OK.
    - Zwei Randnotizen betreffen nur STAND.md (Mittelpunkte ohne Radius, zwei Eintraege vertauscht) und sind nicht
      tragend.
  - Offen bleiben nur Codex als fremdes Haus, ein zweites Programm, die Eindeutigkeit, l > 0 und der nichtlineare Fall.
- **ROT-2 innerer Rotor** (GF-BIC-Agent, RUNDE-08/gf-bic/ERGEBNIS.md, ROT.0 bis ROT.6; Bericht nach 10:03:27;
  eingetragen von der Leitung):
  - **Kein innerer Rotor, keine Schwelle** (am gemischten Ball M1, numerisch mit Kontrolle):
    - Die relative Phase pendelt bei allen Kicks bis Omega0 = 1,3 und bei jedem Ladungsungleichgewicht bis z0 = 0,99.
    - Grund (Hand): Es bleibt ein reiner Paar-Josephson-Kontakt H = -K(1 - z^2) cos 2 phi ohne laufende Bahnen.
    - Nur an der Separatrix (Omega0 = 1,7) dreht die Phase etwa viermal, dabei gehen 4 % Ladung verloren; danach pendelt
      sie. Das dauert etwa 250 bis 500 Zeiteinheiten.
    - Zwei Gitter auf <= 0,3 % gleich.
  - **ROT-3-Test T2 scheitert an M1:** Die Verlustrate waechst glatt wie Omega0^3, ohne Sprung.
  - **Selbststabilisierung teilweise [Befund, nicht vorab]:**
    - Die Pendelfrequenz nu sinkt mit der Amplitude, und die Harmonischen n nu schliessen nacheinander, sobald
      n nu < 1 - omega.
    - Beim Schliessen der 3. Harmonischen faellt die Abstrahlung auf ein Siebtel. Die Vorab-Erwartung VF9 (Abfall schon
      bei der 2.) ist widerlegt.
  - **Stille Stellen im Gegentakt: ja** (g = 0,05):
    - omega^2 = 0,702252 (Umlauf -1) und 0,635507 (+1).
    - Der direkte Kanal ist dort 15- bis 23-mal schwaecher als 0,012 daneben; der Gesamtfluss bleibt gleich, weil die
      Kombinationskanaele offen sind.
    - VF10 bei Kick 0,3 widerlegt.
  - Vorab gegen Ausgang: 7 getroffen, 4 teilweise, 2 widerlegt.
  - Selbst gemeldete Regelverstoesse: einmal leeres `python3 -`; zwei geschaetzte Zeiten in PLAN.md, vor dem Lauf
    berichtigt.
- **ROT-1 Wirbel mit gefuelltem Kern, 2D** (RUNDE-09/rot1/ERGEBNIS.md; Bericht nach der Pause; eingetragen von der
  Leitung). Vorab gegen Ausgang: 14 getroffen, 3 teilweise, 8 nicht.
  - **g = 0:** Der gefuellte Wirbel haelt besser als der einfache.
    - Er existiert an 12 von 12 Punkten und liegt energetisch 2,5 bis 11 Einheiten tiefer als ein Wirbel plus ein
      getrennter Ball.
    - Q = 139: Der einfache Wirbel zerbricht bei t = 1085, der gefuellte bis t = 1500 nicht (nur grob gerechnet).
    - Die Wachstumsrate der Stoerung faellt mit der Fuellung von 0,063 auf 0,027.
    - Kontrolle: Die Zerfallszeiten aus Runde 7 werden zweimal genau wieder erreicht.
  - **g = 0,2 und 0,5:**
    - Die zwei Waende entstehen wie in ROT-3 vorhergesagt: Ising-Typ, Rest der schwaecheren Komponente 2 %.
    - Die Drehung des Musters kommt zum Stillstand, weil sich die Ladung ausgleicht, bis beide Komponenten gleich
      schnell schwingen.
    - Danach zerschneiden die Waende den Ball (g = 0,5, t = 75), oder der Wirbel wird hinausgedrueckt (g = 0,2, t = 65).
    - Ein dauerhaft mitdrehendes Muster (ROT-3 T1) ist nicht gesehen; kleines g (0,02 / 0,05) ist nicht gerechnet.
  - **Band zwischen zwei Wirbeln in verschiedenen Komponenten [Einschluss-Analogon, kein QCD]:**
    - Festgehalten waechst die Energie linear mit dem Abstand: Steigung 0,97 (g = 0,5) bzw. 0,61 (g = 0,2).
    - Frei kreist das Paar mit konstanter Kraft 1,48 bis 1,77 (+-10 %) bei d = 2,6 bis 7,4. Die Schreibtischabschaetzung
      fuer zwei Waende war 1,75.
    - Nur ein Gitter.
    - Deutung als "Linse" (frei) gegen "leerer Schlitz" (festgehalten): aus den Bildern, erst nach dem Ergebnis [H].
  - Kontrollen:
    - g gegen -g nach 90-Grad-Drehung auf 1e-11 gleich.
    - grob gegen fein nur im Feinfenster.
    - Die Bilanzen sind bis 1 % Abfluss < 1e-3, ueber den ganzen Lauf bis 5e-3 (derselbe Randmessfehler wie in R7).
  - Vorschlag des Agenten:
    - gefuellten Kern parken
    - das Band weiter untersuchen: feines Gitter, g gegen -g, groesserer Ball, reisst das Band bei grossem Abstand?
  - Selbstanzeige: gegen 08:11 ein leerer `python3`-Aufruf ohne Rechnung.
- **KRAFT-1 Analogkraefte und TET-1** (RUNDE-09/kraft1/ERGEBNIS.md; K2 und K3 bewertet von Codex ag-phy-min, die Luecken
  vom Agenten; eingetragen von der Leitung):
  - **K1, Randkraft: getroffen.**
    - Formel E_int = -8 pi A^2 cos(Delta theta) e^{-k0 d}/d (3D) bzw. -4 k0 A1^2 cos(Delta theta) e^{-k0 d} (1D).
    - Getestet ueber das Auseinanderfliegen gegenphasiger Baelle: 3D 0,960 / 0,975 des Formelwerts (0,76 / still, beide
      Gitter); 1D 0,996 / 0,991 / 0,921 bei d0 = 12 / 14 / 16.
    - Der R3-Faktor 0,52 ist damit ausgeschlossen, Ursache ungeprueft.
    - Das 3D-Fenster ist nachtraeglich aus der 1D-Regel uebertragen (vermerkt).
    - Bei 60 bis 120 Grad fliesst Ladung; das cos-Gesetz gilt dann nur anfangs.
    - Literatur: Bowcock, Foster, Sutcliffe 2009 (Abstract gelesen).
  - **K2, Bjerknes-Typ:**
    - Bei 0,76 getroffen (Codex-Bewertung; die zweite Gitterstufe ist nachgeholt und besteht: 0,83 bis 1,02, Phase 0,50).
    - **Kraftschalter an der stillen Stelle:** Der Rest ist <= 2,0 % (fein) bzw. 1,6 % (grob) des 0,76-Signals, aber
      nicht gitterstabil. Das strenge Kriterium ist verfehlt (je 2 von 4 Punkten), die 10-%-Widerlegungsgrenze nicht
      erreicht. Also stark gedaempft, nicht nachweislich null.
    - Geprueft ist nur das Fernfeld.
  - **K3, Kondensat: teilweise.**
    - Ruhende Dellen ziehen sich kurzreichweitig an (Codex: Nullkontrollen bestanden, 15 von 15 Mittelwerten
      anziehend, eine konstante Kraft widerlegt).
    - Die vorhergesagte Yukawa-Abklingrate ist nicht bestaetigt. Literatur: Naidon 2018.
  - **TET-1: Kriterien der Leitung bestanden.**
    - Beim 120-Grad-Dreieck heben sich die 1. und 2. Harmonische bis 1e-14 auf.
    - Die cos-3-phi-Amplitude faellt mit 3,13 bis 3,34 k0; die Gegenprobe 0/0/0 faellt mit 1,16 bis 1,31 k0. Die
      neutrale Restkraft reicht also etwa dreimal kuerzer.
    - Die eigenen schaerferen Vorhersagen des Agenten sind teils verfehlt; Dreikoerperterme senken die Amplitude um
      32 bis 43 %.
    - Nur Ueberlagerungsenergie, kein Zeitlauf.
  - Einordnung Dualitaet und akustische Metrik: [L?] bzw. nur Abstracts gelesen.
  - Selbstanzeige:
    - Um 08:35 startete eine falsch verkettete Startzeile nur K3; der Rest ist ab 09:57 nachgeholt.
    - Um 08:24 ein leerer `python3`-Aufruf.

### SD-1 gegen die eingefrorenen Vorhersagen (SD-1-Agent, RUNDE-09/sd1/ERGEBNIS.md; Vergleich der Leitung 2026-09-30 10:15:29 CEST)

- **Messung** (linear, radial, h = 0,02, g = 0,2):
  - Der gegenlaeufige l = 1-Ast im Gegentakt hat **sieben stille Stellen** mit aufgeloestem, abwechselndem Umlauf:
    0,505096 (-1), 0,512706 (+1), 0,522705 (-1), 0,536436 (+1), 0,556504 (-1), 0,588716 (+1), 0,649310 (-1).
  - Schritt in 1/(omega^2 - 0,44875): 2,11 bis 2,16.
  - Existenzschwelle des Asts ~0,6743 +- 0,0005 (g = 0,2) bzw. ~0,742 (g = 0,02).
  - **Spin-Dipol-Gegenprobe bestanden:** Der gleichlaeufige Partner (psi_1 nach vorn, psi_2 nach hinten) ist an 19 von 19
    Punkten gebunden (reell). Belegt ist eine reelle Nullstelle von D; eine Konturzaehlung um sie gab es nicht.
- **Vergleich mit VORHERSAGEN-SD1.md** (eingefroren 08:28:19):

  | Punkt | Vorhersage | Messung | Ausgang |
  |---|---|---|---|
  | Lage m = 6 / 7 / 8 | 0,539 / 0,525 / 0,515, je +-0,004 | 0,536436 / 0,522705 / 0,512706 | getroffen (Abstand -2,3e-3 bis -2,6e-3) |
  | Umlauf | wechselnd | wechselnd | getroffen |
  | Schritt | 1,9 bis 2,2 (Regel: 1,6 bis 2,5) | 2,11 bis 2,16 | getroffen |
  | Re nu* | 1,722 / 1,706 / 1,684, je +-0,01 | 0,086 bis 0,094 tiefer | verfehlt |
  | Existenzschwelle g = 0,2 | 0,540 bis 0,548 | 0,674 | verfehlt, Regel 1a ausgeloest (schmale Pole ueber 0,56) |
  | Gegenprobe g = 0,02 | 0,629 +- 0,01 | 0,742 | verfehlt, der Delta-Ansatz (Innenhub ~1,5 g S) ist widerlegt |
  | Regel 2b | keine Stelle > 0,012 neben einer vorhergesagten | 0,5565 / 0,5887 / 0,6493 liegen weiter weg (oberhalb der vorhergesagten Schwelle) | nach Wortlaut ausgeloest |

- **Urteil der Leitung:**
  - Die Vorhersage ist nach ihren eigenen Scheiterregeln **widerlegt**, und zwar im Teil Existenz und Frequenz (Delta).
  - Der Leiterteil (drei Lagen, Umlaufwechsel, Schritt) ist blind getroffen.
  - Die Phasenregel traegt also auch diesen Ast; das Innenhub-Modell fuer die Schwelle und Re nu ist falsch.
  - Dass der Ast bis 0,674 reicht, ist ein neuer Befund.
- **Bedeutung [H]:** Im Zwei-Sorten-Ball strahlt das eigentliche Gegen-Schwappen (Spin-Dipol) linear nie ab. Sein
  gegenlaeufiger Partner strahlt, hat aber eine Leiter von stillen Stellen.

### ZUS-10: Pruefung der zehn eingefrorenen Ideen (frischer Pruefer Fable; RUNDE-09/zusammenhaenge/pruefung/ERGEBNIS.md, Ende 10:21; eingetragen von der Leitung)

| Idee | Ausgang | Kern |
|---|---|---|
| 1 Zwei Leitern (j1-Formfaktor) | getroffen | n = 6 bis 9 bei 0,57437 / 0,56388 / 0,55598 / 0,54981 (vorab 0,5742 / 0,5637 / 0,5558 / 0,5496, Abstand <= 2,1e-4); Schritt 2,21 (vorab 2,22 +- 0,02); die groben R8-Werte 0,5752 / 0,5656 nicht bestaetigt |
| 2 Gegenlaeufer als Rotor | nicht entscheidbar | Papierteile (a), (d) stimmen; (b), (c) brauchen Code |
| 3 Fuetter-Spitze, Bruecke l = 1 | getroffen | V-Minimum bei d = 2,6 (2,8e-6 gegen 2,4e-4 / 4,1e-4); Endpunkt Re rho = 1,7635199 = 3D-Pol |
| 4 Rayleigh-Tropfen l = 2 | getroffen | Uebertritt bei 0,70 +- 0,01; Wigner-Steigung 4,2 / 3,9 (vorab 5 +- 1,5); kein V-Einbruch; l = 3 tritt bei 0,63 bis 0,66 ueber |
| 5 Lebensdauerstufen | getroffen (Papier und Literatur) | Soffer-Weinstein 1999 (k = 3, t^-1/4), Manton-Merabet 1997 (k = 2, t^-1/2) an der Quelle gelesen; Rechenteil offen |
| 6 Kein Dunkelzustand in 3D | nicht entscheidbar | KOLL-1: Das Paar klingt wie der Einzelball ab (0,163 gegen 0,158 bei t = 500), die Langzeit ist durch Stoermoden unbrauchbar |
| 7 Vernichtungsrest = Oszillon | verfehlt (d = 8) | 0,27 % Energie bei t = 2000, Restfrequenz an der Schwelle. **Neu:** Bei d = 4 entsteht ein langlebiger Ladungstausch-Ball (48 % Energie bei T = 3000, Frequenz 0,80, 127 Ladungswechsel; vgl. Copeland/Saffin/Zhou 2014) |
| 8 Kavitation und Duennwand | gemischt | (c) getroffen (F_b monoton gegen 0,707); (b) verfehlt; (a) je nach Lesart; nichts nachtraeglich gelockert |
| 9 Spinmischung mit Verstimmung | getroffen | lambda(0,05) = 0,0381 (vorab 0,036 +- 10 %); Fenster ~0,087 (vorab 0,081 +- 10 %); delta = 0,10 stabil |

- **Bilanz:** 5 getroffen (1, 3, 4, 5, 9), 1 verfehlt (7, mit neuem Befund), 1 gemischt (8), 3 nicht entscheidbar (2, 6,
  10b).
- Technisch: Der Locale-Fehler (Idee 3 b) und der CUDA-Sync (Idee 7) sind in eigenen Kopien repariert; der ungueltige
  Lauf ist gekennzeichnet.
- Vorschlaege des Pruefers:
  - weiter: 1, 3, 5, 9 und 2 (wenn Code)
  - parken: 4 (bestaetigt), 6, 8, 10
  - verwerfen: 7 fuer d >= 6
  - neue Karte "Ladungstausch-Ball d = 4"

### REGGE-1: kreisende Wirbelpaare am Band (ROT-1-Agent, RUNDE-09/rot1/REGGE-1.md, Vorab eingefroren 10:17:59; eingetragen von der Leitung)

- **Regge ist widerlegt.**
  - J faellt, wenn die Bandenergie steigt: j - j_min = -0,27 (Delta E)^2 bei g = 0,5, Regge verlangt +0,05 bis +0,16.
  - Die Enden laufen mit ~0,33 c (|Omega| d = 0,64 bis 0,75 statt 2).
  - Der Drehsinn ist fest gegen die Windung.
- **In der Form Magnus-artig:**
  - |Omega| d ist konstant (+-10 %) bei d = 2,4 bis 7,0, auch an den neuen Abstaenden 4 und 6.
  - Die Bandkraft daraus ist 1,5 bis 1,7.
  - Omega = Delta E / Delta J stimmt im Vorzeichen (5 von 5), im Betrag 1,3- bis 2,3-mal zu hoch.
- **Nach der Scheiterregel:**
  - Magnus bei g = 0,5 knapp verfehlt: Steigung J gegen d^2 -1,60 +- 0,26, erlaubt -1,49 bis -0,80.
  - Bei g = 0,2 bestanden (-1,04 gegen -1,17).
  - Formaler Ausgang: "etwas anderes". Die Wirbel ruecken um bis zu 22 % zusammen, waehrend J erhalten bleibt [H: Ball
    und Wandlinse nehmen Drehimpuls auf].
- **Energie verunreinigt** durch den unentspannten Start (3,2 je Laengeneinheit gegen die Bandkraft 1,5 bis 1,7).
  Eine saubere Probe braucht einen entspannten Start.
- **Verfahren:**
  - 18 Laeufe, alle rc = 0; die alten Abstaende sind reproduziert.
  - Zwei Laeufe fallen nach der Vorab-Regel heraus (Paar verloren).
  - Vorab gegen Ausgang: 3 getroffen, 1 teilweise, 2 verfehlt.
  - Nur ein Gitter.
  - Die Umlauffrequenzen waren aus ROT-1 schon bekannt; das ist offen vermerkt.
- **Bedeutung:** Das Band hat eine feste Spannung wie ein Farbschlauch. Weil die Enden masselose Wirbel sind (Magnus),
  entsteht aber kein mesonartiges Spektrum. Als Einschluss-Analogon fuer Mesonen traegt es damit nicht weiter.

(weitere Ergebnisse werden eingetragen)

## Abschaetzung

Leitung, 2026-09-30 10:24:52 CEST. Explorativ (v3), keine Messdatenbestaetigung.

| Karte | Entscheidung | Grund |
|---|---|---|
| BEWEIS-1 | weiter | Im Haus Anthropic fertig: Code-Lesung und Lesung der letzten Schicht "traegt", L1 bis L6 eingearbeitet. Offen: Codex als Fremdhaus, zweites Programm. Folgekarte KREIN-1. |
| SP-1 (l = 1, 2) | erledigt | Blind 4 von 5 Lagen, 5 von 5 Umlaeufe. Leitern l = 1 (5 Stellen) und l = 2 (3 Stellen). |
| FA-1 (Farbstern) | parken (bei Codex) | Stern exakt stationaer, kein Grundzustand, kreiselstabil. Die KANDIDAT-Nebenbefunde warten auf eine frische Lesung. |
| EVO-1 Gen 1 | weiter | laeuft, 12 von 17 Modellen fertig |
| BIC-4 (n = 7 bis 9) | erledigt | Breitenminima an den blind fortgesetzten Stellen |
| ABSTAND | erledigt | Kehrwertgesetz (Haeufung ~1/n), kein Primzahl- oder Exponentialgesetz |
| GF-BIC-2 | erledigt | zweite Leiter mit Umlauf; Abbildung auf beta_eff auf 1e-8 |
| ST-2 (Glied 7) | parken | alle Geisterlager mit gleicher Labor-Yukawa |
| Bio 13 (Zufall) | verwerfen | Der Sprung war die Zaehlschwelle, keine Neuron-Schwelle. |
| KOLL-1 | parken | Randkopplung bestaetigt, aber die Baelle fliegen auseinander; kein Band |
| ROT-1 | parken (Kern); Band weiter nur als Reissprobe | gefuellter Kern bei g = 0 stabiler; bei g != 0 zerbricht er; Band mit konstanter Kraft (ein Gitter) |
| REGGE-1 | erledigt | Regge widerlegt; Magnus-artig, nach Regel "etwas anderes" |
| ROT-2 | parken | kein innerer Rotor; teilweise Selbststabilisierung (1/7 beim Schliessen der 3. Harmonischen); stille Stellen im Gegentakt |
| ROT-3 | erledigt | Literatur; Ising-Waende bestaetigt (ROT-1) |
| ZUS-10 | erledigt | 5 getroffen, 1 verfehlt (mit neuem Befund), 1 gemischt, 3 nicht entscheidbar. Folgekarte Ladungstausch-Ball d = 4 |
| MESS-1 | parken | keine stillen Stellen in Troepfchen (kein Wandtopf); Pruefliste fuer die Laborbruecke |
| SUCH-1 | erledigt | Schott 1933 als Kern; Yu und Lu 2025; Leiter bei Q-Baellen nicht gefunden |
| MOD-1 / MOD-2 | erledigt | Drei-Zonen-Modell; blind n = 11 bis 15 getroffen, Versatz ~ -2e-5 |
| FORMEL-1/2/3 | erledigt | n = 11 bis 15 getroffen (fortgeschriebene Vorhersagen, Berichtigung oben) |
| KRAFT-1 + TET-1 | parken | K1 und K2 getroffen, Schalter nicht nachweislich null, K3 teilweise, TET-1 bestanden |
| SD-1 | erledigt | 7 stille Stellen im gegenlaeufigen Ast, Spin-Dipol gebunden; Vorhersage im Teil Existenz/Frequenz widerlegt |
| IE Gen 1 | erledigt; Gen 2 weiter | blind geerntet; E 1 von 6, Z 1 von 3 "weiter" (Regel erst ueber Gen 1 + 2) |
| KREIN-1, SPIN-1 | weiter (laufen) | Krein-Signatur der stillen Moden; Spin-1/2-Wege A (C x S^2) und B (Monopol), Schreibtisch |
| Paper-Leiter (Datenpaket, Duennwand-Abschnitt), SU(3)-v0.6-Nachlesung | weiter (laufen) | Codex fuehrt das zweite Paper; wir liefern Daten und Abschnitte |

- Zaehlung: weiter 8, parken 7, verwerfen 2, erledigt 13 (einige Zeilen fassen Karten zusammen).
- Regelverstoesse dieser Runde, von den Agenten selbst gemeldet: mehrere leere `python3`-Aufrufe ohne Rechnung, ein
  awk auf /dev/null, eine falsch verkettete Startzeile (KRAFT-1).
- Leitung:
  - Geschaetzte Zeiten in Agentennachrichten (z. B. "08:12") statt gemessener Zeiten.
  - Ein Laufwaechter-Kommentar zuerst mit vorab eingetragener Zeit; berichtigt.
  - Pause wegen Nutzungslimit mit acht angehaltenen Agenten.

## Einfach gesagt

Die stillen Stellen unserer Baelle sind jetzt ein Werkzeug: Eine einfache Zaehlformel und ein Modell aus Innenraum, Haut
und Aussenraum haben fuenf neue Stellen blind getroffen, und auch fuers Schwappen und Verformen gibt es solche Stellen.
Der Computerbeweis fuer die erste Stelle ist im eigenen Haus dreimal gegengelesen; jetzt fehlt noch der Blick von Codex.
Zwei Wirbel haengen an einem Band mit fester Spannung wie Quarks, verhalten sich aber nicht wie Mesonen, weil ihre Enden
keine Masse haben. Unsere Baelle koennen sich nur in ganzen Schritten drehen, deshalb sind sie keine Quarks; ob ein Umbau
das aendert, pruefen wir gerade am Schreibtisch. Codex schreibt ein eigenes Paper ueber die ganze Leiter.
