# DOSSIER GRB-221009A: Galanti/Roncadelli, PRL 137, 111002 (2026), und das 300-TeV-Ereignis von Carpet-3

- Feldforscher fuer claude-primary, Runde 34. Karte: KARTE.md (C1-C4 unveraendert). Arbeitsdatei: ARBEITSFELD.md (Abrufprotokoll mit
  Erwartung vor jedem Abruf, Gegensweep, eigene Fehler).
- Start 2026-10-03 17:52:50 CEST; Dossier begonnen nach date 18:11:55 CEST. Quellen als PDF/Text in quellen/ (sha256 im ARBEITSFELD).
- Marken: [S] an der Quelle gelesen (Fundstelle), [A] nur Abstract/Metadaten, [L?] nicht gelesen (nur Zitat), [E] eigene Rechnung,
  [H] eigene Hypothese/Schluss. Die Schranken-Zahlen anderer Arbeiten, die ich nur als Zitat in einer gelesenen Arbeit gesehen habe,
  tragen [S] fuer das Zitat und [L?] fuer die Primaerarbeit.

---

## 1. Kurzfazit (Erwartungsverstoesse zuerst)

1. **LHAASO hat zur Zeit des Carpet-Ereignisses hingeschaut und nichts gesehen.** Die Quelle war bis T0 + 6000 s im LHAASO-Sichtfeld
   (Zenit < 50 Grad); KM2A hat ueber den ganzen Zeitraum T0 bis T0 + 6000 s nach Ereignissen ueber 100 TeV gesucht: "no event was
   detected" (LHAASO, Sci. Adv. 9, eadj2778, S. 4) [S]. Carpet-3, Galanti/Roncadelli (G/R) und Satunin/Troitsky beschreiben LHAASO nur
   als "close to the limit of the field of view" bzw. "did not report ... beyond 2000 s" und gehen auf diese Nullsuche nicht ein [S].
   [E] KM2A ist etwa 5e3- bis 1e4-mal groesser als Carpet-3 (~61 m^2); ein echter Fluss, der Carpet ein Ereignis gibt, haette KM2A
   Tausende gegeben. Nach meiner Abschaetzung ist "Untergrund" damit rund 100-mal wahrscheinlicher als "Photon vom GRB".
2. **Das LIV-Fenster ist nur gegen die Laufzeit offen.** Richtung gleich (subluminal, wie LHAASO) und Breite wie erwartet (n = 1:
   1,0e20 bis 1,22e21 GeV; n = 2: 6,9e11 bis 2,03e13 GeV). Aber im Rechenrahmen von G/R selbst (modifizierte Dispersion mit Energie-
   Impuls-Erhaltung) schliessen andere Schranken es: n = 1 durch Doppelbrechung (> 1,8e34 bzw. 3,6e34 GeV), n = 2 durch Luftschauer
   (> 1,7e13 GeV, Satunin 2021; > 2,4e14 GeV, Martynenko u. a. 2025; vorlaeufig > 1,5e21 GeV, Martynenko u. a. 2026). Dazu [E] mit
   den Schwellenformeln von Jacobson/Liberati/Mattingly 2003 [S]: subluminale Photonen lassen normale Elektronen ab ~110 TeV (n = 1)
   bzw. ~160 TeV (n = 2) Vakuum-Cherenkov-Strahlung abgeben; die 100-TeV-Elektronen in Supernova-Ueberresten lassen nur noch
   Restspalten, PeV-Elektronen im Krebsnebel (falls leptonisch) schliessen beide Fenster. Offen bleibt es nur in String-Schaum-
   Modellen, fuer die G/R die noetige Schwellenverschiebung nicht hergeleitet haben [H].
3. **Das Photon ist schwach belegt.** Ein Ereignis; Zufallskoinzidenz 9e-3 je Tag (einseitig ~2,4 sigma [E]); Richtungsfehler 4,7 Grad
   (90 %); die Hadron-Wahrscheinlichkeit 3e-4 stammt allein aus einem MC-trainierten neuronalen Netz, die Myonzahl allein gibt 12,7 %
   (Carpet-3, S. 3-5) [S].
4. **Gegenpositionen sind duenn, aber es gibt sie, und sie kommen teils von Carpet-Mitgliedern selbst.** Ofengeim/Piran 2025: fuer n = 1
   ist eine Zufallszuordnung wahrscheinlicher als LIV; Satunin/Troitsky 2026: die LIV-Werte sind durch andere Beobachtungen
   ausgeschlossen, ALP passt besser (aber mit Kopplung in Spannung zu Weissen Zwergen). Eine Arbeit, die das Ereignis als Hadron
   oder galaktischen Zufall erklaert, habe ich nicht gefunden.
5. **Fuer unser Programm:** eine Beobachtungsspannung, kein Beleg (C4 bestaetigt); schwaecher als die bisherigen Eintraege in
   BEOBACHTUNGSSPANNUNGEN.md. Ein bestaetigtes Signal saesse an A1 (lokale Lorentz-Invarianz) im Photonsektor bei hohen Energien, nicht
   im Gravitationssektor, und wuerde die IR-Herleitung der Spin-2-Kette nicht direkt treffen [H].

---

## 2. Erwartungen C1 bis C4

