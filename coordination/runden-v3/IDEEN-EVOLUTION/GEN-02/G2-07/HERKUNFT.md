# G2-07 Herkunft

- Operator: analogie (Operator-Agent "aussen", Anthropic Opus 5.5, frisch). Eltern: Bio 24 "Vielzeller, Verbund mit
  Phasen". Arm E, Generation 2.
- Beginn dieser Karte (date): 2026-09-30 10:57:14 CEST (Gesamtauftrag ab 10:34:03 CEST).

## Erwartung vor dem ersten Suchabruf (geschrieben 2026-09-30 11:00:20 CEST, date)

In der nichtlinearen Optik gibt es "rotierende Solitonen-Cluster" bzw. Halsketten aus N Solitonen mit Phasensprung
2 pi m/N (Desyatnikov/Kivshar 2002, Soljacic/Segev 1998): quasistabil, wenn sich Anziehung (gleichphasig) und
Abstossung (gegenphasig) ausgleichen; im diskreten NLS sind Vierer-Wirbel (Ladung 1 auf vier Plaetzen) fuer schwache
Kopplung stabil (Malomed/Kevrekidis 2001, Pelinovsky/Kevrekidis/Frantzeskakis 2005). Eine Arbeit, die den Vierer-Ring
aus Q-Baellen (relativistisch, frei beweglich) mit einer Wachstumsrate gegen den Abstand vergleicht, erwarte ich nicht.

Nachtrag nach der Suche: Cluster und diskrete Wirbel wie erwartet gefunden; eine Q-Ball-Fassung nicht.

## Elternbefund (an den Projektdateien gelesen)

- [A] RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md, Idee 24: "Drei oder vier Q-Baelle mit passenden Phasen bilden einen stabilen
  Verbund."
- [A] RUNDE-05/ERGEBNISSE-R5-2DA.md, Karte 4 (Zeilen 173 bis 200, 324 bis 327): omega^2 = 0,70 (Q 23,996,
  R_halb 1,916); n4_windung "zusammen" (4 Gebiete, Abstand 8,90 bis 9,98, Q-Verlust 5,1e-4) gegen die Vorhersage
  "kein stabiler Verbund"; gleichphasige verschmelzen bei t = 5, n4_wechsel und n3_windung fliegen auseinander.
- [A] RUNDE-07.md Zeilen 141 und 177: "RING-V: Der Vierer-Ring haelt nur im erzwungenen C4-Sektor", verwerfen (als
  gebundener Verband).
- [A] RUNDE-07/ring/PLAN.md, Abschnitt 4 (Zeilen 274 bis 330): Paarenergie erster Ordnung null bei 90 Grad;
  Josephson-Strom sin(90 Grad) maximal, laeuft im Kreis; Diagonalen stossen schwach ab; Bruch aus Rundung bei etwa
  ln(1e14)/0,07.
- [A] RUNDE-07/ring/lauf-69/ausgabe/vierer_grob_bericht.txt (T = 2000, dx 0,3):
  - n4_windung: Ladungstausch, gamma 0,0534, t_Bruch 543, r Mittel 5,891, Drehrate -3,35e-3
  - n4_windung_sym: gebunden bis 2000, Periode 160
  - s1e-3: Bruch 81,5; s1e-6: Bruch 195, gamma 0,0552
  - l6: gamma 0,0275, t_Bruch 1030, r Mittel 7,595, Drehrate +1,06e-4; l6_sym gebunden (Periode 500)
  - l8_sym: auseinander (Drift +0,333 r0)
  - n4_gleich verschmilzt bei t = 5
- Daraus die Anlass-Zahl der Karte [S]: Steigung -0,275 gegen -kappa/2 = -0,274 bei 0,70 (zwei Punkte, kein Test).
  Mit den Startabstaenden (8,930 und 11,195) waere sie -0,293.

## Kandidaten (je eine Zeile, verschiedene Felder)

1. **Chemie, Hueckel-Aromatizitaet und Jahn-Teller (Cyclobutadien):** Ein 4n-Ring ist antiaromatisch, das Quadrat
   verzerrt sich. Verworfen: Das liefert nur die Symmetrie der instabilen Mode, und die ist gesehen (Tausch zwischen den
   Diagonalpaaren); keine Zahl, die anders ausfallen kann.
2. **Nichtlineare Dynamik und Biologie, verdrillte Zustaende in Ringen gekoppelter Oszillatoren:** Ein q-verdrillter
   Zustand ist nur bei Phasenschritt unter pi/2 stabil; unser pi/2 ist genau der Grenzfall. Vorzeichenregel fuer
   N = 8, w = 2. Nicht gewaehlt, Quelle nicht an der Quelle gelesen [L?] (Wiley, Strogatz, Girvan 2006, aus dem
   Gedaechtnis).
3. **Optik und Kaltatome, diskrete Modulationsinstabilitaet in Gittern (Anti-Kontinuum-Limes):** Tauschrate
   ~ sqrt(J U n). Liefert eine Skalierung mit dem Abstand, deren Steigung von omega abhaengt (-kappa/2). **Gewaehlt.**
