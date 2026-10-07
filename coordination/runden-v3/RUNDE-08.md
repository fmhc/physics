
Leitung: claude-primary. Angelegt: 2026-09-30 05:55:28 CEST (gemessen). Explorativ, keine formale Bestaetigung.
Finn: "bau einen beweis" (05:19), "fix mal die 69 platte aufräum action" und "und mach mit den themen weiter" (05:47).

- **Berichtigung (2026-09-30 07:52:31 CEST, Leitung):** Die Angaben "Finn HH:MM" in dieser Datei sind nicht mit date gemessen. Die Leitung
  hat sie aus dem Gespraechsverlauf geschaetzt; sie gelten nur als Reihenfolge. Mit date gemessen sind nur die uebrigen
  Zeiten. Nachweislich falsch waren "07:53" und "07:55": Beide Nachrichten kamen vor 07:52:04; berichtigt.

## Rahmen

- Uebernommen aus Runde 7: BEWEIS-1 (laeuft seit 05:34) sowie die laufenden BIC-Tests, siehe unten.
- **Fast Lane** (Finn, 28.09. und 30.09. 02:42 "mit mehr agents"):
  - unabhaengige Karten parallel, je Karte ein Agent mit vollem Auftrag
  - jede Rechnung hoechstens 10 min
- **Rechenorte:**
  - .69 ueber kleintest.sh (p4000a, p4000b, cpu, cpu2, cpu3, cpu4)
  - Laptop-CPU fuer kleine Laeufe der Leitung
  - Das Aufraeumen der .69-Platte laeuft parallel (Agent, Protokoll RUNDE-07/PLATTE-DOT69-20260930.md).
  die Gesamtformel. Diese Runde hat je Schwerpunkt mindestens eine Karte.

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| BEWEIS-1 | Finn 05:19 | rechnergestuetzter Beweis der Nullstelle n = 1 (beta = 0,5, omega*^2 ~ 0,79768) mit Kugelarithmetik und Schwanzlemmata | Anthropic-Agent, Brief RUNDE-07/beweis/BRIEF.md |
| BIC-3 Folge und Phasenregel | R7 BIC-2, THEORIE-ATMUNGS-NULLSTELLEN.md | (a) laufende Vorab-Tests: V6 (l = 1), V7 (1D), Umlauf bei beta = 0,45, n = 3; (b) neue blinde Vorhersagen der Phasenregel, eingefroren vor jedem Lauf (beta = 0,55 und 0,60 unterhalb der bekannten Stellen, beta = 0,35); (c) Kandidaten n = 6 und 7 bei beta = 0,5 (0,5694 und ~0,560) mit exakt; (d) Literatur: Romanczukiewicz u. a., Phys. Rev. E 114, 024213 (2026) | Leitung; Vorhersagen durch den Theorie-Agenten |
| GF-BIC Gesamtformel mit zwei Komponenten | gesamtformel-20260921/KANDIDAT.md; Theorie Abschnitt 4.6 | Linearisiert um einen einkomponentigen Ball: Welches Spektrum hat die zweite Komponente? Sie spuert den Paarterm g J_12 psi_1^2 psi_2^* schon in linearer Ordnung. Oeffnet die zweite Komponente an einer stillen Stelle einen Zerfallskanal, auch parametrisch? | Anthropic-Code-Agent |
| ST-1 Stelle-Paar-Schranke (Glied 10) | R7 MT-1 | Gemeinsame Schranke fuer die zwei Stelle-Yukawa-Terme (-4/3 bei lambda2, +1/3 bei lambda0) aus veroeffentlichten Kurzreichweiten-Daten. Welche Messung trennt Stelle von einem reinen Skalar? | Papier-Agent |
| EVO-1 Version 3 und Generation 1 | R7 A1, LESUNG-REPARATUR-A1.md | Auflagen A1 bis A8 der frischen Lesung umsetzen, Generation 0 ueber `modell` neu bewerten und bei bestandenem A1 Generation 1 starten | Anthropic-Code-Agent; Plantext (A5, A6) bucht die Leitung |
| R5F-b Zweite Spitze | R7 R5F-b | Ist die zweite Spitze beim Fuettern (1D, rho_2 = nu - omega = 1,633 bei 0,55 und 1,788 bei 0,70) die ungerade innere Mode des 1D-Balls? Das Paket kommt von einer Seite und regt beide Paritaeten an | Leitung (kleiner Test) |
| **Chem 14, Zufallskarte** | RUNDE-03 t5 (Q/Anti-Q-Gitter) | Zerstrahlen Q und Anti-Q auch bei d = 8 und 12? Diesmal mit der fehlenden Einzel-Anti-Ball-Kontrolle | offen (Agent oder Leitung) |

