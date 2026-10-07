# PHASE-3D-BLIND: Ergebnis (Code-Agent, Runde 31, Messseite des Blindtests)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 11:27:13 CEST (date).
- **Rauchlauf 1** (Code Version 1, bekannte Sprossen, ausserhalb der echten Fenster): .69, 09:38:53 bis 09:48:58 UTC,
  vier Aufrufe, alle rc = 0.
- **Rauchlauf 2** (Code Version 2, PB0-Kontrolle, bekannte Sprossen): .69, 09:47:09 bis 10:13:17 UTC, sechs Aufrufe,
  alle rc = 0.
- **Plan eingefroren** 11:51:17 CEST (PLAN.md.eingefroren-20261003-115117), vor jeder echten Rechnung. PLAN.md, Code und
  Skripte sind seither unveraendert (sha256 unten).
- **Echte Laeufe** (code/start.sh, einmal per nohup): .69, 09:51:18 bis 10:16:29 UTC, 22 Aufrufe, alle rc = 0.
- Auswertung lokal mit jq um 12:16:48 CEST: lauf-69/auswertung.json (code/auswertung.jq), lauf-69/sprossen.json
  (code/sprossen.jq), Tabellen per code/bericht.jq. Geschrieben ab 12:17 CEST (date); Ende in der letzten Zeile.
- Markierungen: [A] Festlegung des Code-Agenten (im Plan vor den echten Laeufen), [H] Deutung/Hypothese, [N] nach dem
  Einfrieren hinzugefuegt (nur Bericht, keine Wertung). Alles gilt im linearen, radialen Zweikanalmodell (l = 0,
  abgeschnittener Rand): numerische Evidenz im Modell, keine Messung im Labor.
- **Blindheit:** Codex' versiegelte Datei, BASELINE-VERSIEGELT.json, coordination/resonance-20260930/ und (vorsorglich)
  PROTOKOLL-VORSCHLAG-AN-CODEX.txt habe ich nicht gelesen. Keine Deutung gegen eine Vorhersage; den Vergleich macht die
  Leitung.

## Messergebnis zuerst

1. **In jedem der sechs Fenster liegt genau eine Sprosse.** Lage auf h = 0,02. Unsicherheit [N]: das groessere von
   Plan-Unsicherheit (Gitterdifferenz plus Endklammer) und Rauschmass.

   | Sprosse | omega^2 | 1/eps | Umlauf (Kreuzung) |
   |---|---|---|---|
   | beta = 1/2, n = 16 | 0,52671542 +- 2e-7 | 37,4316 +- 3e-4 | +1 |
   | beta = 1/2, n = 17 | 0,52516277 +- 1,3e-6 | 39,741 +- 2e-3 | -1 |
   | beta = 1/2, n = 18 | 0,5237875 +- 4e-6 | 42,039 +- 7e-3 | +1 |
   | beta = 1, k = 0 | 0,778585440 +- 2e-8 | 34,98284 +- 3e-5 | -1 |
   | beta = 1, k = -1 | 0,776606628 +- 2e-8 | 37,58462 +- 3e-5 | +1 |
   | beta = 1, k = -2 | 0,774882776 +- 2e-8 | 40,18844 +- 3e-5 | -1 |

   - Jede Sprosse: Vorzeichenwechsel von s im Fenster, echte Nullstellensuche in omega^2 auf zwei Gittern, Rechteck um
     die Wurzel mit Umlauf +-1. Die Umlaeufe wechseln ab, auch gegen die bekannten Sprossen (n = 15: -1; k = 1: +1).
   - In allen 30 Startzeilen hat L(y_b) im ganzen rho-Fenster genau eine Nullstelle.
2. **Genauigkeit:**
   - beta = 1: Die Gitter h = 0,04 und 0,02 stimmen auf 1,8e-8 bis 2,1e-8 ueberein (wie RUNDE-24). Das Rundungsrauschen
     ist vernachlaessigbar.
   - beta = 1/2: Das Rundungsrauschen begrenzt die Lage. Das Kernwachstum betraegt 1e12 bis 3e13, s ist an der Sprosse
     nur auf ~1e-11 bestimmt. Die Gitter liegen 9e-8 (n = 16), 6e-7 (n = 17) und 8e-7 (n = 18) auseinander, innerhalb
     des Rauschmasses (2e-7, 1,3e-6, 4e-6).
