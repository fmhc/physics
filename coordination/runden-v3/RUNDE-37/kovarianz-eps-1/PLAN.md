# KOVARIANZ-EPS-1: Plan (Code-Agent, Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 17:04:46 CEST (date). Lesen und Schreibtisch bis etwa
  17:20, code/kovarianz_eps.py bis etwa 17:24 CEST, vorab 15:24:56 bis 15:25:03 UTC, Kontrolle 15:25:09 bis 15:25:54,
  Rauchlaeufe 15:25:54 bis 15:30:00 UTC (blind), Codeprobe 15:31 bis 15:36 UTC (nur Struktur gelesen). VORAB.md ab
  17:33:33 CEST, Plantext ab 17:36:29 CEST.
- **Grundlage:** KARTE.md (KE0 bis KE4, Wahrscheinlichkeiten und Bedeutung unveraendert, Abschnitte 6 und 7);
  kovarianz-kugel-1/ (ERGEBNIS, PLAN mit S4, VORAB, code, Nachtraege), kovarianz-2d-gegenprobe/ (ERGEBNIS, code),
  induziert-kugel-2/ERGEBNIS.md (Regel Q, beta_Q = -1,613 +- 0,052).
- **Code:** code/kovarianz_eps.py (neu; Modi vorab, kontrolle, messung, auswertung). Unveraendert kopiert und importiert
  (sha256 gleich den eingefrorenen Fassungen von KOVARIANZ-2D-GEGENPROBE): kovarianz2d.py (4d83a55d...), kugel.py
  (c2a4d790...), kugel2.py (15dcbd85...); dazu unveraendert kopiert dichte4d.py, induziert.py, zufall2d.py (Importe von
  kugel.py) und kovarianz.py (bed2c12a..., nur Bezug).
- **Vorab-Datei:** VORAB.md (Einstein je Amplitude, Erwartungswert von (a), Scherprognose fuer (b), Moebius, Umklappen).
- Kennzeichen: [M] eigene Mathematik, [ES] eigener Schluss, [F] Festlegung dieses Plans, [K] Kartenpunkt (vor dem
  Rechnen offengelegt), [H] Hypothese, [E] in Kontrolle oder Rauchlauf gerechnet (Rauchlauf blind: keine Gamma-Werte),
  [P] Projektdatei.

## 1. Schreibtisch (Kurzfassung; Einzelheiten VORAB.md)

| Nr | Punkt | Befund |
|---|---|---|
| S1 | eps = +0,1 | Nicht baubar: Regel QI braucht die Einbettung als Rotationshyperflaeche, die nur fuer eps <= 0,05 existiert (Kruemmung am Pol 12 - 240 eps). Kontrolle C6: profil_min = -0,114 [M, E] |
| S2 | Erwartungswert von (a) | E[Delta Gamma_a] = E_frisch[Gamma(S^4, g)] - E_frisch[Gamma(S^4, g0)]: Die verschobenen Punkte sind exakt eine frische Stichprobe auf (S^4, g); die Paarung aendert nur die Streuung. Der Erwartungswert ist glatt in eps, die erste Ableitung bei 0 ist null (SO(5)) [M] |
| S3 | Was "gleiches Vorzeichen" zeigt | Auch eine glatte gerade Antwort c2 eps^2 hat bei +eps und -eps dasselbe Vorzeichen. Nicht glatt heisst: gerader Anteil mit Steigung deutlich unter 2 (in abs(eps)) [M, K1] |
| S4 | Was (b) misst | Festes, im runden Mass isotropes Netz mit der Rueckholung phi*g = e^H g0, tr H = 0 (massstreuer Transport). Scherprognose c N <tr H^2>, 0 <= c <= 1/16, Schaetzung 1/24, positiv, waechst wie N; <tr H^2> = 32,9 eps^2 [M, H] |
| S5 | Erwartung (b) | G_b(0,05) etwa +0,144 im N-Mittel (Spanne -0,014 bis +0,223), Einstein allein -0,0137. Glatt (Steigung 1,99, ungerade/gerade -8,7 %), waechst wie sqrt(N) [H] |
| S6 | Moebius | Bildet das runde Delaunay-Netz auf sich ab: M ist in (a) und (b) dasselbe (C2: 4e-12) und gleich der Groesse, die KOVARIANZ-KUGEL-1 gemessen hat (-0,00166 +- 0,00019, -8,9 SE) [M, P, K2] |
| S7 | Umklappen in (b) | Kontrolle und Rauchlauf (Geometrie): K mit abs(eps) <= 0,025 nie, -0,05 hoechstens 1, -0,1 bis 4 von 27 000 bis 118 000 Simplizes; D(0,25) 8 bis 31, D(0,5) 36 bis 107 [E] |
| S8 | Rauschen (blind) | Std von y je (Saat, N): (a) 0,03 bis 0,23; (b) K 0,001 bis 0,04; M 0,001 bis 0,002; D 0,02 bis 0,05 (2 bis 3 Saaten) [E] |

