# Blinde Vorhersagen fuer Karte SD-1: stille Stellen des gegenphasigen l = 1-Asts im gemischten Ball, g = 0,2

- **Beginn: 2026-09-30 08:16:08 CEST (date).** Schreibbeginn: 08:25:55 CEST (date). Ende: letzte Zeile.
- Bearbeiter: Anthropic-Agent (Opus), MOD-1 fortgesetzt. Nur Papier und Hand; kein Interpreter, keine Laeufe.
- **Blindheit:**
  - Nicht geoeffnet: RUNDE-08/sp1/, alle Dateien unter sd1/ ausser dieser.
  - Laut ls um 08:25:55 lagen dort schon: PLAN.md (08:22), sd1.py (08:24), lauf-69/ (08:22) und lauf-lokal/ (08:25).
    Ich habe keine davon geoeffnet.
  - Diese Datei entsteht also **nach** dem Anlegen der Laufordner; der Vorab-Status ist Sache der Leitung.
  - Gelesen: RUNDE-08/gf-bic/ERGEBNIS.md (Abschnitte 0, 1.3, 1.4, 2.4, 3, R9.1 bis R9.3), RUNDE-09.md (Karte SD-1), mein
    RUNDE-09/MODELL-DUENNWAND.md.
- **Kennzeichen:** [ES] eigene Herleitung, [H] Hypothese, (Hand) Schreibtischrechnung.

## 1. Welcher Ast (Hand, [ES])

- **Gemischter Ball, g > 0:** psi_1 = psi_2 = f e^{i omega t}/sqrt(2).
  - Symmetrischer Sektor = beta_eff-Modell mit beta_eff = 1/(2 (1 + g/4)^2) = 0,4535 bei g = 0,2.
  - omega_c^2 = 0,44875, S_c = 1,05, 2 sqrt(beta_eff) = 1,34688.
- **Gegenphasiger Sektor delta = (delta psi_1 - delta psi_2)/sqrt(2), delta = e^{i omega t}(p + i q):**
  - Die Entwicklung des Paarterms g Re[(psi_1^* psi_2)^2] bis zur zweiten Ordnung gibt L_p = L_eff + g S und L_q = L_eff +
    2 g S (wie GF-BIC 1.4).
  - Kanalform (Kanal u bei omega + nu, Kanal v bei nu - omega):
    - dp_A = U'(S) + g S
    - sp_A = -g S/2
