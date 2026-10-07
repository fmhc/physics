# KOVARIANZ-KUGEL-1: Plan (Code-Agent, Runde 41)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 14:19:28 CEST (date). Lesen und Schreibtisch bis etwa
  14:45, code/kovarianz.py bis 14:50:45 CEST (Rundungsschranke der Profilpruefung nach dem Vorab-Lauf), Vorab-Lauf
  12:50:33 UTC, Kontrolle und Rauchlaeufe 12:50:55 bis 12:52:19 UTC (.69), Codeprobe danach; letzte Codeaenderung
  14:56 CEST (nur Auswertung: unvollstaendige Saaten, Abschnitt 11). Plantext ab 14:54 CEST.
- **Grundlage:** KARTE.md (KV0 bis KV3, Wahrscheinlichkeiten und Bedeutung unveraendert, Abschnitt 7);
  weltmodell-review-1/REVIEW.md Abschnitt 5 Punkt 2 und 4 K-B; induziert-kugel-1/, induziert-kugel-2/ (code/kugel2.py,
  PLAN, ERGEBNIS); induziert-xi-kugel-1/ERGEBNIS.md; kugel-gegenlesen/GEGENLESEN.md (A2: Ellipsoid als Huelle nicht
  sauber); induziert-dichte-4d/ERGEBNIS.md (Torus: Kippen, sp-Regel, Konvexitaet des festen Netzes).
- **Code:** code/kovarianz.py (neu; Modi vorab, kontrolle, messung, auswertung). Unveraendert kopiert und importiert
  (sha256 gleich den eingefrorenen KUGEL-2-Fassungen): kugel.py (c2a4d790...), kugel2.py (15dcbd85...), dichte4d.py
  (2881048e...), induziert.py (b3867eac...), zufall2d.py (37a0fe8f...).
- **Vorab-Datei:** VORAB.md (Kontinuumsvorhersagen mit Fehler, vor jeder Messung).
- Kennzeichen: [M] eigene Mathematik, [ES] eigener Schluss, [F] Festlegung dieses Plans, [K] Kartenpunkt (vor dem
  Einfrieren offengelegt), [H] Hypothese, [E] in Kontrolle oder Rauchlauf gerechnet (blind: keine Gamma-Werte).

## 1. Schreibtisch (vor jeder Messung)

