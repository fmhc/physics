# PAAR-REGGE-2: Plan des Code-Agenten (Runde 46)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 05:42:36 CEST (date), Zeitbox 90 min.
  Plan geschrieben ab 05:49:55 CEST (date), vor jedem Lauf auf der .69.
- Gelesen: KARTE.md (ganz); hish-glueball-l/DOSSIER.md (ganz), ARBEITSFELD.md Z. 240-300; paar-regge-1/ERGEBNIS.md,
  PLAN.md, code/paar_regge.py (nur gelesen); H5 Z. 130-260, 1416-1500, 2440-2720 und PDF-Seiten 47-48 als Bild;
  Sharov S1 und S2 im Volltext (Abschn. 0); A&T Tab. 17 (gluon-paar-l/quellen/F3 Z. 1983-1993).
- Ordner: lokal RUNDE-37/paar-regge-2/; .69: /home/fmh/fmhc-physics-remote/paar-regge-2/ (code/, lauf/).
- Kennzeichen: [E] gerechnet (.69), [M] eigene Rechnung von Hand (nicht gegengelesen), [S] an der Quelle gelesen,
  [P] Projektdatei, [L] Gedaechtnis, [H] Hypothese, [F] Festlegung dieses Plans (nicht aus der Karte), [D] Diagnose
  ohne Urteil, [ES] eigener Schluss.
- Modelle, Daten, Messgroessen, PQ0 bis PQ3, Wahrscheinlichkeiten und Bedeutung der Karte bleiben unveraendert.
- Massen in Einheiten sqrt(sigma), sigma = Fundamentalspannung, c = 1.

## 0. Zuerst: Hat Sharov den Fit schon gemacht? Nein. Die Karte bleibt Rechnung, keine Nachrechnung.

Abrufe (quellen/ABRUFE.log, Erwartung jeweils vorher eingetragen):
- S1 hep-ph/0612373 (2006) und S2 arXiv:0712.4052 (2007), beide im Volltext gelesen [S].
- S3 INSPIRE 789679: Sharov 2008, Phys. Atom. Nucl. 71 (2008) 574-582. Nur Metadaten und Referenzliste; kein
  arXiv-Volltext, drei Abrufe verbraucht.

Befund [S]:
- **Sharov rechnet klassische Rotationsloesungen und fittet keine Gittermassen.**
  - S1: exakte Loesungen des geschlossenen Strings mit zwei Punktmassen. Asymptotik J ~ alpha' E^2 + alpha1 E^(1/2)
    + alpha0 mit alpha' = (1/(2 pi gamma)) n1/(n1^2 - n2^2) (Gl. 47-48).
  - Der lineare Zustand (n1, n2) = (2, 0) ("two masses ... connected two strings") hat den Faktor 1/2. Das ist
    klassisch genau unser Modell (I).
  - Verglichen wird nur qualitativ mit der Pomeron-Geraden J ~ 1,08 + 0,25 M^2.
- **S2 nennt Zahlen, macht aber keinen Fit.**
  - Gewaehlt sind gamma = 0,175 GeV^2 und m1 = m2 = 700 MeV (aus Gluon-Propagator-Abschaetzungen, Gl. 73).
  - Spin S = 2 mit J = L + S (Gl. 71) und ein Spin-Bahn-Term (Gl. 72).
  - Fig. 3 zeigt die Trajektorien nur gegen die Pomeron-Gerade; kein chi^2, keine Gittermasse im Vergleich.
- Beide Schlussabschnitte: "These corrections are to be significant for calculation of the intercept alpha0." Einen
  festen Quanten-Intercept setzt Sharov also nicht.
- [ES] Sharovs J = L + S mit S = 2 verschiebt die (2,0)-Trajektorie zahlenmaessig um +2, wie a = 2 aus H5. Die Herkunft
  ist aber eine andere (Konstituenten-Spin statt Quanten-Intercept), dazu kommt sein Spin-Bahn-Term. Das rechne ich
  nicht nach; es wird nur berichtet.
- Offen: Ob Sharov 2008 (S3) Gittermassen vergleicht, ist nicht gelesen. Die Referenzliste enthaelt Morningstar/Peardon
  1999, Meyer/Teper 2005, Meyer 2005 und Lucini/Teper/Wenger 2004. Die beiden Volltexte unmittelbar davor (S1 Dez.
  2006, S2 Dez. 2007) lassen den Intercept ausdruecklich offen; ein Fit mit festem a = 1 oder 2 ist daher
  unwahrscheinlich, aber nicht ausgeschlossen [ES].

