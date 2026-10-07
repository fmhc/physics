Urteil: T1 traegt mit Auflagen (A2, A3; nur Text). T2 traegt mit Auflagen (A1, A3, A5). Kein blockierender Befund.

# Frische Lesung BEWEIS-2 (Haus Anthropic, frischer Leser)

- Beginn (date): 2026-09-30 12:45:34 CEST
- Ende (date): 2026-09-30 13:12:08 CEST (Dauer 26 min 34 s, gerechnet als 13:12:08 - 12:45:34; Zeitbox 60 min)
- Auftrag: Nachricht der Leitung claude-primary vom 30.09.2026 (kein BRIEF-Pfad mit sha256 genannt; die Nachricht selbst gilt als Auftrag). BRIEF.md im Ordner ist der Auftrag des Autors, nicht meiner.
- Regeln: nur lesen (cat, sed -n, grep, jq, sha256sum, diff, cmp, ls, date); kein python/awk; Rechnungen im Kopf mit Rechenweg. Geschrieben habe ich nur in diese Datei, per Write und Edit und einmal mit sed -i, um Zeilenverweise zu berichtigen.

## 0. Urteil

- **T1 (l = 0, n = 2): traegt mit Auflagen.** Die Auflagen A2 und A3 betreffen nur den Text. Es gibt keinen
  blockierenden Befund. Der Kern ist bytegleich. A und B waren vorab festgelegt und bestanden. Das Flag enthaelt
  2 kappa0 > kappa_c und rho > omega, der Export ist vollstaendig. 0 < h < R ist nachtraeglich aus den
  Schrittprotokollen belegt.
- **T2 (l = 1, n = 1): traegt mit Auflagen.** A1 und A3 betreffen den Text, A5 die Diagnose. Es gibt keinen
  blockierenden Befund. T2-A traegt allein und lief mit den vorab festgelegten Einstellungen.
  - T0-l1, T-l1, J-l1, W-l1 und E-l1 habe ich im Kopf nachgerechnet und gegen den Code gelesen; sie passen.
  - Das Gesamtflag enthaelt 2 kappa0 > kappa_c, rho > omega, kappa_c L >= 1 und 0 < h < R.
  - B2 ist eine nachtraegliche Bestaetigung. Ihr Kasten liegt in A.
  - Die Ursachenangabe zum Fehlschlag von T2-B ist falsch (F1). Das schwaecht den Satz nicht.
- Quote: 0 von 9 Befunden blockierend. Ueber 100 Zahlen im Text gegen JSON und Logs abgeglichen: eine Zahl falsch
  (z0_rho, F6), eine Grenze eine Einheit zu grosszuegig gerundet (harmlos), eine Ursachenangabe falsch (F1).
  sha256sum -c: 37 von 37 OK.

## 1. Integritaet (sha256sum -c, Dateizeiten)

- `sha256sum -c SHA256SUMS.txt` in zertifikat/ (12:46): 37 von 37 Dateien OK.
- Code-Hashes im Text (BEWEIS-2.md:325-330) = sha256sum der Dateien = Eintraege `.sha256` in den ZERT-JSON:
  T1-A/B pruef-l0.py 7713f636..., bewkern.py a8a7ec6f...; T2-A und T2-B pruef-l1.py c1f85f81... (= beigelegte
  pruef-l1-c1f85f81.py); T2-B2 pruef-l1.py eecfb3cd...; Kern bewkern_l1.py 24b3dc8d... in allen T2-Laeufen.
- `cmp` bewkern.py gegen RUNDE-07/beweis/zertifikat/bewkern.py: bytegleich.
- Interpreter- und FLINT-Hashes in allen fuenf ZERT-JSON gleich (e50d468e..., 1f7ef1f5..., 871a4132..., 33d24e67...,
  c4dfcfc7...).
- Die mtimes in zertifikat/ sind Kopierzeiten (alle T1-Dateien 12:23:25, alle T2-A-Dateien 12:31:58). Sie belegen
  keine Laufzeiten; dafuer taugen nur die start/ende-Zeilen in den Logs (UTC).
- `cmp`: SCHRITTE-KASTEN und SCHRITTE-PUNKT von T2-B und T2-B2 sind bitgleich. Das ist zu erwarten, weil c in die
  ODE-Integration nicht eingeht (Spalte c von DH_0 ist in den Zeilen 3 und 4 exakt 0).
- Schrittprotokolle mit jq geprueft (T1-A, T1-B, T2-A, T2-B2, jeweils Punkt und Kasten): kein Schritt verletzt
  0 < h < R, kein Schritt mit r_j > 0 hat R >= r_j, das letzte r_ende ist jeweils L. Schrittzahlen 350/362, 487/508,
  319/338, 445/472 wie im Text.

## 2. Abweichung 1: T2-B gescheitert, B2 nachgeschoben, "Kasten frei waehlbar"

(a) **T2-A traegt allein, mit vorab festgelegten Einstellungen.** Plan 4.8 (BEWEIS-2-PLAN.md:133-134) nennt
L = 36, 256 bit, N = 64/48, q = 1/3, Kastenfaktor 8. `.parameter` in ZERT-T2-A-L36.json nennt L = 36 (Lz = 0,
L aus z0-t2.json), N_punkt 64, N_kasten 48, q 1/3, kfak 8, prec 256. Die Kommandozeile hat keine Zusatzoption.
M3.BESTANDEN = true; alle zehn Kanal- und Schrittbedingungen sind wahr, dazu Lemma_P_ok, Krawczyk_in_Z und
positiv.klein_danach. Treiber c1f85f81 hat gegenueber dem Stand beim Plan nur Pruefungen hinzugefuegt
(0 < h < R, N >= 1, qfac > 1). Das schaerft den Test und lockert ihn nicht. Code: pruef-l1.py:530-543
(`ok_all = ok and okP and pos['klein_danach'] and all(kan.values())`).

(b) **B2 ist eine Bestaetigung, keine vorab festgelegte Wiederholung.** `diff pruef-l1-c1f85f81.py pruef-l1.py`
zeigt nur die Option --dcexp: argparse :250, Parameterblock :448-449, Skalierung :489-493. Die Parameter von B2
sind die von B, dazu dcexp 17. B2 ist also B mit einem nach dem Fehlschlag gewaehlten c-Radius. Plan 2 erlaubte
Aenderungen nach einem Fehlschlag nur ueber L, N, q oder Bitzahl (BEWEIS-2-PLAN.md:31). Diese Regel war fuer T1-A
geschrieben, sie nennt den Kastenradius aber nicht. Fuer T2 fehlt eine entsprechende Regel. Der Text
(BEWEIS-2.md:14-16, 206-207, 309-311) ordnet B2 richtig als nicht vorab festgelegt ein.

