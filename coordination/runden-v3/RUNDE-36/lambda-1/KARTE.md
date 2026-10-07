# LAMBDA-1: Warum genau 1/2? Das Minus-Glied des Netzes als lambda-Problem der Hořava-Gravitation (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 00:15:52 CEST (date), vor jeder Rechnung.
- **Anlass:** TENSOR-EIS-N (RUNDE-36/tensor-eis-n/ERGEBNIS.md).
  - Der Gu/Wen-N-Typ zieht gleiche Massen wie Newton an (-1/(8 pi r)), aber stabil nur mit exakt -1/2 (E^ii)^2.
  - Bei 0,49 und 0,51 waechst die Gitterdynamik exponentiell.
  - Finns Frage: Wie bekommt das Tetraedernetz Schwerkraft?
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Zuordnung** [L]: In der ADM-Form der ART ist der kinetische Teil pi^ij pi_ij - pi^2/(d - 1), bei d = 3 also -1/2
  pi^2. Den Koeffizienten legt die volle Diffeomorphismen-Invarianz fest.
- Die Hořava-Lifshitz-Gravitation (2009) laesst einen Parameter lambda zu.
  - Der kinetische Teil im Impulsbild ist pi^ij pi_ij - (lambda/(3 lambda - 1)) pi^2, also c = lambda/(3 lambda - 1),
    lambda = c/(3 c - 1).
  - c = 1/2 entspricht lambda = 1 (ART); c = 0,49 entspricht lambda ~ 1,043; c = 0,51 entspricht lambda ~ 0,962.
- **Hořavas zusaetzlicher Skalarmodus** [L]: Seine Dispersion im langwelligen Grenzfall ist
  omega^2 ~ -((lambda - 1)/(3 lambda - 1)) k^2.
  - lambda > 1 (also 1/3 < c < 1/2): omega^2 < 0, eine Gradienteninstabilitaet mit Wachstumsrate ~ k
    sqrt(abs(lambda - 1)).
  - 1/3 < lambda < 1 (c > 1/2): omega^2 > 0, aber Geist (negative Energie).
- **Erwartung** [H]: Das Gitter des N-Typs bildet diese Struktur nach. Auf der Seite c < 1/2 gibt es exponentielles
  Wachstum mit Rate ~ sqrt(1/2 - c); auf der Seite c > 1/2 wird es anders (Geist).
  - TENSOR-EIS-N sah aber auch bei 0,51 Wachstum. Das ist offen und genau der Test.

## Test (Code-Agent)

- **Code-Basis:** RUNDE-36/tensor-eis-n/code/tn.py (N-Typ, Fourier, lineare Dynamik, statische Wechselwirkung).
- **Koeffizient c** im Spurglied -c (E^ii)^2: 0,30; 1/3; 0,40; 0,45; 0,48; 0,49; 0,50; 0,51; 0,52; 0,55; 0,60; 0,70.
- **Gemessen je c:**
  - (a) groesste exponentielle Wachstumsrate der linearen Gitterdynamik (Eigenwerte, wie TENSOR-EIS-N), mit Lage im
    k-Raum und Moden-Zusammensetzung (Anteil Skalarbedingung, Eichrichtung, Helizitaet 2)
  - (b) dasselbe auf der Zwangsflaeche (beide Regeln streng erfuellt, physikalische Dynamik)
  - (c) statische Wechselwirkung zweier gleicher Massen, G_eff(c) aus dem 1/r-Ausgleich
- Vergleich mit der Hořava-Formel fuer die Wachstumsrate bei kleinem k.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| L0 | Kontrolle: c = 1/2 gibt die TENSOR-EIS-N-Werte (kein exponentielles Wachstum, Rest < 1e-6; U = -1/(8 pi r) auf 1 % ab r = 8) | 90 % |
| L1 | Seite 1/3 < c < 1/2: exponentielles Wachstum, Rate am Rand der Brillouin-Zone bzw. bei kleinem k ~ sqrt(1/2 - c); Exponent 0,5 +- 0,15 aus c = 0,45 bis 0,49 | 55 % |
| L2 | Die Raten sind um c = 1/2 asymmetrisch: Bei c = 1/2 +- 0,05 unterscheiden sie sich um mehr als 20 % | 60 % |
| L3 | Auf der Zwangsflaeche (b) gibt es fuer kein c exponentielles Wachstum; der gefaehrliche Modus lebt neben der Zwangsflaeche | 50 % |
| L4 | Die statische Anziehung bleibt fuer c ungleich 1/2 bestehen, mit G_eff(c) stetig und bei c = 1/2 gleich 1/(8 pi) | 55 % |

**Bedeutung (vorab):**
- L1 und L2 treffen ein: Das Minus-Glied des Netzes hat dieselbe Struktur wie Hořavas lambda. Exakt 1/2 ist dann die
  Gitterspur der allgemeinen Kovarianz.
  - Finns Netz braucht eine Symmetrie, die den Faktor festhaelt; ein Zufall genuegt nicht.
- L3 trifft ein: Die Instabilitaet steckt nur in den Regelverletzungen. Ein Netz, das seine Regeln streng haelt, bleibt
  stabil, auch bei c ungleich 1/2. Das waere eine Entwarnung fuer Finns Bild.
- L4 trifft ein: Die Newton-Anziehung ist robust, nur ihre Staerke haengt am Faktor.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6 (nicht cpu2, cpu3, cpu4, cpu5, p4000a,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
