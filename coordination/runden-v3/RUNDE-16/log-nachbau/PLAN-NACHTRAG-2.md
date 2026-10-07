# PLAN-NACHTRAG-2 (LOG-NACHBAU, Runde 16), NACHTRAEGLICH

- Verfasst: 2026-10-02 ab 08:23:41 CEST (date), nach den Hauptlaeufen und nach Nachtrag 1. Ob er gilt, entscheidet die
  Leitung.
- Anlass:
  - Die Hauptabtastung liess an beiden Fenstergrenzen je 0,002 in rho aus (PLAN.md, Abschnitt 4).
  - Die Karte verlangt je Zeile alle Nullstellen der geschlossenen Bedingung im Fenster. Der untere Ast der
    geschlossenen Bedingung tritt erst bei w^2 = 0,885 in die Abtastung ein, vorher liegt er vermutlich im Streifen.
- Folgelauf F3 (nachtraeglich), fuer dieselben 57 Zeilen w^2 = 0,700 bis 0,980, beide Stufen, Code stille_n2.py
  (= stille.py plus Schalter fuer die Streifen):
  - Unterer Streifen: rho von 1 - w + 1e-5 bis 1 - w + 0,0025, 101 Punkte gleichabstaendig.
  - Oberer Streifen: rho von 1 + w - 0,0025 bis 1 + w - 1e-5, 101 Punkte.
  - Je Streifen und Zeile dieselbe Auswertung wie im Hauptlauf: Nullstellen von G_b (Illinois), s, beide Detektoren.
    Gepaart wird nur innerhalb desselben Streifens.
  - Fuer Kandidaten: Newton und Rechteck wie im Hauptplan, mit 24 Halbierungsrunden wie Nachtrag 1.
- Auswertung:
  - Gleiche Regel wie PLAN.md Abschnitt 6.
  - Getrennt als nachtraeglich berichtet. Der Hauptbefund wird nicht ersetzt.
  - Ein Treffer im Streifen waere ein zusaetzlicher Kandidat. Kein Treffer schliesst nur Stellen mit Vorzeichenwechsel
    von s zwischen den Zeilen aus, nicht beruehrende Nullstellen.
