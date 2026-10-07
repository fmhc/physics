# KAUSAL-4D-STABIL-L: Waechst die Welle auf dem 3+1-Raumzeit-Netz wirklich an, und kennt die Literatur Abhilfe? (Gegenpruefung und Literatur, Runde 38)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-04 08:10:22 CEST (date), vor jedem Abruf.
- **Anlass:** KAUSAL-WELLE-4D (RUNDE-37/kausal-welle-4d/ERGEBNIS.md).
  - Johnstons 4D-Propagator hat bei endlicher Dichte im Mittel Pole bei Im omega > 0 (0,15 / 0,20 / 0,25 bei rho = 16 /
    8 / 4).
  - Naeherung Im omega ~ (sqrt 6/4) m^4/(omega sqrt rho).
  - Hochgerechnet auf Planck-Dichte: Elektron e-fach in ~3e6 Weltaltern, Top in ~1 Jahr [H, ungeprueft].
  - Das waere ein ernster Einwand gegen Ueberleitung 3 in Johnstons Form, falls es traegt.
- Kennzeichen: [S] an der Quelle gelesen, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [ES] eigener Schluss, [H]
  Hypothese.

## Auftrag (ein tiefer Lauf, zwei gekoppelte Teile)

- **Teil 1, Gegenpruefung (Schreibtisch, ohne Rechnung auf der .69):**
  - Die Herleitung der Erwartungsformel und der Polformel aus ERGEBNIS.md und PLAN.md unabhaengig nachvollziehen.
  - Wo nicht nachvollziehbar: genau benennen.
  - Die Hochrechnung pruefen. Ist die Polformel fuer m^2/sqrt(rho) -> 0 gueltig? Ist omega ~ m fuer ruhende Teilchen
    richtig eingesetzt?
  - Ist das Ensemble-Mittel die physikalisch richtige Groesse, oder waechst eine einzelne Realisierung anders?
- **Teil 2, Literatur (gezielte Abrufe):**
  - Ist das Anwachsen bzw. die Instabilitaet von Johnstons 4D-Propagator bzw. der 4D-Kausalmengen-d'Alembert-Operatoren
    bekannt?
  - Welche Abhilfen gibt es: geglaettete Operatoren mit Nichtlokalitaetsskala (Sorkin; Aslanbeigi/Saravani/Sorkin;
    Belenchia u. a.), veraenderte Sprung- und Haltamplituden, Dowker/Glaser?
  - Gibt es Beobachtungsschranken auf solche Effekte?

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung |
|---|---|
| E1 | Die Polformel ist in erster Ordnung richtig hergeleitet. Die Hochrechnung skaliert wie m^3 l_P^2 fuer ruhende Teilchen. |
| E2 | Fuer 4D-Kausalmengen-Operatoren sind Instabilitaeten bzw. Anwachsen bei endlicher Dichte bekannt, z. B. bei Aslanbeigi/Saravani/Sorkin 2014 (verallgemeinerte d'Alembert-Operatoren, Stabilitaetsbedingungen) [L?]. |
| E3 | Geglaettete Operatoren mit Nichtlokalitaetsskala koennen stabil gemacht werden; der Preis ist eine neue Laengenskala weit ueber der Planck-Laenge. |
| E4 | Fuer Johnstons Pfadsummen-Propagator selbst ist die Instabilitaet nicht ausdruecklich beschrieben. |
| E5 | Das Ensemble-Mittel ist nicht die ganze Physik. Die Literatur betrachtet meist das Mittel oder den Erwartungswert ueber Streuungen. |

## Rahmen

- feldforscher, hoechstens 15 gezielte WebFetch-Abrufe, keine Websuche.
- Teil 1 am Schreibtisch, lokal ohne python, awk oder perl.
- Abgabe: DOSSIER.md und ARBEITSFELD.md in RUNDE-37/kausal-4d-stabil-l/.
- Zeitbox 75 min.
