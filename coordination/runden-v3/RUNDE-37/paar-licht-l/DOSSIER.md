# PAAR-LICHT-L: Dossier. Bekommen Licht und Teilchen von selbst dasselbe Tempo, wenn das Licht aus Paaren der Teilchen gebaut ist? (Runde 45, Literatur und Schreibtisch)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-05 04:30:11 CEST, Dossier ab 04:49:32 CEST (date).
- Grundlage: KARTE.md (bindend, PL1 bis PL4 unveraendert). Protokoll mit Erwartung vor jedem Abruf, Ausgaengen,
  Rechnungen und Gegensweep: ARBEITSFELD.md (gleicher Ordner). Kopien mit Abrufzeit in quellen/.
- 6 von 6 Abrufen verbraucht (R1 leer durch eigenen Bedienfehler), alle auf arXiv (API bzw. pdf, per curl, damit Kopien
  moeglich sind). Keine Websuche. Dazu lokal: D'Ariano/Perinotti 2014 aus qca-tetra-1/quelle (kein Abruf).
- Kennzeichen: [S Abschn./Gl.] an der Quelle gelesen; [S Abstract]; [S-lokal] lokale Kopie, selbst gelesen; [P]
  Projektdatei; [L] Gedaechtnis; [L?] unsicher; [M] eigene Rechnung von Hand, nicht gegengelesen; [ES] eigener Schluss;
  [H] Hypothese.
- **Literatur und Schreibtisch. Keine Messdaten zu Finns Netz, keine Messdatenbestaetigung.**

## 1. Ergebnis zuerst

1. **Der dritte Weg existiert und ist an der Quelle gebaut, aber nur kinematisch.** Bisio, D'Ariano, Perinotti (arXiv
   2014, Ann. Phys. 2016) bauen das Photon als Bilinear zweier Weyl-Automaten (psi mit A_k, phi mit A*_k), verschmiert
   mit f_k(q) bei qbar << k. Es gilt omega(k) = 2 |n_{k/2}|, also genau 2 omega_W(k/2), und langwellig Maxwell mit dem
   Tempo der Fermionen [S Gl. (10)-(13), (20), (27)-(29), (43)]. Das gleiche Tempo kommt ohne Symmetrie zwischen den
   Sorten aus. Gezeigt ist es nur fuer freie Felder; zu Schleifen fand ich nichts (PL2) [S Abstract, Abschn. VII; R6].
2. **Preis an der Quelle: kein exaktes Maxwell.** Die Quelle nennt einen kleinen Laengsanteil (theta ~ 2k), vier statt
   zwei bosonische Moden (dazu eine laengs und eine zeitartig; beide haben nach Gl. (19) Frequenz 0 [M]) und ein
   **lineares**, richtungsabhaengiges Tempoglied ~ kx ky kz/|k|^2, super- oder subluminal [S Abschn. IV-VI, Gl. (37), (44)].
   Meine Handrechnung gibt fuer Gl. (44) einen um 3 sqrt3 = 5,2 kleineren Vorfaktor (|xi| <= 0,19 statt 1) [M, ungeprueft].
3. **Bose: Saettigung, keine Antisymmetrie, und die Entwarnung der Quellen zaehlt die falschen Moden.**
   - Photon-Erzeuger vertauschen exakt [S Gl. (34)]. Die Labortests (DeMille u. a. 1999: v < 1,2e-7; English u. a.
     2010: nu < 4,0e-11) suchen antisymmetrische Zwei-Photonen-Zustaende und treffen den Paarbau deshalb nicht
     [S Abstracts; M].
   - Die Entwarnungen (Bisio: 6e23 Photonen gegen "10^90" Fermionmoden; Perkins: Planck-Abweichung < 1e-8) zaehlen
     alle Moden bzw. nur eine besetzte Mode [S].
   - Meine Phasenraumrechnung: In einem breitbandigen Feld mit Besetzung n je Mode tragen die Bausteinmoden im Mittel
     8 n. Bose-Verhalten verlangt dann n << 1/8 [ES/M, ungeprueft]. Stimmt das, schliessen Spektren im
     Rayleigh-Jeans-Gebiet (n > 1) den Paarbau mit 3D-Verschmierung aus. Urteil nach Feldregel 7: nicht "widerlegt",
     sondern offene, eigene Rechnung; die 24-Monats-Suche fand nichts dazu.
4. **Finns Netz [M]:**
   - Das Gegenlesen der Formabschnitte fand keinen Fehler (PL4).
   - Mit FKM-Kegeln als Bausteinen (a1 = a3 = 0) hat Paar-Licht je Kegel a2_r/4. Neu: Bei scharf gebuendelten Paaren
     ist es im k^2-Glied nie langsamer als irgendein FKM-Fermion (Gleichheit nur laengs der Wuerfelachsen). Aus diesem
     Glied folgt also kein Vakuum-Cherenkov. Breitere Buendelung macht das Licht um 2 eps^2 langsamer (G6).
   - Eis-Licht hat genau 1/3 des kegelgemittelten Fermion-a2, Paar-Licht 1/4.
   - Drei Kegel geben drei langwellige Paarsorten, also drei Photonen. Eine Summe ueber die Kegel waere keine
     Eigenmode [M/ES].
5. **Fuer Finn:**
   - Paar-Licht macht aus Isotacheia ("alle Bausteine laufen mit c") eine Bedingung an *ein* Fermionfeld statt an alle
     Felder; im QCA erzwingt der feste Takt sogar dieses eine Tempo [S-lokal; ES].
   - Der Preis: Bose-Saettigung, Zusatzmoden, drei Photonsorten und die offene Schleifenfrage.
   - Unterscheidungspunkt Eis gegen Paar: Bose-Verhalten bei hoher Besetzung und das Verhaeltnis a2_gamma/a2_F
     (1/3 gegen 1/4).

## 1a. Erwartungsverstoesse (das eigentliche Ergebnis, wichtigstes zuerst)

