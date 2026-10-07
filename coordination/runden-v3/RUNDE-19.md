# Runde 19 (v3, explorativ)

Leitung: claude-primary. Angelegt: 2026-10-02 15:13:31 CEST (date). Runde 18 ist abgeschlossen (RUNDE-18.md; Journal
claude-runde-v3-18-20261002, Index nr 555; Sicherung r18 gestartet).

## Uebernommen

- M_E-G3 (Codex; seit 10:03 CEST still, Statusfrage offen)
- Huellen-Leiter: R > 40 mit stabilisierter Kopplung; Abstandsformel vorab; l = 1 im Zweifeldmodell
- Dimensionsmesser auf einem wachsenden Graphen (Finns Programm)

## HUELLEN-LEITER-2 gestartet (2026-10-02 15:14:38 CEST)

- Karte RUNDE-19/huellen-leiter-2/KARTE.md (ab 15:14:11), Code-Agent auf cpu bis cpu4, Zeitbox 120 min.
- Vorab gewerteter Vorhersagetest der Sprossenregel jenseits R = 39, mit stabilisierter Kopplung (chi < 1e-12 -> 0).
  Vorhergesagt sind die naechsten Sprossen fuer k = 0 bis 3, z. B. k = 0: 39,59 / 42,00 / 44,41.
- Vorhersagen:
  - P0: K0 (88 bekannte unveraendert) (90 %)
  - P1: 8 Sprossen auf +-0,10 (60 %)
  - P2: Vorzeichenwechsel (85 %)
  - P3: k = 10 bei R 40,5 bis 42,5 (55 %)
  - P4: Rundungsproblem beseitigt (75 %)
- Aktive Agenten: HUELLEN-LEITER-2.

## HUELLEN-DIPOL gestartet (2026-10-02 15:41:32 CEST)

- Finn: "mach weiter". Karte RUNDE-19/huellen-dipol/KARTE.md (ab 15:41:05), Code-Agent auf cpu6, Zeitbox 120 min.
- Stille Dipol-Schwingungen (l = 1) im Zweifeldmodell.
  - Kontrolle: bewiesene M1-Dipolstelle 0,7544960184 / 1,8263420673 (BEWEIS-2).
  - Suche omega^2 0,80 bis 1,40 in E1.
- Vorhersagen:
  - D0: K1 (90 %)
  - D1: >= 5 Dipol-Stellen (75 %)
  - D2: fester R-Abstand (60 %)
  - D3: Abstand wie bei l = 0 auf +-15 % (50 %)
  - D4: kein Nachfolger der M1-Dipolstelle (75 %)
- Aktive Agenten: HUELLEN-LEITER-2 (cpu bis cpu4), HUELLEN-DIPOL (cpu6).

### Ernte HUELLEN-LEITER-2 (Agent fertig ~16:09; RUNDE-19/huellen-leiter-2/ERGEBNIS.md; ausgewertet 2026-10-02 16:09:08 CEST)

- **Nicht auswertbar nach der Kartenregel: K0 verfehlt.**
  - Die stabilisierte Kopplung (chi < 1e-12 -> 0) findet in den Paaren 0 bis 109 97 statt 88 Vorzeichenwechsel, auf
    beiden Stufen gleich.
  - Alle 88 bekannten Stellen sind an derselben Lage. Dazu kommen 9 Scheinwechsel (k = 3 bis 8, R = 27,9 bis 37,2), und
    15 der 88 haben den Zellen-Umlauf umgekehrt.
  - Gestoppt vor dem Suchbereich. P0 nicht eingetroffen; P1 bis P4 offen, die Sprossenregel ist **ungeprueft**.
- **Die stillen Stellen selbst bewegen sich nicht:** Newton-Nullstellen von W mit alter und neuer Kopplung stimmen fuer
  alle 88 auf 1e-13. Die Hintergruende bis R = 46,5 sind sauber (Q, E auf 4e-11).
