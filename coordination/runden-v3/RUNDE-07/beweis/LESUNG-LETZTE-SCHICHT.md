# LESUNG-LETZTE-SCHICHT: Frische Lesung der letzten Schicht (BEWEIS-1, M4, nach Einarbeitung der Code-Lesung)

- Leser: frischer Leser (Claude, Haus Anthropic), kein Autor, nicht an Beweis, Plan-Lesung oder Code-Lesung beteiligt.
  Keine Rechnung, keine Aenderung fremder Dateien.
- Beginn 2026-09-30 08:21:54 CEST (date). Ende: letzte Zeile (date).
- Gelesen (ganz): BEWEIS.md, LESUNG-CODE.md, STAND.md, zertifikat/ZERT-A2-L40.json, ZERT-B2-L44.json, z0.json,
  SHA256SUMS.txt, LAUF-zertA2-L40.log, LAUF-zertB2-L44.log, LAUF-satzA2.log, LAUF-satzB2.log, LAUF-kontr2.log,
  diff pruef.py/pruef-v2.py (vollstaendig), pruef-v2.py 205-320 (main), 374-600 (positivity, zert, Protokoll),
  bewkern.py 540-598 (integrate). In Auszuegen: BEWEIS-PLAN.md 6, 7, 9; LESUNG-PLAN.md K6; ZERT-A-L40.json,
  ZERT-B-L44.json (jq-Vergleich); Schrittprotokolle nur mit jq.
- Werkzeuge: Read, sed, grep, jq, diff, cmp, sha256sum, date. Kein python, kein awk, kein git, kein Journal,
  kein Zugriff auf die .69.

## Urteil: LETZTE SCHICHT TRAEGT

Alle neun Befunde der Code-Lesung (W1, K1-K8) sind an der genannten Stelle eingearbeitet und erledigt; die drei
Zusatzbefunde des Autors ebenso. Jede Zahl in Satz, Abschnitt 2, 3.1, 3.2, 3.3 und 4 stimmt mit ZERT-A2/B2 bzw. den
Logs ueberein, und jede Schranke ist in die richtige Richtung gerundet (eine Ausnahme in der Darstellung, L2, ohne
Folge). bewkern.py ist per Hash unveraendert; der Treiber aendert an der Mathematik nichts und an zwei
Pruefbedingungen nur die Art, wie die geprueften Zahlen gebildet werden (strenger, Werte gleich). sha256sum -c: 38
von 38 in Ordnung. Alte und neue Zertifikate stimmen in allen Zahlen ueberein, die Kasten-Schrittprotokolle sind
bitgleich. Der Satz behauptet nichts, was die Zertifikate nicht decken; die offenen Punkte stehen ehrlich da.
Sechs kleine Befunde (L1-L6) betreffen Wortlaut und Protokoll, keiner eine Zahl des Beweises. Sie sind keine
Auflagen; werden sie eingearbeitet, genuegt eine kurze frische Lesung der geaenderten Zeilen.

## 1. Befunde der Code-Lesung gegen die Einarbeitung (BEWEIS.md Abschnitt 7)

