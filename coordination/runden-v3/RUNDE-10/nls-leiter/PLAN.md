# NLS-LEITER (Runde 10): Plan und Vorab-Erwartung

- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung claude-primary (Finn: "bekommen wir damit eine ueberleitung auf
  echte physik / experimente hin?"). Explorativ (v3). Werkzeug: Kopie von RUNDE-09/mess1/mess1.py.
- Auftrag erhalten und begonnen 2026-09-30 11:25:37 CEST (date). Dieser Plan geschrieben ab 2026-09-30 11:27:48 CEST
  (date), **vor jedem Lauf**. Gelesen bis dahin: G2-01/KARTE.md, Pego/Warchall (Text, Gl. 1.1/1.2, Einleitung, Anhang
  A.2), MODELL-DUENNWAND.md (Kopf, M.1, M.2 a bis c, Punkt 6).
- Markierungen: **[H]** Hypothese, **(Hand)** Schreibtischrechnung, **[A]** an der Quelle gelesen.

## 1. Modell

- Pego/Warchall (PW) Gl. (1.1), (1.2) [A]: -i u_t - Lap u = |u|^2 u - |u|^4 u. Stehende Welle u = e^{i Omega t} w(r):
  Lap w = Omega w - w^3 + w^5. Flachkuppe fuer Omega -> Omega_* = 3/16, w -> a_* = sqrt(3)/2 [A]. Wesentliches
  Spektrum der Linearisierung: |tau| >= Omega [A].
- Umrechnung in die MESS-1-Form (Hand): Zeit t' = 2 t gibt i psi_t' = -1/2 Lap psi + F(|psi|^2) psi mit
  F(n) = (-n + n^2)/2 und mu' = -Omega/2. Damit:
  - D = (n F)' - mu' = -n + 1,5 n^2 - mu',  C = n F' = -0,5 n + n^2
  - BdG-Energie eps' = nu/2 (nu = Frequenz in PW-Einheiten). Kanal u offen fuer nu > Omega, Kanal v immer geschlossen.
  - Die Raumkoordinate bleibt die von PW.
- Dimension d = 3 und d = 2, l = 0, reduziert U = r^((d-1)/2) u. Fuer d = 2 exakte Hankel- und K-Funktionen aus scipy
  (1.17 lokal, 1.18 auf der .69) statt der abgebrochenen Reihe.

## 2. Vorab-Erwartung (vor jedem Lauf)

**Kern [H], aus dem Duennwandbild (Hand):**
- Ein stiller Ast braucht einen an die Wand gebundenen Zustand des geschlossenen Kanals v, also W = D + eps' < 0 in der
  Wand bei eps' > -mu' (offener Kanal).
- D hat sein Minimum bei n = 1/3: (nF)'_min = -1/6. Also W_min = -1/6 + |mu'| + eps' > -1/6 + 2 |mu'| = -1/6 + Omega.
  - Flachkuppe (Omega -> 3/16): W_min > +0,021. **Der Kanal v ist ueberall verboten, einen Wandtopf gibt es nicht.**
  - Ebene Kinkwand bei Omega_* (Hand): n(x) = (3/4)/(1 + exp(sqrt(3) x/2)); Innen W = 0,1875 + eps', aussen
    3/32 + eps', Minimum 0,0208 + (eps' - 3/32) > 0.
  - Ein Topf W < 0 gibt es nur fuer Omega < 1/6 und nu/2 < 1/6 - Omega/2, hoechstens 1/6 - Omega tief. Die
    Nullpunktsenergie der Wandmulde ist ~0,1 (Hand, bei Omega = 0,16: W''_x = 3 (dn/dx)^2 = 0,041, E_0 = sqrt(0,041)/2);
    sie ist groesser als jede moegliche Tiefe (<= 0,02 im Flachkuppenbereich). Kein gebundener Wandzustand.
- **Erwartung: nein, keine stillen Stellen (Umlauf +-1) der l = 0-Atmung, weder in 3D noch in 2D** (Wahrscheinlichkeit
  ~85 %). Grund wie bei MESS-1: Der geschlossene Kanal liegt nichtrelativistisch um mindestens 2|mu'| = Omega tief, der
  Wandtopf ist nur 1/6 tief. Beim Klein-Gordon-Q-Ball ist der geschlossene Kanal der Zweig bei omega - rho ~ -omega
  (rho ~ 2 omega), knapp unter der Massenluecke; diesen Zweig gibt es im NLS nicht.
- Knapp: Die Marge ist beim CQ-NLS mit 0,021 viel kleiner als beim Petrov-Troepfchen (0,18). Falls doch Stellen
  auftauchen, dann bei Omega < 1/6 und nu knapp ueber Omega.
