# KUGELSCHALE-1: Ergebnis (Leitung, Runde 23, explorativ)

- Gerechnet von der Leitung auf der .69 (kleintest.sh, cpu3), 22:11 bis 22:12 CEST, rc = 0 (n = 8: 10 s; n = 12: 29 s).
- Karte und Plan: KARTE.md; eingefroren 22:11:30 (PLAN.md.eingefroren-20261002-221130). Code: code/kugelschale.py.
- Rohdaten in aus/ (auf der .69).

## Ergebnis zuerst

1. **Die Dreieckskugel geht mit wachsendem Kraefteverhaeltnis gamma (Dehnen gegen Biegen) von "rund" zu "Ikosaeder mit 12
   Spitzen" ueber.** Beide Groessen (642 und 1442 Ecken) liegen gegen gamma fast deckungsgleich; gamma ist also die richtige
   Steuergroesse.
2. **Biegesteif (kleines gamma):** Die 12 Fuenfer-Ecken liegen leicht eingedellt (0,8 % unter dem mittleren Radius).
   - Bei gamma ~ 70 bis 90 ist die Kugel am rundesten (A ~ 2e-7). Dort klappen die Fuenfer-Ecken von innen nach aussen.
3. **Darueber treten die Fuenfer-Ecken als Spitzen heraus:** +0,7 % bei gamma = 150, +2,7 % bei 300, +5,3 % bei 500, +9,4 %
   bei 1000, +14 % bei 4000. Die Asphaerizitaet steigt von gamma = 50 bis 500 um das ~500-Fache und saettigt ab ~2000 bei
   ~1,5e-3. Literatur (L?): Uebergang um gamma ~ 154, Viruskapside.
4. **Energieaufteilung:** Der Dehnanteil steigt von 4 % (gamma = 10) auf ein Maximum von ~43 % bei gamma ~ 300. Danach faellt
   er wieder (13 % bei 2000, 6 % bei 4000): Das Knicken an den Spitzen baut Dehnung ab und legt die Energie in Biegung an den
   12 Ecken.
5. **Euler-Probe:** V - E + F = 2, genau 12 Fuenfer-Ecken in jeder Groesse.

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang |
|---|---|---|
| K1 | A(500)/A(50) >= 10 (70 %) | **eingetroffen**: ~540 (n = 8), ~600 (n = 12), log-log interpoliert |
| K2 | Steilster Anstieg von log A zwischen gamma 80 und 300 (55 %) | **eingetroffen formal**: steilste Stelle 70 -> 100 (Mitte 84), bei beiden n. Sie entsteht aber am Umklappen der Fuenfer-Ecken (A fast null), nicht an der Facettierung selbst |
| K3 | Oberhalb der K2-Stelle Spitzen > 1,02 (75 %) | **nicht eingetroffen (streng)**: bei 100, 150 und 200 nur +0,1 / +0,7 / +1,4 %; ab gamma = 300 ueber 1,02 |
| K4 | Dehnanteil < 50 % oberhalb (60 %) | **eingetroffen, aber nicht trennscharf**: Er liegt ueberall unter 50 % (Hoechstwert 43 %), wie im Plan vermerkt |

- **Bedeutung (vorab festgelegt):** Der Fall "K1 bis K3" ist nicht ausgeloest, weil K3 streng verfehlt ist.
- **Beschreibend:** Der Uebergang ist ein sanfter Wechsel, keine Kante. Die Fuenfer-Ecken klappen bei gamma ~ 85 nach aussen;
  Spitzen ueber 2 % gibt es ab gamma ~ 300, ab ~2000 ist die Kugel ein facettiertes Ikosaeder. Das ist bekannte
  Schalenphysik [L?, Lidmar/Mirny/Nelson 2003], hier nachgerechnet (L4).

## Latten

- L1: ja
- L2: teilweise (zwei Groessen, Euler-Probe)
- L3: ja (n = 8 und 12 deckungsgleich)
- L4: ja (bekannt)
- L5: nein

## Selbstanzeigen

- Im Rauchlauf (n = 4) waren K1 und K3 schon angedeutet (gesehen, offengelegt).
- K2 und K3 waren mit "Uebergang" als scharfer Stelle formuliert. Der Wechsel ist aber sanft, und die steilste log-Steigung
  sitzt am Nulldurchgang der Spitzenlage; das ist eine Formulierungsschwaeche der Karte.

## Einfach gesagt

Eine Kugel aus Dreiecken ist immer verspannt, und die Spannung sitzt an genau 12 Ecken. Ist die Kugel klein oder steif,
druecken sich diese Ecken sogar leicht ein. Wird sie groesser oder weicher, klappen sie nach aussen und werden zu Spitzen,
bis die Kugel aussieht wie ein Ikosaeder, so wie viele Viren. Was passiert, entscheidet ein einziges Kraefteverhaeltnis:
wie schwer sich die Flaeche dehnen gegenueber biegen laesst.
