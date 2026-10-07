# Runde 5, Paket R5-D: 1D mit zwei komplexen Feldern (Bio 8, 15, 35, 48; Chemie 17; Wellen 10)

Bearbeiter: Anthropic-Agent R5-D (Opus), Auftrag ../AUFTRAG-R5.md, Abschnitt "R5-D". Beginn 2026-09-30 01:43:55 CEST
(gemessen), Ende in der letzten Zeile. Status: Code geschrieben, lokal kompiliert und im Rauchtest durchgelaufen
(Abschnitt 5a, Finns Freigabe 02:42), **Messlaeufe nicht gerechnet**. Explorativ.
Nachricht der Leitung (ca. 02:00, Fable-Review Z. 39-45) eingearbeitet: stabiles Medium fuer chi (Abschnitt 1.3) und
Liste der Medium-Karten, die dieser Aufbau spaeter traegt (Abschnitt 6). Nichts zusaetzlich gerechnet.

## Kurzfassung

- **Code:** r5d.py (PyTorch, float64/complex128, `--geraet cuda|cpu`). Ein Unterbefehl je Idee plus `rauch`. Jeder
  Unterbefehl rechnet alle Laeufe als Stapel, grob (dx 0,1, dt 0,05) und fein (dx 0,05, dt 0,025), und wertet L3 selbst
  aus. Bericht, JSON und Zeitreihen werden nach jedem Test geschrieben.
- **Aus tests1d.py unveraendert:** Gitter (Box [-150, 150], x = 0 auf einem Punkt), Velocity-Verlet, feine Stufe,
  Daempfungsschicht (quadratisch, sigma0 = 1, ab |x| = 110), Anker-Formeln (Q, E, FWHM, Q -> omega), Lorentz-Boost, l3.
- **Geaendert:** zwei Felder. Statt der Schiessbahn das geschlossene 1D-Profil f^2 = 2 a0/(1 + b0 cosh(2 sqrt(a0) x));
  es ist profil_anker aus tests1d.py und dort gegen das Schiessen auf 1,5e-10 geprueft. In 1D ist Schiessen damit
  unnoetig; das spart 83 s und eine Fehlerquelle. Fuer "kreuzen" eine periodische Box ohne Daempfung.
- **Laufzeit:** je Unterbefehl geschaetzt 1 bis 3 min auf der P4000, 1,5 bis 5 min auf einem CPU-Kern; alle unter
  10 min. Rauchtest 0,5 bis 2 min.
- **In 1D nicht sinnvoll pruefbar:** Wellen 10 (Kreuzen) und der Q_min-Teil von Chemie 17. Grund und kleinste
  sinnvolle Form stehen bei der Karte; gerechnet wird jeweils ein 1D-Baustein.
- **Kernvorhersagen:**
  - Zellkern: Kern-Huelle mit Loch in keinem Lauf; die "Kern"-Breite 1/m ist schon ohne Kopplung da.
  - Raeuber-Beute: Pendeln nur gleichphasig und unter z_c ~ 0,43, sonst Selbstfang; kein Lotka-Volterra-Versatz
    (vorab ausgeschlossen).
  - Mitochondrium: Bei Anziehung bleibt der Gast unter v ~ 0,3 gefangen und entkommt darueber.
  - Altern: Verdampfung nur an den Waenden, Rate nach der Formel; kleine Baelle leben am laengsten.
  - Tensid: chi sitzt an der Wand und verbreitert sie; die grosskanonische Wandenergie bleibt fast gleich.
  - Kreuzen: Unter der Schallgeschwindigkeit des Mediums wirkt keine Kraft, darueber Mitnahme.

## 1. Modell und Wahl der Kopplung

### 1.1 Lagrangedichte

L = |psi_t|^2 + |chi_t|^2 - |psi_x|^2 - |chi_x|^2 - V mit

V = U(S) + mc2 C + g4 C^2 + kc (-C^2 + C^3/2) + C (lam S + lam2 S^2) + eps (conj(psi) chi + conj(chi) psi),

U(S) = S - S^2 + S^3/2, S = |psi|^2, C = |chi|^2.
- psi ist unveraendert das Modell der Runden 1 bis 4.
- Fuer chi gibt es drei Rollen:
  - **Kanal** (kc = mc2 = m^2, g4 = 0): Kopie von psi mit Masse m. Loesungen skalieren exakt:
    chi(x, t) = f(m x) exp(-i m omega t). Ein chi-Ball hat dieselbe Ladung und Hoehe wie der psi-Ball bei omega, ist
    m-mal schmaler und hat m-mal mehr Energie. Das Profil ist geschlossen bekannt; kein neues Schiessen.
  - **Medium** (kc = 0, g4 > 0): defokussierend, jede Dichte stabil (1.3).
  - **frei** (kc = g4 = 0): nur die Masse sqrt(mc2).

### 1.2 Kopplungen

- **Dichtekopplung** lam S C (bzw. C (lam S + lam2 S^2)): Das ist die einfachste Kopplung, die die beiden U(1) einzeln
  erhaelt. Q_psi und Q_chi bleiben je fuer sich erhalten. Sie reicht fuer Zellkern, Mitochondrium, Tensid und Kreuzen.
- **Austausch** eps (conj psi chi + c.c.) (Rabi-Mischung): Das ist die einfachste Kopplung mit Ladungsaustausch. Nur
  Q_psi + Q_chi bleibt erhalten. Sie ist noetig fuer Raeuber-Beute und Altern: Mit reiner Dichtekopplung waere
  Q_psi exakt erhalten; "Altern" koennte dann gar nicht auftreten, und der Test waere selbsterfuellend.
- **Vakuum:** Die Massenmatrix [[1, eps], [eps, mc2]] muss nichtnegativ sein, also mc2 >= eps^2; der Code bricht sonst
  ab.
