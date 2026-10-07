
Papier-Agent (Anthropic, fortgesetzt aus Runde 8), Auftrag von claude-primary. Nur Papier: keine lokale Rechnung, keine
Interpreter; Rechnungen von Hand, Formeln im Text. Explorativ, keine formale Bestaetigung. Keine Aenderung an fremden Dateien.

- Beginn: 2026-09-30 07:07:56 CEST (date)
- Ende: 2026-09-30 07:18:47 CEST (date, nach dem letzten inhaltlichen Schreiben gemessen)

Lesetiefe: **[A]** an der Quelle gelesen, **[A-W]** ueber das Abrufwerkzeug gelesen (Zusammenfassung eines Hilfsmodells),
**[S]** nur Suchtreffer, **[L]** Lehrbuch/Gedaechtnis, **[P]** Projektdatei, **[E]** eigene Handrechnung, **[ES]** eigener
Schluss, **[H]** Hypothese.

Status: ARBEITSDATEI (Feldregel 5). Der Bericht kommt oben hinzu, das Arbeitsfeld bleibt unten. Gestrichenes bleibt
~~gestrichen~~.

---

## Kurzfazit

   die Schwarzschild-Metrik (gamma = beta = 1, Photonensphaere 1,5 rs, Schatten 3 sqrt(3) GM/c^2) [A/E].
2. Sein Index ist anisotrop, n_r = (1 - u)^(-1) und n_t = (1 - u)^(-1/2) im Flaechenradius. Als optische Geometrie ist das der
   isotrope Schwarzschild-Index, aber nur, wenn man seine Richtungsregel geometrisch liest (R1).
   Photonenrings steigt von pi auf 1,34 pi, und die Lichtablenkung zweiter Ordnung sinkt um (pi/4)(M/b)^2 [E/H]. Heute ist
   nichts davon messbar.
   woertlich statisches Feld gaebe Frame-Dragging null, Gravity Probe B misst -37,2 +- 7,2 mas/Jahr.
5. **ST-2:** Alle vier Geister-Lager haben dieselbe Laborsignatur, das Yukawa -4/3. Lagertypisch sind nur Streuung bei E >= m2
   (unmessbar klein) und die Kosmologie (r-Fenster, Nicht-Gaussizitaet), und die nur fuer m2 nahe der Inflationsskala.

## Erwartungsverstoesse (das Wichtigste zuerst)

   - Erwartet: keine Starkfeld-Aussage.
   - Gefunden [A]:
     - "In a usual gravitational field (i.e. in absence of a black hole) we can assume that (rs/r) << 1" (gravity.txt Z. 761 f.)
     - Die Richtungsregel ist eine Komponentenzerlegung (A.5 bis A.7).
   - Geometrisch gelesen (R1) ist sie exakt die optische Schwarzschild-Metrik. Woertlich gelesen (R2) ist sie eine
     Finsler-Metrik, die in O(u^2) abweicht (Z2).
2. **V-G2b: Auch die abweichende Lesart laesst den Schatten unveraendert.**
   - Erwartet: Eine andere Richtungsregel verschiebt den Schattenradius.
   - Der Unterschied steckt im Lyapunov-Exponenten (Z3), also in der Helligkeit der Unterringe, nicht im Durchmesser.
3. **V-S1: Es gibt neue lagertypische Signaturen, und eine davon ist schon eine Labormessung.**
   - Erwartet: nur das Fakeon-r-Fenster.
   - Gefunden:
     - Aoki/Strumia 2025: Positivitaetsverletzende Amplituden mit umgekehrtem Vorzeichen und Nicht-Gaussizitaet mit umgekehrtem
       Vorzeichen [A-W].
     - Kubo/Kuntz 2025: unterdrueckte Tensoramplitude [A-W].
   - [ES] Im statischen Grenzfall ist das "umgekehrte Vorzeichen" genau das negative Yukawa -4/3. Die Torsionswaage prueft also
     die Positivitaet eines meV-Spin-2-Pols, aber lageruebergreifend.
   - GP-B misst -37,2 +- 7,2 mas/Jahr (ART -39,2) [A-W].
     es keine Widerlegung, sondern eine fehlende Festlegung.
5. **V-S2: Das Fakeon-r-Fenster sitzt auf Starobinsky-Inflation, und die geraet 2025 unter Druck.** BAO verschiebt n_s nach oben
   und "challenging ... Starobinsky" (Balkenhol u. a. 2025/26 [A-W]). Die Obergrenze r < 0,034 laesst das Fenster (<= 3,3e-3)
   noch offen.
   markiert).

---


### Antwort

nicht rotierende Einzelquelle (Z1):

- Metrik [E]: g_00 = -(c_t/c0)^2 = -(1 - u), g_rr = (c_t/c_r)^2 = (1 - u)^(-1), g_Omega = r^2. Das ist Schwarzschild exakt.
  - r ist der Flaechenradius, weil tangentiale Massstaebe unveraendert bleiben (Exponent p - 1/2 = 0 in 6.2/C.8 [A]).
  - Die Uhren folgen B.10 [A].
- PPN: gamma = 1 und beta = 1 (Weinberg-Standardform) [E/L]. Gemessen: |beta - 1|, |gamma - 1| < ~7e-5 (INPOP [A-W]),
  gamma - 1 = (2,1 +- 2,3)e-5 (Cassini [P]). Vertraeglich.
- Photonensphaere 1,5 rs und Schatten b = 3 sqrt(3) GM/c^2, in R1 und R2 (Z3). EHT Sgr A*: "within ~10% of the Kerr
  predictions" [A-W]. Keine Trennung moeglich.
- Lichtablenkung zweiter Ordnung und Photonenring (Z3, Z4):
  - R1: wie ART.
  - R2: Lyapunov-Exponent 1,342 pi statt pi, Unterring-Helligkeit 1,5 % statt 4,3 % des vorigen Rings.
  - R2: Ablenkung zweiter Ordnung (7 pi/2)(M/b)^2 statt (15 pi/4)(M/b)^2, am Sonnenrand -0,73 uas bei 10,9 uas.
- Periastron hoeherer Ordnung, Doppelpulsar [A, Kramer 2021]:
  - omega-dot_2PN ~ 4,39e-4 Grad/Jahr, das 35-Fache des Messfehlers.
  - Lense-Thirring -3,77e-4 x I_A45 Grad/Jahr.
    Testteilchen-Grenze waere Schwarzschild.
  - Ohne Lense-Thirring laege I_A = 0 noch in der reinen Timing-Schranke I_A < 3,0e45 g cm^2 (90 %) [A]. Heute kein Konflikt.


- Der isotrope Index gehoert zur isotropen Koordinate rho mit r = rho (1 + M/2rho)^2 [E].
- **Als Funktionen verschieden, als optische Geometrie gleich.** Exakt gilt das in R1 (Ellipsenregel), in R2 nur bis zur ersten
  Ordnung.
  Ordnung ist sie eine gewaehlte Potenzform. Unser Paper nennt sie "importiert" (G17 [P]).

**Frage 3: Welche Zusatzannahme legt es fest, und was folgt messbar?**

