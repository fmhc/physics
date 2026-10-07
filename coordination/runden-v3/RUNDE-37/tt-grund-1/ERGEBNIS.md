# TT-GRUND-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 44, Fast Lane)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 22:45:23 CEST. Plantext ab 23:00:53 CEST.
  - Rauchtests r1 bis r8 einzeln (keine Kette), 20:58:45 bis 21:00:17 UTC, nur Schluessel und Laufzeiten (rauch-69/).
  - Eingefroren 2026-10-04 23:02:15 CEST: PLAN.md.eingefroren-20261004-230215 (sha256 9c577ae3...), code/tg.py
    (44421625...), kette-cpu5.sh, kette-cpu10.sh; tti.py, ew.py, nachtrag_kinetik.py, tp.py unveraendert aus TT-ISO-1.
    Liste in EINGEFROREN-SHA256.txt; auf der .69 dieselben Summen (EINGEFROREN-SHA256-69.txt dort).
  - Laufketten gestartet 21:02:29 UTC (nach dem Einfrieren). cpu5: kontrolle, regeln, Karte V, Karte S, fertig
    21:05:49 UTC. cpu10: Profil S, Profil K, best, urteil, bild, fertig 21:09:55 UTC. Alle 9 Laeufe rc = 0, keine
    Zeitschranke ausgeloest (abbruch = false in beiden Profilen). Laengster Lauf 216 s.
  - Nachtrag nach Sicht (beschreibend): nachtrag_wortlaut.py, 21:09:36 bis 21:09:37 UTC auf cpu5.
  - Text dieser Datei ab 23:11:23 CEST (date).
- Alles hier ist eine synthetische Gitterrechnung auf der .69, keine Messung.
- **Kennzeichen:** [E] hier gerechnet, [M] eigene Mathematik, [P] Projektdatei, [H] Hypothese bzw. Lesart.
- **Begriffe:** J = Bewegungsgewicht (inverse Masse), J = m_Finn / m_t, Finn = 1. Ebene: y = (log10 J_Kegel,
  log10 J_Sechs), jeweils T1 = T2 (Fd-3m). Spanne = max/min - 1 ueber 13 Richtungen x 2 Zweige x |k| = 1e-3, 2e-3.
  Paarung A1R1, Regelgewicht g = 1, Netz V. S nur beschreibend.

## 1. Ergebnis zuerst

1. **Keine natuerliche Massenregel macht die Schwerewellen isotrop [E].** N1 bis N6 liegen zwischen 5,28 % (N6,
   Traegheitsmoment) und 8,06 % (N5, Netzecken). Alle sechs sind stabil. TG2 ist eingetroffen, nach Plan und nach
   Wortlaut.
   - Auch kein Potenzgesetz m ~ V^p kommt unter 0,1 %. Das Beste ist p = -3,3 mit 0,107 % (beschreibend).
2. **Die isotrope Menge ist ein langes, sehr schmales Tal [E].** Unter 1e-4 bleibt es von log10 J_Kegel = -2
   (Rand des Bereichs) bis -0,55, also ueber mindestens 1,45 Dekaden. Quer dazu ist es nur in der Groessenordnung
   1e-3 Dekaden breit (grob, Abschnitt 5).
   - Nach der Plan-Definition ist das eine **Kurve: TG1 nach Plan eingetroffen**.
   - Der Talboden ist aber nicht flach. Er faellt von 8e-5 auf 1,7e-7 bei J_Kegel ~ 0,022 und steigt danach wieder.
   - Am besten Punkt (J_Kegel = 0,0215; J_Sechs = 1,141) ist die Spanne 7,1e-8 und das Netz stabil. Das ist rund 160-mal
     besser als der TT-ISO-1-Punkt (1,1e-5); dieser liegt im selben Tal.
3. **Lesart [H]:** Eine Bedingung legt das Tal fest, die zweite aendert sich nur langsam entlang des Tals und wird bei
   einem Punkt null.
   - Bei 1e-4 sieht man deshalb eine Ein-Parameter-Schar. Bei 1e-6 ist sie noch 0,25 Dekaden lang.
   - Exakte Isotropie braucht vermutlich zwei Abstimmungen: quer zum Tal sehr genau, laengs viel weniger genau.
