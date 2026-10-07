# HAGEDORN-1: Plan (Code-Agent, Runde 37)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 05:46:33 CEST (date). Plan geschrieben ab 06:13 CEST
  (date 06:12:37 direkt davor), vor dem Einfrieren; Einfrierzeit siehe PLAN.md.eingefroren-*.
- Explorativ (v3). Alles ist synthetische Rechnung im Modell M1 (2D), keine Messdatenbestaetigung.
- Kennzeichen: [M] Mathematik/eigene Herleitung, [S] an der Quelle gelesen, [L] Literatur aus dem Gedaechtnis,
  [L?] unsicher, [H] Hypothese.
- Karte: KARTE.md daneben. Vorhersagen HG0 bis HG4 und ihre Schwellen gelten unveraendert. Was die Karte offenlaesst,
  ist hier als **[Zusatz]** gekennzeichnet; Kartenfehler stehen in Abschnitt 4 mit Berichtigung und Urteil nach
  Kartenwortlaut.

## 0. Schreibtisch vorab

1. **HG4 ist vorab ableitbar.** Aus den RG-1-Zahlen (RUNDE-06/regge/lauf-lokal/h0005/ergebnis.json, mit jq um
   06:00 CEST gerechnet) liegt die doppelt-logarithmische Steigung von E gegen R_max bei festem omega^2 fuer jedes
   Paar aus m = 1, 2, 3, 5, 8 zwischen 0,99 und 1,07:
   - 0,55: 1,041 (m 1..8), 1,031 (2..8), 1,021 (3..8), 1,067 (1..2)
   - 0,70: 1,010; 1,011; 1,008; 1,008
   - 0,85: 1,005; 1,008; 1,006; 0,998
   - 0,95: 1,003; 1,007; 1,006; 0,995
   - 0,99: 1,003; 1,007; 1,005; 0,994
   - Folge: HG4 trifft ein, sobald es bei einem omega^2 mindestens zwei stabile Profile mit m >= 1 gibt. Neu ist nur
     die Auswahl der stabilen Profile. L1 fuer die Steigung selbst ist schwach.
2. **Profile = RG-1.** regge2d.py unveraendert (sha256 7e7f6667...892608, gleich RUNDE-06), h0 = 0,005. Der
   Profillauf auf der .69 (lauf/profile, 04:05 UTC, 29 s) gibt alle 30 Profile gueltig, Q und E wie RG-1
   (z. B. m = 0, omega^2 = 0,55: Q = 238,43228).
3. **Kontinuum** [M]: u laeuft im Unendlichen wie e^(-i(omega + Omega)t), v wie e^(-i(omega - Omega)t), also
   (Omega + omega)^2 >= 1 bzw. (Omega - omega)^2 >= 1. Luecke |Re Omega| < 1 - omega: 0,258 (0,55), 0,163 (0,70),
   0,078 (0,85), 0,025 (0,95), 0,005 (0,99). Duenne Ringe (omega^2 = 0,99) haben also fast keine Luecke; ihre
   Ringschwingungen liegen im Kontinuum.
4. **VK fuer m = 0:** Q(omega) faellt in RG-1 fuer m = 0 monoton ueber das ganze Raster (238 -> 24 -> 14,5 -> 12,4
   -> 11,8). Die VK-Regel sagt also an allen fuenf Stellen "stabil" voraus; die Kontrolle prueft nur diese Seite.
5. **N(E) beschreibend:** vorab ableitbar und nicht geurteilt (Karte). Nur falls Zeit bleibt.

## 1. Herleitung (BdG fuer Klein-Gordon) [M]

- Feldgleichung aus L = |phi_t|^2 - |grad phi|^2 - U(|phi|^2): phi_tt - Laplace phi + U'(|phi|^2) phi = 0.
  Stationaer f'' + f'/r - m^2 f/r^2 = (U'(f^2) - omega^2) f, U'(S) = 1 - 2S + 3S^2/2, U''(S) = -2 + 3S.