| Nr | Erwartung (Karte, vor Abruf) | Fund | Wertung | Quelle |
|---|---|---|---|---|
| C1 (65 %) | Einzelereignis unter 5 sigma; LHAASO hat zur selben Zeit nichts ueber ~20 TeV gemeldet -> Spannung | Einzelereignis, Zufall 9e-3/Tag, Richtungsfehler 4,7 Grad, Hadron-Wahrscheinlichkeit 3e-4 nur per NN (Myonzahl allein 0,127). LHAASO: Quelle bis T0 + 6000 s im Sichtfeld, KM2A-Suche > 100 TeV von T0 bis T0 + 6000 s ohne Ereignis | **bestaetigt, aber in der Staerke verletzt**: keine "Meldeluecke", sondern eine ausdrueckliche Nullsuche im selben Zeitfenster mit ~1e4-facher Flaeche; die Spannung ist groesser als erwartet und wird in der Carpet-Literatur nicht behandelt | Carpet-3 PRD 111, 102005, Tab. I, S. 3-6 [S]; LHAASO Sci. Adv. 9, eadj2778, S. 2-4 [S]; LHAASO Science 380, S. 3 [S] |
| C2 (60 %) | G/R-Fenster mit LHAASO-Laufzeit vereinbar (gleiche, subluminale Richtung), gut eine Groessenordnung breit | Richtung gleich (G/R xi = +1 subluminal; LHAASO subluminal; Satunin s = -1 subluminal, nur Konvention verschieden). n = 1: 1,0e20 (LHAASO-Text) bzw. 1,22e20 (G/R) bis 1,22e21 GeV -> Faktor 10-12; n = 2: 6,9e11 bis 2,03e13 GeV -> Faktor ~29. Gegen Doppelbrechung (n = 1, EFT) und Luftschauer-Schranken (n = 2) geschlossen, dazu [E] Elektron-Vakuum-Cherenkov mit JLM-Schwellen (Restspalten bzw. geschlossen); G/R verwerfen bzw. umgehen die ersten beiden mit eigenen Argumenten, den dritten erwaehnen sie nicht | **Wortlaut bestaetigt, Kern verletzt**: vereinbar nur mit der Laufzeit; im Gesamtbild nur in einem Modellregime (String-Schaum) offen, das G/R fuer die Schwelle nicht durchrechnen | G/R S. 4, Suppl. S. 21-23 [S]; LHAASO PRL 133, 071501, S. 6, Tab. I [S]; Satunin/Troitsky S. 5 [S]; Martynenko 2025 S. 6 [S]; Martynenko 2026 Gl. 38 [S] |
| C3 (70 %) | mindestens eine Arbeit (seit 10/2024), die das Ereignis ohne neue Physik erklaert (Hadron, galaktischer Zufall) oder die Signifikanz bezweifelt | Keine Arbeit fuer Hadron-Fehlkennung oder galaktischen Zufall gefunden. Ofengeim/Piran 2025: bei n = 1 ist "spurious association ... favored", allgemein "hesitate ... on the basis of a single event". Standardphysik-Mechanismen: Neutronenstrahl (Carpet-3 selbst; von O/P und G/R wegen Neutrinos verworfen), Protonstrahl (Kalashev u. a. 2025, nur fuer LHAASO-Photonen) | **teilweise, schwaecher als erwartet**: Zweifel nur indirekt; die staerkste Gegenevidenz (KM2A-Nullsuche, 2023) wird von niemandem gegen Carpet gewendet | O/P PRD 112, 083055, S. 5-6, 8 [S]; Carpet-3 S. 6-7 [S]; G/R Suppl. S. 25-26 [S]; OpenAlex-Zitatliste (14 Zitate) [A] |
| C4 (80 %) | Beobachtungsspannung, kein Beleg; Eintrag in BEOBACHTUNGSSPANNUNGEN.md, keine Folgen fuer laufende Straenge | Einzelereignis, 2,4 sigma Zufall, KM2A-Nullsuche dagegen, LIV-Deutung im EFT-Regime ausgeschlossen | **bestaetigt**; Eintrag nur mit Gegenrede in derselben Zeile (Regel jener Datei) | siehe Abschn. 4-7 |

---

## 3. Erwartungsverstoesse (das eigentliche Ergebnis, wichtigste zuerst)

1. **KM2A-Nullsuche > 100 TeV im Carpet-Zeitfenster** (Agenten-Erwartung A5 verletzt; Karte C1 in der Staerke verletzt). LHAASO
   Sci. Adv., S. 4, woertlich: "Gamma-ray events with energy above 100 TeV were searched for during a long period from T0 to T0 +6000s;
   however, no event was detected." Sichtfeld "zenith angles less than 50°", Quelle "left the FOV at T0 +6000s" (S. 2-3) [S].
   [E] Eigene Ortsrechnung (LHAASO 29,36 N / 100,14 O; Modell reproduziert LHAASO 28,1 / 35,1 / 50 Grad bei T0 / T0 + 2000 s /
   T0 + 6000 s): bei T0 + 4536 s Zenit ~44,8 Grad, also im Sichtfeld. Die gegenteiligen Saetze stehen bei Carpet-3 (S. 6),
   G/R (S. 1) und Satunin/Troitsky (S. 3) [S]; grep nach "6000" und "searched for" in diesen drei Texten: kein Treffer.
2. **Das n = 2-Fenster ist durch eine Schranke aus dem 24-Monats-Fenster geschlossen, die G/R nicht zitieren.** Martynenko, Rubtsov,
   Satunin, Sharofeev, Troitsky, PRD 111, 063010 (2025): Auger-Myonzahl schliesst M_LIV <= 2,4e14 GeV aus (95 %, Photon-LIV
   subluminal, n = 2, Elektronen und Hadronen ohne LIV) (S. 6, Abb. 3) [S]. G/R: Oberschranke 2,03e13 GeV (Gl. 8) [S]; grep
   "Martynenko|063010" in G/R v3: kein Treffer. Dazu 08/2026, vorlaeufig: M_LIV > 1,5e21 GeV aus Auger-X_max ("toy analysis",
   "should not be interpreted as a detector-level experimental limit") (arXiv:2608.05106, Abstract, Gl. 38) [S].
3. **G/R stuetzen ihren Ausweg auf denselben Effekt, auf dem die schliessenden Schranken beruhen.** Um die GZK-Photon-Schranken (n = 1 > 5e33 GeV, n = 2 > 2,5e22 GeV) zu umgehen,
   berufen sich G/R auf die LIV-Unterdrueckung der Bethe-Heitler-Paarbildung in der Luft (Suppl. S. 22-23) [S]. Genau diese
   Unterdrueckung ist die Grundlage der Schauer-Schranken (Satunin 2021; Martynenko 2025/2026), die das n = 2-Fenster schliessen, und
   G/R geben fuer 300 TeV selbst eine Weglaenge O(1-10) km an (Suppl. S. 23), gegen ~0,4 km normal [E: 47 g/cm^2 / 1,2e-3 g/cm^3]. Der
   Carpet-Schauer haette dann tiefer und anders begonnen; Energie (300 TeV) und Photon/Hadron-Trennung sind aber mit Standard-MC
   bestimmt (Carpet-3 S. 4). Satunin/Troitsky (Carpet-Mitglied Troitsky) sagen das ausdruecklich: "the very air shower detected by
   Carpet would start deeper in the atmosphere and develop in a non-standard way" (S. 6) [S].
