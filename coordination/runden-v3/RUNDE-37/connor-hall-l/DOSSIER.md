# DOSSIER CONNOR-HALL-L: Wer ist Connor Hall, und welche Theorien vertritt er? (feldforscher, Runde 47)

> **Hinweis (08:02, date):** Am Ende steht der "Nachtrag Conor Hall" (ab 08:00:54). Er ist massgeblich; die Abschnitte 1 bis 10 sind der Stand von 07:46.

- Auftrag: Finn (05.10.2026, kurz vor 07:25), woertlich: "Check Connor Hall Theorien im subagents". Bindend ist KARTE.md (CH0 bis CH4 unveraendert).
- Kennzeichen:
  - [E] Messung oder Rechnung (hier keine)
  - [M] Mathematik
  - [S] Fachquelle; [S API] direkte Datenbankantwort, [S Trefferliste] nur Titel, Adresse und Kurzfassung der Suchmaschine, Seite nicht geoeffnet
  - [L] Lehrbuch
  - [H] Hypothese
  - [P] Projektbefund mit Fundstelle
  - [ES] eigener Schluss
- Arbeitsdatei: ARBEITSFELD.md; Abrufprotokoll: ABRUFE.md (beide in diesem Ordner).
- Gliederung: 1 bis 10 wie im Auftrag; die Anhaenge A bis D (Regime, Kalibrierung, offene Fragen, Quellen) stehen vor "Einfach gesagt".

## 1. Zeiten, Abrufe, Websuche

- Start 2026-10-05 07:27:59 CEST (date).
- Dossier geschrieben ab 07:39:19, neu gegliedert ab 07:42:05 CEST (date). Ende nach dem Gegenlesen: 07:46:30 CEST (date). Laufzeit 18 min 31 s (07:27:59 bis 07:46:30), innerhalb der Zeitbox von 60 min.
- **Netzabrufe: 15 von 15** (Budget erschoepft), davon:
  - 8 Websuchen (Abrufe 1, 3, 4, 9, 10, 13, 14, 15)
  - 5 Fach-API-Abfragen: OpenAlex (2), Zenodo (5, fehlgeschlagen; 6), arXiv (7), INSPIRE (8)
  - 2 Seitenabrufe, beide umgeleitet ohne Inhalt (11, 12)
- **Die Websuche ging** (Test mit Abruf 1); das Suchbudget vom 04.10. war nicht mehr erschoepft.
- Lokale grep-Proben im Projekt (kein Netz), siehe 4.3, Zeile G3.

## 2. Ergebnis zuerst

1. **Kein Connor Hall mit eigenen physikalischen Theorien auffindbar.** Gesucht wurde in vier Fachdatenbanken (OpenAlex, Zenodo, arXiv, INSPIRE) und mit acht Websuchen [S API, S Trefferliste]. **CH0 verfehlt.**
   - Unter den Websuchen waren eine mit Video- und Podcast-Stichwoertern (dieselbe Suchmaschine, keine Suche auf den Plattformen selbst), eine mit den Schreibvarianten "Conor"/"Conner" und eine ohne Physik-Stichwort.
2. OpenAlex kennt sieben Profile zu diesem oder einem aehnlichen Namen (darunter "Connor P. Hall", "Connor Harry Hall", "Anne Hall Connor"), **keines mit Physik**: Mikrobiologie, Onkologie, Elektrokatalyse, Dermatologie, Materialchemie, Forstwesen und Raumfahrttechnik (1 Werk, 0 Zitate). Zenodo, arXiv und INSPIRE liefern je 0 Treffer [S API].
3. Die Suchmaschine ersetzt den seltenen Namen unscharf durch Physik-Nachbarn, auch bei Anfragen in Anfuehrungszeichen (Abrufe 3, 14): Connor Behan, Connor Dalton, Jack Connor, Lawrence J. Hall und andere. Drei scheinbare "Connor Hall"-Spuren waren andere Personen oder tote Seiten [S Trefferliste, ES].
4. **CH1 bis CH4 sind nicht entscheidbar**, weil keine Theorie vorliegt. Ueber der leeren Menge waeren CH1/CH2 formal "wahr" und CH3/CH4 "falsch" [M]; beides waere ein Artefakt und wird nicht gezaehlt.
   - Daraus folgt keine Testkarte und keine Einordnung gegen unser Programm.
5. **Naechster Schritt laut Karte:** Rueckfrage an Finn nach dem Link bzw. der Quelle (Plattform, Video, Buch, Gespraech). Es wird nicht geraten.

### 2a. Erwartungsverstoesse (das Wichtigste zuerst)

1. **Keine Physik in OpenAlex** (Abruf 2). Erwartet hatte ich 10 bis 40 Profile, davon 1 bis 3 mit Physik. Gefunden wurden 7 Profile ohne jede Physik.
   - Korrigierte Erwartung: Ein "Connor Hall" mit Physik-Theorien publiziert, wenn es ihn gibt, ausserhalb der indexierten Fachliteratur.
2. **Die Suchmaschine ersetzt den Namen** (Abrufe 3, 14). Erwartet hatte ich Namensgleiche, also gleicher Name, andere Person. Bekommen habe ich Namensersetzung: Physik-Nachbarn mit nur einem passenden Namensteil (Connor Dalton, Connor Behan).
   - Folge: Jede Spur muss an der Quelle geprueft werden (vgl. Memory "Suchtreffer-Zitat vor Vertrag an der Quelle lesen").
3. **Tote Seite im Index** (Abrufe 11, 12). Erwartet war eine lesbare NYIT-Projektseite; sie leitete auf eine 404-Seite um.
   - Der Index fuehrt tote Seiten; eine Namensverknuepfung im Index ist ohne die Seite wertlos.
- Kein Verstoss, aber eine Abweichung von der Kartenvorsicht: Die Websuche ging (E1 hatte beide Zweige vorgesehen).

## 3. Identifizierung mit Belegen

### 3.1 Fachdatenbanken (Regime A: starker Nullbefund)

| Datenbank | Abfrage | Ergebnis | Beleg |
|---|---|---|---|
| OpenAlex | Autorensuche "Connor Hall" | 7 Profile, keines mit Physik-Thema (Liste in ABRUFE Nr. 2) | [S API] Abruf 2 |
| Zenodo | creators.name "Hall, Connor" | 0 | [S API] Abruf 6 (Abruf 5: HTTP 400) |
| arXiv | au:"Connor Hall" | 0 | [S API] Abruf 7 |
| INSPIRE-HEP | a "Hall, Connor" | 0 | [S API] Abruf 8 |

- **Einschraenkungen [ES]:**
  - Die vier Indizes ueberlappen sich: OpenAlex nimmt arXiv und Zenodo auf, INSPIRE nimmt arXiv auf. Sie sind also keine vier unabhaengigen Belege.
  - Die exakten Namensformen decken Veroeffentlichungen unter Initialen ("C. Hall") nicht ab.
  - Die arXiv-Phrasenabfrage ist an keinem bekannten Namen kalibriert. Gegen ein reines Abfrageartefakt spricht, dass auch OpenAlex keinen Physik-Connor-Hall kennt.

### 3.2 Freies Netz (Regime B: schwacher Nullbefund)

| Abruf | Anfrage | Namensgenauer Treffer mit Theorie? |
|---|---|---|
| 1 | Connor Hall physicist theory | nein |
| 3 | "Connor Hall" physics | nein |
| 4 | "Connor Hall" theory universe gravity time | nein (nur Stichwortnachbarn ohne belegte Autorschaft) |
| 9 | "Connor Hall" new physics theory 2026 | nein (Pflichtsuche juengster Zeitraum, Regel 7) |
| 10 | "Connor Hall" YouTube OR TikTok OR podcast physics theory | nein |
| 13 | "Conor Hall" OR "Conner Hall" physics theory | nein (Schreibvarianten) |
| 14 | "Connor Hall" solitons holography | nein |
| 15 | "Connor Hall" theory (ohne Physik) | nein, in keinem Feld |

- **Einschraenkungen [ES]:**
  - Alle acht Anfragen liefen ueber dieselbe Suchmaschine und denselben Index; sie sind korreliert.
  - Videos und Beitraege in sozialen Medien (YouTube, TikTok, X, Instagram) sind darin vermutlich schlecht indexiert [H]. Der Nullbefund im Regime B ist deshalb schwach.

### 3.3 Physiknahe Kandidaten und Namensnachbarn

