# DREI-KEGEL-NEUTRINO-L: Arbeitsfeld (eine Datei, wird vor jedem Schritt neu gelesen; Gestrichenes bleibt stehen)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-05 01:08:24 CEST (date). Zeitbox 30 min, also bis ~01:38.
- KARTE.md gelesen (bindend, DN-1 unveraendert). Vorlektuere: drei-kegel-l/DOSSIER.md (ganz), diamant-nullstellen-1/ERGEBNIS.md,
  licht-finn-netz-1/NACHTRAG-PHASE-GRUPPE.md, kubisch-anker-l/DOSSIER.md; grep IceCube in RUNDE-34/grb-221009a/DOSSIER.md
  und RUNDE-09/spin1/SPIN1.md (alle Ausschluesse): dort nur Neutrinogrenzen gegen GRB-Modelle (Z. 191, 197) und
  IceCube/AMANDA-Monopolsuche (SPIN1 Z. 178). **Keine Neutrino-LIV im Projekt** [P].

## 0. Schreibtisch vor jedem Abruf [M] (ab 01:14 CEST)

### 0.1 Laengeneinheit
- diamant-nullstellen-1/PLAN.md Z. 76: "a = 2 sqrt2 PU, b = sqrt6/2 PU, k in 1/PU" [P].
- licht-finn-netz-1/PLAN.md Z. 32: "Laengeneinheit l = 1 PU = Tetraederkante (Pyrochlor-Abstand). Daraus kubische
  Gitterkonstante 2 sqrt2 PU und Diamant-Kante b = sqrt(6)/2" [P].
- **Also ist die Code-Laenge PU schon die Tetraederkante. Umrechnungsfaktor 1.** Probe von Hand: laengs z an X_z gibt
  der Naechste-Nachbar-Term f = -4 sin(q a/4), also E = 4t sin(qa/4) = t a q (1 - a^2 q^2/96). Mit a^2 = 8 PU^2 folgt
  a2 = -8/96 = -1/12 pro (q PU)^2. Das ist der Tabellenwert [E]. Tempo t a = 2,8284 PU, auch wie Tabelle.
- Vorsicht Namensfalle: Das Tetraeder aus den vier Nachbarn EINES Diamant-Atoms hat die Kante a/sqrt2 = 2 PU. Projektkonvention
  ist die Pyrochlor-Tetraederkante (1 PU). In Diamant-Kanten b: a2 durch 1,5 teilen.

### 0.2 Allgemeine Form a2_r(n) je Kegel (aus den fuenf Tabellenwerten [E] von DIAMANT-NULLSTELLEN-1)
- Ansatz mit der Symmetrie an X_z (D4h, z ausgezeichnet): a2_z = alpha n_z^4 + beta (n_x^4 + n_y^4) + gamma n_x^2 n_y^2
  + delta n_z^2 (n_x^2 + n_y^2).
- laengs z: alpha = -1/12; quer x: beta = -1/3; 110 quer -17/48 gibt gamma = -3/4; 110 schraeg -7/24 gibt delta = -3/4.
- Unabhaengige Probe 111: (-1/12 - 2/3 - 3/4 - 3/2)/9 = -1/3, Tabelle -0,333333. Trifft.
- Vereinfacht (u, v, w = n_x^2, n_y^2, n_z^2; S4 = u^2 + v^2 + w^2):
  **a2_r(n) = -3/8 + S4/24 + n_r^4/4**  (r = Achse des Kegels).
  - Proben: z an X_z: -3/8 + 1/24 + 1/4 = -1/12. x an X_z: -3/8 + 1/24 = -1/3. 110 quer: -3/8 + 1/48 = -17/48.
    110 schraeg: -3/8 + 1/48 + 1/16 = -7/24. 111: -3/8 + 1/72 + 1/36 = -1/3. Alle fuenf treffen.
  - Der gemeinsame Teil -3/8 + S4/24 hat dieselbe kubische S4/24-Form wie Maxwell auf Finns Netz (-1/8 + S4/24) [P].
