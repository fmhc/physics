Urteil: traegt mit Aenderungen (5 A, 8 B, 8 C); in der vorliegenden Fassung nicht weitergeben.

# PAPIER-I-GEGENLESEN: Ergebnis des frischen Lesers (pruefer-opus, Haus Anthropic)

- Beginn: 2026-10-04 10:36:19 CEST (date); Inhalt fertig: 2026-10-04 10:55:53 CEST (date), also 19 min 34 s
  [M: 55:53 - 36:19 = 19:34].
- Auftrag: RUNDE-37/papier-i-gegenlesen/KARTE.md, sha256 ef304a6a2fdd225899754fcf2dd01753b2897d14f34e6e8688606dfd5d2c9e4f (von mir gemessen; die Leitung hat keinen Wert genannt)
- Kennzeichen: [S] an der Quelle gelesen, [ES] eigener Schluss, [M] Rechnung (Kopfrechnung mit Rechenweg).
- Rechenregel: Die festen Pruefer-Regeln verbieten jede Rechnung auf dem Rechner und gehen der lockereren Karte vor
  ("jq kann exp/log"). Alle Kontrollrechnungen sind daher Kopfrechnungen mit offenem Rechenweg; jq nur zum Lesen.

## 1. Ergebnis

**traegt mit Aenderungen.** In der vorliegenden Fassung nicht an Codex weitergeben.
- Die Physik dahinter traegt [S]:
  - Bei eps > 0 bleibt die Transmissionsnullstelle (VW V1).
  - Bei eps < 0 bleibt nur ein nicht stoerungstheoretisches Leck. Es ist bis 1,55e-49 aufgeloest und an Genauigkeit und
    Schrittweite stabil.
  - Der Exponent folgt dem Polabstand pi der logistischen Wand auf 0,2 bis 0,5 % (VP).
- Fuenf A-Befunde (Abschnitt 2):
  - A1: Die Schwanzwahl ist nicht gemessen; der Text sagt "a few per cent", die Quellen zeigen 1,4 bis 27 % zwischen
    Schwanzvarianten und einen Faktor 1,8 bis 2,2 ohne eps im Hintergrund.
  - A2: "about 10^-95 at h = 0.1" laesst einen Vorfaktor von ~10^13 weg; die Ausgleiche ergeben ~10^-82.
  - A3: beta = 1 statt beta = 1/2 des Papiers, ohne Kennzeichnung.
  - A4: zwei neue Kanaele je Seite, nicht "a second channel".
  - A5: "single" behauptet Eindeutigkeit, die das Papier selbst offenlaesst.
- Dazu acht B-Befunde und acht C-Befunde.
- Quote ueber 22 gepruefte Zahlen und Aussagen (Abschnitt 3):
  - 14 stimmen ohne Anmerkung.
  - 3 stimmen in der Zahl, haben aber eine Anmerkung (Z4, Z15, Z17).
  - 5 sind falsch oder nicht gedeckt (Z1 im Zusammenhang, Z3, Z8, Z18, Z21).
- LaTeX ist syntaktisch sauber, Reste der Beschaedigung sind nicht sichtbar.

## 2. Befunde

### A (muss vor Weitergabe geaendert werden)

Zeilenangaben "Entwurf Z." beziehen sich auf RUNDE-37/PAPIER-I-ROBUSTHEIT-ENTWURF.md (sha256 1aca386c..., 70 Zeilen).
Die Vorschlaege behalten das Symbol \epsilon des Entwurfs; zur Umbenennung siehe B1.

**A1. "a few per cent" fuer die Schwanzwahl ist nicht gedeckt.** Entwurf Z. 36 f.
- [S] VP ERGEBNIS Selbstanzeige 6: "Wie stark P von ihr abhaengt (etwa gegen einen zweiseitigen Schwanz), habe ich nicht
  gemessen. Gemessen ist nur der Abstand zu Modell D (Faktor 1,8 bis 2,2)".
- [S] VP Vermerk PR0: Ende 47 gegen 90 aenderte P um 27 %, FD-Variante A gegen B um 6 %; VP gegen FD-A -7,4 %, gegen
  FD-B -1,4 %. [M] (4,61/4,09)^2 = 1,127^2 = 1,27, also 27 % (VW Tabelle Hintergrund-Artefakt).
- [S] VP PLAN Abschnitt 2: Fuer eps < 0 gibt es generisch keine Wand ohne Schwanz (Nanopteron). Der Schwanz ist von der
  Ordnung exp(-pi k0), also von derselben Ordnung wie das Leck, und Teil der Modelldefinition.
- [S] Die Ernte widerspricht sich selbst: RUNDE-37.md Z. 109 "deren Einfluss nicht gemessen ist", Z. 114 "liegt bei ~6 %
  in P". Der Entwurf folgt Z. 114.
- Vorschlag (ersetzt den Satz "The prefactor depends ..."):
  "For $\epsilon<0$ the static wall itself carries an oscillatory tail of order $\exp(-\pi k_0)$,
  $k_0\simeq|\epsilon|^{-1/2}$, so the background is defined only up to this tail; we used the solution without an
  interior tail. The dependence of $P$ on this choice was not measured. In earlier double-precision runs with
  boundary-fixed tails, $P(\epsilon=-10^{-2})$ changed by up to $27\,\%$, and removing the $\epsilon$ term from the
  background changed $P$ by a factor of 1.8 to 2.2, while the channel-wise fitted pole distances moved by at most
  $0.3\,\%$."
