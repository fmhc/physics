# HISH-GLUEBALL-L: Arbeitsfeld (eine Datei, vor jedem Schritt neu gelesen; Gestrichenes bleibt stehen)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-05 05:16:32 CEST (date). Zeitbox 45 min, also Abgabe
  spaetestens ~06:01 CEST. Abrufe hoechstens 10.
- Kennzeichen: [S] an der Quelle gelesen (Z. = Zeile der lokalen Textkopie), [S Abstract], [P] Projektdatei, [L]
  Gedaechtnis, [L?] unsicher, [M] von Hand gerechnet (nicht gegengelesen), [ES] eigener Schluss, [H] Hypothese.
- Erwartungen G1 bis G4 und ihre Bedeutung: woertlich aus KARTE.md, unveraendert (G1 70 %, G2 65 %, G3 60 %, G4 60 %).

## 0. Vorlektuere (nur gelesen, [P])

- PAAR-REGGE-1 (ERGEBNIS.md Abschn. 1, 3, 8): offener Nambu-Goto-String, sigma_A = 9/4 sigma, zwei gleiche
  Endmassen, Intercept fest a = 0 oder 1/12. Daten (A) A&T 2020: 2++ 4,894(22), 4++ 7,60(12)* (in sqrt(sigma));
  (B) MT-Gerade: Steigung 0,281(22) (Einheit Mesonsteigung 1/(2 pi sigma)), Intercept 0,93(24). Ergebnis: traegt in
  keinem Datensatz; 2++ liegt schon unter dem masselosen Wert (5,317 bei a = 0); Endmassen senken den
  Sekanten-Intercept weiter. Nicht geprueft: freier Intercept.
- gluon-paar-l (Abschn. 1, 4, 12): Steigungen in Mesoneinheiten: Gitter MT 0,281(22), aus A&T 0,372(20) [M];
  offenes adjungiertes Paar 4/9 = 0,444; Ring 1/4 (phononisch) bzw. 0,325 (orbital); 1/2 nur fuer den zur Strecke
  gefalteten Ring. MT deuten die fuehrende 3+1D-Trajektorie als OFFENEN adjungierten String. O1: Fit rotierender
  Strings mit Endmassen an Gitter-Glueballs nicht gefunden.
- regge-hadron-ref-l (6.3, 6.4, 7): [161] = arXiv:1812.01619 = INSPIRE recid 1707033 (A9-abstracts.txt Z. 89-92 [P]);
  Abstract: "non-linear Regge trajectories of a string with massive endpoints", "Glueballs, together with a method to
  disentangle them from flavorless mesons".

## 1. Projekt-grep (eigener, 05:17 CEST, mit allen Pflicht-Ausschluessen, ohne *.json)

- "1812.01619": nur RUNDE-37/regge-hadron-ref-l (Dossier, Arbeitsfeld, Artikeltext) und diese Karte.
- "Weissman": regge-anschluss-20260912.md, paar-regge-1 (PLAN, ERGEBNIS: nur [L]), gluon-paar-l, regge-hadron-ref-l,
  RUNDE-45.md; or-jury-20260911/r9/prompt-or-jury-a-H1.txt Z. 332-472 (Mesonen 2014 = 1402.5603, Baryonen 2015,
  Quantisierung 2018 = 1801.00798, alles ohne Glueballs); Scout-jsonl: nur 2608.27224 (Random-Matrix, unverwandt).
- "HISH", "folded closed": nur diese Karte, regge-hadron-ref-l und RUNDE-45.md.
- Ergebnis: HISH-Glueballs im Projekt nicht gelesen (wie Karte).

## 2. Lokale 24-Monats-Spur ohne Abruf (gluon-paar-l/quellen/F5-api-glueball-24m.xml, 58 Treffer, [P]/[S Abstract])

- arXiv:2605.02373 "Geometric QCD III" (2026): geschlossener String, "parameter-free glueball trajectories ... open-string
  tension ... recovers the exact Luescher intercept alpha(0) = 1/12, perfectly matching ... lattice" (XML Z. 364)
  [S Abstract]. Im gluon-paar-l-Dossier als spekulativ markiert. **Bemerkenswert:** fester Intercept 1/12 wird dort als
  Treffer behauptet, PAAR-REGGE-1 fand ihn als Scheitern (anderes Modell: geschlossen, andere Steigung). [ES]
- arXiv:2508.11626 Marczenko u. a. (2025): Glueballs als geschlossene Strings, nur Hagedorn-Zaehlung (Z. 856).
- arXiv:2604.04803 Shuryak/Zahed (2026): Konstituenten-Paar, "semiclassical analysis further supports Regge behavior"
  (Z. 472).

## 3. Abrufprotokoll (Erwartung mit date-Zeit VOR dem Abruf, danach Ausgang)