- **Kegelabhaengig ist nur n_r^4/4.** Differenzen: a2_x - a2_z = (n_x^4 - n_z^4)/4.
  - laengs Wuerfelachse z: Kegel (x, y, z) = (-1/3, -1/3, -1/12), Spaltung 1/4 (ein Kegel gegen zwei entartete).
  - laengs [110]: (-7/24, -7/24, -17/48), Spaltung 1/16.
  - laengs [111]: alle -1/3, Spaltung 0. Die Karte sagt dasselbe.
- **Kugelmittel:** <a2_r> = -3/10 fuer jeden Kegel (Probe: -3/8 + (3/5)/24 + (1/5)/4 = -3/10).
  **Der kegelabhaengige Teil hat also keinen isotropen Anteil (j = 0).** Er ist rein j = 2 und j = 4:
  n_r^4 - S4/3 = (4/7) P2(n_r) + (8/35) [P4(n_r) - (1/3) sum_s P4(n_s)].
  - Folge [ES, vor jedem Abruf]: Isotrope Schranken (c-ring) treffen die Flavour-Differenzen des Modells nicht direkt.
    Die Himmelsrichtung ist nicht Nebensache, sondern traegt das ganze Signal.

### 0.3 Phase gegen Gruppe, SME-Abbildung
- a2 ist Phasenkoeffizient [P NACHTRAG]: omega/k = 1 + a2 (k l)^2, Gruppe 1 + 3 a2 (k l)^2.
- Hamiltonian je Kegel (hbar = c = 1, E ~ p): h_r = p + a2_r(n) l^2 p^3. Oszillationen sehen nur Differenzen von h, also
  Phasen-, nicht Gruppenkoeffizienten. **Fuer Oszillationsschranken entfaellt der Faktor 3.** Er zaehlt nur fuer Laufzeit.
- SME-Neutrinoform [L, an der Quelle zu pruefen]: delta h_ab = -E^3 sum_jm Y_jm(p^) c^(6)_ab,jm, isotrop -E^3 c-ring^(6)_ab.
  Dann c^(6)_eff,rr(n) = -a2_r(n) l^2; kegelabhaengiger Teil -(l^2/4) n_r^4.

### 0.4 Zwei Regime vor dem Abruf (Feldregel 1) [ES]
- **Regime A, Kegel = Flavour-Basis** (geladene Leptonen ebenfalls Kegel auf demselben Netz, schwacher Strom erhaelt den
  Kegelindex; PMNS kommt aus einem translationsbrechenden Neutrino-Massenterm). LIV ist diagonal in e, mu, tau.
  - Bei hoher Energie gewinnt LIV: Propagationszustaende = Flavours, keine Oszillation, Flavour bei der Erde = an der Quelle.
  - Atmosphaerische mu-Disappearance bei TeV: LIV unterdrueckt nur die ohnehin kleine Oszillation, kaum Empfindlichkeit.
  - Astrophysikalische Flavour-Zusammensetzung: sehr empfindlich. Schwelle grob l^2 ~ dm^2/(2 Delta E^4): mit dm^2_atm =
    2,5e-21 GeV^2, Delta ~ 0,1, E = 1e5 GeV folgt l ~ 1e-20 GeV^-1 ~ 2e-36 m ~ 0,1 l_P [M, grob].
- **Regime B, Kegel = Massenbasis** (Neutrinomasse translationsinvariant, also diagonal je Kegel; PMNS aus dem
  geladenen Sektor). LIV ist diagonal in nu_1, nu_2, nu_3.
  - Astrophysikalische Flavour-Zusammensetzung: blind (gemittelte P haengt nur an abs(U)^2).
  - Atmosphaerische Interferometrie bei TeV: empfindlich, Phase c E^3 L ~ 1 bei E ~ 20 TeV, L ~ 1,3e4 km gibt c ~ 2e-36
    GeV^-2. Mit Delta ~ 0,1 bis 0,25: l ~ 3e-18 GeV^-1 ~ 6e-34 m ~ 40 l_P [M, grob].