| Nr | Erwartet | Gefunden | Fundstelle |
|---|---|---|---|
| V1 | PL3: Bose-Abweichung haengt an freier Verschmierung, Labor schliesst nicht aus | Abhaengigkeit von f_k ja. Aber beide Entwarnungen zaehlen falsch: Bisio vergleicht mit "around 10^90 Fermionic modes" in 10^-15 cm^3 (Planck-Zellen dort: 2,4e83 [M]; nach Gl. (20) zaehlen nur |q| < qbar << k, fuer optisches k weniger als 1 Mode [M]). Perkins rechnet mit N(p)\|0> = Delta(p,p)\|0> = 0, also nur einer besetzten Mode; im Hohlraum sind alle Moden besetzt, und Delta ist nach seiner Gl. (12) die mittlere Fermionbesetzung [S; ES]. Eigene Rechnung: Bausteinbesetzung 8 n | Bisio Abschn. I, V, VI, Gl. (20), (36); Perkins Gl. (12), (22), (47)-(50); ARBEITSFELD Zwischenrechnung vor R4 |
| V2 | Paar-Tempo weicht erst bei k^2 ab (wie FKM) | Lineares Glied: "c-+(k) ~ 1 +- 3 kx ky kz/\|k\|^2 ~ 1 +- k/sqrt3", "not isotropic and can be superluminal". Grund: Der Weyl-Automat ist chiral [M]. Meine Nachrechnung: 1 -+ kx ky kz/(sqrt3 \|k\|^2), Faktor 3 sqrt3 kleiner | Bisio Gl. (44) [S]; ARBEITSFELD R3 [M] |
| V3 | Maxwell-Feld mit zwei Querpolarisationen | Vier bosonische Moden: "4 independent Bosonic field modes" (i = 0, 1, 2, 3), darunter "longitudinal" und "timelike". Nach Gl. (19) haben beide Frequenz 0 [M]. In v1 nicht als Problem besprochen | Bisio Gl. (19), (37) und Text danach [S] |
| V4 | Maxwell exakt quer | "small longitudinal polarization", Feld dreht um n_{k/2} statt um k, theta ~ 2k, fuer Gamma-Wellenlaengen 1e-15 rad, waechst nicht mit der Laufstrecke | Bisio Abstract, Gl. (25), Abschn. VI [S] |
| V5 | Bose-Tests an Photonen (DeMille, English) begrenzen den Paarbau | Sie messen den Anteil austauschantisymmetrischer Zustaende; im freien Paarbau ist er exakt null, weil die Erzeuger vertauschen. Die Saettigung ist eine andere Groesse | DeMille Abstract, English Abstract [S]; Bisio Gl. (34) erste Zeile [S]; [M] |
| V6 | Perkins' Neutrino-Photon gleicht dem Bisio-Bau | Anderer Bau: kollinear ("n = p/\|p\| = k/\|k\|"), ein Vernichter und ein Erzeuger je Glied (c^dagger a), Neutrino und Antineutrino "momenta antiparallel and spins parallel". Bisio: zwei Vernichter, 3D-Kugel | Perkins Gl. (25) [S]; Bisio Gl. (12), (13) [S] |
| V7 | Pryce = Einwand gegen Querheit/Drehverhalten [L?] | Bisio fasst Pryce als "a composite particle cannot obey the exact Bosonic commutation relations [39]". Perkins 2001 behandelt Pryce nicht. Inhalt von Pryce 1938 bleibt ungelesen | Bisio Abschn. I [S]; Perkins Lit.-Liste [S] |
| V8 | (Gegensweep) Elektron und Licht im QCA gleich bis auf Planck-k^2 | Die Dirac-Dispersion erbt das lineare Glied des Weyl-Automaten voll, das Paar-Photon nur halb. In EFT-Kinematik: Vakuum-Cherenkov fuer Elektronen ab ~2e4 GeV in der Haelfte der Richtungen [M, grob]. Bei deformierter Relativitaet (Bisio Ref. [51]) gibt es keine solchen Schwellen [ES] | D'Ariano/Perinotti Gl. (37) [S-lokal]; Bisio Abschn. VII [S]; ARBEITSFELD G1 [M] |

## 2. Urteile PL1 bis PL4

| Nr | Erwartung (Karte) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| PL1 | [L?] Photon aus zwei Weyl-Automaten; langwellig Maxwell mit dem Tempo der Fermionen; Bose nur naeherungsweise | 75 % | **eingetroffen** (Wortlaut), mit drei Einschraenkungen ausserhalb des Wortlauts (V2 bis V4) | "the free Maxwell's equations emerge from two Weyl QCAs", "the usual Bosonic statistics is recovered in the low photon density limit" [S Abstract]; Gl. (10)-(13), (27)-(29), (43) [S]. Tempo: 2 n_{k/2} ~ k/sqrt3 wie beim Weyl-Automaten (c = 1/sqrt3 in Gitter-Einheiten), mit x -> x sqrt3 l_P wird daraus c [S Gl. (27), (28)] |
| PL2 | [H] Literatur zeigt nicht, dass die Gleichheit Schleifen uebersteht; sie ist kinematisch | 60 % | **eingetroffen** (nach Recherchestand) | Bisio behandelt nur "free electrodynamics" bzw. "the free quantum radiation field" [S Abstract, Abschn. VII]. Gleichheit = omega(k) = 2 omega_W(k/2) [S Gl. (43)]. 24-Monats-Fenster: kein Treffer zu Paar-Photonen mit Wechselwirkung; Brun/Mlodinow 2025 berichten fuer QCA-QED mit *eigenem* Bose-Automaten eine Spannung beim Koppeln ("unphysical cascade" negativer Energien) [S Abstract, R6]. "Nicht belegt", nicht "widerlegt" |
| PL3 | [H] Bose-Abweichung haengt an freier Verschmierung; Labor-Schranken schliessen den Paarbau nicht aus | 55 % | **nach Wortlaut eingetroffen, Begruendung nicht tragfaehig, Urteil offen** | Freie Verschmierung f_k(q) mit Kriterium M/N_k <= eps [S Gl. (20), (34)-(37)]; Labortests treffen nicht (V5) [S Abstracts; M]. Aber die Schaetzungen der Quellen zaehlen falsch (V1), und nach meiner Phasenraumrechnung braucht Bose-Verhalten n << 1/8 je Mode [ES/M]. Waere das richtig, schloessen Rayleigh-Jeans-Spektren den 3D-Paarbau aus [L fuer die Spektren]. Das ist eigene, ungepruefte Rechnung, deshalb kein Ausschluss |
| PL4 | Kontrolle [M]: Gegenlesen bestaetigt Summe (n.d)^4 = 3 - S4 und a2_gamma = a2_F/4 je Kegel | 85 % | **eingetroffen**; kein Fehler gefunden | Abschnitt 2.1 |

