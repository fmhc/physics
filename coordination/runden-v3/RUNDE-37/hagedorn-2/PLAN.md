# HAGEDORN-2: Plan (Code-Agent, Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 06:35:45 CEST (date). Plan geschrieben ab 06:50:55 CEST
  (date direkt davor), nach dem Profillauf und den Rauchlaeufen r1/r2 (Abschnitt R), vor dem Einfrieren; Einfrierzeit
  siehe PLAN.md.eingefroren-*.
- Explorativ (v3). Alles ist synthetische Rechnung im Modell M1 (2D, U(S) = S - S^2 + S^3/2), keine
  Messdatenbestaetigung.
- Kennzeichen: [M] Mathematik/eigene Herleitung, [S] an der Quelle gelesen, [L] Literatur aus dem Gedaechtnis,
  [L?] unsicher, [H] Hypothese.
- Karte: KARTE.md daneben. Vorhersagen HZ0 bis HZ3 und ihre Schwellen gelten unveraendert. Was die Karte offenlaesst,
  ist als **[Zusatz]** gekennzeichnet; Kartenfehler und offene Punkte stehen in Abschnitt 4, mit Urteil nach
  Kartenwortlaut.
- Uebernommen aus HAGEDORN-1 (RUNDE-37/hagedorn-1/PLAN.md): BdG-Herleitung (Abschnitt 1 dort), Nullpaar-Regel,
  Randmoden-Regel, Klassen und Grauzone, Feinprobe, Kastenprobe, Ringast-Regel (Abschnitt 3.0 dort).

## 0. Schreibtisch vorab [M]

1. **Duennwand-Naeherung.** Bei omega^2 = 1/2 hat V(f) = U(f^2) - f^2/2 = f^2 (1 - f^2)^2 / 2 zwei gleich tiefe Minima
   (f = 0 und f = 1). Die Wand f' = f (1 - f^2)/sqrt(2) hat die Spannung sigma = Int (f'^2 + V) dr = 1/(2 sqrt 2)
   = 0,3536 und die Breite ~ 1/sqrt(2), unabhaengig von omega.
   - Ring als Kreisring mit f ~ 1 zwischen r_i und r_o, eps = omega^2 - 1/2:
     F = 2 pi sigma (r_i + r_o) + 2 pi m^2 ln(r_o/r_i) - pi eps (r_o^2 - r_i^2).
   - Stationaer: eps r_o^2 - sigma r_o - m^2 = 0 und eps r_i^2 + sigma r_i - m^2 = 0, also
     r_o,i = (sqrt(sigma^2 + 4 eps m^2) +- sigma)/(2 eps).
   - Folgen: Ringdicke r_o - r_i = sigma/eps, unabhaengig von m (17,7 bei 0,52; 35,4 bei 0,51). Mittlerer Radius
     ~ m/sqrt(eps).
   - Probe gegen RG-1 (0,52, m = 8): Formel 48,42 / 66,09, Schiessprofil 48,42 / 66,08 (Halbwertsradien).
   - Folge fuer das Gitter: Die Wandbreite bleibt fest, also braucht h nicht zu schrumpfen. Der Kasten waechst mit
     r_o; die Loch-Region r < r_i ist Vakuum und kann bis auf einen Schwanz abgeschnitten werden (Abschnitt 2).
2. **Grenze des Schiessens.** Auf dem Plateau f ~ 1 waechst eine Abweichung wie e^(sqrt(2) r)
   (V''(1) = -2 im Teilchenbild). Die Einschachtelung muss also auf e^(-sqrt(2) sigma/eps) genau sein:
   ~1e-11 bei 0,52 (RG-1 dort gueltig, Spreizung 1e-3), ~1e-22 bei 0,51, jenseits von float64.
   - Erwartung: Schiessen scheitert bei 0,51 fuer alle m. Bestaetigt im Profillauf (Abschnitt R); dort greift
     Versuch 2 (Abschnitt 2).
