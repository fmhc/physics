# PLAN-NACHTRAG-4 (ZWEIFELD-NACHBAU) - NACHTRAEGLICH

- Verfasst 2026-10-02 12:18:01 CEST (date), nach N3-W2 Stufe 1 (aus/n3w2-kand-M2-st1.json), vor jedem Lauf mit zweifeld_n4.py.
- Befund N3-W2 Stufe 1: 9 Vorzeichenwechsel von s (Detektor 1). 4 davon: Newton konvergiert, Umlauf +-1 aufgeloest.
  5 davon: s springt zwischen Nachbarzeilen von ~ -|r_a| auf ~ +|r_a| (|s| ~ 0,7 bis 1 auf beiden Seiten), Newton
  divergiert, Umlauf um den Startpunkt dennoch +-1 aufgeloest (min |W2| ~ 0,6 am Rand).
- Frage: Geht s dort stetig durch 0 (scharfe stille Stelle) oder springt s?
- Verfahren (Lokalisierung entlang der Kurve m_a = 0 statt 2D-Newton; Diagnose):
  - Je Wechselpaar 6 Stufen mit je 9 w^2-Werten in der aktuellen Klammer; je w^2 die Nullstelle von m_a in
    rho_guess -+ 0,0015 (Illinois, 1e-11) und s mit stetig ausgerichtetem eta; neue Klammer = Intervall mit
    Vorzeichenwechsel. Endklammer ~0,002/8^6 = 7,6e-9 in w^2. Lage = lineare Interpolation von s = 0.
  - Dann Umlauf von W2 um die Lage (Halbbreite 1e-3, 16 Punkte je Kante, Sprung < 0,4 rad, hoechstens 40 Runden).
  - Ausgegeben wird s auf jeder Stufe. Geht |s| beim Verfeinern gegen 0 (Wechsel mit kleinen |s| beidseitig), ist die
    Nullstelle stetig. Bleibt |s| auf beiden Seiten gross, springt s: dann keine stille Stelle (verworfen, Grund
    "Sprung von s").
  - Alle 9 Paare, beide Stufen (Paare aus den Zeilen der jeweiligen Stufe).
- Gefunden bleibt: Umlauf +-1 aufgeloest auf beiden Stufen; zusaetzlich (Nachtrag 4) stetiger Nulldurchgang von s;
  K3 mit den Lagen aus diesem Verfahren.
