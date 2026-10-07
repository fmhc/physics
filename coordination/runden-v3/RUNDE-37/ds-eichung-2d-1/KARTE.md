# DS-EICHUNG-2D-1: Misst unser Dimensionswerkzeug aus NETZ-DYN-1 auf 2D-Zufallskarten mit bekannter Antwort richtig? (schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-07 02:59:35 CEST (date), vor jeder Rechnung. Finn 07.10.: "ok mach das".
- **Herkunft:**
  - [P] NETZ-DYN-1: Die 1+1D-Kontrolle gab d_s = 2,00 bis 2,02, aber d_H = 2,23 (Skalierung) bzw. 2,30 bis 2,35 (lokal).
    Das flache Netz gab 2,000.
  - [S] DOSSIER-OPENAI-MATH T2 (Familie 211, Nr. 375 bis 377): zufaellige planare Karten (spannbaumgewichtet bzw.
    FK-Ising). Dort ist der Takt der Irrfahrt bekannt.
  - [L] Uniforme Zufallskarten (2D-Quantengravitation): d_H = 4, d_s = 2.
- **Frage:** Gibt unser Werkzeug auf Ensembles mit bekannter Antwort die richtigen Dimensionen? Daran entscheidet
  sich, ob d_H = 2,3 in D1 ein Methodenfehler war oder echte Physik.

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | So kann sie scheitern | Wahrsch. |
|---|---|---|---|
| E1 | Uniforme Zufallstriangulierungen (Kugel, N bis ~10^5 Dreiecke): d_s = 2,0 +- 0,1 [L] | d_s ausserhalb von 1,9 bis 2,1 | 75 % |
| E2 | Dieselben: d_H = 4,0 +- 0,3 aus der Groessenskalierung [L]; lokale Schaetzung darunter (endliche Groesse) | d_H aus der Skalierung ausserhalb von 3,7 bis 4,3 | 55 % |
| E3 | 1+1D-CDT aus NETZ-DYN-1 mit derselben Methode, groessere N: d_H naehert sich 2 (2,23 -> unter 2,15) | d_H bleibt >= 2,2 oder waechst | 50 % |
| E4 | Die lokale d_H-Schaetzung hat eine systematische Verschiebung nach oben, die auf beiden Ensembles gleich gerichtet ist | entgegengesetzte Richtung | 55 % |

- Vorab ableitbar: E1 und E2 sind Literaturwerte, nur Kontrolle. Echt offen: E3 und E4, also ob unser D1-Befund ein
  Methodenartefakt ist.
- Synthetisch, keine Messdaten.
