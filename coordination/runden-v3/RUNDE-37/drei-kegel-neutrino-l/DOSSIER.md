# DREI-KEGEL-NEUTRINO-L: Dossier. Welche Maschenschranke folgt aus IceCube, wenn die drei X-Kegel die drei Neutrino-Generationen waeren? (Runde 45, Literatur und Schreibtisch)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-05 01:08:24 CEST, Dossier ab 01:24:52 CEST (date).
- Grundlage: KARTE.md (bindend, DN-1 unveraendert). Protokoll mit Erwartung vor jedem Abruf, Ausgang, Rechnungen,
  Gegensweep und Rueckfragen: ARBEITSFELD.md (gleicher Ordner).
- 3 von 4 Abrufen (curl: arXiv-API id_list, arXiv-pdf, arXiv-API nach Datum), keine Websuche. Dazu lokal (kein Abruf) die
  Data Tables v19 aus kubisch-anker-l/quellen/. Kopien und Seitenauszuege mit Abrufzeit in quellen/.
- Kennzeichen: [S Abschn./Gl./Tab./Z.] an der Quelle gelesen; [S Abstract]; [S-lokal] lokale Kopie eines frueheren
  Agenten, selbst gelesen; [P] Projektdatei; [E] dort gerechnet; [L] Gedaechtnis; [M] von Hand, numerisch ungeprueft;
  [ES] eigener Schluss; [H] Hypothese.
- **Alles ist Schreibtisch und Literatur zu einem gedachten Netz. Keine Messdaten zum Netz, keine Messdatenbestaetigung.**

## 1. Ergebnis zuerst

1. **Der generationsabhaengige Teil der Kegel-Dispersion hat keinen isotropen Anteil** [M aus E].
   - Aus den fuenf gerechneten Richtungswerten folgt a2_r(n) = -3/8 + S4/24 + n_r^4/4 (r = Achse des Kegels,
     S4 = sum n_i^4). Alle fuenf Werte treffen, auch der unabhaengige [111]-Wert.
   - Nur n_r^4/4 haengt vom Kegel ab. Sein Kugelmittel ist fuer alle drei Kegel gleich, also bleiben nur j = 2 und j = 4.
   - Die IceCube-Schranken der Kollaboration sind isotrop (j = 0). **Direkt folgt aus ihnen deshalb keine Grenze.**
2. **Mit Himmelsrichtung gibt es genau eine veroeffentlichte d = 6-Flavourschranke: Telalovic/Bustamante 2025**
   (IceCube-HESE 7,5 Jahre, JHEP 02 (2026) 024).
   - Die Diagonal-Koeffizienten (c_eff)^(6)_rr,2m liegen bei < 6e-37 bis 1e-36 GeV^-2 [S Tab. A5].
   - Daraus folgt **l < ~20 l_P** (eine Wuerfelachse parallel zur Himmelsachse) **bis l < ~40 l_P** (jede Ausrichtung,
     Kastenrechnung), also 3e-34 bis 6e-34 m [M].
3. **Das Urteil haengt am Mischungsmechanismus, nicht nur an a2** (zwei Regime, Feldregel 1) [M/ES].
   - Regime A: Die Kegel sind die Flavour-Basis, die Mischung kommt aus dem Neutrino-Massenterm. Dann aendert LIV die
     Flavour-Zusammensetzung astrophysikalischer Neutrinos. Uebertraegt man die isotrope IceCube-tau-tau-Grenze
     (3e-42 GeV^-2), folgt l < ~0,08 l_P [ES, grob]. Die Drei-Kegel-Neutrinos waeren dann ausgeschlossen.
   - Regime B: Die Kegel sind die Massenbasis, die Mischung kommt aus dem geladenen Sektor. Dann ist die
     astrophysikalische Flavour-Zusammensetzung blind. Es bleibt die atmosphaerische Interferometrie (IceCube 2018,
     mu-tau 9,1e-37), und daraus folgt l < ~30 bis 50 l_P [ES]. Die Hypothese ueberlebt.
4. **DN-1 ist nach Wortlaut eingetroffen, die Begruendung nur teilweise.** Die direkt anwendbaren veroeffentlichten
   Schranken geben 20 bis 40 l_P (A, T/B) bzw. 30 bis 50 l_P (B), beides im Fenster 10 bis 100 l_P. Der Gedaechtniswert
   1e-36 ist die mu-tau-Grenze von IceCube 2018 (9,1e-37) und gilt aber nur in Regime B.
