# Runde 6: Die Q-Ball-Resonanz in 3D (Anthropic)

Auftraggeber: claude-primary. Zeit vor dem Schreiben gemessen: 2026-09-30 02:20:54 CEST. Deutsch. Explorativ.

Finn woertlich: "mach das in 3d nach".

## Ausgangslage

- **1D, Codex** (coordination/resonance-20260930/ERGEBNIS.txt):
  - langlebige, ausleckende Resonanz bei rho = 1,49377696 - 6,716e-5 i (omega^2 = 0,7)
  - Die Abklingrate der gespeicherten Ladung trifft 2 Gamma auf 0,13 %.
  - Linear, Abstrahlung nach aussen.
  - Literatur (PDFs in resonance-20260930/papers/): Ciurla u. a. 2405.06591 (dieselbe Potentialfamilie, QNM), Azatov u. a.
    2412.13885, Evslin u. a. 2604.07713, Saffin u. a. 2212.03269.
- **Unsere 1D-Rechnung:** runden-v3/RUNDE-02.md und RUNDE-02/tests1d/ (Stoss- und Streutests; Feinlauf laeuft).
- **Modell:** U = S - S^2 + S^3/2, S = |phi|^2, L = |phi_t|^2 - |grad phi|^2 - U.
- **3D-Grundzustand:** radiales Profil aus RUNDE-02/tests1d/tests1d.py, Test 4, mit Q(omega)-Tabelle in
  RUNDE-02/tests1d/lauf-69/ausgabe/. Q_min = 111,84 bei omega^2 = 0,927; stabil (dQ/domega < 0) fuer omega^2 < 0,927.

## Aufgabe

1. **Lineare Zwei-Kanal-Randwertrechnung in 3D, radial je Drehimpuls l = 0, 1, 2.**
   - Stoerungen phi = [f(r) + u(r) exp(-i rho t) + v*(r) exp(+i rho* t)] exp(-i omega t) Y_lm mit Zentrifugalterm
     l(l+1)/r^2.
   - Gesucht: komplexe Pole rho_l (auslaufender offener Kanal, abklingender geschlossener Kanal) unterhalb bzw. oberhalb der
     Kontinuumskante 1 - omega.
   - Bei omega^2 = 0,7, dazu mindestens zwei weitere omega^2 im stabilen Bereich (etwa 0,6 und 0,8).
   - Kontrollen:
     - l = 1 muss die Translations-Nullmode enthalten (rho = 0 bzw. die Boost-Mode).
     - l = 0 muss die Ladungs- bzw. Phasen-Nullmode enthalten.
     - Negativkontrolle ohne Ball: kein Pol.
     - drei Rand- bzw. Toleranzstufen
2. **Zeitentwicklung radial**, als Gegenprobe zum Pol:
   - l = 0: nichtlineare kugelsymmetrische Zeitentwicklung in r mit kleinem Stoss (schwach und staerker). Spaete Frequenz
     und Abklingrate gegen rho_0.
   - l = 2: linearisierte Zeitentwicklung des l = 2-Kanals mit kleiner Anfangsstoerung. Frequenz und Abklingrate gegen
     rho_2.
   - Das ist die Formschwingung. Vergleiche mit der Rayleigh-Tropfenformel in 3D, omega_2^2 = 8 sigma/(rho R^3) mit
     l(l-1)(l+2) = 8, nur fuer duennwandige Baelle (omega^2 = 0,52 bis 0,55), sigma und Dichte aus dem Profil. Das
     verbindet die Karte mit Wellen 16.
   - Drei Aufloesungen (L3).
3. **Vergleich 1D gegen 3D:** Wandert der Pol, wird er schmaler oder breiter? Gibt es in 3D mehr oder andere Resonanzen?
4. **Vorhersage vorab** (in PLAN.md vor dem Rechnen): Wo erwartest du rho_0, rho_1, rho_2 und warum?

## Rechenort und Abgabe

- Radiale Rechnungen sind billig; CPU reicht. Code mit --geraet cpu oder cuda, float64.
- Aufrufe ueber `cd /home/fmh/fmhc-physics-remote/runde6-3d-resonanz && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
  cpu|cpu2|p4000a <kurzname> <skript> ...`, je hoechstens 10 min.
- Abgabe in RUNDE-06/resonanz3d/:
  - Code
  - PLAN.md: Aufrufe, Laufzeiten, Vorhersagen vorab, Gegenproben, Latten L1 bis L5, "Einfach gesagt"
- Nicht rechnen: Die Leitung startet.
- Codex rechnet parallel und unabhaengig die linearen Pole fuer l = 0 und l = 2 als Zweithaus-Probe; tausche dich nicht
  mit ihm aus.

## Grenzen

- Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik. Der Code bleibt ungetestet; halte ihn einfach und
  gib einen Rauchtest an.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Gesperrt: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
- Literatur: die PDFs in resonance-20260930/papers/ lesen, soweit noetig; Zitate mit Quelle.
- Zeiten mit `date`. Budget hoechstens 90 Minuten.
