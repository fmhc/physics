# V-1-WEITER: Ergebnis (Code-Agent, Runde 36, explorativ)

- Gerechnet vom Code-Agenten fuer die Leitung claude-primary auf der .69 (kleintest.sh, Spur p4000a, ein Lauf zugleich).
- Plan und Code eingefroren 2026-10-04 00:30:57 CEST (PLAN.md.eingefroren-20261004-003057,
  code/v1w.py.eingefroren-20261004-003057, sha256 in EINGEFROREN.sha256).
- Gewertete Laeufe 22:34 bis 23:09 UTC (00:34 bis 01:09 CEST), Diagnose und Zusatz bis 23:13:57 UTC (01:13:57 CEST).
- Drei Code-Korrekturen nach dem Einfrieren und ein Fehlstart, alle unten offengelegt (Selbstanzeigen 1 bis 4).
- Auswertung mechanisch mit jq (code/auswertung.jq -> lauf-69/auswertung.json). Geschrieben ab 2026-10-04 01:10:48 CEST
  (date).
- Kennzeichen: [M] Mathematik, [L] / [L?] Literatur aus dem Gedaechtnis (sicher / unsicher), [H] Hypothese.

## Ergebnis zuerst

1. **Die stille Frequenz wandert nur winzig und glatt:** rho_z(eps) = rho_z(0) - 3,749e-3 eps + 5,3e-3 eps^2.
   - Fuer eps = +-1e-2 sind das -3,696e-5 bzw. +3,803e-5.
   - V0 (Kontrolle auf 2e-16 getroffen) und V2 (Verhaeltnis 2,9915) sind eingetroffen.
2. **Versteifung (eps > 0): Die Stille bleibt exakt** (V1 eingetroffen).
   - Die reelle Stille-Funktion E wechselt das Vorzeichen.
   - Restgroesse an der Nullstelle 1,7e-17 bis 2,5e-15 bei einer Schwelle von 1e-10, in beiden Varianten.
3. **Erweichung (eps < 0): Die Stille des alten Kanals bricht; nur bei eps = -1e-2 ist das aufgeloest.**
   - Eine Mischung aus altem und neuen Innenkanaelen bleibt exakt total reflektiert: E hat weiter eine reelle
     Nullstelle [M].
   - Die reine alte Welle leckt dort in die neuen Kanaele. Bei eps = -1e-2: Amplitude 4,61e-9 (A) bzw. 4,45e-9 (B),
     Fluss 9,4e-17, nach innen und aussen gleich viel.
   - Bei -3e-3 und -1e-3 liegt das echte Leck unter der Rechengrenze. Die gemessenen Werte stammen vom
     FD-Hintergrund: Varianten A und B weichen um Faktor 200 bzw. 36 voneinander ab.
   - Damit sind V3 und V4 nicht auswertbar.
4. **Beschreibend, kein Urteil: Das Leck faellt schneller als jede Potenz, wie die Karte vermutet.**
   - Gerechnet mit schwanzfreiem Hintergrund f0, eps nur in den Schwankungen.
   - Ueber eps = -2e-2, -1,5e-2, -1e-2 gilt ln P = 25,3 - 6,29/sqrt|eps| (Streuung 0,07), also c ~ 2 pi [H].
   - Eine Potenz passt schlechter: oertlicher Exponent 24,5 und dann 28,1, Streuung 0,29.
   - Hochgerechnet ergaebe das bei -3e-3 einen Fluss ~1e-39 und bei -1e-3 ~4e-76, weit unter float64.
   - Mit dem FD-Hintergrund des Kartenmodells (Ende 90) zeigt der aufloesbare Bereich (-2,5e-2 bis -1e-2) dasselbe Bild:
     c = 6,31 (Streuung 0,15) gegen Potenz 25,4 (Streuung 0,43).
