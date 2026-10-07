Urteil: TRAEGT MIT EINSCHRAENKUNG (Vorzeichen, Groessenordnung und Umschlag gegenueber +0,159 tragen; 0,92 P ist eine Fenster-Steigung bei abs(k) etwa 0,3 und Gitterabstand 1 mit unbezifferter k^4-Systematik von etwa +-25 % P, der 30-%-Treffer von ID1 ist daher nicht abgesichert)

# Gegenlesen INDUZIERT-DICHTE-2D

- Pruefer: frischer Gegenleser (Claude, Unteragent der Leitung claude-primary), nicht Autor, nicht Rechner
- Beginn: 2026-10-04 08:37:37 CEST (gemessen mit date)
- Ende: 2026-10-04 08:58:18 CEST (gemessen mit date; Text danach nur noch berichtigt), Dauer 21 min von 60 min
  Zeitbox
- Gelesen: KARTE.md, PLAN.md Abschnitte 1 bis 6, ERGEBNIS.md ganz, code/dichte2d.py Zeilen 1 bis 355,
  code/zufall2d.py Zeilen 41 bis 140, code/dichte_auswertung.py Zeilen 105 bis 179, lauf-69/auswertung.json (per jq),
  lauf-69/fest-N64000-s0.json und .log (Ausschnitt), induziert-zufall-2d/lauf-69/zufall-N64000-s0.json (Saat 0, per
  jq), induziert-1/ERGEBNIS.md Zeilen 34 bis 53. Nicht geoeffnet: Bilder, rauch-69/, kette-*.log.
- Gerechnet: nichts auf dem Rechner. Alle Zahlen sind Kopfrechnung mit gezeigtem Weg; jq nur zum Auslesen.
- Gegenstand: coordination/runden-v3/RUNDE-37/induziert-dichte-2d/ (KARTE.md, PLAN.md, ERGEBNIS.md, code/, lauf-69/auswertung.json)

## 1. Messgroesse und Auswertung

Alle Zahlen unten habe ich im Kopf aus ERGEBNIS.md und lauf-69/auswertung.json gerechnet (Werte dort per jq nur
ausgelesen). Bezeichnungen: x = k^2, y = Gamma''/A je k, P = -1/(24 pi) = -0,013263.

**1a. Was die Fenster-Steigung misst.**
- Die vier x-Werte sind 0,002467 / 0,009870 / 0,039478 / 0,088826; Mittel 0,03516, Sxx = 0,004607.
- Die OLS-Steigung ist eine feste Linearkombination c = Summe w_j y_j mit
  w = (x - Mittel)/Sxx = (-7,10; -5,49; +0,94; +11,65).
  Gegenrechnung mit den Saatmitteln aus Tabelle 3.2: c = -0,01226 und a = +0,00028, wie berichtet.
- Damit ist c praktisch eine Zwei-Punkt-Steigung zwischen abs(k) = 0,3 und dem Mittel der beiden kleinsten k.
  Ein k^4-Glied y = a + c k^2 + d k^4 geht mit dem Hebel Summe w_j x_j^2 = 0,0928 ein: c_Fit = c(0) + 0,0928 d.
  Gemessen ist also die Steifigkeit bei abs(k) etwa 0,30, nicht der Grenzwert k -> 0.
- Probe am festen Netz: Dort ist d etwa (0,15598 - 0,15899)/(0,0888 - 0,0025) = -0,035. Das gibt
  c_Fit = 0,1591 - 0,0032 = 0,1558, wie in ERGEBNIS Abschnitt 4 von Hand gerechnet.
- **Wichtig: L = sqrt(N)** (PLAN Abschnitt 1, code/dichte2d.py Zeile 52). Die Dichte ist also bei beiden N gleich 1,
  und k mal Gitterabstand laeuft in beiden Laeufen von 0,05 bis 0,3.
  - Der Vergleich N = 16 000 gegen 64 000 prueft die Torusgroesse, nicht den Gitterabstand.
  - Ueber das k^4-Glied, ein Gitterartefakt der Ordnung (k eps)^2, sagt er nichts.