### H1: arXiv-PDF 1812.01619 (HISH-Zusammenfassung), ganz, Glueball-Abschnitt und Literaturliste
- Erwartung (geschrieben ab 2026-10-05 05:18:25 CEST, date): Der Glueball-Abschnitt beschreibt Glueballs als
  rotierende gefaltete geschlossene Strings ohne Endmassen, Steigung alpha'/2 mit alpha' aus den Mesonfits
  (~0,9 GeV^-2), Intercept angepasst (an Gitter- oder f0/f2-Kandidaten), dazu eine Vorhersagetabelle und als Methode
  zur Trennung von Mesonen: die halbe Steigung (auch radial). Die Glueball-Arbeit steht in der Literaturliste
  (JHEP 2015, arXiv 1510.x [L?]).
- Abruf: 2026-10-05 05:19:01 CEST, HTTP 200, quellen/H1-1812.01619.{pdf,txt} (pdftotext -layout; Z. = Textzeile).
- Ausgang: **im Kern bestaetigt, drei kleine Verstoesse.**
  - Bestaetigt (je eine Zeile): geschlossene gefaltete Strings, "Folded closed strings describe glueballs [4]" (Z. 84-85);
    Gl. (3.11) J + n - a = (1/2) alpha' M^2, "we do not have the endpoint masses" (Z. 493-498); alpha'_closed =
    alpha'_open/2 und a_closed = 2 a_open (Z. 346-355); nur gerade J + n (Z. 498-499).
  - Intercept: "we fit all the intercepts ... The intercepts however are not free parameters and in principle should be
    calculable" (Z. 98-100); "universal experimental fact that ... intercepts are always negative a < 0" (Z. 300-303).
    Fuer Glueballs setzt der Grundzustand J = n = 0 den Intercept: M^2 = -2a/alpha' (Z. 515-516). Probe [M]: f0(1500),
    alpha'/2 = 0,425 -> a = -0,96 -> J = 2 bei 2,64 GeV; Tab. 8 (Z. 1101-1106) nennt 2640. Stimmt.
  - **Verstoss h1 (klein):** Glueball-Arbeit ist arXiv:1507.01604, JHEP 12 (2015) 011 (Lit. [4], Z. 1468-1469), nicht
    1510.x. Titel "Glueballs as rotating folded closed strings" stimmt.
  - **Verstoss h2 (mittel):** Die Vorhersagen in [161] haengen NICHT an Gitterdaten, sondern an PDG-Kandidaten f0(980),
    f0(1370), f0(1500), f0(1710) als Grundzustand (Z. 143-146, 997-1013; Tab. 5-9). Gitter nur im Satz "The slope of
    glueball trajectories can also be measured on the lattice as we did in [4] or as in [14, 15]" (Z. 139-141);
    [14] = MT hep-ph/0409183, [15] = Athenodorou/Bringoltz/Teper 2011 (geschlossene Flussroehren), Z. 1500-1504.
  - **Verstoss h3 (wichtig fuer das Regime):** In HISH liegt das 0++ AUF der fuehrenden Glueball-Trajektorie: Tab. 6-9
    fuehren J = 0, 2, 4, 6 auf einer Geraden ab dem f0-Grundzustand; "assuming the tensor is an excited partner of the
    scalar ground state" (Z. 1117-1119). Bei MT liegt das 0++ NICHT darauf (Intercept 0,93, Vorlektuere). Das ist der
    Unterscheidungspunkt der zwei Regime. Probe [M] in sqrt(sigma)-Einheiten: 0++ = 3,405 (A&T) auf Steigung
    alpha'/2 gibt M(2++)^2 = 3,405^2 + 8 pi = 36,7 -> 6,06, Gitter 4,894(22). Mit 0++ als Kopf ist der Gitter-Tensor um
    ~24 % zu leicht.
  - Steigungsangaben: J-Ebene 0,40-0,45 GeV^-2, n-Ebene 0,35-0,40 GeV^-2 (Z. 1018-1020); Tensor-Tab. 10: Mesonen 0,85,
    Glueball die Haelfte (Z. 1141-1142); Prioritaet "slope (of around 0.45 GeV^-2)" (Z. 1396).
  - Theorie-Intercept: [36] = 1801.00798 gibt fuer symmetrische Endmassen "always positive", Phaenomenologie braucht
    negativ (Z. 1407-1416; Anhang B Z. 1737-1745: Korrektur "to the result a = 1 of the usual boson string theory").

### H2: arXiv-PDF 1507.01604 (Sonnenschein/Weissman 2015, "Glueballs as rotating folded closed strings")
- Erwartung (geschrieben ab 2026-10-05 05:19:59 CEST, date): [4] passt Gitter-Glueballmassen (MT 2004/05, evtl. Meyers
  Dissertation, Morningstar/Peardon, Chen u. a.) mit linearen Trajektorien geschlossener Strings an, Steigung und
  Intercept beide frei; die Gitter-Steigung kommt dabei ungefaehr bei alpha'/2 heraus, wenn 0++ eingeschlossen wird;
  der Intercept ist negativ; ein offenes adjungiertes Paar mit Gluon-Enden wird hoechstens am Rand erwaehnt.
