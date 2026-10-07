# ARBEITSFELD GEGENLESEN-R45 (frischer Leser)

- Beginn 2026-10-05 04:57:00 CEST (date). Zeitbox 90 min. GEGENLESEN.md abgeschlossen 2026-10-05 05:31:43 CEST (date).
- Hier stehen eigene Zwischenrechnungen und vor jedem Abruf die Erwartung mit date-Zeit, danach der Ausgang.
- Abrufzaehler: 7 von 8 (Endstand; F1 und F7 mit Inhalt, F2 bis F6 ohne, F8 ungenutzt).

## Eigene Herleitungen (vor dem Vergleich mit dem Dossier)

### A. Paar-Photon (ab 04:58, Kopfrechnung, [M])

- Quelle fuer den Bau: lokale Kopie paar-licht-l/quellen/R3-...-layout.txt (kein Abruf), Gl. (12), (20), (32)-(36), (43), (44), Abschn. VI.
- **A1 Kommutator selbst:** Fuer zwei verschiedene Fermionsorten a, c gilt [ac, (ac)^+] = (1 - n_a)(1 - n_c) - n_a n_c = 1 - n_a - n_c.
  Fuer gamma(k) = sum_q f(q) phi(k/2-q) psi(k/2+q) und k = k' fallen die Glieder q != q' weg (vier verschiedene Moden,
  gerade Anzahl Vertauschungen). Also [gamma(k), gamma^+(k)] = 1 - sum_q |f|^2 (n_phi(k/2-q) + n_psi(k/2+q)).
  Das deckt sich mit Bisio Gl. (34) (Diagonalteil) und (36) (geformte Zahloperatoren). **Wichtig:** <Gamma> zaehlt alle
  psi-Fermionen im Traeger, auch die anderer Photonmoden ("M = Fermionen in Omega_k", Abschn. V). Der Fremdmoden-Term
  steckt also schon in Bisios Kriterium; Gl. (34) enthaelt dazu die Nichtdiagonalglieder k != k' ausdruecklich.
