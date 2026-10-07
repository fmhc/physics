# QB-BS-2D: Plan (Code-Agent, Runde 37)

- Code-Agent fuer claude-primary. Start 2026-10-04 04:51:03 CEST (date); Plan geschrieben ab 05:13:48 CEST (date).
- Grundlage: KARTE.md (Vorhersagen QB0 bis QB4, unveraendert uebernommen), spin-hopf-l/DOSSIER.md Abschnitt 7,
  literatur-20260923/SPIN-KONSTRUKTION-codex.md B.5, literatur-20260924/CXS2-TORE-astra-20260924.md (L1 bis L3, F1, T3,
  T7), resonance-20260930/qball-hopf-3d/{ERGEBNIS.txt, ROTATIONSGRENZE.txt}, RUNDE-03/tests2d-r3/KNOTEN-PAPIER.md.
- Kennzeichen: [S] an der Quelle (Projektdatei) gelesen, [L] Gedaechtnis, [L?] unsicher, [H] Hypothese, [ES] eigener Schluss.
- Nur radiale Stufen S0 bis S2. Synthetische Rechnung, keine Messdatenbestaetigung.

## 1. Modell gegen B.5

**B.5 (Codex, SPIN-KONSTRUKTION-codex.md, Abschnitt B.5) [S]:** Signatur (+---),

    L_* = d_mu phi^* d^mu phi + (v^2/4) d_mu n.d^mu n - U(s) + gJ Re[(phi^* b(n))^2] - mu^2 v^2 (1 - n3) - (kappa/4) H_mn H^mn,
    b = (v/2)(n1 + i n2), s = |phi|^2 + |b|^2, U(s) = s - s^2 + s^3/2, phi(inf) = 0, n(inf) = (0,0,1).

**Kartenform:** Gleiche Terme, gleiche Vorzeichen, gleiche Konstanten (G = gJ). Die Lagrangedichte weicht nicht ab.
Abweichungen gegenueber B.5 liegen nur ausserhalb der Lagrangedichte:
1. 2+1 statt 3+1 Dimensionen; der Knoten ist ein Baby-Skyrmion (B = 1) statt eines Hopfions (Kartenwahl, Dossier 7).
2. Drehsinn: Karte e^{+i(...)}, B.5/astra e^{-i omega t}. Das kehrt nur das Ladungsvorzeichen um; ich rechne mit q >= 0.
3. Igel-Ansatz mit gemeinsamer Drehung (G = 1, l = 1) bzw. ruhender Textur (G = 0, l = 0). Bei l = 1 ist phi^* b reell;
   ich waehle die guenstige relative Phase (phi^* b >= 0 bis auf das Vorzeichen von h), der Paarterm wird -G x y in der
   Energie (x = h^2, y = (v^2/4) sin^2 f). Eine relative Phase pi/2 gaebe +G x y; sie wird nicht gerechnet.

**Statische Energie im Igel-Ansatz [ES, aus L1 nach astra]:** Mass 2 pi r dr,

    V = 2 pi Int r dr [ h'^2 + l^2 h^2/r^2 + (v^2/4)(f'^2 + sin^2 f/r^2) + (kappa/2) f'^2 sin^2 f/r^2
                        + U(h^2 + y) - Gp h^2 y + mu^2 v^2 (1 - cos f) ],    y = (v^2/4) sin^2 f,