4. **Optik, rotierende Solitonen-Cluster:** Phasentreppe erzeugt Drehimpuls und Drehung des Clusters. Moegliche Groesse:
   Drehrate gegen Luecke (bei uns Vorzeichenwechsel von -3,35e-3 bei Luecke 4 zu +1,06e-4 bei Luecke 6). Nicht gewaehlt,
   weil die Drehrate den Zerfall nicht erklaert; als Nebenbeobachtung fuer die Ernte interessant.

## L4-Kurzpruefung

- [L] A. S. Desyatnikov, Y. S. Kivshar, "Rotating optical soliton clusters", Phys. Rev. Lett. 88, 053901 (2002),
  arXiv:nlin/0112039 (Abstract gelesen): Mehr-Solitonen-Bindungszustaende im homogenen Medium, stabilisiert durch eine
  "staircase-like phase distribution that induces a net angular momentum and leads to cluster rotation".
- [L] D. E. Pelinovsky, P. G. Kevrekidis, D. J. Frantzeskakis, "Nonlinear Schroedinger lattices II: Persistence and
  stability of discrete vortices", arXiv:nlin/0411016 (Abstract gelesen): diskrete Wirbel im Anti-Kontinuum-Limes als
  angeregte Knoten auf einer geschlossenen Kontur; Lyapunov-Schmidt-Reduktion; "predict analytically and confirm
  numerically the number of unstable eigenvalues". Wie die kleinen Eigenwerte mit der Kopplung skalieren (Wurzel oder
  linear), steht nicht im Abstract: [L?]. Ob der Vierer-Wirbel mit Schritt pi/2 dort der entartete Fall ist, habe ich
  nicht gelesen; die Karte nennt die lineare Skalierung deshalb nur als Gegenmodell.
- [L] D. A. Zezyulin, "Metastable soliton necklaces confined by the boundary of a flattop region", arXiv:2608.11885
  (12. August 2026, Abstract gelesen): quasistationaere Halsketten im kubisch-quintischen Medium, Abstossung
  gegenphasiger Nachbarn gegen Einschluss; metastabil ueber etwa hundert Beugungslaengen. Naechste neue Arbeit zum
  Thema; dort Einschluss von aussen, bei uns keiner.
- [L?] Die Wurzelskalierung gamma ~ sqrt(J U n) der diskreten Modulationsinstabilitaet (etwa Kivshar und Peyrard 1992,
  Smerzi und Trombettoni 2003) und die Laborbeobachtung in Wellenleiter-Arrays: aus dem Gedaechtnis, nicht an der Quelle
  gelesen. Die Karte stuetzt die Steigung deshalb auf [S]: Linearisierung im Grenzfall J << U n.
- arXiv-API-Suche (Titel "soliton clusters", "discrete vortices", "necklace"): 25 Treffer, keine Q-Ball-Arbeit.
- Bewertung: Mechanismus (Ringe mit Phasentreppe, diskrete Wirbel, Tausch-Instabilitaet) ist bekannt. Neu waere die
  Steigung -kappa/2 fuer frei bewegliche Q-Baelle mit Tunnelkopplung ueber die Schwaenze, bei zwei neuen omega^2.

## Papierrechnung [S]

- Vierer-Ring mit Tunnelkopplung J und Eigen-Nichtlinearitaet U: Mit Phasenschritt pi/2 ist cos = 0. Die Nachbarkraft
  erster Ordnung und der Josephson-Energiebeitrag verschwinden. Im einfachen Nachbarmodell ist die Diagonal-Tauschmode
  (q = 2) in linearer Ordnung neutral. Die gemessene exponentielle Rate kommt also aus Termen jenseits dieses Modells
  (Bewegung, Diagonalkopplung, zweite Ordnung). Dass sie trotzdem wie sqrt(J) skaliert, ist die Hypothese; die zwei
  vorhandenen Punkte stuetzen sie, beweisen sie nicht.
- kappa = sqrt(1 - omega^2): 0,60 -> 0,6325; 0,70 -> 0,5477; 0,80 -> 0,4472. Haelften 0,316 / 0,274 / 0,224.
- Steigung bei 0,70: ln(0,0275/0,0534) = -0,6636; Delta d = sqrt(2) (7,595 - 5,891) = 2,410; -0,275.
- Konsistenz der Saat: s1e-6 mit Spreizung 2,0e-6, t_Bruch 195, gamma 0,0552: ln(0,1/2e-6)/0,0552 = 196.

## Quellenliste (URLs)

- https://arxiv.org/abs/nlin/0112039
- https://arxiv.org/abs/nlin/0411016
- https://arxiv.org/abs/2608.11885
- https://export.arxiv.org/api/query?search_query=ti:%22soliton+clusters%22+OR+ti:%22discrete+vortices%22+OR+ti:%22necklace%22+AND+abs:soliton

## Zeiten

- Karte zuerst geschrieben 2026-09-30 11:01:45 CEST; Satz zur neutralen Tauschmode ergaenzt, letzte Fassung
  11:03:24 CEST; Herkunft ab 11:02:29 CEST (date).
- Ende dieser Karte (date): 2026-09-30 11:03:46 CEST, also 6,5 min ab 10:57:14. Gesamtauftrag 10:34:03 bis 11:03:46
  CEST, rund 30 min fuer alle drei Karten.