- Der Dreiparameter-Fit kann d nicht bestimmen: d = -0,055 +- 0,062 (auswertung.json). Er vertraegt d = 0 ebenso wie
  den Wert des festen Netzes.
- Ein d von der Groesse des festen Netzes mit **beiden** Vorzeichen verschiebt c(0) um +-0,0033. Das sind etwa 0,68 P
  bis 1,17 P.
  - ERGEBNIS nennt nur die eine Richtung ("bis zu +0,003, auf etwa 0,7 P").
  - Diese Systematik (etwa +-25 % P) ist doppelt bis dreifach so gross wie der statistische Fehler (+-9 % P) und
    steht nicht im Fehlerbalken.
- **Urteil 1a:** Als Schaetzer des k^2-Koeffizienten im Fenster ist die Steigung mit freiem a sinnvoll.
  - Sie ist die Lesart der Karte ("nach Abzug des Flaechenglieds") und vor dem Einfrieren festgelegt.
  - Sie ist aber die Steifigkeit bei k eps etwa 0,3 und nicht der Kontinuumswert. Der Abstand zu diesem ist nicht
    beschraenkt.

**1b. Warum die Lesarten abweichen (Rauschstruktur).**
- Je Saat streut y bei jedem k um etwa 0,0014 (y_std_je_n: 0,00138 / 0,00149 / 0,00145 / 0,00126).
  - Waere dieses Rauschen ueber k unabhaengig, haette c je Saat die Streuung 0,0014/sqrt(0,004607) = 0,021.
  - Gemessen sind 0,0094.
- Das Rauschen ist also ueberwiegend ein gemeinsamer Versatz je Saat, gleich fuer alle k. Zerlegung aus den Streuungen
  von c und a je Saat (Modell: Versatz + unabhaengiger Rest):
  - Rest je k: sigma^2 = 0,0094^2 x 0,004607 = 4,05e-7, also sigma = 0,00064.
  - Versatz: tau^2 = Var(a) - sigma^2 x Summe x^2/(4 Sxx) = 1,93e-6 - 0,21e-6 = 1,72e-6, also tau = 0,0013.
  - Zusammen 0,00146 je k, gemessen etwa 0,0014: Das Modell passt. Rund 80 % der Varianz sind Versatz.
  - Die Quelle ist plausibel Gamma(0), das fuer alle k einer Saat dasselbe ist. Das bestaetigt auch das
    Verhaeltnis 3,6 der a-Werte bei S = 0,25 und 0,5 (erwartet 4).
- **Freies a** entfernt den Versatz exakt, denn Summe w_j = 0. Daher SE 0,0012.
- **a = 0 erzwungen (OLS):** c0 = Summe x y/Summe x^2 = c + 14,72 a exakt (Normalgleichungen).
  - Der Versatz geht mit Hebel 14,7 in c ein. Daher SE 0,0023 statt 0,0012.
  - Die Abweichung 0,61 P gegen 0,92 P ist genau 14,72 x 0,000279 = 0,0041, also 1,6 SE von a. Das ist eine
    Schwankung, keine Verzerrung des Hauptwerts.
- **a = 0 ist theoretisch begruendet** (Abschnitt 2). Das Vorwissen nutzt man richtig ueber die Kovarianz:
  - c~ = c - [Cov(c,a)/Var(a)] a mit Cov(c,a) = -Mittel(x) sigma^2/Sxx = -3,09e-6 und Var(a) = 1,93e-6 je Saat.
  - Ergebnis: c~ = -0,01226 + 1,60 x 0,000279 = **-0,0118 +- 0,0011 (0,89 P)**. Das ist meine Kopfrechnung unter dem
    Versatz-Modell, nicht vom Code.
  - Die naive a = 0-Lesart (0,61 P) ist also nicht "richtiger", sondern ineffizient.