- **Bedeutung laut Karte:** PL1 und PL3 treffen nach Wortlaut ein, also gibt es "einen dritten Weg ... ohne Symmetrie und
  ohne Abstimmung, dafuer mit naeherungsweiser Bose-Statistik". PL2 trifft ein, also ist die Gleichheit "nur klassisch
  gesichert"; die Collins-Gefahr bleibt offen.
- **Zusatz [ES]:** Die Bedeutungszeile unterstellt, dass "naeherungsweise Bose" ein kleiner Preis ist. Nach V1 ist das
  ungeklaert. Es kann sein, dass Bose-Verhalten nur dort gilt, wo es keine Rolle spielt (n << 1). Diese Frage
  entscheidet, ob der dritte Weg physikalisch offen ist.

### 2.1 Gegenlesen der Formabschnitte der Ableitbarkeitsprobe (nur gegenlesen) [M]

- Summe ueber die 12 fcc-Vektoren: Je Ebene gilt (nx +- ny)^4-Summe/4 = nx^4 + 6 nx^2 ny^2 + ny^4. Ueber drei Ebenen
  ergibt das 2 S4 + 6 P mit P = (1 - S4)/2, also 3 - S4. **Stimmt.**
  - Zweites Moment 4 (isotrop), daher a2 proportional zu (S4 - 3) fuer eine einzelne Schale eines Ein-Band-Modells.
    **Stimmt.**
  - bcc-Schale: (8/9)(3 - 2 S4) als Summe der vierten Potenzen. **Stimmt** (gemeint ist die Form der Summe; a2 ist dann
    proportional zu 2 S4 - 3).
- Eis-Licht -1/8 + S4/24 = (S4 - 3)/24: **stimmt**. Probe an den Projektwerten: -1/12, -5/48, -1/9 [P licht-finn-netz-1].
- a2_r = -3/8 + S4/24 + n_r^4/4: **stimmt**. Probe an allen fuenf FKM-Werten (-1/12, -1/3, -17/48, -7/24, -1/3)
  [P diamant-nullstellen-1 Abschn. 4].
  - Mittel ueber die Kegel: (S4 - 3)/8, **stimmt**.
  - Paarbau a2_r/4 und gemittelt (S4 - 3)/32, **stimmt**.
- omega_gamma(k) = 2 omega_F(k/2): **an der Quelle bestaetigt** (Bisio Gl. (43)). Allgemein gilt a_n -> a_n/2^n. a2/4 ist
  also nur dann das fuehrende Glied, wenn a1 = 0 ist; FKM erfuellt das, der Weyl-Automat nicht (V2).
- **Ergaenzungen, keine Fehler:**
  1. Eis-Licht zu kegelgemitteltem FKM-Fermion: (S4 - 3)/24 geteilt durch (S4 - 3)/8 = 1/3 in jeder Richtung. Das
     Verhaeltnis ist damit ein scharfer Unterscheidungspunkt: Eis 1/3, Paar 1/4.
  2. "Langwellig ist das Tempo damit gleich, schon kinematisch" gilt nur fuer qbar -> 0. Mit Querverschmierung
     q ~ eps k ist das Paar um 2 eps^2 langsamer, unabhaengig von der Energie (G6). Das ist ein Glied der Dimension 4.

## 3. Literaturstand zum Paar-Photon

### 3.1 Bau (Bisio, D'Ariano, Perinotti 2014/2016)
- Zwei unabhaengige Weyl-Felder: psi(k, t+1) = A_k psi(k, t), phi(k, t+1) = A*_k phi(k, t) mit A*_k = sigma_y A_k sigma_y.
  A_k ist einer der beiden Weyl-Automaten A+- auf BCC; "the whole derivation is independent of the choice"
  [S Gl. (8), (10)].
- Bilinear G^mu_f(eta, theta, k) = int dq/(2 pi)^3 f_k(q) eta^T(k/2 - q) sigma^mu theta(k/2 + q), int |f_k|^2 = 1;
  F^mu(k) = G^mu_f(phi, psi, k) [S Gl. (12), (13)].
