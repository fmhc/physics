# Runde 9, Karte SD-1: Gegen-Schwappen (Spin-Dipol) im gemischten Ball (Plan und Erwartung vor dem Rechnen)

- Bearbeiter: Anthropic-Code-Agent (Opus), Folgeauftrag der Leitung vom 2026-09-30 08:16. Explorativ, v3.
- Beginn 2026-09-30 08:16:07 CEST (date). Diese Datei begonnen 2026-09-30 08:22:10 CEST (date), **vor jeder
  Code-Aenderung und vor jedem Lauf**.
- **Blindheit:** RUNDE-09/sd1/VORHERSAGEN-SD1.md nicht geoeffnet. Gelesen: RUNDE-08/gf-bic/ERGEBNIS.md (R8 und R9),
  gfbic.py, gfbic_umlauf.py, die Koepfe von gfbic_anti.py und gfbic_rot.py, der R9-Bericht zu Z1, dazu meine SP-1-Ergebnisse.
- **Reihenfolge laut Leitung:** erst Code und l = 0-Probe. **Kein l = 1-Lauf im psi_2-Kanal vor der Freigabe**, auch
  kein Rauchtest. Die l-Verdrahtung pruefe ich deshalb im psi_1-Kanal gegen SP-1.
- Neue Deutungen sind Hypothesen **[H]**; Zahlen mit **[Hand]** sind von Hand gerechnet.

## 1. Frage und Gleichungen

psi_2 = e^{-i omega t} (u e^{-i nu t} + v^* e^{i nu^* t}) Y_lm um den einkomponentigen Ball psi_1 = f e^{-i omega t}.
Reduziert (A = r u, B = r v, c = l (l + 1)):

