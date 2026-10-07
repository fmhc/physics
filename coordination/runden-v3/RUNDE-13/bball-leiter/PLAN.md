# B-BALL-LEITER: Plan (Runde 13, explorativ)

- Code-Agent, Auftrag der Leitung claude-primary. Start 2026-10-01 19:09:03 CEST (date). Plan begonnen 2026-10-01
  19:21:20 CEST (date), vor jedem Suchlauf. Zeitbox 75 min (Zusatz der Leitung), also bis 20:24 CEST.
- Grundlagen: KARTE.md (dieser Ordner, bindend), RUNDE-12/x-baelle/X-BAELLE.md (T3, Familien-Tabelle),
  RUNDE-12/afm-kanal2/ (PLAN.md, ERGEBNIS.md, afm_bic.py), RUNDE-12/afm-kanal1/ (HERLEITUNG.md, ERGEBNIS.md,
  afm_kanal.py), RUNDE-10/nls-leiter/ (ERGEBNIS.md, nls2.py), RUNDE-07/bic2/bic2.py (nur Referenz).
- Markierungen: [A] an der Quelle gelesen, [L?] aus dem Gedaechtnis, [H] Hypothese, [ES] eigener Schluss. Modell ist
  keine Messung.

## 1 Aus KARTE.md woertlich uebernommen

### Positivkontrolle (bindend)

- K1: Derselbe Code mit dem Sextik-Potential findet die bewiesene Stelle omega^2 = 0,797677, rho = 1,744618 auf 1e-4,
  Umlauf +-1 auf beiden Stufen. Verfehlt K1: nicht auswertbar.
- K2: Profil-Probe des Log-Balls. Ladung Q(omega) und Energie E(omega) auf zwei Gittern auf 1e-4 gleich.

### Regel (bindend)

- **Gesehen:** In mindestens einem Band ein aufgeloestes Rechteck mit Umlauf +-1 auf beiden Stufen, mit Vorzeichenwechsel
  von s, Lagen zwischen den Stufen auf 1e-3 gleich.
- **Nicht gesehen:** In keinem Band ein Vorzeichenwechsel von s, alle Rechtecke aufgeloest mit Umlauf 0, K1 bestanden.
- **Unentschieden:** alles andere.

### Vorhersage (Leitung, vor jedem Lauf)

- K1 besteht: ~85 %.
- Schritt 0 findet einen nackten Zustand im Kontinuum: ~60 %.
- Gesehen (mindestens eine stille Stelle in den drei Baendern): ~45 %. Dafuer spricht, dass die Sextik-Stelle n = 1 im
  dicken Ball sitzt und nicht an die Duennwand gebunden ist. Dagegen spricht, dass das Log-Potential keine Duennwandgrenze
  hat und der Kanal-Topf anders aussieht.
- Falls gesehen: Lage rho zwischen 1,5 und 1,95 (Haeufung nahe 2m, Boussaid/Comech laut X-BAELLE [S]).

## 2 Potential und Quelle

- Abfrage: arXiv-API (https://export.arxiv.org/api/query, search_query=au:Kasuya AND au:Kawasaki AND ti:Q-ball AND
  ti:formation), 19:12:25 CEST; Antwort quellen/arxiv-abfrage-1.xml. Die erste Abfrage per http kam leer zurueck
  (Umleitung, nicht gespeichert); dann https. Die Nummer hep-ph/9909509 stammt aus dieser Antwort.
- **Quelle [A]:** S. Kasuya, M. Kawasaki, "Q-ball Formation through Affleck-Dine Mechanism", arXiv:hep-ph/9909509v3
  (PRD 61, 041301 (2000) [L?, nur das Journal]). Datei quellen/hep-ph-9909509v3.pdf (sha256 dc7f1a96...fdf04), Text
  quellen/hep-ph-9909509v3.txt (pdftotext -layout).
  - **Gl. (1), PDF-Seite 2:** V(Phi) = m^4 ln(1 + |Phi|^2/m^2) - c H^2 |Phi|^2 + (lambda^2/M^2) |Phi|^6, "where m is the
    mass of the field". Woertlich dazu: "This form of the potential arises naturally in the gauge-mediated SUSY breaking
    scenario in MSSM [8]" ([8] = Kusenko/Shaposhnikov, PLB 418, 46; nicht gelesen).
  - Gl. (8), PDF-Seite 2: V1 ~ m^4 log(1 + phi^2/(2 m^2)) mit Phi = phi e^{i theta}/sqrt(2). Das Feld Phi ist also
    kanonisch komplex mit kinetischem Term |d Phi|^2 [ES].
- **Fuer den Q-Ball** gilt: Der Hubble-Term faellt spaet weg (H -> 0). Den |Phi|^6-Term (M = Planckmasse) lasse ich weg.
  Damit bleibt V = m^4 ln(1 + |Phi|^2/m^2).
- **Dimensionslos:** Phi = m phi, x = x'/m, t = t'/m. Daraus folgt L = m^4 (|d' phi|^2 - ln(1 + |phi|^2)), also
  U(S) = ln(1 + S) mit S = |phi|^2 und U'(0) = 1 (Vakuummasse 1). **Die Form stimmt mit der Karte ueberein; es braucht
  keine Umrechnung.**
- Q-Baelle gibt es fuer 0 < omega^2 < 1 (U/S faellt von 1 gegen 0). Es gibt keinen Gipfel des mechanischen Potentials
  (omega^2 S - U(S))/2 und keine Duennwandgrenze.

## 3 Gleichungen (keine neue Herleitung; Verallgemeinerung des KG-Zweigs von afm_bic/bic2)

- Profil: f'' + (2/r) f' = (U'(S) - omega^2) f.
- Linearisierung um phi = f e^{-i omega t}: (U' + S U'') eta + S U'' eta*. Daraus folgen die Kanalgleichungen
  wie afm_bic, l = 0, y = r w, Zeitfaktor e^{-i rho t}:
  - y1'' = (A + B rho - rho^2) y1 + C y2 (geschlossen, omega - rho, Schwelle 1 + omega)
  - y2'' = C y1 + (A - B rho - rho^2) y2 (offen, omega + rho, Schwelle 1 - omega)
  - A = dp - omega^2, B = 2 omega, C = sp, dp = U' + S U'' = d(S U')/dS, sp = S U''.
  - Sextik (U = S - S^2 + S^3/2): dp = 1 - 4S + 4,5 S^2, sp = -2S + 3S^2. Das ist **ziffergleich** der KG-Zweig von
    afm_bic (beta = 1/2).
  - Log: dp = 1/(1 + S)^2, sp = -S/(1 + S)^2.