3. **HZ3 ist bei gegebener Auswahl vorab ableitbar.** E und R_max haengen nur am Profil; der Profillauf (Abschnitt R)
   gibt sie fuer alle 20 Zeilen. Steigung ln E gegen ln R_max je Auswahl stabiler m (mit jq aus
   lauf-69/profile/zeilen.json, 06:50 CEST):

   | omega^2 | 3,5,8 | 3,5,12 | 3,8,12 | 5,8,12 | 3,5,8,12 |
   |---|---|---|---|---|---|
   | 0,51 | 1,220 | 1,180 | 1,191 | 1,149 | 1,185 |
   | 0,52 | 1,115 | 1,093 | 1,099 | 1,073 | 1,096 |
   | 0,53 | 1,064 | 1,050 | 1,054 | 1,037 | 1,052 |
   | 0,54 | 1,034 | 1,025 | 1,027 | 1,016 | 1,026 |
   | 0,55 | 1,021 | 1,015 | 1,017 | 1,009 | 1,016 |

   - Mit dem ladungsgewichteten Radius r_mittel liegt jede Steigung bei 1,015 bis 1,089.
   - Grund [M]: E ~ Q ~ (r_o^2 - r_i^2) ~ sqrt(sigma^2 + 4 eps m^2), der mittlere Radius waechst genauso. R_max liegt
     aber nahe am Aussenrand (die Zentrifugalkraft senkt f innen) und traegt den m-unabhaengigen Versatz
     sigma/(2 eps) - c. Bei 0,51 und kleinem m hebt das die Steigung ueber 1,15.
   - Folge: HZ3 prueft nur, welche m stabil sind. L1 fuer die Steigung selbst ist schwach (wie HG4 in HAGEDORN-1).
4. **Kontinuum** (wie HAGEDORN-1): Luecke |Re Omega| < 1 - omega = 0,286 (0,51) bis 0,258 (0,55).

## 1. Herleitung

- BdG fuer Klein-Gordon wie HAGEDORN-1, PLAN.md Abschnitt 1 dort: Omega (x, y) = [[0, 1], [A, -G]] (x, y),
  A = [[-L_+, W], [W, -L_-]], G = 2 omega diag(1, -1), Stoerung u e^(i (m + l) theta), v* e^(i (m - l) theta).
- Nullmoden: Phase (l = 0, (f, -f)) und Verschiebung (l = 1, (f' - m f/r, f' + m f/r)); Jordan-Bloecke wie dort.

## 2. Numerik

- **Raster (Karte):** m in {3, 5, 8, 12}, omega^2 in {0,51; 0,52; 0,53; 0,54; 0,55}; l = 0 bis 3m (10, 16, 25, 37
  Sektoren).
- **Profile** (code/hagedorn2.py profile):
  - Versuch 1: Schiessen mit regge2d.py (unveraendert, h0 = 0,005). Gueltig, wenn regge2d "gueltig" meldet und
    |Virial| <= 1e-5 **[Zusatz]** (wie VIRIAL_MAX in RG-1).
  - Versuch 2 (wo Versuch 1 scheitert) **[Zusatz]:** gedaempftes Newton auf der vollen Scheibe, versetztes Gitter
    h_t = 0,05, bis r_o + 22/kappa. Start ist der Duennwand-Ansatz S = expit(-sqrt2 (r - r_o)) expit(sqrt2 (r - r_i))
    mit r_i, r_o aus 0.1.
    - Gueltig, wenn Rest <= 1e-10, f >= 0, {S >= S_max/2} ein einziges Intervall und f_max > 0,5.
    - E, Q, R aus Mittelpunktsummen auf diesem Gitter.
  - Beide Versuche laufen fuer alle 20 Zeilen. Wo beide gueltig sind, werden die Newton-Gitterprofile verglichen.
  - Das Gitterprofil fuer BdG entsteht immer durch Newton auf dem jeweiligen Gitter (wie HAGEDORN-1), gestartet aus
    der hermiteschen Interpolation der Quelle.
- **Gitter- und Kastenregel [Zusatz, vor dem ersten BdG-Lauf im Code]:**
  - Versetztes Gitter r_j = r_a + (j - 1/2) h.
  - Innen: r_a = R_innen - 12/kappa, falls >= 2 (dann Dirichlet bei r_a); sonst r_a = 0 mit Paritaet (-1)^|k| wie
    HAGEDORN-1.
  - Aussen: L = R_aussen + 12/kappa, Dirichlet (wie HAGEDORN-1).
  - R_innen und R_aussen sind die Halbwertsradien von S = f^2 aus der Profilquelle.
  - Basis h = 0,2 fuer alle Profile (Wandbreite ~0,7, Abschnitt 0.1); fein h/2 = 0,1 im gleichen Kasten.
  - Kastenprobe: 18/kappa innen und aussen, gleiches h.
  - Begruendung: Kasten und Punktzahl wachsen mit dem Profil (N = 177 bis 349 auf der Basis). Die Schrittweite bleibt,
    weil die Wand im Duennwand-Grenzfall nicht duenner wird.
