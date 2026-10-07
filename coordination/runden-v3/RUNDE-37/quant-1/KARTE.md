# QUANT-1: Erster Quantenschritt: Ist ein Q-Ball ein gebundener Zustand aus Q Feldquanten? (Runde 50, schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-05 17:57:36 CEST (date), vor jeder Rechnung.
- **Finn, 05.10.:** "wie kommen wir dann von dort auf die gemessenen quanten-definitionen in kombiniertenteilchenformen?"
- **Herkunft [P]:**
  - Bisher ist alles klassisch: Q-Baelle sind Feldklumpen (Papier I), Ladung Q ist eine stetige Zahl.
  - Im Projekt gibt es keine Quantisierung des Q-Ball-Sektors (grep nach HMC, Pfadintegral, Korrelator: nichts).
  - Y-1 (RUNDE-10): Der Wirbel-Dreier als Proton-Bild ist fuer die unveraenderte Formel verworfen (19 von 27 Erwartungen
    verfehlt).
- **Ansatz [L]:** Euklidisches Pfadintegral des komplexen Q-Ball-Felds auf dem 4D-Netz (V mal Zeit), Hybrid-Monte-Carlo.
  Massen aus dem Abfall von Korrelatoren, Ladung Q aus Operatoren phi^Q. So rechnet die Gitter-QCD Teilchenmassen.
- **Ableitbarkeit:**
  - [M] Bei schwacher Kopplung liegt die Einteilchenmasse nahe am Massenparameter m.
  - [L] Q-Baelle gelten als Grenzfall grosser Q von gebundenen Zustaenden aus Q Quanten (duenne Wand).
  - Nicht ableitbar: Bindung bei kleinem Q auf V; ab welchem Q die klassische Energie traegt.

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| Q1 | Die Einteilchenmasse aus dem Korrelator von phi liegt bei schwacher Kopplung auf 20 % am Massenparameter | 80 % |
| Q2 | Bei anziehendem Q-Ball-Potential gibt es fuer Q = 2 und 3 gebundene Zustaende unter Q mal Einteilchenmasse; die Bindung je Teilchen waechst mit Q | 55 % |
| Q3 | Fuer das groesste erreichbare Q liegt die Quantenenergie E(Q) auf 10 % an der klassischen Q-Ball-Energie | 40 % |

## Rahmen

- Code-Agent ohne Einfrieren und Leser (Finn: einfach machen).
- Kleines Netz: V 3 x 3 x 3 bzw. 4 x 4 x 4 Zellen mal 32 bis 64 Zeitschritte. Wenn V zu teuer ist, zuerst ein einfaches
  kubisches Gitter als Kontrolle.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu6, je Lauf hoechstens 10 min; df vor jedem Lauf.
- Synthetisch, keine Messdaten.
