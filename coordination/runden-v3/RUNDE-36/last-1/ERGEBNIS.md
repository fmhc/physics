# LAST-1: Ergebnis (Code-Agent fuer die Leitung, Runde 36, explorativ)

- **Rechenort:** .69 ueber kleintest.sh, nur Spuren cpu und cpu6, hoechstens zwei Laeufe zugleich.
- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 22:42:21 CEST, Plantext ab 23:02:23 CEST.
  - Rauchlaeufe 21:02:19 bis 21:11:55 UTC (Abschnitt 5, Punkt 1).
  - Eingefroren 23:12:13 CEST:
    - Kopien: PLAN.md.eingefroren-20261003-231213, code/last1.py.eingefroren-..., code/auswertung.py.eingefroren-...
    - Pruefsummen: code/pruefsummen-einfrieren.txt (last1.py 7a64115f..., auswertung.py 7e3c72dc...).
  - Hauptlaeufe:
    - L = 128: 21:12:17 bis 21:13:36 UTC (cpu6).
    - L = 32/64: 21:12:20 bis 21:14:04 UTC (cpu).
    - Kontrolle L = 16: 21:14:04 bis 21:14:08 UTC.
    - Kontinuum: 21:14:08 bis 21:14:57 UTC.
    - Alle rc = 0; alle tragen sha256 7a64115f... des eingefrorenen Skripts.
  - Auswertung 21:15:03 bis 21:15:12 UTC. Nachschau (beschreibend) 21:17:55 UTC.
  - Text ab 23:19:23 CEST.
- **Daten in lauf-69/:**
  - lauf128.json/.npz, lauf3264.json/.npz, kontrolle.json, kontinuum.json/.npz, Logs;
  - auswertung.json (Urteile, Kontrollen, Tabellen);
  - nachschau.json (beschreibend, nicht eingefroren);
  - Bilder: pi12_a/b/c.png, richtung_a/b/c.png, kelvin.png, torus.png, verschiebung.png.
- **Rauch:** rauch-69/ (rauch1, rauch2). Die Auswertung aus rauch3 liegt ungelesen auf der .69 unter rauch/kette/.
- **Code:** code/last1.py (Rechnung), code/auswertung.py (Urteile, Bilder), beide eingefroren. code/nachschau.py
  (nach dem Einfrieren, nur beschreibend).
