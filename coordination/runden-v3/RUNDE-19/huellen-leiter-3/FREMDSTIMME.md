Urteil: Lesart (a) mit Auflagen L1 bis L4, gegen (b).
- Frage 1: Ja, beide k = 3-Funde liegen auf k = 3, knotenunabhaengig geprueft.
- Frage 2: Die Variantenabhaengigkeit der Knotenzahl ist belegt. Die Saat als Ursache ist plausibel, aber nicht
  direkt gezeigt.

# FREMDSTIMME zu HUELLEN-LEITER-3 (Runde 19)

- Pruefer: frischer Pruefer (Fremdstimme), Haus Anthropic, an den Rechnungen nicht beteiligt
- Beginn (gemessen per date): 2026-10-02 16:51:54 CEST
- Inhaltlich abgeschlossen (gemessen per date): 2026-10-02 17:04:27 CEST, Dauer 12 min 33 s
- Zeitbox: 25 min
- Gelesen nur: huellen-leiter-3 (KARTE, PLAN eingefroren, Nachtraege, ERGEBNIS, aus/), huellen-leiter-2 (KARTE, ERGEBNIS, aus/), RUNDE-18/huellen-leiter (ERGEBNIS, aus/)
- Werkzeuge: nur lesend (ls, cat, sed -n, grep, jq, sha256sum, date); Zahlen im Kopf mit Rechenweg

## 1. Befund zu Frage 1: Liegen die zwei k = 3-Funde auf der Kurve k = 3?

**Ja.** Das zeigen drei Pruefungen, die nicht an der Knotenzahl haengen.

Quellen: RUNDE-18 aus/laeufe/stellen.json (k, R, rho, w2 je Stelle), RUNDE-18 aus/laeufe/z-st1-0100..0110.json
(rho aller Nullstellen von m_bc je Zeile, Code der Runde 18), huellen-leiter-3 aus/test/test-st1-a.json und
-b.json (S-Wurzeln, Newton-Schritte, rho aller Nullstellen der Zeile an jeder Wurzel), aus/diag/knoten-st*.json.

**1a Stetigkeit der Stellenfolge auf k = 3** (rho der Stellen, Runde 18 bis Nr 83, dann die zwei neuen Funde):

| R | omega^2 | rho | Delta rho zum Vorgaenger | Verhaeltnis der Delta | Delta rho / Delta omega^2 |
|---|---|---|---|---|---|
| 31,109 (Nr 58) | 0,772611402 | 1,22985346 | | | |
| 33,286 (Nr 65) | 0,769660202 | 1,22332828 | 0,00652518 | | |
| 35,454 (Nr 74) | 0,767086277 | 1,21787516 | 0,00545312 | 0,8357 | 2,119 |
| 37,613 (Nr 83) | 0,764820007 | 1,21326352 | 0,00461164 | 0,8457 | 2,035 |
| 39,765 (neu) | 0,762808178 | 1,20932238 | 0,00394114 | 0,8546 | 1,959 |
| 41,912 (neu) | 0,761009416 | 1,20592276 | 0,00339962 | 0,8626 | 1,890 |

- Rechenweg, Beispiel: 1,21326352 - 1,20932238 = 0,00394114; 0,00394114 / 0,00461164: 0,8 x 0,00461164 = 0,00368931,
  der Rest 0,00025183 / 0,00461164 = 0,0546, zusammen 0,8546.
- Delta omega^2 = 0,764820007 - 0,762808178 = 0,002011829; 0,00394114 / 0,002011829 = 1,959.
- Die Verhaeltnisse steigen in gleichmaessig kleiner werdenden Schritten: +0,0100, +0,0089, +0,0080. Die Steigung
  dRho/dOmega^2 faellt ebenso gleichmaessig: -0,084, -0,076, -0,069. Am Uebergang von Runde 18 zu den neuen Funden gibt es
  keinen Knick.