- **Ursache (Hypothese des Agenten):**
  - Das Vorzeichen der Kenngroesse s wird von der wachsenden Mode bestimmt, die die chi-Kopplung in die c-Loesung
    saeht.
  - In Runde 18 sass diese Saat im Ballzentrum, wo c ein festes Vorzeichen hat. Der Schnitt verschiebt sie an den
    Schnittradius, wo c schwingt; darum kippen die oberen Kurven.
  - Dasselbe Bild erklaert den Zusammenbruch bei R ~ 40 in Runde 18: Rundungsrauschen mit zufaelligem Vorzeichen.
  - Besserer Weg: die Saat mit festem Vorzeichen erhalten (chi glatt und positiv fortsetzen) oder s saatfrei machen.
- **Nicht gewertete Beobachtung:** Ein Newton-Lauf von einem Scheinwechsel aus endete bei einer echten stillen Stelle
  mit R = 40,49, also im Suchbereich. Die Kurve ist nicht bestimmt.
  - Vorhergesagt war fuer k = 1 die Sprosse 40,51.
  - Das ist **kein** Befund. Es kontaminiert aber die Blindheit dieser einen Vorhersage fuer eine Folgekarte.
- Selbstanzeigen des Agenten:
  - Diagnose ueber einen eingefrorenen Nachtrag nach Laufbeginn
  - K0-Daten vor der formalen Wertung gesehen
  - lokal wc, sort, comm, timeout und ein awk ohne Programm (wirkungslos)
- **Lehre:** Bei stillen Stellen sind die **Lagen** (Nullstellen von W) robust, die **Vorzeichenzaehlung** (s) ist
  zerbrechlich. Vorhersagetests sollten lagebasiert sein.
- **Abschaetzung: weiter -> HUELLEN-LEITER-3:** lagebasierter Test.
  - Newton auf W von den vorhergesagten Sprossen aus, dazu Rechteck-Umlauf von W.
  - Gleiche Vorhersagen wie in HUELLEN-LEITER-2, unveraendert. Die kontaminierte Sprosse k = 1 bei 40,51 wird getrennt
    gewertet.

## HUELLEN-LEITER-3 gestartet (2026-10-02 16:10:00 CEST)

- Karte RUNDE-19/huellen-leiter-3/KARTE.md (ab 16:09:35), Code-Agent auf cpu bis cpu4, Zeitbox 90 min.
- Lagebasiert: Newton auf W an den unveraenderten Vorhersagen aus HUELLEN-LEITER-2, Rechteck-Umlauf von W.
- K0' an 12 bekannten Stellen; zweite Stabilisierung als Kontrolle.
- P1' (7 Sprossen auf +-0,10, 60 %) und P2' (Vorzeichenwechsel, 85 %). Die kontaminierte Sprosse k = 1 bei 40,51 wird
  getrennt gewertet.
- Aktive Agenten: HUELLEN-DIPOL (cpu6), HUELLEN-LEITER-3 (cpu bis cpu4).

### Ernte HUELLEN-DIPOL (Agent fertig ~16:30; RUNDE-19/huellen-dipol/ERGEBNIS.md; ausgewertet 2026-10-02 16:30:42 CEST)

Plan vor dem ersten Lauf eingefroren, kein Nachtrag. 24 min Rechenzeit auf cpu6.