- Ansatz phi = e^(-i omega t) e^(i m theta) [f + eta], eta = u(r) e^(i l theta - i Omega t) + v*(r) e^(-i l theta + i Omega* t).
  - Zeit: phi_tt = e^(...)[eta_tt - 2 i omega eta_t - omega^2 (f + eta)]; Winkel: (d_theta + i m)^2.
  - Linear: U'(|f + eta|^2)(f + eta) = U' f + (U' + S U'') eta + S U'' eta*, S = f^2.
  - Koeffizient von e^(i l theta - i Omega t): -(Omega + omega)^2 u - D_(m+l) u + (U' + S U'') u + S U'' v = 0.
  - Koeffizient von e^(-i l theta + i Omega* t), konjugiert: -(Omega - omega)^2 v - D_(m-l) v + (U' + S U'') v + S U'' u = 0.
  - D_k = d^2/dr^2 + (1/r) d/dr - k^2/r^2.
- Mit L_pm = D_(m pm l) + omega^2 - U' - S U'' (wie im Auftrag), W = S U'', A = [[-L_+, W], [W, -L_-]] und
  G = 2 omega diag(1, -1):
  - Omega^2 x + Omega G x = A x, x = (u, v) (quadratisch in Omega, weil Klein-Gordon zweiter Ordnung in t ist).
  - Lineares Problem doppelter Groesse: y = Omega x, Omega (x, y) = [[0, 1], [A, -G]] (x, y). Groesse 4N.
- Symmetrien: M ist reell, also sind Omega und Omega* Eigenwerte. Sektor -l hat das Spektrum -Omega* von Sektor l
  ((u, v) -> (v*, u*)). l = 0 bis 12 deckt also -12 bis 12 ab.
- **Nullmoden** (Kontrolle der Vorzeichen und Faktoren):
  - l = 0, Phase: x0 = (f, -f), A x0 = 0, weil L_0 f = -W f aus der stationaeren Gleichung folgt.
  - Verallgemeinert: x1 = (f_omega, f_omega) mit A x1 = G x0 = 2 omega (f, f), denn (L_0 - W) f_omega = -2 omega f
    ist die omega-Ableitung der stationaeren Gleichung. Eine dritte Kettenstufe gibt es genau bei dQ/domega = 0
    (Loesbarkeit: <x0, x0 + G x1> ist proportional zu dQ/domega).
  - l = 1, Verschiebung: d_x phi gibt u = (f' - m f/r)/2, v = (f' + m f/r)/2 bei Omega = 0. Probe mit den
    Leiteroperatoren (d/dr -+ m/r) D_m = D_(m+-1) (d/dr -+ m/r): -L_+ u + W v = 0 und W u - L_- v = 0 exakt.
    Partner ist der Boost (nicht gerechnet).
  - **Folge fuer die Numerik:** Omega = 0 ist in l = 0 und l = 1 ein Jordan-Block der Laenge 2. Eine Stoerung delta
    (Rundung, Diskretisierung) verschiebt diese Eigenwerte um etwa sqrt(delta), reell oder imaginaer. Sie muessen
    erkannt und aus dem Stabilitaetsurteil genommen werden (Abschnitt 3.0), sonst erscheinen sie als Scheininstabilitaet.

## 2. Numerik

- **Raster (Karte):** m in {0, 1, 2, 3, 5, 8}, omega^2 in {0,55; 0,70; 0,85; 0,95; 0,99}, alle 30 Profile existieren;
  l = 0 bis 12.
- **Profil:** Schiessprofil aus regge2d.py (h0 = 0,005), kubisch-hermitesch (f, f') auf das Gitter gelegt, dann Newton
  auf derselben diskreten Gleichung (Rest <= 1e-12 oder Stillstand; Rest wird je Zeile berichtet). Damit ist die
  Phasenmode auf dem Gitter exakt.
- **Gitter:** versetzt r_j = (j - 1/2) h, j = 1..N, L = N h; zentrale Differenzen 8. Ordnung (9 Punkte) fuer d/dr und
  d^2/dr^2. Geisterpunkte r < 0 ueber die Paritaet (-1)^|k| der Winkelkomponente k (u: k = m + l, v: k = m - l), bei
  r = L ungerade Spiegelung (Dirichlet).
  - Schrittweite h (Basis): 0,10 (0,55), 0,11 (0,70), 0,15 (0,85), 0,25 (0,95), 0,50 (0,99); etwa ein Siebtel der
    kleinsten Profilskala (Wand ~0,7 bei 0,55/0,70; Ringbreite/4 sonst).
  - Kasten L = R_aussen + 12/kappa (kappa = sqrt(1 - omega^2); f(L) ~ e^-12 f_max). Fein: h/2, gleicher Kasten.
    Kastenprobe: L' = R_aussen + 18/kappa, gleiches h.
- **Eigenwerte:** je Zeile und l das volle Spektrum der dichten 4N-Matrix (LAPACK geev ueber scipy.linalg.eigvals,
  N = 217 bis 575, also n = 868 bis 2300).
  - Eigenvektoren per inverser Iteration (komplexe duenne LU, Verschiebung 1e-9 neben dem Eigenwert) fuer: die sechs
    betragskleinsten Eigenwerte in l = 0 und l = 1; alle mit Im > 1e-7 (hoechstens 120, groesstes Im zuerst); die
    reellen Kandidaten des Ringasts.
  - Feines Gitter: Shift-Invert-Arnoldi (scipy eigs, k = 6) am Basiseigenwert, naechster Eigenwert.
- **Weitere Groessen:** dQ/domega aus der diskreten Familie (J f_omega = -2 omega f, J = Newton-Jacobi-Matrix);
  E, Q, R_max aus dem Schiessen (= RG-1).
- **Code:** code/hagedorn.py (Profile, BdG), code/auswertung.py (Urteile, Bilder), code/regge2d.py (unveraendert).
  Lokal nichts ausgefuehrt; alle Laeufe ueber kleintest.sh auf der .69 (Spuren cpu und cpu6).

## 3. Urteilsregeln (vor dem Einfrieren)

### 3.0 Begriffe [Zusatz, vor dem ersten Rauchlauf im Code festgelegt, sha256 von hagedorn.py damals b6c2e9b9...778d]

- **Nullpaar (l = 0 und l = 1):** unter den sechs betragskleinsten Eigenwerten die zwei mit der groessten Ueberlappung
  |<x_ref, x>|/(|x_ref| |x|) (Gewicht r) mit x_ref = x0 (l = 0) bzw. Verschiebungsmode (l = 1). Nicht gewertet.
- **Randmode:** Anteil der Norm (Gewicht r, |u|^2 + |v|^2) in r >= R_aussen + 0,75 (L - R_aussen) groesser 0,1.
  Gilt als unechter Eigenwert am Gitterrand; nicht gewertet, aber je Zeile offengelegt.
- **Gezaehlt:** alle uebrigen Eigenwerte.
- **max Im** eines Profils: groesstes Im Omega der gezaehlten Eigenwerte ueber l = 0 bis 12 (Basisgitter).
- **Klasse:** "instabil", wenn max Im > 1e-4 (Karte HG1); "stabil", wenn max Im < 1e-6 (Karte HG2); dazwischen "grau".
  - Grauzone: weder stabil (fuer HG2, HG3, HG4) noch instabil (fuer HG1). Das ist der Wortlaut der beiden
    Kartenschwellen; keine weitere Regel.
- **Feinprobe:** Jeder gezaehlte Eigenwert mit Im > 1e-6 wird auf h/2 verfolgt. Ergibt das feine Gitter eine andere
  Klasse als das Basisgitter, heisst die Zeile "nicht konvergiert" (weder stabil noch instabil).
- **Kastenprobe (beschreibend):** die drei groessten gezaehlten Instabilitaeten je Zeile im Kasten L'. Kein Urteil
  haengt daran; Abweichungen werden berichtet.
- **Ringast:** je l unter den gezaehlten reellen Eigenwerten (|Im| <= 1e-6, Re > 0), aufsteigend, der erste mit
  Ringanteil >= 0,6. Ringanteil = Normanteil im Ringband {r : f^2 >= 1e-2 max f^2}.
  - Begruendung: Die Karte will die tiefste reelle Mode je l. Im endlichen Kasten liegen darunter aber diskretisierte
    Kontinuumsmoden (Kastenmoden), die ueber den ganzen Kasten verteilt sind (Ringanteil etwa Bandbreite/L, unter
    0,45 im ganzen Raster). Gebundene oder eingebettete Ringmoden sitzen am Ring.
  - Gibt es mehrere Aeste, waehlt die Regel stets den tiefsten lokalisierten. Ein Astwechsel zwischen l = 2 und 6
    zeigt sich dann als schlechte Anpassung, nicht als ausgelassener Punkt.

### 3.1 HG0 (Kontrollen)

- (a) Nullmoden **[Berichtigung, Abschnitt 4.1]:** Residuum |A x_ref|/|x_ref| (Gewicht r) der Phasenmode (l = 0)
  und der Verschiebungsmode (l = 1), gewertet im Innenbereich r <= R_aussen + 6/kappa, auf Basis- und feinem Gitter
  <= 1e-6 in jeder Zeile. Das Residuum ueber den ganzen Kasten wird mitberichtet.
- (b) Lesart nach Kartenwortlaut: groesster Betrag der Nullpaar-Eigenwerte (l = 0 und l = 1, Basis) <= 1e-6 in jeder
  Zeile. Wird als Zweiturteil berichtet.
- (c) Konvergenz **[Zusatz: welche Eigenwerte]:** relativ |Omega_h - Omega_(h/2)|/|Omega_(h/2)| <= 1e-4 fuer
  (i) den Eigenwert mit dem groessten Im jeder Zeile mit max Im > 1e-6 und (ii) die Ringast-Eigenwerte l = 2 bis 6
  jeder HG3-Zeile (stabil, m >= 2). Gibt es weder (i) noch (ii), gilt (c) als erfuellt.
- (d) VK: Fuer m = 0 an jedem omega^2 gilt Klasse "stabil" genau bei dQ/domega < 0 und "instabil" genau bei
  dQ/domega > 0. "grau" oder "nicht konvergiert" zaehlt als Verstoss.
- **HG0 eingetroffen**, wenn (a), (c) und (d) gelten; sonst nicht eingetroffen; fehlende Zeilen: nicht auswertbar.
  Zweiturteil nach Kartenwortlaut: (b), (c), (d).
- Beschreibend (Auftrag, nicht Karte): verallgemeinerte Nullmode, f_omega aus Differenzen in omega gegen die
  exakte diskrete Ableitung, und das Residuum |A x1 - G x0|/|G x0|.

### 3.2 HG1 (duenne Ringe zerfallen)

- Zeilen m in {3, 5, 8} und omega^2 in {0,95; 0,99} (sechs Profile).
- Eingetroffen, wenn alle sechs "instabil" sind; nicht eingetroffen, wenn eines "stabil" oder "grau" ist; sonst
  (fehlend oder nicht konvergiert, aber keines stabil oder grau) nicht auswertbar.

### 3.3 HG2 (dicke Ringe halten)

- Zeilen m in {1, 2, 3, 5, 8} und omega^2 in {0,55; 0,70} (zehn Profile).
- Eingetroffen, wenn mindestens eines "stabil" ist; nicht eingetroffen, wenn alle "instabil" oder "grau" sind; sonst
  nicht auswertbar.

### 3.4 HG3 (stringartig, wo stabil) [H]

- Zeilen: alle "stabilen" Profile mit m >= 2 (jedes omega^2).
- Je Zeile Anpassung Omega_l = a + b l an die Ringast-Eigenwerte l = 2 bis 6 (Basisgitter, kleinste Quadrate).
  Erfuellt, wenn R^2 > 0,98 und b > 0 (Karte). Linear in l heisst bei festem R auch linear in l/R.
- Nicht eingetroffen, wenn eine Zeile nicht erfuellt; eingetroffen, wenn es mindestens eine Zeile gibt und alle
  erfuellen; sonst (keine stabile Zeile mit m >= 2, oder fehlende Ringast-Werte) nicht auswertbar.
- Beschreibend: b R (Wellengeschwindigkeit laengs des Rings) je Zeile.

### 3.5 HG4 (Energie waechst mit der Ringlaenge) [H]

- Je omega^2 mit mindestens zwei "stabilen" Profilen mit m >= 1 (R = 0 bei m = 0): Steigung s der Anpassung
  ln E gegen ln R_max.
- Eingetroffen, wenn es mindestens ein solches omega^2 gibt und dort |s - 1| <= 0,15 gilt (bei mehreren: an allen);
  nicht eingetroffen, wenn ein solches omega^2 die Grenze reisst; sonst nicht auswertbar.
- Vorab ableitbar (Abschnitt 0.1): Vermerk im Urteil.

## 4. Kartenfehler und offene Punkte

1. **Nullmoden "auf <= 1e-6" (HG0):** Die Karte nennt kein Mass. Als Eigenwertbetrag gelesen ist die Grenze ungeeignet:
   Omega = 0 ist in l = 0 und l = 1 ein Jordan-Block (Abschnitt 1), der numerische Eigenwert waechst wie die Wurzel
   der Stoerung. Eine Diskretisierung mit Fehler 1e-10 gibt schon ~1e-5.
   - Berichtigung: gewertet wird das Residuum der bekannten Nullmode im diskreten Operator, Regel 3.1 (a). Das prueft
     Vorzeichen und Faktoren direkt.
   - Innenbereich statt ganzer Kasten: Nach den Rauchlaeufen r1/r2 festgelegt (Abschnitt R). Die Verschiebungsmode
     (f', f/r) erfuellt die Dirichlet-Spiegelung bei r = L nicht (f'(L) ~ kappa f(L) ~ e^-12). Das Residuum ueber den
     ganzen Kasten misst diesen Abschneidefehler: 6e-4 bis 2e-3, und es waechst bei Gitterverfeinerung (Faktor ~2,8
     je Halbierung, wie f'(L)/h^2). Mit dem BdG-Operator hat es nichts zu tun.
   - Urteil nach Kartenwortlaut: Regel 3.1 (b), wird mitberichtet.
2. **VK-Kontrolle einseitig:** Fuer m = 0 ist dQ/domega im Raster ueberall negativ (Abschnitt 0.4). Die Kontrolle kann
   nur an "stabil" scheitern. Kein Fehler, aber L1 schwach.
3. **HG4 vorab ableitbar** (Abschnitt 0.1).
4. **Schreibweise der Stoerung in der Karte:** "v(r) e^(i (m - l) theta) mit Zeitfaktor e^(-i Omega t)" gilt fuer v*,
   nicht fuer v (v* traegt e^(+i Omega* t)). Gerechnet wird mit dem Ansatz aus dem Auftrag (Abschnitt 1); am Urteil
   aendert das nichts.
5. **R fuer m = 0:** R_max = 0, daher geht m = 0 nicht in HG4 ein (ln R).

## 5. Laufplan

- Profile: lauf/profile (fertig, 04:05 UTC).
- Hauptlaeufe (je hoechstens 540 s Rechenbudget im Skript, Rest im naechsten Block):
  cpu: omega^2 = 0,55 (alle m); cpu6: 0,99; dann cpu: 0,70 und 0,85; cpu6: 0,95.
  Ausgabe /home/fmh/fmhc-physics-remote/runde37-hagedorn/lauf/haupt/, je Zeile eine JSON-Datei.
- Danach code/auswertung.py auf cpu -> lauf/auswertung/ (auswertung.json und drei Bilder), Kopie nach lauf-69/.

## R. Rauchlaeufe (vor dem Einfrieren, alles Gesehene)

Ausgaben auf der .69 unter runde37-hagedorn/rauch/ (r1 bis r5), Kopie in rauch-69/.

- **r1** (m = 1, omega^2 = 0,70 und m = 3, 0,99; l = 0 bis 2) und **r2** (m = 8, 0,55; l = 3), 04:06 UTC:
  - dichte Zerlegung n = 988: 1,2 s; n = 2300: 12,4 s.
  - Phasenresiduum ~1e-14.
  - Verschiebungsresiduum ueber den ganzen Kasten 5,8e-4 (m = 1, 0,70), 1,3e-5 (m = 3, 0,99), 6,3e-4 (m = 8, 0,55);
    auf h/2 groesser (1,6e-3; 3,7e-5; 1,8e-3).
  - Nullpaare: l = 0 bei 3e-8, l = 1 bei 1,6e-6 (m = 1, 0,70) bzw. 3,8e-8.
  - m = 1, 0,70: l = 1: 0,19678 + 0,05007 i; l = 2: 0,14339 + 0,13028 i. Beide ringlokalisiert (Ringanteil 0,91 bzw.
    0,99), auf h/2 und im groesseren Kasten gleich (relativ 7e-6 bzw. 2e-10).
  - m = 3, 0,99: Im 3,1e-3 (l = 1) und 4,9e-3 (l = 2). m = 8, 0,55: l = 3: Im 3,7e-3.
- **r3** (m = 0 bei 0,70, 0,55, 0,99; l = 0 bis 4): alle Eigenwerte reell (max Im = 0). Nullpaar l = 1 bis 3,6e-6.
  Verschiebungsresiduum im ganzen Kasten 1,1e-3 bis 4,2e-5.
- **Danach im Code geaendert:** Residuen zusaetzlich im Innenbereich (INNEN = 6); Auswertung wertet den Innenbereich.
- **r4** (m = 1, 0,70; m = 0, 0,55; m = 8, 0,99; l = 0 bis 2):
  - Verschiebungsresiduum innen 2,8e-8 / 4,2e-8 / 7,1e-10 (Basis), 1,2e-10 / 1,7e-10 / 2,9e-12 (h/2). Faktor ~250 je
    Halbierung, wie 8. Ordnung.
  - m = 8, 0,99: l = 1: Im 1,24e-3, l = 2: Im 2,01e-3.
  - Die Differenzenprobe der verallgemeinerten Nullmode sprang bei m = 8, 0,99 auf einen anderen Ast
    (dQ/domega aus Differenzen 2e7 gegen exakt -506).
- **Danach im Code geaendert:** Newton bei omega +- 1e-4 startet bei f +- 1e-4 f_omega.
- **r5** (l = 0): m = 8, 0,99 weiter falsch (Differenz -1,1e5 gegen -506), m = 1, 0,99 richtig (-71,99). Vermutung
  [H]: Nahe omega = 1 wird der Ast fast kritisch (kubische NLS in 2D), J ist fast singulaer; in l = 0 liegt bei
  0,99 ein reeller Eigenwert bei 1e-4 bis 6e-4. Die Probe ist nur beschreibend; keine weitere Aenderung.
- Schwellen der Karte und die Zusatzregeln 3.0 sind nach keinem Rauchlauf geaendert. Neu nach Rauchlaeufen ist nur
  das Mass "Innenbereich" in 3.1 (a), siehe Abschnitt 4.1.
- Die Rauchlaeufe zeigen schon jetzt Instabilitaeten in mehreren Ringen (auch m = 1 bei 0,70 und m = 8 bei 0,55,
  beide in der HG2-Menge). Die Urteile folgen allein aus den Hauptlaeufen.
