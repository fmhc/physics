# G2-07 Vierer-Ring als Gitter im Anti-Kontinuum-Limes: Zerfallsrate wie die Wurzel der Tunnelkopplung

- **Hypothese [H]:** Der Ladungstausch, der den Vierer-Ring aus Q-Baellen mit Phasenschritt pi/2 zerstoert, ist
  eine diskrete Modulationsinstabilitaet im Grenzfall schwacher Kopplung. Ihre Rate waechst wie die Wurzel aus
  Tunnelkopplung mal Nichtlinearitaet, gamma ~ sqrt(J), mit J ~ exp(-kappa d) und kappa = sqrt(1 - omega^2).
  Daher gilt d ln(gamma)/dd = -kappa/2.

- **Papier vorab [S]:**
  - Bild aus Gittern mit Tunnelkopplung (Wellenleiter-Arrays, Kondensate in optischen Gittern):
    - In jedem Topf sitzt ein Kondensat, die Toepfe sind schwach gekoppelt (J).
    - Die Energie eines Topfes haengt nichtlinear von seiner Besetzung ab (U).
    - Ist J klein gegen U n (Anti-Kontinuum-Limes), wachsen Tausch-Instabilitaeten mit gamma ~ sqrt(J U n), nicht
      mit J.
  - Bei uns:
    - J ist der Ueberlapp der Ballschwaenze, ~ exp(-kappa d), mit d = Nachbarabstand.
    - U n ist die Frequenzverschiebung eines Balls mit seiner Ladung (d omega/dQ mal Q) und haengt nicht von d ab.
    - Also ln(gamma) = konst - (kappa/2) d.
  - Gegenmodelle mit anderer Steigung:
    - Tunnelrate selbst (gamma ~ J): Steigung -kappa
    - zweite Ordnung (gamma ~ J^2): Steigung -2 kappa
    - Beim Phasenschritt pi/2 verschwindet die Nachbarkraft erster Ordnung (cos(pi/2) = 0). Im einfachsten
      Nachbarmodell ist die Diagonal-Tauschmode dort in linearer Ordnung sogar neutral; die Rate muss aus weiteren
      Termen kommen (Bewegung der Baelle, Diagonalkopplung). Ein entarteter Fall mit gamma ~ J ist deshalb denkbar [S].
      Die Karte prueft nur die Skalierung, nicht den Mechanismus.
  - Anlass (vorhandene Rechnung, omega^2 = 0,70, ohne Symmetriezwang, kein Test):
    - Luecke 4: gamma = 0,0534, mittlerer Ringradius 5,891
    - Luecke 6: gamma = 0,0275, mittlerer Ringradius 7,595
    - Mittlerer Nachbarabstand d = sqrt(2) r: 8,331 bzw. 10,741
    - Steigung ln(0,0275/0,0534)/2,410 = -0,275; -kappa/2 = -0,274
  - Vorhersage fuer neue omega^2 (nicht gerechnet):
    - 0,80: kappa = 0,447, Steigung -0,224
    - 0,60: kappa = 0,632, Steigung -0,316

- **Kleiner Test:**
  - Code: Kopie von RUNDE-07/ring/ring.py, Unterbefehl vierer (Vierer-Ring aus m = 0-Baellen, Phase k pi/2, Klassen,
    Spreizung, gamma aus ln Spreizung, C4-Projektion fuer *_sym). Geaendert werden nur omega^2, die Lueckenliste, die
    Saat und die Auswertung der Steigung; neuer Code unter 1 h.
  - Laeufe grob (dx 0,3, dt 0,05, Box L = 38,4, T = 2000), jeweils mit Saat 1e-6 wie der vorhandene s1e-6-Lauf, damit
    die Anfangsamplitude bei allen gleich ist:
    - omega^2 = 0,80: Luecke 4 / 5 / 6 / 7
    - omega^2 = 0,60: Luecke 4 / 5 / 6
  - Gegenprobe: omega^2 = 0,80, Luecke 4 und 6, mit C4-Projektion (sym).
  - Fein (dx 0,2, dt 0,025): omega^2 = 0,80, Luecke 4 und 6.
  - Messung je Lauf:
    - gamma aus der Geraden ln(Spreizung) gegen t im Fenster Spreizung 1e-5 bis 1e-2
    - mittlerer Nachbarabstand d = sqrt(2) r_mittel vor dem Bruch
    - Klasse, t_Bruch, Drehrate
    - Steigung d ln(gamma)/dd je omega^2 als Ausgleichsgerade
  - Rechenort: .69, Spur p4000a oder p4000b, zwei Aufrufe (grob mit Gegenprobe, fein), je unter 10 min. Schaetzung aus
    dem vorhandenen Lauf (9 Laeufe bis T = 2000 in 178 s grob): grob etwa 3 min.

