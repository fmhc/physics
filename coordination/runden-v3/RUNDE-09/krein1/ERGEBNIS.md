# KREIN-1: Ergebnis - Krein-Signatur der stillen Moden

- Auftrag: Leitung claude-primary, 2026-09-30 10:13:41 CEST. Bearbeitet 10:14:02 bis 10:27:41 CEST (date).
- Plan mit Herleitung und Erwartung vorab: PLAN.md (geschrieben ab 10:20:28, vor jeder Rechnung).

## Ergebnis

**Alle acht stillen Stellen tragen positive Energie (positive Krein-Signatur).**
- Der Grund ist strukturell: Die erhaltene Energie einer Mode ist
  E_2 = 2 rho [(omega + rho) ||a||^2 + (rho - omega) ||b||^2].
- An allen Stellen ist rho > omega (Abstand >= 0,845). Beide Gewichte sind positiv, unabhaengig von der
  Eigenfunktion.
- Fuer l = 0, n = 1 ist das Vorzeichen streng bewiesen (Satz K unten, auf BEWEIS-1 gestuetzt).
- Die Rechnung bestaetigt es an jeder Stelle mit einer unabhaengigen Gegenprobe (E_2 direkt aus Feld und
  Zeitableitung) und mit einem zweiten Programm (bic2).

**Vorzeichen gegen die Vermutung im Auftrag:** Der b-Term geht mit (rho - omega) ein, nicht mit (omega - rho).
- Die Form (omega + rho)||a||^2 + (omega - rho)||b||^2 ist die (zeitgemittelte) Ladung der Stoerung im Laborsystem.
- Sie waere an allen Stellen **negativ** (etwa -0,83 je Einheitsnorm), weil der geschlossene Kanal negative
  Laborfrequenz omega - rho hat.
- Die Krein-Signatur ist aber das Vorzeichen der Energie im mitrotierenden Rahmen, E_2 = d^2(H - omega Q). Sie ist
  positiv.
- Wer die Ladungsform nimmt, schliesst also faelschlich auf negative Energie.

## Tabelle (R = 44, Normierung ||a||^2 + ||b||^2 = 1 je Einheitswinkelnorm)

K = E_2 = 2 rho N. Gegenprobe = E_2(0)/(2 rho N) mit E_2(0) direkt bei t = 0, erst r0 = 1e-3, in Klammern r0 = 1e-5.
L-Test = |dN|/N zwischen R = 36 und 44.

| Stelle | omega*^2 | rho* | K | Anteil a (offen) | Vorzeichen | Gegenprobe | L-Test | Anschlussrest | Belegstufe |
|---|---|---|---|---|---|---|---|---|---|
| l = 0, n = 1 (Beweiswerte) | 0,7976767871 | 1,7446175448 | 3,008709 | 0,604 % | positiv | 0,9999732 (0,9999997) | 3e-16 | 4,6e-10 | **Vorzeichen streng** (Satz K); Wert numerisch |
| l = 0, n = 1 (Tabellenwert) | 0,797677 | 1,744618 | 3,008711 | 0,604 % | positiv | 0,9999731 | 9e-14 | 2,6e-6 | numerisch |
| l = 0, n = 2 | 0,685129 | 1,690357 | 2,986921 | 1,262 % | positiv | 0,9999979 (0,9999998) | 1e-12 | 1,7e-6 | Vorzeichen strukturell, Mode numerisch |
| l = 0, n = 3 | 0,631449 | 1,652588 | 2,931173 | 1,818 % | positiv | 0,9999956 (0,9999995) | 6e-11 | 2,1e-5 | wie n = 2 |
| l = 1, n = 1 | 0,754496 | 1,826342 | 3,527840 | 0,466 % | positiv | 1,0000000065 | 2e-11 | 9,4e-8 | wie n = 2 |
| l = 1, n = 2 | 0,660280 | 1,717301 | 3,176562 | 1,240 % | positiv | 1,000000085 | 1e-12 | 5,5e-6 | wie n = 2 |
| l = 2, n = 1 | 0,643905 | 1,762082 | 3,442893 | 1,078 % | positiv | 0,99999988 | 1e-10 | 7,3e-6 | wie n = 2 |
| l = 2, n = 2 | 0,606981 | 1,694040 | 3,194065 | 1,783 % | positiv | 0,99999995 | 2e-12 | 1,7e-5 | wie n = 2 |
| gemischter Ball Z1 (psi_2, g = 0,2) | 0,7113723 | 1,6888290 | 2,859014 | 0,062 % | positiv | 0,9999806 (0,9999998) | 4e-15 | 3,5e-7 | wie n = 2 (Modell gfbic) |

Lesehilfe:
- **K** ist die Energie je Einheitsnorm. Sie liegt stets zwischen 2 rho (rho - omega) und 2 rho (rho + omega). Die
  Werte liegen nahe der unteren Grenze, weil fast die ganze Norm im geschlossenen Kanal b sitzt.