- [M] zum letzten Halbsatz: B neu -0,35 % (Karte) gegen -0,63 % (D), Abstand 0,28 Punkte; A neu -0,42 % gegen -0,48 %,
  Abstand 0,06 Punkte (VP Zusatz, Tabelle kanalweise).

**A2. "about 10^-95 at h = 0.1" laesst einen Vorfaktor von etwa 10^13 weg.** Entwurf Z. 37-39.
- [S] Die Zahl stammt aus der Ernte von V-1-WEITER (RUNDE-36.md Z. 389), also von vor V-1-PRAEZISION. Der dort
  gemessene Vorfaktor ist nicht eingearbeitet.
- [M] Schon an den Messpunkten liegt P weit ueber dem nackten Exponentialfaktor exp(-2 pi/sqrt|eps|):
  - eps = -2e-3: 2 pi x 22,3607 = 140,496, also 10^(-140,496 x 0,434294) = 10^-61,02 = 9,6e-62. Gemessen 1,55e-49,
    Verhaeltnis 1,6e12.
  - eps = -1e-2: 2 pi x 10 = 62,832, also 10^-27,29 = 5,2e-28. Gemessen 8,69e-17, Verhaeltnis 1,7e11.
- [M] Hochrechnung auf h = 0,1, also abs(eps) = 0,01/12 = 8,333e-4:
  - ln abs(eps) = -ln 1200 = -(2,48491 + 4,60517) = -7,09008; 1/sqrt abs(eps) = sqrt 1200 = 34,6410.
  - K_B nach VP PLAN Z. 99: k^2 = (1,77346 + 0,86603)^2 - 1 = 2,63949^2 - 1 = 5,96689; 4 abs(eps) k^2 = 0,019890;
    sqrt(1 - 0,019890) = 0,990005; K_B^2 = 1,990005 x 600 = 1194,003; K_B = 34,5543.
  - FK (a = 14,4074, q = -2,0049, d = 3,13278): ln P = 14,4074 + 14,2146 - 6,26557 x 34,5543 = 14,4074 + 14,2146 -
    216,503 = -187,881, also log10 P = -187,881 x 0,434294 = -81,60.
  - F1 (a = 22,7064, q = -0,38857, c = 6,14923): ln P = 22,7064 + 2,7550 - 213,016 = -187,554, also log10 P = -81,45.
  - Nackter Exponentialfaktor: 2 pi x 34,6410 = 217,656, also 10^-94,53 = 3,0e-95.
- Beide Ausgleiche geben P ~ 10^-82, 13 Zehnerpotenzen ueber dem Text. Auch das ist eine Hochrechnung: Gemessen ist bis
  abs(eps) = 2e-3, das entspricht [M] h = sqrt(12 x 0,002) = sqrt 0,024 = 0,155.
- Vorschlag (ersetzt "For a lattice-like softening ... at $h=0.1$."):
  "For a lattice-like softening $\epsilon=-h^2/12$ the computed points correspond to $0.15\lesssim h\lesssim0.35$.
  The exponent grows as $2\pi\sqrt{12}/h\approx21.8/h$, but the prefactor is large: in the computed range $P$ exceeds
  $\exp(-2\pi|\epsilon|^{-1/2})$ by $10^{11}$ to $10^{12}$. Extrapolating the fit to $h=0.1$ gives $P\sim10^{-82}$."

**A3. Der Absatz rechnet bei beta = 1, der Abschnitt handelt vom Hauptmodell beta = 1/2.** Entwurf Z. 20 und 40-42.
- [S] ME Z. 83: beta = 1/2. ME Z. 446 ff.: Die Gitterbreiten h^4 und h^8 stammen aus 2D-Rechnungen "at the seventh radial
  location", also an der Leiter des Hauptmodells (ME Z. 189: "Radial sequence at beta = 1/2").
- [S] Im Papier heisst beta = 1 "the modified potential U(S) = S - S^2 + S^3 at omega_min = sqrt3/2" (ME Z. 368-372).
- [S][M] Der Polabstand ist pi sqrt(beta) (VW ERGEBNIS Z. 155 f.). Beim Hauptmodell, S(x) = [1 + exp(sqrt2 x)]^-1
  (ME Z. 324), betraegt er pi/sqrt2 = 2,221. Der Exponent waere dort um den Faktor sqrt2 kleiner. Fuer eps = -h^2/12
  ergaebe das [M] 2 pi sqrt6 = 6,28319 x 2,44949 = 15,39, also exp(-15,4/h). Das ist nur der Exponentialfaktor und
  nicht gerechnet.
- Der Schluss im letzten Satz ("consistent with ... the power-law widths reported above") geht damit stillschweigend
  ueber beta, Dimension und Geometrie hinweg.
- Vorschlag: Anfang "For the modified potential $\mathcal U(S)=S-S^2+S^3$ ($\beta=1$,
  $\omega_{\min}=\sqrt3/2$), not for the main model, we added ..."; zusaetzlicher Satz vor "These one-dimensional
  results": "For the main model, $\beta=1/2$, the nearest poles of $S(x)=[1+\exp(\sqrt2x)]^{-1}$ lie at distance
  $\pi/\sqrt2$, so the exponent would be smaller by $\sqrt2$; that case was not computed."