| Befund | Anforderung der Lesung | Steht es da? Erledigt? | Beleg |
|---|---|---|---|
| W1 erster Schritt | 3.2 und PLAN 6: Startversuch R0 = 1, sieben Verkleinerungen, R = 13/64, h0 = 13/128, q = 1/2, Ordnung 2N, Inflationsrunden, Rest | Ja. BEWEIS.md 3.2 Zeile "erster Schritt" nennt alles, getrennt nach Punkt (Runden 4, Rest <= 4,9e-39) und Kasten (Runden 10, Rest <= 1,1e-27); BEWEIS-PLAN.md 306-307 berichtigt | ZERT-A2 protokoll.erster_schritt_punkt/kasten: R_angenommen 13/64, h0 13/128, q 1/2, versuchsfolge_R 1, 51/64, 163/256, 65/128, 13/32, 83/256, 33/128, 13/64, verkleinerungen 7, folge_trifft_R_angenommen true, inflationsrunden 4 bzw. 10, rest 4,84346e-39 bzw. 1,07265e-27; B2: 7,39053e-44 bzw. 2,74598e-25. Schrittprotokolle Schritt 0: R 0,203125, h 0,1015625, r_ende 13/128. Schleifenlogik bewkern.py 551-560 (R -> dyf(4/5 R, 8), erster Erfolg wird angenommen): 13/64 ist das achte Glied, also genau sieben Fehlschlaege. Siehe aber L1. |
| K1 Rundung | kappa_c^2 >= 0,274964; (1 + omega) - rho >= 0,148509; 2 omega^2 - 1 >= 0,595353; Regel im Text | Ja, Tabelle 3.2 und Regel im Tabellenkopf; eigene Berichtigungen des Autors (c - eta 7,5182518; Obergrenzen; D-Breite 1,92e-9; Innenabstand 0,87499) stimmen alle (Abschnitt 2 dieser Lesung) | protokoll.kanaele: 0,274964756794439; 0,148509986432; 0,595353574224; lemma_P (iv) 7,5182518877086526499 |
| K2 K_J | lemma_J mit 20 Stellen oder Logzeile als Quelle | Ja, beides: lemma_J str(20), neues Feld K_J_minus_1_obere_schranke, Satz 2 zitiert das Feld | protokoll.lemma_J.K_J "[1.0000000000000000757 +/- 1.63e-20]"; K_J_minus_1_obere_schranke "[7.568377185e-17 +/- 4.67e-28]" -> Satz "K_J <= 1 + 7,57e-17" aufgerundet |
| K3 Selbstbeschreibung | Laufparameter und sha256 von bewkern.py, pruef.py im JSON | Ja, Neulauf. Feld parameter (L, Lz, N_punkt, N_kasten, N0, q, Rmax, rfrac, R0, kfak, prec, z_datei, kommandozeile) und Feld sha256 (bewkern.py, pruef.py, z0.json, Interpreter, vier Bibliotheken) | pruef-v2.py 401-414; ZERT-A2/B2. Zusatz: die zur Laufzeit auf der .69 gelesenen Hashes von bewkern.py, pruef.py, z0.json sind gleich den lokalen Dateien bewkern.py, pruef-v2.py, z0.json (sha256sum lokal). Damit ist der Lauf an den lokalen Code gebunden, was die Code-Lesung noch nicht pruefen konnte. |
| K4 volle Hashes | Interpreter, libflint, libgmp, libmpfr voll | Ja, BEWEIS.md 4 und JSON; alle fuenf Zeichenketten in BEWEIS.md kommen exakt in A2 und B2 vor (grep) | BEWEIS.md 200-205; ZERT-A2/B2 sha256 |
| K5 Python-max | max ueber .upper() oder Vermerk | Ja, Funktion zeilenschranke (pruef-v2.py 330-343): je Zeile exakte obere Schranke (upper), Maximum ueber exakte Zahlen; benutzt fuer rowsum (469), rs2 (499), rs_unw (543); Vermerk in BEWEIS.md 4 | M3.rowsum alt = neu "[5.6812630e-9 +/- 2.84e-17]"; M1.rowsum gleich |
| K6 T1 getrennt | Mittelpunktsdifferenz und Radiensumme getrennt, Eingangsradien | Ja, LAUF-kontr2.log: M 4,32e-78 / 4,73e-10; Mp 3,45e-77 / 6,11e-9; g', Y', Jets 0 / 2,52e-10, 2,05e-9, 5,37e-8; Eingangsradien bei r = 3 ausgegeben. BEWEIS.md 3.1 gibt <= 3,5e-77 und <= 5,4e-8 (aufgerundet) | pruef-v2.py 643-664 |
| K7 Wortlaut | Ergebnis und Luecke 1 nennen die Code-Lesung; fremdes Haus und zweites Programm fehlen weiterhin | Ja, woertlich so in Ergebnis und 5.1; auch BEWEIS-PLAN.md 7.1 | BEWEIS.md 17-19, 234-236 |
| K8 Empfindlichkeit | delta/4 und delta zusaetzlich, Erwartung vorab | Ja, drei Verschiebungen, Erwartung im Code (pruef-v2.py 512-515) und im JSON (erwartung_vorab); Ausgang wie erwartet in A2 und B2; im Text als Empfindlichkeit, nicht Strenge benannt | empfindlichkeitskontrolle.ergebnisse: 1/4 [T,T,T,T] besteht; 1/1 und 4/1 [T,T,F,T] verfehlen; nicht Teil des BESTANDEN-Flags (M3 wird vorher gebildet, 484-485) |
| Notiert: Huelle je Schritt | - | Feld einschlusstest als Text; Huellen weiterhin nicht gespeichert, im Text so gesagt | protokoll.einschlusstest |
| Notiert: L_p Lauf B | - | Ja, 3.2: 7,3560791015625 | ZERT-B2 M3.positiv.Lp |
| Notiert: consts() | - | unveraendert, ohne Wirkung; im Text gesagt | - |

## 2. Zahlen in beide Richtungen

Vorwaerts (jede Zahl in BEWEIS.md gegen ZERT-A2-L40.json, ZERT-B2-L44.json, LAUF-satzA2.log, LAUF-satzB2.log,
LAUF-kontr2.log, LAUF-zertA2/B2.log); Rundungsrichtung mit dem vollen JSON-Wert verglichen.