- Bedingung: int_{|q| >= qbar(k)} |f_k(q)|^2 << 1 fuer qbar(k) << |k| [S Gl. (20)]. Fehler O(qbar/|n_{k/2}|)
  [S Gl. (21), (23), (24)]; im Beweis zusaetzlich ein mit der Zeit wachsendes Glied O(|a'|^2/|a|^2 t) [S Gl. (A5)].
- Deutung: "composite particle made of a pair of correlated massless Fermions", Naehe zur Neutrinotheorie des Lichts
  (de Broglie, Jordan, Kronig, Perkins) [S Abschn. I, VII].

### 3.2 Maxwell-Grenzfall und Tempo
- d_t F_T = 2 n_{k/2} x F_T, 2 n_{k/2} . F_T = 0 (bis auf Lambda) [S Gl. (25)]. Fuer |k| << 1 folgen Gl. (27) und mit
  x -> x sqrt3 l_P, t -> t t_P, c := l_P/t_P die Gl. (28), (29): div E = div B = 0, d_t E = c rot B, d_t B = -c rot E [S].
- Dispersion omega(k) = 2 |n_{k/2}|; "The usual relation omega(k) = |k| is recovered in the |k| << 1 regime"
  [S Gl. (43)].
- Lichttempo laut Quelle: c-+(k) ~ 1 +- 3 kx ky kz/|k|^2 ~ 1 +- k/sqrt3, Vorzeichen je nach A+ bzw. A-
  [S Gl. (44)]. Dazu meine abweichende Nachrechnung (V2, ARBEITSFELD R3).
- Das Tempo ist dasselbe wie das der Weyl-Bausteine, weil omega_gamma(k) = 2 omega_W(k/2). Auch das Elektron (Dirac-
  Automat aus zwei gekoppelten Weyl-Automaten, cos omega_D = sqrt(1 - m^2) cos omega_W) hat dasselbe Grenztempo bis auf
  O(m^2), fuer das Elektron ~1e-45 [S-lokal D'Ariano/Perinotti Gl. (37), (62), (63); M].

### 3.3 Bose-Statistik
- [gamma_ab(k), gamma_a'b'(k')] = 0 exakt; [gamma_ab(k), gamma^dagger_a'b'(k')] = delta delta delta - Delta, Delta aus
  "geformten" Zahloperatoren [S Gl. (33), (34)]. Abschaetzung |<H>| <= sqrt(<Gamma><Gamma>), Gamma = sum_q |f_k(q)|^2
  psi^dagger psi [S Gl. (35), (36)].
- Fuer konstantes |f_k|^2 = 1/N_k auf Omega_k: <Gamma> = M/N_k (M = Fermionen in Omega_k). Fuer M/N_k <= eps << 1
  gilt Gl. (37) fuer i = 0, 1, 2, 3 [S Abschn. V].
- Anschluss an das Verschraenkungs-Kriterium fuer Komposit-Bosonen (Chudzicki/Oke/Wootters 2010, Law 2005):
  P <= <N|Gamma|N> <= N P, P = Reinheit des Einteilchenzustands [S Gl. (38)-(41), S-sek].
- Perkins 2001/2002 (Quasibosonen): dieselbe Struktur [Q, Q^dagger] = delta - Delta [S Gl. (3), (9)]. Lipkin-Naeherung:
  Q^dagger|n> = sqrt((n+1)(1 - n/Omega))|n+1>; Planck: n_p = 1/(e^{omega/kT}(1 + 1/Omega) - 1) [S Gl. (23), (47)].
- **Eigene Rechnung [ES/M] (ARBEITSFELD, vor R4):**
  - Ein psi-Modus bei p gehoert zu allen Photonmoden k' = 2(p - q'), q' in Omega, also zu 8 N_k Moden.
  - Bei glatter Photonbesetzung n traegt er im Mittel 8 n. Pauli verlangt 8 n <= 1, Gl. (37) verlangt n << 1/8.
  - Schmalbandig (ein Lasermodus der Breite Delta k << qbar) ist es n (Delta k/qbar)^3.
  - Beide Quellen rechnen nur den schmalbandigen bzw. Ein-Moden-Fall.

### 3.4 Klassische Einwaende (Pryce, Perkins)
- Bisio: "The failure of the neutrino theory of light was determined by the fact that a composite particle cannot obey
  the exact Bosonic commutation relations [39]. However, as it was shown in Ref. [38], the non-Bosonic terms introduce
  negligible contribution at ordinary energy densities." [S Abschn. I]; [39] = Pryce, Proc. R. Soc. A 165, 247 (1938),
  [38] = Perkins, IJTP 41, 823 (2002) [S Lit.].
- Pryce 1938 selbst nicht gelesen (nicht frei, nicht auf arXiv). Mein [L?]: Jordans kollinearer Bau gibt in 1D exakte
  Bose-Kommutatoren (Vorlaeufer der Bosonisierung); Pryce zeigte, dass er sich nicht zu queren 3D-Photonen mit
  Drehsymmetrie erweitern laesst. Stimmt das, trifft Pryce genau die Punkte V3/V4 (Laengsanteil, Zusatzmoden). Bisio
  umgeht Drehsymmetrie ohnehin, weil der Automat nur eine diskrete Gruppe hat [ES].
- Perkins 2001: Spin-Statistik-Satz gilt fuer Quasibosonen nicht, weil ihre Felder nicht lokal kommutieren
  [S Abschn. IV, V, Gl. (37)]. Nicht identische Komposit-Photonen koennten antisymmetrische Zwei-Photonen-Zustaende
  bilden; Tests: 1++-Mesonen (f1(1285), f1(1420), chi_c1) und 3P1-Positronium in zwei Photonen [S Abschn. III, VI.B].
  [ES] Diese Lesart behandelt Polarisation als Teilchensorte; im Bisio-Bau vertauschen alle Erzeuger exakt (Gl. 34),
  dort gibt es keinen solchen Kanal.

### 3.5 Neuere Literatur (24-Monats-Fenster, Feldregel 7)
- Brun, Mlodinow 2025 (Entropy 27, 492): QED als Grenzfall von Fermi- und Bose-QCA; das Photon ist ein eigener
  Bose-Automat mit "six-dimensional" innerem Raum, zwei Helizitaeten erst durch Beschraenkung auf positive Energien;
  Kopplung erzeugt negative Energien, in 1D durch groessere Reichweite unterdrueckt [S Abstract].
- Bakircioglu, Arnault, Arrighi 2025; Bakircioglu, Arnault 2026: Fermion-Verdopplung im Dirac-QCA, das fuer QED
  vorgeschlagen ist; Behebung durch Flavour-Staffelung [S Abstracts]. Passt zu den Verdopplern H, P, P' aus QCA-TETRA-1.
- Kein Treffer zum Paar-Photon, zu seiner Saettigung oder zu Schleifen. Urteil: "nach Recherchestand nicht belegt".

## 4. Messdaten (soweit die Quellen sie nennen)

| Groesse | Zahl | Was sie misst | trifft den Paarbau? | Fundstelle |
|---|---|---|---|---|
| Austauschantisymmetrische Zwei-Photonen-Zustaende (Ba, J = 0 <-> J' = 1) | v < 1,2e-7 | Anteil antisymmetrischer Zustaende | nein, im freien Paarbau exakt 0 [M aus S Gl. (34)] | DeMille, Budker, Derr, Deveney 1999 [S Abstract] |
| Bose-verbotene Zwei-Photonen-Anregung (Ba) | nu < 4,0e-11 (90 % CL) | wie oben, als Ratenbruchteil | nein [M] | English, Yashchuk, Budker 2010 [S Abstract] |
| Hohlraumstrahlung (Coblentz 1916, 125 cm^3, 1 bis 6,5 um) | Abweichung "less than one part in 10^-8" | Planck-Verteilung | laut Perkins nein; nach V1 nur in Ein-Moden-Naeherung [ES] | Perkins Abschn. VI.B [S]; Bisio Abschn. VI [S] |
| Staerkster Laser (Dunne 2007) | "approximately an Avogadro number of photons in 10^-15 cm^3" | Saettigung | laut Bisio "very far from being detectable"; nach V1 offen [ES] | Bisio Abschn. VI [S] |
| Laufzeiten von Gammablitzen | keine Zahl in der Quelle; "now approaching a sufficient sensitivity to detect corrections ... of the same order as in Eq. (44)" | lineares Tempoglied | ja, richtungsabhaengig | Bisio Abschn. VI, Ref. [28], [47]-[49] [S] |
| Laengsanteil | theta ~ 2k, ~1e-15 rad fuer Gamma-Wellenlaengen | Querheit | "not reachable by the present technology" | Bisio Abschn. VI [S] |

- Projektzahl zum Vergleich: LHAASO E_QG,1 > 1,0e20 GeV (lineares Glied; das Vorzeichen steht dort nicht)
  [P licht-finn-netz-1]. Daraus |xi| < E_P/E_QG,1
  = 0,12 [M]. Mit der Quellen-Gl. (44) (|xi| bis 1) waeren grosse Teile des Himmels ausgeschlossen, mit meinem
  Vorfaktor (|xi| <= 0,19) nur die Naehe der Raumdiagonalen. Eine einzelne Quelle bei unbekannter Gitterlage entscheidet
  das nicht [M/ES].
- Nicht in den Quellen, nur [L]: CMB-Spektrum (FIRAS) bei 60 GHz mit n ~ 0,5; Radiofelder n >> 1. Das waeren die
  Pruefdaten fuer die Saettigungsfrage.

## 5. Schreibtisch zu Finns Netz [M, nicht gegengelesen]

### 5.1 FKM-Kegel als Bausteine
- Ein Paar aus demselben Kegel X_r mit Impulsen X_r + k/2 +- q hat den Gesamtimpuls 2 X_r + k = k (2 X_r ist
  Gittervektor) [M]. Langwellige Paar-Photonen kommen also aus einem Kegel.
- Paare aus zwei Kegeln haben Gesamtimpuls ~ X_t (X_x + X_y = X_z modulo Gitter) und sind kein langwelliges Licht [M].
- FKM hat a1 = a3 = 0 (wegen -X = X) [P diamant-nullstellen-1]. Das Paar-Photon erbt daher kein lineares Glied, anders
  als im Weyl-QCA (V2). Fuehrend ist a2_r/4 = -3/32 + S4/96 + n_r^4/16 (je Kegel tetragonal).
- Offen [ES]: Bisio braucht zwei unabhaengige Felder (psi mit A, phi mit A*). Bei FKM liegt als phi der Kramers-Partner
  nahe (gleicher Kegel, entartet). Aus 4 x 4 Komponenten je Kegel entstehen 16 Bilineare (Skalar, Vektor, Axialvektor,
  Tensor). Welche davon die zwei Querpolarisationen tragen und was mit dem Rest geschieht, ist nicht untersucht.

### 5.2 Ein Photon oder drei
- Drei Kegel geben drei Paarsorten mit verschiedenen Formen (n_r^4/16).
- Eine symmetrische Summe ueber r ist keine Eigenmode; sie wuerde zwischen den Kegeln oszillieren, mit Phasen ~
  (n_r^4 - n_s^4)/16 (k l)^2 k c t [M].
- Drei getrennte, gleich gekoppelte Photonsorten verdreifachten die Photon-Freiheitsgrade im fruehen Universum (BBN, CMB)
  [L, ES]. Ein einziges Photon braucht also eine Kopplung, die nur eine Kombination an Ladungen bindet [H].
- Liest man die drei Kegel als Neutrino-Generationen (DREI-KEGEL-NEUTRINO-L [P]), dann ist Paar-Licht auf Finns Netz
  woertlich de Broglies Neutrinotheorie des Lichts [H].

### 5.3 Vorzeichen Elektron gegen Licht bei hoher Energie
- **k^2-Glied, gleicher Impuls, Elektron = FKM-Fermion beliebigen Kegels, Licht = Paar beliebigen Kegels [M]:**
  - Mit A = -3/8 + S4/24 (zwischen -0,361 und -0,333) lautet die Bedingung a2_s <= a2_r/4 so:
    n_s^4/4 - n_r^4/16 <= (3/4)|A|.
  - Links steht hoechstens 1/4, rechts mindestens 1/4. Gleichheit gilt nur laengs einer Wuerfelachse
    (n_s = 1, n_r = 0, S4 = 1).
  - **Im k^2-Glied und bei scharf gebuendelten Paaren (qbar -> 0) ist Paar-Licht damit nie langsamer als ein
    FKM-Fermion. Vakuum-Cherenkov ist aus diesem Glied verboten, laengs der Achsen grenzwertig.**
- Photonzerfall in zwei masselose Bausteine liegt genau an der Schwelle (2 omega_F(k/2) = omega_gamma(k)). In massive
  Paare ist er verboten [M].
- **Verschmierungs-Glied (G6) [M]:** Bei Querverschmierung q ~ eps k ist das Paar um 2 eps^2 langsamer als seine
  Bausteine, und zwar energieunabhaengig.
  - Fuer \|c_e - c_gamma\| < 1e-14 [S-sek ueber licht-gleich-l] braucht es eps < 7e-8.
  - Bei kleiner Energie ueberwiegt dieses Glied (Licht langsamer, Cherenkov erlaubt), bei hoher das Gitter-Glied
    (Licht schneller).
- **Zum Vergleich der Weyl-QCA (V8) [M]:** Das Elektron erbt das lineare Glied voll, das Paar-Photon halb. In der Haelfte
  der Richtungen ist das Elektron superluminal. In EFT-Kinematik ergibt das Vakuum-Cherenkov ab
  E^3 ~ m_e^2 E_P/(2 |a1|), also ~2e4 GeV. Gegen PeV-Elektronen im Krebsnebel [L] waere eine Planck-grosse Masche
  dann ausgeschlossen.
  - Diese Folgerung gilt nicht, wenn die QCA-Symmetrie deformiert (DSR) statt gebrochen ist, wie Bisio mit Ref. [51]
    andeutet [S Abschn. VII; ES].
  - Finns FKM-Netz hat dieses Problem nicht (a1 = 0).

## 6. Einordnung fuer Finn

### 6.1 Zwei Regime (Feldregel 1) und Moderatoren
| Moderator | Regime A | Regime B | Beleg |
|---|---|---|---|
| M1 Ist das Photon ein eigener Freiheitsgrad? | Eis-Licht: eigenes Feld, eigenes Tempo sqrt(gJ) a, Gleichheit nur durch Abstimmen; Bose exakt; quer exakt | Paar-Licht: Tempo der Bausteine, kinematisch; Bose genaehert; Laengsanteil, Zusatzmoden | licht-gleich-l [P]; Bisio [S] |
| M2 Verschmierung qbar/k | klein: genaues Maxwell und Tempo, Bose nur bei kleiner Besetzung | gross: Bose besser, Maxwell und Tempo falsch (Fehler O(qbar/k), Abzug 2 eps^2) | Bisio Gl. (20), (21), (A5) [S]; G6 [M] |
| M3 Besetzung je Mode (Phasenraumdichte, nicht Dichte) | n << 1/8: Paar-Photon wie Boson | n >~ 1/8 im Breitband: Bausteine an der Pauli-Grenze | eigene Rechnung [ES/M] |
| M4 Kinematik-Rahmen | Vorzugssystem (EFT): Cherenkov- und Zerfallsschwellen gelten | deformierte Relativitaet (DSR): keine Schwellen, Laufzeiten ggf. schon | Bisio Abschn. VII, Ref. [51] [S]; [ES] |
| M5 Takt | diskrete Zeit (QCA): der Schritt legt das Tempo fest, kein freies t je Sorte | Hamilton-Netz (Finn): t je Sorte frei | D'Ariano/Perinotti [S-lokal]; licht-gleich-l [P] |
| M6 Paritaet der Bausteine | chiral (Weyl-QCA): lineares Glied, Elektron und Licht verschieden | Kegel an TRIM (FKM): a1 = 0, nur k^2 | Bisio Gl. (44) [S]; diamant-nullstellen-1 [P] |

- **Feldregel 6 [ES]:** "Gleiches Tempo" hat im Paarbau drei Wege: gleiche Bausteine (Kinematik), ein eindeutiger Takt
  (QCA) und Abstimmung (Eis). Die gemeinsame Groesse ist die Zahl der unabhaengigen Huepf- bzw. Taktparameter, die ein
  Feld zur Grenzgeschwindigkeit beitraegt. Paar-Licht senkt sie fuer das Licht auf null; das Fermion behaelt seinen
  einen Parameter.

### 6.2 Unterscheidungspunkte (Feldregel 2)
| Paar | Wo sie auseinanderlaufen | zugaenglich? |
|---|---|---|
| Eis gegen Paar | (i) Bose bei hoher Besetzung: Paar saettigt (wenn M3 stimmt), Eis nicht; (ii) a2_gamma/a2_F = 1/3 (Eis) gegen 1/4 (Paar) [M]; (iii) Laengsanteil und Zusatzmoden; (iv) drei Photonsorten | (i) ja, Rayleigh-Jeans-Spektren und Laserfelder [L]; (ii) nur mit richtungsaufgeloesten Laufzeiten von Licht und Fermionen bei Planck-naher Energie, praktisch nein; (iii) nein (1e-15 rad); (iv) kosmologisch ja [L] |
| Bisio Gl. (44) gegen meine Nachrechnung | Vorfaktor des linearen Glieds, |xi|max = 1 gegen 0,19 | am Schreibtisch, durch Gegenlesen |
| EFT gegen DSR | Schwellen (Vakuum-Cherenkov der Elektronen ab ~2e4 GeV) gibt es nur in EFT | ja, ueber TeV- bis PeV-Elektronen [L] |

### 6.3 Was hiesse das fuer Finns Netz, und Isotacheia [H]
- **Eis-Licht** (bisher gerechnet, LICHT-FINN-NETZ-1): eigenes Tempo, gleich dem FKM-Tempo nur durch Einheitenwahl
  (Ableitbarkeitsprobe der Karte). Exakt bosonisch, exakt quer, keine Doppelbrechung bis (k l)^4 [P].
- **Paar-Licht:**
  - gleiches Tempo von selbst, auf Baumebene und bei scharfer Buendelung, mit der Ungleichung aus 5.3 (im k^2-Glied
    nie langsamer als das Fermion).
  - Preise: Bose nur genaehert (vielleicht nur fuer n << 1/8), Zusatzmoden, drei Photonsorten, Schleifen offen.
  - Gebrochene Isotropie im Langwelligen gibt es nicht, aber nur bei t = 4 lambda. Diese Abstimmung erbt das
    Paar-Licht. Fuer die Kegel als Neutrinos muss sie auf ~2e-28 stimmen [P drei-kegel-neutrino-l, Ergebnis 5]; die
    Schranke fuer Licht habe ich nicht nachgeschlagen.
- **Isotacheia [H]:**
    Isotacheia, bei ihm ein Postulat [P RUNDE-41.md Z. 503-506; WEICHE-STAND-v8 Z. 60].
  - Paar-Licht macht daraus eine Aussage ueber *ein* Bausteinfeld: Wenn alles Licht aus Paaren desselben Fermions
    besteht, laeuft es mit dessen Tempo. Damit verschiebt sich das Postulat von "alle Felder" auf "alle Fermionen".
  - Im QCA ist auch dieser Rest erzwungen, weil ein Takt mit festem Schritt und ein eindeutiger Weyl-Automat kein freies
    Tempo lassen [S-lokal; ES].
  - Auf Finns Hamilton-Netz bleibt je Fermionsorte ein t. Ein Tempo fuer alles hiesse dort: eine Fermionsorte (etwa die
    drei X-Kegel), alles andere zusammengesetzt.
    selbst habe ich nicht gelesen.

## 7. Kartenvorschlag (hoechstens einer)

**PAAR-SAETTIGUNG-L (Literatur und Schreibtisch, kein Rechenlauf):** Gilt fuer zusammengesetzte Photonen die Grenze
"Bausteinbesetzung ~ 8 n", und schliessen gemessene Rayleigh-Jeans-Spektren den 3D-Paarbau damit aus? Gibt es einen Bau,
der sie vermeidet (Jordans kollinearer Bau mit Dirac-See, also Bosonisierung; Teilchen-Loch-Paare)?

- **Ableitbarkeitsprobe:**
  - Vorab ableitbar [M]: Faktor 8 (Halbierung des Impulses, Phasenraum / 8) und die Bedingung n << 1/8 im Breitband.
    Darum kein Rechenlauf; ein Gitterlauf wuerde nur diese Zaehlung bestaetigen.
  - Nicht ableitbar, nur Literatur:
    - (a) ob die Zeitschriftenfassung (Ann. Phys. 368, 2016) oder Folgearbeiten die 10^90-Schaetzung und Gl. (44)
      aendern;
    - (b) ob die Komposit-Boson-Theorie (Combescot u. a., Chudzicki/Oke/Wootters, Law; Bisio Ref. [40]-[46]) den
      Fremdmoden-Term kennt oder eine Aufhebung zeigt, etwa im Vakuum mit gefuelltem See, wo Delta nicht positiv ist;
    - (c) was Jordan 1935 und Pryce 1938 tatsaechlich zeigen.
  - Projektsuche: "Pryce", "composite photon", "Neutrinotheorie" kommen laut Karte im Projekt nicht vor [P].
- **Kann scheitern:** wenn (b) eine Aufhebung zeigt oder der Paarbau mit einer Verschmierung arbeitet, die Gl. (20)
  nicht verletzt und trotzdem 8 n vermeidet.
- **Kann bestehen:** wenn keine Quelle den Fremdmoden-Term aufhebt. Dann ist der 3D-Paarbau an Rayleigh-Jeans-Daten
  gebunden, und es bleibt nur der kollineare Bau mit Pryce-Problem.
- **Erwartungen (vorab):**
  - PS1 [H]: Die Zeitschriftenfassung behaelt die 10^90-Schaetzung (60 %).
  - PS2 [H]: Die Komposit-Boson-Literatur beschraenkt Bose-Verhalten auf kleine Phasenraumdichte der Bausteine (65 %).
  - PS3 [H]: Jordans Bau ist nur in 1D bzw. kollinear exakt bosonisch, und nur mit Dirac-See (70 %).
- **Bedeutung:**
  - PS2 trifft ein: Der dritte Weg ist fuer Licht mit hoher Besetzung zu.
  - PS2 verfehlt: Paar-Licht bleibt fuer Finn eine echte Weiche.

## 8. Gegensweep, Kalibrierung, offene Fragen, Quellen, Selbstanzeigen

### 8.1 Gegensweep (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
| Nr | Selbstverstaendlich genommen | geprueft? | Ausgang |
|---|---|---|---|
| G1 | Im QCA hat das Elektron dasselbe Grenztempo wie die Bausteine des Photons | ja, lokal | Ja, bis O(m^2) ~ 1e-45 [S-lokal Gl. (37), (62), (63); M]. **Zusatz:** Das Elektron erbt das lineare Glied voll, das Photon halb (V8) |
| G2 | phi (mit A*) laeuft wie psi | ja, Ueberlegung | Ja, A* hat dieselben Eigenphasen [M] |
| G3 | Zeitschriftenfassung 2016 = arXiv v1 | nein | Kein Abruf frei. Gl. (44) und die 10^90-Schaetzung koennten dort berichtigt sein |
| G4 | Pryce 1938 betrifft Querheit/Drehverhalten | nein | [L?]; Bisio liest ihn als Kommutator-Einwand (V7) |
| G5 | FKM liefert ein (psi, phi)-Paar wie Bisio | nein | Kramers-Partner als phi naheliegend; 16 Bilineare je Kegel, Auswahl offen [ES] |
| G6 | Paarbau gibt exakt dasselbe Tempo | ja, Ueberlegung | Nur fuer qbar -> 0; Querverschmierung eps kostet 2 eps^2 [M] |
| G7 | Zusatzmoden gamma^0, gamma^3 sind harmlos | teilweise | Frequenz 0, also kein Tempo [M aus S Gl. (19)]; thermodynamisch ungeklaert (Moden bei omega = 0) [ES] |

### 8.2 Kalibrierung
- **(a) gemessen:** DeMille v < 1,2e-7; English nu < 4,0e-11 (Abstracts); Coblentz-Hohlraum (ueber Perkins);
  GRB-Laufzeiten nur zitiert; LHAASO-Zahl nur ueber das Projekt.
- **(b) nuetzlich verdichtet:**
  - omega_gamma(k) = 2 omega_F(k/2) an der Quelle;
  - Formabschnitte der Karte gegengelesen;
  - Ungleichung "Paar-Licht im k^2-Glied nie langsamer als FKM-Fermion" (bei qbar -> 0) [M];
  - Verhaeltnis 1/3 gegen 1/4 [M];
  - Moderatoren M1 bis M6;
  - Tausch Bose gegen Maxwell ueber qbar [S + M].
- **(c) gewachsene Gewissheit ohne neue Evidenz:**
  - Die 8n-Rechnung: Nach dem Lesen von Perkins Gl. (22) (Ein-Moden-Annahme) stieg meine Sicherheit. Keine Quelle
    bestaetigt die Rechnung, es ist meine Zaehlung.
  - Der Faktor 3 sqrt3 in Gl. (44): eigene Rechnung gegen eine gedruckte Formel, aus pdftotext gelesen.
  - Cherenkov-Schwelle 2e4 GeV und Krebsnebel: EFT-Annahme plus [L].
- **Warnzeichen:** Meine Sicherheit, dass der Paarbau in Schwierigkeiten ist, stieg, waehrend die Frage in feinere Teile
  zerfiel: Symmetrie gegen Saettigung, eine Mode gegen viele, EFT gegen DSR, quer gegen kollinear. Getragen ist das von
  zwei Quellenstellen (Gl. (20) bei Bisio, Gl. (22) bei Perkins) und sonst von eigener Rechnung.

### 8.3 Offene Fragen
- O1: Haelt die 8n-Rechnung? Frischer Leser plus Literatur (Kartenvorschlag).
- O2: Vorfaktor des linearen Glieds (Gl. (44) gegen meine Rechnung); Zeitschriftenfassung pruefen.
- O3: Schleifen: Bleibt omega_gamma = 2 omega_F(k/2) mit Wechselwirkung? Im freien Bau ist das "Photon" nur eine Wahl
  des Zustands im Zwei-Fermionen-Kontinuum (fuer konkave Dispersion liegt 2 omega(k/2) am oberen Rand des kollinearen
  Kontinuums [M]). Mit Wechselwirkung kann es zerfallen oder gebunden werden; das ist nicht untersucht.
- O4: Thermodynamik der Frequenz-0-Moden gamma^0 und gamma^3.
- O5: Inhalt von Jordan 1935 und Pryce 1938.
- O6: Welche FKM-Bilineare tragen auf Finns Netz die zwei Querpolarisationen, und koppelt nur eine Kegelkombination an
  Ladungen?
- O7 (aus LICHT-GLEICH-L O2): Potenz-Annaeherung fuer ein zusammengesetztes Photon. Der Paarbau braucht sie auf
  Baumebene nicht; fuer Schleifen bleibt sie offen.

### 8.4 Quellenliste (Abrufstand 2026-10-05, Kopien in quellen/)
| Quelle | URL | Abruf (date) | gelesen |
|---|---|---|---|
| Bisio, A.; D'Ariano, G. M.; Perinotti, P. (2014/2016): Quantum Cellular Automaton Theory of Light, Annals of Physics 368, 177-190, doi 10.1016/j.aop.2016.02.009 | https://arxiv.org/abs/1407.6928 (v1) | Liste 04:35:07 (R2-...xml); pdf 04:35:36 (R3-...pdf, .txt, -layout.txt; sha256 8f36b093...) | [S] ganz (v1) |
| Perkins, W. A. (2001/2002): Quasibosons, Int. J. Theor. Phys. 41, 823-838, doi 10.1023/A:1015728722664 | https://arxiv.org/abs/hep-th/0107003 | Abstract 04:42:07 (R4-...xml); pdf 04:42:30 (R5-...pdf, .txt; sha256 1077f959...) | [S] ganz |
| DeMille, D.; Budker, D.; Derr, N.; Deveney, E. (1999): Search for exchange-antisymmetric two-photon states, PRL 83, 3978 | https://arxiv.org/abs/physics/9906025 | 04:42:07 (R4-...xml) | [S Abstract] |
| English, D.; Yashchuk, V. V.; Budker, D. (2010): Spectroscopic test of Bose-Einstein statistics for photons, PRL 104, 253604 | https://arxiv.org/abs/1001.1771 | 04:42:07 (R4-...xml) | [S Abstract] |
| Brun, T. A.; Mlodinow, L. (2025): Quantum Electrodynamics from Quantum Cellular Automata, and the Tension Between Symmetry, Locality and Positive Energy, Entropy 27(5), 492 | https://arxiv.org/abs/2503.05998 | 04:44:01 (R6-...xml) | [S Abstract] |
| Bakircioglu, D.; Arnault, P.; Arrighi, P. (2025): Fermion Doubling in Quantum Cellular Automata | https://arxiv.org/abs/2505.07900 | 04:44:01 (R6-...xml) | [S Abstract] |
| Bakircioglu, D.; Arnault, P. (2026): Fermion-doubling problem in Chiral discretizations of Quantum field theory | https://arxiv.org/abs/2607.14874 | 04:44:01 (R6-...xml) | [S Abstract] |
| D'Ariano, G. M.; Perinotti, P. (2014): Derivation of the Dirac equation from principles of information processing, PRA 90, 062106 | https://arxiv.org/abs/1306.1934 (v2) | lokal: qca-tetra-1/quelle/, Text nach quellen/L1-lokal-... | [S-lokal] Gl. (37), (38), (60)-(64) |
| R1 (leer, 0 Byte) | http://export.arxiv.org/api/query?search_query=au:Bisio+AND+ti:light | 04:34:50 | - |
| Pryce, M. H. L. (1938), Proc. R. Soc. A 165, 247; Jordan, P. (1935), Z. Phys. 93, 464; de Broglie (1934); Kronig (1936) | - | nicht abgerufen (nicht frei bzw. nicht auf arXiv) | nur bibliografisch ueber Bisio [S Lit.] |
| Abdo u. a. (2009), Nature 462, 331; Vasileiou u. a. (2013), PRD 87, 122001; Amelino-Camelia u. a. (1998), Nature 393, 763 | - | nicht abgerufen | nur als Bisio-Zitate |
| Projektdateien: licht-gleich-l/DOSSIER.md, qca-tetra-1/ERGEBNIS.md, diamant-nullstellen-1/ERGEBNIS.md, drei-kegel-neutrino-l/DOSSIER.md, licht-finn-netz-1/ERGEBNIS.md, RUNDE-41.md Z. 500-506, RUNDE-43/WEICHE-STAND-v8.md Z. 60 | lokal | gelesen 04:30 bis 04:48 | [P] |

### 8.5 Selbstanzeigen
1. **R1 verschenkt:** http ohne -L gab 0 Byte (Umleitung auf https). Ein Abruf weniger; deshalb fehlen die Zeitschriftenfassung
   (G3) und Pryce/Jordan.
2. **curl statt WebFetch:** Der Auftrag nennt WebFetch fuer arxiv.org. Ich habe curl auf dieselben arXiv-Adressen
   genutzt, weil nur so Kopien mit Abrufzeit nach quellen/ moeglich waren.
3. **Nur v1 gelesen** (2014), nicht die Zeitschriftenfassung 2016. Formeln aus pdftotext, teils zerlegt. Gl. (44) habe
   ich im Layout-Text gelesen; ein Lesefehler ist moeglich.
4. **Ausserhalb der Leseliste gelesen:** Projekt-grep nach "isotacheia" (mit allen Ausschluessen), dann RUNDE-41.md
5. **Lokale Kopie konvertiert:** pdftotext der D'Ariano/Perinotti-Datei aus qca-tetra-1/quelle nach meinem quellen/
   (Lesen, kein Abruf, nichts in fremde Ordner geschrieben).
6. **Handrechnungen ungegengelesen:** Gl.-(44)-Faktor, 8n-Zaehlung, Cherenkov-Schwelle, a2-Ungleichung,
   2-eps^2-Abzug. Zahlen wie 2,4e83 Zellen und 7e-8 sind Kopfrechnung.
7. **[L]-Zahlen im Text:** CMB-Besetzung bei 60 GHz, PeV-Elektronen im Krebsnebel, BBN/CMB-Freiheitsgrade. Alle
   ungeprueft und als [L] markiert.
8. **24-Monats-Suche schmal:** eine API-Abfrage mit Abstract-Phrasen, 8 Treffer.
9. **Formabschnitte:** wie verlangt nur gegengelesen; die Ergaenzung "Eis/FKM = 1/3" ist eine Division zweier
   Kartenformeln, keine neue Herleitung.
10. Keine Secrets, kein Journal, kein Peerbus, kein Commit, kein Rechenlauf, lokal kein python/awk/perl, jq nicht
    benutzt. Geschrieben nur in RUNDE-37/paar-licht-l/. Versiegeltes und KS-1 nicht geoeffnet.

## 9. Einfach gesagt

Man kann Licht als Paar aus zwei Teilchen bauen, und dann laeuft es automatisch genau so schnell wie diese Teilchen.
Drei italienische Physiker haben das 2014 fuer ein Gitter-Modell durchgerechnet; fuer Finns Netz ergibt die
Tischrechnung, dass solches Licht bei kurzen Wellen nicht hinter die Elektronen zurueckfiele, solange die beiden
Bausteine fast gleich schnell in dieselbe Richtung laufen. Der Haken: Ein Lichtteilchen aus zwei
Teilchen, die sich nicht stapeln lassen, kann vermutlich nicht beliebig viele Geschwister im selben Zustand haben. Nach
meiner eigenen, noch ungeprueften Rechnung ginge das schon bei ganz gewoehnlichem Waermelicht schief. Ob diese Rechnung
stimmt, sollte als Naechstes ein frischer Leser mit der Fachliteratur pruefen.
