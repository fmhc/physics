# PAAR-LICHT-L: Arbeitsfeld (eine Datei, vor jedem Schritt neu gelesen)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-05 04:30:11 CEST (date). Zeitbox 50 min, also bis ca. 05:20.
- Karte KARTE.md bindend gelesen (04:30). PL1 bis PL4 unveraendert.
- Gelesen (nur lesen, 04:30 bis 04:34): licht-gleich-l/DOSSIER.md (Abschn. 1, 9, 10/G7, 12/O2, dazu der Rest),
  qca-tetra-1/ERGEBNIS.md (Ergebnis zuerst), diamant-nullstellen-1/ERGEBNIS.md (ganz), drei-kegel-neutrino-l/DOSSIER.md
  (Abschn. 1, 4), licht-finn-netz-1/ERGEBNIS.md (Abschn. 1 bis 4).
- Kennzeichen: [S Abschn./Gl.], [S Abstract], [S-lokal], [S-sek], [P] Projektdatei, [L], [L?], [M], [ES], [H].
- Abrufe: hoechstens 6. Gezaehlt wird jeder Netzabruf (curl auf export.arxiv.org bzw. arxiv.org), auch leere.

## 0. Projektzahlen, die ich brauche (aus den gelesenen Dateien) [P]

- Eis-Licht (Maxwell auf Finns Netz, M-D): Tempo 2,8284 (Code-Einheit), a2 = -1/12 (100), -5/48 (110), -1/9 (111),
  Form -1/8 + S4/24; keine Doppelbrechung bis (k l)^4 (licht-finn-netz-1 Abschn. 1, 3).
- FKM an X_z (t = 4 lambda): Tempo 2,8284 = t a, a1 = a3 = 0, a2 = -1/12 laengs, -1/3 quer, -17/48 (110 quer),
  -7/24 (110 schraeg), -1/3 (111) (diamant-nullstellen-1 Abschn. 4).