- Moderator: welcher Sektor den translationsbrechenden Massenterm traegt (Neutrinos oder geladene Leptonen).
- Unterscheidungspunkt: Flavour-Zusammensetzung astrophysikalischer Neutrinos (A: Quellmischung bleibt, B: Standardwert)
  gegen TeV-Disappearance atmosphaerischer nu_mu (B: zusaetzliche Disappearance, A: keine).

## 1. Lokale Lesung L1 (kein Abruf): Data Tables v19, lokale Kopie von KUBISCH-ANKER-L

- **Erwartung 01:14:30 CEST (date):** Die Neutrino-Tabellen fuehren fuer d = 6 isotrope c-ring^(6) aus IceCube 2018
  (atmosphaerisch, Re/Im mu-tau, ~1e-36 GeV^-2) und IceCube 2022 (astrophysikalische Flavours, ~1e-42 GeV^-2, Sektoren
  e-mu, mu-tau). Richtungsabhaengige d = 6-Flavourkoeffizienten (j = 2, 4) gibt es dort nicht oder nur als Abschaetzung.
- **Ausgang 01:15 bis 01:16 (Erwartung teils verletzt):** Seiten 114 bis 125 lokal mit pdftotext -layout nach
  quellen/L1-datatables-D39-layout-S114-125.txt (01:15:42). Table D39 (d = 6, Neutrinos):
  - Teil 12, Z. 849: "|Re c-ring^(6)_mu-tau|, |Im c-ring^(6)_mu-tau| < 9.1 x 10^-37 GeV^-2, IceCube [284]" = Aartsen u. a.
    2018, Nature Physics 14, 961, 1709.03434 [S-lokal]. Wie erwartet (~1e-36).
  - Teil 12, Z. 851: "Re c-ring^(6)_tau-tau < 3 x 10^-42 GeV^-2, IceCube [291]" = Abbasi u. a. 2022, Nature Physics 18,
    1287, 2111.04654; Argueelles u. a. ICRC2023 [S-lokal]. **Verstoss:** ein DIAGONALES Element (tau-tau), nicht e-mu/mu-tau.
  - **Teil 4, Z. 194 ff.: richtungsabhaengige Flavour-Koeffizienten (c_eff)^(6)_ab,jm fuer alle ab und jm = 00, 10, 11
    (und weiter), je < 4e-37 bis 1e-36 GeV^-2, "Astrophysical neutrinos" [257]* = Telalovic, B.; Bustamante, M.,
    arXiv:2503.15468** [S-lokal]. Stern = von Dritten aus Daten abgeleitet. **Grosser Verstoss:** Es gibt d = 6-Schranken
    MIT Himmelsrichtung, und sie liegen ~5 Groessenordnungen ueber dem isotropen tau-tau-Wert.
  - Flavour-unabhaengig (Teil 1 bis 3): c_of,jm aus IceCube [294]* = Diaz/Kostelecky/Mewes 2014 (1308.6344), ~1e-27 bis
    1e-28 GeV^-2 fuer j <= 4, c_of,00 > -3e-31; c-ring^(6) > -5.23e-35 [295]* (Stecker u. a. 2015). Nur fuer den
    gemeinsamen Teil (Spur) relevant.
- Korrektur der Erwartung: Fuer die Himmelsrichtung ist Telalovic/Bustamante 2025 die Schluesselquelle (im 24-Monats-Fenster).
  Offen R-1: Warum liegen die anisotropen Werte bei ~1e-36 und der isotrope tau-tau-Wert bei 3e-42?

## 2. Abruf R1 (arXiv-API id_list, Abstracts)

- **Erwartung 01:16:54 CEST (date):** 2503.15468 (Telalovic/Bustamante): Flavour-Zusammensetzung nach Himmelsrichtung
  (HESE), Schranken auf alle c_eff,jm fuer d = 3 bis 8, schwaecher als isotrop, weil wenige Ereignisse je Richtung.
  2111.04654: Flavour-Zusammensetzung, d = 6 "Planck-Skala erreicht", ~1e-42. 1709.03434: mu-tau, d = 6 ~1e-36.
  2403.02516: sieben nu_tau-Kandidaten, Fehlen von nu_tau mit ~5 sigma verworfen.