- **Eigenwerte:**
  - Je Zeile und l das volle Spektrum der dichten 4N-Matrix (LAPACK geev), Eigenvektoren per inverser Iteration
    (wie HAGEDORN-1).
  - Feines Gitter: Shift-Invert-Arnoldi am Basiseigenwert (gezielte Suche an jedem instabilen Eigenwert).
  - Dichteprobe **[Zusatz]:** volles Spektrum auf h/2 fuer die drei HZ1-Zeilen (m = 3, 5, 8 bei 0,52), alle
    l = 0 bis 3m. Sie prueft, ob das Basisgitter Instabilitaeten verpasst.
- **Groessen:**
  - E, Q, R_max, R_innen, R_aussen und r_mittel aus der Profilquelle. Beim Schiessen ist das genau die RG-1-Methode.
  - R = R_max wie in HAGEDORN-1 (Ort des Maximums von f).
  - Nullmoden-Residuen (beschreibend) im Fenster R_innen - 6/kappa <= r <= R_aussen + 6/kappa.
- **Laufplan:**
  - Bloecke mit hoechstens 540 s Rechenbudget im Skript; der Rest kommt in den naechsten Block.
  - cpu: 0,51, dann 0,55. cpu6: 0,52, 0,53, 0,54.
  - Danach die Dichteprobe in zwei Bloecken (cpu: m = 3, 5; cpu6: m = 8).
  - Zuletzt code/auswertung2.py auf cpu.
  - Ausgaben auf der .69 unter runde38-hagedorn2/lauf/ (haupt/, dicht/, auswertung/), Kopie nach lauf-69/.

## 3. Urteilsregeln (vor dem Einfrieren)

### 3.0 Begriffe (HAGEDORN-1, Abschnitt 3.0 dort, mit zwei Zusaetzen)

- **Nullpaar** (l = 0 und 1): unter den sechs betragskleinsten Eigenwerten die zwei mit der groessten Ueberlappung mit
  der bekannten Nullmode. Nicht gewertet.
- **Randmode:** Normanteil im aeusseren Randviertel r >= R_aussen + 0,75 (L - R_aussen) groesser als 0,1. Nicht
  gewertet, aber gezaehlt und offengelegt.
  - **[Zusatz]:** Bei r_a > 0 zaehlt auch das innere Randviertel r <= R_innen - 0,75 (R_innen - r_a).
- **max Im** eines Profils: groesstes Im Omega der gezaehlten Eigenwerte ueber l = 0 bis 3m (Basisgitter).
- **Klasse:**
  - "instabil" bei max Im > 1e-4, "stabil" bei max Im < 1e-6, dazwischen "grau".
  - Grau ist weder stabil noch instabil (Regel aus HAGEDORN-1).
- **Feinprobe:** Jeder gezaehlte Eigenwert mit Im > 1e-6 (der groesste je l) wird auf h/2 verfolgt. Ergibt das feine
  Gitter eine andere Klasse, heisst die Zeile "nicht konvergiert".
- **Dichteprobe [Zusatz]** (nur HZ1-Zeilen): Ergibt das volle Spektrum auf h/2 eine andere Klasse als Basis und
  Feinprobe, heisst die Zeile ebenfalls "nicht konvergiert".
  - Fehlt die Dichteprobe (Zeitbox), gilt die Klasse aus Basis und Feinprobe; das wird vermerkt.
- **Kastenprobe** (beschreibend): die drei groessten gezaehlten Instabilitaeten je Zeile im Kasten 18/kappa. Kein
  Urteil haengt daran.
- **Ringast** (beschreibend, Messgroesse der Karte): kleinste positive reelle Ringmode je l (Ringanteil >= 0,6), Regel
  wie HAGEDORN-1.

### 3.1 HZ0 (Anschluss an HAGEDORN-1)