4. **ALP allein ist nicht "stark benachteiligt", sondern je nach Parameterbereich bevorzugt.** G/R: N(ALP) <~ 1e-4, zwei Groessenord-
   nungen zu wenig, bei g = 3-5e-12 GeV^-1, m = 1e-11 bis 1e-7 eV (S. 2) [S]. Satunin/Troitsky: bester Gesamtfit ALP mit m = 5,16e-7 eV,
   g = 6e-11 GeV^-1, Dchi^2 = 30,48 gegen Standard, LIV nur 12,99 (S. 3-5) [S]; diese Kopplung liegt nahe CAST und in Spannung zu
   Weisser-Zwerg-Polarisation. -> Zwei Regime, Moderator = zugelassener ALP-Bereich (Abschn. 6).
5. **Die Hadron-Wahrscheinlichkeit 3e-4 ist klassifikatorabhaengig.** Myonzahl allein: 0,127 der Hadronschauer haben n_mu <= 3;
   "it is not that rare" (Carpet-3 S. 4) [S]; 3e-4 aus einem neuronalen Netz, trainiert auf CORSIKA/QGSJET-II-04 (S. 4-5) [S].
   Agenten-Erwartung A4 (Richtungsfehler 1,5-2 Grad) ebenfalls verletzt: 4,7 Grad (90 %) (S. 3) [S].
6. **Die Fensterbreite haengt an der Statistikvorschrift und an der Version.** G/R v1 (04/2025): "first evidence for LIV", Punktwert
   "N ~ 1 for E_LIV ~ 3.0 x 10^20 GeV" (v1 S. 3) [S]; v3/PRL: Oberschranke bei N >= 0,0513 (Poisson 95 %), 1,22e21 GeV, und nur noch
   "compatible with specific LIV frameworks", "potential first indication" (v3 S. 1, 5) [S]. O/P und Satunin/Troitsky zitieren noch
   3e20 GeV [S].
7. **Die LHAASO-Laufzeitschranke ist im Text schwaecher als im Abstract.** Abstract "E_QG,1 > 10 times of the Planck energy";
   Text subluminal 1,0e20 GeV (ML/MINOS) = 8,2 E_Pl [E], kalibriert 1,1e20 GeV (S. 6, Tab. I) [S]. G/R setzen 1,22e20 und 7,32e11 GeV
   (Suppl. S. 21) [S], also die gerundeten Abstractwerte.

---

## 4. Die Arbeit selbst: Kernzahlen mit Fundstellen

Galanti, Roncadelli, arXiv:2504.01830v3 (30.06.2026), PRL 137, 111002 (2026), 26 S. inkl. Supplement. Gelesen im Volltext [S].
Seitenangaben nach der arXiv-PDF-Zaehlung.

| Groesse | Wert | Fundstelle |
|---|---|---|
| Photon | Carpet-3, E = 300 (+43/-38) TeV, T0 + 4536 s, ein Ereignis aus der Auswertung **eines Tages** | S. 1 (nach Carpet-3 [11]) |
| Zufall / Hadron | Zufallskoinzidenz "about 9 x 10^-3", Hadron "about 3 x 10^-4" | S. 1 |
| LHAASO-Sicht | "close to the limit of the field of view of the LHAASO experiment"; HAWC unter dem Horizont; "we take this result at face value" | S. 1 |
| Rechenweg | dN/(dE dA dt) = P(E; gamma->gamma) F_em(E), Integral 262-343 TeV, Flaeche ~60 m^2, Belichtung ein Tag; F_em = Carpet-Extrapolation des LHAASO-Spektrums, Faktor 3 nach oben und unten | Gl. (1), S. 2; Appendix S. 5-6 |
| Absorption | CMB dominiert bei 300 TeV, EBL nachrangig; Standard: N(CP) ~ 1e-96 | S. 2, S. 6 |
| ALP | m_a ~ 1e-11 bis 1e-7 eV, g = 3-5e-12 GeV^-1 (aus LHAASO-Erklaerung [47]); N(ALP) <~ O(1e-4), Supplement ~1e-5; Poisson-95-%-Forderung N >= 0,0513 -> "fail ... by about two orders of magnitude"; Grund u. a. schwache Mischung oberhalb E_H (QED, CMB-Dispersion) | S. 2; Suppl. S. 14 (Gl. 33), S. 21 |
| LIV-Form | p^2 = E^2 (1 + xi_n E^n / E_LIV,n^n), xi_n = +1 **subluminal**; nur subluminal; n = 1, 2; nur Photonen (und ALPs), begruendet mit Liouville-String und D-Branen; Energie-Impuls-Erhaltung angenommen | Gl. (5), S. 3; Suppl. Gl. (44)-(46), S. 23 |
| Schranken | E_LIV,1 < 1,22 (+0,19/-0,22)e21 GeV (95 %); E_LIV,2 < 2,03 (+0,17/-0,22)e13 GeV (95 %); Fehler = Systematik der Carpet-Normierung | Gl. (7), (8), S. 4 |
| Herkunft der Schranken | aus N_gamma(E_LIV,n) >= 0,0513 (Gehrels 1986), also "<": nur genuegend starke LIV laesst das Photon durch | S. 4 |
| Doppelbrechung | n = 1 fuehrt "in conventional physics" zu Doppelbrechung, Schranken E_LIV,1 > 3,6e34 GeV, E_LIV,2 > 1,3e11 GeV; Ausweg: D-Brane-Modelle ohne Doppelbrechung | S. 4 |
| Benchmarks | m_a = 1e-10 eV, g = 4e-12 GeV^-1, E_LIV,1 = 3e20 GeV, E_LIV,2 = 5e12 GeV | S. 4 |
| Fremdschranken (eigene Liste) | Laufzeit 1,22e20 / 7,32e11 GeV; Breit-Wheeler (Lang u. a. 2019) 1,21e20 / 2,38e12 GeV; GZK-Photonen 5,08e33 / 2,49e22 GeV (Galaverni/Sigl), O(1e29) / O(1e19) GeV (Lang u. a.) -> "do not apply" wegen Bethe-Heitler-Unterdrueckung; Krebsnebel n = 2 > 1,4e12 GeV; Tibet diffus n = 2 > 1,7e13 GeV -> "effectively disappears" | Suppl. S. 21-23 |
| Bethe-Heitler bei 300 TeV | Weglaenge O(1-10) km im ALP+LIV-Fall | Suppl. S. 23 |
| Verspaetung | Ofengeim/Piran: n = 2 mit E_LIV,2 = 1,59 (+0,56/-0,35)e12 GeV erklaert > 1 h Verspaetung; "consistent with our upper bound" | S. 4 |
| Schluss | "potential first indication of LIV in the considered contexts"; "Only time will tell" | S. 5 |
| v1 zum Vergleich | "first evidence for LIV"; N ~ 1 bei E_LIV ~ 3,0e20 GeV | v1 Abstract, S. 3 |

