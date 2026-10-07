# QB-BS-2D: Ergebnis (Runde 37)

- Code-Agent fuer claude-primary. Start 2026-10-04 04:51:03 CEST; ERGEBNIS geschrieben ab 05:23:48 CEST (date).
- Plan eingefroren 05:16:50 CEST: PLAN.md.eingefroren-20261004-051650, Hashes in EINGEFROREN-20261004-051650.sha256.
  Code danach unveraendert (qbbs2d.py 69bace3e..., auswertung.py d6743320...; beim Laufstart auf der .69 geprueft).
- Hauptlaeufe auf der .69 ueber kleintest.sh, Spuren cpu und cpu6: 03:17:00 bis 03:19:26 UTC (05:17 bis 05:19 CEST),
  alle rc = 0, laengster Lauf 69 s.
- Kennzeichen: [S] an der Quelle (Projektdatei) gelesen, [L] Gedaechtnis, [L?] unsicher, [H] Hypothese,
  [ES] eigener Schluss. Alles ist eine synthetische radiale Rechnung im Modell B.5 (2+1), keine Messdatenbestaetigung.

## Ergebnis zuerst

1. **Der phasengekoppelte Verbund (G = 1) ist nicht gebunden, weder bei kappa = 1 noch bei kappa = 1/4.**
   - Der Verbund liegt ueber der getrennten Referenz (drehender Knoten plus l = 0-Q-Ball mit bester
     Ladungsteilung). E_mix - E_sep betraegt 8,2 bis 8,6 % von E_sep nach Kartenwortlaut bzw. 23,7 bis 24,0 %
     konservativ (kappa = 1) und 10,2 bis 11,1 % (kappa = 1/4).
   - Einen Mischzustand mit beiden Feldern gibt es im radialen Ansatz erst ab q = 72,5 (kappa = 1) bzw. q = 55
     (kappa = 1/4).
   - Darunter traegt der drehende Knoten die Ladung allein. Bei Omega^2 ~ 1 laeuft die Ladung als freie phi-Welle
     ins Rechengebiet aus.
   - Damit sind QB1 und QB3 nicht eingetroffen, auch nach Kartenwortlaut.
2. **QB2 ist nicht eingetroffen.** Es gibt keinen gebundenen Ast. Auf allen qualifizierten Mischzustaenden ist
   Omega^2 > 1/2, das Minimum liegt bei 0,664 (kappa = 1, q = 100) mit fallender Tendenz.
3. **G = 0: Die phi-Ladung haftet an einem ruhenden Knoten, und zwar bei jedem q.**
   - D_A betraegt hoechstens 1,91 % (kappa = 1) bzw. 1,45 % (kappa = 1/4), jeweils bei q = 17,5, und faellt bis q = 100
     auf 0,43 bzw. 0,25 %.
   - QB4 ist nach der berichtigten Hauptregel **nicht eingetroffen**, nach Kartenwortlaut (min_u) **eingetroffen**.
   - Selbstanzeige: Der Ausgang unter der Berichtigung war vorab ableitbar (Produktzustand plus negativer Kreuzterm K1,
     siehe Selbstanzeige 1). Er bestaetigt nur K1 und ist kein eigener Befund. Neu ist allein die Groesse: hoechstens etwa
     2 %.
4. **QB0 ist eingetroffen.**
   - Statisches B = 1-Profil: E = 26,54553 (kappa = 1) bzw. 17,05519 (kappa = 1/4), also 4,22- bzw. 2,71-mal 2 pi.
   - Die relative Aenderung bei Verdopplung von N_r ist hoechstens 2,3e-10; bei den Q-Baellen liegt sie bei 1e-11 bis
     6e-11.
5. **Nebenbefunde [ES]:**
   - Der drehende B = 1-Knoten existiert radial weit ueber der Kartenschwelle Omega^2 = 0,475 hinaus: bei kappa = 1 bis
     Omega^2 ~ 1 mit chi_max <= 0,88.
   - Die bei 0,95 v^2/(2 kappa) abgeschnittene Referenz der Karte haette fuer den reinen Knoten eine Scheinbindung bis
     +3,8 % erzeugt (q = 15 bis 37,5). Die Qualifikationsregel und die konservative Referenz fangen sie ab.
   - Zustaende mit chi_max > 1 sind gitterabhaengig, also keine Kontinuumsloesungen.