**A4. Es oeffnet sich nicht "a second propagating channel", sondern zwei neue Kanaele je Seite.** Entwurf Z. 27 f.;
widerspricht auch "dominant new channel" in Z. 33 f.
- [S] VP PLAN Z. 18 f.: "Fuer eps < 0 je Seite drei offene Kanaele (aussen B alt, A neu, B neu; innen e1 alt, e1 neu,
  e2 neu)". P ist die Summe ueber A neu und B neu; A neu traegt 12,6 % (-1e-2) bis 30,6 % (-2e-3), mit wachsendem Anteil
  (VP Zusatz).
- [M] In der Notation des Papiers (ME Z. 114-119: A offen mit k^2 = (omega + rho)^2 - 1, B geschlossen): Jedes
  Seitenband bekommt eine laufende Wurzel q^2 ~ 1/abs(eps). Das offene A-Band bekommt eine zweite, das geschlossene
  B-Band seine erste.
- Achtung: Die Quellen benennen umgekehrt. VP "B neu" (rho + omega) entspricht dem Papier-A, VP "A neu" dem Papier-B.
- Vorschlag: "For $\epsilon<0$ each sideband acquires a propagating branch with wavenumber $\simeq|\epsilon|^{-1/2}$,
  so two new channels open on each side of the wall, and a wave incident in the original interior channel at $\rho_z$
  leaks into them, but only non-perturbatively."

**A5. "single silent frequency" behauptet Eindeutigkeit, die das Papier ausdruecklich offenlaesst.** Entwurf Z. 20.
- [S] WB KARTE Z. 27 f. und 82: Gemessen wurde ein Vorzeichenwechsel von c_in bei Abtastschritt 0,002 im Fenster
  (1 - omega, 1 + omega). Ein Nullstellenpaar enger als 0,002 waere unentdeckt.
- [S] ME Z. 377-379 zu genau diesem Wert: "This known-target local replication neither counts all planar zeros nor
  establishes ...". Analog fuer beta = 1/2, ME Z. 335-337: "do not prove uniqueness".
- Vorschlag: "..., whose planar transmission zero lies at $\rho_z=1.7734530718$, we added ..."

### B (sollte)

**B1. Notation und Begriffe kollidieren mit dem Papier.** Entwurf Z. 20-28.
- [S] epsilon ist im Papier schon die Verstimmung: "Put $\epsilon=\omega^2-\omega_c^2$" (ME Z. 289), dazu epsilon_n in
  der Leiterformel (ME Z. 313 f., 343). Der Absatz setzte dann "$\epsilon=-h^2/12$" neben "epsilon_n ~ 1/(b n)".
- [S] omega ist im Papier die Q-Ball-Frequenz. Eine allgemeine Laborfrequenz heisst E (ME Z. 127 f.). k ist die
  Wellenzahl des offenen Kanals, k^2 = (omega + rho)^2 - 1 (ME Z. 115).
- [S] "silent frequency", "silence" und "silent wave" kommen im Papier nicht vor (grep). Das Papier sagt "transmission
  zero" bzw. "planar transmission cancellation" (ME Z. 319, 368).
- Ersatzsymbol: Es muss im ganzen Papier frei sein, Anhaenge eingeschlossen. In build/paper.html sind \eta, \sigma,
  \lambda, \gamma, \mu, \nu und \tau schon belegt. Die Wahl liegt bei Codex; unten steht X als Platzhalter.
- Vorschlag fuer Z. 21-24: "we added a term $X\,\partial_x^4$ to the field equation for background and fluctuations
  alike, so that a component of laboratory frequency $E$ obeys $E^2=1+q^2+Xq^4$ in vacuum. For $X>0$ no new propagating
  channel opens and the transmission zero persists". Danach durchgehend "transmission zero" statt "silence".

**B2. Das Wandprofil ist gegenueber Papier und Quelle gespiegelt.** Entwurf Z. 36.
- [S] Im Papier steht das Vakuum rechts: S(x) = [1 + exp(sqrt2 x)]^-1 (ME Z. 324) und f^2 ~ S_c/(1 + exp[(r - R)/sqrt
  beta]) (ME Z. 291-293).
- [S] Die Quelle rechnet ebenso: f(-inf) = f_c, f(+inf) = 0, f0 = sqrt(S_c/(1 + e^x)) (VP PLAN Z. 15 und 40),
  S = S_c/(1 + e^{x/sqrt beta}) (VW ERGEBNIS Z. 156).
- [S] Die Form e^(-x) des Entwurfs stammt aus der Herleitung der Leitung (RUNDE-36.md Ernte V-1-WEITER; VP KARTE Z. 8).
- [M] S_c = 1/(2 beta) = 1/2 und die Breite 1 stimmen: f'^2 = S/4 - S^2 + S^3 = S(S - 1/2)^2, also S' = -S(1 - 2S) im
  Vakuum-rechts-Bild. Die Pole liegen bei x = +-i pi(2n + 1), der Abstand pi gilt fuer beide Orientierungen.
- Vorschlag: "$S(x)=\tfrac12\,[1+\exp x]^{-1}$ ($S=f^2$)".

**B3. "residual" ist undefiniert, und die Gueltigkeit ist nicht eingegrenzt.** Entwurf Z. 24-26.
- [S] Die Groesse ist relativ: Restgroesse = T_aus(rho_z)/T_aus(rho_z + 1e-3) (VW ERGEBNIS Tab. 1, Fussnote).
  Das Papier verwendet "residuals" fuer Restfehler der komplexen Transmission (ME Z. 333).