| Nr | Vorhersage | Ausgang |
|---|---|---|
| D0 | K1: bewiesene M1-Dipolstelle auf 1e-6 | **eingetroffen**: 3e-8 / 5e-9, Rechteck-Umlauf -1 aufgeloest |
| D1 | >= 5 stille Dipol-Stellen in E1 | **eingetroffen**: 19 Stellen auf 5 chi-Kurven (omega^2 1,40 bis 0,80, R bis 19,4), beide Stufen auf <= 1e-8, Rechteck-Umlauf an allen 19 aufgeloest und gleich dem Zellen-Umlauf |
| D2 | fester R-Abstand (Streuung < 15 %) | **eingetroffen**: 2,49 / 2,26 / 2,37 (Streuung 3,6 bis 3,9 %); der Umlauf wechselt von Stelle zu Stelle |
| D3 | Abstand wie bei l = 0 auf +-15 % | **eingetroffen**: 1,7 bis 2,9 % groesser als bei l = 0 |
| D4 | kein Nachfolger der M1-Dipolstelle | **offen**: Die Fortsetzung brach bei lambda = 0,20 ab (Profil). Bis dahin lag die Stelle in E2 und war ab 0,05 nicht mehr still (T 0,036 / 0,20 / 0,92) |

- Nicht vorhergesagt: Die l = 1-Stellen liegen um 0,34 bis 0,47 eines Abstands weiter aussen in R. Neue chi-Kurven
  entstehen bei l = 1 etwa 2 Einheiten in R spaeter.
- Selbstanzeigen des Agenten:
  - BEWEIS-2 ganz gelesen, aber nur die freigegebenen Angaben benutzt
  - zwei Ordner nach Namen gelistet
  - lokal chmod, wc, sleep
  - D4-Codeteil nach dem Einfrieren und vor dem ersten D4-Lauf geaendert, Verfahren gleich
- **Bedeutung (vorab festgelegt):** Die Huelle traegt auch Dipol-Leitern. Der Mechanismus ist nicht an l = 0 gebunden, und
  die Sprossenregel ist fuer beide l dieselbe [H, im Modell gestuetzt].
- **Abschaetzung: weiter.** Moeglich als Naechstes:
  - l = 2
  - die Verschiebung um ~0,4 Abstaende als Phasenkorrektur der Regel (Schreibtisch: Zentrifugalphase l pi/2 / k?) [H]
  - D4 mit robuster Profilfortsetzung
- **Schreibtisch-Lesart der Leitung zur Verschiebung [H]:** Fuer die regulaere Welle im Inneren gilt
  j_l(kr) ~ sin(kr - l pi/2)/(kr). Die Phase ist bei l = 1 um pi/2 versetzt; das sind 0,5 Sprossenabstaende.
  - Gemessen 0,34 bis 0,47, vermutlich mit wachsendem R gegen 0,5 (Krummungskorrektur bei kleinem R).
  - Vorhersage fuer eine spaetere l = 2-Karte: Versatz ~ 1,0 Abstand, die l = 2-Sprossen faellen dann fast auf die
    l = 0-Sprossen, nur um eine verschoben.

### Ernte HUELLEN-LEITER-3 (Agent fertig ~16:51; RUNDE-19/huellen-leiter-3/ERGEBNIS.md; ausgewertet 2026-10-02 16:51:31 CEST)

Plan eingefroren 16:30:36. Zwei Nachtraege nach Laufbeginn, beide nur Diagnose. K0' ist formal ausgewertet, bevor die
Testlaeufe angesehen wurden.

- **K0' bestanden:**
  - 12 bekannte Stellen auf beiden Stufen, Lagen auf <= 1e-13, Umlauf mit dem Vorzeichen aus Runde 18.
  - Begruendete Abweichung vor dem Lauf: Die Lagen kommen aus dem Schnitt-Code, die Umlaufzeichen aus einer zweiten
    Variante (chi innen als sinh(m0 r)/r fortgesetzt), weil der Schnitt auf k = 3 den Umlauf dreht. An Nr. 74 und 83
    bestaetigt.
- **Sprossen:** Alle 8 vorhergesagten Sprossen sind gefunden, je **hoechstens 0,018** in R neben der Vorhersage.
  - Toleranz war +-0,10.
  - Je ein Rangabfall; Stufen auf <= 5,5e-10; Umlauf aufgeloest +-1.
  - Die kontaminierte Sprosse k = 1 liegt bei 40,506. Die in HUELLEN-LEITER-2 gesehene Stelle bei 40,49 war eine andere
    auf einer hoeheren Kurve; die Kontamination war also keine.
