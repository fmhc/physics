# ARBEITSFELD INDUZIERT-G-L (feldforscher, Runde 39)

- Start 2026-10-04 10:07:06 CEST (date). Zeitbox 60 min, also bis etwa 11:07 CEST.
- Einzige Arbeitsdatei dieser Karte. Vor jedem Schritt neu lesen. Gestrichenes bleibt mit ~~ stehen.
- Kennzeichen: [S] an der Quelle gelesen (lokale Kopie in quellen/, mit Zeilenangabe), [L] Gedaechtnis, [L?] unsicher,
  [ES] eigener Schluss, [H] Hypothese.
- Abrufe: hoechstens 15. Jeder curl- oder WebFetch-Aufruf zaehlt als ein Abruf. Volltexte liegen als lokale Kopie in
  quellen/ (pdftotext), Fundstellen nur aus diesen Kopien, nie aus einer Werkzeug-Zusammenfassung.

## 0. Gelesen vor dem ersten Abruf (10:07 bis 10:11)

- KARTE.md (E1 bis E5), induziert-dichte-4d/ERGEBNIS.md, induziert-dichte-2d-grob/ERGEBNIS.md,
  induziert-dichte-2d/gegenlesen/GEGENLESEN.md, induziert-1/ERGEBNIS.md, RUNDE-39/WEICHE-STAND-v2.md, RUNDE-39.md,
  induziert-dichte-4d/KARTE.md, induziert-dirac-2d/KARTE.md, UEBERLEITUNGEN-EMERGENZ.md (Ue1).
- Kernzahlen fuer diese Karte:
  - 2D Dichte-Ensemble: c(0) = 1,075 P +- 0,071 P (P = -1/(24 pi)); festes Netz +0,159; k^4-Glied d = +0,0215.
  - 4D Dichte-Ensemble (Regel sp): c = +0,111 +- 0,045 (rho = 1), -0,017 +- 0,045 (rho = 0,5); festes Netz +0,1706
    bzw. +0,1179 (vorab zwingend >= 0, log-sum-exp-Konvexitaet); geo+ +0,371 (Splitter).
  - Kontinuum (ERGEBNIS-4D [M]): c = -Lambda^2/(32 pi^2) fuer Eigenzeit-Abschneiden, minimal gekoppelt.

## 1. Gegensweep zuerst: Projektsuche (10:09)

