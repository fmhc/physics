# PAAR-REGGE-1: Traegt ein rotierendes Gluonenpaar mit fester Endmasse die fuehrende Gitter-Glueball-Trajektorie, und mit welcher Endgeschwindigkeit? (Runde 42)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 18:22:23 CEST (date), vor jeder Rechnung.
- **Herkunft:** Kartenvorschlag aus GLUON-PAAR-L (RUNDE-37/gluon-paar-l/DOSSIER.md Abschnitt 6, Z. 180 bis 210).
  - Modell, Daten, Baender, Ableitbarkeitsprobe und Kontrollen von dort sind **bindend und woertlich zu uebernehmen**.
  - Zusaetze der Leitung sind unten als **[Zusatz Leitung]** markiert.
- **Finn (04.10., zwischen 17:27 und 17:29), woertlich:** "und wenn gluonen zwei-punkt-symmetrien sind die sich umeinander
  drehen und 1-2 einheiten groß sein können und relativistisch bei 3/4... das mal checkn als idee"
- **Einordnung (GLUON-PAAR-L):** Das rotierende Paar ist ein Glueball-Bild (Meyer/Teper 2004), kein einzelnes Gluon.
  Lesart (a) "Enden mit 3/4 c" ist nur eine von mehreren 3/4-Stellen (Look-elsewhere).
- Kennzeichen: [M] Mathematik, [E] Rechnung, [P] Projektdatei, [S] Quelle, [L] Gedaechtnis, [ES], [H].

## Kurzfassung des Vorschlags (Wortlaut im Dossier)

- **Modell:**
  - Klassischer Nambu-Goto-String mit sigma_A = 9/4 sigma (Varianten 2,14 und 2,36 sigma) zwischen zwei gleichen
    Punktmassen m, starr rotierend.
  - Intercept a fest: 0 bzw. 1/12.
  - Eine freie Groesse: m/sqrt(sigma).
- **Daten:**
  - (A) Athenodorou/Teper 2020: 2++ = 4,894(22), 4++ = 7,60(12).
  - (B) Meyer/Teper-Gerade: 2++ = 4,89, 4++ = 8,29.
- **Messgroessen:** bestes m/sqrt(sigma), chi^2, v_end(J = 2) und v_end(J = 4).
- **Baender (vorab, je Datensatz):**
  - "(a) traegt": p >= 0,05 und v_end(2) in [0,70; 0,82].
  - "masselos": p >= 0,05 mit m = 0 innerhalb 1 sigma.
  - "traegt nicht": p < 0,05 fuer beide a.
- **Kontrollen (ableitbar):**
  - masselos: E = 5,32 sqrt(sigma) bei J = 2, a = 0
  - konstantes v = 3/4: 6,80
  - Sonderfall konstante Endgeschwindigkeit: v ~ 0,77 fuer (B), ~ 0,93 fuer (A)

## Vorhersagen (vor jeder Rechnung)

Uebernommen aus der Erwartung des Dossiers [ES], als Wahrscheinlichkeiten der Karte gesetzt [Zusatz Leitung]:

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| PR0 | Kontrollen: masselos 5,32 und konstantes v = 3/4 6,80 auf 1e-3 reproduziert | 90 % |
| PR1 | [H] Datensatz (B): Band "(a) traegt" | 30 % |
| PR2 | [H] Datensatz (A): Band "(a) traegt" | 10 % |

**Bedeutung (vorab):**
- **PR1 oder PR2 trifft ein:** Ein Paar mit Endmasse, dessen Enden mit rund 3/4 c laufen, beschreibt diese
  Gitter-Trajektorie. Das stuetzt Lesart (a) nur in diesem Modell und nur fuer diesen Datensatz (Look-elsewhere).
- **Beide verfehlt:** Die "3/4" als Endgeschwindigkeit traegt die Gitterdaten nicht.

## Dimensionsvergleich (AGENTS.md) [Zusatz Leitung]

- Gerechnet wird 3+1D.
- Als beschreibenden Nachtrag die 2+1D-Trajektorie aus dem Dossier (Steigung 0,384(16), Intercept -1,144(71)) mit
  demselben Modell, ohne Urteil.
- In 1+1D gibt es keine Drehung.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu11 (frei seit SPIEGEL-HAELFTE-1). Je Lauf <= 10 min, 1 Thread.
  Zeitbox 60 min.
- Zahlenwerte und Formeln vor der Rechnung gegen die Quellen in gluon-paar-l/quellen/ pruefen. Die Handrechnungen des
  Dossiers sind nicht gegengelesen (K(v), 0,372(20)).