- **Mit k^4-Glied** (0,54 P +- 0,45 P): ein Parameter mehr bei vier Punkten, SE 5-fach. Das ist nicht informativ und
  weder Beleg noch Gegenbeleg.
- **Begruendete Lesart:** die Hauptlesart, gleichwertig mit c~. Der verbleibende echte Vorbehalt ist nicht die Lesart,
  sondern das k^4-Glied aus 1a.

**1c. Staerke der Aussage.**
- **Negativ:** Im Fenster ist das sicher.
  - y(abs(k) = 0,3) allein, ohne jeden Fit, ist -0,000841 +- 0,000156, also 5,4 SE unter 0.
  - a = 0-Lesart: 3,6 SE unter 0. Hauptlesart: 10,6 SE.
  - Fuer k -> 0 kippte das Vorzeichen erst bei d < -0,01226/0,0928 = -0,13. Das waere fast viermal das feste Netz
    und liegt 1,2 SE vom gefitteten d. Es ist unwahrscheinlich, aber durch die Daten nicht ausgeschlossen.
- **"Polyakov-gross":** Das ist richtig, wenn es "gleiche Groessenordnung" heisst: 0,6 P bis 1,2 P je nach Lesart und
  k^4-Annahme.
  - "Trifft Polyakov auf 8 %" oder "innerhalb 30 %" ist nicht abgesichert.
  - ID1 ist nach der eingefrorenen Regel formal eingetroffen. Das haelt aber nur ohne k^4-Systematik und ist nach
    Kartenwortlaut nicht auswertbar.
- **Robust und der eigentliche Befund:** gleiche Grundpunkte, festes Netz +0,159; nach Flaeche gestreut ein negativer
  Wert der Groesse Polyakovs. Der Abstand ist 148 SE und haelt jede Lesart und jede plausible k^4-Annahme aus.

## 2. Grosse Verformung S = 0,5

**2a. Erwartungstreue trotz 19 % Kippen: begruendet.**
- psi_S bildet die Phase per exakter Umkehr der Verteilungsfunktion ab, die Querkoordinate bleibt (Pruefung in
  Abschnitt 3). Die Jacobi-Determinante ist dphi/dphi'.
  - Die Bildpunkte sind deshalb fuer jedes S exakt unabhaengig mit Koordinatendichte e^(2 sigma)/I0(2S) verteilt.
  - Jedes Gamma(+-S) ist damit, fuer sich genommen, eine Stichprobe aus dem richtigen Ensemble.
- Der Erwartungswert ist linear. Darum ist E[y] die Ensemble-Differenz, gleich wie stark Gamma(S) und Gamma(0) je Saat
  korreliert sind.
- Das Kippen kostet nur Varianz. Je Saat streut c um 0,0094, mehr als P selbst.
  - Polyakov steckt also im gequenchten Mittel, nicht im einzelnen Netz. ERGEBNIS Abschnitt 7 sagt das richtig.
- Zusatz: Fuer Achsen-k ist sigma -> -sigma eine Verschiebung um eine halbe Periode. Gamma(S) und Gamma(-S) haben also
  dieselbe Verteilung, und ungerade Ordnungen in S fallen von selbst weg.
- Erwartungstreu ist der Schaetzer fuer die Differenz bei endlichem S. Ob diese gleich der zweiten Ableitung ist,
  entscheidet 2b.

**2b. Hoehere Ordnungen in sigma [M].**
- **Polyakov ist exakt quadratisch:** richtig.
  - Auf dem flachen Torus gilt die Formel von Osgood, Phillips und Sarnak fuer endliches sigma exakt:
    log det' Delta_g - log A_g = const - (1/(12 pi)) Integral (grad sigma)^2 [L].
  - In der K-Konvention mit festem N faellt log A_g ganz heraus, weil die Kotangens-Gewichte skaleninvariant sind.