- Abruf: 2026-10-05 05:20:23 CEST, HTTP 200, quellen/H2-1507.01604.{pdf,txt} (v3, 18 Aug 2015; Z. = Textzeile).
- Ausgang (Text ab 05:22:55 CEST): **G1, G2, G3, G4 im Wortlaut eingetroffen; der Gehalt liegt in vier Verstoessen.**
  - Bestaetigt (je eine Zeile):
    - (a)/(b) gefalteter geschlossener String, alpha'_gb = alpha'_meson/2 ~ 0,45 GeV^-2 (Gl. 1.1, Z. 120-125; Abstract).
    - (c) Fit-Modell Gitter Gl. (3.12): M^2/T = (2 pi/q)(N + a), "q ... the primary fitting parameter (in addition to the
      intercept a)" (Z. 1475-1482); Intercept also frei. Theorie: "the determination of the intercept is still not fully
      understood. Thus the intercept cannot currently serve as a tool for identifying glueballs" (Z. 126-134).
    - (d) keine Endmassen; Figure 1: gefalteter String "would look like an open string with no endpoint masses"
      (Z. 524-528).
    - (e) Gitterdaten: Meyer [35] = hep-lat/0508002 (Dissertation, Z. 1851) als "most extensive study ... Meyer and
      Teper [34, 35]" (Z. 1419-1421); Tab. 8 dazu M&P [64], Chen [65], Bali/UKQCD [66], Gregory [62] (Z. 1427-1440);
      SU(N): Lucini/Teper/Wenger [68] ueber Lucini [67] (Z. 1567-1580).
  - **Verstoss h4 (wichtigster): Die Gitter-Zustaende 2++ und 4++ liegen bei S&W NICHT auf einer gemeinsamen
    String-Trajektorie.** S&W zitieren die MT-Gerade 2++ -> 4++ mit q = 0,28(2) (Gl. 3.13) bzw. mit 6++ q = 0,29(15)
    (Gl. 3.14), schlagen aber vor: 0++ (Grundzustand), 2++* (angeregter Tensor), 4++, 6++ auf EINER Geraden mit
    q = 0,43(3) (Gl. 3.16), chi^2/dof 0,37 gegen 1,24 fuer die MT-Gerade (Z. 1495-1506; Fig. 6 Z. 1525-1531).
    "the lowest 2++ state is then left out". Das PAAR-REGGE-1-Datenpaar (leichtestes 2++, 4++) mischt nach dieser
    Lesart zwei Trajektorien.
  - **Verstoss h5: Das leichteste 2++ ist "zu leicht" fuer jede String-Gerade vom 0++, und S&W sagen das.**
    "the spin-2 state is, in most studies, lower than we would expect it based on the Regge slope assumption"
    (Z. 1453-1455), Fussnote 12: "tensor glueball is close to the scalar seems to have been long known" (APE [63],
    Z. 1468-1469). SU(N) (Gl. 3.18-3.20, Z. 1567-1593): Abstand 0++ -> 2++ entspricht q = 1,16(27) (SU(3)) bzw.
    1,04(13) (N -> unendlich), also der OFFENEN Fundamental-Steigung, nicht 1/2; radial 0++ -> 0++* q = 0,65(11) bzw.
    0,52(5), also geschlossen. "the first 2++ does not seem to lie on the trajectory of the 0++ ground state".
    Das ist der literaturbekannte Kern hinter "2++ liegt schon unter dem masselosen Wert" (PAAR-REGGE-1 Punkt 2).
  - **Verstoss h6: Massen auf den Faltstellen = Finns Paar als Regularisierungsidee, nicht gerechnet.**
    Abschn. 2.2.2 (Z. 455-480): Hellerman/Swanson [23] geben fuer offene Strings a = 1 fuer alle D; fuer den gefalteten
    geschlossenen String in D = 4 ist ihr Ausdruck (Gl. 2.24) singulaer. "One potential way ... might be to add two
    masses at the two endpoints of the folded string. The resulting system looks like two open strings connected at
    their boundaries by these masses ... effective double tension T -> 2T"; Ergebnis dann "probable ... simply double
    that of the open string". Nicht ausgefuehrt (Quantisierung mit Endmassen damals nicht beherrscht); als offene
    Aufgabe im Summary (Z. 1645-1651).
  - **Verstoss h7: Das adjungierte Paar wird ausdruecklich behandelt, aber nur als Steigungsvorhersage.** Abschn. 2.3
    (Z. 600-617): "a model of the glueball as two adjoint charges (or constituent gluons) joined by a flux tube predicts
    the ratio ... 4/9", "For N -> infinity we recover the ratio of 1/2". Kein Fit, keine Endmassen, kein Intercept.
  - Nebenbefunde: Pomeron-Steigung 0,25 GeV^-2 ~ 0,28 alpha'_meson "closer to a quarter ... rather than half ... still
    an open question" (Z. 1666-1673). Holographisch: J = alpha'_closed (E^2 - 2 m0 E) + a mit modellabhaengigem m0
    (Gl. 2.37, Z. 566-571); mit a = alpha' m0^2/2 (Abschn. 3.5.2, "constrained intercept", Z. 1379-1397) "the energy
    rises much too fast with J" fuer die PDG-Kandidaten. Intercepts der PDG-Fits negativ: Glueball -0,38, -0,80, -0,99,
    -1,17 (Z. 953, 1036, 1069, 1103). Intercept-Werte der Gitterfits nennt der Text nicht.
  - Probe [M] (von Hand): q = 0,43 mit 0++ = 3,405 sqrt(sigma) (A&T) gibt a = -(0,43/(2 pi)) x 3,405^2 = -0,79;
    S&W-Lesart hat also einen NEGATIVEN Intercept, MT-Lesart +0,93. Die zwei Lesarten sind zwei Regime (Moderator:
    Zuordnung des leichtesten 2++ und des 4++).
  - Korrektur meiner Erwartung (protokolliert): Ich erwartete "Gitter-Steigung ~alpha'/2, wenn 0++ eingeschlossen".
    Das stimmt nur, wenn das leichteste 2++ HERAUSGENOMMEN wird; mit ihm ist der 0++ -> 2++-Abstand halb so gross wie
    vom geschlossenen String verlangt.