mit Gp = G fuer den gekoppelten Ast (l = 1) und Gp = 0 sonst.
- In 2D ist (kappa/4) Sum_ij H_ij^2 = (kappa/2) H_12^2 = (kappa/2)(f' sin f/r)^2.
- Traegheiten (astra L3, sinngemaess 2D): Lambda_n = 2 pi Int r dr [(v^2/2) sin^2 f + kappa sin^2 f f'^2],
  Lambda_phi = 2 pi Int r dr 2 h^2.

**Ladung:**
- Gekoppelter Ast (G = 1): Es gibt nur die gemeinsame Ladung. Gemeinsame Drehung Omega, q = Omega Lambda,
  Lambda = Lambda_n + Lambda_phi (astra L2/L3); q_n = Omega Lambda_n, q_phi = Omega Lambda_phi. Das deckt sich mit
  dem Dossier: Groesse ist die gemeinsame Drehung Omega.
- G = 0: q_n und q_phi sind getrennt erhalten. Der Mischast der Karte hat eine ruhende Textur, also q_n = 0, q = q_phi,
  omega = q/Lambda_phi.
- Referenzen: E_H(u) = V_H + u^2/(2 Lambda_n) mit phi = 0; E_Q(q) = V_Q + q^2/(2 Lambda_phi) mit n = Nordpol (exakter
  alter Teilsektor, B.5 Punkt 1). Bei n = Nordpol ist G wirkungslos; E_Q haengt nicht von kappa ab.
- J (Karte "je q ... J"): Fuer den Igel ist Isorotation gleich Raumdrehung, daher J = q_n + l q_phi aus dem Ansatz
  (Dossier K3). Das ist vorab ableitbar (G = 1: J = q; G = 0: J = 0) und wird nur als Kontrolle gefuehrt.

**Topologische Schranke:** f(0) = pi, f(R) = 0 erzwingen B = 1. Bogomolny: E_sig = (v^2/4) Int |grad n|^2 >= 2 pi v^2 |B|
[L, Standard]. Alle anderen Terme sind >= 0 (fuer |G| < 4(sqrt 2 - 1) nach Codex/astra [S]), also E >= 2 pi.

**Derrick/Virial in 2D bei festem q [ES]:** Unter x -> lambda x sind die Zweiableitungsterme invariant, Potentialterme
skalieren mit lambda^2, der Faddeev-Term mit lambda^-2, Lambda_phi und (v^2/2)-Teil von Lambda_n mit lambda^2. Am
Minimum gilt E_0 - E_4 = (Omega^2/2) Lambda_pot (E_0 = Potentialterme, E_4 = Faddeev-Term). Gefuehrt als relatives
Residuum je Punkt.

## 2. Normierungen und Parameter (vorab gebunden)

- v = mu = 1; kappa in {1; 1/4}; G in {0; 1}. Keine weiteren Werte.
- Rechengebiet r in [0, 60]. Dirichlet f(60) = 0, h(60) = 0. h'(0) = 0 (l = 0, natuerliche Randbedingung) bzw.
  h(0) = 0 (l = 1). Delokalisierungsmass: Anteil von Lambda_phi bei r > 45.

## 3. Loeser

- P2-Finite-Elemente (quadratische Lagrange-Elemente), exponentiell gestrecktes Gitter r_k = 60 (e^{3,5 s_k} - 1)/(e^{3,5} - 1),
  s_k gleichabstaendig; 3-Punkt-Gauss je Element. Diskretes Energiefunktional mit analytischem Gradienten.
- Minimierung von E_q bei festem q: Newton-Levenberg-Marquardt. Hesse-Matrix von F_Omega = V - (Omega^2/2) Lambda per
  gefaerbter Zentraldifferenz (Schritt 1e-5) des analytischen Gradienten, Rang-1-Term (Omega^2/Lambda) gL gL^T per
  Sherman-Morrison, Armijo-Liniensuche auf E_q. Konvergenz: Newton-Dekrement < 1e-20 |E| bei vollem Schritt.
- Aufloesung: grob M = 600 Elemente (N_r = 1201 Knoten), fein M = 1200 (N_r = 2401). "Verdopplung von N_r" heisst
  M -> 2M.
- Feingitterpunkte starten aus der interpolierten Grobloesung desselben q.

## 4. Festladungsverfahren (Begruendung)

- Gewaehlt: E_q = V + q^2/(2 Lambda) nach astra L3, bei festem q minimiert.
- Begruendung: E_q ist die Energie bei fester Ladung (Cauchy-Schwarz, astra Abschn. 5). Sie ist nach unten beschraenkt
  (E_q >= V >= 2 pi), die Minimierung liefert direkt die untere Huellkurve je Ast. Omega = q/Lambda folgt;
  dE/dq = Omega ist eine echte Kontrolle.
- Verworfen: fester Multiplikator Omega. Bei festem Omega ist der Q-Ball ein Sattel (Bergpass) von F_Omega, und an
  Falten von q(Omega) bricht die Fortsetzung ab.

## 5. chi_max (Definition mit Fundstelle)

- Quelle [S]: coordination/resonance-20260930/qball-hopf-3d/ROTATIONSGRENZE.txt, Absatz "Unabhaengiger lokaler
  Principal-Check", und ERGEBNIS.txt Abschnitt 3:
  chi = c^T G^-1 c, G = (1/2) Id + Sum_i a_i a_i^T, a_i = (d_i n) x n, c = n x v, v = ndot = Omega e3 x n (v = kappa = 1).
  In einer Raumrichtung e mit a_e = 0 sind die charakteristischen Geschwindigkeiten^2 gleich 1 und 1 - chi.
- Uebertragung auf allgemeine v, kappa [ES]: G = (v^2/2) Id + kappa Sum a_i a_i^T, chi = kappa c^T G^-1 c.
- Igel [ES]: c = -Omega sin f e_f, G_ff = v^2/2 + kappa sin^2 f/r^2, also
  chi(r) = kappa Omega^2 sin^2 f / (v^2/2 + kappa sin^2 f/r^2); chi_max = Maximum ueber alle Gauss-Punkte.
- Lesart [ES]:
  - Fuer den geraden String (2D-Loesung in 3D eingebettet) ist e = z eine Nullrichtung; dort gilt die 3D-Aussage
    unveraendert.
  - In echter 2+1-Dynamik gibt es dort, wo die topologische Dichte nicht verschwindet, keine Nullrichtung in der Ebene;
    chi > 1 ist dann nicht automatisch hinreichend fuer komplexe Geschwindigkeiten.
  - chi(r) < 1 ist gleichwertig mit positivem Leitkoeffizienten der radialen F_Omega-Gleichung.
- Bei G = 0 ruht die Textur: chi = 0.

## 6. Referenzaeste (S1)

- E_H(u) je kappa:
  - u = 0; 0,25; 0,5; ... aufwaerts bis Omega^2 > 0,95 v^2/(2 kappa) (dieser Punkt zaehlt nicht mehr) oder bis der
    Loeser versagt. u_max ist der letzte gueltige Punkt.
  - Je Punkt: chi_max.
- E_Q^l(q') fuer l = 0 und l = 1:
  - q' = 100, 99, ... abwaerts bis delokalisiert (Anteil > 1e-4 bei r > 45), omega > 0,999 oder Loeserversagen.
  - q_lo^l ist der kleinste gueltige Punkt.
- Interpolation zwischen Astpunkten: kubisch-hermitesch mit dE/dq = Omega.
- **E_Q\*(q') (Kartenluecke, festgelegt):**
  - E_Q\*(q') = min(E_Q^0(q'), E_Q^1(q') [jeweils nur im berechneten Bereich], q') fuer q' > 0; E_Q\*(0) = 0.
  - Die Linie q' ist der Kanal "freie phi-Ladung" mit Grenzkosten m_phi = 1 (astra T3). Sonst fehlt unterhalb q_lo
    jede Referenz und E_sep waere dort ueberhoeht.

## 7. E_sep und Bindung D

- **E_sep,K(q) (Kartenwortlaut):** min ueber u in [0, min(q, u_max)] von E_H(u) + E_Q\*(q - u), Raender u = 0 und
  u = min(q, u_max) eingeschlossen. Suche auf 4001 gleichverteilten u-Werten plus allen Astenden.
- **E_sep,C(q) (konservativ, Hauptregel fuer G = 1):** wie E_sep,K, zusaetzlich fuer q > u_max die Fortsetzung
  E_H(u) -> E_H(u_max) + Omega_H(u_max)(u - u_max) fuer u in (u_max, q].
  - Grund (Kartenluecke): Die Karte schneidet E_H bei 0,95 v^2/(2 kappa) ab, nimmt aber min_u bis q. Fuer q > u_max
    koennte die Referenz dann keine weitere Ladung auf den Knoten legen und waere kuenstlich hoch, eine Bindung waere
    vorgetaeuscht (astra T6).
  - Bei konvexem E_H (Omega steigt mit u) ist die Tangente eine untere Schranke [ES].
- **E_sep,A(q) = E_H(0) + E_Q\*(q) (Hauptregel fuer G = 0, Berichtigung, siehe Abschnitt 11a).**
- D_X(q) = (E_sep,X(q) - E_mix(q))/E_sep,X(q), X in {K, C, A}.

## 8. Mischaeste (S2)

- q-Raster (vorab, ohne Kenntnis der Aeste): q_k = 2,5 k, k = 1 bis 40, also q in [2,5; 100].
- G = 1: gekoppelter Ast, l = 1, Gp = 1, Lambda = Lambda_n + Lambda_phi.
- G = 0: ruhende Textur plus phi mit l = 0, Gp = 0, Lambda = Lambda_phi.
- Grobgitter, drei Starts je q:
  - "fortsetzung": Auswahl des vorigen q;
  - "ring": statische Textur, h = 0,8 sin f;
  - "ball": statische Textur, Q-Ball-artiges h (l passend).
- **E_mix(q)** ist die niedrigste konvergierte qualifizierte Loesung; ohne qualifizierte Loesung gilt der Punkt als
  "kein Mischzustand".
  - Feingitter: ein Start aus der interpolierten Grobauswahl.
  - Qualifiziert heisst: konvergiert, q_phi/q >= 0,01 und Anteil von Lambda_phi bei r > 45 kleiner als 1e-4.
- Je q protokolliert: E, Omega^2, D_K, D_C, D_A, chi_max, J, q_phi/q, Virial, Start.

## 9. Urteilsregeln (vor dem Einfrieren, danach unveraendert)

- **"D(q) > 0" (robust):** Der Mischzustand ist auf beiden Gittern qualifiziert, D_fein > 0 und
  |D_fein - D_grob| < D_fein/3. Ein Rasterpunkt ohne qualifizierten Mischzustand zaehlt als "nicht D > 0".
- **QB0:**
  - Eingetroffen, wenn alle fuenf Teilproben bestehen:
    - statisches B = 1-Profil fuer kappa = 1 und kappa = 1/4: E > 2 pi und E_sig >= 2 pi, relative
      Energieaenderung grob -> fein <= 1e-6, beide Gitter konvergiert;
    - Q-Ball l = 0 an den drei Astpunkten mit omega am naechsten an 0,75, 0,85 und 0,95 (Feingitter): omega in
      (1/sqrt 2, 1) und relative Energieaenderung <= 1e-6.
  - Sonst nicht eingetroffen; nicht auswertbar, wenn ein Teil fehlt.
  - Festlegung [Kartenluecke]: Die Karte nennt "drei omega"; ich nehme die Astpunkte bei festem q, deren omega den
    drei Zielwerten am naechsten liegt.
- **QB1 (kappa = 1, G = 1):** Eingetroffen, wenn D_C auf mindestens drei aufeinanderfolgenden Rasterpunkten robust > 0
  ist. Nicht auswertbar, wenn kein Rasterpunkt einen qualifizierten Mischzustand hat. Urteil nach Kartenwortlaut mit
  D_K wird mitgeteilt.
- **QB2:**
  - Lesart: QB2 ist ein Teilereignis von QB1 (35 % < 50 %).
  - Eingetroffen, wenn QB1 eingetroffen ist und auf mindestens einem Punkt der QB1-Laeufe (drei oder mehr
    aufeinanderfolgende robuste Punkte) Omega^2 < 1/2 auf beiden Gittern gilt.
  - Nicht eingetroffen, wenn QB1 nicht eingetroffen ist oder kein solcher Punkt existiert. Nicht auswertbar, wenn QB1
    nicht auswertbar ist.
- **QB3 (kappa = 1/4, G = 1):** wie QB1.
- **QB4 (G = 0):**
  - Eingetroffen, wenn fuer beide kappa auf keinem Rasterpunkt D_A robust > 0 ist. Festlegung [Kartenluecke]: "fuer
    alle q" gilt fuer beide kappa.
  - Nicht auswertbar, wenn fuer ein kappa kein qualifizierter Mischzustand existiert. Urteil nach Kartenwortlaut mit D_K
    wird mitgeteilt.

## 10. Kontrollen (keine Vorhersagen)

- Virial (2D-Derrick bei festem q) je Punkt, relatives Residuum.
- dE/dq = Omega laengs aller Aeste (zentrierte Differenz).
- Bogomolny: E_sig/(2 pi) >= 1.
- K3: J = q fuer G = 1 (aus dem Ansatz, nur Konsistenz).
- **K4 Nullprobe (Codex/astra T7):**
  - G = 0 und U(x) + U(y) statt U(x + y), ruhende Textur, Ballstart, bei q = 30, 60, 90 (kappa = 1).
  - Erwartet exakt E_null = E_H(0) + E_Q^0(q), also D_null = 0. Schwelle |D_null| <= 0,002 (Codex B.5-Skelett).
- K1 (Vorzeichen des Kreuzterms) ist vorab ableitbar: U(x+y) - U(x) - U(y) = xy[-2 + 1,5(x + y)] < 0 fuer
  x + y < 4/3 [S, astra P3]. K2 (Omega^2 -> 1/2 von oben bei grossem q) wird nur berichtet.
- Gitter: alle Energien grob und fein; Residuum skaliert; Newton-Dekrement.

## 11. Kartenfehler und Kartenluecken (vor dem Einfrieren offengelegt)

**a) G = 0, Referenz (Kartenfehler, berichtigt):**
- Bei G = 0 sind q_n und q_phi einzeln erhalten (astra, Papierkontrollen zu L3, und T7).
- Der Mischast der Karte hat eine ruhende Textur, also q_n = 0. Seine Zerfallskanaele haben ebenfalls q_n = 0, also
  u = 0.
- E_sep = min_u vergleicht mit Zustaenden q_n = u > 0, die bei G = 0 nicht erreichbar sind. Das macht die
  Referenz zu niedrig und laesst QB4 ("keine Bindung") zu leicht eintreffen.
- Berichtigung: Hauptregel D_A mit E_sep,A = E_H(0) + E_Q\*(q). Das Urteil nach Kartenwortlaut (D_K) wird mitgeteilt.

**b) Abgeschnittener E_H-Ast (Kartenluecke):** E_sep,C nach Abschnitt 7 als Hauptregel fuer G = 1; D_K nach
Kartenwortlaut mitgeteilt.

**c) E_Q unterhalb q_lo (Kartenluecke):** Kanal "freie Ladung" q' nach astra T3.

**d) QB2 (Lesart):** QB2 bedingt auf QB1, siehe Abschnitt 9.