| Spur | Person laut Quelle | Bezug zu "Connor Hall" | Beleg |
|---|---|---|---|
| MPG.PuRe persons243583 | Connor Dalton (Max-Planck-Institut fuer Chemische Physik fester Stoffe) | anderer Nachname | [S Trefferliste] Abruf 3 |
| Acadia-Physikseminar, 28.11.2025 | Connor Behan (laut Trefferliste Postdoc am Perimeter Institute, Quantenfeldtheorie) | anderer Nachname | [S Trefferliste] Abrufe 1, 14 (PDF-Dateiname) |
| NYIT "Broader Impacts for NSF Grant RUI: Solitons in Holography" | unbekannt | Namensbezug unbelegt; Seite geloescht (Umleitung auf 404) | Abrufe 10 bis 12 |
| UConn "Physics major wins national recognition for research" | Name nicht in der Trefferliste | unaufgeloest (kein Budget) | [S Trefferliste] Abruf 1 |
| Indico IHEP 28588, Indico Edinburgh 377 | unbekannt | unaufgeloest (kein Budget) | [S Trefferliste] Abruf 9 |
| Nachhilfe-Profil (varsitytutors.com) | ein "Connor" mit Physik-Bachelor; Nachname nicht in der Trefferliste | unaufgeloest; kein Hinweis auf eine eigene Theorie | [S Trefferliste] Abruf 3 |
| Namensnachbarn | Jack Connor (Plasmaphysik, Bootstrap-Strom im Tokamak), Lawrence J. Hall (Berkeley), Geoff Hall (Imperial College), Trevor Hall (Ottawa, Ingenieurfakultaet), Raymond Hall (Fresno State), Dean Connor (Doktorand NC State, medizinische Bildgebung), Conner Behan (Bootstrap, Holografie; ob dieselbe Person wie Connor Behan, ist nicht geprueft), Pierre Conner und Gregory Conner (Mathematik) | nicht "Connor Hall" | [S Trefferliste] Abrufe 1, 3, 10, 13 |
| andere Felder | Anthony J. Hall (laut Trefferliste Verschwoerungsthesen zu 9/11), Chris Connor (forscht ueber Verschwoerungstheorien) | nicht "Connor Hall"; keine Physik | [S Trefferliste] Abruf 15 |

- **Welcher Kandidat ist gemeint?** Keiner ist eindeutig. Kein Kandidat traegt zugleich den Namen "Connor Hall" und eine eigene Physik-Theorie.
- Mehrere Physiker teilen nur einen Namensteil (Connor Behan, Connor Dalton, Jack Connor, Lawrence J. Hall). Einem von ihnen Finns Auftrag zuzuschreiben, waere Raten; das unterbleibt.
- **Privatdaten:** Keine gesammelt. Notiert sind nur Name, Zugehoerigkeit laut Quelle und Veroeffentlichungsort.

## 4. Je Theorie: Kernaussage, Stand, Vorhersagen, Unterscheidungspunkt, Pruefstand, Gegensweep

- **Keine Theorie identifiziert.** Kernaussage, Stand, Vorhersagen, Unterscheidungspunkt und Pruefstand bleiben leer; was hier stuende, waere erfunden.
- Der Gegensweep betrifft deshalb die Identifizierung (4.3).

### 4.1 Unterscheidungspunkt der Identifizierung (Regel 2) [ES]

- H-a: Es gibt keine oeffentliche Person dieses Namens mit Physik-Theorien. Der Name waere dann verhoert, vertippt oder verwechselt.
- H-b: Es gibt sie, aber in einem nicht indexierten Kanal (Video, soziale Medien, Vortrag, privat geteilter Text) oder unter anderer Namensform.
- Trennend ist allein Finns Quelle. Mit unseren Werkzeugen sind H-a und H-b empirisch nicht unterscheidbar; keine Seite wird bevorzugt.

### 4.2 Pruefraster fuer den Fall, dass Finn eine Quelle nennt [ES]

- Wo weicht die Theorie messbar von ART, Quantenmechanik oder Standardmodell ab, und gibt es dort Daten?
- Ist der Parameterbereich vorab festgelegt, mit einer Messabbildung? Das ist Codex' Massstab fuer L9 (LUECKEN-ABGLEICH Teil A L9 [P]).
- Vor jedem "widerlegt": Suche ueber die letzten 24 Monate.

### 4.3 Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendliche Annahme | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | Die Schreibweise "Connor Hall" stimmt | ja, Abruf 13 | "Conor Hall"/"Conner Hall": nichts |
| G2 | "Theorien" heisst Physik-Theorien | ja, Abruf 15 | auch ohne Physik-Stichwort keine "Connor Hall"-Theorie |
| G3 | Der Name kommt von aussen, nicht aus unseren eigenen Scout-Ausgaben | ja, lokal per grep, 07:35:54 bis 07:37:24 | siehe die Punkte unter der Tabelle [P] |
| G4 | Die Nullen in arXiv, INSPIRE und Zenodo sind echt | teilweise | durch die OpenAlex-Ueberlappung gestuetzt [ES]; die arXiv-Phrasenform ist nicht kalibriert |
| G5 | Die Person publiziert unter vollem Vornamen | nein | Initialen ("C. Hall") nicht abgefragt |
| G6 | Es ist eine reale Person, kein Kanalname, kein Pseudonym und keine Figur | nicht pruefbar | braucht Finns Quelle |
| G7 | Ein Treffer in einer Namenssuche ist ein Namenstreffer | ja, nebenbei (Abrufe 3, 14) | **nein:** pure.mpg.de war Connor Dalton, Acadia war Connor Behan |

**G3 im Einzelnen:**
- "connor/conor/conner hall" bzw. "hall, connor" in coordination/ und model-lab/: einziger Treffer RUNDE-47.md Z. 16 und 30, also die Leitung mit Finns Auftrag.
- "Hall" als Wort: 0 Treffer in research-watch-20260910/papers.json und BERICHT.md, 0 in codex-ideation-20261005.
- Die Regex-Suche ueber die Scout-Archive (rund 2 GB) brach am 60-s-Deckel ohne Ausgabe ab. Die Archive sind nicht vollstaendig durchsucht.

## 5. Urteile CH0 bis CH4 nach Kartenwortlaut

| Nr | Wortlaut (Karte) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| CH0 | Eine Person Connor Hall mit eigenen physikalischen Theorien ist ueber Fachdatenbanken oder freie Seiten eindeutig auffindbar | 45 % | **verfehlt** | Fachdatenbanken: OpenAlex 7 Profile ohne Physik, Zenodo 0, arXiv 0, INSPIRE 0 (Abrufe 2, 6, 7, 8). Freie Seiten: 8 Websuchen ohne namensgenauen Treffer mit Theorie (Abschnitt 3.2). Das Urteil heisst "mit 15 Abrufen ueber diese Wege nicht auffindbar"; ueber die Existenz sagt es nichts. |
| CH1 | [H] Die Theorien sind nicht in begutachteten Physik-Fachzeitschriften erschienen (Preprint, Eigenverlag, Video oder soziale Medien) | 60 % | **nicht entscheidbar** | Es fehlt der Gegenstand: Keine Theorie ist identifiziert. Der negative Teil ("nicht begutachtet") passt zwar zum OpenAlex/INSPIRE-Nullbefund. Er folgt aber schon aus dem Scheitern von CH0, ist also vorab ableitbar und zaehlt nicht als Treffer. Den positiven Teil (Preprint, Video ...) stuetzt nichts: Zenodo und arXiv 0, kein Video gefunden. |
| CH2 | [H] Keine der Theorien macht eine quantitative Vorhersage, die von ART bzw. Standardmodell abweicht und mit vorhandenen Daten pruefbar ist | 65 % | **nicht entscheidbar** | Keine Theorie bekannt. Ueber der leeren Menge waere die Aussage leer wahr [M]; das wird nicht als "eingetroffen" gezaehlt. |
| CH3 | [H] Mindestens ein Kerngedanke ueberschneidet sich konkret mit Finns Netzbild | 55 % | **nicht entscheidbar** | Kein Kerngedanke bekannt. Ueber der leeren Menge waere die Aussage leer falsch [M]; das wird nicht als "verfehlt" gezaehlt. |
| CH4 | [H] Mindestens ein Gedanke laesst sich als kleiner Test auf unserem Netz rechnen | 35 % | **nicht entscheidbar** | wie CH3 |

