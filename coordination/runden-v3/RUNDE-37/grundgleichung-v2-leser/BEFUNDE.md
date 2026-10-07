Urteil: 7 A-, 13 B-, 7 C-Befunde. Strukturbefund 2.3 haelt mit Bedingung (Kern richtig, die zwei "nur" falsch, Folgerung aus den Zahlen traegt nicht).

# Blinde Zweitmeinung zu GRUNDGLEICHUNG-SKIZZE-v2.md (RUNDE-48)

- Leser: frischer, unabhaengiger Pruefer (Claude, Opus), ohne Kenntnis der Fassung 1 beim ersten Lesen
- Beginn: 2026-10-05 10:51:32 CEST (per `date` gemessen)
- Ende: 2026-10-05 11:16:26 CEST (per `date` gemessen; Dauer 24 min 54 s = 11:16:26 - 10:51:32)
- Gepruefte Datei: /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-48/GRUNDGLEICHUNG-SKIZZE-v2.md
- Beigezogen: codex-ideation-20261005/GRUNDGLEICHUNG-GEGENBLICK.md; RUNDE-37/hodge-masse-1/ERGEBNIS.md (Tab. 4.2); RUNDE-48.md (Ernten ab 10:09)
- Arbeitsweise: nur lesende Befehle, Rechnungen von Hand im Text gezeigt, Literatur aus dem Gedaechtnis mit [L] markiert

## Lesestand

- Fassung 2 vollstaendig gelesen (207 Zeilen), danach Codex-Gegenblick vollstaendig, dann ERGEBNIS HODGE-MASSE-1 Abschnitte 0 bis 4.5 (Tab. 4.2 und 4.4), RUNDE-48.md Zeilen 34 bis 54, 56 bis 80 und 221 bis 413 (Ernten SKALAR-SEKTOR-L, SKALAR-MISCH-1, REGGE-KINETIK-L, CODEX-REVIEW-R48, HODGE-MASSE-1, GLAS-STRAHLUNG-1, Codex-Gegenblick).
- Fassung 1 erst danach und nur per grep auf Kernbegriffe (Takt, K = 0, Delaunay, Einfach gesagt) abgeglichen.
- Keine BRIEF-Datei mit sha256 genannt; der Auftrag stand in der Nachricht der Leitung und wurde woertlich befolgt. Ausgabepfad RUNDE-37/grundgleichung-v2-leser/ deckt sich mit RUNDE-48.md 10:52:04.
- Kennzeichen hier: [M] von Hand gerechnet (Rechenweg im Anhang R1 bis R9), [P] Projektdatei mit Fundstelle, [L] Literatur aus dem Gedaechtnis, ungeprueft.

## A-Befunde (sachlich falsch oder zu stark)

Vorschlaege sind Anforderungen an den Wortlaut; formulieren muss der Autor.

### A1 Zwei "nur" im Strukturbefund sind mathematisch falsch (Abschnitt 0, Zeile 1; Abschnitt 2.3, Form B)

- Zitate:
  - Abschnitt 0: "Neu dabei: Nur die impulsseitige Form je Zelle macht H linear in N (Abschnitt 2.3)."
  - Abschnitt 2.3: "Linear wird es nur bei einem N fuer alle Zellen, also mit einem globalen Takt (projizierbar, Horava-artig)."
- Begruendung [M, R2, R3]:
  - H_B(N) = (1/2) pᵀ (Summe_t M_t/N_t)^-1 p ist homogen vom Grad 1 in N, denn M(sN) = M(N)/s. Damit ist H_B linear entlang **jedes** Strahls N = s(t) N̂ mit festem, auch ungleichmaessigem Profil N̂. "Ein N fuer alle Zellen" ist nur der Sonderfall N̂ = 1.
  - Gegenbeispiel zum ersten "Nur": H_kin = (1/2) Summe_e N_e p^e (M^-1 p)_e mit M = Summe_t M_t (Lund-Regge bei N = 1) und N_e = Kantenmittel. Symmetrisch geschrieben ist das (1/2) pᵀ [(D_N M^-1 + M^-1 D_N)/2] p mit D_N = diag(N_e). Es ist linear in N und bei gleichem N exakt Form B.
  - Der Preis ist Nichtlokalitaet: M^-1 ist dicht. Ob es schnell abfaellt, ist offen, weil M indefinit ist.
  - Das ist genau Ausweg (iii), den 2.3 "im Projekt unbekannt" nennt. Er laesst sich in einer Zeile hinschreiben. Das "Nur" in Abschnitt 0 widerspricht also dem eigenen Ausweg (iii).
- Vorschlag:
  - "Von den zwei ultralokalen Formen ist nur A linear in N."
  - "B ist homogen vom Grad 1 in N, also linear nur entlang eines Strahls N = s(t) N̂ (ein einziger globaler Multiplikator; N̂ = 1 ist der projizierbare Fall)."
  - Bei (iii): "konstruierbar (Beispiel), Preis: nichtlokal; offen sind der Abfall von M^-1 und die Stabilitaet, die bei gleichem N die von B ist."

### A2 Glas-/Kristall-Satz widerspricht Tabelle 4.2 (Abschnitt 2.3, "Bisherige Rechnungen", letzter Unterpunkt)

- Zitat: "Auf Glas wachsen Moden in allen Paarungen ausser A1 und A2 mit R1; die Kristalle sind dort regulaer."
- Begruendung [P, HODGE-MASSE-1 Tab. 4.2]:
  - Spalte A2LR2 (= A3R2): Glas s1 8,19 %, s3 8,01 %, s4 8,54 % ohne wachsende Mode, nur s2 "(neg 1)". Also nicht "in allen Paarungen".
  - Spalte A2LRH: V, S und A15 je "(neg 1)". Dort sind die Kristalle also nicht regulaer. Der Text sagt das zwei Unterpunkte vorher selbst ("Kristalle 1").
  - Die Vorlage (ERGEBNIS Abschnitt 2, Punkt 5) sagt nur: "Nur R1 mit A1 oder A2 ist auf allen Netzen und im Kasten stabil."
- Vorschlag (sinngemaess):
  - Ohne wachsende Moden auf allen sieben Netzen und im Kasten sind nur A1R1 und A2R1.
  - Auf Glas wachsen Moden mit RH (A1, A2, A2L) und mit A2LR1 in jedem Netz, mit A2LR2 in einem von vier (s2).
  - Auf den Kristallen wachsen Moden nur mit A2LRH (je 1).

### A3 Die gemeinsame Zeiteinheit steht nur im Text, nicht in den Formeln (Abschnitt 3.1, 3.2, Abschnitt 0 Zeile 2)

