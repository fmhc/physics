Urteil gesamt: haelt mit Einschraenkung. Frage 3 haelt; Fragen 1, 2, 4 und 5 halten mit Einschraenkung; keine faellt.
A-Befunde 0, B-Befunde 11, Auflagen N1 bis N3.

# GEGENLESEN KAUSAL-4D-KERNMASSE-1 (Leser pruefer-opus)

- Beginn: 2026-10-04 17:01:35 CEST (date); Abschluss: 2026-10-04 17:27:17 CEST (date), also 25 min 42 s von 60 min.
- Auftrag: RUNDE-37/kernmasse-leser/KARTE.md, sha256 f410002711f68fc08b87936dd2ea9f3ffc0b63762540ca367a398e21403cf71a
  (sha256 selbst gemessen; die Leitung nannte keinen Sollwert)
- Frischer Agent, kein Fork. Nur gelesen und auf dem Papier gerechnet; keine Laeufe, keine Abrufe.

## Gelesene Dateien

- kausal-4d-kernmasse-1/: KARTE.md, VORAB.md, PLAN.md (cmp gleich mit *.eingefroren-20261004-151112; sha256 wie
  EINGEFROREN-SHA256.txt, auch alle sieben Codedateien), ERGEBNIS.md, code/kernmasse_kont.py, kernmasse_feld.py,
  kernmasse_auswertung.py (Urteilsteil), kausal4d.py (Kopf, Quelle, Pruefpunkte), schicht2_kont.kt_gen;
  lauf-69/auswertung.json, kont/kern.json, kont/pole-VJ.json (per jq); rauch-69/pfad/aw/auswertung.json und Logs;
  quellen/: johnston-0806.3083v2.txt (3.25, 3.44), bbl-1411.6513v2.txt (Abschnitt 3, Fn. 8, Fn. 10),
  ass-1403.1622v1 (2.11 bis 2.18, Seitenbild PDF-S. 9 mit Abb. 3, Abschnitt 3.5 per grep); QUELLEN-SHA256.txt stimmt
- kausal-4d-schicht-2/lauf-69/kont/pole-VJ.json (sha256 e7e48961..., KM0-Bezug); kausal-4d-schicht-2/ERGEBNIS.md per grep
  (Vergleichszahlen 0,246 / 0,198 / 0,152 usw. stimmen mit VORAB und ERGEBNIS)
- kausal-4d-stabil-l/DOSSIER.md Z. 57-58 (V3, V4); weltmodell-review-1/REVIEW.md Z. 140-147 und 327-336
- RUNDE-41.md Z. 463-493 (Ernte) und 769-818 (Abschluss); Journal claude-runde-v3-41-20261004.json per jq

## Frage 1: Herleitung und Diskretisierung

