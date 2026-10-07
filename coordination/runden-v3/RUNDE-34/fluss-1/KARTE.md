# FLUSS-1: Erhaltene Einheiten entlang von Tetraederkanten: Coulomb oder Abschirmung? (Runde 34)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 19:10:32 CEST (date), vor jeder Rechnung.
- **Anlass:** Finn ~19:09 "ja mach weiter", ~19:11 "rechne das durch".
  - Finns Fotos (RUNDE-34/tetra-konzept/): Krafteinheiten fliessen entlang der Knicklicht-Kanten eines Tetraeders.
  - WEITERGEDACHT.md, Abschnitte 1, 2 und 5.

## Schreibtisch (vor jeder Rechnung)

- **Modell:** Jede Kante traegt einen Pfeil (eine Einheit fliesst in eine Richtung). Eisregel an jeder Ecke: so viele
  Pfeile rein wie raus. Die Ladung einer Ecke ist q = (rein - raus).
- **Einzeltetraeder (K4):**
  - Jede Ecke hat 3 Kanten, die Regel ist also unerfuellbar; bestenfalls q = +-1.
  - 24 von 64 Zustaenden sind am ausgeglichensten (Eingangsgrade 1, 1, 2, 2; per jq abgezaehlt) und enthalten einen
    Rundlauf. Finns Fotos sind solche Zustaende [M, B].
- **Netz A, Pyrochlor-Kanten** (eckverknuepfte Tetraeder): Jede Ecke hat 6 Kanten, die Regel (3 rein, 3 raus) ist exakt
  erfuellbar.
  - Erwartung: Coulomb-Phase wie im Spin-Eis [L: Henley 2010].
  - Pfeil-Korrelationen fallen dipolar (~1/r^3); zwei Regelverletzungen (q = +2 und -2) ziehen sich entropisch mit ~1/r
    an.
- **Netz B, K4-Kristall** (srs-Netz, Laves-Graph): das unendliche, periodische "Aufrollen" des Tetraedergraphen K4
  [L: Sunada 2008]. Jede Ecke hat 3 Kanten.
  - Die Regel ist wie im Einzeltetraeder ueberall unerfuellbar: Jede Ecke traegt q = +-1, ein dichtes Ladungsgemisch.
  - Erwartung [H]: Abschirmung wie in einem Plasma. Pfeil-Korrelationen fallen schneller als jede Potenz (exponentiell),
    eine Fernwirkung gibt es nicht.
- **Ableitbarkeit:**
  - F1 und F2 sind Literatur-Erwartung, auf diesem Gitter aber nicht als Zahl bekannt (Projekt-grep: nie gerechnet).
  - F3 (K4-Kristall) ist offen; die Abschirmung ist meine Hypothese.

## Test (Code-Agent)

- **Netz A:**
  - Pyrochlor-Gitter, periodisch, L^3 kubische Zellen (16 Ecken je Zelle), Kanten = Tetraederkanten (6 je Tetraeder,
    Grad 6 je Ecke).
  - Abtastung der Eiszustaende mit Schleifenzuegen (gerichtete Schleifen umklappen erhaelt alle Ladungen) bzw. mit einem
    Wurm.
  - **(a) Paarpotential:** zwei Defekte q = +-2 (ein Pfeil zu viel bzw. zu wenig), Wurm mit genau zwei Defekten,
    gleichgewichtet. Abstandshistogramm, F(r) = -ln[P(r)/g(r)], Ausgleich a - C r^(-p).
  - **(b) Korrelationen:** im defektfreien Sektor C(r) = <s_e s_e'> fuer Kanten gleicher Richtungsklasse, Ausgleich
    gegen r (Potenz bzw. exponentiell).
- **Netz B:**
  - srs-Netz (K4-Kristall), periodisch, Grad 3. Koordinaten nach Standard-Lagen (8 Ecken je kubischer Zelle; Grad 3 und
    Taillenweite 10 pruefen).
  - Abtastung aller Zustaende mit q = +-1 an jeder Ecke: Ein Pfeil darf umklappen, wenn danach beide Enden in +-1 liegen.
    Gleichgewichtet, Ergodizitaet pruefen.
  - **(b) Korrelationen** wie in Netz A, Ausgleich Potenz gegen exponentiell.
- Zwei Gittergroessen je Netz.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| F0 | Kontrolle: Eisregel (Netz A) bzw. q = +-1 (Netz B) nach jedem Zug exakt erhalten; Gitterzahlen (Grad, Kanten) stimmen | 95 % |
| F1 | Netz A, Paarpotential: anziehend, bester Exponent p in [0,8; 1,2] (Coulomb) | 75 % |
| F2 | Netz A, Korrelationen: Potenzgesetz mit Exponent in [2,5; 3,5] (dipolar) | 65 % |
| F3 | Netz B (K4-Kristall), Korrelationen: abgeschirmt, ein exponentieller Ausgleich ist besser als jeder Potenzansatz, Korrelationslaenge <= 3 Kantenlaengen | 60 % |

**Bedeutung (vorab):**
- F1 bis F3 treffen ein: Aus Finns Bild entsteht eine Fernkraft genau dann, wenn die Fluss-Regel an jeder Ecke exakt
  aufgeht (gerader Grad, eckverknuepfte Tetraeder). Das frustrierte Einzeltetraeder, fortgesetzt als K4-Kristall,
  schirmt ab [H].
- F3 trifft nicht ein (auch Netz B weitreichend): Frustration allein verhindert die Fernwirkung nicht. Beschreiben.
- F1 trifft nicht ein: Werkzeug pruefen (gegen EIS-1, Teil 1), dann deuten.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren cpu, cpu3, cpu4, cpu6; nicht cpu2, die braucht
  Codex; nicht cpu5; je <= 10 min).
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min.