| Nr | Punkt | Befund |
|---|---|---|
| S1 | Vorzeichenformel des Reviewers | Richtig [M]: Delta S = (6 l(l+3) - 24)/a^2 Int sigma^2 fuer konforme Verformungen bei festem Volumen (Aenderung bis zur zweiten Ordnung; Herleitung und numerische Probe in VORAB.md Abschnitt 1) |
| S2 | Spurfreie (TT-)Verformung | Delta S = -(1/4) Int <(Nabla*Nabla + 2/a^2) h, h>, fuer l = 2: -(5/2)/a^2 Int h_ab h^ab < 0 [M]; Gamma steigt bei B < 0 (Sattel) |
| S3 | **Kartenfehler: "gestauchte Kugel" ist nicht spurfrei** | Die Ellipsoid-Stoerung ist konform plus Eichung (Darstellung (2,0) von SO(5), TT-Tensoren (l,2)); Rotationsellipsoide sind exakt konform flach. Einstein sagt fuer die gestauchte Kugel Delta S > 0 voraus, also **Gamma sinkt wie bei KV1** (VORAB.md: y_E = -0,0458 +- 0,0015). KV2 im Kartenwortlaut kann bei Einstein nur verfehlt werden [M] |
| S4 | Mitnehmen oder neu bauen? | **Neu bauen [F].** Eine Dichte-l = 2-Aenderung verlangt eine nicht konforme Punktverschiebung (Scherung bis 3 abs(eps) sin^2 theta; der Gradientenfluss ist minimal). Ein mitgenommenes Netz ist dann im neuen Mass geschert; ein festes Netz unter Scherung h aendert Gamma um etwa + N tr(h^2)/24 (Impulsraum-Abschaetzung mit festem Schnitt [ES]). Fuer K waere das ~1,4 N eps^2 gegen ein Signal ~5,5 eps^2 sqrt(N): 8- bis 22-mal groesser und mit entgegengesetztem Vorzeichen. Neu bauen ist kovariant (Punkte sind eine Stichprobe der Dichte 1 in g); Preis: Kippen (Rauchlauf: 53 bis 63 % neue Simplizes bei K und E), also fast ungepaarte Netze |
| S5 | Welche Huelle? | Jede O(4)-symmetrische Metrik auf S^4 ist konform flach [M]. In der konformen Karte ist die konvexe Huelle das Delaunay-Netz bezueglich der konformen Struktur (leere runde Kugeln; Moebius-invariant), also fuer diese g intrinsisch. Die Huelle der Punkte auf dem Ellipsoid selbst waere es nicht (GEGENLESEN A2, Scherung in erster Ordnung) |
| S6 | Laengenregel | **QI [F]:** Sehnen in R^5 der isometrischen Einbettung als Rotationshyperflaeche (eindeutig bis auf Verschiebung laengs e5), je Simplex auf das g-Volumen seines Grosskreis-Simplex in der konformen Karte skaliert; fuer g = g0 genau Regel Q. Immer einbettbar (echte Abstaende). Konforme Sehnen e^((s_i + s_j)/2) abs(u_i - u_j) waeren genau Moebius-kovariant, aber nicht einbettbar: Kontrolle C4 findet 27 (K) und 26 (E) nicht einbettbare Simplizes bei N = 1000 [E]. Nebenlesart **CI**: dieselben Sehnen ohne Skalierung, Fassung korr (wie Regel C) |
| S7 | Was die Nullprobe prueft | **Vorab ableitbar [M, E]:** Fuer den Moebius-Schub ist die monotone Umordnung in theta genau die Moebius-Abbildung (C2: 4e-14), die Huelle kombinatorisch gleich (Moebius-Invarianz) und die Einbettung die runde Kugel (Punkte gleich auf 4e-14). CI ist dann exakt null (C2: 2e-12). Die Nullprobe (QI) prueft also nur die Volumenzuordnung je Simplex (Grosskreis-Simplex in der konformen Karte haengt von der Wahl der runden Metrik in der Konformklasse ab) und die Numerik, nicht Transport und Netz |
| S8 | Signal und Rauschen | Signal y_K = -0,0554, y_E = -0,0458 (VORAB.md). Rauschen: Rauchlauf (blind, 2 bis 3 Saaten) Std y je (Saat, N) 0,09 bis 0,34 fuer K und E, 0,001 bis 0,002 fuer M. Erwartung bei voller Entkopplung etwa 0,24 (Std eines Netzes 0,17 sqrt(N), KUGEL-1). Mit dem Mittel ueber drei N je Saat etwa 0,14; fuer 3 SE bei K braucht es etwa 60 Saaten, fuer 5 SE etwa 160 [ES] |
| S9 | N und Fit | N = 1000, 2000, 4000 (N = 8000 kostet je Saat etwa 250 s; nicht im Budget). Die Vorhersage y ist N-unabhaengig. Hauptschaetzer ist das Saatmittel des N-Mittels (Konstantenfit); der Zweiparameterfit y = b + d/sqrt(N) vergroessert die SE bei diesen N um den Faktor 3,7 und wird beschreibend berichtet. Rechtfertigung: Beim runden Netz war y(N) ueber 1000 bis 8000 auf +-0,05 flach (KUGEL-1/-2) |

## 2. Konstruktion (code/kovarianz.py) [F]

- **Rundes Netz:** k1.kugelnetz(4, N, saat) und Regel Q genau wie kugel2.eine_messung (Gamma_Q roh), dazu Regel C
  (korr). Fuer die Saaten 0 bis 39 muss Gamma_Q und Gamma_C bitgleich mit KUGEL-2 sein (K0).
- **Verformungen** (alle um die Achse e5, in der konformen Karte g = e^(2 sigma(theta)) g0, auf Int e^(4 sigma) dV0 = V0
  normiert; sigma als kubischer Hermite-Spline auf 8193 Gitterpunkten):
  - M (KV0): sigma = -ln(cosh t + sinh t cos theta), t = 0,2 (Moebius-Schub, isometrisch).
  - K (KV1): sigma = eps (1 - 5 cos^2 theta) + c, eps = -0,1. Vorzeichen: Fuer eps > 0,05 ist das Profil nicht als
    Rotationshyperflaeche einbettbar (negative Kruemmung am Pol); eps = -0,1 ist ueberall einbettbar [M].
  - E (KV2, Kartenwortlaut "gestauchte Kugel"): Rotationsellipsoid mit Halbachsen p (vierfach) und q = lam p,
    lam = e^(-0,5) = 0,607 (gestaucht laengs e5); konforme Karte durch Begradigung d theta~/sin theta~ = d l/s
    (Spiegelsymmetrie: theta~(pi/2) = pi/2). Staerke wie K (Spanne von sigma 0,5).
  - Je Verformung nur ein Vorzeichen (einseitig); die erste Ordnung ist im Kontinuum null und traegt nur Rauschen bei.