- [S] Geprueft sind nur eps = 1e-3, 3e-3 und 1e-2 (V1). Die Steigung stammt aus +-1e-3 (VW Tab. 1, Fussnote).
- Vorschlag: "the transmission zero persists for $X=10^{-3}$, $3\times10^{-3}$ and $10^{-2}$ (transmitted flux at the
  zero below $3\times10^{-15}$ of its value at $\rho_z+10^{-3}$, in double precision)".

**B4. "leaked fraction" ist nur die Haelfte des Lecks.** Entwurf Z. 29-31.
- [S] P ist der Flussanteil in die neuen Aussenkanaele bei Einfall mit Fluss 1 im alten Innenkanal (VP PLAN Z. 21 f.).
  Gleich viel geht in die neuen Innenkanaele: "P_neu_innen = P_neu_aus an allen sechs Punkten auf 15 Stellen" (VP
  ERGEBNIS unter der Tabelle P(eps); VW Z. 93). Die alte Welle verliert also 2P.
- Vorschlag: "resolves the flux fraction $P$ transmitted into the new exterior channels, for unit incident flux in the
  original interior channel, from ... (an equal fraction is converted into the new interior channels)".

**B5. Der Ausgleich klingt sicherer, als die Quelle ihn nennt.** Entwurf Z. 32-36.
- [S] Das d haengt an der Wahl K = K_B (VP Vermerk PR2). Andere K-Varianten geben d/pi - 1 = -2,54 %, -1,61 % und
  -2,17 %. Mit K = abs(eps)^(-1/2) kommt c = 6,149 heraus, 2,1 % unter 2 pi (PR1 nicht eingetroffen). Die Kurzform in
  Z. 38 benutzt genau diese K-Wahl.
- [S] "Gesamt-P mit K_B ist eine Mischung zweier Exponenten. Die 0,28 % sind deshalb teils Mischungsglueck [H]."
  Kanalweise ergeben sich -0,35 % und -0,42 %, der Hintergrundschwanz gibt +0,21 %. Die Schwelle von PR2 lag bei 0,3 %,
  bestanden also knapp.
- [S] q ist schwach bestimmt: -2,0 (FK) bzw. -0,39 (F1). Die Reste zeigen in allen Ausgleichen dasselbe
  Vorzeichenmuster, die Ursache ist offen (VP Ausgleich).
- Vorschlag: "Over the six computed points, $2\times10^{-3}\le|X|\le10^{-2}$, the form $\ln P=a+p\ln|X|-2dK$ fits
  with residuals below $0.007$. Here $K^2=[1+(1-4|X|k^2)^{1/2}]/(2|X|)$, with $k$ from Eq.~\eqref{eq:channels} at
  $\rho_z$, is the new branch of the open sideband, which carries 69 to $87\,\%$ of $P$. The fitted $d=3.1328$ is
  $0.28\,\%$ below $\pi$, the distance of the nearest complex poles of $S$. Separate fits per channel give $0.35$ and
  $0.42\,\%$ below $\pi$, the background tail $0.21\,\%$ above. The power $p$ is poorly constrained ($-0.4$ to $-2.0$,
  depending on the form of the exponent)."
- Die Potenz heisst hier p, weil q im Vorschlag zu B1 schon fuer die allgemeine Wellenzahl steht. Ob p im Papier frei
  ist, habe ich nicht geprueft; die Wahl liegt bei Codex.

**B6. Ein echtes Naechste-Nachbar-Gitter hat diesen Kanal nicht [ES].** Entwurf Z. 41-43.
- [M] Fuer eine achsparallele ebene Wand auf dem Fuenfpunkt-Stencil (in 1D das Dreipunkt-Gitter) gilt
  E^2 = 1 + (4/h^2) sin^2(qh/2). Das ist monoton in abs(q) <= pi/h. Jede Frequenz unter der Bandkante hat also genau eine
  laufende Wellenzahl.
- Den zweiten Ast gibt es nur im bei k^4 abgeschnittenen Kontinuum. "is not shown" untertreibt deshalb: In dieser
  Geometrie gibt es den Kanal nicht.
- [H] Bei einem offenen Kanal je Seite sollte eine ebene Gitterwand eine exakte, nur verschobene Nullstelle behalten,
  wie bei X > 0. Nicht gerechnet.
- Vorschlag: "For an axis-aligned planar wall on a nearest-neighbour stencil the discrete dispersion
  $E^2=1+(4/h^2)\sin^2(qh/2)$ has a single propagating branch in the Brillouin zone, so this high-$q$ channel is an
  artefact of truncating the dispersion at fourth order. The calculation constrains the continuum model, not the
  lattice itself."

**B7. Der Mechanismus ist Lehrbuchstoff und braucht einen Beleg.** Ohne Zitat liest er sich als neuer Befund.
- [S] VP Latten L4: Abstrahlung jenseits aller Ordnungen mit exp(-Polabstand x Wellenzahl) behandeln
  Pomeau/Ramani/Grammaticos (KdV 5. Ordnung) und Boyd, "Weakly Nonlocal Solitary Waves and Beyond-All-Orders
  Asymptotics" (1998). Beides ist als [L?] markiert, also aus dem Gedaechtnis.
- Vorschlag: "This is the standard beyond-all-orders radiation of weakly nonlocal solitary waves~\cite{...}". Das Zitat
  erst nach Lesen der Primaerquelle setzen. Ich habe es nicht geprueft.