**Bedeutung nach Kartenwortlaut:**
- **CH0 verfehlt:** "Ohne Link bleibt die Zuordnung offen" (KARTE.md). Damit geht die Rueckfrage an Finn, und es wird nicht geraten.
- **CH3 und CH4 nicht eingetroffen:** keine Testkarte aus Connor Halls Theorien.
- **CH2 nicht entschieden:** weder Ideengeber noch Pruefstein.

## 6. Bezug zu unserem Programm [H]

Ohne Inhalt laesst sich kein Bezug herstellen. Jede Zeile unten ist eine **Prueffrage fuer den Fall eines Links** [ES]. Keine Zeile ist ein Befund.

| Programmteil | Bezug heute | Prueffrage, falls Finn eine Quelle nennt |
|---|---|---|
| Finns Netz (Raum = Netz, Umklappen, 600-Zelle, Licht im Netz, TENSOR-EIS) | keiner | siehe die Punkte unter der Tabelle |
| Q-Baelle | keiner | Sind Teilchen dort Solitonen? Gilt eine Stabilitaetsbedingung vom Typ E < m\|Q\| (LUECKEN-ABGLEICH T2 [P])? |
| Spin-2-Kette, Glied 10 (Eindeutigkeit) | keiner | Rueckt die Theorie an der Eindeutigkeit der ART? Zwei Faelle, je mit eigener Datenseite (Memory project-art-spin2-kompass; RUNDE-45.md Z. 200 [P]): Bei **Stelle-artigen Zusatztermen** ist die Sub-Millimeter-Schranke einschlaegig. Bei **Lambda als Integrationskonstante** (unimodular/WTDiff) ist es die Datenseite "everpresent Lambda gegen DESI", die das Projekt bei Glied 10 fuehrt |
| Spin-2-Kette, Glied 7 (Spin >= 3) | keiner | Aendert sie die Drei-Graviton-Kopplung oder fuehrt sie hoehere Spins ein? Nach CEMZ (arXiv 1407.5597) verlangt eine veraenderte Drei-Graviton-Kopplung einen unendlichen Turm hoeherer Spins (Memory [P]); Hintergrund in RUNDE-45.md Z. 438 bis 440 |
| Luecken L1 bis L11 | keiner | Welche Luecke wuerde die Theorie fuellen? Zuerst L9 (festgelegter Parameterbereich mit Messabbildung), L10 (gemeinsame Wirkung) und L11 (Energie nach unten beschraenkt, kausales Anfangswertproblem) (LUECKEN-ABGLEICH Teil A [P]) |

**Prueffragen zu Finns Netz:**
- Ist der Raum dort diskret? Traegt das Netz lokale Kinematik, greift nach GEMEINSAMES-NETZ-v3, Abschnitt 1 der Satz von Marolf 2015: lineare Schwerewellen ja, Einstein-Schwerkraft nein [P; dort als "S laut Agent" gefuehrt].
- "Netz = Geometrie" ist dort laut Codex allein weder Gegenbeweis noch hinreichender Ausweg [P].
- Sagt die Theorie eine Lichtverlangsamung durch eine feste Laengenskala voraus, ist ein Abgleich mit den LHAASO-Schranken noetig.
  - Fuer unsere Netze ergab er l < 5,9e-28 m (Zufallsnetz) bzw. 7e-28 m (regelmaessig), bedingt (LUECKEN-ABGLEICH L8 [P]).
  - Fuer eine fremde Theorie haengt die Zahl an deren Dispersionsform.

## 7. Kartenvorschlag (hoechstens zwei; hier einer)

### K1: CONNOR-HALL-L2 (nur nach Finns Antwort auf R1)

- **Frage:** Was behauptet die von Finn genannte Quelle? Wie urteilen CH1 bis CH4, wenn die Leitung sie vor dem Lesen der Quelle mit frischen Wahrscheinlichkeiten neu setzt?
- **Rahmen:** feldforscher, hoechstens 10 Abrufe, 45 min.
  - Die Quelle selbst zuerst lesen.
  - Danach Gegensweep nach Kritik der letzten 24 Monate.
  - Zum Schluss das Pruefraster aus 4.2 und Abschnitt 6.
- **Ableitbarkeitsprobe:**
  - *Vorab ableitbar* (Schreibtisch, keine Messung):
    - Sagt die Theorie eine Lichtverlangsamung durch eine feste Laengenskala voraus, ist der Abgleich mit den LHAASO-Schranken eine Umrechnung. Fuer unsere Netze steht er in L8 [P]; fuer die fremde Theorie folgt er aus deren Dispersionsform.
    - Sagt sie Abweichungen vom Newton-Gesetz bei kurzen Abstaenden voraus, ist der Abgleich mit der Sub-Millimeter-Schranke (Glied 10) Literaturabgleich.
    - Beides darf nicht als Test auf unserem Netz gelten.
  - *Nicht ableitbar:*
    - Identitaet und Inhalt der Theorie
    - ob ein Kerngedanke eine Groesse liefert, die wir auf unserem Netz messen koennen (CH4)
- **Abbruch:** Ist die Quelle ohne Groessen (rein qualitativ), endet die Karte mit "Ideengeber" oder "kein Bezug", ohne Rechenlauf.

### Kein zweiter Vorschlag

Ohne Inhalt waere jede zweite Testkarte erfunden. Die offenen Spuren (UConn, Indico IHEP und Edinburgh) lohnen eine Karte nur, wenn Finn bestaetigt, dass er Nachwuchs- oder Fachforschung meint.

## 8. Negativliste: Saetze, die wir nicht behaupten duerfen

1. "Connor Hall existiert nicht" oder "Es gibt keinen Connor Hall mit Physik-Theorien." Zulaessig ist nur: mit 15 Abrufen ueber vier Fachdatenbanken und eine Suchmaschine nicht auffindbar.
2. "Connor Halls Theorien sind widerlegt", "unserioes" oder "nicht begutachtet." Ihr Inhalt ist nicht bekannt.
3. "CH1 und CH2 sind eingetroffen" (leer wahr; CH1 folgt vorab aus dem Scheitern von CH0) oder "CH3 und CH4 sind verfehlt" (leer falsch).
4. "Finn meinte Connor Behan", "Jack Connor", "Lawrence Hall" oder irgendeine andere Person.
5. "Die NYIT-Seite zu Solitonen in der Holografie nannte einen Connor Hall." Das ist unbelegt, die Seite ist geloescht.
6. "Der Name stammt nicht aus unseren Scout-Daten." Zulaessig ist nur: in den gelesenen Scout-Dateien und in coordination/ sowie model-lab/ nicht gefunden; die Scout-Archive sind nicht vollstaendig durchsucht.
7. "Acht Websuchen sind acht unabhaengige Belege." Sie sind korreliert (dieselbe Suchmaschine).
8. "Connor Behan oder Connor Dalton vertreten eigene Theorien." Dazu wurde nichts geprueft.

## 9. Selbstanzeigen

1. **Geschaetzte Zeiten geschrieben, dann berichtigt:**
   - ABRUFE Nr. 1 ("07:28:45 (ca.)") habe ich per sed ueberschrieben statt durchgestrichen. Das verletzt die Regel "streichen statt loeschen"; die alte Fassung steht nur hier.
   - Im ARBEITSFELD standen "07:29:4x" (E3) und "07:2x" (Kontext). E3 ist ebenfalls per sed ersetzt (gleicher Verstoss), der Kontext-Stempel durchgestrichen.
2. **Zeitangaben sind Klammern:**
   - Die Zeiten in ABRUFE.md sind date-Klammern (vorher/nachher), keine exakten Abrufzeiten.
   - Bei den Erwartungen E1 bis E15 steht der letzte date-Stempel davor. Geschrieben wurde jede Erwartung zwischen diesem Stempel und dem Abruf.
3. **E9 wich vom Plan ab:** Die gesendete Anfrage war anders formuliert als die notierte. Im ARBEITSFELD ist das durchgestrichen und berichtigt.
4. **3 von 15 Abrufen ohne Inhalt verbraucht:**
   - Zenodo HTTP 400, vermutlich durch meine Parameterwahl: size=50 oder das unkodierte Komma. Beim zweiten Versuch habe ich beides zugleich geaendert, die Ursache ist also nicht getrennt [H].
   - zwei NYIT-Umleitungen
   - Dadurch blieben UConn und Indico ungeprueft.