## 2. Konstruktion (code/kovarianz_eps.py) [F]

- **Rundes Netz:** k1.kugelnetz(4, N, saat) (Saatschluessel [20261004, 39, 4, N, saat]) und Regel Q roh, Operationen wie
  kv2.rundes_netz, nur Q. Bitgleich mit KOVARIANZ-KUGEL-1 (C3).
- **Verformungen:** K(eps) = kv2.verf_konform(eps, 4): sigma = eps (1 - 5 cos^2 theta) + c, Volumen N.
  - (a): eps = -0,1, -0,05, -0,025, +0,025, +0,05 (Karte ohne +0,1, S1).
  - (b): dieselben und zusaetzlich +-0,0125 (Zusatz, beschreibend); dazu M (Moebius t = 0,2) und D(kappa) mit
    kappa = 0,25 und 0,5 (Scherkontrolle, beschreibend).
- **Punkte:** dieselben Zufallspunkte; theta' = F_g^-1(F_0(theta)) (kv2 Verformung.transport, Rest <= 1e-10 Pflicht),
  Faserrichtung w fest.
- **(a) Neuvernetzung:** kv2.huellnetz der verschobenen Punkte (konforme Karte), alle Pruefungen von kugel.kugelnetz;
  Laengen QI = Sehnen^2 der Einbettung mal sqrt(V_g/V_Sehnen) je Simplex (V_g = Koordinatensimplex mal
  Grundmann-Moeller-Mittel Grad 5 von J e^(4 sigma)); Gamma = k1.auswerten (duenne LU). Fuer QI dieselben Operationen
  wie kv2.verformtes_netz (C3: bitgleich, auch gegen die Laufdatei von KOVARIANZ-KUGEL-1). CI wird nicht gerechnet.
- **(b) Mitgenommene Verbindungen:** kn['tri'] des runden Netzes (orientiert) bleibt; dieselben verschobenen Punkte;
  Sehnen^2 der Einbettung je Kante; QI mit **|V_g|** je Simplex [F]. Fuer nicht umgeklappte Simplizes ist das genau QI.
  - **Umgeklappt** heisst n.c <= 0 in der Karte (Kreuzprodukt der Kanten in der runden Eckenreihenfolge, c =
    Schwerpunkt); dann ist V_g < 0, und |V_g| ist das unsignierte g-Volumen des Kugelsimplex der fuenf Kartenpunkte.
  - **Entartet** heisst Sehnen-Gram-Eigenwert <= 0; fast entartet < 1e-6. Ein entartetes Simplex macht das Netz ungueltig
    (keine LU), umgeklappte nicht.
  - **Behandlung [F]:** Umgeklappte Simplizes bleiben mit |V_g| im Netz und werden je Netz gezaehlt und gemeldet; die
    Urteile nutzen alle gueltigen Netze. Beschreibend: Umklappzahlen je (Amplitude, N), Netze ohne Umklappen, kleinste
    Sehnen-Gram-Eigenwerte, staerkste Quetschung V_Sehnen(b)/V_Sehnen(rund), Summen V_g/N (signiert) und |V_g|/N.
- **D(kappa):** sigma = 0; Punkte vor dem Transport mit der Faserdrehung w -> R(kappa theta) w in der (w1, w2)-Ebene
  verschoben (massstreu, nicht isometrisch; wie nachtrag_drehung.py von KOVARIANZ-KUGEL-1), dann wie (b).

## 3. Messgroessen und Schaetzer [F]

- Je Saat j, N und Netz X: y_j(N) = (Gamma_QI(X) - Gamma_Q(rund))/sqrt(N). ybar_j = Mittel ueber N = 1000, 2000, 4000.
  b_X = Mittel der ybar_j, SE = Std(ybar_j, ddof 1)/sqrt(M) (wie KOVARIANZ-KUGEL-1).