**B8. Der Evidenzgrad fehlt.** Das Papier trennt sonst sorgfaeltig Eigenrechnung und unabhaengige Pruefung (ME Z.
330-333, Abschnitt "Evidence hierarchy").
- [S] VW und VP Latten L2: "Kein zweites Haus". VP prueft intern mit zwei Genauigkeiten, zwei Schrittweiten und drei
  Gebietslaengen; im schwanzfreien Modell D stimmt VP mit VW auf 1,8e-6.
- Vorschlag (Satzanfang): "In exploratory single-implementation calculations, with internal precision, step and domain
  controls but no independent replication, ...". Die Pfade gehoeren in die Provenienztabelle (ME ab Z. 517).

### C (kann)

**C1. "<= 2.5e-15" ist als Schranke knapp falsch.** Das Maximum betraegt 2,505385e-15 (VW
`.urteile.V1.werte[5].restgroesse_rel`, eps = +1e-2, B). Vorschlag: "below $3\times10^{-15}$" (so in B3).

**C2. "within 0.28 %" ist knapp falsch und verschweigt das Vorzeichen.** Der Wert ist -0,2804 % (Z15). Vorschlag:
"$0.28\,\%$ below $\pi$" (so in B5).

**C3. "isotropic term $\epsilon\partial_x^4$" ist in 1D ein schiefer Begriff [M][ES].** Entwurf Z. 21 und 39 f.
- Fuer die Wandnormale n wird jeder Viertordnungsterm, auch der anisotrope Stencilterm sum_i d_i^4, zu
  (sum_i n_i^4) d_n^4.
- Die ebene Reduktion kann isotrop und anisotrop also nicht unterscheiden. Ihr fehlt die Winkelkopplung (cos 4 theta,
  cos 6 theta), auf die sich die Deutung des Papiers stuetzt (ME Z. 454-458).
- Vorschlag: "the planar reduction of an isotropic fourth-order term". Statt "These one-dimensional results concern
  isotropic dispersion changes only": "The planar reduction contains no angular coupling and therefore cannot represent
  the anisotropic mechanism invoked above."

**C4. -h^2/12 ist der 1D-Dreipunktwert, nicht der isotrope Anteil der Papier-Stencils [M][ES].**
- Fuenfpunkt: (h^2/12)(k_x^4 + k_y^4) = (h^2/12) k^4 (3/4 + cos(4 theta)/4). Der isotrope Anteil ist h^2 k^4/16.
- Siebenpunkt-Dreieck: (2/(3h^2)) x (h^4/24) x (9/4) k^4 = h^2 k^4/16, isotrop. Ueber sechs Richtungen gilt
  sum cos^4 = 6 x 3/8 = 9/4.
- Bei beta = 1 waere der Exponent also 2 pi x 4/h = 25,1/h. Den gewichteten Neunpunkt-Stencil habe ich nicht
  hergeleitet, seine Gewichte kenne ich nicht.
- Stuetzendes Argument [ES]: Der Dreiecks-Stencil hat einen solchen isotropen O(h^2)-Term, seine Breiten skalieren aber
  wie h^8 (ME Z. 452 f.). Das passt zur Aussage des Absatzes. Codex sollte das gegen die Stencil-Definitionen pruefen,
  bevor es in den Text geht.

**C5. "Fixed-point Taylor integration" laesst sich als Fixpunktiteration lesen.** Vorschlag: "Taylor-series
integration in fixed-point arithmetic with 133 and 200 bits (about 40 and 60 decimal digits)".

**C6. Die Verschiebungsformel gilt fuer beide Vorzeichen.** Sie stammt aus +-1e-3 (VW Tab. 1, Fussnote). Fuer
eps < 0 ist rho_z die reelle Nullstelle von E; eine Mischung aus alten und neuen Innenkanaelen bleibt dort exakt total
reflektiert (VW Ergebnis 3).
- Im Entwurf haengt die Formel am eps > 0-Satz. Vorschlag: ein eigener Satz vor "For $\epsilon>0$": "On both sides of
  $X=0$ the zero moves as ..."

**C7. Die schwaechste Numerikprobe nennen.** Die Gebietslaenge aendert ln P auf der 12. Stelle (VP Kontrollen,
7,3e-13 bei -2e-3). Vorschlag: "with $\ln P$ unchanged to at least 12 digits under changes of precision, step size and
domain length".

**C8. P ist keine Breite.** Der Abschnitt misst Gamma = -Im rho (ME Z. 449 f.), P dagegen ist ein Flussanteil je
Einfall. Der Entwurf vergleicht beides nicht zahlenmaessig, und das sollte so bleiben. Wer vergleichen will, braucht
eine Umrechnung, etwa ueber Gruppengeschwindigkeit und Laufweg einer Radialmode; die gibt es nicht.

## 3. Zahlentabelle

Abkuerzungen: VW = RUNDE-36/v1-weiter/, VP = RUNDE-37/v1-praezision/, WB = RUNDE-24/wand-beta/, ME = Papier I
(coordination/resonance-20260930/paper-v42-beta1/stage/main.tex), jq-Pfade auf lauf-69/auswertung.json.