- **Kennzeichen:** [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese, [E] hier
  gerechnet, [F] Festlegung im Plan.
- **Einheiten:** Stablaenge 1, Federn k = 1, Last f = 1, Ueberlaenge delta = 1 (linear; Pi skaliert mit f^2 bzw.
  delta^2). r in Stablaengen. Pi_12 < 0 heisst Anziehung.

## 1. Ergebnis

1. **Gleich gerichtete Punktlasten ziehen sich im Stabnetz an, und zwar genau wie 1/r [E].**
   - Das gilt in beiden Netzen fuer alle 24 166 Gittervektoren mit 3 <= r <= 16.
   - Exponenten je Richtung: 0,993 bis 1,013.
   - Im isotrop abgestimmten Netz trifft die Kelvin-Formel fuer r >= 6 auf 0,47 %.
   - Laengs der Lastrichtung ist die Anziehung um den Faktor (4 - 4 nu)/(3 - 4 nu) = 1,36 staerker als quer dazu.
   - Jede Last traegt aber eine Nettokraft. Auf dem Torus nimmt ein gleichmaessiger Gegenhintergrund sie auf.
     - Ohne Korrektur verfaelscht er Pi_12 bei L = 128 um 14 % (r = 8) bis 28 % (r = 16), im iso-Netz laengs [110];
       aniso 15 % bzw. 30 %.
     - Bei L = 32 kehrt sich das Vorzeichen in 1220 (aniso) bzw. 648 (iso) von 24 166 Abstaenden um:
       Scheinabstossung.
2. **Quellen ohne Nettokraft (aufgeweiteter Knoten, zu langer Stab) wirken anders [E]:**
   - Die Verschiebung faellt wie r^-2,00 (Punktlast: r^-1,00).
   - Die Wechselwirkung faellt wie r^-3, mit richtungsabhaengigem Vorzeichen:
     - Dilatationszentren im anisotropen Netz ziehen sich laengs [100] an und stossen sich laengs [110] und [111] ab.
     - Zwei parallele zu lange Staebe stossen sich Ende an Ende ab und ziehen sich Seite an Seite an.
   - Das Mittel einer solchen 1/r^3-Wechselwirkung ueber alle Richtungen ist null [M, Abschnitt 6].
3. **Im isotrop abgestimmten Netz verschwindet die elastische Wechselwirkung zweier Dilatationszentren [E].**
   - Zener-Verhaeltnis 1 + 2e-10 bei k_theta = 1/18.
   - Was bleibt, ist ein Gitterrest, der wie r^-5 faellt (Schalen-Exponent 5,00; laengs [100] lokal 5,00).
   - Bei r nahe 8 ist er 2,5 % (Schalen-RMS) des anisotropen Werts, laengs [111] 4,2 %, laengs [110] 0,09 %.
4. **Alle fuenf Vorhersagen sind eingetroffen (L0 bis L4), auch mit L = 64.**
   - L2 und L3 gelten nach der vorab festgelegten Regel: genannte Richtungen plus Schale [F].
   - In 24 von 121 Listenrichtungen waere die strenge Lesung "alle Richtungen" verfehlt. Das sind die Familien <211>
     und <320>, in denen der anisotrope Betrag klein ist.
     - L2-Verhaeltnis dort 6,1 % bzw. 6,3 %.
     - L3-Exponent dort 3,63 bzw. 1,62.
5. **Bedeutung (wie vorab festgelegt, ausgeloest):**
   - Kraefte in Staeben geben eine schwerkraftartige 1/r-Anziehung nur fuer Lasten mit Nettokraft, und diese Kraft
     muss von aussen kommen (Gummituch-Zirkel).
   - Abgeschlossene Klumpen wechselwirken ueber das Netz nur kurzreichweitig und mit wechselndem Vorzeichen. Im
     isotropen Netz tun sie es in elastischer Ordnung gar nicht.
   - Elastizitaet allein macht also keine Schwerkraft.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 23:12:13 CEST) durch code/auswertung.py, Hauptgroesse L = 128 (Kante 181
Stablaengen), korrigierte Werte; alle Zahlen in lauf-69/auswertung.json.

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| L0 | aniso: C11 = 2 C44, C12 = C44 auf 1e-6; iso: Zener 1 auf 1 % | 85 % | **eingetroffen**, vorab ableitbar [M] | aniso: C11/(2 C44) - 1 = 0, C12/C44 - 1 = 8,3e-10; iso: Zener 1,0000000002 (aniso 2,0000); iso: mu = 1,17851, lambda = 0,15713, nu = 0,058824 = 1/17 |
| L1 | Punktlasten: Pi_12 < 0 fuer r >= 3 in allen Richtungen; Exponent 1 +- 0,1; iso innerhalb 5 % von Kelvin fuer r >= 6 | 75 % | **eingetroffen** | (i) 0 von 24 166 Vektoren >= 0 (je Netz); groesster Wert -0,0063 (aniso), -0,0031 (iso). (ii) p je Richtung 0,993 bis 1,013 (aniso), 0,993 bis 1,002 (iso), Schale 0,998 / 0,999. (iii) Kelvin: groesste Abweichung 0,47 % (-0,47 % bis +0,14 %) ueber alle Vektoren mit 6 <= r <= 16 |
| L2 | iso-Dilatation: bei r = 8 hoechstens 5 % des aniso-Betrags; faellt mindestens wie r^-3 | 60 % | **eingetroffen** nach Regel [F] | Verhaeltnis bei r nahe 8: [100] 0,024 (r = 8,49), [110] 0,0009 (r = 8), [111] 0,042 (r = 7,35), Schale 0,025. Abfall: p_schale 5,00; p_env [100] 4,96, [110] 5,65, [111] 4,78. Alle 121 Richtungen: Median 0,025, groesstes 0,063; 80 % <= 0,05 |
| L3 | aniso-Dilatation: Exponent 3 +- 0,4; Vorzeichen [100] und [111] entgegengesetzt | 60 % | **eingetroffen** nach Regel [F] | p: [100] 2,99, [110] 3,35, [111] 2,68, Schale 3,03. Vorzeichen auf 4 <= r <= 16: [100] durchweg negativ (Anziehung), [111] durchweg positiv (Abstossung), [110] positiv. Alle 121 Richtungen: p 1,62 bis 3,63, 80 % in [2,6; 3,4] |
| L4 | b, c: Verschiebung faellt wie r^-2, nicht wie r^-1 | 85 % | **eingetroffen**, vorab ableitbar [M] | p_u: b 2,001 (aniso) / 2,006 (iso); c 2,000 / 1,994. Kontrast Punktlast (korrigiert): 0,998 / 0,999; unkorrigiert auf dem Torus 1,158 / 1,155 |