| Zusatzannahme | Folge | messbar? |
|---|---|---|
| Richtungsregel als Strahlflaechen-Ellipse (R1) | Schwarzschild exakt fuer Licht | nichts zu trennen |
| Richtungsregel woertlich (R2) [H] | Lyapunov 1,34 pi (Unterringe ~2,9-mal schwaecher); Ablenkung zweiter Ordnung -(pi/4)(M/b)^2 | Unterringe erst mit BHEX (Vorschlag, Weltraum-VLBI; Lyapunov mit ~10 % bei n = 2 [S]); zweite Ordnung am Sonnenrand (0,7 uas) ausser Reichweite |
| Random Walk in zweiter Ordnung, v^2/c^2 = u + kappa u^2 (z. B. Austauschteilchen selbst gebremst) [H] | beta = 1 - 2 kappa; Schatten delta b/b = (2/3) kappa | Ephemeriden: |kappa| < 3,6e-5, Schatten < 2,4e-5 veraendert; das EHT sieht nichts. Nur Terme ab u^3 waeren an der Photonensphaere frei |
| Regel fuer bewegte/rotierende Quellen | Gravitomagnetismus, Frame-Dragging, Kerr-Schatten | woertlich statisch: Frame-Dragging 0 gegen GP-B -37,2 +- 7,2 mas/Jahr (5 sigma) [A-W]; Kerr gegen Schwarzschild im Schatten nur wenige % [L] |
| Zweikoerpergesetz (Ueberlagerung, Retardierung) | omega-dot_2PN, Lense-Thirring, Pdot | Doppelpulsar: 2PN-Term 35 sigma, Lense-Thirring vergleichbar [A] |

### Belegstufe

- Lyapunov-Exponent und zweite Ordnung in R2: [E], Handrechnung, nicht nachgerechnet. Die R1-Probe trifft den bekannten
  Schwarzschild-Wert gamma = pi.
- Messwerte: [A-W] (EHT, INPOP, GP-B), [A] (Kramer 2021), [S] (EHT-delta-Zahlen, BHEX-Genauigkeit).

### Unterscheidungspunkt

- Schraege Strahlen bei u ~ 0,5 bis 0,7, also die Unterringe n >= 1 des Photonenrings. Dort trennt sich R2 von Schwarzschild,
  im Starkfeld. Dort ist er heute unbestimmt.

### Naechster Schritt (mit Aufwand)

- Keiner fuer die Starkfeld-Frage. Moeglich waere eine Nachrechnung von Z3 (Lyapunov in R2) als kleiner Test auf der .69 durch
  numerische Strahlverfolgung beider Lesarten: 30 min Schreiben, unter 1 min Rechnung. Der Ausgang ist aber weitgehend vorab
  ableitbar; ich empfehle ihn nicht.
  - Hinweis GP-B

### Latten

  Schwarzschild).
- L2: R1 gibt Photonensphaere 1,5 rs, b = 3 sqrt(3) M und gamma = pi (bekannte Werte).
- L3: entfaellt (Papier).
- L4: Optische Metrik und PPN sind Standard; neu sind nur die R2-Zahlen.
- L5: ja (EHT, INPOP, GP-B, Doppelpulsar); keine trennt.


  woertlichen Lesart R2, und die ist heute nicht messbar.

---

## Karte ST-2 (Glied 7: Geister-Lager gegen Messsignaturen)

### Antwort

Tabelle Z6 und Groessenordnungen Z7 unten. Kurz:

| Lager | lagertypisch | Labor |
|---|---|---|
| 1 Lee-Wick, instabile Resonanz | Positivitaetsverletzende Amplituden, Akausalitaet auf 1/|Gamma|, Nicht-Gaussizitaet mit umgekehrtem Vorzeichen (Aoki/Strumia 2025) | nur statisches Yukawa -4/3 |
| 2 komplexer Geist, Unitaritaetsbruch (Kubo/Kugo) | Wahrscheinlichkeitsverlust oberhalb 2 Re m; Tensoramplitude unterdrueckt (Kubo/Kuntz 2025) | nur statisches Yukawa |
| 3 Fakeon (Anselmi) | r-Fenster 4/3 < N^2 r < 12 (Starobinsky + C^2); Mikroakausalitaet, die den klassischen Grenzfall ueberlebt: "<F> = ma" mit einem Mittel, das "a little bit of 'future'" enthaelt (Anselmi 2019 [A-W]), auf der Zeitskala ~hbar/(m_chi c^2) | keine (m_chi ~ Inflationsskala); bei einer Labormasse m_chi ~ 5 meV waeren es ~0,1 ps Vorlauf, siehe Z7 |
| 4 "dualer invertierter Oszillator" (Kumar/Marto 2026) | keine genannt | nur statisches Yukawa |

- **Wo waere eine Laborsignatur?** Nur im statischen Potential, und das ist fuer alle Lager dasselbe [ES]: Yukawa -4/3 bei
  lambda2 plus +1/3 bei lambda0.
  - Groessenordnung: heute m2 >~ 5 bis 8 meV (lambda2 < 25 bis 39 um); ein Nachweis braucht ~20-fache Empfindlichkeit bei ~20 um
    (ST-1).
  - Das negative Vorzeichen ist zugleich der Positivitaetstest.
- **Akausalitaet im Labor:** Zeitskala hbar/m2 ~ 1e-13 s bei Laengen ~40 um und gravitativen Kraeften ~1e-14 N; die gravitative
  Breite liegt bei ~1e-63 eV. Nicht zugaenglich.
- **Streuamplituden:** ~ (m2/M_Pl)^2 ~ 1e-61 bei sqrt(s) ~ m2. Nicht zugaenglich.
- **Kosmologie:** Das Fakeon-r-Fenster ist mit LiteBIRD im oberen Teil pruefbar (r < 0,034 heute [A-W]; delta r < 0,001 geplant
  [S]). Die Lee-Wick-Nicht-Gaussizitaet braucht m2 ~ H_inf.
- **Glied 7:** Keines der Lager erfuellt die CEMZ-Voraussetzungen (Positivitaet, Kausalitaet). Das Fakeon-Lager gibt die
  Kausalitaet sogar ausdruecklich auf (Anselmi 2026 [A]). Die Glied-7-Aussage bleibt davon unberuehrt, und es entsteht keine neue
  Laborgroesse fuer Glied 7.

### Belegstufe

- Abstracts [A]/[A-W], einzelne Zahlen [S] (r-Fenster in der 1000r-Form, LiteBIRD-Genauigkeit).
- Groessenordnungen [E], Buendelung [ES].

### Unterscheidungspunkt

- Lager untereinander: on-shell bei E >= m2 (Resonanzform, Unitaritaet, Kausalitaet) und in der Inflation fuer m2 ~ H_inf. Im
  Labor **empirisch nicht unterscheidbar**.
- Geist gegen gesunden Spin 2: das Vorzeichen des Yukawa-Terms, zugaenglich fuer m2 <~ 10 meV.

### Naechster Schritt