(c) **"Kasten frei waehlbar" stimmt im Sinn von Lemma K, unter drei Bedingungen, die der Code erfuellt:**
1. z0 liegt in Z, und Z ist konvex. Z = z0 +- delta ist ein Quader, der Mittelwertsatz gilt zeilenweise auf der
   Strecke in Z.
2. Alle Einschluesse gelten fuer genau dieses Z. Die Skalierung `delta[1] * 2**dcexp` (:493) steht vor
   `Zb = ...`, `evalH(Zb, ...)` fuer DH_0(Z), `tail_E(Zb, ...)` fuer eps und Lemma P ueber Z sowie vor den
   Kanalbedingungen ueber Zb. Deshalb unterscheiden sich eps_1 in B und B2 in der 10. Stelle: 1,3830165065e-17
   gegen 1,3830165068e-17, wegen |c|.upper.
3. Der Einschluss ist strikt (pruef-l1.py:521-523, `lower() > z0 - delta` und `upper() < z0 + delta`), und die
   gewichtete Zeilensumme ist < 1. Die exakte Zweierpotenz haelt delta dyadisch.

Unter diesen Bedingungen ist jeder Kasten zulaessig. Ein Kasten, der erst nach dem Ergebnis gewaehlt wird, macht den
Satz nicht falsch, weil nur Existenz behauptet wird und keine Eindeutigkeit (BEWEIS-2.md:55, 305).

(d) **B2 liegt in A (nachgeprueft).** protokoll.Z, Grenzen von A und B2 ziffernweise verglichen:
- a: 1,05352428417626453999773 < 1,05352428417626454001709 und 1,05352428417626454002058 < 1,05352428417626454003994
- c: 12,12363911266 < 12,12363938534 und 12,12363938714 < 12,12363965982
- rho: ...956187559 < ...956237658 und ...956246675 < ...956296774
- om: ...559803916 < ...559828704 und ...559833167 < ...559857955

Die Aussage "B2-Kasten liegt im A-Kasten" (BEWEIS-2.md:195) stimmt.

(e) **Die Begruendung des Fehlschlags ist falsch** (Abschnitt 5 (b)). Die c-Zeile scheitert an den Profilzeilen 1
und 2 und nicht an den l = 1-Zeilen 3 und 4. Das zeigt schon M1: das 2x2-Profilproblem scheitert in T2-B mit
Zeilensumme 19,10. Die Abhilfe B2 wirkt trotzdem, denn ein groesseres delta_c senkt die gewichtete c-Zeile,
gleich aus welcher Ursache: 19,1 / 2^17 = 1,46e-4, das ist .M1.rowsum von B2 (1,457e-4).

## 3. Abweichung 2: Codezeilen-Liste und Zeitfolge (BEWEIS-2.md 4.7)

Logzeiten stehen in UTC, CEST ist UTC + 2 h. Die start-Zeile ist die Einreihzeit vor flock; der Lauf beginnt erst,
wenn der vorige endet.

| Lauf | start (CEST) | ende (CEST) | Treiber-sha256 im JSON |
|---|---|---|---|
| t1-start / t1-newton | 12:12:13 / 12:12:20 | 12:12:14 / 12:19:11 | (Vorfassung, nicht beigelegt) |
| T1-A, T1-B | 12:20:15, 12:21:23 | 12:21:23, 12:23:00 | pruef-l0 7713f636 |
| t2-frei | 12:21:50 (Warteschlange) | 12:23:04 | - |
| t2-start / t2-newton | 12:24:09 / 12:24:10 | 12:24:10 / 12:30:24 | (Vorfassung 6ca5c2d9, nicht beigelegt) |
| T2-A | 12:30:40 | 12:31:43 | c1f85f81 |
| t2-kontrolle, T2-B | 12:31:36, 12:31:43 | 12:33:02, 12:34:39 | c1f85f81 (B) |
| T2-B2 | 12:37:00 | 12:38:36 | eecfb3cd |

Was vor welchem Lauf feststand:
- **Code, belegt durch Hashes und mtimes.** pruef-l0.py ist seit 12:16:55 unveraendert (vor T1-A). bewkern_l1.py ist
  seit 12:18:11 unveraendert und hat in allen T2-JSON denselben Hash. pruef-l1.py (eecfb3cd) hat mtime 12:36:39,
  also nach dem Ende von B (12:34:39) und vor B2 (12:37:00). Jedes Zertifikat nennt die sha256 der laufenden
  Fassung. Die Zuordnung Lauf zu Code ist damit belegt, soweit man den JSON-Dateien traut.
- **Plan- und Vorab-Zeilen: per mtime nicht belegbar.** BEWEIS-2-PLAN.md hat mtime 12:40:52, STAND.md 12:44:06.
  Beide liegen nach allen Ergebnisdateien. Die Zeiten 12:11:22 (T1), 12:22:22 (T2) und 12:36:54 (B2) sind nur
  Selbststempel des Autors. BRIEF.md:37 verlangt "vorab heisst: vor der Ergebnisdatei, mtime pruefen". Diese Pflicht
  ist nicht erfuellt, und der Text sagt das auch (BEWEIS-2.md:228-230). Die Stempel sind in sich stimmig: B2-Stempel
  12:36:54 liegt 15 s nach der mtime der Codeaenderung und 6 s vor dem Start von B2. Unabhaengig belegen kann ich
  sie nicht.
- **Zeilenliste.** Vor den Beweislaeufen stand sie nicht vollstaendig im Plan. Es fehlten die Auflagen-Aenderungen
  in pruef-l0.py (vor T1-A), alle Zeilennummern fuer T2, 0 < h < R (vor T2-A) und --dcexp (vor B2). Nachgetragen
  ist sie ab 12:40:27 (BEWEIS-2-PLAN.md:150-175, als verspaetet gekennzeichnet). Inhaltlich fuegt jede dieser
  Aenderungen nur Pruefungen oder Exporte hinzu, --dcexp nur die Kastenwahl. Keine davon lockert ein Tor. Das habe
  ich per diff fuer --dcexp und anhand der Flag- und Exportzeilen (pruef-l1.py:530-543, 658-666) fuer den Rest
  nachgesehen. Fuer pruef-l0 gegen pruef-v2 habe ich keinen vollstaendigen diff gelesen.
- **Newton-Vorfassungen** (b3c42c59, 6ca5c2d9) liegen nicht bei. Fuer die Strenge ist das ohne Belang, weil Newton nur
  z0 liefert. Die Angabe "Unterschied nur in zert()" ist deshalb nicht pruefbar.
- **Frei-Test l = 1:** eingereiht 12:21:50, gelaufen bis 12:23:04, also vor dem T2-Newton und vor T2-A. Der Text
  (BEWEIS-2.md:225-228) beschreibt das richtig.
