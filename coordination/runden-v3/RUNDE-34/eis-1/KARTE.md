# EIS-1: Zaehlregel gegen Kraftregel auf demselben Tetraedergitter (Runde 34)

- Leitung claude-primary. Karte, Schreibtisch und Vorhersagen geschrieben ab 2026-10-03 18:11:05 CEST (date), vor jeder
  Rechnung.
- **Anlass:** Finn ~18:05: "mach A, Spin-Eis und dann unsere Variante alles pruefen". Vorschlag A aus
  RUNDE-34/TETRAEDER-ANALYSE.md, Abschnitt 5.
- **Frage:** Entsteht Fernwirkung zwischen Defekten in einem Gitter aus Tetraedern, und wovon haengt das ab?
  - Teil 1 rechnet die bekannte Antwort fuer Spin-Eis nach (Zaehlregel je Tetraeder).
  - Teil 2 prueft unsere Variante: Stab-Tetraeder auf demselben Gitter (Kraftregel, also Gleichgewicht je Knoten).
  - Teil 3 nimmt ein steifes Vergleichsgitter.

## Schreibtisch der Leitung (vor jeder Rechnung)

1. **Gitter:** Pyrochlor, also eckenverknuepfte Tetraeder; die Tetraedermitten bilden das Diamantgitter.
   - Spin-Eis: ein Ising-Spin je Ecke, entlang der Verbindung der beiden Tetraedermitten.
   - Mechanik: dieselben Ecken als Gelenke, je Tetraeder 6 Staebe.
2. **Spin-Eis** [L: Castelnovo/Moessner/Sondhi 2008; Henley 2010; Isakov u. a. 2004, aus dem Gedaechtnis]:
   - Die Eisregel (2 rein, 2 raus) ist eine diskrete Divergenzfreiheit des Spinfelds auf dem Diamantgitter.
   - Grobkoernig gilt F = (K/2) int B^2 mit entropischer Steifigkeit K ~ T.
   - Zwei Defekte (3 rein 1 raus und Gegenstueck) spueren F(r) = a - C/r, also entropisches Coulomb. Die
     Spin-Korrelationen fallen dipolar wie 1/r^3.
3. **Mechanik, Kraftregel:**
   - Gleichgewicht je Knoten ist ein Gauss-Gesetz fuer das Stabkraftfeld: Summe der Stabkraefte = aeussere Kraft.
   - Eigenspannungen sind die divergenzfreien Kraftfelder.
   - Die Energie ist quadratisch im Kraftfeld selbst (sum t^2/(2k)), wie im Spin-Eis quadratisch im Fluss.
   - Der Unterschied ist die Vertraeglichkeit: In einem ueberbestimmten (steifen) Netz muessen die Dehnungen von
     Knotenverschiebungen kommen. Das macht die Gleichungen elliptisch: Eine Kraft- bzw. Dipolquelle faellt wie in der
     Elastizitaet (Kraft ~ 1/r^2, Fehlpass-Dipol ~ 1/r^3).
   - In einem isostatischen Netz bestimmt das Gleichgewicht allein die Kraefte. Dann laufen Kraefte entlang von Linien
     weiter ("Kraftketten", hyperbolisch) [L?: Moukarzel 1998; Tkachenko/Witten 1999].
4. **Maxwell-Zaehlung** [M]:
   - Pyrochlor-Gelenkwerk: je Tetraeder 2 Knoten (6 Freiheitsgrade) und 6 Staebe, also isostatisch. Es gibt
     Starrkoerper-Einheitsmoden (RUM) wie in beta-Cristobalit [L?: Dove, Heine, Hammonds].
   - Tetraeder-Oktaeder-Netz (fcc-Knoten, alle 12 Nachbarn als Staebe): 6 Staebe je Knoten gegen 3 Freiheitsgrade, also
     ueberbestimmt und steif.
5. **Erwartung:**
   - Spin-Eis ergibt Coulomb, 1/r im Potential.
   - Das steife Netz faellt mindestens wie 1/r^3 (Fehlpass-Dipol).
   - Das isostatische Pyrochlor-Netz liegt dazwischen oder traegt Kraefte sogar entlang von Linien ungedaempft. Ob dort
     etwas Coulomb-artiges entsteht, ist die offene Frage.