- Zeilen m = 3 und m = 5 bei omega^2 = 0,55.
- Referenz: HAGEDORN-1, lauf-69/auswertung.json: max Im = 4,289659e-3 (m = 3) und 5,402169e-3 (m = 5), beide bei l = 2
  (dort l = 0 bis 12).
- **[Zusatz] Vergleichsbereich:** max Im von HAGEDORN-2 ueber den gemeinsamen Bereich l = 0 bis min(12, 3m).
  - HAGEDORN-1 hatte bei beiden Zeilen nur l = 2 instabil, also gilt sein Wert auch fuer den gemeinsamen Bereich.
- Eingetroffen, wenn |Differenz| <= 1e-4 fuer beide m; nicht eingetroffen, wenn eine Differenz > 1e-4; fehlende Zeile:
  nicht auswertbar.
- Zweiturteil nach Kartenwortlaut (max Im ueber l = 0 bis 3m): wird mitberichtet.

### 3.2 HZ1 (bei 0,52 stabil)

- Zeilen m = 3, 5, 8 bei omega^2 = 0,52.
- Eingetroffen, wenn alle drei "stabil" sind (das ist genau "alle Im < 1e-6 fuer l = 0 bis 3m").
- Nicht eingetroffen, wenn eine "instabil" oder "grau" ist.
- Sonst (fehlend oder nicht konvergiert, aber keine instabil oder grau): nicht auswertbar.

### 3.3 HZ2 (monoton fallend)

- Fuer m = 3, 5, 8 die Folge v(omega^2) fuer omega^2 = 0,55; 0,54; 0,53; 0,52; 0,51, alle Werte aus HAGEDORN-2.
- **[Zusatz] Lesart:**
  - v = max Im bei Klasse "instabil" oder "grau"; v = 0 bei "stabil" (das ist "wird null").
  - "Monoton fallend" heisst nicht steigend: Fuer omega_b^2 < omega_a^2 muss v(b) <= v(a) gelten, fuer jedes Paar,
    auch ueber Luecken. Keine Toleranz.
- Nicht eingetroffen, wenn fuer ein m ein Paar die Bedingung verletzt (beide Werte vorhanden).
- Eingetroffen, wenn kein Verstoss vorliegt und alle 15 Werte vorhanden sind (keine Zeile fehlend oder nicht
  konvergiert).
- Sonst nicht auswertbar.

### 3.4 HZ3 (E ~ R auf stabilen Profilen) [H]

- Je omega^2 mit mindestens drei "stabilen" m (aus 3, 5, 8, 12): Steigung s der Anpassung ln E gegen ln R_max (kleinste
  Quadrate).
- Eingetroffen, wenn es mindestens ein solches omega^2 gibt und dort |s - 1| <= 0,15 gilt (bei mehreren: an allen).
- Nicht eingetroffen, wenn ein solches omega^2 die Grenze reisst.
- Sonst nicht auswertbar.
- Vorab ableitbar bei gegebener Auswahl (Abschnitt 0.3): Vermerk im Urteil. Beschreibend: dieselbe Steigung mit
  r_mittel und ueber alle m ohne Auswahl.

## 4. Kartenfehler und offene Punkte

1. **HZ0, l-Bereich:**
   - HAGEDORN-1 rechnete l = 0 bis 12, HAGEDORN-2 rechnet l = 0 bis 3m. Fuer m = 5 sind l = 13 bis 15 neu.
   - Ein Unterschied dort waere kein Anschlussfehler, sondern ein neuer Befund. Deshalb wird im gemeinsamen Bereich
     verglichen (3.1).
   - Urteil nach Kartenwortlaut: mitberichtet.
2. **HZ3, Definition von R:**
   - Die Karte sagt "E ~ R", definiert R aber nicht. Uebernommen ist R = R_max aus HAGEDORN-1.
   - Im Duennwand-Bereich liegt R_max nahe am Aussenrand; die Steigung waechst dort fuer kleine m ueber 1 (0.3). Fuer
     die Laenge eines Strings waere der mittlere Radius das passendere Mass.
   - Keine Berichtigung, weil die Karte R nicht festlegt. Die Steigung mit r_mittel wird beschreibend mitberichtet.