5. **Gelesen hat ein Hilfsmodell:** Treffer wurden ueberwiegend nur als Trefferliste gelesen (Titel, Adresse, Kurzfassung des Suchwerkzeugs). Die API-Antworten hat das Abrufwerkzeug von einem kleinen Modell lesen lassen, nicht als Rohtext. Ein Name tief in einer Seite koennte so entgehen.
6. **Zu starke Saetze im ARBEITSFELD, dort berichtigt:**
   - "Vier unabhaengige Indizes" (sie ueberlappen sich)
   - "neun" statt acht Websuchen
   - In der Kandidatentabelle und bei Ergebnis 14 waren Angaben zu "Connor Behan" und "Conner Behan" vermengt.
7. **Erwartungsverstoss Nr. 2 erst nachtraeglich eingestuft:** Die Namensersetzung stand zur Zeit des Abrufs im ARBEITSFELD nur als "Nebenbefund". Als Verstoss eingestuft habe ich sie erst in der Synthese; die Einstufung ist dort mit Zeit vermerkt.
8. Eine breite Regex-Suche ueber die Scout-Archive brach am 60-s-Deckel ab und wurde nicht wiederholt.
9. Die Endzeile nannte zuerst eine falsche Restzeit ("rund 21 Minuten unter der Zeitbox"; richtig sind gut 41). Vor der Abgabe berichtigt.
10. **Ausschlussliste nicht in jedem grep:** Die greps auf RUNDE-47.md, papers.json und BERICHT.md (einzeln benannte Dateien) sowie der grep ueber codex-ideation-20261005 liefen ohne die volle Pflicht-Ausschlussliste (nur --exclude-dir=VERSIEGELT und --exclude=*VERSIEGELT* bzw. gar keine). Die Nachpruefung um 07:46:48 per find ergab in codex-ideation-20261005 keine Pfade mit VERSIEGELT, vertraege-20260925, ks-1-dk-lauf(e) oder T8-SOLL-*. Versiegeltes wurde nicht beruehrt; der Regelverstoss bleibt.

## Anhang A: Regime, Moderatoren, Kopplungsgroesse

- **Regime A, Fachdatenbanken:** starker Nullbefund. Moderator ist der Publikationskanal (begutachtet, Preprint, Datensatz).
- **Regime B, freies Netz:** schwacher Nullbefund. Moderatoren:
  - Indexierung der Plattform (Video und soziale Medien schwach)
  - unscharfe Namensersetzung
  - tote Seiten
- **Kopplungsgroesse (Regel 6) [ES]:** Drei Wege fuehren zu "nicht gefunden": ein in der Physik seltener Name, die Namensersetzung und schlecht indexierte Plattformen. Gemeinsam ist ihnen die Sichtbarkeit im Index.
  - Mehr Abrufe ueber dieselben Indizes aendern sie nicht; nur Finns Quelle umgeht sie.

## Anhang B: Kalibrierung

- **(a) gemessen:** 15 Abrufe mit den Zaehlungen in ABRUFE.md: OpenAlex 7 Profile ohne Physik; Zenodo, arXiv und INSPIRE je 0; 8 Websuchen ohne namensgenauen Theorie-Treffer.
- **(b) nuetzlich verdichtet:**
  - "ueber Fachdatenbanken nicht auffindbar" (stark)
  - "ueber eine Suchmaschine nicht auffindbar" (schwach)
- **(c) gewachsene Gewissheit ohne neue Evidenz:**
  - Meine Sicherheit, dass es diese Person nicht gibt, stieg mit jeder Nullsuche. Die Suchen sind aber korreliert. **Warnzeichen**; deshalb steht nirgends "existiert nicht".

## Anhang C: Offene Fragen (wandern mit)

- **R1 an Finn:** Wo hast du "Connor Hall" gesehen (Link, Plattform, Video, Buch, Vortrag, Gespraech)? Ging es um Physik oder ein anderes Feld?
- R2 (intern): Spuren UConn (physics.uconn.edu/?p=4935), Indico IHEP 28588 und Indico Edinburgh 377 sind ungeprueft.
- R3 (intern): Initialen-Suche ("C. Hall" mit Physikthemen) ist nicht gelaufen.
- R4 (intern): Die arXiv-Phrasenabfrage au:"Vorname Nachname" ist an einem bekannten Namen nicht kalibriert.

## Anhang D: Quellenliste

**Fachdatenbanken [S API]** (alle abgerufen am 05.10.2026):
- OpenAlex (2026). Autorensuche "Connor Hall". https://api.openalex.org/authors?search=Connor%20Hall&per_page=50&select=id,display_name,works_count,cited_by_count,last_known_institutions,topics
- Zenodo (2026). Records, creators.name "Hall, Connor". https://zenodo.org/api/records?q=creators.name:%22Hall%2C%20Connor%22&size=20
- arXiv (2026). API, au:"Connor Hall". http://export.arxiv.org/api/query?search_query=au:%22Connor%20Hall%22&max_results=50
- INSPIRE-HEP (2026). Literatur, a "Hall, Connor". https://inspirehep.net/api/literature?q=a%20%22Hall%2C%20Connor%22&size=25&fields=titles,authors.full_name,authors.affiliations,collaborations,publication_info,arxiv_eprints,earliest_date

**Seiten** (nur Trefferliste [S Trefferliste], nicht geoeffnet, ausser wo vermerkt):
- New York Institute of Technology (o. J.). "Broader Impacts for NSF Grant RUI: Solitons in Holography". https://www.nyit.edu/event/source/manoj_avarna. Geoeffnet: Umleitung auf 404.
- Acadia University Physics (2025). Physics Seminar Acadia, 28.11.2025, Connor Behan (PDF; nur der Dateiname). https://physics.acadiau.ca/files/sites/physics2020/Other%20Files/Physics%20Seminar%20Acadia%20November%2028%202025%20Connor%20Behan.pdf
- MPG.PuRe (o. J.). Researcher Portfolio persons243583, laut Trefferliste Connor Dalton. https://pure.mpg.de/cone/persons/resource/persons243583
- University of Connecticut Physics (o. J.). "UConn Physics major wins national recognition for research". https://physics.uconn.edu/?p=4935
- Indico IHEP, Event 28588: https://indico.ihep.ac.cn/event/28588/event.ics
- Indico Edinburgh, Event 377: https://indico.ph.ed.ac.uk/event/377/
- Wikipedia. "Jack Connor (physicist)". https://en.wikipedia.org/wiki/Jack_Connor_(physicist)
- Wikipedia. "Lawrence John Hall". https://en.wikipedia.org/wiki/Lawrence_John_Hall
- Wikipedia. "Geoff Hall (physicist)". https://en.wikipedia.org/wiki/Geoff_Hall_(physicist)
- Brookhaven National Laboratory (Upload-Pfad 2021/09). PDF "Dean.pdf" (laut Trefferliste Dean Connor, NC State). https://wpw.bnl.gov/asap/wp-content/uploads/sites/5/2021/09/Dean.pdf
- Varsity Tutors (o. J.). Nachhilfe-Profil eines "Connor" mit Physik-Bachelor. Die Profiladresse ist bewusst nicht aufgenommen: Privatperson ohne Bezug zum Auftrag.
- Universite d'Ottawa (o. J.). Verzeichnis, Trevor Hall. https://www.uottawa.ca/faculte-genie/ecole-science-informatique-genie-electrique/repertoire/trevor-hall
- Southeast University (2024). Seminar Conner Behan, "Conformal defects: A bridge between local and nonlocal physics". https://yauc.seu.edu.cn/2024/1009/c27642a505756/page.htm
- KVPR (2018). Fresno-State-Physiker Raymond Hall. https://www.kvpr.org/science/2018-11-27/how-a-fresno-state-physicist-got-more-instagram-followers-than-neil-degrasse-tyson
- KY3 (2025). Chris Connor (University of Missouri) zu Verschwoerungstheorien. https://www.ky3.com/2025/12/19/ky3-digital-extra-univ-missouri-professor-uncovers-fact-fiction-conspiracy-theories/
- Scientific American (o. J.). "The Conspiracy Theory Director" (laut Trefferliste Anthony J. Hall). https://www.scientificamerican.com/article/the-conspiracy-theory-director/

**Projekt [P]:**
- KARTE.md (dieser Ordner)
- RUNDE-47.md Z. 16 und 30
- RUNDE-44/GEMEINSAMES-NETZ-v3.md, Abschnitt 1 (Marolf 2015, Codex-Vorbehalt)
- RUNDE-46/LUECKEN-ABGLEICH-20261005.md: Teil A L1 bis L11, Teil B T2
- RUNDE-45.md Z. 200 und 438 bis 440
- Memory project-art-spin2-kompass (Glieder 10 und 7, CEMZ arXiv 1407.5597)

