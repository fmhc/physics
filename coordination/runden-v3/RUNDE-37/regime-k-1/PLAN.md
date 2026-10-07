# REGIME-K-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 48)

- Start 2026-10-05 11:41:02 CEST (date). Plantext ab 12:06:15 CEST (date), vor jedem Rauchtest und vor jeder Rechnung.
  Zeitbox 150 min ab Start.
- Grundlage: KARTE.md (RK0 bis RK3, Wortlaut, Schwellen und Wahrscheinlichkeiten unveraendert).
- Gelesen: KARTE.md; pachner-takt-1/ (KARTE, PLAN, ERGEBNIS, code/pt.py); regge-kinetik-l/DOSSIER.md;
  lund-regge-masse-1/ERGEBNIS.md (Abschnitte 1 bis 5); tt-iso-1/KARTE.md und ERGEBNIS.md (Abschnitte 1, 2);
  nach dem Projekt-grep (1.1) zusaetzlich RUNDE-36/regge-4d-1/ (KARTE, ERGEBNIS, PLAN Abschnitt 4).
- Kennzeichen: [M] Mathematik (vorab ableitbar), [S] an der Quelle gelesen, [P] Projektdatei, [E] hier gerechnet,
  [F] Festlegung dieses Plans, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.
- Alles synthetische Gitterrechnung, keine Messdaten, keine Messdatenbestaetigung.

## 1. Vorab

### 1.1 Projekt-grep (Pflicht, mit den Ausschluessen)

- In pachner-takt-1 und regge-kinetik-l (11:41:41 CEST):
  - "Fierz": kein Treffer.
  - "Bloch": ein Treffer, regge-kinetik-l/DOSSIER.md Z. 277 (Lund-Regge-Masse M_LR(k) im Regime H mit Bloch-Phasen
    wie in ops()); keine 4D-Regge-Dispersion.
  - "Dispersion": nur Suchbegriffe von Abrufen (ARBEITSFELD F5, F7; quellen/F5, F13) und DOSSIER Z. 413
    ("Fuer Dispersion und Abstrahlung zaehlt das Zweite"); keine Rechnung.
  - Die Kartenaussage "in diesen zwei Ordnern ohne Treffer zur Sache" ist bestaetigt.
- **Erweitert (runden-v3, "Rocek"):** RUNDE-36/regge-4d-1 (REGGE-4D-1, Runde 36) hat die Bloch-Hesse-Matrix der
  linearisierten 4D-Regge-Wirkung auf dem **Kuhn-Wuerfelgitter** gerechnet [P]:
  - effektive Form auf h nach Schur = c k^2 (P2 - 2 P0s) mit c = 0,2499 (Erwartung 1/4) fuer H = -Hesse(S);
  - Spin-2-Werte richtungsgleich auf 0,034 % / 0,14 % / 0,55 % bei |k| = 0,05 / 0,1 / 0,2 (waechst wie k^2);
  - Verhaeltnis konform zu Spin 2 = -2 (0,02 % bei 0,05);
  - eine fuenfte Nullmode je k (tote Hyperdiagonale, Thales-Mechanismus; Rocek/Williams' "fifth zero mode" [S dort]).
  - Die Kartenzeile "Im Projekt ist keine Bloch-Dispersion einer 4D-Regge-Wirkung gerechnet" stimmt also nur fuer die
    zwei genannten Ordner. Fuer das Kuhn-Gitter ist die Isotropie bei kleinem k Projektbefund [P]; fuer das
    Zeltstangen-Gitter auf B1 ist nichts gerechnet.
- Folge fuer diese Karte: Das Kuhn-Gitter wird **Pipeline-Kontrolle PK** (Abschnitt 5). Es prueft die ganze Kette
  (Geometrie, Bloch-Phasen, Eichreduktion, Schur, TT-Zerlegung, Normierung) gegen einen Projektbefund.

### 1.2 Ableitbarkeit (verkettet, je Vorhersage)

- **RK0:** Flachheit ist fuer eine echte Einbettung in R^4 vorab sicher [M] (Kontrolle). "Genau 16 Nullmoden" ist nicht
  ableitbar: Das Kuhn-Gitter hat eine tote Kante (rechte Winkel an allen Dreiecken der Hyperdiagonale) [P]. Ob das
  Zeltstangen-Gitter tote Kanten oder andere Zusatznullmoden hat, zeigt erst die Rechnung. Schreibtisch: Zeltstange
  v-v' mit Nachbar w bei Hoehe h_w (Hub 1, raeumlicher Abstand^2 = 1/2): (v - w).(v' - w) = 1/2 - h_w (1 - h_w) > 0,
  also dort kein rechter Winkel [M]; die anderen Kantenarten sind nicht am Schreibtisch geprueft.
