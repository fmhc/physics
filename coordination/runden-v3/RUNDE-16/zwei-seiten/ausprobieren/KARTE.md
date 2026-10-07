# AUSPROBIEREN: fuenf kleine Versuche zum Arbeitsmodell "Zwei Seiten des Feldes" (Runde 16)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 08:15:23 CEST (date), vor jeder Codezeile.
- Auftrag Finn: "probier in einem subagent einfach mal aus die sachen".
- Grundlage: RUNDE-16/zwei-seiten/ZWEI-SEITEN-DES-FELDES-v2.md (v2 der Leitung) und v1-original.md (Finn).
- Explorativ, kleine Laeufe. Positivkontrollen zuerst, wie in v2, Abschnitt 17 A.

## Versuche

| Nr | Versuch | Vorhersage (Leitung, vor dem Lauf) |
|---|---|---|
| V1 | **Federtetraeder:** 4 gleiche Massen, 6 gleiche Federn mit Ruhelaenge. Normalmoden aus der Hesse-Matrix. | Spektrum (k/m) x {0 (6-fach), 1, 1, 2, 2, 2, 4}; ~95 % |
| V2 | **Maxwell-Ring (Positivkontrolle fuer Variante R):** N gleiche Massen m auf einem Kreis um eine Zentralmasse M, Newton-Gravitation, gleichfoermige Rotation (relatives Gleichgewicht). Lineare Stabilitaet im mitrotierenden System (gyroskopisch) fuer N = 3 bis 16, kleines m/M, z. B. 1e-6 und 1e-4. | Stabil genau fuer N >= 7, wenn m/M klein genug ist (nach Moeckel 1994, aus dem Gedaechtnis, [L?]) ~70 %. Fuer grosses N schrumpft das stabile m/M wie N^-3 (Maxwell) ~60 % |
| V3 | **Federring N+1 (Variante R mit Federn):** N Punkte auf dem Kreis, Federn zu den Nachbarn und Speichen zum Zentrum, Ruhelaengen, Rotation Omega. R(Omega) aus der Kraeftebilanz; lineare Stabilitaet im mitrotierenden System fuer N = 4 bis 32 und drei Omega. | Kein N ist auffaellig: S(N) verlaeuft glatt, 11 und 19 nicht mehr als 3 sigma vom Nachbarverlauf (~85 %). Ab einem kritischen Omega werden Ringe instabil (~70 %) |
| V4 | **Ticks ereignisgenau:** zwei starre Tetraeder, die sich gegeneinander drehen oder bewegen und dabei durchdringen. Ticks = Vorzeichenwechsel der Orientierungsdeterminante mit Innen-Test, Zeit per Nullstellensuche. Vergleich mit naivem Zaehlen ueber Zeitschritte, bei dt, dt/2, dt/4. | Ereignisgenaue Zaehlung gleich fuer alle dt (~95 %). Naive Zaehlung haengt von dt ab oder verpasst Ereignisse (~70 %) |
| V5 | **Diskretes Feld auf dem Ring-Graphen (11+1, 19+1 und Nachbarn):** Gleichung aus v2 Abschnitt 2 mit V = S - S^2 + S^3/2, feste Geometrie. Lokalisierte, phasenrotierende Mode (diskreter Q-Ball am Zentrum oder auf dem Ring) per Newton bei festem omega. Lineare Stabilitaet bei fester Ladung (mitrotierendes Phasenbild). | Lokalisierte Moden existieren fuer omega^2 im Fenster (0,5; 1) bei kleiner Kopplung J (~80 %). Kein N ist besonders (~85 %) |

## Kontrollen

- Erhaltungsgroessen in jeder Zeitentwicklung, soweit gerechnet: Energie, Drehimpuls, Ladung (relativer Fehler < 1e-6).
- Zwei Aufloesungen bzw. Toleranzen je Ergebnis.
- V2 ist die Positivkontrolle fuer V3: Faellt V2 deutlich anders aus als die Literatur, wird V3 nur mit Vermerk berichtet.

## Rahmen

- Code-Agent, eigener Code (numpy, scipy), alles im Ordner RUNDE-16/zwei-seiten/ausprobieren/.
- Nur .69 ueber kleintest.sh, Spuren cpu und cpu2 (cpu3/cpu4 belegt), jeder Aufruf hoechstens 10 min.
- Lokal nur Rauchtests (<= 120 s, ein Thread, nice 19).
- Kurzer Plan vor den Laeufen, eingefroren. Zeitbox 90 min.
- Reihenfolge, wenn es eng wird: V1, V2, V4, V3, V5.
