# INDUZIERT-1: Erzeugt ein Materiefeld auf dem Laengennetz Einsteins Steifigkeit von selbst? (Sakharov, Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 05:21:13 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn: "Ideate drei Überleitungen zu einer emergenten Theorie".
  - Ueberleitung 1 (RUNDE-37/UEBERLEITUNGEN-EMERGENZ.md): Schwerkraft als Echo der Materie.
  - In REGGE-4D-1, REGGE-RAND-1, REGGE-SCHAUM-1 und REGGE-WELLE-1 war Regges Wirkung hineingesteckt. Hier soll sie aus
    dem Zittern eines Feldes auf dem Netz entstehen.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Materie:**
  - Freies Skalarfeld phi auf den Knoten, lineare finite Elemente (P1) auf jedem Simplex:
    S[phi; l] = 1/2 sum_sigma V_sigma sum_ab (grad lambda_a . grad lambda_b)_sigma phi_a phi_b, optional mit kleiner
    Masse (konzentrierte Massenmatrix).
  - Die Wirkung haengt nur von den Kantenlaengen ab (Gram-Matrix je Simplex).
- **Induzierte Wirkung:** Gamma[l] = 1/2 log det K(l) (euklidisch, eine Schleife).
  - Gemessen wird ihre zweite Variation um das flache Netz.
  - Im Impulsraum ist das eine Blasensumme ueber die Brillouin-Zone:
    Pi(k) = 1/2 Tr(G K2) - 1/2 Tr(G K1 G K1), mit G = K0^-1.
  - K1 und K2 sind die erste und zweite Ableitung der Steifigkeitsmatrix nach den Kantenlaengen.
- **Erwartung im Kontinuum [L Sakharov 1967; Visser 2002]:**
  - Gamma enthaelt ein Volumenglied (Vakuumenergie) und ein Kruemmungsglied mit positivem G.
  - Nur diese beiden sind bei zwei Ableitungen moeglich, wenn die Materie nur die Geometrie sieht. Dann gilt
    c0s/c2 = -2, die 1/2.
- **Auf dem Gitter [M/H]:**
  - Das feste Netz bricht die Umbenennung, denn Knotenverschiebungen im flachen Raum aendern die Diskretisierung.
  - Die Vakuumenergie je Zelle haengt von der Zellform ab und nicht vom Volumen; die Zahl der Moden je Zelle ist fest.
    Sie ist deshalb per Gegenterm abzuziehen (= Problem der kosmologischen Konstante).
  - Offen ist, ob danach der k^2-Teil Einsteins Struktur hat.
- **2D-Kontrolle [L Polyakov 1981; diskret L? Kokotov 2013]:**
  - Fuer einen masselosen Skalar ist die Steifigkeit der konformen Mode universell, und zwar fuer m << k << 1:
    1/2 log det aendert sich um -(1/(24 pi)) int |grad sigma|^2.
  - Im Gitter gilt delta l_ij / l_ij = (sigma_i + sigma_j)/2.
- **Vermutung [M?]:** Auf dem flachen Kuhn-Netz ist die P1-Steifigkeit gleich dem Wuerfelgitter-Laplace
  sum_mu 4 sin^2(q_mu/2). Die Diagonalkanten haetten dann Gewicht null (rechte Diederwinkel). Zu pruefen.

## Test (Code-Agent)

- **Teil A (2D, Kontrolle):**
  - Rechtwinklige Dreiecke (Quadrate mit einer Diagonale), Torus L x L, masselos mit entfernter Nullmode.
  - Konforme Mode bei k = 2 pi n/L, Steifigkeit pro Flaeche geteilt durch k^2, gegen -1/(24 pi).
  - Beschreibend: Steifigkeit der zwei Knotenverschiebungs-Moden.
- **Teil B (4D):**
  - Kuhn-Netz und Auswertungskette aus RUNDE-36/regge-4d-1/code/regge4d.py:
    - 15 Kanten je Knoten
    - Metrikabbildung
    - Schur-Komplement der Gittermoden
    - Spin-Projektoren, c2 und c0s
  - Pi(k) fuer mehrere Richtungen und kleine abs(k) (Blasensumme auf feinem q-Gitter).
  - Gegenterm: Pi(0) vor Ort abziehen. Der Agent legt im Plan fest, ob ganz oder nur der Metrik-Teil, und begruendet
    es.
  - Dann wie in REGGE-4D-1: c2, c0s/c2 und die Steifigkeit der vier Knotenverschiebungs-Moden.
  - Zusaetzlich: Pi(0) gegen die zweite Variation des 4-Volumens.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IN0 | Kontrollen 4D: P1-Symbol des flachen Kuhn-Netzes = sum_mu 4 sin^2(q_mu/2) auf <= 1e-12; Pi(k) hermitesch auf <= 1e-9 (relativ) | 70 % |
| IN1 | Teil A (2D): Steifigkeit der konformen Mode pro Flaeche und k^2 = -1/(24 pi) auf 3 % beim kleinsten ausgewerteten k im Fenster m << k << 1 | 55 % |
| IN2 | Teil B: Die induzierte Spin-2-Steifigkeit c2 ist positiv, mit demselben Vorzeichen wie in REGGE-4D-1 | 60 % |
| IN3 | [H] Teil B: Nach dem Gegenterm gilt c0s/c2 = -2 auf 10 % (k -> 0), also Einsteins 1/2 aus Materie | 25 % |
| IN4 | [H] Teil B: Nach dem Gegenterm sind die vier Knotenverschiebungs-Moden weich: Steifigkeit <= 5 % der Spin-2-Steifigkeit bei abs(k) = 0,2 (je Einheit Kantenlaengen-Aenderung) | 25 % |
| IN5 | [H] Teil B: Pi(0) weicht in Metrik-Komponenten um mehr als 10 % (relative Frobenius-Norm) von einem Vielfachen der zweiten Variation des 4-Volumens ab | 70 % |

**Bedeutung (vorab):**
- **IN3 und IN4 treffen ein:** Ein Materiefeld auf Finns Laengennetz erzeugt Einsteins Steifigkeit von selbst, bis
  auf die Vakuumenergie. Regges Wirkung muesste nicht hineingesteckt werden. Ueberleitung 1 waere rechnerisch offen.
- **IN3 oder IN4 verfehlt:** Das feste Netz bricht die Umbenennung auch bei langen Wellen.
  - Materie allein waehlt die 1/2 dann nicht.
  - Ue1 braucht dann eine Materie-Diskretisierung, die selbst umbenennungsfrei ist (Hinweis auf Pachner-invariante,
    spinschaum-artige Bauweisen; vgl. PONZANO-1).
- **IN5 trifft ein:** Die Vakuumenergie gibt dem Graviton ohne Gegenterm eine Gittermasse. Sie muss feinabgestimmt
  werden, wie die kosmologische Konstante.
- **IN1 verfehlt:** Die Kette ist nicht richtig normiert; dann Teil B nur beschreibend werten.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min. Wenn Teil B nicht fertig wird: Teil A abgeben, Teil B als "nicht gerechnet" mit Grund.