- **Anteil a** ist der offene Kanal, also die unterdrueckte Abstrahlungskomponente. Er betraegt 0,06 bis 1,8 Prozent.
  Vorab hatte ich 5 bis 30 Prozent geschaetzt; der Anteil ist kleiner als erwartet.
- **Anschlussrest**: relativer Rest beim Anschluss regulaere/Jost-Loesung. Er misst, wie genau die Tabellenwerte die
  Stelle treffen (6 bis 7 Stellen). Mit den Beweiswerten fuer n = 1 sinkt er auf 4,6e-10.
- **"Vorzeichen strukturell, Mode numerisch"**: Die Existenz einer exakten L^2-Mode an diesen Stellen ist numerische
  Evidenz (Umlaufzahlen aus Runde 7/8/9), kein Beweis. Falls sie existiert, ist ihre Signatur wegen rho > omega
  sicher positiv (Satz K', streng).

## Gegenproben und Kontrollen

1. **Direkte Energie bei t = 0** (Auftrag Schritt 2):
   - E_2(0) = int rho^2 (A - B)^2 + (A' + B')^2 + l(l+1)(A + B)^2/r^2 + (dp + sp - omega^2)(A + B)^2 dr benutzt
     Ableitungen und Potential, nicht die Gewichte.
   - Uebereinstimmung mit 2 rho N auf 1e-5 bis 1e-8.
   - Die groessere Abweichung bei l = 0 (bis 2,7e-5) kommt vom Randterm am unteren Integrationsende. Mit
     r0 = 1e-5 statt 1e-3 sinkt sie auf <= 5e-7 (Faktor etwa 100, wie ~ r0 erwartet).
   - Vorzeichen und Normierung der Formel sind damit bestaetigt, bis auf den Faktor rho wie verlangt.
2. **Zweites Programm:** bic2 (torch, RK4, h = 0,02, Runde 7) gibt in lauf-69/aus-exakt-002 die Krein-Norm N_K bei
   Normierung n_b = 1.
   - Zwischen omega^2 = 0,79766 (42,8177) und 0,79768 (42,7882) interpoliert auf omega*^2 ergibt sich 42,793.
   - krein.py (scipy, DOP853) gibt 42,7928 bzw. 42,7929 (r0 = 1e-3 bzw. 1e-5): Uebereinstimmung etwa 1e-5.
3. **Abschneideradius:** N haengt nicht von R ab (R = 36 gegen 44: <= 1e-10). Die Moden sind normierbar, das
   Ergebnis haengt also nicht am Rand.
4. **Freies Feld** (S = 0, analytisch, PLAN.md): H_2 - omega Q_2 = 2 rho [(omega + rho) a^2 + (rho - omega) b^2],
   dieselbe Formel.
5. **Nichtrelativistische Grenze:** Fuer omega -> 1 und kleines rho wird N zu ||a||^2 - ||b||^2. Das ist die Form der
   NLS-Krein-Norm. Der Abgleich mit Cuccagna, Pelinovsky, Vougalter (CPAM 58, 2005) ist **[L?]**: Die Quelle war
   hier nicht erreichbar (arXiv ohne Treffer, Verlagsseite 403, Suchbudget der Sitzung erschoepft). Nicht tragend.
6. **Nachlauf:** Die Endfassung krein.py (sha256 f815aa4d...) reproduziert den Standardlauf in allen Feldern
   (jq-Vergleich, 10:27).

## Satz K (streng) und Satz K' (streng, bedingt)

**Satz K'.** Die Linearisierung der NLKG um e^{i omega t} f habe eine reelle Mode
psi = a e^{i rho t} + b e^{-i rho t} mit a, b in H^1(R^3), nicht beide null. Es gelte rho > omega > 0. Dann ist ihre
Energie im mitrotierenden Rahmen positiv:

E_2 = 2 rho int (omega + rho) a^2 + (rho - omega) b^2 d^3x >= 2 rho (rho - omega)(||a||^2 + ||b||^2) > 0.

Die Krein-Signatur ist also positiv.

Beweis:
- E_2 = d^2(H - omega Q) ist die erhaltene Hamiltonfunktion der Linearisierung im mitrotierenden Rahmen (PLAN.md 1).
- Einsetzen der Mode und die Modengleichungen, mit a bzw. b multipliziert und integriert (partielle Integration
  zulaessig fuer H^1-Moden mit Abfall), geben den konstanten Wert 2 rho N; der cos(2 rho t)-Anteil verschwindet.
- Beide Gewichte sind positiv. QED.

Das gilt ebenso fuer den psi_2-Kanal (dp = U', sp = -g J S) und fuer jedes l.

**Satz K (l = 0, n = 1).** Die in BEWEIS-1 bewiesene BIC-Mode hat positive Krein-Signatur.
- Aus dem zertifizierten Kasten (BEWEIS.md 1) folgt
  rho* - omega* >= 1,744617544837398735780754587 - 0,893127531269675502074377802 = 0,851490013567723233706376785 > 0.
- Die Mode ist nichttrivial (B~ -> 1), glatt und faellt samt Ableitungen exponentiell ab (Lemma J, R). Sie liegt also
  in H^1.
- Satz K' gibt E_2 >= 2 rho* 0,85149 ||Psi||^2 > 0. Streng.
- Fuer die Einheitsnorm gilt zudem die strenge Einschliessung 2,971 <= K <= 9,204 (Gewichtsgrenzen).
- Der Zahlenwert 3,00871 ist numerisch. Eine Kugelhuelle des Werts selbst ist nicht noetig und nicht gerechnet.

## Bedeutung (Einordnung; physikalische Folgerungen als Hypothese, wo nicht bewiesen)

- **Linear, bewiesen fuer n = 1 und bedingt fuer alle:** Positive Signatur heisst, dass eine Stoerung der Stelle die
  eingebettete Mode nicht in eine oszillatorische Instabilitaet treibt. Das Kontinuum des offenen Kanals hat fuer
  rho > 0 ebenfalls positive Energie ((omega + rho) rho > 0).
  - Mit der Flussidentitaet aus bic2 (Gamma = J/(2 N_K), J >= 0 auslaufender Fluss) folgt: Neben der Stelle werden
    die Moden zu Resonanzen mit Gamma >= 0. Sie klingen ab und wachsen nicht.
  - Das passt zum Befund "Resonanz auf beiden Seiten" (N7 in L4-BIC-LITERATUR.md).
- **Nichtlinear (Hypothese, [L?] fuer die Literaturaussage):** Eine Mode positiver Energie verliert beim Abstrahlen
  Amplitude. Codex' Abstrahlung in der zweiten Harmonischen (~ epsilon^4) daempft also; sie waechst nicht an. Ein
  Aufbrechen in komplexe Paare (Mechanismus negativer Energie) ist fuer diese Stellen ausgeschlossen, soweit er
  negative Signatur braucht.
- **l = 1 ("dunkler Leuchtturm") und l = 2:** Alle m-Komponenten haben dieselbe Radialfunktion und dieselbe
  (positive) Signatur. Die quadratische Dynamik auf dem entarteten Unterraum ist rho mal eine positiv definite Form.
  Die notwendige Bedingung fuer eine U(3)- bzw. U(5)-Symmetrie ist damit erfuellt; hinreichend ist sie nicht.
- **Wo negative Energie moeglich waere:** nur bei 0 < rho < omega und ueberwiegendem b-Anteil, genauer bei
  ||a||^2/(||a||^2 + ||b||^2) < (omega - rho)/(2 omega). Keine der stillen Stellen liegt dort.

## Laeufe und Dateien (Spur cpu5, kleintest.sh, gemessen)

| Lauf | Zweck | Ergebnis | Laufzeit |
|---|---|---|---|
| krein1 (08:22:53 UTC) | erster Versuch | Abbruch: leere Teilmenge im Profil-Auswerter (Fehler behoben) | 3,6 s |
| krein2 (08:23:19 UTC) | alle Stellen, r0 = 1e-3 | Tabelle oben | 45,4 s |
| krein3 (08:24:51 UTC) | l = 0 und Z1 mit r0 = 1e-5 | Gegenprobe <= 5e-7 | 19,5 s |
| krein4 (Nachlauf, Endfassung) | Reproduktion krein2 | alle Felder gleich | 45,5 s |

sha256:
- PLAN.md 8a983839d6602e839f17b92be37353743c9c5b9dffb9158e55f56d28a10dee33
- krein.py f815aa4dbf1b121692d782a5ed2d7c1b52ec2046f527aa3cb5e03a2beb484305
- laeufe/KREIN-ERGEBNIS.json 0441f068f0502e5af9c171b8907b361ca56f36a3a98d3ece75c03fb1b1c8087f
- laeufe/KREIN-ERGEBNIS-r0-1e-05.json 7a81df634e3049629907761804f0b5e6a5c33d9034a05bffab681e4f83d342fb
- Logs laeufe/LAUF-krein1..3.log, laeufe/LAUF-krein4-nachlauf.log (Hashes in SHA256SUMS.txt)

Vermerk zu den Regeln: Beim Anlegen des Ordners auf der .69 habe ich einmal `python -c 1` direkt aufgerufen, nicht ueber
kleintest.sh. Das war nur die Pruefung, ob die venv vorhanden ist, ohne Rechnung. Alle Rechnungen liefen ueber
kleintest.sh. Lokal kein python, kein awk.

## Einfach gesagt

Eine Schwingung kann man sich wie eine Kugel in einer Mulde (positive Energie) oder auf einem Huegel (negative Energie)
vorstellen. Im ersten Fall laeuft sie beim Abgeben von Energie ruhig aus, im zweiten kann sie sich aufschaukeln. Wir
haben die Energieformel fuer die stillen Schwingungen des Q-Balls sauber hergeleitet und an acht Stellen nachgerechnet:
Ueberall ist die Energie positiv, und fuer die erste Stelle ist das sogar streng bewiesen. Die stillen Schwingungen sind
also gutartig: Wo sie doch etwas abstrahlen, werden sie dabei kleiner, nicht groesser.