- **RK1:** nicht ableitbar. FFLR nur Abstract [S, ueber REGGE-KINETIK-L]; REGGE-4D-1 zeigt es fuer ein anderes Gitter
  (Kuhn, eine Ecke je Zelle, inversionssymmetrisch) [P]. Das B1-Zeltstangen-Gitter hat vier Ecken je Zelle und ist
  vermutlich nicht inversionssymmetrisch (2.6).
- **RK2:** bedingt ableitbar: Trifft RK1 ein, ist fuer die gerade Form (3.4) eine fuehrende Korrektur in (kl)^2 zu
  erwarten [M]; offen bleiben ein verschwindender (kl)^2-Koeffizient und grosse (kl)^4-Terme im Fenster 0,05 bis 0,2.
  Ohne RK1 waechst die Spanne nicht wie eine Potenz (endlicher Grenzwert).
- **RK3:** nicht ableitbar; folgt aus FFLR fuer jedes Gitter, falls FFLR fuer beide Gitter gilt (die gestreckte Fassung
  ist ein anderes Gitter, keine Isometrie).

## 2. Gitter [F, M]

### 2.1 Raum: B1-Kopie (Begruendung der Wahl)

- B1 statt V: Fuer B1 gibt es Netz und Zeltzug-Konstruktion in pt.py (PACHNER-TAKT-1, dort flach und mit positiven
  4-Volumen gerechnet [P]). Fuer V muesste eine 4D-Hubfolge der Fuellecken erst entworfen werden; das passt nicht in
  die Zeitbox. B1 ist Finns Netz (eine der zwei Kopien); FFLR spricht von "any lattice", also ist B1 ein fairer Test.
  V bleibt offen.
- Ecken: fcc, vier Klassen 0, X, Y, Z (kubische Untergitter, pt.PAR2KL) an (0,0,0), (0,1/2,1/2), (1/2,0,1/2),
  (1/2,1/2,0); kubische Kante 1, Stablaenge 1/sqrt2. Tetraeder je kubischer Zelle: 4 tet1, 4 tet2, 4 Oktaeder je in
  4 Tetraeder (Diagonale wie pt.Netz, Variante TT/C2: Oktaeder mit Grundklasse M traegt die Diagonale der Klasse
  max(M+1, M+3 mod 4)). Die 24 Tetraeder je Zelle werden aus pt.Netz(2) gelesen und modulo Z^3 normiert (Kontrolle:
  24 Klassen, je 8-mal).

### 2.2 Zeit: Zeltstangen als periodische Treppen-Triangulierung

- Ein Takt hebt jede Ecke einmal um tau (Zeltstange), Klassenfolge 0, X, Y, Z, Klassenhoehen tau (0, 1/4, 1/2, 3/4),
  wie PACHNER-TAKT-1 (TT). Danach ist die Flaeche dieselbe, um tau e_t verschoben: periodisch in der Zeit.
- Ueber jedem raeumlichen Tetraeder mit gehobener Reihenfolge v0 < v1 < v2 < v3 entstehen die vier 4-Simplizes
  S_j = {v0', ..., v_j', v_j, ..., v3} (j = 0..3). Jede Zwischenflaeche ist ein Graph ueber dem Tetraeder und hebt sich
  monoton, also kacheln die S_j das Prisma ohne Ueberlappung, fuer jede Reihenfolge [M]; Volumen je S_j = tau V_tet / 4.
