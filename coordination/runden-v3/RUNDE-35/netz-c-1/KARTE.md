# NETZ-C-1: Hat ein Stabnetz eine Lichtgeschwindigkeit, und gehorchen Fehlstellen darin der Relativitaet? (Runde 35)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 20:43:31 CEST (date), vor jeder Rechnung.
- **Anlass:** Finns Fragen vom 03.10.: Tetraeder-Netz mit Krafteinheiten (RUNDE-34/tetra-konzept/), "ist das vllt
  lichtgeschwindigkeit" (Peitsche, ~19:12).
  - In einem Weltbild aus Staeben ist "Lichtgeschwindigkeit" die Wellengeschwindigkeit des Netzes. Zwei Fragen
    entscheiden, ob das traegt:
    1. Hat das Netz eine einzige, richtungsunabhaengige Wellengeschwindigkeit?
    2. Werden Fehlstellen (Teilchen) darin automatisch relativistisch, mit der Netzgeschwindigkeit als c?
  - Bezug Spin-2-Kette: Glied 10 setzt Lorentz-Invarianz voraus; LORENTZ.md sammelt die Schranken.
- Kennzeichen: [M] Mathematik (vorab ableitbar), [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

### Teil A: Wellengeschwindigkeiten von Stabnetzen

- **fcc-Netz** (Kanten des Tetraeder-Oktaeder-Gitters, Grad 12), Zentralfedern k, Gitterkonstante a, Masse m je Knoten
  [M, Born-Summe]: C11 = 2k/a, C12 = C44 = k/a. Mit c0 = sqrt(C44/rho) = (a/2) sqrt(k/m):

  | Richtung | laengs | quer 1 | quer 2 |
  |---|---|---|---|
  | [100] | 1,414 | 1 | 1 |
  | [110] | 1,581 | 1 (Polarisation [001]) | 0,707 (Polarisation [1-10]) |
  | [111] | 1,633 | 0,816 | 0,816 |

  - Drei verschiedene Geschwindigkeiten laengs [110], also Doppelbrechung der Querwellen, Spanne 0,707 bis 1,633.
- **Allgemein** [M]: In jedem isotropen, stabilen elastischen Medium gilt c_laengs/c_quer >= 2/sqrt 3 (Kompressionsmodul
  > 0). Ein Stabnetz hat also nie eine einzige Lichtgeschwindigkeit, sondern mindestens zwei Lichtkegel ("bimetrisch"
  [L: Barcelo/Liberati/Visser, Living Rev. Rel., analoge Gravitation]).
- **Diamant- und srs-Netz** (Grad 4 bzw. 3) mit Zentralfedern sind beweglich [M, Maxwell-Zaehlung]: Querwellen haben
  Geschwindigkeit 0. Erst Winkelfedern machen sie steif [L: Keating 1966 fuer Diamant].
- **Pyrochlor-Netz** (eckverknuepfte Tetraeder, Grad 6 = 2d) ist isostatisch. Nach EIS-1 hat es 12 L^2 Eigenspannungen
  laengs gerader <110>-Linien und ebenso viele Nullmoden [H: Nullmoden laengs Linien im k-Raum, ein Ast mit
  Geschwindigkeit 0 in manchen Richtungen].

### Teil B: Fehlstelle in einer Kette (Frenkel-Kontorova bzw. diskretes Sine-Gordon)

- **Kette:** u_n'' = (u_{n+1} - 2 u_n + u_{n-1})/h^2 - sin u_n - eta u_n' + F, Abstand h.
  - Die Langwellen-Geschwindigkeit ist 1; die Gruppengeschwindigkeit sin(kh)/(h omega) bleibt < 1 [M].
- **Kontinuum (h -> 0)** [M, L: Frank 1949 fuer Versetzungen; McLaughlin/Scott 1978]:
  - Kink u = 4 arctan exp(gamma (x - v t)), Ruheenergie 8, Breite 1/gamma (Lorentz-Verkuerzung mit der
    Kettengeschwindigkeit).
  - Endgeschwindigkeit unter Kraft und Reibung: gamma v = pi F/(4 eta). Die Kraft gibt 2 pi F je Weglaenge, die Reibung
    nimmt 8 gamma eta v^2.
  - Ohne Reibung waechst gamma = 1 + 2 pi F x/8 ohne Grenze, v -> 1.
- **Gitter** [H]: Wird die verkuerzte Breite 1/gamma vergleichbar mit h, strahlt der Kink ab (Peierls-Nabarro). Dann ist
  gamma begrenzt: Die Relativitaet gilt nur oberhalb der Gitterskala, wie die Lorentz-Verletzung bei der Planck-Laenge
  (LORENTZ.md).

## Test (Code-Agent)

- **Teil A:**
  - Dynamische Matrix D(k) fuer Zentralfedern (Ruhelaenge = Kantenlaenge, Steifigkeit 1) und mit Winkelfedern (je Paar von
    Kanten an einem Knoten, Steifigkeit k_theta = 0,1).
  - Netze:
    - fcc (Grad 12)
    - Pyrochlor (Grad 6)
    - Diamant (Grad 4)
    - srs (Grad 3; K4-Kristall wie FLUSS-1)
    - optional Tetraeder-Oktaeder-Fachwerk mit Zusatzdiagonalen
  - Akustische Geschwindigkeiten c(k-Richtung, Ast) aus der Steigung bei kleinem |k| (zwei |k|), in [100], [110], [111]
    und auf mindestens 200 Richtungen der Einheitskugel.
  - Nullmoden: Zahl, Lage im k-Raum (Gitter von k-Punkten).
  - Kontrolle fcc gegen die Tabelle oben.
- **Teil B:**
  - Kette mit N Knoten, Kink starten.
  - (1) Reibung eta = 0,01, Kraefte so, dass pi F/(4 eta) = 0,3; 1; 3; 10 (F = 0,0038 bis 0,127); h = 0,1 und 1.
    - Berichtigung der Leitung vor dem Start (Messvorschrift, keine Vorhersage geaendert): Zuerst stand eta = 0,1. Dann
      waere F = 1,27 > 1 fuer pi F/(4 eta) = 10, und die Kette haette kein ruhendes Vakuum mehr (gekippte Waschbrett-
      Kraft). Mit eta = 0,01 bleibt F < 1; die Einschwingzeit ~ 1/eta = 100 verlangt Laufzeiten bis t ~ 1000.
  - (2) Ohne Reibung, F = 0,02, h = 0,5; 0,25; 0,125: gamma(t) bis zur Zerstoerung oder Laufende.
  - Gemessen:
    - Kinkort (u = pi, interpoliert) und Schnelle
    - gamma aus der groessten Steigung (u_x,max = 2 gamma)
    - Energiebilanz
- Gitterweiten bzw. Zeitschritte je zwei.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| P0 | Kontrolle: fcc-Geschwindigkeiten treffen die Tabelle auf 1e-4 relativ; Zahl der Nullmoden passt zur Maxwell-Zaehlung | 95 % |
| P1 | In jedem steifen Netz (alle akustischen Geschwindigkeiten > 0) gibt es in jeder Richtung mindestens zwei verschiedene Geschwindigkeiten, Verhaeltnis groesster zu kleinster >= 1,15 | 90 % |
| P2 | Pyrochlor nur mit Zentralfedern: mindestens ein akustischer Ast hat in einigen Richtungen Geschwindigkeit 0 (< 1e-6) | 60 % |
| P3 | Mit Winkelfedern sind alle Netze steif, und jeder Querast schwankt ueber die Richtungen um mindestens 10 % (keine zufaellige Isotropie) | 70 % |
| K0 | Kontrolle: ohne Kraft und Reibung Energie auf 1e-6 erhalten; groesste Gruppengeschwindigkeit der Kette < 1 | 95 % |
| K1 | h = 0,1: Endgeschwindigkeit innerhalb 2 % von gamma v = pi F/(4 eta) (Sollwerte v = 0,287; 0,707; 0,949; 0,995) | 80 % |
| K2 | h = 0,1, v <= 0,95: gamma aus der Steigung innerhalb 3 % von 1/sqrt(1 - v^2) | 75 % |
| K3 | Kein Kink ist je schneller als 1 (Kinkort-Schnelle <= 1 + 1e-3, alle Laeufe) | 95 % |
| K4 | [H] Ohne Reibung waechst gamma bis zu einer Grenze, die mit kleinerem h steigt; gamma_max h liegt fuer alle drei h zwischen 0,3 und 5 | 55 % |
| K5 | [H] h = 1: Endgeschwindigkeit bei pi F/(4 eta) = 10 mindestens 10 % unter dem Kontinuumswert (Gitterabstrahlung) | 50 % |

**Bedeutung (vorab):**
- K1 bis K3 treffen ein: Fehlstellen in einem Netz verhalten sich automatisch relativistisch, mit der Wellengeschwindigkeit
  des Netzes als ihrer Lichtgeschwindigkeit [L: das ist bekannt, Frank 1949]. Das stuetzt Finns Bild an einer Stelle.
- P1 und P3 treffen ein: Ein Stabnetz hat aber nie eine einzige, richtungsfreie Geschwindigkeit. Eine Welt aus solchen
  Staeben haette Doppelbrechung und Richtungsabhaengigkeit des Lichts, und genau das ist durch Messungen sehr eng
  ausgeschlossen (LORENTZ.md).
  - Finns Bild braucht dann ein "Licht", das nicht die gewoehnliche Netzschwingung ist. Ein Kandidat waere das
    Eis-Photon aus der Erhaltungsregel (FLUSS-1, Hermele/Fisher/Balents 2004) [H].
- K4 trifft ein: Die Relativitaet gilt nur oberhalb der Gitterskala; sehr schnelle Fehlstellen merken das Gitter.
- P2 trifft ein: Das eckverknuepfte Tetraedernetz ist an der Grenze zur Beweglichkeit; seine "Lichtgeschwindigkeit"
  verschwindet in manchen Richtungen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber coordination/runden-v3/kleintest.sh, Spuren cpu3, cpu4 oder cpu6 (nicht cpu2,
  cpu5, p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