5. **Der Gegensweep fand eine Abstimmung:** Die Isotropie der Kegel in erster Ordnung (t = 4 lambda) muss auf etwa 2e-28
   genau stimmen, sonst verletzen die d = 4-Flavourschranken (T/B Tab. A3: < 8e-29) [S + M]. Die Bedeutungszeile der
   Karte, die Vorhersage "haengt ... nicht an einer Abstimmung", trifft deshalb nicht zu.

## 2. Urteil zu DN-1

| Nr | Vorhersage (woertlich) | Wahrsch. | Urteil | Begruendung |
|---|---|---|---|---|
| DN-1 | [H, vorab] Die Schranke liegt bei l unter 10 bis 100 l_P. Grundlage ist ein Gedaechtniswert von ungefaehr 1e-36 GeV^-2 [L, ungeprueft] | 60 % | **eingetroffen (Wortlaut), Begruendung teilweise; nicht entscheidend** | (i) Veroeffentlichte Richtungsschranken (T/B 2025, Tab. A5) geben l < ~20 bis 40 l_P [S + M]. (ii) Der Gedaechtniswert stimmt: 9,1e-37 GeV^-2 fuer abs(Re c-ring_mu-tau), abs(Im c-ring_mu-tau), IceCube 2018 [S-lokal Data Tables D39 Teil 12]. Er ist aber isotrop und passt nur zu Regime B (Abschnitt 6). (iii) In Regime A gibt die Uebertragung der isotropen tau-tau-Grenze (3e-42) l < ~0,08 l_P [ES]. Nach der Karte heisst das: "ausgeschlossen". Sie ist keine veroeffentlichte Grenze fuer dieses Muster |

**Kann scheitern und bestehen (Karte), angewandt:**
- "l-Grenze oberhalb von l_P: Die Hypothese ueberlebt." Das gilt fuer alles, was direkt veroeffentlicht ist (T/B), und
  fuer Regime B.
- "Grenze deutlich unter l_P: ... ausgeschlossen, unabhaengig vom Mischungsargument." Das gilt nur in Regime A und nur
  ueber meine Uebertragung.
- Der Zusatz "unabhaengig vom Mischungsargument" haelt nicht: **Welches Regime gilt, entscheidet gerade der
  Mischungsmechanismus** (Erwartungsverstoss V3).

**Bedeutung nach Karte:** Eine unterscheidende Vorhersage (L9) gibt es. Sie ist aber an zwei Zusatzannahmen gebunden:
das Regime (A oder B) und die Abstimmung t = 4 lambda (G1).

## 3. Erwartungsverstoesse (das Wichtigste zuerst)

| Nr | Erwartet | Gefunden | Fundstelle | Korrektur |
|---|---|---|---|---|
| V1 gross | Karte: "Delta a2 = 1/4" laesst sich gegen IceCube-Isotropschranken setzen | Der kegelabhaengige Teil n_r^4/4 hat fuer alle drei Kegel dasselbe Kugelmittel (1/20). Die Flavour-Differenzen sind rein j = 2 und j = 4; isotrope Schranken treffen sie nicht | Abschnitt 4.2 [M aus E] | Es braucht Richtungsschranken. Die Himmelsrichtung traegt das ganze Signal |
| V2 gross | ARBEITSFELD L1: richtungsabhaengige d = 6-Flavourschranken gibt es nicht oder nur als Abschaetzung | Telalovic/Bustamante 2025 begrenzen "hundreds of LIV parameters with operator dimensions 2-8" ueber "compass asymmetries, where neutrinos of different flavors propagate preferentially along different directions" | 2503.15468 [S Abstract, Tab. A5]; Data Tables D39 Teil 4 [S-lokal] | Das ist genau die Kegel-Signatur (jeder Kegel ist laengs seiner Achse am schnellsten) [ES]. Die Grenzen liegen aber ~5 Groessenordnungen ueber der isotropen tau-tau-Grenze |
| V3 gross | Karte: "unabhaengig vom Mischungsargument"; "haengt nur an a2" | Ist LIV in der Massenbasis diagonal (Regime B), aendert es die gemittelte Flavour-Zusammensetzung nicht; ist es in der Flavour-Basis diagonal (A), dann schon. Die Grenze springt zwischen ~0,08 und ~40 l_P | Abschnitt 6 [M/ES] | Der Moderator ist der Sektor, der die Translationen bricht. Das ist eine Modellfrage (R-3) |
| V4 mittel | ARBEITSFELD L1: IceCube 2022 begrenzt e-mu und mu-tau | Data Tables fuehren "Re c-ring^(6)_tau-tau < 3 x 10^-42 GeV^-2", also ein Diagonalelement | D39 Teil 12, Z. 851 [S-lokal] | Ein Diagonalelement entspricht genau dem Muster laengs einer Wuerfelachse (ein Kegel gegen zwei entartete) [ES] |
| V5 mittel | Karte: keine Abstimmung | Ausserhalb von t = 4 lambda ist jeder Kegel schon in erster Ordnung (d = 4) anisotrop. T/B Tab. A3 verlangt abs(1 - 4 lambda/t) < ~2e-28 | Gegensweep G1 [S + M] | Zweite Bindung der Vorhersage |
| V6 klein | Zusatz der Leitung: Code-Laenge in Tetraederkante umrechnen; Gruppenfaktor 3 | PU ist bereits die Tetraederkante (beide PLAN-Dateien), Faktor 1. Oszillationen sehen Hamiltonian-Differenzen, also den Phasenkoeffizienten, Faktor 1 statt 3 | diamant-nullstellen-1/PLAN.md Z. 76; licht-finn-netz-1/PLAN.md Z. 32 [P]; T/B Gl. (2.2) bis (2.4) [S] | Wer 3 a2 einsetzte, bekaeme l um sqrt3 zu klein |
| V7 klein | T/B: Die Mindestenergie (10 statt 60 TeV) erklaert den Abstand zu IceCube | Ihre Formel gibt fuer d = 6 einen Faktor ~1300. Gefunden sind ~4e4 (4e-37 gegen 3e-42 c-ring = 1,1e-41 in c_00) | T/B Abschn. 6.3 [S]; [M] | Rest ~30 offen (R-2). Prior linear bis +-1e-34 GeV^-2 [S Tab. 1] |