Satz (Abschnitt 1):
- Tabelle Z, acht Grenzen gegen protokoll.Z (45 Stellen): a unten ...903719568|08 -> 903719568 (ab), a oben
  ...903976114|46 -> 903976115 (auf), c unten 7,518251887708654655|97 -> ...655 (ab), c oben 7,518253935068731843|88
  -> ...844 (auf), rho unten ...780754587|26 -> ...587 (ab), rho oben ...781671830|65 -> ...831 (auf), omega unten
  ...073897354|79 -> ...354 (ab), omega oben ...074377801|99 -> ...802 (auf). Alle acht richtig gerundet; A2 und A haben
  dasselbe protokoll.Z (jq gleich), wie im Text gesagt.
- omega^2 +- 4,8e-22 (Log 4,74e-22), rho +- 6,8e-22 (6,72e-22), kappa0 +- 1,4e-21 (1,36e-21), kappa_c +- 5,5e-21
  (5,45e-21): aufgerundet, richtig. k^2 >= 5,9576 (5,95769908652711 - 4,87e-15), kappa_c^2 >= 0,27496, Abstaende
  >= 1,6377 (1,63774507611) und >= 0,14850 (0,148509986432): abgerundet, richtig. K_J <= 1 + 7,57e-17: richtig.
- Lauf B2: rho +- 3,9e-25 (Log 3,84e-25), omega^2 +- 6,5e-25 (6,41e-25), a +- 4,1e-25 (4,06e-25): richtig. Der
  satz-Modus liest delta aus dem JSON als Kugel und nimmt .upper(), also eine Obermenge von Z (pruef-v2.py 305-308):
  konservativ.
Abschnitt 2: Innenabstand >= 0,87499 delta (innenabstand_rel_delta 0,875000 +- 7,33e-9, also >= 0,87499999),
gewichtete Zeilensumme <= 5,7e-9 (5,68126297e-9), ungewichtet <= 27253 (27252,939), f > 0 auf [0; 7,0475] (L_p =
7,04754638671875 = 115467/16384, Ende des letzten Schritts mit f_unten > 0: r_j 6,9232788, f_unten 0,0222246;
erster Schritt mit f_unten <= 0 bei r_j = 7,04754638671875, f_unten -0,00349034): richtig. Zu "|f| < 0,33208949"
siehe L2.
Abschnitt 3.1: Laufzeiten 113,1 s (Service runtime 1min 53,133s), 123,2 s (2min 3,203s), 95,9 s (1min 35,913s),
3,8 s (3,753s), 297 s: richtig. kontr2-Zahlen: richtig (siehe K6). Empfindlichkeitskontrolle: richtig.
Zur Erklaerung der hoeheren Laufzeit siehe L4.
Abschnitt 3.2 (alle Zeilen): khat, s1, s3 gleich JSON; Schritte 324/328; R in [49/4096; 3583/4096] =
[0,011962890625; 0,874755859375] und h in [0,00396728515625; 0,29156494140625] gleich JSON und per jq aus dem
Punkt-Schrittprotokoll bestaetigt (auch: kein Schritt mit R >= r_j bei r_j > 0, Fehlversuche 184, Inflationsrunden
max 13); erster Schritt siehe W1; Schrittreste Punkt <= 3,5e-30 (3,445e-30 + 3,35e-34), Kasten <= 7,8e-13
(7,741e-13); H_0(z0) 1,3e-7 (1,28e-7), 6,1e-8 (6,09e-8), 9,9e-26 (9,90e-26), 3,8e-25 (3,71e-25): aufgerundet;
delta mit "~" gegen delta[]: richtig; eps_1..4 <= 1,5467e-16 (1,54660747e-16), 1,4301e-16 (1,43000417e-16),
2,3122e-26 (2,31210111e-26), 2,3101e-26 (2,31006719e-26): aufgerundet; Lemma P (i) f* <= 2,8852e-9 (2,88515673e-9,
auf) < 2,9140e-9 <= phibar (2,91400830e-9, ab); (ii) 1,5467e-16 (Km3 1,54660747e-16, auf) < 3,0932e-16 <= eta
(3,09321493e-16, ab); (iii) 6,172e-17 (6,17140953e-17, auf); (iv) 7,5182518 (7,51825188770865, ab); K <= 3,640e-19
(3,63939448e-19, auf), m <= 7,518254 (7,51825393507, auf); Lemma J Q 5,552e-17 (5,55184355e-17), mu 0,95353
(0,95352369), eps 5,294e-17 (5,29381436e-17), E_A 2,275e-17 (2,27456283e-17), E_B 5,294e-17, E_A' 6,872e-17
(6,87122953e-17), E_B' 8,328e-17 (8,32776533e-17): alle aufgerundet; Kanaele 5,957699, 0,274964, 1,637745, 0,148509
und 2 kappa0 - kappa_c >= 0,375236 (0,375236234040), 2 omega^2 - 1 >= 0,595353 (0,595353574224): alle abgerundet;
Krawczyk 0,87499, 5,6813e-9 (5,68126297e-9, auf), 27253: richtig; D-Breite <= 1,92e-9 (groesster Eintrag 1,91e-9 +
1,73e-12 = 1,9117e-9, auf): richtig; M1 a +- 2,2e-22 (2,17e-22), c +- 2,2e-7 (2,17e-7), Zeilensumme 1,8e-12
(1,7603489e-12): richtig; M2 1,2e-14 (1,15e-14), 1,2e-13 (1,19e-13): richtig; "|Psi(0)| <= 1e-22": M2 teilt durch
s3 (pruef-v2.py 508), s3 = 1,2495e51 * 2^-200 = 7,78e-10 = e^{-kappa_c L}, 7,78e-10 * 1,19e-13 = 9,3e-23 < 1e-22:
plausibel; L_p 7,04754638671875 und B2 7,3560791015625: gleich JSON.
Lauf B2 in 3.2: Ordnung 144/88 (N 72/44), Reste 7,4e-44 (7,39053e-44), 2,8e-25 (2,74598e-25); eps 3,4980e-18
(3,49797771e-18), 3,2264e-18 (3,22630491e-18), 6,7951e-29 (6,79509417e-29), 6,7892e-29 (6,78910092e-29); K_J - 1
<= 1,72e-18 (1,711747734e-18); Zeilensumme 2,6010e-7 (2,60097985e-7); Innenabstand 0,87499 (c: 0,875000 +- 2,61e-7,
also >= 0,8749997): alle richtig gerundet.
Abschnitt 3.3: Breite H_0,1 1,3e-7 bzw. 6,7e-18 (B2 H0_z0[0] Radius 6,70e-18), dH/dc = -1, dH/da -2,1e15 (Log
-2,10839e15), delta_c, delta_a, kfak 8, z0-Bits 200/199/200/197: richtig. Zu "Auflage K6" siehe L5.
Abschnitt 4: alle neun Datei-Hashes und alle fuenf Software-Hashes gleich sha256sum bzw. JSON (grep exakter
String, je 1 Treffer in BEWEIS.md, A2, B2); Kommandozeilen gleich parameter.kommandozeile; 38 Dateien: richtig.
4.1 Code-Landkarte: alle Zeilennummern fuer pruef-v2.py (57, 88, 330, 358, 374, 393, 602) und bewkern.py stimmen
mit grep -n "def".