5. **Bedeutung:**
   - Robust gegen Versteifung, wie vorab vermutet.
   - Bei gitterartiger Erweichung wird die Stille undicht, aber extrem schwach: bei |eps| = 1e-2 ein Flussanteil
     von 1e-16, bei feineren Stufen unmessbar klein.
   - Die vorab festgelegte Bedeutungszeile "V1 bis V3 treffen ein" ist nicht ausgeloest, weil V3 nicht auswertbar ist.
   - Vorbehalt fuer Finns Netz [H]: Der Kontinuumsterm -h^2 k^4/12 bildet ein Gitter nur bei kleinen k ab. Der neue Ast
     liegt bei k ~ sqrt(12)/h, also ausserhalb der Brillouin-Zone (k <= pi/h). Ob ein echtes Gitter denselben neuen
     Kanal oeffnet, ist damit nicht gezeigt.

## Urteile (mechanisch nach PLAN.md Abschnitt 7, lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Urteil | Werte |
|---|---|---|---|
| V0 | eps = 0: rho_z = 1,7734530718 auf 1e-8 | **eingetroffen** | A: 1,7734530718065 (Abweichung -2,2e-16), B: Abweichung 0 |
| V1 | eps > 0: Restgroesse < 1e-10, beide Varianten, alle drei eps | **eingetroffen** | 1,3e-15 / 1,8e-15 (1e-3), 1,1e-16 / 4,3e-16 (3e-3), 1,7e-17 / 2,5e-15 (1e-2), je A / B |
| V2 | Verhaeltnis der Verschiebungen 3e-3 zu 1e-3 in [2,7; 3,3] | **eingetroffen** | A: 2,991541, B: 2,991541 |
| V3 | eps < 0: Restkopplung ungleich 0, steigend mit abs(eps) | **nicht auswertbar** | nur -1e-2 aufgeloest (Tabelle 2) |
| V4 | Restkopplung faellt schneller als jede Potenz | **nicht auswertbar** | weniger als drei aufgeloeste Werte |

- Die Festlegungen [F] des Plans galten unveraendert: Restgroesse relativ zu T_aus(rho_z + 1e-3), Aufloesung = rtol-
  Probe 20 % und A/B-Uebereinstimmung 30 %, Operationalisierung von V3 und V4.
- **Vermerk zu V3/V4 (Datengrundlage):**
  - Gewertet sind fuer eps < 0 die Laeufe mit Hintergrundende 90 (A_m*x, B_m*x), siehe Selbstanzeige 3.
  - Mit dem Plan-Ende 47 gibt es nur Variante A, B wurde abgebrochen.
  - Die A-Werte dort (8,1e-9 bei -3e-3, 6,8e-11 bei -1e-3) sind ebenfalls Hintergrund-Artefakte, siehe Kontrollen.
  - Das Urteil waere mit diesen Laeufen ebenfalls "nicht auswertbar", weil B fehlt.

## Tabellen

**Tabelle 1: Lage und Restgroesse** (A: h_bg 0,0025, rtol 1e-11; B: h_bg 0,005, rtol 1e-10)

| eps | rho_z (A) | rho_z - rho_z(0) (A) | rho_z (A) - rho_z (B) | Restgroesse A | Restgroesse B | T bei +1e-6 / +1e-5 | Breite Gamma |
|---|---|---|---|---|---|---|---|
| -1e-2 | 1,7734911003052 | +3,80285e-5 | +5,5e-13 | 9,4e-17 | 8,8e-17 | 0,0156 / 0,613 | 0,79e-5 |
| -3e-3 | 1,7734643656246 | +1,129382e-5 | +8,5e-14 | 2,4e-18 | 1,4e-22 | 0,0102 / 0,508 | 0,98e-5 |
| -1e-3 | 1,7734568256840 | +3,753878e-6 | -3,0e-13 | 1,3e-20 | 1,6e-20 | 0,0092 / 0,481 | 1,04e-5 |
| 0 | 1,7734530718065 | 0 | -2,2e-16 | 4,6e-25 | 2,9e-21 | 0,0087 / 0,468 | 1,07e-5 |
| +1e-3 | 1,7734493285697 | -3,743237e-6 | -6,9e-13 | 1,3e-15 | 1,8e-15 | 0,0083 / 0,455 | 1,10e-5 |
| +3e-3 | 1,7734418737612 | -1,1198045e-5 | +3,9e-13 | 1,1e-16 | 4,3e-16 | 0,0075 / 0,430 | 1,15e-5 |
| +1e-2 | 1,7734161077320 | -3,6964074e-5 | +9,1e-13 | 1,7e-17 | 2,5e-15 | 0,0055 / 0,355 | 1,35e-5 |