## 1. H5 an der Quelle [S]

- Gl. (1.4): a_open = (D - 2)/24 + (26 - D)/24 = 1. Gl. (1.5): a_closed = (D - 2)/12 + (26 - D)/12 = 2. Dazu (1.6)
  J = alpha' M^2 + 1, (1.7) J = alpha' M^2/2 + 2, alpha' = 1/(2 pi T) (H5 Z. 211-233). Konvention also J = J_cl + a.
- Abschn. 5.2.1 (Z. 1416-1497): Massen m0, ml auf den Faltstellen. Randbedingung (5.7) "the same equations as for a
  rotating open string solution with massive endpoints"; "Classically this string is completely equivalent to an open
  string with massive endpoints ..., with the string tension effectively doubled".
  - [M] (5.7) ergibt sin^2(phi)/cos(phi) = (1 - v^2)/v = m omega/(2T), also kappa/omega = m v/(1 - v^2) mit
    kappa = 2T. Das ist die [P]-Randbedingung von PAAR-REGGE-1.
  - Modell (I) ist also klassisch der PAAR-REGGE-1-String mit kappa = 2.
- Gl. (7.9), auf PDF-Seite 48 als Bild gelesen:
  a = 2 + (3D - 55)/(24 pi) (eps1 + eps2) + (D - 3)/(24 pi^2) (eps1 + eps2)^2 + (D - 3)/(24 pi^3) (eps1 + eps2)^3
  + (8D - 495)/(1440 pi) (eps1^3 + eps2^3) + ..., "in the small masses expansion".
