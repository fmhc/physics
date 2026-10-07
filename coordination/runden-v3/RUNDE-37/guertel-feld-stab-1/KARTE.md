# GUERTEL-FELD-STAB-1: Sattel oder Rast? Loest sich die Feld-Verdrillung nach einem Stoss in Staley-Richtung auf (Guertel-Trick, Spin 1/2)? (Runde 42)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 18:59:32 CEST (date), vor jeder Rechnung.
- **Herkunft:** Kartenvorschlag 1 aus GUERTEL-2 (RUNDE-37/guertel-2/ERGEBNIS.md, Abschnitt "Kartenvorschlaege",
  Punkt 1). Rechnung, Vorhersage, Ableitbarkeitsprobe und Scheitern von dort sind **bindend und woertlich**.
- **Stand aus GUERTEL-2:**
  - Im Raum (SO(3)) waechst die Vorwaertsverdrillung ueber 360 Grad hinaus, bis an einer Bindung der Drehwinkel pi
    erreicht ist; dann springt das Feld auf dem Gitter.
  - Auf dem glatteren Gitter (12, 24) ist der Ast bei 450 Grad gueltig (Nachtrag N1).
  - Offen: echt metastabil oder nur langsam zerfallend?
- **Finn (04.10.):** Guertel-Basis fuer kleinste Bewegungen (Viertakt, 720 Grad), Spin 1/2 (RUNDE-41, RUNDE-42).
- Kennzeichen: [M] Mathematik, [E] Rechnung, [L] Literatur, [H] Hypothese.

## Rechnung (woertlich aus GUERTEL-2)

- (12, 24) bis 420 und 450 Grad drehen (gueltig nach N1).
- Dann gezielt in Staley-Richtung stossen: Die Drillachse wird in der inneren Haelfte um eps gekippt, eps = 0,01, 0,1
  und 0,3.
- Danach lange relaxieren (FIRE 3000) mit Gittersprung-Sonde.

## Vorhersage (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GS0 | Kontrolle: Der Vorwaertsast bei 420 und 450 Grad wird aus GUERTEL-2 (N1) reproduziert (Energie auf 1e-6 relativ) | 85 % |
| GS1 | [M fuer das Kontinuum, H fuer das Gitter] Der Ast ist ein Sattel: Der Stoss fuehrt ohne Gittersprung in die umgekehrte Verdrillung (E faellt auf etwa E(720 - theta)) | 50 % |

**Ableitbarkeitsprobe (aus GUERTEL-2):** Im Kontinuum ableitbar (konjugierter Punkt). Auf dem Gitter nicht, weil die
Bindungswinkel bei 450 Grad schon 2,1 rad betragen.

**Scheitern:** Der Stoss endet im Gittersprung oder faellt in den Ast zurueck.

**Bedeutung (vorab):**
- **GS1 trifft ein:** Das Feld um einen drehenden Kern kann seine Verdrillung nach 720 Grad ohne Sprung aufloesen. Das
  ist der Guertel-Trick im Feld, die Grundlage fuer den halben Spin (Luecke L4 in GEMEINSAMES-NETZ-v1) [H].
- **GS1 verfehlt:** Auf dem Gitter bleibt der Trick hinter Gitterspruengen verborgen; ein feineres Gitter oder GUERTEL-3
  waeren noetig.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu5 (frei seit RAUTE-ATEM-1). Je Lauf <= 10 min
  (laut GUERTEL-2 etwa 3,5 min je Stoss), 1 Thread. Zeitbox 75 min.
