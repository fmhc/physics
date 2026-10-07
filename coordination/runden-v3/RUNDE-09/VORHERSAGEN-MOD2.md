# Blinde Modell-Vorhersagen MOD-2: Atmungsleiter l = 0, beta = 0,5, Stellen n = 10 bis 15

- Auftrag der Leitung 08:28:19. **Erste date-Messung dieser Karte: 2026-09-30 08:32:44 CEST.** Die Handrechnung davor lief
  ohne Zeitmessung. Ende: letzte Zeile.
- Bearbeiter: Anthropic-Agent (Opus), MOD-1 fortgesetzt. Nur Hand; kein Interpreter, keine Laeufe.
- **Blindheit:**
  - Nicht geoeffnet: RUNDE-09.md, Ordner aus-pole-dw-n1* (lokal und .69), alles zur Atmungsleiter nach 08:11:43.
  - Datengrundlage sind nur die Werte in meiner RUNDE-09/MODELL-DUENNWAND.md (Ende 08:11:43): omega*^2, Re rho*,
    theta_mess und c bei n = 5, 7, 8, 9 aus Tabelle M.4 und dem Abschnitt "Einschraenkung".
  - n = 6 lasse ich weg; dort ist die Lage ein nicht konvergierter Kandidat, theta weicht um 0,003 ab.

## 1. Modell (aus MODELL-DUENNWAND.md, M.3)

    Psi = k_c(omega, rho) R_tw(omega) = pi (n + theta(epsilon)),     epsilon = omega^2 - 0,5,   R_tw = 0,707107/epsilon
    k_c^2 = omega^2 + rho^2 - 1,5 + sqrt(4 omega^2 rho^2 + 1),         Re rho = omega + c(epsilon)

**Wandphase theta(epsilon), nur n >= 5 (Duennwandbereich):**
- Linearer Fit (Kruemmungsterm ~ 1/R ~ epsilon) an n = 5, 7, 8, 9:

      theta = 0,657643 + 0,334145 epsilon

- Reste: +2e-5 / -6e-5 / -2e-5 / +5e-5 (n = 5 / 7 / 8 / 9).

**Re rho ueber c = Re rho* - omega* (ohne neue Messung).** Zwei Fits an denselben vier Stellen (c = 0,8481 / 0,8417 /
0,8394 / 0,8374 bei epsilon = 0,0824 / 0,0599 / 0,0526 / 0,0470):
- linear: c = 0,823591 + 0,298618 epsilon (Reste <= 2e-4)
- Wurzel: c = 0,804533 + 0,151818 sqrt(epsilon) (Reste <= 5e-5)
  - Die Schritte in c werden zur duennen Wand hin steiler (0,28 / 0,32 / 0,36 je Einheit epsilon). Das spricht fuer eine
    konkave Form.
  - Der Grenzwert 0,8045 liegt nahe am nackten Wandzustand c_w = 0,7993 (MODELL, M.2 c).
- Angesetzt ist der **Mittelwert beider Fits**. Die halbe Spreizung dient als 1 sigma: 2e-4 bei n = 10, 1e-3 bei n = 15.

**Loesung:** Fuer jedes n habe ich 1/epsilon = 4,442883 (n + theta)/k_c(epsilon) von Hand iteriert, bis der Rest unter
1e-6 in omega^2 lag.
- Stichproben der Endwerte: n = 12 gibt Psi/pi = 12,66933 gegen das Ziel 12,66949 (Rest 5e-7 in omega^2). Bei n = 15 ist
  der Rest 2e-8.

## 2. Vorhersagen

| n | omega*^2 | Balken (~2 sigma) | 1/(omega*^2 - 0,5) | Schritt | Re rho* | Balken | Umlauf (bic2-Konvention) |
|---|---|---|---|---|---|---|---|
| 10 | **0,542382** | +-2e-5 | 23,595 | 2,296 (von n = 9) | 1,57248 | +-5e-4 | +1 |
| 11 | **0,538619** | +-2,5e-5 | 25,894 | 2,299 | 1,56865 | +-6e-4 | -1 |
| 12 | **0,535468** | +-3e-5 | 28,194 | 2,300 | 1,56541 | +-8e-4 | +1 |
| 13 | **0,532792** | +-3,5e-5 | 30,495 | 2,302 | 1,56263 | +-1e-3 | -1 |
| 14 | **0,530490** | +-4e-5 | 32,798 | 2,302 | 1,56022 | +-1,2e-3 | +1 |
| 15 | **0,528489** | +-5e-5 | 35,101 | 2,304 | 1,55810 | +-1,5e-3 | -1 |