- **eps1, eps2 sind eindeutig definiert:**
  - direkt unter (7.9) "where eps1 = 1/gamma0 and eps2 = 1/gamma_l", ebenso Z. 1743 "eps1 = 1/gamma0 and
    eps2 = 1/gamma_l";
  - gamma0 = 1/sin(phi), gamma_l = 1/sin(delta + phi) nach (5.9), mit den Faltstellen-Geschwindigkeiten beta0 = cos(phi),
    beta_l = -cos(delta + phi) nach (5.8);
  - also eps = sqrt(1 - v_end^2) des klassischen Zustands, bei gleichen Massen eps1 = eps2.
  - **Die Variante (I') wird gerechnet.**
- [M] Erste Ordnung in D = 4: a = 2 - (43/(24 pi)) * 2 eps = 2 - 1,140612 eps.
- Folgen [M, F]:
  - Der Intercept haengt vom Zustand ab (eps bei J = 2 und J = 4 verschieden). J = J_cl + a(eps) wird gemeinsam in
    eta geloest (v = tanh(eta)). J_cl(eta) und a(eta) steigen beide mit eta, die Loesung ist also eindeutig.
  - Bei eta -> 0 gilt a -> 2 - 1,1406 = 0,859; bei m = 0 gilt a = 2.
  - Gueltigkeit: Entwicklung in 1/gamma (kleine Massen); die Bedingung in H5 Abschn. 5.2 hat in der Textkopie
    verlorene Zeichen.
  - Beim besten m berichte ich eps(2), eps(4) und die Groesse der Terme zweiter und dritter Ordnung, nur
    beschreibend [D].

## 2. Modelle (Karte; Ergaenzungen [F])

- Klassischer, starr rotierender Nambu-Goto-String, zwei gleiche Massen m, Spannung kappa sigma. Formeln [P] wie in
  PAAR-REGGE-1, Funktionen EJ/loese unveraendert uebernommen:
  - kappa/omega = m v/(1 - v^2);
  - E = 2 m gamma + (2 kappa/omega) arcsin v;
  - J_cl = 2 m v^2 gamma/omega + (kappa/omega^2) (arcsin v - v sqrt(1 - v^2)).
- J = J_cl + a.
- **(I)** kappa = 2, a = 2. **(II)** kappa = 9/4, a = 1. **(I')** kappa = 2, a = 2 - 1,140612 eps(Zustand).
- **Zehn Kandidaten:** kappa = 9/4 (Steigung 4/9) und kappa = 2 (Steigung 1/2), mal a = 0, 1/12, 1/6, 1, 2. Die Liste
  stammt aus hish-glueball-l/ARBEITSFELD.md Z. 273 [P]. (I) und (II) sind zwei davon.
- **[F] J_cl = 0, also a = J:** Das ist ein ruhendes Paar mit E = 2m, v = 0, Laenge 0. Es betrifft a = 2 bei J = 2, also
  (I) und (9/4, 2). Der Grenzwert J_cl -> 0+ der [P]-Formeln ist stetig [M]; Kontrolle K3 prueft das.
- **Numerik [F]:**
  - Wie PAAR-REGGE-1: brentq in eta, m-Gitter mit Schritt 0,002, dann Verfeinerung (bounded) und m = 0 immer geprueft.
  - Das Gitter reicht bis m = 6 (3001 Punkte) statt 4, weil (I) auf (C) etwa m = 3,39 braucht [M].
  - Liegt das beste m am Rand 6, wird das markiert.

## 3. Daten (Karte woertlich)

- (A) A&T 2020 Tab. 17: 2++ gs 4,894(22), 4++ gs 7,60(12)* [S, F3 Z. 1986 und 1993]. chi^2 diagonal.
- (B) MT-Gerade s = 0,281(22), a0 = 0,93(24) wie in PAAR-REGGE-1. Hauptlesart R3 (Parameterraum, Sekante des Modells
  durch J = 2 und 4), dazu R1 und R2. Definitionen unveraendert aus PAAR-REGGE-1 PLAN Abschn. 3.
- (C) 2++ ex1 6,788(40) statt 2++ gs, mit 4++ gs 7,60(12)* [S, F3 Z. 1988 und 1993]. chi^2 diagonal.

## 4. Fit und Messgroessen

- Ein freier Parameter m >= 0. Zwei Datenpunkte (A, C: Massen; B-R3: s und a0), also 1 Freiheitsgrad,
  p = P(chi^2_1 >= chi^2).
- Je Kandidat und Datensatz:
  - bestes m, chi^2, p, 1-sigma-Intervall von m (Delta chi^2 <= 1), Delta chi^2 bei m = 0;
  - v_end(2), v_end(4), E(2), E(4), Sekante (s, a0) und die Zahl lokaler Gitterminima.
  - Fuer (I') zusaetzlich a(2), a(4), eps(2), eps(4) und die Terme hoeherer Ordnung [D].
- **Baender wie PAAR-REGGE-1, hier je Kandidat und Datensatz (nur ein a je Kandidat) [F]:**
  - "(a) traegt": p >= 0,05 und 0,70 <= v_end(2) <= 0,82;
  - "masselos": p >= 0,05 und Delta chi^2(m = 0) <= 1;
  - "traegt nicht": p < 0,05;
  - "uebrig" [F]: keines davon.

## 5. Urteile

| Nr | Karte | nach Plan [F] | nach Kartenwortlaut [F] |
|---|---|---|---|
| PQ0 | masselose Werte (I) 0 und 5,013, (II) 3,760 und 6,512 auf 1e-6 reproduziert | eingetroffen, wenn (i) der allgemeine Loeser bei m = 1e-8 die geschlossene Form sqrt(2 pi kappa J_cl) (bzw. 2m fuer J_cl = 0) auf 1e-6 trifft (relativ; absolut beim Wert 0) und (ii) die geschlossene Form die Kartenzahlen auf deren Rundung trifft (<= 5e-4) | absolute Abweichung <= 1e-6 von den Kartenzahlen; siehe Abschn. 6 (a) |
| PQ1 | (I) mit (A): eine Endmasse gibt p >= 0,05 | p(bestes m) >= 0,05 fuer kappa = 2, a = 2 fest | wie nach Plan. (I') ist "Variante zu (I)", nicht (I), und zaehlt nicht; ihr Ausgang wird daneben berichtet |
| PQ2 | (II) mit (A): eine Endmasse gibt p >= 0,05 | p(bestes m) >= 0,05 fuer kappa = 9/4, a = 1 fest | wie nach Plan |
| PQ3 | mit (C) erreicht mindestens eines der Modelle p >= 0,05 | (I) oder (II) auf (C) | (I), (II) oder (I'); (I') steht in der Karte unter "Modelle" |

## 6. Vorab ableitbar (Schreibtisch [M], vor jedem Lauf; diese Zahlen sind keine Messungen)

- **(a) PQ0 nach Kartenwortlaut ist vorab nicht erfuellbar, wegen der Rundung der Karte.**
  - Exakt [M]: sqrt(8 pi) = 5,013257; sqrt(4,5 pi) = 3,759942; sqrt(13,5 pi) = 6,512411.
  - Abstand zu 5,013 / 3,760 / 6,512 also 2,6e-4 / 5,8e-5 / 4,1e-4, jeweils > 1e-6. Nur "(I) M(2) = 0" ist exakt.
  - Nach Wortlaut also "nicht eingetroffen (Rundung der Karte)"; das ist keine Messung. Nach Plan entscheidet der Lauf.
- **(b) Modell (I) bei J = 2: J_cl = 0, also E(2) = 2m und v_end(2) = 0 fuer jedes m.**
  - Das Band "(a) traegt" ist fuer (I) und (9/4, 2) auf jedem Datensatz unerreichbar.
  - "masselos" ist auf (A) und (C) unerreichbar, denn M(2) = 0.
- **(c) Steigungsschranke, betrifft PQ3:**
  - Entlang einer Trajektorie mit festem m gilt dE/dJ = omega (PAAR-REGGE-1 K3 [E]) und
    E omega = 2 kappa [sqrt(1 - v^2)/v + arcsin v] >= pi kappa [M]. Also dJ/dM^2 <= 1/(2 pi kappa) und
    M(4)^2 - M(2)^2 >= 4 pi kappa, fuer jedes m und jedes feste a.
  - (C) hat 7,60^2 - 6,788^2 = 11,68 +- 1,90 [M]; die Schranke ist 25,13 (kappa = 2) bzw. 28,27 (kappa = 9/4).
  - Linearisiert ist chi^2 >= ~50 bzw. ~75 [M]. Damit ist **PQ3 fuer (I) und (II) und fuer alle zehn Kandidaten vorab
    "nicht eingetroffen"**; der Lauf prueft die Schranke (K5) und rechnet die Fits trotzdem.
  - Fuer (I') gilt die Schranke nicht streng, weil a bei J = 2 und 4 verschieden ist. Die schwaechste Fassung,
    2 pi kappa (2 - 1,1406) = 10,8, liegt unter 11,68. Fuer (I') ist PQ3 also nicht ableitbar. Ich erwarte ein
    Scheitern, gerechnet habe ich es nicht.
- **(d) PQ1, Schreibtisch [M]:**
  - E(2) = 2m legt m ~ 2,447 +- 0,011 fest.
  - Bei diesem m, J_cl = 2 und kappa = 2 gibt meine Handrechnung v_end(4) ~ 0,553 und E(4) ~ 8,17, Gitter 7,60(12).
  - Linearisiert mit dem Ausgleich in m (~ -0,007) folgt chi^2 ~ 22, p ~ 3e-6.
  - **Erwartung: PQ1 nicht eingetroffen**, weitgehend vorab ableitbar. Die genaue Zahl liefert der Lauf.
- **(e) PQ2, Schreibtisch [M]:**
  - Bei m = 1 gibt meine Handrechnung E(2) ~ 4,843 (v ~ 0,69) und E(4) ~ 7,356.
  - Mit Delta E ~ m^(3/2) folgt fuer E(2) = 4,894 ein m ~ 1,03 und E(4) ~ 7,40, also chi^2 ~ 3, p ~ 0,08.
  - Die Handrechnung ist auf etwa +-0,05 in E(4) genau; das gibt chi^2 ~ 2 bis 4. **Der Ausgang ist offen, nicht
    ableitbar.** v_end(2) ~ 0,69 liegt an der Bandkante 0,70.
- Erwartung fuer (B) und die uebrigen Kandidaten: nicht gerechnet.

## 7. Kontrollen

- K1 (PQ0): geschlossene Form und allgemeiner Loeser bei m = 1e-4, 1e-6, 1e-8 fuer (I) J = 2, 4 und (II) J = 2, 4.
- K2: erster Hauptsatz dE/dJ = omega entlang der Trajektorie, kappa = 2 und 9/4, m = 1, eta = 0,1 bis 3.
- K3: Stetigkeit bei J_cl -> 0: E(J_cl = 1e-10) gegen 2m, m = 0,5; 1; 2,5.
- K4: Nachrechnung PAAR-REGGE-1 (kappa = 9/4, a = 0 und 1/12; (A) und (B-R3)). Soll [P]: chi^2 370,77 / 202,11 und
  70,08 / 67,03; m = 0 / 0 / 0,258 / 0,413. Toleranz 1e-2 relativ in chi^2, 2e-3 absolut in m [F].
- K5: Steigungsschranke numerisch. Min ueber das m-Gitter von (E4^2 - E2^2)/(4 pi kappa) >= 1 - 1e-9, fuer alle zehn
  Kandidaten.
- K6: Variante (I'): m -> 0 gibt a -> 2 und die masselosen Werte; J(eta) monoton auf einem Gitter.
- Budget: Zeit je Loesung, ohne Datensicht.

## 8. Laufliste (nur .69, kleintest.sh, Spuren cpu5 und cpu6, je Lauf <= 10 min, 1 Thread)

1. R0 Rauchtest (cpu5, <= 120 s), Modus "rauch": K1, K2, K3, K6 und Budget, keine Datenfits. Danach Plan und Code
   einfrieren (Kopien mit Zeitstempel, EINGEFROREN-SHA256.txt).
2. R1 "kontrollen" (cpu5): K1 bis K6 und Budget.
3. R2 "fits" (cpu6), parallel zu R1: zehn Kandidaten mal (A, B-R3, B-R1, B-R2, C) = 50 Fits, dazu (I') auf denselben
   fuenf.
4. R3 "bild" (cpu5): J gegen M^2 aus fits.json, eingefrorener Code.

- Skripte auf der .69 nie in place ueberschreiben (neue Fassung per mv).
- Keine Aenderung von Baendern, Lesarten oder Code nach der Sicht auf Fit-Ergebnisse. Fehler danach nur als
  Selbstanzeige und, wenn noetig, als getrennt gekennzeichnete Diagnose.

## 9. Look-elsewhere [F]

- Berichtet werden alle zehn Kandidaten je Datensatz, dazu die Zahl der Kandidaten mit p >= 0,05.
- (I) und (II) hat die Karte vorab festgelegt; nur sie tragen PQ1 und PQ2. Die uebrigen acht sind Kontext.
- Ein Treffer unter zehn Kandidaten mit je einem freien Parameter ist schwach: Mit zehn Intercept-Steigungs-Paaren
  und freier Masse findet sich leichter einer, der zwei Punkte trifft. Die Zahl der Treffer je Datensatz wird
  berichtet; eine formale Korrektur rechne ich nicht.

## 10. Rauchtest R0 (vor dem Freeze; Text fertig 2026-10-05 05:56:48 CEST, date)

- Lauf 1 (03:55:24 UTC, cpu5): rc = 1. Fehler im Rauchpfad: chi2_funktion kannte den synthetischen Datensatz "S"
  nicht (ValueError "diag"). Behoben: Abfrage "datensatz in DATEN" statt ("A", "C"). Nur der Rauchpfad war betroffen.
- Lauf 2 (03:55:35 bis 03:55:39 UTC, cpu5): rc = 0, 2,5 s. Ergebnisse [E], nur Kontrollen ohne Datenfit:
  - K1: Loeser bei m = 1e-8 gegen geschlossene Form: 2e-8 (Wert 0, absolut), 2,1e-13, 2,8e-13, 1,4e-13 (relativ).
    Geschlossene Form gegen Karte: 0; 2,57e-4; 5,76e-5; 4,11e-4. Also PQ0 nach Plan erfuellt, nach Wortlaut nicht,
    wie in Abschn. 6 (a) vorab abgeleitet.
  - K2: dE/dJ = omega bis 3,5e-9 (kappa = 2 und 9/4).
  - K3: E(J_cl) - 2m = 3,8e-4 bei J_cl = 1e-6 und 8,1e-7 bei 1e-10; stetig.
  - K6: J(eta) der Variante streng monoton; a(eta -> 0) = 0,8594. Bei m = 1e-8 gibt (I') E(4) = 5,01337 (masselos
    5,01326) und E(2) = 0,092 statt 0: Der masselose Grenzwert bei J = 2 wird nur langsam erreicht (eps = 5,9e-4,
    J_cl = 6,7e-4) [D].
  - K7: synthetische Rueckgewinnung (m = 1,3, Pseudodaten aus dem Modell) fuer (I), (II), (I'): m = 1,300, chi^2 = 0.
  - Budget 0,13 ms je Loesung (fest und Variante).
- Bild-Rauchtest (03:56:01 bis 03:56:04 UTC, cpu5, rc = 0): gezeichnet sind die Gitterpunkte und die synthetischen
  Kurven bei m = 1,3, keine Fits. Offenlegung: Ich habe dieses Bild angesehen, also die Lage der Daten gegen die
  Modellkurven bei m = 1,3. Keine Aenderung an Plan, Baendern oder Lesarten danach.