### H3: INSPIRE-API, Zitate von 1507.01604 oder 1812.01619 seit 2024-10-05 (Feldregel 7)
- Erwartung (geschrieben ab 2026-10-05 05:22:55 CEST, date; Text vor dem Abruf): 5 bis 20 zitierende Arbeiten in 24
  Monaten, vorwiegend holographische Glueball-/Regge-Arbeiten und Sonnenschein-Folgearbeiten; hoechstens eine fittet
  Gitter-Glueballs mit Strings, und keine mit Endmassen und festem Intercept.
- Abruf: 2026-10-05 05:23:25 CEST, HTTP 200, quellen/H3-inspire-zitate-24m.json.
- Ausgang: **fehlgeschlagen (Abfragesyntax).** hits.total = 141012, Treffer unverwandt (Quanteninformatik, Magnete).
  Vermutung [L?]: der Operator ">=" im Datumsteil wird nicht verstanden, die Abfrage faellt auf eine breite
  Textsuche zurueck. Zaehlt als Abruf 3 von 10. Datei bleibt als Beleg liegen.

### H4: INSPIRE-API, neuer Versuch: refersto:recid:1707033 or refersto:arxiv:1507.01604, ohne Datumsteil, sortiert
### nach mostrecent; Datumsfilter lokal mit jq
- Erwartung (geschrieben ab 2026-10-05 05:23:49 CEST, date): wie H3. Zusaetzlich: Gesamttreffer 50 bis 150 (beide
  Arbeiten zusammen), davon 5 bis 20 seit 2024-10-05; falls hits.total > 1000, ist die Syntax wieder gescheitert.
- Abruf: 2026-10-05 05:24:00 CEST, HTTP 200, quellen/H4-inspire-zitate.json.
- Ausgang (Text ab 05:24:54 CEST): **teils gescheitert, ein grosser Fund.**
  - hits.total = 47, fruehester Treffer 2018-12-12. Es fehlen alle Zitate von 1507.01604 aus 2015 bis 2018; also hat
    nur refersto:recid:1707033 (HISH) gegriffen, refersto:arxiv:1507.01604 offenbar nicht [ES]. Die Zitate der
    Glueball-Arbeit selbst sind damit NICHT geprueft (offen, siehe H6/H7).
  - 24 Monate (ab 2024-10-05): 10 Treffer. Davon glueball-nah nur Marczenko/McLerran/Redlich 2603.28668 (Hagedorn,
    keine Trajektorienfits) [S Abstract]; sonst Regge-Trajektorien exotischer Hadronen (Chen-Gruppe, 6 Arbeiten),
    Armoni/Weissman 2512.18274 (Pionstreuung), Winney/Szczepaniak 2512.21805 (Review), Dong u. a. 2025 (Flussrohr,
    Charmonium). **Kein Glueball-String-Fit an Gitterdaten.** Erwartung insoweit bestaetigt.
  - **Verstoss h8 (gross, ausserhalb des 24-Monats-Fensters): Sonnenschein/Weissman 2020, arXiv:2006.14634, "On the
    quantization of folded strings in non-critical dimensions"** [S Abstract, H4-JSON]: "We overcome this obstacle by
    putting a massive particle at each folding point which can be used as a regulator ... the intercepts are a = 1 and
    a = 2 for the open and closed string respectively, independent of the target space dimension ... one can expect
    corrections from finite masses associated with either the endpoints of an open string or the folding points on a
    closed string. We compute explicitly the corrections in the presence of these masses."
    - Bedeutung [ES]: Die Idee aus H2 (Massen auf den Faltstellen) ist 2020 ausgefuehrt. Ein gefalteter geschlossener
      String mit Massen an den Faltstellen IST ein rotierendes Paar (zwei Massen, doppelter String, Spannung 2T).
      Die Theorie legt den Intercept FEST: a = 2 (geschlossen), a = 1 (offen), nicht 0 oder 1/12.
    - Damit ist G2 zeitabhaengig: In [161] (2018/19) und [4] (2015) wird der Intercept gefittet; die Theorie der Gruppe
      liefert seit 2020 einen festen Wert, der weit ueber den phaenomenologischen (negativen) Intercepts liegt.
    - PAAR-REGGE-1 hat mit a = 0 und 1/12 die Werte ohne Polchinski-Strominger-Beitrag genommen [ES, L]. Die Werte der
      Literatur fuer rotierende Strings (a = 1 offen, a = 2 geschlossen) sind nicht getestet.

