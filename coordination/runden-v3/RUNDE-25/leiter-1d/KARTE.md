# LEITER-1D: Gibt es die stille Leiter auch in 1D, nur bei viel kleinerem eps? (Runde 25, aus der Zufallskarte G2-10)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 02:25:15 CEST (date), vor jeder Rechnung.
- **Herkunft:** Zufallskarte R25 = G2-10 (IDEEN-EVOLUTION/GEN-02/G2-10).
  - Dort: "d = 1: keine Stelle auf 0,55 bis 0,70 (ohne Innenbarriere keine Leiter; bekannt: keine Stelle auf 0,55 bis
    0,88)".
  - Die Projekt-Erklaerung (HERKUNFT.md): In 1D fehlt die Innenbarriere.
- **Gegenhypothese der Leitung [H]**, aus WAND-BETA, LEITER-BETA und der blinden Codex-Nachrechnung:
  - Die Leiter entsteht aus der Transmissionsnullstelle der **ebenen** Wand plus Fabry-Perot der Innenwelle. Eine
    Kruemmung ist dafuer nicht noetig.
  - Ein 1D-Q-Ball besteht aus zwei ebenen Waenden um ein Plateau der Laenge L. Also muesste es die Leiter auch in 1D geben.
  - In 1D waechst das Plateau aber nur logarithmisch: L ~ (1/lambda) ln(1/eps).
    - lambda = Rate am Sattel f_c = sqrt(S_c); lambda^2 = 2 S_c U''(S_c) = 2 bei beta = 1/2, also lambda = sqrt2.
  - Aufeinanderfolgende Sprossen (abwechselnde Paritaet) haben Delta L = pi/k_in, also
    Delta ln(1/eps) = lambda pi/k_in(rho_z) = sqrt2 pi/1,92332 = 2,3100.
    - Jede Sprosse liegt etwa 10-mal naeher an omega_min (Faktor e^-2,31 = 0,099).
    - G2-10 suchte nur bis eps = 0,05, also koennen die Sprossen dort fehlen.
  - Da es keine Kruemmung gibt, sollten die Sprossenfrequenzen mit fallendem eps direkt auf rho_z = 1,52414976 zulaufen.
- Projekt-grep (fuenfte Probe) nach "d = 1" in den Leiter-Karten:
  - RUNDE-06 (Bruecke dim 1 bis 3 bei omega^2 = 0,7)
  - RUNDE-07/08 (G2-10, Gegenproben)
  - Nach 1D-Sprossen bei eps < 0,05 hat niemand gesucht.

## Test

- Modell M1, beta = 1/2, 1D, beide Paritaeten (gerade: Y'(0) = 0; ungerade: Y(0) = 0).
- Profil:
  - 1D-Q-Ball bei omega^2 = 1/2 + eps, aus der ersten Integralform oder per ODE vom Umkehrpunkt S0.
  - Der Ausenschwanz ist so weit genau, dass er vernachlaessigbar wird.
- Linearisierung wie in WAND-BETA: A'' = [W - (rho - omega)^2] A + C B, B'' = C A + [W - (rho + omega)^2] B, mit
  W = U' + U'' S und C = U'' S.
- **Verfahren (W-Abbildung):**
  - Aussen rein abklingend im geschlossenen Kanal starten, offener Kanal null, nach innen bis x = 0 integrieren.
  - Paritaetsbedingungen (zwei Komponenten): Eine stille Stelle ist eine gemeinsame Nullstelle in (rho, eps).
  - Je eps die Nullstellenlinie der ersten Komponente in rho verfolgen. Die Vorzeichenwechsel der zweiten Komponente
    entlang eps sind die Sprossen; verfeinern und den Umlauf pruefen.
- eps logarithmisch von 0,05 bis 1e-7. Kontrolle: Bei eps -> 0 muss die Nullstellenlinie gegen rho_z laufen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| L1D-1 | In eps [1e-7; 0,05] gibt es mindestens drei stille Stellen (beide Paritaeten zusammen), mit aufgeloestem Umlauf | 65 % |
| L1D-2 | Die zwei kleinsten-eps-Schritte Delta ln(1/eps) zwischen aufeinanderfolgenden Sprossen liegen innerhalb +-10 % von 2,3100 | 45 % |
| L1D-3 | Die Sprossenfrequenzen laufen mit fallendem eps auf rho_z zu; die Sprosse mit dem kleinsten eps liegt innerhalb 0,005 von 1,52415 | 50 % |

**Bedeutung (vorab):**
- L1D-1 und L1D-2 treffen ein:
  - Die stille Leiter gibt es auch in 1D. Dafuer reicht die ebene Wand mit stehender Innenwelle; eine Kruemmung oder
    "Innenbarriere" ist nicht noetig.
  - In 1D liegen die Sprossen geometrisch dicht (Faktor ~0,1 in eps) [H].
  - Die Projekt-Erklaerung "ohne Innenbarriere keine Leiter" (G2-10) ist dann ueberholt.
- L1D-1 trifft nicht ein: Die ebene Wand allein reicht in 1D nicht, oder die Stellen sind numerisch unzugaenglich.
  Beschreiben, mit Belegen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min, 4 GB).
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf vorher erlaubt, mit Parametern, die in keinem echten Lauf
  vorkommen.
- Zeitbox 120 min.