- Probe [ES]: Aussen ist S -> 0, also dp -> 1 und sp -> 0, Fenster 1 - omega < rho < 1 + omega.
- W = L(y_a) + i L(y_b); W = 0 <=> stille Stelle (Satz in RUNDE-07/bic2/PLAN.md, wie afm_bic).
- Code bball.py: Die Teile W_reell, W_multi, wurzeln, rechteck, paaren, lokalisieren, D_komplex, pole, reihe und
  umlauf sind aus afm_bic.py unveraendert kopiert. Neu sind:
  - der Profilloeser: Schiessen wie nls2.profile, fuer beide Potentiale. Beim Log gibt es keinen Gipfel; die obere
    Grenze startet bei 2 sqrt(X_z + 1) und wird verdoppelt, bis ein Ueberschuss auftritt. Der Schwanz A e^{-kappa r}/r
    wird ab f < 1e-4 f0 angesetzt.
  - die Kommandos schritt0, k2 und auswertung, letzteres nach der Regel oben.
  - **Sextik und Log laufen durch denselben Code**; nur U', U'', dp und sp wechseln.
- Rauchtest (lokal, h = 0,04): Sextik lokalisiert bei 0,79767659 / 1,74461748, ziffergleich mit dem
  AFM-KANAL-2-Rauchtest (0,79767659 / 1,74461748). Der nackte Kanal gibt E = 0,706247 bei omega^2 = 0,7977, wie R10
  und AFM-KANAL-1 K2. Der neue Profilloeser trifft das Sextik-Modell also.

## 4 Schritt 0: nackter geschlossener Kanal (bindend, vor dem Einfrieren gerechnet)

- Methode wie AFM-KANAL-1 (C = 0): -y'' + dp(r) y = E y, E = (rho - omega)^2, Dirichlet bei r = 0 und R_max.
  R_max = max(3 R_w, R_w + 40); Gegenprobe mit R_max + 20. Tridiagonal (eigh_tridiagonal), Profilschritt h/2.
  Gebundene Zustaende: E < 1; zugehoerige Lagen rho+ = omega + sqrt(E), rho- = omega - sqrt(E). Eingebettet heisst
  1 - omega < rho < 1 + omega.
- Kontrolle im selben Code (Rauchtest lokal, rauch-s0-kg, 2,9 s): Sextik omega^2 = 0,7977 ergibt E = 0,706247,
  rho+ = 1,733525 (eingebettet). AFM-KANAL-1 K2: 1,733525; R10: E = 0,706247.
- **Ergebnis (.69, cpu3/cpu4, alle 33 Zeilen, h = 0,02 und 0,01 gleich bis ~1e-5 in E):**
  - Band [0,30; 0,40]: zwei Zustaende je Zeile, beide eingebettet.
    - k = 0: rho+ = 1,0133 (0,30) .. 1,1676 (0,40), E = 0,2167 .. 0,2864
    - k = 1: rho+ = 1,4178 .. 1,5878, E = 0,7570 .. 0,9126
  - Band [0,50; 0,60]:
    - k = 0 eingebettet, rho+ = 1,3049 .. 1,4312 (E = 0,3573 .. 0,4311)
    - k = 1 nur bei 0,50 / 0,51 / 0,52, knapp unter der Schwelle (E = 0,9946 / 0,9977 / 0,99999; rho+ 1,7044 .. 1,7211;
      kastenabhaengig, |dE| bis 4,8e-4). Ab 0,53 ist er weg.
  - Band [0,70; 0,80]: ein Zustand k = 0, rho+ = 1,5511 .. 1,6698 (E = 0,5104 .. 0,6012), eingebettet. Fuer 0,78 bis
    0,80 liegt auch rho- = 0,1205 .. 0,1191 knapp ueber 1 - omega, also eingebettet.
  - Die Zustaende sitzen im Ball: r_spitze 2,2 bis 5,5 bei R_w = 2,7 bis 3,7; P = 3,8 bis 7,2.
- **Folge:** In allen drei Baendern gibt es nackte Zustaende im Kontinuum. "Nicht gesehen" ist darum **nicht**
  vorhersagbar, und der Test ist eine offene Frage, keine Mechanismus-Bestaetigung. Schritt 0 nennt keinen besseren
  Bereich; **die Baender bleiben wie in der Karte.**
- Laeufe: s0-log-h0.02 (cpu3, 7,3 s, rc = 0; enthaelt als 34. Zeile versehentlich Log bei 0,7977, ohne Bedeutung),
  s0-log-h0.01 (cpu4, 16,2 s, rc = 0), beide 17:19:16 UTC. Ausgaben lauf-69/aus/s0-log-h0.0{2,1}.{json,txt}
  - sha256 s0-log-h0.02.json 4d34402e7c1453de416900a5a5059ecbb2615c1e18ec4d61e6c46ec865e7612a
  - sha256 s0-log-h0.01.json f74fe5533f2860e0268df5723e2b8944716ae78563f8f121ac7041c0fb50ce65

## 5 K2 (vor dem Einfrieren gerechnet)