3. **PB0 eingetroffen:** n = 15 bei 0,52846934 (Delta +3,4e-7), k = 1 bei 0,78087985 (Delta +8,5e-7), beide unter 1e-6.
4. **PB1 nach der Plan-Regel nicht eingetroffen**, allein wegen Bedingung (b) bei beta = 1/2:
   - Die h = 0,02-Laeufe stiessen dort an die Zeitreserve. Die Endklammern sind 1,09e-9 (n = 16), 1,16e-9 (n = 17) und
     1,7e-7 (n = 18) statt <= 1e-9.
   - Alle uebrigen Teile von PB1 gelten: in jedem Fenster genau ein Wechsel, Lagen beider Gitter auf 1e-6 gleich,
     Umlauf +-1 in jedem Fenster, wechselnd fuer beide beta.
   - Im Rauschbereich (Abschnitt Kontrollen) bringen weitere Illinois-Schritte keine Genauigkeit mehr; das aendert die
     Wertung nicht.
5. **Randprobe** (Aussenrand + 20): k = -2 verschiebt sich um 1,4e-12, n = 18 um 5,9e-7. Das ist innerhalb des
   Rauschmasses von n = 18 (4e-6).

## Vorab gegen Ausgang (mechanisch nach PLAN.md Abschnitt 6; auswertung.jq)

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang |
|---|---|---|---|
| PB0 | Kontrolle: Der Code findet die bekannte Sprosse n = 15 (beta = 1/2) und eps = 0,030879 (beta = 1) mit \|Delta omega^2\| < 1e-6 wieder | 85 % | **eingetroffen**: h = 0,02 0,5284693357 (+3,36e-7 gegen 0,528469) und 0,7808798529 (+8,53e-7 gegen 0,780879), Endklammern 2,2e-10 und 7,3e-11 |
| PB1 | In jedem der sechs Fenster gibt es genau eine Sprosse, mit wechselnder Umlaufzahl | 80 % | **nicht eingetroffen** nach Plan-Regel: (b) verfehlt bei n = 16, 17, 18 (Endklammer h = 0,02 > 1e-9, Zeitreserve); (a), (c), (d) erfuellt |

- PB0 berichtet, nicht entscheidend: h = 0,04 0,5284692532 (+2,53e-7) und 0,7808798305 (+8,31e-7). Gegen den genaueren
  R24-Wert 0,7808792886 liegt k = 1 um +5,6e-7 hoeher. R24 hatte zwischen Zeilen im Abstand 3e-4 linear interpoliert und
  die Kruemmungskorrektur auf +1,9e-7 bis +3,7e-7 geschaetzt.

| Fenster | (a) ein Wechsel, Ast konsistent | (b) Wurzel beide Stufen (Endklammer <= 1e-9), Lagen auf 1e-6 | (c) u004 Wechsel und Umlauf +-1 |
|---|---|---|---|
| b05-n16 | ja | nein (Endklammer h = 0,02 1,09e-9; Lagen 9,4e-8 auseinander) | ja |
| b05-n17 | ja | nein (1,16e-9; Lagen 6,1e-7) | ja |
| b05-n18 | ja | nein (1,7e-7; Lagen 8,0e-7) | ja |
| b1-k0 | ja | ja | ja |
| b1-km1 | ja | ja | ja |
| b1-km2 | ja | ja | ja |

- (d) Umlaeufe (bekannte Sprosse, Fenster 1, 2, 3): beta = 1/2: -1, +1, -1, +1; beta = 1: +1, -1, +1, -1. Beide
  wechselnd.