- **Masseloser Kanal (Altern):** Streng masseloses chi (mc2 = 0) mit eps != 0 gibt det = -eps^2 < 0. Dann waechst eine
  tachyonische Mode fuer k < eps mit der Rate ~eps, das Vakuum ist instabil. Mit mc2 = eps^2 ist det = 0: Die
  Eigenwerte sind 0 und 1 + eps^2, eine Eigenmode ist also genau masselos und das Vakuum stabil.
  - Verworfen: Lorentz-invariante kinetische Mischung. Sie ist nur eine Feldumdefinition; der masselose Teil entkoppelt
    dann vollstaendig, und es gibt keine Verdampfung.
- **Amphiphile Kopplung (Tensid):** lam = -a, lam2 = +a ergibt -a S (1 - S) C. Sie zieht nur in der Wand an (Minimum
  bei S = 1/2) und ist innen (S ~ 1) und aussen (S ~ 0) null. Reine Dichtekopplung setzt chi ins Innere; sie ist die
  Gegenprobe.

Bewegungsgleichungen (im Code `kraft`):
- psi_tt = psi_xx - [U'(S) + C (lam + 2 lam2 S)] psi - eps chi
- chi_tt = chi_xx - [mc2 + 2 g4 C + kc (-2C + 1,5C^2) + lam S + lam2 S^2] chi - eps psi

Ladungsdichte je Feld 2 Im(f conj f_t), Energiedichte |psi_t|^2 + |chi_t|^2 + |psi_x|^2 + |chi_x|^2 + V.

### 1.3 Stabilitaet des chi-Mediums (Bitte der Leitung)

- **Hintergrund:** chi = sqrt(C0) exp(-i omega0 t) mit omega0^2 = U_chi'(C0).
- **Linearisierung:** Die Bogoliubov-Dispersion ist (k^2 - Om^2)(k^2 - Om^2 + 2g) = 4 omega0^2 Om^2 mit
  g = U_chi''(C0) C0. Hergeleitet ist sie von Hand aus der Stoerung u exp(i(kx - Om t)) + conj(v) exp(-i(kx - Om t)).
- **Stabilitaetsbedingung:** Als quadratische Gleichung in Om^2 hat sie das Wurzelprodukt k^2 (k^2 + 2g).
  - Fuer g < 0 ist es bei k^2 < -2g negativ, eine Wurzel Om^2 < 0: Modulationsinstabilitaet.
  - Fuer psi ist g = (-2 + 3S) S. Das ist genau die Grenze S = 2/3 aus Codex' Dispersionsrelation und dem Fable-Review.
  - Fuer g >= 0 sind Summe und Produkt positiv. Die Diskriminante ist 4 [g^2 + 4 omega0^4 + 4 k^2 omega0^2
    + 4 g omega0^2] > 0. Also sind beide Wurzeln reell und positiv, stabil fuer alle k.
- **Unser Medium:** U_chi = C + g4 C^2 hat U_chi'' = 2 g4 > 0, also ist **jede Dichte linear stabil**, auch eine
  duenne.
- **Schallgeschwindigkeit:** c_s^2 = g/(2 omega0^2 + g), aus der Entwicklung fuer kleine k.
  - Fuer C0 = 0,1 und g4 = 0,5: omega0^2 = 1,1, g = 0,1, **c_s = 0,2085**.
  - Die Landau-Schwelle existiert also bei jeder Dichte. Im Ein-Feld-Modell fehlt sie fuer S < 2/3 (v_c = 0, Fable).
- **Pruefung im Lauf:** "kreuzen", Lauf "Medium allein": Die stroemende Ebene Welle ist eine exakte Gitterloesung (omega
  mit k_eff^2 = (2 - 2 cos(k dx))/dx^2). C muss auf 1e-9 konstant bleiben.
- Die Kanal-Rolle (Zellkern, Raeuber, Mitochondrium) braucht dagegen ein fokussierendes chi, sonst gibt es keinen
  chi-Ball. Ein chi-Hintergrund kommt dort nicht vor.

## 2. Die sechs Karten: Aufbau, Vorhersage, Gegenprobe, L3

Alle Laeufe: offene Box mit Daempfung (ausser "kreuzen"), grob und fein. Zahlen mit Anker-Formeln von Hand gerechnet:

| omega^2 | 0,500001 | 0,5001 | 0,51 | 0,55 | 0,6 | 0,7 | 0,8 | 0,9 |
|---|---|---|---|---|---|---|---|---|
| Q | 14,51 | 9,90 | 5,34 | 3,81 | 3,16 | 2,44 | 1,89 | 1,29 |
| FWHM | 10,26 | 7,04 | 4,14 | 3,47 | 3,36 | 3,56 | 4,16 | 5,70 |

E(0,6) = 2,878, E(0,8) = 1,818.
Duenne Wand bei 0,500001: Plateau S = 0,9986, Waende bei +-5,13, 2 sigma = E - omega Q = 0,70710.

### 2.1 zellkern (Bio 8): Kern-Huelle-Profil bei verschiedenen Massen?

- **Aufbau:**
  - psi-Ball omega^2 = 0,6 bei 0.
  - chi-Kanal mit Masse m = 1; 1,5; 2,5, chi-Ball mit omega_chi = m sqrt(0,6) bei +0,5 (Versatz bricht die Symmetrie).
  - lam = -0,4; 0; +0,4. 9 Laeufe, T = 400, Messung alle 0,5.
- **Messung:**
  - Schwerpunkte und Breiten (Standardabweichung) von S und C in |x| < 60; K = w_chi/w_psi.
  - Loch = 1 - (Dichte der breiteren Komponente am Schwerpunkt der schmaleren)/(ihr Maximum).
  - Ladungen im Fenster; t_Trennung = erstes Mal Abstand > 5. Endfenster [3T/4, T].
- **Klassen (vorab):**
  - getrennt: einmal Abstand > 5
  - Huelle mit Loch: Abstand < 1 und Loch > 0,2 in der breiteren Komponente
  - verschachtelt: Abstand < 1 und K oder 1/K > 1,25
  - gemeinsam: Abstand < 1
  - sonst unklar
- **Papierbild:**
  - Die Kopplung wirkt wie ein Potential lam S fuer chi und lam C fuer psi: Topf fuer lam < 0, Huegel fuer lam > 0.
  - Eine echte Huelle (Loch) braucht Abstossung und zugleich etwas, das den Kern in der Mitte haelt. In 1D ohne Falle
    fehlt das: Trennen kostet nichts, Aufspalten von psi um chi herum kostet zwei neue Waende.
- **Vorhersagen:**
  - **V8a (lam = 0, vorab ableitbar, nur Kontrolle):** Abstand bleibt 0,5, K = 1/m auf 0,01 (1; 0,667; 0,4). Klassen:
    m = 1 gemeinsam, m = 1,5 und 2,5 verschachtelt. Das Kern-Huelle-Bild bei verschiedenen Massen entsteht also schon
    ohne jede Kopplung, allein aus der Breite 1/m.
  - **V8b (lam = -0,4):** gebunden und gemeinsam.
    - Abstand am Ende < 0,3; chi pendelt gedaempft um die Mitte.
    - |dK| < 0,1, Loch < 0,05, Ladungen im Fenster >= 0,97.
    - Klassen wie bei lam = 0.
  - **V8c (lam = +0,4):** getrennt bei allen m, t_Trennung < 100. Die Abstossungsenergie lam Int S C betraegt 0,18 bis
    0,29, das gibt eine Relativgeschwindigkeit von etwa 0,4 bis 0,6.
  - **V8d:** "Huelle mit Loch" in 0 von 9 Laeufen.
- **Gegenprobe:** lam = 0 (Effekt der Kopplung verschwindet) und m = 1 (Massenunterschied verschwindet, K = 1).
- **L3 im Code:**
  - lam = -0,4: dK und dAbstand gegen lam = 0 bei gleichem m.
  - getrennte Laeufe: t_Trennung.

### 2.2 raeuber (Bio 15): Pendeln die Bestaende?

- **Aufbau:**
  - chi-Kanal mit m = 1 (zweite "Art", gleiche Masse), lam = 0, Austausch eps = 0,02 (Vakuum: Eigenwerte 0,98 und
    1,02).
  - Je Einheit psi-Ball mit Q_a = (1 + z0)/2 * 4,883 und chi-Ball mit Q_b = (1 - z0)/2 * 4,883 am selben Ort. Die
    Relativphase ist 0 (gleichphasig) oder pi (gegenphasig).
  - Laeufe: rein (z0 = 1); gleichphasig z0 = 0,05 / 0,3 / 0,6; gegenphasig z0 = 0,05 / 0,3; Kontrolle eps = 0;
    Kontrolle getrennt (Abstand 40); Box mit drei Einheiten (Ladung x 0,8 / 1 / 1,2 bei x = -60 / 0 / 60, z0 = 0,3).
  - 9 Laeufe, T = 500, Messung 0,5, Fenster [T/6, T].
- **Messung:**
  - z(t) = (Q_psi - Q_chi)/(Q_psi + Q_chi) in |x| < 100; Amplitude A = (max - min)/2.
  - Nulldurchgaenge von z mit Hysterese 0,005; Periode aus der FFT; Relativphase in der Mitte.
  - Klasse: ruhig (A < 0,01), pendelt um Gleichstand (>= 2 Durchgaenge), sonst Selbstfang.
- **Papierbild (Zwei-Moden-Rechnung von Hand):** H = E(Q_a) + E(Q_b) + (eps/omega) sqrt(Q_a Q_b) cos(dphi)
  ~ -0,60 z^2 + 0,058 sqrt(1 - z^2) cos(dphi).
  - Das ist ein Josephson-Paar mit anziehender Nichtlinearitaet (domega/dQ = -0,101 bei 0,7), Lambda ~ -21.
  - Gleichphasig ist der Gleichstand ein Zentrum, gegenphasig ein Sattel.
- **Vorhersagen:**
  - **V15a (gleichphasig z0 = 0,05):** pendelt um den Gleichstand, z zwischen -0,05 und +0,05, Periode 57 (40 bis 80).
  - **V15b (gleichphasig z0 = 0,3):** pendelt, A ~ 0,3, Periode 60 bis 110.
  - **V15c (gleichphasig z0 = 0,6):** Selbstfang. Die Schwelle ist z_c ~ 0,43; mit der Unsicherheit von Lambda liegt
    sie zwischen 0,36 und 0,53. z bleibt zwischen etwa 0,44 und 0,6.
  - **V15d (gegenphasig):** Selbstfang auf der Seite von z0 mit laufender Phase: z zwischen 0,05 und ~0,43 bzw. zwischen
    0,3 und ~0,52. Kein Pendeln um den Gleichstand.
  - **V15e (rein):** ruhig, z > 0,98. chi hat bei omega < 1 keine eigene Mode, nur eine Bekleidung von ~0,2 %.
  - **V15f (Kontrollen):** eps = 0: A < 1e-4; getrennt: A < 1e-3.
  - **V15g (Box):** Die drei Einheiten pendeln mit verschiedenen Perioden. Klasse "pendelt", aber keine einzelne saubere
    Periode.
- **Vorab ableitbar, keine Messung:**
  - Q_psi + Q_chi ist erhalten. Die Korrelation der Bestaende ist daher -1.
  - Der Lotka-Volterra-Versatz (Raeuber eine Viertelperiode hinter der Beute) ist mit zwei Arten und erhaltener Summe
    unmoeglich.
  - Geprueft wird nur, ob und wann ueberhaupt gependelt wird.
- **L1:** Lotka-Volterra sagt Pendeln fuer jeden Start voraus; das Josephson-Bild sagt Selbstfang ab z_c und bei
  gegenphasigem Start. Pendeln in allen sechs Austauschlaeufen widerspraeche dem Josephson-Bild.
- **Gegenprobe:** eps = 0, raeumlich getrennt.
- **L3 im Code:** A und Periode je Austauschlauf (ohne die Kontrollen).

### 2.3 mitochondrium (Bio 35): Lebt ein kleiner chi-Ball dauerhaft im grossen psi-Ball?

- **Aufbau:**
  - Wirt: psi-Ball omega^2 = 0,500001 (Plateau S ~ 1, FWHM 10,26, Q 14,51, E ~ 10,97).
  - Gast: chi-Kanal m = 2, omega_rel^2 = 0,8 (FWHM 2,08, Q 1,887, E 3,64), Start in der Mitte mit v = 0; 0,2; 0,4.
  - lam = -0,3; 0; +0,3. 9 Laeufe, T = 400.
- **Messung:**
  - Gastort (Maximum von C, Parabel), Wirtschwerpunkt und Wirt-Halbbreite (halbe Laenge ueber halber Hoehe).
  - drin = |Gast - Wirt| < Halbbreite; Anteil drin auf [T/4, T]; t_raus = erstes Mal |Gast - Wirt| > Halbbreite + 3.
  - Mittendurchgaenge (Hysterese 1); Q_gast in +-6 um den Gast.
  - Klassen: entkommen (t_raus endlich), gefangen bzw. ruht innen (Anteil >= 0,9 und am Ende drin), sonst unklar.
- **Papierbild:**
  - Im flachen Innern spuert der Gast keine Kraft.
  - An der Wand aendert sich seine Energie um lam S Int C dx = lam * 0,527. Bei lam = -0,3 ist das eine Stufe von
    0,158 (Topf), bei +0,3 ein Rauswurf.
  - Fluchtgeschwindigkeit bei lam = -0,3: 0,29 (Wirt fest) bzw. 0,34 relativ (Wirt beweglich).
- **Vorhersagen:**
  - **V35a (lam = -0,3):**
    - v = 0: ruht innen.
    - v = 0,2: gefangen (Anteil drin >= 0,9, mindestens 3 Mittendurchgaenge, Pendelperiode ~80 bis 100).
    - v = 0,4: entkommen, t_raus < 60.
  - **V35b (lam = 0, Kontrolle):** v = 0 ruht; v = 0,2 und 0,4 fliegen frei durch (t_raus ~ 41 bzw. 20).
  - **V35c (lam = +0,3):** v = 0 ruht innen (flaches Innere, metastabil). v = 0,2 und 0,4 entkommen frueher als bei
    lam = 0, mit Austrittsgeschwindigkeit ~0,39 bzw. ~0,5.
  - **V35d:** Der Gast ueberlebt ueberall (Q_gast gehalten >= 0,9 bis Austritt oder Ende); Q_wirt gehalten >= 0,98.
- **L1:** Entkommt oder zerfaellt der Gast bei lam = -0,3 und v = 0,2, ist V35a verfehlt.
- **Gegenprobe:** lam = 0.
- **L3 im Code:** d_drin gegen lam = 0 bei gleichem v (Laeufe mit lam != 0, v > 0).

### 2.4 altern (Bio 48): Verdampfung in einen masselosen Kanal

- **Modell:** chi frei mit mc2 = eps^2 und eps = 0,05: genau eine masselose Eigenmode (1.2).
- **Aufbau:**
  - psi-Ball ruhend bei omega^2 = 0,500001; 0,5001; 0,51; 0,55; 0,6; 0,7; 0,8; 0,9.
  - chi startet mit der lokalen Bekleidung eps f/(U'(S) - mc2), das verkleinert den Anfangsstoss.
  - Gegenproben: Kanal mit Masse 1,2 > omega (mc2 = 1,44) bei 0,500001 und 0,7; eps = 0 bei 0,7.
  - 11 Laeufe, T = 400, Messung 1.
- **Messung:** Q_Ball = Q_psi + Q_chi in |x| < 40; Gamma = -dQ_Ball/dt aus einer Geraden auf [T/4, T]; Lebensdauer
  Q/Gamma.
- **Formel (vorab, erste Ordnung in eps):**
  - Fernfeld: chi'' + omega^2 chi = eps f.
  - Auslaufende Welle je Seite mit k = omega und Amplitude eps f~(omega)/(2 omega); Ladungsfluss je Seite
    2 omega |A|^2.
  - Also **Gamma = eps^2 f~(omega)^2/omega** mit f~(k) = Int f(x) cos(kx) dx.
  - Der Code rechnet f~ durch Quadratur (h = 0,005) und schreibt die Vorhersage neben die Messung.
  - Im homogenen Innern (k = 0) kann ein Quant nicht in eine Welle mit k = omega uebergehen. Abgestrahlt wird nur an
    den Waenden, also an der "Oberflaeche". f~ enthaelt die Interferenz der beiden Waende.
- **Handschaetzung** (Verzweigungspunkt-Naeherung, Faktor 2 bis 3):

| omega^2 | 0,500001 | 0,5001 | 0,51 | 0,55 | 0,6 | 0,7 | 0,8 | 0,9 |
|---|---|---|---|---|---|---|---|---|
| Gamma | ~1,8e-3 | 1e-5 bis 3e-3 (Interferenz) | ~1,3e-3 | ~1,2e-3 | ~8e-4 | ~2,6e-4 | ~5e-5 | 2e-6 bis 5e-6 |
| Lebensdauer | ~8e3 | ? | ~4e3 | ~3e3 | ~4e3 | ~9e3 | ~4e4 | ~3e5 bis 6e5 |
| **Formel im Code** (Quadratur, im lokalen Rauchtest ausgegeben; keine Messung) | 5,39e-3 | 1,92e-4 | 6,49e-3 | 4,96e-3 | 3,04e-3 | 9,65e-4 | 1,86e-4 | 6,97e-6 |
| Lebensdauer nach Formel (Q_Ball/Gamma) | 2,7e3 | 5,2e4 | 8,4e2 | 7,8e2 | 1,1e3 | 2,6e3 | 1,0e4 | 1,9e5 |

- **Nachtrag nach dem lokalen Rauchtest (30.09. ~02:52):**
  - Die Formel ist dieselbe wie oben; nur ihre Zahlen stehen jetzt fest.
  - Meine Handschaetzung lag bis zu fuenffach zu tief.
  - Die Interferenz-Delle bei 0,5001 ist echt: Sie liegt 30-mal unter den Nachbarn.
  - Bei 0,51 bis 0,6 verliert der Ball in T = 400 bis zu ein Drittel seiner Ladung; er schrumpft dabei, und die
    Geradenanpassung mittelt ueber die Groesse.
  - V48a bleibt unveraendert (Verhaeltnis 0,5 bis 2).

- **Vorhersagen:**
  - **V48a:** Gamma_mess/Gamma_Formel liegt fuer alle 8 Groessen mit Gamma_Formel > 1e-5 zwischen 0,5 und 2. Die
    Grundlinie aus eps = 0 muss darunter liegen.
  - **V48b:** Gamma ist nicht monoton in Q. Die kleinen Baelle (0,8; 0,9) verdampfen mindestens 20-mal langsamer als
    die bei 0,55 bis 0,6. Die Lebensdauer waechst zu kleinen Baellen hin; "Altern" laeuft hier rueckwaerts.
  - **V48c (Gegenproben):** Kanal m = 1,2: |Gamma| < 0,01 * Gamma_Formel desselben omega; eps = 0: |Gamma| < 1e-7.
- **Einordnung der Idee:**
  - In 1D besteht die "Oberflaeche" aus zwei Punkten. "Rate ~ Oberflaeche" heisst hier: Gamma ungefaehr konstant fuer
    grosse Baelle, Lebensdauer ~ Q ~ R.
  - V48b sagt: Das gilt hoechstens fuer die grossen Baelle, und auch dort mit Interferenzwellen.
- **Quellenhinweis (Fable-Review):** Cohen, Coleman, Glashow, Georgi 1986 behandeln Verdampfung in masselose Fermionen;
  die Oberflaechengrenze kommt dort vom Pauli-Prinzip [L, aus dem Gedaechtnis, nicht nachgelesen]. Unser Kanal ist
  bosonisch; die Bindung an die Oberflaeche kommt hier aus der Impulserhaltung. Vor einem formalen Schritt die Quelle
  lesen.
- **L3 im Code:** Gamma je masselosem Lauf.

### 2.5 tensid (Chemie 17): chi an der Wand

- **In 1D nicht sinnvoll pruefbar (Q_min-Teil):** Q_min gibt es in 1D nicht, jede Ladung hat einen Ball, und ebene
  Waende haben keinen Laplace-Druck. Die Wandspannung aendert Groesse und omega eines 1D-Balls nicht.
  - Kleinste sinnvolle Form: 3D radial mit zwei Feldern. Dazu wird das radiale Schiessen aus RUNDE-02 Test 4 auf
    (f, h) erweitert; dann Q_min mit und ohne chi.
  - Die Reifungsbremse braucht 3D mit vielen Tropfen.
- **1D prueft:** Sitzt chi an der Wand? Aendert es Breite und Energie der Wand?
- **Aufbau:**
  - Wirt psi omega^2 = 0,500001 (Waende bei +-5,13).
  - chi frei mit Masse 1, zwei Gauss-Pakete (Breite 1) an den Waenden, Amplitude A = 0,05 bzw. 0,15, Startfrequenz 0,95.
  - Kopplung amphiphil a = 1 bzw. 2.
  - Gegenproben: nackt (ohne chi), chi frei (ohne Kopplung), reine Dichte lam = -0,5 (gleiche Tiefe 0,5 wie a = 2,
    aber im ganzen Innern), anti (a = -1, abstossend in der Wand).
  - 8 Laeufe, T = 400, Fenster [T/2, T].
- **Messung:**
  - Wandanteil = C in ||x| - 5,13| < 2 durch C in |x| < 60; Innenanteil (|x| < 3,13).
  - Wandbreite w = Int_{x>0} 4 p (1 - p) dx mit p = S/S_max; Anker 2/sqrt(a0) = 2,828.
  - E, Q_psi, Q_chi; omega_psi und omega_chi aus Phasensteigungen.
  - Omega = E - omega_psi Q_psi - omega_chi Q_chi: grosskanonische Wandenergie; nackt 2 sigma = 0,70710.
  - E_ads = E - E_nackt - 1 * Q_chi: Energiegewinn gegen chi-Quanten in Ruhe.
- **Vorhersagen:**
  - **V17a:** Amphiphil (a = 1 und 2, beide A): Wandanteil >= 0,6; chi gehalten 0,3 bis 0,9.
  - **V17b:** omega_chi bei a = 1: 0,90 bis 0,97; bei a = 2: 0,75 bis 0,92.
  - **V17c:** E_ads < 0 und innerhalb 30 % von -(1 - omega_chi) Q_chi (gebundene lineare Mode). Das Absenken ist durch
    die Kopplung vorgegeben, also keine Messung der Idee; geprueft wird nur die Groesse.
  - **V17d:** Grosskanonisch fast nichts: |dOmega| < 0,3 |E_ads|. Eine lineare gebundene Mode hat E = omega Q und traegt
    zu Omega nichts bei; es bleibt ein Rest zweiter Ordnung. "Senkt die Wandenergie" haengt also an der Bezugsgroesse.
  - **V17e:** Die Wand wird breiter: dw > 0.
    - dw(A = 0,15)/dw(A = 0,05) zwischen 4 und 12 (~ gebundene Menge ~ A^2).
    - dw(a = 2) > dw(a = 1).
  - **V17f (Gegenproben):**
    - chi frei: Wandanteil < 0,2, dw = 0 auf 1e-6.
    - Dichte: Innenanteil >= 0,5, Wandanteil < 0,4.
    - anti: Wandanteil < 0,3.
  - **Kontrolle nackt:** Omega = 0,7071 auf 1e-3, w = 2,83 auf 1e-2.
- **L3 im Code:** Wandanteil (gegen "chi frei"), dw und E_ads je gekoppeltem Lauf.

### 2.6 kreuzen (Wellen 10): Nettobewegung eines Balls zwischen zwei Stroemungen

- **In 1D nicht sinnvoll pruefbar:**
  - Kreuzen braucht eine Kraft quer zur Stroemung (Auftrieb) und einen Kiel, der die Querbewegung sperrt. In 1D gibt es
    keine Querrichtung, und zwei Widerstandskraefte ergeben nur ein gewichtetes Mittel der beiden Stroemungen.
  - Zudem traegt ein Feld nicht zugleich einen hellen Ball und ein stabiles Medium: Im psi-Feld ist das Medium erst ab
    S > 2/3 stabil, und dort gibt es nur Dellen. Zwei Medien fuer einen psi-Ball brauchen also drei Felder.
  - **Kleinste sinnvolle Form:** 2D mit drei Feldern (Ball psi, "Wind" chi1, "Wasser" chi2, beide defokussierend wie
    in 1.3) oder 2D mit zwei Feldern und einem festen Kiel (Fuehrung in y).
- **1D-Baustein (dieser Unterbefehl):** Kraft eines stroemenden, stabilen Mediums auf einen ruhenden Ball, also die
  "Segelkennlinie". Durch Lorentz-Invarianz ist das dieselbe Frage wie ein bewegter Ball im ruhenden Medium.
- **Aufbau:**
  - psi-Ball omega^2 = 0,7 ruhend.
  - chi-Medium C0 = 0,1, U_chi = C + 0,5 C^2 (c_s = 0,2085), stroemend mit k = 2 pi n/300, u = k/omega_k.
  - Dichtekopplung lam = 0,1: Delle ~ lam S/(2 g4) ~ 37 %. Bei lam = 0,3 wird das Medium im Ballkern ganz verdraengt.
  - Laeufe: n = 0; +5 (u = 0,099 = 0,48 c_s); -5 (Spiegel); +8 (0,158 = 0,76 c_s); +16 (0,304 = 1,46 c_s);
    +29 (0,501 = 2,40 c_s); dazu n = +16 mit lam = 0 und mit lam = 0,3; Medium allein.
  - Periodische Box, 9 Laeufe, T = 300.
- **Messung:** Ballort (Maximum von S mit Parabel, periodisch entfaltet); v aus einer Geraden, a aus einer Parabel, beide
  auf [T/3, T]; C am Ball; C min/max.
- **Vorhersagen (Landau):**
  - **V10a:** n = 0: v = a = 0 bis auf Rundung (Symmetrie).
  - **V10b:** n = +-5 (0,48 c_s): kraftfrei, |a| < 2e-5, |v| < 0,01; v(-5) = -v(+5).
  - **V10c:** n = 8 (0,76 c_s): unsicher. Erwartet kraftfrei bei lam = 0,1 (schwaches Hindernis); ein 1D-Hindernis kann
    aber schon unter c_s dunkle Solitonen abgeben.
  - **V10d:** n = 16 und 29 (ueber c_s): Mitnahme in +x, a > 5e-5, v_Ende > 0,01. Bei n = 16 ist die Mitnahme mit
    lam = 0,3 staerker als mit 0,1.
  - **V10e:** lam = 0: v = a = 0 exakt.
  - **V10f:** Medium allein: C bleibt 0,1 auf 1e-9.
    - Nach dem lokalen Rauchtest berichtigt: C bleibt raeumlich gleichfoermig (C_max - C_min < 1e-6).
    - Der Absolutwert weicht um 6e-4 (grob) bzw. 1,5e-4 (fein) ab. Das ist der O(dt^2)-Fehler des Velocity-Verlet fuer
      eine Kreisbahn: Die Startgeschwindigkeit -i omega chi ist nicht die exakte diskrete Kreisbahn.
    - Dieselbe Groesse zeigt das "Atmen" ruhender Baelle in tests1d.py (1,4e-3 grob, 3,6e-4 fein).
- **Folgerung fuer die Idee:** Unter c_s uebt ein suprafluessiger "Wind" gar keine Kraft aus; ein "Segel" bekommt erst
  ueber der Schwelle Schub. Zwei Medien ergeben in 1D dann hoechstens ein gewichtetes Mittel.
- **Gegenprobe:** lam = 0, n = 0, Spiegel n = -5.
- **L3 im Code:** a und v je gekoppeltem, stroemendem Lauf. Fuer die kraftfreien Laeufe ist L3 bei Effekt ~0 nicht
  bestehbar; das ist dort kein Mangel, sondern das Ergebnis.

## 3. Latten (Vorschlag, die Leitung entscheidet)

| Latte | Zellkern | Raeuber-Beute | Mitochondrium | Altern | Tensid | Kreuzen |
|---|---|---|---|---|---|---|
| L1 kann scheitern | ja: "Huelle mit Loch" oder Bindung bei lam > 0 | ja: Pendeln fuer jeden Start (gegen z_c) | ja: Gast bei lam = -0,3, v = 0,2 entkommt oder zerfaellt | ja: Gamma monoton wachsend oder weit neben der Formel | teilweise: Belegung und Wand; die Energie ist vorgegeben | ja: Kraft unter c_s oder keine Kraft darueber |
| L2 Gegenprobe | lam = 0, m = 1 | eps = 0, getrennt | lam = 0 | Kanal mit Masse, eps = 0 | ohne Kopplung, reine Dichte, anti | lam = 0, n = 0, Spiegel |
| L3 Numerik | im Code: dK, dAbstand, t_Trennung | im Code: A, Periode | im Code: d_drin | im Code: Gamma | im Code: Wandanteil, dw, E_ads | im Code: a, v |
| L4 bekannt | teilweise: symbiotische Solitonen in Zweikomponenten-BEC; Kern-Huelle in Fallen | ja: Bose-Josephson-Paar, Selbstfang (Smerzi u. a. 1997; Raghavan u. a. 1999) | teilweise: Einfang einer Komponente in der anderen | teilweise: Strahlung von Q-Baellen/Oszillonen in leichte Moden; CCGG 1986 nur fuer Fermionen | teilweise: Tenside an Grenzflaechen in Mehrkomponenten-Kondensaten, Gibbs-Adsorption | ja: Landau-Kriterium; Stroemung am 1D-Hindernis (Hakim 1997; Pavloff 2002) |
| L5 Messbezug | nein | nein | nein | nein (Q-Ball-Dunkle-Materie nur als Bild) | nein | nein |

Literatur aus dem Gedaechtnis, nicht nachgelesen.
- Vorab ableitbare Kennzahlen sind als Kontrollen markiert: K = 1/m bei lam = 0; Q_psi + Q_chi und die Korrelation -1;
  E_ads < 0 per Konstruktion; v = 0 bei lam = 0 und n = 0.
- Schwellen und Klassen stehen in Code und Plan fest und werden nach dem Lauf nicht gelockert.

## 4. Aufruf (Leitung, auf der .69 ueber kleintest.sh)

Remote-Ordner /home/fmh/fmhc-physics-remote/runde5-r5d/ mit r5d.py darin.
- Das Programm braucht nur torch und schreibt nur in --out.
- CPU-Spuren brauchen `--geraet cpu`: kleintest.sh setzt dort CUDA_VISIBLE_DEVICES leer, `--geraet cuda` bricht
  ab.
- Mit `--geraet cpu` setzt der Code torch.set_num_threads(1), passend zu CPUQuota=100 %.

**Rauchtest** (alle sechs, Laufzeiten x 0,05), zuerst und auf beiden Geraetearten:

```
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5d-rauch r5d.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5d/rauch-cuda
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5d-rauchcpu r5d.py rauch --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5d/rauch-cpu
```

**Hauptlauf**, ein Aufruf je Idee, nur nach rc = 0 im Rauchtest (Spurvorschlag; jede Spur geht, siehe Laufzeiten):

```
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5d-rb r5d.py raeuber --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5d/raeuber
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5d-al r5d.py altern --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5d/altern
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b r5d-zk r5d.py zellkern --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5d/zellkern
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5d-mt r5d.py mitochondrium --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5d/mitochondrium
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5d-ts r5d.py tensid --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5d/tensid
cd /home/fmh/fmhc-physics-remote/runde5-r5d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5d-kz r5d.py kreuzen --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5d/kreuzen
```

- Ist p4000b gesperrt (WM-1-MB laeuft), dann zellkern auf p4000a nach altern oder auf cpu2.
- Der Rauchtest zeigt nur, ob alles durchlaeuft; seine Zahlen gelten nicht.
- **Hochrechnung:** jede gedruckte Stufenzeit des Rauchtests mal 20, plus 10 s Start. Ergibt ein Unterbefehl mehr als
  9 min, ihn nicht starten; die Leitung entscheidet.

## 5a. Lokaler Rauchtest (Finns Freigabe 30.09. 02:42), gemessen

- **Aufruf** (Laptop, nur CPU, 1 Thread):
  `CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 r5d.py rauch --geraet cpu --out lauf-lokal/r5d-rauch`
- **Ergebnis:** 30.09. 02:51:04 bis 02:51:41, **Dauer 34,8 s, rc = 0, keine Fehler.** Alle sechs Unterbefehle liefen
  grob und fein durch. py_compile ohne Befund.
- **Stufenzeiten** (Laufzeit x 0,05):

| Unterbefehl | grob + fein | Hochrechnung x 20 (Laptop-Kern) | .69-Kern (x 1 bis 2) |
|---|---|---|---|
| zellkern | 1,2 + 4,9 s | ~2,0 min | 2 bis 4 min |
| raeuber | 1,2 + 5,4 s | ~2,2 min | 2,2 bis 4,4 min |
| mitochondrium | 0,9 + 3,9 s | ~1,6 min | 1,6 bis 3,2 min |
| altern | 1,4 + 5,8 s | ~2,4 min | 2,4 bis 4,8 min |
| tensid | 1,2 + 4,7 s | ~2,0 min | 2 bis 4 min |
| kreuzen | 0,7 + 3,1 s | ~1,3 min | 1,3 bis 2,6 min |

- Die Schaetzung in Abschnitt 5 wird damit fuer die CPU bestaetigt: alle unter 5 min auf einem Kern.
- Die Rauchtest-Zahlen selbst gelten nicht, weil die Zeit zu kurz ist. Ausnahme sind die Formelwerte der Rate in
  "altern" (Abschnitt 2.4); sie sind keine Messung.
- Physik, Vorhersagen und Schwellen sind durch den Rauchtest nicht geaendert. Einzige Berichtigung: V10f (numerischer
  Nullpunkt, siehe dort).

## 5. Erwartete Laufzeit (Schaetzung, nicht gemessen)

Grundlage:
- tests1d.py auf der P4000: ~1,0 bis 1,3 ms je Verlet-Schritt mit einem Feld, also rund 40 us je Torch-Operation. Die
  Laeufe sind durch Kernelstarts begrenzt, grob und fein kosten je Schritt gleich viel.
- r5d.py hat ~67 Operationen je Schritt, also ~2,7 ms je Schritt auf der P4000.
- Ein CPU-Kern (ein Thread): ~2,5 ms je Schritt bei 9 x 3001 Punkten, ~5 ms bei 9 x 6001 Punkten.

| Unterbefehl | Laeufe | Schritte grob + fein | P4000 | CPU-Kern |
|---|---|---|---|---|
| rauch | alle | 5 % von allem | 0,5 bis 1 min | 1 bis 2 min |
| zellkern | 9 | 8000 + 16000 | 1 bis 2 min | 2 bis 4 min |
| raeuber | 9 | 10000 + 20000 | 1,5 bis 3 min | 2,5 bis 5 min |
| mitochondrium | 9 | 8000 + 16000 | 1 bis 2 min | 2 bis 4 min |
| altern | 11 | 8000 + 16000 | 1 bis 2 min | 2,5 bis 5 min |
| tensid | 8 | 8000 + 16000 | 1 bis 2 min | 2 bis 4,5 min (Energie bei jeder Messung) |
| kreuzen | 9 | 6000 + 12000 | 1 bis 1,5 min | 1,5 bis 3 min |

- Jeder Aufruf liegt auch in der oberen Schaetzung unter 10 min (RuntimeMaxSec 600).
- **Speicher:**
  - Groesstes Feld 11 x 6001 complex128 = 1 MB; alle Tensoren zusammen unter 0,1 GB.
  - Mit CUDA-Kontext unter 0,5 GB. Der Code deckelt den Torch-Speicher auf 1,5 GB und meldet den Hoechststand.

## 6. Welche Medium-Karten dieser Aufbau spaeter traegt (Bitte der Leitung; nichts davon gerechnet)

Grundlage ist ein psi-Ball im duennen, stabilen chi-Medium (1.3) mit Dichtekopplung lam; fuer Ladungsaustausch mit dem
Medium kommt eps dazu (Vakuum stabil fuer mc2 >= eps^2).

| Karte | mit diesem Aufbau | wie |
|---|---|---|
| Wellen 5 Rumpfgeschwindigkeit/Landau | ja, 1D | Ball bewegt durch ruhendes Medium; Kraft gegen v, Schwelle bei c_s (einstellbar ueber C0 und g4). Im Ein-Feld-Modell fehlt die Schwelle (Fable) |
| Wellen 6 Gleiten | ja, 1D | wie Wellen 5 bis u ~ 0,9; ist die Kraft ueber der Schwelle nicht monoton? |
| Wellen 7 Windschatten | ja, 1D | zwei psi-Baelle hintereinander im stroemenden Medium; Kraft auf den hinteren |
| Wellen 11 Fahrtwind | ja, 1D | bewegter Ball im ruhenden Medium gegen ruhender Ball im stroemenden Medium. Das Modell ist Lorentz-invariant; Gleichheit wird erwartet, eher Codeprobe als Physik |
| Wellen 3 Stokes | ja, 1D | Ball in einer laufenden Schallwelle des Mediums; Drift je Periode ~ a^2 |
| Wellen 8/9 Magnus, Flettner | nur 2D | m = +-1-psi-Ball im stroemenden chi-Medium; braucht den 2D-Code mit zweitem Feld |
| Wellen 14 Brechung | nur 2D | Dichtestufe im chi-Medium; in 1D nur Durchgang und Reflexion an einer Stufe |
| Bio 2 Osmose | ja, 1D, mit eps | Ladung fliesst nur ueber eps zwischen Ball und Medium. Reine Dichtekopplung haelt Q_psi fest (keine Osmose moeglich) |
| weitere | ja | Bio 21 Nische (Dichtegefaelle des Mediums), Chemie 9 Massenwirkung (mit eps), Chemie 20 Chromatographie (raues Medium) |

## 7. Ausgabedateien (im --out-Ordner)

- `r5d_<unterbefehl>_bericht.txt`: Tabellen je Stufe, L3-Zaehlung, Rechenzeiten; auch auf stdout
- `r5d_<unterbefehl>_ergebnis.json`: alle Kenngroessen, Laufliste, Fehlertexte
- `r5d_<unterbefehl>_reihen.pt`: Zeitreihen je Stufe (Spaltennamen gespeichert), x, Endprofile S und C

## 8. Grenzen

- **Nur im Rauchtest gelaufen** (lokal, CPU, Laufzeit x 0,05; Abschnitt 5a): Tensorformen und Messfunktionen laufen
  durch. Ungeprueft sind die Klassen-Logik bei voller Laufzeit, die periodische Entfaltung bei grossen Wegen in
  "kreuzen" und der CUDA-Pfad.
- **Anfangsfelder sind keine exakten Loesungen des gekoppelten Systems:** Zwei Baelle am selben Ort bzw. ein Ball im
  Medium starten angeregt. Deshalb werden alle Groessen erst ab T/6 bis T/2 ausgewertet.
- **Zwei-Moden-Bild (raeuber) und Formel (altern) sind Naeherungen erster Ordnung.** Die Zahlen darin tragen einen
  Faktor 1,5 bis 3.
- **Feine Stufe:** Wie in tests1d.py halbiert sie dx und dt zugleich. Nur dt: in stufen_rechnen `DX * FEIN` durch `DX`
  ersetzen (eine Stelle).
- **Allgemein:** 1D, explorativ. Zellkern, Mitochondrium und Tensid sagen nichts ueber 3D-Schalen, Laplace-Druck oder
  Q_min.

## Einfach gesagt

Wir geben dem Q-Ball ein zweites Feld als Partner, einmal als zweite Ballsorte, einmal als duennes, ruhiges Medium
drumherum. Damit pruefen wir sechs Bilder aus Biologie, Chemie und Segeln: ob ein Ball einen Kern bildet, ob zwei
Sorten wie Raeuber und Beute schwanken, ob ein kleiner Ball in einem grossen wohnen kann, ob ein Ball langsam
verdampft, ob sich ein Stoff wie Seife an seine Haut setzt und ob eine Stroemung ihn mitnimmt. Nach der Papierrechnung
halten die Bilder nur zum Teil: Die Bestaende pendeln nur bei fast gleicher Verteilung, sonst bleiben sie stecken; die
kleinsten Baelle verdampfen am langsamsten; und unter einer Schallgeschwindigkeit schiebt die Stroemung gar nicht.
Jede Rechnung dauert auf einer Grafikkarte oder einem Prozessorkern nur wenige Minuten; gerechnet ist noch nichts.

Ende der ersten Fassung: 2026-09-30 02:29:14 CEST (gemessen mit date). Code und Plan ungetestet; nichts gerechnet.
Nachtrag nach dem lokalen Rauchtest (Abschnitt 5a, Formelwerte in 2.4, V10f berichtigt): 2026-09-30 02:57:14 CEST (gemessen mit date).