- **Kosmologisches Glied k-unabhaengig:** richtig.
  - Integral e^(2 sigma) = A I0(2S) fuer jeden Gittervektor k ungleich 0, denn die Phase k.x ist auf dem Torus
    gleichverteilt. Es geht also nur in a.
  - Hier fehlt es sogar ganz: Bei festem N ist rho A_g = N fest.
- **Andere k-abhaengige Glieder hoeherer Ordnung gibt es, aber erst ab k^4:**
  - **(i) Kovariante Gegenterme mit vier Ableitungen.** Der erste ist b (1/rho) Integral sqrt(g) R^2
    = b (A I0(2S)/N) Integral 4 e^(-2 sigma) (Laplace sigma)^2.
    - Das ist reines k^4. In der zweiten Differenz traegt es aber den Faktor 1 + (5/2) S^2 + ..., bei S = 0,5 etwa
      1,6.
    - Rechnung: Mittel von cos^2 mal e^(-2S cos) = 1/2 + (3/4) S^2, dazu I0(2S) = 1 + S^2.
    - Grosses S verstaerkt also das k^4-Glied, und dieses geht mit Hebel 0,093 in c_Fit (Befund 1a).
  - **(ii) Nicht kovariante Reste.**
    - Delaunay in Koordinaten: Der Inkreistest ist moebiusinvariant. Die lokale Abbildung auf flache Koordinaten
      weicht von Moebius erst in zweiter Ordnung ab (Schwarzsche Ableitung, also zweite Ableitungen und
      (grad sigma)^2 mal l^2). Zahl und Gewicht falscher Vierecke sind je O(s (k l)^2). Der Beitrag zu y ist
      ~ k^4 l^2.
    - Laengenformel: Fehler vierter Ordnung (K3: 2,4e-4 bei s k l = 0,51; typische Kanten im Lauf haben s k l etwa
      0,15). Auch das ist k^4 oder hoeher.
  - **(iii) Kein k^2 S^4.** Ein kovariantes lokales Glied mit zwei Ableitungen ausser Integral sqrt(g) R (= 0 auf dem
    Torus) gibt es nicht.
    - Die globale Kopplung ueber rho = N/A_g multipliziert nur Integral sqrt(g) R oder k^4-Glieder.
    - c(k -> 0) wird durch endliches S also nicht verzerrt. Das ist ein Argument aus der Kovarianz des Ensembles, kein
      Messbefund.
- **Empirisch ist die S-Probe schwach.**
  - N = 16 000: S = 0,25 gibt -0,0168 +- 0,0047, S = 0,5 gibt -0,0131 +- 0,0022 (gleiche Saaten).
  - Die Differenz ist 0,0037 bei 0,7 SE (ERGEBNIS A5), ihr SE also etwa 0,0053.
  - Ein Ansatz c(S) = c + e S^2 gibt e = 0,0037/0,1875 = 0,02 +- 0,03. Bei S = 0,5 ist das eine Verschiebung von
    0,005 +- 0,007; die Daten schliessen also bis etwa 50 % P nicht aus.
  - Auf dem festen Netz faellt S = 0,5 gegen Richardson genau wie k^2 in c ab (+0,00001 / 0,00003 / 0,00012 / 0,00027,
    jeweils etwa 0,003 k^2). Das passt zu "S wirkt auf k^4, nicht auf k^2".
- **Kleinigkeit:** PLAN Abschnitt 3 sagt, das Rauschen falle wie S^(-1/2). Die eigenen Zahlen zeigen Faktor 2 zwischen
  S = 0,25 und 0,5 (y-Streuung je k 0,0056 bis 0,0058 gegen 0,0028 bis 0,0030), also eher S^(-1). Fuers Urteil ist das
  ohne Folgen.
- **Urteil 2:** S = 0,5 verzerrt den k^2-Koeffizienten nicht, nach einem Kovarianzargument mit schwacher empirischer
  Stuetze. Es verstaerkt aber das k^4-Glied, das die Fenster-Steigung ohnehin mitnimmt (Befund 1a).