- Zitate:
  - 3.1: "Mit Z_s/Z_t = 8 lautet die Gleichung *0 phi'' = -T phi" und "Die 8 ist damit eine Wahl der Zeiteinheit." sowie "Dieselbe Zeiteinheit muss in Maxwell und Geometrie stehen."
  - 3.2: "H^EM = Summe_e N_e (E^e)^2/(2 *1_e) + Summe_f N_f *2_f (d1 A)_f^2/2"
  - Abschnitt 0: "Zeit-Normierungen Z je Sektor ... als [W] markiert"
- Begruendung [M, R5]:
  - Aus H^EM folgt bei N = 1: *1 A'' = -d1ᵀ *2 d1 A, langwellig also c_Licht^2 = 1 (Netzeinheiten).
  - Form A traegt die ADM-Faktoren 16 pi G und 1/(8 pi G); im ADM-Kontinuum gibt das c_Schwere^2 = 1. Fuer Form A selbst ist selbst das unsicher, weil sie den Kontinuumswert der Bewegungsenergie verfehlt (B1).
  - Der Skalar hat c_phi^2 = Z_s/Z_t = 8.
  - Mit den Formeln von Fassung 2 sind die drei Grundgeschwindigkeiten also **verschieden**. Ein Z gibt es nur im Skalarsektor.
  - Zweitens: Eine Zeiteinheit skaliert alle Terme von omega^2 gleich. Mit Potential gilt omega^2 = (Z_s/Z_t) k^2 + U'(0)/Z_t. Die 8 ist nur dann eine Zeiteinheit, wenn sie ueber Z_t kommt (oder als gleichmaessiges N = Wurzel 8 in allen Sektoren). Kommt sie ueber Z_s, aendert sie die Compton-Laenge in Netzeinheiten, also Physik.
  - Codex-Punkt 2 verlangte genau das: "einmal gemeinsame Zeit-/Einheitenkonvention zeigen".
- Vorschlag:
  - Zeitnormierung je Sektor in die Formeln schreiben (Maxwell z. B. Y_t, Y_s; Geometrie ein Faktor im Bewegungsanteil) und gemeinsam als [W] setzen.
  - Oder einfacher: die 8 als gleichmaessigen Lapse-Faktor N0 = Wurzel 8 fuer alle Sektoren schreiben, denn eine Zeiteinheit ist ein konstanter Lapse-Faktor.
  - Den Satz "Die 8 ist damit eine Wahl der Zeiteinheit" an diese Bedingung binden.

### A4 K = 0 ist auf dem geschlossenen Torus nichtlinear keine zulaessige Eichung (Abschnitt 4)

- Zitate:
  - "Im ungefixten Modell ist K = 0 eine Eichfixierung. Das Paar (H, K) ist zweiter Klasse."
  - "N ist dann nicht frei, sondern folgt aus der Lapse-Gleichung, der diskreten Form von Laplace N = N (K:K + 4 pi G (rho + S)) - N Lambda"
  - "Finns Takt ist so eine Wahl der Zeitscheiben"
- Form und Vorzeichen der Lapse-Gleichung stimmen [M, R6]. Auf dem Torus ohne Rand gilt aber:
  - (a) Setze W = K:K + 4 pi G (rho + S) - Lambda. Multipliziert man mit N und integriert, folgt -Integral |grad N|^2 = Integral W N^2.
    - Bei Lambda = 0, das der flache ruhende Torus braucht, und W >= 0, nicht ueberall null (eine Schwerewelle genuegt), folgt grad N = 0 und dann N = 0. Die Zeit steht still.
    - Bei Lambda ≠ 0 gibt es N ≠ 0 nur, wenn 0 Eigenwert von Laplace - W ist, also nicht generisch. Zudem ist der flache ruhende Torus dann keine Loesung, denn H_v enthaelt (Lambda/8 pi G) V ≠ 0.
    - Diskret gilt dasselbe, solange d0ᵀ *1 d0 positiv semidefinit ist (*1 >= 0).
  - (b) Am flachen Hintergrund ist W = 0. Die Matrix {K(x), H(y)} ist dann -Laplace und hat die Nullmode "konstantes N". Das Paar ist dort also nicht ganz zweiter Klasse; die globale Zeitumparametrisierung bleibt erster Klasse.
  - (c) Zulaessig ist K = 0 nur linear um den ruhenden flachen Torus (dort ist dN konstant). Ab zweiter Ordnung muss sich das Volumen aendern. Der flache T^3 ist linearisierungsinstabil [L: Moncrief 1975; Fischer/Marsden/Moncrief 1980].
  - (d) SKALAR-SEKTOR-L setzt fuer "ART in maximaler Zeitscheibung" ausdruecklich einen asymptotisch flachen Rand voraus [P, RUNDE-48.md 09:01, Zeile 61]. Der Torus hat keinen.
- Vorschlag:
  - In Abschnitt 4 die Bedingung nennen: K = 0 ist auf dem Torus nur linear um den ruhenden flachen Hintergrund eine Eichung; nichtlinear hat die Lapse-Gleichung dort nur N = 0.
  - Die uebliche Wahl auf geschlossenen Raeumen nennen: konstante mittlere Kruemmung K = tau(t) (York-Zeit) mit inhomogener Lapse-Gleichung [L].
  - Die Nullmode als erster Klasse vermerken und "Finns Takt" entsprechend einschraenken.

### A5 "Kruemmung = Spannung" gilt nur bei raeumlich gleichem N (Abschnitt 5)

- Zitate:
  - "Die 'Zugspannung' einer Kante im Kruemmungsanteil ist also ihr Fehlwinkel."
  - "Im ruhenden Fall steht ihr in der Kantengleichung die Spannung der Materie gegenueber. Das ist die diskrete Einsteingleichung."
  - "'Kruemmung wird Spannung' ist die Feldgleichung selbst, keine Zusatzregel."
- Begruendung [M, R7]:
  - Schlaefli gilt fuer die **ungewichtete** Summe Summe_e l_e eps_e. In H_tot steht aber Summe_v N_v H_v, also -(1/8 pi G) Summe_e N_e l_e eps_e mit dem Kantenmittel N_e.
  - Die Ableitung von Summe_e N_e l_e eps_e nach l_e ist N_e eps_e + Summe_e' (N_e' - N_ref) l_e' d eps_e'/d l_e, mit beliebiger Konstante N_ref. Der zweite Term ist die diskrete Form von D_i D_j N - g Laplace N.
  - Im ruhenden Fall mit Materie ist N nicht konstant: N ist etwa 1 + Newton-Potential. Der Zusatzterm hat dann dieselbe Ordnung wie eps.
  - Gegenfall Vakuum um eine ruhende Masse: Die raeumliche Ricci-Kruemmung ist ungleich null (Schwarzschild-Schnitt), die Materiespannung null. Die Kantengleichung schliesst nur ueber den Lapse-Term (im Kontinuum N R_ij = D_i D_j N).
  - Gegenfall ruhender Staub: keine Spannung, aber Kruemmung.