4. **Die ganze Spanne sitzt in der Masse [E].** Die relaxierte Steifigkeit je metrischer Amplitude ist an allen
   13 Richtungen 0,25 (Spanne 1,9e-7). Die Masse je metrischer Amplitude traegt die 6,34 % (N1) bzw. 1,1e-5
   (TT-ISO-1-Punkt) voll.
5. **Kontrollen [E]:**
   - N1 6,339 %, der TT-ISO-1-Punkt exakt 1,12e-5, N2 5,924 % wie in TT-ISO-1, 56 alte Gitterpunkte auf <= 5e-8.
   - TG0 nach Plan eingetroffen.
   - Nach Wortlaut verfehlt TG0, weil der gerundete Punkt (0,090; 1,00) neben dem schmalen Tal liegt: 1,15e-4.
   - TG1 nach Wortlaut ist verfehlt, aber nur durch einen Fehler meiner Wortlaut-Regel (negative Scheinspannen,
     Selbstanzeige 1).

## 2. Urteile (mechanisch, tg.py urteil, eingefroren 23:02:15 CEST)

| Nr | Vorhersage (Kurzform) | Wahrsch. | nach Plan | nach Kartenwortlaut | tragende Zahlen [E] |
|---|---|---|---|---|---|
| TG0 | Kontrolle: N1 gibt 6,34 % und der TT-ISO-1-Punkt (0,090; 1,00) <= 2e-5 | 90 % | **eingetroffen** | **verfehlt** | N1 0,0633881 (Abw. 1,9e-4 relativ, Grenze 1e-3); exakter Punkt (-1,04533; -0,00101) 1,122e-5, plan-gueltig; gerundeter Punkt (0,090; 1,00) 1,148e-4 > 2e-5 |
| TG1 | [H] Menge mit Spanne < 1e-4 ist eine Kurve, kein Punkt, kein Gebiet | 65 % | **eingetroffen** (Kurve) | **verfehlt** ("Gebiet", Artefakt, s. Selbstanzeige 1) | Plan: R_max = 1,45 Dekaden (Profil K, 30 Werte von -2,00 bis -0,55), Profil S 0,25 Dekaden (6 Werte); kein 3x3-Block unter 1e-4 (0 von 159^2); 3 Rasterpunkte unter 1e-4. Wortlaut: 300 Bloecke, alle aus negativen Scheinspannen |
| TG2 | [H] keine der Regeln N2 bis N6 liegt unter 0,1 % | 75 % | **eingetroffen** | **eingetroffen** | kleinste N6 5,275 %; keine Regel unter 1e-3 |

- **Bedeutung, wie auf der Karte vorab festgelegt:**
  - **TG2 trifft ein:** Fuer das isotrope Massenverhaeltnis gibt es keinen der naheliegenden Gruende. Es bleibt eine
    Abstimmung. Die Kristall-Lesart braucht einen neuen Grund [H].
  - **TG1 trifft ein (nach Plan):** Laut Karte gibt es eine Ein-Parameter-Schar isotroper Massen; ein Grund muesste nur
    eine Bedingung erfuellen.
    - Vermerk [E]: Das gilt fuer die Schwelle 1e-4.
    - Entlang der Schar aendert sich die Spanne von 1,7e-7 bis 1e-4. Fuer kleinere Schwellen schrumpft die Schar zu
      einem Stueck um den besten Punkt.
    - Fuer c_T/c - 1 ~ 1e-15 reicht eine Bedingung nach diesen Zahlen nicht [H].
- Agenten-Erwartung vorab (kein Urteil): TG1 Kurve 35 %, Punkt 50 %; TG2 eingetroffen 85 %.

## 3. Regeln N1 bis N6 (V, Hauptergebnis; S beschreibend)

J = m_Finn / m_t aus der Geometrie (Plan 1.4). Der Lauf hat sie aus den Code-Koordinaten nachgerechnet; die
Abweichung zum Plan ist <= 1,1e-15. "stabil ja" heisst: plan-gueltig und an den 511 k (L = 8) 0 negative und
0 komplexe omega^2. Werte aus lauf-69/regeln.json [E].