- **Gerader und ungerader Anteil** je Saat: G_j(e) = (ybar_j(+e) + ybar_j(-e))/2, U_j(e) = (ybar_j(+e) - ybar_j(-e))/2,
  e = 0,025 und 0,05 (beide Bauweisen) und 0,0125 (nur (b)); Mittel und SE ueber die Saaten; ebenso je N.
- **Steigung** des geraden Anteils in ln abs(G) gegen ln e: zwischen 0,025 und 0,05 (Karte; in (b) zusaetzlich ueber
  0,0125 bis 0,05), SE per Jackknife ueber die Saaten (kv2.steigung_jackknife). Beschreibend: einseitige Steigung ueber
  eps = -0,025, -0,05, -0,1 (Vergleich mit KOVARIANZ-KUGEL-1).
- **N-Abhaengigkeit:** je Bauweise y je N und Delta Gamma je N (Mittel, SE).
- **Scherkontrolle (beschreibend):** c_Scher = y_D/(sqrt(N) <tr H^2>_D) je N; scherbereinigt G_b(e) - y_D(0,5)
  <tr H^2>_K,gerade(e)/<tr H^2>_D(0,5) je N, gegen y_E gerade.

## 4. Saaten, N, Laeufe [F, nach dem Rauchlauf; Zeitregel vorher notiert]

- **Saaten 0 bis 39** (dieselben Nummern und Punkte wie KOVARIANZ-KUGEL-1, INDUZIERT-KUGEL-1/-2 und der
  Amplituden-Nachtrag), N = 1000, 2000, 4000. Rauchzeit je (Saat, N) 14 / 33 / 90 s, zusammen etwa 5480 s.
- .69, /home/fmh/fmhc-physics-remote/runde42-kovarianz-eps/lauf/, nur ueber kleintest.sh, je Spur eine Kette:
  - cpu: kontrolle (eingefrorener Code); N = 4000 Saaten 0-4, 5-9, 10-14, 15-19; N = 2000 Saaten 0-13, 14-27.
  - cpu4: N = 4000 Saaten 20-24, 25-29, 30-34, 35-39; N = 2000 Saaten 28-39; N = 1000 Saaten 0-19, 20-39.
  - Je Lauf hoechstens etwa 470 s geplant (Grenze 600 s); Ausgabe lauf/messung-N<N>-s<saat0>.json, Schreiben nach jeder
    (Saat, N).
- **Abbruch [F]:** letzter Start spaetestens 18:50 CEST. Fehlende (Saat, N) zaehlen als unvollstaendig (nicht
  ausgeschlossen).
- Danach: kovarianz_eps.py auswertung lauf /home/fmh/fmhc-physics-remote/runde41-kovarianz-kugel/lauf lauf/auswertung.json.

## 5. Tor [F]

- Je Bauweise getrennt: (a) rundes Netz und alle fuenf (a)-Netze gueltig bei allen drei N; (b) rundes Netz, M und alle
  sieben K-Netze gueltig bei allen drei N; D (beschreibend) eigenes Tor. Gueltig: (a) Huellenpruefungen, LU, Transportrest
  <= 1e-10, Profil einbettbar; (b) LU (also kein entartetes Simplex), Transportrest, Profil.
- Bestanden, wenn mindestens 20 Saaten gut und hoechstens 10 % der vollstaendigen Saaten ausgeschlossen; sonst die
  Urteile der Bauweise "nicht auswertbar (Tor)".

## 6. Vorhersagen der Karte (unveraendert) und Urteilsregeln (mechanisch in kovarianz_eps.py auswertung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KE0 | Kontrollen: Bauweise (a) reproduziert die KOVARIANZ-KUGEL-1-Werte bei eps = -0,1 im Rahmen der Fehler; Moebius-Nullprobe in (b) innerhalb 3 SE um null | 85 % |
| KE1 | [H] Bauweise (a): Bei +eps und -eps hat Delta Gamma dasselbe Vorzeichen (nicht glatt), mindestens bei eps = 0,025 und 0,05 | 60 % |
| KE2 | [H] Bauweise (b): Antwort glatt (gerader Anteil mit Steigung 1,7 bis 2,3 in log abs(eps); ungerader Anteil unter 20 % des geraden) | 55 % |
| KE3 | [H] Bauweise (b): Der gerade Anteil haengt nicht von N ab (Aenderung 1000 auf 4000 unter 15 % bzw. 2 SE) | 40 % |
| KE4 | [H] Bauweise (b): Der gerade Anteil trifft das Einstein-Vorzeichen und liegt innerhalb Faktor 3 der Kontinuumsvorhersage aus dem gemessenen B | 25 % |