- Restgroesse = T_aus(rho_z)/T_aus(rho_z + 1e-3), T_aus = Flussanteil in alle offenen Aussenkanaele bei Einfall im alten
  Innenkanal. Gamma aus T(+1e-5) = d^2/(d^2 + Gamma^2), nachtraeglich und nur beschreibend.
- Fuer eps < 0 besteht die Restgroesse fast ganz aus dem neuen Kanal: T_alt(rho_z) = 1,3e-20 (-1e-3), 4,1e-23 (-3e-3),
  3,2e-23 (-1e-2).
- Erste Ordnung (aus +-1e-3, zentral): d rho_z/d eps = -3,7486e-3; zweite Ordnung +5,32e-3. Damit trifft die Formel aus
  Punkt 1 auch +-1e-2 auf 1,1e-8 [M, beschreibend].

**Tabelle 2: Restkopplung in die neuen Aussenkanaele bei rho_z** (groesste Amplitude, Fluss P_neu)

| eps | Amplitude A | A mit 10 rtol | Amplitude B | aufgeloest | P_neu (A) | Diagnose f0-Hintergrund (Amplitude) |
|---|---|---|---|---|---|---|
| -1e-2 | 4,608e-9 | 4,608e-9 | 4,450e-9 | ja | 9,4e-17 | 3,30e-9 (stabil) |
| -3e-3 | 4,47e-10 | 4,47e-10 | 2,2e-12 | nein | (2,4e-18) | 1,0e-15 (Rauschen: 4,4e-15 bei 10 rtol) |
| -1e-3 | 1,58e-12 | 1,58e-12 | 4,4e-14 | nein | (5,1e-23) | 9,1e-16 (Rauschen: 1,4e-15 bei 10 rtol) |

- Bei eps = -1e-2 ist die Kopplung an der stillen Stelle resonant ueberhoeht: bei rho_z +- 1e-3 nur 3,7e-11, also
  Faktor ~125 kleiner.
- Der Fluss in die neuen Innenkanaele ist gleich dem nach aussen (9,37819e-17 gegen 9,37819e-17).
  - Deutung [H, nachtraeglich]: An der stillen Stelle braucht die total reflektierte Mischung eine kleine
    Beimischung u_neu der neuen Kanaele.
  - Eine reine alte Welle verliert deshalb |u_neu|^2 einmal durch die Wand (neue Kanaele laufen fast ungestoert
    durch) und einmal in der Reflexion.

## Kontrollen

- **Hintergrund:**
  - Hilfsparameter delta <= 2,3e-11 (alle Laeufe); Residuum (long double) <= 3,8e-10 (A, |eps| = 1e-2), <= 2,3e-11 (B).
  - max |f - f0| = 5,85e-5, 1,75e-4, 5,79e-4 fuer eps = 1e-3, 3e-3, 1e-2, also linear in eps.
- **Flussbilanz:**
  - eps < 0: <= 1,1e-12 (A) bzw. 5,2e-13 (B).
  - eps = 0: 1,1e-11 (A) bzw. 1,4e-10 (B).
  - eps > 0: bis 4,5e-8 (Selbstanzeige 5); Plan-Schwelle 1e-6 eingehalten.
- **Stille-Funktion:** E(rho_z) <= 9,6e-15 bei Abtastwerten bis 7,8e-2 (eps = 0) bzw. 4,5e-5 bis 4,8e-4 (eps > 0, siehe
  Selbstanzeige 5). Je Lauf genau eine Nullstelle im Fenster, der weite Rueckfall wurde nie ausgeloest.
- **Varianten:** rho_z stimmt zwischen A und B auf <= 9,1e-13 ueberein; Restgroesse und Amplituden bei 10-fach groeberem
  rtol siehe Tabelle 2.
- **Kanalzahl** wie im Plan: eps > 0 aussen ein laufender Kanal; eps < 0 aussen drei (B alt, A neu, B neu), innen drei.
- **Hintergrund-Artefakt bei eps < 0** (nachtraeglich gefunden, Selbstanzeige 3):