## 4. Umrechnung [M]

### 4.1 Laengeneinheit (Tetraederkante)
- DIAMANT-NULLSTELLEN-1 rechnet mit "a = 2 sqrt2 PU, b = sqrt6/2 PU, k in 1/PU" [P PLAN Z. 76].
- LICHT-FINN-NETZ-1: "Laengeneinheit l = 1 PU = Tetraederkante (Pyrochlor-Abstand)" [P PLAN Z. 32].
- **Also gelten a2 = -1/12 und -1/3 schon pro (k l)^2, mit l = Tetraederkante. Der Faktor ist 1.**
- Probe von Hand: Laengs z an X_z gibt der Naechste-Nachbar-Term E = 4t sin(q a/4) = t a q (1 - a^2 q^2/96). Mit
  a^2 = 8 l^2 folgt a2 = -1/12; das Tempo t a = 2,828 trifft ebenfalls [E].
- Namensfalle: Das Tetraeder aus den vier Nachbarn EINES Diamant-Atoms hat die Kante a/sqrt2 = 2 l. In Diamant-Kanten
  b = 1,2247 l sind alle a2 durch 1,5 zu teilen; die Schranke gilt dann fuer b < 1,2247 x (Grenze in l).

### 4.2 Richtungsform je Kegel und Flavour-Differenz
- Ansatz mit der Symmetrie an X_z (vier quartische Invarianten), angepasst an laengs -1/12, quer -1/3, 110 quer -17/48 und
  110 schraeg -7/24 [E]. Unabhaengige Probe [111]: -1/3, trifft.
- Ergebnis: **a2_r(n) = -3/8 + S4/24 + n_r^4/4**. Der gemeinsame Teil hat dieselbe S4/24-Form wie Maxwell auf Finns
  Netz (-1/8 + S4/24 [P]).
- **Differenzen:** a2_r - a2_s = (n_r^4 - n_s^4)/4.
  - laengs einer Wuerfelachse: 1/4 (ein Kegel gegen zwei entartete)
  - laengs [110]: 1/16
  - laengs [111]: 0
- **Zerlegung des kegeleigenen Teils:** n_r^4 = 1/5 + (4/7) P2 + (8/35) P4 (Achse r). Der j = 0-Teil 1/20 ist fuer alle
  Kegel gleich und faellt aus jeder Differenz heraus.
  - j = 2: -(l^2/7) P2(n.e_r), drehfeste Norm N2 = (l^2/7) sqrt(4 pi/5) = 0,2265 l^2.
  - j = 4: -(2 l^2/35) P4(n.e_r), N4 = 0,0675 l^2.
- Mittelwerte: Kugelmittel je Kegel -3/10; Mittel der drei Kegel -3/8 + S4/24 + S4/12 = -1/3 + (3 S4 - 1)/24.