**ALP-Aussage in einem Satz:** ALPs allein (im von G/R zugelassenen Parameterbereich, der fuer die LHAASO-Photonen gewaehlt ist) liefern
fuer Carpet nur ~1e-4 bis 1e-5 erwartete Ereignisse statt >= 0,05; erst ALP plus LIV erklaert LHAASO und Carpet zugleich (S. 2-4,
Suppl. S. 21-23) [S].

---

## 5. Schranken-Tabelle

Alle Skalen in derselben Normierung: Gruppengeschwindigkeit v = 1 - (n+1)/2 (E/E_*)^n (an den Gleichungen von G/R, LHAASO, Satunin/
Troitsky, Martynenko geprueft, ARBEITSFELD Abschn. 4 Punkt 2) [E]. E_Pl = 1,22e19 GeV.

| Quelle | Richtung | Ordnung | Wert | Art | Status |
|---|---|---|---|---|---|
| G/R 2026 (Carpet-Photon als echt angenommen) | subluminal | n = 1 | **< 1,22e21 GeV** (95 %) | Schwellenverschiebung, bedingt | [S] Gl. 7 |
| G/R 2026 | subluminal | n = 2 | **< 2,03e13 GeV** (95 %) | dito | [S] Gl. 8 |
| G/R v1 2025 | subluminal | n = 1 | ~3,0e20 GeV (N = 1) | dito | [S] v1 S. 3 |
| LHAASO PRL 133, 071501 (2024) | subluminal | n = 1 | > 1,0e20 GeV (ML/MINOS); Abstract "> 10 E_Pl" | Laufzeit, WCDA 0,2-7 TeV | [S] S. 6, Tab. I |
| dito | subluminal | n = 2 | > 6,9e11 GeV; Abstract "> 6e-8 E_Pl" | Laufzeit | [S] |
| dito | superluminal | n = 1 / 2 | > 1,1e20 / > 7,0e11 GeV | Laufzeit | [S] |
| Ofengeim/Piran 2025 | subluminal | n = 2 | = 1,30 (+0,56/-0,35)e-7 E_Pl [E: 1,59e12 GeV] (95,4 %), zweiseitig, wenn Photon aus dem Nachleuchten | Schwelle + Verspaetung | [S] Abstract, S. 8 |
| dito | subluminal | n = 1 | aus dem Nachleuchten: mit LHAASO-Laufzeit nur bei 0,1 % vereinbar; sonst 9 bis 25 E_Pl [E: 1,1e20 bis 3,05e20 GeV] | dito | [S] S. 5-6 |
| Satunin/Troitsky 2026 (Fluenz-Fit) | subluminal | n = 2 | flaches Minimum ~4e12 GeV, Dchi^2 = 12,99 | Fit | [S] S. 3 |
| Lang, Martinez-Huerta, de Souza 2019 (111 Spektren, 38 Quellen) | subluminal | n = 1 / 2 | > 1,21e20 / > 2,38e12 GeV (EBL Franceschini); je nach EBL 6,85e19-1,50e20 / 1,56-2,17e12 | Breit-Wheeler | Zitat [S] G/R Suppl. S. 21-22; Primaer [L?] |
| Satunin 2019, Krebsnebel (Tibet) | subluminal | n = 2 | > 1,4e12 GeV | Luftschauer | Zitat [S] G/R, Martynenko 2026; Primaer [L?] |
| **Satunin 2021, Tibet diffus** | subluminal | n = 2 | **> 1,7e13 GeV** (G/R: wahres CL "much less than 95 %") | Luftschauer | Zitat [S] G/R, S/T, Martynenko; Primaer [L?] |
| **Martynenko u. a. 2025, PRD 111, 063010** | subluminal (nur Photonen) | n = 2 | **> 2,4e14 GeV** (95 %) | Auger-Myonzahl | [S] S. 6 |
| Martynenko u. a. 2026, arXiv:2608.05106 (nicht begutachtet) | subluminal (nur Photonen) | n = 2 | > 1,5e21 GeV (95 %, "toy", zusammensetzungsabhaengig) | Auger-X_max | [S] Gl. 38 |
| Doppelbrechung, Goetz u. a. 2013 (GRB 061122, INTEGRAL/IBIS) | beide Helizitaeten (EFT) | n = 1 | > 1,8e34 GeV (S/T); G/R nennen > 3,6e34 GeV | Polarisation | Zitate [S]; Primaer [L?] |
| GZK-Photonen (Galaverni/Sigl 2008; Lang u. a.) | subluminal | n = 1 / 2 | > 5,08e33 / > 2,49e22 GeV; > O(1e29) / > O(1e19) GeV | Nichtnachweis UHE-Photonen | Zitat [S] G/R; von G/R per Bethe-Heitler-Argument bestritten |
| Elektron-Vakuum-Cherenkov, Krebsnebel (Li/Ma 2022, 2023 u. a.) | relativ Elektron gegen Photon | — | Werte nicht gelesen | PeV-Elektronen | [A] Li/Ma JHEP 10 (2025) 216; in String-Schaum "evaded" |
| Elektron-VCR, eigene Anwendung der JLM-Schwellen (Rahmen I, LI-Elektronen) | subluminal (nur Photonen) | n = 1 | > 9,6e20 GeV (100-TeV-Elektronen, SN1006/Krebsnebel); > 9,6e23 GeV (PeV-Elektronen, falls leptonisch) | Schwelle p_th = (4 m_e^2 E_LIV,1)^(1/3) | [E] mit JLM 2003 Gl. (21) [S] |
| dito | subluminal (nur Photonen) | n = 2 | > 7,5e12 GeV (100 TeV); > 7,5e14 GeV (PeV) | p_th = (27/4)^(1/4) sqrt(m_e E_LIV,2) | [E] mit JLM 2003 Gl. (27)-(29) [S] |
| Photonzerfall / -spaltung (z. B. LHAASO 2022) | nur superluminal | — | fuer subluminal nicht anwendbar | — | [S] G/R Suppl. S. 21 ("do not occur") |
| H.E.S.S./Mrk 501 | subluminal | n = 1 / 2 | in dieser Runde nicht gelesen | Breit-Wheeler | [L?] |