- Lesart [A, im Plan]: "Wurzel mit Endklammer <= 1e-9" gilt auf beiden Stufen. Ohne diese Teilbedingung (nur "Lagen auf
  1e-6 gleich") waere PB1 eingetroffen. Das ist die einzige Stelle, an der das Urteil haengt.

## Neue Sprossen (Lage aus h = 0,02)

R_halb in der Konvention von RUNDE-26 (S(R) = S_c/2, S_c = 1/(2 beta)); rho = Nullstelle von L(y_b) an der Sprosse.
Rauschmass = 1e-15 * groesster Einzelterm von L(y_a) / Steigung von s in der weiten h004-Startklammer [N].

| Sprosse | omega^2 (h = 0,02) | eps | 1/eps | Umlauf Kreuzung / Phase (Sprung, Runden, aufgeloest) | R_halb | rho | Unsicherheit omega^2 / 1/eps (Plan) | Rauschmass omega^2 / 1/eps | h002 - h004 | Randprobe - h004 | Kernwachstum |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b05-n16 | 0,5267154164 | 0,026715416 | 37,43157 | +1 / 1 (0,298 rad, 37, ja) | 26,79284 | 1,55532975 | 9,5e-8 / 1,3e-4 | 1,9e-7 / 2,7e-4 | 9,4e-8 | - | 9,7e11 |
| b05-n17 | 0,5251627699 | 0,02516277 | 39,74125 | -1 / -1 (0,275 rad, 39, ja) | 28,4277 | 1,55360468 | 6,1e-7 / 9,6e-4 | 1,3e-6 / 2,1e-3 | -6,1e-7 | - | 5,2e12 |
| b05-n18 | 0,5237874659 | 0,023787466 | 42,03895 | +1 / 1 (0,585 rad, 50, nein) | 30,05388 | 1,55206822 | 9,7e-7 / 1,7e-3 | 4,2e-6 / 7,4e-3 | -8e-7 | 5,9e-7 | 2,8e13 |
| b1-k0 | 0,7785854399 | 0,02858544 | 34,98284 | -1 / -1 (0,291 rad, 19, ja) | 17,90493 | 1,80077636 | 2,1e-8 / 2,6e-5 | 4,2e-13 / 5,2e-10 | 2,1e-8 | - | 2,9e5 |
| b1-km1 | 0,7766066277 | 0,026606628 | 37,58462 | +1 / 1 (0,281 rad, 20, ja) | 19,21173 | 1,79904197 | 1,9e-8 / 2,7e-5 | 8,4e-13 / 1,2e-9 | 1,9e-8 | - | 7,1e5 |
| b1-km2 | 0,7748827758 | 0,024882776 | 40,18844 | -1 / -1 (0,299 rad, 22, ja) | 20,51879 | 1,79751388 | 1,8e-8 / 2,9e-5 | 1,9e-12 / 3e-9 | 1,8e-8 | 1,4e-12 | 1,8e6 |

| Sprosse | omega^2 h = 0,04 | 1/eps h = 0,04 | Endklammer h = 0,04 / 0,02 (Schritte) | R aussen h = 0,04 / 0,02 / Randprobe | R_halb_S0 (S(R) = S(0)/2) |
|---|---|---|---|---|---|
| b05-n16 | 0,5267153222 | 37,4317 | 3e-10 / 1,1e-9 (8 / 9) | 53,68 / 46,2 / - | 26,75818 |
| b05-n17 | 0,5251633775 | 39,74029 | 1,5e-10 / 1,2e-9 (5 / 8) | 55,36 / 47,84 / - | 28,3949 |
| b05-n18 | 0,5237882695 | 42,03753 | 2,5e-11 / 1,7e-7 (9 / 7) | 56,96 / 49,44 / 76,16 | 30,02275 |
| b1-k0 | 0,7785854193 | 34,98287 | 3,9e-10 / 1e-10 (3 / 3) | 55,84 / 45,48 / - | 17,80837 |
| b1-km1 | 0,7766066086 | 37,58465 | 6,2e-13 / 1,4e-10 (5 / 3) | 57,12 / 46,72 / - | 19,12095 |
| b1-km2 | 0,7748827581 | 40,18847 | 5,9e-13 / 1,8e-10 (5 / 3) | 58,32 / 48 / 77,76 | 20,43314 |

- **Umlauf:** Kreuzungszaehlung und Phase geben ueberall dasselbe Vorzeichen. Die Phase ist in fuenf Fenstern
  aufgeloest (groesster Sprung 0,275 bis 0,299 rad); bei n = 18 nach 50 Runden nicht (0,585 rad, Abschnitt Kontrollen).
- **Rechteckzeilen** x* +- d: d = 6,6e-4 / 5,8e-4 / 5,2e-4 (n = 16, 17, 18) und 8,5e-4 / 7,4e-4 / 6,4e-4 (k = 0, -1, -2),
  rho* +- 0,01. s wechselt zwischen den beiden Zeilen in allen sechs u004-Laeufen das Vorzeichen.
- **Bekannte Sprossen** (pb0-*-u004, gleiche Bauart): n = 15 Umlauf -1 (aufgeloest, 0,299 rad), k = 1 Umlauf +1
  (aufgeloest, 0,292 rad). h = 0,02: R_halb 25,16034 und 16,59845, rho 1,55726643 und 1,80276150.
- **Leiternummer bei beta = 1** nur als Fortsetzung der R24-Zaehlung (k = 0, -1, -2); mit R24s vorlaeufiger Zuordnung
  k = 1 ~ n = 12 waeren es n = 13, 14, 15 [H, nicht geprueft]. Die Umlaeufe -1, +1, -1 passen dann zur Regel "n gerade
  +1, n ungerade -1"; ebenso bei beta = 1/2 (n = 16 +1, 17 -1, 18 +1).

## Verfahren in Kuerze (PLAN.md Abschnitte 3 bis 6)

- **Fenster** [A]: u = 1/eps, Schritt b = zuletzt gemessener Schritt (2,306760 bei beta = 1/2, 2,596420 bei beta = 1),
  Fenster k = 1, 2, 3: [u_bekannt + (k - 1/2) b, u_bekannt + (k + 1/2) b], lueckenlos. u_bekannt: n = 15 bei
  eps = 0,028469 (beta = 1/2), k = 1 bei eps = 0,0308792886 (beta = 1, genauer R24-Wert).
- **Code** code/bic2_3d_suche_v2.py: Kopie von RUNDE-13/leiter3d-praez/bic2_3d_praez.py, Physik unveraendert, neues
  Kommando suche. Je Zeile Profil, rho-Abtastung, Nullstelle von L(y_b), s = L(y_a) dort; s per Zweipunkt-Interpolation
  (Version 2, Grund unten). Vorzeichenwechsel von s zwischen den 5 Startzeilen je Fenster (Abstand b/4), dann echte
  Nullstellensuche in omega^2 (Illinois, neues Profil je Schritt) bis zur Klammer 1e-9.
- **Laeufe je Sprosse:** h004 (h = 0,04, Fenster), h002 (h = 0,02, enge Klammer x* +- 1e-5 um die h004-Wurzel), u004
  (h = 0,04, Umlauf-Rechteck auf den Zeilen x* +- d, d = 0,4 erwarteter Sprossenabstand), dazu Randprobe (Aussenrand
  R + 20) bei den zwei groessten Baellen (b05-n18, b1-km2).
- **Umlauf** [A]: massgeblich die Kreuzungszaehlung von praez_rechteck; die Phasenaufloesung wird berichtet.
- **Unsicherheit** [A]: |omega*^2(h002) - omega*^2(h004)| + groessere Endklammer; daneben Randprobe und Rauschmass.

## Kontrollen

- **Ein Ast je Zeile:** In allen 30 Startzeilen der sechs Fenster hat L(y_b) im ganzen rho-Fenster (1000 + 801 Punkte)
  genau eine Nullstelle; der Zielast ist in jedem Fenster konsistent (gleiche Richtung, |Delta rho| <= 0,03).
- **Doppelt gerechnete Randzeilen** (benachbarte Fenster teilen ihre Randzeile; anderes R und r_m):
  - beta = 1: s stimmt auf relativ 3,5e-10 (u = 36,2788) und 2,7e-9 (u = 38,8752) ueberein.
  - beta = 1/2: auf relativ 7,6e-4 (u = 38,5861; absolut 9,8e-12) und 1,7e-4 (u = 40,8928; absolut 8,7e-13). Das ist
    die Groesse des Rundungsrauschens von s (unten).
- **R und rho gegen RUNDE-26** (Startzeilen der PB0-Rauchlaeufe liegen genau auf den bekannten Lagen):
  - beta = 1/2 bei omega^2 = 0,528469: R = 25,1606316 gegen RUNDE-26 25,1606319 (-2,6e-7).
  - beta = 1 bei 0,7808792884: R = 16,5987472 gegen 16,5987471 (+1,3e-7); rho = 1,80276101 gegen 1,80276100 (+1,2e-8).
- **Rundungsrauschen von s bei beta = 1/2** [N, Bericht]:
  - Das Kernwachstum am Ast betraegt 2e11 (n = 15) bis 3e13 (n = 18); bei beta = 1 nur 1e5 bis 2e6.
  - Der groesste Einzelterm von L(y_a) erreicht bei beta = 1/2 bis 7e4, bei beta = 1 hoechstens 7. Damit ist s an der
    Sprosse bei beta = 1/2 nur auf ~1e-11 bestimmt.
  - In den letzten Illinois-Schritten springt s bei beta = 1/2 um +-1e-11 ohne Trend. Beispiel n = 16, h = 0,02: neun
    Schritte innerhalb von 2e-8 in omega^2, s zwischen -9e-12 und +1e-11.
  - Das Rauschmass (Tabelle) ist bei beta = 1/2 so gross wie oder groesser als die Unsicherheit nach Plan; bei beta = 1
    vernachlaessigbar.
  - Ohne die Zweipunkt-Interpolation (s_roh) waere s bei beta = 1/2 unbrauchbar. In Startzeilen mit vielen
    Illinois-Schritten lag s_roh bei 1e-6 bis 1e-5 statt 1e-9 bis 3e-8 (n = 18, Zeile 0,52346: s_roh 1,2e-5, s -1,8e-9).
    Bei beta = 1 stimmen s und s_roh auf relativ <= 1e-4 ueberein.
- **Phase bei n = 18:** W laeuft auf den rho-Seiten in einem Abstand ~|s|/|dL(y_b)/drho| ~ 1e-15 an 0 vorbei, das sind
  wenige Rechenstellen von rho. Nach 50 Halbierungsrunden blieb ein Sprung von 0,585 rad; die Phasensumme gibt trotzdem
  +1,0000, die Kreuzungszaehlung +1.
- **Zeitgrenze:** Die h002-Laeufe bei beta = 1/2 brachen die Illinois-Suche an der Zeitreserve ab (Budget 560 s; 471 bis
  486 s Rechenzeit): n = 16 und 17 mit Endklammer 1,09e-9 und 1,16e-9, n = 18 mit 1,7e-7 nach 7 Schritten.
- **Randprobe:** Aussenrand 76,16 statt 56,96 (n = 18) und 77,76 statt 58,32 (k = -2), h = 0,04, enge Klammer um die
  h004-Wurzel. Verschiebung +5,9e-7 (n = 18, im Rauschen) und +1,4e-12 (k = -2).
- **Rauchlauf 1 gegen Rauchlauf 2** (Version 1 gegen 2): k = 1 auf h = 0,04 0,780879830033 gegen 0,780879830520
  (5e-10), auf h = 0,02 0,780879852890 gegen 0,780879852891. Bei n = 15 gab Version 1 0,528468949 (nicht konvergiert,
  s verfaelscht), Version 2 0,5284692532.
- **Laufzeiten** (.69, Rechenzeit laut Programm; alle unter 600 s, Wartezeiten auf Spur-Sperren bis 8,2 min):
  - h004: 216 bis 434 s; h002: 228 bis 243 s (beta = 1), 471 bis 486 s (beta = 1/2, Zeitreserve); u004: 89 bis 193 s;
    Randprobe 190 s (k = -2) und 401 s (n = 18).
  - Rauchlauf 2: h004 256 und 302 s, u004 117 und 167 s, h002 227 und 337 s. Rauchlauf 1: 77 bis 524 s.
  - Einzelzeiten und Spuren in lauf-69/lauf/LAUF-*.log, lauf-69/rauch2/, lauf-69/rauch/.
- **Unveraendert seit dem Einfrieren (sha256):**
  - PLAN.md = PLAN.md.eingefroren-20261003-115117 (lokal = .69): e479d39be295504ca3bbc38a7ad759e3da71544615d81723d6826d9a7a617d08
  - code/bic2_3d_suche_v2.py (lokal = .69): 6beabc3f0d499df31a20c21fc9a35a2dc028117be5df05badf7863c22eb53c71
  - code/bic2_3d_suche_v2.diff (gegen RUNDE-13): 48186dc3c2fbc873cfeb50dab760681d7fc1af0464007710922e07d5eabe436f
  - code/start.sh (lokal = .69): af6a07a54d012c021e99e3581974a51317efc6094c0a1e5e593a6f975be2534e
  - code/rauch2.sh (lokal = .69): f2e09062a5b60ca2c047b56e2b58127357e53ec760f21b1964ceaebc9d4330e8
  - nur Rauchlauf 1: code/bic2_3d_suche_v1.py 3eb8fd8d02c0e526a34520e95f94439fcb0143390de60db07ab0d22c47fb4303,
    code/rauch.sh fff753864bc9f323bf03a75937dd1769b6f9e8bd4276a0bf32138eb0c48dcf65
- **Nach dem Einfrieren [N]:** code/auswertung.jq 8cf8a4e3..., code/bericht.jq cef098d4..., code/sprossen.jq
  4f02b191...; lauf-69/auswertung.json dc254a75..., lauf-69/sprossen.json 4267791b... (volle Werte per sha256sum).

## Latten (v3)

- **L1 (kann scheitern): ja.** PB0 und PB1 standen in der Karte; die Regeln waren vor dem ersten echten Lauf
  eingefroren. PB1 ist an einer Teilbedingung gescheitert.
- **L2 (Gegenprobe): teilweise.** Je Sprosse Vorzeichenwechsel und Rechteck, zwei Gitter, Randprobe, doppelt gerechnete
  Randzeilen. Die Kreuzungszaehlung haengt am Vorzeichenwechsel; die unabhaengigere Phase ist bei n = 18 nicht
  aufgeloest. Es gibt kein zweites Programm (alles bic2).
- **L3 (Numerik): ja bei beta = 1, begrenzt bei beta = 1/2** (Rundungsrauschen 2e-7 bis 4e-6 in omega^2; eine Stufe
  h = 0,01 fehlt).
- **L4 (schon bekannt):** RUNDE-13, RUNDE-24 und RUNDE-26 (Projekt); Literatur nicht gesucht.
- **L5 (Messbezug): nein.** Modellintern: linear, radial, l = 0.

## Grenzen

- Nur zwei Stufen h = 0,04 / 0,02; h = 0,02 startete in der engen Klammer um die h = 0,04-Wurzel.
- Bei beta = 1/2 ist die Lage durch das Rundungsrauschen begrenzt. [H] Ein kleinerer Anschlusspunkt r_m (naeher am
  Kern) oder die Pluecker-Koordinaten der Polsuche koennten das Rauschen senken; das ist nicht geprueft.
- Die Unsicherheit nach Plan (Gitterdifferenz plus Endklammer) unterschaetzt bei beta = 1/2 das Rauschen; die
  Tabelle nennt beide.
- Die Fenster setzen Sprossen im Abstand ~b voraus; ausserhalb der Fenster ist nicht gesucht.

## Selbstanzeigen

1. **Rauchlauf 1 vor dem Einfrieren, mit Folgen fuer Code und Plan.**
   - An den bekannten Sprossen (ausserhalb der echten Fenster, Auftrag der Leitung) zeigte Version 1 bei beta = 1/2,
     n = 15: Rest L(y_b) an der Nullstelle ~5e-8, so gross wie s (1e-8 bis 7e-8). Das unkorrigierte s war dort nicht
     verlaesslich; das Rechteck war nach 30 Runden nicht aufgeloest.
   - Daraufhin, noch vor dem Einfrieren: Version 2 (Zweipunkt-Interpolation von s, Zoom), getrennter Rechtecklauf auf
     x* +- d, und die Kreuzungszaehlung statt der Phase als massgeblicher Umlauf.
   - Gesehen hatte ich dabei die PB0-Lagen von Version 1: 0,780879830 (beta = 1) und ~0,5284689 (beta = 1/2, nicht
     konvergiert). Die PB0-Regel stammt woertlich aus der Karte und ist nicht angepasst.
2. **PB0 aus Rauchlauf 2.** Die Wertung nimmt die h002-Laeufe des zweiten Rauchlaufs (Code Version 2, gleiche sha256 wie
   die echten Laeufe). Beim Einfrieren waren dort die ersten Wurzelschritte von n = 15 auf h = 0,04 sichtbar (0,5284692);
   das steht im Plan.
3. **Massgeblicher Umlauf = Kreuzungszaehlung** [A, vor den echten Laeufen]. Sie ist mit dem Vorzeichenwechsel von s
   nicht unabhaengig: Kreuzt L(y_b) jede rho-Seite genau einmal, ist sie (1/2) Richtung * (sgn s(x*+d) - sgn s(x*-d)).
   Die Phasenaufloesung ist die unabhaengigere Probe; sie stimmt in allen sechs Fenstern ueberein, ist aber bei n = 18
   nicht aufgeloest.
4. **h002 haengt an h004:** Die enge Klammer x* +- 1e-5 kommt aus dem h004-Ergebnis. Die h002-Wurzel ist auf h = 0,02
   selbst gesucht, aber nicht unabhaengig gestartet.
5. **PB1-Lesart:** "Wurzel mit Endklammer <= 1e-9 auf beiden Stufen" habe ich in den Plan geschrieben, bevor ich wusste,
   dass die h = 0,02-Laeufe bei beta = 1/2 an die Zeitreserve stossen. Nach dem Einfrieren nicht geaendert; das Urteil
   haengt nur daran.
6. **b = b_letzt statt b_inf** fuer die Fenster (Auftrag der Leitung; die Karte nennt b_inf als Beispiel).
7. **Gelesen:** der R-Teil von RUNDE-26/phase-3d/code/phase_3d.py (Konvention des Halbhoehenradius), nicht dessen KARTE
   oder ERGEBNIS. Nicht gelesen (vorsorglich): PROTOKOLL-VORSCHLAG-AN-CODEX.txt.
8. **Nach dem Einfrieren geschrieben, nur Darstellung** [N]: code/auswertung.jq, code/bericht.jq, code/sprossen.jq.
   Das Rauschmass rechne ich dort mit der Steigung der weiten h004-Startklammer statt mit der Endklammer (die Endklammer
   liegt bei beta = 1/2 im Rauschen und gaebe ein zu kleines Mass). Die Spalte "groesseres von Plan-Unsicherheit und
   Rauschmass" im Abschnitt Messergebnis ist ebenfalls [N]. Keine dieser Dateien aendert eine Regel.
9. **Lokal:** kein Interpreter (kein python3, perl, awk). Benutzt: jq, ssh, scp, rsync, sha256sum, diff, date sowie cp,
   mv, chmod, mkdir, ls, cat, grep, cut, head, tail, wc, sort, comm und bash-Warteschleifen (Ueberwachung).
   - Zweimal sed, gegen die Liste des Auftrags: einmal nur zum Anzeigen von Zeilen (sed -n), einmal ein
     Ersetzungsversuch in auswertung.jq, der mit Syntaxfehler abbrach, ohne die Datei zu aendern (Sicherung vorher im
     Scratchpad). Danach nur Edit.
10. **Auf der .69:** Rechnungen nur ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6; nicht cpu5, keine GPU);
    Start der Skripte per nohup setsid bash; sonst mkdir, chmod, sha256sum und zur Ueberwachung ls, cat, head, tail,
    grep, jq (auch ls auf /run/user/1000/systemd/transient/ und cat /proc/loadavg). Nichts in place ueberschrieben
    (Version 2 unter neuem Namen), kein pkill/pgrep, kein flock von Hand. Rauchlauf 2 und die echte Kette teilten sich
    cpu3 und cpu4; die Reihenfolge ergab sich aus den Sperren.
