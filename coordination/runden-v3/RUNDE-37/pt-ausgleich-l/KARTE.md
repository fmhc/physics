# PT-AUSGLEICH-L: Kann ein PT-symmetrischer Ausgleich (Gewinn auf der einen, Verlust auf der anderen Seite) Finns Umklappen zwischen sichtbarer und verborgener Haelfte verlustfrei machen? (Runde 45, Literatur und Schreibtisch, Luecke L5)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-05 04:20:55 CEST (date), vor jedem Abruf.
- **Finn (05.10., gegen 04:15):** "Führe alle Themen weiter ... teste herum, was richtig ist".
- **Herkunft:**
  - Lesart N9 (RUNDE-42/NEGATIV-LESARTEN.md): "Verlustseite eines ausgeglichenen Paars (PT-Symmetrie): Gewinn auf der einen, Verlust auf der anderen Seite, im Gleichgewicht: reelles Spektrum trotz Abfluss; Finns 'Ausgleich'" [H].
  - SPIEGEL-HAELFTE-1 (Runde 42): Mit einer verborgenen Haelfte mit eigenem Takt gilt Foster/Jacobsons Umklappen nur im Mittel. Einzeln fliessen 44 % zurueck. Die Doppler wachsen.
  - Scout: arXiv 2610.00774 (diskrete PT-symmetrische Solitonen auf verzweigten Gittern) und die Arbeit vom 06.01.2026 zu PT-symmetrischen verzweigten optischen Gittern (RUNDE-42/quellen-leitung/ABRUFE-1830.md).
- **Luecke L5 (GEMEINSAMES-NETZ v3.1):** Masse ohne Verlust.
- Kennzeichen: [S], [S Abstract], [L], [M], [ES], [H].

## Ableitbarkeitsprobe (vor der Karte)

- **Vorab ableitbar [L, M]:**
  - Ein PT-symmetrischer Hamilton-Operator mit ungebrochener PT-Symmetrie hat ein reelles Spektrum (Bender).
  - Er ist pseudo-hermitesch und mit einem anderen inneren Produkt einem hermiteschen Operator aequivalent (Mostafazadeh) [L].
  - Ein "Ausgleich" ist also entweder eine Umformulierung einer gewoehnlichen unitaeren Theorie oder, bei gebrochener PT-Symmetrie, echter Verlust bzw. Gewinn.
- **Nicht ableitbar:**
  - ob Finns Umklappen (Foster/Jacobson mit verborgener Haelfte) sich als ungebrochen PT-symmetrisches System schreiben laesst
  - ob die 44 % Rueckfluss dann verschwinden oder nur umgedeutet werden
  - was die verzweigten PT-Gitter dazu sagen
- **Projektsuche:** PT-Symmetrie nur als Lesart N9 und in den zwei Scout-Treffern. SPIEGEL-HAELFTE-1 enthaelt den Code der verborgenen Haelfte.

## Auftrag (feldforscher)

1. **Lesen:** 2610.00774 und die PT-Arbeit vom Januar 2026; aus dem Gedaechtnis Bender 1998 und Mostafazadeh 2002, als [L] gekennzeichnet.
   - Unter welchen Bedingungen bleibt das Spektrum auf verzweigten Gittern reell?
   - Wo liegt der Ausnahmepunkt?
2. **Schreibtisch:**
   - Laesst sich das SPIEGEL-HAELFTE-1-Modell (Umklappen mit verborgener Haelfte; Code und ERGEBNIS lesen) mit einer Gewinn-Verlust-Kopplung PT-symmetrisch schreiben?
   - Was waere die erhaltene Norm (eta-Metrik)?
   - Verschwindet der Rueckfluss, oder wird er nur umbenannt?
3. **Einordnung fuer Finn:** Ist "Ausgleich" eine neue Physik, eine Umformulierung oder ein Weg zu messbarem Verlust?

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| PA1 | [H] Das Umklappen mit verborgener Haelfte laesst sich PT-symmetrisch schreiben; unterhalb des Ausnahmepunkts ist es einer gewoehnlichen unitaeren Theorie aequivalent (keine neue Physik) | 60 % |
| PA2 | [H] Der Rueckfluss von 44 % verschwindet dabei nicht, sondern wird in der eta-Metrik als Teil der Erhaltung gezaehlt | 55 % |
| PA3 | [H] Die verzweigten PT-Gitter der Literatur haben reelle Spektren nur bei abgestimmter Verzweigung (Bedingung an die Kopplungen der Aeste) | 65 % |

**Bedeutung (vorab):**
- **PA1 trifft ein:** Finns Ausgleich ist mathematisch moeglich, aber eine Umformulierung. Fuer L5 gewinnt man ein anderes Bild, keine neue Vorhersage.
- **PA1 verfehlt:** Entweder ist PT gebrochen (echter Verlust, messbar) oder das Umklappen passt nicht in die PT-Form. Beides waere informativ.

## Rahmen

- feldforscher, Zeitbox 50 min, hoechstens 5 Abrufe (arXiv-API oder arxiv.org per WebFetch), keine Websuche.
- Erwartung mit date-Zeit vor jedem Abruf in ARBEITSFELD.md.
- Schreiben nur in RUNDE-37/pt-ausgleich-l/.