| Nr | Wert im Text | Wert in der Quelle | Fundstelle | Urteil |
|---|---|---|---|---|
| Z1 | beta = 1 | beta = 1 (Quelle); Hauptmodell des Papiers beta = 1/2 | VP PLAN.md Z. 14; ME Z. 83 und 189 | richtig fuer die Quelle, aber nicht das Modell des Abschnitts (A3) [S] |
| Z2 | rho_z = 1.7734530718 | 1,7734530718; V0: 1,773453071806469; Papier: 1.77345307180 | WB ERGEBNIS Tab. Zeile beta = 1; VW `.urteile.V0.werte.rho_z_A`; ME Z. 372 | stimmt [S] |
| Z3 | "single silent frequency" | genau ein Vorzeichenwechsel von c_in im Fenster (1 - omega, 1 + omega), Abtastschritt 0,002; Papier: "neither counts all planar zeros" | WB KARTE Z. 27 f., 82; ME Z. 377-379 | zu stark (A5) [S] |
| Z4 | residual <= 2.5e-15 | 1,75e-17 (eps = +1e-2, A) bis 2,505e-15 (eps = +1e-2, B), relativ T_aus(rho_z)/T_aus(rho_z + 1e-3) | VW `.urteile.V1.werte[].restgroesse_rel`; VW ERGEBNIS Tab. 1 | gerundet richtig, als Schranke knapp falsch (C1); Groesse undefiniert (B3) [S] |
| Z5 | Steigung -3.749e-3 | -3,7486e-3; [M] (-3,743237e-6 - 3,753878e-6)/2e-3 = -7,497115e-6/2e-3 = -3,74856e-3 | VW ERGEBNIS Tab. 1 und Fussnote; `.urteile.V2.werte.d1e3_A` | stimmt [S][M] |
| Z6 | + O(eps^2) | +5,32e-3 eps^2; [M] (-3,743237e-6 + 3,753878e-6)/(2 x 1e-6) = 1,0641e-8/2e-6 = 5,32e-3 | ebd. | stimmt [M] |
| Z7 | eps > 0: kein neuer offener Kanal | "eps > 0 aussen ein laufender Kanal" | VW ERGEBNIS, Kontrollen, Kanalzahl | stimmt [S] |
| Z8 | eps < 0: "a second propagating channel" | "je Seite drei offene Kanaele (aussen B alt, A neu, B neu; innen e1 alt, e1 neu, e2 neu)", also zwei neue je Seite | VP PLAN.md Z. 18 f.; VW ERGEBNIS Kontrollen | falsch (A4) [S] |
| Z9 | k ~ abs(eps)^(-1/2) | bei eps = -1e-2: K_A = 10,0088, K_B = 9,6761 gegen 10,000 | VP ERGEBNIS Tabelle P(eps) | stimmt als fuehrende Ordnung [S] |
| Z10 | 40 und 60 Stellen | G 133 bit, H 200 bit; [M] 133 x 0,30103 = 40,04 und 200 x 0,30103 = 60,21 | VP ERGEBNIS Kontrollen | stimmt [S][M] |
| Z11 | P = 8.69e-17 bei eps = -1e-2 | 8,6866472e-17 (nur neue Aussenkanaele; P_neu_innen gleich gross) | VP `.tabelle.m1e-2.H.P_neu_aus`, `.P_neu_innen` | Zahl stimmt; Bedeutung siehe B4 [S] |
| Z12 | P = 1.55e-49 bei eps = -2e-3 | 1,5486e-49 | VP ERGEBNIS Tabelle P(eps) | stimmt [S] |
| Z13 | ln P auf >= 16 Stellen | float64-gleich; volle Ketten weichen hoechstens in der 17. Stelle ab (-2e-3: 5e-17 relativ); Gebietslaenge nur 12 Stellen | VP ERGEBNIS Ergebnis 1 und Kontrollen; `.tabelle.m1e-2.rel_lnP_H_G` = 0 | stimmt [S] |
| Z14 | d = 3.1328 | 3,1327843 (q = -2,0049, a = 14,4074, groesster Rest 0,0063) | VP `.ausgleich.FK_K_B` | stimmt [S] |
| Z15 | "within 0.28 %" von pi | d/pi - 1 = -0,0028038; [M] pi - d = 3,1415927 - 3,1327843 = 0,0088084, durch pi = 0,28038 % | VP `.ausgleich.FK_K_B.d_durch_pi_minus_1` | Zahl stimmt; "within" knapp falsch, Vorzeichen fehlt (C2); Vorbehalte fehlen (B5) |
| Z16 | K = Wellenzahl des dominanten neuen Kanals | K_B, Kanal "B neu" (Seitenband rho + omega), Anteil 87,4 % (-1e-2) bis 69,4 % (-2e-3) | VP ERGEBNIS Tabelle P(eps) und Ergebnis 3 | stimmt [S] |
| Z17 | S(x) = (1/2)[1 + e^(-x)]^(-1), Pole im Abstand pi | Quelle: S = S_c/(1 + e^(x/sqrt beta)), f(-inf) = f_c, f(+inf) = 0, f0 = sqrt(S_c/(1 + e^x)); Papier: S(x) = [1 + exp(sqrt2 x)]^(-1) bei beta = 1/2 | VW ERGEBNIS Z. 155 f.; VP PLAN.md Z. 15 und 40; ME Z. 289-293 und 323 f. | Abstand pi und S_c = 1/2 stimmen [M]; Orientierung gespiegelt (B2) |
| Z18 | Schwanzwahl "a few per cent" | Einfluss "nicht gemessen"; FD A gegen B 6 %; Ende 47 gegen 90: 27 %; -7,4 % bzw. -1,4 %; gegen Modell D Faktor 1,83 bis 2,22 | VP ERGEBNIS Vermerk PR0, Selbstanzeige 6, Zusatz Modell D; RUNDE-37.md Z. 109 | nicht gedeckt (A1) [S] |
| Z19 | eps = -h^2/12 | "etwa -h^2 k^4/12 (QBALL-GITTER-1)" | VW KARTE Z. 7 | stimmt fuer das 1D-Dreipunktgitter [M]; Papier-Stencils siehe C4 |
| Z20 | exp(-21.8/h) | [M] 2 pi sqrt12 = 6,28319 x 3,46410 = 21,766 | RUNDE-36.md Z. 389 | stimmt als Exponentialfaktor |
| Z21 | "about 10^-95" bei h = 0,1 | [M] Exponentialfaktor 10^-94,53 = 3e-95; Ausgleich FK hochgerechnet 10^-81,6, F1 10^-81,5 (Rechenweg in A2) | VP `.ausgleich.FK_K_B`, `.ausgleich.F1` | als Schaetzung von P um ~13 Zehnerpotenzen zu klein (A2) [M] |
| Z22 | neuer Ast ausserhalb der Brillouin-Zone | [M] sqrt12/h = 3,46/h > pi/h = 3,14/h | VW ERGEBNIS Ergebnis 5 | stimmt [S][M] |