## 10. Einfach gesagt

Wir haben einen Connor Hall gesucht, der eigene Physik-Theorien hat: in vier Wissenschaftsdatenbanken und mit acht Internetsuchen. Gefunden haben wir sieben Eintraege zu diesem oder einem aehnlichen Namen, aus Medizin, Chemie, Technik und Forstwirtschaft, aber niemanden mit Physik-Theorien. Die Suchmaschine hat uns mehrmals andere Physiker mit nur aehnlichem Namen untergeschoben, zum Beispiel Connor Behan. Daraus folgt nicht, dass es die Person nicht gibt, denn Videos und Beitraege in sozialen Medien findet so eine Suche schlecht. Deshalb brauchen wir von Finn den Link, wo er den Namen gesehen hat; wuerden wir raten, pruefen wir womoeglich die falsche Person.

---

# Nachtrag Conor Hall (ab 08:00:54 CEST, date)

**Massgeblich ist ab hier dieser Nachtrag.** Die Abschnitte 1 bis 10 bleiben als Stand von 07:46 unveraendert stehen. Ueberholt sind:
- Abschnitt 2, Punkt 5, und Anhang C, R1 (Rueckfrage nach dem Link)
- Abschnitt 5 (Urteile CH1 bis CH4 "nicht entscheidbar")
- Abschnitt 7, K1 (CONNOR-HALL-L2)

## N1. Anlass, Zeiten, Abrufe

- **Finns Hinweise (ueber die Leitung, woertlich):**
  - "Conor hall ist ein 18 jähriger der komplexe Strukturen untersucht hat"
  - "Ein ggf Youtuber oder so jetzt am MIT"
- **Beide Leitungsnachrichten** stehen woertlich im ARBEITSFELD ("Zusatz der Leitung"); aufgenommen um 07:47:42 (date).
- **Budget:** +10 Abrufe, hoechstens 25 insgesamt; Zeitbox bis 08:57:59.
  - Verbraucht: Abrufe 16 bis 25, damit **25 von 25**.
  - Davon 7 Websuchen (16, 17, 19, 20, 22, 23, 25) und 3 Abrufe per WebFetch: arXiv-API (18), Regeneron-PDF (21, Zeitueberschreitung), arXiv-PDF (24).
  - Das Papier habe ich lokal ganz gelesen (Seiten 1 bis 26), ohne weitere Netzabrufe.
- **Ende Phase 2:** 08:03:59 CEST (date), nach dem Gegenlesen des Nachtrags. Laufzeit gesamt 07:27:59 bis 08:03:59, innerhalb der verlaengerten Zeitbox (bis 08:57:59).
- **Ablage:** Primaerquelle als quellen/arxiv-2607.28711v1.pdf (SHA-256 c20df0785c3fe00a2b2f4940a6dd7b970527e877d8885a1e4d77ae5bd7d58b22).

## N2. Ergebnis zuerst

1. **Gemeint ist sehr wahrscheinlich Connor Hill [H].** Er gewann mit 17 Jahren den ersten Preis der Regeneron Science Talent Search 2026 (250 000 USD), mit dem Projekt "The Complete Set of Noble Polyhedra" [S Trefferliste, Society for Science].
   - Das Werk liegt als arXiv-Preprint vor: Hill 2026, arXiv:2607.28711 [math.CO] [S].
   - Name ("Hall" statt "Hill"), MIT und YouTube sind **nicht** belegt. Finn sollte das bestaetigen.
2. **Das Werk ist Mathematik, keine physikalische Theorie** [S].
   - Es ist eine rechnergestuetzte, vollstaendige Aufzaehlung der edlen Polyeder, also der Vielflaechner, deren Symmetrien alle Ecken und alle Flaechen ineinander ueberfuehren.
   - Ergebnis: Neben den unendlichen Familien der Stephanoide und Disphenoide gibt es genau 146 (bis auf Aehnlichkeit).
   - **Damit bleibt CH0 verfehlt.**
3. **Urteile nach Kartenwortlaut** (bedingt auf Finns Bestaetigung):
   - CH1 teilweise
   - CH2 eingetroffen, aber trivial
   - CH3 teilweise (nur geometrische Bausteine: Tetraeder, Vorzeichen-Volumen, Disphenoide)
   - CH4 eingetroffen (methodisch, modellintern)
4. **Uebertragbarer Gedanke:** Hill ersetzt Probieren durch eine vollstaendige Aufzaehlung, mit drei Schritten:
   - Symmetriebahnen
   - Nullstellenmengen von Tetraedervolumen-Polynomen
   - Resultanten
   - Bei uns fand ISO-ATEM-1 zwei isotrope Atemformen nur aus 600 Zufallsstarts; ob es mehr gibt, ist offen. Kartenvorschlag ATEM-VOLLZAEHLUNG-1 (N8).
5. **Keine Kritik und kein Fehlerbericht gefunden** (Werk vom Juli 2026, also ganz im 24-Monats-Fenster).
   - Zwei unabhaengig von dritter Seite gefundene Polyeder stehen in Hills Liste.
   - Die Teilsummen ergeben 146 [M].
   - Eine unabhaengige Gesamtpruefung ist nicht belegt.

## N3. Erwartungsverstoesse Phase 2 (das Wichtigste zuerst)

1. **Namensersetzung als Signal statt Rauschen (Abruf 20).**
   - In Phase 1 waren alle Ersetzungen der Suchmaschine Rauschen (Behan, Dalton). Erwartet hatte ich bei Abruf 20 wieder Rauschen oder einen namensgenauen Treffer.
   - Hier fuehrte die Ersetzung "Conor Hall" -> "Connor Hill" vermutlich genau zur gemeinten Person.
   - Regel 1, zwei Regime, Moderator ist die Verlaesslichkeit des vorgegebenen Namens: Ist der Name richtig, ist eine Ersetzung Rauschen. Ist er verhoert, kann die Ersetzung der einzige Weg zum Ziel sein.
2. **Mein Gegensweep G1 aus Phase 1 war zu eng.**
   - "Schreibweise geprueft" galt nur fuer "Conor/Conner Hall" zusammen mit "physics theory".
   - Die tatsaechliche Abweichung lag im Nachnamen (Hill) und im Fach (Mathematik). Gefunden hat sie Finns Hinweis, nicht mein Gegensweep.
3. **Das Abrufmodell konnte die PDF nicht lesen (Abruf 24).** Es lieferte eine Schein-Zusammenfassung, die Teile meiner Frage wiederholte (Brueckner, Gruenbaum, "61"). Nicht verwendet; das Papier habe ich selbst gelesen.
4. **Finns zwei Unterscheidungsmerkmale fanden sich nicht** (Abrufe 17, 23, 25): weder MIT (erwartet 50 %) noch YouTube (erwartet 35 %), auch nicht im Papier (keine Affiliation, Danksagung ohne MIT).

### N3a. Kalibrierung Phase 2

- **(a) gemessen bzw. an der Quelle gelesen:**
  - Inhalt des Papiers, Seiten 1 bis 26 [S]
  - Teilsummen = 146 [M]
  - Kleins zwei Funde in der Liste [S]
  - Preis, Alter 17 und Projekttitel nur aus Trefferlisten [S Trefferliste]
- **(b) nuetzlich verdichtet:**
  - "Das Werk ist Mathematik, keine Physik": stark, Primaerquelle.
  - "Connor Hill ist Finns Person": mittel. Alter und Thema passen; Name, MIT und YouTube nicht.
- **(c) gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):**
  - Mit jedem passenden Detail stieg meine Sicherheit, dass Connor Hill gemeint ist. Dazu zaehlen Kepler und "conic section" im Papier, passend zu Finns 06:05-Frage.
  - Kepler steht aber in fast jeder Polyeder-Einleitung, und die zwei harten Merkmale (MIT, YouTube) fehlen. Die Zuordnung bleibt [H].

## N4. Identifizierung mit Belegen

