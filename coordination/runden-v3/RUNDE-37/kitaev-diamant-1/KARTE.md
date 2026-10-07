# KITAEV-DIAMANT-1: Entstehen auf Finns Tetraederknoten-Gitter Fermionen plus Eichfeld aus reinen Spins? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 04:58:01 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - STRINGENDE-1: In bosonischen Netzmodellen koennen Stringenden Fermionen sein. In 3D braucht das eine besondere
    innere Bauweise je Knoten (Levin/Wen, Spin 3/2 auf dem Wuerfelgitter).
  - Vorschlag des Agenten: dasselbe auf einem Gitter mit vier Strichen je Knoten, also dem Diamantgitter. Dort ist jeder
    Knoten ein Tetraeder-Mittelpunkt mit vier Strichen, wie in Finns Bild.
  - Ideenpool H9 (Kitaev-Netz).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Gamma-Matrix-Kitaev-Modelle [L?: Ryu 2009, "Three-dimensional topological phase on the diamond lattice"; Wu, Arovas,
  Hung 2009, "Gamma-matrix generalization of the Kitaev model"]:**
  - Auf jedem Knoten sitzt ein vierdimensionaler Raum (Spin 3/2) mit vier antikommutierenden Gamma-Matrizen
    Gamma^1..Gamma^4, eine je Strich-Richtung.
  - H = sum_{<ij> Richtung a} J_a Gamma_i^a Gamma_j^a (plus ggf. Zusatzterme aus der Quelle).
- **Loesungsweg [L, Kitaev 2006]:**
  - Mit Majorana-Darstellung (Gamma^a = i b^a c bzw. aehnlich, mit Nebenbedingung) zerfaellt das Modell in freie
    Majorana-Fermionen c, die in einem statischen Z_2-Eichfeld u_ij = i b_i^a b_j^a huepfen.
  - Die Schleifenoperatoren (Produkte entlang geschlossener Wege, auf dem Diamantgitter Sechserringe) sind Erhaltungsgroessen.
- **Fuer Finns Bild [H]:** Aus reinen Spins auf Tetraederknoten entstehen exakt Fermionen (die c) und ein Eichfeld (die u)
  mit Fluessen auf den Ringen. Das waere ein konkretes Modell fuer "Fermionen und Licht-artiges Eichfeld aus dem Netz",
  hier mit Z_2- statt U(1)-Eichfeld.

## Test (Code-Agent)

- **Quelle zuerst:** Modell aus der Literatur (gezielte Abrufe, hoechstens 5, keine Websuche) genau uebernehmen: Gamma-Matrizen,
  Kopplungen, Nebenbedingung, Schleifenoperatoren.
- **Pruefen auf einem kleinen Diamantgitter** (z. B. 2x2x2 fcc-Zellen mit 2 Knoten je Zelle, also 16 Knoten, Hilbertraum
  4^16 zu gross fuer exakte Diagonalisierung, also algebraisch):
  - Kommutieren die Schleifenoperatoren mit H und miteinander? Algebraische Pruefung der Gamma-Produkte, Vorzeichen exakt.
- **Majorana-Spektrum:** im fluss-freien Sektor (bzw. dem von der Quelle angegebenen Grundzustandssektor) die freien
  Huepfmatrizen auf grossem Gitter im Impulsraum. Lage der Nullstellen (Punkte, Linien, Luecke) fuer gleiche Kopplungen
  J_a = 1 und fuer eine unsymmetrische Wahl.
- **Vertauschungsphase:** Wie in STRINGENDE-1 (Drei-String-Verfahren) fuer die Anregungen, sofern die Quelle die
  String-Operatoren angibt. Sonst nur Spektrum und Erhaltungsgroessen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KD0 | Kontrolle: Die vier Gamma-Matrizen antikommutieren und quadrieren zu 1; H und die Schleifenoperatoren (Sechserringe) kommutieren exakt | 85 % |
| KD1 | Die Abbildung auf freie Majorana-Fermionen im statischen Z_2-Feld gelingt; Spektrum im fluss-freien Sektor bei J_a = 1 hat Nullstellen (Punkte oder Linien), keine Luecke [L?] | 55 % |
| KD2 | Eine unsymmetrische Kopplung (ein J_a deutlich groesser) oeffnet eine Luecke im Majorana-Spektrum | 55 % |
| KD3 | [H] Die Vertauschungsphase der Majorana-Anregung (bzw. eines geeigneten Stringendes) laesst sich wie in STRINGENDE-1 messen und ist -1 | 40 % |

**Bedeutung (vorab):**
- **KD0 und KD1 treffen ein:** Auf einem Netz mit vier Strichen je Knoten, also Finns Tetraederknoten, gibt es ein exakt
  loesbares Spinmodell, aus dem Fermionen und ein Eichfeld entstehen.
  - Das ist die Netz-Fassung von "Elektronen und Licht aus demselben Netz", hier mit Z_2 statt U(1) [L/H].
- **KD3 trifft ein:** Die Fermionen sind auch als Stringenden messbar.
- **Grenzen:**
  - Spin 1/2 unter echten Raumdrehungen ist auch hier nicht gezeigt.
  - Das U(1)-Gegenstueck (Pfeil-Eis) waere ein eigener Schritt.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a (CPU-Rechnung); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
