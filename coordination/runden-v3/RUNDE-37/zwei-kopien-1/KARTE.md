# ZWEI-KOPIEN-1: Kann eine oertliche Eckkopplung die zwei Schwerkraft-Kopien von Finns Netz so binden, dass genau ein masseloses Gravitonpaar bleibt? (Runde 43)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 19:47:40 CEST (date), vor jeder Rechnung.
- **Herkunft:** Kartenvorschlag aus GEMEINSAMES-NETZ-L (RUNDE-37/gemeinsames-netz-l/DOSSIER.md, Z. 176 bis 215). Anlass,
  Bau, Messgroessen, Baender B-a bis B-d, Erwartung und Ableitbarkeitsprobe von dort sind **bindend und woertlich**.
  Zusaetze der Leitung sind markiert.
- **Finn (19:28 bis 19:31):** "der raum ist das netz"; die Kantenlaengen sind die Geometrie.
- **Projektbezug [Zusatz Leitung]:**
  - TENSOR-EIS-PYRO-1, Bauweise B1: zwei unabhaengige Kopien, 4 statt 2 Helizitaet-2-Moden.
  - EINE-WELT-LOCH-1: Mit gefuellten Loechern gibt es schon eine Welt mit genau 2 masselosen TT-Moden.
  - Diese Karte fragt, ob eine reine Eckkopplung ohne neue Bauteile dasselbe leistet oder ob BDGH (keine Kreuzkopplung
    masseloser Gravitonen) auf dem Gitter greift.
- Kennzeichen: [M], [E], [L], [S], [ES], [H].

## Ableitbarkeitsprobe (woertlich, mit Schritt 0)

- **Schritt 0 (vor dem Bau, hoechstens 30 min Schreibtisch):** pruefen, ob K2 unter einer exakten Abbildung
  xi_Ab = Mittel(xi_Auf) invariant ist. Wenn ja, ist B-b ableitbar und die Karte schrumpft zur Kontrolle.
- **Ableitbar:**
  - BDGH verbietet im Lorentz-invarianten Grenzfall eine nichttriviale Kreuzkopplung zweier masseloser Zweige mit
    hoechstens zwei Ableitungen.
  - Teilten beide Kopien dieselben Eichparameter, gaebe eine Differenzkopplung genau eine masselose Diagonale.
- **Nicht ableitbar:** In B1 sitzen die Eichfreiheiten der Kopien auf verschiedenen Untergittern. Ob die Eckkopplung eine
  diagonale Eichung wenigstens langwellig erhaelt (B-b) oder bricht (B-c), legen weder BDGH noch die Zaehlung fest.

## Bau und Messgroessen (woertlich aus dem Dossier)

- **Bau:**
  - Die vorhandene lineare B1-Rechnung (12 Kanten je primitiver Zelle) bekommt einen Zusatzterm kappa K.
  - K2: Differenz der mittleren Kantendehnung beider Tetraeder an der Ecke, quadriert.
  - K4: Produkt der Fehlwinkel-Aenderungen beider Kopien an der Ecke.
  - Je drei Werte von kappa.
- **Messgroessen** (aus dem Fourier-Spektrum gemessen, nicht eingesetzt):
  - n0: Zahl der Helizitaet-2-Zweige mit omega -> 0 fuer k -> 0
  - Exponent p aus Delta ~ kappa^p
  - Streuung s von omega^2/k^2 ueber 26 Richtungen
- **Baender:**
  - B-a: n0 = 4
  - B-b: n0 = 2, Delta > 0, s < 5 %
  - B-c: n0 = 0
  - B-d: omega^2 < 0 oder negative Norm

## Vorhersagen (vor jeder Rechnung; Erwartung des Dossiers als Wahrscheinlichkeiten [Zusatz Leitung])

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| ZK0 | Kontrolle: kappa = 0 reproduziert TENSOR-EIS-PYRO-1 B1 (n0 = 4, Tempi auf 1e-8) | 90 % |
| ZK1 | [H] K2 landet in Band B-b (eine masselose Kombination wie bei Bigravitation) | 35 % |
| ZK2 | [H] K4 landet in Band B-a (Kopplung linear wirkungslos) | 50 % |

**Bedeutung (vorab):**
- **ZK1 trifft ein:** Eine einfache Eckkopplung macht aus Finns zwei Welten eine Schwerkraft plus eine massive
  Zusatzmode. Das waere ein zweiter Weg neben den gefuellten Loechern.
- **ZK1 verfehlt mit B-c:** Die Kopplung zerstoert beide masselosen Gravitonen; dann bleibt nur der Weg ueber die Loecher.
- **B-d:** Die Eckkopplung macht das Netz instabil.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu8 und cpu9. Je Lauf <= 10 min, 1 Thread. Zeitbox 90 min.
