# V-1-WEITER: Plan des Code-Agenten (Runde 36)

- Code-Agent fuer die Leitung claude-primary. Plan geschrieben ab 2026-10-04 00:29 CEST (date: 00:28:26 kurz vorher).
  Start der Arbeit 2026-10-03 23:52:19 CEST, Zeitbox 150 min bis 02:22 CEST.
- Grundlage: KARTE.md (unveraendert), WAND-BETA (RUNDE-24/wand-beta/: KARTE, ERGEBNIS, code/wand_beta.py,
  code/fd_schiessen.py, lauf-69/b1.json).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese, **[F]** Festlegung des Code-Agenten
  (von der Karte offen gelassen, hier vor dem Einfrieren festgelegt).
- Code: code/v1w.py (eine Datei). Rechnungen nur auf der .69, Spur p4000a, ueber kleintest.sh.

## 1. Gleichungen [M]

- Feldgleichung: phi_tt - phi_xx + eps phi_xxxx + U'(|phi|^2) phi = 0, U = S - S^2 + beta S^3, beta = 1.
  Vakuum: omega^2 = 1 + k^2 + eps k^4 (wie Karte).
- **Hintergrund** phi = f(x) e^{i omega t}, omega = omega_min = sqrt(1 - 1/(4 beta)) = 0,8660254:
  eps f'''' - f'' + (U'(f^2) - omega^2) f = 0, f(-inf) = f_c = sqrt(S_c), S_c = 1/(2 beta), f(+inf) = 0.
  - Erhaltene Groesse H = -f'^2 + 2 eps f' f''' - eps f''^2 + U(f^2) - omega^2 f^2. An beiden Enden H = 0 genau bei
    omega_min, fuer jedes eps. f_c bleibt Ruhepunkt. Damit gibt es die Wand bei omega_min auch mit eps (eps > 0:
    2+2-dimensionale Mannigfaltigkeiten in der 3-dimensionalen Niveauflaeche, generisch) [M].
  - eps < 0: an beiden Ruhepunkten zwei rein imaginaere Eigenwerte (statischer Kurzwellenast k0 ~ 1/sqrt|eps|). Eine
    exakt lokalisierte Wand ist dann nicht generisch; die Abweichung ist ein Schwanz der Groesse ~exp(-pi k0 sqrt(beta))
    (Nanopteron) [L?]. Fuer |eps| <= 1e-2 ist das <= ~1e-12 und liegt an oder unter der Rechengenauigkeit.
    Wir rechnen die Wand ohne Schwanz (Randbedingungen unten).