- Keiner im Labor ausser dem ST-1-Datenweg (Drehmomentdaten Lee 2020).
- Kosmologisch: das r-Fenster und die n_s-Frage beobachten (LiteBIRD, CMB-S4). Das ist extern und fuer uns kein Rechenauftrag.

### Latten

- L1: ja. Ein Lager haette eine Laborsignatur haben koennen; keines hat eine eigene.
- L2: Z7-Groessenordnungen sind Einheitenumrechnungen; die Yukawa-Aussage ist mit ST-1 konsistent.
- L3: entfaellt.
- L4: Literatur.
- L5: ja (Torsionswaage, CMB).

### Vorschlag ST-2: **parken**

- Grund: Keine Laborsignatur ueber das lageruebergreifende Yukawa hinaus. Lagertypische Tests gibt es nur kosmologisch und nur bei
  Inflationsmassen.

---

## Regime und Moderatoren (Regel 1)

| Befund | Moderator |
|---|---|
| R1 gegen R2 | nur fuer schraege Strahlen in O(u^2); radial, tangential und in erster Ordnung identisch |
| Geister-Lager | Pol-Vorschrift (Feynman, Lee-Wick, Fakeon, Hauptwert) und Zeitregime (kuerzer oder laenger als 1/Gamma); im statischen Regime ohne Wirkung |
| Signaturen im Labor gegen Kosmologie | Verhaeltnis m2 zu H_inf bzw. zur Labor-Energieskala |

## Gegensweep (Regel 4)

| Selbstverstaendlich | geprueft? | Ergebnis |
|---|---|---|
| GS4: Das Fakeon-r-Fenster ist unbelastet | **ja** | r < 0,034 laesst es offen; BAO-verschobenes n_s setzt Starobinsky unter Druck [A-W] |
| GS5: Statisches Potential vorschriftsunabhaengig | **teilweise** | Fakeon: klassischer Grenzfall = Mittel aus retardiertem und avanciertem Potential [S]. Bei statischer Quelle sind beide gleich, also dasselbe Yukawa [ES]; Lee-Wick und Kubo-Kugo nicht an einer Quelle geprueft |
| GS6: Kerr-Schatten nur wenige % von Schwarzschild | nein | [L] |

## Kalibrierung

- **(a) Gemessen:**
  - EHT Sgr A* ~10 %
  - INPOP beta, gamma < ~7e-5
  - Cassini
  - GP-B
  - Doppelpulsar omega-dot mit 2PN-Anteil 35 sigma
  - r < 0,034
- **(b) Nuetzlich verdichtet:**
  - R1/R2
  - Lyapunov 1,34 pi
  - delta alpha = -(pi/4)(M/b)^2
  - kappa-Abbildung
  - Lager-Signatur-Tabelle
  - Residuum-Vorzeichen als gemeinsame Groesse
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "Keine Laborsignatur der Lager" haengt daran, dass m2 nur gravitativ koppelt.
  Deshalb stehen beide Lesarten im Bericht.