## 3. Code und Konvention

Stichprobe am eingefrorenen Code. sha256 von dichte2d.py, dichte_auswertung.py, zufall2d.py und PLAN.md stimmen mit
EINGEFROREN-SHA256.txt und den *.eingefroren-Kopien ueberein (lokal gemessen).

- **Abbildung psi** (dichte2d.py Zeilen 63 bis 92): richtig.
  - Phi_s(t) = t + Summe 2 I_m(2s)/(m I0(2s)) sin(m t) folgt aus e^(2s cos u) = I0 + 2 Summe I_m cos(m u). Es gilt
    Phi_s(2 pi) = 2 pi, und dF = e^(2s cos t)/I0 stimmt.
  - Newton bis 1e-14 mit Startwert erster Ordnung. 30 Glieder genuegen bei 2s <= 1 bei weitem.
  - Bildpunkt y = z + khat (phi' - phi)/abs(k). Damit ist k.y = phi' (mod 2 pi), und die Querkoordinate bleibt.
  - Die Bildphase hat die Dichte Phi_s'(phi')/(2 pi), proportional zu e^(2 sigma). Die Verteilungsfunktion ist exakt
    umgekehrt.
- **Kantenlaengen geo** (Zeilen 142 bis 151): Die Formel habe ich selbst hergeleitet.
  - Das gerade Linienintegral von e^sigma um den Mittelpunkt gibt (b + a^2)/24.
  - Die optimale Querbiegung h(u) = (g l^2/2)(u^2 - 1/4) verkuerzt den Weg um (d x grad sigma)^2/24.
  - Mit grad sigma = -s sin(k.m) k folgt genau korr = (-s (k.d)^2 cos + s^2 sin^2 ((k.d)^2 - (d x k)^2))/24.
- **Kotangens-Gewichte und log det'** (zufall2d.py Zeilen 92 bis 135): richtig.
  - w = Summe (b^2 + c^2 - a^2)/(8 A_Dreieck) ist die halbe Kotangens-Summe; Flaeche per Kahan-Heron.
  - Gamma = 1/2 (Summe log U_ii + log N) bei Erdung des Knotens 0. Nach dem Matrix-Baum-Satz ist det K_(0) = det' K/N
    fuer jeden geerdeten Knoten; die Wahl des Knotens ist also gleichgueltig.
  - Das Tor verlangt U_ii > 0 und perm_r = perm_c.
- **Gamma(0) und Gamma(+-S) auf demselben Codeweg** (periodisches_netz, Netz.gamma; bei s = 0 sind die geo-Laengen
  gleich l0).
  - Ein Codeweg-Versatz, der ein Flaechenglied a vortaeuschen koennte, ist ausgeschlossen. "art" ist nur ein Etikett.
- **Fit-Code** (dichte_auswertung.py Zeilen 105 bis 166): wie beschrieben.
  - Je Saat erst Mittel ueber 0 und 90 Grad, dann OLS mit Achsenabschnitt.
  - c0 = Summe y x/Summe x^2; dazu der k^4-Fit und die Werte je k.
  - Die Tabellenwerte habe ich in Abschnitt 1a von Hand nachgerechnet.
- **Konvention gegen INDUZIERT-ZUFALL-2D:** stichprobenartig bitgleich.
  - zufall2d.py hat dort und hier denselben sha256 (37a0fe8f...).
  - Saat 0, N = 64 000, n = 2: gamma0 = 45129,853485896616 in beiden Dateien.
  - Eckenregel 0 Grad: c = 0,1588500866696066 (hier fest-N64000-s0.json, dort zufall-N64000-s0.json c_P).
  - Eckenregel 90 Grad: c = 0,15862422590911307 in beiden.