**Fensterbilanz [E/H]:**
- n = 1: 1,0e20 (LHAASO-Text) bis 1,22e21 GeV (G/R). Gegen Laufzeit und Breit-Wheeler offen. Im EFT-Rahmen (Myers-Pospelov) durch
  Doppelbrechung um ~13 Groessenordnungen geschlossen; offen nur ohne Doppelbrechung (D-Branen). Fuer ein Photon, das zum LHAASO-
  Nachleuchten gehoert, nach O/P praktisch ausgeschlossen (0,1 %). Im G/R-Rahmen I (LI-Elektronen) dazu Elektron-VCR [E]: mit
  100-TeV-Elektronen Restspalt 9,6e20 bis 1,22e21 GeV; mit PeV-Elektronen geschlossen.
- n = 2: 6,9e11 bis 2,03e13 GeV. Mit Satunin 2021 bleibt 1,7e13 bis 2,03e13 GeV (innerhalb des G/R-Fehlerbands); mit Martynenko 2025
  geschlossen (Faktor 12); mit Martynenko 2026 (vorlaeufig) um ~8 Groessenordnungen geschlossen. Elektron-VCR [E]: mit 100-TeV-
  Elektronen Restspalt 7,5e12 bis 2,03e13 GeV; mit PeV-Elektronen geschlossen.
- Bei G/R-Werten selbst liegt die VCR-Schwelle normaler Elektronen bei ~108 TeV (n = 1, 1,22e21 GeV) bzw. ~164 TeV (n = 2,
  2,03e13 GeV) [E]; darueber verlieren Elektronen ihre Energie auf einer Strecke ~100/E (JLM S. 9) [S].
- Die Annahme "Elektronen und Hadronen ohne LIV" ist bei Martynenko und G/R dieselbe (G/R: nur neutrale Anregungen haben LIV, S. 3).

---

## 6. Regime und Moderatoren (Regel 1)

| Widerspruch | Vermuteter Moderator | Regime A | Regime B |
|---|---|---|---|
| G/R: n = 1-Fenster offen; O/P: n = 1 unvereinbar; S/T: n = 1 um 14 Groessenordnungen ausgeschlossen | (a) ob die Verspaetung mit erklaert werden muss; (b) EFT mit Doppelbrechung oder nicht | O/P: Photon aus dem Nachleuchten -> Verspaetung noetig -> n = 1 scheitert an LHAASO-Laufzeit | G/R: nur Durchsichtigkeit, D-Brane ohne Doppelbrechung -> 1e20 bis 1,2e21 GeV |
| G/R: Schauer-/GZK-Schranken "do not apply"; S/T, Martynenko: n = 2-Bereich ausgeschlossen | **LIV-Klasse**: (I) modifizierte Dispersion mit Energie-Impuls-Erhaltung (Schwellen und Schauer veraendert) vs. (II) String-Schaum (Laufzeit ja, Schauer nach C. Li 2025 nicht) | (I): Durchsichtigkeit ja, aber Schauer- (n = 2), Doppelbrechungs- (n = 1) und [E] Elektron-VCR-Schranken (beide n, JLM-Schwellen) greifen | (II): Schauer- und VCR-Schranken laut Li/Ma "evaded"; ob dort die Schwellenverschiebung fuer Durchsichtigkeit entsteht, zeigen G/R nicht [H] |
| G/R: ALP allein scheitert; S/T: ALP bester Fit | zugelassener ALP-Parameterbereich (Weisser-Zwerg-Schranke g < 5,4e-12 GeV^-1 ja/nein) | G/R: g <= 5e-12 -> ALP zu schwach | S/T: g = 6e-11 (nahe CAST) -> ALP bevorzugt, aber in Spannung mit MWD |
| Carpet/G/R/S/T: LHAASO "am Rand"/"keine Meldung"; LHAASO: Nullsuche bis T0 + 6000 s | **kein Regime**, sondern eine nicht gelesene Primaerangabe [H] | — | — |
| Hadron-Wahrscheinlichkeit 0,127 vs. 3e-4 | Messgroesse: Myonzahl allein vs. MC-trainiertes Netz mit 400 Detektorbildern | 0,127 | 3e-4 (haengt an QGSJET-II-04/FLUKA-Simulation) |
| N = 1 (v1, 3e20 GeV) vs. N >= 0,05 (v3, 1,22e21 GeV) | Statistikvorschrift fuer ein Einzelereignis | Punktwert | 95-%-Grenze |

---

## 7. Unterscheidungspunkte (Regel 2)

| Erklaerungspaar | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|
| Photon von GRB 221009A vs. Untergrund (Hadron oder galaktisches Photon im 4,7-Grad-Kreis, z. B. 3HWC J1928+178 in 2,5 Grad) | KM2A-Zaehlung > 100 TeV zur selben Zeit: Fluss-Hypothese erwartet ~R x mu_Carpet mit R ~ 5e3-1e4 [E], Untergrund erwartet 0 | **ja, gemessen: 0 Ereignisse** (LHAASO Sci. Adv. S. 4). [E] P(Carpet 1, KM2A 0 | Fluss) <= 1/(e(1+R)) ~ 4e-5 bis 7e-5 gegen 9e-3 (Untergrund je Tag) |
| LIV (I) vs. Standard-Photon fuer das Carpet-Ereignis selbst | Schauerbeginn/Alter: bei LIV tieferer Start (Weglaenge O(1-10) km statt ~0,4 km) | im Prinzip ja (Carpet-NKG-Alter, Laufzeiten), nicht veroeffentlicht |
| LIV (I) vs. LIV (II, String-Schaum) | Luftschauer von Photonen > 100 TeV bis PeV aus galaktischen Quellen; PeV-Elektronen im Krebsnebel (VCR) | ja; LHAASO sieht Krebsnebel-Photonen bis 1,1 PeV (Science 373, 425) [A], mit dem Vorbehalt "we do not exclude a non-negligible contribution of PeV protons". Harte VCR-Schwelle fuer LI-Elektronen: n = 1 p_th = (4 m_e^2 E_LIV)^(1/3) ~ 110 TeV bei 1,22e21 GeV; n = 2 p_th = (27/4)^(1/4) sqrt(m_e M) ~ 160 TeV bei 2e13 GeV - beide Formeln stehen bei Jacobson/Liberati/Mattingly 2003, Gl. (21) und (27)-(29) mit eta = 0 [S], Zahlen [E]. Martynenko u. a. nennen (2 m_e M^2)^(1/3) ~ 7e16 eV (nicht die Minimalschwelle; offen, welche Konfiguration gemeint ist). |
| LIV vs. ALP | LIV veraendert nur den CMB-Teil (>~100 TeV); ALP erzeugt Strukturen bei 5-10 TeV (KM2A-Delle) und keine Verspaetung; LIV n = 2 bei ~1,6e12 GeV verspaetet 300 TeV um ~4000 s [E] | teils ja (S/T Abb. 4: ALP passt die 5-TeV-Delle, LIV nicht) |
| n = 1 vs. n = 2 | Energieabhaengigkeit der Verspaetung mehrerer Photonen > 100 TeV | nein (ein Ereignis) |