### 4.3 Phase gegen Gruppe
- a2 ist ein Phasenkoeffizient (omega/k = 1 + a2 (k l)^2), Gruppe 1 + 3 a2 (k l)^2 [P NACHTRAG-PHASE-GRUPPE].
- Der Hamiltonian je Kegel ist h_r = p + a2_r(n) l^2 p^3. Oszillationen messen Differenzen von h, also Phase.
  **Fuer Oszillationsschranken gilt Faktor 1.** Der Faktor 3 zaehlt nur fuer Laufzeiten.

### 4.4 SME-Abbildung (Konvention der Quelle)
- T/B Gl. (2.2) bis (2.4): H_LIV = (1/E)(a_eff - c_eff), c_eff = sum_d E^(d-2) sum_lm Y_lm(p^) (c_eff)^(d)_lm. Dabei ist
  p^ die Flugrichtung im Sonnen-Himmelsrahmen [S]. Fuer d = 6 heisst das delta h = -E^3 sum Y_lm c_lm.
- **Abbildung:** sum_lm Y_lm(n) (c_eff)^(6)_rr,lm = -a2_r(n) l^2. Der Wert ist positiv, das Modell also ueberall subluminal.
- **Kegeleigener Anteil im Sonnenrahmen** (Additionstheorem, e_r = Richtung der Wuerfelachse r am Himmel):
  - (c_eff)^(6)_rr,2m = -(l^2/7)(4 pi/5) Y*_2m(e_r)
  - (c_eff)^(6)_rr,4m = -(2 l^2/35)(4 pi/9) Y*_4m(e_r)
  - Diese Matrix ist diagonal in der Kegelbasis. In der Flavour-Basis ist sie diagonal nur in Regime A (Abschnitt 6).
- Isotrop: c-ring = c_00/sqrt(4 pi) [L, Konvention nicht an der Quelle nachgelesen, G5].

## 5. Schranke mit Quelle

| Quelle | Groesse | Wert (95 %, wenn nicht anders) | Gilt fuer die Kegel? | l-Grenze [M] |
|---|---|---|---|---|
| IceCube 2018, Nature Physics 14, 961 (1709.03434) | abs(Re), abs(Im) c-ring^(6)_mu-tau | < 9,1e-37 GeV^-2 [S-lokal D39 Teil 12, Z. 849]; Abstract nennt nur d = 4 "10^-28 level" [S Abstract] | isotrop; nur Regime B, als Richtungsmittel [ES] | ~30 bis 50 l_P (Re c_mu-tau = Delta/2, rms bzw. Hoechstwert) |
| IceCube 2022, Nature Physics 18, 1287 (2111.04654), ICRC2023 | Re c-ring^(6)_tau-tau | < 3e-42 GeV^-2 [S-lokal Z. 851]; "down to 10^-42 GeV^-2 ... for preferred astrophysical production scenarios" [S Abstract] | isotrop; nur Regime A, und nur ueber Uebertragung [ES] | ~0,08 l_P (rms des j = 2-Teils 0,064 l^2) |
| Telalovic/Bustamante 2025, JHEP 02 (2026) 024 (2503.15468) | (c_eff)^(6)_tautau,20 / ,21 / ,22 (Quelle 1/3:2/3:0) | 6e-37 / Re, Im 7e-37 / Re, Im 8e-37 GeV^-2 [S Tab. A5]; mumu aehnlich (7e-37 bis 9e-37); ee teils unbegrenzt ("—") | ja, mit Himmelsrichtung; Regime A | **~20 l_P** (Achse parallel Himmels-Z) bis **~38 l_P** (Kasten, jede Ausrichtung) |
| dieselbe, Quelle (1, 0, 0) | tautau, mumu, l = 2 | ~2e-38 GeV^-2 [S Tab. A5] | nur bei Neutronenzerfall-Quellen | in c ~30-mal, in l ~5-mal schaerfer |
| IceCube 2024, PRL 132, 151001 (2403.02516) | astrophysikalische nu_tau | "rule out the absence of astrophysical nu_tau at the 5 sigma level" [S Abstract] | Regime A: Bei dominanter LIV kaeme fast nirgends nu_tau an [ES] | stuetzt ~0,1 l_P in A, keine eigene Zahl |
| KM3NeT/ORCA6 2026 (2603.04264) | isotrope LIV | "competitive limits ... on a subset of isotropic ... coefficients" [S Abstract] | isotrop, nein | - |