| eps | Ende 47 (A) | Ende 90 (A) | Ende 90 (B) | f0-Hintergrund |
|---|---|---|---|---|
| -1e-2 | 4,09e-9 | 4,61e-9 | 4,45e-9 | 3,30e-9 |
| -3e-3 | 8,05e-9 | 4,47e-10 | 2,2e-12 | <= 1e-15 |
| -1e-3 | 6,8e-11 | 1,6e-12 | 4,4e-14 | <= 1e-15 |

  - Bei -1e-2 aendern Hintergrundende, Gitter und Hintergrundwahl die Amplitude nur um <= 40 %.
  - Bei -3e-3 und -1e-3 haengt sie um Groessenordnungen davon ab und ist unabhaengig von rtol. Sie stammt also aus
    stehenden Schwanzwellen des numerischen Hintergrunds (Wellenzahl k0 ~ 1/sqrt|eps|), nicht aus der Wand [H].
  - Moegliche Quellen: Randbedingung f = 0 am rechten Ende (bei 47 noch 6e-11 vom wahren Wert entfernt) und Rauschen
    der Newton-Residuen (~1e-10, waechst wie 1/h^4).

## Zusatz (beschreibend, kein Urteil)

- **Zwei Reihen**, beide mit Hintergrundende 90:
  - Z: Kartenmodell (FD-Hintergrund mit eps), Variante A, eps laut Plan Abschnitt 9.
  - D: nachtraegliche Diagnose mit schwanzfreiem Hintergrund f0, eps nur in den Schwankungen (anderes Modell).
- "stabil" heisst: Amplitude bei 10-fachem rtol auf 20 % gleich. Eine B-Probe gibt es fuer die Zusatzwerte nicht.

| eps | 1/sqrt(-eps) | Z: Amplitude | Z: P_neu | D: Amplitude | D: P_neu |
|---|---|---|---|---|---|
| -2,5e-2 | 6,32 | 7,34e-4 | 1,16e-6 | - | - |
| -2e-2 | 7,07 | 5,57e-5 | 8,14e-9 | 4,37e-5 | 4,95e-9 |
| -1,5e-2 | 8,16 | 1,49e-6 | 7,27e-12 | 1,15e-6 | 4,30e-12 |
| -1e-2 | 10,00 | 4,61e-9 (A_m1e-2x) | 9,38e-17 | 3,30e-9 | 4,75e-17 |
| -7e-3 | 11,95 | 1,91e-11 | 2,61e-21 | - | - |
| -3e-3 | 18,26 | Artefakt (Tabelle 2) | - | 1,0e-15, nicht stabil | - |
| -1e-3 | 31,62 | Artefakt (Tabelle 2) | - | 9,1e-16, nicht stabil | - |

- **Anpassungen** (code/zusatz_fit.jq; lauf-69/zusatz_fit_*.json), ln P = a - c/sqrt|eps| gegen ln P = a' + p ln|eps|:

| Reihe | Punkte | c | Streuung (exp) | p | Streuung (Potenz) |
|---|---|---|---|---|---|
| D (f0) | -2e-2, -1,5e-2, -1e-2 | 6,295 | 0,071 | 26,7 | 0,29 |
| Z (FD) | -2,5e-2 bis -1e-2 (4) | 6,310 | 0,150 | 25,4 | 0,43 |
| Z (FD) mit -7e-3 | 5 | 6,006 | 0,490 | 26,6 | 0,61 |

- In beiden Modellen passt die Form exp(-c/sqrt|eps|) besser als eine Potenz.
  - Die oertliche Potenz waechst zu kleinem |eps| hin (D: 24,5, dann 28,1).
  - c liegt bei 2 pi = 6,283.
- Deutung [H]: Amplitude ~ exp(-pi sqrt(beta) K) mit K ~ 1/sqrt|eps| (Wellenzahl des neuen Kanals) und pi sqrt(beta)
  als Abstand der komplexen Pole des Wandprofils S = S_c/(1 + e^{x/sqrt beta}) von der reellen Achse (Pole: [M]).
  Der Fluss ist das Quadrat, also c = 2 pi.