Rueckwaerts (JSON -> Text): parameter, sha256, delta, eps, lemma_info, M1, M2, M3, empfindlichkeitskontrolle,
protokoll (Z, innenabstand, Zeilensummen, D_relbreite, kanaele, lemma_P, lemma_J, K_J_minus_1, eps_1_bis_4, H0_z0,
regel_rundung, schritte_punkt/kasten, erster_schritt_punkt/kasten, einschlusstest, software) finden sich alle in
BEWEIS.md wieder oder sind dort zusammengefasst. Nicht im Text: B2 M2 (F1 1,6e-17, F2 -2,6e-16; nicht Null-zentriert,
weil z0 bei L = 40 bestimmt wurde; unerheblich, da nur A2 massgeblich ist) und B2 H_0(z0) mit Mittelpunkten -2,61e-15,
-1,24e-15 (der Text nennt nur die Breite; die Verschiebung faengt Krawczyk ab). Beides nicht tragend.

## 3. Treiber pruef.py -> pruef-v2.py (diff -u, 29 Zeilen weg, 132 neu, zehn Bloecke, alle gelesen)

Mathematik der strengen Kette unveraendert: evalH (57-87), tail_E (88-136), Krawczyk-Formel (464-468),
Einschlusstest (472), positivity (374-391), M1-Formel (496-497), M2 (505-509) sind nicht im diff. bewkern.py ist
nicht im Umfang des diff und per Hash unveraendert: a8a7ec6f... in SHA256SUMS.txt (Zeile aus der ersten Fassung),
in BEWEIS.md 4, in ZERT-A2 und ZERT-B2 (zur Laufzeit auf der .69 gelesen) und lokal (sha256sum) gleich; mtime 07:02;
die Zeilennummern der Code-Lesung (apriori 350, step 456, integrate 540, dyf 527, fr_arb 533, contains_all 277,
acb_beta 284) passen auf die Datei; Kasten-Schrittprotokolle bitgleich.