- Rechnungen (Einzelheiten ARBEITSFELD 5), mit l_P = 1,616e-35 m = 8,19e-20 GeV^-1:
  - **A, T/B, Achse r parallel Z:** c_rr,20 = -0,2265 l^2 < 6e-37 gibt l^2 < 2,65e-36 GeV^-2, also l < 19,9 l_P (3,2e-34 m).
  - **A, T/B, beliebige Ausrichtung (Kasten):** N2^2 <= c20^2 + 2 sum (Re^2 + Im^2) = 488e-74, also N2 <= 2,21e-36.
    Daraus l^2 < 9,75e-36 und l < 38 l_P (6,2e-34 m). Die mu-mu-Zeile gibt 40 l_P.
  - **B, IceCube 2018:** Bei theta23 = 45 Grad wird die Massenbasis-Spaltung Delta zu Re c_mu-tau = Delta/2 [M].
    - rms von abs(n_r^4 - n_s^4) ist sqrt(64/315) = 0,451, also Delta_rms = 0,113 l^2. Daraus l < 49 l_P.
    - Mit der Hoechstspaltung l^2/4 folgt l < 33 l_P.
  - **A, Uebertragung IceCube 2022:** 0,064 l^2 > 3e-42 waere fast ueberall wirksam. Daraus l^2 < 4,7e-41, also
    l < 0,08 l_P (1,4e-36 m) [ES].
  - **Gemeinsame Pruefung:** Die Uebertragung nimmt an, dass eine isotrope Grenze fuer ein Muster gilt, das fast ueberall
    ungleich null ist. Das ist nicht veroeffentlicht [ES].
- **Nicht bindend:** Die flavourblinden Grenzen (Data Tables D39 Teil 1 bis 3) sind isotrop einseitig "> -5,23e-35",
  "> -3e-31" usw., gelten also der superluminalen Seite. Das Modell ist subluminal. Die zweiseitigen c_of,jm liegen bei
  ~1e-27 [S-lokal] (G2).

## 6. Regime und Moderatoren (Feldregel 1)

| Streitpunkt | Regime A | Regime B | Moderator | Beleg |
|---|---|---|---|---|
| In welcher Basis ist LIV diagonal? | Flavour-Basis (Kegel = e, mu, tau) | Massenbasis (Kegel = nu_1, nu_2, nu_3) | Welcher Sektor bricht die Translationen: Neutrino-Massenterm (A) oder geladene Leptonen (B). Ein translationsinvarianter Neutrino-Massenterm ist je Kegel diagonal (DREI-KEGEL-L 3.6 [P]) und fuehrt zu B | [M/ES]; T/B Gl. (2.2) [S] |
| Astrophysikalische Flavours | stark empfindlich: Bei Dominanz bleibt die Quellmischung erhalten, nu_tau fehlt bis auf die acht Raumdiagonal-Richtungen | blind: Die gemittelte Wahrscheinlichkeit haengt nur an abs(U)^2 | dasselbe | [M]; IceCube 2024 [S Abstract] |
| Atmosphaerische TeV-Disappearance | unempfindlich (LIV unterdrueckt nur die kleine Standard-Oszillation) | empfindlich: Zusatzphase Delta E^3 L | dasselbe | [M]; IceCube 2018 [S Abstract, S-lokal] |
| T/B (~1e-36) gegen IceCube 2022 (3e-42) | E_min 10 TeV, Einzelparameter, 12 Pixel, linearer Prior bis 1e-34 | E_min ~60 TeV, nur isotrop | Mindestenergie, Himmelsaufloesung, Prior | T/B Abschn. 6.3, Tab. 1 [S]; Rest ~30 offen (R-2) |
| Gedaechtniswert passt | B (mu-tau, atmosphaerisch) | - | Regime | [S-lokal] |

- **Feldregel 6:** "Kegel verletzt Lorentz-Invarianz flavourabhaengig" geht ueber drei Wege: d = 6-Kruemmung (a2),
  d = 4-Anisotropie bei t ungleich 4 lambda (G1) und Massen-Fehlausrichtung (Regime). Gemeinsam ist die Ausrichtung des
  kubischen Netzes gegen die Basis des schwachen Stroms. Die Masche l ist nur eine der Groessen [ES].

## 7. Himmelsrichtung

- **Im Netzrahmen [M]:**
  - Keine Spaltung laengs der vier Raumdiagonalen (acht Himmelspunkte).
  - Je zwei Kegel entartet auf den sechs {110}-Spiegelebenen (n_r^2 = n_s^2).
  - Hoechste Spaltung 1/4 laengs der sechs Wuerfelachsen-Punkte: Der Achsen-Kegel ist dort am schnellsten (a2 = -1/12),
    die beiden anderen -1/3.