**Fehlerbalken, Herkunft (Hand):**
- **Wandphase:**
  - Die Lagen bei n = 7 bis 9 stammen aus je drei Polen, linear interpoliert. Das ergibt je etwa +-1e-5 in omega^2, also
    +-0,0015 bis 0,002 in theta.
  - Eine quadratische statt lineare Interpolation verschiebt theta um bis zu 0,002. Gerechnet ist das mit Werten, die ich
    vor 08:11:43 notiert hatte; sie stehen nicht in MODELL-DUENNWAND.md und gehen deshalb nur in den Balken ein.
  - In omega^2: 6e-6 bei n = 10, 3e-6 bei n = 15.
- **c:** Die halbe Spreizung linear gegen Wurzel gibt 5e-6 bei n = 10 und 1,6e-5 bei n = 15 in omega^2
  (Delta x ~ epsilon (dk_c/drho) Delta c/k_c, dk_c/drho ~ 1,12).
- **Nicht im Balken:**
  - ein epsilon^2-Glied in theta (bei epsilon ~ 0,03 hoechstens ~5e-4 in theta, also ~1,5e-6 in omega^2)
  - ein Versagen der Duennwand-Phasenbedingung selbst. Dagegen spricht nur der Verlauf n = 5 bis 9.
- Die Balken sind etwa 2 sigma, auf halbe Einheiten gerundet.

**Probe auf Selbstkonsistenz:**
- Die Schritte in 1/(omega*^2 - 0,5) wachsen langsam von 2,296 auf 2,304.
- Der Grenzschritt des Modells mit Niveauverschiebung war 2,298 (MODELL, M.4). Die Folge laeuft also sauber auf den
  Grenzwert zu.

## 3. Was die Vorhersage widerlegt

1. **Lage:** Eine gemessene Stelle liegt mehr als 3 Balken daneben: 6e-5 bei n = 10 bis 1,5e-4 bei n = 15. Dann ist die
   Extrapolation der Phasenbedingung widerlegt.
   - Liegen alle Stellen systematisch auf einer Seite, trifft es die Form von theta(epsilon) oder c(epsilon), nicht die
     Periode.
   - **Vergleichsgrundlage:** Gemeint ist die echte Nullstelle, nicht ein Rasterminimum. Mit einem Polraster von 6e-4 ist
     die Lage nur auf etwa +-1e-5 bis +-3e-5 bestimmt, wenn man wie bei n = 7 bis 9 die signierte Wurzel interpoliert.
2. **Periode:** Ein Schritt ausserhalb 2,25 bis 2,35 in 1/(omega^2 - 0,5) widerlegt die Periode pi in k_c R_tw.
3. **Paritaet:** Zwei aufgeloeste Nachbarn mit gleicher Umlaufzahl.
4. **Re rho:** Mehr als 3 Balken Abweichung trifft nur die c-Hochrechnung, nicht die Nullstellenregel.

## 4. Einfach gesagt

Unsere Duennwand-Formel sagt, bei welchen Groessen ein grosser Q-Ball ohne Abstrahlung atmen kann. Wir haben sie jetzt
sechs Sprossen weiter oben auf der Leiter angewandt, wo noch niemand nachgesehen hat, von n = 10 bis n = 15. Die Formel
legt sich auf wenige Hunderttausendstel fest; die Abstaende der Sprossen sollen dabei fast gleich bleiben und langsam
auf einen festen Wert zulaufen. Liegen die gerechneten Stellen so nah, ist die Formel ein echtes Werkzeug fuer grosse
Baelle. Liegen sie deutlich daneben, stimmt etwas an der Wandphase oder am Wandzustand nicht.


**Ende: 2026-09-30 08:33:26 CEST (date, nach dem Schreiben gemessen).** Danach keine Aenderungen mehr an dieser Datei.
