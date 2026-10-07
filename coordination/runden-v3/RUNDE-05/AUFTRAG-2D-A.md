# Runde 5, Paket 2D-A (Zelle): Bio 5/29, 7, 23, 24, 28, 49 und Chemie 12 (Anthropic)

Auftraggeber: claude-primary. Zeit vor dem Schreiben: siehe Arbeitsfeld 30.09. 02:09 CEST. Deutsch. Explorativ, leicht.

## Rahmen

- Lies coordination/runden-v3/README.md, RUNDE-05.md und die Ideen in RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md (Nr. 5, 7, 23,
  24, 28, 29, 49) und RUNDE-03/IDEEN-20-QBALL-CHEMIE.md (Nr. 12).
- **Code-Grundlage:** RUNDE-03/tests2d-r3/tests2d_r3.py (2D, spektraler Laplace, radiales Schiessen m = 0 und m = 1).
  - Er ist ungetestet; sein Rauchtest laeuft gerade auf der .69. Uebernimm Schiessen, Laplace und Integrator in deine
    eigene Datei und aendere so wenig wie moeglich.
  - Ergebnisse des Rauchtests stehen spaeter in /home/fmh/fmhc-physics-remote/r3-tests2d-20260930/ (nur lesbar fuer die
    Leitung; du rechnest nicht).
- **Wichtig, aus dem Fable-Review** (runden-v3/REVIEW-FABLE-20260930/REVIEW-FABLE.md, Z. 39-45):
  - Ein duennes, ruhiges Hintergrundmedium gibt es im Ein-Feld-Modell nicht. Der homogene Hintergrund ist fuer
    0 < S < 2/3 modulationsinstabil und erst ab S > 2/3 stabil, dort so dicht wie das Ballinnere.
  - Karten, die ein Medium oder ein "Ladungsbad" brauchen (Bio 28 Zufluss, Bio 49 Bad), baust du ohne Bad. Nimm etwa
    einen einlaufenden Ring aus Wellenpaketen oder eine Verschmelzung mit einem zweiten Ball als "Futter", oder markiere
    die Karte als "im Ein-Feld-Modell nicht umsetzbar" mit einem Satz Grund.

## Karten (je hoechstens 10 min auf einer Quadro P4000, zusammen moeglichst unter 30 min)

1. **Bio 5/29, Teilung und Vererbung:** drehender Ball m = 2 mit kleiner Stoerung. Teilt er sich? Wenn ja: welche
   Windungen haben die Toechter (m = 1 + 1)? Gegenprobe: m = 1 ohne Teilung.
2. **Bio 7, Q-Schale:** Ringprofil (Hohlball) ohne und mit Windung. Zerfaellt er, und wie schnell?
3. **Bio 23, Polaritaet:** Ball in einem schwachen Potentialgradienten V(x) |psi|^2 (kein Hintergrund). Dipolmoment der
   Ladungsdichte, Verformung. Gegenprobe: ohne Gradient.
4. **Bio 24, Vielzeller:** drei bzw. vier Baelle in Dreieck- bzw. Quadratanordnung mit Phasenmustern (alle gleich,
   wechselnd, Windung 2 pi/N). Zusammenhalt, Verschmelzen oder Auseinanderlaufen?
5. **Bio 28, Groessengrenze:** m = 1-Ball, dem durch ein oder zwei gleichphasige Nachbarbaelle Ladung zugefuehrt wird.
   Wird er ab einer Groesse instabil?
6. **Bio 49, Selbstreplikation:** nur, wenn Karte 1 eine Teilung zeigt: Waechst eine Tochter durch Verschmelzen wieder zu
   m = 2 und teilt sich erneut? Sonst "nicht pruefbar ohne Teilung".
7. **Chemie 12, Phasendiagramm:** 2D-Box mit zufaelligem Anfangsfeld bei 3 mittleren Dichten x 3 Rauschenergien. Endzustand
   als Gas (Wellen), Tropfen oder Kondensat klassifizieren; Kriterien vorab festlegen.

## Abgabe (Ordner RUNDE-05/r5-2d-a/)

- Code (CUDA, float64, Unterbefehle, Rauchtest)
- PLAN.md:
  - Aufrufe ueber `cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
    <spur> <kurzname> <skript> ...`
  - Laufzeit je Aufruf auf der P4000 (GPU-Speicher hoechstens 1,5 GB)
  - Vorhersagen vor dem Rechnen, Gegenproben, Aufloesungsvergleich (L3)
  - Latten L1 bis L5, "Einfach gesagt"
- Nicht rechnen: Die Leitung startet.

## Grenzen

- Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik. Der Code bleibt ungetestet; halte ihn einfach.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Gesperrt: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
- Zeiten mit `date`. Budget hoechstens 90 Minuten.
