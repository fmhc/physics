# KOVARIANZ-KUGEL-1: Vorab-Datei (Kontinuumsvorhersagen, vor jeder Messung)

- Code-Agent fuer die Leitung claude-primary. Geschrieben ab 2026-10-04 14:51 CEST (date 14:51:08), vor den
  Hauptlaeufen und ohne Kenntnis eines verformten Gamma-Werts. Die Zahlen stammen aus `kovarianz.py vorab`
  (.69, 12:50:33 bis 12:50:36 UTC, rc 0; rauch-69/vorab.json): reine Kontinuumsrechnung (eindimensionale Quadratur),
  keine Gitterrechnung.
- Kennzeichen: [M] eigene Mathematik, [L] Literatur aus dem Gedaechtnis, [E-v] numerische Auswertung einer
  Kontinuumsformel (keine Messung), [H] Hypothese.
- Konvention: y = Delta Gamma/sqrt(N) mit Delta Gamma = Gamma(verformt) - Gamma(rund), gepaart je Saat und N.
  Gamma ⊃ B Int sqrt(g) R, beta = 61,56 B = 32 pi^2 a^2/sqrt(N) B. Fuer eine Verformung mit Delta S = Int sqrt(g) R
  - 32 pi^2 a^2 (festes Volumen N) gilt dann **y = beta Delta S_1/(32 pi^2)**, Delta S_1 auf der Einheitskugel. Die
  Vorhersage haengt nicht von N ab.
- Eingang: beta_Q = -1,613 +- 0,052 (Regel Q, Karte; KUGEL-2), Nebenlesart beta_C = -1,455 +- 0,053 (Regel C, korr).

## 1. Schreibtisch: Vorzeichenrechnung des Reviewers

- **Konform, nachgerechnet [M]:** g = e^(2 sigma) g0 auf S^4 vom Radius a. In 4D ist sqrt(g) R = e^(2 sigma)(R0 -
  6 Laplace sigma - 6 |grad sigma|^2) sqrt(g0); partiell integriert Int sqrt(g) R = Int e^(2 sigma)(R0 + 6 |grad
  sigma|^2) dV0 (exakt). Mit sigma = c + tau, Int tau = 0 und festem Volumen (Int e^(4 sigma) = V0, also
  c V0 = -2 Int tau^2 bis zur zweiten Ordnung) wird Delta S = -2 R0 Int tau^2 + 6 Int |grad tau|^2. Fuer tau = Y_l
  (Eigenwert l(l+3)/a^2): **Delta S = (6 l(l+3) - 24)/a^2 Int tau^2**; l = 1: 0, l = 2: 36/a^2. Die Formel des
  Reviewers stimmt. Sie ist die Aenderung von S bis zur zweiten Ordnung; die zweite Ableitung (Besse S'') ist doppelt
  so gross.
  - Numerische Probe [E-v]: l = 2 mit eps = 0,001: Delta S/eps^2 = 1082,35 gegen 36 <Y^2> V0 = 1082,84 (Abweichung
    -4,5e-4, dritte Ordnung). l = 1 (tau = eps cos theta) mit eps = 0,01: Delta S/eps^2 = 0,001 (gegen 0).
- **Spurfrei-transversal (TT) [M]:** fuer g = g0 + h, h TT, auf festes Volumen normiert:
  Delta S = -(1/4) Int <(Nabla*Nabla + 2/a^2) h, h> dV0 (Besse 4.60 in derselben Normierung wie oben; R^ h = -h/a^2
  fuer spurfreie h auf S^4). Kleinste TT-Moden l = 2: Nabla*Nabla = 8/a^2 (Lichnerowicz 16/a^2) [L], also
  **Delta S = -(5/2)/a^2 Int h_ab h^ab < 0**. Mit B < 0 steigt Gamma: die Kugel ist ein Sattel, wie der Reviewer sagt.