- **Kleinigkeit:** Die Logkopfzeile "modus zert ... L 40" (LAUF-t2-zertA-L36.log:3) gibt args.L aus und nicht das
  benutzte L. Benutzt wird L = 36 aus z0-t2.json (pruef-l1.py:438). Gleiches gilt fuer die Kontrolle
  (pruef-l1.py:688). Die Kopfzeile ist irrefuehrend, hat aber keine Wirkung.

## 4. Abweichung 3: Empfindlichkeitskontrollen T1-B, T2-B2

- JSON `.empfindlichkeitskontrolle.ergebnisse`:
  - T1-A und T2-A: delta/4 besteht, delta und 4 delta verfehlen.
  - T1-B und T2-B2: delta/4 und delta bestehen, 4 delta verfehlt.
  - T2-B: alle drei verfehlen (in c, bei 4 delta auch in rho).

  So steht es in den Tabellen BEWEIS-2.md:147-150 und 213-217.
- **Die Einordnung des Textes stimmt.** Nachgerechnet fuer T1-B:
  - z0_rho ist die Mitte der Z-Grenzen: (…682715392199807570527527996 + …682736351217943619340089709) / 2.
    Die Summe der Endziffern ist 51743417751189867617705, die Haelfte 25871708875594933808852,5, also
    z0_rho = 1,690356597328143456827258717...
  - Kr_rho = 1,69035659732814345682727 +- 1,82e-24 (M3.K). Die Mitte liegt 1,128e-23 ueber z0, das sind
    1,128e-23 / 1,048e-22 = 0,108 delta; der Radius ist 0,017 delta. Obergrenze 0,125 delta, Innenabstand
    1 - 0,125 = 0,875. Das ist protokoll.innenabstand_rel_delta.rho = 0,874988.
  - Bei Verschiebung um +delta liegt die Nullstelle bei 0,108 delta im Kasten [z0, z0 + 2 delta], also innen. Die
    Kontrolle setzt voraus, dass Kr um z0 zentriert ist. Diese Voraussetzung faellt weg, wenn der Newton-Abstand
    (etwa 0,1 delta) den Kr-Radius (etwa 0,02 delta) uebertrifft. So steht es in BEWEIS-2.md:152-156 und 312-314.
- **Falsche Zahl (nicht blockierend):** BEWEIS-2.md:154 gibt z0_rho = 1,69035659732814345682725950 an. Richtig ist
  1,69035659732814345682725871(7) aus den Z-Grenzen, siehe oben. Die Abweichung betraegt 7,9e-25, das sind etwa
  0,0075 delta. An der Aussage "etwa 0,10 delta" aendert das nichts.
- **Zusatz:** BRIEF.md:41-42 verlangt als Negativkontrolle nur, dass delta/4 besteht und 4 delta verfehlt. Das
  erfuellen alle Laeufe ausser dem gescheiterten T2-B, auch T1-B und T2-B2. Verfehlt wurde nur die strengere
  Zusatzerwartung des Autors ("delta verfehlt", BEWEIS-2-PLAN.md:37-38, 137). Der Text koennte das deutlicher
  trennen. Fuer B2 ist die Erwartung "delta offen" nur selbst gestempelt, siehe Abschnitt 3.

## 5. Abweichung 4: breiter Teil der l=1-Jacobi-Matrix (etwa 1,6e-3)

Die Daten stammen aus `protokoll.D_relbreite` (rad/|mid|, pruef-l1.py:605) und `export.Mk`.

| Lauf | D-Zeilen 3/4, Spalte a | Spalte om | Zeilen 1/2, Spalte a |
|---|---|---|---|
| T1-A (l=0) | 7,33e-5 / 5,50e-5 | 6,37e-5 / 2,53e-5 | 5,79e-7 / 1,82e-6 |
| T1-B (l=0) | 2,54e-6 / 1,90e-6 | 2,20e-6 / 8,61e-7 | 7,67e-10 / 2,23e-9 |
| T2-A (l=1) | 1,34e-3 / 1,26e-3 | 4,56e-5 / 3,47e-5 | 1,36e-9 / 3,46e-9 |
| T2-B, B2 (l=1) | 1,64e-3 / 1,54e-3 | 5,56e-5 / 4,23e-5 | 4,04e-10 / 1,21e-9 |

(a) **Strenge.** Eine zu breite Huelle von DH_0(Z) macht den Krawczyk-Test nur schwerer. Einen falschen Einschluss
bewirkt sie nicht. Gefaehrlich waere eine zu schmale oder falsch zentrierte Huelle. Die Punkt-Jacobi-Matrix bei z0
(LAUF-t2-zertB-L40.log:13-14, zum Beispiel -0,748703 und 2,65990 in Spalte a) liegt in den Kastenwerten
(:19-20, -0,75 +- 2,53e-3 und 2,66 +- 4,19e-3). Die Kontrolle mit Differenzenquotienten
(LAUF-t2-kontrolle.log:14-17) bestaetigt die Punkt-Jacobi-Matrix relativ bis 7,74e-14. Einen Hinweis auf einen
Einschlussfehler finde ich nicht. Dass die Breite nichts an der Strenge aendert, stimmt.

(b) **Mit dem Scheitern von T2-B hat die Breite nichts zu tun. Das widerspricht dem Text.** Nachrechnung im Kopf mit
den exportierten Werten von T2-B:
- Das M1-Unterproblem (2x2 in a, c; pruef-l1.py:547-560) benutzt nur die Profilzeilen 1 und 2 von D. Es scheitert in
  T2-B ebenfalls, mit Zeilensumme 19,10 (ZERT-T2-B-L40.json .M1.rowsum). Probe:
  7,54e7 * delta_a / delta_c = 7,54e7 * 1,745e-21 / 6,887e-15 = 7,54e7 * 2,534e-7 = 19,1.
  Die c-Zeile scheitert also schon ohne die Zeilen 3 und 4.
- Die c-Zeile von Y im 2x2-Profilblock: D11 = -9,836e16, D12 = -1,0, D21 = -4,628e16, D22 = 0,5205.
  Determinante = -9,836e16 * 0,5205 - (-1)(-4,628e16) = -5,120e16 - 4,628e16 = -9,747e16.
  c-Zeile der Inversen = (-D21, D11) / det = (-0,475, 1,009).
- Radien der Profilzeilen, Spalte a: 4,04e-10 * 9,836e16 = 3,97e7 und 1,21e-9 * 4,628e16 = 5,60e7.
  Ergebnis: 0,475 * 3,97e7 + 1,009 * 5,60e7 = 1,89e7 + 5,65e7 = 7,54e7. Das ist genau |Mk|_{c,a} = 7,54e7 aus
  export.Mk.
- Spalte om: 0,475 * (5,52e-10 * 7,694e16 = 4,25e7) + 1,009 * (1,38e-9 * 3,620e16 = 5,00e7) = 2,02e7 + 5,04e7
  = 7,06e7. Das ist genau |Mk|_{c,om} = 7,07e7.