- **Ausgang 01:17:17 (Kopie quellen/R1-arxiv-api-idlist-20261005-011717.xml), alle vier bestaetigen die Erwartung:**
  - 2111.04654 (Nature Physics 2022): "We place the most stringent limits ..., down to 10^-42 GeV^-2, on the
    dimension-six operators ... for preferred astrophysical production scenarios" [S Abstract].
  - 1709.03434: d = 4 "to the 10^-28 level", hoehere Dimensionen ohne Zahl [S Abstract]; d = 6 nur ueber Data Tables
    (9.1e-37) [S-lokal].
  - 2403.02516 (PRL 132, 151001, 2024): "seven candidate nu_tau events ... 20 TeV to 1 PeV ... we rule out the absence of
    astrophysical nu_tau at the 5 sigma level" [S Abstract].
  - 2503.15468 (JHEP 02 (2026) 024): Titel "No Flavor Anisotropy in the High-Energy Neutrino Sky Upholds Lorentz
    Invariance"; "compass asymmetries, where neutrinos of different flavors propagate preferentially along different
    directions"; HESE 7.5 Jahre; Schranken auf "hundreds of LIV parameters with operator dimensions 2-8" [S Abstract].
  - [ES] "Kompass-Asymmetrie" ist genau die Signatur der drei Kegel: Kegel r ist laengs seiner Achse am schnellsten.
- Offen R-1 bleibt: Abstract erklaert nicht, warum 4e-37 (anisotrop, T/B) gegen 3e-42 (isotrop tau-tau, IceCube).

## 3. Abruf R2 (arXiv-pdf 2503.15468)

- **Erwartung 01:18:11 CEST (date):** H_LIV im Sonnen-Himmelsrahmen mit Y_jm(Ankunftsrichtung), je Koeffizient einzeln
  variiert (die uebrigen null), Quellzusammensetzung frei bzw. marginalisiert; dadurch viel schwaecher als IceCube 2022.
  Konvention wie Kostelecky/Mewes 2012 (delta h = -E^3 sum Y_jm c_jm). Grenzen fuer j = 2 und j = 4 ebenfalls ~1e-36.
- **Ausgang 01:18:31 (Kopie quellen/R2-telalovic-bustamante-2503.15468-20261005-011831.pdf/.txt; Tabelle A5 Seiten 54
  bis 57 mit -layout in R2-TB-tabelleA5-layout-S54-57.txt):** Erwartung im Kern bestaetigt, zwei Teilverstoesse.
  - Konvention [S Gl. (2.2) bis (2.4), Z. 289-330]: H_LIV = (1/E)(a_eff - c_eff), c_eff = sum_d E^(d-2) sum_lm
    Y_lm(p^) (c_eff)^(d)_lm, p^ = Flugrichtung im Sonnen-Himmelsrahmen. Also delta h = -E^3 sum Y c fuer d = 6. Wie [L].
  - Strategie [S Tab. 1, Z. 1935 ff.; Abschn. 6.2 Z. 2486-2490]: "a single nonzero complex LIV parameter at a time";
    vier Annahmen zur Quellzusammensetzung (beliebig, 1/3:2/3:0, 1:0:0, 0:1:0); 12 Himmelspixel [S Z. 1925 ff.].
  - **Teilverstoss 1 (Prior):** "Uniform in [-10^-(4d+10), 10^-(4d+10)]" [S Tab. 1], fuer d = 6 also linear-gleichverteilt
    bis +-1e-34 GeV^-2. Nicht erwartet. [ES] Bei einer saettigenden Likelihood haengt eine 95-%-Grenze ~1e-36 dann
    vom Prior-Fenster ab. Offen R-2.
  - **Teilverstoss 2 (Grund der Schwaeche):** T/B nennen die Mindestenergie: IceCube 2022 E_min ~ 60 TeV, T/B 10 TeV;
    Empfindlichkeit ~1e-23 (E_min/GeV)^(2-d) GeV^(4-d) [S Abschn. 6.3, Z. 2828-2870]. Dazu "strong degeneracy with the
    flavor composition at the sources" und "coarse sky tessellation" [S Z. 2820-2827].
    Probe [M]: d = 6 gibt 7,7e-43 (60 TeV) gegen 1e-39 (10 TeV), Faktor 1300. Gefunden: 4e-37 (T/B, c_00 tau-tau) gegen
    3e-42 c-ring = 1,1e-41 in c_00 (c_00 = sqrt(4 pi) c-ring), Faktor ~4e4. **Rest ~30 bleibt unerklaert** (R-2).
  - Werte Tab. A5, d = 6, diagonal, Quelle (1/3, 2/3, 0), 95 % [S]:
    - l = 0: ee "—" (nicht begrenzt), mumu 4e-37, tautau 4e-37.
    - l = 2: ee_20 9e-37, ee_21 Re 9e-37, ee_22 Norm 1e-36; mumu_20 7e-37, mumu_21 Norm 1e-36 (Re, Im 8e-37), mumu_22
      Norm 1e-36 (Re 8e-37, Im 9e-37); tautau_20 6e-37, tautau_21 Norm 9e-37 (Re, Im 7e-37), tautau_22 Norm 1e-36
      (Re, Im 8e-37).
    - l = 4: ee_40 "—"; mumu_40 7e-37; tautau_40 7e-37; tautau_41 bis 44 Norm 9e-37 bis 1e-36.
    - Quelle (1, 0, 0): mumu und tautau ~2e-38 (staerker). "Any": 6e-37 bis 1e-36.
  - [ES] ee aus Pion-Quelle unbegrenzt passt zum Schreibtisch: entkoppelt nu_e, mischen mu und tau weiter fast maximal,
    das Ergebnis liegt nahe 1/3:1/3:1/3.