- **Ableitbarkeit:** E0 und E1 sind Literatur bzw. Lehrbuch-Elastizitaet, also nur Kontrollen. E2 ist die eigentliche
  Frage. Projekt-grep: Spin-Eis und isostatische Netze wurden im Projekt nie gerechnet.

## Test (Code-Agent)

- **Teil 1 (Spin-Eis):**
  - Klassisches Eismodell auf einem periodischen Pyrochlor-Gitter (L^3 kubische Zellen zu je 16 Ecken).
  - Zwei entgegengesetzte Defekte, Abtastung aller Eis-Konfigurationen mit genau diesen zwei Defekten, z. B. mit einem
    Wurm-Algorithmus, der einen Defekt durch Spinumklappen bewegt (T -> 0, alle Eiszustaende gleich gewichtet).
  - Histogramm des Abstands, F(r) = -T ln[P(r)/g(r)] mit g(r) = Zahl der Tetraederpaare im Abstand r.
  - Ausgleich a - C r^(-p).
- **Teil 2 (Pyrochlor-Stabnetz, isostatisch):**
  - Gelenkwerk mit gleichen Staeben (k = 1), periodisch.
  - Fehlpass: ein Stab um delta zu lang (Eigendehnung).
  - Lineare Antwort: Stabkraefte t = Projektion der Eigendehnung auf die Eigenspannungen (Methode der kleinsten Quadrate,
    duenn besetzt). Bei Starrkoerpermoden mit Pseudo-Inverser oder winziger Zusatzfeder; die Regel steht im Plan.
  - Gemessen: Betrag der Stabkraefte gegen den Abstand, richtungsaufgeloest entlang der Gitterrichtungen [110], [100],
    [111], und die Zahl der Eigenspannungen.
- **Teil 3 (steifes Vergleichsnetz):** Tetraeder-Oktaeder-Netz mit gleichem Fehlpass, gleiche Auswertung.
- **Zusatz (nur berichtet, wenn die Zeit reicht):** zwei Fehlpaesse in Teil 2 und 3, Wechselwirkungsenergie gegen
  Abstand.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| E0 | Spin-Eis: F(r) ist anziehend, und der beste Exponent p liegt in [0,8; 1,2] (Coulomb); Kontrolle aus der Literatur | 80 % |
| E1 | Steifes Tetraeder-Oktaeder-Netz: Stabkraft eines Fehlpasses faellt mit Exponent in [2,5; 3,5] (Elastizitaet, Dipol) | 75 % |
| E2 | Isostatisches Pyrochlor-Netz: in mindestens einer Gitterrichtung faellt die Stabkraft mit Exponent <= 1,5, also deutlich langsamer als im steifen Netz | 55 % |
| E3 | Pyrochlor-Netz: Die Zahl der Eigenspannungen waechst mit der Gittergroesse (ausgedehnte Eigenspannungen, wie bei RUM-Gittern), statt konstant zu bleiben | 60 % |

**Bedeutung (vorab):**
- E0, E1 und E2 treffen ein: Gleiches Gitter, verschiedene Regel, verschiedene Reichweite. Eine Zaehlregel ergibt
  Coulomb; eine Kraftregel im isostatischen Netz traegt weit, im steifen nicht.
  - Fuer die "Tetraeder-Ursuppe" [H]: Fernwirkung braucht Regeln, die das Gleichgewicht allein festlegen (isostatisch)
    oder zaehlen (entropisch), keine ueberbestimmte Steifigkeit.
- E2 trifft nicht ein: Auch das isostatische Stabnetz schirmt ab. Dann erzeugt nur die Zaehlregel Fernwirkung; unsere
  mechanische Variante braucht etwas anderes. Beschreiben.
- E0 trifft nicht ein: Das Werkzeug ist fehlerhaft (Wurm, Abstandsmass, Gittergroesse). Erst beheben, dann Teil 2
  bewerten.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU- oder P4000-Spur; je <= 10 min).
- Plan vor der ersten echten Rechnung einfrieren. Rauchlaeufe nur mit anderen Gittergroessen.
- Zeitbox 150 min.
- Literatur nur aus dem Gedaechtnis [L?]. Der Agent darf die drei Quellen per arXiv-API kurz pruefen (Coulomb-Phase des
  Eismodells, Isostatik), ohne die Vorhersagen zu aendern.