- Vorschlag:
  - Bei raeumlich gleichem N ist die Kantenkraft des Kruemmungsanteils proportional zum Fehlwinkel (Schlaefli).
  - Im ruhenden Fall mit Materie kommt der diskrete Lapse-Term hinzu. Erst Fehlwinkel, Lapse-Term und Materiespannung zusammen ergeben die diskrete Einsteingleichung.
  - Die Folgerung zum Sandhaufen (Zusatzregel, eigener Arm) bleibt davon unberuehrt.

### A6 "fuenf Punkte, alle uebernommen" und "eine Phasenraumform mit allen Multiplikatoren" (Kopf; Abschnitt 0, Zeilen 1 und 2; Abschnitt 2.1)

- Zitate:
  - Kopf: "fuenf Punkte, alle uebernommen"
  - Abschnitt 0: "Eine Phasenraumform mit allen Multiplikatoren (N, s, A0)"
  - Abschnitt 2.1: "H_v, D_v und G_v werden unten definiert."
- Begruendung:
  - Codex 1: Die "diskrete Shift-Wirkung [muss] auf alle Variablen feststehen, nicht bloß ihr Name". 2.4 sagt dazu: "Die genaue Form steht noch aus." D_v ist also nur benannt, H_tot ist nicht definiert und 2.1 verspricht mehr ("werden unten definiert").
  - Die Interpolation von s fehlt in Abschnitt 1, obwohl Abschnitt 8 "Interpolation von N, s und A0" als gesetzt fuehrt. Fuer einen je Zelle konstanten Mittelwert s_t waere L_s g = 0; gebraucht wird das stueckweise lineare Feld aus den Eckwerten.
  - Codex 2: Die gemeinsame Zeitkonvention sollte gezeigt werden. Fassung 2 verlangt sie nur (A3).
  - Codex 1: Der Spurkoeffizient sollte vor Vergleichen gebunden werden. 2.2 sagt "noch nicht gebunden", 2.3 vergleicht trotzdem (B8).
- Vorschlag: "Alle fuenf Punkte angenommen. Eingearbeitet sind 3, 4 und 5. Bei 1 (Shift-Wirkung D_v, Interpolation von s, Spurbindung im Code) und 2 (gemeinsame Zeiteinheit in Maxwell und Geometrie) ist die Anforderung benannt, aber noch nicht in Formeln umgesetzt."

### A7 "Einfach gesagt" ist an drei Stellen staerker als der Text

- Zitate und Begruendung:
  - (1) "Fassung 2 schreibt die Grundgleichung so, dass man sie wirklich nachrechnen kann." D_v fehlt, ebenso die Zeitnormierung in Maxwell und Geometrie und die Spurbindung (A3, A6). Nachrechnen kann man das noch nicht.
  - (2) "Die Form der Traegheit, die Schwerewellen von selbst in alle Richtungen gleich schnell macht, passt nicht gut zu einer oertlichen Uhr in jeder Ecke".
    - Isotrop ist sie nur mit RH, und dann hat sie auf jedem Netz wachsende Moden (2.3).
    - Der Satz verschweigt beides und ist damit staerker als der Text.
    - "passt nicht gut" gilt nur fuer die ultralokale Form (A1).
  - (3) "Krümmung und Spannung sind im Netz ohnehin dasselbe, das ist schon Einsteins Gleichung."
    - "dasselbe" ist staerker als das "steht gegenueber" in Abschnitt 5.
    - Selbst das gilt nur bei gleichem N (A5).
- Vorschlag (Anforderung):
  - Satz 1: klar machen, was noch fehlt, bevor man nachrechnen kann.
  - Satz 3: die Instabilitaet der isotropen Form nennen.
  - Satz 4: Kruemmung und Spannung halten sich in der Feldgleichung die Waage; bei ruhender Materie gehoert der unterschiedliche Gang der Uhren dazu.

## B-Befunde (ungenau, missverstaendlich, fehlende Bedingung)

### B1 Form A ist eine Setzung, keine Uebersetzung aus ADM (Abschnitt 2.2)

- Zitate: "wird daraus auf dem Netz [ES]: Bewegungsanteil (Form A ...)" und "Er entspricht der geschwindigkeitsseitigen Form h:h - (tr h)^2."
- Begruendung [M, R1]:
  - Das Kontinuum gibt je Zelle (16 pi G/V_t)[Pi_t:Pi_t - (1/2)(tr Pi_t)^2], wobei Pi_t der **Anteil** der Zelle am Impuls ist.
  - Ein Kantenimpuls p^e ist die Summe der Beitraege aller Zellen um e. Form A setzt aber in jede Zelle den vollen p^e. Das ist eine Setzung.
  - HM0 bestaetigt das [P, ERGEBNIS Abschnitt 3]: Bei gleichmaessiger Rate trifft A2 den Kontinuumswert nicht (1,02 bis 1,36; spurfrei 0,019 bis 0,039), A2L trifft ihn auf 1,2e-13.
  - "entspricht" gilt je Zelle, global nicht. Das ERGEBNIS sagt selbst: "Je Tetraeder sind A2 und A2L zueinander invers, global nicht."
- Vorschlag:
  - "wird daraus" ersetzen durch "setzen wir als Form A [W]".
  - "entspricht ... je Zelle" schreiben.
  - Den HM0-Ausgang in 2.3 neben die anderen Punkte A gegen B stellen.

### B2 Shift-Terme in Form B (Abschnitt 2.3)

- Zitat: "L_kin = Summe_t (1/(2 N_t)) qdotᵀ M_t qdot mit hdot = gdot - L_s g"; die Legendre-Zeile nennt keinen Shift.
- Begruendung [M, R2]:
  - Die Formel benutzt qdot, definiert wird aber hdot. Gemeint ist (qdot - B s).
  - Ist die shiftbedingte Kantengeschwindigkeit (B s)_e in allen Zellen gleich, gilt H = (1/2) pᵀ M(N)^-1 p + pᵀ B s. Das ist linear in s, der Shiftteil haengt nicht von N ab, und der Strukturbefund bleibt richtig.
  - Ist sie zellweise verschieden (B_t), etwa weil abseits von flach kein gemeinsamer Rahmen existiert (2.4), wird H quadratisch in s. Dann ist auch s kein Multiplikator mehr.