- Der Punkt -7e-3 liegt ~12-fach ueber der D-Hochrechnung (FD/f0 sonst 1,6 bis 2,0). Vermutlich ist er schon vom
  Hintergrund-Artefakt mitbestimmt; eine B-Probe fehlt.
- Vorhersage fuer eine spaetere Rechnung mit hoeherer Genauigkeit (mpmath): P(-3e-3) ~ 1e-39, P(-1e-3) ~ 4e-76.
  Damit waeren V3 und V4 pruefbar [H].

## Latten (v3)

- **L1 (kann scheitern):** ja.
  - V1 haette brechen koennen: E ohne Vorzeichenwechsel oder T_aus deutlich ueber 1e-10.
  - V2 haette ausserhalb [2,7; 3,3] liegen koennen.
- **L2 (Gegenprobe):** teilweise.
  - V0 gegen WAND-BETA, unabhaengig gerechnet (Evans-Determinante statt c_in).
  - Restgroesse aus der Streuung als zweiter Weg zur Nullstelle von E.
  - Diagnose mit f0-Hintergrund.
  - Kein zweites Haus.
- **L3 (Numerik):** ja. Zwei Gitter, zwei Toleranzen, Hintergrundende 47 und 90, Flussbilanz. Die Aufloesungsgrenze
  fuer eps < 0 ist benannt.
- **L4 (schon bekannt):** teilweise.
  - Exponentiell kleine Abstrahlung bei Kurzwellen-Dispersion ist bekannte Physik: Nanopteronen, "weakly nonlocal
    solitary waves" (Boyd), Pomeau/Ramani/Grammaticos zur KdV 5. Ordnung [L?].
  - Fuer die Q-Ball-Wand nicht gesucht.
- **L5 (Messbezug):** nein. Rein modellintern.

## Selbstanzeigen

1. **Fehlstart der Laufkette (00:31 CEST).**
   - lauf.sh gab die Fensterargumente nicht weiter. Die Voreinstellung im Code (rho_WB -+ 0,15, 61 Punkte)
     widersprach dem Plan (-+ 0,01, 11 Punkte) und reichte ueber die Kanalschwelle 1 + omega = 1,866.
   - A_e0 brach ab (rc = 1); A_p1e-3 habe ich nach etwa 1 min gestoppt (eigene Unit, systemctl --user stop).
   - Logs in lauf-69/fehlstart/. Neustart 00:34:44 CEST mit den Planwerten.
2. **Korrektur 1 nach dem Einfrieren (00:35:26 CEST, sha256 6c064850...).**
   - Bei eps = 0 liegt die Fenstermitte rho_WB praktisch auf der Nullstelle. E wechselte dort zwischen Abtast- und
     voller Toleranz das Vorzeichen; brentq brach ab (A_e0 im Neustart, rc = 1).
   - Korrektur: Fehlt der Vorzeichenwechsel bei voller Toleranz, wird mit den Nachbarpunkten geklammert; doppelte
     Nullstellen werden verworfen.
   - Betrifft nur diesen Fehlerpfad. A_p1e-3 lief noch mit dem eingefrorenen Code, eps = 0 (A) wurde als A_e0b
     wiederholt (Ergebnis in A_e0.json).
3. **Korrektur 2 nach dem Einfrieren (00:51:44 CEST, sha256 c6fdeab5...): Hintergrundende rechts 47 -> 90 fuer
   eps < 0.**
   - Der Plan behauptete, die wahre Wand weiche an den Raendern nur um ~e^-40 ab. Rechts stimmt das nicht: Der Abfall
     ist e^{-x/2}, bei x = 47 also noch ~6e-11.
   - Fuer eps < 0 regt die Randbedingung f = 0 dort stehende Schwanzwellen im Hintergrund an. Diese koppeln alte und
     neue Kanaele und taeuschen eine Restkopplung vor (A_m3e-3: 8,1e-9).
   - Die Kette wurde nach B_p1e-3 abgebrochen; B fuer eps < 0 mit Ende 47 gibt es nicht.
   - Alle eps < 0 sind mit Ende 90 neu gerechnet (A und B).
   - Fuer eps >= 0 ist das Ende unerheblich. Gegenprobe A_p1e-2x mit Ende 90: rho_z aendert sich um -2,8e-12,
    Restgroesse 5,1e-16.
   - Auch mit Ende 90 bleiben bei -3e-3 und -1e-3 Artefakte, die das Aufloesungskriterium (A/B-Vergleich) als
     unaufgeloest erkennt.