## 4. Abruf R3 (arXiv-API, 24-Monats-Fenster, Feldregel 7)

- **Erwartung 01:21:55 CEST (date):** Ausser Telalovic/Bustamante 2025 keine weitere veroeffentlichte richtungsabhaengige
  d = 6-Flavour-Schranke 2024-10 bis 2026-10; zu erwarten sind KM3NeT/ORCA-Isotropschranken (d = 3, 4),
  KM3-230213A-Arbeiten (flavourblind) und Prognosen (IceCube-Gen2, P-ONE).
- **Ausgang 01:22:25 (Kopie quellen/R3-arxiv-api-24monate-20261005-012225.xml, 40 Eintraege nach Datum):** bestaetigt.
  - KM3NeT/ORCA6, 2603.04264: "A search for isotropic Lorentz invariance violation ... competitive limits ... on a subset
    of isotropic ... coefficients" [S Abstract]. Nur isotrop.
  - 2604.19880 (GRAND/POEMMA, UHE-nu_tau): Prognose [S Abstract]. Sonst DUNE/NOvA-Sidereal (Prognosen, d = 2 bis 4),
    Reaktor-Anisotropie (2025), Superluminal-Schranken aus UHE-Ereignissen (flavourblind).
  - Keine weitere richtungsabhaengige d = 6-Flavourschranke ausser T/B (Titel-Liste; Wortwahl-Grenze: "Lorentz" Pflicht).
- Zusatzpruefung lokal (kein Abruf), 01:23:19: T/B Tab. A3 (d = 4), Seite 49 -layout: (c_eff)^(4)tautau_00 < 4e-29,
  tautau_20 < 8e-29 (Quelle 1/3:2/3:0) [S]. Fuer Gegensweep G1 (Abstimmung t = 4 lambda).

## 5. Rechnungen fuer das Dossier [M] (01:23 bis 01:24)

- 1 GeV^-1 = 1,97327e-16 m; l_P = 1,616e-35 m = 8,19e-20 GeV^-1; l_P^2 = 6,7e-39 GeV^-2 [L, Standardwerte].
- j = 2-Teil des kegeleigenen Terms: -(l^2/4)(4/7) P2(n.e_r) = -(l^2/7) P2(n.e_r). Additionstheorem:
  c_rr,2m = -(l^2/7)(4 pi/5) Y*_2m(e_r); drehfeste Norm N2 = (l^2/7) sqrt(4 pi/5) = 0,2265 l^2.
