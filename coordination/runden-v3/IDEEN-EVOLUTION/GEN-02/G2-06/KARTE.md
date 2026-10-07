# G2-06 Zweistufiger Einfang: Zwischenlager, dann paarweise Ausfaellung in den Grundzustand

- Quelle: GEN-01/G1-06/KARTE.md (dazu GEN-01/G1-06/NACHTRAG.md mit Bauhinweisen). Nur ins Kartenformat gebracht,
  keine neue Idee; Inhalt woertlich aus G1-06. Bisheriges Ergebnis: nicht getestet, weil der neue Code (40 bis 60 min)
  nicht in die Zeitbox von Generation 1 passte. Test hier: der Test der Karte nach den Bauhinweisen aus G1-06/NACHTRAG.md.

- Hypothese: Ein Ball, der einlaufende Wellen resonant in einer inneren Mode zwischenlagert, faellt einen Teil davon
  paarweise und endgueltig in seinen Grundzustand aus: Je zwei gelagerte Quanten werden zu einem gebundenen Quant und
  einem schnellen Quant bei 2 nu - omega, sodass der dauerhafte Ladungsgewinn wie eps^4 waechst und so gross ist wie die
  Ladung der schnellen Linie [H].

- Papier vorab [S] (eigene Rechnung, von Hand):
  - Zwischenlager: bekannte Pole des 1D-Balls [A: Resonanzrechnungen des 1D-Balls, Bruecke dims 1, zwei Haeuser]:
    - omega^2 = 0,55 (omega = 0,7416): rho = 1,3767 - 5,1e-3 i, nu_r = omega + Re rho = 2,1183, 2 Gamma = 0,0102
    - omega^2 = 0,70 (omega = 0,8367): rho = 1,4938 - 6,7e-5 i, nu_r = 2,3305, 2 Gamma = 1,3e-4
    - Linear gilt: Die gelagerte Ladung ist proportional zu eps^2, traegt nu je Ladung und laeuft mit 2 Gamma elastisch
      bei nu wieder aus. Unter der Schwelle 2 omega + 1 (2,483 bzw. 2,673) bleibt linear nichts dauerhaft am Ball.
  - Zweite Ordnung in der Lageramplitude a: Der kubische Term enthaelt a^2 psi_Ball^* mit der Frequenz 2 nu - omega:
    3,495 (0,55) bzw. 3,824 (0,70), also ueber 1 und offen. Der andere neue Term psi_Ball^2 a^* hat 2 omega - nu = -0,635
    bzw. -0,657 und ist geschlossen. In O(a^2) gibt es also genau einen neuen offenen Kanal.
  - Bilanz dieses Prozesses: 2 gelagerte Quanten (Ladung 2, Energie 2 nu) -> 1 Quant im Grundzustand (Energie omega) plus
    1 freies Quant (Energie 2 nu - omega). Daraus folgen:
    - dauerhafter Ladungsgewinn des Balls = Ladung der Linie
    - Energie je Ladung der Linie = 2 nu - omega
    - Rate ~ (Lager)^2 ~ eps^4

- Kleiner Test:
  - Code-Basis: RUNDE-07/r5f/r5f.py, Befehl fuettern (1D, Ball plus Paket mit sigma und x0, Ball-allein- und
    Paket-allein-Partnerlaeufe, Q und E in Fenstern, Fluesse, C_nach, C_Ende, kappa), aufgerufen mit --T 1200. Neu
    (unter 1 h):
    - eigene Liste von eps und nu
    - Zeitreihe psi(x = +-100, t) alle 0,25 mit Bandfilter um 2 nu - omega (+-0,15) und um nu; Ladung und Energie der
      Linie aus dem gefilterten Fluss
    - Ballfenster |x - x_Ball(t)| < 20 mit mitgefuehrtem Ballort (Rueckstoss)
  - Laeufe (sigma = 32, Paketmitte startet bei x0 = -150, Box und Schwamm wie in fuettern):
    - omega^2 = 0,55, nu = nu_r = 2,118: eps = 0,005 / 0,01 / 0,02 / 0,035 / 0,05
    - omega^2 = 0,70, nu = nu_r = 2,330: eps = 0,01 / 0,02 / 0,05 (Lager lebt etwa 7500, nur die Linie waehrend der
      Lagerung wird ausgewertet)
    - Gegenproben: Paket allein (nu_r, eps = 0,05); Ball allein; nicht resonant nu = 1,95 bei omega^2 = 0,55 und eps = 0,05
  - Rechenort: .69 ueber kleintest.sh, p4000a (grob, etwa 3 bis 5 min) und p4000b (fein, eigener Aufruf, unter 10 min).
  - Messgroessen:
    - dQ_perm = Q_Ballfenster(Ball + Paket) - Q_Ballfenster(Ball allein) bei t - Ankunft >= 800, wenn der Speicher bei
      0,55 auf unter e^-8 geleert ist
    - Q_Linie und E_Linie (beide Detektoren, ganze Laufzeit)
    - dE_Ball/dQ_perm