## Urteile

| Nr | Vorhersage (Karte, unveraendert) | Urteil (Hauptregel, Plan Abschn. 9) | Urteil nach Kartenwortlaut | Tragende Werte (Feingitter M = 1200) |
|---|---|---|---|---|
| QB0 | B = 1 ueber Schranke und konvergent (<= 1e-6); Q-Baelle konvergent (<= 1e-6) | **eingetroffen** | gleich | Textur 1,7e-10 und 2,3e-10; Q-Baelle 6,2e-11, 1,5e-11, 2,4e-12 bei omega = 0,761, 0,852, 0,956; E/2pi = 4,22 und 2,71 |
| QB1 | [H] G = 1, kappa = 1: D > 0 auf >= 3 aufeinanderfolgenden Punkten | **nicht eingetroffen** | nicht eingetroffen | 12 qualifizierte Punkte (q = 72,5 bis 100); D_C = -0,237 bis -0,240; D_K = -0,082 bis -0,086; robust > 0: 0 |
| QB2 | [H] Auf dem gebundenen Ast Omega^2 < 1/2 | **nicht eingetroffen** (kein gebundener Ast) | gleich | min Omega^2 qualifiziert = 0,664 (q = 100), max 0,805 (q = 72,5) |
| QB3 | [H] G = 1, kappa = 1/4: D > 0 auf >= 3 Punkten | **nicht eingetroffen** | nicht eingetroffen | 19 qualifizierte Punkte (q = 55 bis 100); D_C = D_K = -0,102 bis -0,111 |
| QB4 | G = 0: D(q) <= 0 fuer alle q | **nicht eingetroffen** (D_A robust > 0 auf allen 79 qualifizierten Punkten) | **eingetroffen** (D_K = -0,013 bis -0,250) | max D_A = 0,0191 (kappa = 1), 0,0145 (kappa = 1/4); unter der Berichtigung vorab ableitbar |

Robust heisst nach Plan: auf beiden Gittern qualifiziert, D_fein > 0 und |D_fein - D_grob| < D_fein/3. Gemessen war
|D_fein - D_grob| <= 1,5e-9 an allen qualifizierten Punkten.

## Tabellen

### S0 (Eichproben)

| Probe | E grob (M = 600) | E fein (M = 1200) | rel. Aenderung | Zusatz |
|---|---|---|---|---|
| B = 1 statisch, kappa = 1 | 26,545532623 | 26,545532619 | 1,7e-10 | E/2pi = 4,225; E_sig/2pi = 1,244 >= 1; E_Faddeev = E_Pot = 9,3643 (Derrick); r_Ring = 0,990 |
| B = 1 statisch, kappa = 1/4 | 17,055185533 | 17,055185529 | 2,3e-10 | E/2pi = 2,714; E_sig/2pi = 1,173; E_Faddeev = E_Pot = 4,8410; r_Ring = 0,676 |
| Q-Ball l = 0, q = 100 | 82,139707576 | 82,139707571 | 6,2e-11 | omega = 0,7613 (Ziel 0,75; kleinstes omega bei q <= 100) |
| Q-Ball l = 0, q = 21 | 20,097535160 | 20,097535160 | 1,5e-11 | omega = 0,8521 |
| Q-Ball l = 0, q = 13 | 12,969231428 | 12,969231428 | 2,4e-12 | omega = 0,9557 |

Die Bogomolny-Schranke betrifft nur den Sigma-Term: E_sig >= 2 pi v^2 |B| [L, Standard]. Sie ist erfuellt. Einen
Literaturwert fuer das Baby-Skyrmion dieses Modells (mit U(y)) gibt es nicht; PSZ 1995 habe ich nicht gelesen.

### S1 (Referenzaeste, Feingitter)

