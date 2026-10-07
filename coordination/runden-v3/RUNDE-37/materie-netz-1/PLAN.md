# MATERIE-NETZ-1: Plan (Code-Agent, Runde 45, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 04:18:53 CEST (date). Plantext ab 04:37:04 CEST (date),
  vor jeder Rechnung mit Werten. Zeitbox 90 min, also bis 05:48:53 CEST; danach kein neuer Lauf.
- Grundlage: KARTE.md (MN0 bis MN2; Wortlaut, Schwellen und Wahrscheinlichkeiten unveraendert).
- Werkzeug: code/ew.py und code/tp.py unveraendert aus EINE-WELT-LOCH-1 (sha256 fa7b6417..., 419d7da6...),
  code/licht_netz.py unveraendert aus LICHT-FINN-NETZ-1 (98d3960a...). Neu: code/mn.py (Statik, Maxwell, Auswertung).
- Kennzeichen: [M] eigene Mathematik (vorab), [E] gerechnet, [P] Projektdatei, [ES] eigener Schluss, [F] Festlegung,
  [H] Hypothese. Alles ist synthetische Gitterrechnung, keine Messdaten.

## 1. Ableitbarkeitsprobe (vor jeder Rechnung)

### 1.1 Die Schreibtischformel von GAMMA-NETZ-L, selbst nachgeleitet [M]

- Lageenergie: Mit eps_e = 2 pi - Summe_t theta_t,e und B = l (Summe_t d theta/d l) l gilt fuer a_e = delta l_e/l_e
  zweiter Ordnung Summe_e l_e eps_e = -(1/2) a^T B a. Also -S_Regge = (1/2) a^T B a, positiv auf TT, negativ auf
  Eck-Skalierungen bei kleinem k [P, EINE-WELT-LOCH-1].
- Regel je Ecke: c_v^T a = Summe_{e an v} l_e delta eps_e (ew.py Z. 221-228). Aus der Codelesung: c = -B W, mit
  W[e, s] = 1, W[e, s2] = e^{i k.T_e} (Eck-Skalierung -> Kantendehnung). Das wird in mn.py je k nachgerechnet (K0).