- **Vorzeichen und Normierung bis -1/(24 pi):** schluessig.
  - Mit sigma = s cos(k.x) ist Integral (grad sigma)^2 = s^2 k^2 A/2. Also ist
    Gamma(s) - Gamma(0) = -(1/(24 pi)) s^2 k^2 A/2 und (Gamma(S) + Gamma(-S) - 2 Gamma(0))/S^2 = -k^2 A/(24 pi).
  - Daraus folgen y = -k^2/(24 pi) und c = -0,013263.
  - Vorzeichen: Bei fester Flaeche maximiert die flache Metrik det' (Osgood, Phillips, Sarnak [L]), also ist c < 0.
  - Dieselbe Kette hat INDUZIERT-1 Teil A numerisch geeicht: nicht-analytischer Anteil lambda = 0,9962.
- **Tor:** laut auswertung.json bestanden. Urteile ID0 bis ID3 "eingetroffen", wie berichtet.
- **intr gegen koord** (16 Saaten): -0,01885 gegen -0,01845.
  - Die Richtung passt zur Erwartung: Ein nicht-Delaunay-Viereck macht K steifer (Rippa), koord ist also eher nach
    oben verschoben.
  - intr beseitigt aber nur 0 bis 17 % der negativen Gewichte und beschraenkt den Rest daher nicht. Der Rest ist nach
    2b(ii) ein k^4-Effekt.
- **Urteil 3:** In der Stichprobe kein Code- oder Konventionsfehler. Die Kette bis -1/(24 pi) stimmt.

## 4. Gegenprobe

- **Nicht gerechnet.**
  - Meine festen Prueferregeln verbieten ssh und jede Rechnung auf dem Rechner. Sie gelten, sofern der Auftrag nichts
    Strengeres sagt; das optionale Angebot im Auftrag lockert sie nicht.
  - Ich habe deshalb nichts auf der .69 gestartet und im Ordner gegenlesen/ nur diese Datei angelegt.
- **Inhaltlich waere die angebotene Probe auch wenig ergiebig.**
  - S = 0,25 bei N = 16 000 liegt schon vor: 64 Saaten, -0,0168 +- 0,0047.
  - Sie prueft nicht den Hauptvorbehalt, das k^4-Glied beim Gitterabstand 1.
- **Empfehlung an die Leitung (nicht gerechnet): Gitterabstand variieren, k fest.**
  - Das y-Rauschen je Saat geht wie sqrt(N)/A: 0,0029 bei N = 16 000 und 0,0014 bei N = 64 000, mit A = N.
  - **Groeber, billig:** N = 16 000 auf L = sqrt(64 000), also Abstand 2, mit denselben vier k.
    - Ein Gitterglied d (k eps)^2 waechst dann um den Faktor 4, der Kontinuumswert bleibt.
    - Das y-Rauschen ist etwa halb so gross wie im Hauptlauf. 66 Saaten geben dann SE(c) etwa 0,0006, und d waere auf
      etwa +-0,005 bestimmt; der Wert des festen Netzes ist 0,035.
    - Vorsicht: Bei abs(k) = 0,3 ist k eps = 0,6, dort kann k^6 mitspielen.
  - **Feiner, sauberer, teuer:** N = 64 000 auf L = sqrt(16 000), also Abstand 1/2. Das Rauschen ist viermal so gross
    wie im Hauptlauf, man braeuchte also etwa sechzehnmal so viele Saaten fuer dieselbe SE.
  - L = sqrt(N) ist im Code fest verdrahtet (grundpunkte, Zeile 52; modus_dichte). Beide Proben brauchen also eine
    Kopie unter neuem Namen und eine eigene Vorab-Datei.
- **Alternative:** mehr Saaten bei abs(k) = 0,1 bis 0,2 (ERGEBNIS 7(b)); der Aufwand waechst wie 1/k^4.

## Befunde (nummeriert, Fundstelle, Schwere)