Geaenderte Pruefbedingungen (Art der Bildung, nicht die Bedingung selbst):
1. M3: `ok = ok and bool(rowsum < 1)` (477): rowsum vorher Python-max ueber arb-Kugeln, jetzt zeilenschranke =
   Maximum exakter oberer Zeilenschranken. Strenger oder gleich (das alte max konnte bei ueberlappenden Kugeln eine
   kleinere waehlen); Wert unveraendert (M3.rowsum bitgleich als Text, protokoll 5,6812629716e-9 gegen alt
   5,681262972e-9).
2. M1: `ok1 = ... bool(rs2 < 1)` (501): ebenso; M1.rowsum unveraendert.
3. rs_unw (543): nur Protokoll.
Nur Buchfuehrung: parameter, sha256 (401-414); lemma_info, lemma_P, lemma_J, eps_1_bis_4, Zeilensummen mit 20
Stellen; neue Felder K_J_minus_1_obere_schranke, H0_z0, regel_rundung, erster_schritt_punkt/kasten (Nachbildung
der Versuchsfolge mit bewkern.dyf), einschlusstest; Punkt-Schrittprotokoll; T1 getrennt (643-664).
Kontrollen (nicht streng, nicht im BESTANDEN-Flag): Negativkontrolle (eine Verschiebung 4 delta) ersetzt durch
drei Verschiebungen delta/4, delta, 4 delta mit Erwartung vorab; Feldname negativkontrolle -> empfindlichkeitskontrolle,
Flag test_verfehlt -> test_bestanden je Verschiebung. Der 4-delta-Fall ist in alt und neu [T,T,F,T].

## 4. Kontrollen

- `sha256sum -c SHA256SUMS.txt` in zertifikat/: 38 OK, 0 Fehler, rc 0. SHA256SUMS.txt hat 39 Zeilen: 38 Hashes und
  eine Kommentarzeile (Nachtrag, Hinweis pruef-v2.py = pruef.py auf der .69); alle 38 anderen Dateien im Ordner
  erfasst.
- jq alt gegen neu, alle gemeinsamen Felder einzeln (A/A2 und B/B2): L, M1, M2, M3, delta, eps, eps_vorschaetzung,
  khat, prec, s1, s3, z0, protokoll.D_relbreite, Z, innenabstand_rel_delta, kanaele, schritte_punkt, schritte_kasten,
  software: als Text gleich. lemma_info, protokoll.lemma_P, lemma_J, eps_1_bis_4, zeilensumme_gewichtet,
  zeilensumme_ungewichtet: als Text verschieden, weil 8 bzw. 10 Stellen gegen 20; jeden Wert verglichen, alle
  vertraeglich (die alte Ausgabe ist die Rundung der neuen). Siehe L3 zum Wortlaut "alle gleich".
- Kastengrenzen (protokoll.Z, alle vier Koordinaten, z0_m_e, delta_m_e, untere und obere Grenze) und Einschluesse
  (M3.K, M1.K, Krawczyk_in_Z, innenabstand_rel_delta, BESTANDEN): A = A2 und B = B2 vollstaendig gleich.
- cmp ZERT-A-L40-SCHRITTE-KASTEN.json ZERT-A2-L40-SCHRITTE-KASTEN.json und B/B2: bitgleich (auch gleiche sha256
  in SHA256SUMS.txt).
- Empfindlichkeitskontrolle: alt negativkontrolle 4 delta [T,T,F,T] test_verfehlt true; neu wie oben.
- Nicht prueffbar von hier: Gleichheit der Kopien auf der .69 mit den lokalen Dateien (Aussage des Autors); fuer
  bewkern.py, pruef-v2.py und z0.json aber durch die Laufzeit-Hashes im JSON belegt (Abschnitt 3 dieser Lesung).

## 5. Satz gegen Beleg

- Der Satz behauptet Existenz in Z mit Profil, Mode, Einfachheit, Folgerung; die Zertifikate zeigen M3 BESTANDEN
  (Krawczyk_in_Z, rowsum < 1, Lemma_P_ok, klein_danach, vier Kanalflags), dazu die Protokollzahlen fuer Lemma E
  (2 kappa0 - kappa_c >= 0,375236) und die Kanaele. Keine Ueberdehnung gefunden. Die Zahlen des Satzes stammen aus A2;
  B2 wird als engerer Kasten mit demselben Code (kein zweites Programm) ausgewiesen: richtig eingeordnet.