### H5: arXiv-PDF 2006.14634 (Sonnenschein/Weissman 2020)
- Erwartung (geschrieben ab 2026-10-05 05:24:54 CEST, date): Die Arbeit ist rein theoretisch: Intercept a = 2 fuer den
  geschlossenen gefalteten String mit Massenregulator, Korrekturen in m/E (oder m^(3/2)). Sie vergleicht NICHT mit
  Gitter-Glueballs; hoechstens ein Satz, dass a = 2 phaenomenologisch zu gross ist bzw. dass negative Intercepts
  weiter ungeklaert sind.
- Abruf: 2026-10-05 05:25:15 CEST, HTTP 200, quellen/H5-2006.14634.{pdf,txt} (v3, 11 Nov 2020).
- Ausgang (Text ab 05:25:48 CEST): **bestaetigt (rein theoretisch, kein Gittervergleich), mit zwei Zusaetzen.**
  - Bestaetigt (eine Zeile): Gl. (1.4)-(1.7) (Z. 211-233): a_open = (D-2)/24 + (26-D)/24 = 1, a_closed = (D-2)/12 +
    (26-D)/12 = 2 fuer jedes D; "J = (1/2) alpha' M^2 + 2" fuer geschlossene Strings. Kein Gitterfit; Schluss: "It will be
    interesting to see if there is evidence of mass corrections in YM by comparing with results from the lattice"
    (Z. 2783-2786).
  - Zusatz 1 (Verstoss h9, klein, Richtung wichtig): Mit endlichen Faltstellen-Massen SINKT der Intercept in D = 4:
    Gl. (7.9) a = 2 + (3D - 55)/(24 pi) (eps1 + eps2) + ..., "the leading order correction is negative for any D <= 18"
    (Z. 2604-2619). Also: Massen ziehen a von 2 nach unten, in Richtung der phaenomenologischen Werte.
  - Zusatz 2 (Verstoss h10): Die Faltstellen-Masse ist nicht nur Rechentrick. Sever/Zhiboedov [23] (1707.05270) zeigen
    eine universelle Korrektur J = alpha' M^2 + c_m alpha' m^(3/2) M^(1/2) + ... (Gl. 1.2, Z. 160-170); "since the result
    also applies to theories with only closed strings, such as large N YM, it was conjectured that the m^(3/2)
    correction for closed strings can be associated with the folding points" (Z. 170-174). "folding point masses that
    will affect the closed string states, the glueballs" (Z. 2783-2784).
  - [ES] Damit hat Finns Paar eine zweite, geschlossene Lesart: zwei Punktmassen an den Wendepunkten eines doppelt
    gelegten Strings (Spannung 2T, Steigung alpha'/2, Intercept 2 minus Massenkorrektur). PAAR-REGGE-1 ist die offene
    Lesart (Spannung 9/4 T, Steigung 4/9, Intercept fest 0 oder 1/12). Klassisch liegen beide um 11 % auseinander
    (2 gegen 9/4); bei grossem N fallen die Steigungen zusammen (Gl. 2.41 in H2).

### H6: INSPIRE-API, Datensaetze zu arxiv:1507.01604 und arxiv:2006.14634 (recid, Zitatzahl)
- Erwartung (geschrieben ab 2026-10-05 05:26:08 CEST, date): zwei Treffer; Zitatzahl 1507.01604 etwa 40 bis 70,
  2006.14634 etwa 10 bis 25.
- Abruf: 2026-10-05 05:26:17 CEST, HTTP 200, quellen/H6-inspire-recids.json.
- Ausgang: zwei Treffer; recid 1381769 (1507.01604, 24 Zitate), recid 1803333 (2006.14634, 7 Zitate). Zitatzahlen unter
  der Erwartung (kleiner Verstoss h11: die Linie ist wenig rezipiert).

### H7: INSPIRE-API, refersto:recid:1381769 or refersto:recid:1803333, alle, mostrecent
- Erwartung (geschrieben ab 2026-10-05 05:26:21 CEST, date): hoechstens 31 Treffer, davon 0 bis 3 seit 2024-10-05;
  keiner fittet Gitter-Glueballs mit Faltstellen-Massen oder festem Intercept a = 2.
- Abruf: 2026-10-05 05:26:33 CEST, HTTP 200, quellen/H7-inspire-zitate-glueball-falt.json.
- Ausgang (Text ab 05:27:48 CEST): **bestaetigt** (eine Zeile je Punkt):
  - 29 Treffer; seit 2024-10-05 drei: Wiedner 2604.12895 (Glueball-Uebersicht, Abstract ohne Strings), Shukla u. a.
    2411.12536 (Chaos geschlossener Strings, holographisch), Caldararu/Pantev 2504.02023 (unverwandt). Kein Gitterfit.
  - Nebenfund (ausserhalb 24 Monate, dritte Linie): Dubovsky/Hernandez-Chifflet 1611.09796 (2016) "Axionic String
    Ansatz": Glueballs als geschlossene bosonische Strings, Quantenzahlen von ~39 Gitter-Glueballs (3D) "good agreement";
    4D braucht eine massive pseudoskalare Weltflaechenmode [S Abstract]. Dubovsky/Hernandez-Chifflet/Zare 2104.02154
    (2021, zitiert 1507.01604 und 2006.14634): Glueballe als Anregungen um den gefalteten rotierenden Stab, "only
    glueballs of even spin J show up at the leading Regge trajectory" [S Abstract]. Boulanger/Buisseret 1509.09312
    (2015, Mons): geschlossene Strings, 2+1D, skalare Massen bei grossem N [S Abstract].

### Gegensweep-Probe (lokal, ohne Abruf; Text ab 05:27:48 CEST)
- MT 2004 (gluon-paar-l/quellen/F2, Z. 147-157) [S]: fuehrende Trajektorie "passes through the lightest J = 2 and J = 4
  glueballs", 2 pi sigma alpha' = 0,281(22), alpha0 = 0,93(24). S&W Gl. (3.13) q = 0,28(2) ist dieselbe Gerade; ihr
  4++ in Gl. (3.16) ist also dasselbe leichteste 4++. **Geprueft: PAAR-REGGE-1 (B) und S&W benutzen denselben 4++.**
- Vorzeichen-Falle: In H2 Gl. (3.12) steht M^2/T = (2 pi/q)(N + a), also Regge-Intercept alpha0 = -a. In H1 Gl. (3.11)
  steht J + n - a = alpha' M^2/2, also alpha0 = +a. Meine [M]-Werte nenne ich immer als alpha0 (J = s M^2/(2 pi sigma) +
  alpha0).