- j = 4-Teil (kegeleigen): -(2 l^2/35) P4(n.e_r); N4 = (2/35) sqrt(4 pi/9) l^2 = 0,0675 l^2.
- Regime A mit T/B (tau-tau, Quelle 1/3:2/3:0):
  - Achse r parallel Himmels-Z: 0,2265 l^2 < 6e-37 gibt l^2 < 2,65e-36, l < 19,9 l_P = 3,2e-34 m.
  - Kasten (alle fuenf Komponenten zugleich am Einzelrand): N2 <= sqrt(36 + 2 (49 + 49 + 64 + 64)) e-37 = 2,21e-36,
    l^2 < 9,75e-36, l < 38 l_P = 6,2e-34 m. mu-mu-Zeile: sqrt(595) e-37 = 2,44e-36, l < 40 l_P.
- Regime A, Uebertragung IceCube 2022 [ES]: rms des j = 2-Teils (l^2/7) sqrt(1/5) = 0,064 l^2; 0,064 l^2 > 3e-42 fast
  ueberall verboten gibt l^2 < 4,7e-41, l < 0,08 l_P ~ 1,4e-36 m.
- Regime B, Uebertragung IceCube 2018 [ES]: theta23 = 45 Grad bildet die Massenbasis-Spaltung auf Re c_mu-tau = Delta/2
  ab [M]. <(n_r^4 - n_s^4)^2> = 2/9 - 2/105 = 64/315, rms 0,451, also rms Delta = 0,113 l^2, Re c_mu-tau ~ 0,056 l^2.
  0,056 l^2 < 9,1e-37 gibt l < 49 l_P; mit der Hoechstspaltung 1/4 (Re c = l^2/8): l < 33 l_P.
- d = 4-Probe (G1): Bei t ungleich 4 lambda ist v(n) ~ v0 (1 + eps n_r^2), eps ~ 1 - 4 lambda/t; j = 2-Norm
  (2/3) sqrt(4 pi/5) abs(eps) = 1,06 abs(eps) < ~3 x 8e-29, also abs(eps) < ~2e-28.

## 6. Gegensweep (Feldregel 4) und Rueckfragen

- G1 "t = 4 lambda ist gegeben": GEPRUEFT (T/B Tab. A3 [S] + [M]): eine Abstimmung auf ~2e-28. Widerspricht "haengt
  nicht an einer Abstimmung".
- G2 "Der gemeinsame (flavourblinde) Teil spielt keine Rolle": GEPRUEFT (Data Tables Teil 3 [S-lokal]): die
  flavourblinden isotropen Grenzen sind einseitig "> -..." (superluminal); das Modell ist ueberall subluminal (a2 < 0),
  also nicht bindend. Die zweiseitigen c_of,jm (~1e-27) sind viel schwaecher.
- G3 "Oszillation sieht Phase, nicht Gruppe": GEPRUEFT ueber T/B Gl. (2.2) bis (2.4) [S] und Ableitung [M]. Faktor 1.
- G4 "Kegelbasis = Basis des schwachen Stroms" (Regime A): nicht geprueft, Modellfrage.
- G5 "Konvention c-ring = c_00/sqrt(4 pi)": nicht an der Quelle gefunden (grep in Data Tables ohne Treffer) [L].
- G6 "Einzelparameter-Grenzen gemeinsam verwendbar (Kasten)": nicht geprueft [ES].
- G7 "Erdmaterie und Rotverschiebungs-Verschmierung egal": nicht geprueft.
- Rueckfragen offen: R-2 (Prior und Restfaktor ~30 bei T/B), R-3 (welcher Sektor bricht die Translationen: A oder B).

## 7. Abschluss

- DOSSIER.md geschrieben ab 01:24:52, Korrekturen (Parameterzahl, Faktor in l) um 01:28:00 CEST. Abrufe: 3 von 4.
- Ende (date): 2026-10-05 01:28:05 CEST.