- **Schwankungen** phi = e^{i omega t}(f + A e^{i rho t} + B e^{-i rho t}), A, B reell:
  eps Z'''' - Z'' + V(x) Z = 0, Z = (A, B), V = [[W - (rho - omega)^2, C], [C, W - (rho + omega)^2]],
  W = 1 - 4S + 9 beta S^2, C = -2S + 6 beta S^2, S = f^2. Der eps-Term wirkt auf beide Komponenten gleich.
  Bei eps = 0 ist das genau WAND-BETA (zweite Ordnung, 4-dimensionales System).

## 2. Kanaele, Randbedingungen, Normierung [M]

- Mode Z = u e^{lam x}, u Einheits-Eigenvektor von V(+-inf) mit Eigenwert mu: eps lam^4 - lam^2 + mu = 0,
  lam^2 = 2 mu/(1 + sqrt(1 - 4 eps mu)) (alter Zweig, ~ mu) oder (1 + sqrt(1 - 4 eps mu))/(2 eps) (neuer Zweig).
- Aussen (x -> +inf): V = diag(mu_A, mu_B), mu_A = 1 - (rho - omega)^2 > 0, mu_B = 1 - (rho + omega)^2 < 0.
  Innen (x -> -inf): Eigenwerte mu_1 < 0 (e1, laufend) und mu_2 > 0 (e2) von V(S_c) (wie WAND-BETA innen_moden).

| Seite | eps = 0 | eps > 0 | eps < 0 |
|---|---|---|---|
| aussen A | abklingend (q) | abklingend (q), abklingend schnell | abklingend (q), **laufend neu** |
| aussen B | laufend alt | laufend alt, abklingend schnell | laufend alt, **laufend neu** |
| innen e1 | laufend alt | laufend alt, abklingend schnell | laufend alt, **laufend neu** |
| innen e2 | abklingend (kappa) | abklingend (kappa), abklingend schnell | abklingend (kappa), **laufend neu** |

- Offene Kanaele: eps >= 0 je Seite einer (wie WAND-BETA), eps < 0 je Seite drei (Karte: neuer Kanal bei hohem k).
- Fluss: erhaltene Form J(Y,Z) = Y.Z' - Y'.Z - eps (Y.Z''' - Y'.Z'' + Y''.Z' - Y'''.Z) (dJ/dx = 0 fuer reelles,
  symmetrisches V). Fluss einer laufenden Mode: J(conj v, v)/(2i) = k + 2 eps k^3. Das Vorzeichen bestimmt die
  Laufrichtung; auf dem neuen Ast (eps < 0) ist sie dem Wellenvektor entgegengesetzt (k + 2 eps k^3 < 0).
- Eigenvektor-Vorzeichen fest (erste Komponente > 0), reelle Basis der laufenden Paare (Re, Im); alles stetig in rho.

## 3. Hintergrund numerisch

- Finite Differenzen 4. Ordnung (D2 5 Punkte, D4 7 Punkte, D1 5 Punkte), Gebiet [-40; 47], Gitter h.
- Randbedingungen: je drei Randpunkte f = f_c (links) bzw. f = 0 (rechts) (Abweichung der wahren Loesung dort
  ~e^{-40}).
- Translation: Phasenbedingung f(0) = f0(0) = sqrt(S_c/2) plus Hilfsparameter delta vor f' (Gleichung
  eps f'''' - f'' + delta f' + ... = 0); an der Loesung delta = 0 bis auf Abschneidefehler (Kontrolle).
- Newton mit Residuum in long double (Rauschen der 1/h^4-Schablone sonst ~1e-7), Korrektur per sparse LU in float64.
  Start eps = 0-Profil f0 = sqrt(S_c/(1 + e^x)), Fortsetzung in 5 gleichen eps-Schritten, je hoechstens 6 Newton-
  Schritte.
- Fuer die Schwankungen: f = f0 (analytisch) + quintischer Spline von f - f0. Bei eps = 0 genau f0 (wie WAND-BETA).

## 4. Lage der stillen Stelle: Stille-Funktion E(rho)

- Q_aus: Orthonormalbasis der aussen nur abklingenden Loesungen (kein laufender Anteil aussen): eps > 0 drei, eps = 0
  und eps < 0 eine Spalte. Integration von x_b = 43 nach x_m = 0.
- Q_innen: Orthonormalbasis der innen beschraenkten Loesungen (alle laufenden Paare + nach -inf abklingende): eps > 0
  fuenf, eps = 0 drei, eps < 0 sieben Spalten. Integration von x_a = -36 nach x_m = 0 (Gebiet wie WAND-BETA).
- **E(rho) = det[Q_aus | Q_innen]** (reell, stetig, |E| <= 1). E = 0 genau dann, wenn eine aussen nur abklingende Loesung
  innen beschraenkt ist [M]:
  - eps >= 0: das ist die Transmissionsnullstelle (T = 0). Bei eps = 0 ist es dieselbe Bedingung wie c_in = 0 in
    WAND-BETA (dort nur anders normiert).
  - eps < 0: Es gibt eine Mischung der drei Innenkanaele, die ganz zurueckgeworfen wird. Diese Bedingung ist ebenfalls
    eine reelle Gleichung in einem Parameter und bleibt deshalb bestehen [M]. Die Stille im Sinn der Karte (reiner
    alter Kanal, nichts nach aussen) ist damit nicht garantiert; das misst die Restkopplung (Abschnitt 5).
  - rho_z(eps) := Nullstelle von E.