- A&T 2020 (F3 Tab. 17, Z. 1983-1996) [S]: 0++ 3,405(21); 0++* 5,855(41); 2++ 4,894(22); 2++* 6,788(40); 3++ 7,71(9)*;
  4++ 7,60(12)*. Sekanten [M] (q = 2 pi Delta J / Delta M^2, Einheit Mesonsteigung):
  - 0++ -> 2++: 12,566/12,36 = 1,02 (offen-fundamental; S&W SU(3) 1,16(27)).
  - 0++ -> 0++* (n = 2): 12,566/22,69 = 0,55 (geschlossen; S&W/Meyer 0,50(7)).
  - 0++ -> 4++: 25,13/46,17 = 0,54, alpha0 = -0,54 x 11,59/(2 pi) = -1,00.
  - 0++ -> 2++*: 12,566/34,48 = 0,36; 2++* -> 4++: 12,566/11,68 = 1,08. **Mit dem A&T-4++ bildet die S&W-Kette 0++, 2++*,
    4++ keine Gerade.** Mit dem MT-4++ (8,285) gaebe 0++ -> 4++ 25,13/57,06 = 0,44, passend zu S&W 0,43(3).
  - Bedeutung [ES]: Der Moderator ist wieder das 4++ (MT ~8,3 gegen A&T 7,60*), wie schon in gluon-paar-l Abschn. 7.

### H8: arXiv-API, 24-Monats-Suche (submittedDate 2024-10-05 bis 2026-10-05): abs:glueball AND (abs:Regge OR
### abs:"closed string" OR abs:"folded string" OR abs:"rotating string")
- Erwartung (geschrieben ab 2026-10-05 05:27:48 CEST, date): 15 bis 50 Treffer, ueberwiegend holographisch oder
  Pomeron; 0 bis 2 fitten Gitter-Glueball-Trajektorien mit Strings; keiner mit Faltstellen-/Endmassen und festem
  Intercept 1 oder 2.
- Abruf: 2026-10-05 05:28:12 CEST, **HTTP 429 "Rate exceeded."** (14 Byte, quellen/H8-arxiv-api-24m.xml). Zaehlt als
  Abruf 8 von 10. Vermutlich teilen sich mehrere laufende Karten die arXiv-API [L?].