- **A2 Zaehlung Breitband:** psi-Modus p erhaelt Beitraege von allen Photonmoden k' mit p - k'/2 in Omega. Die Menge
  {p - k'/2} ist ein Gitter mit halbem Abstand (pi/L statt 2 pi/L), also 2^3 = 8 mal so dicht: 8 N Photonmoden, je
  Gewicht n * (1/N). Summe 8 n. Gegenprobe ueber Teilchenzahl: Photonen im k-Gebiet V_k: n V_k (L/2pi)^3; ihre
  psi-Bausteine liegen bei p ~ k/2 im Gebiet V_k/8, dort (V_k/8)(L/2pi)^3 Moden; Besetzung n V_k/(V_k/8) = 8 n. Das gilt
  fuer jedes f mit Traeger |q| < qbar, solange n auf der Skala 2 qbar glatt ist.
  - Polarisation: Im Helizitaetsbasis-Bild (Spin laengs n_{k/2}) ist phi^T sigma_+ psi = phi_up psi_down und
    phi^T sigma_- psi = phi_down psi_up; die zwei Querzustaende benutzen je eine psi-Komponente. Bei Besetzung n in beiden
    Querpolarisationen also 8 n je psi-Komponente (bzw. je phi-Komponente). [Nachtrag 05:31: Eine einzelne
    Linearpolarisation (u^1.sigma = sigma_x) belegt beide Komponenten je zur Haelfte, dann 4 n je Komponente;
    unpolarisiert bzw. zirkular bleibt es 8 n.] Der Diagonalteil der Abweichung ist die Summe
    beider Sorten, also 16 n. Pauli-Schranke: 8 n <= 1, also n <= 1/8 je Polarisation als harte Grenze (Fock-Vakuum,
    Bau aus zwei Vernichtern).
- **A3 Schmalband:** N_ph = Delta k^3 (L/2pi)^3 Photonmoden mit je n, alle Traeger ueberlappen (Delta k << qbar):
  Besetzung n N_ph/N = n Delta k^3 / ((4 pi/3) qbar^3), also n (Delta k/qbar)^3 bis auf einen Formfaktor O(1)
  (hier 1/4,19 fuer Wuerfel der Kante Delta k gegen Kugel vom Radius qbar). Obergrenze 8 n (Breitbandfall). Als
  Dichte: rho_ph < qbar^3/(6 pi^2) < k^3/(6 pi^2); optisch k = 2 pi/600 nm = 1,05e5/cm, k^3 = 1,16e15, /59,2 = 1,96e13/cm^3.
- **A4 Verschmierung:** Paar (k/2 + q, k/2 - q), beide mit Tempo c. Schwerpunkttempo = c |n1 + n2|/2 = c cos(theta/2).
  Fuer q quer: tan(theta/2) = q/(k/2) = 2 eps, cos = 1/sqrt(1 + 4 eps^2) = 1 - 2 eps^2. Allgemein 1 - 2 q_perp^2/k^2
  (Laengsanteil von q kostet in dieser Ordnung nichts). Fuer isotrope Verschmierung kleiner: Kugelschale <q_perp^2> =
  (2/3) qbar^2 gibt (4/3) eps^2, Vollkugel (2/5) qbar^2 gibt (4/5) eps^2. Energieunabhaengig nur, wenn qbar proportional
  zu k ist. Achtung: Die "Dispersion" omega(k) = c k sqrt(1 + 4 eps^2) bei festem eps gaebe ein Tempo > c; massgeblich
  ist das Gruppentempo bei festem q (Bausteinmittel), also langsamer. 2 eps^2 < 1e-14 gibt eps^2 < 5e-15, eps < 7,07e-8.
- **A5 Cherenkov Weyl-QCA:** Eigenphase cos lambda = c_x c_y c_z +- s_x s_y s_z mit u = k/sqrt3 (Dossier-Konvention):
  lambda ~ sqrt(u^2 +- 2 u_x u_y u_z) = |u| +- |u|^2 n_x n_y n_z. Elektron (Dirac, erbt das Glied): Tempo
  1 +- 2 p nnn; Photon omega(p) = 2 lambda(p/2) = p +- p^2 nnn/2, Tempo 1 +- p nnn. Max |nnn| = 1/(3 sqrt3) = 0,192.
  Schwelle (weiches Photon, Tempo 1): 2 a1 p = m^2/(2 p^2), also p^3 = m^2 E_P/(4 a1) mit a1 = Phasenkoeffizient;
  mit a1 als Tempokoeffizient p^3 = m^2 E_P/(2 a1). Zahlen: m_e^2 = (0,511e-3)^2 = 2,61e-7 GeV^2, mal E_P = 1,22e19:
  3,19e12 GeV^3. /0,385 = 8,28e12, Kubikwurzel 2,02e4 GeV; /0,77 = 4,14e12, Kubikwurzel 1,61e4 GeV. Also 1,6e4 bis
  2,0e4 GeV, Dossierzahl "~2e4 GeV" haelt in der Groessenordnung; die Formel mit "2|a1|" gilt, wenn a1 der Tempo-
  koeffizient ist, mit dem Phasenkoeffizienten steht 4|a1|.
- **A6 Gl. (44)-Faktor (nur Beiprobe):** Photon c = 1 +- (|k|/sqrt3) nnn = 1 +- kx ky kz/(sqrt3 |k|^2); laengs 111:
  1 +- |k|/9. Bisio 1 +- 3 kx ky kz/|k|^2 = 1 +- |k|/sqrt3 laengs 111. Verhaeltnis (1/sqrt3)/(1/9) = 9/sqrt3 = 3 sqrt3
  = 5,196. Unter der Dossier-Konvention stimmt die Dossier-Nachrechnung; ob Bisios Gl. (7) dieselbe Konvention hat, habe
  ich nicht nachgeprueft (nur A_k = exp(-i n_k . sigma) gesehen).
- **A7 10^90:** l_P^3 = 1,616^3 e-99 = 4,22e-99 cm^3; 1e-15/4,22e-99 = 2,37e83. Selbst mit Impulsmoden bis pi/l_P:
  (pi/6) * 2,37e83 = 1,2e83. Die 10^90 sind so nicht nachvollziehbar; 2,4e83 haelt. Optisches N_k in 1e-15 cm^3:
  1,16e15 * 1e-15/59,2 = 0,0196 haelt. Der Laser der Quelle (6e23 Photonen in 1e-15 cm^3 = 6e38/cm^3) laege um
  6e38/1,96e13 = 3e25 ueber der Pauli-Grenze, gleich welches qbar < k.

### B. PT-AUSGLEICH-L (ab 05:08, [M]; Bezeichnungen aus spiegel-haelfte-1/PLAN.md Z. 13-15, 58-63)

- Rahmen: h_a Tetraeder, n_a.n_b = -1/3; P_2 = V^+V, <a|P_2|b> = (1/2)<n_a|n_b>, Diagonale 1/2, Nebenbetrag
  (1/2) sqrt((1 + n_a.n_b)/2) = (1/2) sqrt(1/3) = 1/sqrt12. Gamma := P_2 - P_2' = 2 P_2 - 1 (Diagonale 0, Nebenbetrag 1/sqrt3).
- **S4(a):** G und C sind Funktionen von P_2, vertauschen; S_+(0) = 1. U_gamma(0) = e^{i alpha - gamma} P_2 +
  e^{i beta + gamma} P_2'. Betraege e^{-+gamma}. Haelt. Grenze des Satzes: gilt fuer Gewinn/Verlust zwischen den Haelften
  (G vertauscht mit P_2). Gewinn/Verlust auf einzelnen Verschiebungskomponenten (G diagonal in |a>) faellt nicht darunter;
  dort koppelt C = 2 P_2 - 1 (fuer 0, pi) alle Komponenten schon bei k = 0. Das Dossier behauptet nur den ersten Fall.
- **S4(b):** Bargmann: Tr(P_a P_b P_c) = (1/4)[1 + a.b + b.c + c.a + i a.(b x c)]; Realteil 1 - 3/3 = 0; Tripelprodukt
  (1,1,1).((1,-1,-1) x (-1,1,-1))/(3 sqrt3) = (1,1,1).(2,2,0)/(3 sqrt3) = 4/(3 sqrt3), also Tr = i/(3 sqrt3), rein
  imaginaer. Damit -B = B*, D mit D P_2* D^+ = P_2' existiert. Haelt.
  - Konvention: Mit Konjugation bei festem k (K_k, entspricht D P K im Ortsraum) gilt Theta S_+(k) Theta^-1 = S_+(k)^-1;
    dann Theta U Theta^-1 = (e^{-i alpha} P_2' + e^{-i beta} P_2) S_+^-1, gleich U^-1 genau fuer alpha = beta (bei k = 0
    zwingend). Im Projektfall (0, pi) gibt dieselbe Abbildung -C S_+^-1 = -C U^-1 C^-1, also (C Theta) U (C Theta)^-1 = -U^-1.
    Mit reellem K im Ortsraum (k -> -k, K S_+ K = S_+) gilt dagegen Theta U Theta^-1 = -U (Dossier), aber dann ist auch fuer
    alpha = beta Theta U Theta^-1 = e^{-i alpha} S_+ != U^-1. **Das Dossier nutzt in (b) zwei verschiedene Theta.**
    Folge unveraendert: -U^-1 paart lambda mit -1/lambda* (nie Theta-invariant, |lambda|^2 = -1 unmoeglich), -U paart
    lambda mit -lambda*; beide erzwingen keine Unimodularitaet.
  - Staerker als das Dossier: Keine Haelften tauschende antiunitaere Abbildung leistet PT fuer (0, pi): Theta'' = X Theta
    mit X vertauscht mit P_2, also mit C; bei k = 0 verlangt PT -X C X^-1 = C, also -C = C. Widerspruch.
- **S4(c):** alpha = beta: G^{1/2} ~ 1 - (gamma/2) Gamma. Nicht entartet: delta ln lambda_a = -gamma <a|Gamma|a> = 0, und
  |a> ist Theta-invariant (bis auf Phase), also geschuetzt. Entartet (k.(h_a - h_b) in 2 pi Z): 2 x 2-Block mit
  Nebenelement Betrag 1/sqrt3, Verschiebungen +-gamma/sqrt3. Haelt. Streifenbreite aus H_eff = [[d/2, -i g gamma],
  [-i g gamma, -d/2]], E = +-sqrt(d^2/4 - g^2 gamma^2): gebrochen fuer |d| < 2 gamma/sqrt3 (d Phasenabstand der zwei
  Baender). Probe bei k = 0 (alle vier entartet): Gamma hat Eigenwerte +-1, also +-gamma, stimmt mit S4(a).
- **S4(d):** U_gamma ~ U - (gamma/2)(Gamma U + U Gamma); fuer normales U ist u_j^+ U = lambda_j u_j^+, also
  delta lambda_j = -gamma lambda_j <Gamma>_j, delta ln|lambda_j| = -gamma (w_j - (1 - w_j)) = -gamma (2 w_j - 1). Haelt.
- **S5:** psi_2(t) = R Lambda^t c, c = R^-1 psi_2(0). M^+ eta M = R^-+ Lambda^+ R^+ (R R^+)^-1 R Lambda R^-1 = R^-+ R^-1 = eta.
  psi_2^+ eta psi_2 = c^+ R^+ (R R^+)^-1 R c = c^+ c = ||psi||^2. R R^+ = sum_j a_j a_j^+ = P_2 Pi_alpha P_2 <= P_2, also
  eta >= 1 auf Ran P_2. Haelt, **aber nur fuer Zustaende in den alpha-Baendern** (so in 3.3). Fuer einen rein sichtbaren
  Anfangszustand (Projektlauf: P_2 psi_0 = psi_0) ist die sichtbare Dynamik die Kompression P_2 U^t P_2 mit vier Baendern
  in zwei Dimensionen, keine Halbgruppe M^t; pseudo-unitaer nur bis auf den beta-Anteil O(k^2). Abschnitt 1 Punkt 2 laesst
  die Einschraenkung weg.
- **S3:** (|lambda|^2 - 1) v^+ eta v = 0 mit |lambda|^2 = 1 - (2/9) k^2 < 1 fuer k != 0. Haelt.
- **S2 (Beiprobe):** sigma = 8: 9 sigma^2 = 576, 100/576 = 0,1736, 1,1736^-1,5 = e^{-1,5 * 0,1601} = 0,787. sigma = 4:
  1,6944^-1,5 = e^{-0,791} = 0,453. Haelt.
- **S6 (Beiprobe):** 0,4937 + 0,2237 = 0,7174 stimmt. w_2 - N_FJ = 0,7174 - 0,496 = 0,2214; Abschnitt 1 nennt 0,222,
  ARBEITSFELD S6 0,221 (Rundung bzw. anderer N_FJ-Wert; unkritisch). Rueckgabequote 0,2214/0,504 = 0,439, also 44 %.

## Abrufprotokoll

### F1: arxiv.org/abs/1407.6928 (WebFetch), Fassungen und Zeitschriftenangabe [Teil A, (a)]
- Erwartung 2026-10-05 05:04:34 CEST (date), vor dem Abruf: Es gibt eine spaetere Fassung v2 oder v3 (2016) mit
  Journal-Ref Ann. Phys. 368 (55 %). Der Kommentar nennt keine inhaltliche Berichtigung (70 %).

### F2: export.arxiv.org/api/query, Folgearbeiten D'Ariano/Perinotti/Bisio zu Photon, Maxwell, Elektrodynamik [Teil A, (a)]
- Erwartung 2026-10-05 05:04:34 CEST (date), vor dem Abruf: Mindestens ein Uebersichtsartikel (etwa D'Ariano/Perinotti,
  Front. Phys. 2017) fasst den Paarbau zusammen (65 %). Kein Abstract nennt eine Saettigungs- oder Statistik-
  Berichtigung (80 %).
- Ausgang F1 (05:05:13): nur v1 (25.07.2014) auf arXiv, keine spaetere Fassung; Journal-Ref Ann. Phys. 368 (2016)
  177-190, doi 10.1016/j.aop.2016.02.009. Erste Erwartung (v2/v3) **verfehlt**; Kommentar ohne Berichtigung **eingetroffen**.
  Folge: Die Zeitschriftenfassung ist ueber arXiv nicht frei; ob sie Gl. (44) oder die 10^90 aendert, bleibt offen.
  Kopie: quellen/F1-arxiv-abs-1407.6928-20261005-0505.txt (WebFetch-Auszug).
- Ausgang F2 (05:05:13): HTTP 429 (zu viele Anfragen; F1 und F2 liefen gleichzeitig). Abruf verbraucht, kein Inhalt.
  Selbstanzeige: parallele Abrufe gegen die arXiv-Taktregel. Weitere Abrufe nur nacheinander.
- Zaehler: 2 von 8.

### F3: export.arxiv.org/api/query, Komposit-Bosonen mit vielen Moden bzw. thermisch [Teil A, (b)]
- Erwartung 2026-10-05 05:05:45 CEST (date), vor dem Abruf: Treffer zu Combescot (Pauli-Streuung zwischen verschiedenen
  Komposit-Zustaenden) bzw. Tichy/Bouvrie/Molmer oder Kurzynski u. a. (zwei Komposite in verschiedenen Zustaenden) (70 %).
  Ein Abstract nennt Phasenraumfuellung bzw. Dichte mal Kompositvolumen als Parameter (60 %). Keine Quelle zeigt eine
  Aufhebung des Fremdmoden-Terms fuer Paare aus zwei Teilchen mit leerem Vakuum (85 %).
- Ausgang F3: Zeitueberschreitung (60 s), kein Inhalt. Als verbraucht gezaehlt (streng). Zaehler: 3 von 8.

### F4: wie F3, einfachere Abfrage (max_results=15) [Teil A, (b)]
- Erwartung wie F3 (unveraendert), eingetragen vor dem Abruf; Zeit siehe naechste date-Zeile im Ausgang.
- Ausgang F4 (05:08:20): wieder HTTP 429. Verbraucht. Zaehler: 4 von 8. Die arXiv-API sperrt das Werkzeug derzeit;
  arxiv.org/abs ging (F1). Plan: Teil B vorziehen, API spaeter genau einmal je Frage (b), (c) neu versuchen.

### Lokal, ohne Abruf (Quellenkopien des Autors, paar-licht-l/quellen/, nur gelesen), 05:06 bis 05:08
- Bisio Lit. [S]: [35] Jordan, Z. Phys. 93, 464 (1935); [36] Kronig, Physica 3, 1120 (1936); [39] Pryce, Proc. R. Soc. A
  165, 247 (1938); [40] Chudzicki/Oke/Wootters PRL 104, 070402 (2010); [42] Combescot/Tanguy EPL 55, 390 (2001);
  [43] Rombouts u. a. MPLA 17, 1899 (2002); [44] Avancini/Marinelli/Krein J. Phys. A 36, 9045 (2003); [45] Combescot/
  Leyronas/Tanguy EPJ B 31, 17 (2003); [46] Law PRA 71, 034306 (2005).
- Bisio Abschn. V [S]: Kriterium Tr[rho Gamma] <= eps mit M = "number of psi Fermions in the region Omega_k", also alle
  Fermionen im Traeger, gleich zu welchem Photon sie gehoeren. Gl. (34) enthaelt Nichtdiagonalglieder k != k'. Gl. (41):
  Kreuzkommutator zweier verschiedener Komposite |<N|[c1, c2^+]|N>| <= 2 N P (Vermutung aus [40] bewiesen).
- Perkins Gl. (41)-(50) [S]: Lipkin-Naeherung je Photonmodus mit eigenem Omega(p, p) = (3/(8 pi))^(3/2) V/lambda^3
  (Impulsbreite k0 ~ hbar/lambda); Coblentz 125 cm^3: 1/Omega <= 1e-9. Jeder Modus hat sein eigenes Omega; dass die
  Bausteine der Nachbarmoden dieselben Zustaende fuellen, kommt nicht vor. Das bestaetigt V1 des Dossiers fuer Perkins.
  Nachrechnung: lambda = 1 um: V/lambda^3 = 125/1e-12 = 1,25e14; (3/8pi)^1,5 = 0,119^1,5 = 0,041; Omega ~ 5e12.
  Bei 1 bis 6,5 um und ~1600 K ist n von 1e-4 bis 0,33 (hnu/kT = 9,0 bzw. 1,39); 8 n reicht bis 2,7 > 1. Schon Coblentz
  laege damit ueber der Pauli-Grenze des 3D-Paarbaus [M]. (Perkins' Text nennt "15960 K"; bei dieser Temperatur waere
  n bei 1 um 0,68, 8 n = 5,5.)

### F5: export.arxiv.org/api/query, abs:"neutrino theory of light" [Teil A, (c)]
- Erwartung 2026-10-05 05:16:29 CEST (date), vor dem Abruf: 3 bis 10 Treffer (Perkins, Dvoeglazov o. ae.) (60 %).
  Mindestens ein Abstract nennt Pryce bzw. das Querheits-/Drehproblem (40 %). Mindestens ein Abstract nennt Jordans Bau
  als exakt bosonisch nur fuer kollineare Neutrinos (35 %). Risiko: erneut HTTP 429 (40 %).
- Ausgang F5 (05:17): HTTP 429. Verbraucht. Zaehler: 5 von 8. Risiko eingetreten. Naechster API-Versuch fruehestens
  05:30, dann als eine kombinierte Abfrage fuer (b) und (c); bei erneutem 429 keine weiteren API-Versuche.

### F6: export.arxiv.org/api/query, kombiniert: abs:"neutrino theory of light" OR (abs:"composite bosons" AND abs:Pauli) [Teil A, (b) und (c)]
- Erwartung 2026-10-05 05:22:47 CEST (date), vor dem Abruf: erneut HTTP 429 (55 %). Falls Inhalt: Combescot-Treffer
  mit "Pauli scattering" zwischen verschiedenen Komposit-Zustaenden (65 %); kein Treffer zeigt eine Aufhebung fuer Paare
  aus zwei Teilchen (85 %); ein Abstract zur Neutrinotheorie nennt Pryce (40 %).
- Ausgang F6 (05:24:01): HTTP 429. Verbraucht. Zaehler: 6 von 8. Erste Erwartung eingetroffen, die uebrigen nicht
  pruefbar. **Keine weiteren Abrufe:** arXiv-IDs zu Combescot, Chudzicki/Oke/Wootters, Law, Pryce kenne ich nicht sicher;
  geratene IDs oder DOIs (Royal Society, Elsevier mit Umleitungskette) wuerden die zwei Restabrufe mit geringer
  Trefferaussicht verbrauchen. 2 Abrufe bleiben ungenutzt.
- Ersatz fuer (b) aus vorhandenen Quellen [S, lokale Kopie]: Bisio Abschn. V und V.A: Kriterium Tr[rho Gamma] <= eps
  mit M = alle psi-Fermionen im Traeger Omega_k; Gl. (34) mit k != k'; Gl. (41) Kreuzkommutator zweier verschiedener
  Komposite; "even in the case of several composite Bosons, the amount of entanglement for each pair is a good measure"
  (Abschn. VII). Das Kriterium enthaelt den Fremdmoden-Term; ausgewertet wird es in der Quelle nur fuer einen Modus.

### F7: arxiv.org/pdf/1608.02004 (WebFetch) [Teil A, (a) Folgearbeiten]
- Erwartung 2026-10-05 05:26:21 CEST (date), vor dem Abruf (Entscheidung umgestellt: eine ID, die ich mit ~60 % fuer
  D'Ariano/Perinotti, "Quantum cellular automata and free quantum field theory", Front. Phys. 2017, halte):
  - Die ID trifft diese Uebersicht (60 %).
  - Falls ja: Sie fasst den Paarbau des Photons zusammen (70 %), nennt die Saettigung nur qualitativ oder gar nicht
    (65 %), wiederholt die 10^90 nicht (70 %) und gibt fuer das Lichttempo dieselbe Form wie Gl. (44) oder keine Formel
    (60 %).
- Ausgang F7 (05:27:25): WebFetch konnte die PDF nicht lesen, legte die Binaerdatei aber im Werkzeugordner ab
  (sha256 570d2df2...). Kopie nach quellen/F7-dariano-perinotti-1608.02004v1-20261005-0527.pdf, gelesen mit pdftotext
  nach stdout. Zaehler: 7 von 8.
  - ID trifft: D'Ariano, Perinotti, "Quantum cellular automata and free quantum field theory", arXiv:1608.02004v1,
    5.8.2016 [S Titelseite]. **eingetroffen.**
  - Abschn. VII fasst Bisio u. a. (Ref. [4] = Ann. Phys. 368, 177 (2016)) zusammen: Photon als "entangled pair of
    Fermions", F^i(k) wie Bisio Gl. (12), aber nur zwei Querpolarisationen gamma^i, i = 1, 2 (Gl. (41), (42)).
    Kriterium woertlich: "M_phi,k (resp. M_psi,k) the mean number of type phi (resp psi) Fermionic excitations in the
    region Omega_k ... for states such that M_xi,k/N_k <= eps for all xi = phi, psi and k and for eps << 1 we can safely
    assume [gamma^i(k), gamma^j(k')^+] = delta delta". **eingetroffen** (Paarbau zusammengefasst).
  - Keine Saettigungsabschaetzung, kein "10^90", kein Laser, keine Planck-Verteilung, keine Formel fuer das Lichttempo
    (grep: "superluminal", "speed of light" nur in der Einleitung). **eingetroffen** (nicht wiederholt; keine Formel).
  - Konvention: "c_i := cos(k_i/sqrt3), s_i := sin(k_i/sqrt3)" (Z. 792; das Wurzelzeichen fehlt im pdftotext, wie bei
    "k_i/sqrt2" fuer d = 2), "omega_k^+- = arccos(c_x c_y c_z -+ s_x s_y s_z)" (Z. 800). Das ist genau die Konvention der
    Dossier-Nachrechnung. Mit den naheliegenden Variablen (Gitter-k: Vorfaktor 1/sqrt3; p = k/sqrt3 in Planck-Einheiten:
    Vorfaktor 1; andere Konvention cos k_i mit Gitter-k: Vorfaktor 1) erreicht keine den Vorfaktor 3 von Gl. (44);
    dafuer braeuchte es k' = p/3, eine Variable ohne erkennbare Bedeutung. [Korrigiert 05:29: zuerst stand hier
    absolut "mit keiner Skalierung" und "Faktor 9" fuer cos k_i; beides falsch bzw. zu stark. Richtig: Vorfaktor 1,
    Abstand Faktor 3.] Die 3 sqrt3 der Dossier-Rechnung haelt damit unter der Konvention der Quelle [S + M].
  - Folge fuer PS1: Die Folgearbeit wiederholt die 10^90 nicht und aendert sie nicht; die Zeitschriftenfassung bleibt
    ungelesen. PS1 weiter nicht entscheidbar.
  - F8 bleibt ungenutzt (keine sichere ID fuer (b) oder (c)).

### C. DANZER-L 3.2 und 3.4 (ab 05:12, [M])
- Achsen a = (0, +-1, tau)/N usw., N^2 = 1 + tau^2 = tau + 2 = 3,618; Bilder b = (0, +-1, -1/tau)/N', N'^2 = 1 + 1/tau^2
  = 1,382; N^2 N'^2 = (tau + 2)^2/tau^2 = (5 tau + 5)/(tau + 1) = 5. a.a' = (tau^2 - 1)/(tau^2 + 1) = tau/3,618 = 0,447 =
  1/sqrt5; b.b' = (1/tau^2 - 1)/(1 + 1/tau^2) = -1/sqrt5. Probe haelt.
- E_i = a_i b_i^T transformieren wie die Permutation der sechs Achsen (Vorzeichen heben sich in a b^T auf); Permutations-
  darstellung von A5 auf 6 Punkten (zweifach transitiv) = A + H. Equivariante Abbildung A + H -> G + H: A -> 0 (also
  sum E_i = 0), H -> H nach Schur, nicht null (E_1 != 0). Spannt genau H. Haelt.
- Gram: <E_i, E_j> = (a_i.a_j)(b_i.b_j) = -(a_i.a_j)^2 = -1/5 (i != j), 1 (i = j): (6/5) I - (1/5) J. Haelt. Rahmenoperator
  hat die Nicht-Null-Eigenwerte der Gram-Matrix (6/5, fuenffach), also P_H = (5/6) sum E_i <E_i, .>. Haelt.
- B(n) = (5/6) sum (a_i.n)^2 b_i b_i^T aus <E_i, q w^T> = (a_i.q)(b_i.w). Steifigkeit K_G(|q|^2 - B) + K_H B. Haelt.
- tr B = (5/6) * 2 = 5/3 (sum a a^T = 2 * 1). tr B^2 = (25/36)[(4/5) S4 + (1/5) * 4], S4 = sum (a.n)^4 = 6/5 (5-Design):
  (25/36)(4/5)(11/5) = 44/36 = 11/9. Haelt.
- 5-zaehlig n = a_1: B = (5/6)[b_1 b_1^T + (1/5)(2 - b_1 b_1^T)] = (2/3) b_1 b_1^T + 1/3: (1, 1/3, 1/3), tr B^3 = 1 + 2/27
  = 29/27 = 1,0741. Haelt.
- 3-zaehlig n = (1,1,1)/sqrt3: cos^2 nah c_n = (5 + 2 sqrt5)/15 = 0,6315, fern c_f = (5 - 2 sqrt5)/15 = 0,0352; c_n c_f
  = 5/225 = 1/45. Galois tauscht nah und fern: (b.m)^2 = c_f fuer nahe, c_n fuer ferne Achsen. m^T B m = (5/6) * 6 c_n c_f
  = 5/45 = 1/9; Rest (5/3 - 1/9)/2 = 7/9. tr B^3 = (1 + 2 * 343)/729 = 687/729 = 0,9424. Haelt.
- 2-zaehlig n = (1,0,0): (a.n)^2 = 0, 0, p, p, q, q mit p = 1/(tau + 2), q = tau^2/(tau + 2), pq = 1/5. B = (1/3) diag(2,
  1/tau^2, tau^2) = (0,667; 0,127; 0,873). tr B^3 = (8 + tau^6 + tau^-6)/27, tau^6 + tau^-6 = 3^3 - 3 * 3 = 18: 26/27 =
  0,963. Haelt.
- Zwei Spektren mit Spur 5/3, Quadratspur 11/9 und Doppelwert: 27 y^2 - 30 y + 7 = 0, y = 7/9 oder 1/3. Haelt.
- Laengsanteil: |v|^2 = sum_ij (a_i.n)^3 (a_j.n)^3 (b_i.b_j) = 2 sum (a.n)^6 - |sum (a.n)^3 a|^2; sum (a.n)^3 a = (1/4) grad
  [(6/5)|n|^4] = (6/5) n, Quadrat 36/25 in jeder Richtung. 5-zaehlig: sum (a.n)^6 = 1 + 5/125 = 26/25, |v|^2 = 52/25 -
  36/25 = 16/25 = 0,64. 2-zaehlig: 2(p^3 + q^3) = 2(1 - 3/5) = 4/5, |v|^2 = 40/25 - 36/25 = 4/25 = 0,16. 3-zaehlig:
  3(c_n^3 + c_f^3) = 3(8/27 - 2/45) = 34/45, |v|^2 = 68/45 - 36/25 = (340 - 324)/225 = 16/225 = 144/2025 = 0,0711.
  Kugelmittel 2 * 6/7 - 36/25 = 48/175 = 0,274. Alle haelt.
- Kopplung: eps hat A + H, grad w hat G + H: genau eine Invariante (H mit H). Ebene Wellen: a^T eps a = i (a.q)(a.u),
  a^T grad w b = i (a.q)(b.w), Summe u^T X(q) w. Statisch relaxiert, K_G = K_H = K: Phi_eff = Phi - (R^2/(K|q|^2)) X X^T,
  X = |q|^2 X(qhat): Korrektur ~ |q|^2, also gleiche Ordnung wie die Elastizitaet. Laengs: (lambda + 2 mu) - (R^2/K)
  |v(qhat)|^2 in erster Stoerungsordnung (L-T-Mischung erst R^4). |v|^2 = 2 sum (a.n)^6 - 36/25 ist Grad 6 und I-invariant,
  also Konstante plus reines l = 6. Haelt. Zusatz: Fuer mitlaufende (traege) Phasonen steht K - rho_w c_L^2 statt K
  (Betrag und Vorzeichen aendern sich, das Winkelmuster nicht).
- 3.2 Zaehlung: Sym^2(D0 + D2) = 2 D0 + 2 D2 + D4 (21); mal (D0 + D2): D0 4, D1 2, D2 7, D3 3, D4 4, D5 1, D6 1; Dimension
  4 + 6 + 35 + 21 + 36 + 11 + 13 = 126. Invarianten: SO(3) 4; O: 4 (l=0) + 4 (l=4) + 1 (l=6) = 9 (l = 3, 5 ohne
  O-Invariante); I: 4 + 1 = 5. Haelt.
- Eichprobe: D6 kommt in V^6 nur einmal vor (nur in Sym^6, Young-Form (6)), also ist das D6-Stueck der total symmetrische
  spurfreie Teil. E(k) h fuer h = k xi + xi k ergibt 2 T(., ., xi, k, k, k); verschwaende das fuer alle k, xi, waere
  T(k,...,k) = 0, also T = 0. Kern einer aequivarianten Abbildung zerfaellt nach isotypischen Teilen. Haelt.