- Reihenfolge innerhalb eines Tetraeders: Klasse zuerst; zwei Ecken derselben Klasse (Diagonalenden, Abstand 1 laengs
  einer Achse) von unten nach oben in Achsrichtung. Das ist eine translationsinvariante Gesamtordnung (Klasse, x, y, z
  lexikografisch), also auf jedem Tetraeder azyklisch und auf gemeinsamen Flaechen gleich [M].
- pt.py hebt innerhalb einer Klasse nach Eckindex. Im Inneren der Superzelle ist das dieselbe Reihenfolge; nur an
  Diagonalen ueber den Kastenrand kehrt sie sich um. Darum hat pt.py keine Translationsinvarianz der Einheitszelle;
  hier ist sie hergestellt. Kontrolle KP: Simplizes eines TT-Takts aus pt.py (n = 3) gegen dieses Gitter; erwartet:
  alle Simplizes ohne Randueberschreitung stimmen ueberein.
- Translationsgitter: kubisch Z^3 mal Zeit tau Z. Grundzelle: 4 Ecken, Zellvolumen V_c = tau.
- Zaehlung je Grundzelle [M]: Kanten = 2 E_Sigma + V = 2 x 28 + 4 = 60 (je raeumliche Kante zwei neue, je Ecke eine
  Zeltstange); 4-Simplizes = 4 x 24 = 96; Eichfreiheiten 4 x 4 = 16.
- Hintergrundlaengen: aus den Eckkoordinaten im euklidischen R^4 (x, y, z, t). Die Hintergrundmetrik ist in diesen
  Koordinaten delta_mu_nu.
- Flachheitspruefung: fuer jedes Dreieck (modulo Translation) Fehlwinkel = 2 pi - Summe der Diederwinkel aller
  anliegenden 4-Simplizes (pt.geometrie). Dazu: jedes Tetraeder genau zweimal (geschlossene Pseudomannigfaltigkeit),
  Summe der Betraege der 4-Volumen = V_c.

### 2.3 Varianten

- **B1-t1:** tau = 1 (Hauptgitter; RK0, RK1, RK2).
- **B1-t15:** tau = 1,5, alle Zeitkoordinaten mal 1,5 (Klassenhoehen und Hub) [F]. Lesart von "Zeltstangenhoehe x 1,5"
  als gleichmaessiger Lapse. RK0 (zusammen mit B1-t1) und RK3.
- **B1L-t15** (beschreibend, kein Urteil): Hub 1,5, Klassenhoehen fest 0 / 0,25 / 0,5 / 0,75 (nur die Stange laenger).
- **KW:** Kuhn-Wuerfelgitter mit derselben Treppenkonstruktion ueber dem 3D-Kuhn-Gitter, Hubfolge umgekehrt zur
  Inklusion (groesste Koordinatensumme zuerst); das ergibt genau die 4! = 24 Kuhn-Simplizes je Hyperwuerfel [M].
  Pipeline-Kontrolle PK.
- **KW2** (Codeprobe, beschreibend): dasselbe Kuhn-Gitter mit verdoppelter Zelle (2 Grundecken), damit auch Kanten
  zwischen verschiedenen Grundecken durch Eich- und Metrikabbildung laufen. Muss dieselben TT-Werte wie KW liefern.

## 3. Bloch-Hesse-Matrix und Zerlegung [M, F]

### 3.1 H(k)