---

## 8. Gegenpositionen (24-Monats-Fenster ab 10/2024)

1. **Ofengeim/Piran, PRD 112, 083055 (2025)** [S]: zweiseitige LIV-Schranke n = 2 (1,59e12 GeV) unter der Annahme, das Photon gehoere
   zum Nachleuchten; n = 1 dann nur bei 0,1 %; "the possibility of a spurious association is favored" fuer n = 1 (S. 6); Schluss:
   "hesitate accepting LIV ... on the basis of a single event" (S. 8). Neutronenstrahl-Modell: zu viele Neutrinos (Anhang A).
2. **Satunin/Troitsky, JETP Lett. 123, 73 (2026)** [S]: LIV verbessert den Gesamtfit nur maessig und "requires parameters excluded by
   other constraints"; ALP besser, aber in Spannung mit MWD (S. 1, 5-6). Kein Zweifel am Ereignis selbst; Troitsky ist Carpet-Autor.
3. **Martynenko u. a. 2025 und 2026** [S]: keine Aussage zum Carpet-Ereignis, aber Schranken, die die n = 2-LIV-Deutung ausschliessen
   (Abschn. 5). Nebenbei: 2025 schlagen sie M_LIV ~ 1,9e16 GeV als Erklaerung des Myonraetsels vor (S. 6-7) - ebenfalls neue Physik.
4. **Standardphysik-Mechanismen:** Neutronenstrahl-"Echo" (Carpet-3 S. 6-7, nach Dermer/Atoyan; erreicht ~100 TeV nur mit
   zehnfachem Magnetfeld oder 3-4-facher Protonenergie) [S]; von O/P und G/R wegen IceCube-Neutrinogrenzen verworfen [S].
   Protonstrahl-Kaskade (Kalashev, Aharonian, Essey, Inoue, Kusenko, PRD 112, 023022 (2025)) fuer die LHAASO-Photonen, laut G/R am
   Wirtsgalaxie-Magnetfeld scheiternd [L?, nur ueber G/R Suppl. S. 25-26].
5. **Andere neue Physik:** Song/Ma, PLB 870, 139959 (2025): subluminal E_LV ~ 3e17 GeV [A] - [E] Faktor ~300 unter der LHAASO-
   Laufzeitschranke; Qin u. a., ApJ (2026): ALP g = 1,685e-10 GeV^-1 (ueber CAST) plus LIV n = 2 [A]; Rescic u. a., Phys. Dark Univ.
   (2026): "excesses" in LHAASO-Nichtnachweisen ueber ~30 TeV als moegliches n = 2-Signal [A]; Wang u. a., PRD 114, 063023 (2026):
   TeV-Photonen aus PeV-Neutrinos (Vorlaeufer-Photonen, nicht Carpet) [A]; C. Li, PLB 869, 139823 (2025) und Li/Ma, JHEP 10 (2025) 216:
   String-Schaum entgeht Schauer- und VCR-Schranken [A].
6. **Nicht gefunden:** eine Arbeit, die das Ereignis als Hadron-Fehlkennung oder galaktischen Zufall erklaert, oder die die KM2A-
   Nullsuche gegen Carpet wendet. Kanaele: arXiv-API (vier Abfragen), OpenAlex-Zitate von Carpet-3 (14). WebSearch war in dieser
   Sitzung erschoepft (200/200). Urteil daher: **nach Recherchestand nicht belegt**, nicht "gibt es nicht".

---

## 9. Programmbezug [H]

- **Wo saesse ein solches Signal?** An A1 (lokale Lorentz-Invarianz, LORENTZ.md 1/3d), und zwar im **Photonsektor bei hohen Energien**:
  Dimension-5/6-Operatoren mit Vorzugssystem (Martynenko Gl. 4: F_kj d_i^2 F^kj / M^2, "motivated by Horava-type models"). Die
  Spin-2-Kette nutzt Lorentz-Invarianz in Glied 2 (Weinbergs Satz ueber weiche Gravitonen, Lorentz-Invarianz der S-Matrix) und
  Glied 10 (Eindeutigkeit). Eine Korrektur ~ (E/E_LIV)^n verschwindet im weichen Grenzfall; die IR-Aussagen (Glied 2, GW170817,
  LLR-Schranken auf s^XY) blieben unberuehrt. Ein n = 2-Operator mit hoeheren raeumlichen Ableitungen beruehrte zusaetzlich A5 im
  UV - wie bei Horava, dessen IR-Teil nach GW170817 auf |c_13| <= 1e-15 gedrueckt ist (LORENTZ.md 3d).
- **Was es nicht waere:** kein Hinweis auf ein Vorzugssystem im Niedrigenergiebereich, also kein Rueckenwind fuer Badmodelle mit
  Ruhesystem (LORENTZ.md 4.2: Widerspruch ~1e14 bei O(beta)); deren Skala ist eine voellig andere.
- **Wie stark ist der Beleg heute?** Schwach: ein Ereignis, Zufall ~2,4 sigma [E], Hadron-Wahrscheinlichkeit modellabhaengig, KM2A-
  Nullsuche dagegen, und die LIV-Deutung ist in ihrem eigenen Rechenrahmen durch Schauer- und Doppelbrechungsschranken
  ausgeschlossen. Schwaecher als jeder bisherige Eintrag in BEOBACHTUNGSSPANNUNGEN.md (dort mehrere Datensaetze je Spannung).
- **Vorschlag an die Leitung (nicht ausgefuehrt, Dateien nur gelesen):**
  - BEOBACHTUNGSSPANNUNGEN.md: neuer Abschnitt "Carpet-3-Photon aus GRB 221009A" mit Gegenrede in derselben Zeile (KM2A-Nullsuche;
    Schauer-/Doppelbrechungsschranken; O/P-Zufallsabwaegung).
  - LORENTZ.md Z. 63: LHAASO-Textwerte jetzt [S]: subluminal 1,0e20 GeV (n = 1), 6,9e11 GeV (n = 2), PRL 133, 071501, S. 6, Tab. I;
    Abstract "> 10 E_Pl" entspricht im Text 8,2 E_Pl [E]. Die Berichtigung Z. 501 ("'> 10 E_Planck' bleibt richtig") stimmt nur fuer
    den Abstractwortlaut.
  - Keine Folgen fuer laufende Straenge.