## 4. Rueckwaerts: Vorbehalte der Quellen

Jeder Vorbehalt der Quellen und ob der Absatz ihn traegt:

| Vorbehalt in der Quelle | Fundstelle | Im Absatz? | Befund |
|---|---|---|---|
| PR0 nicht eingetroffen: -7,4 % gegen FD-A; Ursache Schwanzwahl, Einfluss nicht gemessen | VP Urteile, Vermerk PR0, Selbstanzeige 6 | nein; stattdessen "a few per cent" | A1 |
| Hintergrund fuer eps < 0 ist ein Nanopteron, Schwanz ~exp(-pi k0) von der Ordnung des Lecks, Teil der Modelldefinition | VP PLAN Abschnitt 2 | nein | A1 |
| Ernte widerspricht sich: "nicht gemessen" (Z. 109) gegen "~6 % in P" (Z. 114) | RUNDE-37.md | Absatz folgt Z. 114 | A1 |
| Die Hochrechnung "~1e-95" stammt aus der Zeit vor V-1-PRAEZISION, ohne Vorfaktor | RUNDE-36.md Z. 389 | uebernommen | A2 |
| Nur ebene Wand, beta = 1, 1D; Papier-Hauptmodell beta = 1/2, Gitterbreiten aus 2D-Radialmode | VW KARTE, VP PLAN Z. 14; ME Z. 83, 448 | "one-dimensional" ja, beta-Wechsel nein | A3 |
| Je Seite zwei neue Kanaele (A neu, B neu); P ist ihre Summe | VP PLAN Z. 18-22 | nein ("a second ... channel") | A4 |
| Eindeutigkeit der Nullstelle nur als Abtastbefund (Schritt 0,002) | WB KARTE Z. 27 f., 82; ME Z. 377-379 | nein ("single") | A5 |
| P_neu_innen = P_neu_aus | VP unter Tabelle P(eps); VW Z. 93 | nein | B4 |
| PR1 nicht eingetroffen: c = 6,149, 2,1 % unter 2 pi | VP Urteile, Vermerk PR1 | nein; die h-Formel nutzt genau diese Kurzform | B5 |
| PR2 nur knapp; haengt an K = K_B; 0,28 % "teils Mischungsglueck" | VP Vermerk PR2 | nein | B5 |
| Vorfaktor ohne festes q (-0,4 bis -2,0); systematisches Restmuster, Ursache offen | VP Ergebnis 5, Ausgleich | nein | B5 |
| Neuer Ast ausserhalb der Brillouin-Zone, echtes Gitter nicht gezeigt | VW Ergebnis 5 | ja | verschaerft in B6 [ES] |
| Bekannte Physik (Boyd, Pomeau u. a.), nur [L?] | VP und VW Latten L4 | nein | B7 |
| Kein zweites Haus | VW und VP Latten L2 | nein | B8 |
| eps > 0 nur bei 1e-3, 3e-3, 1e-2; Hochpraezision dort nur mit f0-Hintergrund | VW V1; VP Selbstanzeige 1 | Absatz nennt nur den float64-Wert, das ist richtig; Bereich fehlt | B3 |
| V3/V4 in V-1-WEITER nicht auswertbar; FD-Werte bei -3e-3 und -1e-3 waren Artefakte | VW Urteile, Selbstanzeige 3 | nicht verwendet, das ist richtig | - |
| Vorab-Auswertung: PR1-PR3 waren vor den Kontrollen bekannt; die K_B-Wahl stuetzt sich auf V-1-WEITER-Daten | VP Selbstanzeigen 2 und 3 | nein | fuer das Papier unerheblich, nur Vermerk |
| Rein modellintern (L5 nein) | VW, VP Latten | im Abschnitt "Exploratory" implizit | - |

Ergebnis rueckwaerts [ES]: Der Absatz glaettet an drei Stellen in dieselbe Richtung, naemlich zu mehr Sicherheit:
- Schwanzwahl: "nicht gemessen" wird zu "a few per cent".
- Polabstand: "knapp, teils Glueck" wird zu "within 0.28 %".
- Gitterfolge: Ein Vorfaktor von 10^13 faellt weg.