- **Punkte:** dieselben Zufallspunkte wie das runde Netz; theta' = F_g^-1(F_0(theta)) (monotone Umordnung, Newton auf
  zellweiser 10-Punkt-Gauss-Legendre-Quadratur, Rest <= 1e-10 Pflicht), Breitenrichtung w unveraendert. Dichte in g = 1.
- **Netz:** konvexe Huelle der verschobenen Punkte auf der Kugel vom Radius a (konforme Karte), mit allen Pruefungen von
  kugel.kugelnetz (Topologie, Euler 2, Facetten gepaart, leere Kappen, Normalen).
- **Laengen:** Einbettung y = a (s(theta') w, z(theta')) mit s = e^sigma sin theta, z' = -sqrt(e^(2 sigma) - s'^2)
  (Mittelpunkt bei z = 0); Sehnen^2 je Kante. QI: Sehnen^2 mal sqrt(V_g/V_Sehnen) je Simplex, V_g = flaches
  Koordinatensimplex mal Grundmann-Moeller-Mittel (Grad 5) von J e^(4 sigma). CI: Sehnen^2 unveraendert.
- **Gamma:** k1.auswerten (duenne LU, wie KUGEL-1/-2). QI roh, CI korr (V_ziel = V_K = N).

## 3. Messgroesse und Fit [F]

- Je Saat j, N und Verformung X: y_j(N) = (Gamma_X - Gamma_rund)/sqrt(N); QI gegen Q (roh), CI gegen C (korr).
- Je Saat ybar_j = Mittel ueber N = 1000, 2000, 4000 (nur Saaten mit allen drei N). **b_X = Mittel der ybar_j,
  SE = Std(ybar_j, ddof 1)/sqrt(M).**
- Beschreibend: y je N (Mittel, SE), Zweiparameterfit je Saat (b, d), Anteil negativer Saaten, b/y_pred, Abstand zur
  Vorhersage in kombinierten SE, Kippanteile, Volumen- und Transportdaten.

## 4. Saaten, N, Laeufe [F, nach dem Rauchlauf; Zeitregel vorher notiert]

- N = 1000, 2000, 4000; **Saaten 0 bis 119** (0 bis 39 dieselben wie KUGEL-1/-2). Rauchzeit je Saat 5,5 / 13,4 /
  39 s, also etwa 6950 s Rechenzeit, auf drei Spuren etwa 40 min.
- .69, /home/fmh/fmhc-physics-remote/runde41-kovarianz-kugel/lauf/, nur ueber kleintest.sh, Spuren cpu3, cpu4, cpu5, je
  Spur eine Kette nacheinander (ein ssh je Spur). Laeufe (je <= 8 min geplant):
  - cpu3: kontrolle; N = 4000 Saaten 0-10, 11-21, 22-32, 33-43; N = 2000 Saaten 0-29; N = 1000 Saaten 0-59.
  - cpu4: N = 4000 Saaten 44-54, 55-65, 66-76, 77-87; N = 2000 Saaten 30-59.
  - cpu5: N = 4000 Saaten 88-98, 99-109, 110-119; N = 2000 Saaten 60-89, 90-119; N = 1000 Saaten 60-119.
  - Ausgabe lauf/messung-N<N>-s<saat0>.json, jeder Lauf schreibt nach jeder (Saat, N).
- **Abbruch [F]:** Letzter Start spaetestens 15:55 CEST. Nicht fertige (Saat, N) fehlen; Saaten ohne alle drei N fallen
  aus dem Fit (offengelegt).
- Danach: kovarianz.py auswertung lauf /home/fmh/fmhc-physics-remote/runde40-induziert-kugel2/lauf lauf/auswertung.json.

## 5. Tor [F]

- Je (Saat, N): rundes Netz gueltig (kugel_gueltig, LU fuer Q und C), jede Verformung gueltig (Huellenpruefungen,
  LU fuer QI und CI, Transportrest <= 1e-10, Profil einbettbar). Eine Saat mit einem Fehler bei irgendeinem N wird
  ausgeschlossen und gezaehlt.
- Tor bestanden, wenn mindestens 20 Saaten gut sind und hoechstens 10 % der vollstaendigen Saaten ausgeschlossen;
  sonst KV0 bis KV3 "nicht auswertbar (Tor)". Unvollstaendige Saaten (Zeitgrenze) zaehlen nicht als ausgeschlossen.
  Kontrollen (Abschnitt 8) muessen ihre Schwellen erfuellen.