- Vorschlag: Bedingung "Shift wirkt als globale Kantengeschwindigkeit" in 2.3 nennen und die Notation qdot/hdot vereinheitlichen.

### B3 Legendre braucht eine invertierbare Massenmatrix (Abschnitt 2.3)

- M(N) = Summe_t M_t/N_t ist indefinit: Je Zelle hat DeWitt mit lambda = 1 in 3D die Signatur (5,1).
- Die Formel (1/2) pᵀ M(N)^-1 p setzt det M(N) ≠ 0 fuer alle zugelassenen N voraus. Diese Bedingung fehlt.
- Form A braucht sie nicht, weil sie direkt auf der Impulsseite steht.

### B4 Die lineare Ordnung ist fuer den Strukturbefund blind (Abschnitt 2.3 "Bisherige Rechnungen" und "Folge"; Abschnitt 9, Punkt 2)

- Zitat "Folge [H]": "In den bisher gerechneten Formen stehen die saubere Zwangsstruktur (A) und die Isotropie ohne Abstimmung (B, nur mit RH) gegeneinander."
- Begruendung [M, R4]:
  - Um p = 0, N = 1 ist die N-Abhaengigkeit des Bewegungsterms dritter Ordnung (dN mal p^2).
  - Quadratische Hamilton-Funktion und linearisierte Zwangsbedingungen sind daher fuer A, B und die nichtlokale Variante aus A1 gleich gebaut; nur M(1) unterscheidet sich.
  - Weder Tabelle 4.2 noch die geplante "Algebra-Karte ... linearisiert um das flache Netz V" kann die N-(Nicht-)Linearitaet pruefen.
  - Die Daten zeigen den Gegensatz Isotropie (B mit RH) gegen Stabilitaet, nicht Isotropie gegen N-Linearitaet.
- Vorschlag:
  - In "Folge [H]" beides trennen: Gerechnet ist "isotrop heisst bisher instabil"; "nicht linear in N" ist eine Strukturaussage, die keine Rechnung beruehrt hat.
  - Fuer die Algebra-Karte {H_v, H_w} mindestens in erster Ordnung in p verlangen, oder einen Hintergrund mit p ≠ 0.

### B5 "keine Zwangsbedingung der ueblichen Art" ist haltbar, aber unvollstaendig (Abschnitt 2.3)

- Zitat: "Die N-Variation liefert dann eine Gleichung, in der N selbst stehen bleibt, keine Zwangsbedingung der ueblichen Art."
- Begruendung [M, R2]:
  - C_v = dH/dN_v ist homogen vom Grad 0 und haengt nur von den Verhaeltnissen N_v/N_w ab.
  - Nach Euler gilt Summe_v N_v C_v = H_tot. Die Gesamtskala von N bleibt also freier Multiplikator, und eine globale Bedingung der ueblichen Art bleibt bestehen.
  - Generisch legen die V Gleichungen die V-1 Verhaeltnisse fest und lassen eine globale Bedingung uebrig. Abseits der linearen Ordnung waere die Zaehlung dann die des projizierbaren Falls: eine Zwangsbedingung statt V [H, zu pruefen].
- Literatur:
  - [L] Gambini/Pullin, "consistent discretizations" (ab 2003): Die Diskretisierung legt die Multiplikatoren fest.
  - [P] REGGE-KINETIK-L (RUNDE-48.md Zeile 246): "In stetiger Zeit bleiben die Bedingungen nicht erhalten, wenn Lapse und Shift vorab gewaehlt werden (Friedman/Jack 1986)." Das gehoert in die Literaturzeile von 2.3, die Friedman/Jack bisher nur als "[L, ungeprueft]" fuehrt.
- Vorschlag: den Grad-0-/Euler-Satz und die verbleibende globale Bedingung ergaenzen.

### B6 "saubere Zwangsstruktur (A)" sagt mehr als belegt (Abschnitt 2.3 "Folge"; auch 2.3 Form A: "echte Zwangsfunktion")

- Form A liefert N-freie Zwangsfunktionen. Ob sie erster Klasse sind, ist offen (Abschnitt 4).
- Abseits von flach bricht Regge die Verschiebungssymmetrie (Bahr/Dittrich, im Dokument 2.4 selbst zitiert). Friedman/Jack laut REGGE-KINETIK-L zeigt in dieselbe Richtung.
- Auch A kann am Ende N festlegen.
- Vorschlag: "N-freie Zwangsfunktionen (A; Klasse offen)" statt "saubere Zwangsstruktur".

### B7 "exakt TT-isotrop" (Abschnitt 2.3)

- Zitat: "Form B ist mit der Reduktion RH exakt TT-isotrop (S 1,3e-7, A15 7,5e-8)"
- Begruendung [P, Tab. 4.2 und Text darunter]:
  - Auf V ist die Spanne wegen einer Nullmode nicht trennbar ("Ritz 3,16 %").
  - Auf S und A15 bleibt ein Rest von 1e-7. Er liegt auf der Hoehe der Spanne der affinen Steifigkeit (S 3,5e-8, A15 2,4e-7).
  - Auf Glas liegt die Ritz-Spanne bei 3,5e-6 bis 7,7e-6.
- Vorschlag: "bis auf etwa 1e-7 TT-isotrop (S, A15; Rest auf Hoehe der Steifigkeitsspanne; V nicht trennbar)".

### B8 Spurkoeffizient: Vorbehalt und Vergleich widersprechen sich (Abschnitt 2.2 gegen 2.3)

- Zitat 2.2: "Im Code ist der Spurkoeffizient noch nicht gegen 1/2 gebunden. Vor jedem Vergleich pruefen." Abschnitt 2.3 vergleicht danach Form A mit A1- und A2-Zahlen aus diesem Code.
- HODGE-MASSE-1 meldet als Code-Gegenprobe "A2_t K_t = 1 auf 1,6e-9" und fuer A2L in HM0 "hoechstens 1,2e-13" [P].
- Ist K_t die lambda = 1-Form (das sagt HM0), dann ist A2_t je Zelle ihre Inverse und hat damit den Spurkoeffizienten 1/2 (R1). A1 hat dieselbe Zellform ohne Volumengewicht.
- Vorschlag: entweder diese Kette ausdruecklich als Bindung nennen und den Satz in 2.2 berichtigen, oder die Vergleichszahlen in 2.3 unter Vorbehalt stellen. Welche Lesart stimmt, kann ich ohne Code nicht entscheiden.