- a2_r(n) = -3/8 + S4/24 + n_r^4/4 (drei-kegel-neutrino-l Abschn. 4.2).
- a2 ist Phasenkoeffizient (omega/k = c (1 + a2 (k l)^2)), Gruppe 3 a2 (licht-finn-netz-1 Nachtrag).
- Weyl-Automat (D'Ariano/Perinotti 2014) auf BCC: c = 1/sqrt3, nur Klein-Gruppe, drei Verdoppler H, P, P'
  (qca-tetra-1, Ergebnis zuerst).
- Wilson-Dirac auf Finns Netz: 0,8165 (diamant-nullstellen-1 Tab. Abschn. 4).

## 1. Gegenlesen der Formabschnitte der Ableitbarkeitsprobe (nur gegenlesen) [M]

(wird unten gefuellt)

## 2. Abrufprotokoll (Erwartung vor dem Abruf, mit date)

### R1: arXiv-API, search_query=au:Bisio AND ti:light (Liste mit Abstracts)
- Erwartung eingetragen 2026-10-05 04:34:46 CEST (date), vor dem Abruf:
  - Treffer "Quantum cellular automaton theory of light" (Bisio, D'Ariano, Perinotti), arXiv 2014, Zeitschrift um 2016
    (Annals of Physics [L?]). Abstract nennt: Photon aus Paaren von Weyl-Feldern, Maxwell fuer kleine Wellenzahlen,
    frequenzabhaengiges Lichttempo, Abweichung von der Bose-Statistik, Hinweis auf moegliche Tests (Gammablitze bzw.
    Statistik). Kein Wort zu Wechselwirkungen.
- Ausgang R1 (04:34:50, quellen/R1-arxiv-api-bisio-light-20261005-043450.xml): **0 Byte**, rc = 0. Vermutlich
  Umleitung http -> https ohne -L (die Kopie von drei-kegel-neutrino-l zeigt https://arxiv.org/api als Antwortquelle).
  Kein Inhalt, Abruf zaehlt trotzdem (1 von 6). Eigener Bedienfehler, Selbstanzeige.

### R2: wie R1, aber https://export.arxiv.org/api/query mit -L
- Erwartung eingetragen 2026-10-05 04:35:04 CEST (date), vor dem Abruf: unveraendert wie R1.
- Ausgang R2 (04:35:07, quellen/R2-arxiv-api-bisio-light-20261005-043507.xml, 12 Eintraege, einschlaegig nur einer):
  arXiv:1407.6928v1 (nur v1), Bisio, D'Ariano, Perinotti, "Quantum Cellular Automaton Theory of Light",
  Annals of Physics 368 (2016) 177-190, doi 10.1016/j.aop.2016.02.009. Abstract woertlich (Auszug):
  "in the limit of small wave-vector k, the free Maxwell's equations emerge from two Weyl QCAs" / "the photon is
  introduced as a composite particle made of a pair of correlated massless Fermions, and the usual Bosonic statistics
  is recovered in the low photon density limit" / "dispersive propagation in vacuum, the occurrence of a small
  longitudinal polarization, and a saturation effect originated by the Fermionic nature of the photon" / "only the
  dispersive effects are accessible with current technology, from observations of arrival times of pulses originated
  at cosmological distances".
  - **Bestaetigt:** Paarbau aus zwei Weyl-QCA, Maxwell nur fuer kleine k, Dispersion, Bose nur naeherungsweise, Test
    ueber Laufzeiten. Kein Wort zu Wechselwirkungen.
  - **Verstoss V-a (gross):** "small longitudinal polarization". Ich hatte ein querpolarisiertes Maxwell-Feld erwartet.
    Der Paarbau gibt also nicht exakt Maxwell, sondern ein Feld mit kleinem Laengsanteil. Korrigierte Erwartung: Der
    Laengsanteil waechst mit k (wie stark: Volltext).
  - **Verstoss V-b (mittel):** Die Bose-Abweichung ist eine Saettigung bei hoher Photonendichte ("low photon density
    limit"), kein fester Anteil antisymmetrischer Zustaende. Die Labortests nach DeMille bzw. English messen einen
    festen Anteil; ob sie diesen Effekt ueberhaupt treffen, ist damit fraglich. Korrigierte Erwartung: Die Quelle nennt
    diese Tests nicht.
  - Version: Auf arXiv gibt es nur v1 (2014). Die Zeitschriftenfassung 2016 kann abweichen; ich lese v1.

### R3: arxiv.org/pdf/1407.6928v1 (Volltext, Kopie und pdftotext nach quellen/)
- Erwartung eingetragen 2026-10-05 04:35:33 CEST (date), vor dem Abruf:
  - Photonfeld als Integral ueber eine Verschmierungsfunktion f_k(q) mit zwei Weyl-Feldern bei k/2 -+ q, Pauli-Matrizen
    als Kopplung; fuer scharfe f folgt omega_gamma(k) = 2 omega_W(k/2), also langwellig dasselbe Tempo wie der
    Weyl-Automat (in Gittereinheiten 1/sqrt3 bzw. in deren Einheiten 1).
  - Kommutator [F, F^dagger] = delta - Delta, Delta ~ Fermionendichte im Traeger von f geteilt durch dessen Volumen;
    die Saettigung haengt an der Breite von f (frei) und an der Photonendichte.
  - Laengsanteil der Polarisation von der Ordnung k (Planck-Einheiten).
  - Einleitung zitiert de Broglie, Jordan, Kronig, Pryce, Perkins (Neutrino-Theorie des Lichts) (60 %).
  - Laufzeiten: Vergleich mit Fermi-LAT-Gammablitzen (GRB 090510) (60 %). Keine Bose-Tests an Photonen zitiert (60 %).
- Ausgang R3 (04:35:36, quellen/R3-bisio-dariano-perinotti-1407.6928v1-20261005-043536.pdf, sha256 8f36b093...,
  9 Seiten; pdftotext normal und -layout daneben). Gelesen: ganzer Text (Abschn. I bis VII, Anhang A, B, Literatur).
  - **Bestaetigt (je eine Zeile):**
    - Bau: zwei verschiedene Weyl-Automaten, psi mit A_k, phi mit A*_k = sigma_y A_k sigma_y; Bilinear
      G^mu_f(eta, theta, k) = int dq/(2pi)^3 f_k(q) eta^T(k/2 - q) sigma^mu theta(k/2 + q), int |f_k|^2 = 1;
      F^mu(k) = G^mu_f(phi, psi, k) [S Gl. (10)-(13)].
    - Scharfe Verschmierung ist Voraussetzung: int_{|q| >= qbar(k)} |f_k(q)|^2 << 1 fuer qbar(k) << |k| [S Gl. (20)].
    - Dispersion omega(k) = 2 |n_{k/2}| [S Gl. (43)], also genau 2 omega_W(k/2) (Weyl-Eigenphase |n_k| = lambda_k,
      Gl. (7)). Das ist die Kartenformel omega_gamma(k) = 2 omega_F(k/2), an der Quelle.
    - Langwellig Maxwell: 2 n_{k/2} ~ k/sqrt3, Gl. (27); mit x -> x sqrt3 l_P, t -> t t_P, c := l_P/t_P folgt
      Gl. (28), (29) (div E = div B = 0, d_t E = c rot B, d_t B = -c rot E) [S]. Tempo = Tempo des Weyl-Automaten.
    - Pryce [39] und Perkins [37, 38] zitiert, de Broglie [34], Jordan [35], Kronig [36] [S Abschn. I, Lit.].
    - Gammablitze zitiert: Abdo u. a. 2009 Nature 462, 331 [47]; Vasileiou u. a. 2013 PRD 87, 122001 [48] [S Abschn. VI].
    - Keine Bose-Symmetrie-Tests an Photonen zitiert (DeMille, English fehlen) [S Lit.-Liste].
  - **Verstoss V-c (gross): Das Lichttempo hat ein LINEARES Glied.** Gl. (44): c-+(k) ~ 1 +- 3 kx ky kz/|k|^2
    ~ 1 +- k/sqrt3 (laengs 111), Vorzeichen je nach Automat A+ bzw. A-, "not isotropic and can be superluminal" [S].
    Erwartet hatte ich eine k^2-Abweichung wie bei FKM. Grund [M]: Der Weyl-Automat ist chiral (keine Paritaet), die
    Kubik-Invariante kx ky kz ist erlaubt. Das ist dieselbe Lage wie W-D und Q-W in LICHT-FINN-NETZ-1 (a1 ungleich 0),
    nicht wie FKM (a1 = 0 wegen -X = X). Folge: Fuer Finns Netz ist a2_gamma = a2_F/4 nur dann das fuehrende Glied,
    wenn die Bausteine a1 = 0 haben (FKM ja).
    - **Nachrechnung von Hand [M], Ergebnis weicht ab:** cos lambda = cx cy cz +- sx sy sz mit Argument k/sqrt3.
      Mit p = k/sqrt3 (Impuls in Planck-Einheiten, folgt aus x -> x sqrt3 l_P): lambda(p) ~ |p| -+ |p|^2 nx ny nz.
      Probe laengs 111 direkt: d = cos^3 u +- sin^3 u, lambda ~ sqrt(3u^2 -+ 2u^3) = |p| (1 -+ |p|/(3 sqrt3)), trifft.
      Photon: omega(p) = 2 lambda(p/2) = |p| -+ (|p|^2/2) nx ny nz; Gruppentempo radial 1 -+ |p| nx ny nz.
      In k: 1 -+ kx ky kz/(sqrt3 |k|^2). **Gl. (44) hat 3 statt 1/sqrt3, also Faktor 3 sqrt3 = 5,2 mehr.** Laengs 111:
      meine Rechnung 1 -+ 0,19 E/E_P, Quelle 1 +- E/E_P. Moeglich: Fehler in v1, oder ich lese eine Konvention falsch.
      Nicht an der Zeitschriftenfassung geprueft. Fuer Schranken zaehlt das: mit Faktor 1 waere xi_max = 0,19.
  - **Verstoss V-d (gross): vier statt zwei bosonische Moden.** Gl. (37) gilt fuer i = 0, 1, 2, 3: zwei quere, eine
    "longitudinal" (e_k = n_{k/2}/|n_{k/2}|) und eine "timelike" (Skalar, sigma^0 = I) [S Abschn. V]. Die Autoren deuten
    alle vier als "4 independent Bosonic field modes". Aus Gl. (19) [M]: F^0 = F~^0 und der Anteil von F laengs n_{k/2}
    werden von Exp(-2i n_{k/2}.J t) nicht gedreht, haben also Frequenz 0 (bis O(qbar/|n|)). Zwei nicht laufende
    Zusatzmoden je k, in v1 nicht besprochen. Das ist genau das Gebiet des Pryce-Einwands (Querheit) [ES, L?].
  - **Verstoss V-e (gross): Die Saettigungsschaetzung zaehlt die falschen Moden [ES/M].** Quelle Abschn. VI: staerkster
    Laser "approximately an Avogadro number of photons in 10^-15 cm^3, whereas in the same volume on has around 10^90
    Fermionic modes". Zwei Punkte:
    1. 10^-15 cm^3 / l_P^3 = 1e-15 / 4,2e-99 = 2,4e83 Zellen, nicht 1e90 [M].
    2. Wichtiger: Nach Gl. (20) darf f_k nur in |q| < qbar(k) << |k| liegen. Die Zahl N_k der Moden in Omega_k
       (Gl. 36) ist dann hoechstens V |k|^3/(6 pi^2). Fuer optisches k ~ 1e5 /cm und V = 1e-15 cm^3: ~ 0,02, also
       weniger als eine Mode, gegen 6e23 Photonen. Das Kriterium M/N_k <= eps << 1 waere grob verletzt. Die 10^90
       zaehlen Moden bis zur Planck-Skala, die Gl. (20) gerade ausschliesst. [ES, grob; Gegenrechnung offen]
    - Folge: Die Bose-Abweichung haengt an qbar/k (frei), aber nicht frei nach oben: Gl. (21), (23), (24) haben Fehler
      O(qbar/|n_{k/2}|), Anhang A Gl. (A5) dazu ein mit t wachsendes Glied O((|a'|/|a|)^2 t). Kleine Bose-Abweichung
      (grosses qbar) und genaues Maxwell (kleines qbar) ziehen gegeneinander [S Gl. 20, 21, A5 + ES].
  - **Verstoss V-f (mittel): Pryce wird als Kommutator-Einwand zitiert.** "The failure of the neutrino theory of light
    was determined by the fact that a composite particle cannot obey the exact Bosonic commutation relations [39].
    However, as it was shown in Ref. [38], the non-Bosonic terms introduce negligible contribution at ordinary energy
    densities." [S Abschn. I]. Mein [L?]: Pryce betraf Querheit und Drehverhalten. Klaeren nur ueber Perkins (R4).
  - Zusatz [S Abschn. VI]: Laengsanteil theta ~ 2k, "10^-15 rad for a gamma-ray wavelength", waechst nicht mit der
    Laufstrecke. Planck-Verteilung: Abweichung nach Perkins [38] "less than one part over 10^-8" (so im Text).
  - Zusatz [S Abschn. V, Gl. (34) erste Zeile]: [gamma_ab(k), gamma_a'b'(k')]_- = 0 exakt. Zwei-Photonen-Zustaende sind
    also exakt austauschsymmetrisch [M]. Tests auf antisymmetrische Zwei-Photonen-Zustaende (DeMille, English [L?])
    sehen dann nichts; sie pruefen eine andere Groesse als die Saettigung [ES].
  - Korrigierte Erwartungen: PL1 nur teilweise (Maxwell mit Laengsanteil und zwei Zusatzmoden; lineares Tempoglied).
    PL3: freie Verschmierung ja, "Labor schliesst nicht aus" nur nach der Schaetzung der Autoren, die ich anzweifle.

### Zwischenrechnung vor R4 (Phasenraum der Bausteine) [M, ES, nach R3, vor R4]
- Gl. (36): Gamma = sum_q |f_k(q)|^2 psi^dagger psi, Kriterium <Gamma> <= eps << 1 [S]. Fuer ein breitbandiges
  Photonfeld mit Besetzung n je Mode, glatt auf der Skala 2 qbar: Ein psi-Modus bei p gehoert zu allen Photonmoden
  k' = 2(p - q'), q' in Omega, also zu 8 N Moden, jede mit Gewicht n/N. Folge: Besetzung des psi-Modus = 8 n.
  - Pauli verlangt 8 n <= 1; das Kriterium eps << 1 verlangt n << 1/8. Halber Impuls heisst Phasenraum / 8.
  - Schmalbandig (ein Lasermodus, Breite Delta k << qbar): Besetzung n (Delta k/qbar)^3, also n << (qbar/Delta k)^3
    mit qbar << k; als Dichte: rho_ph << qbar^3/(6 pi^2) < k^3/(6 pi^2) (optisch ~ 1,7e13 /cm^3).
  - Wenn das stimmt: Bose-Verhalten nur im klassischen Grenzfall n << 1, wo Bose-Statistik gar nicht zaehlt.
    Rayleigh-Jeans-Gebiet (CMB unter ~60 GHz n > 0,5; Radiofelder n >> 1) waere gesaettigt. [ES, ungeprueft]
  - Das ist meine Rechnung, keine Quelle. Kein "widerlegt" ohne Gegenlesen und 24-Monats-Suche (Feldregel 7).

### R4: arXiv-API, (au:Perkins AND ti:quasibosons) OR (au:Budker AND ti:Bose) OR (au:DeMille AND ti:photon)
- Erwartung eingetragen 2026-10-05 04:42:03 CEST (date), vor dem Abruf:
  - Perkins "Quasibosons" (2001/2002, IJTP 41, 823 = Bisio-Ref. [38]) auf arXiv (60 %); Abstract nennt Pryce und
    die Planck-Verteilung.
  - English, Yashchuk, Budker 2010 (PRL 104, 253604 [L?]): Schranke auf den Anteil austauschantisymmetrischer
    Zwei-Photonen-Zustaende um 4e-11 [L?] (55 %).
  - DeMille, Budker u. a. 1999 (PRL 83, 3978 [L?]): Schranke um 1e-7 [L?] (40 %, vielleicht nicht auf arXiv).
- Ausgang R4 (04:42:07, quellen/R4-arxiv-api-perkins-budker-demille-20261005-044207.xml, 6 Eintraege, 3 einschlaegig):
  - Bestaetigt: Perkins, "Quasibosons", hep-th/0107003, IJTP 41, 823-838 (2002): "existing experiments do not rule out
    the possibility that it [the photon] is also a quasiboson" [S Abstract]. Pryce und Planck nicht im Abstract.
  - Bestaetigt: English, Yashchuk, Budker, arXiv:1001.1771, PRL 104, 253604 (2010): "nu < 4.0 x 10^-11 at the 90%
    confidence level" fuer "Bose-Einstein-statistics-forbidden two-photon excitation in atomic barium" [S Abstract].
  - Bestaetigt (auf arXiv, besser als erwartet): DeMille, Budker, Derr, Deveney, physics/9906025, PRL 83, 3978 (1999):
    "probability v that photons are in exchange-antisymmetric states: v < 1.2 10^-7" [S Abstract].
  - Beide Tests messen einen Anteil austauschantisymmetrischer Zustaende. Nach Gl. (34) erste Zeile ist dieser im
    Paarbau exakt null (Erzeuger vertauschen exakt) [M]. Die Tests begrenzen den Paarbau also nicht [ES].

### R5: arxiv.org/pdf/hep-th/0107003v1 (Perkins, Quasibosons, Volltext)
- Erwartung eingetragen 2026-10-05 04:42:26 CEST (date), vor dem Abruf:
  - Perkins schildert Pryce 1938 als Einwand gegen Querheit bzw. Drehverhalten (nicht nur Kommutator) (55 %) und
    seine Antwort mit gleichgerichteten (kollinearen) Neutrinos.
  - Die Planck-Abweichung (< 1e-8) schaetzt er ueber das Verhaeltnis Photonen zu verfuegbaren Neutrino-Zustaenden in
    einem Volumen, ohne die Phasenraum-Verdichtung (Faktor 8 bzw. Rayleigh-Jeans-Besetzung n > 1) (60 %).
  - Er nennt keine DeMille-artigen Tests (2001, DeMille 1999 vielleicht doch) (50 %).
- Ausgang R5 (04:42:30, quellen/R5-perkins-quasibosons-hep-th-0107003v1-20261005-044230.pdf, sha256 1077f959...,
  15 Seiten; -layout-Text daneben). Gelesen: ganz.
  - **Bestaetigt (je eine Zeile):**
    - Quasiboson-Kommutator [Q, Q^dagger] = delta - Delta, Delta = gewichtete Fermion-Besetzung [S Gl. (3), (9), (12)].
    - Lipkin-Naeherung |F|^2 = 1/Omega: N(p)(Q^dagger)^m|0> = (m - m(m-1)/Omega)(...) [S Gl. (22)],
      Q^dagger|n> = sqrt((n+1)(1 - n/Omega))|n+1> [S Gl. (23)].
    - Planck: n_p = 1/(e^{omega/kT}(1 + 1/Omega) - 1) [S Gl. (47)]; Omega = (3/(8 pi))^{3/2} V/lambda^3 mit
      k0 ~ hbar/lambda und V = Hohlraumvolumen [S Gl. (49), (50)]; Coblentz-Hohlraum 125 cm^3, 1 bis 6,5 um:
      "1/Omega(p,p) <= 10^-9, and the maximum deviation from Planck's law is less than one part in 10^-8" [S Abschn. VI.B].
    - Keine Laboranordnung empfohlen: "we cannot recommend any practical experimental test of Eq. (48)" [S VI.B].
  - **Verstoss V-g (gross): Perkins' Schaetzung ist eine Ein-Moden-Rechnung.** Gl. (22) benutzt N(p)|0> =
    Delta(p,p)|0> = 0, also einen Zustand, in dem nur die Mode p besetzt ist [S]. Im Hohlraum sind alle Moden mit
    n ~ 1/(e^x - 1) besetzt. Nach seiner eigenen Gl. (12) ist Delta(p,p) die mittlere Fermion-Besetzung im Traeger von F;
    die Fermionen der Nachbarmoden zaehlen mit. Mit k0 ~ 1/lambda teilen sich ~Omega Photonmoden dieselben Fermionmoden,
    also <Delta> ~ n (Ordnung 1) statt 1/Omega [ES/M]. Fuer Coblentz (x = hc/(lambda k T) ~ 0,14 bis 1,4) ist n ~ 0,3
    bis 7. **Damit stuetzt R5 meine Phasenraum-Rechnung, statt sie zu widerlegen.** Erwartet hatte ich nur
    "ohne Faktor 8"; gefunden: Die Schaetzung laesst die Fremdbesetzung ganz weg. Bisio u. a. uebernehmen sie (Ref. [38]).
  - **Verstoss V-h (mittel): Perkins' Photon ist kollinear und teilchen-loch-artig gebaut.** Gl. (25):
    gamma_R(p) = (1/sqrt2) sum_k F(k,n)[c1^dagger(k,-n) a1(p+k,n) + c2(p+k,n) a2(k,-n)], "n = p/|p| = k/|k|",
    Neutrino und Antineutrino "(momenta antiparallel and spins parallel)" [S Abschn. II]. Bisio dagegen: zwei
    Vernichter phi, psi, Verschmierung in einer 3D-Kugel. Die beiden "Neutrino-Photonen" sind also verschiedene Bauten.
  - **Verstoss V-i (mittel): Perkins sagt das Gegenteil von exakter Austauschsymmetrie fuer verschiedene Photonen.**
    Gleiche Quasibosonen sind symmetrisch (Gl. 28), aber "two composite quasibosons ... can be antisymmetric" wenn nicht
    identisch (Gl. 29 bis 31); Vorschlag: Zerfall von 1++-Mesonen (f1(1285), f1(1420), chi_c1) und 3P1-Positronium in
    zwei Photonen als Test [S Abschn. III, VI.B]. Die Atomtests (DeMille, English) messen genau so etwas fuer gleiche
    Energie. Perkins zitiert sie nicht (2001; DeMille 1999 lag vor).
  - Pryce wird bei Perkins 2001 nicht behandelt (nicht in der Literaturliste). Der Inhalt von Pryce 1938 bleibt [L?].

### R6: arXiv-API, 24-Monats-Fenster (Feldregel 7), nach Datum
- Anfrage: (abs:"composite photon" OR abs:"neutrino theory of light" OR (abs:"cellular automaton" AND abs:photon) OR
  (abs:"cellular automata" AND abs:photon) OR (abs:"cellular automaton" AND abs:electrodynamics) OR
  (abs:"quantum walk" AND abs:Maxwell)) AND submittedDate:[202410050000 TO 202610052359], neueste zuerst, max 50.
- Erwartung eingetragen 2026-10-05 04:43:57 CEST (date), vor dem Abruf:
  - Wenige einschlaegige Treffer (<= 10). Keiner zeigt, dass ein Paar-Photon dasselbe Tempo mit Wechselwirkung
    (Schleifen) behaelt (PL2). Keiner behandelt die Saettigung im breitbandigen Feld (Besetzung n > 1/8).
  - Moeglich: QCA- bzw. Quantenlauf-Arbeiten zu QED mit Eichfeld auf Kanten (Eis-artiges Licht, nicht Paare).
- Ausgang R6 (04:44:01, quellen/R6-arxiv-api-24monate-20261005-044401.xml, 8 Treffer, 3 einschlaegig): **bestaetigt.**
  - Brun, Mlodinow 2025, arXiv:2503.05998, Entropy 27(5), 492 [S Abstract]: freie QED als Grenzfall von Fermi- und
    Bose-QCA; Photon als eigenes Bose-QCA ("boson internal space that is six-dimensional"), zwei Helizitaeten erst
    durch Beschraenkung auf positive Energien; Kopplung Fermi-Bose: "nonzero amplitude to produce negative-energy
    states, leading to an unphysical cascade", in 1D durch groessere Reichweite exponentiell unterdrueckt.
    Das ist der Eis-Weg im QCA-Rahmen (eigenes Photonfeld), nicht der Paarbau.
  - Bakircioglu, Arnault, Arrighi 2025, arXiv:2505.07900 und Bakircioglu, Arnault 2026, arXiv:2607.14874
    [S Abstract]: Fermion-Verdopplung im Dirac-QCA, das fuer QED vorgeschlagen ist; Behebung durch Flavour-Staffelung.
    Passt zu QCA-TETRA-1 (Verdoppler H, P, P' beim Weyl-Automaten).
  - Kein Treffer zum Paar-Photon, zu seiner Saettigung oder zu Schleifen. PL2 und die Saettigungsfrage: nach
    Recherchestand nicht belegt (Abfrage schmal: Abstract-Phrasen).
- **Abrufe: 6 von 6 verbraucht (R1 leer).** Ab hier nur lokale Dateien.

## 3. Gegensweep (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe? (ab 04:47)

- G1 **geprueft (lokal, kein Abruf)**: "Das Elektron hat im QCA-Bild dasselbe Grenztempo wie die Bausteine des Photons."
  D'Ariano/Perinotti 2014 (lokale Kopie aus qca-tetra-1/quelle, pdftotext nach quellen/L1-lokal-...):
  omega^E = arccos[sqrt(1 - m^2)(cx cy cz -+ sx sy sz)] [S-lokal Gl. (37)], H_D = (n/sqrt d) alpha.k + m beta,
  n = sqrt(1 - m^2) [S-lokal Gl. (62), (63)]. Aus Gl. (37) von Hand [M]: omega_D^2 ~ m^2 + (1 - m^2/2) omega_W^2, also
  Grenztempo (1 - m^2/4) c; Gl. (62) gibt (1 - m^2/2). Beides fuer das Elektron (m ~ 4e-23 in Planck-Einheiten)
  ~ 1e-45. **Ausgang: bestaetigt, mit Zusatz.** Das gemeinsame Tempo im QCA kommt aus zwei Quellen: (i) alle Fermionen
  aus demselben, eindeutigen Weyl-Automaten ohne freien Huepfparameter (diskrete Zeit, Schritt fest), (ii) Paarbau
  fuer das Photon. (i) ist eine Einzigkeits-/Symmetrie-Aussage, (ii) Kinematik.
  - Folge [M]: Die Dirac-Dispersion erbt das lineare Glied des Weyl-Automaten voll (cx cy cz -+ sx sy sz), das Photon
    nur halb (omega = 2 lambda(k/2)). Elektron und Licht unterscheiden sich daher schon in erster Ordnung in E/E_P,
    in der Haelfte der Richtungen ist das Elektron schneller. Vakuum-Cherenkov-Schwelle E^3 ~ m^2/(2 Delta a1):
    mit Delta a1 ~ 0,1 (meine Zahl, Faktor 1/2 von 0,19) E_th ~ (1,8e-45/0,2)^(1/3) E_P ~ 2e-15 E_P ~ 2e4 GeV [M, grob].
    PeV-Elektronen im Krebsnebel [L] waeren damit unvereinbar, wenn die Masche Planck-gross ist. [ES, ungeprueft]
- G2 geprueft (Ueberlegung) [M]: phi laeuft mit A* = sigma_y A sigma_y; A* hat dieselben Eigenphasen {-lambda, +lambda}
  wie A, also dasselbe Tempo und dasselbe lineare Glied. Bestaetigt.
- G3 nicht geprueft: Zeitschriftenfassung (Ann. Phys. 2016) gleich v1? Gl. (44) und die 10^90-Schaetzung koennten dort
  berichtigt sein. Kein Abruf frei.
- G4 nicht geprueft: Inhalt von Pryce 1938 und Jordan 1935 [L?]: Jordans kollinearer Bau gilt als fruehe
  Bosonisierung (in 1D exakte Bose-Kommutatoren), Pryce zeigte [L?], dass er sich nicht zu queren 3D-Photonen mit
  Drehsymmetrie erweitern laesst. Bisio fasst Pryce als Kommutator-Einwand. Offen.
- G5 nicht geprueft: Ob FKM-Kegel ein (psi, phi)-Paar mit konjugierter Entwicklung liefern (Kramers-Partner als phi?) [ES].
- G6 geprueft (Ueberlegung) [M]: "gleiches Tempo" gilt nur bei qbar -> 0. Fuer q quer zu k:
  omega(k/2+q) + omega(k/2-q) = 2 c sqrt(k^2/4 + q^2), Gruppentempo c (1 - 2 q^2/k^2). Mit qbar = eps k ist das ein
  energieunabhaengiger Tempo-Abzug 2 eps^2 (Glied der Dimension 4). Fuer |c_e - c_gamma| < 1e-14 [S-sek licht-gleich-l]
  braucht es eps < 7e-8. Kleines eps verschaerft die Saettigung im Einzelmodus. Bestaetigt die Gegenlaeufigkeit.
- G7 geprueft (Ueberlegung) [M]: Die Zusatzmoden gamma^0, gamma^3 haben Frequenz 0 (Gl. 19), also kein Tempo; sie
  stoeren die Tempofrage nicht, wohl aber die Thermodynamik (Moden bei omega = 0) [ES, offen].

## 4. Schreibtisch zu Finns Netz [M] (ab 04:48)

- Vorzeichen FKM-Fermion gegen Paar-Licht im k^2-Glied, gleicher Impuls: a2_s(n) <= a2_r(n)/4 fuer alle Kegel r, s?
  Mit A = -3/8 + S4/24 (in [-0,361; -0,333]): Bedingung n_s^4/4 - n_r^4/16 <= (3/4)|A|. Links <= 1/4, rechts >= 1/4.
  Gleichheit nur laengs einer Wuerfelachse (n_s = 1, n_r = 0, S4 = 1). **Paar-Licht ist nie langsamer als irgendein
  FKM-Fermion; Vakuum-Cherenkov im k^2-Glied verboten, laengs der Achsen grenzwertig.** FKM hat a1 = a3 = 0, also
  kein Problem erster Ordnung wie im QCA (G1-Folge).
- Photonzerfall in zwei Bausteine: genau an der Schwelle (2 omega_F(k/2) = omega_gamma), fuer massive Paare verboten.
- Ein Photon oder drei: Paare aus demselben Kegel haben Gesamtimpuls ~ k (2 X_r = Gittervektor); Paare aus zwei
  Kegeln haben Gesamtimpuls ~ X_t (X_x + X_y = X_z modulo Gitter) [M]. Langwellig also drei Paarsorten, je tetragonal
  (a2_r/4). Eine symmetrische Summe ueber r ist keine Eigenmode (Glieder a2_r/4 verschieden), sie oszilliert. Drei
  getrennte Photonen haetten in der Kosmologie dreifache Photonendichte bei gleicher Temperatur [L, ES].

## 5. Berichtigungen (nicht geloescht, hier vermerkt) und Abschluss

- [berichtigt beim Schreiben des Dossiers] G1-Folge: Fuer Vakuum-Cherenkov zaehlt das Gruppentempo des Elektrons gegen
  weiches Licht (Tempo c), nicht gegen das Paar-Photon gleicher Energie. ~~Delta a1 ~ 0,1 (Faktor 1/2 von 0,19)~~ ->
  massgeblich ist das lineare Glied des Elektrons selbst (Phase |nx ny nz| <= 0,19, Gruppe doppelt). Schwelle bleibt
  E ~ 1 bis 2e4 GeV [M, grob]. Gilt nur in EFT-Kinematik, nicht bei deformierter Relativitaet (Bisio Ref. [51]).
- [berichtigt im Dossier, Gegenlesen] Ungleichung aus Bisio Gl. (40) richtig herum: P <= <N|Gamma|N> <= N P.
- [berichtigt im Dossier] LHAASO E_QG,1 = 1,0e20 GeV ohne Vorzeichenangabe (licht-finn-netz-1 nennt keines).
- [berichtigt im Dossier] Oszillationsphase der Kegel-Photonen: (n_r^4 - n_s^4)/16 (k l)^2 k c t.
- Offene Rueckfragen an die Leitung (wandern mit):
  - R-1: Darf ein frischer Leser die 8n-Zaehlung gegenlesen, bevor sie in WEICHE-STAND oder an Finn geht?
  - R-2: Zeitschriftenfassung Ann. Phys. 368 (2016) pruefen (Gl. (44), 10^90-Schaetzung), sobald ein Abruf frei ist.
- DOSSIER.md geschrieben ab 04:49:32, Korrekturen bis 2026-10-05 04:53:47 CEST (date). Abrufe 6 von 6.
- Letzte Dossier-Aenderung (Widerspruchsprobe absoluter Aussagen: "nie langsamer" eingeschraenkt auf k^2-Glied und qbar -> 0; "exakt null" auf den freien Paarbau; Einfach-gesagt-Wortlaut) bis 2026-10-05 04:54:30 CEST (date).