- **KE0** (Plan = Karte): Teil 1: In allen (Saat, N), die auch KOVARIANZ-KUGEL-1 gerechnet hat, sind Gamma_Q(rund) und
  Gamma_QI von (a) bei eps = -0,1 gleich deren Laufdateien (Abweichung <= 1e-8; erwartet bitgleich). Teil 2: abs(b_M)
  <= 3 SE_M in (b). Eingetroffen, wenn beide Teile. Mitberichtet: b_M/b_a(-0,1). Vorab [K2]: Teil 2 ist durch
  KOVARIANZ-KUGEL-1 bestimmt (erwartet etwa -5 SE, also nicht eingetroffen).
- **KE1** (a):
  - Karte: b(+e) und b(-e) haben fuer e = 0,025 und e = 0,05 jeweils dasselbe Vorzeichen (Punktschaetzer).
  - Plan [K1]: Vorzeichenteil: fuer beide e sind b(+e) und b(-e) je >= 3 SE von null und gleichen Vorzeichens; sind sie
    je >= 3 SE und entgegengesetzt, "nicht eingetroffen"; sonst "nicht entschieden". Dazu Glaetteteil: Steigung s des
    geraden Anteils zwischen 0,025 und 0,05: s + 2 SE < 1,7: eingetroffen (nicht glatt im gemessenen Bereich);
    s - 2 SE >= 1,7: "nicht eingetroffen (gerader Anteil quadratisch)"; sonst "nicht entschieden".
- **KE2** (b): Steigung s des geraden Anteils zwischen 0,025 und 0,05; Quotient abs(U)/abs(G) bei 0,025 und 0,05.
  - Karte: 1,7 <= s <= 2,3 und beide Quotienten < 0,2 (Punktschaetzer).
  - Plan: auswertbar nur, wenn abs(G) >= 3 SE bei beiden e; dann eingetroffen, wenn [s - 2 SE, s + 2 SE] in [1,7; 2,3]
    und bei beiden e abs(U) + 2 SE_U < 0,2 abs(G); nicht eingetroffen, wenn das Steigungsintervall [1,7; 2,3] nicht
    schneidet oder bei einem e abs(U) - 2 SE_U >= 0,2 abs(G); sonst "nicht entschieden".
- **KE3** (b), e = 0,05 [K3]: D = G(N = 4000) - G(N = 1000) in y (Saatmittel je N), SE_D = Wurzel aus SE_1000^2 + SE_4000^2.
  Plan = Karte: eingetroffen, wenn abs(D) <= 2 SE_D oder abs(D) <= 0,15 abs(G(1000)). Zusatzzeilen: e = 0,0125 und 0,025.
- **KE4** (b), e = 0,05 [K3]: r = G/y_E,gerade mit y_E,gerade = -0,013706 +- 0,000442 (VORAB.md); SE_r aus SE_G und
  dem Fehler von beta.
  - Karte: G < 0 und 1/3 <= r <= 3 (Punktschaetzer).
  - Plan: G >= +3 SE: "nicht eingetroffen (falsches Vorzeichen)"; sonst Intervallregel [r - 2 SE_r, r + 2 SE_r] in
    [1/3; 3]: eingetroffen (nur wenn zugleich G <= -3 SE), ganz ausserhalb: nicht eingetroffen, sonst nicht entschieden.
    Zusatzzeilen: e = 0,0125 und 0,025.
- Bei nicht bestandenem Tor: "nicht auswertbar (Tor)" fuer die Urteile der Bauweise.

## 7. Bedeutung (Karte, unveraendert) und Kernaussage [F]

- Karte: "KE1 und KE2 treffen ein: Die 4D-Anomalie ist ein Neuvernetzungs-Effekt. Mit mitgenommenen Verbindungen ist die
  Antwort glatt; ob sie Einstein ist, sagen KE3 und KE4." "KE2 verfehlt: Auch ohne Neuvernetzung ist die Antwort nicht
  glatt. Dann liegt es an der 4D-Steifigkeit bzw. an der Grobheit, und das 4D-Kugelnetz ist so nicht als Einstein
  lesbar."