## Offene Fragen

   "black hole"-Stelle ausser Z. 761; Rotation nicht gesucht.)~~ Erledigt (G7, 07:18): keine solche Regel in pdf/*.txt und im
2. R2-Lyapunov numerisch bestaetigen? Nur, falls die Leitung den R2-Fall weiterverfolgen will.
3. Statisches Potential in allen vier Vorschriften an einer Quelle nachlesen (GS5).
4. Fakeon-Fenster unter der 2025er n_s-Verschiebung: Gilt m_chi > m_phi/4 mit dem neuen n_s noch?

## Quellenliste

  C) [A]
- EHT Collaboration (2022): First Sgr A* EHT Results VI. ApJL 930, L17. https://arxiv.org/abs/2311.09484 [A-W]; delta-Werte [S]
  ueber https://iopscience.iop.org/article/10.3847/2041-8213/ac6756
- Fienga, A. u. a. (2021): Evolution of INPOP planetary ephemerides and Bepi-Colombo simulations. IAU Symp. 364.
  https://arxiv.org/abs/2111.04499 [A-W]
- Kramer, M. u. a. (2021): Strong-field Gravity Tests with the Double Pulsar. PRX 11, 041050. https://arxiv.org/abs/2112.06795
  [A, PDF-Text]
- Everitt, C. W. F. u. a. (2011): Gravity Probe B: Final Results. PRL 106, 221101. https://arxiv.org/abs/1105.3456 [A-W]
- Lupsasca, A. u. a. (2024): The Black Hole Explorer: Photon Ring Science, Detection and Shape Measurement.
  https://arxiv.org/abs/2406.09498 [A]
- Salehi, K. u. a. (2024): Influence of Observer Inclination and Spacetime Structure on Photon Ring Observables.
  https://arxiv.org/abs/2411.15310 [A-W]
- Aoki, S.; Strumia, A. (2025): Testing the arrow of time at the cosmo collider. https://arxiv.org/abs/2510.05204 [A-W]
- Kubo, J.; Kuntz, J. (2025): Primordial Gravitational Waves in Quadratic Gravity. JCAP 05 (2025) 093.
  https://arxiv.org/abs/2502.03543 [A-W]
- Balkenhol, L. u. a. (2025/2026): Inflation at the End of 2025: Constraints on r and n_s. https://arxiv.org/abs/2512.10613 [A-W]
- Anselmi, D.; Bianchi, E.; Piva, M. (2020): JHEP 07 (2020) 211. https://arxiv.org/abs/2005.10293 [A-W, Runde 8]
- Anselmi, D. (2026): On Causality and Predictivity. https://arxiv.org/abs/2601.06346 [A, Runde 8]
- Kubo, J.; Kugo, T. (2023, 2024): PTEP 2023, 123B02; PTEP 2024, 053B01 [S, Runde 8]
- Buoninfante, L. (2025): https://arxiv.org/abs/2501.04097 [S]; (2026): https://arxiv.org/abs/2606.18349 [A, Runde 8]
- Kumar, K. S.; Marto, J. (2026): https://arxiv.org/abs/2604.19707 [A, Runde 8]
- Donoghue, J. F.; Menezes, G. (2024): Physical Running of Couplings in Quadratic Gravity. PRL 133, 021604.
  https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.133.021604 [S]
- Weinberg, S. (1972): Gravitation and Cosmology, Standardform A(r), B(r) mit beta, gamma [L]
  art-grenzen-20260921/WARUM-SPIN-2.md (Cassini-gamma, CEMZ) [P]

## Einfach gesagt

genau Einsteins Loesung fuer einen ruhenden Stern oder ein ruhendes Schwarzes Loch heraus, auch der Schattenring, den das
Event Horizon Telescope fotografiert hat. Nur wenn man eine seiner Formeln sehr woertlich nimmt, waeren die feinen Nebenringe
um ein Schwarzes Loch etwas dunkler; das koennte erst ein geplantes Weltraumteleskop sehen. Bei den Geister-Theorien der
Quantengravitation gilt: Im Labor sehen alle gleich aus, naemlich als leicht geschwaechte Anziehung auf winzigen Abstaenden;
unterscheiden kann man sie hoechstens an den Spuren des Urknalls.

---


- Beginn: 2026-09-30 07:24:36 CEST (date). Hoechstens etwa 60 Minuten, nur Papier.

### Erwartungen vor den Abrufen (07:24:36, vor jedem Abruf dieses Nachtrags)

| Nr | Abruf | Erwartung | Ergebnis | Verstoss? |
|---|---|---|---|---|
| H2 | LAGEOS/LARES, neueste Auswertung (24 Monate, auch LARES-2) | Ciufolini u. a.: Mitfuehrung auf ~2 bis 5 % bestaetigt (mu ~ 0,99 bis 1,00); Kritik (Iorio) an der Fehlerbilanz; LARES-2 erste Ergebnisse moeglich | **Verstoss:** Ciufolini u. a., Nature 2026 (DOI 10.1038/s41586-026-10715-0): LARES-2 + LAGEOS + GRACE, drei Jahre, relative Unsicherheit "one part in a thousand" [A-W, nur ueber phys.org 07/2026; Nature-Abstract nicht erreichbar (Login), Wortlaut dort nicht gelesen]. Aelter: mu = (0,994 +- 0,002) +- 0,05 (Ciufolini u. a. 2016, EPJC 76:120 [A-W]). Kritik: Iorio 2025 (EPJC 85, 255): J2 verfaelscht die Messung direkt und ueber Bahnfehler, keine Zahl im Abstract [A-W]. Sollwert ~30,7 mas/Jahr [S] | ja (Genauigkeit 20-mal besser als erwartet) |
| H3 | Breton u. a. 2008 (Spinpraezession von B im Doppelpulsar) | Omega_B = 4,77 (+0,66/-0,65) Grad/Jahr gegen ART 5,07 | Bestaetigt: "4.77 (+0.66,-0.65) degrees per year (68% confidence level) ... consistent with ... general relativity within an uncertainty of 13%" [A-W, arXiv:0807.2644]. ART-Wert 5,07 Grad/Jahr selbst nachgerechnet (G3-Z3) | nein |
| H4 | Desvignes u. a. 2019 (PSR J1906+0746) und Venkatraman Krishnan u. a. 2020 (PSR J1141-6545, Lense-Thirring durch einen Weissen Zwerg) | J1906: Praezession ~2,2 Grad/Jahr auf ~5 % mit der ART vertraeglich; J1141: Frame-Dragging im Binaersystem nachgewiesen, Genauigkeit ~20 % | J1906: 2,17 +- 0,11 Grad/Jahr, "within 5%" nur [S] (meine arXiv-Nummer war falsch, Quelle nicht gelesen). Neu: Vleeschower u. a. 2026 (MNRAS, arXiv:2602.05947): Massen 1,316(5) und 1,297(5) Msun, und ein anomales xdot deutet auf einen schnell rotierenden Weissen Zwerg als Begleiter [A-W]. J1141: Abstract [A-W] nennt "combination of a Newtonian quadrupole moment and Lense-Thirring precession", keinen Anteil und keine Signifikanz | teilweise (J1141 ohne Zahl) |
| H5 | alpha1-Schranke (Shao/Wex 2012) und PPN-Form der Lense-Thirring-Praezession (Will, Living Reviews 2014) | alpha1 = -0,4 (+3,7/-3,1)e-5 (95 %); Lense-Thirring proportional zu (1 + gamma + alpha1/4)/2 | alpha1 bestaetigt: "-0.4^{+3.7}_{-3.1} e-5 (95% CL) from PSR J1738+0333" [A-W, arXiv:1209.4503]. Die Will-Form nicht nachgelesen [L] | nein |

### Zwischenbefunde G3

- pdf/rfeld.txt ("Relativistic Contraction without Einstein!"):
  - "it is assumed that the exchange particles are moving with the speed of light in relation to a fixed frame. So the
    following is compatible with the assumption of an ether as a general reference of motion" (Z. 31 bis 34).
    Aberration der Austauschteilchen, "an increase of density in the direction of motion" (Z. 72 bis 76).
  - Ergebnis: Das Feld zwischen zwei **mitbewegten** Ladungen ist um 1/gamma^2 geschwaecht, "compensated by a reduction of the
    distance by a factor of gamma^2" (Z. 130 bis 157). Das ist seine Herleitung der Laengenkontraktion.
- pdf/main.txt Z. 86 bis 88: "The contraction is simply a consequence of the fact that the fields holding together the
  constituents of physical objects contract. The reason for this is the finite speed of light at which the binding fields
  propagate when in motion."
- **Nicht vorhanden** (grep nach drag, Fresnel, aether/ether, carried, entrain, moving source, rotat, frame-dragging,
  Lense-Thirring, Gravity Probe, gravitomagnet in pdf/*.txt und fmhc-physics-fulltext.md):
  - keine Regel fuer die Gravitation einer bewegten oder rotierenden Quelle
  - keine Kraft zwischen **relativ** zueinander bewegten Koerpern, also auch kein Magnetismus-Analogon
  - keine Mitfuehrung
  - Rotation kommt nur als Galaxienrotation (Dunkle Materie) und Sagnac vor.
- [ES] Die Aether-Kinematik aus rfeld.txt (Austauschteilchen mit c im Aethersystem, Aberration am bewegten Sender) ist
  dieselbe, aus der in der Elektrodynamik das Magnetfeld folgt (Lienard-Wiechert). Auf Gravitation angewandt wuerde sie das

**G3-Z2 (statische Lesart gegen Messungen, [E] mit Quellzahlen):**

| Messung | gemessen | ART | statische Lesart | Abstand "null" bzw. statisch zur Messung |
|---|---|---|---|---|
| GP-B Frame-Dragging | -37,2 +- 7,2 mas/Jahr [A-W] | -39,2 | 0 | 37,2/7,2 = **5,2 sigma** |
| LAGEOS/LAGEOS 2/LARES 2016 | mu = 0,994 +- 0,002 (formal) +- 0,05 (systematisch) [A-W] | 1 | 0 | 0,994/0,05 = **~20 sigma** (mit der systematischen Schranke als sigma) |
| LARES-2 + LAGEOS 2026 | relative Unsicherheit ~1e-3 [A-W, Sekundaerquelle] | 1 (~30,7 mas/Jahr Knoten [S]) | 0 | **~1000 sigma** (Sekundaerquelle; Nature-Wortlaut nicht gelesen) |
| Doppelpulsar, Spin-Bahn (Lense-Thirring an omega-dot) | omega-dot_LT,A ~ -3,77e-4 x I_A45 Grad/Jahr; aus Timing allein I_A < 3,0e45 g cm^2 (90 %) [A] | I_A ~ 1,15 bis 1,48 | I_A-Term fehlt | **nicht getrennt**: "null" liegt in der Timing-Schranke |
| Doppelpulsar, Spinpraezession von B | 4,77 (+0,66/-0,65) Grad/Jahr [A-W] | 5,07 [E] | 2,26 [E, G3-Z3] | (4,77 - 2,26)/0,65 = **3,9 sigma** |

**G3-Z3 (Spinpraezession im Doppelpulsar zerlegt, [E]):**
- Barker-O'Connell-Form fuer den Spin von B: Omega_B = (2 pi/P_b)^(5/3) T_sun^(2/3) m_A (4 m_B + 3 m_A)/(2 M^(4/3)) / (1 - e^2) [L].
- Mit P_b = 0,1022515593 d, e = 0,087777, m_A = 1,338185, m_B = 1,248868 Msun (Kramer 2021, Tab. IV [A]) ergibt sich
  Omega_B = 5,074 Grad/Jahr. Probe: Das trifft den Literaturwert 5,0734 [L].
- Zerlegung im Schwerpunktsystem, in Einheiten G m_A v/(c^2 r^2) (m_A/M):
  - geodaetischer Anteil (3/2) m_A (B bewegt sich im Feld von A)
  - gravitomagnetischer Anteil 2 m_B (A bewegt sich)
- Die statische Lesart (bewegte Quelle ohne Zusatzfeld) behaelt nur (3/2) m_A: Anteil 2,007/(2,007 + 2,498) = 0,4456, also
  2,26 Grad/Jahr.
- Anteile linear in der Schwerpunktgeschwindigkeit gegen das Aethersystem mitteln sich ueber eine Bahn heraus (Gradient dreht
  mit) [ES].

**G3-Z4 (Mitfuehrung als minimale Erweiterung [H], [E]/[L]):**
- Optische Metrik eines bewegten Mediums (Gordon 1923 [L]): g_munu = eta_munu + (1 - 1/n^2) u_mu u_nu.
  folgt g_0i = -(4U/c^2)(w_i/c).
- ART (linear): g_0i = -4 V_i/c^3 mit V = G Int rho v/|x - x'| d^3x'.
- **Gleichheit genau dann, wenn U w = V:** Das Medium am Ort x bewegt sich mit dem U-gewichteten Mittel der
  Quellgeschwindigkeiten. Das ist die einfachste Regel: "Jedes Teilchen fuehrt seinen Brechungsbeitrag voll mit
  (Koeffizient kappa = 1), die Beitraege addieren sich linear, und Licht erfaehrt im bewegten Medium die Fresnel-Mitnahme
  1 - 1/n^2."
  - Translation: w = v (volle Mitfuehrung).
  - Rotierende Kugel, Fernfeld: V = G (J x x)/(2 r^3), also Medium-Winkelgeschwindigkeit omega_m(r) = J/(2 M r^2) = (C/2)(R/r)^2
    Omega (C = Traegheitsmomentfaktor).
  - Erde (C = 0,3307 [L]): an der Oberflaeche 16,5 % der Erddrehung, auf LAGEOS-Hoehe (a = 12 270 km) 4,5 %.
- **Frei oder erzwungen?**
  - Mit Teilmitfuehrung kappa ist Frame-Dragging proportional zu kappa. In der PPN-Sprache wird aus
    1 + gamma + alpha1/4 = 2 kappa dann alpha1 = -8 (1 - kappa) [L: Will; ES].
  - Die Pulsarschranke |alpha1| <~ 4e-5 gibt |1 - kappa| <~ 5e-6, falls dasselbe kappa fuer Translation und Rotation gilt
    (natuerlich, wenn jedes Massenelement seinen Beitrag mitfuehrt).
  - **kappa = 1 ist also erzwungen, nicht frei.**
  - Der Faktor 4 = 2(1 + gamma) koppelt Frame-Dragging an gamma. Mit Cassini-gamma ist der Wert festgelegt.
- **Zweite Messung fuer diese Erweiterung:**
  - (a) alpha1: die Translations-Mitfuehrung, schon auf 5e-6 bestaetigt.
  - (b) LARES-2 (1e-3) prueft kappa (1 + gamma)/2 bei Rotation.
  - (c) Spinpraezession von B: Mitfuehrung durch Bahnbewegung, 13 %.
  - (d) Erst jenseits der ersten Ordnung waere etwas Neues moeglich: nichtlineare Ueberlagerung der Mitfuehrung nahe
    rotierender Schwarzer Loecher (Kerr). Die Gordon-Form mit n = 1 + 2U ist dort nicht festgelegt.


   - Zu Gravitation bewegter oder rotierender Quellen, zur Mitfuehrung des Mediums, zu Fresnel und zu Gravitomagnetismus steht
     nichts da [A, G3-Z1].
   - Es gibt aber eine Aether-Kinematik fuer Felder bewegter **Ladungen**: rfeld.txt Z. 31 bis 34, "an ether as a general
     reference of motion"; Aberration der Austauschteilchen Z. 72 bis 76.
     bewegten Koerpern leitet er nicht her.
2. **Statische Lesart** (Brechungsfeld reist mit der Quelle, erzeugt aber keine geschwindigkeitsabhaengige Wirkung):
   - GP-B: "null" liegt 5,2 sigma neben -37,2 +- 7,2 mas/Jahr.
   - LAGEOS/LARES 2016: ~20 sigma (mu = 0,994 +- 0,05).
   - LARES-2 2026: ~1000 sigma, nach einer Sekundaerquelle; den Nature-Wortlaut habe ich nicht gelesen.
   - Doppelpulsar:
     - Spinpraezession von B: statisch 2,26 statt 5,07 Grad/Jahr, gemessen 4,77 (+0,66/-0,65), also **3,9 sigma**.
     - Lense-Thirring an omega-dot ist noch nicht von den Massen getrennt; "null" ist dort erlaubt.
   - Im PPN-Rahmen entspricht die statische Lesart alpha1 = -8. Das waere um ~5 Groessenordnungen ausgeschlossen, gilt aber nur,
3. **Minimale Erweiterung [H]:**
   - Jedes Teilchen fuehrt seinen Brechungsbeitrag voll mit (kappa = 1), die Beitraege addieren sich linear, und im bewegten Medium
     gilt die Fresnel-Mitnahme 1 - 1/n^2 = 4U/c^2.
   - Das ergibt genau g_0i = -4V/c^3 der linearen ART, also Einsteins Frame-Dragging. Um die Erde rotiert das Medium mit
     (C/2)(R/r)^2 der Erddrehung.
   - **kappa ist erzwungen, nicht frei:** Teilmitfuehrung entspricht alpha1 = -8 (1 - kappa), und Pulsare verlangen
     |1 - kappa| <~ 5e-6.
   - Zweite Messungen: alpha1 (Translation, schon erfuellt), LARES-2 (Rotation, 1e-3), Spinpraezession im Doppelpulsar
     (Bahnbewegung, 13 %).
4. **Einordnung:** Kein echter Unterscheider, sondern eine Luecke.
   - Mit der einen, erzwungenen Zusatzannahme "volle Mitfuehrung" faellt er in erster Ordnung mit der ART zusammen; eine eigene
     Vorhersage bleibt dort nicht.
     ausgeschlossen (4e-12 gegen 4,5e-3 [P]).

### Belegstufe, Unterscheidungspunkt, naechster Schritt

- **Belegstufe:**
  - GP-B, LAGEOS 2016, Breton 2008, Shao/Wex [A-W]
  - Kramer 2021 [A]
  - LARES-2 2026 [A-W, Sekundaerquelle]
  - J1906 und J1141 ohne gelesene Zahl [S]
  - Zerlegungen und Mitfuehrung [E]; PPN-Zuordnung [L/ES]
- **Unterscheidungspunkt:**
  - Zwischen statischer Lesart und ART ist er schon ueberschritten: jeder Test mit bewegter oder rotierender Masse.
- **Naechster Schritt:**
  - Keiner als Rechnung.
    LAGEOS, Doppelpulsar); ohne sie ist es ausgeschlossen, mit ihr in 1PN gleich der ART."
  - Optional: den Nature-Wortlaut LARES-2 per Zugang lesen (Finns APS/Nature-Login).

### Regime und Moderatoren G3 (Regel 1)

- LAGEOS/LARES-Genauigkeit:
  - Ciufolini u. a.: 5 %, 2026 dann 0,1 %.
  - Iorio 2025: J2 und Bahnfehler begrenzen die Genauigkeit.
  - Moderator: Behandlung des Erdschwerefelds (J2, Gezeiten) und der Bahnunterschiede der Satelliten. Fuer die Frage "null
    oder nicht" ist das ohne Belang, denn GP-B und die aelteren 5 % reichen dafuer schon.
- Statisch gegen mitgefuehrt: Moderator ist allein kappa. Messungen an Translation (alpha1) und Rotation (GP-B, LARES) greifen an
  derselben Groesse an (Regel 6: drei Wege zu kappa; der schaerfste ist alpha1).

### Gegensweep G3 (Regel 4)

| Selbstverstaendlich | geprueft? | Ergebnis |
|---|---|---|
| Die ART-Spinpraezession von B ist 5,07 Grad/Jahr | **ja** | selbst nachgerechnet: 5,074 [E, Eingaben A] |
| Gravitomagnetismus ist nur die Rotation der Quelle | **ja** | Nein: 55 % der Spinpraezession von B stammen aus der Bahnbewegung von A (G3-Z3) |
| Nature 2026 (LARES-2) sagt 1e-3 | nein | nur Sekundaerquelle und Suchtreffer; Wortlaut nicht gelesen |
| Die PPN-Form (1 + gamma + alpha1/4)/2 | nein | [L] |

### Kalibrierung G3

- **(a) Gemessen:** GP-B, LAGEOS 2016, Breton 2008, alpha1 (Shao/Wex), Massen und Bahn des Doppelpulsars (Kramer 2021).
- **(b) Verdichtet:**
  - 3,9-sigma-Zerlegung fuer B
  - Mitfuehrungsregel U w = V
  - kappa-alpha1-Kopplung
  - Mediumrotation (C/2)(R/r)^2
- **(c) Gewachsene Gewissheit:**
  - "kappa = 1 erzwungen" gilt nur, wenn Translation und Rotation dasselbe kappa haben.
  - Die LARES-2-Zahl stammt aus einer Sekundaerquelle.
- **Warnzeichen:** Die ~1000 sigma (LARES-2) und ~5e5 sigma (alpha1) wirken eindrucksvoll. Beide beruhen auf nicht selbst
  gelesenem Wortlaut bzw. auf einer PPN-Zuordnung. Tragfaehig und selbst belegt sind GP-B (5,2 sigma), LAGEOS 2016 (~20 sigma)
  und B (3,9 sigma).


  stimmt es in erster Ordnung mit der ART ueberein; eine unterscheidende Vorhersage bleibt nicht.
- Als Dossier-Eintrag erledigt.

- Ende Nachtrag G3: 2026-09-30 07:29:23 CEST (date, nach dem letzten inhaltlichen Schreiben gemessen).

---

## 0. Arbeitsfeld

### 0.1 Offene Rueckfragen

- (keine)

### 0.2 Erwartungsprotokoll (Erwartung vor Abruf, mit date)

| Nr | Zeit (date) | Quelle / Abruf | Erwartung | Ergebnis | Verstoss? |
|---|---|---|---|---|---|

| G2 | 07:10:21 | EHT Sgr A* Paper VI (2022) und Websuche EHT-GR-Tests 09/2024 bis 09/2026 | Schattengroesse Sgr A*: delta = -0,08 +- 0,09 (VLTI) bzw. -0,04 +0,09/-0,10 (Keck); neuere Arbeiten ohne engere Schranke als ~10 % | Bestaetigt: Abstract "within ~10% of the Kerr predictions" [A-W, arXiv:2311.09484 = ApJL 930, L17]; delta-Werte -0,04 (+0,09/-0,10) Keck, -0,08 (+0,09/-0,09) VLTI [S, Suchtreffer-Zitat]; M87* 2018: Ringdurchmesser 43,3 (+1,5/-3,1) uas [S]; keine engere GR-Schranke im Fenster gefunden | nein |
| G3 | 07:10:21 | PPN beta, gamma aktuell (Websuche, 24 Monate) | gamma - 1 = (2,1 +- 2,3)e-5 (Cassini); |beta - 1| ~ 1e-5 bis 1e-4 aus Ephemeriden/MESSENGER | Fienga u. a. (IAU Symp. 364, arXiv:2111.04499): "conservative limits of about 7.16e-5 and 7.49e-5 for beta-1 and gamma-1" [A-W]; nichts Neueres im Fenster gefunden [S] | nein |
| G4 | 07:10:21 | Kramer u. a. 2021 (PRX 11, 041050), Volltext: Zerlegung von omega-dot | omega-dot relativ ~1e-6 gemessen; 2PN- und Lense-Thirring-Anteil ~1e-4 relativ; daraus Traegheitsmoment-Schranke fuer A | Bestaetigt [A, PDF-Text]: omega-dot = 16,899323(13) Grad/Jahr (Tab. IV); omega-dot_2PN ~ 4,39e-4 Grad/Jahr, "about 35 times the measurement error"; omega-dot_LT,A ~ -3,77e-4 x I_A45 Grad/Jahr; I_A ~ 1,15 bis 1,48 (95 %, mit Radiusdaten); aus Timing allein I_A < 3,0e45 g cm^2 (90 %); 3PN ~4e-6 der 2PN-Terme | nein |
| G5 | 07:10:21 | Gravity Probe B (Everitt u. a. 2011) | Frame-Dragging -37,2 +- 7,2 mas/Jahr gegen ART -39,2 | Bestaetigt woertlich: "frame-dragging drift rate of -37.2 +/- 7.2 mas/yr ... GR predictions of ... -39.2 mas/yr"; geodaetisch -6601,8 +- 18,3 gegen -6606,1 [A-W, arXiv:1105.3456] | nein |
| G6 | 07:10:21 | Photonenring-Lyapunov-Exponent: Messaussichten (BHEX, Johnson u. a. 2020) | Schwarzschild gamma = pi je halbem Umlauf; Messung erst mit Weltraum-VLBI (BHEX, Vorschlag) | Bestaetigt: BHEX "is a proposed space-based experiment ... ~30,000 km" (Lupsasca u. a. 2024, arXiv:2406.09498 [A]); n = 1 braucht Weltraumbasislinien; Lyapunov-Exponent mit ~10 % (n = 2) bzw. ~1 % (n = 3) Systematik [S] | nein |
| S1 | 07:13:13 | Websuchen 24 Monate: Fakeon-Phaenomenologie (r-Fenster), Lee-Wick/Kausalitaet beobachtbar, Salvio/agravity, CMB-r-Stand | Fakeon: r ~ 4e-4 bis 3e-3 bleibt die einzige lagertypische Vorhersage; Lee-Wick-Akausalitaet nur auf Skala 1/m2; keine Laborsignatur; CMB r < ~0,03 bis 0,036 (95 %) | Teilweise. **Verstoss:** Es gibt neue lagertypische Signaturen: Aoki/Strumia (arXiv:2510.05204, 10/2025) fuer Lee-Wick-Geister: "opposite-sign scattering amplitudes that violate positivity bounds; acausality on time scales set by their negative decay rate", in der Inflation "opposite-sign non-Gaussianities" [A-W]; Kubo/Kuntz (JCAP 05 (2025) 093): Tensorspektrum um (1 + 2H*^2/m_gh^2)^(-1) unterdrueckt, r = -8 n_t bleibt [A-W]. Fakeon-Fenster 0,4 <~ 1000 r <~ 3,5 [S]. CMB: r < 0,034 (95 %, Planck + SPT + ACT + BK + DESI; Balkenhol u. a., arXiv:2512.10613), dort auch: BAO verschiebt n_s nach oben und setzt Starobinsky unter Druck [A-W]. Donoghue/Menezes im Fenster: kein Treffer (juengste gefundene PRL 133 (2024), 03/2024) [S] | ja (V-S1) |

| S2 | 07:17:47 | Websuche: statisches Potential unter der Fakeon-/Lee-Wick-Vorschrift | Die Arbeiten sagen, das statische (Newton-)Potential ist dasselbe Yukawa wie bei Stelle; die Vorschrift wirkt nur on-shell | Teilweise: Der klassische Grenzfall der Fakeons ist der Mittelwert aus retardiertem und avanciertem Potential [S]. Bei statischer Quelle sind beide gleich, das Yukawa bleibt [ES]. **Zusatz** (Anselmi, CQG 36 (2019) 065010, arXiv:1809.05037): "violation of microcausality, which survives the classical limit"; Bewegungsgleichung "<F> = ma, where <F> is an average that includes a little bit of 'future'" [A-W] | teilweise (Zusatz: klassische Akausalitaet) |

**Z6 (ST-2, vier Lager gegen Messsignaturen):**

| Lager | Kernaussage | lagertypische Signatur | bei welcher Masse sichtbar? | Laborsignatur |
|---|---|---|---|---|
| 1 Instabile Lee-Wick-Resonanz (Donoghue/Menezes 2019 bis 2024; Buoninfante 2025/2026; Aoki/Strumia 2025) | Geist zerfaellt mit negativer Breite; Pole im ersten Blatt; kein freies asymptotisches Geistteilchen | Streuamplituden mit "falschem" Vorzeichen (Positivitaetsverletzung); Akausalitaet auf der Zeitskala 1/|Gamma|; schmalere Resonanzen mit schwaecherer Interferenz; Inflation: Nicht-Gaussizitaet mit umgekehrtem Vorzeichen, IR-verstaerktes Spektrum | Streuung erst bei sqrt(s) >= m2; Inflationssignale nur fuer m2 ~ H_inf | nur das statische Yukawa (-4/3), siehe Z7 |
| 2 Stabiler komplexer Geist mit Unitaritaetsbruch (Kubo/Kugo 2023/2024; Kubo/Kuntz 2025) | komplexe Geister entstehen paarweise aus physikalischen Stoessen | Wahrscheinlichkeitsverlust oberhalb 2 Re(m); Tensorspektrum unterdrueckt um (1 + 2H^2/m_gh^2)^(-1) | fuer m_gh <~ H_inf in der Kosmologie | nur das statische Yukawa |
| 3 Fakeon (Anselmi; Anselmi/Bianchi/Piva 2020; Anselmi 2025/2026) | rein virtuell, unitaer, Mikrokausalitaet auf ~1/m_chi aufgegeben | r-Fenster 4/3 < N^2 r < 12 mit m_chi > m_phi/4 (Starobinsky-Inflation) | m_chi ~ Inflationsskala | keine (m_chi weit ueber Labormassen); statisches Yukawa nur, falls m_chi doch klein waere |
| 4 "Dualer invertierter Oszillator" ohne Geist (Kumar/Marto 2026) | Spektraldichte null, Hauptwert-Propagator, nur virtuelle Beitraege | im Abstract keine genannt [A]; auf Baumniveau wie Fakeon | - | nur das statische Yukawa |
| (lageruebergreifend: klassische Loesungen) | 2-2-Loecher (Holdom/Ren), "powerballs" (Liu/Quintin/Afshordi 2025) | GW-Echos, horizontlose kompakte Objekte | Starkfeld, unabhaengig von der Vorschrift | keine |

**Z7 (ST-2, Groessenordnungen fuer eine Laborsignatur, [E]/[ES]):**
- Statisches Potential (alle Lager gleich, [ES] aus Runde 8): -4/3 exp(-r/lambda2) + 1/3 exp(-r/lambda0). Heute m2 >~ 5 bis
  8 meV (ST-1-R); ein Nachweis braucht |alpha| ~ 1 bei lambda ~ 20 um, also rund 20-mal empfindlicher (ST-1).
- **Positivitaet im Labor [ES]:** Das "falsche Vorzeichen" der Amplitude (Lager 1) ist im statischen Grenzfall genau das negative
  Vorzeichen des Yukawa-Terms. Ein gesunder massiver Spin-2-Zustand gaebe +4/3, der Geist gibt -4/3. Die Torsionswaage misst also
  schon heute im meV-Bereich die Positivitaet eines Spin-2-Pols, aber nicht, welches Lager recht hat.
- **Akausalitaet [E, grob]:** Zeitskala hbar/m2 = 6,58e-16 eV s / 5e-3 eV = 1,3e-13 s, Laenge hbar c/m2 ~ 40 um.
  - Gravitative Zerfallsbreite Gamma ~ m2^3/M_Pl^2 = (5e-3 eV)^3/(1,22e28 eV)^2 ~ 8e-64 eV.
  - Kraefte zwischen mg-Massen auf 40 um ~ G m^2/r^2 ~ 4e-14 N.
  - Eine zeitaufgeloeste Messung der Gravitation im Pikosekundenbereich zwischen solchen Massen ist nicht in Sicht.
- **Streuung:** Graviton-Austausch bei sqrt(s) ~ m2: Amplitude ~ s/M_Pl^2 ~ (5e-3/1,22e28)^2 ~ 2e-61. Unmessbar.
- **Kosmologie** ist der einzige Ort mit lagertypischen Signaturen, und nur fuer m2 ~ H_inf:
  - Fakeon: r ~ 3,7e-4 bis 3,3e-3 (N = 60 [E]) gegen heute r < 0,034; LiteBIRD soll delta r < 0,001 erreichen [S]. Der obere
    Teil des Fensters ist also pruefbar.
  - Lee-Wick: Vorzeichen der Nicht-Gaussizitaet.
  - Komplexer Geist: Unterdrueckung von A_t.
- **[ES] Regel 6:** Akausalitaet, Unitaritaets- bzw. Positivitaetsverletzung und das negative Yukawa-Vorzeichen sind drei Wege zu
  **einer** Groesse, dem Vorzeichen (der Norm) des Residuums am Spin-2-Pol. Die Lager streiten nicht ueber dieses Vorzeichen, sondern
  darueber, wie man es quantisiert.

**Z3 (G2, Photonensphaere und Schatten in beiden Lesarten, [E]):**
- Winkelparametrisierte Wirkung F~(r, r') mit r' = dr/dphi (c0 = 1):
  - R1: F~ = sqrt(r'^2/(1 - u)^2 + r^2/(1 - u))
  - R2: F~ = (r'^2 + r^2)/sqrt((1 - u) r^2 + (1 - u)^2 r'^2)
  - beide: F~0(r) = F~(r, 0) = r (1 - u)^(-1/2)
- Kreisbahn: dF~0/dr = 0, also r0 = 1,5 rs in beiden Lesarten; kritischer Stossparameter b = F~0(r0) = 1,5 sqrt(3) rs =
  3 sqrt(3) GM/c^2. **Schattenradius gleich Schwarzschild, in R1 und R2.**
- Instabilitaet: Entwicklung F~ ~ F~0 + (1/2) K r'^2, Wachstum je Radiant lambda = sqrt(F~0''/K); F~0''(r0) = F~0 (ln F~0)''
  = 2,598 x 4/3 = 3,464 (rs = 1).
  - R1: K = 1/(r (1 - u)^(3/2)) = 3,464, also lambda = 1 und je halbem Umlauf gamma = pi. **Probe: Schwarzschild-Wert
    getroffen.**
  - R2: K = (1 + u)/(r (1 - u)^(1/2)) = 1,925, also lambda = sqrt(1,8) = 1,342 und gamma = 1,342 pi = 4,21.
  - Helligkeitsverhaeltnis aufeinanderfolgender Unterringe e^(-gamma): R1 0,0432, R2 0,0148, also ~2,9-mal schwaecher [H].

**Z4 (G2, Lichtablenkung zweiter Ordnung, [E]):**
- R2 - R1 im Index: delta n = -(1/2) u^2 cos^2 theta sin^2 theta; entlang der geraden Bahn (cos theta = x/r, sin theta = b/r):
  delta S = -(rs^2 b^2/2) Int x^2/(x^2 + b^2)^3 dx = -pi rs^2/(16 b).
- delta alpha = -d(delta S)/db = -pi rs^2/(16 b^2) = -(pi/4)(M/b)^2 (Kreuzterme erster Ordnung sind in beiden Lesarten gleich).
- ART zweite Ordnung: (15 pi/4)(M/b)^2 [L]. R2 gibt also (7 pi/2)(M/b)^2, rund 6,7 % weniger.
- Sonnenrand: (M/b)^2 = (1,4766 km/6,957e5 km)^2 = 4,50e-12; ART-Term 10,9 uas, Unterschied -0,73 uas [E].

**Z5 (G2, Zusatzannahme "Random Walk in zweiter Ordnung", [E]/[H]):**
  angepasst, C.7) [A].
  lichtartigen Teilchen, 6.1 [A]).
  - Dann g_00 = -(1 - u - kappa u^2), g_rr = 1/(1 - u - kappa u^2).
  - In Weinbergs Standardform: gamma = 1, beta - gamma = -2 kappa, also beta = 1 - 2 kappa.
  - Schatten: b^2 = rs^2/h(u) mit h = u^2 (1 - u - kappa u^2), Maximum bei u ~ 2/3 - 16 kappa/27; delta b/b = (2/3) kappa.
- Ephemeriden |beta - 1| < 7,2e-5 [A-W] geben |kappa| < 3,6e-5, also delta b/b < 2,4e-5; das EHT (~10 %) sieht davon nichts.
  Nur Terme ab u^3, die das Sonnensystem nicht spuert, koennten an der Photonensphaere (u = 2/3) etwas ausmachen.

### 0.3 Zwischenbefunde

- Hauptrichtungen (A.4, 2.1): c_r = c0 (1 - u), c_t = c0 (1 - u)^(1/2), u = rs/r.
- Massstaebe (6.2, B.6, C.8): radial Faktor (1 - u)^(1/2), tangential Exponent p - 1/2 = 0, also unveraendert. Damit ist r der
  Umfangsradius (Flaechenradius) [ES].
- Uhren (B.9, B.10): dtau/dt = c_t/c0 in Ruhe.
- Zusammen [E]: g_00 = -(c_t/c0)^2 = -(1 - u), g_rr = (c_t/c_r)^2 = (1 - u)^(-1), g_Omega = r^2. Das ist die
  Schwarzschild-Metrik in Standardkoordinaten, exakt, nicht nur in erster Ordnung.
- PPN [E, L: Weinberg-Standardform A = 1 - 2M/r + 2(beta - gamma)(M/r)^2, B = 1 + 2 gamma M/r]: A hat keinen M^2-Term,
  B = 1 + 2M/r + ... Also gamma = 1 und beta = 1.
  anisotroper Index n_r = (1 - u)^(-1), n_t = (1 - u)^(-1/2) im Flaechenradius ist dieselbe Riemannsche optische Metrik in
  anderen Koordinaten, **wenn** schraege Strahlen der Ellipsenregel folgen (Z2).

**Z2 (G2, zwei Lesarten der Richtungsregel A.5 bis A.7, [E]):**
  (cos theta = sin(vartheta) in seiner Notation); Betrag c^2 = c_r^2 cos^2 theta + c_t^2 sin^2 theta.
- **R1 (geometrisch folgerichtig):** Die Menge dieser Vektoren ist eine Ellipse mit Halbachsen c_r und c_t, also die
  Strahlflaeche. Die Richtung des Vektors ist tan theta' = (c_t/c_r) tan theta. Misst man den Betrag entlang der
  tatsaechlichen Richtung theta', gilt 1/v^2 = cos^2 theta'/c_r^2 + sin^2 theta'/c_t^2: die optische Metrik von
  Schwarzschild, exakt.
- **R2 (woertlich, wie in A.7 benutzt):** Der Betrag wird der unverdrehten Richtung theta zugeordnet:
  v^2/c0^2 = 1 - u (1 + cos^2 theta) + u^2 cos^2 theta.
  - Die Ellipse gibt v^2/c0^2 = (1 - u)^2/(1 - u sin^2 theta) = 1 - u (1 + cos^2 theta) + u^2 cos^4 theta + O(u^3).
  - Unterschied R2 - R1 = u^2 cos^2 theta sin^2 theta: null fuer rein radiale oder rein tangentiale Strahlen, sonst von
    zweiter Ordnung.
  - R2 ist eine Finsler-, keine Riemann-Metrik: F = (dr^2 + r^2 dphi^2)/(c0 sqrt((1 - u)^2 dr^2 + (1 - u) r^2 dphi^2)).
  seinem Text vertraeglich.