| Regel | Masse ~ | J_Kegel | J_Sechs | Spanne V | stabil V | omega^2/k^2 V (min bis max) | Spanne S (J_Achse) | stabil S |
|---|---|---|---|---|---|---|---|---|
| N1 | gleich | 1 | 1 | 6,339 % | ja | 0,11889 bis 0,12643 | 2,685 % (1) | ja |
| N2 | Volumen | 4/5 | 4/3 | 5,924 % | ja | 0,14807 bis 0,15684 | 6,408 % (2/3) | ja |
| N3 | 1/Volumen | 5/4 | 3/4 | 6,361 % | ja | 0,09819 bis 0,10443 | 0,294 % (3/2) | ja |
| N4 | Volumen^2 | 16/25 | 16/9 | 5,558 % | ja | 0,18833 bis 0,19879 | 10,743 % (4/9) | ja |
| N5 | Netzecken (4/3/2) | 4/3 | 2 | 8,064 % | ja | 0,22041 bis 0,23819 | 2,200 % (2) | ja |
| N6 | Traegheitsmoment (Spur) | 64/95 = 0,6737 | 64/49 = 1,3061 | 5,275 % | ja | 0,14351 bis 0,15108 | 9,413 % (1/2) | ja |
| bester Punkt | - | 0,02148 | 1,14084 | 7,06e-8 | ja | 0,1175452 bis 0,1175452 | - | - |

- An den 511 k ist das kleinste omega^2 relativ zum groessten bei allen Regeln 0,014 bis 0,015 (V) bzw. 0,030 bis
  0,033 (S); B_red und A_red sind an allen 511 k positiv definit.
- Die Spanne an den 23 Hauptlauf-Richtungen ist in V gleich der an den 13 Plan-Richtungen; in S weicht sie hoechstens
  um 1e-8 ab.
- Abstand der Regeln zum naechsten Talbodenpunkt unter 1e-4 (beschreibend): 0,49 (N6) bis 0,84 Dekaden (N5). Der
  naechste ist fuer alle das Ende des Teilstuecks bei (-0,544; -0,200).
- In S kommt N3 (Masse ~ 1/Volumen) mit 0,29 % am naechsten, aber nicht unter 0,1 % (beschreibend).

## 4. Bild: Spannenkarte mit isotroper Menge und Regelpunkten

![Spannenkarte V](lauf-69/spannenkarte-V.png)

- Datei lauf-69/spannenkarte-V.png (sha256 094e2dae...), vom eingefrorenen tg.py (Modus bild) auf der .69 gezeichnet.
- **Links:** log10 Spanne auf dem Raster 161 x 161. Weiss heisst: nicht plan-gueltig.
  - Konturen bei 1e-3 (orange) und 1e-2 (rot). Die 1e-4-Kontur ist auf dem Raster nicht zu sehen; dafuer ist das Tal
    zu schmal (nur 3 Rasterpunkte).
  - Weisse und cyan Punkte: verfeinerte Talbodenpunkte unter 1e-4 aus den zwei Profilen.
  - Rote Kreise: N1 bis N6. Stern: TT-ISO-1-Punkt. Kreuz: bester Punkt. Gestrichelt: Potenzgesetz-Gerade.
- **Rechts:** kleinste Spanne quer zum Profil, ueber log10 J_Sechs (blau) und ueber log10 J_Kegel (orange), mit der
  Schwelle 1e-4.

## 5. Form der Menge (Einzelheiten) [E]

- **Karte V (161 x 161, Schritt 0,025):**
  - 18 462 von 25 921 Punkten sind plan-gueltig. Unter 1e-2: 723, unter 1e-3: 55, unter 1e-4: 3, unter 1e-5: 0.
  - Kein 3 x 3-Block liegt unter 1e-4. Die 3 Punkte sind getrennte Einzelpunkte.
  - Rasterminimum 1,93e-5 bei (-1,05; 0,00).
- **Profil K** (Minimum ueber log10 J_Sechs fuer 81 Werte log10 J_Kegel):
  - Unter 1e-4 durchgehend von -2,00 bis -0,55 (30 Werte). Der Talboden liegt dabei bei log10 J_Sechs = 0,066 bis
    -0,195.
  - Boden 1,5e-6 bei -2,00; Minimum 1,7e-7 bei -1,65; 1,1e-5 bei -1,05 (TT-ISO-1-Punkt); 8,0e-5 bei -0,55; 1,03e-4
    bei -0,50.
  - Danach folgt ein zweiter Ast. Er steigt bis 7,4e-4 bei log10 J_Kegel ~ 0 und faellt bis 2,2e-4 bei +2. Dort liegt
    das zweite TT-ISO-1-Minimum (A2R1-Lauf, 3,3e-4).
