# G2-01 Herkunft

- Operator: research (Operator-Agent "aussen", Anthropic Opus 5.5, frisch). Eltern: G1-03 "Teilung eines m = 2-Balls".
  Arm E, Generation 2.
- Beginn (date): 2026-09-30 10:34:03 CEST (Auftragsbeginn fuer alle drei Karten; diese Karte ab 10:35:42 CEST).

## Erwartung vor dem ersten Suchabruf (geschrieben 2026-09-30 10:35:42 CEST, date)

Die Literatur kennt die azimutale Instabilitaet drehender Wirbel-Solitonen gut: Im kubisch-quintischen NLS (2D) sind
Wirbel mit Windung 1 und 2 oberhalb einer Schwellen-Leistung (flache Kuppe) stabil und zerfallen darunter in Fragmente
ohne Windung. Fuer relativistische Q-Baelle mit Windung in 2+1 D erwarte ich wenige direkte Zahlen; die Schwelle genau in
unserem Potential ist vermutlich nicht veroeffentlicht, aber die Profilgleichung laesst sich vermutlich auf die
CQ-NLS-Profilgleichung abbilden.

Nachtrag nach der Suche: Die Erwartung traf zu. Neu war, wie genau die umgerechnete NLS-Zahl unsere m = 2-Schwelle trifft.

## Elternbefund (an den Projektdateien gelesen)

- [A] GEN-01/G1-03/KARTE.md: Modell L = |psi_t|^2 - |grad psi|^2 - U(S), U(S) = S - S^2 + S^3/2 (Kopf von
  teilung_schwelle.py), Stoerung l = 1 bis 6, Amplitude 0,01, T = 1200.
- [A] GEN-01/G1-03/lauf-69-kopie/lauf-69/teilung_haupt_grob_bericht.txt: m = 2 bei 0,55 (Q 627,9) keine Teilung;
  0,57 (Q 385,8) Teilung bei t = 440, gamma 0,0098; 0,59: 0,0265; 0,61: 0,0403; 0,63: 0,0719; 0,65: 0,0913;
  0,70: 0,1179. "nullpunkt_gamma2": 0,5668. l_dom 2 bis 0,61, 3 ab 0,63. 15 Toechter, alle Windung 0.
- [A] teilung_haupt_fein_bericht.txt: fein gleich (gamma rel. Aenderung <= 2,3e-4). teilung_gegen_grob_bericht.txt:
  m = 0 bei 0,59 keine Teilung, kein gamma.
- [A] GEN-01/ERNTE.md, Zeile G1-03: "weiter"; die Schwelle stuetzt sich auf einen nicht teilenden Punkt; Ladung verlaesst
  nach der Teilung den Suchkasten.
- [A] RUNDE-05/ERGEBNISSE-R5-2DA.md, Zeilen 67 bis 79: m = 1 (T = 600): 0,55 (Q 370,2) keine Teilung; 0,65 (Q 93,9)
  Teilung bei t = 50, gamma 0,0926, 2 Toechter; 0,80 Teilung bei t = 35, gamma 0,1368.
- [A] RUNDE-07/ring/lauf-69/ausgabe/teilung_grob_bericht.txt (RING-T, gleiches Stoerverfahren, T = 3000): m = 1 bei
  0,55 / 0,575 / 0,59 keine Teilung; 0,60 Teilung bei t = 1045, gamma 0,0041; 0,625 bei 75, gamma 0,0641; 0,65 bei 50,
  gamma 0,0925; "schwelle_zwischen": [0,59; 0,6]. fein (T = 1500) gleich; RUNDE-07.md Zeile 140 und 176 (parken).
- **Berichtigung des ersten Entwurfs (10:43 bis 10:47):** Die erste Fassung der Karte sagte die m = 1-Schwelle "blind"
  vorher (Band [0,598; 0,616]). Um 10:46 fand ich RING-T: Die m = 1-Schwelle ist schon gerechnet (0,59 bis 0,60). Die
  Vorhersage waere aus vorhandenen Dateien ableitbar gewesen und haette RING-T gedoppelt. Die Karte sagt jetzt m = 3
  vorher; m = 1 und m = 2 dienen nur der Eichung. Keine m = 3-Zeitentwicklung in runden-v3 gefunden (grep "m3_",
  "m = 3 bei", "m=3": nur REGGE-Energien bei omega^2 = 0,990).

## L4-Notiz zur Elternkarte: teilweise bekannt