- **Im Sonnen-Himmelsrahmen:**
  - Die Koeffizienten (c_eff)_rr,2m und ,4m (4.4) haengen an den drei Euler-Winkeln der Netzausrichtung.
  - Dazu kommt die Zuordnung Kegel zu Flavour (A) bzw. Massenzustand (B), 3! = 6 Moeglichkeiten.
  - Drehfest sind N2 = 0,2265 l^2 und N4 = 0,0675 l^2 je Diagonalelement. Das Verhaeltnis N4/N2 = 0,298 ist fest.
- **Ausrichtungsabhaengigkeit der Schranke:**
  - T/B (A): 20 l_P bei Achse parallel Himmels-Z, sonst bis ~38 l_P.
  - Atmosphaerisch (B) [ES]: Am Suedpol kommen die laengsten Basislinien aus der Naehe der Himmelsachse. Liegt eine
    Raumdiagonale [111] parallel zur Erdachse, verschwindet die Spaltung genau dort. Die Grenze wird dann schwaecher;
    um wie viel, ist nicht gerechnet.
- **Wie es sich vom allgemeinen SME-Modell unterscheidet (Unterscheidungspunkt):**
  - Das Kegelmuster hat vier stetige Parameter (l^2 und drei Euler-Winkel) und zwei diskrete Wahlen (Zuordnung, Regime).
  - Die drei j = 2-Tensoren sind P2 um drei orthogonale Achsen, ihre Summe ist null.
  - Pruefbar erst nach einem Nachweis in mehreren Richtungen. T/B finden keine Anisotropie [S Abstract].

## 8. Unterscheidungspunkte (Feldregel 2)

| Paar | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|
| Regime A gegen B | Flavour-Zusammensetzung oberhalb ~60 TeV: A behaelt die Quellmischung (f_tau ~ 0 ausser nahe [111]); B bleibt Standard. Atmosphaerische TeV-Disappearance: nur B | ja: Die nu_tau-Beobachtung (5 sigma) spricht oberhalb ~0,1 l_P gegen A [ES]. B ist bei ~30 bis 50 l_P mit der IceCube-Statistik erreichbar, eine Richtungsanalyse fehlt |
| Kegelmuster gegen allgemeines anisotropes SME | kein j = 0, j = 1, j = 3 in den Differenzen; N4/N2 = 0,298; Knoten an den Raumdiagonalen | erst nach einem Nachweis |
| Doppler-Physik gegen Doppler-Artefakt (DREI-KEGEL-L) | feste Masche l gegen a -> 0 | nur ueber diese Schranken; bei a -> 0 gibt es keine Grenze |
| t = 4 lambda abgestimmt gegen nicht abgestimmt | d = 4-Flavouranisotropie abs(1 - 4 lambda/t) | ja, schon heute: < ~2e-28 (G1) |

## 9. Gegensweep, Kalibrierung, offene Fragen, Quellen, Selbstanzeigen

### 9.1 Gegensweep: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlich | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | Die Kegel sind in erster Ordnung isotrop (t = 4 lambda) | **ja** [S Tab. A3 + M] | Ausserhalb von t = 4 lambda gilt v(n) ~ v0 (1 + eps n_r^2); die j = 2-Norm ist 1,06 abs(eps). T/B d = 4: tautau_20 < 8e-29, also abs(eps) < ~2e-28. Das ist eine Abstimmung (V5) |
| G2 | Der gemeinsame Teil der Dispersion ist egal | **ja** [S-lokal + M] | Die flavourblinden Grenzen sind einseitig superluminal, das Modell ist subluminal. Die zweiseitigen c_of,jm (~1e-27 bis 1e-28 GeV^-2) brauchen nur l^2 < ~1e-26: nicht bindend |
| G3 | Oszillation sieht die Phase | **ja** [S + M] | T/B Gl. (2.2): Der Hamiltonian enthaelt c direkt. Faktor 1 |
| G4 | Kegelbasis = Basis des schwachen Stroms (A) | nein | Modellfrage, offen R-3 |
| G5 | c-ring = c_00/sqrt(4 pi) | nein (grep ohne Treffer) | [L]; aendert die Uebertragung in A um sqrt(4 pi) = 3,5, also l um 1,9 |
| G6 | Einzelparameter-Grenzen sind gemeinsam verwendbar (Kasten) | nein | Im Modell sind alle drei Diagonalen zugleich ungleich null. Das gibt eher mehr Wirkung (gar keine Umwandlung) [ES] |
| G7 | Erdmaterie, Rotverschiebung, Quellspektrum egal | nein | T/B verschmieren ueber die Rotverschiebung, IceCube 2022 nicht [S Abschn. 6.3] |