- Stabilisierung: abschnittsweise DOP853 (rtol wie Variante, atol = 1e-3 rtol), nach jedem Abschnitt QR mit positiver
  Diagonale (Godunov/Conte). Abschnittslaenge 2 (eps <= 0) bzw. 12 sqrt(eps) (eps > 0, Wachstum <= e^12 je Abschnitt).
  Die verfolgten Unterraeume sind in Integrationsrichtung die dominanten (aussen: am staerksten nach innen wachsende;
  innen: am staerksten nach aussen wachsende), also stabil [M].
- **Suche** (Lehre aus WAND-BETA: keine Minimierung von T): Abtastung von E auf [rho_WB - 0,01; rho_WB + 0,01], 11
  Punkte (Schritt 0,002) mit rtol 1e-8, Vorzeichenwechsel, dann brentq (xtol 1e-14) mit der vollen Toleranz der
  Variante. Ohne Vorzeichenwechsel automatisch [rho_WB -+ 0,15], 61 Punkte.
  - rho_WB = 1,7734530718064692 (WAND-BETA lauf-69/b1.json).
  - Mehrere Nullstellen: gewertet wird die mit kleinstem |rho_z - rho_z(0)| **[F]**, alle werden berichtet.

## 5. Restgroesse und Restkopplung

- Streuung bei Einfall mit Fluss 1 im alten Innenkanal (e1, kleines k, nach rechts laufend). Aussen nur auslaufende und
  abklingende Moden, innen Einfall + zuruecklaufende + nach -inf abklingende. Gleiches QR-Verfahren; die Amplituden der
  laufenden Moden kommen aus dem Endblock der akkumulierten Dreiecksmatrix (laufende Spalten zuletzt).
- **Restgroesse R(eps)** **[F]**: T_aus(rho_z) / T_aus(rho_z + 1e-3), mit T_aus = Anteil des einfallenden Flusses, der in
  alle offenen Aussenkanaele geht. Fuer eps >= 0 ist T_aus = T aus WAND-BETA (dieselbe Groesse, "Durchlaessigkeit");
  der Nenner (~0,9999) macht sie relativ zur Durchlaessigkeit neben dem Einbruch.
- **Restkopplung in den neuen Kanal P_neu(eps)** (eps < 0) **[F]**: Flussanteil in die neuen Aussenkanaele (A neu + B neu)
  bei rho_z. Dazu berichtet: Amplituden, alter Aussenkanal T_alt(rho_z), Konversion in neue Innenkanaele, Verlauf bei
  rho_z +- 1e-6, 1e-5, 1e-3.
- **Aufloesung** **[F]**: P_neu(eps) gilt als aufgeloest, wenn (a) in Variante A die groesste Amplitude in einen neuen
  Aussenkanal bei 10-fach groeberem rtol um hoechstens 20 % abweicht und (b) Variante B auf 30 % mit A uebereinstimmt.
  Sonst "unter der Aufloesungsgrenze", Wert von A als obere Schranke.

## 6. Varianten und Konvergenzproben (Karte: zwei Gitterweiten bzw. Toleranzen)

- Variante A: h_bg = 0,0025, rtol = 1e-11. Variante B: h_bg = 0,005, rtol = 1e-10. (eps = 0: h_bg ohne Bedeutung.)
- Je Nullstelle zusaetzlich die Streuung mit 10-fach groeberem rtol (Aufloesungsprobe, Abschnitt 5).
- Kontrollen (berichten, kein Urteil): Hintergrund-Residuum (long double) und delta; Abweichung f - f0 (~eps);
  Flussbilanz T_aus + R_innen - 1 an allen Streupunkten (Erwartung <= 1e-6, sonst Selbstanzeige); Kanalzahl wie
  Tabelle; E(rho_z) klein gegen die Abtastwerte.

