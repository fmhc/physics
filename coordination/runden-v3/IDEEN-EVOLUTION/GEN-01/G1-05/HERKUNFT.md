# G1-05 Herkunft

- Operator: research. Eltern: Wel 5 (Landau-Schwelle im stabilen chi-Medium). Arm E, Generation 1.
- Bearbeiter: Operator-Agent "aussen" (Anthropic, Opus 5.5). Beginn (date, Gesamtauftrag): 2026-09-30 07:18:19 CEST.

## Erwartung vor dem ersten Suchabruf (geschrieben 2026-09-30 07:27:34 CEST, date)

Die Literatur (Hakim 1997, Pavloff 2002, Leboeuf/Pavloff 2001) kennt fuer 1D-Stroemung um ein endliches Hindernis eine
nichtlineare kritische Geschwindigkeit unter c_s, an der die stationaere Loesung in einem Sattel-Knoten verschwindet;
darueber loest das Hindernis periodisch graue (dunkle) Solitonen ab. Erwartet: Unser u_c < c_s ist damit qualitativ
bekannt; offen bleibt, ob 0,43 und 0,65 c_s mit der exakten Sattel-Knoten-Grenze fuer unser Ballprofil uebereinstimmen.
Laborwerte fuer die kritische Machzahl vermute ich bei Kondensaten (Engels/Atherton 2007) und Polaritonen (Amo 2009).

## Elternbefund (an den Projektdateien gelesen)

- [A] RUNDE-06/medium1d/PLAN.md, 1.1 und 2.1: Medium chi mit mc2 = 1, g4 = 0,5, lam = 0,1; c_s = 0,2085 (C0 = 0,1) und
  0,3216 (C0 = 0,3); Heillaenge 2,24 bzw. 1,29; Ball omega^2 = 0,7 (FWHM 3,56); Delle 37 % bzw. 12 %; hydraulische Grenze
  0,30 bzw. 0,58 c_s; Vorhersage V5b 0,55 +- 0,2 und 0,75 +- 0,15; Messfenster [370, 570], F_MIN = 2e-6, Box 600.
- [A] RUNDE-06/ERGEBNISSE-R6-C.md, M1-W5 und Kernfrage 2.1: u_c/c_s = 0,43 (Klammer 0,38 bis 0,48) und 0,65 (0,59 bis
  0,72); keine scharfe Kante (F steigt stetig ueber fast vier Groessenordnungen); an allen vier Klammerpunkten faellt die
  Kraft im Fenster noch ab (E1 nicht erfuellt); V5d verfehlt (5,77e-6 bei 0,48 c_s).
- Abweichung der Quellen: Der Auftrag und pool.jsonl sagen "Vorhersage 0,55 bzw. 0,75 verfehlt, Richtung getroffen";
  die Ernte R6-C wertet V5b als "getroffen" (beide Werte im Band), verfehlt ist dort V5d. Die Karte stuetzt sich nur auf
  die gemessenen Klammern, nicht auf dieses Urteil.

## L4-Notiz zur Elternkarte: teilweise bekannt

- [L] Hakim, "Nonlinear Schroedinger flow past an obstacle in one dimension", Phys. Rev. E 55, 2835 (1997)
  (Abstract-Seite gelesen; der erste Satz woertlich, der Rest dort nur zusammengefasst): unter einer vom Hindernis
  abhaengigen kritischen Geschwindigkeit stationaere, verlustfreie Stroemung; dort verschwindet die Loesung in einem
  Sattel-Knoten mit einer instabilen Loesung (Uebergangszustand fuer die Abloesung grauer Solitonen); darueber werden
  graue Solitonen wiederholt stromab abgeloest, stromauf laufen dispersive Wellen.
- [L] Kato, Watabe, Phys. Rev. Lett. 105, 035302 (2010), arXiv 1006.2999 (Abstract gelesen): Stabilitaetskriterium mit
  "a dynamical scaling near the saddle-node bifurcation" fuer die Solitonen-Instabilitaet. [L?] Die Form "Rate ~
  sqrt(|V - V_c|)" nur laut Suchtreffer, im PDF-Abruf nicht gefunden; die Karte stuetzt V3 deshalb auf [S]: generische
  Sattel-Knoten-Normalform, Durchgangszeit ~ (u - u_SN)^(-1/2).
