# Review der Codex-Anmerkungen durch die Leitung (erste von zwei Pruefungen; Finn 05.10.: "Review Codex Anmerkungen noch mal doppelt")

- Leitung claude-primary, geschrieben ab 2026-10-05 09:58 CEST (date-Klammer 09:57:18 bis 09:58).
- **Gelesen, vollstaendig:**
  - coordination/codex-ideation-20261005/IDEATION-3-20261005.md
  - coordination/codex-ideation-20261005/IDEATION-3-REVIEW.txt
- **Schon frueher gelesen:** GAP-REVIEW.txt und IDEATION-REVIEW.txt (Runde 46, eingearbeitet in Lueckenabgleich 1.1).
- **Zweite, unabhaengige Pruefung:** pruefer-opus, Karte RUNDE-37/codex-review-r48 (laeuft seit 09:55). Sie hat diese Datei nicht gesehen.

| Nr | Codex' Anmerkung (kurz) | Wertung der Leitung | Handrechnung bzw. Beleg | Folge fuer uns |
|---|---|---|---|---|
| C1 | Rang 2 => Rang 4 gilt nicht: drei Achsen mit Gewicht 1 geben Summe n n^T = I, aber M_1122 = 0 statt 1/5 | **richtig** | Isotrop M_ijkl = (d_ij d_kl + d_ik d_jl + d_il d_jk)/5; die Spur M_iikk = (9 + 3 + 3)/5 = 3 ist gleich der Summe der \|n\|^4 = 3, also M_1122 = 1/5. Bei den Achsen ist n_1 n_2 = 0 [M] | Die DANZER-2-Identitaet (Licht isotrop auf jedem Netz) sagt nichts ueber Schwerewellen. In v4.1 ist das nicht behauptet; in Berichten an Finn so lassen |
| C2 | Tensorielle Rekonstruktion K_t = (V_t/2) q'^T R^T G R q' gibt eine affine Patch-Identitaet | **richtig**, und vermutlich gleich A2 | Bei gleichem h ist die Summe ueber t von V_t G(h, h)/2 = Vol G(h, h)/2 [M]; entspricht HM0 | Codex sagt selbst: Kontrolle, kein neuer Erfolg |
| C3 | min_g K(v + g) braucht einen positiven vertikalen Block C = R^T A R; die DeWitt-Form kann indefinit sein | **richtig** | Schur-Komplement A - A R C^-1 R^T A nur bei C > 0 ein Minimum; bei indefinitem C nur stationaere Elimination [M] | an HODGE-MASSE-1 weitergegeben (09:46) |
| C4 | Horizontal ist nicht die einzig korrekte Eichfixierung; jede regulaere, konsistente Fixierung mit Dirac-Klammer gibt dieselben Observablen | **richtig**, und es trifft meine Karte | Standard der Zwangssysteme [L]. Meine Karte HODGE-MASSE-1 schrieb "nur mit der horizontalen Reduktion" | **Selbstanzeige:** Das absolute "nur" ist falsch. Das ist ein Verstoss gegen die eigene Regel "jede nie/immer/nur-Aussage gegen die Mechanik pruefen". Weitergegeben; Wertung in HM1 entsprechend vorsichtig |
| C5 | "Unprojiziert 0 %" beweist keine isotropen physikalischen Moden | **richtig** | Unprojizierte Vektoren koennen Zwangsbedingungen verletzen [M] | Der Verdacht "Reduktionsartefakt" bleibt Verdacht; frueher gemeldete Zahlen erst nach korrektem Vergleich berichtigen |
| C6 | HM4 < 1e-4 heisst nicht, dass der Taktschritt die Energie exakt erhaelt; kleine Spruenge koennen sich aufsummieren | **richtig** | [M] | Die Bedeutungszeile von HM4 ist zu stark; weitergegeben |
| C7 | Umklappen braucht eine kanonische Zustandsuebertragung: p_- = P^T p_+, M_- = P^T M_+ P; ein Zug, der die Zahl der Freiheitsgrade aendert, ist keine symplektische Bijektion | **richtig** | Beim 2-3-Zug in flacher Geometrie: 9 Kanten (zwei Tetraeder) gegen 10 Kanten mit einer Flachheitsbedingung, also beidseitig 9 geometrische Freiheitsgrade. Ein gemeinsamer reduzierter Raum existiert [M, Leitung] | Starker Kandidat fuer den Energiesprung in TAKT-DYNAMIK-1. Folgekarte nach HODGE-MASSE-1 (Codex Rang 2) |
| C8 | Verschwindendes duales Mass kann M^-1 singulaer machen: p^2/(2 mu) unbeschraenkt bei mu -> 0 | **richtig** (elementar) | [M] | gehoert in die Folgekarte zu C7 |
| C9 | Bewegliche kinetische Metrik braucht die dM-Terme in der Bewegungsgleichung | **richtig** als Formel; ob der Code sie hat, ist offen | Euler-Lagrange-Gleichung mit M(q) [M]. In der linearen Rechnung auf festem Hintergrund ist M konstant, die Terme sind dort zweiter Ordnung | Codelektuere vor jeder Rechnung |
| C10 | Lineare Erstklassigkeit nicht ausweiten; "maximales Slicing" ist kein Nachweis "Netz = ART"; Prozentzahlen nicht unbedingt mit Messgrenzen vergleichen | **richtig** | deckt sich mit dem v4-Leser (A2, A3, B7) | in v4.1 schon berichtigt |

**Gesamturteil der Leitung:** Alle zehn Anmerkungen sind richtig. Vier treffen Formulierungen in meinen eigenen Karten oder Texten (C4, C5, C6, C10). Keine verlangt, ein gerechnetes Ergebnis zurueckzunehmen; sie engen Deutungen ein. Der wichtigste neue Anstoss ist C7, die kanonische Zustandsuebertragung beim Umklappen.

**Nachgefuehrt:** Gedaechtnis "Widerspruchsprobe absoluter Aussagen" um den "nur"-Fall aus HODGE-MASSE-1 ergaenzt.
