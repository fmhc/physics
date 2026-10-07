# TENSOR-EIS-N: Macht ein Energieglied mit "falschem" Vorzeichen aus Abstossung Anziehung, und ist das auf dem Gitter stabil? (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 23:23:42 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Dossier GRAVITON-NETZ-L (RUNDE-35/graviton-netz-l/DOSSIER.md, V4 und Abschnitt 6, RT-2): Gu/Wen 2009
    (arXiv:0907.1203).
    - Im L-Typ stossen sich gleiche "Massen" ab (Kraft ~ r^-4).
    - Im N-Typ ziehen sie sich an (~ m1 m2/r^2). Den Unterschied macht ein indefinites Glied -1/2 (E^ii)^2.
    - Die Autoren nennen den N-Typ "not reliable".
  - TENSOR-EIS-0, LAST-1 und AEQ-0: Mit positiv definitem Quellsektor stossen sich gleiche Quellen ab.
  - Finns Frage: Wie bekommt das Tetraedernetz Schwerkraft?
- Kennzeichen: [S] an der Quelle gelesen (Dossier), [L] Literatur aus dem Gedaechtnis, [H] Hypothese, [M] Mathematik.

## Schreibtisch (vor jeder Rechnung)

- **Gu/Wen** [S, Dossier]: symmetrisches Tensorfeld a_ij mit konjugiertem E^ij auf dem Gitter.
  - Vektorielles Gauss-Gesetz d_i E^ij = 0 (linearisierte Diffeomorphismen als Eichung).
  - "Masse" = Verletzung der skalaren Bedingung (delta_ij d^2 - d_i d_j) a_ij = 0, also der linearisierten
    Hamilton-Bedingung (raeumliche Skalarkruemmung ~ Quelle).
  - L-Typ: positiv definite Energie. N-Typ: zusaetzlich -1/2 (E^ii)^2.
  - Mit a_00 und a_0i ist die Wirkung laut Quelle "exactly the linearized Einstein action".
- **Erwartung** [S]: L stoesst ab, N zieht an. Der Kontinuumsausgang ist Literatur; dies ist ein Nachbau.
- **Neu waeren zwei Antworten:**
  1. Ist der N-Typ auf dem Gitter ueberhaupt stabil (Energie nach unten beschraenkt, keine wachsenden Moden)? [H: eher
     nicht; in der ART ist der konforme Modus durch die Zwangsbedingung gebunden, nicht frei]
  2. Gilt die Vorzeichenregel auch auf Finns Pyrochlor-Gitter (wahlweise)?

## Test (Code-Agent)

- **Quelle lesen:** Gu/Wen 2009 (arXiv:0907.1203), Abschnitte IV.B bis D und VII.
  - Gezielter Abruf erlaubt (Abstract-Seite, PDF per WebFetch speichern und mit dem Read-Werkzeug lesen).
  - Daraus L- und N-Typ als Gittermodell nachbauen: Freiheitsgrade, Hamilton-Funktion, Zwangsbedingungen, Massenquelle.
  - Die Rekonstruktion im PLAN mit Gleichungsnummern der Quelle belegen.
- **Statik:** Wechselwirkung zweier gleicher Massen gegen r auf dem kubischen Gitter.
  - Fourier-Werkzeug wie TENSOR-EIS-0; Torus-Hintergrund mit Groessenreihe bzw. Korrektur wie LAST-1.
  - Fuer den N-Typ den stationaeren Wert (Sattel), wenn kein Minimum existiert; offenlegen.
- **Stabilitaet:** Spektrum der quadratischen Form bzw. der linearen Dynamik des N-Typs auf dem Gitter.
  - Negative Richtungen, wachsende Moden, ihre Lage im k-Raum.
- **Wahlweise:** dasselbe auf dem Pyrochlor-Gitter (Finns Tetraeder).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| N0 | Rekonstruktion: L-Typ auf dem kubischen Gitter stoesst gleiche Massen ab, Kraftexponent 4 +- 0,4 (nach Torus-Korrektur) | 70 % |
| N1 | N-Typ: stationaere statische Wechselwirkung gleicher Massen ist anziehend, Potential ~ 1/r (Exponent 1 +- 0,1) | 50 % |
| N2 | N-Typ: Die quadratische Form auf dem Gitter ist indefinit (negative Richtungen ausserhalb der eichfreien Zwangsflaeche) | 75 % |
| N3 | N-Typ: Die lineare Gitterdynamik hat wachsende Moden (instabil) | 55 % |
| N4 | Wahlweise, Pyrochlor: Vorzeichenregel gilt (L stoesst ab, N zieht an) | 50 % |

**Bedeutung (vorab):**
- N0 und N1 treffen ein: Gleiche Massen ziehen sich in einem Erhaltungsregel-Netz an, sobald ein Energieglied das
  "falsche" Vorzeichen traegt. Das ist die gesuchte Zutat fuer Schwerkraft in Finns Bild.
- N2 und N3 treffen ein: Diese Zutat macht das Netz instabil, ausser die negative Richtung ist (wie in der ART) durch eine
  Zwangsbedingung gebunden. Dann braucht Finns Netz eine zusaetzliche Regel, die diese Richtung festlegt [H].
- N1 verfehlt: Die Anziehung des N-Typs haengt an Annahmen, die auf dem Gitter fehlen; beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6 (nicht cpu2, cpu3, cpu4, cpu5, p4000a,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min.