- **Falls ja, wo (Phasenregel) [H]:** k R = pi (n + theta) mit der Innenwellenzahl der propagierenden Mischmode,
  k^2 = 2 (sqrt(eps'^2 + c^4) - c^2), c^2 = 0,1875 (Flachkuppe). Bei nu = 0,2 (eps' = 0,1): k = 0,22, Abstand der
  Stellen in R etwa 14; bei nu = 0,6: k = 0,58, Abstand etwa 5,4. Radius (PW A.22, m = 0) [A]:
  R_2D = sqrt(3)/(8 (3/16 - Omega)), in 3D etwa das Doppelte (Hand).

**Weitere Vorhersagen:**
- V1 Profile gegen PW: w(0) -> a_* = 0,8660 fuer Omega -> 3/16; 2D-Kinkradius (w = a_*/2) bei Omega = 0,17 / 0,175 /
  0,18 innerhalb +-1,5 von sqrt(3)/(8 (3/16 - Omega)) = 12,4 / 17,3 / 28,9.
- V2 Atmung (l = 0): Fuer Flachkuppen in 2D und 3D unter der Schwelle (gebunden, nu < Omega), wie grosse Troepfchen.
  In 3D ein Fenster mittlerer Omega, in dem sie ueber der Schwelle liegt (Wahrscheinlichkeit ~70 %); in 2D offen (~50 %).
- V3 Wo die Atmung ueber der Schwelle liegt: breit (Guete <= 5), glatt, ohne Einbruch.
- V4 W-Gitter in (nu, Omega), nu von Omega bis 1: keine Zelle mit Vorzeichenwechsel beider Komponenten, 3D und 2D,
  zwei Gitterstufen.

**Scheiterregel:** Die Kern-Erwartung scheitert, wenn eine W-Zelle mit Umlauf +-1 auftaucht, die auf der zweiten
Gitterstufe und auf einem eigenen kleinen Rechteck bestehen bleibt (3D oder 2D, nu > Omega). Dann rechne ich Lage,
Phasenregel und Laborgroessen.

## 3. Kontrollen

- K1 Zaehlmaschine: Q-Ball-Positivkontrolle wie MESS-1 (bekannte Stelle omega*^2 = 0,797677, rho* = 1,7446: Umlauf +1;
  Nachbarkasten 0), mit dem geaenderten Code.
- K2 Profile gegen PW (V1) und Norm N(Omega) monoton steigend (PW: stabil fuer dN/dOmega > 0) [A, PW Abschnitt 5].
- K3 Zwei Gitterstufen (h = 0,02 und 0,01) fuer W; 2D-Randfunktionen exakt (scipy).
- Grenze: Schiessen in doppelter Genauigkeit traegt bis R ~ 35 (Wachstumsrate auf der Kuppe sqrt(0,75) = 0,87, Hand):
  2D bis Omega ~ 0,181, 3D bis Omega ~ 0,175.

## 4. Laeufe

- Rauchtests lokal (CPU, 1 Thread, nice 19, timeout 120), Ausgaben lauf-lokal/.
- Messlaeufe .69 ueber kleintest.sh, Spuren p4000a, p4000b, cpu6, je hoechstens 10 min, Logs mit absolutem Pfad.

## 5. Nachtrag vor dem Lauf: Wandtopf-Kriterium fuer allgemeine konkurrierende Nichtlinearitaeten (2026-09-30 11:37:09 CEST, date)

- Geschrieben waehrend die CQ-NLS-Laeufe in der Warteschlange standen; die Rauchtests bis dahin (Profile, W auf 3 x 31
  Punkten, zwei Polsuchen) zeigten keine Stelle, die volle Rechnung lief noch nicht.
- **Kriterium (Hand):** F(n) = (-n^p + n^q)/2 (fokussierend p, defokussierend q > p). Flachkuppe n_*^(q-p) =
  p (q+1)/(q (p+1)), mu_* = F(n_*); (nF)' minimal bei n_m^(q-p) = p (p+1)/(q (q+1)). Der geschlossene Kanal kann knapp
  ueber der Schwelle in der Wand erlaubt sein (W_min < 0), wenn (nF)'_min < 2 mu_*, gleichwertig
  ((p+1)/(q+1))^(2p/(q-p)) > 2/(p+1)^2.
  - kubisch-quintisch (p = 1, q = 2): 0,444 < 0,5, kein Topf (Marge wie oben 0,021)
  - Petrov-EGPE (p = 1, q = 3/2): 0,410 < 0,5, kein Topf (MESS-1)
  - kubisch-septisch (p = 1, q = 3): 0,5 = 0,5, Grenzfall
  - **quintisch-septisch (p = 2, q = 3): 0,316 > 0,222, Topf vorhanden** (Tiefe bis 0,037 unter null bei der
    Flachkuppe, Omega_* = 64/729 = 0,0878 in der PW-artigen Normierung -i u_t - Lap u = |u|^4 u - |u|^6 u)
- **Zusatzhypothese [H], vorab:** Das quintisch-septische NLS ist der einfachste nichtrelativistische Kandidat fuer eine
  stille Leiter. Erwartung: Stellen moeglich, aber nicht sicher (Wahrscheinlichkeit ~35 %), weil der Topf flach ist und
  die Nullpunktsenergie ihn aufzehren kann. Falls es sie gibt, dann nahe der Schwelle (nu/2 zwischen |mu'| und
  0,125 - |mu'|, also nu knapp ueber Omega) und im Flachkuppenbereich.
- Umsetzung als eigene Datei nls2.py (Modellschalter --modell qs), damit die laufenden nls1.py-Rechnungen unberuehrt
  bleiben. Scheiterregel wie in Abschnitt 2, getrennt fuer das Zusatzmodell.