- [L] R. M. Caplan, R. Carretero-Gonzalez, P. G. Kevrekidis, B. A. Malomed, "Existence, stability, and dynamics of
  bright vortices in the cubic-quintic nonlinear Schroedinger equation", Math. Comput. Simulat. 82, 1150 (2012),
  arXiv:0910.5758 (Volltext v3 gelesen, S. 1 bis 12 und 16 bis 18):
  - Modell Gl. (1): i Psi_t + Laplace Psi + |Psi|^2 Psi - |Psi|^4 Psi = 0; Ansatz Psi = f(r) e^{i(m theta + Omega t)}
    (Gl. 2, 3); Profilgleichung Gl. (4); Existenz 0 < Omega < 3/16; Kuppe f0 = sqrt(3/4).
  - S. 2: "the critical frequencies were found as Omega_st(m = 1) ~ 0.16 and Omega_st(m = 2) ~ 0.17" (Refs. 10, 23,
    36), Ref. 31 fand Omega_st(m = 1) ~ 0.145.
  - Tabelle II (S. 11), woertlich: m = 1: NUM 0,147, Ref. [27] 0,1487, Ref. [23] 0,16, Ref. [31] 0,145; m = 2: NUM
    0,162, [27] 0,1619, [23] 0,17; m = 3: NUM 0,171, [27] 0,1700; m = 4: (0,178), [27] 0,1769; m = 5: (0,18), [27]
    0,1806. "The predictions made in Ref. [27] are the most accurate ones, in comparison to our simulations."
  - Verfahren NUM (S. 10 f., Fig. 11): Omega_1 zerfaellt, Omega_2 = Omega_1 + 0,001 bleibt bis t = 50 000 stabil;
    fuer m = 1 also Omega_st in [0,146; 0,147]. Fuer m = 1, 2, 3 "easily able to identify the transition", fuer m > 3
    stoert eine Schlangen-Instabilitaet.
  - Fig. 9 zeigt lambda_max nur fuer Omega von 0,03 bis 0,14; zur 0,14 hin fallend, dort (aus der Grafik abgelesen)
    etwa 0,01 bis 0,03 in NLS-Zeiteinheiten. Die Form des Abfalls an der Grenze selbst zeigt die Arbeit nicht.
- [L] R. L. Pego, H. A. Warchall, "Spectrally stable encapsulated vortices for nonlinear Schroedinger equations",
  J. Nonlinear Sci. 12, 347 (2002), arXiv:nlin/0108009 (nur Abstract gelesen): spektral stabile drehende Wellen fuer
  kubisch-quintische Nichtlinearitaet, instabile Eigenwerte als Nullstellen von Evans-Funktionen, "spectrally stable
  standing waves having central vortex of any degree". Die Zahlen 0,1487 / 0,1619 / 0,1700 habe ich nur in Caplan u. a.
  Tabelle II gelesen, nicht im Volltext von Pego und Warchall.
- [L?] Towers, Buryak, Sammut, Malomed, Crasovan, Mihalache, Phys. Lett. A 288, 292 (2001) und Malomed, Crasovan,
  Mihalache, Physica D 161, 187 (2002): nur als Refs. 36 und 23 aus Caplan u. a. bekannt, nicht an der Quelle gelesen.
- [L] N. Siemonsen, W. E. East, "Stability of rotating scalar boson stars with nonlinear interactions", Phys. Rev. D
  103, 044022 (2021), arXiv:2011.08247 (Abstract gelesen): mit Gravitation und 3D; die m = 1-Instabilitaet
  nicht-achsensymmetrischer Art laesst sich durch nichtlineare Wechselwirkung in Teilen des Parameterraums
  unterdruecken; m = 2-Sterne waren dort alle instabil, Zerfall u. a. in mehrere ungebundene Sterne. Kein Zahlenvergleich
  mit unserem flachen 2D-Modell.
- Nichts gefunden: Arbeit zur azimutalen Stabilitaetsgrenze relativistischer (Klein-Gordon-)Q-Baelle mit Windung in
  2+1 D fuer dieses Potential. arXiv-API: abs:"spinning Q-balls" (15 Treffer 2002 bis 2024, Titel und Abstracts der
  Liste; nur Arodz u. a. 0907.2801 ist 2+1 D, signum-Gordon, ohne Stabilitaetsschwelle im Abstract);
  abs:"Klein-Gordon" AND vortex AND quintic: 0 Treffer; au:Kinach (drei Arbeiten zu geeichten Q-Baellen, ohne
  Drehung). Die 24-Monats-Suche ist damit nur ueber arXiv-Abstracts gemacht, nicht erschoepfend.
- Bewertung: Der Mechanismus (azimutale Modulationsinstabilitaet, Stabilisierung grosser Wirbel mit flacher Kuppe,
  Toechter ohne Windung) ist bekannt. Neu fuer uns: Unsere Profilfamilie ist exakt die CQ-NLS-Familie mit
  Omega = (3/8)(1 - omega^2) [S]. Die umgerechneten Grenzen liegen knapp ueber unseren gerechneten Schwellen: m = 1
  Evans 0,6035 gegen 0,59 bis 0,60 (RING-T), m = 2 Evans 0,5683 gegen gamma^2-Nullpunkt 0,567. Ob das fuer die
  relativistische Dynamik allgemein gilt, ist offen; dafuer die blinde m = 3-Zahl.