- **Groessenprobe:** Mit L = 64 lauten die vier groessenabhaengigen Urteile L1 bis L4 gleich (L0 haengt nicht von L
  ab). Die Werte sind fast dieselben, z. B. L2 [111] 0,0421, L3 [111] 2,678, L4 2,003 bis 2,019.
- **Bedeutung, wie vorab festgelegt:**
  - "L1 bis L4 treffen ein" ist ausgeloest (Abschnitt 1, Punkt 5).
  - "L2 verfehlt" und "L0 verfehlt" sind nicht ausgeloest: Die isotrope Abstimmung des Gegenlesers (B1) stimmt.
- **Gewicht der Festlegung [F] bei L2 und L3:**
  - Die Karte sagt bei L2 "in derselben Richtung" und bei L3 "Pi_12 ~ r^-3", ohne Richtungsmenge.
  - Ich habe vor dem Lauf die drei genannten Richtungen plus den Schalen-RMS bewertet. Begruendung: Knotenkegel der
    anisotropen Wechselwirkung.
  - Bei der strengen Lesung "jede der 121 Richtungen" waeren L2(i) und L3(i) nicht eingetroffen. Die Ausnahmen liegen
    genau in den Familien mit kleinem anisotropem Betrag:
    - <320>: r^3 Pi = 0,047 gegen das Maximum 0,76, also nahe dem Knotenkegel;
    - <211>: 0,114.
  - Die Nachschau zeigt dort den Uebergang zum r^-3-Gesetz:
    - <320>: lokale Steigung 1,0, dann 2,88; bei r = 15,3 Gitter 1,390e-5 gegen Kontinuum 1,403e-5.
    - <211>: lokale Steigung 3,20 bei r = 15,6, fallend gegen 3.

## 3. Tabellen

### 3.1 Elastische Konstanten [E] (D(q) = Omega C q q bei |q| = 1e-4; Probe 2e-4 gleich auf 2,7e-8)

| Netz | k_theta | C11 | C12 | C44 | Zener 2 C44/(C11 - C12) | geschlossene Form [M] |
|---|---|---|---|---|---|---|
| aniso | 0 | 1,414214 | 0,707107 | 0,707107 | 2,0000 | sqrt2 (1, 1/2, 1/2) |
| iso | 1/18 | 2,514157 | 0,157135 | 1,178511 | 1,0000 | sqrt2 (16/9, 1/9, 5/6) |

- Abweichung von den geschlossenen Formen C11 = sqrt2 (1 + 14 k_theta), C12 = sqrt2 (1/2 - 7 k_theta),
  C44 = sqrt2 (1/2 + 6 k_theta) hoechstens 9e-9.
- Kompressionsmodul in beiden Netzen 2 sqrt2/3 = 0,9428: Winkelfedern aendern ihn nicht.

### 3.2 Punktlasten (a), korrigiert, L = 128 [E]