### B9 "waere eine andere Theorie" (Abschnitt 4)

- Zitat: "Die andere Lesart (K = 0 als eigenes Gesetz, Horava-Ecke alpha = beta = 0) waere eine andere Theorie und ein eigener Arm."
- Begruendung:
  - SKALAR-SEKTOR-L sagt ohne Gegenbegruendung im Text das Gegenteil: "Mit asymptotisch flachem Rand ist diese Variante die ART in maximaler Zeitscheibung (Jacobson/Pulakkat 2025)" [P, RUNDE-48.md Zeile 61].
  - Formal ist es ein anderes Zwangssystem, unter Randbedingung aber loesungsgleich. Auf dem Torus ist das offen (A4).
  - [L] Shape Dynamics (Gomes/Gryb/Koslowski 2011) behandelt eine Spurbedingung als eigene Erzeugende und ist dual zur ART in CMC-Eichung.
- Vorschlag: "formal ein anderes Zwangssystem; mit asymptotisch flachem Rand nach SKALAR-SEKTOR-L loesungsgleich mit der ART in maximaler Zeitscheibung; auf dem Torus offen".

### B10 "Die Stabilitaetstests (R1, RH) tun genau das." (Abschnitt 4, Energie)

- Die Tests pruefen das Vorzeichen der **quadratischen** reduzierten Energie, und zwar fuer zwei Reduktionen auf sieben Netzen und im Kasten.
- Die zwei Reduktionen widersprechen sich (R1 stabil, RH nicht). "Die" reduzierte Energie des ungefixten Modells ist damit noch nicht bestimmt.
- Auf T^3 hat die globale Volumenmode nach DeWitt eine negative Bewegungsenergie. In der ART ist sie physikalisch (Skalenfaktor), und die globale Bedingung zweiter Ordnung bindet die Wellenenergie an sie [L, Moncrief 1975].
- Negative Richtungen im Kasten (k = 0) sind deshalb vor der Deutung "Instabilitaet" auf diese Mode zu pruefen.
- Vorschlag: "pruefen dies in quadratischer Ordnung fuer zwei Reduktionen; die globale Volumenmode gesondert behandeln".

### B11 Ausweg (ii) loest die Takt-Frage nicht von selbst (Abschnitt 2.3, Auswege)

- Zitat: "(ii) Regime K: kovariante 4D-Zeit mit Zeltstangen. Dort wird keine eigene Bewegungsenergie gesetzt; sie folgt aus der 4D-Regge-Wirkung."
- Der Satz stimmt. Aber in 4D-Regge legen die Gleichungen die Zeltstangenlaengen (den diskreten Lapse) abseits flacher Loesungen in der Regel fest [L, Bahr/Dittrich 2009; Dittrich/Hoehn].
- (ii) ersetzt also die gesetzte Bewegungsenergie, beantwortet aber die Frage nach dem freien Lapse nicht.
- Vorschlag: so vermerken.

### B12 Energiesprung ohne Bezugsgroesse (Abschnitt 6)

- Zitat: "Gemessen: 1,2e-3 bis 3,9e-3 je 2-3-Zug, A2 und R1 [P, HODGE-MASSE-1]."
- Die Zahlen stimmen: Tab. 4.4 gibt je Lauf 1,26e-3 / 3,93e-3 / 1,17e-3.
- Es fehlt, was sie sind: das Mittel von |dH|/H0 je 2-3-Zug, je Lauf, auf Glas mit N = 128 und A = 1e-3, Saaten s1 bis s3 (s4 ohne Zug), hoechstens 3,1e-2.
- "Gemessen" widerspricht dem Kopf ("Modellrechnungen, keine Messdaten").
- Vorschlag: "gerechnet" und die Bezugsgroessen ergaenzen.

### B13 Voraussetzungen der Algebra-Karte (Abschnitt 9, Punkt 2)

- Zitat: "Algebra-Karte: Poisson-Matrix von H_v, D_v, G_v, linearisiert um das flache Netz V, Form A."
- Sie braucht zuerst eine Definition von D_v (A6).
- Linear sieht sie den Unterschied A/B nicht (B4).
- Auf dem Torus muss sie die Nullmoden (konstantes N, globale Verschiebung) gesondert fuehren (A4 b).
- Vorschlag: diese drei Punkte als Vorbedingungen in die Karte.

## C-Befunde (Stil, Kleinigkeiten)

- **C1 "Takt" hat drei Bedeutungen:**
  - der Operator T = 8 d0ᵀ *1 d0 (3.1)
  - maximale Zeitscheiben K = 0 (4)
  - gleiches N fuer alle Zellen (2.3, "globaler Takt")
  - Vorschlag: drei Namen verwenden.
- **C2 Kuerzel ohne Aufloesung:**
  - "HKV": vermutlich Hirani/Kalyanaraman/VanderZee 2013, "Delaunay Hodge star" [L].
  - "HM-B0" (Quelle: CODEX-REVIEW-R48), "Codex Rang 8", "L2 haengt an L1".
  - "Horava-Ecke alpha = beta = 0": Quelle SKALAR-SEKTOR-L nennen.
- **C3 Abschnitt 5, "ist ihr Fehlwinkel":** besser "proportional zum Fehlwinkel"; bezogen auf q_e ist die Ableitung -eps_e/(16 pi G l_e) (R7). Der Lambda-Beitrag (Lambda/8 pi G) dV/dl_e fehlt in der Aufzaehlung.
- **C4 Absolute Kurzformen in 2.3:**
  - "auf allen Netzen" heisst "auf allen sieben gerechneten Netzen und im Kasten".
  - "Kristalle 1" heisst "je 1 auf V, S und A15".
- **C5 "(wie parallel geschaltete Widerstaende)":** Das Bild passt fuer positive Massen. Bei indefinitem M_t (DeWitt) koennen die "Leitwerte" negativ sein; dann hinkt es. Optional einen Halbsatz ergaenzen.
- **C6 Dittrich/Hoehn (Abschnitt 6):** genannt sind nur 1-4 und 4-1. REGGE-KINETIK-L meldet auch "3-2- und 4-1-Zuege senken den Rang der Symplektik (Dittrich/Hoehn 2013, Satz 4.1)", allerdings fuer diskrete Zeit. Ergaenzen oder abgrenzen.
- **C7 Schreibweise:** "Krümmung" (Zeilen 8 und 206) neben "Kruemmung". Ausserdem fehlt in 8 "Gesetzt" die Delaunay-Klasse aus Abschnitt 6, ebenso die Gewichte w_vt, w_ve (in 2.2 als [W] markiert).

