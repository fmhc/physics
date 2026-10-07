# FLUSS-TEXTUR-1: Sind Igel des Drehrahmens Quellen des Z2-Flusses, den die Fadenend-Fermionen sehen? (Runde 50, Ziel Schritt b, schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-05 19:45:21 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:** Befund 5 von GERAHMTER-FADEN-1. In Variante B (Twist-Konvention je Knoten aus der Rahmenrichtung
  n_i) erzeugt die Rahmentextur ein Z2-Flussmuster fuer die Fermionen: bis 198 von 432 Sechsecken mit Fluss -1, bei
  fester Projektion ueberall +1.
  - Das lokale Muster haengt stark von der Push-off-Richtung w ab (n = 2, 15 Grad: w_haupt 1 bis 20 Sechsecke mit -1,
    w_alt 0).
  - Offene Fragen des Agenten: Quellen (Kaefigprodukte), Abhaengigkeit von der Textur, Verwandtschaft mit dem
    Kopplungsgesetz aus C.
- **Projektsuche der Leitung** (19:45, mit Sperrausschluessen; Igel mit Monopol/Quelle, Kaefigprodukt): nur
  VIERTE-KOORDINATE-L (Spin aus Isospin am Igel nach Jackiw/Rebbi, ein anderes Thema) und GERAHMTER-FADEN-1.
- **Literatur [L]:** Texturen als Eichfelder fuer Teilchen sind bekannt (Berry-Phase, Skyrmionen als Flussquellen).
  Keine Neuheit des Mechanismus beanspruchen.
- **Frage:** Hat der Texturfluss Quellen? Liegen sie genau an den Igeln des Rahmens, unabhaengig von der willkuerlichen
  Push-off-Richtung? Dann waere die Quelle eine Eigenschaft der Rahmentopologie und keine Konvention.

## Pflicht vor jeder Rechnung: Schreibtischprobe (VORAB.md)

- Kann das Kaefigprodukt (Produkt der Sechseckfluesse ueber einen geschlossenen Kaefig) per Konstruktion nur +1 sein?
  Das waere so, wenn die Fluesse Produkte von Link-Vorzeichen sind (Bianchi-Identitaet).
  - Wenn ja: FT1 und FT2 stehen vorab fest. Dann ist das Ergebnis "Quellen strukturell ausgeschlossen", und es wird
    nicht gerechnet, nur belegt.
- Je Erwartung eine Zeile, wie sie scheitern kann. Feste Ausgaenge offen nennen.

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | So kann sie scheitern | Wahrsch. |
|---|---|---|---|
| FT1 | Glatte Texturen R1 (alle theta_max, beide w): jedes Kaefigprodukt ist +1 (keine Quellen) | mindestens ein Kaefig mit -1 in R1 | 60 % |
| FT2 | Igel-Textur (n_i radial um einen Kernpunkt, Grad 1): Der Kaefig um den Kern hat Produkt -1 fuer beide w, alle Kaefige weit weg +1 | +1 um den Kern fuer ein w, oder -1 weit weg | 40 % |
| FT3 | Zwei Igel (Grad 1 und 1) im selben Netz: Je Kern -1, ein Kaefig, der beide umschliesst, gibt +1 (Z2-Addition) | ein umschliessender Kaefig mit -1, oder +1 an einem Einzelkern | 35 % |

## Rahmen

- Folgeauftrag an den GERAHMTER-FADEN-1-Agenten (Code und Netz vorhanden), ohne Einfrieren und Leser.
- Diamant n = 2, 3 bzw. so gross, dass zwei Igel getrennt Platz haben; Spuren cpu8 bis cpu10, je Lauf hoechstens 10 min;
  df vor jedem Lauf.
- Synthetisch, keine Messdaten.