**Urteil: haelt mit Einschraenkung** (Mathematik haelt; Einordnung als Antwort auf BBL Fn. 8 und "treue
Diskretisierung" zu weit).

**1a. Ortsraumform, auf dem Papier nachgerechnet [M]:**
- Schwinger-Darstellung: int_0^inf exp(-a l - b/l) dl = 2 sqrt(b/a) K1(2 sqrt(ab)). Mit a = Z^2, b = tau^2/4 folgt
  int exp(-l Z^2 - tau^2/(4l)) dl = (tau/Z) K1(Z tau), also K1(Z tau)/Z = (1/tau) * Integral. Stimmt.
- 4D-Transformierte: (4 pi/Z) int tau^2 g K1(Z tau) dtau = (2 pi/Z) int sqrt(sigma) K1(Z sqrt sigma) f(sigma) dsigma
  (tau^2 dtau = sqrt(sigma) dsigma/2). Einsetzen gibt f~(Z) = 2 pi int dl e^(-l Z^2) F(1/(4l)). Stimmt.
- Z^2 -> Z^2 + m^2 multipliziert mit e^(-l m^2) = e^(-m^2/(4 beta)). Inverse Laplace: Aus L[J0(2 sqrt(kt))] = e^(-k/s)/s
  und d/dt J0(2 sqrt(kt)) = -sqrt(k/t) J1(2 sqrt(kt)) folgt L^-1[e^(-k/s)] = delta(t) - sqrt(k/t) J1(2 sqrt(kt)). Mit
  k = m^2/4 ist das delta - h_m, h_m(y) = (m/(2 sqrt y)) J1(m sqrt y). Stimmt.
- Dimension: In d Dimensionen steht im Schwinger-Integral nur eine andere Potenz l^(d/2-2); der Faktor e^(-l m^2)
  wirkt gleich. "Gilt in jeder Dimension" stimmt.
- Proben: f = delta(sigma)/(2 pi) gibt (1/2 pi) delta(tau^2) - (m/4 pi) J1(m tau)/tau, das ist Johnston (3.25), an der
  Quelle gelesen (johnston-0806.3083v2.txt Z. 355-359). 2D: (1/2)[1 - int_0^(m tau) J1(x) dx] = (1/2) J0(m tau). Stimmt.
- Folgerungen in VORAB 2: a int e^(-c s^2) ds = a sqrt(pi/c)/2 = 1/(2 pi); |h_m| <= m^2/4 (|J1(x)/x| <= 1/2), also
  |T| <= m^2/(8 pi) = 0,0398; delta_sigma = 1/sqrt(pi c) = 0,780 / 0,551 / 0,390. Alles nachgerechnet, stimmt.
- Kleiner Vorzeichenfehler (B): Poisson-Glaettung einer Schwingung daempft. Ich erhalte
  g_bar - g_K ~ -T m^2/(32 c tau^2), nicht +T m^2/(32 c tau^2) (VORAB 3). Die Betraege 1,5 % und 0,4 % stimmen.

**1b. Numerische Probe:** Sie prueft genau die behauptete Identitaet. Links steht das Fourier-Bild von a e^(-c sigma^2)
+ T (T mit 128 Knoten), rechts kt_gen bei sqrt(Z^2 + m^2), mit eigener Quadratur und ohne T. Die Probe ist empfindlich:
Bei rho = 4, Z = 0,5 ist der masselose Wert 3,468 und das Ziel 0,520 (kern.json). T traegt also rund -2,95 bei, und
die Abweichung ist 3,6e-13 relativ. Insgesamt <= 1,93e-11 (Z = 4, rho = 4). Die Probe deckt nur reelles Z und nur
diesen einen Kern f ab. Komplexes omega folgt aus der Analytizitaet, die allgemeine Form aus der Herleitung.

**1c. Diskretisierung und Kontinuumswissen:**
- Im Mittel ist der Bau richtig. Fuer Zuschauerpunkte gilt das Mecke-Argument, und die Intervalle liegen ganz in D
  (D kausal konvex, B in D). Fuer rho -> oo geht g_bar gegen Johnston (3.25). Der Realisierungsfehler an den
  Pruefpunkten faellt etwa wie rho^(-1/2): 20 / 15 / 11 %, Verhaeltnisse 1,33 und 1,36 gegen sqrt 2 = 1,41.
  Er sitzt in einem Lichtkegelstreifen der Breite ~ rho^(-1/4) mit fester Hoehe 0,0135.
  - Nachgerechnet: Nahe am Lichtkegel haengt T als Funktion von u nicht von rho ab, denn
    T ~ -(m^2/4)(a/sqrt c) sqrt u mit a/sqrt c = 1/(pi sqrt pi).
  - Darum liegt das Fehlermaximum bei festem u, also bei tau ~ c^(-1/4): 0,93 * 0,841 = 0,78 und 0,78 * 0,841 = 0,66.
    Das stimmt mit ERGEBNIS 3.2.
  - Ab tau = 3 halbiert sich der Fehler je Verdopplung von rho (1,2e-4 / 5,9e-5 / 2,9e-5), wie 1/c.
- **Bei endlicher Dichte ist die Diskretisierung nicht exakt, nur asymptotisch treu.** Kein Kern, der nur von n
  abhaengt, trifft das Ziel exakt (VORAB 2, das Argument ueber halbzahlige Potenzen haelt). Das Mittel des gebauten
  Kerns weicht an den Pruefpunkten um 11 bis 20 % vom Ziel ab.
- **Kontinuumswissen steckt in:**
  - der ganzen Gewichtsfunktion t(n): Bessel-Kern h_m der Kontinuums-Green-Funktion, gefaltet mit Johnstons Linkmittel;
  - dem Eigenzeit-Schaetzer sigma_n = sqrt(n/c): flaches 4D-Volumengesetz V = pi tau^4/24 und bekannte Dichte, also
    nur in flacher Raumzeit richtig;
  - a aus Johnston (3.44), dazu d = 4 fest im Code.
- Von der Kausalmenge kommen nur die Ordnung und die Zahl n. Der Bau ist damit im Wesentlichen eine Monte-Carlo-Quadratur von
  int G_R^(m) J d^4y: Die gestreuten Punkte sind die Stuetzstellen, n liefert die geschaetzte Eigenzeit. Dazu kommt
  Johnstons Linkterm fuer den Lichtkegelanteil. Diese Lesart fehlt im ERGEBNIS (B, siehe Frage 5).
- **Einordnung BBL Fn. 8 (B-Befund):** Fn. 8 fragt nach der inversen Laplace-Transformierten von f(z + m^2) fuer BBLs
  f, also nach dem massiven BD-Operator (Gl. 2.1), und nennt als Ziel "a definition of the KG equation on a causal set"
  (bbl Z. 378-380).
  - Die Formel des Agenten gilt allgemein und wuerde auch den nichtlokalen Teil von (2.1) liefern. Angewandt und
    geprueft ist sie aber auf Johnstons masselosen Propagator k~, also auf f = 1/k~, nicht auf BBLs f.
  - Auf der Kausalmenge ist sie nach dem eigenen Satz des Agenten nicht exakt darstellbar.
  - ERGEBNIS 1.2 ("Die Ortsraumform, die BBL in Fussnote 8 als offenes Problem nennen, ist eine Faltung ...") liest
    sich deshalb wie eine Loesung des offenen Problems.
  - Wortlaut-Vorschlag: "Im Kontinuum ist die Ortsraumform von f(Box + m^2) fuer jeden retardierten invarianten Kern
    eine Volterra-Faltung in sigma = tau^2 (Herleitung [M], hier fuer Johnstons Linkkern numerisch geprueft). Eine
    exakte Kausalmengen-Form aus Intervallzahlen gibt es nicht; gebaut ist eine Naeherung."
- Neuheit [L?, aus dem Gedaechtnis, nicht geprueft]: Die Massenentwicklung retardierter Kerne als Reihe in
  m^2 sigma (Riesz-Kerne, M. Riesz 1949) ist dieselbe Struktur. e^(-m^2/(4 beta)) = sum (-m^2/4)^k beta^(-k)/k!
  entspricht k-facher Integration in sigma. Die Selbsteinstufung "moeglich bekannt" (ERGEBNIS L4) ist angemessen.
  "Eigene Herleitung" ja, "neues Ergebnis" ungeprueft.

## Frage 2: Urteile KM0, KM1, KM2

**Urteil: haelt mit Einschraenkung.** Alle sechs Urteile (Plan, Wortlaut) folgen mechanisch aus dem eingefrorenen Code
und stimmen mit den Regeln in PLAN 5 ueberein. KM1 ist eine Kontrolle. KM2 ist im Bereich rho = 4 bis 16 belastbar,
trennt VK aber nicht von den instabilen Varianten.

**KM0 (haelt):**
- Eigene Nachpruefung: Ich habe per jq die "ergebnisse" ohne zeit_s der neuen kont/pole-VJ.json mit SCHICHT-2
  lauf-69/kont/pole-VJ.json verglichen (sha256 e7e48961..., gleich dem Bezug in eingaben_sha256). Ergebnis: inhaltsgleich.
- Die eigene Datei hat einen anderen Hash (5a075b07..., PRUEFSUMMEN.txt). Ein Selbstvergleich ist das also nicht.
- Die Felder (24 Dateien) habe ich nicht nachgeprueft (npz, kein python); dafuer verlasse ich mich auf array_equal im
  Code.
- KM0 ist eine Reproduktion mit unveraendertem Code und sagt nichts ueber VK.

**KM1 (haelt als Kontrolle):**
- Die Ableitung habe ich selbst geprueft:
  - k~ als Funktion von Z^2 ist in C ohne (-oo, 0] analytisch. Wegen e^(-c tau^4) konvergiert das Integral fuer jedes
    Z mit |arg Z| < pi.
  - Fuer omega = x + iy mit y > 0 liegt Z_m^2 = k^2 + m^2 - x^2 + y^2 - 2ixy nur dann auf (-oo, 0], wenn x = 0 und
    k^2 + m^2 + y^2 <= 0. Das ist unmoeglich.
  - Residuum: Nahe Z = 0 gilt k~ ~ pi a sqrt(pi/c)/Z^2 = 1/Z^2 (eingesetzt: pi * sqrt(rho)/(2 pi sqrt 6) *
    2 sqrt 6/sqrt rho = 1). Also R -> 1.
  - Mit dem Logterm eps ln Z_m^2 und Z_m^2 ~ -2i omega_0 e folgt bei rho = 4 (eps = 0,195, omega_0 = 1, e = 1e-5):
    - Im R ~ 2 omega_0 e eps |ln(2 omega_0 e)| = 2e-5 * 0,195 * 10,8 = 4,2e-5;
    - Re R - 1 ~ -pi omega_0 e eps = -6,1e-6.
    Beides passt zur Tabelle (0,999994 + 4,2e-5 i).
- Fuer das tatsaechliche Mittel g_bar gilt |g_bar| <= sup |w_n| (Poisson-Mischung). Damit ist das Fourier-Integral fuer
  Im omega > 0 absolut konvergent, und das ist ein Satz.
- **"Jede beschraenkte Gewichtsfolge gibt ein stabiles Mittel" stimmt, aber es ist eine Eigenschaft des
  Ein-Schritt-Baus ohne Resummation, nicht der Kausalmenge.** KM1 ist eine Kontrolle, kein Befund. Die Ernte sagt das,
  das ERGEBNIS sagt es in Abschnitt 2.
- Unscharf ist dagegen:
  - ERGEBNIS 1.3 ("ableitbar und bestaetigt");
  - ERGEBNIS 6 ("Gezeigt [E, M]: ... das Mittel bei jeder Dichte stabil, und die Masse ist exakt"). Das ist [M]; [E]
    prueft nur den Bau (B).
- **"Masse genau m" gilt fuer das Ziel G_K~.** Fuer das Mittel des gebauten Kerns (g_bar) ist es nur ueber die
  Asymptotik begruendet (VORAB 3) und nicht gezaehlt. Das Argument halte ich fuer richtig: Die Poisson-Glaettung gibt
  den Faktor exp(-m^2/(32 c tau^2)) -> 1 und eine Phasenkorrektur ~ 3m/(32 c tau^3) -> 0. Gezaehlt ist es nicht (B).

**KM2 (haelt im Bereich rho = 4 bis 16):**
- Steigung nachgerechnet:
  - ln s = -0,9997 / -1,1809 / -1,4872. Bei drei gleich verteilten ln rho ist die LSQ-Steigung
    (y3 - y1)/(2 ln 2) = -0,4875/1,3863 = -0,352.
  - Zweipunkt: -0,1812/0,6931 = -0,261 und -0,3063/0,6931 = -0,442. Stimmt mit auswertung.json.
- Bootstrap (4 000 Ziehungen, Saaten je Dichte, Korrelation ueber die Punkte bleibt erhalten): 2,5 % -0,464,
  97,5 % -0,233, Anteil <= -0,2: 99,4 %.
  - Mit 12 Saaten hat eine einzelne sd 15 bis 21 % relativen Fehler: 1/sqrt 22 fuer eine Komponente, 1/sqrt 44 fuer
    Re + Im. Das geometrische Mittel ueber 18 korrelierte Punkte und die Bootstrap-Breite (68-%-Halbbreite 0,055)
    passen dazu.
  - Der Abstand zur Schwelle ist 0,152, also etwa 2,8 Halbbreiten. Fuer drei Dichten ist das belastbar.
- **Misst es, was KM2 verlangt?** Ja: sd ueber Netze an festen Punkten, relativ zu |K|; relativ zu |E| faellt es
  ebenfalls.
- **Einschraenkungen (B):**
  1. **Nicht trennscharf:** VJ -0,27, V-0 -0,35 und V-00 -0,30 erfuellen dieselbe Schwelle, jeweils aus ERGEBNIS 3.3
     nachgerechnet, z. B. VJ ln(0,310/0,453)/ln 4 = -0,274. Faellendes Rauschen ist hier eine Eigenschaft aller vier
     Schaetzer, auch der instabilen. VK unterscheidet sich nur im Niveau (VK/VJ = 0,81 / 0,74 / 0,73), und das ist
     beschreibend, nicht vorab festgelegt.
  2. **Bereich:** Die Pfadprobe (rho = 1,5 / 2 / 3, je 3 Saaten) gab s = 0,353 / 0,400 / 0,321, also keinen Abfall
     (rauch-69/pfad/aw/auswertung.json). Mit den Zweipunktsteigungen -0,26 -> -0,44 ist das kein Potenzgesetz, sondern
     ein Abfall, der um rho ~ 4 einsetzt. Der Satz "faellt mit der Dichte" gilt fuer rho = 4 bis 16.
  3. 16 der 18 Pruefpunkte liegen im Traeger der gekappten Quelle (t^2 + r^2 <= 12,25). Die zwei uebrigen (eta = 0,5,
     t = 3,2, Lagen A und B: 12,43 und 12,79) liegen knapp ausserhalb. Bei (2, 0, 0, 0) ist |J| = e^(-2) = 0,135.
     Gemessen ist also das Rauschen nahe der noch aktiven Quelle ueber 2/m, nicht das Rauschen einer frei laufenden
     Welle.

## Frage 3: Selbstanzeigen

**Urteil: haelt.** Die Regeln wurden nach der Pfadprobe nachweislich nicht geaendert, soweit es sich pruefen laesst. Fuer
das KM2-Urteil wiegt das nicht.

- **Zeitachse** (mtime und Logs, CEST = UTC + 2):
  - VORAB.md mtime 14:48, also vor dem Start der Pfadprobe (12:50:20 UTC = 14:50:20 CEST). Darin stehen
    die Baubedingung 15/18 und die Bau-gegen-Befund-Tabelle.
  - Das Pfadprobe-Urteil "KM2 nicht eingetroffen" lag um 13:10:49 UTC vor (rauch-69/pfad/aw.log).
  - Eingefroren wurde um 15:11:12 CEST, also 23 s spaeter. PLAN.md hat mtime 15:11 und berichtet in Abschnitt 9 bereits
    das Pfadprobe-Urteil, wurde also nach dessen Sichtung noch bearbeitet.
- **Entscheidend: Der Urteilscode lief unveraendert.**
  - rauch-69/pfad/aw/auswertung.json traegt skript_sha256 3c4601da... Das ist derselbe Hash wie der eingefrorene
    kernmasse_auswertung.py und die Hauptauswertung.
  - Ebenso kernmasse_feld.py (54cf8d35...) in den Pfadfeldern, und kernmasse_kont.py (5b7047eb...) in
    pole-VK-r1.5.json (12:58:43Z) und erwartung-VK-b.json (13:10:26Z) der Pfadprobe.
  - Damit sind Schwelle -0,2, LSQ-Steigung, s-Definition (geometrisches Mittel von sd/|K|) und Baubedingung >= 15 vor
    dem Pfadurteil im Code festgelegt und danach gleich geblieben.
- **Nicht pruefbar:**
  - Der Plantext in Abschnitt 4 und 5 vor 15:10:49 (es gibt keine Zwischenfassung). Er ist aber nicht urteilsbildend;
    urteilsbildend ist der Code.
  - Die Saatzahl 12 ist nur ueber den Laufplan PLAN 10 belegt, der zu 12 passt. Mehr Saaten verschieben die erwartete
    Steigung nicht, sie verengen nur das Band.
- **Gewicht fuer KM2: keins im Urteil.** Inhaltlich ist die Pfadprobe aber eine Information, die in die Bedeutung
  gehoert: Unter rho ~ 4 ist kein Abfall sichtbar (siehe Frage 2, KM2-Einschraenkung 2).
- Die uebrigen Selbstanzeigen habe ich geprueft:
  - Die Hauptlaufdateien tragen alle die eingefrorenen Hashes. Alle 36 Felddateien stammen aus der Zeit nach dem
    Einfrieren (13:13:45Z bis 13:40:02Z).
  - Die scp-Ueberschreibung ist in den Pfaddateien sichtbar: kern.json und erwartung-VK-a.json der Pfadprobe tragen
    kont-Hash 2f89b1fb... Auf die Hauptlaeufe wirkt sie nicht.
  - Die Doppelbelegung von "pole-VJ.json" in eingaben_sha256 ist wie angezeigt; der Vergleich lief ueber den Inhalt.
  - Der Bootstrap der Pfadprobe ist bei 3 Saaten entartet (Perzentile -820 / +683; sd = 0 bei gleichen Ziehungen).
    Bei 12 Saaten spielt das keine Rolle. Es ist ein Codehinweis fuer kuenftige Kleinlaeufe (B).

## Frage 4: Nebenbefund (Nullstellen von k~, BD-UV-Mode)

**Urteil: haelt mit Einschraenkung.** Die Rechnung stimmt. Die Lesart "vertauschte Achsen" ist gut gestuetzt, aber nur
gegen die eigene k~-Numerik geprueft. "Zehnmal langsamer" bleibt [H], bis eine unabhaengige Auswertung vorliegt.

**4a. Umrechnung nachgerechnet:**
- rho = 4: omega = 7,2142 + 0,5261 i, k = 0. omega^2 = 51,768 + 7,591 i, also Z_m^2 = 1 - omega^2 = -50,768 - 7,591 i,
  geteilt durch sqrt(rho) = 2 gibt -25,384 - 3,795 i.
- rho = 8: omega = 8,5551 + 0,6274 i. omega^2 = 72,796 + 10,735 i, also Z_m^2 = -71,796 - 10,735 i, geteilt durch
  2,8284 gibt -25,384 - 3,795 i. Der Spiegelpunkt liefert den konjugierten Wert. Das ergibt -25,38 -+ 3,80 i, stimmt.
- "Beide Dichten gleich" ist keine unabhaengige Bestaetigung. Mit tau = c^(-1/4) x haengt k~ nur von Z c^(-1/4) ab,
  also gilt Z^2 ~ sqrt(rho) exakt, und jede gleich skalierte Quadratur-Eigenheit skaliert mit.

**4b. Verknuepfung mit dem BD-Operator, auf dem Papier hergeleitet [M]:**
- Mit Delta = d^2/dtau^2 + (3/tau) d/dtau und partieller Integration (Randterm bei tau = 0) gilt fuer g = e^(-c tau^4):
  Z^4 L_g = L_(Delta^2 g) + 8 pi g(0), weil (Delta g)(0) = 0.
- Delta^2 e^(-u) = -192 c (1 - 9u + 8u^2 - (4/3) u^3) e^(-u) mit 192 c = 8 pi rho. Das ist genau das BD-Polynom zu
  b = (4/sqrt 6)(1, -9, 16, -8) aus ASS (2.12) (ass Z. 440-450).
- Damit gilt rho^(-1/2) g^(4) = -rho^(-1/2) Z^4 k~ exakt, und das Dossier V3 (B~ = Z^4 k~, dort aus Johnston 2010/2014)
  stimmt bis aufs Vorzeichen. Die Nullstellen von k~ mit Z != 0 sind also genau die von ASS' g^(4).
- Das Vorzeichen habe ich ueber die Grenzwerte geprueft:
  - IR: -Z^4 k~ -> -Z^2 (ASS (2.16): -Z);
  - UV: -Z^4 k~ -> -8 pi a = -4 sqrt(rho)/sqrt 6 (ASS (2.17): -4/sqrt 6).
  - Dazu die naechste UV-Ordnung: +64 pi^2 a/Z_ASS^2, mal rho^(-1/2) gibt 32 pi/(sqrt 6 Z^2), wie ASS (2.17).

**4c. Lesart von ASS Abb. 3a (Seitenbild PDF-S. 9 selbst angesehen):**
- Die Abbildung zeigt die Nullstelle bei der Achsenbeschriftung Re(Z) ~ 3,8 (senkrecht, 3,4 bis 4,2) und
  Im(Z) ~ -25,4 (waagrecht, -26 bis -25). Woertlich ist das Z = 3,8 - 25,4 i.
- Fuer "Achsen vertauscht" sprechen drei Indizien:
  1. In A hat die Zaehlung W = 2, stabil bei zwei Aufloesungen. Die woertliche Lage gaebe bei rho = 4 zusaetzlich
     omega = +-4,72 + 5,38 i in A, also W = 4. Das gilt aber nur, wenn kt_gen bei komplexem Z stimmt.
  2. ASS Abb. 3b zeigt fuer zeitartiges Z ~ -25 eine Schwingung der Amplitude ~ 2 bis 3 um den Wert -4/sqrt 6 = -1,63.
     Nach meiner Sattelpunktschaetzung (Exponent -1,5 c (kappa/4c)^(4/3) ~ -4,0, Vorfaktor ~ 170) liegt die
     Amplitude dort bei ~ 3. Eine Nullstelle wenige Einheiten neben der negativen reellen Achse ist damit natuerlich.
  3. Die Hoehenlinien in Abb. 3a geben |g'| ~ 0,35 je Einheit. Im Abstand 3,8 erwartet man damit |g| von etwa 1 bis 2,
     wie in Abb. 3b bei Re Z ~ -25. Die woertliche Lage ist 25,4 von der raumartigen Achse entfernt, wo g ~ -1,7 glatt
     verlaeuft.
- Gegen die Lesart spricht nur die Beschriftung. Die k~-Numerik bei komplexem Argument ist nur gegen sich selbst
  geprueft: Quadratur 128 gegen 256 und Newton. Die Fourierprobe deckt nur reelles Z ab.

**4d. Folgerung:**
- k = 0, masseloser BD-Operator: omega^2 = sqrt(rho) (25,38 +- 3,80 i).
  - sqrt(25,38 + 3,80 i): Betrag 25,66, Wurzel 5,066; halber Winkel 0,0743; ergibt 5,052 + 0,376 i.
    Also Im omega = 0,376 rho^(1/4).
  - Woertliche Lage: omega^2 = sqrt(rho)(-3,8 + 25,4 i), ergibt 3,31 + 3,84 i, also 3,8 rho^(1/4) (Dossier V4 Z. 58).
  - Verhaeltnis 10,2. "Zehnmal langsamer" stimmt rechnerisch, "masselos instabil" bleibt.
- Auflage N1: Vor jeder Uebernahme ins Dossier (V4) oder in einen Weichenstand wertet ein Haus, das kt_gen nicht
  geschrieben hat, ASS (2.14) unabhaengig aus, an Z = 3,8 - 25,4 i und an Z = -25,38 - 3,80 i. Genau einer der beiden
  Werte muss ~ 0 sein. Bis dahin lautet der Wortlaut: "[H] Unsere Nullstellen von k~ liegen bei
  Z^2/sqrt(rho) = -25,38 -+ 3,80 i. ASS Abb. 3a ist mit Re(Z) = 3,8, Im(Z) = -25,4 beschriftet; wir vermuten
  vertauschte Achsenbeschriftung. Dann waere die BD-UV-Rate 0,38 statt 3,8 rho^(1/4)."

## Frage 5: Bedeutungssatz in RUNDE-41.md und Journal

**Urteil: haelt mit Einschraenkung.**
- Kein Satz ist im engen Sinn falsch.
- Die Ernte (RUNDE-41.md Z. 463-493) ist weitgehend sauber: "Vorab ableitbar", "prueft den Bau, nicht die Kausalmenge",
  "Gewichte aus der Kontinuumsformel".
- Zu stark sind die verdichteten Stellen. Ihnen fehlen die Qualifizierer, die in der Ernte noch stehen:
  - RUNDE-41.md Z. 814: "Positiv: Die Kausalmenge traegt massive Materie in 3+1 stabil, mit Kontinuumsgewichten."
  - Journal-Titel: "die Kausalmenge traegt massive Materie in 3+1 stabil (Gewichte aus dem Kontinuum)".
  - Journal meaning: "Positiv: Auf der Kausalmenge bleibt massive Materie in 3+1 stabil, wenn die Masse im nichtlokalen
    Kern sitzt, und das Rauschen des einzelnen Netzes faellt mit der Dichte".
  - Ernte Z. 490-493: "K-B traegt im Mittel stabile massive Materie ..." und "positiv beantwortet".
- Das Kartenzitat der Leser-Karte (Frage 5) mischt Ernte und Journal. Woertlich steht im Journal "die Kausalmenge traegt
  massive Materie in 3+1 stabil" (Titel) und "Kontinuumsformel" (meaning).

**Was fehlt (Anforderungen an den Wortlaut, Formulierung bei der Leitung):**
1. **Stabil durch Bau, nicht durch die Kausalmenge.**
   - Jeder beschraenkte Ein-Schritt-Kern ist im Mittel stabil (Frage 2). Sogar jedes Einzelnetz ist beschraenkt:
     |phi(x)| <= (1/rho) max|W| sum |J(y)|. Exponentielles Anwachsen ist in dieser Bauweise unmoeglich.
   - "Stabil" darf deshalb nicht als positiver Befund ueber die Kausalmenge stehen (Regel "Vorab ableitbare Kennzahl ist
     keine Messung").
   - Gemessen ist nur das Rauschen.
2. **Fallendes Rauschen ist nicht trennscharf.** Es faellt bei allen vier Varianten, auch bei den instabilen
   (VJ -0,27, V-0 -0,35, V-00 -0,30). Positiv und VK-eigen ist nur das niedrigere Niveau, 0,73- bis 0,81-mal VJ auf
   denselben Netzen, und das ist beschreibend.
3. **Propagator, keine Dynamik.**
   - VK ist eine vorgegebene retardierte Green-Funktion: ein einziger Summenschritt ueber die Quelle, keine Pfadsumme,
     keine Rekursion.
   - Die VK-Matrix ist als gebaut streng dreieckig und damit nilpotent. Eine Gleichung auf der Kausalmenge, deren
     Green-Funktion VK ist, ist weder angegeben noch untersucht. Mit Diagonalterm gaebe es formal (I + W)^-1; dessen
     Eigenschaften (Lokalitaet, Stabilitaet) sind offen.
   - Das ERGEBNIS sagt das selbst ("Offen bleibt, ob eine Dynamik der Kausalmenge diesen Kern auswaehlt"). Im
     Bedeutungssatz fehlt es.
   - Fuer den genannten naechsten Schritt (Wechselwirkung, Eichfeld) ist das die entscheidende Luecke.
4. **Bereich:** freier Skalar, flache Raumzeit (der Schaetzer sqrt(n/c) setzt V = pi tau^4/24 voraus), rho = 4 bis 16,
   Laufstrecke 2/m, Pruefpunkte im Traeger der Quelle. Unter rho ~ 4 zeigte die Pfadprobe keinen Abfall des Rauschens.
5. **"Masse im nichtlokalen Kern" nicht mit BBLs Gleichung verwechseln.**
   - Ernte Z. 474 sagt "(BBLs f(Box + m^2))". BBLs f ist der BD-Operator. Wegen B~ = -Z^4 k~ (Frage 4b) hat BBLs eigene
     Form 1/B~(Z_m) Pole genau an den Nullstellen von VK.
   - Bei rho = 4 liegen sie bei omega = +-7,21 + 0,53 i. Die Gleichung waere also instabil, sogar schneller als VJ
     (0,25). Bei woertlicher Lesart von ASS Abb. 3a waere sie mit Im omega ~ 5,4 noch instabiler; instabil ist sie
     also unter beiden Lesarten.
   - Stabil ist nur BBLs Vorschrift (Masse ins Argument), angewandt auf Johnstons Propagator k~ statt auf den Operator.
     VORAB 2 sagt das richtig ("BBL (3.2) fuer den Propagator f^-1 = k~"), ERGEBNIS 1.2 und die Ernte verkuerzen es.
6. **"positiv beantwortet"** (Ernte Z. 492-493): Das Review-Kriterium ist als Ausschlusskriterium formuliert (REVIEW.md
   Z. 332: "Sonst traegt K-B keine massive Materie auf diesem Weg"). Bestanden heisst: auf diesem Weg nicht
   ausgeschlossen, mit Kontinuumsgewichten. Das ist eine Existenzaussage, kein Beleg fuer K-B als Grundlagenmodell.

**Wortlaut-Vorschlag** (fuer RUNDE-41.md Z. 814 und eine Journal-Berichtigung mit neuer ID ueber research_journal.py;
der Eintrag selbst bleibt unveraendert):
> "K-B ist fuer massive Materie in 3+1 auf diesem Weg nicht ausgeschlossen. Ein Ein-Schritt-Kern, der die massive
> Kontinuums-Green-Funktion mit der Intervallzahl als Eigenzeit-Schaetzer abtastet (Masse im Argument von Johnstons
> masselosem Kern), hat ein stabiles Mittel; das folgt fuer jeden beschraenkten Ein-Schritt-Kern schon am Schreibtisch.
> Gemessen: Das Einzelnetz-Rauschen faellt zwischen rho = 4 und 16 (Steigung -0,35) und liegt 19 bis 27 % unter dem von
> Johnstons Pfadsumme (VJ) auf denselben Netzen, deren Rauschen ebenfalls faellt. Freier Skalar, flache Raumzeit,
> Laufstrecke 2/m; eine Bewegungsgleichung auf der Kausalmenge fehlt."

- Rechnung zu "19 bis 27 %": VK/VJ = 0,368/0,453 = 0,81 und 0,226/0,310 = 0,73, also 1 - 0,81 = 0,19 und
  1 - 0,73 = 0,27. Gegen V-0 und V-00 ist der Abstand groesser (0,226/0,636 = 0,36 bei rho = 16).

**Kleinere Stellen in der Ernte (B):**
- Ernte Z. 472, "ihre Normen wachsen": Das gilt nicht fuer V-0 bei rho = 16 (G = 1,02 bzw. 1,07; Saatmedian 1,01).
- Ernte Z. 480, "(bis etwa 40 % Fehler im Mittel)": Die 40 % sind der Fehler des Schweifkerns nahe am Lichtkegel
  (0,0135 gegen 0,032 bis 0,035). Im Mittelfeld an den Pruefpunkten sind es 11 bis 20 % von |K| (ERGEBNIS 3.2).
- Ernte Z. 482-483: "ASS Abb. 3a mit vertauschten Achsen" steht als Tatsache. Nach Frage 4 ist das [H], bis N1
  erledigt ist.

## A-Befunde

**Keine.**
- Kein Urteil (KM0 bis KM2, nach Plan und nach Wortlaut) kippt.
- Keine Zahl, die eine Aussage traegt, ist falsch. Die Herleitung haelt.
- 42 Nachrechnungen, je mit Rechenweg in den Fragen. 41 stimmen, eine hat ein falsches Vorzeichen ohne Folgen (B7):
  - F1 (16): Schwinger; 4D-Laplace-Form; L^-1[e^(-k/s)]; Dimensionsunabhaengigkeit; Johnston (3.25); 2D-J0;
    a int = 1/(2 pi); |T| <= 0,0398; delta_sigma (3); Asymptotik-Betrag; Asymptotik-Vorzeichen (falsch);
    Fehlerverhaeltnisse; Lage des Fehlermaximums; Halbierung ab tau = 3.
  - F2 (13): Analytizitaet; Z_m^2-Argument; Residuum 1; Im R; Re R; |g_bar|-Schranke; KM0-Inhalt per jq; LSQ -0,352;
    Zweipunkt (2); VJ, V-0, V-00 (3).
  - F4 (9): Z^2/sqrt rho bei rho = 4 und 8 (2); Skalierung; BD-Polynom aus Delta^2; Grenzwerte gegen ASS (2.16)/(2.17);
    0,376; 3,31 + 3,84 i; Faktor 10,2; VORAB 4,72 + 5,38 i.
  - F5 (4): VK/VJ (3); VK/V-0.
- B1 ist kein A-Befund, weil der Satz im schwachen Sinn ("die Kausalmenge kann diesen Kern tragen") stimmt. Er muss
  aber vor jedem Weichenstand und vor jeder Meldung an Finn geaendert werden.

## B-Befunde

Nach Gewicht geordnet.

- **B1 Bedeutungssatz zu stark.** Fundstellen: RUNDE-41.md Z. 814; Journal claude-runde-v3-41-20261004 Titel und
  meaning; Ernte Z. 490-493.
  - Die Stabilitaet folgt fuer jeden beschraenkten Ein-Schritt-Kern (Satz, KM1 ableitbar), nicht aus der Kausalmenge.
  - Das Fallen des Rauschens gilt fuer alle vier Varianten.
  - Gebaut ist ein Propagator ohne Gleichung auf der Kausalmenge, im Bereich rho = 4 bis 16 ueber 2/m.
  - Wortlaut-Vorschlag in Frage 5. Das Journal braucht eine Berichtigung mit neuer ID (research_journal.py).
- **B2 "BBLs f(Box + m^2)".** Fundstellen: ERGEBNIS 1.2, Ernte Z. 474.
  - Das f ist hier 1/k~, nicht BBLs BD-Operator.
  - BBLs eigene Form 1/B~(Z_m) hat wegen B~ = -Z^4 k~ Pole an den VK-Nullstellen und ist instabil (rho = 4:
    Im omega = 0,53 > VJ 0,25).
  - Wortlaut-Vorschlag: "BBLs Vorschrift (Masse ins Argument), angewandt auf Johnstons masselosen Propagator k~; BBLs
    Operatorform mit dem BD-Operator bliebe instabil".
- **B3 BBL Fn. 8 "als offenes Problem ... ist eine Faltung".** Fundstellen: ERGEBNIS 1.2, Ernte Z. 475-476.
  - Geloest ist nur die Kontinuumsform; sie gilt allgemein, geprueft ist sie fuer Johnstons Kern.
  - Eine exakte Kausalmengen-Form gibt es nach dem eigenen Satz nicht.
  - Neuheit ist ungeprueft (Riesz-Struktur [L?]). Wortlaut-Vorschlag in Frage 1.
- **B4 Nebenbefund als Tatsache.** Fundstelle: Ernte Z. 482-483 ("mit vertauschten Achsen").
  - Rechnung richtig, Lesart gut gestuetzt, aber nur gegen die eigene k~-Numerik geprueft.
  - [H] bis Auflage N1.
- **B5 KM1-Kennzeichnung.**
  - ERGEBNIS 1.3 "ableitbar und bestaetigt" und 6 "Gezeigt [E, M]" sollten [M] heissen, mit dem Zusatz "Rechnung
    prueft den Bau".
  - "Masse genau m" gilt fuer das Ziel. Fuer das Mittel des gebauten Kerns ist es per Asymptotik begruendet, aber nicht
    gezaehlt.
- **B6 KM2: Bereich und Trennschaerfe.**
  - Der Satz "faellt mit der Dichte" gilt fuer rho = 4 bis 16. In der Pfadprobe (rho = 1,5 bis 3) ist kein Abfall zu
    sehen.
  - Die Zweipunktsteigungen (-0,26 und -0,44) zeigen kein reines Potenzgesetz.
  - VJ, V-0 und V-00 erfuellen die Schwelle ebenfalls.
  - 16 von 18 Pruefpunkten liegen im Traeger der Quelle.
- **B7 Vorzeichen** (VORAB 3): Die Poisson-Glaettung daempft, also g_bar - g_K ~ -T m^2/(32 c tau^2). Die Betraege
  stimmen. Ohne Folgen; die Vorab-Datei bleibt eingefroren, Vermerk im ERGEBNIS genuegt.
- **B8** (Ernte Z. 472): "ihre Normen wachsen" stimmt nicht fuer V-0 bei rho = 16 (G = 1,02 / 1,07).
- **B9** (Ernte Z. 480): "bis etwa 40 % Fehler im Mittel". Die 40 % gelten fuer den Schweifkern nahe am Lichtkegel; an
  den Pruefpunkten sind es 11 bis 20 % von |K|.
- **B10** (Code, ohne Wirkung): Der Bootstrap entartet bei 3 Saaten (sd = 0 bei gleichen Ziehungen, Perzentile
  -820 / +683 in der Pfadprobe). Fuer kuenftige Kleinlaeufe: Ziehungen mit sd = 0 verwerfen oder melden.
- **B11** (Leser-Karte, Frage 5): Das Zitat mischt Ernte ("K-B traegt im Mittel ...") und Journal ("Kontinuumsformel").
  Der Journaltitel lautet "die Kausalmenge traegt massive Materie in 3+1 stabil (Gewichte aus dem Kontinuum)".

**Auflagen:**
- **N1 (vor Uebernahme des Nebenbefunds):** Ein Haus, das kt_gen nicht geschrieben hat, wertet ASS (2.14) unabhaengig
  aus, an Z = 3,8 - 25,4 i und an Z = -25,38 - 3,80 i.
- **N2 (vor Weichenstand oder Meldung an Finn):** B1 umsetzen, also RUNDE-41.md Z. 814 berichtigen und das Journal mit
  neuer ID berichtigen. Ernte Z. 474 und Z. 482-483 nach B2 und B4 nachziehen.
- **N3 (fuer den naechsten Schritt "Wechselwirkung bzw. Eichfeld"):** Vorab klaeren, wie ein Ein-Schritt-Propagator ohne
  Gleichung Wechselwirkung tragen soll, etwa ueber Stoerungsreihe oder Operator mit Diagonalterm. Sonst baut der
  naechste Schritt auf einem Propagator, zu dem es keine Dynamik gibt.

## Einfach gesagt

Der Agent hat eine Regel gebaut, mit der eine schwere Welle auf dem zufaelligen Raumzeit-Netz nicht mehr von selbst
anwaechst. Seine Mathematik habe ich auf dem Papier nachgerechnet, sie stimmt, und die Rechnungen auf dem Computer passen
dazu. Dass die Welle nicht anwaechst, liegt aber an der Bauart der Regel und nicht am Netz: Jede Regel dieser Art mit
begrenzten Gewichten waere stabil, und die Gewichte stammen aus der bekannten Formel fuer schwere Teilchen. Neu gemessen
ist nur, dass das Rauschen eines einzelnen Netzes kleiner wird, wenn das Netz feiner wird. Das gilt aber auch fuer alle
alten Regeln, die neue rauscht nur etwas weniger. Man sollte deshalb sagen "auf diesem Weg nicht ausgeschlossen", nicht
"das Netz traegt massive Materie".