- S = Summe_t A_t eps_t (euklidisch). Um flach: H_ee' = d^2 S / dl_e dl_e' = Summe_t (dA_t/dl_e)(d eps_t/dl_e')
  = -Summe_sigma M^sigma_ee' mit M^sigma aus pt.geometrie (Diederwinkel per komplexem Schritt, Heron) [P, pt.py].
- Kanten modulo Translation: 60 Klassen e, jede Kante = e + T. Bloch-Ansatz delta l_(e+T) = x_e exp(i k . R_T).
  H(k)_ee' = Summe_sigma Summe_(i,j in sigma) H^sigma_ij exp(i k . (R_Tj - R_Ti)); Phasen in allen vier Richtungen.
  Hermitesch; H(-k) = conj H(k).
- k ist der physikalische Wellenvektor in (x, y, z, t). kl mit l = mittlere Kantenlaenge der 60 (bzw. 15) Kantenklassen
  je Gitter [F].

### 3.2 Eichmoden und Nullmoden

- Eckverschiebung xi_b exp(i k . R_n) an Ecke (b, n): delta l_e = u_e . (xi_b2 exp(i k . R_d) - xi_b1) (u_e
  Einheitsvektor, d Gitterversatz der Kante). G(k): 60 x 16. Exakte Nullvektoren von H(k) bei flachem Hintergrund [M].
- Nullmoden: Eigenwerte mit |lambda| <= 1e-12 max|lambda| [F]. Luecke = kleinster Nicht-Null-Betrag / groesster
  Null-Betrag.
- Abgleich Nullraum gegen Eichraum: Rang G(k) (Singulaerwerte > 1e-10 s_max), ||H G||_max / (max|lambda| ||G||_max),
  und bei gleicher Dimension der groesste Sinus der Hauptwinkel zwischen Nullraum und Bild G.
- **Eichabzug:** Weiter wird im orthogonalen Komplement des numerischen Nullraums gerechnet (Z = Eigenvektoren mit
  |lambda| > Schwelle). Ist der Nullraum genau Bild G, ist das der Eichabzug. Tote Kanten (wie beim Kuhn-Gitter)
  fallen so mit heraus; sonst wuerde eine tote Richtung mit Metrik-Anteil die Schur-Form entarten [M].

### 3.3 Metrikabbildung und Fierz-Pauli-Zerlegung

- Glatte Metrikstoerung h_mu_nu exp(i k . x) gibt delta l_e = E_e^T h E_e / (2 l_e) an der Kantenmitte:
  x_e = (E^T h E / 2l) exp(i k . m_e) (Mittelpunktskonvention) [F]. h in einer Frobenius-orthonormalen Basis
  (10 Komponenten).
- Fierz-Pauli-Symbol der Hintergrundmetrik delta (euklidisch) [M]: Eichrichtungen k xi + xi k (4, Eigenwert 0);
  transversaler Raum (k.h = 0, 6-dim) = 5 TT (spurfrei) + 1 Spurrichtung P_k/sqrt3 (konform). Fuer S = 1/2 Int sqrt(g) R
  (Regge-Normierung) erwartet je Zellvolumen und k^2: TT -1/4, konform +1/2, Verhaeltnis -2 (Vorzeichen fuer
  H = Hesse(S); REGGE-4D-1 zaehlt mit -Hesse und findet +1/4 [P]).
- T(k): 10 x 6, Frobenius-orthonormale Basis der transversalen Tensoren, Spalte 0 = Spurrichtung, 1..5 TT.
- B = Z^H P(k) T (Metrik-Anteil im eichreduzierten Raum); C = orthonormales Komplement von Bild B im reduzierten Raum.
- **Schur-Form** (Gittermoden ausintegriert, Rocek/Williams-Weg):
  M6 = B^H H B - B^H H C (C^H H C)^+ C^H H B (6 x 6, in den Koordinaten a mit h = T a).
  Pseudo-Inverse ueber Eigenwerte > 1e-12 max|lambda|; Zahl verworfener Richtungen wird gezaehlt.
  Die fuehrende Ordnung k^2 von M6 haengt nicht von der Wahl des Komplements oder der Phasenkonvention ab [M:
  Aenderungen wirken wie B -> B S(k) + C F(k) mit S = 1 + O(k); der C-Teil verschiebt nur die Minimierungsvariable].

### 3.4 Gerade und volle Form; Messgroessen

- Wegen H(-k) = conj H(k) ist M6(-k) = conj M6(k), also M6 = gerader Realteil + i ungerader Imaginaerteil [M].
  Konventionsaenderungen (Phasenbezug, Komplement) aendern den Realteil erst relativ in O((kl)^2), den Imaginaerteil
  schon in O(kl); in einem fast entarteten TT-Quintett spaltet ein Imaginaerteil die Werte schon in O(kl) auf [M].
  Darum [F]:
  - **"gerade" (Hauptgroesse):** Eigenwerte von Re M6.
  - **"voll" (fuer den Kartenwortlaut):** Eigenwerte der hermiteschen M6.
  - **"affin" (beschreibend):** Re(B^H H B) ohne Ausintegrieren.
- Zuordnung: Der Eigenvektor mit dem groessten Gewicht auf der Spurrichtung (|a_0|^2) ist der konforme Modus; die
  uebrigen fuenf sind die TT-Eigenwerte, aufsteigend sortiert. Normierung: lambda / (|k|^2 V_c).
- **TT-Spanne** (wie TT-ISO-1 und LUND-REGGE-MASSE-1): max|w| / min|w| - 1 ueber alle Richtungen und die fuenf
  TT-Werte; nur definiert, wenn alle Werte dasselbe Vorzeichen haben (sonst "nicht definiert" = verfehlt).
- Weitere Werte je k: Imaginaeranteil max|Im M6| / max|Re M6|, kleinster Betrag im Gitterblock (C^H H C) relativ,
  Spur-Gewicht des konformen Modus und groesstes Spur-Gewicht eines TT-Modus, Hermitezitaet von H(k).

## 4. Raster und Regeln [F]

- **Richtungen (92 in 4D, davon 25 raeumlich):** 4 Achsen; 12 (e_mu +- e_nu)/sqrt2; 16 (+-1, +-1, +-1, 0)-Typ / sqrt3
  (Null an jeder Stelle, Vorzeichen modulo Gesamtvorzeichen); 8 (1, +-1, +-1, +-1)/2; 40 Zufallsrichtungen in 4D und
  12 raeumliche Zufallsrichtungen (numpy default_rng(20261005), Normalverteilung, normiert). Raeumlich = t-Komponente 0:
  3 Achsen, 6 Flaechendiagonalen, 4 Raumdiagonalen, 12 zufaellige. Zeitrichtung = e_t.
- **kl-Raster:** 0,005; 0,01; 0,02; 0,03; 0,05; 0,07; 0,1; 0,14; 0,2.
- **Extrapolation "Spanne bei kl -> 0":** je Richtung und TT-Index (aufsteigend) Ausgleich w(x) = w0 + w2 x^2 + w4 x^4
  ueber x = kl in {0,005; 0,01; 0,02; 0,05; 0,1} (kleinste Quadrate); s0 = Spanne der w0. Fuer "voll" mit
  w0 + w1 x + w2 x^2 + w3 x^3 (ungerade Terme moeglich), sonst gleich. Raeumliche Spanne s0_raum: nur die 25
  raeumlichen Richtungen.
- **Exponent (RK2):** Spanne s(x) je kl ueber alle Richtungen und TT-Werte; p = Steigung der Ausgleichsgeraden von
  log s gegen log x ueber x in {0,05; 0,07; 0,1; 0,14; 0,2}. Beschreibend: lokale Steigungen; Steigung von s - s0.
- **Steifigkeitsverhaeltnis (RK3):** R = Mittel der fuenf extrapolierten TT-Werte bei k || e_t geteilt durch das Mittel
  ueber die 25 raeumlichen Richtungen (je fuenf). In physikalischen Koordinaten sagt "nur ueber die Hintergrundmetrik"
  R = 1 voraus (gleichwertig: in Gitterkoordinaten 1/tau^2) [M].

## 5. Urteilsregeln (mechanisch in code/rk.py, Modus auswertung)

- **PK (Pipeline-Kontrolle, Kuhn-Gitter KW):** bestanden genau dann, wenn s0 (gerade) < 1e-6, Mittel der w0 auf 1e-3
  gleich -1/4 und konform/TT auf 2e-3 gleich -2 (reproduziert REGGE-4D-1 [P]). Faellt PK, lauten RK1 bis RK3 nach Plan
  und Karte "unklar (Pipeline)"; die Werte werden trotzdem berichtet.
- **RK0** ("Das periodische 4D-Zeltstangen-Gitter ist flach (Innen-Fehlwinkel <= 1e-12). Die Bloch-Hesse-Matrix H(k)
  hat an jedem gerechneten k ungleich 0 genau 4 Nullmoden je Ecke der Grundzelle (Eckverschiebungen in 4D)"):
  eingetroffen genau dann, wenn fuer B1-t1 **und** B1-t15 gilt:
  - max |Fehlwinkel| <= 1e-12;
  - an allen 92 x 9 = 828 k je Gitter: genau 16 Nullmoden, Luecke >= 1e3, Rang G = 16, ||H G|| rel <= 1e-12,
    Sinus Nullraum/Eichraum <= 1e-6.
  - Nach Plan = nach Kartenwortlaut.
- **RK1** ("Fuer kl -> 0 naehert sich der Nicht-Null-Teil von H(k) dem Fierz-Pauli-Symbol der Hintergrundmetrik: Die auf
  k^2 normierten physikalischen (TT-)Eigenwerte haben ueber mindestens 50 Richtungen in 4D eine Spanne, die
  extrapoliert unter 1e-6 liegt"), B1-t1:
  - Nach Plan: eingetroffen genau dann, wenn s0 (gerade, 92 Richtungen) < 1e-6.
  - Nach Kartenwortlaut: eingetroffen, wenn s0 (gerade) und s0 (voll) < 1e-6; nicht eingetroffen, wenn beide nicht;
    sonst "unklar" (die Karte legt die Form nicht fest).
- **RK2** ("Die fuehrende Richtungsabhaengigkeit ist O((kl)^2): Die Spanne waechst zwischen kl = 0,05 und 0,2 mit einem
  Exponenten 1,8 bis 2,2"), B1-t1:
  - Nach Plan: eingetroffen genau dann, wenn p (gerade) in [1,8; 2,2].
  - Nach Kartenwortlaut: wie RK1 mit p (gerade) und p (voll).
- **RK3** ("Wird sie um den Faktor 1,5 geaendert, bleibt die extrapolierte raeumliche Spanne unter 1e-6, und das
  Verhaeltnis der zeitlichen zur raeumlichen Steifigkeit folgt der Metrik auf 1e-6"), B1-t15:
  - Nach Plan: eingetroffen genau dann, wenn s0_raum (gerade) < 1e-6 und |R - 1| <= 1e-6.
  - Nach Kartenwortlaut: wie RK1 mit beiden Formen.

## 6. Kontrollen (technisch; gehen nur ueber PK in Urteile ein)

- Geometrie: Schlaefli und Symmetrie von M^sigma (pt.geometrie) <= 1e-12; Kantenlaengen aus pt.geometrie gleich den
  kanonischen; Pseudomannigfaltigkeit (jedes Tetraeder zweimal); Summe |Vol| = V_c; Simplizes paarweise verschieden;
  tote Kanten (alle lokalen Hesse-Zeilen null) aufgelistet.
- Hermitezitaet von H(k) vor dem Symmetrisieren.
- k = 0: Nullmoden (erwartet B1: 10 Metrik + 12 innere Verschiebungen = 22 [M]; KW: 10 + tote Hyperdiagonale = 11
  [P]); H(0) P(0) = 0 (konstante Metrik bleibt flach); Rang [P(0), G(0)].
- Superzelle: reelle periodische Hesse-Matrix auf 2 x 2 x 2 x 2 Zellen gegen die Vereinigung der Bloch-Spektren an den
  16 passenden k (prueft die Phasenbuchhaltung).
- KP: pt.py-Takt (n = 3, TT) gegen das Treppengitter (2.2).
- KW2 gegen KW: gleiche TT-Werte (Codeprobe fuer Kanten zwischen verschiedenen Grundecken).

## 7. Laeufe auf der .69

- Ordner /home/fmh/fmhc-physics-remote/regime-k-1/ (code/, rauch/, lauf/). Aufruf ueber
  /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu2, cpu3, cpu4; je Lauf <= 600 s, 1 Thread, 4 GB.
- Hauptlaeufe: B1-t1 (mit KP), B1-t15, KW, KW2, B1L-t15 (Modus gitter); danach auswertung.
- Rauchtests (je <= 120 s, 6 Richtungen, volles kl-Raster): nur Laufzeit, Rueckgabewert, Schluessel und technische
  Kontrollen ansehen. Fuer B1 werden **keine** Fehlwinkel, Nullmoden-Zahlen, ||H G||, H(0) P(0), Spektren,
  TT-Werte oder Urteile gelesen (RK0 bis RK3). Fuer KW und KW2 (keine Kartenvorhersage) darf alles gelesen werden;
  das ist Pipeline-Pruefung vor dem Einfrieren und wird so berichtet.
- Danach PLAN.md und code/ als *.eingefroren-<zeit> kopieren, sha256 in EINGEFROREN-SHA256.txt (lokal und .69).

## 8. Agenten-Vorhersagen (vorab, gehen in kein Urteil ein)

| Nr | Vorhersage |
|---|---|
| A1 | RK0 eingetroffen: flach ~1e-15, ueberall genau 16 Nullmoden (keine tote Kante auf B1), 22 bei k = 0 (75 %) |
| A2 | PK bestanden (90 %) |
| A3 | RK1 nach Plan eingetroffen; TT-Mittel -1/4, konform/TT -2 auf 1e-4 (65 %) |
| A4 | Imaginaerteil von M6 ungleich null (B1 ohne Inversionssymmetrie), relativ ~ kl (60 %) |
| A5 | RK2 nach Plan eingetroffen, falls A3; "voll" mit kleinerem Exponenten (Aufspaltung in O(kl)) (45 %) |
| A6 | RK3 nach Plan eingetroffen (60 %) |

## 9. Rauchtests (vor dem Einfrieren; Spur cpu2, alle rc = 0, je unter 2 s)

- **r1** (10:07:58 bis 10:07:59 UTC, rk.py e0fbe694...): KW, 6 Richtungen, volles kl-Raster. Alles gelesen
  (Pipeline-Pruefung): NE = 15, S = 24, 50 Dreiecke, 4 bis 6 Simplizes je Dreieck, jedes Tetraeder zweimal, flach
  1,8e-15, Summe |Vol| = 1, tote Kante = Hyperdiagonale (1,1,1,1); k = 0: 11 Nullmoden; je k 5 Nullmoden, Rang G = 4,
  ||H G|| <= 3,4e-15; Superzelle 8,9e-16; TT -0,25 und konform +0,5 mit Abweichungen wie (kl)^2; Imaginaerteil
  <= 3,7e-13. Das reproduziert REGGE-4D-1 [P] (dort ebenfalls 1,8e-15, 50 Dreiecke, 11 Nullmoden bei k = 0).
  Aenderung danach: HG0 = None, wenn G(0) = 0 (KW: eine Ecke je Zelle), statt Division durch null.
- **r2** (10:08:26 bis 10:08:29 UTC, rk.py afd77889...): KW2 (alles gelesen: 10 Nullmoden je k = 8 Eich + 2 tote
  Hyperdiagonalen, Rang G = 8, ||H G|| 1,1e-16; TT gleich KW auf 5e-10 relativ) und B1-t1 mit KP. Bei B1 gelesen nur:
  NE = 60, S = 96, NV = 4, V_c = 1, 200 Dreiecke, 4 bis 6 Simplizes je Dreieck, 240 Tetraeder je zweimal, 96 Simplizes
  verschieden, Summe |Vol| exakt, kleinstes Volumen relativ 0,0137, Schlaefli 1,0e-15, M symmetrisch 1,0e-15, 24
  Tetraederklassen je 8-mal, Superzelle (2,1,1,2) 3,9e-15, Hermitezitaet 6,4e-16, KP: 2304 von 2592 pt-Simplizes,
  1300 von 1300 ohne Randueberschreitung (288 = 36 Randdiagonalen x 4 Tetraeder x 2 Simplizes, wie in 2.2
  erwartet), Laufzeit 1,6 s, Schluessel. **Nicht gelesen:** Fehlwinkel, tote Kanten, k = 0, Nullmoden, ||H G||,
  Spektren, TT-Werte.
- **r3** (10:09:01 bis 10:09:02 UTC, rk.py afd77889...): B1-t15 und B1L-t15 (nur rc und Laufzeit), Auswertung auf den
  Rauchdateien. Gelesen nur: Schluessel, PK und die KW-/KW2-Kennzahlen (KW: s0 = 1,3e-9, w0 = -0,25 auf 5e-11,
  konform/TT = -2 auf 5e-10, p = 2,001; PK bestanden). **Nicht gelesen:** alle B1-Kennzahlen und RK-Urteile.
- Kein Schwellenwert und keine Regel wurde nach r1 bis r3 geaendert.