## 7. Urteilsregeln (mechanisch; Schwellen der Karte unveraendert)

- **V0**: eingetroffen, wenn |rho_z(0) - 1,7734530718064692| < 1e-8 in A und B; sonst nicht eingetroffen.
- **V1**: fuer jedes eps in {1e-3, 3e-3, 1e-2} und jede Variante (A, B): Vorzeichenwechsel von E gefunden und
  R(eps) < 1e-10. Alle sechs erfuellt: eingetroffen; sonst nicht eingetroffen.
- **V2**: r = (rho_z(3e-3) - rho_z(0)) / (rho_z(1e-3) - rho_z(0)) aus Variante A. 2,7 <= r <= 3,3: eingetroffen,
  sonst nicht eingetroffen. B wird berichtet; anderes Urteil aus B gibt einen Vermerk **[F]**.
- **V3** **[F]** (Karte: "keine exakte Stille; Restkopplung ungleich 0 und steigend mit |eps|"):
  - eingetroffen: P_neu fuer alle drei eps < 0 aufgeloest, > 0 und P(1e-3) < P(3e-3) < P(1e-2) (Betraege von eps).
  - nicht eingetroffen: aufgeloeste Werte, die nicht mit |eps| steigen.
  - nicht auswertbar: mindestens ein Wert unter der Aufloesungsgrenze und kein aufgeloester Widerspruch.
- **V4** **[F]** (Karte: "faellt schneller als jede Potenz, ln Rest ~ -c/sqrt|eps|"):
  - nur mit drei aufgeloesten Werten. p1 = ln(P(1e-2)/P(3e-3))/ln(10/3), p2 = ln(P(3e-3)/P(1e-3))/ln 3 (oertliche
    Potenzen); c1 = ln(P(1e-2)/P(3e-3))/(1/sqrt(3e-3) - 1/sqrt(1e-2)), c2 entsprechend fuer 3e-3/1e-3.
  - eingetroffen: p2 > p1 > 0 und |c1 - c2| <= 0,3 (c1 + c2)/2. Sonst nicht eingetroffen.
  - nicht auswertbar: weniger als drei aufgeloeste Werte.

## 8. Schreibtisch zur Aufloesung (vor den Hauptlaeufen) [H]

- Konversion vom alten in den neuen Kanal an einer glatten Wand: Fourier-Anteil des Profils beim Impulsunterschied
  dk = K - k (K ~ 1/sqrt|eps|, k ~ 2,4); Pole von S bei x = +-i pi sqrt(beta) geben Amplitude ~exp(-pi dk) mal
  Vorfaktor [M/H].
  - eps = -1e-2: dk ~ 7,6, Amplitude ~1e-10 bis 1e-9 (Fluss ~1e-19 bis 1e-18).
  - eps = -3e-3: dk ~ 16, Amplitude ~1e-21. eps = -1e-3: dk ~ 29, Amplitude ~1e-39.
- In float64 liegt die Rauschgrenze der Amplitude bei ~1e-13 bis 1e-11 (Rauchlauf r2). Erwartung: Nur eps = -1e-2 ist
  vielleicht aufloesbar; V3 und V4 werden dann "nicht auswertbar". Hoehere Genauigkeit (mpmath) fuer Hintergrund und
  Schwankungen passt nicht in die Zeitbox.

## 9. Zusatz (beschreibend, kein Urteil, nur falls Zeit bleibt)

- Variante A fuer eps in {-7e-3, -1,5e-2, -2e-2, -2,5e-2} (alle mit 4 |eps| |mu| < 1, also gueltige Kanaele).
- Mit allen aufgeloesten Werten (einschliesslich -1e-2): Anpassung ln P gegen 1/sqrt|eps| und gegen ln|eps|, Restfehler
  beider Formen. Das prueft die Form aus V4 im aufloesbaren Bereich; es ersetzt kein Urteil.