- **Kernaussage fuer ERGEBNIS.md (vorab festgelegt):** "Liegt die Anomalie an der Neuvernetzung?"
  - **ja**, wenn KE1 und KE2 nach Plan eingetroffen sind;
  - **nein**, wenn KE2 nach Plan nicht eingetroffen ist oder KE1 nach Plan "nicht eingetroffen (gerader Anteil
    quadratisch)" ist;
  - **offen** sonst.
  - Lesart [M, S2]: "an der Neuvernetzung" heisst hier "an den frisch gebauten Netzen der verformten Kugel", nicht
    "an den Umschaltspruengen der Paarung"; diese verschieben den Mittelwert nicht.
  - Lesart [H, S4]: "(b) glatt" heisst nicht "(b) Einstein"; dafuer sind KE3 und KE4 da, und die Scherprognose sagt fuer
    beide "nicht eingetroffen" voraus.

## 8. Kontrollen (Schwellen vor dem Lauf; Rauchwerte .69)

- **C1 (sigma = 0, N = 1000, Saat 991):** (a) und (b) gleich Gamma_Q(rund) <= 1e-8, 0 neue bzw. umgeklappte Simplizes.
  Rauch: -6,8e-13 und -6,8e-13; 0; 0 [E].
- **C2 (Moebius):** (a) netzgleich, (a) - (b) <= 1e-8. Rauch: gleich, -4,1e-12 [E].
- **C3 (Codepfad, Saat 0, N = 1000):** rund Q und (a) K-0,1 QI bitgleich mit kv2 (live) und mit der Laufdatei von
  KOVARIANZ-KUGEL-1; (a) K+0,05 bitgleich mit kv2. Rauch: alle bitgleich [E].
- **C4 (LU gegen dicht fuer (b), N = 400, Saat 990, K-0,1, K+0,05, D0,5):** <= 1e-8. Rauch: <= 2,8e-13, mit 1 bzw. 27
  umgeklappten Simplizes [E].
- **C5 (Negativprobe Umklappen):** drei Simplizes mit vertauschten Ecken werden als 3 umgeklappte erkannt, V_g < 0 bei 3,
  Gamma unveraendert. Rauch: 3, 3, -6,8e-13 [E].
- **C6:** eps = +0,1 nicht baubar (profil_min < 0). Rauch: -0,114 [E].
- **C7:** Umklappzahlen je Amplitude (Abschnitt 1, S7).
- **In jedem Netz:** Transportrest <= 1e-10, Huellenpruefungen (a), LU (a) und (b), Profil.

## 9. Kartenpunkte (vor dem Rechnen offengelegt)

- **[K1] KE1 "dasselbe Vorzeichen (nicht glatt)":** Der Klammerschluss gilt nicht allein: Eine glatte gerade Antwort hat
  ebenfalls dasselbe Vorzeichen (VORAB Abschnitt 2). Der Karte nach wird das Vorzeichen geurteilt; der Plan verlangt
  zusaetzlich eine Steigung des geraden Anteils klar unter 1,7. Diese Zusatzvorgabe ist eine Festlegung des Agenten,
  nicht der Karte.
- **[K2] KE0 Teil 2 vorab bestimmt:** M ist in (a) und (b) dasselbe und schon gemessen (-8,9 SE bei 120 Saaten).
  Erwartet "nicht eingetroffen"; KE0 ist damit im Wortlaut fast sicher verfehlt, ohne dass etwas Neues schiefgeht.
  Teil 1 ist eine Codepruefung (bitgleich).
- **[K3] KE3/KE4 auf e = 0,05 und in y:** Die Karte nennt keine Amplitude; gewaehlt ist die groesste baubare
  symmetrische (bestes Signal-Rausch-Verhaeltnis); 0,0125 und 0,025 als Zusatzzeilen. N-Unabhaengigkeit in
  y = Delta Gamma/sqrt(N), weil die Einstein-Vorhersage in y von N unabhaengig ist (in Delta Gamma waechst sie wie
  sqrt(N)). "Unter 15 % bzw. 2 SE" als "oder" gelesen wie bei KOVARIANZ-2D-GEGENPROBE (KG2).
- **[K4] eps = +0,1 nicht baubar (S1):** Bei abs(eps) = 0,1 gibt es nur die einseitige Antwort; gerader und ungerader
  Anteil nur bei 0,025 und 0,05 (und 0,0125 in (b)). Die Karten-Steigung ist damit eine Zweipunktsteigung.
- **[K5] Zusaetze ueber die Karte hinaus (beschreibend, keine Urteile):** +-0,0125 und D(0,25), D(0,5) in (b); (a) ohne
  M (in (a) und (b) gleich, C2).