- **Profil S** (Minimum ueber log10 J_Kegel fuer 81 Werte log10 J_Sechs):
  - Unter 1e-4 von -0,20 bis +0,05 (6 Werte); auf diesem Stueck steht das Tal schraeg zur Profilachse.
  - Bei +0,05 liegt der Wert 1,3e-6 bei log10 J_Kegel = -1,52. Ab +0,10 springt das Minimum auf den zweiten Ast
    (2,2e-4 bis 3,0e-4).
- **Bester Punkt** (Nelder-Mead aus dem besten Profilminimum, 524 Auswertungen):
  - y = (-1,66799; 0,05723), J_Kegel = 0,02148, J_Sechs = 1,14084. Spanne 7,06e-8 (13 und 23 Richtungen),
    omega^2/k^2 = 0,1175452.
  - Stabil an den 511 k, keine negative Mode bei kleinem k, Luecke 1,4e-7.
- **Entlang der Menge** (5 Talbodenpunkte, beschreibend): bei log10 J_Kegel = -2,00; -1,55; -1,15; -0,84; -0,54 mit
  Spanne 1,5e-6 bis 8,2e-5. Alle stabil (0 negativ, 0 komplex an den 511 k).
- **Plan-Beschreibung "Kurve exakter Isotropie"** (ganzer Lauf mit Boden < 1e-6 ueber >= 0,25 Dekaden): 0 Laeufe.
  - Nachtrag nach Sicht: Ein Teilstueck von -1,80 bis -1,55 (6 Werte, 0,25 Dekaden) bleibt unter 1e-6.
- **Steilheit [E, grob aus zwei Punkten, nach Sicht]:**
  - Quer zum Tal: Der gerundete TT-ISO-1-Punkt liegt etwa 1e-3 Dekaden neben dem exakten, und die Spanne steigt dort von
    1,1e-5 auf 1,15e-4, also um etwa 0,1 je Dekade.
  - Laengs des Tals: Vom Minimum aus steigt sie um etwa 4e-6 (Richtung -2) bis 7e-5 je Dekade (Richtung -0,55).
  - Das Tal ist damit rund 1 000- bis 20 000-mal flacher laengs als quer.
- **S (beschreibend):** Raster 81 x 81. Minimum 7,4e-5 bei (-0,15; 0,10), 2 Rasterpunkte unter 1e-4, kein Block. Ein
  schmales Tal gibt es also auch dort; Profile fuer S wurden nicht gerechnet.

## 6. Kontrollen (lauf-69/kontrolle.json, karte-V.json)

- **a) Geometrie [E]:**
  - Volumen x 768: Finn 4, Kegel 5, Sechseck 3, Achse 6. Netzecken: 4, 3, 2, 2.
  - Ipol x 8^5: 1,6; 2,375; 1,225; 3,2. Das sind genau die Planwerte 8/5, 19/8, 49/40, 16/5.
  - Die J der Regeln weichen hoechstens um 1,1e-15 vom Plan ab. T1 und T2 sind je Art gleich.
  - Haupttraegheitsmomente (x 8^5): Finn 1,067 dreifach (kugelfoermig), Kegel 1,333 / 1,708 / 1,708, Sechseck 0,529 /
    0,825 / 1,096.
- **b) TG0 [E]:**
  - N1 0,06338810, also 6,339 %.
  - TT-ISO-1-Punkt exakt 1,1221e-5, gleich dem TT-ISO-1-Wert (1,1221128e-5) bis auf die letzte Stelle.
  - Gerundeter Punkt (0,090; 1,00): 1,148e-4.
- **c) Steifigkeit gegen Masse [E]:**

| Fall | Spanne kappa (Steifigkeit) | kappa | Spanne mu (Masse) | Spanne omega^2 weich / Z-Verfahren | Abw. weich gegen Z |
|---|---|---|---|---|---|
| V, N1 | 1,9e-7 | 0,2500000 (+-2,6e-8) | 6,339 % | 6,339 % / 6,339 % | <= 8,7e-8 |
| V, TT-ISO-1-Punkt | 1,9e-7 | 0,2500000 | 1,119e-5 | 1,12e-5 / 1,12e-5 | <= 1,1e-7 |
| S, N1 | 1,1e-7 | 0,2500000 | 2,685 % | 2,685 % / 2,685 % | <= 4,5e-8 |

  - Die Euklidischen Eigenwerte von B_red / k^2 sind dagegen richtungsabhaengig (0,0245 bis 0,0346). Erst die
    Normierung je metrischer Amplitude macht sie isotrop. Die Steifigkeit ist relaxiert gleich der affinen aus TT-ISO-1
    (1/4).
  - Fit-Rest der Tensoranpassung <= 3e-9.