- Takt: N_v = 1 + mu_v. Regge-Anteil im Ecktakt: S_N = Summe_e N_e l_e eps_e mit N_e = Mittel der zwei Eck-Takte. Der in
  mu lineare Teil ist -(kappa_g/2) Summe_v mu_v c_v^T a. Materie im Ecktakt: Summe_v (1 + mu_v) m_v.
  Also H = (kappa_g/2) a^T B a + Summe_v mu_v (-kappa' c_v^T a + m_v) mit kappa' = kappa_g/2. **Stimmt.**
- dH/da = 0: kappa_g B a = kappa' c mu = -kappa' B W mu, also B (kappa_g a + kappa' W mu) = 0.
  - Bei k != 0 ist ker B = Bild M. Beweis: Aus B v = 0 und v senkrecht zu Bild M folgt c^H v = -W^H B v = 0. Dann liegt v
    im physikalischen Raum, und dort ist B_phys positiv definit [P, an 4 095 k]. Widerspruch.
  - Damit a = -(kappa'/kappa_g) W mu + M xi. **Stimmt** (das Argument des Dossiers ist richtig).
- dH/dmu = 0: kappa' c^H a = m. Eingesetzt: (kappa'^2/kappa_g) W^H B W mu = m, also mu = -(kappa_g/kappa'^2) P^{-1} m
  mit P = -W^H B W. Bei kleinem k ist P positiv [P, M: B negativ auf Eck-Skalierungen], also mu < 0 nahe der Masse.
- gamma: Kantendehnung a_e = -(kappa'/kappa_g)(mu_v + mu_w). Mit Phi = mu und (1 - 2 Psi) dl^2, also delta l/l = -Psi:
  Psi_e = (2 kappa'/kappa_g) Phi_e. Also gamma = 2 kappa'/kappa_g, an jeder Ecke. **Stimmt.**
- Die Zerlegung a = W psi + M xi ist eindeutig, weil [W, M] bei k != 0 vollen Rang hat (aus Rang [c, M] = 40 [P]
  folgt das wie oben). psi ist also eichinvariant; gamma_S ist es auch.

### 1.2 Was daraus vorab folgt [M]

- **Statik haengt nicht von der Bewegungsenergie ab.** Bei p = 0 faellt A heraus; der statische Punkt erhaelt alle
  Zwangsbedingungen (p-dot = -dH/da = 0, a-dot = A p + c nu = 0 mit nu = 0). Paarung A1R1 und der Spur-Eichdefekt
  (eine Eigenschaft von A c_v) gehen in die statische Antwort nicht ein. Die Karte nennt das "nicht ableitbar"; nach
  dieser Rechnung ist es ableitbar.
- **gamma_S ist exakt 2 q an jeder Ecke** (q = kappa'/kappa_g): V1 gibt 1, V2 gibt 0. MN0 ist nach Plan und nach
  Kartenwortlaut (beide ueber gamma_S) vorab "eingetroffen", MN1 vorab "nicht eingetroffen". Gerechnet wird nur, ob die
  Identitaeten auf dem Gitter numerisch halten (K0, K1).
- **Fernfeld-Staerke unabhaengig von der Ecke der Quelle:** Der Nullvektor von P(0) ist die gleichfoermige
  Skalierung u = (1, ..., 1). Die Fernkopplung ist also u . m = Gesamtenergie. Erwartet: A(P0) = A(C1) = A(H0) = A(QB)
  bis auf Torus- und Rundungsreste.
- **V2 streng (kappa' = 0) hat keine Takt-Gleichung:** dH/dmu = m kann nicht null sein; mu ist dann ein Multiplikator
  ohne Gleichung. Ohne ein zusaetzliches Gesetz gibt V2 keine Newton-Anziehung. Siehe [F] in Abschnitt 2.
- **Nicht vorab:**
  - P an allen Gitter-k positiv (K2); daran haengt das Vorzeichen in allen Abstaenden (MN2).
  - Das Nahfeld von mu: 9 gestaffelte Takt-Moden mit Luecke (V: 10 Ecken je Zelle, eine weiche).
  - gamma_K, die kruemmungsbasierte Fassung, im Nahfeld.
  - Punkt gegen Q-Ball im Nahfeld.

### 1.3 Umsetzung von kappa' und kappa_g im Code [F]

- Rechnung mit Einheitskopplung G = kappa_g/kappa'^2 = 1. Je k != 0 das KKT-System (Eichwahl M^H a = 0):
  [B, -c, M; -c^H, 0, 0; M^H, 0, 0] [a_hat; mu; lambda] = [0; -m; 0].
  - "Quelle in der Eckregel": rechte Seite m in der Zeile c^H a_hat = m.
  - "Materie im Ecktakt": mu ist der Multiplikator, der m in H multipliziert (Zeile aus dH/dmu).
- Physikalische Raumantwort: a = q a_hat. V1: q = 1/2. V2: q = 0.
- Unabhaengig davon dieselbe Loesung ueber die Formel (mu = -P^{-1} m); Vergleich K1.

## 2. Varianten [F]

| Variante | Karte | Umsetzung |
|---|---|---|
| V1 | Energie in der Regel je Ecke, Materie und Regge im Ecktakt (kappa' = kappa_g/2) | q = 1/2, Takt aus dem KKT-System |
| V2 | Materie tickt nur im Ecktakt, Regel ohne Quelle (kappa' = 0) | Grenzfall q -> 0 bei fester Newton-Kopplung G: Takt aus derselben Regel, Raum antwortet nicht (a = 0) |

- Die V2-Umsetzung ist eine Festlegung [F]. Sie entspricht unendlich steifem Raum (kappa_g -> unendlich bei
  kappa_g/kappa'^2 fest), nicht woertlich kappa' = 0. Woertlich hat V2 keine Takt-Gleichung (1.2).
- Folge: mu ist in V1 und V2 gleich; gamma_V2 = 0 ist eine Identitaet.

## 3. Quellen, Gitter, Rand, Eichung

- **Netz:** gefuellt V (ew.baue('V'): 10 Ecken, 68 Kanten, 58 Tetraeder je Zelle). Gitterabstand l_P = sqrt2/4
  (Finn-Kante); alle Abstaende r in l_P.
- **Quellen** (Gesamtenergie je 1, G = 1):
  - Punkt P0 (Finn-Ecke, Untergitter 0), C1 (Lochmitte, 4), H0 (Sechseckmitte, 6).
  - Q-Ball QB: Papier I, f'' + 2 f'/r = (1 - omega^2) f - 2 f^3 + (3/2) f^5, omega = 0,8; Schiessen auf f(0)
    (scipy DOP853, Bisektion). Energiedichte rho = omega^2 f^2 + f'^2 + U(f^2). Eine Q-Ball-Laengeneinheit = 1 l_P.
    Mitte auf C1; m_v = rho(r_v) mal Eckvolumen (1/4 jedes anliegenden Tetraeders), normiert. Nur als Materie.
- **Gitter und Rand:** Torus aus L^3 primitiven Zellen, L = 16, 24, 32 (Bloch-Summe ueber alle L^3 Gitter-k). Der Torus
  ist bis r = L l_P eindeutig (halber kuerzester Superzellen-Vektor). k = 0 entfaellt: Das ist ein gleichfoermiger
  Gegen-Hintergrund. Im Kontinuum gibt er Phi = -A/r - (2 pi A/(3 V)) r^2 + C (V = Torusvolumen).
  - **Primaer L = 32**, Ersatz L = 24, falls L = 32 abbricht.
- **Eichung:** im KKT-System M^H a = 0. gamma_S und gamma_K sind eichinvariant (psi eindeutig, Fehlwinkel invariant).

## 4. Messgroessen und Definitionen

- **Lapse:** mu_v je Ecke (Takt-Stoerung). Fernfit ueber alle Ecken mit r in [0,25 L; 0,5 L]:
  mu = A f(r) + C mit f(r) = -1/r - (2 pi/(3 V)) r^2 (kleinste Quadrate). Zur Kontrolle ein freier Fit mit beta r^2.
  Newton-Verhaeltnis je Ecke: (mu_v - C)/(A f(r_v)).
- **Raum:** psi_v aus a_hat = W psi + M xi (Pseudoinverse); physikalisch q psi_v. Kantendehnung q a_hat.
- **gamma_S** (Kartenwortlaut "Eck-Skalierung"; GAMMA-NETZ-L 5.2): gamma_S,v = -2 q psi_v/mu_v je Ecke, nur wo
  abs(mu_v) > 1e-6 max abs(mu). Je Schale (Breite 0,5 l_P) die Steigung -2 q Summe psi mu / Summe mu^2.
- **gamma_K** (kruemmungsbasiert, Zusatzlesart, nur Punktquellen): Fehlwinkel der Loesung d_eps = -(B q a_hat)/l
  gegen die Fehlwinkel der Kontinuum-Metrik (1 - 2 Phi_ref) delta_ij mit gamma = 1, Phi_ref = A f(r).
  - Referenzdehnung: a_ref,e = -Mittel von Phi_ref laengs der Kante (geschlossen: arsinh-Formel fuer 1/r, Polynom fuer
    r^2), auf allen Kanten des Torus (kuerzestes Bild der Kantenmitte), FFT, dann B(k).
  - Kanten an der Quellecke bekommen 0. Ihr Einfluss reicht nur bis zu Kantenmitten r < 1,2 l_P, deshalb gamma_K erst
    ab r = 2 l_P.
  - Je Schale: gamma_K = q Summe d_eps d_ref / (A Summe d_ref^2). Fernwert ueber alle Kanten mit r_Mitte in
    [0,25 L; 0,5 L].
- **Vorzeichen:** Einsteins Vorzeichen = Takt nahe der Masse langsamer als fern (mu nahe < C); raeumlich (V1): Kanten
  nahe der Masse laenger (q psi > 0), beschreibend.
- **Nahfeld** r < 3 l_P; **Fernfeld** r in [0,25 L; 0,5 L] l_P (L = 32: [8; 16]).
- **Kontrollen:** K0 max abs(c + B W)/max abs(c); K1 mu(KKT) gegen mu(Formel), Rest der Zerlegung, abs(psi + mu)/abs(mu),
  KKT-Rest, M^H a; K2 kleinster Eigenwert von P relativ zum groessten an allen k, Zahl der k mit Eigenwert <= 0;
  Imaginaerteil nach der Ruecktransformation; weiche Richtung von P bei abs(k) = 1e-3, 2e-3 ([100], [110], [111]) durch k^2.
- **Q-Ball-Vergleich:** (mu - C)/(A phi_QB(r)) mit dem Kontinuum-Potential des Profils (Gesamtenergie 1, mit
  demselben r^2-Glied); Gitter-Summe der Energie gegen das Kontinuum-Integral.

## 5. Urteilsregeln (mechanisch in mn.py auswertung, primaeres Gitter)

**MN0** (Kontrolle, Fernfeld gamma = 1 +- 0,05 in V1 und 0 +- 0,05 in V2):
- Nach Plan: eingetroffen, wenn fuer alle vier Quellen jedes gamma_S,v im Fernband beider Varianten im Toleranzband liegt.
- Nach Kartenwortlaut: wie Plan, aber mit den Schalen-Steigungen der Fernschalen statt der Einzelecken.
- Zusatzlesart K (beschreibend vorab festgelegt): gamma_K-Fernwert der drei Punktquellen in V1 in 1 +- 0,05 (V2: 0).

**MN1** ([H], V1: Nahfeld r < 3 weicht um mehr als 10 % vom Fernwert ab):
- Nach Plan: eingetroffen, wenn fuer mindestens eine Quelle ein gamma_S,v mit r_v < 3 um mehr als 10 % vom Median
  des Fernbands abweicht.
- Nach Kartenwortlaut: dasselbe mit den Schalen-Steigungen (Schalen bis r = 3) gegen den Median der Fernschalen.
- Zusatzlesart K: eingetroffen, wenn eine gamma_K-Schale in [2; 3) l_P (Punktquellen) um mehr als 10 % vom
  gamma_K-Fernwert abweicht. Unter 2 l_P ist gamma_K nicht definiert (Abschnitt 4).

**MN2** ([H], Einsteins Vorzeichen in beiden Varianten):
- Nach Plan: eingetroffen, wenn fuer alle vier Quellen A > 0 und jede Ecke mit r < 3 mu_v < C hat.
- Nach Kartenwortlaut ("Takt verlangsamt nahe der Masse"): jede Ecke mit r < 3 hat mu_v < Median von mu im Fernband.
- Der Takt ist nach [F] in V1 und V2 gleich; das Urteil gilt fuer beide.

- Bedeutung der Ausgaenge: wie auf der Karte; nichts daran geaendert.
- Bricht der primaere Lauf ab, wird L = 24 primaer. Bricht auch der ab, sind die Urteile "nicht entscheidbar".

## 6. Maxwell (beschreibend, kein Urteil)

- licht_netz.maxwell_diamant (A auf Diamant-Bindungen, Fluss auf Sechsringen), K = C^H C. Gleichmaessige Streckung
  lambda in {1; 1,01; 1,1} bei gleichem Takt (N = 1), Richtungen [100], [110], [111], abs(k_Gitter) = 1e-3:
  - Einheitsgewichte (wie LICHT-FINN-NETZ-1): K unveraendert.
  - Gewichte aus Laengen (Hodge-Form): Bindungsgewicht = 3 V_e/abs(e)^2, Ringgewicht = 3 V_f/abs(f)^2 (V_e, V_f:
    Volumen je Bindung bzw. Ring, abs(e) Bindungslaenge, abs(f) Ringflaeche, alle aus der gestreckten Geometrie),
    normiert auf lambda = 1.
- Ausgabe: Tempo in Gitter-Einheiten (Kanten je Takt) und physikalisch (Laengen je Takt).
- Vorab [M]: Einheitsgewichte spueren die Streckung nicht (Gittertempo gleich, physikalisch mal lambda). Hodge-Gewichte
  geben Gittertempo durch lambda, physikalisch gleich. Lokal folgt fuer Licht mit Hodge-Gewichten n = lambda/N, also
  1 - (1 + gamma) Phi; mit Einheitsgewichten n = 1/N, also die halbe Ablenkung.

## 7. Agenten-Erwartungen (vorab; kein Kartenurteil)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| Z1 | K0, K1 <= 1e-9 an allen k | 90 % |
| Z2 | P an allen Gitter-k positiv definit (K2) | 70 % |
| Z3 | A gleich fuer alle vier Quellen auf 2 % (L = 32) | 75 % |
| Z4 | Newton-Verhaeltnis der Punktquellen bei r in [1; 2) weicht um mehr als 10 % von 1 ab | 60 % |
| Z5 | gamma_K in [2; 3) weicht um mehr als 10 % vom Fernwert ab (Zusatzlesart K von MN1) | 45 % |

## 8. Laeufe (.69, kleintest.sh, Spuren cpu5 und cpu10, je 1 Thread, <= 600 s)

| Lauf | Spur | Aufruf | Schaetzung |
|---|---|---|---|
| S16 | cpu5 | mn.py statik --L 16 --out lauf/statik-L16.json | 20 s |
| S24 | cpu10 | mn.py statik --L 24 --out lauf/statik-L24.json | 1 min |
| S32 | cpu5 | mn.py statik --L 32 --out lauf/statik-L32.json | 3 bis 4 min, < 1 GB |
| MX | cpu10 | mn.py maxwell --out lauf/maxwell.json | < 1 s |
| AW | cpu10 | mn.py auswertung --ein lauf/statik-L16.json lauf/statik-L24.json lauf/statik-L32.json --maxwell lauf/maxwell.json --primaer 32 --out lauf/auswertung.json --bild lauf/bild-materie-netz.png | < 10 s |

- Schaetzung aus Rauchlauf r1 (L = 4: k-Schleife 0,23 s fuer 63 k, also 3,6 ms je k; Vorbereitung 4,4 s).
- **Rauchlauf r1** (vor dem Einfrieren, Code b36984d3..., 02:36:16 bis 02:36:3x UTC, cpu5/cpu10, alle rc = 0):
  statik L = 4, maxwell, auswertung. Gelesen nur Rueckgabewerte, Laufzeiten, Speicher und JSON-Schluessel; keine
  Werte, keine Urteile. Das Bild r1-bild.png ist nicht angesehen.