- **[K6] Umklappen in (b):** mit |V_g| gerechnet und gezaehlt, nicht ausgeschlossen (Abschnitt 2); bei abs(eps) <= 0,025
  erwartet keines.
- **[K7] Scherprognose:** Sie sagt fuer (b) "glatt, aber nicht N-unabhaengig und nicht Einstein" voraus (VORAB
  Abschnitt 3). Das ist eine Hypothese des Agenten mit Schranken (c zwischen 0 und 1/16), keine Kartenaussage.

## 10. Agenten-Vorhersagen (nach Kontrolle und Rauchlauf, vor den Hauptlaeufen; ohne Kenntnis von Messwerten)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Tore (a) und (b) bestanden ohne Ausschluss | 90 % |
| A2 | KE0 Teil 1 (Reproduktion) eingetroffen | 97 % |
| A3 | KE0 Teil 2 (Moebius innerhalb 3 SE) eingetroffen | 10 % |
| A4 | KE1 nach Karte eingetroffen | 75 % |
| A5 | KE1 nach Plan eingetroffen | 50 % |
| A6 | KE2 nach Karte eingetroffen | 75 % |
| A7 | KE2 nach Plan eingetroffen | 60 % |
| A8 | KE3 eingetroffen | 15 % |
| A9 | KE4 nach Karte eingetroffen | 10 % |
| A10 | G_b(0,05) > 0 (Punktschaetzer; Scherterm groesser als Einstein) | 75 % |
| A11 | y_D > 0 fuer beide kappa (Scherkontrolle) | 90 % |

## 11. Rauchlaeufe und Kontrolle (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC)

- **vorab** (15:24:56 bis 15:25:03, cpu, rc 0): VORAB.md.
- **kontrolle** (15:25:09 bis 15:25:54, cpu, rc 0): C1 bis C7 wie Abschnitt 8.
- **rauch-b** (15:25:54 bis 15:28:55, cpu, rc 0): N = 4000, Saaten 900, 901, blind; alle Netze gueltig; 90 s je Saat; RSS
  433 MB.
- **rauch-a** (15:27:39 bis 15:30:00, cpu4, rc 0): N = 1000, 2000, Saaten 900 bis 902, blind; alle gueltig; 14 / 33 s je
  Saat. Ein erster Startversuch um 15:25 lief wegen eines cd-Fehlers im Befehl nicht an (keine Datei erzeugt).
- **Blindheit geprueft (jq):** In rauch-a.json und rauch-b.json hat kein Objekt ein Feld gamma oder gamma_M.
- **Codeprobe** (15:31:25 bis 15:36:11 UTC, cpu und cpu4, rc 0): nicht blind auf N = 200, 300, 400, Saaten 950 bis 971,
  dann Auswertung mit Haupt-N 200, 300, 400; nur Struktur geprueft (jq keys: Tor 22/22/22, Urteile KE0 bis KE4 mit allen
  Feldern, Steigungen, Scherkontrolle). Werte und Urteile der Probe nicht gelesen.
  - Zwei Fehlversuche der Probe-Auswertung: (1) Argumente vertauscht: Die Ausgabe ging als Datei
    runde41-kovarianz-kugel/lauf.tmp in den fremden Ordner (Abbruch beim Umbenennen, rc 1). Ich habe sie sofort in meinen
    Ordner verschoben (rauch/probe/probe-aw-irrlauf-lauf.tmp, Inhalt ungelesen); dessen lauf/ ist unveraendert
    (38 von 38 Pruefsummen gleich). (2) Probedateien hiessen nicht messung-*.json (Tor 0/0/0); Kopien in rauch/probe2/.
- **Codeaenderung nach Rauchlauf, vor dem Einfrieren:** nur der Vergleichswert der Scherprobe in vorab_daten
  (48 mal 96/140 statt 48/140; mein Rechenfehler beim S^4-Mittel von sin^4), ohne Wirkung auf Messung und Urteile.
- **Zeitfolge der Festlegungen:** Bauweisen, Amplituden (einschliesslich der Zusaetze), Behandlung des Umklappens,
  Messgroessen, Tor und alle Urteilsregeln standen vor der Kontrolle im Code (17:24 CEST); nach Kontrolle und Rauchlauf
  festgelegt: Saatzahl und Laufaufteilung (aus den Zeiten), Agenten-Vorhersagen, Text.