4. **Korrektur 3 nach dem Einfrieren (00:55:44 CEST, sha256 9ad59ac5...):** Diagnose-Schalter "f0" (Hintergrund =
   eps-0-Profil, eps nur in den Schwankungen). Er dient nur der Diagnose (D_*-Laeufe) und aendert keinen gewerteten
   Lauf.
5. **Flussbilanz bei eps > 0 nur ~1e-8 bis 4,5e-8** (eps < 0: ~1e-13), kaum abhaengig von rtol.
   - Vermutung [H, nachtraeglich]: Rundungsfehler werden je Abschnitt um bis zu e^12 verstaerkt (Abschnittslaenge
     12 sqrt(eps)) und nahe der Resonanz noch einmal durch die Kondition der Anschlussmatrix (~2,5e4).
   - In unskalierten Variablen ist ausserdem |E| bei eps > 0 klein (bis 4,5e-5), weil die schnellen Moden fast
     parallele Zustandsvektoren haben.
   - Beides beruehrt die Urteile nicht: Die Restgroesse liegt fuenf Groessenordnungen unter der Schwelle, rho_z stimmt
     zwischen A und B auf 1e-12.
6. **Festlegungen und Plan:**
   - Die Festlegungen [F] (Restgroesse, Aufloesung, V3/V4-Regeln) stammen von mir und standen vor den Hauptlaeufen im
     eingefrorenen Plan.
   - Der Plan nannte die Zusatz-eps nur fuer den FD-Hintergrund. Die f0-Diagnosereihe ist nachtraeglich und
     beschreibend.
   - Die Rauchlaeufe (r1 bis r5) zeigten Verschiebungen und Linearitaet schon vor dem Einfrieren; im Plan offengelegt,
     Schwellen unveraendert.
7. **Vorab-Schaetzung:** Die Schreibtisch-Schaetzung im Plan (Abschnitt 8: Amplitude ~1e-10 bis 1e-9 bei -1e-2) lag um
   Faktor ~5 zu tief. Die Groessenordnung fuer -3e-3 und -1e-3 (unter float64) hat sich bestaetigt.

## Bilder (lauf-69/)

- bild1_restgroesse.svg: log10 T_aus gegen rho - rho_z (gestaucht, Punkte bei 0, +-1e-6, +-1e-5, +-1e-3), je eps
  (Variante A).
- bild2_rho_z.svg: rho_z(eps) - rho_z(0), A und B.
- bild3_restkopplung.svg: log10 P_neu gegen 1/sqrt|eps|.
  - Gewertete Laeufe (gefuellt = aufgeloest, offen = unter der Grenze).
  - Zusatz mit FD-Hintergrund.
  - Diagnose f0.

## Einfach gesagt

Die Wand eines Q-Balls laesst bei genau einer Frequenz keine Welle durch, sie ist dort "still". Wir haben geprueft, ob
das so bleibt, wenn der Raum ein feines Gitter ist, das sehr kurze Wellen anders laufen laesst. Wird die Gleichung bei
kurzen Wellen steifer, bleibt die Stille vollkommen erhalten, und die Frequenz verschiebt sich nur um ein paar
Hunderttausendstel. Wird sie weicher, wie bei einem echten Gitter, oeffnet sich ein neuer Weg fuer sehr kurze Wellen,
und die Wand wird undicht, aber nur ganz wenig: Bei der groebsten Stufe geht etwa ein Zehnbilliardstel der Energie
verloren, bei feineren Stufen so wenig, dass unser Rechner es nicht mehr von null unterscheiden kann. Wie schnell das
Leck mit feinerem Gitter verschwindet, haben wir nur an Hilfsrechnungen gesehen (schneller als jede Potenz), nicht im
gewerteten Test.