## Rechenwege (Anhang zu A und B)

Alle Rechnungen sind von Hand gemacht, ohne Rechner.

### R1 ADM, Spurkoeffizient, Regge-Uebersetzung (2.2): haelt, ausser beim Zellimpuls

- **ADM-Hamilton-Funktion:**
  - Ansatz: L = (1/16 pi G) N wurzel(g) (K:K - K^2 + R - 2 Lambda) und pi = (wurzel g/16 pi G)(K - K g).
  - Daraus: pi:pi = g/(16 pi G)^2 (K:K - 2K^2 + 3K^2) = g/(16 pi G)^2 (K:K + K^2).
  - tr pi = (wurzel g/16 pi G)(K - 3K) = -2K wurzel g/16 pi G, also (tr pi)^2 = 4K^2 g/(16 pi G)^2.
  - Damit pi:pi - (1/2)(tr pi)^2 = g/(16 pi G)^2 (K:K - K^2). Mal 16 pi G/wurzel g ergibt das (wurzel g/16 pi G)(K:K - K^2), den Bewegungsterm.
  - Ergebnis: H = (16 pi G/wurzel g)(pi:pi - (1/2)(tr pi)^2) - (wurzel g/16 pi G)(R - 2 Lambda). Wie im Dokument.
- **Spurkoeffizient:**
  - G h = h - lambda tr(h) I, also G^-1 pi = pi - mu tr(pi) I.
  - Bedingung: lambda + mu(1 - d lambda) = 0, also mu = lambda/(d lambda - 1). Bei lambda = 1, d = 3 ist mu = 1/2. Wie im Dokument.
- **Regge-Kruemmungsanteil:** -(1/16 pi G)(2 Summe l eps - 2 Lambda Summe V) = -(1/8 pi G) Summe l eps + (Lambda/8 pi G) Summe V. Wie im Dokument, Minuszeichen richtig.
- **Gewichte:** Summe_v w_vt = 4 · 1/4 = 1 und Summe_v w_ve = 2 · 1/2 = 1. Ausserdem Summe_v N_v w_vt = N_t (Mittel der 4 Ecken). Passt zu Abschnitt 1.
- **Zellimpuls:**
  - Mit pi = wurzel(g) rho ist Integral_t (16 pi G/wurzel g)(pi:pi - ...) = 16 pi G V_t (rho:rho - ...).
  - Mit Pi_t = rho V_t wird daraus (16 pi G/V_t)(Pi_t:Pi_t - (1/2)(tr Pi_t)^2). Die Form stimmt also, wenn Pi_t der Anteil der Zelle ist.
  - Aus Summe_t Pi_t : Phi_t qdot_t = Summe_e p^e qdot_e folgt aber p^e = Summe_{t enthaelt e} (Phi_tᵀ Pi_t)_e, eine Summe ueber die Zellen.
  - Form A setzt Phi_t^-T p_t, also den vollen Kantenimpuls je Zelle (B1).

### R2 Zwei Zellen, eine gemeinsame Kante (2.3)

- **Ansatz:** L = (1/2) qdot^2 (m1/N1 + m2/N2). Daraus p = (m1/N1 + m2/N2) qdot und H = p^2 N1 N2 / (2 (m1 N2 + m2 N1)).
- **Mit m1 = m2 = 1:** f(N1, N2) = N1 N2/(N1 + N2).
  - Werte: f(1,1) = 1/2 und f(2,0) = f(0,2) = 0. Linearitaet verlangte f(1,1) = (f(2,0) + f(0,2))/2 = 0. Also nicht linear.
  - f(2,2) = 4/4 = 1 = 2 f(1,1), also homogen vom Grad 1.
  - df/dN1 = N2^2/(N1 + N2)^2. Bei (1,3) ergibt das 9/16, bei (2,6) 36/64 = 9/16: Es haengt nur vom Verhaeltnis ab (B5).
- **Allgemein:** M(sN) = M(N)/s, also H(sN) = s H(N). Nach Euler gilt Summe_v N_v dH/dN_v = H.
- **Shift global** [L = (1/2)(qdot - Bs)ᵀ M(N)(qdot - Bs)]: H = (1/2) pᵀ M^-1 p + pᵀ B s.
- **Shift je Zelle (B_t):**
  - Mit b = Summe_t M_t B_t s/N_t gilt qdot = M^-1 (p + b).
  - Damit H = (1/2)(p + b)ᵀ M^-1 (p + b) - Summe_t (1/2N_t) sᵀ B_tᵀ M_t B_t s, quadratisch in s.
  - Probe: Fuer B_t = B gibt das wieder die globale Form.

### R3 Gegenbeispiel zum "Nur" (A1)

- Setze S(N) = (1/2)(D_N M^-1 + M^-1 D_N) mit D_N = diag(N_e) und N_e = (N_a + N_b)/2.
- Weil M^-1 symmetrisch ist, gilt pᵀ S p = Summe_e N_e p^e (M^-1 p)_e. Das ist linear in N.
- Bei N_v = n fuer alle v ist S = n M^-1 = (M/n)^-1, also genau Form B mit N_t = n.

### R4 Ordnung der N-Abhaengigkeit um den flachen Hintergrund (B4)

- **Hintergrund:** q0 flach, p = 0, N = 1, Lambda = 0. Die Stoerungen dq, p und dN sind von der Ordnung eps.
- **Bewegungsterm:** H_kin = (1/2) pᵀ A(1 + dN) p = (1/2) pᵀ A(1) p + O(eps^3).
- **Potential:**
  - Summe_v V_v(q0) = 0.
  - Die erste Variation -(1/8 pi G) Summe eps_e dl_e verschwindet bei eps = 0 (Schlaefli).
  - In zweiter Ordnung bleiben V^(2)(dq) + Summe_v dN_v V_v^(1)(dq).
- **Folge:**
  - In H^(2) geht nur A(1) ein; A, B und S(N) unterscheiden sich dort nur ueber A(1).
  - Unterschiede in N zeigen sich erst in {H_v, H_w} erster Ordnung in p, z. B. Form A: Summe_e [dV_v/dq_e (A_w p)_e - (A_v p)_e dV_w/dq_e].

### R5 Grundgeschwindigkeiten (A3)

- **Skalar:**
  - Bewegungsgleichung: Z_t *0 phi'' = -Z_s d0ᵀ *1 d0 phi - *0 U'(S) phi.
  - Langwellig gilt d0ᵀ *1 d0 ≈ -*0 Laplace, also omega^2 = (Z_s/Z_t) k^2 + U'(0)/Z_t.