| Netz | Richtung | r | Pi_12 | Kontinuum | Kelvin (nur iso sinnvoll) | Torus unkorrigiert |
|---|---|---|---|---|---|---|
| aniso | [100] | 8,49 | -0,012569 | -0,012582 | - | -0,010648 |
| aniso | [110] | 16 | -0,0063292 | -0,0063265 | - | -0,0044170 |
| aniso | [111] | 14,70 | -0,0083688 | -0,0083737 | - | -0,0064552 |
| iso | [100] | 15,56 | -0,0031883 | -0,0031876 | -0,0031876 | -0,0023208 |
| iso | [110] | 16 | -0,0030992 | -0,0030992 | -0,0030992 | -0,0022319 |
| iso | [111] | 14,70 | -0,0037820 | -0,0037808 | -0,0037808 | -0,0029153 |
| iso | [001] (laengs f) | 8,49 | -0,0079354 | - | r Pi = -0,06752 (Gitter -0,06733) | - |

- Kraft f laengs [001]. Kontinuum: Kreisintegral nach Synge/Lifshitz mit den gemessenen C [L]; im iso-Netz gleich
  Kelvin auf 1e-10.
- Gitter gegen Kontinuum fuer 12 <= r <= 16: hoechstens 0,22 % (aniso), 0,14 % (iso).
- r Pi_12 quer zur Last (iso): -0,04959 = -(3 - 4 nu)/(16 pi mu (1 - nu)), laengs: -0,06752.

### 3.3 Dilatationszentren (b), korrigiert, L = 128 [E]

| Richtung | r | aniso Pi_12 | aniso Kontinuum | iso Pi_12 | iso/aniso |
|---|---|---|---|---|---|
| [100] | 2,83 | -0,03222 | -0,03320 | -0,005226 | 0,16 |
| [100] | 8,49 | -0,0012217 | -0,0012298 | -2,879e-5 | 0,024 |
| [100] | 15,56 | -1,991e-4 | -1,996e-4 | -1,391e-6 | 0,0070 |
| [110] | 2 | +0,09615 | +0,05987 | +0,05833 | 0,61 |
| [110] | 8 | +0,0010927 | +0,0009355 | -9,73e-7 | 0,0009 |
| [110] | 16 | +1,210e-4 | +1,169e-4 | -1,85e-7 | 0,0015 |
| [111] | 2,45 | +0,01700 | +0,06331 | +0,002409 | 0,14 |
| [111] | 7,35 | +0,0019228 | +0,0023448 | +8,106e-5 | 0,042 |
| [111] | 14,70 | +2,779e-4 | +2,931e-4 | +2,691e-6 | 0,0097 |

- Kontinuum (aniso): (1/(8 pi^2 r^3)) Kreisintegral von d^2 s/dt^2 [M, hergeleitet].
  - Fuer 12 <= r <= 16 weicht das Gitter im Median um 1,5 % ab.
  - Das Maximum 53 % liegt in Richtungen nahe dem Knotenkegel.
  - Lokale Steigungen: [110] 3,07 bei r = 16, [111] 2,88 bei r = 14,7; beide naehern sich 3.
  - Vorzeichenmuster: Anziehung laengs [100], Abstossung laengs [110] und [111] bei Zener 2 (> 1).
    - Das passt zu dem, was ich fuer kubische Kristalle mit Zener > 1 erinnere: Dilatationszentren und kohaerente
      Ausscheidungen ordnen sich laengs <100> an [L?].
    - In erster Ordnung der Anisotropie traegt der Winkelfaktor x^4 + y^4 + z^4 - 3/5 [L?]. Er hat bei [100] das
      andere Vorzeichen als bei [110] und [111].
- **iso-Rest:**
  - Lokale Steigung laengs [100] 4,44 bei r = 4,2; ab r = 11 genau 5,00.
  - Laengs [111]: 4,98 bei r = 14,7.
  - Laengs [110] wechselt das Vorzeichen zwischen r = 7 (+2,6e-6) und r = 8 (-9,7e-7). Danach steigt die lokale
    Steigung von 1,8 (r = 10) auf 4,39 (r = 16). Deshalb gibt das Fenster [8, 16] laengs [110] nur 2,78.
  - Lesart [H]: Ein r^-5- und ein r^-7-Term mit entgegengesetztem Vorzeichen kreuzen sich bei r etwa 7,5.
  - Das Kontinuum ist dort null (|Pi| <= 1e-11).
