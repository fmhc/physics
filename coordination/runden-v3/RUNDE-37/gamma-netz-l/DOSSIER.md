# GAMMA-NETZ-L: Dossier. Lenkt Finns Netz Licht richtig ab, und was legt gamma (PPN) im Netz fest? (Runde 43)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-04 19:33:05 CEST. Unterbrochen durch ein Sitzungslimit nach
  19:51:49 CEST (letzte eigene date-Messung), laut Leitung gegen 19:53; fortgesetzt 21:35:52 CEST. Text dieser Datei ab
  21:42:58 CEST (alles date). Zeitbox: Abschnitt 13.
- Arbeitsdatei: ARBEITSFELD.md (Erwartung mit date-Zeit vor jedem Abruf, Ausgang, Gegensweep, Rueckfragen).
- **Abrufe: 8 von 8**, alle arXiv-API, einer davon leer (Selbstanzeige 1). Kopien in quellen/ (F1 bis F7; die leere F1a-Antwort hatte denselben Dateinamen und wurde vom Wiederholungsabruf ueberschrieben). Keine Websuche.
- Code nur gelesen: RUNDE-37/eine-welt-loch-1/code/ew.py (Zeilen unten als "ew.py Z."), dazu nachtrag-69/kinetik.json per
  jq. Nichts ausgefuehrt, kein python/awk/perl.
- Kennzeichen: [S] an der Quelle gelesen (Z. = Zeile der lokalen Kopie), [S Abstract], [P] Projektdatei, [L] Gedaechtnis,
  [L?] unsicher, [M] eigene Mathematik bzw. Codelesung, [ES] eigener Schluss, [H] Hypothese.
- Art: Literatur, Code-Lesung, Schreibtisch. Keine Rechnung, keine Messdaten. Zahlen aus Projektlaeufen sind
  Gitterrechnungen.

## 1. Ergebnis zuerst

1. **Die "skalaren Regeln" sind der Form nach die diskrete Hamilton-Bedingung, aber ohne Quelle, ohne Takt und nicht
   erster Klasse [M, Codelesung; ES].**
   - In ew.py ist die Regel an Ecke v per Konstruktion c_v = - B w_v; w_v streckt alle Kanten an v um denselben
     Bruchteil (ew.py Z. 219-228). Damit gilt c_v . a = Summe ueber Kanten e an v von l_e delta eps_e (Z. 6-7, 168).
   - Das ist die Ableitung der Regge-Wirkung nach einer Eck-Skalierung, also die eckweise Skalarkruemmung
     delta R^(3); gleich null gesetzt ist es die linearisierte Hamilton-Bedingung des Vakuums bei Zeitsymmetrie [ES].
   - Ueber die symmetrische Reduktion wirkt dieselbe Regel auch auf die Impulse, dort als Eichwahl (Gegenstueck von
     maximalem Slicing) [ES].
   - Schon im flachen Netz ist sie nicht erster Klasse: Spur-Eichdefekt Median 0,91 [P].