- **d) TT-ISO-1-Gitter [E]:** 56 plan-gueltige symmetrische Punkte stimmen auf <= 5,0e-8 absolut (Rundung der alten
  Datei). 25 Punkte sind in beiden ungueltig, keiner ist nur in einem gueltig.

## 7. Ableitbarkeit

- **Schreibtisch der Leitung [M, E]:**
  - p ~ 10,8 stimmt (10,79). Kein Potenzgesetz trifft den TT-ISO-1-Punkt, weil J_Sechs = 1 p = 0 verlangt (Plan 1.1).
  - Gerechnet: Die Potenzgesetz-Gerade kreuzt das Tal nur auf dem zweiten Ast. Dort ist der Boden 2e-4 bis 7e-4; auf
    der Geraden ist das beste 0,107 % bei p = -3,3.
  - Die Aussage gilt also auch fuer die ganze Menge, nicht nur fuer den Punkt.
- **Freie Verhaeltnisse [M]:** In der symmetrischen Ebene gibt es 2, beide auf der Massenseite; B hat keinen freien
  Parameter, g = 1. Die Steifigkeit traegt nichts zur Spanne bei (6c). Isotropie ist hier also allein eine Frage des
  Massenverhaeltnisses.
- **Vorab bekannt [P]:**
  - N1 (6,34 %) und N2 (5,92 %, Nachtrag A2R1) waren bekannt; TG2 war fuer N2 also vorab entschieden. Beide sind
    reproduziert.
  - N3 bis N6 und die Form der Menge waren nicht ableitbar.
- **TG0-Wortlaut:** Das Risiko stand vorab im Plan (1.3). Wie gross es ist, zeigte erst die Rechnung: Das Tal ist nur
  etwa 1e-3 Dekaden breit.
- **Gegen die Vorhersage der TT-ISO-1-Lesart "isolierter Punkt in zwei Verhaeltnissen":** Bei 1e-4 stimmt sie nicht
  (Kurve). Beim Boden ist sie als Lesart [H] weiter moeglich (ein Minimum 1,7e-7 bzw. 7e-8 auf dem Tal).

## 8. Selbstanzeigen

1. **Fehler in meiner Wortlaut-Regel:**
   - Der Plan setzte "Wortlaut-gueltig: jeder endliche Wert", anders als TT-ISO-1 (dort musste die Klassifikation
     eindeutig sein).
   - An 698 der 25 921 Rasterpunkte ist max/min - 1 negativ, weil die zwei betragsgroessten 1/omega^2 nicht beide
     positiv sind. Diese Scheinspannen zaehlen als "< 1e-4" und ergeben 300 Bloecke, also "Gebiet".
   - TG1 nach Wortlaut ist damit mechanisch verfehlt, aber das ist ein Artefakt der Regel.
   - Nachtrag nach Sicht (code/nachtrag_wortlaut.py, sha256 fb46a81b...; lauf-69/nachtrag-wortlaut.json): Alle 300
     Bloecke stammen aus negativen Werten. Mit der Zusatzbedingung Spanne >= 0 gibt es 0 Bloecke, 3 Punkte (wie Plan) und
     keinen Punkt, der nur nach Wortlaut darunter liegt. Alle 122 Wortlaut-Verfeinerungen der Profile sind negativ.
   - Mit dieser Zusatzbedingung waere der Wortlaut gleich dem Plan (Kurve). Das ist ein Nachtrag und kein Urteil.
2. **Kurve nach Definition, Boden nicht flach:**
   - Die Plan-Definition (Schwelle 1e-4, Lauf >= 0,25 Dekaden) nennt das Tal eine Kurve.
   - Der Boden faellt aber um fast drei Groessenordnungen zu einem Minimum. Die Lesart "eine Bedingung plus ein
     langsamer zweiter Parameter" ist [H].
   - Die Steilheiten in Abschnitt 5 sind grob, aus wenigen Punkten und nach Sicht.
3. **Nach Sicht hinzugekommene Beschreibungen:** das Teilstueck unter 1e-6, die Steilheiten, "zweiter Ast", der Verlauf
   der Potenzgesetz-Geraden relativ zum Tal (aus dem Bild). Sie stehen in keinem Urteil.