- **Vorhersage nur aus Runde 18**, nach demselben Muster wie oben gerechnet.
  - Die k = 3-Stellen Nr 42, 50, 58, 65, 74, 83 haben die rho-Werte 1,24752021, 1,2377683, 1,22985346, 1,22332828,
    1,21787516 und 1,21326352.
  - Daraus folgen die Verhaeltnisse 0,8116, 0,8244, 0,8357 und 0,8457. Die Zuwaechse betragen 0,0128, 0,0113 und
    0,0100 und schrumpfen je um rund 0,0013.
  - Fortgesetzt ergibt das die naechsten Verhaeltnisse ~0,8545 und ~0,8622.
  - Fuer 39,765: Delta rho = 0,00461164 x 0,8545 = 0,0039406, also rho = 1,21326352 - 0,0039406 = 1,2093229.
    Gefunden: 1,20932238, Abweichung 4,9e-7.
  - Fuer 41,912: Delta rho = 0,0039406 x 0,8622 = 0,0033976, also rho = 1,2093229 - 0,0033976 = 1,2059253.
    Gefunden: 1,20592276, Abweichung 2,5e-6.
  - Beide Abweichungen sind rund 4900- bzw. 27700-mal kleiner als der Abstand zur naechsten Nachbarkurve (1c).
    Rechenweg: 0,01223 / 2,5e-6 = 4892; 0,01357 / 4,9e-7 = 27694.

**1b Die Kurve als Ganzes:** Die Nullstelle mit Rang 3 in jeder Zeile, verfolgt ueber den Uebergang hinweg. Die Werte
bis R = 38,952 stammen aus dem Code der Runde 18, ab 39,594 aus S an den acht neuen Wurzeln.

| R | Rang 2 (k = 2) | Rang 3 (k = 3) | Rang 4 (k = 4) | Steigung Rang 3 je Einheit R (zum Vorgaenger) |
|---|---|---|---|---|
| 36,436 (Z 105) | 1,19957414 | 1,21568675 | 1,23759465 | |
| 37,442 (Z 107) | 1,19832815 | 1,21360174 | 1,23440599 | -0,00207 |
| 37,946 (Z 108) | 1,19773680 | 1,21261492 | 1,23289740 | -0,00196 |
| 38,952 (Z 110) | 1,19661246 | 1,21074379 | 1,23003832 | -0,00186 |
| 39,594 | 1,19593202 | 1,20961482 | 1,22831434 | -0,00176 |
| **39,765 (Fund)** | 1,19575549 | **1,20932238** | 1,22786793 | -0,00171 |
| 40,229 | 1,19528644 | 1,20854625 | 1,22668349 | -0,00167 |
| 40,506 | 1,19501301 | 1,20809439 | 1,22599415 | -0,00163 |
| **41,912 (Fund)** | 1,19369470 | **1,20592276** | 1,22268391 | -0,00154 |
| 42,351 | 1,19330579 | 1,20528433 | 1,22171170 | (-0,00145 ab 42,004) |
| 42,613 | 1,19307838 | 1,20491149 | 1,22114420 | -0,00142 |

- Rechenweg Uebergang: (1,20961482 - 1,21074379) / (39,594 - 38,952) = -0,00112897 / 0,642 = -0,001759.
  Zum Vergleich davor: -0,00187113 / 1,006 = -0,001860. Der Betrag der Steigung faellt glatt von 0,00207 auf 0,00142.
  Die Spur hat weder einen Sprung noch einen Knick.
- Die Nachbarkurven haben am Uebergang klar andere Steigungen.
  - k = 2: -0,00068044 / 0,642 = -0,00106
  - k = 4: -0,00172398 / 0,642 = -0,00269
- Unterhalb von Rang 5 tritt zwischen Zeile 110 und 39,594 keine Nullstelle neu hinzu. Die Raenge 0 bis 5 verschieben
  sich jeweils um weniger als 0,0025.
  - Die elfte Nullstelle der neuen Zeilen liegt oben bei rho = 1,41223, nahe hi = 1,41411.
  - Ein Rang 3 von unten bezeichnet also dieselbe Kurve wie in Runde 18.
- Die Lagen der Nullstellen sind variantenfest.
  - Zeilen 100, 105, 108, 110: Rang 3 in Runde 18 (alt) und in HUELLEN-LEITER-2 (S) auf 8 Nachkommastellen gleich
    (1,22164611 / 1,21568675 / 1,21261492 / 1,21074379).
  - D1: An 39,77 haben F und alt ein bitgleiches d_rho (2,8588760248e-9).