| Merkmal aus Finns Hinweis | Befund | Beleg |
|---|---|---|
| Name "Conor Hall" | weicht ab: Connor Hill (Vor- und Nachname anders geschrieben) | Abrufe 20, 22, 23; Papier S. 1 [S] |
| 18 Jahre | 17 laut Wettbewerbsmeldung (Fruehjahr 2026); 18 im Oktober ist moeglich, nicht belegt | [S Trefferliste] Abrufe 20, 22, 23 |
| "komplexe Strukturen untersucht" | passt: hochsymmetrische, oft nicht konvexe, sich selbst durchdringende Vielflaechner; vollstaendige Aufzaehlung | Papier S. 1, 21 [S] |
| "ggf Youtuber" | nicht belegt | Abrufe 16, 23, 25 |
| "jetzt am MIT" | nicht belegt; im Papier keine Affiliation | Abrufe 17, 23, 25; Papier S. 1, 22 [S] |

- **Ergebnis:** Wahrscheinlichster Kandidat ist Connor Hill [H]. Andere physik- oder mathematiknahe Kandidaten namens Conor Hall fanden sich nicht (Abrufe 13, 16, 17, 18, 19, 20).
- **Werk und Preis gehoeren zusammen:** gleicher Titel, gleicher Autorname (Abrufe 22, 23; Papier S. 1) [S].
- **Nur oeffentliches Werk aufgenommen:**
  - Wettbewerb und Preis
  - Preprint und Code-Repositorium (im Papier selbst als Ref. 16 genannt)
  - Presseberichte zum Werk
- **Bewusst nicht aufgenommen:** der Wohnort aus den Pressetexten und Berufsprofile anderer Personen gleichen Namens.

## N5. Das Werk: Hill (2026), "The complete set of noble polyhedra", arXiv:2607.28711v1 [math.CO]

- **Stand:**
  - arXiv-Preprint v1 vom 30.07.2026; die PDF ist auf den 3. August 2026 datiert.
  - Einzelautor, 26 und mehr Seiten mit Anhang A (Liste aller edlen Polyeder).
  - Begutachtete Zeitschriftenfassung nicht geprueft (kein Crossref-Abruf mehr).
  - Fachliche Aussenbewertung gibt es durch die Jury der Regeneron STS (erster Preis 2026) [S Trefferliste]. Das ist kein Zeitschriften-Gutachten.
- **Kernaussage [S]:**
  - Satz 1.1: Edle Polyeder mit prismatischer Symmetrie sind genau die Stephanoide (Kronenpolyeder) und die Disphenoide (Tetraeder mit vier kongruenten Flaechen). Alle anderen gibt es nur in endlicher Zahl.
  - Satz 1.2: Ohne diese beiden Familien sind es genau 146, bis auf Aehnlichkeit.
  - Polyeder sind dabei streng definiert: abstrakte Halbordnung vom Rang 3, realisiert in R^3; endlich, treu, ebene Flaechen, keine zwei kantenbenachbarten Flaechen in einer Ebene. Edel heisst ecken- und flaechentransitiv (Def. 2.1 bis 2.4).
- **Verfahren [S, S. 4 bis 20]:**
  - Jedes edle Polyeder entsteht als Bahn G(F) einer Flaeche F unter einer Punktgruppe G (Lemma 3.3).
  - Die Eckenmengen sind Bahnen von Punktgruppen: 23 nichtprismatische Bahntypen mit 0 bis 2 Parametern, 5 prismatische Klassen.
  - Ob vier Ecken in einer Ebene liegen, entscheidet eine 4x4-Determinante, das Sechsfache des Vorzeichen-Volumens des Tetraeders aus diesen Punkten (S. 10). In den Bahnparametern ist sie ein Polynom hoechstens dritten Grades.
  - "Kritische" Bahnen liegen auf den Nullstellen. Bei zwei Parametern sind das kubische ebene Kurven; ihre Schnittpunkte bestimmt er ueber Resultanten und Intervall-"Wurzelatlanten".
  - Endlich viele Aequivalenzklassen (Satz 3.23) machen eine endliche Rechnersuche moeglich.
  - Umsetzung in Python (sympy, numpy) und Wolfram Language. Code und 3D-Modelle sind oeffentlich (Ref. 16).
- **Vorhersagen:** keine physikalischen.
  - Die pruefbare Aussage ist mathematisch: Es gibt unter seinen Definitionen genau 146.
  - Widerlegbar waere sie durch ein edles Polyeder ausserhalb der Liste oder durch einen Listeneintrag, der eine Bedingung verletzt.
- **Unterscheidungspunkt (Regel 2):**
  - Ein echter Widerspruch zu frueheren Zaehlungen (2020 laut Presse 61 Einzelbeispiele bekannt; Mikloweit 2020) laege nur bei gleichem Polyederbegriff vor.
  - Hill schliesst V-Flaechen-Polyeder, Kranzpolyeder, Verbindungen und windschiefe Flaechen ausdruecklich aus (S. 3, 21 f.).
  - Regel 1: Der Begriff ist der Moderator; "146 gegen 61" ist kein Widerspruch, solange die Begriffe verschieden sind [ES].
  - Physikalisch gibt es keinen Unterscheidungspunkt zu ART oder Quantenmechanik, weil das Werk keine Physik behauptet.
- **Pruefstand:**
  - Der Code ist offen (nicht von mir geprueft).
  - Die zwei waehrend der Arbeit unabhaengig von Ben Klein gefundenen Polyeder stehen in der Liste (Tab. 8: sD-10.1, sD-12.1) [S].
  - Die Teilsummen je Bahntyp (S. 21) ergeben 146: 6 + 4 + 6 + 7 + 17 + 6 + 19 + 7 + 3 + 33 + 38 [M].
- **Grenzen laut Autor (Abschnitt 5.3) [S]:** unendliche Polyeder, nicht treue Realisierungen, windschiefe Flaechen (er vermutet Tausende bis Millionen), koplanare Nachbarflaechen, edle Verbindungen. Edle n-Polytope fuer n > 3 sind offen; in 4D ist der Rechenaufwand "immense" (Beispiel 120-Zelle).
- **Gegensweep (Kritik, Erwiderungen, Gegenbelege):**
  - Abruf 25 fand keine Kritik und keinen Fehlerbericht. Das Werk ist vom Juli 2026, liegt also ganz im 24-Monats-Fenster. Deshalb gilt: "nach Recherchestand keine Kritik gefunden", nicht "bestaetigt".
  - **Kleiner Gegenbeleg [M, eigene Rechnung]:** Auf S. 15 steht, jedes Dreieck sei Flaeche genau eines edlen Tetraeders (Disphenoid). Ein echtes, nicht flaches Disphenoid gibt es aber nur zu spitzwinkligen Dreiecken: V^2 = (a^2+b^2-c^2)(a^2-b^2+c^2)(-a^2+b^2+c^2)/72 > 0 genau dann [L/M]. Bei rechtwinkligen Dreiecken entartet es zum Rechteck, bei stumpfwinkligen gibt es keines.
  - Die Saetze 1.1 und 1.2 beruehrt das nicht (Satz 4.8 handelt von existierenden Polyedern). Es ist eine ungenaue Formulierung im Hintergrundtext.

### N5a. Gegensweep nach Regel 4 (Phase 2): Was war selbstverstaendlich?

| Nr | Annahme | geprueft? | Ergebnis |
|---|---|---|---|
| P1 | Connor Hill ist Finns Person | gegen Finns Angaben abgeglichen | Alter und Thema passen; Name, MIT und YouTube nicht; bleibt [H] |
| P2 | arXiv-Papier und STS-Projekt sind dasselbe Werk | ja | gleicher Titel, gleicher Autorname (Abrufe 22, 23; Papier S. 1) [S] |
| P3 | "146" stimmt | teilweise | Teilsummen [M] und Kleins zwei Funde [S] passen; keine unabhaengige Gesamtpruefung |
| P4 | Fruehere Zaehlungen sind vergleichbar | ja, am Text | nein: Sie haengen am Polyederbegriff (Def. 2.3/2.4 und Ausschluesse) [S] |
| P5 | Die Kepler/Kegelschnitt-Naehe zu Finns 06:05-Frage zeigt, dass Finn das Papier kannte | nicht pruefbar | Kepler ist ein Standard-Einstieg in Polyeder-Texte [ES] |

## N6. Urteile CH0 bis CH4 nach Kartenwortlaut (Nachtrag; bedingt auf Finns Bestaetigung der Person)