### H9: dieselbe arXiv-Abfrage, zweiter Versuch nach >= 60 s Pause (Text ab 05:29:04 CEST)
- Erwartung: wie H8. Scheitert auch H9, bleibt die 24-Monats-Suche auf INSPIRE-Zitate (H4, H7) und die lokale
  Titelsuche (gluon-paar-l F5) beschraenkt; das steht dann so im Dossier.
- Abruf: 2026-10-05 05:30:07 CEST (Hintergrundbefehl mit 40 s Pause), **wieder HTTP 429 "Rate exceeded."**
  (quellen/H9-arxiv-api-24m.xml, 14 Byte). Abruf 9 von 10.

### Zwischenbefund lokal (ohne Abruf, Text ab 05:31:11 CEST)
- HISH-Randbedingung H1 Gl. (3.4) (Z. 405-406): T l_i/m_i = beta_i^2/(1 - beta_i^2). Das ist dieselbe Gleichung wie die
  [P]-Form von PAAR-REGGE-1 (sigma_A sqrt(1 - v^2) = gamma m v omega mit omega = v/R; umgeformt sigma_A R/m =
  v^2/(1 - v^2)) [M]. **PAAR-REGGE-1 Selbstanzeige 6 ("S&W-Randbedingung [L]") ist damit an der Quelle bestaetigt.**

### H10 (letzter Abruf): INSPIRE-API, Abstract-Suche glueball AND (regge OR "closed string" OR "folded string"),
### sortiert mostrecent, Datum lokal filtern
- Erwartung (geschrieben ab 2026-10-05 05:31:11 CEST, date): Wenn die Feldsuche "abstracts.value:" greift: 100 bis 600
  Treffer gesamt, davon 10 bis 40 seit 2024-10-05, ueberwiegend holographisch/Pomeron; kein Gitterfit mit Faltstellen-
  oder Endmassen und festem Intercept 1 oder 2. Greift sie nicht (hits.total > 5000): gescheitert, dann bleibt es bei
  H4/H7/F5.
- Abruf: 2026-10-05 05:31:25 CEST, HTTP 200, quellen/H10-inspire-abstract-suche.json (100 neueste von 119).
- Ausgang (Text ab 05:32:21 CEST): **Feldsuche greift; 24 Monate bestaetigt, aelterer Bestand mit grossem Verstoss.**
  - 24 Monate: 12 Treffer. Glueball-Trajektorien nur bei Migdal 2605.02373 (geschlossener String, "parameter-free",
    "exact Luescher intercept alpha(0) = 1/12", "matching ... large-N_c lattice QCD extrapolations") und
    Shuryak/Zahed 2604.04803 (Konstituenten, "semiclassical ... Regge behavior") [S Abstract]. Sonst Holographie,
    Streuung, Mesonen (Afonin 2607.21035, 2504.13698). Kein Gitterfit mit Faltstellen-/Endmassen und festem a = 1 oder 2.
  - **Verstoss h12 (gross, vor dem 24-Monats-Fenster): Finns Paar mit doppeltem String ist ein veroeffentlichtes
    Glueball-Modell.** Sharov, hep-ph/0612373 (2006): "The closed relativistic string carrying two point-like masses is
    considered as the model of a glueball with two constituent gluons. Here the gluon-gluon interaction is simulated by
    a pair of strings ... exact solutions ... rotational states ... quasilinear Regge trajectories"; Sharov 0712.4052
    (2007): n = 2 oder 3 Massen, Stabilitaet; Sharov 2008 (ohne arXiv-Nummer im Datensatz): "Regge trajectories
    characterized by a specific set of slopes are used to describe glueball states" [S Abstract]. Ob und gegen welche
    Gitterdaten Sharov fittet, ist NICHT gelesen (Budget erschoepft). Das betrifft gluon-paar-l O1 direkt.
  - Weitere aeltere Treffer (nur Titel/Abstract): Brisudova/Burakovsky/Goldman/Szczepaniak nucl-th/0303012 (2003):
    nichtlineare Trajektorien, Intercept und Schwelle aus Pomeron-Daten, "applied to available quenched lattice data ...
    discrepancy between the lattice based thresholds and the pomeron threshold" [S Abstract]; Meyer hep-ph/0510038
    (2005): dieselbe Trajektorie 0,93(24) + 0,28(2) alpha'_R t, "interpret ... in terms of open and closed string models"
    [S Abstract]; Dymarsky/Melnikov 2206.14826 (2022): grosses N, Holographie gegen Gitter, 2++/1-- "consistent with ...
    pomeron and odderon Regge trajectories" [S Abstract].
  - [M] (nach dem Abruf, nicht gegengelesen): geschlossene Steigung 1/2 mit festem alpha0 = 1/12 und masselos gibt
    M(2++)^2 = 4 pi (2 - 1/12) = 24,09 -> 4,908 sqrt(sigma); A&T 4,894(22), Abstand 0,6 sigma. M(4++) = sqrt(4 pi x
    3,9167) = 7,016; A&T 7,60(12)* (4,9 sigma darunter), MT 8,29. Also trifft "geschlossen + 1/12" den Tensor, nicht das
    4++. Look-elsewhere: fuenf Intercepts (0, 1/12, 1/6, 1, 2) mal zwei Steigungen (4/9, 1/2) = zehn Kandidaten.