- **Im Plateau (U'(S_in) - g S_in/2 = omega^2):** Die zwei Innenmoden haben

      k_pm^2 = nu^2 - 1,5 a +- sqrt(a^2/4 + 4 omega^2 nu^2),   a = g S_in ~ 0,21

  - Gegenueber dem U(2)-Grenzfall g -> 0 ist das Innere fuer beide Kanaele um **Delta = 1,5 a ~ 0,3** angehoben.
- **Der Ast:** Gegenlaeufer mit l = 1.
  - Ein l = 1-Hohlraumzustand chi_1 des v-Kanals, Energie E = (nu - omega)^2 < 1, Frequenz nu = omega + sqrt(E).
  - Er strahlt ueber die Kopplung sp_A in den offenen u-Kanal bei omega + nu = 2 omega + sqrt(E).
  - Bei l = 0 ist das der Gegenlaeufer der zweiten Leiter (nu ~ 2 omega, chi = f).
  - Der gleichlaeufige Partner (nu = omega - sqrt(E), der eigentliche Spin-Dipol der Kondensate) liegt unter der Kante:
    Sein u-Kanal bei 2 omega - sqrt(E) < 1 ist geschlossen. Er ist echt gebunden und hat keine "stillen Stellen".
- **Existenz:**
  - Der l = 1-Hohlraumzustand braucht einen Topf der Tiefe V0 = 1 - omega^2 - Delta mit sqrt(V0) R > pi (Schwelle der
    l = 1-Bindung).
  - Das schraenkt den Ast auf die duenne Wand ein:
    - **omega^2 < 0,548** bei Delta = 0,28
    - **< 0,5395** bei Delta = 0,315
    - **< 0,600** im Grenzfall g -> 0
  - R = R_tw + 0,06, geeicht an der l = 0-Leiter mit Plateauniveau omega^2 (Hand).

## 2. Wie sich der Formfaktor fuer l = 1 aendert ([ES])

- **l = 0 (zweite Leiter):**
  - Die Quelle S f ist innen flach, also eine gefuellte Kugel.
  - Formfaktor ~ j_1(k_a R)/(k_a R); Nullstellen bei den Nullstellen von j_1, k_a R ~ 4,49 / 7,73 / 10,90 / ...
- **l = 1:**
  - Die Quelle ist S chi_1 mit chi_1 ~ j_1(kappa r) innen. Die offene Welle ist j_1(k_a r).
  - Das Ueberlappintegral (Lommel) ist

        Integral_0^R j_1(k_a r) j_1(kappa r) r^2 dr = R^2 [kappa j_1(k_a R) j_1'(kappa R) - k_a j_1'(k_a R) j_1(kappa R)]/(k_a^2 - kappa^2)

  - Mit der Bindungsbedingung fuer chi_1 an der Wand verschwindet es genau dann, wenn die logarithmischen Ableitungen
    uebereinstimmen:

        g(k_a R) = g(kappa R) = -z - 1 - 1/(z + 1),   g(x) := x j_1'(x)/j_1(x),   z = Abfall aussen mal R

  - Daraus folgt [ES]: **k_a R = m pi + h/(m pi)** mit h = z^2/(z + 1). Das sind die Nullstellen von j_0(k_a R), wenig nach
    oben geschoben.
- **Folge:** Die l = 1-Leiter sitzt in k_a R eine halbe Stufe (~pi/2) unter der l = 0-Leiter. Das ist der Bessel-Versatz
  l pi/2, jetzt fuer eine Volumenquelle.
- **Groessen (Hand):**
  - E = omega^2 + Delta + kappa^2
  - k_a^2 = (2 omega + sqrt(E))^2 - omega^2 - Delta
  - kappa R aus der l = 1-Topfbedingung y cot y = 1 + y^2 (z + 1)/z^2 mit y^2 + z^2 = V0 R^2

## 3. Vorhersagen (g = 0,2)

**Die Stellen haengen kaum von Delta ab, die Existenzschwelle schon.**
- Gerechnet mit Delta = 0,28 (Hauptwert) und 0,315 (Plateau voll).
- Delta = 0,28 kommt aus der Pseudo-Goldstone-Eichung: Die Plateauschaetzung ueberschaetzt dort die g-Wirkung um den
  Faktor 1,4 bis 2,7, mit wachsendem Radius weniger. Bei R ~ 8 bis 11 erwarte ich 0,85 bis 0,9 des Plateauwerts.

| Stelle (Zaehlung m: k_a R ~ m pi) | omega*^2 | Re nu* (Konvention GF-BIC: Gegenlaeufer nu ~ omega + sqrt(E)) | Umlauf | Herleitung (Hand) |
|---|---|---|---|---|
| **oberste, m = 6** | **0,539 +- 0,004**, nur falls der Ast dort existiert (Schwelle 0,5395 bis 0,548) | 1,722 +- 0,01 | s | Delta = 0,28: 0,5391 (Schwelle 0,548). Delta = 0,315: 0,5395, genau an der Schwelle. Grenzfall g -> 0: 0,5350 |
| **m = 7** | **0,525 +- 0,004** | 1,706 +- 0,01 | -s | Delta = 0,28: 0,5253. Delta = 0,315: 0,5250. g -> 0: ~0,521 |
| **m = 8** | **0,515 +- 0,004** | 1,684 +- 0,01 | s | Delta = 0,315: 0,5146 (R ~ 11,2) |

- **Umlaufzahl:** Nachbarn haben entgegengesetzte Umlaufzahl (fest vorhergesagt). Das Vorzeichen s der obersten Stelle
  lege ich nicht fest (50/50). Die Konvention der W-Abbildung fuer l = 1 im neuen Code kenne ich nicht.
- **Abstand:** in 1/(omega*^2 - 0,44875) von Stelle zu Stelle 1,9 bis 2,2 (Hand: 2,00 von m = 6 zu 7, 2,13 von m = 7 zu 8).
- **Nur zur Einordnung, kuenstlich:** Delta = 0 auf dem Hintergrund von g = 0,2 (beta_eff = 0,4535). Das ist durch
  Verkleinern von g nicht erreichbar, weil sich dabei beta_eff mitaendert. Es gaebe dann hoehere Stellen bei 0,5924
  (m = 4), 0,5567 (m = 5) und 0,5350 (m = 6); Schwelle 0,600.

## 4. Scheiterregeln (vorab) und Gegenprobe

1. **Existenz:**
   - Gibt es bei g = 0,2 einen schmalen gegenlaeufigen l = 1-Pol (Re nu ~ omega + sqrt(E), E < 1) oberhalb omega^2 =
     0,56, dann ist die Plateauverschiebung Delta widerlegt.
   - Gibt es unterhalb 0,535 keinen solchen Pol, ist das Hohlraumbild widerlegt.
2. **Lage:**
   - Existiert der Ast und hat seine Breite im Fenster 0,51 bis 0,545 keine Nullstelle, ist das Bild widerlegt. Gemeint
     ist ein V-foermiger Einbruch unter 1e-3 des Nachbarwerts, oder ein Vorzeichenwechsel der signierten Amplitude.
   - Liegt eine gefundene Stelle mehr als 3 Balken (0,012) von der naechsten vorhergesagten entfernt, ist die
     Lommel-Formel fuer l = 1 widerlegt.
3. **Abstand:** Zwei benachbarte Stellen mit Schritt ausserhalb 1,6 bis 2,5 in 1/(x - 0,44875) widerlegen die Periode pi
   in k_a R.
4. **Paritaet:** Zwei benachbarte aufgeloeste Stellen mit gleicher Umlaufzahl widerlegen die Abwechslung.
5. **Halbe-Stufe-Versatz (optional, falls die l = 0-Gegenlaeufer-Leiter des gemischten Balls mitgerechnet wird):**
   - Die l = 1-Stellen muessen in k_a R ungefaehr in der Mitte zwischen zwei l = 0-Stellen liegen (Abweichung unter 0,25
     pi).
   - Liegen sie auf den l = 0-Stellen, ist der Bessel-Versatz widerlegt.

**Gegenprobe:**
- **(a) g-Abhaengigkeit der Existenzschwelle (Hand):**
  - Bei g = 0,02 gilt beta_eff = 0,4950, omega_c^2 = 0,4950 und Delta = 0,030. Dann liegt die Schwelle des l = 1-Asts
    bei **omega^2 ~ 0,629 +- 0,01**, also 0,134 ueber omega_c^2.
  - Bei g = 0,2 liegt sie nur 0,09 bis 0,10 darueber (0,5395 bis 0,548).
  - Die Breiten muessen mit g wie g^2 fallen.
  - Liegt die Schwelle bei g = 0,02 ebenfalls nur ~0,09 bis 0,10 ueber omega_c^2, ist die Verschiebung Delta = 1,5 g S
    widerlegt.
- **(b) Gleichlaeufiger Partner:** Der Spin-Dipol-Pol (nu = omega - sqrt(E)) muss reell sein (Breite unter der
  Aufloesung). Er ist echt gebunden; eine endliche Breite widerspraeche der Kanalzaehlung.

## 5. Grenzen

- Die Kopplung ist nur in fuehrender Ordnung behandelt (goldene Regel, Lommel-Integral).
- Plateau innen, R = R_tw + 0,06 (an l = 0 geeicht), Wandbeitrag zur Quelle vernachlaessigt.
- Die Verschiebung Delta = 1,5 g S ist hergeleitet. Ihre effektive Groesse ist unsicher: Die Pseudo-Goldstone-Daten
  sagen, dass die Plateauschaetzung bei kleinen Baellen um das 1,4- bis 2,7-Fache zu stark ist.
- Die Stellen liegen alle tief im Duennwandbereich (epsilon 0,066 bis 0,09, R ~ 8 bis 11). Dort hat die Numerik der Runde
  zweimal gemischt (Kernwachstum bis 1e9). Ein "nicht entscheidbar" ist dort wahrscheinlich.

## Einfach gesagt

Im gemischten Ball koennen die beiden Feldsorten gegeneinander schwappen: die eine nach vorn, die andere nach hinten.
Nach unserem Modell gibt es dabei eine gegenlaeufige Schwingung, die nur in ziemlich grossen Baellen existiert und
Energie nach aussen verliert, ausser an bestimmten Groessen. Dort passt die innere Welle so, dass sich die Abstrahlung
aufhebt, eine halbe Wellenlaenge versetzt gegenueber dem gleichmaessigen Fall. Wir sagen drei solche Stellen voraus, bei
omega^2 ~ 0,539, 0,525 und 0,515, mit abwechselndem Drehsinn. Weil sie tief im Bereich sehr grosser Baelle liegen, kann
die Rechnung dort auch unentschieden ausgehen.


**Ende: 2026-09-30 08:27:29 CEST (date, nach dem Schreiben gemessen).** Ab jetzt keine Aenderungen mehr an dieser Datei; Nachtraege nur in einer neuen Datei.