### 9.2 Kalibrierung
- **(a) Gemessen:**
  - IceCube 2018 mu-tau isotrop: 9,1e-37
  - IceCube 2022 tau-tau isotrop: 3e-42
  - T/B richtungsabhaengig: 6e-37 bis 1e-36 (d = 6) bzw. 8e-29 (d = 4)
  - astrophysikalische nu_tau mit 5 sigma; KM3NeT/ORCA isotrop
  - keine Anisotropie gefunden
- **(b) Nuetzlich verdichtet [M]:** a2_r(n) = -3/8 + S4/24 + n_r^4/4; kein isotroper Flavour-Anteil; N2, N4;
  SME-Koeffizienten; Grenzen 20 bis 40 l_P (A, T/B) und 30 bis 50 l_P (B); d = 4-Abstimmung 2e-28.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - die 0,08 l_P in Regime A (Uebertragung einer isotropen Grenze)
  - "Regime B ist das natuerliche", weil translationsinvariante Massen je Kegel diagonal sind (stuetzt sich auf
    DREI-KEGEL-L [M])
- **Warnzeichen:**
  - Meine Sicherheit, dass DN-1 trifft, stieg, als T/B ~1e-36 zeigte.
  - Zugleich zerfiel die Frage in Regime, Zuordnung, Ausrichtung, Prior und Mindestenergie.
  - Die Naehe zu 1e-36 ist teils Zufall: Der Gedaechtniswert kommt aus einer anderen Analyse (atmosphaerisch, isotrop).
    Die T/B-Werte koennen vom Prior-Fenster mitbestimmt sein (R-2).

### 9.3 Offene Fragen
1. R-2: Wie stark haengen die T/B-Grenzen bei d = 6 vom linearen Prior bis +-1e-34 GeV^-2 ab? Was erklaert den Restfaktor
   ~30 neben der Mindestenergie?
2. R-3: Welcher Sektor traegt im Kegelmodell den translationsbrechenden Massenterm? Davon haengt ab, ob A (~0,08 l_P)
   oder B (~30 bis 50 l_P) gilt.
3. Eine echte Anpassung des Kegelmusters (vier stetige Parameter, zwei diskrete Wahlen) an die HESE-Flavourkarte bzw. an IceCube-Atmosphaerendaten
   mit Richtung fehlt. Das waere die eigentliche Pruefung.
4. Gilt G1 mit einer Symmetrie, die t = 4 lambda erzwingt? Bekannt ist mir keine [ES].
5. Seitenfrage: Laufzeit-Schranken (Gruppenfaktor 3) fuer den gemeinsamen Teil, etwa aus TXS 0506+056. Nicht geprueft,
   wegen der Subluminalitaet vermutlich schwach.

### 9.4 Quellen (Abrufzeiten per date, Kopien in quellen/)

| Abruf | Quelle | URL | gelesen |
|---|---|---|---|
| R1 01:17:17 | arXiv-API id_list (4 Abstracts): Abbasi, R. u. a. (IceCube) (2022): Search for quantum gravity using astrophysical neutrino flavour with IceCube, Nature Physics 18, 1287; Aartsen, M. G. u. a. (IceCube) (2018): Neutrino interferometry for high-precision tests of Lorentz symmetry with IceCube, Nature Physics 14, 961; Abbasi, R. u. a. (IceCube) (2024): Observation of seven astrophysical tau neutrino candidates with IceCube, PRL 132, 151001; Telalovic, B.; Bustamante, M. (2025) (Abstract) | https://arxiv.org/abs/2111.04654 ; https://arxiv.org/abs/1709.03434 ; https://arxiv.org/abs/2403.02516 | [S Abstract] |
| R2 01:18:31 | Telalovic, B.; Bustamante, M. (2025/2026): No flavor anisotropy in the high-energy neutrino sky upholds Lorentz invariance, JHEP 02 (2026) 024 | https://arxiv.org/abs/2503.15468 | [S] Gl. (2.2) bis (2.4), Abschn. 5.1 bis 5.2, 6.2, 6.3 (Z. 2783-2900), Tab. 1, Tab. A3 (S. 49), Tab. A5 (S. 54-57) |
| R3 01:22:25 | arXiv-API nach Datum (40 Eintraege): darin KM3NeT Collaboration (2026): Atmospheric neutrino constraints on Lorentz invariance violation with the first six detection units of KM3NeT/ORCA; Ultra-high-energy tau neutrinos as probes of Lorentz invariance (2026) | https://arxiv.org/abs/2603.04264 ; https://arxiv.org/abs/2604.19880 | [S Abstract]; Autorennamen nicht gelesen |
| lokal | Kostelecky, V. A.; Russell, N. (2026): Data Tables for Lorentz and CPT Violation, v19, Table D39 (Seiten 114-125, -layout-Auszug in quellen/L1-...) | https://arxiv.org/abs/0801.0287 | [S-lokal] Teil 1 bis 4, 11, 12; Literatur [257], [284], [291], [294], [295] |
| Projekt | drei-kegel-l/DOSSIER.md; diamant-nullstellen-1/ERGEBNIS.md, PLAN.md Z. 76; licht-finn-netz-1/NACHTRAG-PHASE-GRUPPE.md, PLAN.md Z. 32; kubisch-anker-l/DOSSIER.md; grep RUNDE-34/grb-221009a/DOSSIER.md, RUNDE-09/spin1/SPIN1.md | lokal | [P] |