- **Maxwell:**
  - Adot = E/*1 und Edot = -d1ᵀ *2 d1 A ergeben *1 A'' = -d1ᵀ *2 d1 A.
  - Langwellig ist das rot rot, also omega^2 = k^2.
- **Geometrie mit ADM-Faktoren:** omega^2 = k^2 im Kontinuum (G kuerzt sich).
- **Zeiteinheit:**
  - Ein gleichmaessiges N0 skaliert alle omega^2 mit N0^2.
  - Mit N0 = Wurzel 8 und Z_s/Z_t = 1 folgt *0 phi'' = -8 d0ᵀ *1 d0 phi - ... = -T phi - ...
- **Skalar richtungsgleich (zu 3.1):**
  - Bei umkreisbasierten Dualen gilt Summe_{e an v} *1_e (x_v - x_w) = Summe_e |Dualflaeche_e| n_e = 0, weil die Dualzelle geschlossen ist.
  - Lineare Funktionen sind also diskret harmonisch; es gibt keinen Korrektor. Mit Summe *1 l lᵀ = Vol I ist die Geschwindigkeit damit richtungsgleich.
  - Maxwell habe ich nicht nachgerechnet; da gilt [P].

### R6 Lapse-Gleichung und Torus (A4)

- **Herleitung:**
  - Spur der ADM-Evolution: dK/dt = -D^2 N + N(R + K^2) + 4 pi G N (S - 3 rho) - 3 N Lambda.
  - Mit der Hamilton-Bedingung R + K^2 = K:K + 16 pi G rho + 2 Lambda folgt dK/dt = -D^2 N + N (K:K + 4 pi G (rho + S) - Lambda).
  - K = 0 erhalten heisst Laplace N = N W, wie im Dokument. Die Gleichung ist quadratisch in K und haengt deshalb nicht von der Vorzeichenkonvention fuer K ab.
- **Torus:**
  - Integral N Laplace N = -Integral |grad N|^2 <= 0, aber Integral W N^2 >= 0 bei W >= 0. Also verschwinden beide Seiten.
  - Dann ist grad N = 0, also N = c, und c^2 Integral W = 0 ergibt c = 0, sobald Integral W > 0.
- **Diskret:** -Nᵀ (d0ᵀ *1 d0) N <= 0 bei *1 >= 0. Dasselbe Argument.
- **Nullmode:** Bei W = 0 hat (-Laplace + W) als Kern die Konstanten.

### R7 Gewichtete Regge-Summe (A5, C3)

- **Schlaefli je Tetraeder:** Summe_{e in t} l_e d theta_{e,t} = 0. Mit eps_e = 2 pi - Summe_t theta_{e,t} folgt Summe_e l_e d eps_e = 0.
- **In H_tot steht** -(1/8 pi G) Summe_e N_e l_e eps_e. Die Ableitung nach l_e ist -(1/8 pi G)[N_e eps_e + Summe_e' (N_e' - c) l_e' d eps_e'/d l_e]. Hier ist c beliebig, und der zweite Term verschwindet nur bei gleichem N.
- **Nach q_e = l_e^2** (bei N = 1): -eps_e/(16 pi G l_e).

### R8 Pachner, Delaunay, Bipyramide (Abschnitt 6): haelt

- **Pachner:** Eine 3-Kugel (ein Teil des Randes eines 4-Simplex) wird durch die komplementaere 3-Kugel mit derselben 2-Sphaere als Rand ersetzt. Das ist ein PL-Homoeomorphismus, die Topologie bleibt also gleich.
- **Delaunay:** Die Umkreismittelpunkte der Tetraeder sind die Voronoi-Ecken. Das umkreisbasierte Dual einer Kante ist die Voronoi-Facette zwischen ihren Endpunkten. Ihre Flaeche ist >= 0 und = 0 bei Kosphaerizitaet, also am Zug.
  - Der Protokollsatz "*1 >= 0 [M]" (RUNDE-48.md Zeile 390) haelt fuer periodische Delaunay-Netze, wenn sie echte Simplizialkomplexe sind [L, HKV 2013: "pairwise Delaunay" ergibt nichtnegative duale Volumina].
  - Im Dokument steht der Satz nur als "zu pruefen"; das ist vorsichtiger als noetig, aber nicht falsch.
- **Bipyramide:** 5 · 3 - 6 = 9 Freiheitsgrade, gleich der Kantenzahl der Zwei-Tetraeder-Lage (3 + 6).

### R9 Weitere Stellen, die halten

- **H_tot ist auf den Loesungen null.**
  - Form A: Summe von Zwangsbedingungen.
  - Form B: nach Euler ebenfalls (Summe N_v C_v).
- **Gauss:**
  - {G_v, G_w} = 0.
  - H haengt von A nur ueber d1 A ab, und d1 d0 = 0.
- **3.1:** Die Euler-Lagrange-Gleichung von L_phi auf festem Netz stimmt.

## Zahlenabgleich (Auftrag C)

| Stelle | Dokument | Quelle | Ergebnis |
|---|---|---|---|
| 2.3 | V: A1 6,34 %, A2 5,92 % | Tab. 4.2 A1R1 6,339 %, A2R1 5,924 % | stimmt |
| 2.3 | S 1,3e-7, A15 7,5e-8 | Tab. 4.2 A2LRH 1,34e-7, 7,53e-8 | stimmt ("exakt": B7) |
| 2.3 | Kristalle 1, Glas 46 bis 50 | A2LRH V/S/A15 je neg 1; Glas 48/50/47/46 | stimmt |
| 2.3 | V 10,6 %, S 0,74 %, A15 4,7 % | A2LR1 10,56 %, 0,743 %, 4,69 % | stimmt |
| 2.3 | Glas 28 bis 33 (A2LR1) | 28/31/33/28 | stimmt |
| 2.3 | kleinstes Volumen 0,007 des Mittels | ERGEBNIS 4.2, Code-Gegenproben "vol_min/Mittel 0,007" | stimmt |
| 2.3 | R1 mit A1/A2 "auf allen Netzen stabil" | Tab. 4.2 ohne *, ERGEBNIS Abschnitt 2 Punkt 5 | stimmt fuer die sieben Netze und den Kasten (C4) |
| 2.3 | "auf Glas ... alle Paarungen ausser A1 und A2 mit R1; Kristalle dort regulaer" | Tab. 4.2 A2LR2 und A2LRH | **falsch** (A2) |
| 6 | 1,2e-3 bis 3,9e-3 je 2-3-Zug | Tab. 4.4 je Lauf 1,26e-3 / 3,93e-3 / 1,17e-3; RUNDE-48.md 10:20 | stimmt gerundet (Bezug fehlt: B12) |
| 2.2 | A2 = Masse ~ Volumen (HM-B0) | RUNDE-48.md Zeile 266 | stimmt |
| 2.3 | globaler Takt durch SKALAR-SEKTOR-L ausgeschlossen | RUNDE-48.md Zeile 65 | stimmt |
| 2.3/6 | LUND-REGGE-MASSE-1, DANZER-TT-1, V1-AUFHEBUNG-1 laufen; SPLITTER-FREI-1 Warteschlange; KRUEMMUNG-SPANNUNG-SPIN-L laeuft | RUNDE-48.md Zeilen 22, 23, 28, 383, 402, 408 | stimmt zum Stand 10:44 |

Rundungen geprueft: 1,17e-3 wird zu 1,2e-3, 3,93e-3 zu 3,9e-3, 10,56 zu 10,6, 4,69 zu 4,7, 0,743 zu 0,74. Alle richtig.

## Codex-Punkte einzeln (Auftrag B)

| Codex | Eingearbeitet | Nur benannt oder offen |
|---|---|---|
| 1 Konvention | Phasenraumform, A0 als Multiplikator, ADM-Vorzeichen und 1/8 pi G, 1/N_t in Form B, N-Interpolation, Spurkoeffizient 1/2 | D_v nur dem Namen nach ("genaue Form steht noch aus"), s-Interpolation fehlt, Spurbindung im Code offen (A6, B8) |
| 2 Hodge legt nicht alles fest | [W]-Marken, c^2 ~ Z_s/Z_t, Rang 2 gegen Rang 4, metrische Kopplung als Setzung | gemeinsame Zeiteinheit nur verlangt; die Formeln widersprechen ihr (A3) |
| 3 Klassen, K = 0, Positivitaet | Wahl "ungefixt", K = 0 als Eichfixierung, Pruefliste, kein Positiv-Energie-Import, Lapse-Gleichung genannt | eingearbeitet. Neu und nicht von Codex: Torus-Hindernis und Nullmode (A4) |
| 4 Ladung | neutraler erster Arm, U(S), A reell und nicht kompakt, zweiter Arm mit Linktransport und A0, rho aus den Materieimpulsen | eingearbeitet |
| 5 Umklappen und Zutaten | Mass null, E^2/*1 singulaer, M- gegen M^-1-Stetigkeit, Uebergabe mit Gauss, drei getrennte Erhaltungen, 9 Freiheitsgrade, Sprung als [H], Lambda/SOC/Kaehler-Dirac/hbar ausgelagert, Titel geaendert | im Schlussabsatz nur teilweise: "von selbst" und "Einsteins Gleichung" versprechen wieder mehr (A7) |

**Wo Fassung 2 mehr verspricht, als die Definitionen tragen:**
- Abschnitt 2.1: "werden unten definiert" (D_v).
- Abschnitt 0: "alle Multiplikatoren", "alle uebernommen".
- Abschnitt 3.1: "Gleiche Grundgeschwindigkeit" bei Formeln mit verschiedenen Faktoren.
- Abschnitt 4: "K = 0 ist eine Eichfixierung" auf dem Torus.
- Abschnitt 5: "Feldgleichung selbst".
- Einfach gesagt.

## Urteil zum Strukturbefund 2.3

**Haelt mit Bedingung.**

1. Richtig ist der Kern:
   - Form A ist linear in N.
   - Die Lund-Regge-Form B gibt nach Legendre (1/2) pᵀ (Summe_t M_t/N_t)^-1 p. Das ist bei zellweise verschiedenem N nicht linear; dH/dN_v haengt dann von den Lapse-Verhaeltnissen ab.
   - Das gilt fuer jede zellweise Lapse-Interpolation, solange der Shift als globale Kantengeschwindigkeit wirkt und M(N) invertierbar ist (B2, B3).
2. Nicht haltbar sind die zwei "nur" (A1):
   - B ist entlang jedes Strahls N = s N̂ linear.
   - Eine nichtlokale Kopplung, (1/2) Summe_e N_e p^e (M^-1 p)_e, ist linear in N und bei gleichem N gleich B.
   - "Keine Zwangsbedingung der ueblichen Art" gilt nur fuer die lokalen Gleichungen; eine globale Bedingung bleibt (B5).
3. Die Folgerung, die gerechneten Zahlen zeigten einen Gegensatz von Zwangsstruktur und Isotropie, traegt nicht:
   - Die N-Abhaengigkeit des Bewegungsterms geht um p = 0 erst in dritter Ordnung ein (B4). Belegt ist nur "isotrop (B mit RH) heisst bisher instabil".
   - Den globalen Takt als projizierbar einzuordnen ist richtig, er ist aber nicht die einzige Lage, in der B linear wird.

## Selbstanzeigen

- Gegen die harten Regeln habe ich nach meiner Kenntnis nicht verstossen.
  - Benutzt: nur date, ls, wc, grep, sed -n (lesend) sowie Read.
  - Geschrieben: nur diese Datei. Den Ordner hat das Schreibwerkzeug beim ersten Write angelegt.
- `ls -la` auf RUNDE-37 zeigte die Ordnernamen anderer Karten und Leser (z. B. codex-review-r48, gemeinsames-netz-v4x-leser). Geoeffnet habe ich keinen davon.
- Fassung 1 habe ich erst nach Fassung 2 und nur per grep auf Kernbegriffe angesehen, nicht ganz gelesen.
- RUNDE-48.md ist die laufende Leitungsdatei. Ich habe bis Zeile 413 gelesen, also auch Eintraege nach dem Start dieser Pruefung (10:52 ff., andere Themen). Auf die Befunde hat das keinen Einfluss.
- Literatur stammt nur aus dem Gedaechtnis [L] und ist an keiner Quelle geprueft; Jahreszahlen und Einzelheiten koennen abweichen. Betroffen: Moncrief 1975, Fischer/Marsden/Moncrief 1980, Gambini/Pullin, Bahr/Dittrich 2009, Gomes/Gryb/Koslowski 2011, HKV 2013, York-Zeit.
- Zwei Punkte habe ich nicht am Code geprueft:
  - B8 (Spurbindung).
  - Die Lesart der HM0-Zahlen fuer A2 ("1,02 bis 1,36; spurfrei 0,019 bis 0,039": Verhaeltnis oder Abweichung?). Die Zahlen sind woertlich aus dem ERGEBNIS uebernommen; B1 haengt nur am Wortlaut "verfehlt".
- Eine BRIEF-Datei mit sha256 wurde nicht genannt. Grundlage war die Nachricht der Leitung.