- **Vorhersage vorab:**
  - V1: Bei 0,80 liegt die Steigung d ln(gamma)/dd in [-0,268; -0,179] (-kappa/2 = -0,224, plus/minus 20 %).
  - V2: Bei 0,60 liegt sie in [-0,380; -0,253] (-kappa/2 = -0,316, plus/minus 20 %).
  - V3: ln(gamma) ist linear in d: Abweichung jedes Punktes von der Ausgleichsgeraden hoechstens 0,15.
  - **Scheitert, wenn:**
    - eine Steigung ausserhalb ihres Bandes liegt, etwa nahe -kappa (Tunnelrate) oder -2 kappa (zweite Ordnung)
    - V3 reisst
    - ein Ring ohne Symmetriezwang bis T = 2000 keinen Ladungstausch zeigt (dann fehlt der Messwert; "nicht
      entscheidbar", wenn es mehr als einen Punkt je omega^2 betrifft)
  - Zerfaellt der Ring vor dem Bruch anders, zaehlt der Punkt nicht, und das wird genannt: Er verschmilzt, oder er
    faellt auseinander (Nachbarabstand ausserhalb [0,8; 1,25] d_start).

- **Gegenprobe (Effekt muss verschwinden):** Mit C4-Projektion bei 0,80 (Luecke 4 und 6) bleibt die Spreizung bis
  T = 2000 unter 1e-8; kein Ladungstausch.

- **Plausibilitaetsschranke:**
  - Q, E und J der Box bis zum Bruch auf 1e-4 relativ erhalten (wie in den vorhandenen Bilanzen)
  - 0 < gamma < 1; Spreizung >= 0
  - Nachbarabstand bis zum Bruch in [0,8; 1,25] d_start
  - Drehrate |Omega| < 0,01
  - gamma(Saat 1e-6) passt zu t_Bruch: t_Bruch ungefaehr ln(0,1/Spreizung_Start)/gamma, auf 30 %

- **Latten erwartet:**
  - L1 ja: Die Steigung kann bei -kappa, -2 kappa oder anderswo liegen, und das bei zwei neuen omega^2.
  - L2: C4-Sektor.
  - L3: grob gegen fein bei 0,80, Luecke 4 und 6: gamma-Aenderung hoechstens ein Fuenftel.
  - L4 teilweise:
    - Modulationsinstabilitaet in Gittern und die Wurzelskalierung im Grenzfall schwacher Kopplung sind Standard.
    - Ringe aus Solitonen mit Phasentreppe gibt es in der Optik.
    - Die Uebertragung auf frei bewegliche relativistische Q-Baelle mit Tunnelkopplung ueber die Schwaenze habe ich
      nicht gefunden.
  - L5 nein: Modellaussage; die Laboranaloga (Wellenleiter, optische Gitter) sind nicht quantitativ angeschlossen.

- **Einfach gesagt:** Vier Q-Baelle im Quadrat, deren Phasen um je eine Vierteldrehung versetzt sind, ziehen sich weder
  an noch stossen sie sich ab. Sie halten deshalb lange zusammen, bis ein Ball-Paar langsam dem anderen die Ladung
  abnimmt. Solche Tauschvorgaenge kennt man aus Lichtleitern und Atomgittern, und dort gilt eine einfache Regel: Die
  Geschwindigkeit waechst mit der Wurzel der Kopplung. Wenn das auch fuer Q-Baelle gilt, koennen wir vorhersagen, wie
  schnell der Ring bei anderen Ballgroessen zerfaellt, wenn man die Baelle weiter auseinanderstellt.

- Karte geschrieben: 2026-09-30 11:03:24 CEST

- Vorhersage geschrieben: 2026-09-30 11:06:31 CEST