2. **Mit Quelle und Takt folgt gamma ohne Rechnung [ES, Schreibtisch].**
   - Statisch ist der Raum exakt eine Eck-Skalierung durch den Takt: a = -(kappa'/kappa_g) W mu plus Eichung. Daraus
     gamma = 2 kappa'/kappa_g.
   - Ein einziges Hamilton aus eckgewichteten Energien (Regge-Anteil und Materie im selben Takt) gibt
     kappa' = kappa_g/2, also gamma = 1 an jeder Ecke.
   - Das gilt unabhaengig von Bewegungsenergie, Paarung R1/R2, Fuellung V oder S und der 1/2.
3. **Im kovarianten 4D-Regge-Netz ist gamma schon gerechnet [P].** REGGE-ZEIT-1 und REGGE-4D-SCHIEF-1 geben gamma -> 1
   im Fernfeld; nahe der Masse geht (gamma - 1) r^2 je nach Achse gegen -1,1 bis +2,2 (r in Gitterabstaenden). Fuer
   Cassini reicht danach jede Gitterweite unter einigen 1e3 km (Abschn. 5.2) [ES, Ueberschlag]. Ein messrelevanter Rechenrest fuer gamma
   bleibt nicht. Offen ist eine Modellfrage an Finn (R1): Steckt die Energie in der Regel je Ecke, und tickt die Materie
   im Takt der Ecke?
4. **Groesster Literatur-Verstoss: Im fluktuierenden Regge-Netz ist das statische Potential Yukawa-artig.** Langreichweitig
   ist es nur am kritischen Punkt (Hamber/Williams 1995 [S Abstract]); spaeter deuten sie es als kovariant laufendes G
   (2007 [S Abstract]). Fuer ein zitterndes Netz ist die erste Huerde die Reichweite, nicht gamma.
5. **Gegensweep: Bindend ist die Spin-2-Ausbreitung, nicht gamma.**
   - Langwellig sind die zwei TT-Zweige auf dem gefuellten Netz richtungs- und polarisationsabhaengig, in allen fuenf
     ausgelesenen Bewegungs-Festlegungen um 3,2 bis 10,6 % in omega^2/k^2 [P, Quotienten von Hand].
   - Licht als Vektorfeld waere dort isotrop [M]. Der Anker ist c_T/c - 1 in [-3e-15; 7e-16] [P].
6. **Dimensionsvergleich [M, ES; P].**
   - In 2+1 ist die Regge-Wirkung konstant (B = 0); die Regel je Ecke ist dann der Fehlwinkel selbst (Kegel). Licht wird
     abgelenkt, eine Newton-Kraft gibt es nicht; gamma = 1/(D - 3) ist dort nicht endlich.
   - Erst in 3+1 koppelt B den Takt an die Raumskalierung (Faktor d - 2 = 1).

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

| Nr | Erwartet | Gefunden | Beleg | Folge |
|---|---|---|---|---|
| V1 | Karte: gamma auf dem Netz ist eine offene Rechenfrage (Fragen 2 und 4) | **Schon gerechnet und ableitbar.** 4D-Regge-Netze: gamma -> 1 im Fernfeld, (a/r)^2 nahe der Masse. Hamilton-Netz: gamma = 2 kappa'/kappa_g aus der Gitteridentitaet c = - B W | REGGE-ZEIT-1 Abschn. 1, REGGE-4D-SCHIEF-1 Abschn. 1 und 3.3 [P]; ew.py Z. 219-228 [M] | Kein gamma-Lauf mit Messbezug; Rueckfrage R2 (Projektstand der Karte unvollstaendig) |
| V2 | F6: Hamber/Williams finden ein anziehendes, Newton-artiges ~1/r im glatten Bereich | **Yukawa-artig**, Masse -> 0 nur am kritischen Punkt; Grund: "non-linear graviton interactions" | Hamber/Williams 1995 [S Abstract] | Zweites Regime (fluktuierend); dort gefaehrdet die Reichweite, und bei Fierz-Pauli-artiger Masse gaebe vDVZ gamma = 1/2 |
| V3 | Karte, Frage 1: Regel = Hamilton-Bedingung **oder** Eichfixierung **oder** anderes; E2: nicht erster Klasse erst auf gekruemmtem Hintergrund | **Beides zugleich**, als Paar zweiter Klasse: auf a die Hamilton-Bedingung (ohne Quelle), auf p eine Eichwahl. Nicht erster Klasse **schon flach**, weil die Bewegungsenergie gesetzt und nicht aus einer 4D-Wirkung abgeleitet ist | ew.py Z. 253-259, 311-318, 397-401 [M]; ERGEBNIS Abschn. 4 (Defekt 0,91) [P] | Fuer gamma folgenlos (Statik braucht A nicht); fuer Finns "Umbauten = Umbenennungen" nicht folgenlos (Abschn. 6.4) |
| V4 | Selbstverstaendlich: gamma ist der bindende Anker fuer "Netz = Raum" | **Die Spin-2-Ausbreitung bindet staerker**: TT-Tempo langwellig anisotrop um 3,2 bis 10,6 %, gegen 1e-15 | kinetik.json [P]; STRANG-ANKER-L Z. 24, 81 [P] | Offene Frage O1 |
| V5 | E3: gelueckte Moden wirken wie massive Brans-Dicke-Skalare, gamma - 1 ~ e^(-m r) | Im Hamilton-Netz sind es gebundene Eck-Skalierungen, die in Phi und Psi gleich eingehen: Sie aendern G(r) auf Gitterreichweite, nicht gamma. Im 4D-Regge ist die Nahabweichung auf den Achsen meist **gamma > 1**, ein gesunder Skalar gibt gamma < 1 | Abschn. 5.2 [ES]; REGGE-ZEIT-1, -SCHIEF-1 [P]; Will 2014 Z. 1807-1809 [S] | Die Brans-Dicke-Analogie traegt nicht |
| V6 | klein: F2 findet Hamber/Williams; F4-Abstract nennt gamma(r) | Suchwort "Regge" traf Regge-Wheeler (F2); Formel nicht im Abstract (F4) | quellen/F2, F4 | Suchdesign; Vorzeichen ueber Will 2014 lokal belegt |

## 3. Pruefung des Schreibtischs der Leitung

| Punkt (Karte Z. 18-22) | Urteil | Begruendung |
|---|---|---|
| 1. Gelueckte Skalare geben nur Yukawa ~ e^(-m r); langwellig bestimmt die Hamilton-Bedingung gamma | **im Ergebnis richtig, Begruendung zu schaerfen** | Statik braucht die Bewegungsenergie A nicht; massgeblich ist die Steifigkeit von B auf den harten Richtungen, nicht die Luecke omega^2 = 3,43 von A B [M]. Die harten Eck-Skalierungen (9 bei V, 5 bei S, ERGEBNIS Abschn. 1.3 [P]) stecken im Takt mu und damit in Phi und Psi gleich; sie aendern G(r) nahe der Masse, gamma nicht [ES]. Langreichweitig bleibt die weiche Spurmode (Signatur -, +, +, ERGEBNIS Abschn. 3 [P]) |
| 2. gamma = 1 verlangt: Regel = diskrete Hamilton-Bedingung und Lapse aus derselben Kopplung | **richtig, und praeziser: gamma = 2 kappa'/kappa_g** | Erste Haelfte gilt in ew.py per Konstruktion (c = - B W) [M]. Zweite Haelfte heisst: Der Multiplikator der Regel ist zugleich das Gewicht der Regge-Energie und der Takt der Materie (ein Hamilton). Dann kappa' = kappa_g/2 [ES]. Nicht noetig: die 1/2, erste Klasse, die Wahl von A (TAKT-UMBENENNUNG-L: gesundes Horava hat lambda != 1 und gamma = 1 [P]) |
| 3. Ist die Regel etwas anderes, kann gamma von 1 abweichen | **richtig; vier Wege benennbar** | (i) Gewichte der Regel nicht die Eck-Skalierungs-Ableitung desselben B: Raumantwort nicht mehr rein konform, gamma != 1 und richtungsabhaengig moeglich [ES]. (ii) kappa' != kappa_g/2: gamma = 2 kappa'/kappa_g auf allen Abstaenden [ES]. (iii) Regel nur global (ein Takt je Schicht): keine lokale Hamilton-Bedingung, Schwerkraft im Shift (Mukohyama 2009/2010 [P]). (iv) Licht spuert nur den Takt: halbe Ablenkung (SCHREIBTISCH-QBALL-EIS-LAPSE [P]; Will 2014 Z. 2172 [S]) |

## 4. Erwartungen mit Ausgang

| Nr | Erwartung (Karte bzw. ARBEITSFELD, vor dem Abruf) | Ausgang | Beleg |
|---|---|---|---|
| E1 | Linearisiertes Regge gibt im Kontinuum die linearisierte ART samt Propagator (Rocek/Williams) | **eingetroffen, ohne Abruf** | GRAVITON-NETZ-L E2 (Regge/Williams 2000, S. 4-5 [S sekundaer]); REGGE-4D-1; REGGE-4D-SCHIEF-1: c0s/c2 = -1,9989 bis -2,0047 [P] |
| E2 | Hamilton-Regge mit Zwangsbedingungen je Ecke existiert; nicht exakt erster Klasse auf gekruemmtem Hintergrund | **fuer 4D-Regge eingetroffen, ohne Abruf; fuer ew.py in der Schaerfe verletzt (V3)** | TAKT-UMBENENNUNG-L: Bahr/Dittrich 2009 [S], Dittrich/Hoehn 2010 [S Abstract], 4D linear um flach exakt (Hoehn 2014) [P]; ew.py schon flach nicht erster Klasse [M, P] |
| E3 | Gelueckte Moden wie massive Brans-Dicke: gamma - 1 ~ e^(-m r) | **Form eingetroffen, Uebertragung auf Finns Netz verletzt (V5)** | Perivolaropoulos 2010 [S Abstract]: Schranken "relax for a field mass m >~ 20 x m_AU"; Will 2014 Z. 1807-1809 [S]: gamma = (1 + omega)/(2 + omega) |
| E4 | Fuer Gitter-Gravitonen ist gamma meist nicht berechnet; wo doch, haengt es an der Materiekopplung | **eingetroffen (nach Recherchestand)** | F5: keine Arbeit mit gamma [S Abstract]; GRAVITON-NETZ-L Regime B: Universalitaet nicht gezeigt, Quellen sind Ladungen; Carlip 2012: "ad hoc symmetry is the only known way to force universality" [P] |
| F1 | Glickenstein: konforme Variationen; Ableitung des Regge-Funktionals = Kruemmung je Ecke | **im Kern eingetroffen**; Formel nicht im Abstract | Glickenstein 2011 [S Abstract] |
| F2 | Regge + Ablenkung: wenige Treffer, Hamber/Williams | **teilweise verletzt (Suchdesign)** | 1 von 30 Treffern einschlaegig (Arrighi/Dowek 2015) |
| F3 | "Regge calculus" + Schwarzschild usw.: Konvergenz, Regge-Schwarzschild, kein gamma | **eingetroffen** | Khatsymovsky 2020, Miller 1995, Chakrabarti u. a. 1999 [S Abstract] |
| F4 | Perivolaropoulos: gamma(r) mit e^(-m r), gamma < 1 | **Form eingetroffen, Formel nicht pruefbar** | [S Abstract]; Ersatz Will 2014 lokal [S] |
| F5 | Emergente Gravitonen + PPN: kein gamma | **eingetroffen** | 2 Treffer, ohne gamma [S Abstract] |
| F6 | Hamber/Williams 1995: ~1/r im glatten Bereich | **verletzt (V2)** | [S Abstract] |
| F7 | Hamber/Williams spaeter: kovariant, laufendes G, statisch isotrop | **eingetroffen**; gamma nicht im Abstract | Hamber/Williams 2007 [S Abstract] |

## 5. Antworten 1 bis 4

### 5.1 Frage 1: Was sind die "skalaren Regeln"?

- **Konstruktion [M, Codelesung]:**
  - ew.py Z. 221-227: crow_v = - Summe_{e an v} (Bloch-Phase) B[e, :]; Z. 228: c = crow^dagger, "c_v^dagger a =
    crow_v . a".
  - Das heisst c_v = - B w_v. Dabei ist w_v die Eck-Skalierung: a_e = 1 fuer jede Kante an v (Phase fuer die Nachbarzelle).
  - B = l (Summe_t d theta_t/d l) l (Z. 6, 168), mit eps_e = 2 pi - Summe_t theta_t,e (Diedersumme 2 pi, Z. 279-283).
    Daraus (B a)_e = - l_e delta eps_e und c_v^dagger a = Summe_{e an v} l_e delta eps_e, wie im Docstring Z. 7.
- **Bedeutung [ES]:**
  - Die Regel ist die Euler-Lagrange-Gleichung der linearisierten 3D-Regge-Wirkung (Summe l_e eps_e) fuer eine
    konforme Eck-Skalierung l_e -> l_e (1 + phi_v + phi_w).
  - Konforme Variationen des Regge-Funktionals sind ein eingefuehrter Begriff; ihre Kruemmungsableitungen "resemble the
    formulas for the change of scalar curvature under a conformal variation" (Glickenstein 2011 [S Abstract]). Die Formel
    Summe l_e eps_e je Ecke steht nicht im Abstract.
  - Im Kontinuum ist die konforme Ableitung von Int sqrt(h) R in d Raumdimensionen (d - 2) sqrt(h) R [M]. Fuer d = 3 ist
    die Regel also delta R^(3) = 0 je Ecke. Das ist die linearisierte Hamilton-Bedingung des Vakuums um flach, weil die
    Impulsterme quadratisch sind [L, ADM].
- **Rolle im Werkzeug [M, Codelesung; ES]:**
  - Die Zwangsflaeche ist das Komplement von Bild [M, c] (Z. 253-259); a und p werden gleich reduziert (Z. 316-318).
  - Auf a wirkt das als M^dagger a = 0 (Eichwahl) und c^dagger a = 0 (Hamilton-Bedingung ohne Quelle).
  - Auf p wirkt es als M^dagger p = 0 (Impulsbedingung) und c^dagger p = 0. Das Letzte ist im Kontinuum
    d_i d_j pi_ij - Lap pi = 0, mit der Impulsbedingung also tr pi = 0: maximales Slicing [ES, Kontinuumsanalogie].
  - Z. 397-401 ("Spur-Eichdefekt") prueft, ob A c_v im Bild von M liegt, also ob der Fluss der Regel nur Ecken
    verschiebt. Nur dann bleibt c^dagger a = 0 unter der Bewegung erhalten (erster Klasse) [M]. Gemessen: Median 0,91,
    max 0,98 auf L = 16 [P]. Die Regel ist also mit der gesetzten Bewegungsenergie zweiter Klasse.
  - Im Kontinuum macht genau die DeWitt-1/2 den Fluss zur Umbenennung: delta pi_ij = (d_i d_j - delta_ij Lap) N gibt
    delta hdot_ij = d_i d_j N [M]. Das deckt sich mit "1/2 als Passbedingung" (TAKT-UMBENENNUNG-L [P]).
- **Antwort:** Weder reine Hamilton-Bedingung noch reine Eichfixierung, sondern ein Paar zweiter Klasse. Seine
  Konfigurationshaelfte ist die diskrete linearisierte Hamilton-Bedingung des Vakuums (ohne Quelle, ohne Takt), seine
  Impulshaelfte eine Eichwahl. Es ist von Hand gesetzt und nicht aus einer 4D-Wirkung abgeleitet.
- **Folge fuer die Stabilitaet [M, P]:** B hat auf dem eichfreien Raum bei kleinem k so viele negative Richtungen wie
  Ecken (V 10, S 6), und auf der Zwangsflaeche keine [P]. Die Zwangsflaeche ist das B-orthogonale Komplement der
  Eck-Skalierungen. Nach der Traegheitsadditivitaet (Haynsworth [L]) ist W^dagger B W dann negativ definit [M].
  - Die Lesart [H] im ERGEBNIS ("negative Richtungen = oertliche Umskalierungen") ist damit strukturell gestuetzt, fuer
    kleine k.
  - Dieselbe Negativitaet macht unten die Takt-Gleichung anziehend.

### 5.2 Frage 2: Folgt gamma = 1 vorab?

- **Statik im Hamilton-Netz [ES, Schreibtisch]:**
  - H = - kappa_g S_Regge + Summe_v mu_v (- kappa' c_v^dagger a + m_v) + ...; dabei ist mu_v die Abweichung des Takts von 1
    an Ecke v und m_v die Ruheenergie dort. Fuer p = 0 faellt A heraus.
  - Aus dH/da = 0 folgt kappa_g B a = kappa' C mu = - kappa' B W mu, also a = -(kappa'/kappa_g) W mu plus Eichung.
    Das ist exakt, weil B auf dem eichfreien Raum bei k != 0 keinen Nullraum hat: Sonst haette B_phys einen Nullwert,
    gemessen ist B_phys an allen 4 095 k positiv [P].
  - Aus dH/dmu = 0 folgt die Hamilton-Bedingung mit Quelle: kappa' c^dagger a = m, also
    (-W^dagger B W) mu = -(kappa_g/kappa'^2) m. Das ist eine Poisson-Gleichung (Kontinuum: (-Lap) Phi = -4 pi G rho); ihr
    Operator -W^dagger B W ist bei kleinem k positiv definit (5.1). Damit ist mu < 0 nahe der
    Masse: Uhren gehen langsamer, ruhende Testmassen (Energie (1 + mu) m) werden angezogen.
  - Raum: delta l/l = -(kappa'/kappa_g)(mu_1 + mu_2), langwellig -2 (kappa'/kappa_g) Phi. Mit (1 - 2 Psi) folgt
    gamma = Psi/Phi = 2 kappa'/kappa_g.
  - Ein Hamilton aus eckgewichteten Energien (S_N = Summe_e N_e l_e eps_e mit N_e = Mittel der Eck-Takte, Materie mit
    demselben Takt) gibt kappa' = kappa_g/2, also gamma = 1. Weil die Raumantwort exakt eine Eck-Skalierung ist, gilt
    das an jeder Ecke (mit gamma ueber die Eck-Skalierung definiert).
- **Kontinuumsprobe [M]:** delta G_ij[2 phi delta] = -(d_i d_j - delta_ij Lap) phi in d = 3. Die statische
  Impulsgleichung delta G_ij[h] + delta G_ij[2 Phi delta] = 0 gibt h = -2 Phi delta, also Psi = Phi.
- **Was die Formel nicht braucht (Regel 6, Kopplung vor Bauteil):** Fuenf verschiedene Wege geben gamma = 1, und allen
  gemeinsam ist dieselbe Kopplungsgroesse: eine lokale Hamilton-Bedingung mit Energie als Quelle, deren Multiplikator
  der Takt ist (kappa'/kappa_g = 1/2).
  - Die fuenf Wege: ART; gesundes Horava mit lambda != 1 (BPS 2011 [P]); 4D-Regge (REGGE-ZEIT-1 [P]); dieses
    Hamilton-Netz [ES]; Einstein-Aether [L].
  - Nicht gebraucht werden die 1/2, die erste Klasse, die Bewegungsenergie und die Fuellung.
- **4D-Regge-Netz (Zeltstangen) [P]:**
  - REGGE-ZEIT-1 (Kuhn): Masse koppelt ueber Eigenzeit an die Zeitkanten. gamma = 1,087 (r = 6), 1,023 (r = 10),
    1,014 (r = 14), etwa 1 + 2,2/r^2; L = 64 bei r = 24: 1,0038. Diagonale kinematisch 0,82 bis 0,95. "gamma = 1 im
    Fernfeld war nach REGGE-4D-1 vorab erwartbar."
  - REGGE-4D-SCHIEF-1: gamma(6) = 1,056 / 1,308 / 1,113 je Achse; Schwanz (gamma - 1) r^2 -> +1,65 / +1,65 / -1,1.
  - Fuer Finns gefuelltes Netz ist das nicht gerechnet. Das Fernfeld folgt aber aus Einsteins Langwellenform (E1).
- **Rechenbarer Rest:** Nur die Nahzone. Das sind Koeffizient und Anisotropie von (gamma - 1)(r/a)^2 bei
  kruemmungsbasierter Definition, G(r) und die Yukawa-Reichweiten der gestaffelten Takt-Moden.
  - Ueberschlag [ES, von Hand, mit Koeffizienten anderer Gitter]: Cassini mit naechstem Abstand 1,6 R_sun (Will Z.
    2363-2364 [S]) und |gamma - 1| <~ 5e-5 verlangt bei C = 2 bis 11 etwa a <~ 2e3 bis 5e3 km.
  - Ohne Messbezug, solange das Netz mikroskopisch ist.
- **Nicht ableitbar und keine Rechnung:** ob Finns Bild die Energie in die Regel je Ecke legt und die Materie im Takt der
  Ecke ticken laesst (R1). Davon haengt gamma ab.

### 5.3 Frage 3: Literatur zu gamma und statischer Antwort in Regge- und Gitter-Gravitation

| Arbeit | Was sie rechnet | gamma? | Kennz. |
|---|---|---|---|
| Khatsymovsky 2019, 2020 | Schwarzschild-Problem im Regge-Kalkuel, Finite-Differenzen-EH; "at large distances is close to the continuum Schwarzschild geometry", Zentrum auf Elementarlaenge abgeschnitten | indirekt (Fernfeld = Schwarzschild), nicht explizit | [S Abstract] |
| Hamber/Williams 1995 | Potential zweier schwerer Massen aus Wilson-Linien im Quanten-Regge; schwaches Feld gibt Newton; im glatten Bereich Yukawa-artig, Masse -> 0 am kritischen Punkt | nein | [S Abstract] |
| Hamber/Williams 2007 | Korrekturen zur statischen isotropen Loesung, langsam mit dem Abstand wachsendes G, kovariante nichtlokale Feldgleichungen | nicht im Abstract | [S Abstract] |
| Miller 1995 | Konvergenz: einzelne Regge-Gleichungen ~ a^2, Mittel ~ a^3, numerisch a^4 | nein | [S Abstract] |
| Chakrabarti/Gentle/Kheyfets/Miller 1999 | Geodaetenabweichung; Fehlwinkel ueber ein Flaechenelement summiert = Kontinuumskruemmung | nein (Grundlage fuer Fehlwinkel-Definitionen) | [S Abstract] |
| Arrighi/Dowek 2015 | diskrete Geodaeten, Periheldrehung in vorgegebener diskretisierter Raumzeit | nein | [S Abstract] |
| EDT (Dai u. a. 2021) | Bindungsenergie "compatible with ... Newton's potential" im Kontinuumslimes | nein | [P, GRAVITON-NETZ-L] |
| BPS 2011, Mukohyama 2009/2010 | bevorzugte Zeit: gesund gamma = beta = 1; projizierbar ohne lokale Hamilton-Bedingung, Staub als Integrationskonstante | ja (Kontinuum) | [P, TAKT-UMBENENNUNG-L] |
| Projekt: REGGE-ZEIT-1, REGGE-4D-SCHIEF-1 | gamma(r) einer ruhenden Masse im linearisierten 4D-Regge | ja | [P] |

- Nach Recherchestand (drei API-Suchen) berechnet keine gefundene Arbeit gamma bzw. die Lichtablenkung fuer ein Regge-
  oder Gitter-Graviton; die einzigen expliziten gamma(r) auf Regge-Netzen, die ich kenne, sind die zwei Projektlaeufe.
- Williams/Ellis ("Regge calculus and observations", 1981/1984) sollen Bahnen und Lichtablenkung im Regge-Schwarzschild
  gerechnet haben [L?]; nicht auf arXiv, nicht geprueft.

### 5.4 Frage 4: Rechenkarte

Abschnitt 8 (ein Vorschlag mit Ableitbarkeitsprobe; Empfehlung: niedrige Prioritaet).

## 6. Regime, Moderatoren, Unterscheidungspunkte, Dimensionsvergleich

### 6.1 Regime (Regel 1)

| Regime | Zeit kommt aus | Regel je Ecke | gamma | Beleg |
|---|---|---|---|---|
| H: Hamilton-Gitter (ew.py) | von Hand gesetzte Bewegungsenergie | zweiter Klasse, ohne Quelle | 2 kappa'/kappa_g; = 1 bei einem Hamilton | [M, ES] |
| K: kovariantes 4D-Regge mit Zeltstangen (PACHNER-TAKT-1, REGGE-ZEIT-1) | 4D-Wirkung; Zeltstange = Takt je Ecke, flach exakte Eichung | Teil der 4 Eckverschiebungen | -> 1, Nahzone (a/r)^2 | [P] |
| Q: fluktuierendes Netz (Quanten-Regge) | Pfadintegral | wie K, nichtlinear | Potential Yukawa-artig; 1/r nur am kritischen Punkt | Hamber/Williams 1995, 2007 [S Abstract] |
| P: globaler Takt (projizierbar) | ein Takt je Schicht | nur integriert | Schwerkraft im Shift; lambda in der Statik | Mukohyama 2009/2010, BPS 2011 [P] |

- Moderatoren:
  - Herkunft der Zeit (4D-Wirkung oder gesetzt), trennt H und K.
  - Ort der Regel (je Ecke oder je Schicht), trennt H/K und P.
  - Fluktuationsstaerke (Abstand zum kritischen Punkt, bei Finns Netz etwa die Temperatur wie in FLUSS-1), trennt K
    und Q.
  - Universalitaet der Kopplung (kappa'/kappa_g; Licht spuert Laenge und Takt), wirkt in allen Regimen.

### 6.2 Unterscheidungspunkte (Regel 2)

| Paar | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|
| H gegen K | nur nahe der Masse, r ~ wenige a: H (Eck-Definition) genau 2 kappa'/kappa_g, K 1 + 2,2 (a/r)^2 | nein fuer mikroskopisches a. **Empirisch nicht unterscheidbar.** |
| kappa' = kappa_g/2 gegen kappa' != kappa_g/2 | auf allen Abstaenden: gamma = 2 kappa'/kappa_g | ja: Cassini, abs(2 kappa'/kappa_g - 1) <~ 5e-5 |
| je Ecke gegen global (H/K gegen P) | lokales Newton-Potential im Takt gegen Shift; Staub-artige Integrationskonstante | ja, ueber Dunkle-Materie-artige Effekte und lambda in der Statik [P] |
| K gegen Q | r ~ xi (Korrelationslaenge): exponentieller Abfall | nur wenn xi nicht kosmologisch ist |
| Q mit Fierz-Pauli-artiger Masse gegen Q mit kovariant laufendem G | bei r << xi: vDVZ gamma = 1/2 gegen gamma = 1 | ja: Cassini schliesst gamma = 1/2 aus (3/4-Ablenkung, GEGENLESEN-R35 B7 [P]) |
| Licht spuert nur den Takt gegen Laenge und Takt | Ablenkung halb gegen voll | ja, gemessen: voll (Will Z. 2172 [S]) |

### 6.3 Dimensionsvergleich 3+1 gegen 2+1

- In d Raumdimensionen ist die konforme Ableitung von Int sqrt(h) R gleich (d - 2) sqrt(h) R [M]. Linear gilt
  gamma_D = 1/(D - 3) = 1/(d - 2) (STRANG-ANKER-L [ES dort]; Kontinuumsprobe 5.2 mit d - 2 statt 1 [M]).
- **2+1:**
  - Die Regge-Wirkung der Flaeche ist Summe der Fehlwinkel = 2 pi chi, also konstant (Gauss-Bonnet), und B = 0 [M].
  - Die Konstruktion c = - B W ergaebe die Nullregel. Die Regel je Ecke muss deshalb der Fehlwinkel selbst sein: Kegel
    proportional zur Masse (Carlip 2005, "conical defects" [S, ueber GRAVITON-NETZ-L]; 8 pi G M [L]).
  - Die Takt-Gleichung (d_i d_j - delta_ij Lap) N = 0 laesst nur konstanten Takt zu: keine Newton-Kraft, wie Carlips
    "no good Newtonian limit" [P].
  - Licht wird am Kegel um einen festen Winkel abgelenkt [L]. Zaehlung auf dem Torus: E = 3V, minus 2V Eichung, minus V
    Regeln, gibt 0 Freiheitsgrade, keine Gravitonen [M].
- **3+1:** B != 0, die Regel folgt aus B (c = - B W), und B koppelt den Takt an die Raumskalierung. Ergebnis: Newton-Kraft
  plus gleich grosse Raumkruemmung, also gamma = 1 bei einer Kopplung. Gezaehlt sind 2 masselose TT-Moden [P].
- [ES] Dieselbe Zahl d - 2 entscheidet, ob die Regel aus der Wirkung folgt und wie stark Raum und Takt gekoppelt sind.

### 6.4 Bezug zu Finns Satz "der Raum ist das Netz"

- GEMEINSAMES-NETZ-L [P] nach Marolf 2015 [S dort]: Universelle nichtlineare Kopplung an die Energie verlangt, dass die
  Kantenlaengen eichredundante Geometrie sind, mit Zwangsbedingungen wie Regge oder CDT.
- [ES] In Regime K ist der Takt eine exakte Eichung (Zeltstange, flach). In Regime H ist die Regel zweiter Klasse; ein
  Umbau dort ist keine reine Umbenennung.
- Finns Satz passt damit zu K besser als zu H. Fuer gamma (linear) ist das ohne Folge, fuer beta und die Nichtlinearitaet
  nicht [ES].

## 7. Gegensweep (Regel 4)

| Nr | Selbstverstaendlich und nicht geprueft | Geprueft? | Befund |
|---|---|---|---|
| G1 | gamma ist der bindende Messanker | **ja**, an eine-welt-loch-1/nachtrag-69/kinetik.json (jq, Netz V, abs(k) = 1e-3 und 2e-3, Richtungen [100], [110], [111]) | omega^2/k^2 der TT-Zweige: A1-R1 0,11889 bis 0,12643; A1-R2 0,12325 bis 0,12714; A2-R1 0,14807 bis 0,15684; A3-R1 0,0052083 bis 0,0057584; A3-R2 0,0050477 bis 0,0052083 [P]. Spanne 6,3 / 3,2 / 5,9 / 10,6 / 3,2 % (von Hand). Auch A3-R2, in der ERGEBNIS-Tabelle (Abschn. 5) bei [100] gerundet "0,0052 / 0,0052", spaltet in [100] um 0,6 % und haengt von der Richtung ab ([111] 0,0050477). Licht (Rang 2) waere bei kubischer Symmetrie langwellig isotrop [M]. Gegen c_T 1e-15 [P] ist das die schaerfere Huerde. |
| G2 | Cassini misst die Ablenkung | **ja**, Will 2014 Z. 2352-2367 [S] | Gemessen ist die Laufzeit per Doppler (X- und Ka-Band), naechster Abstand 1,6 R_sun; "gamma - 1 = (2.1 +- 2.3) x 10^-5"; Skalar-Tensor "omega > 40,000". Ablenkung und Laufzeit haengen beide an (1 + gamma)/2 (Z. 2172, 2354). Aussage der Karte gilt sinngemaess. |
| G3 | Licht spuert Kantenlaenge und Takt | nein (kein Licht in ew.py) | offen (O2) |
| G4 | Vorzeichen und Normierung meiner Schreibtischformel | nur Kontinuumsprobe | Gitter offen (Abschn. 8) |
| G5 | Bloch-Phasen von c passen zu W | indirekt, [P] | cM_null <= 4,0e-15 (ERGEBNIS Abschn. 6) ist die notwendige Folge c^dagger M = - W^dagger B M = 0 |

## 8. Rechenkartenvorschlag (einer) mit Ableitbarkeitsprobe

**GAMMA-HAMILTON-1** (Kleintest-Spur, <= 10 min). Frage: Haelt gamma = 2 kappa'/kappa_g am echten Netz (V, S), und ist
der Takt-Operator -W^dagger B W an allen Gitter-k positiv?

- **Aufbau:**
  - ew.py unveraendert importieren (baue, ops); W aus kliste mit denselben Phasen wie crow.
  - Je Gitter-k (L = 16) das statische System [kappa_g B, -kappa' C; -kappa' C^dagger, 0] mit Eichwahl M^dagger a = 0
    loesen, kappa' = kappa_g/2; Punktquelle an einer Ecke je Untergitterart; Bloch-Summe in den Ortsraum.
- **Kennzahlen:**
  - K1: Rest von a + (kappa'/kappa_g) W mu ausserhalb von Bild M.
  - K2: Eigenwerte von -W^dagger B W an allen k.
  - K3: mu(r) r gegen r; Reichweiten der 9 (V) bzw. 5 (S) gestaffelten Takt-Moden.
  - K4: gamma aus Raum-Fehlwinkeln gegen Takt-Gefaelle (Vergleich mit REGGE-ZEIT-1).
- **Ableitbarkeitsprobe:**

| Kennzahl | vorab ableitbar? | Messbezug |
|---|---|---|
| K1 | ja, Identitaet aus c = - B W [M]: nur Kontrolle (<= 1e-12 erwartet) | keiner |
| gamma im Fernfeld | ja, 1 [ES] | Cassini, aber vorab bestimmt |
| K2 | nur bei kleinem k (Traegheit, [P] + [M]); sonst nicht | keiner (Stabilitaet der Statik) |
| K3, K4 | nein | keiner, solange a unter einigen 1e3 km liegt |

- **Latten:**
  - L1 (kann scheitern): ja, an K2 (indefinite Takt-Moden) und an K1, falls meine Codelesung falsch ist.
  - L4 (bekannt): Fernfeld [P, ES].
  - L5 (Messbezug): keiner.
- **Empfehlung:** nur als billige Kontrolle der Schreibtischformel, bevor sie in Texte geht. Wichtiger ist die offene
  Frage O1 (TT-Isotropie); das ist keine gamma-Frage und deshalb hier kein Kartenvorschlag.

## 9. Kalibrierung

- **(a) Gemessen:**
  - Cassini gamma - 1 = (2,1 +- 2,3)e-5 (Will 2014 Z. 2358-2359 [S]) und c_T/c - 1 in [-3e-15; 7e-16] [P].
  - Gitterrechnungen des Projekts (keine Messdaten): gamma(r) in REGGE-ZEIT-1/-SCHIEF-1; ERGEBNIS- und kinetik.json-Zahlen
    von EINE-WELT-LOCH-1.
- **(b) Nuetzlich verdichtet:** c = - B W (Codelesung, exakt); gamma = 2 kappa'/kappa_g (Schreibtisch); vier Regime H, K,
  Q, P mit Moderatoren; der Faktor d - 2.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:** Im Lauf der Recherche wuchs meine Sicherheit, dass gamma fuer Finns
  Netz "kein Problem" ist. Zugleich zerfiel die Frage in eine Modellfrage (R1) und eine Schreibtischformel, die am Gitter
  nicht gerechnet ist. **Das ist ein Warnzeichen**: Die Sicherheit stammt aus der Struktur, nicht aus einer neuen
  Messung oder Rechnung. Auch der Vorrang von c_T (V4) beruht auf Projektzahlen; ob andere Gewichte die Anisotropie
  beseitigen, ist offen.

## 10. Offene Fragen und Rueckfragen

- **R1 (an Finn, ueber die Leitung):** Steckt die Energie einer Masse in der Regel je Ecke (nicht ihre Ladung Q,
  vgl. SCHREIBTISCH-QBALL-EIS-LAPSE Folge 1 [P])? Und tickt die Materie im Takt dieser Ecke? Beides zusammen ist
  kappa' = kappa_g/2.
- **R2 (an die Leitung):** Der Projektstand der Karte nennt REGGE-ZEIT-1 und REGGE-4D-SCHIEF-1 nicht, obwohl beide gamma(r)
  schon rechnen (Ableitbarkeits- und Projekt-grep-Probe).
- **O1:** Gibt es Gewichte der Bewegungsenergie je Tetraeder-Art, bei denen beide TT-Zweige langwellig isotrop und
  entartet sind? Danach: gleich schnell wie Licht? LICHT-GLEICH-L sagt dazu: nur durch Abstimmen oder Symmetrie [P].
  Messanker c_T 1e-15.
- **O2:** Welches Feld ist Licht im Netz, und koppelt es an Laengen und Takt? Ohne Licht-Modell ist "lenkt es Licht
  richtig ab" nur bedingt beantwortet. Mit Takt allein waere es die halbe Ablenkung.
- **O3:** Zittert Finns Netz (FLUSS-1: Kraefte ~ Temperatur [P])? Dann gilt Regime Q: Reichweite ~ Korrelationslaenge,
  und eine Fierz-Pauli-artige Masse gaebe vDVZ, also gamma = 1/2.
- **O4:** Spur-Eichdefekt bei k -> 0 (ERGEBNIS: nicht gerechnet): Wird die Regel langwellig erster Klasse? Das betrifft
  Marolf und Finns "Umbauten = Umbenennungen", nicht gamma.
- **O5:** Ein Netz mit Ruhesystem verlangt auch die Vorzugssystem-Parameter alpha1 und alpha2: abs(alpha1) < 1e-4,
  abs(alpha2) < 4e-7 (nach Will, TAKT-UMBENENNUNG-L [P]). Hier nicht untersucht.

## 11. Quellenliste

- **Abrufe (arXiv-API, Kopien in quellen/):**
  - F1: Glickenstein, D. (2011): Discrete conformal variations and scalar curvature on piecewise flat two and three
    dimensional manifolds. J. Differential Geom. 87, 201-237. https://arxiv.org/abs/0906.1560 [S Abstract]
    (F1-api-glickenstein-conformal.xml).
  - F1: Champion, D.; Glickenstein, D.; Young, A. (2010): Regge's Einstein-Hilbert functional on the double tetrahedron.
    https://arxiv.org/abs/1007.0048 [S Abstract].
  - F2/F3: Arrighi, P.; Dowek, G. (2015): Discrete geodesics and cellular automata. https://arxiv.org/abs/1507.06836
    [S Abstract] (F2-api-regge-ablenkung-newton.xml, F3-api-regge-calculus-statik.xml).
  - F3: Khatsymovsky, V. M. (2020): On the discrete version of the Schwarzschild problem. Universe 6, 185.
    https://arxiv.org/abs/2008.13756 [S Abstract].
  - F3: Khatsymovsky, V. M. (2020): On the discrete version of the black hole solution. Int. J. Mod. Phys. A 35,
    2050058. https://arxiv.org/abs/1912.12626 [S Abstract].
  - F3: Miller, M. A. (1995): Regge calculus as a fourth order method in numerical relativity. Class. Quantum Grav. 12,
    3037-3052. https://arxiv.org/abs/gr-qc/9502044 [S Abstract].
  - F3: Chakrabarti, S.; Gentle, A. P.; Kheyfets, A.; Miller, W. A. (1999): Geodesic deviation in Regge calculus. Class.
    Quantum Grav. 16, 2381-2391. https://arxiv.org/abs/gr-qc/9810031 [S Abstract].
  - F4: Perivolaropoulos, L. (2010): PPN parameter gamma and solar system constraints of massive Brans-Dicke theories.
    Phys. Rev. D 81, 047501. https://arxiv.org/abs/0911.3401 [S Abstract] (F4-api-0911.3401.xml).
  - F5: Sexty, D.; Wetterich, C. (2012): Emergent gravity in two dimensions. https://arxiv.org/abs/1208.2168
    [S Abstract] (F5-api-emergent-graviton-ppn.xml; nur als Fehlanzeige fuer gamma).
  - F6: Hamber, H. W.; Williams, R. M. (1995): Newtonian potential in quantum Regge gravity. Nucl. Phys. B 435, 361-398.
    https://arxiv.org/abs/hep-th/9406163 [S Abstract] (F6-api-hep-th-9406163.xml).
  - F7: Hamber, H. W.; Williams, R. M. (2007): Renormalization group running of Newton's G: the static isotropic case.
    Phys. Rev. D 75, 084014. https://arxiv.org/abs/hep-th/0607228 [S Abstract] (F7-api-hamber-running-g.xml).
- **Lokal, ohne Abruf:** Will, C. M. (2014): The confrontation between general relativity and experiment. Living Rev.
  Relativ. 17, 4. https://arxiv.org/abs/1403.7377 (ID nach Projektdateien). Gelesen Z. 1800-1810 (Tab. 3), 1905,
- **Projekt [P]:**
  - RUNDE-37/eine-welt-loch-1/: ERGEBNIS.md, code/ew.py (Codelesung), nachtrag-69/kinetik.json (jq).
  - RUNDE-37/: regge-zeit-1/ERGEBNIS.md, regge-4d-schief-1/ERGEBNIS.md, pachner-takt-1/ERGEBNIS.md,
    takt-umbenennung-l/DOSSIER.md (grep), gemeinsames-netz-l/DOSSIER.md (Abschn. 1), strang-anker-l/DOSSIER.md (grep).
  - RUNDE-35/: graviton-netz-l/DOSSIER.md (grep), SCHREIBTISCH-QBALL-EIS-LAPSE.md, GEGENLESEN-R35.md (grep).
  - RUNDE-22/dunkel-zeit/ERGEBNIS.md (grep, vDVZ nach Hinterbichler 2012).
- **Gedaechtnis [L], nicht geprueft:**
  - ADM-Linearisierung (Hamilton-Bedingung delta R^(3) = 16 pi G rho, maximales Slicing).
  - Haynsworth-Traegheitsadditivitaet.
  - Deser/Jackiw/'t Hooft 1984 (Kegel 8 pi G M).
  - Einstein-Aether gamma = 1 (Foster/Jacobson 2006).
  - Williams/Ellis 1981/1984 (Regge und Beobachtungen) [L?].
  - R_sun ~ 7e8 m.

## 12. Selbstanzeigen

1. **Leerer Abruf:** F1a (19:47:33) rief die arXiv-API per http ohne Weiterleitung; die Antwort war leer. Ich zaehle ihn
   als Abruf; damit sind 8 von 8 verbraucht, 7 mit Inhalt.
2. **Suchdesign F2:** "Regge" traf Regge-Wheeler und Regge-Trajektorien; F3 korrigierte das mit der Phrase "Regge calculus".
3. **Nachtrag nach der Unterbrechung:** Die Ausgaenge von F3 bis F5 habe ich vor der Unterbrechung gelesen (19:48 bis
   19:49), aber erst ab 21:36 aus den lokalen Kopien in ARBEITSFELD.md eingetragen. Die Erwartungen standen vor den
   Abrufen (19:48:21).
4. **Schreibtischformel:** gamma = 2 kappa'/kappa_g, das Vorzeichen (Anziehung) und kappa' = kappa_g/2 sind [ES]. Geprueft
   ist das nur gegen das Kontinuum, nicht am Gitter. Die Exaktheit der Eck-Skalierung haengt an c = - B W
   (Codelesung) und an B_phys > 0 [P].
5. **Von Hand:** Prozentspannen aus kinetik.json und der Cassini-Ueberschlag fuer a sind Kopfrechnung, gerundet. Die
   Koeffizienten (2,2; 1,65; 11,1) stammen von anderen Gittern (Kuhn, schief, 4D), nicht von Finns gefuelltem Netz.
6. **Kontinuumsanalogien:** "c^dagger p = 0 entspricht maximalem Slicing" und "Regel = delta R^(3)" sind Analogien [ES].
   Glickensteins Eckformel habe ich nur im Abstract gesehen, ohne die Formel selbst.
7. **Gelesen nur per grep:** TAKT-UMBENENNUNG-L, GRAVITON-NETZ-L, STRANG-ANKER-L, GEGENLESEN-R35. Von
   GEMEINSAMES-NETZ-L nur Abschnitt 1. Zitate daraus sind [P] und tragen deren Kennzeichen weiter.
8. **Ausserhalb des Auftrags beruehrt:** V4/O1 (TT-Isotropie) ist keine gamma-Frage. Ich melde es wegen des
   Gegensweeps und schlage dafuer bewusst keine Karte vor.
9. **Lokale Werkzeuge:** date, ls, grep, sed, jq, curl (nur fuer die 8 API-Abrufe), mkdir, paste, cut, tr, wc, head. Kein
   python/awk/perl, nichts ausgefuehrt, nichts im Scratchpad der Leitung. Projekt-grep mit den verlangten Ausschluessen;
   ein grep in coordination/ lief mit --include='*.md' und denselben Ausschluessen.

## 13. Zeitbox und Unterbrechung

- Start 2026-10-04 19:33:05 CEST; Zeitbox 75 min.
- Unterbrechung (Sitzungslimit): letzte eigene date-Messung 19:51:49 CEST, Abbruch laut Leitung gegen 19:53. Streng
  gerechnet mit 19:53:00 waren 19 min 55 s verbraucht, Rest 55 min 05 s.
- Wiederaufnahme 21:35:52 CEST (date); neues Ende spaetestens 22:30:57 CEST.
- Abgabe 2026-10-04 21:47:27 CEST (date), also nach der Wiederaufnahme innerhalb der Restzeit bis 22:30:57.

## 14. Einfach gesagt

Ob Licht in Finns Netz richtig abgelenkt wird, ist keine neue Rechnung, sondern eine Bauregel. Die Masse muss an jeder
Ecke als Energie in die Regel eingehen, und Uhren wie Licht muessen denselben Takt dieser Ecke spueren. Dann staucht die
Regel, die die Uhren bremst, auch die Laengen um genau gleich viel, und das gibt Einsteins volle Lichtablenkung. Im
4D-Netz haben wir das schon nachgerechnet: Weit weg stimmt es, nur ganz nah an der Masse weicht es auf ein paar
Gitterabstaenden ab. Das groessere Problem liegt woanders: Die Schwerkraftwellen laufen im gefuellten Netz je nach
Richtung ein paar Prozent verschieden schnell, Messungen erlauben hoechstens ein Billiardstel.