- Q = 8 pi omega Int f^2 r^2 dr, E = 4 pi Int (omega^2 f^2 + f'^2 + U(f^2)) r^2 dr (Simpson, mit Schwanz), alle
  33 Zeilen, Profilschritte 0,01 und 0,005 (= Gitterstufen h = 0,02 und 0,01). Kriterium: |dQ|/Q < 1e-4 und
  |dE|/E < 1e-4 je Zeile.
- Zusatz, nicht entscheidend: Virialprobe E - omega Q - (2/3) T = 0 mit T = 4 pi Int f'^2 r^2 dr.
- **Ergebnis k2-log (.69 cpu3, 17:20:25 bis 17:20:44 UTC, 18,7 s, rc = 0): bestanden.**
  - groesstes |dQ|/Q = 6,2e-11, groesstes |dE|/E = 5,5e-11
  - Virialrest < 1e-12 (Schritt 0,005)
- Beispiele (Schritt 0,005):
  - omega^2 = 0,30: f0 = 6,7638, R_w = 3,665, Q = 7717,90, E = 5106,75
  - 0,55: f0 = 3,5428, R_w = 2,855, Q = 1452,55, E = 1248,57
  - 0,80: f0 = 1,8647, R_w = 2,698, Q = 464,79, E = 455,99
  - Q faellt mit omega (dQ/domega < 0) [ES].
- sha256 k2-log.json e1e416997b0211a806db061ecc70e26e3e431a5d5bafae10158357961d9dc1b6
- Lesart des Agenten (vor dem Einfrieren): Die Karte bindet an K2 keinen eigenen Ausgang. Verfehlt K2, waeren die
  Profile nicht belastbar; der Ausgang waere dann hoechstens "Unentschieden". Gilt nur als Vorsorge; K2 ist bestanden.

## 6 Baender, Zeilen, Abtastung, Gitter

- Baender wie in der Karte, je 11 Zeilen im Abstand 0,01:
  - b1: omega^2 = 0,30; 0,31; ...; 0,40
  - b2: 0,50; ...; 0,60
  - b3: 0,70; ...; 0,80
- Zwischen benachbarten Zeilen liegt je ein Streifen, also 10 je Band. Je Streifen 2 Zwischenreihen (n_mid = 2,
  1500 rho-Punkte). Sie dienen als omega^2-Seiten und fuer die Astpaarung.
- rho je Zeile:
  - 4000 Punkte gleichabstaendig im Fenster [1 - omega + 0,002; 1 + omega - 0,002]
  - plus 2000 Punkte in [1,5; 1,95] geschnitten mit dem Fenster (Vorhersage-Bereich der Leitung)
  - plus die Fensterecken der Nachbarzeile
- Nullstellensuche direkt:
  - jede Vorzeichenklammer von L(y_b) mit 100 Punkten nachrastern
  - Sekante in der Endklammer
  - dort W exakt neu rechnen, s = L(y_a) an der Nullstelle, ohne lineare Interpolation von s
- Gitterstufen h = 0,02 und h/2 = 0,01; das Profilgitter ist jeweils h/2.
- Aussenrand R: erster Gitterpunkt mit f < 1e-6 f(0), mindestens 20. Die Rand-Abweichung von A, B, C gegen die
  Aussenwerte wird je Zeile berichtet; im Rauchtest war sie <= 1,2e-11 (R = 20 bis 24). Anschlusspunkt r_m = R_w
  (halbe Amplitude).
- Zur Groesse: Bei omega^2 = 0,30 ist der Log-Ball noch klein (R_w = 3,67, f0 = 6,76). Der Aussenrand liegt im
  Rauchtest bei R = 20 (Minimum) bis 24; dort ist f < 1e-6 f(0). Das Profil ist am Rand also abgeklungen.

## 7 Verfahren je Band und Stufe (bball.py familie, wie afm_bic)

- Streifen-Umlauf: Rechteck [omega^2_i, omega^2_{i+1}] x Fenster(omega^2_i). Die rho-Seiten sind die dichten
  Zeilen, die omega^2-Seiten die Zwischenreihen plus adaptiv neue Profile (bis 8 Runden, hoechstens 60 Profile); die
  rho-Seiten werden bis 40-mal halbiert. **Aufgeloest = jeder Phasensprung < 0,4 rad.** Gegenprobe:
  Kreuzungszaehlung (nicht entscheidend).
- Paarung: Nullstellen benachbarter Reihen (Zeilen und Zwischenreihen nach omega^2 geordnet), wechselseitig naechste
  gleicher Richtung, Abstand < 0,3. Ein Vorzeichenwechsel von s auf einem gepaarten Ast ist ein Kandidat.
- Je Kandidat (hoechstens 4):
  - Illinois in omega^2 auf s entlang des Astes, bis die Klammer < 1e-7 ist oder 10 Schritte erreicht sind
  - kleines Rechteck omega^2* +- 4e-4, rho* +- max(2e-3, 3 |drho/domega^2| 4e-4), hoechstens 0,02
- Pole (Breiten): nur auf h = 0,02, Newton wie afm_bic, Nullstellen mit rho < 1 - omega + 0,02 ausgelassen. Sie sind
  Zusatz und nicht Teil der Regel.
- K1: Sextik mit den Zeilen 0,785; 0,79; ...; 0,815 (7 Zeilen wie AFM-KANAL-2), sonst gleiche Einstellungen, beide
  Stufen.

## 8 Laufliste (.69, nur Spuren cpu3 und cpu4, ueber kleintest.sh; Starter start.sh einmalig per nohup)

| Lauf | Spur | Inhalt | Dauer |
|---|---|---|---|
| s0-log-h0.02 | cpu3 | Schritt 0, 33 Zeilen | gemessen 7,3 s |
| s0-log-h0.01 | cpu4 | Schritt 0, 33 Zeilen | gemessen 16,2 s |
| k2-log | cpu3 | K2, 33 Zeilen, Schritte 0,01 und 0,005 | gemessen 18,7 s |
| kg-h0.02 | cpu3 | K1, mit Polen | erwartet ~1 min |
| kg-h0.01 | cpu4 | K1 | erwartet ~1,5 min |
| auswertung-k1 | cpu3 | Pruefung K1; verfehlt -> Abbruch des Starters | < 5 s |
| log-b1-h0.02, log-b2-h0.02, log-b3-h0.02 | cpu3 nacheinander | Baender, mit Polen | erwartet je 1 bis 4 min |
| log-b1-h0.01, log-b2-h0.01, log-b3-h0.01 | cpu4 nacheinander | Baender | erwartet je 1,5 bis 5 min |
| auswertung | cpu3 | Regel | < 5 s |

- Hochrechnung aus den Rauchtests (lokal, h = 0,04, 800 + 300 rho-Punkte): 0,1 s Abtastung je Zeile, Streifen
  0,1 s, Profile ~1 s je Stapel. Bei h = 0,01 und 6000 Punkten ~2 s je Zeile; Lokalisierung ~10 Profile. Budget im
  Code 520 s je Aufruf; was danach nicht mehr passt, entfaellt mit Vermerk ("budget_entfallen").
- Rauchtests lokal (System-python3, 1 Thread, nice 19, timeout), Ausgaben lauf-lokal/, ungueltig fuer die Regel:
  - rauch-s0-kg 2,9 s; rauch-s0-log 2,1 s; rauch-k2 4,3 s
  - rauch-kg 9,5 s (K1-Pfad, h = 0,04)
  - rauch-log-b3 3,6 s (omega^2 0,70/0,71/0,72): je 1 Nullstelle bei rho 1,557 .. 1,580, s/median +1,2e-2 .. +9,6e-3,
    Gamma 8,4e-5 .. 6,0e-5, kein Wechsel
  - rauch-log-b1 2,5 s (0,30/0,31): je 2 Nullstellen (rho 1,020/1,036 und 1,422/1,441) mit s/median +5e-2 bzw. -7e-2,
    Gamma 1,9e-3 bzw. 1,4e-3, kein Wechsel
  - **Diese Rauchtestzahlen kannte ich vor meiner eigenen Vorhersage (Abschnitt 10).**

## 9 Auswertung (wortgleich zur Regel der Karte; Umsetzung bball.py auswertung)

- Regel (Karte, woertlich):
  - **Gesehen:** In mindestens einem Band ein aufgeloestes Rechteck mit Umlauf +-1 auf beiden Stufen, mit
    Vorzeichenwechsel von s, Lagen zwischen den Stufen auf 1e-3 gleich.
  - **Nicht gesehen:** In keinem Band ein Vorzeichenwechsel von s, alle Rechtecke aufgeloest mit Umlauf 0, K1 bestanden.
  - **Unentschieden:** alles andere.
- K1 bestanden: auf beiden Stufen ein lokalisierter Kandidat (aus einem s-Wechsel) mit |omega*^2 - 0,797677| < 1e-4,
  |rho* - 1,744618| < 1e-4 und aufgeloestem kleinem Rechteck mit Umlauf +-1. Verfehlt: "nicht auswertbar", und der
  Starter rechnet die Baender nicht.
- "Gesehen": in einem Band auf beiden Stufen je ein lokalisierter Kandidat (also mit s-Wechsel). Sein kleines Rechteck
  muss aufgeloest sein und Umlauf +-1 haben, und die Lagen omega*^2 und rho* muessen zwischen den Stufen auf 1e-3
  uebereinstimmen.
- "Nicht gesehen": K1 bestanden und, auf beiden Stufen in allen drei Baendern:
  - 0 s-Wechsel
  - alle 10 Streifen vorhanden, aufgeloest, Umlauf 0
  - kein Kandidaten-Rechteck mit Umlauf ungleich 0
  - alle 11 Zeilen gueltig
  - dazu K2 bestanden (Lesart Abschnitt 5)
- Sonst "Unentschieden". Ausdruecklich auch: ein nicht aufgeloester oder fehlender Streifen, ein s-Wechsel ohne
  aufgeloestes +-1-Rechteck auf beiden Stufen, oder ein Streifen-Umlauf ungleich 0 ohne s-Wechsel.
- Lesart [ES]: "Rechteck" heisst in "Nicht gesehen" die Streifen und die Kandidaten-Rechtecke, in "Gesehen" das kleine
  Rechteck um den lokalisierten Kandidaten (wie AFM-KANAL-2).
- Folgelaeufe nach den Hauptlaeufen nur als Nachtrag mit Vorhersage, vor dem Lauf eingefroren und als nachtraeglich
  gekennzeichnet. Sie aendern den Ausgang nicht; ob sie gelten, entscheidet die Leitung.

## 10 Eigene Vorhersagen (Code-Agent, nach den Rauchtests und Schritt 0, vor den Hauptlaeufen)

- E-1 K1 besteht auf beiden Stufen: ~92 % (Rauchtest ziffergleich mit AFM-KANAL-2).
- E-2 Ausgang:
  - "Gesehen" ~15 %
  - "Nicht gesehen" ~55 %
  - "Unentschieden" ~30 %
  - [H] Begruendung: In b3 faellt s im Rauchtest nur um ~4e-4 je 0,01 (KG: ~1e-2 je 0,005). Linear gerechnet laege
    die Nullstelle erst bei omega^2 ~ 0,86, also ausserhalb. In b1 liegen beide Aeste mit |s|/median 5e-2 bis 7e-2
    weit weg von 0.
  - Risiko fuer "Unentschieden": der Ast k = 1 in b2, der an der geschlossenen Schwelle austritt, und schmale
    Resonanzen an den Raendern.
- E-3 Falls gesehen: in b2 oder b3, rho 1,5 .. 1,75: ~60 %.
- E-4 Die Polbreiten liegen bei 1e-5 bis 1e-2, viel breiter als beim dicken AFM-Ball. Kein Ast wird schmaler als 1e-7:
  ~75 %.
- E-5 Streifen-Umlauf und gepaarte s-Wechsel stimmen je Streifen ueberein: ~90 %.

## 11 Einfrieren

- Vor dem ersten Suchlauf: Kopie PLAN.md.eingefroren-<JJJJMMTT-HHMMSS> (Zeit per date), chmod a-w, sha256 im
  ERGEBNIS.
- Hashes beim Einfrieren:
  - bball.py 2edf52b6344aa4dc88cdca095c022a3d06b27e5c2215e1a9b0e97accbe2f349b (lokal = .69)
  - start.sh d8548ceb8c37829bf8d5d95b798f68640f92242eecf3d128fe8bca5210aac6fa
  - KARTE.md 2794de28cf18ce6395a00b2bed67836d15c61d6b0d1f16ff36a65b71e25ab811
  - Quelle hep-ph-9909509v3.pdf dc7f1a96b484a6def22f3c24bfd00ebbe27e7f75c64218de9504e87d1a9fdf04
  - Abfrage arxiv-abfrage-1.xml c87ea12931cb2a0ee79e83aab7cfef3ad32b9196a15ae96dd7f1c90938bdcd51

## 12 Nachtrag 1 (NACHTRAEGLICH, nach Kenntnis der Hauptlaeufe; geschrieben ab 2026-10-01 19:27:49 CEST, date)

- Stand beim Schreiben: K1 auf beiden Stufen bestanden. b1 und b2 (beide Stufen) sowie b3 (h = 0,02) zeigen 0
  s-Wechsel; alle Streifen sind aufgeloest und haben Umlauf 0. b3 bei h = 0,01 und die Schlussauswertung liefen noch.
- Anlass: Der Ast k = 0 in b3 (Richtung +1) hat s > 0 und faellt gleichmaessig. Bei h = 0,02 geht s von +6,73e-3
  (omega^2 = 0,70) auf +2,67e-3 (0,80), die Polbreite Gamma von 8,4e-5 auf 1,0e-5. Ein Vorzeichenwechsel oberhalb
  von 0,80 ist damit moeglich, liegt aber ausserhalb der Baender der Karte.
- **Wertung:** Der Folgelauf aendert den Ausgang nach der Regel nicht. Die Karte verbietet, die Baender nach dem
  Einfrieren zu verschieben. Ob er gilt, entscheidet die Leitung.
- Folgelauf:
  - bball.py unveraendert (gleicher Hash), familie --modell log --band b3plus, Zeilen omega^2 = 0,80; 0,81; ...; 0,95
    (16 Zeilen, Abstand 0,01)
  - sonst alle Einstellungen wie die Hauptlaeufe; h = 0,02 mit Polen (cpu3), h = 0,01 ohne Pole (cpu4)
  - Ausgabe aus-nachtrag/, getrennt von aus/; Start per kleintest.sh, je Spur ein Aufruf
- Auswertung des Folgelaufs, gleiches Kriterium wie "Gesehen":
  - je Stufe ein lokalisierter Kandidat aus einem s-Wechsel
  - sein kleines Rechteck aufgeloest (< 0,4 rad), Umlauf +-1
  - Lagen omega*^2 und rho* zwischen den Stufen auf 1e-3 gleich
  - Pruefung per jq, weil bball.py auswertung K1-Laeufe im selben Ordner erwartet. Berichtet werden auch alle Streifen.
- Vorhersage (vor dem Lauf):
  - s wechselt auf diesem Ast zwischen 0,80 und 0,95 das Vorzeichen: ~70 %
  - falls ja:
    - Kriterium oben auf beiden Stufen erfuellt: ~90 %
    - Lage omega*^2 in [0,84; 0,92] und rho* in [1,70; 1,80]: ~65 %
    - Umlauf -1 wie bei K1 (gleiche Richtung +1, s von + nach -): ~80 %
    - Gamma hat dort ein V-foermiges Minimum (Gamma ~ s^2 wie beim Sextik-Modell): ~80 %
  - alle Streifen des Folgelaufs aufgeloest: ~85 %

## 13 Karte 2: B-BALL-2 Interpolation (KARTE-2-INTERPOLATION.md; geschrieben ab 2026-10-01 19:43:26 CEST, date)

- Folgeauftrag der Leitung, Start 2026-10-01 19:40:47 CEST (date), Zeitbox 45 min (bis 20:25:47 CEST). Nur Spuren
  cpu3 und cpu4 (Zusatz der Leitung). Wird es eng: zuerst t = 0,5, dann 0,25, dann 0,75 (Zusatz der Leitung).
- Entscheidung der Leitung zu Nachtrag 1 (Abschnitt 12): Der Ausgang der ersten Karte bleibt "Nicht gesehen". Der
  Fund bei omega^2 = 0,925610 zaehlt nicht fuer die erste Karte; Karte 2 prueft ihn mit vorab gebundener Vorhersage.

### 13.1 Aus KARTE-2-INTERPOLATION.md woertlich

- Mischpotential U_t(S) = (1 - t)(S - S^2 + S^3/2) + t ln(1 + S), t in [0, 1]. U_t'(0) = 1 fuer jedes t.
- Vorhersage (Leitung, vor jedem Lauf): lineare Interpolation zwischen den Endpunkten

| t | omega_t^2 (Vorhersage) | rho_t (Vorhersage) |
|---|---|---|
| 0,25 | 0,8297 | 1,7680 |
| 0,50 | 0,8617 | 1,7913 |
| 0,75 | 0,8936 | 1,8147 |

  - Formel: omega_t^2 = 0,7977 + 0,1279 t, rho_t = 1,7446 + 0,0934 t.
  - Kontinuitaet traegt (fuer alle drei t gefunden): ~70 %.
  - Bei t = 0,5 liegt die gefundene Stelle hoechstens 0,015 in omega^2 von der linearen Vorhersage entfernt: ~60 %.
  - Umlauf an allen drei Stellen -1, wie an beiden Endpunkten: ~85 %, falls gefunden.
- Kontrollen (bindend):
  - K1: t = 0 gibt die Sextik-Stelle (0,797677; 1,744618) auf 1e-4, Umlauf -1 auf beiden Stufen.
  - K2: t = 1 gibt die Log-Stelle des Nachtrags (0,925610; 1,837996) auf 1e-4, Umlauf -1 auf beiden Stufen.
  - Verfehlt K1 oder K2: nicht auswertbar.
- Regel (bindend, je t):
  - **Gefunden:** Aufgeloestes Rechteck mit Umlauf +-1 auf beiden Stufen, dazu ein Vorzeichenwechsel von s. Die Lage
    liegt im Fenster |omega^2 - omega_t^2| <= 0,04 und |rho - rho_t| <= 0,05, und die Stufen stimmen auf 1e-4 ueberein.
  - **Nicht gefunden:** Im Fenster kein Vorzeichenwechsel von s auf beiden Stufen, alle Rechtecke aufgeloest mit
    Umlauf 0.
  - **Unentschieden:** alles andere.
- Gesamt: "Kontinuitaet traegt": gefunden fuer alle drei t. "Kontinuitaet traegt nicht": fuer mindestens ein t nicht
  gefunden. Sonst unentschieden.

### 13.2 Code

- bball2.py = Kopie von bball.py. Einzige Aenderung: Modell "mix" mit U_t, U_t', U_t'' und daraus dp = U_t' + S U_t'',
  sp = S U_t''. Dazu der Parameter --t (globale Groesse T_MIX) und die Schiessgrenzen fuer U_t:
  - X_z = erste Nullstelle von U_t(X) - omega^2 X (Abtastung 1e-8 .. 1e4, dann Halbierung)
  - Gipfel X_m = erste Stelle X > X_z mit U_t'(X) = omega^2; es gibt ihn nur fuer t < 1
  - ohne Gipfel (t = 1) wie beim Log-Modell: die obere Grenze wird verdoppelt
  - Diff: bball2.diff. Die Kopfzeile der Textausgabe sagt weiterhin "bball.py" (nicht geaendert).
- Rechenteil (W, Nullstellen, Streifen, Paarung, Lokalisierung, kleines Rechteck, Pole) und Einstellungen wie in den
  Hauptlaeufen: n1 = 4000, n2 = 2000 in [1,5; 1,95], 2 Zwischenreihen je Streifen (1500 rho-Punkte), Rechteck
  omega*^2 +- 4e-4, rho* +- max(2e-3, 3 |drho/domega^2| 4e-4), Budget 520 s. Pole nur auf h = 0,02.

### 13.3 Zeilen je t (17 Zeilen, Abstand 0,005, Fenster Mitte +- 0,04)

| Lauf | t | Mitte | Zeilen omega^2 |
|---|---|---|---|
| K1 | 0 | 0,7977 (Sextik-Stelle) | 0,7577; 0,7627; ...; 0,8377 |
| t0.25 | 0,25 | 0,8297 | 0,7897; 0,7947; ...; 0,8697 |
| t0.5 | 0,5 | 0,8617 | 0,8217; 0,8267; ...; 0,9017 |
| t0.75 | 0,75 | 0,8936 | 0,8536; 0,8586; ...; 0,9336 |
| K2 | 1 | 0,9256 (Log-Stelle des Nachtrags) | 0,8856; 0,8906; ...; 0,9656 |

- Gitterstufen h = 0,02 (mit Polen) und h = 0,01. 16 Streifen je t und Stufe.

### 13.4 Laufliste (.69, kleintest.sh, Starter start2.sh einmalig per nohup)

- cpu3: K1-h0.02, K2-h0.01, t0.5-h0.02, t0.25-h0.01, t0.75-h0.02
- cpu4: K1-h0.01, K2-h0.02, t0.5-h0.01, t0.25-h0.02, t0.75-h0.01
- So sind Kontrollen und t = 0,5 nach etwa der halben Zeit fertig; die Reihenfolge folgt dem Zusatz der Leitung.
- Erwartete Dauer aus Nachtrag 1 (16 Zeilen 0,80 .. 0,95: 130 s bzw. 227 s): je Aufruf 1 bis 6 min, je Spur ~14 min.
- Ausgabe aus2/ (getrennt von aus/ und aus-nachtrag/).

### 13.5 Auswertung (per jq-Filter auswertung2.jq; bball2.py auswertung wird nicht benutzt)

- K1 bzw. K2 bestanden: auf beiden Stufen ein lokalisierter Kandidat mit |omega*^2 - Ziel| <= 1e-4,
  |rho* - Ziel| <= 1e-4 und kleinem Rechteck aufgeloest mit Umlauf -1.
- Je t "Gefunden":
  - auf beiden Stufen ein lokalisierter Kandidat (aus einem s-Wechsel)
  - sein kleines Rechteck aufgeloest (< 0,4 rad) mit Umlauf +-1
  - Lage im Fenster |omega*^2 - omega_t^2| <= 0,04 und |rho* - rho_t| <= 0,05
  - Lagen der Stufen auf 1e-4 gleich (omega^2 und rho)
- Je t "Nicht gefunden":
  - auf beiden Stufen kein s-Wechsel mit einer Lage im Fenster (beide Reihen des Wechsels gemittelt)
  - alle 16 Streifen beider Stufen aufgeloest mit Umlauf 0
  - kein Kandidaten-Rechteck mit Umlauf ungleich 0
- Sonst "Unentschieden", auch bei fehlenden Streifen oder ungueltigen Zeilen.
- Gesamt nach der Karte. Verfehlt K1 oder K2: "nicht auswertbar".
- Zusatzangaben je t:
  - Abstand der Lage zur Vorhersage
  - Umlauf und groesster Sprung des kleinen Rechtecks
  - Breitenminimum = kleinstes Gamma auf dem Ast mit dem s-Wechsel (Zeilen, h = 0,02)

### 13.6 Eigene Vorhersagen (vor jedem Lauf mit dem Mischpotential, auch vor dem Rauchtest)

- E2-1 K1 und K2 bestehen beide: ~93 %.
- E2-2 Gesamt:
  - "Kontinuitaet traegt" ~70 %
  - "traegt nicht" ~20 %
  - "unentschieden" ~10 %
- E2-3 Bei t = 0,5 liegt die Stelle hoechstens 0,015 in omega^2 von 0,8617 entfernt: ~50 %. Die Richtung der
  Abweichung kann ich nicht begruenden.
- E2-4 Falls gefunden: Umlauf -1 an allen drei t: ~90 %.
- E2-5 rho* steigt mit t monoton: ~80 %.
- E2-6 Das Breitenminimum nimmt von t = 0 zu t = 1 monoton ab (s wird mit t flacher): ~60 %.

### 13.7 Rauchtests (lokal, nach den eigenen Vorhersagen, vor dem Einfrieren; ungueltig fuer die Regel)

- System-python3, 1 Thread, nice 19, timeout 110 bis 115 s, h = 0,04, kleine Raster (800 + 300 rho-Punkte,
  1 Zwischenreihe), Ausgaben in lauf-lokal/:
  - rauch2-t0.5 (13,1 s), Zeilen 0,855 / 0,86 / 0,865: s-Wechsel, lokalisiert bei 0,85882371 / 1,79581474. Das kleine
    Rechteck hat Umlauf -1 und ist aufgeloest (0,399 rad); Gamma 3,4e-6 / 2,9e-7 / 7,0e-6.
  - rauch2-t1 (16,9 s), Zeilen 0,92 / 0,93: lokalisiert bei 0,92560847 / 1,83799391, Umlauf -1, aufgeloest
    (0,397 rad).
  - rauch2-t0 (8,7 s), Zeilen 0,795 / 0,80: lokalisiert bei 0,79767659 / 1,74461748 (wie der bball.py-Rauchtest),
    Umlauf -1, aufgeloest (0,359 rad).
- **Diese Rauchtestzahlen kannte ich nach meinen Vorhersagen in 13.6 und vor dem Einfrieren.** An der Regel und an
  den Laeufen aendern sie nichts.

### 13.8 Hashes beim Einfrieren

- bball2.py 9c13a5f1bf33fb021863a27f1b06c38648255fe68ca471d21f170d57c16d96c3
- bball2.diff 66d2557290a654ebfc4cb4bde8c70ed9e26b0cf498ffaf5843a72082f7642053
- start2.sh 4a35df16ba468581498c44927fa2653fd10ad23e3b79891b46228eb880d1f501

## 14 Karte 2b: B-BALL-2b letztes Viertel (KARTE-2B-LETZTES-VIERTEL.md; geschrieben ab 2026-10-01 20:04:14 CEST, date)

- Folgeauftrag der Leitung, Start 2026-10-01 20:03:07 CEST (date), Zeitbox 25 min (bis 20:28:07 CEST). Nur cpu3 und
  cpu4 (Zusatz der Leitung).
- Aus der Karte woertlich:
  - Vorhersage (Leitung, vor dem Lauf):
    - Quadratische Interpolation durch t = 0,5 / 0,75 / 1: omega*^2(0,9) = 0,9022 +- 0,012, rho*(0,9) = 1,8252 +- 0,008.
    - Gefunden (Kontinuitaet im letzten Viertel): ~85 %.
    - Umlauf -1: ~90 %, falls gefunden.
  - Regel (bindend):
    - **Gefunden:** Aufgeloestes Rechteck mit Umlauf +-1 auf beiden Stufen und ein Vorzeichenwechsel von s, mit der
      Lage in 0,8765 <= omega^2 <= 0,9256 und 1,810 <= rho <= 1,838. Die Lagen beider Stufen stimmen auf 1e-4 ueberein.
      Dann gilt "Kontinuitaet im letzten Viertel traegt". Die quadratische Vorhersage wird getrennt gewertet:
      getroffen, wenn die Lage im Band +-0,012 bzw. +-0,008 liegt.
    - **Nicht gefunden:** Im Fenster kein Vorzeichenwechsel von s auf beiden Stufen, alle Rechtecke aufgeloest mit
      Umlauf 0. Dann haengen Sextik- und Log-Stelle nicht nachweislich stetig zusammen.
    - **Unentschieden:** alles andere.
- Code: bball2.py unveraendert (Hash wie Karte 2), --modell mix --t 0.9.
- Zeilen: 18, gleichabstaendig von 0,8765 bis 0,9256, Abstand 0,002888 (per jq erzeugt):
  0,8765; 0,879388; 0,882276; 0,885165; 0,888053; 0,890941; 0,893829; 0,896718; 0,899606; 0,902494; 0,905382;
  0,908271; 0,911159; 0,914047; 0,916935; 0,919824; 0,922712; 0,9256. Damit 17 Streifen je Stufe.
- Einstellungen wie Karte 2 (n1 = 4000, n2 = 2000 in [1,5; 1,95], 2 Zwischenreihen, Budget 520 s).
- Laeufe:
  - t0.9-h0.02 auf cpu3 (mit Polen)
  - t0.9-h0.01 auf cpu4
  - je ein kleintest-Aufruf, direkt per setsid/nohup gestartet; Ausgabe aus2b/
  - Erwartet 2 bis 4 min je Lauf (Karte 2, t = 0,75: 130 s bzw. 220 s)
- Auswertung: auswertung2b.jq, vor dem Einfrieren geschrieben. Sie setzt die Regel oben um; "alle Rechtecke" heisst
  alle 17 Streifen beider Stufen und die Kandidaten-Rechtecke.
- Eigene Vorhersagen (vor dem Lauf; Rechnung im Kopf, nicht lokal gerechnet):
  - Gefunden: ~85 %
  - Lage in beiden quadratischen Baendern: ~60 %. Die kubische Interpolation durch t = 0,25 .. 1 gibt
    omega*^2 ~ 0,8995, ebenfalls im Band.
  - Umlauf -1, falls gefunden: ~92 %
- Hashes beim Einfrieren:
  - bball2.py 9c13a5f1bf33fb021863a27f1b06c38648255fe68ca471d21f170d57c16d96c3
  - auswertung2b.jq 3e1464fa0056095b0e0e4ea30a856da6e7e363cdbac8ac7096ce5260c71406c8

### 14.1 Nachtrag 2b (NACHTRAEGLICH, nach Kenntnis der Hauptlaeufe t = 0,9; geschrieben ab 2026-10-01 20:08:23 CEST, date)

- Stand: Bei t = 0,9 ist s im ganzen Fenster 0,8765 .. 0,9256 auf beiden Stufen negativ. s/median betraegt
  -4,8e-4 bei 0,8765, das Minimum ~-1,07e-3 liegt nahe 0,90, am oberen Rand sind es -7,2e-4. Nach der Regel heisst
  das "Nicht gefunden"; dieser Ausgang bleibt.
- Frage des Nachtrags: Liegt die Stelle bei t = 0,9 ausserhalb des Fensters? Erwartet waere unterhalb von 0,8765, weil
  s dort schon negativ ist, und eventuell eine zweite Nullstelle oberhalb von 0,9256.
- Laeufe (bball2.py unveraendert, --modell mix --t 0.9, Einstellungen wie Karte 2b, Ausgabe aus2b-nachtrag/):
  - unten: 13 Zeilen 0,82 .. 0,8765 (Abstand 0,004708): h = 0,02 (mit Polen) auf cpu3, h = 0,01 auf cpu4
  - oben: 11 Zeilen 0,9256 .. 0,9706 (Abstand 0,0045): h = 0,02 auf cpu3, h = 0,01 auf cpu4, jeweils danach
- Wertung: aendert den Ausgang der Karte 2b nicht; ob er gilt, entscheidet die Leitung. Berichtet werden s-Wechsel,
  lokalisierte Lagen, kleine Rechtecke (Umlauf, Sprung) und Streifen.
- Vorhersage (vor dem Lauf):
  - unten: ein s-Wechsel von + nach - mit Umlauf -1, aufgeloest auf beiden Stufen, Lage omega^2 in [0,84; 0,8765]:
    ~70 %
  - oben: ein s-Wechsel von - nach + mit Umlauf +1 (zweite Stelle, Gegenstueck): ~50 %

## 15 Karte 2c: B-BALL-2c letztes Zehntel (KARTE-2C-LETZTES-ZEHNTEL.md; geschrieben ab 2026-10-01 20:17:47 CEST, date vor dem Schreiben)

- Folgeauftrag der Leitung, Start 2026-10-01 20:16:17 CEST (date), Zeitbox 30 min (bis 20:46:17 CEST). Nur cpu3 und
  cpu4. Wird es eng: zuerst t = 0,95, dann 0,975, dann 0,925 (Zusatz der Leitung).
- Aus der Karte woertlich:
  - Regel (bindend):
    - **Eine wandernde Nullstelle:** Fuer jedes der drei t gibt es im weiten Fenster genau einen Vorzeichenwechsel von
      s, mit aufgeloestem Rechteck und Umlauf -1 auf beiden Stufen, und alle anderen Rechtecke haben aufgeloest Umlauf
      0. Die Lagen steigen mit t und liegen zwischen 0,8679 und 0,9256.
    - **Falte (zwei verschiedene Stellen):** Fuer mindestens ein t gibt es drei oder mehr Vorzeichenwechsel (ein Paar
      mit Umlauf +1 und -1 dazu), auf beiden Stufen aufgeloest. Oder der eine Wechsel springt nicht monoton.
    - **Unentschieden:** alles andere, auch kein Wechsel bei einem t.
  - Vorhersage (Leitung): Eine wandernde Nullstelle ~60 %; Falte ~30 %; falls eine wandernde Nullstelle, Lage bei
    t = 0,95 zwischen 0,88 und 0,91 ~60 %.
- Code bball2.py unveraendert (--modell mix, t in {0,925; 0,95; 0,975}).
- Zeilen je t: 31 Zeilen 0,82; 0,825; ...; 0,97 (Abstand 0,005), per jq erzeugt. Damit 30 Streifen je t und Stufe.
- Wegen der Laufzeit (t = 0,9: 13 + 18 + 11 Zeilen brauchten 95 + 106 + 105 s bei h = 0,02 und 165 + 174 + 177 s bei
  h = 0,01) laeuft jedes (t, h) in zwei Haelften:
  - A: 0,82 .. 0,895 (16 Zeilen), B: 0,895 .. 0,97 (16 Zeilen); die Zeile 0,895 ist in beiden.
  - Jedes Zeilenpaar und damit jeder s-Wechsel gehoert zu genau einer Haelfte. Die Streifen (je 15) werden addiert.
  - Erwartet je Aufruf 2 bis 4 min.
- Einstellungen sonst wie Karte 2 (n1 = 4000, n2 = 2000 in [1,5; 1,95], 2 Zwischenreihen, Rechtecke wie bisher,
  Budget 520 s). Pole nur bei h = 0,02.
- Laufliste (start2c.sh, einmalig per nohup; Ausgabe aus2c/):
  - cpu3: t0.95-h0.02-A, -B; t0.975-h0.01-A, -B; t0.925-h0.02-A, -B
  - cpu4: t0.95-h0.01-A, -B; t0.975-h0.02-A, -B; t0.925-h0.01-A, -B
  - Erwartet je Spur ~15 bis 18 min. Nicht fertige Teile werden als "nicht gerechnet" gefuehrt.
- Auswertung auswertung2c.jq, vor dem Einfrieren geschrieben. Je t und Stufe werden beide Haelften zusammengefasst.
  - "eine" je t: genau 1 s-Wechsel und 1 Kandidat; das kleine Rechteck aufgeloest mit Umlauf -1; alle 30 Streifen
    vorhanden und aufgeloest; Streifen mit Umlauf ungleich 0 nur der mit der Stelle (Umlauf -1); 31 Zeilen gueltig.
    Das alles auf beiden Stufen.
  - "falte" je t: >= 3 s-Wechsel, alle lokalisiert, alle kleinen Rechtecke aufgeloest, Umlaeufe +1 und -1
    vorhanden; auf beiden Stufen.
  - Gesamt:
    - "Eine wandernde Nullstelle", wenn "eine" fuer alle drei t gilt, die Lagen (h = 0,02) mit t streng steigen und
      alle in [0,8679; 0,9256] liegen
    - "Falte", wenn "falte" fuer ein t gilt, oder wenn "eine" fuer alle t gilt und die Lagen nicht streng steigen
    - sonst "Unentschieden"
  - Meine Lesart: "Stufen" heisst h = 0,02 und h = 0,01. Eine Uebereinstimmung der Lagen auf 1e-4 verlangt die Karte
    hier nicht; ich berichte sie nur.
- Eigene Vorhersagen (vor dem Lauf, Kopfrechnung):
  - Eine wandernde Nullstelle ~55 %, Falte ~25 %, Unentschieden ~20 %
  - Begruendung [H]: Bei t = 1 bleibt s oberhalb der Stelle nur schwach negativ (Delle bei ~0,94). Bei t = 0,9 liegt
    die Delle tiefer (Minimum bei ~0,90). Am einfachsten ist ein Bild, in dem die Delle mit t ueber 0 steigt und die
    eine Nullstelle nach rechts schiebt. Ein zweites Paar koennte am oberen Rand entstehen (s -> 0 bei 0,97 fuer
    t = 0,9).
  - Falls eine wandernde Nullstelle: Lage bei t = 0,95 in [0,88; 0,91] ~55 %
- Hashes beim Einfrieren:
  - bball2.py 9c13a5f1bf33fb021863a27f1b06c38648255fe68ca471d21f170d57c16d96c3
  - start2c.sh e9f10b03b4bbe89433027fd81ec83de3de3d2a50ec77284254d9c5e9eab04f29
  - auswertung2c.jq 0fc3cc7d42ac7efc78a945f270ceaa002b05129a493a408fff3ea8674df303bb