**e) QB4:** Die Karte nennt kein kappa; "alle q" gilt fuer beide kappa.

**f) "Omega(q)" bei G = 0:** Dort ist es die phi-Frequenz omega; die Textur ruht.

**g) "E_Q(q) fuer l = 0 und l = 1":** E_Q\* nimmt das Minimum beider Aeste (und des freien Kanals).

**h) "Q-Ball-Profile bei drei omega":** Astpunkte mit naechstem omega, siehe QB0.

**i) Dossier:** Dort heisst es "Kerntest min_q Omega^2(q) < 1/2"; die Karte bindet das an den gebundenen Ast (QB2).
Ich folge der Karte.

## 12. Rauchlauf (vor dem Einfrieren, offengelegt)

- **Rauchlauf 1:** 2026-10-04 03:10:06 bis 03:10:08 UTC (Starter-Ausgabe), Spur cpu, rauch/smoke1.json.
  - Nur Codepfade, M = 200 und 400. D wurde nicht berechnet.
  - Gesehene Werte:
    - Statische Textur: kappa = 1 E = 26,545533 bzw. 26,545533 (relativ 1,4e-8); kappa = 1/4 E = 17,055186.
    - H bei u = 3: kappa = 1 Omega^2 = 0,0274; kappa = 1/4 Omega^2 = 0,309.
    - Q-Ball q = 60: l = 0 E = 51,389467, omega^2 = 0,606 (!); l = 1 E = 59,2886.
    - M1 (kappa = 1, G = 1, q = 20, nur Ringstart): h -> 0, also reiner drehender Knoten mit E = 36,56495,
      Omega^2 = 0,797, chi_max = 0,676.
    - M0 (kappa = 1, G = 0, q = 20, Ringstart): E = 44,92326, omega^2 = 0,7258, h_max = 0,847.
  - Laufzeit je Loesung 0,04 bis 0,2 s.