1. **Fenster-Steigung ist die Steifigkeit bei abs(k) etwa 0,3, die k^4-Systematik fehlt im Fehler.**
   - Fundstelle: ERGEBNIS Abschnitt 1 Punkt 1 ("c = -0,0123 +- 0,0012 ... Verhaeltnis 0,92"), Punkt 3, Abschnitt 7
     "Genauigkeit".
   - Gewichte -7,1 / -5,5 / +0,9 / +11,6; Hebel auf d gleich 0,093. Der Fit laesst d offen (-0,055 +- 0,062).
   - Bei d von der Groesse des festen Netzes (+-0,035) liegt c(0) bei 0,68 P bis 1,17 P. ERGEBNIS nennt nur die
     untere Seite.
   - Schwere: **mittel**. Das aendert die erlaubte Genauigkeitsaussage, nicht Vorzeichen oder Kontrast.
2. **"Zwei N" ist kein Kontinuumstest.**
   - Fundstelle: ERGEBNIS Abschnitt 1 Punkt 1 ("Gegenproben: N = 16 000 ..."), Abschnitt 4 L2; PLAN Abschnitt 1
     (L = sqrt(N)).
   - Beide Laeufe haben die Dichte 1 und dieselben k eps. Geprueft ist die Torusgroesse, nicht der Gitterabstand.
   - Schwere: **mittel**. Ohne Hinweis liest man das leicht als Konvergenzbeleg.
3. **ID1 "eingetroffen" und der ausgeloeste Zweig haengen an Planlesart und Fenster.**
   - Fundstelle: ERGEBNIS Abschnitt 1 Punkt 4, Tabelle Abschnitt 2, Abschnitt 7 erster Punkt.
   - Formal ist das nach der eingefrorenen Regel korrekt, und die Lesart ist offengelegt ([K3]).
   - Mit Befund 1 reicht der Bereich fuer c(0) bis 0,68 P, also an den Rand des Bandes [0,7 P; 1,3 P] und knapp
     darunter. Die a = 0-Lesart (0,61 P) zaehlt dafuer nicht (Befund 4). Der Satz "stellt die geometrische Antwort
     her" ist daher staerker als belegt.
   - Belegt sind ID2, ID3 (im Fenster) und der Kontrast zu +0,159.
   - Schwere: **mittel**.
4. **Die Lesarten-Abweichung ist erklaerbar und spricht nicht gegen den Hauptwert.**
   - Fundstelle: ERGEBNIS Abschnitt 1 Punkt 3, Abschnitt 7.
   - Etwa 80 % des Rauschens sind ein gemeinsamer Versatz je Saat, vermutlich aus Gamma(0).
   - a = 0 erzwungen laedt ihn mit Hebel 14,7 auf c; die 0,61 P sind die 1,6-SE-Schwankung von a mal 14,7.
   - Das a = 0-Vorwissen, richtig ueber die Kovarianz genutzt, ergibt -0,0118 +- 0,0011 (0,89 P; Kopfrechnung unter
     Versatz-Modell).
   - ERGEBNIS sollte das so erklaeren statt "andere Lesarten liegen weiter weg".
   - Schwere: **gering** (Klarstellung; staerkt das Ergebnis).
5. **Endliches S verzerrt c(0) nicht, verstaerkt aber k^4.**
   - Fundstelle: PLAN Abschnitt 3 "[M, H]"; ERGEBNIS [K1].
   - Das Kovarianzargument traegt: Polyakov ist exakt quadratisch, das kosmologische Glied ist k-unabhaengig, und es
     gibt kein lokales k^2 S^4.
   - Die empirische S-Probe ist schwach (+-0,007 bei S = 0,5).
   - R^2-artige Glieder wachsen bei S = 0,5 um etwa den Faktor 1,6. Das fliesst in Befund 1.
   - Schwere: **gering**.
6. **Erwartungstreue trotz 19 % Kippen ist begruendet.**
   - Grund: exakte Randverteilung von psi_S(z) und Linearitaet des Erwartungswerts.
   - Fundstelle: PLAN Abschnitt 1, ERGEBNIS [K1].
   - Schwere: **kein Mangel**.