- [L] Engels, Atherton, "Stationary and nonstationary fluid flow of a Bose-Einstein condensate through a penetrable
  barrier", Phys. Rev. Lett. 99, 160405 (2007), arXiv 0704.2427 (Abstract und HTML-Fassung gelesen): langsam stationaer,
  mittlere Geschwindigkeit "filled with dark solitons", schneller wieder "remarkable absence of excitation". Zahlen laut
  HTML-Abruf: Barriere "about 24% of the chemical potential", breit gegen die Heillaenge 0,17 um; Schall 3 mm/s in der
  Mitte, gemittelt 2,1 mm/s; Einsatz "above a critical velocity of roughly 0.3 mm/s", "much lower than ... the Landau
  criterion". [S] Daraus Mach etwa 0,10 bis 0,14; die 1D-Hydraulik gaebe fuer beta = 0,24 etwa 0,43. Der Laborwert liegt
  also dreimal tiefer (Hypothese: Queranregungen der elongierten 3D-Wolke, die unser 1D-Modell nicht hat).
- [L] Huynh, Hebert, Albert, Larre, Phys. Rev. A 109, 013317 (2024), arXiv 2305.01293 (Abstract gelesen): geschlossene
  Ausdruecke fuer die kritische Geschwindigkeit einer 2D-Stroemung an einer beliebig durchlaessigen Barriere.
- [L] Aladjidi, Baker-Rasooli, Ferreira, Bramati, Albert, Glorieux, Larre, arXiv 2609.03948 (3. September 2026; Abstract
  gelesen): Lichtfluid in warmem 87Rb-Dampf, 2D, bewegliche abstossende Stoerstelle mit einstellbarem Radius und endlicher
  Masse; kritische Geschwindigkeit ueber drei Messgroessen (Wirbelzahl, Kraft, Relativgeschwindigkeit), "systematically
  below the Landau criterion", faellt mit dem Radius. Zahlen nicht im Abstract. Naechstes Laboranalogon zu unserem
  beweglichen Ball, aber 2D (Wirbel statt Solitonen).
- [L?] Larre, Michel, Cherroret, "Critical speed of a binary superfluid of light", arXiv 2601.16005 (2026): nur
  Suchtreffer, nicht an der Quelle gelesen.
- Bewertung: Mechanismus (Sattel-Knoten, Solitonen, u_c < c_s abhaengig von Hoehe und Breite) ist bekannt. Neu waere
  der quantitative Anschluss an unsere gemessene Schwelle mit dem echten Ballprofil im relativistischen Medium und die
  blinde dritte Dichte. Nicht gefunden: Q-Ball als Hindernis in einem Kondensat mit dieser Frage.

## Papierwerte der Karte [S]

- c_s bei C0 = 0,2: omega0^2 = 1,2, g = 0,2, c_s^2 = 0,2/2,6, c_s = 0,2774; Heillaenge 1/sqrt(0,4) = 1,58; Ball
  3,56/1,58 = 2,25 Heillaengen; beta = 0,1 x 0,368/(1 x 0,2) = 0,184; hydraulisch M = 0,49 (Interpolation zwischen
  M = 0,48 mit 0,196 und M = 0,50 mit 0,180).
- Die Karte nutzt die vorhandene Messung nur als Vergleich mit vorab festgelegter Toleranz (V1); die blinde Probe ist
  C0 = 0,2 (V2, V3), deren Gitter erst aus u_SN folgt.

## Quellenliste (URLs)

- https://journals.aps.org/pre/abstract/10.1103/PhysRevE.55.2835
- https://arxiv.org/abs/1006.2999 und https://arxiv.org/pdf/1006.2999
- https://arxiv.org/abs/0704.2427 und https://arxiv.org/html/0704.2427
- https://arxiv.org/abs/2305.01293
- https://arxiv.org/abs/2609.03948
- https://arxiv.org/html/2601.16005 (nur Suchtreffer)

## Zeiten

- Karte geschrieben 2026-09-30 07:38:50 CEST; Schreibbeginn der Herkunftsdateien 2026-09-30 07:42:58 CEST (date).
- Ende (date): 2026-09-30 07:45:15 CEST. Beginn 07:18:19, also 27 min fuer alle drei Karten.