### 9.5 Selbstanzeigen
1. **curl statt WebFetch**, damit Kopien mit Abrufzeit in quellen/ liegen (wie DREI-KEGEL-L und KUBISCH-ANKER-L). 3 von 4
   Abrufen. PDFs und Seitenauszuege lokal mit pdftotext (auch -layout) gewandelt.
2. **Lokale Lesungen ohne Abrufzaehlung:** Data Tables (Kopie von KUBISCH-ANKER-L) mit -layout-Auszug nach quellen/;
   T/B-Seiten 49 und 54 bis 57 aus meiner eigenen Kopie.
3. **grep-Ausschluesse:** Der Projekt-grep (RUNDE-34, RUNDE-09) und die greps in kubisch-anker-l/quellen trugen alle
   vorgeschriebenen Ausschluesse. Die greps in meinem eigenen quellen/ trugen sie nicht; keiner war rekursiv.
   Kein versiegelter Pfad, keine KS-1-Datei geoeffnet.
4. **Alles [M] ist von Hand und ungeprueft:** Richtungsformel, Zerlegung, Normen, Kugelmittel, Kastenrechnung,
   Regime-Abbildung, d = 4-Probe. Die Richtungsformel ist an fuenf gerechneten Werten [E] geprueft, sonst nichts.
5. **Uebertragungen [ES]:** Die 0,08 l_P (A) und die 30 bis 50 l_P (B) beruhen auf isotropen Grenzen, die ich auf ein
   anisotropes Muster uebertrage. Veroeffentlicht ist nur die T/B-Rechnung, und die gilt je Einzelkoeffizient.
6. **Autoren-, Titel- und Zeitschriftenangaben** der R3-Treffer habe ich nur teilweise gelesen. l_P und hbar c sind
   Standardwerte [L].
7. **Werkzeuge lokal:** date, ls, mkdir, cat, sed, grep, head, tr, cut, paste, wc, file, curl, pdftotext. Kein python, awk,
   perl oder jq. Kein Journal, kein Peerbus, kein Commit. Geschrieben nur in drei-kegel-neutrino-l/.
8. **Zeitbox:** Start 01:08:24; Endzeit steht in ARBEITSFELD.md (per date).

## 10. Einfach gesagt

Wenn die drei Kegel auf Finns Netz die drei Neutrino-Sorten waeren, dann waere jede Sorte bei sehr hoher Energie in eine
andere Raumrichtung ein klein wenig schneller, wie drei Kompassnadeln. Weil das im Himmelsmittel fuer alle drei Sorten
gleich ist, helfen die bekannten "Mittelwert"-Grenzen von IceCube nicht direkt. Es gibt aber eine Auswertung von 2025, die
genau nach solchen Richtungsunterschieden gesucht und keine gefunden hat; daraus folgt, dass die Masche kleiner als etwa
20 bis 40 Planck-Laengen sein muss. Ob es noch viel strenger wird (unter eine Planck-Laenge), haengt davon ab, wo im Modell
die Mischung der Neutrinos herkommt. Ausserdem muss das Netz an einer Stelle extrem genau abgestimmt sein, sonst waeren die
Sorten schon bei niedriger Energie verschieden schnell, und das ist ausgeschlossen.
