# PLAN-NACHTRAG-3 (ZWEIFELD-NACHBAU) - NACHTRAEGLICH

- Verfasst 2026-10-02 12:13:46 CEST (date), nach dem Abbruch von L13, L14 (kand M2 mit W1) und N2-M2 (kand M2 mit W2), vor jedem Lauf
  mit zweifeld_n3.py.
- Befund: Alle vier kand-Laeufe fuer M2 brachen in der Hintergrund-Fortsetzung ab ("Fortsetzung gescheitert" bei
  w^2 = 0,805; 0,815; 0,8236 usw.), sobald Newton unter die unterste Zeile 0,830 lief.
  - Diagnose D1/D2 (cpu3, nicht gewertet): Newton aus der gespeicherten Zeile 0,830 nach 0,829 divergiert; 0,8299
    konvergiert; 0,832 -> 0,831 braucht 9 Iterationen mit Anfangsschritten ~0,8. Ursache: weicher Wandmodus grosser
    Baelle (R_half ~14); Schritte ~1e-3 ohne Praediktor liegen am Rand des Einzugsbereichs.
- Behebung (Programmfehler, Verfahren unveraendert; code/zweifeld_n3.py, Monkeypatch, zweifeld.py und zweifeld_n2.py
  bleiben unveraendert):
  1. Fortsetzung mit Schritt <= 0,0005, Sekanten-Praediktor, bis zu 30 Halbierungen.
  2. Scheitert ein Profil trotzdem, wird nur dieser Punkt NaN (Kandidat dann nicht konvergiert), statt Laufabbruch.
  3. Newton: w^2 auf [0,828; 0,912] (M2) bzw. [0,784; 0,812] (M1) begrenzt.
- Laeufe:
  - N3-W2: kand mit W2 (Nachtrag 2) fuer M2 und M1, beide Stufen (aus/n3w2-kand-*.json).
  - N3-W1: kand mit W1 (eingefrorener Plan) fuer M2, beide Stufen (aus/n3w1-kand-*.json), damit der eingefrorene Plan
    fuer M2 ein Ergebnis hat.
  - Zeilen unveraendert aus L7b/L8b und L9b bis L12b (aus/zeilen-M2-st1-b, -st2-b) und L3/L4.