---

## 10. Gegensweep-Befunde (Regel 4)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
1. **Richtungsabstand 1,8 Grad** (von Carpet uebernommen) - **geprueft**: Swift-XRT RA 288,2643, Dec +19,7712 (GCN 32632) [S] gegen
   RA 289,5, Dec 18,4 -> 1,80 Grad [E]. Bestaetigt.
2. **Gleiche Skalennormierung** in G/R, LHAASO, Satunin/Troitsky, Martynenko - **geprueft** an den Gleichungen; nur die
   Vorzeichenkonvention unterscheidet sich (G/R xi = +1, S/T s = -1 fuer subluminal). Skalen direkt vergleichbar.
3. **LHAASO-Zenit bei T0 + 4536 s** - **geprueft** [E]: 44,8 Grad (Modell trifft LHAASO-Angaben 28,1 / 35,1 / 50 Grad).
4. **Ungebrochenes Potenzgesetz bis 300 TeV** - nicht geprueft, nur gelesen: Carpet-3 erwartet Klein-Nishina-Abfall oberhalb 10 TeV
   (S. 6); S/T: jede konkave Form erschwert den Carpet-Punkt (S. 3). Jede Kruemmung verschaerft die G/R-Oberschranke [H].
5. **"LIV nur fuer Photonen" als gemeinsame Annahme** von G/R und Martynenko - nicht weiter geprueft.

---

## 11. Kalibrierung

- **(a) Gemessen:** Ereignisdaten Carpet-3 (Zeit, Richtung, Ne, n_mu); KM2A-Nullsuche > 100 TeV T0 bis T0 + 6000 s; LHAASO-Laufzeit-
  schranken; Auger-Myonzahl- und X_max-Daten (Grundlage Martynenko); Polarisation GRB 061122 (Grundlage Doppelbrechung).
- **(b) Nuetzlich verdichtet:** G/R-Oberschranken (bedingt auf: Photon echt und vom GRB, Potenzgesetz bis 300 TeV, Poisson-Kriterium,
  Rechenrahmen I); Zufall 9e-3 (ein Tag, 4,7-Grad-Kreis, Schnitte am Ereignis selbst gewaehlt); Hadron 3e-4 (MC-Klassifikator);
  meine KM2A/Carpet-Abschaetzung [E].
- **(c) Gewachsene Gewissheit ohne neue Evidenz:** 14 Zitate des Carpet-3-Papiers, fast alle "at face value"; die Formulierung
  "LHAASO am Rand des Sichtfelds/keine Meldung nach 2000 s" wandert von Carpet-3 zu G/R und S/T, ohne dass jemand den LHAASO-Satz zur
  Nullsuche zitiert. G/R wurden zwischen v1 und PRL vorsichtiger ("first evidence" -> "potential first indication"), die Evidenz
  blieb dieselbe.
- **Warnzeichen in eigener Sache:** Meine Sicherheit "eher Untergrund" stieg im Lauf der Recherche, waehrend die Frage sich in
  Regime und Konventionen aufloeste. Sie beruht auf einer eigenen Groessenordnungsrechnung (effektive KM2A-Flaeche bei 45 Grad und
  300 TeV geschaetzt), nicht auf einer publizierten Analyse.

---

## 12. Offene Fragen

1. Hat LHAASO eine quantitative obere Grenze (Fluss oder Fluenz > 100 TeV) fuer T0 + 4536 s oder ein Fenster darum? Im Sci.-Adv.-Text
   steht nur "no event was detected". Mit Zahl liesse sich das [E]-Verhaeltnis R ersetzen.
2. Wie gross ist die KM2A-Flaeche fuer 300-TeV-Photonen bei 45 Grad Zenit nach Photon/Hadron-Schnitt (Sci. Adv. Abb. 8 nennt nur bis
   35,1 Grad)?
3. ~~Harte Vakuum-Cherenkov-Schwelle: meine Kinematik gegen die Formel (2 m_e M^2)^(1/3) bei Martynenko u. a.?~~ Teilweise
   beantwortet (Block 10): Jacobson/Liberati/Mattingly 2003, Gl. (21) und (27)-(29), geben mit eta = 0 genau meine Schwellen
   (n = 1: (4 m_e^2 E_LIV)^(1/3), x = 1/2; n = 2: (27/4)^(1/4) sqrt(m_e E_LIV), x = 2/3) [S]. Offen bleibt: (a) welche Konfiguration
   Martynenko u. a. mit (2 m_e M^2)^(1/3) meinen; (b) ob die PeV-Elektronen im Krebsnebel gesichert sind (LHAASO schliesst einen
   Protonenanteil nicht aus) - davon haengt ab, ob die VCR-Schranke die G/R-Fenster schliesst oder nur Restspalten laesst;
   (c) ob jemand diese Rechnung schon fuer Carpet publiziert hat (nicht gefunden).
4. Liefert der String-Schaum (Regime II) ueberhaupt die Schwellenverschiebung der Paarbildung am CMB, die G/R brauchen, wenn er die
   Bethe-Heitler-Schauer unveraendert laesst? G/R rechnen die Schwelle in Regime I.
5. Carpet-Ereignis: gibt es Schauerform-Daten (NKG-Alter, Zeitprofil), die einen tieferen Schauerbeginn pruefen koennten?
6. Satunin 2021 (1,7e13 GeV): ist der Einwand von G/R ("real CL much less than 95 %") berechtigt? Primaerarbeit nicht gelesen.

---

## 13. Quellenliste

