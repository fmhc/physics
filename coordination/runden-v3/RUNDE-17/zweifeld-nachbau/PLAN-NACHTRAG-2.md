# PLAN-NACHTRAG-2 (ZWEIFELD-NACHBAU) - NACHTRAEGLICH

- Verfasst 2026-10-02 12:09:25 CEST (date), nach L5/L6 (kand K1 mit W1) und waehrend der M2-Scans, vor jedem Lauf
  mit zweifeld_n2.py. Der eingefrorene Plan bleibt die gewertete Folge; dieser Nachtrag ist Diagnose bzw. Ersatz, ueber
  dessen Geltung die Leitung entscheidet.
- **Befund, der den Nachtrag ausloest (K1 nach eingefrorenem Plan):**
  - Newton auf W1 landet bei w^2 = 0,797676, rho = 1,744617 (beide Stufen), konvergiert aber nicht quadratisch
    (letzter Schritt ~1e-7).
  - Umlauf von W1 um den Startpunkt: 0 auf beiden Stufen (aufgeloest, groesster Sprung 0,38 rad).
  - Erklaerung (Herleitung, nachtraeglich): Bei Isotropie von R ist jede 2x2-Klammer in W1 ein Volumen, also
    W1 = vol(Y_a, Y_b, Z_b, k Z_2 - i Z_1) und k Z_2 - i Z_1 ist eine auslaufende Welle. W1 ist die Jost-Determinante.
    Nahe einer stillen Stelle W1 ~ (rho - rho_r) + i Gamma/2 mit Gamma >= 0 quadratisch: Nullstelle ohne Umlauf.
    Genau davor warnte HERLEITUNG.md von LOG-NACHBAU; mein eingefrorener Plan hat das uebersehen. Selbstanzeige.
  - Auch die Phasenprobe r_m gegen r_m + 4 (~1e-15) ist deshalb schwach: Volumina skalieren unter jeder linearen
    Fortpflanzung mit derselben Determinante.
- **Ersatz W2 (fuer Lokalisierung und Umlauf):**
  - W2 = s~ + i m_a, s~ = det(B^T zeta0 ; Zeile a von G), zeta0 = Einheitsvektor der Spaltenrichtung von B
    (groessere Spalte, groesste Komponente positiv).
  - In Kofaktoren: W2 = zeta0_c c_1 - zeta0_b c_2 + i c_0. Bei zwei Kanaelen (K1): W2 = G_ab + i G_bb, also genau das
    W von LOG-NACHBAU.
  - Auf m_a = 0 ist s~ = (zeta0 . u) (Zeile a . J r) mit B = u r^T, also bis auf einen positiven Faktor die
    Kenngroesse s; nahe dem Mittelpunkt (u ~ zeta0) hat W2 nur an stillen Stellen Nullstellen.
  - Newton: zeta0 je Iteration am aktuellen Punkt; Rechteck: zeta0 fest aus dem Mittelpunkt.
- Unveraendert: Hintergrund, Kanaele, Zeilen, Nullstellen von m_a, s mit gefuehrtem eta, Detektor 1, Rechteck
  (Halbbreite 1e-3, 16 Punkte je Kante, Sprung < 0,4 rad, hoechstens 40 Runden), Kriterien K1, K3, "gefunden".
- Detektor 2 (Zellen-Umlauf von W1) liefert nur noch zusaetzliche Startpunkte, kein Kriterium.
- Laeufe (Code code/zweifeld_n2.py, importiert code/zweifeld.py unveraendert):
  - N2-K1: kand M1 Stufe 1 (cpu3) und Stufe 2 (cpu4) aus den vorhandenen Zeilen von L3/L4.
  - N2-M2: kand M2 Stufe 1 (cpu3) und Stufe 2 (cpu4) aus den Zeilen von L7b/L8b und L9b bis L12b.
  - Ausgaben aus/n2-kand-*.json; nichts wird ueberschrieben.