| Nr | Wortlaut (Karte) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| CH0 | Eine Person Connor Hall mit eigenen physikalischen Theorien ist ueber Fachdatenbanken oder freie Seiten eindeutig auffindbar | 45 % | **verfehlt** | (1) Unter "Connor Hall" und "Conor Hall" fand sich niemand mit Theorien (Abrufe 1 bis 19). (2) Der wahrscheinlich Gemeinte heisst Connor Hill und war erst ueber Finns Zusatzangaben und eine Namensersetzung der Suchmaschine auffindbar. (3) Sein Werk ist Mathematik (arXiv math.CO), keine eigene physikalische Theorie [S]. (4) Eindeutig ist die Zuordnung nicht: MIT und YouTube sind unbelegt |
| CH1 | [H] Die Theorien sind nicht in begutachteten Physik-Fachzeitschriften erschienen (Preprint, Eigenverlag, Video oder soziale Medien) | 60 % | **teilweise** | Die Form trifft zu: arXiv-Preprint, in keiner Physik-Zeitschrift. Fuer ein Mathematikwerk ist "nicht in einer Physik-Zeitschrift" aber trivial (aus dem Fach ableitbar), und eine physikalische Theorie ist es nicht. Ob eine Mathematik-Zeitschrift es begutachtet, ist nicht geprueft |
| CH2 | [H] Keine der Theorien macht eine quantitative Vorhersage, die von ART bzw. Standardmodell abweicht und mit vorhandenen Daten pruefbar ist | 65 % | **eingetroffen (trivial)** | Das Werk macht keine physikalischen Vorhersagen [S]. Das folgt schon daraus, dass es Mathematik ist, ist also vorab ableitbar und keine Messung. Kartenbedeutung: Ideengeber, nicht Pruefstein |
| CH3 | [H] Mindestens ein Kerngedanke ueberschneidet sich konkret mit Finns Netzbild (diskreter Raum, Geometrie als Grundlage, entstehende Schwerkraft, Licht als Netzwelle) | 55 % | **teilweise** | Konkret gemeinsam sind nur geometrische Bausteine, siehe die Punkte unter der Tabelle. Keine Ueberschneidung mit Raum als Physik, Schwerkraft oder Licht |
| CH4 | [H] Mindestens ein Gedanke laesst sich als kleiner Test auf unserem Netz rechnen, also als Groesse, die wir messen koennen | 35 % | **eingetroffen (methodisch, modellintern)** | Hills Kerngedanke ist die vollstaendige Aufzaehlung ueber Symmetriebahnen und Polynom-Nullstellen statt Stichprobe. Auf unser Netz uebertragen: Zahl und Symmetrie der isotropen Atemformen der 8-Tetraeder-Zelle (ISO-ATEM-1 fand 2 aus 600 Zufallsstarts [P]). Der Ausgang ist offen (N8). Der Gedanke ist nicht exklusiv Hills; Rechenalgebra kennt ihn allgemein [ES] |

**CH3, was konkret gemeinsam ist:**
1. Hills zentrale Groesse ist das Vorzeichen-Volumen von Tetraedern aus vier Ecken (S. 10). "Kritisch" heisst: ein solches Tetraeder wird flach. In Finns Netz sind entartende Tetraeder genau die Stellen, an denen Zellen umklappen koennen (Pachner) [H].
2. Disphenoide sind laut Hill die einzigen nicht regulaeren konvexen edlen Polyeder (S. 1, 15) [S]. Codex arbeitet im Projekt auf einem Disphenoid-Formraum (RUNDE-44.md Z. 231; RUNDE-46.md Z. 450) [P].