## 10. Rauchlaeufe vor dem Einfrieren (offengelegt)

Alle mit eps-Werten ausserhalb der Hauptliste, Fenster [rho_WB -+ 0,01] bzw. 0,05.

| Lauf | eps | h_bg, rtol | Ergebnis | Dauer |
|---|---|---|---|---|
| r1 | +2e-3 | 0,005, 1e-9 | rho_z - rho_WB = -7,476e-6; T_aus(rho_z) = 1,1e-15; Flussbilanz 1,5e-8 | 136 s |
| r2 | -2e-3 | 0,005, 1e-9 | +7,518e-6; T_alt = 5e-24; Amplitude neu 4e-11 bei rho_z, 3e-13 bei rho_z +- 1e-3 (Rauschen, resonant verstaerkt); Fluss 3e-13 | 69 s |
| r3 | +1,5e-3 | 0,0025, 1e-11 | -5,611e-6; T_aus = 1,1e-16; Flussbilanz 1,5e-8 (bei rho_z), 1e-10 daneben | 195 s |
| r4 | -1,2e-2 | 0,0025, 1e-11 | +4,577e-5; T_alt = 8e-25; Amplitude neu 6,95e-8 (B neu), 2,1e-8 (A neu) bei rho_z, bei 10-fachem rtol gleich auf 6e-8 relativ (aufgeloest); bei rho_z +- 1e-3 nur ~5e-10 (resonant verstaerkt); P_neu_aus = P_neu_innen = 1,878e-14 auf 9 Stellen; Fluss 1e-13 | 53 s |
| r5 | 0 (beta = 0,6) | -, 1e-11 | Pfad 2. Ordnung: rho_z = 1,60956; T_aus = 3e-25; Fluss 6e-15 | 6 s |

- Was die Rauchlaeufe schon zeigen: Die Verschiebung ist winzig (~ -3,7e-3 eps) und in r1/r3 linear; r1/r2 fast
  spiegelbildlich. Das nimmt V2 vermutlich vorweg; die Schwellen bleiben unveraendert.
- r4 zeigt: Bei eps ~ -1e-2 ist die Restkopplung in float64 aufloesbar und an der stillen Stelle resonant ueberhoeht
  (Wandzustand). Fuer -3e-3 und -1e-3 bleibt die Erwartung aus Abschnitt 8 (unter der Grenze).
- Nach r4: optionales 8. Argument beta (nur fuer r5, Hauptlaeufe beta = 1).
- Bei eps > 0 bleibt die Flussbilanz nahe rho_z bei ~1e-8, unabhaengig von rtol (Ursache nicht gefunden; die
  Restgroesse 1e-16 liegt weit unter der V1-Schwelle). Wird als Kontrolle berichtet.
- Nach r1: atol von 1e-300 auf 1e-3 rtol gesetzt (Ueberlaufwarnungen in der Schrittweitenwahl); nach r2: Probe mit
  10-fach groeberem rtol und Rueckfall auf weites Fenster eingebaut. Sonst keine Aenderung.

## 11. Laufplan

- Je Lauf ein eps und eine Variante, nacheinander auf p4000a (Rauchlaeufe: 70 bis 200 s je Lauf).
- Hauptliste: eps = 0, +1e-3, +3e-3, +1e-2, -1e-3, -3e-3, -1e-2, je Variante A und B (14 Laeufe).
- Danach Zusatz (Abschnitt 9), dann auswertung.json (jq, mechanisch nach Abschnitt 7) und ERGEBNIS.md.
- Abbruch laut Auftrag: wenn die Rechnung 4. Ordnung nach zwei ernsthaften Versuchen nicht stabil laeuft, "nicht
  gerechnet" mit Grund; dann Stoerungsrechnung erster Ordnung (nur Beschreibung).