| Quelle | Lesetiefe | Datei |
|---|---|---|
| G. Galanti, M. Roncadelli, "Lorentz-Violating Scenarios for the Highest-Energy Photons from GRB 221009A", PRL 137, 111002 (2026), arXiv:2504.01830v3, https://arxiv.org/abs/2504.01830 ; https://journals.aps.org/prl/abstract/10.1103/zjh2-mc47 | [S] Volltext inkl. Supplement | quellen/galanti-roncadelli-2504.01830v3.pdf |
| dies., arXiv:2504.01830v1 (02.04.2025) | [S] Abstract, S. 3 | quellen/galanti-roncadelli-2504.01830v1.pdf |
| D. D. Dzhappuev u. a. (Carpet-3 Group), "Carpet-3 detection of a photon-like air shower ...", PRD 111, 102005 (2025), arXiv:2502.02425, https://arxiv.org/abs/2502.02425 | [S] Volltext | quellen/carpet3-2502.02425v1.pdf |
| D. Dzhappuev u. a., ATel #15669 (2022) | [L?] nur ueber Carpet-3 (pre-trial 1,2e-4, 4536 s) | — |
| LHAASO Collaboration, "Very high energy gamma-ray emission beyond 10 TeV from GRB 221009A", Sci. Adv. 9, eadj2778 (2023), arXiv:2310.08845, https://arxiv.org/abs/2310.08845 | [S] S. 2-4, Abschn. 4.1 | quellen/lhaaso-2310.08845.pdf |
| LHAASO Collaboration, "A tera-electronvolt afterglow from a narrow jet ...", Science 380, adg9328 (2023), arXiv:2306.06372, https://arxiv.org/abs/2306.06372 | [S] S. 3 (Sichtfeld) | quellen/lhaaso-2306.06372.pdf |
| LHAASO Collaboration, "Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A", PRL 133, 071501 (2024), arXiv:2402.06009, https://arxiv.org/abs/2402.06009 | [S] Abstract, S. 2-3, S. 6, Tab. I | quellen/lhaaso-2402.06009.pdf |
| P. S. Satunin, S. V. Troitsky, "Testing new-physics scenarios with the combined LHAASO and Carpet-3 fluence spectrum ...", JETP Lett. 123, 73 (2026), arXiv:2510.07234, https://arxiv.org/abs/2510.07234 | [S] Volltext | quellen/satunin-troitsky-2510.07234v2.pdf |
| N. S. Martynenko, G. I. Rubtsov, P. S. Satunin, A. K. Sharofeev, S. V. Troitsky, "Hypothetical Lorentz invariance violation and the muon content of extensive air showers", PRD 111, 063010 (2025), arXiv:2412.08349, https://arxiv.org/abs/2412.08349 | [S] Abschn. II, V, VI | quellen/martynenko-2412.08349v2.pdf |
| dies., "Constraining Lorentz invariance violation from the depth of air-shower maximum", arXiv:2608.05106 (05.08.2026, nicht begutachtet), https://arxiv.org/abs/2608.05106 | [S] Abstract, Abschn. II, Gl. 38, S. 10 | quellen/martynenko-2608.05106v1.pdf |
| D. D. Ofengeim, T. Piran, "The 300 TeV photon from GRB 221009A: a Hint at Non-linear Lorentz Invariance Violation?", PRD 112, 083055 (2025), arXiv:2508.07153, https://arxiv.org/abs/2508.07153 | [S] S. 5-8, Anhang A | quellen/ofengeim-piran-2508.07153v3.pdf |
| H. Song, B.-Q. Ma, "Carpet-3 300 TeV Photon Event as an Evidence for Lorentz Violation", PLB 870, 139959 (2025), arXiv:2508.08984 | [A] | quellen/arxiv-meta-24m-kandidaten.xml |
| G. Galanti, M. Roncadelli, G. Bonnoli, L. Nava, F. Tavecchio, "GRB 221009A: two distinct hints at once at new physics", arXiv:2502.03453 | [A] | dito |
| L. Qin u. a., "Revisiting Very High Energy Gamma-Ray Absorption ... ALPs and LIV", ApJ (2026), 10.3847/1538-4357/ae4c4d, arXiv:2510.23113 | [A] | dito |
| J.-C. Wang, H. Song, H. Li, J. Zhu, B.-Q. Ma, "Generation of TeV Photons by PeV Neutrinos ...", PRD 114, 063023 (2026), arXiv:2608.21266 | [A] | dito |
| F. Rescic, L. Recabarren Vergara, M. Doro, T. Terzic, "Is There New Physics Beyond 30 TeV in the BOAT?", Phys. Dark Univ. (2026) 102389, arXiv:2511.15542 | [A] | quellen/arxiv-q-gegen.xml |
| C. Li, "Shower formation in the presence of a string-inspired foam in space-time", PLB 869, 139823 (2025), arXiv:2509.00552 | [A] | dito |
| C. Li, B.-Q. Ma, "Probes for String-Inspired Foam, Lorentz, and CPT Violations in Astrophysics", Symmetry 17, 974 (2025), arXiv:2508.11172 | [A] | dito |
| H. Abdalla, "Multi-TeV Gamma Rays from GRB 221009A: Challenges ...", Galaxies 13, 95 (2025), arXiv:2508.09948 | [A] | dito |
| C. Li, B.-Q. Ma, "Constraints to Lorentz violation and ultrahigh-energy electrons in D-foamy space-times", JHEP 10 (2025) 216, arXiv:2505.06121 | [A] | quellen/arxiv-q-vcr.xml |
| LHAASO Collaboration, "Peta-electron volt gamma-ray emission from the Crab Nebula", Science 373, 425 (2021), arXiv:2111.06545 | [A] | quellen/arxiv-2111.06545-meta.xml |
| T. Jacobson, S. Liberati, D. Mattingly, "Threshold effects and Planck scale Lorentz violation: combined constraints from high energy astrophysics", PRD 67, 124011 (2003), arXiv:hep-ph/0209264, https://arxiv.org/abs/hep-ph/0209264 | [S] Abschn. III B, S. 9-10, Gl. (14)-(29) | quellen/jlm-hep-ph-0209264.pdf |
| S. Dichiara u. a., GCN Circ. 32632 (2022), Swift-XRT-Position | [S] | quellen/gcn-32632.json |
| OpenAlex, Zitate von W4410437820 (Carpet-3), Abruf 03.10.2026 | [A] Liste | quellen/openalex-cites-carpet3.json |
| O. Kalashev, F. Aharonian, W. Essey, Y. Inoue, A. Kusenko, PRD 112, 023022 (2025) | [L?] nur ueber G/R | — |
| P. Satunin, EPJC 81, 750 (2021); P. Satunin, EPJC 79, 1011 (2019); R. G. Lang, H. Martinez-Huerta, V. de Souza, PRD 99, 043015 (2019); M. Galaverni, G. Sigl, PRL 100, 021102 (2008); D. Goetz u. a., MNRAS 431, 3550 (2013); R. C. Myers, M. Pospelov, PRL 90, 211601 (2003) | [L?] nur als Zitat in gelesenen Arbeiten | — |

**Eigener Regelverstoss:** einmal `awk` in einem Anzeige-Befehl (18:11:55, Dateiliste); kein Ergebnis haengt daran (ARBEITSFELD
Abschn. 6). WebSearch war ab Block 6 nicht verfuegbar (Sitzungsbudget erschoepft); Ersatz arXiv-API und OpenAlex.