- Projekt-grep (05:32, Pflicht-Ausschluesse, ohne *.json/*.jsonl und ohne diese Karte): "0712.4052",
  "hep-ph/0612373", "folding point", "Faltstelle", "Axionic String": 0. "Sharov": nur fremde Literaturlisten in
  literatur-20260926/glied10-r-lesart-quellen (Kontext nicht geprueft [L?]). "2006.14634": nur Zufallsziffern in einer
  CSV (boufourou-dr4-l). "Hellerman": nur Carroll/Hellerman/Trodden (Domaenenwaende, RUNDE-10). "Dubovsky": nur
  RUNDE-13/RUNDE-23-Quellen (andere Themen, nicht geprueft). "2605.02373", "Brisudova": nur RUNDE-37 (gluon-paar-l,
  regge-hadron-ref-l).

## 4. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
1. Dass S&W denselben 4++ meinen wie MT und PAAR-REGGE-1 (B). **Geprueft** (MT F2 Z. 147-157; S&W Gl. 3.13): ja.
2. Dass "Steigung" und "Intercept" in allen Quellen gleich definiert sind. **Geprueft**: q (S&W) = 2 pi sigma alpha'
   (MT, PAAR-REGGE-1); Intercept-Vorzeichen in S&W Gl. (3.12) umgekehrt (alpha0 = -a), in HISH Gl. (3.11) gleich.
3. Dass die PAAR-REGGE-1-Randbedingung die von S&W ist. **Geprueft**: H1 Gl. (3.4), gleich [M].
4. Dass 1/12 = (D - 2)/24 der "natuerliche" Intercept eines rotierenden Strings ist. **Geprueft (H5)**: Mit
   Polchinski-Strominger-Term gilt a = 1 (offen) und a = 2 (geschlossen), fuer jedes D. 1/12 ist nur der Casimir-Teil.
5. Dass Glueball-Trajektorien Literatur zu "Strings ohne Massen" sind. **Widerlegt durch H10**: Sharov 2006-2008
   (geschlossener String mit zwei Punktmassen), S&W 2020 (Faltstellen-Massen).
6. Dass Meyer [35] (Dissertation) dieselben Zahlen wie MT 2004 hat. Nicht geprueft (kein Abruf mehr); Meyer 2005
   (hep-ph/0510038) nennt dieselbe Gerade [S Abstract].
7. Dass die Spinzuordnung des 4++ belastbar ist. Nicht geprueft; die A&T-Zahl bricht die S&W-Kette [M].

## 5. Gestrichenes / Berichtigungen
- ~~Glueball-Arbeit vermutlich arXiv 1510.x~~ -> 1507.01604 (H1, Lit. [4]).
- ~~"HISH-Intercept ist theoretisch unbestimmt" als Endstand~~ -> gilt fuer 2015/2019; seit 2020 a = 2 (H5).
- ~~"Endmassen-Glueball-Modelle nicht in der Literatur" (gluon-paar-l O1, meine Grundannahme)~~ -> Sharov 2006-2008
  (Abstract), S&W 2020 (Regulator).
- Berichtigung Zeilenangaben (Rueckwaertspruefung 05:36 CEST per grep -n): H1 Steigungen 0,40-0,45 und 0,35-0,40
  stehen in ~~Z. 1018-1020~~ Z. 1025-1026; H5 Gl. (1.2) und die Vermutung stehen in ~~Z. 160-170/160-174~~
  Z. 155-170; H2 Gl. (3.13)-(3.16) in Z. 1486-1506; H1 Tab. 6-9 in Z. 1050-1106. Im DOSSIER berichtigt.

## 6. Offene Rueckfragen (wandern mit)
- R1: Fittet Sharov (2006-2008) Gitter-Glueballs, und mit welchem Intercept? (Volltext nicht gelesen.)
- R2: Welche Steigung, welche Zustaende und welche Gitterdaten nutzt Migdal 2605.02373 fuer "alpha(0) = 1/12"?
- R3: Haengt die fuehrende Gitter-Steigung (2++ -> 4++) von N ab? Offenes adjungiertes Paar: 3/8 (SU(2)), 4/9 (SU(3)),
  -> 1/2; geschlossen: 1/2 fuer alle N [M]. Das ist der sauberste Unterscheidungspunkt der zwei Regime.
- R4: Gilt die S&W-Lesart (0++, 2++*, 4++) mit dem A&T-4++? [M] sagt nein; Zuordnung des 4++ entscheidet.