## 6. Vorhersagen der Karte (unveraendert) und Urteilsregeln (mechanisch in kovarianz.py auswertung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KV0 | Nullprobe: Die l = 1-Umbenennung gibt eine Antwort innerhalb von 2 SE um null | 60 % |
| KV1 | [H] Konforme l = 2-Verformung: Gamma sinkt (Vorzeichen wie Einstein mit B < 0), mit >= 3 SE | 55 % |
| KV2 | [H] Spurfreie volumentreue Verformung: Gamma steigt (entgegengesetzt zu KV1), mit >= 3 SE | 45 % |
| KV3 | [H] Beide Antworten treffen die Kontinuumsvorhersage aus dem gemessenen B innerhalb von 30 % | 25 % |

Alle Urteile auf Regel QI (Hauptlesart); CI wird mit denselben Regeln beschreibend berichtet.
- **KV0** (M): Karte = Plan: eingetroffen, wenn abs(b_M) <= 2 SE_M; sonst nicht eingetroffen. Mitberichtet:
  b_M/y_pred,K (Groesse gegen das K-Signal). Kein Wesentlichkeitsrabatt: Die SE von M ist sehr klein (kein Kippen), schon
  ein kleiner systematischer Rest kann KV0 verfehlen lassen; das ist der Kartenwortlaut.
- **KV1** (K): Karte = Plan: eingetroffen, wenn b_K <= -3 SE_K.
- **KV2** (E, gestauchte Kugel): Karte = Plan: eingetroffen, wenn b_E >= +3 SE_E. Vorab [M, S3]: Einstein sagt das
  Gegenteil voraus. Zusatzzeile (kein Kartenurteil): "Einstein-Lesart" b_E <= -3 SE_E.
- **KV3**: Karte = Plan: eingetroffen, wenn abs(b_K/y_pred,K - 1) <= 0,3 und abs(b_E/y_pred,E - 1) <= 0,3
  (Punktschaetzer, y_pred aus VORAB.md mit beta_Q, Vorzeichen der Einstein-Rechnung). Mitberichtet: Vertraeglichkeit
  innerhalb 2 kombinierter SE je Verformung.
- Bei nicht bestandenem Tor: alle "nicht auswertbar (Tor)".

## 7. Bedeutung (Karte, unveraendert)

"Trifft die Vorhersage, ist die 1/2 im induzierten Glied auf diesem Netz erstmals entstanden statt eingesetzt
(euklidisch) und die Torus-Frage erledigt. Verfehlt sie (Nullkontrolle, Vorzeichen, Verhaeltnis), ist Schwerkraft aus
Materie in 4D auf diesem Netz nicht Einstein." Vorab-Einschraenkung [M, S3/S5]: Alle hier baubaren Verformungen sind
konform flach; die Spin-2-Struktur (TT) wird nicht geprueft.

## 8. Kontrollen (Schwellen vor dem Lauf)

- **C1 (sigma = 0):** Pipeline gibt das runde Netz (0 neue Simplizes) und Gamma_QI - Gamma_Q <= 1e-8, CI korr - C korr
  <= 1e-8 (N = 1000, Saat 991). Rauch: 0, 6,8e-13, 1,6e-12 [E].
- **C2 (Moebius):** Transport gegen exakte Moebius-Abbildung <= 1e-10, Netz gleich, Punkte gleich <= 1e-10,
  CI korr - C korr <= 1e-8. Rauch: 4,3e-14, gleich, 4,0e-14, 2,3e-12 [E].
- **C3 (LU gegen dicht, N = 400, Saat 990, M/K/E, QI):** <= 1e-8. Rauch: <= 6,3e-13 [E].
- **C4 (Negativprobe konforme Sehnen):** K und E nicht einbettbar (> 0), M 0. Rauch: 27, 26, 0 [E].
- **Vorab-Proben:** Delta S_M <= 1e-9 (5,7e-14), Ellipsoid Gauss gegen konform <= 1e-8 (2,3e-13), Profil <= 1e-9
  (1,3e-14), Volumennormierung <= 1e-12 [E-v].
- **In jedem Netz:** Transportrest <= 1e-10, Huellenpruefungen, LU, Summe V_g/N - 1 (beschreibend, Rauch <= 2e-4),
  M: Netz gleich und Punkte gleich (beschreibend je Netz).
- **K0:** Gamma_Q und Gamma_C rund bitgleich mit KUGEL-2 (Saaten 0 bis 39).

## 9. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K1] KV2 betrifft eine Verformung, die nicht spurfrei ist** (S3). Gerechnet wird der Kartenwortlaut (gestauchte
  Kugel); Einstein erwartet dort "Gamma sinkt". Eine echte TT-Verformung ist mit dieser Vorschrift nicht kovariant baubar
  (S4, S5) und wird nicht gerechnet. Die Wahrscheinlichkeit der Karte (45 %) bleibt stehen.