Keine der beiden gescheiterten Vorhersagen (PR0, PR1) ist erkennbar. Fuer ein Papier muss nicht jede Vorhersage
genannt werden. Die Sachverhalte dahinter gehoeren aber hinein: Schwanzabhaengigkeit und K-Wahl.

## 5. Form: LaTeX und Einpassung in Papier I

**LaTeX (Entwurf Z. 19-43) [S]:**
- Dollarzeichen: In jeder Zeile steht eine gerade Anzahl (2, 4 oder 6), jedes Paar schliesst in derselben Zeile.
  Geprueft mit `sed -n '19,43p' | tr -cd '$\n'`.
- Kein Nicht-ASCII-Zeichen, kein "$(", kein Backtick, kein "\\".
- Befehle vollstaendig und Standard: \paragraph, \beta, \rho_z, \epsilon, \partial_x, \omega, \le, \times, \simeq,
  \ln, \propto, \exp, \pi, \tfrac, \sim, \, und \% im Mathemodus. \tfrac braucht amsmath; das laedt ME Z. 4.
- Reste der Beschaedigung: keine sichtbar.
  - Die Berichtigung nennt "$k", "$8", "$P", "$K", "$d", "$S", "$h" und "$0"; alle sind wieder da.
  - Ein ungequoteter Heredoc haette auch "$1" in "$1.55" und "$10^{-95}" geleert. Beide stehen heute richtig da, und die
    Zahlen stimmen mit der Quelle (Z12, Z21).
  - Ob der Wortlaut ausserhalb der Zahlen dem urspruenglichen Text entspricht, kann ich nicht pruefen (Abschnitt 6).
- Uebersetzt habe ich nichts (keine Laeufe).

**Einpassung [S]:**
- Stelle: Der Absatz gehoert ans Ende des Unterabschnitts "Exploratory sensitivity to the numerical lattice" (ME
  Z. 446-467), vor "Remaining mathematical and experimental tasks" (Z. 469). Dort bezieht sich "reported above"
  richtig auf die h^4- und h^8-Breiten in Z. 451-453.
- \paragraph mit Punkt am Titelende passt zum Stil von Z. 419 ("An additional radiation channel.").
- "anisotropic stencil terms" passt zu "leading anisotropic operator correction" (Z. 457).
- Notation: Kollisionen bei epsilon, omega und k sowie der fremde Begriff "silent" (B1); gespiegeltes S(x) (B2);
  beta-Wechsel ohne Kennzeichnung (A3).
- Der Unterabschnitt schliesst mit "They motivate explicit stencil and resolution checks before angular radiation
  patterns are interpreted as physical structure." Ein Absatz zu isotropen Termen danach ist folgerichtig. Er darf die
  Winkeldeutung aber nicht staerker stuetzen, als die ebene Reduktion kann (C3).
- Provenienz: Fuer VW und VP fehlt ein Eintrag in der Tabelle ab ME Z. 517 (B8).

## 6. Nicht geprueft

- Die Peerbus-Nachricht von 01:46Z, die Quelle der Wiederherstellung, habe ich nicht gelesen (feste Regel: kein
  Peerbus). Die Zahlen habe ich gegen die Ergebnisdateien geprueft, den uebrigen Wortlaut gegen nichts.
- Die von der Karte verlangte jq-Rechnung zu 10^-95 lief nicht auf dem Rechner. Die festen Pruefer-Regeln verbieten
  Rechnungen dort; ich habe stattdessen im Kopf gerechnet, mit Rechenweg in A2 und Z21.
- Literatur (Boyd 1998; Pomeau/Ramani/Grammaticos) nicht an der Quelle geprueft.
- In auswertung.json habe ich nur Stichproben gelesen: VW `.urteile` V0 bis V3, VP `.ausgleich` und
  `.tabelle.m1e-2`. Die uebrigen VP-Tabellenwerte stammen aus ERGEBNIS.md. Code und Einzel-JSONs (K_H_*, A_*, B_*)
  habe ich nicht geoeffnet.
- Dass die 2D-Gitterbreiten des Papiers zum Hauptmodell beta = 1/2 gehoeren, habe ich aus ME Z. 189 und 448 erschlossen
  ("seventh radial location"). Die 2D-Rohdaten habe ich nicht geoeffnet.
- Das Gewicht des Neunpunkt-Stencils und damit dessen isotropen Viertordnungsterm kenne ich nicht (C4).
- WAND-BETA: nur KARTE.md und ERGEBNIS.md gelesen, keine Laufdateien.
- Kein LaTeX-Uebersetzungslauf (keine Laeufe erlaubt).

## 7. Einfach gesagt

Der Absatz erklaert richtig, dass die stille Stelle der Q-Ball-Wand eine steifere Gleichung uebersteht und bei einer
weicheren nur winzig undicht wird. An einigen Stellen sagt er aber mehr, als die Rechnungen hergeben. Die Zahl fuer
ein Gitter (10 hoch minus 95) ist um etwa 13 Zehnerpotenzen zu klein, weil ein grosser Vorfaktor fehlt. "Ein paar
Prozent" fuer die Schwanzwahl wurde nie gemessen. Ausserdem rechnet der Absatz mit einem anderen Modellwert (beta = 1)
als der Rest des Papiers (beta = 1/2), ohne das zu sagen. Mit den fuenf Pflichtaenderungen kann Codex ihn verwenden.