- Obergrenze fuer den Beitrag der Zeilen 3 und 4: |Mk|_{c,rho} <= 1,96e-6. Die Radien von D in Spalte rho sind
  7,89e-10 * 8,309 = 6,6e-9 und 7,89e-10 * 38,09 = 3,0e-8. Daraus folgt |Y_{c,3}| <= 300 und |Y_{c,4}| <= 65. Der
  Beitrag der Zeilen 3 und 4 zu |Mk|_{c,a} ist damit hoechstens 300 * 1,23e-3 + 65 * 4,1e-3, also etwa 0,6. Das ist
  kleiner als 1e-7 des Gesamtwerts 7,5e7.
- Der Mechanismus ist also der aus l = 0. Bei 320 bit wird delta_c aus |Y H_0(z0)| sehr klein. Die absoluten Breiten
  der Profilzeilen in den Spalten a und om (etwa 4e7 bis 6e7) schrumpfen nicht im gleichen Mass. Dieselbe Rechnung
  erklaert T1-B: 4,85e8 * (1,065e-23 / 1,509e-13) = 0,0342, das ist .M1.rowsum; dazu
  9,19e7 * (8,26e-23 / 1,509e-13) = 0,0503; Summe 0,0845, das ist .M3.rowsum. T1-B lag also schon nahe an derselben
  Grenze.
- Falsch sind deshalb BEWEIS-2.md:200-203 ("Zeilen H_0,3/4 ... Die c-Zeile von Y verstaerkt diese Breiten") und
  STAND.md:24 ("Breite der Zeilen 3, 4 von D relativ 1,6e-3").
- Richtig ist dagegen BEWEIS-2.md:319-320: "stoert den Beweis nicht (Zeilensumme <= 1,9e-3)". In T2-A und B2 legt
  gerade die l = 1-Breite die groesste Zeilensumme fest, und zwar ueber die a-Zeile und nicht ueber die c-Zeile.
  - T2-A: |Mk|_{a,a} + |Mk|_{a,om} * delta_om / delta_a = 7,70e-4 + 6,02e-4 * (2,702 / 2,111)
    = 7,70e-4 + 7,71e-4 = 1,541e-3. Das ist rowsum 1,5401e-3.
  - B2: 9,39e-4 + 7,34e-4 * 1,2785 = 1,877e-3. Das ist rowsum 1,8769e-3.
  - Dass die Profilzeilen hier nicht beitragen, folgt aus |Mk|_{a,rho} = 1,5e-8, woraus |Y_{a,3}| <= 0,9 folgt.
  - Die Breite bestimmt also die Zeilensumme in den bestandenen Laeufen (etwa 1e-3, weit unter 1), das Scheitern
    von B verursacht sie nicht.

(c) **Woher die Breite von 1,3e-3 bis 1,6e-3 in den Zeilen 3 und 4, Spalte a kommt, bleibt offen.** Bei l = 0
schrumpft sie von A nach B um den Faktor 30, bei l = 1 gar nicht. Fuer die Strenge ist das harmlos, siehe (a). Fuer
die Diagnose ist es eine offene Frage. Die Vermutung "Einwickeln nahe r = 0" ist ungeprueft. Moeglich ist auch das
Produkt f * f_a in der a-Quelle, weil f im Kastenlauf bei L relativ 2872 (T2-A) breit ist; siehe
`schritte_kasten.relw_f_bei_L`. Das habe ich nicht entschieden.

## 6. Lemma T0-l1 (Start am Ursprung, A = r^2 alpha)