- Offene Punkte, jeweils genannt: fremdes Haus (Ergebnis, 5.1, Einfach gesagt), zweites Programm (Ergebnis, 5.1,
  5.3, Satztext zu B2), Softwarevertrauen (Ergebnis, 5.2), Eindeutigkeit des Profils [L?] (Satz 1, 5.4) und von
  (rho*, omega*) in Z (Nicht behauptet, 5.5), l > 0 und wesentliches Spektrum (Nicht behauptet, 5.6), nichtlinear
  (Nicht behauptet, 5.7, Einfach gesagt). Alle ehrlich, keiner kleingeredet.
- "Vollstaendig streng" ist wie zuvor durch die zwei Vertrauensannahmen eingegrenzt; "Einfach gesagt" gibt den
  Stand richtig wieder ("nur Fehler in der Beschreibung", "Pruefung durch ein anderes Haus steht noch aus").
- STAND.md: Verlauf stimmt mit den Dateizeiten (pruef-v2.py 08:08, Laeufe 06:08:47-06:14:19 UTC = 08:08-08:14 CEST,
  BEWEIS.md 08:20) ueberein; der gemeldete Regelverstoss (awk auf /dev/null) ist ohne Wirkung und offen gelegt.

## Befundliste (Schweregrade wie in LESUNG-PLAN.md und LESUNG-CODE.md)

### Blockierend: keiner.

### Wesentlich: keiner.

### L1 (klein, Protokoll): Schritt 0 traegt "fehlversuche: 0", der Text sagt "sieben Verkleinerungen"
Alle vier Schrittprotokolle (A2/B2, Punkt/Kasten) zeigen fuer den ersten Schritt fehlversuche 0. Ursache:
bewkern.integrate setzt info['nfail'] nur fuer Schritte mit r_j > 0 (Zeile 587); im ersten Schritt (551-560) wird
nicht gezaehlt, schrittliste liest i.get('nfail', 0). Die Summen "Fehlversuche 184/186" enthalten die sieben
Startversuche also nicht. Die sieben Verkleinerungen folgen trotzdem zwingend aus der Schleife (nur Glieder der Folge
R -> dyf(4/5 R, 8) werden versucht, der erste Erfolg angenommen; 13/64 ist das achte Glied), und
folge_trifft_R_angenommen bestaetigt, dass 13/64 auf der Folge liegt. Der Beweis ist nicht beruehrt.
Vorschlag: in BEWEIS.md 3.2 einen Satz "Schritt 0 zaehlt keine Fehlversuche (nfail wird erst ab r_j > 0 gesetzt);
die Versuchsfolge ist aus der Schleifenlogik nachgebildet" ergaenzen; beim naechsten Neulauf nfail auch fuer den
ersten Schritt setzen.

### L2 (klein, Rundungsrichtung in der Darstellung): "|f| < 0,33208949" ist fuer eine Oberschranke von |f| abgerundet
Der Code prueft |f| < thr mit thr = untere Schranke von sqrt(S_-) ueber Z (positivity 378, 388; schwelle
[0,3320894957 +- 1,99e-11]). Daraus folgt |f| < thr <= sqrt(S_-), was Lemma Pos braucht. Die Zahl 0,33208949 ist
kleiner als thr; "|f| < 0,33208949" folgt daher nicht aus dem Testflag, sondern erst aus dem Schrittprotokoll (ab
r_j >= L_p: f_real_oben max 0,0929549, f_real_unten min -0,0130459 in A2; B2 0,0842439 und -0,0161641). Die Aussage
ist also wahr, aber die Klammer "(abgerundete untere Schranke von sqrt(S_-))" nennt den falschen Grund. Vorschlag
(BEWEIS.md 2.5 und 3.2 "Positivitaet"): "danach |f| < thr <= sqrt(S_-) mit thr >= 0,33208949 (Zertifikat schwelle);
tatsaechlich |f| <= 0,093 (Schrittprotokoll)".

### L3 (klein, Wortlaut): "Alle mit A und B gemeinsamen Felder sind gleich" (BEWEIS.md 3.1; STAND.md 08:14:21)
Als Text gleich sind nur die Felder mit unveraenderter Ausgabegenauigkeit (die im Text aufgezaehlten). Sechs Felder
(lemma_info, protokoll.lemma_P, lemma_J, eps_1_bis_4, beide Zeilensummen) sind wegen 20 statt 8 bzw. 10 Stellen
als Text verschieden, in den Werten vertraeglich. Abschnitt 7 sagt es richtig ("delta, Kr, ... gleich"). Vorschlag:
in 3.1 "Alle gemeinsamen Felder mit gleicher Ausgabegenauigkeit sind gleich; die uebrigen sind Rundungen derselben Werte".