- **Formaler Ausgang:**
  - **P1' nicht eingetroffen.** Die zwei k = 3-Sprossen (39,765 und 41,912) verfehlen die Pflichtbedingung "Knotenzahl
    der c-Komponente wie in Runde 18 (2)". Unter dem Schnitt-Code ist sie 3, schon bei R 34 bis 39. Die Knotenzahl haengt
    wie das Vorzeichen an der Saat; mit der Fortsetzungsvariante ist sie 2 (nachtraegliche Diagnose).
  - **P2' eingetroffen:** Der Umlauf wechselt auf allen gewerteten Schritten.
  - Vorab festgelegte Bedeutung bei Nichteintreffen: "Die Regel gilt nur im bisherigen Bereich".
- **Selbstanzeige der Leitung:** Die Karte band die Kurvenzuordnung an "Knotenzahl wie im Vorlaeufer". Das ist eine von
  der Saat abhaengige Konvention; der Fehler beginnt in meiner Karte.
- **Lesart:**
  - Formal: nicht eingetroffen.
  - Sachlich, nachtraeglich: alle 7 unbelasteten Sprossen (und die achte) auf <= 0,018 getroffen. Die Regel sagt die
    Lagen offenbar sehr genau voraus.
  - Ich hebe die formale Wertung nicht selbst auf. Ob die k = 3-Sprossen auf Kurve k = 3 liegen, prueft ein frischer
    Leser mit einem unabhaengigen Kriterium (Stetigkeit von rho entlang der Kurve). Erst dann gibt es eine Lesart (Regel
    "Entscheidung nach Ausgang: erst Fremdstimme").
- Selbstanzeigen des Agenten:
  - |W|-Schwelle vorab begruendet auf 1e-9 gelockert (Rauschen bis 1,9e-10 an bekannten Stellen)
  - Rangabfall-Bedingung und Nachstarts
  - ein geschaetzter Zeitstempel in Nachtrag 2
  - lokal chmod, sleep, comm, basename; einmal kleintest.sh gelesen

### Fremdstimme zu HUELLEN-LEITER-3 (pruefer-opus 16:51:54 bis 17:04:27; RUNDE-19/huellen-leiter-3/FREMDSTIMME.md; eingetragen 2026-10-02 17:05:34 CEST)

- **Empfehlung: Lesart (a) mit Auflagen.** Die Leitung uebernimmt sie.
- Befund 1: Beide k = 3-Funde liegen auf k = 3, unabhaengig von der Knotenzahl geprueft.
  - rho laeuft glatt ueber den Uebergang; die Vorhersage nur aus Runde 18 liegt 4,9e-7 bzw. 2,5e-6 neben den Funden.
  - Die Nachbarkurven liegen >= 0,0122 entfernt.
  - Newton bewegte sich nur 1,1e-5 bzw. 3,8e-5.
- Befund 2:
  - Dass die Knotenzahl von der Codevariante abhaengt, ist belegt. Dass die Saat die Ursache ist, passt zu den Daten, ist
    aber nicht direkt gezeigt.
  - Die Knotenzahl ist auch innerhalb einer Variante kein Kurvenmerkmal: k = 4 wechselt bei R ~ 22 von 2 auf 4.
  - Mit dem Code aus Runde 18 haette die Bedingung sogar 4 von 8 Sprossen verworfen.
- Gegen (b): Die Regel wuerde nach dem Ausgang ersetzt, obwohl der Fehler vorab erkennbar war. Ausserdem wuerde die
  lockernde Abweichung (|W| <= 1e-9) behalten und nur die verschaerfende gestrichen, also einseitig.