Mathematik, nachgerechnet:
- **Zentrifugalterm hebt sich weg.** Mit A = r^2 alpha ist A'' = 2 alpha + 4 r alpha' + r^2 alpha''. Daraus folgt
  A'' - (2/r^2) A = r^2 (alpha'' + (4/r) alpha'). Die Gleichung in BEWEIS-2-PLAN.md:71 stimmt.
- **Integralform.** Aus (r^4 y')' = r^4 F folgt y'(r) = r * int_0^1 tau^4 F(tau r) dtau (Masse 1/5). Vertauschen der
  Integrale gibt y(r) = y(0) + (1/3) int_0^r (s - s^4 / r^3) F(s) ds = y(0) + (r^2/3) int_0^1 tau (1 - tau^3)
  F(tau r) dtau. Masse (1/2 - 1/5) / 3 = 1/10. Die Gewichte sind nichtnegativ. Das Mittel liegt deshalb in der
  konvexen Kugel F(B), auch fuer komplexes r auf dem Strahl.
- **Reihe.** Einsetzen von y = sum y_n r^n gibt n (n + 3) y_n = F_{n-2}, also (n + 2)(n + 5) y_{n+2} = F_n und
  y_1 = 0 (aus 1 * 4 * y_1 = 0).
- **Singulaere Exponenten** (fuer W-l1): s (s - 1) = 2 gibt s = 2 und s = -1. W(r^-1, r^2) = 2 + 1 = 3.

Code gegen Plan:
- bewkern_l1.py:283-336 (`lin_series0_l1`): `den = (n+2)(n+5)`, alpha_1 = beta_1 = 0, V_+ = dV - k^2,
  V_- = dV + kc^2, C = 3S^2 - 2S. Jet-Quellen: d_a V = (9S - 4) * 2 f f_a, d_a C = (6S - 2) * 2 f f_a,
  rho-Quellen dPr, dQr konstant, omega-Quellen mit dPw, dQw. Die Gegenkomponente ist jeweils richtig gekreuzt.
- bewkern_l1.py:498-527 (a-priori-Huelle erster Schritt): `Y0 + Dt2*F/10` fuer alpha und beta, `Dt*F/5` fuer alpha'
  und beta'. Dt2 = Kasten +-R^2 enthaelt {r^2 : |r| <= R}. Die Selbstabbildung wird in der Schleife :552-554
  (`contains_all`) geprueft. Das stimmt mit dem Plan (:73-76) ueberein.
- bewkern_l1.py:584-634 (`step`): Cauchy-Rest `q**N/(1-q)` mal die Komponentenmajorante, auch fuer alpha', danach
  `voc_aus_alpha`. Umgerechnet wird die Kugel einschliesslich Rest, als Linearform in (alpha, alpha'), so dass alpha
  nicht doppelt gezaehlt wird. Die Formeln al = alpha (h^2 c - 2 h s / khat) - alpha' h^2 s / khat und
  be = alpha (h^2 s + 2 h c / khat) + alpha' h^2 c / khat habe ich aus A = h^2 alpha, A' = 2 h alpha + h^2 alpha'
  nachgerechnet.
- Anfangszustand :651-657: alpha(0) = 1 fuer R_1, beta(0) = 1 fuer R_2, Ableitungen und Jets 0.
- Die Diff-Zeilenliste bewkern.py gegen bewkern_l1.py stimmt mit BEWEIS-2.md 5.2 ueberein (1-7, 63, 65-66, 177,
  185-192, 283-356, 380, 385-391, 498-528, 597-599, 617-622, 625-628, 633-634, 651-657).

**Urteil T0-l1:** Code und Plan passen zusammen. Rekursion, Huelle und Rest sind richtig. Kein Befund.

Lemma T-l1: P und Q erhalten `cent * (w*w)_n`, die Huelle erhaelt `cent * WD^2` mit WD = 1/(r_j + Dt)
(bewkern_l1.py:185-192, 385-391). `R < r_j` wird vor jedem Schritt mit r_j > 0 streng geprueft, sonst bricht der
Lauf mit Fehler ab (:457-458). Die jq-Pruefung der Schrittprotokolle bestaetigt R < r_j in allen Schritten.
Anmerkung: R < r_j steht nicht im Gesamtflag, wird aber durch den Abbruch erzwungen. "alle R < r_j ... (Gesamtflag)"
in BEWEIS-2.md:177 ist in diesem Punkt ungenau, ohne Folgen.

## 7. Lemmata J-l1, W-l1 (Fernbereich, Jost-Daten, Stetigkeit von E)

Nachgerechnet im Kopf (BEWEIS-2-PLAN.md:87-105):
- **Riccati-Funktionen.** j = sin x / x - cos x und y = -cos x / x - sin x loesen u'' = (2/x^2 - 1) u.
  - W(j, y) = 1; das folgt aus der Asymptotik (-cos, -sin), und W ist konstant.
  - j^2 + y^2 = 1 + 1/x^2.
  - Mit P = 1 - 1/x^2 und Q = 1/x ist j' = P sin + Q cos und y' = -P cos + Q sin. Also
    j'^2 + y'^2 = P^2 + Q^2 = 1 - 1/x^2 + 1/x^4, und das ist <= 1 fuer x >= 1.
- **Geschlossener Kanal.** g = e^u (1 - 1/u) erfuellt g'' = e^u (1 - 1/u + 2/u^2 - 2/u^3) = (1 + 2/u^2) g.
  W_u(d, g) = (1 + 1/u^3) + (1 - 1/u^3) = 2, also W_r = 2 kc.
- **Greensche Funktionen.** G(r, r) = 0 und d_r G(r, s) bei s = r ist -1, fuer G_A und G_B. Daraus folgen
  A'' + (k^2 - 2/r^2) A = Quelle und B'' - (kc^2 + 2/r^2) B = Quelle, mit richtigem Vorzeichen.
- **Majoranten** fuer r, s >= L:
  - |G_A| <= |(j, y)(kr)| * |(j, y)(ks)| <= 1 + 1/(kL)^2 nach Cauchy-Schwarz, daraus a1.
  - K_B ist Differenz zweier Terme in [0, b0], wenn kc L >= 1, also |K_B| <= b0 / (2 kc).
  - K_B' ist Summe zweier Terme gleichen Vorzeichens: (1 + 1/u + 1/u^2) + (1 - 1/u + 1/u^2)(1 + 1/u_s)
    <= 2 + 2/U + 1/U^2, daraus b2 (mit 1/u^2 <= 1/u fuer u >= 1).
  - |d_r G_A| <= 1 * sqrt(1 + 1/(kL)^2) = a2, gebraucht wird kL >= 1.
- **Gronwall.** psi <= b0 + mu int q_J psi gibt int q_J psi <= b0 (e^{mu Q} - 1) / mu = eps.
  q_J <= 6S + 7,5 S^2 und Q <= (6 + 7,5 fs0^2) m^2 e^{-2 kap0 L} / (2 kap0 L^2). Das ist pruef-l1.py:129
  (K.C75 = 15/2).
- **J_0 und Normierung.** e^{kc r} d(kc r) = 1 + 1/(kc r) geht gegen 1. Die Ableitung ist
  -(kc + 1/r + 1/(kc r^2)). Das ist J_0 = (0, j0, 0, -j1), und K_J = b0 + (a1 + b1) eps.
- **Zahlen T2-A** (protokoll.lemma_J):
  - kc = 0,2876862, L = 36, kc L = 10,3567, b0 = 1 + 0,096556 = 1,096556;
    b1 = 1,096556 / 0,575372 = 1,90582; b2 = (2 + 0,193112 + 0,009323) / 2 = 1,101218.
  - k = 2,502560, k L = 90,09, a1 = 1,000123 / 2,50256 = 0,399640.
  - eps = 2,4177e-16. a1 eps = 9,662e-17 = E_A; b1 eps = 4,608e-16 = E_B; b2 eps = 2,662e-16 = E_B'.
  - Alle Werte stimmen.

Code (pruef-l1.py):
- :74-80: H_0,3/4 = s3 (j0 B_i' + j1 B_i). Das ist W(J_0, R_i) mit W(u, v) = <u, v'> - <u', v> und J_0 =
  (0, j0, 0, -j1).
- :87-99: DH-Zeilen 3 und 4. dj0/dkc = -1/(kc^2 L), dj1/dkc = 1 - 1/(kc L)^2, dkc/drho = (om - rho)/kc,
  dkc/dom = -(om - rho)/kc. Alle stimmen. s3 ist konstant.
- :130-141: Konstanten wie oben; mu nimmt obere Schranken; okJ ist kL >= 1 und kc L >= 1 in Kugelarithmetik ueber Zb.
- :143-150: Schranke eps_3/4 = s3 (E_A |A'| + E_B |B'| + E_A' |A| + E_B' |B|). Sie gilt mit dem Kastenzustand bei L.
  A und A' kommen aus der VOC-Darstellung zurueck, A = al cos + be sin und A' = khat (-al sin + be cos). Das passt
  zur Umrechnung in voc_aus_alpha.

**W-l1** (Plan :107-112): W(S_i, R_j) = delta_ij und W(R_i, R_j) = 0 als Grenzwert r -> 0. Nachgerechnet:
r^-1 * 2r + r^-2 * r^2 = 3, und die Log-Terme der Ordnung r^3 tragen im Grenzwert nicht bei. W(Psi_n, R_j) = 0 fuer
j = 1, 2 heisst dann, dass Psi keinen singulaeren Anteil hat. Die Folgerung H(z*) = 0 => regulaer braucht s3 != 0.
s3 ist eine positive Exponentialzahl, das ist erfuellt.

**Stetigkeit von E auf Z.** Der Plan sagt nur "Stetigkeit wie Zusatz S" (:105). Die Kerne haengen stetig von
(k, kc, r, s) ab. Die Majoranten a1, b1 und q_J gelten gleichmaessig auf Z, weil kL >= 1 und kc L >= 1 ueber Zb
geprueft sind. Die Konvergenz der Neumann-Reihe ist gleichmaessig, also ist die Jost-Loesung bei L stetig in z.
Das Argument aus BEWEIS-1 (Fremdlesung Punkt 2) traegt deshalb auch hier. Ausgeschrieben ist es fuer l = 1 nicht;
das ist nicht blockierend.

**Frei-Test l = 1** (LAUF-t2-frei.log:11-16): relative Abweichungen der Mittelpunkte <= 4,22e-37, B_1 und A_2
enthalten 0. Das passt zu BEWEIS-2.md:162. Der Test prueft die Umsetzung (Zentrifugalterm, Start, Umrechnung) und
nicht die Lemmata.

**Urteil J-l1 und W-l1:** Vorzeichen, Majoranten auf ganz Z, Jost-Daten und Normierung stimmen. Kein
blockierender Befund.

## 8. Lemma E-l1, "einfach", "eingebettet" (Wortlaut nach OpenAI-Auflagen)

- **Argument (BEWEIS-2-PLAN.md:114-125), im Kopf nachvollzogen.** Die zwei Loesungen Psi_c und Psi_s ~ (j(kr), 0)
  und (y(kr), 0) werden von aussen konstruiert. Ihre geschlossene Komponente ist int G_B C A. Sie konvergiert und
  faellt ab, weil int_r^oo e^{kc (s - r)} e^{-2 kappa0 s} ds endlich ist genau dann, wenn 2 kappa0 > kc. Die
  Auflage steht damit an der richtigen Stelle.
  - W(Psi_c, Psi_s) = k * W_x(j, y) = k != 0.
  - Fuer eine L^2-Loesung Phi verschwinden W(Phi, Psi_c), W(Phi, Psi_s) und W(Phi, J). Grund: j, y und ihre
    Ableitungen sind fuer x >= kL >= 1 beschraenkt.
  - Mit der nichtausgearteten Form W bleibt ein hoechstens eindimensionaler Rest, und der ist span{J}.
  - Die Voraussetzungen 2 kappa0 > kc und kL >= 1 stehen im Gesamtflag von T2-A und T2-B2.
  - Tragfaehig.
- **Kanalungleichungen aus dem Kasten.** Die Werte stehen in protokoll.kanaele, als Untergrenzen in
  Kugelarithmetik ueber Z; im Kopf gegengerechnet:
  - T2: omega + rho = 2,694959; das Quadrat minus 1 ist 6,262806, also k^2 >= 6,262805.
    rho - omega = 0,957725; 1 - 0,917237 = 0,082763, also kc^2 >= 0,082763.
    2 kappa0 - kc = 2 * 0,495484 - 0,287686 = 0,703281, also >= 0,703280.
  - T1: 2,518082^2 - 1 = 5,340735. 1 - 0,862631^2 = 0,255867. 2 * 0,561134 - 0,505833 = 0,616435.
  - Alle stimmen mit BEWEIS-2.md:134-135 und 186-187 ueberein.
- **Wortlaut.** Er folgt den Auflagen 5 und 6 von GESAMT-REVIEW.txt:
  - "Einfachheit (geometrisch)" meint den Raum der L^2-Loesungen auf [L, oo) bei festen (rho*, omega*) mit
    Dimension 1, ohne algebraische Vielfachheit und ohne Stabilitaet (BEWEIS-2.md:47-48, 77-79). Die m-Entartung
    wird genannt.
  - "Eingebettet im operationalen Sinn" (:50-51, :81-84) wird gestuetzt durch den offenen Kanal und die
    lokalisierte Loesung.
  - "periodisch oder quasiperiodisch" (:84).
  - Kein Wort zum wesentlichen Spektrum des vollen Bueschels (:55, :307-308).
- **Kleinigkeit (nicht blockierend):** Die Lemmatabelle BEWEIS-2.md:291 schreibt "BIC = regulaer bei 0". Die
  Abkuerzung BIC steht fuer die staerkere spektrale Lesart. In einem Satz, der sich auf den operationalen Sinn
  beschraenkt, waere "Nullstelle von H = regulaer bei 0" sauberer. Dasselbe gilt fuer BEWEIS-2-PLAN.md:112.
- **Translationsmode:** Die Begruendung ist richtig und reicht aus. Die Translationsmode loest die Gleichung nur bei
  rho = 0, E-l1 ist eine Aussage bei festem rho* = 1,826.

## 9. Gesamtflag (Auflage 1) und Export (Auflage 4)

**Gesamtflag M3.BESTANDEN**
- T2-A und T2-B2 (pruef-l1.py:530-543), laut JSON alles true:
  - Kanalbedingungen: k2>0, kapc2>0, om>1/sqrt2, om<1.
  - `einfachheit_2kap0>kapc`, `krein_rho>om`, `pos_4-6kap0^2>0`.
  - `lemmaJ_l1_kL>=1_kcL>=1` und `schritte_0<h<R` (ueber infp + infZ), `N>=1_qfac>1`.
  - Dazu Krawczyk_in_Z (strikt, Zeilensumme < 1), Lemma_P_ok (i-iv) und positiv.klein_danach.

  Damit ist die Frage der Leitung beantwortet: 2 kappa0 > kappa_c, rho > omega, kappa_c L >= 1 und 0 < h < R stehen
  alle im Flag. **Erfuellt.**
- T1-A und T1-B (pruef-l0.py, Fassung 7713f636): Im Flag stehen 2 kappa0 > kappa_c, rho > omega und
  4 - 6 kappa0^2 > 0.
  - Nicht im Flag stehen 0 < h < R, N >= 1 und qfac > 1; sie kamen erst um 12:28 in pruef-l1. Der Autor hat sie
    nachtraeglich per jq geprueft (STAND.md:21), ich ebenfalls (Abschnitt 1): kein Verstoss.
  - kappa_c L >= 1 braucht Lemma J fuer l = 0 nicht. Bei T1 ist kc L = 0,5058 * 32 = 16,2.
  - Die Fremdlesung hat das nur als "defensiv kuenftig" verlangt, nicht blockierend.
  - Der Satz BEWEIS-2.md:93-94 "Alle Voraussetzungen ... stehen im Gesamtflag M3.BESTANDEN" ist fuer T1 in diesem
    Punkt zu weit: 0 < h < R ist fuer T1 nicht im Flag, sondern nachtraeglich geprueft. Nicht blockierend.

**Export (Auflage 4).** In allen fuenf ZERT-JSON:
- `export` enthaelt Y (4x4, exakt dyadisch), DH0_Z und Mk (Mitte und Radius exakt als Mantisse und Exponent), H0_z0,
  eps_obere, delta und Kr.
- `protokoll.lemma_P_untergrenzen` enthaelt phibar_unten und eta_unten.
- Stichprobe: export.Mk[1][0].radius von T2-B ist 603148081 * 2^-3 = 75393510, also 7,54e7. Das passt zu Abschnitt 5.
- **Erfuellt.**
- Hinweis: Die `text`-Felder schreiben die Mitte nur so genau, wie sie gesichert ist, und schlagen den Rundungsfehler
  dem Radius zu. Beispiel: DH0_Z[2][0] von T2-A lautet "-0,75 +- 2,31e-3", der echte Radius ist etwa 1,0e-3
  (D_relbreite 1,34e-3). Massgeblich sind mitte_m_e und radius_m_e; das Feld `hinweis` sagt das.

## 10. Zahlen vorwaerts und rueckwaerts (Text gegen JSON)

**Vorwaerts (Text gegen JSON und Logs), per jq gelesen und im Kopf verglichen.**
- Kastentabellen T1 (BEWEIS-2.md:35-38) und T2 (:64-67) gegen protokoll.Z: alle 16 Grenzen nach aussen gerundet.
  15 Grenzen sind knapp gerundet. Die obere rho-Grenze von T1 ist eine Einheit zu grosszuegig: aus
  ...846998027|298 wird im Text ...029, knapp waere ...028. Das ist weiterhin nach aussen gerundet, also harmlos.
- Kastenradien delta, geprueft als halbe Differenz der Tabellengrenzen:
  - T1-A: 8157325e-27 / 2 = 4,08e-21; 1,685e-5 / 2 = 8,43e-6; 3,948e-20 / 2 = 1,97e-20; 2,723e-20 / 2 = 1,36e-20.
  - T2-A: 2,11e-20; 2,74e-7; 5,46e-20; 2,70e-20.
  - Alle stimmen mit :128, :181 und `.delta` ueberein.
- Satz-Modus (LAUF-t1-satzA.log, LAUF-t2-satzA.log):
  - T1: om^2 +- 2,47e-20 wird zu 2,5e-20, rho +- 4,70e-20.
  - T2: om^2 +- 7,78e-20; rho +- 2,97e-19 wird zu 3,0e-19.
  - Einschluss geprueft, zum Beispiel T2-rho: Kasten [...956187,6; ...956296,8] liegt in [...955700; ...956300]
    (Einheit 1e-21).
- Tabellen 4.2 und 4.5 wie geprueft: H_0(z0), eps_1..4, Lemma P (i)-(iv) mit den Untergrenzen, Lemma J bzw. J-l1
  (a1, a2, b0, b1, b2, mu, Q, eps, E_A..E_B', K_J), Kanaele, erster Schritt, groesster Rest, Fehlversuche,
  Innenabstand, Zeilensummen gewichtet und ungewichtet, M1, L_p und Schwelle. Alle stimmen mit dem JSON ueberein.
- Die Zeilen fuer B und B2 (:141-143, :193-195) stimmen: delta, eps, K_J - 1 bzw. K_J, Zeilensumme, Innenabstand,
  L_p, Schritte.
- Laufzeiten (4.1, 4.4) gegen "Service runtime": 68,4; 97,0; 410,5; 63,7; 96,5; 96,0; 3,4; 79,2 s. Stimmen bis auf
  0,1 s.
- Vorab-Bereiche:
  - T1: 0,685128904458 liegt in 0,68512891 +- 1e-7.
  - T2: 0,7544960138 liegt in 0,7544961 +- 3e-7; rho 1,826342030 liegt in 1,826342 +- 1e-5.
  - Abstand zu A_out (T2): 0,7544960184 - 0,7544960138 = 4,6e-9, wie STAND.md:20.
- khat: T1 2540974827025 / 2^40 = 2,31100; T2 2751593698811 / 2^40 = 2,502560. Beide stimmen mit k.
- Codezeilen-Tabellen 5.1-5.3 gegen `diff`: alle Hunks genannt. Bei 5.3 "256-261, 270-290" schliesst der Text die
  unveraenderten Zeilen 260 und 278 mit ein; das ist unerheblich.
- **Falsch:** z0_rho in BEWEIS-2.md:154 (Abschnitt 4). Die Ursache des Fehlschlags von B in :200-203 und
  STAND.md:24 (Abschnitt 5).
- **Ungenau:** "in der a- und omega-Spalte relative Breiten bis 1,6e-3" (:200). Die om-Spalte der Zeilen 3 und 4
  hat relativ nur 5,6e-5; absolut ist sie etwa gleich breit (3,1e-3 bis 7,3e-3).

**Rueckwaerts (jede Datei auf Fehler, false und Warnungen).**
- `paths(. == false)` in allen ZERT-JSON: T1-A, T2-A (delta und 4 delta), T1-B, T2-B2 (4 delta) liefern nur die
  Empfindlichkeitskontrolle, wie beschrieben.
- T2-B liefert zusaetzlich M3.Krawczyk_in_Z, M3.BESTANDEN und **M1.BESTANDEN = false**. M1 (Zeilensumme 19,10) nennt
  BEWEIS-2.md nicht, nur STAND.md:24. Das ist der direkte Beleg gegen die Ursachenangabe im Text.
- Logs: keine Traceback-, Fehler- oder Warnzeilen. "NICHT" steht nur in LAUF-t2-zertB-L40.log:24, 29-30 (bekannt).
  Alle Laeufe enden mit rc=0.
- Nicht im Text, fuer die Strenge ohne Belang:
  - Im Kastenlauf ist f bei L relativ sehr breit (relw_f_bei_L: T1-A 26282, T2-A 2872, B2 14558), der
    Kastenzustand Y bei L bis 55 (Protokoll `schritte_kasten`).
  - Die Inflationsrunden gehen bis 13 bei maxit = 14 (bewkern_l1.py:448), knapp am Limit.
  - M2 von T1-B, T2-B und B2 enthaelt 0 nicht. M2 ist aber nur eine Auswertung F(z0), kein Test
    (pruef-l1.py:563-570).

## 11. Befunde (nummeriert, blockierend / nicht blockierend)

Einen blockierenden Befund habe ich nicht gefunden.

| Nr | Befund | Fundstelle | Art | betrifft |
|---|---|---|---|---|
| F1 | Die Ursache des Fehlschlags von T2-B ist falsch angegeben. Die c-Zeile von I - YD (7,54e7 und 7,07e7) entsteht vollstaendig aus den Profilzeilen 1 und 2 (Spalten a und om, Radien 4e7 bis 6e7) mal der c-Zeile von Y, die von der Groessenordnung 1 ist. Die l = 1-Zeilen 3 und 4 tragen hoechstens etwa 0,6 bei. Beleg: M1, das 2x2-Profilproblem, scheitert ebenso mit 19,10. Die Abhilfe B2 bleibt gueltig. | BEWEIS-2.md:200-203; STAND.md:24; ZERT-T2-B-L40.json .M1, .export.Mk | nicht blockierend (Text) | T2 |
| F2 | BEWEIS-2.md verschweigt, dass in T2-B auch M1 scheiterte (M1.BESTANDEN = false, Zeilensumme 19,10). | BEWEIS-2.md:166, 197-208 | nicht blockierend (Text, rueckwaerts) | T2 |
| F3 | Die Vorab-Stempel (12:11:22, 12:22:22, 12:36:54) lassen sich per mtime nicht belegen. Plan und STAND haben mtimes 12:40:52 und 12:44:06, nach allen Ergebnisdateien. Das verfehlt die Pflicht aus BRIEF.md:37; der Autor meldet es selbst. Die Zuordnung Lauf zu Code ist durch die sha256 im JSON belegt. | BEWEIS-2-PLAN.md mtime; BEWEIS-2.md:219-230; BRIEF.md:37 | nicht blockierend (Prozess) | T1, T2 |
| F4 | Die Zeilenliste stand vor den Beweislaeufen nicht vollstaendig im Plan: Auflagen-Aenderungen vor T1-A, Zeilennummern T2, 0 < h < R, --dcexp. Alle diese Aenderungen fuegen nur Pruefungen, Exporte oder die Kastenwahl hinzu und lockern kein Tor. | BEWEIS-2-PLAN.md:150-175 | nicht blockierend (Prozess, gemeldet) | T1, T2 |
| F5 | B2 wurde nicht vorab festgelegt. Die Abhilfe (Kastenradius) steht nicht in der vorab erlaubten Liste (L, N, q, Bitzahl), die fuer T1-A formuliert war. Damit ist die BRIEF-Forderung "zwei Zertifizierungen je Ziel" fuer T2 nur nachtraeglich erfuellt. T2 stuetzt sich allein auf T2-A; das haelt der Text richtig fest. | BEWEIS-2-PLAN.md:31; BEWEIS-2.md:309-311; BRIEF.md:50 | nicht blockierend (Status) | T2 |
| F6 | z0_rho ist falsch abgeschrieben: 1,69035659732814345682725950 statt 1,690356597328143456827258717. Die Differenz betraegt 7,9e-25, also 0,0075 delta. Die Aussage "0,10 delta" bleibt richtig (0,108). | BEWEIS-2.md:154 | nicht blockierend (Zahl) | T1 |
| F7 | "Alle Voraussetzungen ... im Gesamtflag" stimmt fuer T1 nicht ganz: 0 < h < R, N >= 1 und qfac > 1 fehlen im T1-Flag und wurden nachtraeglich per jq geprueft (von mir bestaetigt). R < r_j steht in keinem Flag, wird aber durch den Abbruch erzwungen. | BEWEIS-2.md:93-94, 177 | nicht blockierend (Text) | T1, T2 |
| F8 | Die kastenunabhaengige relative Breite 1,3e-3 bis 1,6e-3 (D-Zeilen 3 und 4, Spalte a) ist nicht aufgeklaert. Sie ist fuer die Strenge harmlos: zu breit, aber richtig zentriert, und die Punkt-Jacobi-Matrix liegt darin. In A und B2 bestimmt sie die groesste Zeilensumme (1,54e-3 und 1,88e-3). Bei laengerem L oder hoeherem l kann sie begrenzen. | BEWEIS-2.md:208-209, 319-320; protokoll.D_relbreite | nicht blockierend (Diagnose) | T2 |
| F9 | Kleinigkeiten im Wortlaut. "BIC = regulaer bei 0" deutet eine staerkere spektrale Lesart an. "a- und omega-Spalte ... bis 1,6e-3" stimmt nur fuer Spalte a; relativ hat om 5,6e-5. Die obere rho-Grenze in der T1-Tabelle ist eine Einheit zu grosszuegig, das ist harmlos. Die Logkopfzeile "L 40" steht bei T2-A und in der Kontrolle. | BEWEIS-2.md:291, 200, 37; BEWEIS-2-PLAN.md:112; LAUF-t2-zertA-L36.log:3 | nicht blockierend | T1, T2 |

**Auflagen** (Anforderungen, keinen Wortlaut schreibe ich vor):
- **A1 (T2, zu F1, F2):** Die Ursachenangabe in BEWEIS-2.md 4.5 berichtigen, den M1-Fehlschlag nennen und die
  l = 1-Breite nur der Zeilensumme der a- und om-Zeile in A und B2 zuordnen. STAND.md mit einer neuen Zeile
  berichtigen, die alte Zeile stehen lassen.
- **A2 (T1, zu F6):** z0_rho in BEWEIS-2.md:154 aus den Z-Grenzen neu uebertragen.
- **A3 (T1, T2, zu F7):** Den Satz zum Gesamtflag fuer T1 praezisieren (nachtraegliche Pruefung von 0 < h < R) und
  festhalten, dass R < r_j durch Abbruch erzwungen wird.
- **A4 (Prozess, zu F3, F4, fuer kuenftige Beweise):** Den Planstand vor jedem Beweislauf nachpruefbar einfrieren,
  zum Beispiel mit sha256 des Plans in einer STAND-Zeile vor dem Lauf oder einer gestempelten Kopie. So wird
  "vor der Ergebnisdatei" per mtime oder Hash pruefbar.
- **A5 (T2, zu F8, vor weiteren Laeufen mit l >= 1 oder groesserem L):** Die Herkunft der Breite klaeren, zum
  Beispiel mit einem Kastenlauf mit kleinerem delta_a oder mit Breiten je Schritt. Den Satz T2 beruehrt das nicht.
- **A6 (Text, zu F9):** optional.

## 12. Nicht geprueft

- Keine Nachrechnung von H_0, DH_0, Y, Kr oder der ODE-Einschluesse; lokal durfte ich nicht rechnen. Die Strenge
  beruht weiter auf python-flint 0.9.0 / FLINT und darauf, dass die JSON-Dateien echt sind. Ein zweites,
  unabhaengiges Programm fehlt (BEWEIS-2.md:302-304).
- Die Herkunft der Breite aus F8 und ob sie mit groesserem L waechst (bei 2 Laeufen nur 1,34e-3 zu 1,64e-3).
- Die Newton-Vorfassungen b3c42c59 und 6ca5c2d9 liegen nicht bei; "nur zert() verschieden" ist nicht pruefbar. Fuer
  die Strenge ist das ohne Belang.
- Die Vorab-Zeitstempel: nur Selbststempel, siehe F3.
- pruef-l0.py gegen pruef-v2.py: gelesen habe ich die Hunk-Liste und die Hunks zu Flag und sha256; die Export- und
  Argparse-Hunks nur ueberflogen.
- Die Kernfunktionen aus BEWEIS-1 (Profil, lin_Mp_series, lin_recursion, Lemma Pos, Lemma P): nicht neu gelesen,
  weil bytegleich bzw. nur um par.l ergaenzt und schon zweimal gegengelesen.
- Die Punktlauf-Tails von T2-B2 gegen T2-B: nur Bitgleichheit der Schrittdateien geprueft.
- Den Ordner eines parallelen Pruefers habe ich nicht geoeffnet; in beweis2/ gab es keinen.
