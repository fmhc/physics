# PLAN-NACHTRAG-2 (nachtraeglich, vor den betroffenen Laeufen eingefroren)

- Geschrieben ab 2026-10-02 09:10:53 CEST (date). Nachtraeglich zum eingefrorenen PLAN (08:47:17) und NACHTRAG-1 (09:01:33).
- Anlass: Lauf 7 (D2 komplett in einem Aufruf) wurde nach 600 s beendet (rc = 1, keine Ausgabe). Kein D2-Ergebnis
  ist bekannt.
- Aenderung: D2 in zwei Aufrufen mit code/d2_phasen_teile.py (Funktionen d2a, d2b, d2c unveraendert aus
  d2_phasen.py kopiert, nur main() teilt auf): Aufruf "ab" (D2a und D2b) und Aufruf "c" (D2c). Parameter, Gitter,
  Zeiten und Klassen wie im PLAN.
- Selbstanzeige: Die Aufteilung von main() wurde lokal mit einem kurzen python3-Textersatz (ohne Rechnung)
  eingefuegt; lokal ist ausser Rauchtests kein python erlaubt. Danach Rauchtest (rauch) lokal.