4. **Abstand der Regeln:** Er ist nur zu den 36 Talbodenpunkten unter 1e-4 gemessen, nicht zum Tal selbst (das Tal mit
   Boden 1e-4 bis 1e-3 liegt den Regeln naeher). Beschreibend.
5. **Werkzeuge:**
   - Vor dem Einfrieren habe ich mit dem Edit-Werkzeug eine Kopie tg.py.neu bearbeitet (Laufzeitfelder der Rauchausgabe)
     und per mv ersetzt; kein sed -i.
   - Die Rauchlaeufe schrieben die vollen Daten zusaetzlich in *.roh-Dateien (fuer die Rauchtests von best, urteil und
     bild). Ich habe sie nicht gelesen und vor dem Einfrieren auf der .69 geloescht. r8 zeichnete ein Bild aus
     Konstanten.
   - Gestartet habe ich mit setsid und nohup ueber ssh. Gewartet habe ich mit until-Schleifen und sleep auf der .69.
   - jq nur zum Lesen. Lokal lief kein python, awk oder perl.
6. **Vor dem Plan gelesen:** aus TT-ISO-1 verf-V-A1R1.json den symmetrischen Bestpunkt mit Spanne und omega^2-Bereich
   und Laufzeiten, aus gitter-V-A1R1.json Schluessel und Laufzeiten. Diese Werte standen schon im TT-ISO-1-ERGEBNIS.
7. **Bester Punkt nicht als Minimum belegt:** Nelder-Mead hat abgebrochen. Ob der Boden bei 7e-8 echtes Null plus
   Dispersion zwischen |k| = 1e-3 und 2e-3 ist, habe ich nicht getrennt.
8. **Kein unabhaengiges Gegenlesen** in der Zeitbox; das bleibt der Leitung.

## 9. Einfach gesagt

Wir haben am Computer gesucht, ob eine einfache Regel fuer die Massen der Tetraeder-Sorten die Schwerewellen auf Finns
gefuelltem Netz in alle Richtungen gleich schnell macht. Sechs naheliegende Regeln (gleich schwer, nach Volumen, nach
Ecken, nach Traegheitsmoment und so weiter) helfen alle nicht: Die Wellen bleiben um 5 bis 8 % richtungsabhaengig. Die
guten Massenverhaeltnisse bilden eine lange, aber haarfeine Rinne in der Landkarte der Moeglichkeiten; in ihr ist das
Tempo bis auf ein Zehntausendstel gleich, an einer Stelle (Kegel rund 47-mal so traege wie Finns Tetraeder) sogar bis auf
etwa ein Zehnmillionstel. Einen natuerlichen Grund fuer genau diese Rinne haben wir nicht gefunden; es bleibt eine
Feineinstellung.

## 10. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-230215, EINGEFROREN-SHA256.txt, KARTE.md (Leitung).
- code/: tg.py (Laeufe), kette-cpu5.sh, kette-cpu10.sh, je mit .eingefroren-20261004-230215; tti.py, ew.py,
  nachtrag_kinetik.py, tp.py unveraendert aus TT-ISO-1 (ebenfalls eingefroren kopiert); nachtrag_wortlaut.py (Nachtrag
  nach Sicht, nicht eingefroren).
- lauf-69/: kontrolle.json, regeln.json, karte-V.json, karte-S.json, profil-S-V.json, profil-K-V.json, best-V.json,
  urteil.json, bild.json, spannenkarte-V.png, nachtrag-wortlaut.json, Logs. PRUEFSUMMEN.txt (lokal) und
  PRUEFSUMMEN-69.txt (.69) sind gleich. Alle 9 Laufdateien nennen tg.py 44421625... (eingefroren).
- rauch-69/: r1 bis r8 (nur Schluessel und Laufzeiten).
- Auf der .69: /home/fmh/fmhc-physics-remote/tt-grund-1/ (code/, ref/gitter-V-A1R1.json, rauch/, lauf/).

Abschluss des Textes 2026-10-04 23:13:55 CEST (date). Die Zeitbox von 60 min ab 22:45:23 CEST endet um 23:45:23; sie ist eingehalten. Kein Lauf
ist mehr aktiv (beide Ketten beendet 21:05:49 bzw. 21:09:55 UTC, Nachtrag 21:09:37 UTC). Journal, Peerbus und Commit
uebernimmt die Leitung.