### L4 (klein, Erklaerung): Laufzeitunterschied nur zum Teil erklaert (BEWEIS.md 3.1, BEWEIS-PLAN.md 6)
Die drei Empfindlichkeits-Punktlaeufe kosten in A2 etwa 24,6 s (Log 88,3 s -> 112,9 s), das Hashen 0,2 s. Die
Kernlaeufe selbst dauerten aber etwa doppelt so lang wie in A (Punkt 13,6 s gegen 6,9 s, Jacobi 33,5 s gegen 18,4 s,
Kasten 41,0 s gegen 18,3 s; B2: 16,7/48,3/24,2 s gegen 11,0/23,4/24,0 s). Bei bitgleichen Schrittprotokollen ist
das Umgebung (Last auf der .69), keine Rechnung. Vorschlag: "und langsamere Kernlaeufe bei gleichen Ergebnissen"
ergaenzen.

### L5 (klein, Bezeichner): "Auflage W1" (3.3), "Lesung B1" (3.2) und "Auflage K6" (3.3) meinen die Plan-Lesung
Seit Abschnitt 7 gibt es zwei Befundreihen mit gleichen Kuerzeln (Plan-Lesung B1, W1-W7, K1-K9; Code-Lesung W1,
K1-K8). In 3.2 und 3.3 sind die Kuerzel der Plan-Lesung gemeint (K6: z0 mit mindestens 120 Bit, LESUNG-PLAN.md 221),
in Abschnitt 7 die der Code-Lesung. Vorschlag: "(Plan-Lesung K6)" bzw. "(Code-Lesung K1)" schreiben.

### L6 (klein, Verwechslungsgefahr): Treiber heisst im JSON "pruef.py", lokal pruef-v2.py
ZERT-A2/B2 sha256.pruef.py = 922eb191... = lokal pruef-v2.py; die lokale pruef.py (4c58d569...) ist die alte
Fassung. BEWEIS.md 4 und die Kommentarzeile in SHA256SUMS.txt erklaeren es; wer nur JSON und SHA256SUMS.txt
vergleicht, sieht zunaechst einen Widerspruch. Vorschlag: beim naechsten Neulauf die Datei auch auf der .69
pruef-v2.py nennen oder das Feld sha256 um einen Hinweis "lokal: pruef-v2.py" ergaenzen.

### Nicht beanstandet, aber notiert
- Logkopf "modus zert prec 320 L 40 N 72" in LAUF-zertB2-L44.log (und satzB2): args.L ist 40, der Lauf nutzt
  L = args.Lz = 44 (zert 395, parameter.L 44). Schon in LAUF-zertB-L44.log so; nur Anzeige.
- Der Wert K_J_minus_1_obere_schranke ist mit str(10) eine Kugel um die exakte obere Schranke (Radius 4,67e-28);
  die Rundung ging nach oben (Log: K_J - 1 = 7,5683771849535e-17 < 7,568377185e-17), der Satz rundet nochmals auf
  7,57e-17. In Ordnung; bei Wiederverwendung des Feldes den Radius mitnehmen.
- Huellen B je Schritt und Testausgang je Schritt weiterhin nicht im Protokoll (Plan-Lesung K5); im Text offen gelegt.
- BEWEIS-PLAN.md 7 (Lueckenliste, sechs Punkte) fuehrt den nichtlinearen Ausschluss nicht als eigenen Punkt;
  BEWEIS.md 5.7 tut es. BEWEIS.md ist massgeblich.

## Gepruefte Stellen

BEWEIS.md ganz (1-277). LESUNG-CODE.md ganz. STAND.md ganz. BEWEIS-PLAN.md 299-333, 355-372. LESUNG-PLAN.md 221-224.
pruef-v2.py: diff gegen pruef.py vollstaendig; 205-320 (main: frei, start, newton, zert, kontrolle, satz);
330-372 (zeilenschranke, sha256_datei, arb_fraction, erster_schritt); 374-391 (positivity); 393-528 (zert bis
Empfindlichkeitskontrolle); 530-600 (Protokoll, Schrittlisten). bewkern.py 540-598 (integrate); def-Zeilen per grep.
ZERT-A2-L40.json und ZERT-B2-L44.json ganz; ZERT-A-L40.json und ZERT-B-L44.json per jq feldweise; z0.json ganz;
SHA256SUMS.txt ganz (cat -A). Schrittprotokolle per jq: Schritt 0 (alle vier), Statistik Punkt (A2, B2), letzter
Schritt, Schritte ab L_p (A2, B2), letzter positiver Schritt. Logs: LAUF-zertA2-L40, LAUF-zertB2-L44, LAUF-satzA2,
LAUF-satzB2, LAUF-kontr2 ganz; LAUF-zertA-L40, LAUF-zertB-L44, LAUF-satzA/B, LAUF-kontr1, LAUF-frei3 nur Kopf und
Service runtime.