7. **Code und Konvention: in der Stichprobe fehlerfrei.**
   - Geprueft: psi, Geodaetenformel (selbst hergeleitet), Kotangens-Gewichte, log det' mit Erdung, derselbe Codeweg
     fuer Gamma(0), Fit-Code.
   - ID0 ist je Saat bitgleich zu INDUZIERT-ZUFALL-2D (Saat 0, beide Achsen). Die Kette bis -1/(24 pi) ist schluessig.
   - Schwere: **kein Mangel**.
8. **Richtungen 0 und 90 Grad: Die Uebereinstimmung auf 4e-5 ist Zufall.**
   - Fundstelle: ERGEBNIS Abschnitt 1 Punkt 1, Abschnitt 3.1.
   - Die beiden Werte sind je Saat fast unkorreliert (Korrelation etwa 0,04 aus den Streuungen). Die Differenz hat
     daher SE etwa 0,0022.
   - Eine Abweichung unter 4e-5 hat etwa 1,4 % Wahrscheinlichkeit.
   - Als Gegenprobe gilt nur "vertraeglich innerhalb 0,0022", nicht "reproduziert auf drei Stellen". Ein Fehler ist
     es nicht: a je Richtung unterscheidet sich (0,00017 gegen 0,00039).
   - Schwere: **gering**.
9. **"Schwerkraft aus Materie wird damit ... moeglich"** ist eine Hochrechnung aus einem 2D-Befund zur konformen Mode.
   - Fundstelle: ERGEBNIS Abschnitt 2, Bedeutung zweiter Punkt.
   - In 2D gibt es keine Gravitationsdynamik. Der Satz gehoert als [H] markiert und als "vertraeglich mit" formuliert.
   - Schwere: **gering bis mittel**. Es ist der vorab festgelegte Kartentext, aber in Karten und Berichten wird er
     sonst wiederholt.
10. **PLAN Abschnitt 3: "Rauschen faellt wie S^(-1/2)"** widerspricht den eigenen Zahlen (Faktor 2 von S = 0,25 zu
    0,5).
    - Schwere: **gering**, ohne Folgen.

## Empfohlene Formulierung

**Anforderungen an jede Fassung:**
- (A1) Die Zahl -0,0123 +- 0,0012 heisst Fenster-Steigung bei Gitterabstand 1, gewichtet bei abs(k) etwa 0,3. Der
  Fehler ist statistisch.
- (A2) Fuer k -> 0 steht der Bereich etwa 0,7 P bis 1,2 P mit Grund (k^4-Glied nicht bestimmt).
- (A3) Der N-Vergleich gilt nicht als Kontinuumsbeleg.
- (A4) "Trifft Polyakov auf 8 %" entfaellt.
- (A5) Der Rahmen bleibt genannt: 2D, euklidisch, gequenchtes Netzmittel, nur konforme Mode.

**Vorschlag; die Endfassung schreibt der Autor:**

> Auf denselben Grundpunkten macht die Streuung nach physikalischer Flaeche mit Neuvernetzung aus der induzierten
> konformen Steifigkeit eines P1-Skalars, +0,159 auf festem Netz, einen negativen Wert von der Groesse Polyakovs. Die
> Steigung ueber abs(k) = 0,05 bis 0,3 bei Gitterabstand 1 ist -0,0123 +- 0,0012 (statistisch; 0,92 P), und
> Vorzeichen und Groessenordnung sind gesichert. Der Kontinuumswert k -> 0 ist nur auf etwa 0,7 P bis 1,2 P
> eingegrenzt, weil ein k^4-Gitterglied von der Groesse des festen Netzes nicht ausgeschlossen ist; gezeigt ist das
> fuer ein gequenchtes Mittel ueber Netze in 2D, euklidisch, nur fuer die konforme Mode.