- A'' = [U'(S) + c/r^2 - (omega + nu)^2] A + sp B
- B'' = sp A + [U'(S) + c/r^2 - (omega - nu)^2] B
- sp = -g J S. Der Paarterm erhaelt l, weil psi_1^2 kugelsymmetrisch ist.

**Die gegenlaeufige Mode je l [Hand]:**

- Bei g = 0 hat Kanal b einen gebundenen Zustand phi_n^(l) von L_0^(l) = -d^2/dr^2 + c/r^2 + U'(f^2) mit Eigenwert
  E_n^(l) < 1. Er sitzt eingebettet bei nu = omega + sqrt(E), gegenlaeufig psi_2 ~ phi e^{+i sqrt(E) t}.
- l = 0: E_0 = omega^2 (phi = r f), also nu = 2 omega. Das ist der Gegenlaeufer der zweiten Leiter.
- l = 1: E_0^(1) > omega^2, also nu = omega + sqrt(E_0^(1)) im Fenster (2 omega, 1 + omega).
- Bei g != 0 strahlt die Mode in Kanal a mit k^2 = (2 omega + sqrt(E))^2 - 1. Die Breite ist ~ g^2 I_l^2 mit
  I_l = int Phi_l S phi dr (Phi_l regulaere Streuloesung zu l). Stille Stellen liegen dort, wo I_l = 0 ist; bei
  endlichem g werden daraus Kurven in der Ebene (omega^2, g), wie Z1 bis Z3 fuer l = 0.
- Die mitlaeufige Mode (nu = sqrt(E) - omega) liegt unter 1 - omega und ist fuer l = 1 bei kleinem g nicht mit einem
  Partner entartet. Anders als die l = 0-Nullmode wird sie deshalb nicht instabil [Hand].

**Bezug zum gemischten Ball [Hand]:**

- Bei g = 0 ist der gemischte Ball eine U(2)-Drehung des einkomponentigen. Sein Gegentakt (psi_1 - psi_2) ist dann
  genau der psi_2-Kanal.
- Bei g != 0 weichen beide ab. Der Gegentakt hat dp = U' + g J S, sp = -g J S/2 und das native Profil (gfbic_anti.py).
- Der Auftrag nennt den psi_2-Kanal; den Gegentakt baue ich als Option "anti" mit ein, ungeprueft.

## 2. Code

- Neuer Ordner auf der .69: /home/fmh/fmhc-physics-remote/runde9-sd1/. Kopien (unveraendert): bic2.py (Version 3),
  gfbic.py, resonanz3d.py.
- Neu: sd1.py, eine Kopie von gfbic_umlauf.py (Fassung 2), erweitert um:
  - --l fuer punkt (Umlauf nach dem R9-Verfahren): nu = l + 1 an allen Stellen, die bisher 1.0 hatten
  - kurve und exakt: die Verfahren aus bic2.py Version 3 (mit l), aber mit den Koeffizienten des gewaehlten Kanals
    (--kanal psi2 | psi1 | sym | anti) und dem passenden Profil
  - Optionen fuer freie Punkte (--dnu, --kanal)
- Fuer l = 0 bleibt der Rechenweg von punkt gleich (nu = 0 + 1.0 = 1.0).
- Die Originale in RUNDE-08/gf-bic und runde8-gfbic / runde9-gfbic2 bleiben unberuehrt. Lokal liegt nur sd1.py in
  RUNDE-09/sd1/; die Importe greifen lokal auf die Originale (nur lesend).

## 3. Proben (vor der Freigabe)

- **Q0 (l = 0, punkt):** Z1 mit den R9-Argumenten (g = 0,2, h = 0,02). Soll: Bericht wie R9 (0,711372264 / Umlauf -1 /
  -1), bitgleich bis auf Zeiten und Pfade.
- **Q1 (l = 0, exakt-psi2):** Z2 bei g = 0,2, h = 0,02. Soll: 0,645862 +- 2e-6, Umlauf +1 auf beiden Rechtecken.
- **Q2 (l = 0, kurve-psi2):** g = 0,2, 0,63 bis 0,73, h = 0,02. Soll: Vorzeichenwechsel bei 0,64586 und 0,71137 (je
  +- 2e-5).
- **Q3 (l-Verdrahtung, psi_1-Kanal):** kurve --kanal psi1 --l 1 bei 0,72 und 0,75 (h = 0,01). Soll: SP-1-P1-Pole
  (1,7855450099 - 1,698e-3 i; 1,8210850747 - 2,037e-5 i) auf 1e-10.

## 4. Erwartung vor dem Rechnen (eigene Schaetzung, vor jedem Lauf)

Grundlage [Hand]:

- Aus R8 (1.2): E_1^(0) = 0,91080 bei 0,601422 und 0,81032 bei 0,582417. Mit t = omega^2 - 0,5 ist
  E_1^(0) - omega^2 ~ c t^2 mit c = 30 bis 34 (Duennwand).
- Kugeltopf-Verhaeltnis (E^(l=1) - E_0)/(E_1^(l=0) - E_0) = (4,493^2 - pi^2)/(4 pi^2 - pi^2) = 0,35; weicher Topf bis
  0,5. Also E_0^(1) ~ omega^2 + (11 bis 16) t^2.
- E_0^(1) = 1 bei t = 0,148 bis 0,173, also omega^2 = 0,65 bis 0,67.

**Erwartungen:**

- **E1 Existenz:** Die gegenlaeufige l = 1-Mode liegt nur unterhalb x_c = 0,66 +- 0,04 im Einkanal-Fenster. Darueber
  gibt es in (1 - omega, 1 + omega) keinen l = 1-Kandidaten dieser Art und keine stille Stelle. 70 %.
- **E2 stille Stellen:** Unterhalb x_c hat die Breite der Mode Nullstellen mit Umlauf +-1: 75 %.
  - Lage in fuehrender Ordnung: die l = 0-Nullstellen des psi_2-Kanals (R8 3.2: u = 1/(x - 0,5) = 6,864 / 9,041 /
    11,30), jeweils um +0,5 bis +1,2 in u verschoben. Das ist der Versatz l = 1 gegen l = 0 aus SP-1.
  - Gegenlaeufige Effekte, darum weiter gefasst: +0,5 durch die Phase l pi/2 der Kugelwelle, aber etwa -0,6 durch das
    groessere k (2 omega + sqrt(E) > 3 omega). Deshalb Fenster -0,3 bis +1,3 in u:
    - u = 6,6 bis 8,2 (x = 0,622 bis 0,652)
    - u = 8,7 bis 10,3 (x = 0,597 bis 0,614)
    - u = 11,0 bis 12,6 (x = 0,579 bis 0,591)
  - Eine Stelle bei u ~ 5,3 bis 6,0 (x = 0,667 bis 0,689) gibt es nur, wenn x_c hoeher liegt als geschaetzt: 35 %.
- **E3:** Die Umlaufzahlen wechseln entlang der Leiter das Vorzeichen. Der Schritt in u ist 2,0 bis 2,4.
- **E4:** Die Breite der l = 1-Mode bei g = 0,2 liegt abseits der Nullstellen bei 1e-6 bis 3e-5, wie beim
  l = 0-Gegenlaeufer.
- **E5 (Proben):** Q0 bitgleich (95 %); Q1, Q2 in den Toleranzen oben (90 %); Q3 auf 1e-10 (90 %).

## 5. Belegstufen (wie SP-1)

- **exakt (Umlauf):** +-1 auf einem Rechteck um die Stelle, groesster Phasensprung < 0,4 rad. Numerische Evidenz im
  radialen linearen Modell, kein Beweis.
- **Vorzeichenwechsel:** Wechsel von s in kurve mit Feinverfahren. Das Grobraster-Vorzeichen gilt nur bei |s| > 1e-4
  (Lehre aus SP-1).
- **Minimum:** nur kleine Breite. "Nicht gesehen" statt "gibt es nicht".

## Nachtrag 2026-09-30 08:34:33 CEST (date), nach der Freigabe der Leitung (08:28:19)

- Nach der Freigabe gelesen: VORHERSAGEN-SD1.md.eingefroren-20260930-082819. Die Datei entstand ab 08:25:55, also nach
  diesem Plan (08:22:10 bis 08:22:50, mtime 08:22:50). Meine Erwartungen in Abschnitt 4 bleiben unveraendert.
- **Gerechneter Ast:** wie in der Freigabe der Gegentakt des gemischten Balls (Kanal "anti": dp = U'(S) + g S,
  sp = -g S/2, natives Profil), gegenlaeufiger l = 1-Partner bei nu ~ omega + sqrt(E).
- Meine Erwartungen E1 bis E4 (08:22) galten dem psi_2-Kanal um den einkomponentigen Ball (dp = U'(S), ohne g S). Fuer
  "anti" hatte ich vorab keine eigene Lage festgelegt. E1 bis E4 werte ich deshalb nur, soweit psi_2 mit l = 1 gerechnet
  wird; sonst stehen sie als "nicht geprueft" im Ergebnis.
- Rauchtest (lokal, h = 0,08, 08:31:32 bis 08:32:15, lauf-lokal/aus-rauch-anti-l1-*): Die Zahlen sind keine Messung und
  stehen hier nur, weil ich sie vor den .69-Laeufen gesehen habe. Gebundener l = 1-Zustand bei 0,52 / 0,54 / 0,60 mit
  E = 0,774 / 0,802 / 0,896; Gegenlaeufer-Pol bei 0,60 mit Gamma 3,8e-7.
- Der Newton-Test aus nu - 1e-5 i fuer gebundene Zustaende taugt nicht: Unter der Kante waehlt jost_start fuer
  Im nu != 0 den anderen Zweig von q. Ich melde deshalb nur die reellen Nullstellen von D; D ist auf der reellen Achse
  reell.