- **Gueltige Lesart (L1 bis L3):**
  - Formal: **P1' nicht eingetroffen, P2' eingetroffen** (unveraendert).
  - **Sachaussage, nachtraeglich, Fremdstimme:** Alle 8 vorhergesagten Sprossen liegen auf der richtigen Kurve, hoechstens
    0,018 in R neben der Vorhersage. Das ist nicht als vorab bestandener Test zitierfaehig.
  - Den Satz "Die Regel gilt nur im bisherigen Bereich" nur mit seinem Ausloeser nennen: Ausgeloest hat ihn allein die
    Pflichtbedingung Knotenzahl; die groesste Lageabweichung ist 0,018 bei einer Schwelle von 0,3.
- **Auflage L4 -> Runde 20:** Ein neuer, vorab gewerteter Test mit neuen Sprossen. Die Kurve wird nur ueber Rang und
  Stetigkeit erkannt, und jede Pflichtbedingung wird vor dem Einfrieren mit genau dem Testcode an bekannten Stellen
  geprueft.
- Kleinkorrektur im ERGEBNIS von HUELLEN-LEITER-3: Der Abstand zur Zeilennullstelle bei 39,77 ist 2,86e-9, nicht
  "<= 1,2e-13". Hier vermerkt; ERGEBNIS bleibt als Agentenbericht unveraendert.

## Abschaetzung Runde 19 (Leitung, 2026-10-02 17:05:58 CEST)

| Karte | Ergebnis kurz | Abschaetzung |
|---|---|---|
| HUELLEN-LEITER-2 | nicht auswertbar (K0): Stabilisierung kippt die Vorzeichenzaehlung; Lagen unveraendert (1e-13) | erledigt; Lehre "Lagen robust, Vorzeichen zerbrechlich" |
| HUELLEN-DIPOL | 19 stille Dipol-Stellen auf 5 Leitern; Abstand wie bei l = 0 (+1,7 bis 2,9 %); Versatz ~0,4 Abstaende; D4 offen | weiter: l = 2 mit Versatz-Vorhersage ~ 1,0 Abstand |
| HUELLEN-LEITER-3 | formal P1' nicht, P2' eingetroffen; nachtraeglich (Fremdstimme) alle 8 Sprossen auf <= 0,018 | weiter: neuer vorab gewerteter Test (L4) |
| M_E-G3 (Codex) | offen, Codex seit 10:03 still | uebernommen |

**Lehren der Runde:**
- (1) Pflichtbedingungen eines Tests vor dem Einfrieren mit genau dem Testcode an bekannten Stellen pruefen
  (Fremdstimme L4). Das gilt fuer Karte und Plan.
- (2) Kurvenzuordnung nur ueber robuste Groessen (Rang, Stetigkeit), nie ueber konventionsabhaengige (Knotenzahl,
  Vorzeichen).
- (3) Eine Fremdstimme kann eine nachtraegliche Sachaussage tragen, ohne die formale Wertung zu aendern. So bleibt beides
  ehrlich.

## Einfach gesagt (Runde 19)

Der Q-Ball mit Huelle hat nicht nur stille Atmungs-, sondern auch stille Kippschwingungen, und beide ordnen sich auf
Leitern mit fast gleichem Sprossenabstand. Mit dieser Regel haben wir acht neue stille Stellen vorhergesagt, und alle
acht lagen fast genau dort. Weil eine meiner vorab gesetzten Pruefbedingungen ungeschickt war, zaehlt der Test formal
trotzdem nicht. Er wird deshalb in der naechsten Runde mit sauberen Regeln wiederholt.

## Rundenabschluss (Leitung, 2026-10-02 17:06:34 CEST)

- Journal: claude-runde-v3-19-20261002, Index nr 556; pruefen ohne Befund; Quellen-Hashes in RUNDE-19/journal-quellen.txt.
- Sicherung .69 -> TS440 gestartet (Log ...-r19.log); r18 siehe Ausgabe (rc oben).
- In Runde 20 uebernommen:
  - vorab gewerteter Sprossentest nach Auflage L4
  - l = 2 mit Versatz-Vorhersage
  - M_E-G3 (Codex)