- **Bedeutung:**
  - Der Q-Ball bei q = 60 hat omega^2 = 0,606 > 1/2, liegt also im Fenster.
  - Der drehende Knoten bei kappa = 1 existiert noch bei Omega^2 = 0,80 > 1/2 mit chi_max = 0,68 < 1, also weit
    jenseits der Kartenschwelle 0,475.
  - Die Regel E_sep,C (Abschnitt 7) hatte ich vor dem Rauchlauf erwogen, schriftlich fixiert erst danach. Der
    Rauchlauf zeigt, dass sie greift.
  - Die Schwellen der Karte sind unveraendert.
- **Rauchlauf 2 (Pipeline-Test):** 2026-10-04 03:15:36 bis 03:15:58 UTC (Starter-Ausgabe), Spur cpu, rauch/pipe/.
  - Alle Aufgaben auf M = 100 und 200, refQ ab q' = 30, mix bis q = 15, danach auswertung.py.
  - Angesehen habe ich nur die Fehlerliste (leer), die Abbruchgruende und Laufzeiten der Aeste sowie die Nullprobe.
    Urteile und D-Werte habe ich nicht angesehen.
  - Abbruchgruende (du = 0,5):
    - E_H: kappa = 1 bei u = 14 (Omega^2 > 0,475), u_max = 13,5; kappa = 1/4 bei u = 9, u_max = 8,5.
    - E_Q l = 0: delokalisiert bei q' = 11, q_lo = 12. Passt zur Townes-Grenze q -> N_T ~ 11,7 fuer omega -> 1 [ES].
    - E_Q l = 1: schon bei q' = 30 delokalisiert (Startpunkt), im Hauptlauf startet der Ast bei 100.
  - Nullprobe K4 bei q = 30: D_null = 0,0 auf beiden Gittern.
  - Laufzeit: Mischast etwa 0,8 s je q bei M = 100 mit drei Starts.