**1c Abstand zu den Nachbarkurven gegen Abstand zur Fortsetzung:**

| Fund | Abstand nach unten (k = 2) | Abstand nach oben (k = 4) | Newton-Weg ab Start (Start = Fortsetzung der k = 3-Kurve aus Runde 18, quadratisch in 1/R) |
|---|---|---|---|
| 39,765 | 1,20932238 - 1,19575549 = 0,01356689 | 1,22786793 - 1,20932238 = 0,01854555 | 1,12e-5 (erster Schritt; dann 3,0e-9, 1,9e-12) |
| 41,912 | 1,20592276 - 1,19369470 = 0,01222806 | 1,22268391 - 1,20592276 = 0,01676115 | 3,75e-5 (dann 7,0e-8, 2,2e-11) |

- Newton blieb also innerhalb von 0,3 % des Abstands zur naechsten Nachbarkurve: 3,75e-5 / 0,01223 = 0,0031.
- Davon geht der groessere Teil auf die Verschiebung in omega^2 entlang der Kurve zurueck.
  - Delta omega^2 = 0,7610094156 - 0,7609957176 = 1,37e-5.
  - Mal Steigung ~1,94 ergibt das ~2,65e-5.
- Die Nachstarts bei R +-0,25 enden an derselben Wurzel, obwohl sie in rho bis 4,3e-4 entfernt starten.
  - Rechenweg zum Startabstand: 1,2093223758 - 1,2088894286 = 4,33e-4.
  - Wurzeln untereinander in (omega^2, rho) gleich auf <= 6,7e-14 (st1, 41,93: 1,2059227553634210 -
    1,2059227553633538), in R auf <= 1,1e-10 (st1, 39,77).

**Nebenbefunde (aendern das Urteil nicht):**
- ERGEBNIS Abschnitt 3 nennt fuer die k = 3-Stellen einen "Abstand <= 1,2e-13 zur Nullstelle der Zeile". Fuer 41,93
  stimmt das (1,1e-13, 4,2e-14). Fuer 39,77 ist d_rho aber 2,86e-9, in allen drei Starts und auf beiden Stufen (bei F
  und alt in D1 ebenso). Das liegt weit unter der Planschranke 1e-6, die Angabe im ERGEBNIS ist aber falsch.
- Die Stufen der neuen Funde stimmen ueberein: rho 1,2093223763619 - 1,2093223758165 = 5,45e-10,
  omega^2 2,84e-10 (39,765). Das passt zu "<= 5,5e-10".

## 2. Befund zu Frage 2: Haengt die Knotenzahl an der Saat?

**Dass die Knotenzahl von der Variante abhaengt, belegen die Daten. Dass die Saat die Ursache ist, ist plausibel und
passt zu allen Daten, sehe ich aber nicht direkt.** Die Ausgaben enthalten nur Knotenzahlen, keine Knotenorte und
keine c-Profile.

Belege, je mit Fundstelle:

1. **Gleiche Lage, gleicher Rang, verschiedene Knotenzahl.**
   - Lagen: S gegen alt <= 9,5e-14 und F gegen alt <= 8,9e-16 (K0'). F gegen S an den zwei k = 3-Funden <= 4,8e-14
     (diag/umlauf-k3-st1.json, dF).
   - Rang: in allen drei Varianten 3 (D1, knoten-st1.json).
   - Knotenzahl an denselben Wurzeln:
     - S: 3 und 3
     - F: 2 und 2 (beide Stufen)
     - alt: 3 und 2
   - Eine Groesse, die sich aendert, waehrend die Stelle auf 1e-13 gleich bleibt, ist an dieser Stelle kein Merkmal der
     Kurve.
2. **Der Code der Runde 18 selbst reproduziert seine Knotenzahlen jenseits R ~ 39,7 nicht.**
   - alt gibt (D1) an 40,24 (k = 2) 1 statt 2, an 42,00 (k = 0) 1 statt 0 und an 42,62 (k = 1) 1 statt 0.
   - Das Muster je Rang springt ganz (1,1,1,3,3,3,5,5,7,7,7 an 39,77).
   - Mit dem Bezugscode haette die Knotenbedingung also 4 von 8 Sprossen verworfen: 39,77, 40,24, 42,00 und 42,62,
     darunter k = 0, 1 und 2.
   - Das passt zur Aussage "Kopplung der Runde 18 ab R ~ 40 rundungsbestimmt".
3. **Der zeitliche Verlauf unter S passt zum Saat-Bild.** In den S-Zeilen von HUELLEN-LEITER-2 (aus/laeufe/z-st1-*)
   kippt die Knotenzahl von oben nach unten durch die Raenge, waehrend R waechst:

   | Rang | Knotenzahl kippt zwischen |
   |---|---|
   | 6 und 7 | Zeile 88 (R 27,85) und 90 (R 28,87) |
   | 5 | Zeile 90 (R 28,87) und 92 (R 29,88) |
   | 4 | Zeile 92 und 94 (30,9) |
   | 3 | Zeile 99 (R 33,412: 2) und 100 (R 33,916: 3; Stufe 2 ebenso) |

   - Der Plan hatte vor jedem Lauf vorausgesagt (Abschnitt 7): S verlegt die Saat nach r_s ~ R - 23, die c-Loesung auf
     k = 3 hat ihren ersten Knoten bei r ~ 11 bis 12, ab R ~ 34 kippt die Konvention.
   - Beobachtet ist der Wechsel bei R = 33,4 bis 33,9, also r_s ~ 10,4 bis 10,9. Das liegt nahe an der Voraussage.
   - Das S-Umlaufzeichen auf k = 3 kippt im selben Bereich: Nr 65 (R 33,29) ist unveraendert, Nr 74 und 83 sind
     umgekehrt (K0'-Tabelle).
   - Hoehere Kurven haben mehr Knoten und kippen frueher. Auch das passt zu einer Saat, die mit R nach aussen wandert.
4. **Eine Voraussage aus der Saat-Erklaerung ist eingetroffen.**
   - PLAN-NACHTRAG-1 (eingefroren 16:38:37) erwartete mit F die Knotenzahlen 0, 0, 2, 2 fuer k = 0 bis 3.
   - D1 entstand danach (knoten-st1.json 16:42:12, knoten-st2.json 16:46:55).
   - Ergebnis: an allen 8 Stellen und auf beiden Stufen 0, 0, 2, 2. Das ganze untere Muster 0,0,2,2,4,4,4,6,6,6 gleicht
     dem der Runde 18 in Zeile 110.
   - Einschraenkung: Die Voraussage entstand nach Kenntnis des S-Befunds, ist also keine Vorab-Wertung.

**Einschraenkungen zur Begruendung des Agenten:**
- Der Satz im ERGEBNIS 5, die Knotenzahl tauge "nur innerhalb einer festen Variante" als Kurvenmerkmal, ist zu
  weit. Auch innerhalb einer Variante ist sie entlang einer Kurve nicht fest:
  - S: k = 3 wechselt von 2 auf 3 (siehe 3.).
  - Auf k = 4 wechselt sie in Runde 18 (kn_1: Nr 21 und 27 haben 2, ab Nr 33 bei R 23,36 dann 4) und in S gleich
    (Zeile 75: 2, Zeile 80: 4).
  - Dieser Wechsel ist in beiden Varianten gleich, also vermutlich keine Saatfolge.
- Fazit: Die Knotenzahl ist hier ueberhaupt kein verlaessliches Kurvenmerkmal ueber einen R-Bereich hinweg. Rang und
  Stetigkeit der Lage sind es (Frage 1).
- Nach der S-Variante waere die Bedingung "wie im Vorlaeufer" erfuellt gewesen, wenn man "Vorlaeufer" als
  HUELLEN-LEITER-2 liest. Dort hat Rang 3 in den Zeilen 100 bis 110 die Knotenzahl 3.
  - Die KARTE ("Knotenzahl wie im Vorlaeufer") laesst beide Lesarten zu.
  - Der Plan legte vorab Runde 18 fest ([Lesart], Abschnitt 4).
  - Der Fehler sitzt also in der Planlesart, die eine S-Knotenzahl mit einer Knotenzahl des alten Codes vergleicht,
    nicht im Wortlaut der Karte. Die Karte waehlte allerdings ein zerbrechliches Merkmal.

## 3. Empfehlung zur Lesart

**Empfehlung: (a), mit den Auflagen L1 bis L4. Gegen (b).**

Die formale Wertung bleibt "P1' nicht eingetroffen, P2' eingetroffen". Daneben steht eine gekennzeichnete
Sachaussage: Alle 8 Sprossen wurden in Lage und Kurve getroffen. Diese Pruefung ist nachtraeglich und stammt von
einer Fremdstimme.

Warum nicht (b):

1. **(b) ersetzt eine eingefrorene Regel nach Kenntnis des Ausgangs, und der Fehler war vorab erkennbar.**
   - Die S-Zeilen von HUELLEN-LEITER-2 mit Knotenzahl 3 auf Rang 3 lagen im erlaubten Lesebereich.
   - Der Plan selbst sagte in Abschnitt 7 voraus, dass S auf k = 3 ab R ~ 34 die Konvention kippt.
   - Gerade fuer solche Faelle gilt die Regel, Kontrollen nicht nach dem Befund zu lockern.
2. **Die Begruendung von (b) stimmt nicht genau.** Der Fehler steckt in der Planlesart (S-Knotenzahl gegen
   Runde-18-Knotenzahl), nicht in der Karte.
   - Unter der Lesart "Vorlaeufer = HUELLEN-LEITER-2" waere die Kartenbedingung erfuellt gewesen.
   - Diese Lesart jetzt zu waehlen hiesse aber wieder, nach dem Ausgang zwischen Lesarten zu waehlen.
3. **(b) waehlt einseitig aus den Abweichungen des Plans von der Karte.**
   - Der Plan lockerte vorab das woertliche Kartenkriterium abs(W) < 1e-10 auf <= 1e-9. Woertlich waere k = 1 / 42,62
     verworfen (2,7e-10 / 4,2e-10) und P1' ebenfalls nicht eingetroffen.
   - (b) behielte die lockernde Abweichung und striche nachtraeglich die verschaerfende. Das ist eine Auswahl nach dem
     Ausgang, auch wenn beide Einzelgruende vertretbar sind.
4. **(b) bringt keinen Erkenntnisgewinn.** Die Sachlage laesst sich unter (a) vollstaendig sagen. (b) fuegt nur das
   Etikett "vorab bestanden" hinzu, und genau dieses deckt das Verfahren nicht.

**Auflagen (Anforderungen, kein Wortlaut):**

- **L1 Formale Wertung unveraendert.** P1' nicht eingetroffen, P2' eingetroffen, K0' und Kontrolle bestanden. Keine
  Neuwertung und kein "eingetroffen mit Vorbehalt".
- **L2 Sachaussage nur gekennzeichnet.** Sie muss enthalten:
  - "nachtraeglich, Fremdstimme 2026-10-02, knotenunabhaengiges Kriterium (Rang und Stetigkeit von rho, Abstand zu den
    Nachbarkurven)"
  - alle 8 Lagen mit abs(Delta R) <= 0,018
  - den Hinweis, dass die zwei k = 3-Funde nur an der Knotenbedingung scheiterten und diese Bedingung ein Planfehler
    war
  - Die Sachaussage ist nicht als vorab gewerteter Beleg der Sprossenregel zitierfaehig.
- **L3 Bedeutungssatz nie allein fuehren.**
  - "Die Regel gilt nur im bisherigen Bereich" wird formal nur ueber die Planlesart "nicht gefunden = Abweichung > 0,3"
    ausgeloest.
  - Eine Lageabweichung > 0,3 gibt es nicht: Das Maximum ist 0,018, also rund ein Siebzehntel der Schwelle
    (0,3 / 0,018 = 16,7).
  - Wo der Satz erscheint (Karte, Dashboard, Paper qball-bic-ladder), muss der Ausloeser dabei stehen.
    Umgekehrt darf auch "Die Sprossenregel sagt neue stille Stellen voraus" nur mit dem Vermerk "nachtraeglich" stehen.
- **L4 Fuer eine vorab gewertete Bestaetigung einen neuen Test.**
  - Anforderung: neue Sprossen, etwa die dritten auf k = 0 bis 3 oder Kurven k >= 4.
  - Kurvenkriterium nur variantenfest: Rang plus Stetigkeit der Lage. Die Knotenzahl entweder ganz weglassen oder nur
    gegen Bezugswerte derselben Variante im selben R-Bereich.
  - Vor dem Einfrieren pruefen, ob jede Pflichtbedingung an den K0'-Stellen mit genau dem Testcode erfuellt ist.
  - Hier haette das den Konflikt gezeigt: In den S-Zeilen 103 und 107 von HUELLEN-LEITER-2 (Zeilen von Nr 74 und 83,
    beide Stufen) hat Rang 3 die Knotenzahl 3.
- **Kleinkorrektur am ERGEBNIS** (per Nachtrag, nicht im Text): Der Abstand zur Zeilennullstelle betraegt bei 39,77
  2,86e-9, nicht "<= 1,2e-13" (siehe 1, Nebenbefunde).

Kennzeichnung nach Projektregel: (a) ersetzt keine Regel und braucht daher keine Ausnahme. Wuerde die Leitung dennoch
(b) waehlen, traegt diese Fremdstimme das nicht. Die Entscheidung muesste dann als "nach Ausgang, gegen die
Fremdstimme" gekennzeichnet werden.

## 4. Grenzen der eigenen Pruefung

- **Nichts neu gerechnet.** Ich habe nur Ausgabedateien gelesen und daraus im Kopf gerechnet.
  - Dass "knoten" die Nullstellen der c-Komponente zaehlt und "rang" der Rang von unten ist, uebernehme ich aus PLAN
    und ERGEBNIS.
  - code/, hilfs/, ref/ und logs/ waren nicht freigegeben und sind ungelesen. Ob ref/stellen-r18.json der Datei
    RUNDE-18 aus/laeufe/stellen.json gleicht, habe ich nicht geprueft.
- **Stetigkeit nur an Stuetzstellen.**
  - Die Spur von Rang 3 stuetzt sich auf 14 Punkte: 6 Zeilen der Runde 18 bis R 38,95 und die 8 Zeilen an den neuen
    Wurzeln ab 39,59.
  - Zwischen 38,95 und 39,59 liegt keine Zeile. Eine Kreuzung oder ein Eintritt eines Nullstellenpaars zwischen den
    Stuetzstellen ist damit nicht streng ausgeschlossen. Bei Nachbarabstaenden >= 0,0122 und glatten Steigungen ist
    er unplausibel.
  - Steigungen ueber kurze Intervalle sind wegen auf 3 Stellen gerundeter R-Werte nur auf wenige Prozent genau. Das
    Urteil haengt daran nicht.
- **Ursache der Knotenabhaengigkeit nicht gezeigt.**
  - Die Daten enthalten keine Knotenorte und keine c-Profile.
  - Das Saat-Bild ist darum nur als passend bewertet, nicht als bewiesen. Gestuetzt wird es durch das Kippen in der
    Reihenfolge der Raenge, die Lage des Kippens nahe der Planvoraussage und die eingetroffene F-Voraussage.
- **Zeitangaben.** PLAN-NACHTRAG-2 nennt "Geschrieben ab 16:46", eingefroren wurde laut Dateiname und mtime aber um
  16:45:57.
  - Die D2-Ausgaben entstanden 16:46:14 und 16:46:30, also 17 bzw. 33 s nach dem Einfrieren.
  - Die Reihenfolge Einfrieren vor Ausgabe ist eingehalten, die Angabe "ab 16:46" ist ungenau.
  - D2 ist ungewertete Diagnose, das Urteil haengt daran nicht.
- **Nur ein Haus.** Diese Fremdstimme ist ein einzelner frischer Anthropic-Pruefer, keine Dreihausjury. Die
  Rechenwege oben sind von Hand und koennen Rundungsfehler in der letzten Stelle haben.
- **Gelesen:**
  - huellen-leiter-3: KARTE, PLAN eingefroren, beide Nachtraege eingefroren (sha256 jeweils gleich der Arbeitsdatei),
    ERGEBNIS, aus/test, aus/diag
  - huellen-leiter-2: KARTE per grep, aus/laeufe z-Dateien
  - RUNDE-18: aus/laeufe/stellen.json und z-st1-Zeilen 75 bis 110
  - Nicht gelesen: KS-1-Dateien, T8-SOLL-*, vertraege-20260925/ und Geheimnisse.