3. **HZ3 vorab ableitbar** (0.3). Die Karte nennt das nicht; es ist kein Fehler, aber L1 fuer HZ3 ist schwach.
4. **HZ2, "monoton":** Die Karte nennt keine Toleranz und keine Regel fuer "grau". Die Lesart steht in 3.3.
5. **"Kasten und Gitter mitwachsen lassen":** Der Kasten waechst, die Punktzahl auch. Die Schrittweite bleibt fest,
   weil die Wandbreite im Duennwand-Grenzfall fest bleibt (0.1). Die Konvergenz zeigen Feinprobe, Dichteprobe und
   Kastenprobe.

## R. Profillauf und Rauchlaeufe (vor dem Einfrieren, alles Gesehene)

Ausgaben auf der .69 unter runde38-hagedorn2/lauf/profile und rauch/r1, r2; Kopien in lauf-69/profile, lauf-69/profile.log
und rauch-69/. Code-Hash vor dem ersten Lauf: code/SHA256-vor-erstem-rauchlauf.txt (hagedorn2.py 81cd74bb...ee654,
06:47:31 CEST). hagedorn2.py ist seitdem unveraendert. code/auswertung2.py entstand waehrend r1/r2, bevor ich deren
Ausgaben gelesen hatte.

- **Profillauf** (04:47:31 bis 04:48:16 UTC, 45 s):
  - Schiessen bei 0,51 fuer alle vier m ungueltig ("Mitte-Bahn vor dem Schwanz umgekehrt"), wie in 0.2 erwartet.
    Bei 0,52 bis 0,55 gueltig, |Virial| <= 7,4e-9; bei 0,52 Spreizung 4e-4 bis 2e-3.
  - Versuch 2 (Duennwand-Newton) fuer alle 20 Zeilen gueltig: Rest <= 9,3e-13 nach 4 bis 8 Schritten, ein Ring.
  - R_innen und R_aussen weichen um <= 0,1 von der Duennwand-Formel ab.
  - Vergleich der beiden Quellen (16 Zeilen): Gitterprofile gleich auf <= 1,7e-12 relativ. E gleich auf <= 3,7e-7
    (0,52) bzw. <= 1,6e-10 (0,53 bis 0,55).
  - Bei 0,51 stammen die Profile also aus Versuch 2.
- **r1** (m = 3, 0,55, l = 0 bis 3, h = 0,2, 04:48:32 UTC, 2,4 s):
  - l = 2: Omega = 0,0259659911 + 0,0042896584 i. HAGEDORN-1 (h = 0,1, volle Scheibe): 0,0259659911 + 0,0042896585 i,
    Differenz im Im 1,4e-10.
  - l = 0, 1, 3 ohne gezaehlte Instabilitaet. Nullpaar l = 1: 2,4e-6.
  - Verschiebungsresiduum im Fenster 4,9e-6 (h = 0,2), 2,3e-8 (h/2).
  - Kastenprobe l = 2: relativ 3e-8.
- **r2** (m = 12, 0,51, l = 0 bis 2, 04:48:32 UTC, 9,2 s):
  - N = 349, r_a = 86,47, L = 156,27; dichte Zerlegung n = 1396: 2,9 s je l.
  - l = 2 instabil: Omega = 0,0015588 + 0,00048099 i (Ringanteil 0,989, Randanteil 1e-8), Kastenprobe relativ 3e-7.
  - l = 0, 1 ohne gezaehlte Instabilitaet.
  - Verallgemeinerte Nullmode (nur beschreibend) unbrauchbar: Rest 2,1e2, dQ/domega = -8,2e6. Der Newton-Sprung bei
    omega +- 1e-4 ist hier fast singulaer.
- **Laufzeit fuer den Laufplan:** 0,51 etwa 300 s, 0,52 etwa 130 s, 0,53 bis 0,55 je 50 bis 80 s; Dichteprobe etwa
  460 s.
- Schwellen der Karte und die Regeln in Abschnitt 3 sind nach keinem Lauf geaendert. Die Zusatzregeln 3.0 und die
  Gitter- und Kastenregel standen vor r1/r2 im Code (Hash oben). Die Lesarten in 3.1 und 3.3 und die Dichteprobe
  habe ich in auswertung2.py und hier festgelegt, nachdem ich r1/r2 gesehen hatte.
- r2 zeigt schon jetzt: m = 12 ist bei 0,51 instabil (l = 2, Im 4,8e-4). Keine HZ-Zeile haengt an m = 12 ausser der
  Auswahl in HZ3. Die Urteile folgen allein aus den Hauptlaeufen.