- **r^3 Pi_12 bei r nahe 8 (aniso):** [100] -0,746; [110] +0,559; [111] +0,763; <211> +0,114; <320> +0,047.
  Das Bild richtung_b.png zeigt die kubische Winkelstruktur.

### 3.4 Zwei parallele zu lange Staebe laengs [110] (c), korrigiert, L = 128 [E]

| Anordnung | Richtung von r | aniso r^3 Pi_12 | iso r^3 Pi_12 |
|---|---|---|---|
| Ende an Ende | [110] (r = 16) | +0,323 (Abstossung) | +0,135 (Abstossung) |
| Seite an Seite, in der Ebene | [1-10] (r = 8) | -0,0257 (Anziehung) | -0,0144 (Anziehung) |
| Seite an Seite, senkrecht | [001] (r = 8,49) | +0,0089 (Abstossung) | -0,0145 (Anziehung) |
| schraeg, 60 Grad zur Stabachse | [101] (r = 8) | -0,079 (Anziehung) | -0,026 (Anziehung) |

- Exponenten: p_schale 3,06 (aniso), 3,04 (iso). Lokale Steigung laengs [110] bei r = 16: 3,03 bzw. 3,006.
- Im iso-Netz sind [1-10] und [001] gleichwertig (beide senkrecht zur Stabachse). Gerechnet sind sie gleich auf
  0,4 %: Das Kontinuum ist dort rotationssymmetrisch.
- Gitter gegen Kontinuum fuer 12 <= r <= 16: Median 1,0 % (aniso), 0,7 % (iso).

### 3.5 Verschiebung einer einzelnen Quelle (L4) [E]

| Quelle | aniso p_u | iso p_u | L = 64 (aniso / iso) |
|---|---|---|---|
| (a) Punktlast, korrigiert | 0,998 | 0,999 | 0,998 / 0,999 |
| (a) Punktlast, Torus unkorrigiert | 1,158 | 1,155 | 1,371 / 1,367 |
| (b) Dilatationszentrum | 2,001 | 2,006 | 2,009 / 2,019 |
| (c) zu langer Stab | 2,000 | 1,994 | 2,010 / 2,003 |

- Schalen-RMS von |u| um die Quellmitte, Schalen 4 bis 16. Bild: verschiebung.png.

### 3.6 Torus und Hintergrundkorrektur [E]

| Groesse | Kante (Stablaengen) | Punktlast: Anteil dPi/Pi bei r = 8 [110] (iso) | Punktlast: Vektoren mit Pi_torus >= 0 (aniso / iso) | iso-Dilatation [110] r = 8: Pi_torus / dPi / Pi_korr |
|---|---|---|---|---|
| 32 | 45 | -55 % | 1220 / 648 von 24 166 | +6,77e-5 / 6,87e-5 / -1,01e-6 |
| 64 | 91 | -28 % | 0 / 0 | +7,61e-6 / 8,58e-6 / -9,74e-7 |
| 128 | 181 | -14 % | 0 / 0 | +1,00e-7 / 1,07e-6 / -9,73e-7 |

- **Korrektur:** dPi aus dem periodischen Kontinuum (Ewald-artig, PLAN 3.2).
- **Groessenreihe nach der Korrektur, groesste Abweichung L = 64 gegen 128 auf allen Vektoren mit 3 <= r <= 16
  (relativ zum groessten Betrag der jeweiligen Reihe):**
  - Punktlasten 3,9e-5 (aniso) und 1,9e-6 (iso), lokal hoechstens 2,1e-4.
  - Dilatation 1,2e-5 / 1,9e-7.
  - Staebe 1,3e-6 / 1,5e-6.
  - Lokal relativ gibt es bei b und c Werte bis 1,2. Sie liegen an Punkten nahe einem Vorzeichenwechsel, wo der Wert
    selbst fast null ist.
- **Ohne Korrektur:**
  - Die Punktlast-Wechselwirkung ist um einen Versatz der Ordnung 1/L zu schwach.
  - Bei L = 32 kippt sie fuer grosse r in Abstossung (torus.png). Das ist das Gegenstueck zur Scheinanziehung in
    TENSOR-EIS-0.
  - Die iso-Dilatation traegt auf dem Torus den konstanten Versatz +P^2/((lambda + 2 mu) V) = 1,073e-6 bei L = 128.
    Gerechnet sind 1,0729e-6; die Erwartung war [M].