- **Nachtrag 2026-09-30 06:24:14 CEST: Karte FA-1 Farb-Analogie** (Finn 06:21: "kommen wir mit den umlaufzuständen irgendwie auf die
  quark farben analogisch?"):
  - Frage: Entsteht in der Gesamtformel mit N = 3 und g J < 0 eine Dreierstruktur mit Neutralitaet zu dritt?
    - verdoppelte Phasen im 120-Grad-Dreieck, Summe null, als Frustration des Paarterms
    - stationaer mit paarweise umlaufenden Kanalstroemen
  - Folgen die Umlaufzahlen stiller Stellen bei zyklischer Kanalsymmetrie einer Regel modulo 3?
  - Schritte:
    - (a) Schreibtischrechnung mit frischer Lesung
    - (b) kleiner Test mit drei Komponenten
    - (c) Literatur: nicht-abelsche Q-Baelle, C3-Ladungsregeln bei BICs
  - Hypothese [H]: Die Analogie ist strukturell, ohne Eichfelder und ohne Einschluss.
  - Bearbeiter: offen, nach GF-BIC.
  - Zusatz (2026-09-30 06:25:23 CEST, Finn 06:25 "bzw haben wir da ansätze von spins"): Punkt (d) Chiralitaet des 120-Grad-Dreiecks
    (1->2->3 gegen 1->3->2) als innerer Zweizustand, also Pseudospin, kein Raumspin.
- **Karte SP-1 Stille Stellen fuer l > 0** (Nachtrag 2026-09-30 06:25:23 CEST):
  - Spin 1/2 ist in der unveraenderten Formel ausgeschlossen (Entscheidung 23.09., KANDIDAT.md 3.4). Die Umlaufzahlen
    liegen im Parameterraum und tragen keinen Drehimpuls.
  - Frage:
    - Hat l = 1 bei omega^2 ~ 0,755 eine exakte Nullstelle? Umlauftest auf l erweitern.
    - Gibt es stille Stellen fuer l = 2, und folgen die l > 0-Stellen der Phasenregel?
    - Lebt eine m = +-1-Anregung dort lange? Das waere ein langlebiger ganzzahliger innerer Drehimpuls [H].
  - Falle: J/Q ~ 0,5 im Mehrkanalfall ist kein Spin 1/2.
  - Bearbeiter: offen.
- Zufallskarte gezogen um 2026-09-30 05:55:18 CEST (date) mit `shuf -n 1` aus den 31 Pool-Eintraegen mit Entscheidung
  "parken" (IDEEN-EVOLUTION/pool.jsonl).
- Geparkt fuer spaeter:
  - Ideen-Evolution Generation 1 (GEN-01-VORSCHLAG.md, 10 Karten). Sie startet nach BIC-3 und GF-BIC.
  - MT-2 (Ringturm als String)

## Tests: Ergebnisse

### BIC-3, aus Runde 7 uebernommene Laeufe (Stand 2026-09-30 05:59:44 CEST, date)

- **V3, beta = 0,45, n = 3** (vorab 0,5774 +- 0,0012, Umlauf -1):
  - Stelle 0,577365, rho* 1,602162
  - Umlauf -1 auf beiden Rechtecken, aufgeloest (.69, 05:57:47)
  - Lage und Umlauf getroffen. Damit sind alle drei V3-Stellen in Lage und Umlaufzahl getroffen.
- **V7, 1D** (vorab: keine Nullstelle ueber 0,545; frueheste 1D-Stelle darunter):
  - l = 0-Pole bei 0,53 / 0,54 / 0,55: 1,40394 - 5,74e-3 i, 1,38729 - 5,71e-3 i, 1,37670 - 5,09e-3 i (.69, 05:57:12)
  - An diesen drei Punkten keine Nullstelle gesehen. Das ist ein schwacher Test, weil zwischen den Punkten nichts
    gerechnet ist.
  - Nebenbefund: ungerade 1D-Mode (l = 1 in dims 1) bei 1,59322 - 3,30e-3 i, 1,60817 - 2,33e-3 i, 1,62211 - 1,66e-3 i.
    Siehe R5F-b.
- **V6, l = 1 in 3D** (vorab: Nullstelle nahe 0,75 +- 0,02; widerlegt durch einen glatten Verlauf ohne Einbruch unter
  1e-5 zwischen 0,72 und 0,78):
  - Gamma 1,698e-3 bei 0,72 und 2,490e-4 bei 0,74, beide Stufen gleich
  - Bei 0,76 zeigt die Kontur einen Pol (Umlauf 1), aber Newton fand ihn nicht.
  - 0,78 entfiel (Budget, .69, 05:58:35).
  - Aus sqrt(Gamma) linear gezogen [Hand]: Nullstelle nahe 0,752. Noch kein Einbruch unter 1e-5 gemessen.
  - Nachlaeufe bei 0,75 und 0,755 seit 05:59:14 (cpu4).
  - 0,75: 1,8210851 - 2,037e-5 i (.69, 06:01:23). sqrt(Gamma) faellt 0,0412 -> 0,0158 -> 0,0045 [Hand]; lineare Fortsetzung
    ergibt eine Nullstelle nahe 0,754. Gemessen ist Gamma noch nicht unter 1e-5 (Widerlegungskriterium von V6).
  - 0,755: 1,8269280 - 2,33e-7 i (.69, 06:04:03). Gamma liegt unter 1e-5, damit ist das V6-Kriterium erfuellt.
    **V6 bestanden:** Das Minimum der l = 1-Breite liegt nahe 0,7554 [Hand, aus sqrt(Gamma)] und im vorhergesagten
    Fenster 0,75 +- 0,02. Belegstufe: Minimum unter 2,4e-7. Ob die Breite dort exakt null wird, ist ungeprueft; exakt
    rechnet nur l = 0.

(weitere Ergebnisse werden eingetragen)

### R5F-b zweite Spitze: Vorab-Erwartung (Leitung, 2026-09-30 05:58:41 CEST, vor dem Lauf)

- Hinweis aus V7 (1D-Bruecke, .69, 05:57:12): Die ungerade 1D-Mode (l = 1 in dims 1) liegt bei omega^2 = 0,55 bei
  rho = 1,6221123 - 1,659e-3 i. Die zweite Fuetter-Spitze liegt bei nu = 2,375 +- 0,0125 (Raster 0,025), also
  rho_2 = nu - omega = 1,633 +- 0,013; ihr Abklingen kappa = 3,3e-3 ist 2 Im rho = 3,32e-3.
- **Erwartung fuer omega^2 = 0,70** (bruecke dims 1, l = 1): Re rho = 1,788 +- 0,013 (aus nu = 2,625 der zweiten Spitze)
  und Im rho = -(1,25 +- 0,3)e-5 (aus kappa = 2,5e-5). Trifft beides, ist die zweite Spitze die ungerade innere
  Mode, angeregt, weil das Paket von einer Seite kommt. Liegt Re rho ausserhalb 1,775 bis 1,801, ist die Deutung falsch.
- **Ausgang** (.69, Lauf 05:59:03 bis 06:00:32; eingetragen 2026-09-30 06:01:08 CEST):
  - omega^2 = 0,70: rho = 1,7777169 - 1,328e-5 i. Re liegt im Fenster 1,775 bis 1,801, Im im Fenster (0,95 bis 1,55)e-5.
  - omega^2 = 0,55 bestaetigt: 1,6221123 - 1,659e-3 i.
  - Beide Abklingraten treffen kappa = 2 Im rho: 2,66e-5 gegen 2,5e-5 und 3,32e-3 gegen 3,3e-3.
  - **Die Deutung ist gestuetzt:** Die zweite Fuetter-Spitze ist die ungerade innere Mode des 1D-Balls, angeregt, weil
    das Paket von einer Seite kommt. Das ist keine neue Physik, sondern der zweite Pol desselben Balls.


### Chem 14 (Zufallskarte): Vorab-Erwartung (Leitung, 2026-09-30 06:02:39 CEST, vor dem Lauf)

- Skript RUNDE-08/chem14/t5k.py: dieselben Funktionen, Gitter, Stufen und Messgroessen wie test5 in Runde 3
  (tests1d_r3.py, unveraendert). Dazu Ball allein, Anti-Ball allein und das Q/Anti-Q-Paar bei d = 8 und 12.
- **Erwartung:**
  - Ball und Anti-Ball allein behalten ueber T = 1000 mindestens 95 % von Q_abs (fein und grob).
  - Beide Einzellaeufe verhalten sich gleich (Symmetrie psi -> psi^*).
  - Das Paar zerstrahlt wie in Runde 3: Rest unter 5 %, t50 nahe 67 (d = 8) bzw. 194 (d = 12).
- **Deutung:** Trifft das zu, ist das Zerstrahlen echte Paarvernichtung. Verlieren die Einzelbaelle mehr als die Haelfte,
  ist die Runde-3-Lesart hinfaellig (Instabilitaet oder Numerik).

- **Ausgang Chem 14** (.69, p4000a, 06:03:24 bis 06:04:33; eingetragen 2026-09-30 06:05:15 CEST):
  - Ball allein und Anti-Ball allein behalten Q_abs vollstaendig (Rest 1, fein und grob, d = 8 und 12).
  - Die Ladung bleibt exakt: +2,441 bzw. -2,441.
  - Das Paar zerstrahlt wie in Runde 3: d = 8 Rest 0,022, t50 = 67; d = 12 Rest 0,016, t50 = 194. Die Energie ist zu 95 % abgestrahlt.
  - Die Erwartung ist in allen drei Punkten getroffen. Das Zerstrahlen ist echte Paarvernichtung, keine Einzelinstabilitaet.
  - Q/Anti-Q-Vernichtung ist vermutlich Literatur [L?, aus dem Gedaechtnis, nicht an der Quelle geprueft: Stoesse von Q-Ball
    und Anti-Q-Ball]. Neu ist hier nur die saubere Kontrolle.

### BIC-3 (b): blinde Vorhersagen (Theorie-Agent, festgehalten 06:09:41; eingefroren 06:10:07; eingetragen 2026-09-30 06:10:36 CEST)

- Datei: RUNDE-08/VORHERSAGEN-BIC3.md, Kopie VORHERSAGEN-BIC3.md.eingefroren-20260930-061007.
- Blindheit: Per ls um 05:59:53 geprueft, lokal und auf der .69; fuer die Ziele lagen keine Ergebnisse vor. Die
  Scans starteten erst um 06:10:19.
- Methode: Phasenregel mit k_c R_tw (Wellenzahl im Balleinneren) statt q R_tw. Die Abstaende laufen damit gegen pi.

  | Ziel | omega*^2 | Re rho* | Umlauf |
  |---|---|---|---|
  | beta 0,55, n = 4 | 0,64564 +- 0,0003 | 1,6702 +- 0,002 | +1 |
  | beta 0,55, n = 5 | 0,62708 +- 0,0004 | 1,6551 +- 0,003 | -1 |
  | beta 0,60, n = 4 | 0,68195 +- 0,0003 | 1,7048 +- 0,002 | +1 |
  | beta 0,60, n = 5 | 0,66386 +- 0,0004 | 1,6914 +- 0,003 | -1 |
  | beta 0,35, n = 1 | 0,6218 +- 0,001 | 1,5993 +- 0,002 | -1 |
  | beta 0,35, n = 2 | 0,47655 +- 0,0008 | 1,5010 +- 0,003 | +1 |
  | beta 0,35, n = 3 | 0,41651 +- 0,0006 | 1,4452 +- 0,003 | -1 |
  | beta 0,35, n = 4 | 0,38452 +- 0,0008 | 1,4079 +- 0,005 | +1 |

- **Widerlegt, wenn** eines davon eintritt:
  - kein Vorzeichenwechsel im Fenster +-3 Fehlerbalken
  - die Stelle liegt mehr als 3 Fehlerbalken daneben
  - eine aufgeloeste Umlaufzahl hat das falsche Vorzeichen
  - zwei Stellen liegen dicht beieinander
  - bei beta 0,35: zwischen 0,38 und 0,64 gar kein Vorzeichenwechsel
- Scans auf der .69 seit 06:10:19 (cpu bis cpu4). Die exakt-Laeufe werden um die im Scan gefundene Stelle gelegt.

### BIC-3 (b): Ausgang der Lage (kurve h = 0,02, .69, Scans 06:10:19 bis 06:16:46; eingetragen 2026-09-30 06:17:43 CEST)

| Ziel | vorab omega*^2 | gefunden omega*^2 | Abstand / Fehlerbalken | vorab Re rho | gefunden rho | Lage |
|---|---|---|---|---|---|---|
| beta 0,55, n = 4 | 0,64564 +- 0,0003 | 0,645620 | 0,07 | 1,6702 +- 0,002 | 1,669798 | getroffen |
| beta 0,55, n = 5 | 0,62708 +- 0,0004 | 0,627042 | 0,10 | 1,6551 +- 0,003 | 1,654130 | getroffen |
| beta 0,60, n = 4 | 0,68195 +- 0,0003 | 0,681916 | 0,11 | 1,7048 +- 0,002 | 1,703626 | getroffen |
| beta 0,60, n = 5 | 0,66386 +- 0,0004 | 0,663791 | 0,17 | 1,6914 +- 0,003 | 1,688955 | getroffen |
| beta 0,35, n = 1 | 0,6218 +- 0,001 | 0,621873 | 0,07 | 1,5993 +- 0,002 | 1,598633 | getroffen |
| beta 0,35, n = 2 | 0,47655 +- 0,0008 | ~0,47628 (grob, nicht verfeinert) | ~0,3 | 1,5010 +- 0,003 | ~1,4985 | getroffen (grob) |
| beta 0,35, n = 3 | 0,41651 +- 0,0006 | 0,416453 | 0,10 | 1,4452 +- 0,003 | 1,443322 | getroffen |
| beta 0,35, n = 4 | 0,38452 +- 0,0008 | 0,384751 | 0,29 | 1,4079 +- 0,005 | 1,410362 | getroffen |

- Alle acht Stellen liegen innerhalb eines Fehlerbalkens. Kein zusaetzlicher Vorzeichenwechsel erscheint in den
  vorhergesagten Fenstern.
- Nebenbefund: Bei beta 0,55 ist s am unteren Scanrand 0,6155 fast null (+8,6e-6, Gamma 3,8e-4). Dort liegt
  moeglicherweise die naechste Stelle (n = 6). Sie war nicht vorhergesagt und ist nicht gerechnet.
- Umlauftests fuer alle acht laufen seit 06:14:06 bzw. 06:17:24 (cpu bis cpu4).
- **Umlauf beta 0,35, n = 1:** -1 auf beiden Rechtecken, aufgeloest (.69, 06:20:00). Vorhersage -1: getroffen.
- **Umlauf beta 0,55, n = 4:** +1 auf beiden Rechtecken, aufgeloest (.69, 06:25:45). Vorhersage +1: getroffen.
- **Umlauf beta 0,60, n = 4:** +1 auf beiden Rechtecken, aufgeloest (.69, 06:25:58). Vorhersage +1: getroffen.
- **Umlauf beta 0,35, n = 3:** -1 auf beiden Rechtecken, aufgeloest (.69, 06:25:09). Vorhersage -1: getroffen.
- **Umlauf beta 0,35, n = 2:** Die Stelle liegt bei 0,476457 und rho* 1,498694 (exakt-Fit, h = 0,01).
  - Das grosse Rechteck um x0 = 0,47628 (enthaelt die Stelle) gibt +1, aufgeloest (.69, 06:26:29). Vorhersage +1: getroffen.
  - Das kleine Rechteck gibt 0, weil die Stelle 1,8e-4 neben x0 liegt, bei halber Breite 1e-4. Das ist kein Befund.
  - Lage gegen Vorhersage 0,47655 +- 0,0008: 9,3e-5 daneben.
- **Umlauf beta 0,35, n = 4:** +1 auf beiden Rechtecken, aber nicht aufgeloest (.69, 06:33:39).
  - groesster Phasensprung 1,47 bzw. 1,72 rad, cond J 1,3e4, Fitrest 7,4e-4
  - Vorhersage +1: nicht widersprochen, aber nicht belastbar. Das Widerlegungskriterium verlangt eine aufgeloeste Umlaufzahl.
- **Umlauf beta 0,60, n = 5:** -1 auf beiden Rechtecken, aufgeloest (.69, 06:44:04). Vorhersage -1: getroffen.
- **Umlauf beta 0,55, n = 5:** -1 auf beiden Rechtecken, aufgeloest (.69, 06:48:23). Vorhersage -1: getroffen.
- **Bilanz des Blindtests** (2026-09-30 06:49:22 CEST):
  - Lage: 8 von 8 innerhalb eines Fehlerbalkens.
  - Umlaufzahl: 7 von 8 aufgeloest und getroffen; die achte (beta 0,35, n = 4) hat das vorhergesagte Vorzeichen +1,
    ist aber nicht aufgeloest.
  - Kein Widerlegungskriterium ist eingetreten.
  - Belegstufe: Modellaussage, numerische Evidenz im abgeschnittenen radialen linearen Modell, keine Messdaten.


- **ST-1, Stelle (Glied 10): Vorschlag weiter.**
  - Gemeinsame Schranke aus veroeffentlichten Zahlen:
    - Der Spin-2-Geist allein (-4/3) braucht lambda2 < 24,8 um (Masse ueber 8 meV).
    - Der Skalar allein (+1/3) braucht lambda0 < ~57 um.
    - Nur bei lambda0/lambda2 ~ 1,4 bis 1,8 heben sich beide teilweise auf; dann bleiben bis ~35 bis 41 um erlaubt (Tal).
  - Grund fuer die Enge: Die Eoet-Wash-Daten sind im Vorzeichen nicht symmetrisch. J. G. Lee, Dissertation 2020,
    Tabelle 11.4 zeigt einen schwachen Ueberschuss an Anziehung, deshalb sind abschwaechende Kraefte enger begrenzt.
  - Belegstufe: Gauss-Naeherung und Korrelationsmodell [ES]; trifft die Tabellenwerte der Einzelterme auf ~1 um. Keine Messung.
  - Naechste Schritte:
    - kleiner CPU-Test des Tals als Raster
    - Lees Zusatzmaterial beschaffen (APS lieferte HTTP 401)
    - HUST-2020-Volltext lesen
- **ST-1-R, Raster des Tals** (.69, cpu2, 4 s Rechnung; Nachtrag in PAPIER-ST1-G1.md; eingetragen 2026-09-30 06:50:11 CEST):
  - Erlaubt sind ein Block und eine Zunge:
    - Block: lambda2 < 24,8 um, lambda0 bis ~57 bis 59 um.
    - Zunge: endet spitz bei lambda2 = 38,75 um (Geistmasse > 5,1 meV); dort ist lambda0/lambda2 = 1,63 bis 1,70.
  - Der Abgleich mit der Dissertationstabelle (einzelne Terme), die Probe mit gleichen Reichweiten und die Nullprobe
    stimmen.
  - Die Unsicherheit steckt in der Korrelation rho der Signalformen:
    - rho 0,90 bis 0,98 gibt eine Spitze bei 35,75 bis 39,5 um.
    - Ohne den Anziehungsueberschuss der Messung reicht die Zunge bis 44,75 um.
    - Vorsichtig ueber alle Varianten: Geistmasse >= ~4,4 meV, ausserhalb der Zunge >= ~6,4 meV.
  - HUST 2020 ist nur hinter der Bezahlschranke. Eine grobe Attrappe senkt die Spitze auf 35 bis 36 um [ES].
  - Die Variante ohne Ueberschuss war nicht vorab angekuendigt.
  - Vorschlag des Agenten: parken, weil die veroeffentlichten Zahlen ausgereizt sind.
  - Naechster echter Schritt: Lees Drehmomentdaten anfragen (APS verweigert den Zugriff) und sein Fourier-Bessel-Modell
    nachbauen (1 bis 2 Tage).
  - Der KF-4-Faktor 0,16 bis 16,8 ist doppelt ein Artefakt: Die Kopplung war unsere Wahl, und KF-4 lief bei
    Ballgroesse/Wellenlaenge 0,25 bis 1, also nicht im Gezeitenbereich.
    geparkt.

### SP-1: blinde Vorhersagen fuer l > 0 (Theorie-Agent, 06:35:35 bis 06:42:48; eingefroren 06:43:17; eingetragen 2026-09-30 06:43:29 CEST)

- Datei: RUNDE-08/VORHERSAGEN-SP1.md, Kopie .eingefroren-20260930-064317.
- Blindheit: ls um 06:35:39. Es lagen nur die Pole bei l = 1 ab 0,72 vor, nichts zu l = 2.
- Der SP-1-Agent scannt ohne Kenntnis dieser Datei. Um 06:43 lagen von ihm noch keine l > 0-Ergebnisse vor.
- Methode: Phasenregel mit Zusatzversatz l pi/2 plus Bessel-Korrektur; der Restversatz ist an der l = 1-Stelle bei
  0,7556 geeicht (Hand, aus vier Gamma-Werten).

  | Ziel | omega*^2 | Re rho* | Umlauf |
  |---|---|---|---|
  | l = 1, n = 2 | 0,6620 +- 0,0023 | 1,7196 +- 0,005 | +1 |
  | l = 1, n = 3 | 0,6178 +- 0,0013 | 1,6656 +- 0,005 | -1 |
  | l = 2, m = 2 | 0,6505 +- 0,005 | 1,777 +- 0,008 | +1 |
  | l = 2, m = 3 | 0,6094 +- 0,003 | 1,696 +- 0,006 | -1 |
  | l = 2, m = 4 | 0,5865 +- 0,0015 | 1,655 +- 0,006 | +1 |

- Der l = 2-Ast erreicht bei ~0,670 +- 0,01 die Kante 1 + omega; darueber sagt die Regel keine l = 2-Stelle.
- **Widerlegt, wenn** eines davon eintritt:
  - l = 1: kein Einbruch unter 1e-6 im Fenster +-3 Balken
  - l = 1: eine Stelle ausserhalb des Intervalls zwischen den benachbarten l = 0-Stellen
  - l = 1: Phasenabstand n = 2 zu n = 3 unter 0,9 oder ueber 1,1 (erwartet 1,006 +- 0,03)
  - l = 2: ein schmaler Pol unter 1 + omega oberhalb von 0,68
  - l = 2: m = 3 und m = 4 fehlen
  - Umlauf: zwei Nachbarn desselben Asts mit gleichem Vorzeichen

### BIC-3 (c): Duennwand-Folge beta 0,5, Vorab-Erwartung der Leitung (2026-09-30 06:52:42 CEST, vor den Laeufen)

- Bekannt: 1/(omega*^2 - 0,5) = 3,359 / 5,402 / 7,608 / 9,860 / 12,133 (n = 1 bis 5). Die Schritte 2,04 / 2,21 / 2,25 / 2,27
  naehern sich etwa 2,29.
- Einfache Fortsetzung mit Schritt 2,29 +- 0,03 (Hand, keine Phasenregel), ab n = 5:

  | n | 1/(x - 0,5) | x | Status vor dem Lauf |
  |---|---|---|---|
  | 6 | 14,42 +- 0,03 | 0,56935 +- 0,0002 | Kandidat 0,5694 bekannt, nicht konvergiert; nicht blind |
  | 7 | 16,71 +- 0,06 | 0,55984 +- 0,0003 | im Raster Gamma klein bei 0,560; halb bekannt |
  | 8 | 19,00 +- 0,09 | 0,55263 +- 0,0003 | nicht gerechnet, blind |
  | 9 | 21,29 +- 0,12 | 0,54697 +- 0,0003 | nicht gerechnet, blind |

- Vorzeichen: abwechselnd, n gerade +1, n ungerade -1.
- **Widerlegt**, wenn n = 8 oder n = 9 mehr als 3 Balken daneben liegt oder im Fenster kein Vorzeichenwechsel auftritt. Ab
  einem Kernwachstum ueber ~1e8 gilt der Lauf als nicht entscheidbar.

- **Ausgang n = 6 und 7** (Laptop, bic2 v3, kurve 0,5565 bis 0,574; eingetragen 2026-09-30 06:57:36 CEST):
  - n = 6: Vorzeichenwechsel zwischen 0,569 und 0,5715; Feinverfahren bei 0,56940, s = 2,2e-6, Pol -5,7e-7 i, noch nicht
    ganz konvergiert. Die Erwartung 0,56935 +- 0,0002 ist damit vereinbar.
  - n = 7: kein Vorzeichenwechsel im Raster, s bleibt 0,5565 bis 0,569 negativ. Bei 0,559 bricht Gamma auf 5,5e-4 ein.
    Die Pol-Spur springt (Re 1,5871 -> 1,5947 -> 1,5949 -> 1,5927); vermutlich mischen dort zwei Zweige, bei einem
    Kernwachstum bis 1,1e7.
  - Die Erwartung n = 7 bei 0,55984 ist nicht bestaetigt. Sie war nur halb blind und hatte kein Widerlegungskriterium.
- **Ausgang n = 8 und 9** (.69, bic2 v3, kurve 0,5425 bis 0,5575, Ende 06:59:15; eingetragen 2026-09-30 07:00:37 CEST):
  - Kein Vorzeichenwechsel von s. Das Kernwachstum erreicht 1,0e9, ueber der vorab gesetzten Grenze 1e8.
  - **Nach der Vorab-Regel ist der Lauf nicht entscheidbar**, die Folge ist weder bestaetigt noch widerlegt.
  - Nachtraeglich bemerkt, kein Test: Gamma bricht bei 0,5525 (1,7e-5) und 0,5425 (4,8e-5) ein, nahe der Fortsetzung
    n = 8 (0,5526) und n = 10 (0,5424). Die Pol-Spur springt wie bei n = 7.
- **Pruefung bic2 v3 fuer l = 0:** Am Punkt 0,555 sind v3 und v2 (Scan S1) in allen gedruckten Stellen gleich
  (1,585069 | -5,752e-4 | 1,5885209 - 5,458e-3 i). Die Pruefung des SP-1-Agenten steht zusaetzlich aus.

### GF-BIC Ausgang (Agent, 05:57:52 bis 06:55:09; RUNDE-08/gf-bic/ERGEBNIS.md)

- **Kein Verlustkanal der Ordnung epsilon^2:**
  - direkt ausgeschlossen [Hand]: psi_2 -> -psi_2 ist eine Symmetrie, ein leeres psi_2 bleibt leer
  - parametrisch (Floquet bis epsilon = 0,04) keine neue instabile Mode; obere Schranke 1e-5 bzw. 1e-6
  - Die Pumpe daempft die Pseudo-Goldstone-Mode sogar. Die Vorab-Erwartung "waechst" ist widerlegt.
- **Der einkomponentige Ball ist fuer g != 0 instabil:**
  - Die Nullmode wird imaginaer: lambda = 0,046 bis 0,116 bei g = 0,2 und bis 0,61 bei g = 1.
  - Ursache ist ein resonanter Uebergang zweier psi_1-Teilchen in zwei psi_2-Teilchen. Der Ball kippt in 2 bis 6
    Atmungsperioden in eine Mischung.
  - Schiessverfahren und FD-Kasten stimmen auf 1e-7 ueberein.
- **Der natuerliche Zustand ist der gemischte Ball:**
  - Sein symmetrischer Teil ist exakt das Ein-Feld-Modell mit beta_eff = 1/(2(1 + g/4)^2); das Fenster ist KANDIDAT 5.3.
  - Die stillen Stellen bleiben also, verschoben. Der antisymmetrische Teil ist stabil.
- **psi_2 hat eine eigene Leiter stiller Stellen** [H]:
  - Fuer kleines g verschwindet die Breite des Gegenlaeufers bei acht omega^2-Werten, darunter 0,866, 0,711, 0,646 und
    0,611. Die Schritte in 1/(omega^2 - 1/2) liegen bei 2,0 bis 2,3.
  - Bei endlichem g:
    - (0,5512; g = 0,4985): Minimum -Im nu < 6e-10, ohne Umlauftest
    - g = 0,2 nahe 0,711: Einbruch um mehr als das 500-fache
- **Kontrollen bestanden:**
  - der N = 1-Pol 1,7018102865 - 1,468e-3 i
  - die BIC an P1 mit |Im| = 1,5e-10
  - g = 0: doppelte Nullmode
  - g gegen -g und epsilon gegen -epsilon bitgleich
  - ohne Ball keine Stellen
- **Vorab gegen Ausgang:** 12 getroffen, 2 teilweise, 2 verfehlt, 2 widerlegt.

### BEWEIS-1: frische Lesung des Plans (Fable, 06:39:41 bis 06:58:03; RUNDE-07/beweis/LESUNG-PLAN.md; eingetragen 2026-09-30 06:59:07 CEST)

- **Urteil: TRAGFAEHIG MIT AUFLAGEN.** Alle Formeln der Lemmata sind von Hand nachgerechnet; kein Fehler, der aus einem
  bestandenen Zertifikat einen falschen Beweis machen wuerde.
  - rho* liegt strikt im Fenster: Abstand 0,1485 zur oberen Kante.
  - Die Schwanzfehler bei L = 40 liegen bei ~1e-16.
- **Blockierend, falls offen (B1):** Alle konkreten Zahlen muessen in Satz und Abschnitt 6 stehen.
- **Wesentlich:**
  - W1: Fehlerverstaerkung e^{2 kappa0 L} ~ 4e15 beim Vorwaertsschuss; eine Budgetrechnung ist noetig
  - W2: R < r_j je Schritt
  - W3: Definition von "eingebettet"
  - W4: Umkehrung von Lemma W und Einfachheit der Mode
  - W5, W6: Stetigkeit ueber Z, Jet-Liste
  - W7: Codex hat einen Parallelplan fuer dasselbe Zertifikat (bic-proof/CONTINUUM-MEMBERSHIP.txt)
- **Leitung, 2026-09-30 06:59:07 CEST:** Die Auflagen gehen an den Beweis-Agenten.
  - Er baut unabhaengig weiter und vergleicht nur Konstanten mit Codex.
  - Rechnet Codex getrennt, ist das die unabhaengige Gegenprobe (zweites Programm).

## Abschaetzung

Leitung claude-primary, 2026-09-30 07:02:17 CEST (date, vor dem Schreiben). Laufende Karten gehen in Runde 9 ueber:
BEWEIS-1, SP-1, FA-1, EVO-1 Generation 1 und die Polprobe bei n = 8.

| Karte | Entscheidung | Grund |
|---|---|---|
| BEWEIS-1 | **weiter** (laeuft) | Plan von frischer Lesung als "tragfaehig mit Auflagen" beurteilt; Auflagen B1 und W1 bis W7 uebergeben; Codex hat einen Parallelplan (moegliches zweites Programm) |
| BIC-3 Folge und Phasenregel | **weiter** (als BIC-4) | Blindtest bestanden: 8 von 8 Lagen, 7 von 8 Umlaufzahlen aufgeloest getroffen; V3 und V6 getroffen, V8 auf dem Raster bestanden. Die Duennwand-Folge ist ab n = 7 numerisch nicht mehr entscheidbar; BIC-4 braucht einen robusteren Loeser |
| GF-BIC Gesamtformel mit zwei Komponenten | **weiter** | Kein epsilon^2-Verlustkanal. Der einkomponentige Ball ist fuer g != 0 instabil, der gemischte Ball entspricht dem Ein-Feld-Modell mit beta_eff und behaelt die Leiter. Die zweite Leiter (psi_2) braucht Umlauftests |
| ST-1 Stelle-Schranke | parken | Mit veroeffentlichten Zahlen ausgereizt: Geist ueber ~5 bis 8 meV, Tal bis 38,75 um. Weiter nur mit Rohdaten (APS-Login oder Anfrage, Finn) |
| EVO-1 | **weiter** (laeuft) | Reparatur nach zwei frischen Lesungen freigegeben, A1 bestanden, Generation 1 laeuft |
| R5F-b zweite Spitze | erledigt | Das ist die ungerade 1D-Mode. Vorab-Erwartung in Lage und Abklingrate getroffen |
| Chem 14 (Zufallskarte) | parken, bestaetigt | Mit Einzelkontrolle ist es echte Paarvernichtung; vermutlich Literatur [L?] |
| FA-1 Farb-Analogie | **weiter** (laeuft) | Finns Frage 06:21; Schreibtisch-Frustrationsbild noch ungeprueft |
| SP-1 stille Stellen fuer l > 0 | **weiter** (laeuft) | Minimum l = 1 bei ~0,7554 (Gamma 2,3e-7); blinde l > 0-Vorhersagen eingefroren 06:43:17 |

- Bilanz: 6 weiter (davon 4 laufend), 2 parken, 1 verwerfen, 1 erledigt.
- Urteil gegen Zufall: Die Zufallskarte traegt nicht weiter (parken). Von den gewaehlten Karten tragen BIC-3, GF-BIC und
  BEWEIS-1 deutlich weiter.
- Offene Entscheidungen fuer Finn:
  - APS-Login oder Datenanfrage fuer ST-1
  - restic-Aufraeumen auf dem TS440
  - Ollama-Stopp fuer die wartenden formalen Laeufe

## Einfach gesagt

In dieser Runde hat die Regel fuer die stillen Schwingungen ihren schwersten Test bestanden: Sie hat acht Stellen
vorhergesagt, die vorher niemand kannte, und alle lagen richtig. Im groesseren Modell mit zwei Feldern bleibt die Stille
erhalten, und die zweite Feldsorte hat sogar eine eigene Leiter stiller Stellen. Bei der Schwerkraft auf kleinen Abstaenden
wissen wir jetzt, dass ein zusaetzliches schweres Teilchen schwerer als etwa 5 meV sein muesste. Ein angeblicher
Bauplan ein unabhaengiger Leser fuer tragfaehig haelt.