| Ast | Bereich | Ende | Werte |
|---|---|---|---|
| E_H, kappa = 1 | u = 0 bis 13,5 (du = 0,25) | Omega^2 > 0,475 bei u = 13,75 | E_H(13,5) = 31,3805, Omega^2 = 0,4671, chi_max <= 0,387; Traegheit aus E_H(1) - E_H(0) etwa 18,0 |
| E_H, kappa = 1/4 | u = 0 bis 8,5 | Omega^2 > 1,9 bei u = 8,75 | E_H(8,5) = 23,3859, Omega^2 = 1,8955, chi_max <= 0,556; Traegheit ebenso etwa 5,3 |
| E_Q, l = 0 | q' = 12 bis 100 (dq' = 1) | delokalisiert bei q' = 11 | omega von 0,988 (q' = 12) bis 0,761 (q' = 100); h_max <= 1,032; E_Q < q' ueberall (max E_Q - q' = -0,0018) |
| E_Q, l = 1 | q' = 49 bis 100 | delokalisiert bei q' = 48 | omega von 0,990 bis 0,799; E_Q^1(100) = 92,642 gegen E_Q^0(100) = 82,140 |

- q_lo = 12 passt zur Townes-Grenze der kritischen 2D-NLS (q -> N_T ~ 11,7 fuer omega -> 1) [ES, L].
- Unterhalb q_lo gilt der Kanal "freie Ladung" E = q' (Plan Abschn. 6).

### S2 (Mischaeste, Auswahl, Feingitter; volle Tabelle in lauf-69/auswertung.json, tabellen.bindung)

**G = 0 (ruhende Textur plus phi, l = 0):**

| kappa | q | E_mix | E_sep,A = E_H(0) + E_Q\*(q) | D_A | D_K (Karte) | omega^2 | h_max |
|---|---|---|---|---|---|---|---|
| 1 | 2,5 | 29,0209 | 29,0455 (freie Ladung) | +0,085 % | -8,6 % | 0,970 | 0,19 |
| 1 | 10 | 36,1594 | 36,5455 (freie Ladung) | +1,06 % | -23,6 % | 0,833 | 0,59 |
| 1 | 17,5 | 42,7822 | 43,6165 | **+1,91 %** | -20,9 % | 0,742 | 0,81 |
| 1 | 30 | 53,3051 | 54,1297 | +1,52 % | -12,1 % | 0,683 | 0,92 |
| 1 | 60 | 77,3716 | 77,9350 | +0,72 % | -7,2 % | 0,614 | 0,97 |
| 1 | 100 | 108,2162 | 108,6852 | +0,43 % | -4,8 % | 0,581 | 0,99 |
| 1/4 | 5 | 22,0405 | 22,0552 (freie Ladung) | +0,067 % | -13,9 % | 0,980 | 0,23 |
| 1/4 | 17,5 | 33,6323 | 34,1262 | **+1,45 %** | -5,7 % | 0,761 | 0,80 |
| 1/4 | 60 | 68,1571 | 68,4447 | +0,42 % | -2,0 % | 0,610 | 0,97 |
| 1/4 | 100 | 98,9425 | 99,1949 | +0,25 % | -1,3 % | 0,580 | 1,00 |

- kappa = 1/4, q = 2,5: nicht qualifiziert, der phi-Schwanz reicht ins Rechengebiet (Anteil 2,6e-3 bei r > 45).
- Bei grossem q ist der Zustand ein Q-Ball, der die ruhende Textur in sich traegt; omega^2 liegt nahe dem freien
  Q-Ball (0,5806 gegen 0,5796 bei q = 100).

**G = 1 (gekoppelter Ast, l = 1, gemeinsame Drehung):**

| kappa | q | Zustand | E_mix | E_sep,C | E_sep,K | D_C | D_K | Omega^2 | chi_max | q_phi/q |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10 | reiner Knoten (h -> 0), n. q. | 29,2527 | 29,2527 | 29,2527 | 0 | 0 | 0,279 | 0,229 | 0 |
| 1 | 25 | reiner Knoten jenseits u_max, n. q. | 41,2637 | 39,2399 | 42,8805 | -5,2 % | **+3,8 %** (Scheinbindung) | 0,954 | 0,829 | 0 |
| 1 | 40 | Knoten plus auslaufende phi-Welle, n. q. | 56,2535 | 49,4912 | 56,0889 | -13,7 % | -0,3 % | 1,002 | 0,888 | 0,30 |
| 1 | 65 | reiner Knoten, chi > 1, gitterabhaengig, n. q. | 80,7930 | 66,5767 | 76,1251 | -21,4 % | -6,1 % | 0,918 | 1,0004 | 0 |
| 1 | 72,5 | **Mischzustand** | 88,7129 | 71,7024 | 81,9910 | -23,7 % | -8,2 % | 0,805 | 0,701 | 0,72 |
| 1 | 85 | Mischzustand | 99,5276 | 80,2451 | 91,6844 | -24,0 % | -8,6 % | 0,711 | 0,624 | 0,79 |
| 1 | 100 | Mischzustand | 111,9430 | 90,4964 | 103,2145 | -23,7 % | -8,5 % | 0,664 | 0,585 | 0,83 |
| 1/4 | 5 | reiner Knoten, n. q. | 19,3558 | 19,3558 | 19,3558 | 0 | 0 | 0,804 | 0,225 | 0 |
| 1/4 | 20 | Knoten plus auslaufende Welle, n. q. | 34,3439 | 34,1887 | 34,1887 | -0,45 % | -0,45 % | 1,002 | 0,283 | 0,72 |
| 1/4 | 55 | **Mischzustand** | 69,3088 | 62,8842 | 62,8842 | -10,2 % | -10,2 % | 0,953 | 0,268 | 0,90 |
| 1/4 | 70 | Mischzustand | 82,8406 | 74,5854 | 74,5854 | -11,1 % | -11,1 % | 0,740 | 0,210 | 0,93 |
| 1/4 | 100 | Mischzustand | 107,6122 | 97,6304 | 97,6304 | -10,2 % | -10,2 % | 0,644 | 0,184 | 0,95 |

- n. q. = nicht qualifiziert (Plan Abschn. 8). Solche Punkte zaehlen nie als D > 0.
- **Referenzkanal:**
  - kappa = 1, Hauptregel C: Der fortgesetzte Knoten nimmt alle Ladung. Die Tangente mit Omega_H(13,5) = 0,683
    liegt unter allen Q-Ball- und Freikanalkosten.
  - kappa = 1, Kartenwortlaut K: Knoten mit u = 13,5 plus l = 0-Q-Ball.
  - kappa = 1/4: Inneres Optimum bei u ~ 4,2 bis 4,3 mit Omega_H = omega_Q (astra T3), Rest im l = 0-Q-Ball. Die
    Fortsetzung greift hier nicht, deshalb ist D_C = D_K.
- Selbst gegen die Referenz "ruhender Knoten plus Q-Ball" (D_A) liegt der gekoppelte Mischzustand hoeher: um 1,2 bis
  3,0 % (kappa = 1) bzw. 7,4 bis 8,8 % (kappa = 1/4).
- **Nur zur Einordnung, kein Urteil [ES]:** Gegen "ruhender Knoten plus l = 1-Q-Ball" laege der gekoppelte Zustand
  tiefer, bei q = 100 um 6,1 % (kappa = 1) bzw. 1,9 % (kappa = 1/4).
  - Der Verbund schlaegt also den Wirbel-Q-Ball, nicht aber den billigeren l = 0-Q-Ball.
  - Die Phasenkopplung erzwingt l = 1 (b ~ e^{i theta}), und dieser Wirbel kostet mehr, als Paarterm und Kreuzterm
    einbringen.

**J (Karte "je q ... J"):** Aus dem Ansatz gilt J = q_n + l q_phi, also J = q auf allen G = 1-Punkten (Abweichung
<= 2e-16) und J = 0 bei G = 0 (ruhende Textur, l = 0). Die Werte stehen je Punkt in auswertung.json (J_f, J_g).

**Omega^2 und chi_max:**
- Bilder: lauf-69/bilder/omega2.svg und chi_max.svg.
- Qualifizierte G = 1-Zustaende: chi_max = 0,585 bis 0,701 (kappa = 1) bzw. 0,184 bis 0,268 (kappa = 1/4), alle < 1.
- Referenzaeste: chi_max <= 0,387 bzw. 0,556.
- Der Wert chi_max = 1,0006 in auswertung.json (kontrollen.chi_max_mix) stammt von nicht qualifizierten
  Reinknotenpunkten (q = 57,5 bis 70, kappa = 1). Bei G = 0 ruht die Textur, dort ist chi = 0.

## Kontrollen

| Kontrolle | Ergebnis |
|---|---|
| Virial (2D-Derrick bei festem q), relatives Residuum | H-Aeste <= 3,7e-11 (fein); Q l = 0 <= 1,4e-8; Q l = 1 <= 4,8e-7; qualifizierte Mischpunkte <= 1,1e-8 |
| dE/dq = Omega (zentrierte Differenz) | H: 3,5e-5 bzw. 1,3e-4; Q l = 0: 1,4e-3 (am steilen Ende bei q_lo); Q l = 1: 1,9e-4; Mischaeste max 9e-4 bis 2,3e-3, Median 4e-5 bis 1,5e-4 (Schritt 2,5) |
| Gitter grob/fein | Energien rel. <= 3,3e-10, D <= 1,5e-9 an allen qualifizierten Punkten |
| Bogomolny E_sig >= 2 pi | 1,244 bzw. 1,173 (statisch) |
| K3 J = q (G = 1) | Abweichung <= 2e-16 (aus dem Ansatz, nur Konsistenz) |
| K4 Nullprobe (G = 0, U(x)+U(y), q = 30, 60, 90, beide Gitter) | D_null = 0 bzw. +-1,4e-16 (Schwelle 0,002): Normierung und Pfad konsistent |
| K1 Kreuzterm | vorab: xy[-2 + 1,5(x+y)] < 0 fuer x + y < 4/3; auf allen Q-Baellen gilt x <= 1,065, y <= 1/4 |
| K2 Omega^2 -> 1/2 von oben | Mischaeste fallen monoton gegen 1/2 (0,664 bzw. 0,644 bei q = 100); Grenzwert nicht erreicht |
| Konvexitaet der E_H-Fortsetzung | Die tatsaechlichen Reinknotenzustaende jenseits u_max (q = 15 bis 27,5) liegen ueber der Tangente, etwa q = 20: 36,565 > 35,823 |
| Start-Unabhaengigkeit | G = 0: alle drei Starts treffen dieselbe Energie (11 Stellen); G = 1: siehe alle_starts in den mix-JSON |

## Was diese Rechnung nicht zeigt

- Nur der radiale (achsensymmetrische) Ansatz. Nicht axiale Zustaende (phi aussermittig am Ring, Dossier P4, Stufe S3)
  und die Zeitentwicklung (S4) sind nicht gerechnet. Ein nicht axialer gebundener G = 1-Zustand ist damit nicht
  ausgeschlossen [H].
- G = 1 nur mit l = 1 und guenstiger relativer Phase, G = 0 nur mit l = 0 und ruhender Textur (Kartenansatz).
- chi_max ist die 3D-Kennzahl des Projekts, fuer den geraden String exakt. Das 2D-Hauptsymbol in der Ebene habe ich
  nicht berechnet.
- Kein Spin, keine Quantenkorrektur, kein 3D-Knoten. Die Aussage betrifft das 2D-Gegenstueck von B.5 bei
  v = mu = 1, kappa in {1, 1/4}, G in {0, 1}.

## Selbstanzeigen

1. **QB4 unter der Berichtigung war vorab ableitbar.** Das habe ich erst nach dem Lauf gesehen.
   - Fuer q >= q_lo liefert der Produktzustand (statische Textur plus Q-Ball, beide im Ursprung)
     E_prod = E_H(0) + E_Q(q) + Int xy[-2 + 1,5(x+y)].
   - Mit x <= 1,065 und y <= 1/4 ist der Kreuzterm ueberall <= 0, also E_mix <= E_prod < E_sep,A und D_A > 0.
   - Fuer q < q_lo bindet jeder anziehende l = 0-Topf in 2D [L, Simon 1976, nicht geprueft].
   - Die Ableitbarkeitsprobe haette vor dem Einfrieren stattfinden muessen. Plan und Regel bleiben unveraendert.
     QB4 "nicht eingetroffen" bestaetigt nur K1; informativ ist allein die Groesse von etwa 2 %.
   - Nach Kartenwortlaut war der Ausgang dagegen nicht vorab festgelegt.
   - Der Vermerk zu QB4 in lauf-69/auswertung.json stammt aus dem Lauf und nennt die Ableitbarkeit nicht. Ich habe die
     Maschinenausgabe nicht von Hand geaendert (Hashes in lauf-69/SHA256SUMS.txt); massgeblich ist dieser Abschnitt.
2. **Rauchlauf 1 vor dem Einfrieren zeigte Energiewerte**, auch den Reinknoten bei q = 20 (kappa = 1, G = 1).
   - Die Fortsetzungsregel E_sep,C hatte ich vorher erwogen, schriftlich fixiert aber erst danach (Plan Abschn. 12).
   - Sie macht das Urteil strenger. Am Ausgang aendert sie nichts: QB1 ist auch nach Kartenwortlaut nicht eingetroffen.
3. **Aufloesung vor dem Einfrieren von M = 1000/2000 auf 600/1200 gesenkt**, nur wegen der Laufzeit (offengelegt).
4. **QB0:**
   - Das Ziel omega = 0,75 ist mit q <= 100 nicht erreichbar. Der naechste Astpunkt hat omega = 0,761 (Regel: naechster
     Punkt).
   - Die drei omega sind Astpunkte bei festem q, keine Rechnungen bei festem omega.
5. **E_mix ist das Minimum aus drei Starts.**
   - Bei kappa = 1, G = 1 fand fuer q < 72,5 kein Start einen qualifizierten Mischzustand.
   - Lokale Minima ausserhalb der Startfamilien sind nicht ausgeschlossen.
6. **Reinknotenzustaende mit chi_max > 1** (kappa = 1, q = 57,5 bis 70) konvergieren auf dem Gitter, haben aber ein
   Virial von 4 bis 10 % und Grob-Fein-Abweichungen von 5e-4.
   - Erwartet bei Verlust der Elliptizitaet [ES].
   - Sie sind nicht qualifiziert, die Urteile beruehren sie nicht.
7. Die Kanaele "freie Ladung" (E = q') und die Tangentenfortsetzung von E_H sind meine Ergaenzungen fuer Kartenluecken
   (Plan Abschn. 6, 7, 11). Das Kartenwortlaut-Urteil steht jeweils daneben.
8. Die SVG-Bilder habe ich lokal nicht gerendert (kein lokaler Renderer erlaubt). Geprueft sind nur ihr Aufbau, die
   Legenden und dass sie keine NaN- oder Inf-Werte enthalten.
9. Literaturwert fuer das statische Baby-Skyrmion, Simon 1976 und PSZ 1995: nicht an der Quelle gelesen.
10. Zeiten: .69-Stempel in UTC, lokale in CEST, alle per date bzw. aus der Starter-Ausgabe.

## Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-051650, EINGEFROREN-20261004-051650.sha256
- code/qbbs2d.py (Loeser, Aeste), code/auswertung.py (D, Urteile, Bilder)
- rauch-69/smoke1.json, rauch-69/pipe/ (Rauchlaeufe 1 und 2 vor dem Einfrieren)
- lauf-69/refH_k1.json, refH_k025.json, refQ_l0.json, refQ_l1.json, mix_k{1,025}_G{1,0}.json, *.log
- lauf-69/auswertung.json (Urteile, Tabellen, Kontrollen)
- lauf-69/bilder/:
  - energie_kappa{1,025}_G{1,0}.svg (E_H, E_Q l = 0/1, E_sep, E_mix);
  - bindung_kappa{1,025}_G{1,0}.svg (D grob/fein, D_K);
  - omega2.svg;
  - chi_max.svg.

## Einfach gesagt

Wir wollten wissen, ob ein Feldklumpen (unser Q-Ball) an einem kleinen Knoten im Feld haengen bleibt. Das waere ein
moeglicher Weg zu Teilchen mit halbem Spin. In einer flachen, kreisrunden Modellrechnung zeigt sich: Muessen Knoten
und Klumpen im Gleichtakt drehen, fallen sie auseinander, denn zusammen brauchen sie 8 bis 24 Prozent mehr Energie
als getrennt.
Ohne Gleichtakt klebt die Ladung zwar an einem ruhenden Knoten, aber nur mit etwa 2 Prozent Gewinn, und das konnte man
schon aus der Formel ablesen. Der Weg "Knoten haelt Ladung fest" ist in dieser Form also nicht offen. Er braeuchte eine
andere Kopplung oder eine nicht kreisrunde Anordnung, die wir noch nicht gerechnet haben.