## 4. Kontrollen

- **K1, Ortsraum-Residuum (L = 16, beide Netze, alle Quellen, sechs Paare und Einzelquellen):**
  max |dU/du - f + f_mittel| = 7,8e-16 relativ zu max|f|.
- **K2, Pi(Paar) - 2 Pi(einzeln) explizit gegen Korrelationsweg:**
  - Groesste relative Abweichung 2,6e-11.
  - Beispiel iso (a), R = (0, 0, 8)/sqrt2 (r = 5,66): -0,00540286211615 gegen -0,00540286211615.
  - Die Karten-Definition "Paar minus zweimal einzeln" ist damit genau die verwendete Groesse.
- **K3, Hilfsgitter:**
  - ungerade Punkte <= 2,1e-16 relativ;
  - genau 2 Nullpunkte (q kongruent 0) in jedem Gitter.
- **K4, Groessenreihe:** Abschnitt 3.6. Urteile mit L = 64 gleich.
- **K5, Kontinuum:**
  - Synge-Kreisintegral gegen Kelvin (iso): 1,0e-10.
  - iso-Dilatation im Kontinuum: |Pi| <= 9,7e-11, also null.
- **K6, Quadratur:**
  - Ewald 32x64 gegen 64x128: <= 7e-14 (Rauch 2); 64x128 gegen 96x192: <= 7e-14 (Rauch 1).
  - Dipolformel h gegen h/2: 8,6e-6; 128 gegen 256 phi-Punkte: 7e-11.
- **K7:** C bei |q| = 1e-4 gegen 2e-4: 2,7e-8.
- **K8:** C gegen die geschlossenen Formen: 9e-9.

## 5. Selbstanzeigen

1. **Rauchlaeufe vor dem Einfrieren:**
   - rauch1 (cpu, 21:02:19 bis 21:02:35 UTC), rauch2 (cpu6, 21:04:32 bis 21:05:08 UTC).
   - rauch3 als ganze Kette auf L = 32/64:
     - kontrolle 21:09:28, kontinuum 21:09:31 bis 21:10:21, lauf 21:09:58 bis 21:11:38, Auswertung bis etwa 21:11:55
       UTC.
   - Gesehen habe ich:
     - die elastischen Konstanten (L0, vorab ableitbar);
     - Codekontrollen K1 bis K3 bei L = 8;
     - Zeiten, Speicher und Quadraturproben.
   - Keine Pi_12-Werte, keine Exponenten, keine Urteile.
   - Von rauch3 habe ich nur Rueckgabewerte, Fehlermeldungen und Dateinamen gelesen. Die Ausgaben
     (auswertung.stdout, aus/auswertung.json, Bilder) blieben ungelesen.
   - Keine Schwelle wurde nach einem Rauchlauf geaendert.
2. **Fehlstart in rauch3:** Der erste Versuch lief durch eine falsche Klammerung (`cd ... && (...) & ...`) im
   Heimatordner und brach sofort ab (lauf und Auswertung rc = 1, ohne Rechnung). Er wurde im richtigen Ordner
   wiederholt.
3. **Codeaenderungen:**
   - Vor dem Einfrieren, nach rauch1:
     - Winkelquadratur 64x128 auf 32x64, nach der Probe in rauch2;
     - kleinere Bloecke;
     - Option --netz;
     - Modus rauch2.
   - Nach dem Einfrieren: keine. code/nachschau.py ist nachtraeglich und nur beschreibend (sha256 2acae1a3...).
4. **Festlegungen mit Gewicht [F]:**
   - Bei L2 und L3 bewerte ich nur [100], [110], [111] plus Schale (Abschnitt 2). Die strenge Lesung ueber alle
     Richtungen haette beide Teile (i) verfehlt.
   - Weitere: Last laengs [001], Stab laengs [110], r in Stablaengen, Fenster [4, 16], Huellkurven-Exponent fuer L2,
     Toleranz 0,3 bei L4, "alle Richtungen" bei L1 = alle Gittervektoren (strenger als die Liste).