- Vorhersage vorab:
  - V1 (Kern, omega^2 = 0,55): dQ_perm > 0 und dQ_perm ~ eps^p mit p = 4,0 +- 0,6 (Fit ueber alle eps mit
    dQ_perm > 10 x Aufloesung).
  - V2 Linie: Die Detektoren zeigen eine Linie bei 2 nu_r - omega = 3,495 +- 0,03 (0,55) bzw. 3,824 +- 0,03 (0,70). Ihre
    Ladung waechst wie eps^4 (Exponent 4,0 +- 0,6).
  - V3 Bilanz (0,55): Q_Linie/dQ_perm = 1,0 +- 0,3; E_Linie/Q_Linie = 2 nu_r - omega auf 3 %.
  - V4: dE_Ball/dQ_perm liegt zwischen omega = 0,742 und omega + 0,3, also nahe dem Grundzustand und nicht bei nu = 2,12.
  - **Scheitert, wenn** eines davon eintritt:
    - dQ_perm skaliert wie eps^2 (p < 3); dann faengt ein linearer Mechanismus dauerhaft ein.
    - Bei aufgeloestem dQ_perm fehlt die Linie (Q_Linie < 1e-2 x dQ_perm).
    - Q_Linie/dQ_perm liegt ausserhalb 0,5 bis 2.
    - Die Linie erscheint auch ohne Ball.
  - Nicht entscheidbar, wenn dQ_perm bei eps = 0,05 unter 3e-4 liegt (Aufloesung) oder die Ladungsbilanz reisst.

- Gegenprobe:
  - Paket allein: keine Linie bei 2 nu - omega (unter 1e-3 der Linie mit Ball); ein freies Paket kennt kein omega.
  - Ball allein: keine Linie, Q konstant.
  - Nicht resonant (nu = 1,95): Lager winzig, also dQ_perm und Linie unter 1e-2 der resonanten Werte bei gleichem eps.

- Plausibilitaetsschranke:
  - 0 <= R, T <= 1; |Ladungsbilanz| < 1e-4
  - dQ_perm <= groesste gelagerte Ladung; Q_Linie <= Ladung des Pakets
  - E_Linie/Q_Linie = 2 nu - omega (eine einfarbige Linie traegt genau diese Energie je Ladung)

- Latten erwartet:
  - L1 ja: Exponent, Linie und Bilanz koennen je einzeln scheitern.
  - L2: Paket allein, Ball allein, nicht resonant.
  - L3: dx/2 und dt/2; dQ_perm und Q_Linie auf 20 %, Exponenten auf 0,3.
  - L4 teilweise: nichtlineare Abstrahlung innerer Moden bei doppelter Frequenz (Manton und Merabet 1997, phi^4-Kink) und
    Wachstum von Q-Baellen durch Einfang (Solitosynthese, Griest und Kolb 1989) [L, aus dem Gedaechtnis, nicht
    nachgelesen]. Den geladenen Kanal 2 nu - omega mit dauerhaftem Einfang kenne ich nicht [H].
  - L5 Analogie: inelastische Paarverluste an Feshbach-Resonanzen in kalten Gasen (Rate ~ Dichte^2, gemessen) [L]; kein
    Zahlvergleich.

- Einfach gesagt: Ein grosser Q-Ball kann Wellen einer bestimmten Frequenz eine Weile zwischenlagern, gibt sie aber
  normalerweise wieder ab, wie ein Schwamm, der Wasser nur kurz haelt. Wir sagen voraus: Treffen zwei gelagerte Wellen
  aufeinander, faellt eine davon endgueltig in den Ball, so wie Kristalle aus einer uebersaettigten Loesung ausfallen, und
  die andere fliegt mit der ueberschuessigen Energie als schnelle Welle davon, bei einer vorher berechneten Frequenz. Weil
  dafuer zwei Wellen zusammenkommen muessen, waechst der dauerhafte Gewinn mit der vierten Potenz der Wellenhoehe. Fehlt
  die schnelle Welle oder waechst der Gewinn nur quadratisch, ist die Idee falsch.

- Karte geschrieben: 2026-09-30 11:16:09 CEST
- Vorhersage geschrieben: 2026-09-30 11:16:14 CEST