- Befehl: grep -rli "sakharov\|induziert\|visser" coordination/runden-v3 coordination/*.md (ohne Sperrpfade, ohne
  json/py/log).
- Befund:
  - Keine lokale Kopie von Visser 2002, Sakharov 1967, Frolov/Fursaev oder einer Gitter-Arbeit zur induzierten
    Schwerkraft. Alle bisherigen Nennungen im Projekt sind [L] (INDUZIERT-1, -DICHTE-2D, -DICHTE-4D, Ue1).
  - RUNDE-22/geometrie-stand: Raasakka 2025, arXiv:2505.07102, "Emergence of gravity from QFT in triangulated
    spacetime": induzierte Gravitationswirkung aus freiem massivem Skalar auf 2D-Lorentz-Triangulierung (dort nur
    Abstract gelesen, [L?]). Liegt im 24-Monats-Fenster und ist der naechste bekannte Simplex-Fall. -> Abrufkandidat.
  - RUNDE-35/graviton-netz-l: Carlip 2012 zaehlt Sakharov als "Dynamik emergent bei vorhandener Metrik" [S dort].
  - INDUZIERT-1 nennt Collins/Perez/Sudarsky/Urrutia/Vucetich 2004 (nicht kovariante Regulatoren erzeugen
    Lambda^2-Glieder), nicht an der Quelle geprueft.
  - INDUZIERT-DIRAC-2D laeuft (Fermion, Doppler-Zaehler ueber die Anomalie). Beruehrt E5.

## 2. Eigene Vorueberlegung vor den Abrufen (Schreibtisch, [ES]/[L]; 10:12 bis 10:17)

- **Waermeleitung mit Reglerfunktion [L/M]:** Gamma = -1/2 Int ds/s f(s Lambda^2) Tr e^(-s Delta), a_1 = (1/6 - xi) R.
  R-Glied: -(Lambda^2 m_f/(32 pi^2)) (1/6 - xi) Int sqrt(g) R mit m_f = Int dx x^(-2) f(x). Eigenzeit: m_f = 1.
  Vorzeichen also (1/6 - xi) mal Vorzeichen von m_f. m_f > 0 fuer f >= 0; fuer Pauli-Villars-artige f nicht fest.
  Konforme Mode (4D, Torus): c = 6 B mit Gamma ⊃ B Int sqrt(g) R, also c = -(m_f Lambda^2/(32 pi^2)) (1 - 6 xi).
- **Masse:** Der Koeffizient von m^2 log m^2 im R-Glied ist -(1/6 - xi)/(32 pi^2), unabhaengig von f (universell).
- **Verschiebungssymmetrie [ES, M]:** Die P1-Steifigkeit hat Zeilensumme 0 (K 1 = 0). Ein Potentialglied xi R phi^2
  ist damit auf jeder Skala verboten; das langwellige xi ist exakt 0. Ein "xi_eff" kann nur die UV-Groesse m_f
  umbenennen. Gitterglieder der Art h^2 R Box im Operator tragen aber ~ h^2 Lambda^4 ~ Lambda^2 zum R-Glied bei, also
  in derselben Ordnung wie a_1. Darum ist B auf dem Gitter nicht (1/6 - xi) mal etwas Positives, sondern eine
  Gitterzahl.
- **2D gegen 4D [ES]:** In 2D ist jedes kovariante Zwei-Ableitungs-Glied Int sqrt(g) R topologisch; nach Entfernen der
  Dichtegradienten ("Zahl = Volumen") bleibt nur die Anomalie (universell, misst xi_IR; gemessen 1,075 P heisst
  xi_IR = -0,0125 +- 0,012, vertraeglich mit dem exakten Wert 0). In 4D bleibt B Int sqrt(g) R mit B ~ rho^(1/2) mal
  Gitterzahl, Vorzeichen frei. Zwei Regime desselben Mechanismus, Moderator: Dimension (Leistungsglied gegen Log-Glied).
- **Rechenkarten-Idee [H]:** Poisson-Punkte auf S^4 (konvexe Huelle in R^5 = spherisches Delaunay), P1 mit
  Sehnenlaengen. Gamma_S4(N) - Gamma_T4(N) = beta sqrt(N) + gamma log N + delta. beta = 61,6 B (Dichte 1). Rauschen je
  Netz ~0,15 sqrt(N) (aus den Torus-Saaten geschaetzt), also S/R je Netz ~ beta/0,15. 2D-Kontrolle auf S^2: kein
  sqrt(N)-Glied erwartet. Ausarbeitung nach den Abrufen.

## 3. Abrufplan (Erwartung je Abruf steht VOR dem Abruf in Abschnitt 4)

| Nr | Ziel | Zweck |
|---|---|---|
| A1 | Visser 2002, gr-qc/0204062 (PDF) | E1, E2, E5 |
| A2 | Fursaev 2004 (gr-qc/0404038) oder Frolov/Fursaev/Zelnikov 1996 (hep-th/9607104) | E1 (xi), E2 |
| A3 | Raasakka 2025, arXiv:2505.07102 | E3, Regel 7 |
| A4 | arXiv-API-Abfrage "induced gravity" + lattice/simplicial (Entdeckung) | E3 |
| A5 | arXiv-API-Abfrage 24 Monate (Regel 7) | E3, E4 |
| A6 | Kenyon 2000 (asymptotische Determinante des diskreten Laplace) oder Gleichwertiges | E2 am Gitter, E4 |
| A7+ | nach Lage | |

## 4. Abrufprotokoll

| Nr | Zeit (Erwartung) | Ziel | Erwartung (vor dem Abruf) | Ausgang | Verstoss? |
|---|---|---|---|---|---|
| A1 | 10:17:06 | arxiv.org/pdf/gr-qc/0204062 (Visser 2002) | Formel 1/G ~ Lambda^2 mal gewichtete Feldzahl (Skalare, Fermionen gleiches Vorzeichen, Vektoren entgegengesetzt); Aussage, dass Vorzeichen und Wert vom Regler bzw. Teilcheninhalt abhaengen; in dimensionaler Regularisierung Superspur m^2 log m^2. xi-Abhaengigkeit (1/6 - xi) vermutlich NICHT explizit | quellen/visser-gr-qc-0204062.txt (17 S.). Gl. (3) nicht-minimaler Skalar; Gl. (14) a1 = k1 R - m^2; Gl. (21) 1/G = 1/G0 - (1/2pi) str[k1 kappa^2 - k1 m^2 ln(kappa^2/m^2)]; Gl. (29) Sakharov: 1/G ~ -(1/2pi) str[k1] kappa^2 mit "str[k1] ~ -1"; Tabelle 1: Skalar generisch k1 = 1/6 - xi, konform 0, Dirac -1/3 (in str mit Fermion-Minus also +1/3), Vektor masselos -2/3. Fussnote a: Schwinger nicht besonders, PV ginge auch; Zeta/dim. Reg. "hiding some of the interesting terms". Pauli/FF-Weg Gl. (36), (43): 1/G = -(1/2pi) str[k1 m^2 ln(m^2/mu^2)], endlich, Vorzeichen vom Spektrum. Kein Wort zu Gittern ausser S. 15 ("lattice quantum gravity" als Kandidat; Einstein-Form "automatic") | **ja, zweifach:** (1) xi steht explizit da (Tabelle 1). (2) **Absolutes Vorzeichen:** In Vissers Konvention braucht Sakharov str[k1] < 0, minimale Skalare (+1/6) und Dirac (+1/3) wirken also *gegen* positives G, Vektoren dafuer. Das widerspricht meiner Euklid-Rechnung und dem [M] in ERGEBNIS-4D. Relativvorzeichen sind konventionsfrei; das absolute braucht einen zweiten Anker (A2) |
| A2 | 10:21:47 | arxiv.org/pdf/gr-qc/9404039 (Jacobson 1994) | Skalar mit Abschneiden: 1/G_ind positiv, ~ Lambda^2/(12 pi) je Feld (Eigenzeit); Verschraenkungsentropie A/(4 G_ind) mit demselben Abschneiden; eventuell Hinweis, dass Vektoren/nicht-minimale Kopplung anders sind | quellen/jacobson-gr-qc-9404039.txt (7 S.). Keine Formel, kein Koeffizient. S. 4: W_loc = hbar Int sqrt(g) [a0 + a1 R + ...], a1 ~ Lc^-2; Beitrag zur Entropie "4 pi hbar a1 A ... with hbar a1 in place of (1/16 pi G)". S. 5: "the entanglement entropy of the quantum fields will always contribute to the renormalized Bekenstein-Hawking entropy A/4hbarGren in proportion to their contribution to the renormalized inverse gravitational constant 1/Gren ... independent of their number and the nature of their interactions." **Fussnote 1:** "If the cutoff breaks general covariance, then one should no longer expect the effective action to contain only generally covariant terms ... Still, for background metrics that are slowly varying on the scale of the cutoff, the generally covariant terms should dominate." | **ja:** keine Zahl, kein explizites Vorzeichen. Dafuer ein Vorzeichen-Anker ueber Positivitaet (5.2) und eine Fussnote, der INDUZIERT-1 widerspricht |
| A3 | 10:22:33 | arxiv.org/pdf/2505.07102 (Raasakka 2025) | 2D-Lorentz-Simplexe, freier massiver Skalar, effektive Wirkung ueber Simplex-Summe; Ergebnis: Einstein-Hilbert-artiger Term (in 2D topologisch) plus kosmologischer Term, evtl. Liouville; Vorzeichen bzw. Regler-Frage wohl nicht allgemein fuer 4D; keine Aussage zu 4D-Vorzeichen | quellen/raasakka-2505.07102.txt (v2 vom 13.08.2026). Bestaetigt: 2D-Lorentz, Schleifen um Ecken, Phase linear in n_v + n*_v, "G_eff = theta1/(8 pi Delta phi) ~ 0.015" (S. 7); Fussnote 5: Zahlenwerte in 2D "do not have any immediate physical significance"; S. 8: andere Quantisierungen "may also lead to ... different behavior of the effective gravitational constant"; 4D nur Ausblick ("assuming that the proportionality constant comes out as approximately of order unity", S. 9) | nein (bestaetigt, eine Zeile) |
| A4 | 10:23:22 | export.arxiv.org/api/query, (abs:"induced gravity" OR abs:Sakharov) AND (lattice OR simplicial OR Regge OR triangulated OR "causal set"), neueste zuerst, 100 | 10 bis 40 Treffer; Diakonov-Spinor-Gitter, Volovik/Zubkov (Graphen, emergente Gravitation), Raasakka; keine Arbeit, die das 4D-Vorzeichen von G_ind fuer einen Skalar auf Simplex- oder Zufallsgittern rechnet | Erster Versuch (http) leer, 0 Byte, zaehlt als Abruf. A4b (https): quellen/api-A4.xml, **nur 4 Treffer**, davon einer einschlaegig (Raasakka 2025); zwei Fehltreffer ("Sakharov factor" bei B-Zerfaellen, BEC). Diakonov, Volovik/Zubkov nicht dabei (deren Abstracts nennen "induced gravity" offenbar nicht zusammen mit den Gitterwoertern) | **ja (Menge):** viel weniger als erwartet; Kernaussage "keine 4D-Simplex-Vorzeichenrechnung" bestaetigt (nach Recherchestand, Abfragegrenze: nur Abstracts, nur diese Woerter) |
| A5 | 10:24:05 | arXiv-API, (abs:"Newton constant" OR abs:"Newton's constant" OR abs:"gravitational constant" OR abs:"emergent gravity") AND (abs:lattice OR abs:simplicial OR abs:Regge OR abs:"random lattice") AND (abs:induced OR abs:fermion OR abs:scalar), neueste zuerst | 20 bis 60 Treffer, ueberwiegend Gitter-Quantengravitation (Hamber, EDT/CDT mit Materie), Diakonov/Vladimirov (Spinor-Gitter), Volovik/Zubkov; hoechstens eine Arbeit mit Vorzeichen der induzierten Kopplung auf dem Gitter | quellen/api-A5.xml, 11 Treffer. Einschlaegig: **Donoghue/Menezes, arXiv:1712.04468, "Inducing the Einstein action in QCD-like theories"**, Abstract: "We evaluate the induced value of Newton's constant which would arise in QCD. The ingredients are modern lattice results, perturbation theory and the operator product expansion. The resulting shift in the Planck mass is positive." Daneben Sexty/Wetterich 2012 (2D-Gitter mit Gitter-Diffeomorphismus-Invarianz, kein G-Vorzeichen), Ansel 2024 (Monte-Carlo-Punkte statt Simplexe), Hamber/Yu 2020, Bassler u. a. 2021 (EDT) | **ja:** Es gibt eine Rechnung, in der G_ind endlich und reglerfrei ist (asymptotisch freie Theorie, Gitter-QCD als Eingabe) und das Vorzeichen positiv herauskommt. Das ist ein zweites Regime, das E2 nicht vorsieht -> voller Zyklus (A6) |
| A6 | 10:24:44 | arxiv.org/pdf/1712.04468 (Donoghue/Menezes) | Formel nach Adler/Zee: 1/G_ind ~ Int d^4x x^2 <T(x)T(0)> (Spur des Energie-Impuls-Tensors); endlich nur, wenn die Theorie im UV konform/asymptotisch frei ist; Vorzeichen nicht allgemein fest (Khuri 1982), fuer QCD aus Gitterdaten positiv; freie Felder hier gerade NICHT erfasst (dort Potenzdivergenz) | quellen/donoghue-menezes-1712.04468.txt (v3, 6 S.). Gl. (2)/(12) Adler-Zee; **Gl. (16) euklidisch: 1/(16 pi G_ind) = -(1/96) Int d^4y_E y^2 <T{Tbar(y) Tbar(0)}>**. S. 2: "this procedure determines that the induced G is positive and evaluates its magnitude to within about 30%"; S. 6: "I_UV^L may change sign depending on the values assigned for x0"; S. 7: "Because the glueball contribution is negative ..."; S. 8 Diskussion: positiv, bleibt positiv fuer SU(N) mit groesserem N; frueher Krasnikov/Pivovarov ebenfalls positiv. Khuri nicht zitiert. Zum Gitter nur: Gitter-Glueball-Daten als Eingabe; Gluonkondensat auf dem Gitter schwierig wegen "dimensionful cut-off" | **teilweise:** Formel und QCD-Vorzeichen wie erwartet. Neu und wichtig: Der Fernbereich (Glueball, positiver euklidischer Korrelator) traegt NEGATIV zu 1/G bei; das positive Gesamtvorzeichen kommt aus dem UV-Teil, dessen Vorzeichen selbst vom Anschlusspunkt abhaengt. Voller Zyklus in 5.3 |
| A7 | 10:26:54 | arXiv-API, (abs:"heat kernel" OR abs:"heat trace" OR abs:"Seeley") AND (abs:"piecewise flat" OR abs:simplicial OR abs:"discrete Laplacian" OR abs:"cotangent" OR abs:polyhedral) AND abs:curvature, neueste zuerst | 10 bis 40 Treffer; Waermeleitung auf polyedrischen Flaechen (Kokotov), Graphen-Kruemmung (Ollivier/Bakry-Emery), Cheeger-artige Konvergenz; KEINE Arbeit, die einem diskreten Laplace (P1/Kotangens) eine effektive Kruemmungskopplung xi zuschreibt | quellen/api-A7.xml, nur 4 Treffer, keiner einschlaegig (Finanznetze 2026, Li-Yau auf Z 2022, Knill 2017 Gauss-Bonnet auf Simplexkomplexen, nichtkommutative Ricci-Kruemmung 2016) | Kernaussage bestaetigt ("keine xi-Zuschreibung", nach Recherchestand); Menge kleiner als erwartet. Abfrage eng (nur Abstracts) |
| A8 | 10:27:34 | arXiv-API id_list: gr-qc/0403053 (Collins u. a. 2004), 1104.3712 (Solodukhin 2011), hep-th/9607104 (Frolov/Fursaev/Zelnikov), nur Abstracts. Gegensweep-Pruefung | Collins: Lorentz-verletzender Regler bei Planck-Skala gibt unterdrueckungsfreie Lorentz-Verletzung bei kleinen Energien (Feinabstimmung). Solodukhin: Verschraenkungsentropie, Bezug zur induzierten Gravitation, nicht-minimale Kopplung. FFZ: induzierte Gravitation mit Bedingungen an Massen und Kopplungen, Entropie endlich | quellen/api-A8.xml. Collins u. a.: "a Planck-scale preferred frame gives rise to Lorentz violation at the percent level, some 20 orders of magnitude higher than earlier estimates, unless the bare parameters of the theory are unnaturally strongly fine-tuned." Solodukhin: "The puzzling behavior of the entanglement entropy due to fields which non-minimally couple to gravity is emphasized." FFZ: "The induced gravitational constant is determined by the masses of the heavy constituents." | nein (alle drei bestaetigt, je eine Zeile). Damit ist das [L] von INDUZIERT-1 zu Collins u. a. auf Abstract-Ebene [S] |
| A9 | 10:28:01 | arXiv-API: au:Hamber AND (abs:scalar OR abs:matter OR abs:induced) | 5 bis 20 Treffer; Hamber/Williams zu Materie auf Regge-Gittern, Hamber-Uebersicht 2009; hoechstens Nebensaetze zu induzierten Gliedern, keine Vorzeichenrechnung fuer G_ind aus einem Gitter-Skalar | quellen/api-A9.xml, 18 Treffer. Einschlaegig: Hamber/Williams 1993 (hep-th/9308099) und Hamber 1993 (hep-th/9310152): Skalar auf 4D-Regge-Gitter, aber dynamische Gravitation mit Regge-Wirkung; "effects of matter are rather small, unless the number of scalar flavors is large". **Hamber/Liu 1996 (hep-th/9603016): "the two-dimensional conformal anomaly due to a D-component scalar field is explicitly computed in perturbation theory"** auf Regge-Gittern. Hamber/Williams 1996 (hep-th/9607153): Gitter-Diffeomorphismen fuer die Skalarwirkung | **teilweise:** keine G_ind-Vorzeichenrechnung (bestaetigt); neu ist, dass die 2D-Anomalie eines Gitter-Skalars auf Regge-Gittern schon 1996 gerechnet wurde, also eine Vorlaeuferin von INDUZIERT-1 Teil A -> A10 |
| A10 | 10:28:35 | arxiv.org/pdf/hep-th/9603016 (Hamber/Liu 1996) | Sie rechnen die Polyakov-Zahl -D/(24 pi) bzw. (D/96 pi) Int R Box^-1 R auf dem Regge-Gitter in schwacher Feldentwicklung nach und finden im Langwellenlimes den Kontinuumswert; lokale Gitterglieder werden als nicht universell genannt oder durch Gegenglieder entfernt | quellen/hamber-liu-hep-th-9603016.txt (30 S., Textfolge im pdftotext verwuerfelt, Seitenzahlen aus dem Text). S. 28 (Schluss): "the two-dimensional conformal anomaly due to a massless scalar field was computed by diagrammatic methods ... a new diagram, the tadpole term, which vanishes in the continuum but is necessary on the lattice for canceling unwanted terms. Finally we have shown that in the leading continuum approximation the expected continuum form for the anomaly is obtained, with the correct coefficient." S. 26 bis 27 (Seitenfolge im Text verwuerfelt): Liouville-Wirkung Gl. (3.94) "One therefore completely recovers the result derived perturbatively from the continuum"; Gl. (3.103) mit (26 - D)/96 pi | nein (bestaetigt, eine Zeile). Passt zu INDUZIERT-1 Teil A2 (universeller Anteil richtig) und zur Tadpole-Rolle in 5.3 |

## 5. Laufende Befunde

### 5.1 Analysezyklus zum Verstoss A1(2), absolutes Vorzeichen (10:20 bis 10:24)

- Saubere Euklid-Rechnung [M]: Z = det(Delta + m^2)^(-1/2), W = -ln Z = 1/2 ln det = -1/2 Int_(1/kappa^2) ds/s Tr e^(-s(..)).
  W ⊃ -(1/(32 pi^2)) Int sqrt(g) [kappa^4/2 + (R/6 - m^2) kappa^2]. Mit I_E = -(1/(16 pi G)) Int sqrt(g) (R - 2 Lambda)
  (S^4-Wirkung negativ, konformer Faktor instabil, Gibbons/Hawking/Perry [L]) folgt 1/(16 pi G_ind) = kappa^2/(192 pi^2)
  > 0. Minimaler Skalar mit Eigenzeit-Regler: positives G. Das [M] in ERGEBNIS-4D (c = -Lambda^2/(32 pi^2)) stimmt damit.
- Querprobe 2D [ES]: dieselbe Kette gibt in 2D das Polyakov-Vorzeichen (negativ), das das Projekt gemessen hat
  (1,075 P). Materie macht die konforme Mode in beiden Dimensionen weich; in 4D ueber das Potenzglied, in 2D ueber
  das Log-Glied.
- Lesart Visser: Gl. (19) setzt das R-Glied als "-R/(16 pi G)" an, Gl. (9) traegt +k1 kappa^2 R/(32 pi^2) in S_g = -1/2 ln
  det = +ln Z. Das gibt sein 1/G = -k1 kappa^2/(2 pi). Mit der Euklid-Konvention oben waere das physikalische G das
  Negative davon. Ich lese Gl. (19)/(29) daher als Konventionsfrage und stuetze das absolute Vorzeichen NICHT auf
  Visser; zweiter Anker noetig (A2).
- **Nebenfund [S + Nachrechnung]:** Visser Gl. (20) (Eigenzeit) gibt fuer ein Boson Lambda = -kappa^4/(64 pi^2) + ...,
  Fussnote c (Nullpunktsumme mit Impulsschnitt) +kappa^4/4 mal positiver Faktor. Die Log-Glieder stimmen ueberein
  (-m^4 ln/(64 pi^2), wenn man in Fussnote c ln kappa statt ln kappa^2 liest), das kappa^4-Glied hat in beiden
  Reglern entgegengesetztes Vorzeichen. Am Vakuumglied zeigt Vissers eigener Text also: Potenzglieder koennen mit dem
  Regler das Vorzeichen wechseln, Log-Glieder nicht. Visser selbst kommentiert das nicht ("precisely yields").

### 5.2 Vorzeichen-Anker ueber Entropie (aus A2, eigene Rechnung, 10:23)

- Kegelmethode [M]: Int sqrt(g) R hat an der Kegelspitze 4 pi (1 - alpha) A. Mit W ⊃ a1 Int sqrt(g) R und
  S = (1 - beta d/dbeta) ln Z folgt S = -4 pi a1 A. Mit I_E = -(1/(16 pi G)) Int sqrt(g) R ist a1 = -1/(16 pi G) und
  S = A/(4G). Jacobsons "hbar a1 in place of (1/16 pi G)" ist also vorzeichenlos gemeint.
- Positive Verschraenkungsentropie verlangt a1 < 0, also positives G. Mein minimaler Skalar mit Eigenzeit-Regler hat
  a1 = -kappa^2/(192 pi^2) < 0: passt. Damit ist das absolute Vorzeichen fuer kovariante Regler ueber Positivitaet
  verankert, und Vissers Gl. (29) ist eine Konventionsfrage (5.1).
- **Folgerung fuer das Projekt [ES, H]:** Auf einem Gitter ist die Verschraenkungsentropie eines Gebiets positiv
  (von-Neumann-Entropie), mit Flaechengesetz. Gaelte Jacobsons Gleichheit S_ent = A/(4 G_ind) auch fuer unseren
  Gitter-Regler, waere 1/G_ind > 0 und c < 0. Unser 4D-Wert (c = +0,111 +- 0,045, also G_ind < 0) hiesse dann: Die
  Gleichheit gilt fuer dieses Gitter nicht. Jacobsons Fussnote 1 nennt genau die Bedingung (kovarianter Regler). Das
  ist ein Unterscheidungspunkt, der sich rechnen laesst (Karte B).
- **INDUZIERT-1 gegen Fussnote 1 [ES]:** Jacobson erwartet, dass bei nicht kovariantem Regler die kovarianten Glieder
  fuer langsam veraenderliche Metriken "should dominate". INDUZIERT-1 fand das Gegenteil (Gitterglieder im k^2-Teil,
  Streuung von c2 78 %). Nach Potenzzaehlung sind nicht kovariante Glieder von derselben Ordnung Lambda^2; die
  Fussnote ist zu optimistisch.

### 5.3 Analysezyklus A6: Woher kommt das Vorzeichen? Kontakt gegen Korrelator (10:26 bis 10:30)

- **Positivitaet [M aus Gl. (16)]:** Der euklidische Korrelator eines hermiteschen Skalars ist bei getrennten Punkten
  positiv (Reflexionspositivitaet [L]). Mit Gl. (16) traegt jeder Abstandsbereich mit getrennten Punkten also
  NEGATIV zu 1/G bei. Positives G muss aus dem UV- bzw. Kontaktanteil kommen. D/M finden genau das: Glueball
  negativ, UV-Teil positiv und groesser; der UV-Teil wechselt das Vorzeichen mit dem Anschlusspunkt x0.
- **Gleiche Zerlegung bei uns [ES, M]:** INDUZIERT-1 schreibt die Hesse-Matrix als Pi = 1/2 Tr(G K2) - 1/2 Tr(G K1 G K1).
  Der zweite Teil ist der verbundene Korrelator (Blase). Fourier: Pi_Blase(Q) = Pi(0) - (Q^2/8) Int y^2 psi + ...,
  also liefert die Blase bei getrennten Punkten im k^2-Glied +(1/8) Int y^2 psi > 0, steif, anti-Einstein. Dasselbe
  Vorzeichen wie D/Ms Glueball-Anteil. Einsteins Vorzeichen muss aus dem Kontaktglied (Tadpole 1/2 Tr(G K2)) bzw. dem
  divergenten Nahbereich der Blase kommen, also genau aus dem Teil, den der Regler festlegt.
- Freies Feld, Probe [M]: Fuer den Skalar mit xi gilt auf der Schale T = -((1 - 6 xi)/2) Box phi^2, also
  <TT>_E = (1 - 6 xi)^2 (6/pi^4) y^-8 > 0. Gl. (16) gaebe -(1 - 6 xi)^2 Lambda^2/(16 pi^2), quadratisch in (1 - 6 xi)
  und negativ, waehrend die Waermeleitung (1 - 6 xi) linear und positiv gibt. Die Adler-Zee-Form ohne Kontaktglieder
  gilt fuer freie Felder also nicht; dort entscheidet der Kontaktanteil. (D/M Anhang: "The issue hinges on the
  two-graviton coupling called tau_mu nu, alpha beta"; dort fuer die kosmologische Summenregel.)
- **Regime [ES]:** (i) UV-endliche, asymptotisch freie Materie: G_ind endlich, Vorzeichen dynamisch bestimmt
  (QCD positiv). (ii) Freie bzw. Gitter-Materie mit Potenzdivergenz: Vorzeichen = Vorzeichen des Kontakt- bzw.
  Reglerteils. Moderator: Verhalten der Spur T im UV (verschwindet logarithmisch gegen bleibt kanonisch).
  Unser P1-Skalar liegt in (ii).
- **Festes Netz [ES]:** Die Konvexitaet (log-sum-exp) heisst: Auf festem Netz gewinnt der Kontaktteil immer gegen
  die Blase. Erst das Dichte-Ensemble aendert die Bilanz. ~~In 2D gewinnt dann die Blase mit genau dem
  universellen Gewicht (Polyakov)~~ (gestrichen 10:31: In 2D ist der masselose Skalar konform, die Spur verschwindet
  bei getrennten Punkten; Polyakov ist dort ein reiner Anomalie- bzw. Kontaktbeitrag mit universellem Gewicht c. Die
  Blasen-Lesart passt nur fuer 4D.) In 2D bleibt im Dichte-Ensemble genau der universelle Anomalieteil; in 4D
  verschiebt sich die Bilanz nur teilweise (c von +0,17 auf +0,11 bzw. -0,02).

### 5.4 Kartenerwartungen E1 bis E5, Ausgang (10:31)

| Nr | Ausgang | Fundstelle |
|---|---|---|
| E1 | eingetroffen fuer Form und Kipppunkt xi = 1/6; absolutes Vorzeichen bei Visser konventionsabhaengig, verankert ueber Euklid-Rechnung und Entropie-Positivitaet [M] | Visser 2002, Gl. (3), (14), (21), Tabelle 1 [S]; 5.1, 5.2 |
| E2 | eingetroffen, mit Erweiterung um ein zweites Regime (UV-endlich, dynamisches Vorzeichen) | Visser Fussnote a, Gl. (20) gegen Fussnote c, Gl. (36)/(43) [S]; Donoghue/Menezes Gl. (16) S. 3, S. 2, 6, 7, 8 [S] |
| E3 | teilweise: simpliziale Rechnungen gibt es (2D-Anomalie Hamber/Liu 1996; 2D-Lorentz Raasakka 2025; 4D-Skalar in dynamischer Regge-Gravitation Hamber/Williams 1993), aber keine 4D-Vorzeichenrechnung fuer G_ind aus einem Gitter-Skalar (nach Recherchestand nicht belegt) | A3, A4b, A5, A9, A10 |
| E4 | nicht belegt (A7 ohne Treffer). Eigener Schluss: K 1 = 0 erzwingt xi_IR = 0; der UV-Teil ist keine Kopplung | 2., 5.3 [ES, M] |
| E5 | erster Teil eingetroffen (relativ: Dirac wie minimaler Skalar, doppeltes Gewicht); zweiter Teil ("weniger reglerempfindlich") nicht belegt | Visser Tabelle 1 [S] |

## 6. Erwartungsverstoesse (eigene Abruf-Erwartungen und Karten-E1 bis E5)

1. **Zwei Regime fuer das Vorzeichen** (A6): UV-endliche, asymptotisch freie Materie hat ein dynamisch festes
   Vorzeichen (QCD positiv); freie bzw. Gitter-Materie ein reglerbestimmtes. Getrennte Punkte tragen nach Gl. (16)
   und Reflexionspositivitaet immer anti-Einstein bei. E2 sah nur ein Regime.
2. **Visser-Vorzeichen** (A1): woertlich gelesen brauchen Vissers Gl. (19)/(29) str[k1] < 0, also wuerden minimale
   Skalare und Dirac-Fermionen G negativ machen. Konventionsfrage; Relativvorzeichen robust.
3. **xi_eff > 1/6 im IR-Sinn ausgeschlossen** (eigene Herleitung, durch 2D-Messung gestuetzt). Leitungs-[H] nur als
   Umbenennung des Reglermoments haltbar.
4. **Jacobsons Fussnote 1** (A2) zu optimistisch, gegen INDUZIERT-1 und Collins u. a. 2004 (A8).
5. **Menge der Treffer** (A4b, A7) kleiner als erwartet; Kernaussagen trotzdem bestaetigt.

## 7. Gegensweep am Ende: Was habe ich als selbstverstaendlich angenommen? (10:32)

1. **Dass der 4D-Torus-Wert c ueberhaupt das kovariante B misst** (c = 6 B). Gilt nur, wenn das Dichte-Ensemble
   kovariant ist. Delaunay in Koordinaten und Regel sp sind es nur in erster Ordnung (ERGEBNIS-4D [K6]). Nicht kovariante
   Lambda^2-Glieder wuerden c verfaelschen. Gepruefte Spur: Die Dichte-Abhaengigkeit passt nicht zu c ~ rho^(1/2)
   (c(0,5) = -0,017 +- 0,045 gegen erwartet c(1)/sqrt(2) = +0,078 +- 0,032; Abstand 0,095 +- 0,055, 1,7 SE). Kein
   Beweis, aber ein Hinweis. -> Karte A prueft genau das.
2. **Dass "minimaler Skalar gibt positives G" eine Tatsache ist.** Geprueft (5.1, 5.2): gilt fuer Regler, die Funktion
   des Operators mit f >= 0 sind; Visser woertlich widerspricht; Anker ueber Entropie-Positivitaet.
3. **Dass INDUZIERT-1s Collins-Zitat stimmt.** Geprueft (A8, Abstract): stimmt.
4. **Dass Rauschen je Netz ~0,15 sqrt(N) auf S^4 gilt.** Aus Torus-Zweitdifferenzen geschaetzt, Netze dort korreliert
   (gleiche Saatpunkte). Nicht geprueft; Karte muss es im Rauchlauf messen.
5. **Dass die Laengenregel ein Reglermerkmal ist und kein Fehler.** Begruendet (h^2 R-Glieder speisen Lambda^2 R),
   nicht an Literatur geprueft.
6. **Dass Polyakov in 2D "universell" auch fuer Zufallsnetze gilt.** Fuer Regge-Gitter bestaetigt (Hamber/Liu), fuer
   Poisson-Delaunay nur durch unsere Messung.

## 8. Offene Rueckfragen (wandern mit)

- R1: Vissers Konvention in Gl. (19): Ist "-R/(16 pi G)" mit seiner Kruemmungs-Vorzeichenwahl physikalisch? (offen;
  fuer uns ohne Folgen, weil Relativvorzeichen und eigene Euklid-Rechnung reichen)
- R2: Gibt es eine Gitter-Rechnung der Flaechengesetz-Konstante der Verschraenkungsentropie und von 1/G_ind auf
  demselben Gitter? (nicht gesucht; Karte B)
- R3: Laesst sich das Reglermoment der P1-Delaunay-Diskretisierung analytisch angeben (Spektraldichte gegen Weyl)?
  (offen)
- R4: Frolov/Fursaev-Formel mit xi_s im Volltext (nur Abstract gelesen). (offen)
- R5: Khuri 1982 o. ae. zum Vorzeichen in asymptotisch freien Theorien (von D/M nicht zitiert, nicht gesucht). (offen)

## 9. Abschluss (10:36:30 CEST, date)

- Abrufe: 11 von 15 (A1, A2, A3, A4 leer, A4b, A5, A6, A7, A8, A9, A10).
- Ableitbarkeitsprobe fuer Karte A (Projekt-grep S^4/4-sphere/Kugel mit log det, 10:35): nur Fehltreffer.
- Seitenangaben D/M nach Formfeed-Zaehlung berichtigt (10:34): "may change sign" S. 6, "glueball ... negative" S. 7.
- Dossier: DOSSIER.md. Nichts im Scratchpad der Leitung abgelegt; Quellenkopien in quellen/.