- **Fehler in Karte und Review [M]: Die "gestauchte Kugel" ist keine spurfreie (TT-)Verformung.**
  - Ein Ellipsoid ist in Polarform r = a rho(u) mit rho = 1 + eps Y_2 + O(eps^2); seine Metrik ist rho^2 g0 + d rho
    d rho, also in erster Ordnung **konform** mit sigma = eps Y_2. Darstellungstheoretisch: die Stoerung eines
    beliebigen (auch dreiachsigen) Ellipsoids gehoert zur Darstellung (2,0) von SO(5); TT-Tensoren auf S^4 zu (l,2).
    Sie ist also konform plus Eichung; am kritischen Punkt (festes Volumen) traegt die Eichung zur zweiten Ordnung
    nichts bei und die O(eps^2)-Metrikglieder auch nicht (erste Variation null).
  - Rotationsellipsoide sind sogar exakt konform flach (jede O(4)-symmetrische Metrik auf S^4 ist es).
  - **Folge: Einstein sagt fuer die gestauchte Kugel dasselbe Vorzeichen wie fuer die konforme l = 2-Verformung:
    Delta S > 0, Gamma sinkt.** KV2 ("Gamma steigt, entgegengesetzt zu KV1") widerspricht bei der gestauchten Kugel
    der Einstein-Erwartung; trifft Einstein zu, muss KV2 im Kartenwortlaut verfehlt werden.
  - Eine echte TT-Verformung ist nicht konform flach (Weyl-Kruemmung in erster Ordnung). Fuer sie gibt es mit der
    Huellen-Vorschrift kein intrinsisches Netz; ein mitgenommenes Netz traegt einen nicht kovarianten
    Scherterm ~ N eps^2 mit demselben Vorzeichen wie die Einstein-Antwort und etwa sqrt(N)/8-mal so gross (PLAN S4).
    Sie wird deshalb nicht gerechnet.

## 2. Verformungen (Festlegung PLAN Abschnitt 2) und Kontinuumsantworten [E-v]

Alle drei Verformungen sind rotationssymmetrisch um e5, auf Volumen N normiert und konform flach.

| X | Verformung | Parameter | Delta S_1 (Einheitskugel) | Delta S_1/(32 pi^2) | **y_pred (beta_Q)** | y_pred (beta_C, CI) |
|---|---|---|---|---|---|---|
| M | Nullprobe: konformer Faktor eines Moebius-Schubs, sigma = -ln(cosh t + sinh t cos theta) | t = 0,2 | -5,7e-14 (exakt 0) | 0 | **0** | 0 |
| K | konform l = 2: sigma = eps (1 - 5 cos^2 theta) + c | eps = -0,1, c = -0,02707 | +10,857 (zweite Ordnung allein 10,828) | +0,03438 | **-0,0554 +- 0,0018** | -0,0500 +- 0,0018 |
| E | gestauchte Kugel: Rotationsellipsoid, Achsenverhaeltnis q/p = e^(-0,5) | lam = 0,6065 | +8,958 | +0,02837 | **-0,0458 +- 0,0015** | -0,0413 +- 0,0015 |

- Fehler der Vorhersage: nur aus beta (3,2 %); Quadraturfehler < 1e-12.
- Kontrolle E [E-v]: Delta S aus der konformen Karte (Begradigung) und unabhaengig aus den Hauptkruemmungen des
  Ellipsoids (Gauss-Gleichung) stimmen auf 2,3e-13 ueberein; das eingebettete Profil trifft die Ellipse auf 1,3e-14,
  Achsenverhaeltnis 0,60653 = lam.
- Verhaeltnis E/K = 0,825 (beide Einstein-Vorzeichen). Unter der Kartenlesart (spurfrei mit entgegengesetztem
  Vorzeichen) waere E positiv; das ist fuer die gestauchte Kugel keine Einstein-Vorhersage (Abschnitt 1).
- In absoluten Zahlen (Delta Gamma = y sqrt(N)), beta_Q: K -1,75 / -2,48 / -3,51, E -1,45 / -2,05 / -2,89 bei
  N = 1000 / 2000 / 4000.
- Groessenordnung der Kruemmung (beschreibend, von Hand): K hat am Pol R = 1,42 R0, am Aequator 0,64 R0
  (R a^2 = e^(-2 sigma)(12 - 6 Laplace sigma) mit sigma = 0,373 bzw. -0,127); E am Pol 0,31 R0, am Rand 1,55 R0 (nach
  der Volumennormierung). Alle Kruemmungen positiv, Betraege wie beim runden Netz.

## 3. Was als Einstein-Antwort gilt (fuer die Urteile)

- M: y = 0. K: y = -0,0554 +- 0,0018. E: y = -0,0458 +- 0,0015. Gleiche Vorzeichen fuer K und E.
- Kartenwortlaut KV2 erwartet fuer E das entgegengesetzte Vorzeichen; nach Abschnitt 1 ist das fuer die gestauchte
  Kugel falsch. Die Karte bleibt unveraendert; das Urteil nach Kartenwortlaut wird mechanisch gefaellt.