**Bedeutung nach Kartenwortlaut:**
- **CH0 verfehlt:** Die Zuordnung braucht Finns Bestaetigung (R1' unten).
- **CH2 eingetroffen:** Das Werk ist Ideengeber, nicht Pruefstein.
- **CH3 und CH4:** CH4 ist eingetroffen, CH3 nur teilweise. Daraus folgt hoechstens eine kleine, modellinterne Testkarte (N8), keine physikalische Pruefung.

## N7. Bezug zu unserem Programm [H]

| Programmteil | Bezug | Stufe |
|---|---|---|
| Finns Netz: Tetraeder, Umklappen | gemeinsamer Baustein ist das Vorzeichen-Volumen; Hills "kritische" Orte (ein Tetraeder wird flach) entsprechen den Stellen, an denen Pachner-Zuege moeglich werden | [H], Analogie, nicht gerechnet |
| Finns Netz: ISO-ATEM-1 (zwei isotrope Atemformen aus Zufallsstarts) | Hills Vollzaehlung ueber Symmetriebahnen koennte klaeren, ob es genau zwei sind | Kartenvorschlag N8 |
| 600-Zelle, 4D | regulaere 4-Polytope sind edel [M]; Hill nennt edle 4-Polytope als offene, sehr aufwendige Frage (S. 22) | Ideengeber, keine Karte |
| Codex' Disphenoid-Formraum (Lenia-Referenzmodell N4; A5-Papier) | siehe die Punkte unter der Tabelle | [S] + [P] + [M/ES], ungeprueft |
| Q-Baelle | kein Bezug | – |
| Spin-2-Kette, Glieder 10 und 7 | kein Bezug (keine Gravitationsaussage) | – |
| Luecken L1 bis L11 | keine direkt. Indirekt L3/T9, falls Atemkanaele als Pumpkanaele dienen (RUNDE-43.md Z. 314: "Pumpen ueber die isotropen Atemkanaele", Idee) | [H] |
| Finns 06:05-Frage (Bezout, Kepler, Kegelschnitte; RUNDE-46.md Z. 129) | siehe die Punkte unter der Tabelle | [H], unbelegt |

**Codex' Disphenoid-Formraum:**
- Disphenoide sind Hills edle Tetraeder [S].
- Eigene, ungepruefte Schreibtischnotiz [M/ES]:
  - Sie sind genau die Vier-Punkt-Lagen, die unter der Kleinschen Vierergruppe (Doppeltranspositionen, je als Halbdrehung verwirklicht) fest bleiben.
  - Nach Palais (1979) [L] sind kritische Punkte einer symmetrischen Energie auf dieser Fixpunktmenge auch im Ganzen kritisch.

**Finns 06:05-Frage:**
- Im Papier kommen Kepler (Sternpolyeder, Einleitung) und "conic section" (S. 12) vor; endliche Schnitte kubischer Kurven sind der Sache nach Bezout.
- Das Wort "Bezout" steht nicht im Text (S. 1 bis 26). Keplers Optik ist ein anderes Werk Keplers.

## N8. Kartenvorschlag (ersetzt K1; hoechstens zwei, hier einer)

### ATEM-VOLLZAEHLUNG-1: Gibt es in der 8-Tetraeder-Zelle von Finns Netz genau zwei isotrope Atemformen?

- **Frage:** ISO-ATEM-1 fand bei festem lambda nur zwei Loesungsarten (P2_13 etwa 55 %, Punktgruppe 222 etwa 45 %), aber nur aus 600 Zufallsstarts (ISO-ATEM-1/ERGEBNIS.md Z. 26 bis 29 [P]). Gibt es weitere, seltene Formen?
- **Weg (nach Hill, Abschnitt 3):**
  1. Fuer jede Symmetrie-Untergruppe H der Zelle die starren Drehungen der 8 Tetraeder auf wenige Bahnparameter reduzieren.
  2. Die Bedingungen (gemeinsame Ecken, F = lambda I) als Polynomsystem schreiben.
  3. Alle reellen Loesungen exakt aufzaehlen: Resultanten, Wurzelisolation; bei mehr Variablen Homotopie-Fortsetzung mit Bezout-Schranke als Startzahl [L].
  4. Klein heisst: nur Untergruppen-Systeme mit wenigen Parametern. Das volle System ohne Symmetrie ist eine eigene, groessere Frage.
- **Messgroesse:** Anzahl und Symmetrie der isolierten Loesungsfamilien bei lambda = 0,97 und einem zweiten lambda.
  - Erwartbarer Fehlerarm: eine dritte Form. Bestehensarm: genau zwei unter allen gerechneten Untergruppen.
  - Beide Ausgaenge sind moeglich, die Karte ist also nicht selbsterfuellend.
- **Ableitbarkeitsprobe:**
  - *Vorab ableitbar* (Kontrollen, keine Befunde):
    - die P2_13-Schar (Handformel lambda = (1 + cos phi_A + cos phi_B)/3, ISO-ATEM-1)
    - die Existenz der 222-Form (schon gefunden)
    - fuer hochsymmetrische Untergruppen moeglicherweise die ganze Loesungsmenge von Hand. Das muss vor der Karte am Schreibtisch geprueft werden.
  - *Nicht ableitbar:*
    - ob Formen mit niedrigerer Symmetrie (Gruppen 2, 3, 1) existieren
    - die Gesamtzahl isolierter Loesungsfamilien
  - Grenze: "keine dritte Form in den gerechneten Untergruppen" heisst nicht "keine dritte Form ueberhaupt".
- **Projektsuche (07:57:21):** kein ISO-ATEM-2, keine "dritte Atemform", keine Vollzaehlung im Projekt [P]. Gesucht wurde mit den Pflicht-Ausschluessen; die beabsichtigte Einschraenkung auf *.md griff nicht (Treffer auch in .xml, .json, .txt), die Suche lief also ueber alle Textdateien.
- **Bezug:** modellintern; Nutzen fuer das gemeinsame Netz (Atemkanaele) und indirekt PUMPE-NETZ-1 [H]. Keine Messdaten.

### Kein zweiter Vorschlag

Edle 4-Polytope und die 600-Zelle bleiben Ideengeber, ohne Karte. Hill selbst nennt den 4D-Aufwand "immense", und eine physikalische Frage ist daraus nicht abgeleitet.

## N9. Negativliste Nachtrag (Saetze, die wir nicht behaupten duerfen)

1. "Conor Hall ist Connor Hill." Nur [H]; Finn muss bestaetigen.
2. "Connor Hill ist am MIT" oder "Connor Hill ist YouTuber." Unbelegt.
3. "Connor Hill hat eine physikalische Theorie" oder "Seine Arbeit stuetzt Finns Netz." Nein: Es ist Mathematik, und der Bezug ist nur Ideengeber [H].
4. "Die 146 sind unabhaengig bestaetigt." Nicht gefunden. Belegt sind nur die Teilsummen [M] und Kleins zwei Funde in der Liste [S].
5. "Hill widerlegt fruehere Zaehlungen." Die Zahlen haengen am Polyederbegriff.
6. "Hill benutzt Bezout" oder "Finn hat das Papier gelesen." Beides nicht belegt.
7. "Die Disphenoid-Notiz loest Codex' Frage." Ungepruefte Schreibtischnotiz [M/ES].
8. Keine Alters-, Wohnort- oder sonstigen Personenangaben ueber das hinaus, was die Wettbewerbsmeldung zum Werk sagt.

## N10. Selbstanzeigen Nachtrag

1. Abruf 21 (Regeneron-PDF) lief in eine Zeitueberschreitung, Abruf 24 lieferte eine unbrauchbare Zusammenfassung. Belastbar wurde das Papier erst durch eigenes Lesen der abgelegten PDF.
2. Der Gegensweep G1 der Phase 1 galt als "geprueft", deckte aber nur Schreibweise mal Physik-Theorie ab (N3, Punkt 2).
3. Die Phase-2-Urteile habe ich nach dem Lesen des Werks geschrieben, nicht vorab. CH1 bis CH4 standen aber unveraendert in der Karte; neu ist nur ihre Anwendung auf das gefundene Werk.
4. Die Disphenoid- und Palais-Notiz sowie die Volumenformel sind eigene Schreibtischrechnungen, nicht gegengelesen.
5. Die Zeitangaben "07:4x" in den woertlich uebernommenen Leitungsnachrichten stammen von der Leitung, nicht von mir.
6. **Regelverstoss "lokal kein awk":** Zwischen 08:02:35 und 08:03:59 (date-Klammer) lief in einem Shell-Befehl versehentlich ein wirkungsloses awk-Fragment mit (awk 'NR>=0' /dev/null), ohne Eingabe und ohne Ergebnis. Es hat nichts gelesen oder geschrieben; der Verstoss bleibt.
7. **Ausschlussliste:** Der grep auf iso-atem-1/ERGEBNIS.md (eine einzelne, nicht versiegelte Datei) lief ohne die Pflicht-Ausschlussflags.

## N11. Offene Fragen (wandern mit)

- **R1' an Finn:** Meinst du Connor Hill, den Sieger der Regeneron STS 2026 mit "The complete set of noble polyhedra" (arXiv 2607.28711)? Falls ja: Wo hast du ihn gesehen (Video, Kanal, Artikel)? Das wuerde die Hinweise "YouTuber" und "MIT" klaeren.
- Offen und mit einem Abruf pruefbar [H]: ob es ein Video oder einen Kanal zum Werk gibt, etwa unter dem im Papier genannten Repository-Namen. Nur das, was die Forschung selbst zeigt.
- Begutachtungsstand (Crossref oder Zeitschrift) und eine unabhaengige Pruefung der 146 sind ungeprueft.

## N12. Quellen Nachtrag

- **Primaerquelle:** Hill, C. (2026). "The complete set of noble polyhedra". arXiv:2607.28711v1 [math.CO], 30.07.2026. https://arxiv.org/abs/2607.28711 (PDF: https://arxiv.org/pdf/2607.28711; lokale Kopie quellen/arxiv-2607.28711v1.pdf). Ganz gelesen [S].
- **Nur Trefferliste [S Trefferliste]:**
  - Society for Science (2026). Regeneron STS 2026 top awards. https://www.societyforscience.org/press-release/regeneron-sts-2026-top-awards/
  - Society for Science (2026). Finalistenseite Connor Hill. https://www.societyforscience.org/regeneron-sts/2026-student-finalists/connor-hill/
  - Society for Science (2026). 2026 STS winners. https://www.societyforscience.org/regeneron-sts/2026-sts-winners/
  - Regeneron (2026). How Student Math Research Connects to Modern Science. https://www.regeneron.com/stories/student-math-research-connects-modern-science
  - Regeneron (2026). Regeneron Science Talent Search 2026 recognizes America's top young scientists. https://investor.regeneron.com/news-releases/news-release-details/regeneron-science-talent-search-2026-recognizes-americas-top
  - Business Today (19.08.2026). "Meet Connor Hill ...". https://www.businesstoday.in/education/story/meet-connor-hill-the-17-year-old-who-cracked-a-3d-geometry-puzzle-and-won-rs2-39-crore-549922-2026-08-19
  - Wikipedia. "Noble polyhedron". https://en.wikipedia.org/wiki/Noble_polyhedron
  - Mikloweit, U. (2020). "Exploring Noble Polyhedra With the Program Stella4D". Bridges 2020, S. 257 bis 264 (Hill Ref. 15). https://2020.bridgesmathart.org/regular/257.html
- **Nicht lesbar:** Regeneron-Mitteilung (Zeitueberschreitung). https://newsroom.regeneron.com/node/31881/pdf
- **Nicht abgerufen:** Code laut Hill Ref. 16, https://github.com/Plasmath/noble-tools-revised
- **Gedaechtnis [L], nicht abgerufen:**
  - Palais, R. S. (1979). "The principle of symmetric criticality". Communications in Mathematical Physics 69, 19 bis 30.
  - Volumenformel des Disphenoids.
- **Projekt [P]:**
  - RUNDE-37/iso-atem-1/ERGEBNIS.md Z. 1 bis 40
  - RUNDE-43.md Z. 254 ff. und 314
  - RUNDE-44.md Z. 231
  - RUNDE-46.md Z. 129 und 450
  - RUNDE-47.md Z. 71

## N13. Einfach gesagt (Nachtrag)

Finns zweiter Hinweis hat geholfen. Gemeint ist sehr wahrscheinlich Connor Hill, ein Schueler, der 2026 den aeltesten und angesehensten US-Wissenschaftswettbewerb fuer Schueler im Abschlussjahr gewonnen hat. Er hat mit einem eigenen Computerprogramm bewiesen, dass es ausser zwei unendlichen Familien genau 146 "edle" Vielflaechner gibt, also Koerper, bei denen alle Flaechen gleich sind und alle Ecken gleich aussehen. Das ist Mathematik und keine neue Physik-Theorie; man kann damit keine Physik pruefen, aber gute Ideen holen. Eine Idee passt zu unserem Netz: Statt mit Zufallsversuchen nach Formen zu suchen, kann man wie er mit Symmetrie und Gleichungen alle Moeglichkeiten vollstaendig abzaehlen, zum Beispiel fuer die zwei bekannten "Atemformen" unseres Tetraeder-Netzes. Ob er wirklich Finns "Conor Hall" ist, muss Finn bestaetigen, denn Name, MIT und YouTube sind nicht belegt.