5. **Knapp an der Schwelle:** L2 laengs [111] mit 0,042 gegen 0,05. Bei L = 64 ist es 0,0421, also kein
   Torus-Effekt.
6. **Vorab ableitbar [M]:**
   - L0 (geschlossene Formen), L4 (Dipolfeld r^-2) und das Vorzeichen in L1 im Kontinuum (-f.G.f < 0).
   - L2 im Kern (Bitter/Crum [L?], hier [M]: s konstant fuer isotropes Gamma).
   - Neu gerechnet sind: Gitterabweichungen und ihre Groesse, Kelvin-Genauigkeit 0,47 %, der r^-5-Rest im iso-Netz,
     Vorzeichenmuster und Torusfehler.
7. **"Kelvin" fuer das aniso-Netz:** In den Tabellen von auswertung.json gibt es diese Spalte (mu = C44,
   nu = 0,25). Physikalisch ist sie dort ohne Bedeutung und geht in kein Urteil ein.
8. **Vorzeichenkriterium:** Pi_12 < 0 ist ein Energiekriterium. Wo |Pi_12| nicht monoton faellt (iso-Dilatation
   laengs [110] bei r = 7 bis 9), zeigt die Kraft -dPi_12/dr nicht in Richtung des Vorzeichens. L1 und L3 betrifft
   das nicht.
9. **Zeitbox:** Start 22:42:21 CEST, Text ab 23:19:23 CEST, innerhalb von 120 min.

## 6. Lesart

- **[M] Mittelwert null:**
  - Die Wechselwirkung zweier Quellen ohne Nettokraft ist im Kontinuum die Fouriertransformierte einer Funktion
    s(q-Dach) vom Grad 0.
  - Ihr Integral ueber jede Kugelschale um den Ursprung ist null.
  - Eine 1/r^3-Wechselwirkung zwischen abgeschlossenen Klumpen ist also im Richtungsmittel weder anziehend noch
    abstossend.
  - Schwerkraft dagegen zieht in jeder Richtung.
- **[H] Fuer Finns Frage "Kraefte in den Staeben -> Schwerkraft?":**
  - Ein Netz, das nur ueber seine Spannungen wirkt, gibt 1/r-Anziehung nur dann, wenn eine aeussere Nettokraft an
    den Quellen zieht. Genau diese Kraft ist beim Gummituch die Erdschwere.
  - Abgeschlossene Koerper (von Laue: Spannungsintegral null) erzeugen kein 1/r-Feld.
  - Eine gravitationsartige Quelle muesste deshalb an etwas anderes koppeln als an die Staebe allein, etwa an Energie
    und Zeit (h_00, LAPSE-0). Das ist hier nicht gerechnet.
- **[H] Isotrope Abstimmung:** k_theta = 1/18 macht das Netz in elastischer Ordnung isotrop. Ein Gitterrest
  ~ r^-5 bleibt, also eine Anisotropie der Ordnung (Stablaenge/r)^2. Das passt zum Gegenleser (B1, "erst ab Ordnung
  (ka)^2").

## 7. Einfach gesagt

Haengt man an zwei Knoten eines Stabnetzes gleich gerichtete Gewichte, rutschen sie aufeinander zu, und die
Anziehung wird mit dem Abstand genau wie 1/r schwaecher, so wie bei der Schwerkraft. Das klappt aber nur, weil an den
Gewichten eine Kraft von aussen zieht, und diese Kraft ist beim Gummituch selbst schon die Schwerkraft. Steckt die
Spannung dagegen ganz im Netz (ein zu langer Stab, ein aufgeweiteter Knoten), dann spuert das andere Teilchen viel
weniger: Die Wirkung faellt wie 1/r^3, sie zieht in manche Richtungen an und stoesst in andere ab, und im Mittel bleibt
nichts. In einem richtig abgestimmten, in alle Richtungen gleich steifen Netz verschwindet sie fast ganz. Kraefte in
Staeben allein ergeben also keine Schwerkraft.