- **Folge vor dem Einfrieren:** Aufloesung von M = 1000/2000 auf M = 600/1200 gesenkt (Abschnitt 3), damit jeder
  Mischlauf mit grob und fein sicher unter 600 s bleibt. Grund ist nur die Laufzeit. Die Energieaenderung bei
  Verdopplung lag im Rauchlauf 1 schon bei M = 200 -> 400 bei 1,4e-8 (Textur) bzw. 3e-9 (Q-Ball).
- **Weitere Festlegung:** Fuer E_H gilt du = 0,25, fuer E_Q dq' = 1.

## 13. Laufplan

- Spuren cpu und cpu6, hoechstens zwei Laeufe zugleich, je Lauf deutlich unter 600 s.
- Je Lauf grob und fein im selben Lauf.
- Reihenfolge:
  1. refH kappa = 1 und kappa = 1/4 (du = 0,25);
  2. refQ l = 0 und l = 1 (dq = 1, ab q' = 100);
  3. mix fuer (kappa, G) in {1, 1/4} x {1, 0}, mit Nullprobe bei kappa = 1, G = 0;
  4. auswertung.py -> lauf/auswertung.json, lauf/bilder/*.svg.
- Ein Lauf, der an der 600-s-Grenze abbricht, wird geteilt (grob und fein getrennt) und neu gestartet. Das
  Abbruchprotokoll bleibt erhalten.