## Papierrechnung der Karte [S]

- Einsetzen f = a g, r = b rho in f'' + f'/r - m^2 f/r^2 - (1 - omega^2) f + 2 f^3 - (3/2) f^5 = 0 und Multiplikation mit
  b^2/a: Koeffizienten 2 a^2 b^2 (bei g^3) und (3/2) a^4 b^2 (bei g^5) gleich 1 setzen: a^2 b^2 = 1/2, a^2 = 4/3,
  b^2 = 3/8; dann Omega = (1 - omega^2) b^2 = (3/8)(1 - omega^2).
- Ladung: rho = 2 omega f^2, Q = 2 omega a^2 b^2 Int g^2 d^2rho = omega N.
- Umrechnung: 8/3 x 0,1487 = 0,3965 -> 0,6035; 8/3 x 0,146 = 0,3893 -> 0,6107; 8/3 x 0,147 = 0,392 -> 0,608;
  8/3 x 0,1619 = 0,4317 -> 0,5683; 8/3 x 0,161 = 0,4293 -> 0,5707; 8/3 x 0,162 = 0,432 -> 0,568;
  8/3 x 0,1700 = 0,4533 -> 0,5467; 8/3 x 0,171 = 0,456 -> 0,544.
- Linearisierung: psi = e^{-i omega t}(f e^{i m theta} + eta), eta = A e^{i(m+L)theta} e^{lambda t} +
  conj(B) e^{i(m-L)theta} e^{conj(lambda) t}: Klein-Gordon gibt (lambda^2 - 2 i omega lambda) bei A und
  (lambda^2 + 2 i omega lambda) bei B, der statische Teil ist nach der Umskalierung der NLS-Teil. Nur bei lambda = 0 sind
  beide Probleme gleich. Daraus: gleiche Schwelle nur, wenn die Stabilitaet ueber einen Nulldurchgang kippt [Hypothese].
- Eichung: m = 1 gamma^2 bei 0,60 = 1,68e-5, bei 0,625 = 4,11e-3; Sehne gibt Nullpunkt 0,5999, mit der flachen
  m = 2-Steigung nahe der Schwelle (0,030) 0,5994; gegen Evans 0,6035 also -0,0036 bis -0,0041. m = 2: Sehne
  0,57/0,59 gibt 0,5668; gamma^2 ist nach oben gekruemmt (Sehnensteigungen 0,030 / 0,046 / 0,177 zwischen 0,57 und
  0,63), der wahre Nullpunkt liegt also hoechstens bei 0,5668; gegen Evans 0,5683 also hoechstens -0,0015.
- Band m = 3: 0,5467 - [0; 0,006] = [0,5407; 0,5467], mit 0,001 Rand [0,540; 0,548]. Die Simulationsklammer
  (0,544 stabil, 0,5467 instabil) liegt darin.
- Laufzeit geschaetzt aus G1-03 (grob 65,2 s fuer 7 Laeufe bis T = 1200, also 0,0078 s je Lauf und Zeiteinheit bei
  n = 256; fein 175,6 s fuer 4 Laeufe, 0,037 s bei n = 384; Schiessen 57 bis 74 s), Flaechenfaktor (48/38,4)^2 = 1,56:
  6 m = 3-Laeufe grob bis 2400 etwa 175 s, 2 m = 2-Laeufe etwa 37 s; 2 feine m = 3-Laeufe etwa 275 s.

## Suchweg

- WebSearch zweimal abgelehnt (Sitzungsbudget 200 von 200 verbraucht). Stattdessen WebFetch auf die arXiv-API und auf
  Abstract-Seiten; das PDF von arXiv:0910.5758 wurde geladen und seitenweise gelesen.

## Quellenliste (URLs)

- https://arxiv.org/abs/0910.5758 und https://arxiv.org/pdf/0910.5758 (v3)
- https://arxiv.org/abs/nlin/0108009
- https://arxiv.org/abs/2011.08247
- https://export.arxiv.org/api/query?search_query=abs:%22cubic-quintic%22+AND+abs:vortex+AND+abs:stab*
- https://export.arxiv.org/api/query?search_query=abs:%22spinning+Q-balls%22
- https://export.arxiv.org/api/query?search_query=au:Kinach

## Zeiten

- Erste Fassung (m = 1) 2026-09-30 10:43:08 CEST; nach dem RING-T-Fund neu geschrieben ab 10:47:34; letzte Fassung
  und Zeile "Karte geschrieben" 2026-09-30 10:48:29 CEST (date).
- Herkunft geschrieben ab 2026-09-30 10:44:10 CEST. Ende dieser Karte (date): 2026-09-30 10:49:10 CEST, also
  13,5 min ab 10:35:42.