11. **Sonst:** kein git, kein Peerbus, kein Journal, keine Unteragenten, keine Dienste, Timer oder Hooks. Testausgaben
    der jq-Skripte nur im Scratchpad. Die Ueberwachungs-Werkzeuge legten ihre Ausgaben selbst unter /tmp/claude-1000/
    ab.

## Einfach gesagt

Ein Q-Ball kann bei bestimmten Frequenzen schwingen, ohne Wellen abzustrahlen; diese Frequenzen bilden eine Leiter mit
fast gleichen Abstaenden. Ein anderes Team hat vorher versiegelt aufgeschrieben, wo die naechsten sechs Sprossen liegen
sollen, und ich habe nur gemessen, ohne diese Vorhersage zu kennen. In jedem der sechs Suchfenster habe ich genau eine
Sprosse gefunden, auf zwei verschieden feinen Rechengittern, und ihr Drehsinn wechselt jedes Mal wie erwartet. Bei der
einen Modellvariante (beta = 1) sind die Lagen auf acht Stellen sicher; bei der anderen (beta = 1/2) sind die Baelle so
gross, dass die Rechnung an die Grenze der Computergenauigkeit stoesst, und die Lage ist nur auf drei bis vier Stellen
nach dem Komma von 1/eps sicher. Ob die Vorhersage trifft, prueft jetzt die Leitung.

---
Letzte Aenderung dieser Datei: 2026-10-03 12:19:20 CEST (date). Zeitbox 90 min ab 11:27:13 eingehalten.