## Was ich nicht getan habe

Keine Rechnung, kein Interpreter (kein python, kein awk), keine Aenderung an BEWEIS.md, BEWEIS-PLAN.md, STAND.md,
Code, Zertifikaten oder SHA256SUMS.txt, kein git, kein Journaleintrag, kein Zugriff auf die .69, keine der
ausgeschlossenen Dateien und Ordner geoeffnet. Die Lemmata selbst (P, J, T, T0, K, Pos, E) habe ich nicht erneut
gegen den Code gehalten; das war Gegenstand der Code-Lesung, deren Stellen im Kern (bewkern.py) per Hash unveraendert
sind und deren Treiberstellen ich im diff auf Unveraendertheit geprueft habe. Die Korrektheit von python-flint/FLINT
bleibt Vertrauensannahme.

- Ende 2026-09-30 09:56:58 CEST (date). Unterbrechung durch ein Nutzungslimit der Leitung etwa 08:37 bis 09:51 (Angabe der Leitung); Wiederaufnahme 09:56:19 CEST (date). Seit Beginn keine Aenderung im Beweisordner (find -newermt 08:21:54: nur diese Datei; sha256sum -c erneut 38 OK).

## Nachtrag: Nachlesung der Einarbeitung L1-L6 (nur die vom Autor genannten Zeilen)

- Beginn 2026-09-30 10:01:35 CEST (date), Ende 2026-09-30 10:03:16 CEST (date). Gelesen: BEWEIS.md 18, 100-102, 118-123, 126-130, 135, 146, 163, 170, 179, 186-189, 246, 279-292; BEWEIS-PLAN.md 316-319; STAND.md 30-32. Gegengeprueft mit jq (Schrittprotokolle A2/B2 ab L_p, Mittelpunkt plus Radius), ZERT-A2/B2 (Teillaufzeiten), LAUF-zertA2-L40.log (Zeiten der Empfindlichkeitslaeufe), pruef-v2.py 406, sha256sum -c.
- zertifikat/ unveraendert (keine Datei neuer als 08:21:54); sha256sum -c: 38 von 38 OK. BEWEIS.md 277 -> 302 Zeilen = genau die Summe der genannten Einfuegungen (L2 +1, L3 +3, L4 +3, L6 +4, 7.1 +14); alte Formulierungen (0,33208949 abgerundete Schranke, Alle Felder gleich, Auflage K6/W1/B1 ohne Zusatz, Laufzeit-Erklaerung) sind weg; Einfach gesagt unveraendert.
- Je Befund erledigt: L1 ja (146: nfail erst ab r_j > 0, Nachbildung, Summen 184/186 ohne Startversuche; stimmt mit bewkern.py 551-560, 587). L2 ja (100-102, 163: |f| < thr <= sqrt(S_-), thr >= 0,33208949 abgerundet aus schwelle 0,3320894957 - 1,99e-11; tatsaechlich |f| <= 0,093 (A2: max Huelle inkl. Radius 0,0929549363, min -0,0130459) und <= 0,085 (B2: 0,0842439050, min -0,0161641): beide aufgerundet, richtig). L3 ja (118-123: sechs Felder richtig benannt; STAND.md 10:00:53 Berichtigungszeile, Original 08:14:21 unveraendert). L4 ja (126-130, PLAN 316-319: etwa 25 s = 10,6 + 7,1 + 6,9 s im Log, Hashen 0,2 s, Teillaufzeiten 13,6/33,5/41,0 gegen 6,9/18,4/18,3 und 16,7/48,3/24,2 gegen 11,0/23,4/24,0 s gleich JSON). L5 ja (18, 135, 170, 179, 246). L6 ja (186-189: Zeile 406 ist die Zuweisung der Schluessel; Hashes richtig zugeordnet). 7.1 gibt Urteil, Zeiten und Stellen richtig wieder.
- Neue Ungenauigkeiten in BEWEIS.md und BEWEIS-PLAN.md: keine. Zwei Randnotizen zu STAND.md, nicht tragend: (a) Zeile 09:58:03 nennt "|f| <= 0,0929549 (A2) bzw. 0,0842439 (B2)"; das sind die gedruckten Mittelpunkte der Huellen, mit Radius 0,0929549363 bzw. 0,0842439050. BEWEIS.md rundet richtig auf 0,093 und 0,085; fuer STAND.md genuegt eine Berichtigungszeile oder das Belassen, da BEWEIS.md massgeblich ist. (b) Die Eintraege 10:00:53 und 10:00:36 stehen in vertauschter Reihenfolge.
- Urteil unveraendert: letzte Schicht traegt. Keine Auflagen.