- **[K2] KV3 "beide Antworten":** mit den Einstein-Vorhersagen aus VORAB.md (beide negativ), nicht mit dem
  Kartenvorzeichen fuer KV2.
- **[K3] Nullprobe teilweise vorab entschieden** (S7): Transport, Netz und Sehnen sind fuer M exakte Moebius-Bilder;
  offen ist nur die Volumenzuordnung je Simplex. CI-Nullprobe exakt null.
- **[K4] Neu bauen statt mitnehmen** (S4); Rauschpreis: 53 bis 63 % neue Simplizes.
- **[K5] Laengenregel QI statt Q** (S6): Q ist auf der verformten Kugel nicht definiert; QI ist Q fuer g = g0.
- **[K6] Einseitige Verformungen, eps = -0,1** (Einbettbarkeit, Abschnitt 2); N bis 4000 (S9).
- **[K7] Hauptschaetzer Konstantenfit** (S9).
- Kartenfehler, die ein Urteil nach Kartenwortlaut veraendern koennen: [K1] (KV2 misst nicht, was die Karte meint).

## 10. Agenten-Vorhersagen (nach Kontrolle und Rauchlauf, vor den Hauptlaeufen; ohne Kenntnis von Messwerten)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Tor besteht ohne Ausschluss | 90 % |
| A2 | K0 bitgleich | 90 % |
| A3 | KV0 (Karte) eingetroffen | 45 % |
| A4 | b_K < 0 (Punktschaetzer) | 70 % |
| A5 | KV1 eingetroffen (>= 3 SE) | 45 % |
| A6 | KV2 (Karte) eingetroffen | 10 % |
| A7 | b_E < 0 (Punktschaetzer) | 70 % |
| A8 | KV3 eingetroffen | 15 % |

## 11. Rauchlaeufe und Kontrolle (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC)

- **vorab** (12:50:33 bis 12:50:36, cpu3, rc 0): VORAB.md.
- **kontrolle** (12:50:55 bis 12:51:11, cpu3, rc 0): C1 bis C4 wie Abschnitt 8; Kippanteil bei N = 1000: K 0,60, E 0,53,
  M 0.
- **rauch-a** (cpu4, rc 0, 57 s): N = 1000, 2000, Saaten 900 bis 902, blind; alle Netze gueltig; Kippanteil K 0,59 bis
  0,61, E 0,53 bis 0,55, M 0; Summe V_g/N - 1 <= 2e-4; 5,4 / 13,3 s je Saat (alle vier Netze).
- **rauch-b** (cpu5, rc 0, 79 s): N = 4000, Saaten 900, 901, blind; gueltig; Kippanteil K 0,62, E 0,57; 39 bis 40 s je
  Saat; RSS 422 MB.
- **Blinde Streuung** (Std von y ueber die Saaten, keine Mittel): M 0,0012 / 0,0023 / 0,0024, K 0,093 / 0,18 / 0,004,
  E 0,34 / 0,12 / 0,040 (N = 1000 / 2000 / 4000; 3 bzw. 2 Saaten, wenig belastbar).
- **Blindheit geprueft (jq):** In rauch-a.json und rauch-b.json hat keine Regel ein Feld gamma.
- **Codeprobe** (12:53 bis 12:56 UTC, cpu3, rc 0): nicht blind auf N = 300, 600, Saaten 950 bis 969, dann Auswertung;
  nur Struktur geprueft (jq keys: Tor, Urteile KV0 bis KV3, Messgroessen M/K/E x QI/CI; K0 dort ohne Vergleichsnetze).
  Werte und Urteile der Probe nicht gelesen. Danach (14:56 CEST, vor dem Einfrieren) eine Codeaenderung: Saaten ohne
  alle N zaehlen als "unvollstaendig" statt "ausgeschlossen" (wie Abschnitt 4 verlangt); Probe-Auswertung erneut rc 0,
  nur Struktur. Struktur der KUGEL-2-Laufdateien fuer K0 geprueft (kugel.regeln.Q hat gamma).
- **Zeitfolge der Festlegungen:** Verformungen, Amplituden, Regel QI, Huelle, Transport, Messgroesse, Fit, Tor und
  Urteilsregeln standen vor der Kontrolle im Code (14:50 CEST); nach Kontrolle und Rauchlauf festgelegt: Saatzahl und
  Laufaufteilung (aus den Zeiten), Agenten-Vorhersagen, Text.
