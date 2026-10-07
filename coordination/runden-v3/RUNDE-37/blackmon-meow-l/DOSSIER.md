# BLACKMON-MEOW-L: Dossier (feldforscher fuer claude-primary)

- Karte: RUNDE-37/blackmon-meow-l/KARTE.md. Erwartungen der Leitung ab 15:45:45 CEST, vor jedem Abruf.
- Beginn 2026-10-04 15:46:28 CEST, Text ab 15:57:09 CEST (beides per date).
- Arbeitsdatei mit Vorhersage je Abruf, Protokoll und Gegensweep: ARBEITSFELD.md. Kopien in quellen/ (SHA256SUMS).
- Kennzeichen wie in der Karte:
  - [S] an der Quelle gelesen (Zeile der lokalen Kopie)
  - [P] Projektdatei, von mir gelesen
  - [L] Gedaechtnis, [L?] unsicher
  - [ES] eigener Schluss, [H] Hypothese
- Abrufe: 4 von 4. Den Aufsatz selbst (BLAAEM-3) konnte ich nicht lesen.

## Ergebnis zuerst

1. **Den Text von BLAAEM-3 habe ich nicht gelesen.**
   - PhilArchive sperrt Programme: Cloudflare-Seite "Just a moment...", HTTP 403 fuer curl und fuer WebFetch.
   - Das Internet Archive hat die Adresse nie aufgenommen (HTTP 404).
2. **Was BLAAEM-3 ist, sagt ein lokaler OpenAlex-Datensatz aus Runde 20 (02.10.) [P: OpenAlex].**
   - Die Adresse gehoert zum Aufsatz "An Epicurean Model of Time Dilation" von James C. Blackmon (San Francisco State
     University), Ancient Philosophy Today 7(1), S. 98-119, DOI 10.3366/anph.2025.0122.
   - OpenAlex fuehrt BLAAEM-3 als **eingereichte Fassung** ("submittedVersion"), nicht als Verlagsfassung.
3. **MEOW ist eine Vortragsreihe des Philosophie-Instituts der SFSU [S].**
   - Blackmon eroeffnete die "nach langer Pause" wiederbelebte Reihe am Freitag, 7. Maerz 2025, 15 bis 17 Uhr
     Pazifikzeit, per Zoom.
   - Titel: "Isotacheia: How the Epicureans Could Have Derived Time Dilation".
   - Die Seite hat ein inhaltliches Abstract. Der Vortrag lag 25 Tage vor dem Erscheinen des Aufsatzes (1. April 2025
     laut OpenAlex [P]; Tage per date in UTC gezaehlt).
4. **Soweit die Abstracts reichen, setzt Blackmon das gemeinsame Tempo voraus.**
   - Die Herleitung geht "from the Epicurean atomist doctrine of isotakheia" aus [P: OpenAlex-Abstract].
   - Eine Begruendung, warum alle Bausteine gleich schnell sind, steht in keinem der beiden Abstracts.
   - Er spricht von "(Epicurean) atoms" und rahmt das historisch ("could have anticipated"). Eine Forderung an heutiges
     Licht und heutige Materie stellt er dort nicht, und er sagt dieselben Messwerte wie die Relativitaetstheorie voraus.
5. **Fuer Finns Netz [ES]:**
   - Blackmon liefert keine Ursache, die das Netz uebernehmen koennte. Er liefert genau die Bedingung, die AETHER-UHR-1 als
     noetig gezeigt hat.
   - "Gleich im Mittel ueber Kantenlaengen" reicht nach einer Rechenskizze wohl nicht. Der Lorentz-Faktor ist nicht linear
     in der Geschwindigkeit, also geht auch die Streuung der Sprungtempi in den Uhrgang ein (Abschnitt 4.4).

## Erwartungen mit Ausgang

| Nr | Erwartung (Kurzform) | Ausgang | Fundstelle |
|---|---|---|---|
| E2 | PhilArchive- und Verlagsfassung unterscheiden sich hoechstens in Kleinigkeiten | **offen; das einzige Indiz spricht eher dagegen (schwach)** | OpenAlex: BLAAEM-3 = "submittedVersion" [P]. Solche Etiketten vergibt OpenAlex oft automatisch [L?]. Keine der beiden Fassungen habe ich gelesen |
| E3 | SFSU-Seite: Workshop MEOW mit Vortrag Blackmons zum Thema; Datum, Ort, Programm, keine weiteren Inhalte | **teilweise eingetroffen** | Workshop, Vortrag, Thema und Datum ja [S: Z. 252-282]. Ort ist Zoom, kein Raum [S: Z. 260-261]. Programm: ein Vortrag. **Gegen die Erwartung** steht dort ein Abstract mit Inhalt [S: Z. 284-286] |

## Erwartungsverstoesse (das Wichtigste zuerst)

1. **E4, erste Haelfte: Blackmon stellt (im Abstract) keine physikalische Forderung, sondern eine historische
   Moeglichkeitsaussage.**
   - Wortlaut: "the Epicureans could have anticipated time dilation measurements" [P: OpenAlex].
   - Er beansprucht dieselben Vorhersagen wie die Relativitaetstheorie ("precisely as our standard model predicts"),
     also keinen messbaren Unterschied.
   - Korrigierte Erwartung: Blackmon ist eine Quelle fuer eine Deutung, nicht fuer eine Vorhersage.
2. **Lokal lag mehr, als ich erwartet hatte.**
   - Der OpenAlex-Datensatz aus Runde 20 enthaelt das Abstract (als Wortindex, per jq zusammengesetzt).
   - Ausserdem: die Zuordnung BLAAEM-3 zum Werk, das Fassungsetikett und die Hochschule des Autors.
3. **E3: Die SFSU-Seite hat ein inhaltliches Abstract [S: Z. 285-286].**
   - Die Herleitung sei kurz, brauche "only basic algebra", und "all terms have direct physical interpretations".
   - Ort ist Zoom. Der Vortrag liegt vor dem Erscheinen des Aufsatzes.
4. **E2:** Die PhilArchive-Fassung ist nach OpenAlex die eingereichte Fassung, nicht die Verlagsfassung (schwaches Indiz).
5. **Zugang:** Meine Vorhersage fuer Abruf 2 setzte stillschweigend voraus, dass PhilArchive eine PDF liefert. Es kam
   eine Cloudflare-Pruefung. Dasselbe hatte Runde 20 schon fuer PhilPapers gemeldet (RUNDE-20 ERGEBNIS F7).

## Antworten auf die Fragen der Karte

### 1. Was genau behauptet Blackmon?

- **Kernaussage [P: OpenAlex-Abstract]:**
  - Aus der epikureischen Lehre der Isotacheia ("all (Epicurean) atoms have equal speed") lasse sich "a mathematical
    equivalent of the velocity Lorentz transformation" herleiten.
  - Die Herleitung sei "brief and classical" und brauche keine Mathematik, die den alten Griechen fremd waere.
- **Vortragsfassung [S: sfsu-meow.html Z. 286]:**
  - Die Epikureer haetten "a simple theorem of kinematics" nutzen koennen, um die heutigen Gleichungen der Zeitdehnung
    herzuleiten.
  - Das biete "an alternative explanation of this phenomenon".
  seinen Zustand langsamer, genau nach dem Lorentz-Faktor. Von mir nicht gelesen.
  und Roth. Wortlaut und Seite kann ich nicht liefern.
    OpenAlex-Volltextindex [P: RUNDE-20 ARBEITSFELD Z. 239-243].
  - **Wortlaut mit Seite: von mir nicht lieferbar.**
- **Schwerkraft:** nicht pruefbar.

### 2. Was ist der MEOW-Workshop?

- **Name und Herkunft [S: sfsu-meow.html Z. 15, 252]:** "Metaphysics, Epistemology, and Ontology Workshop (M.E.O.W.)",
  Veranstaltungsseite des Department of Philosophy der SFSU.
- **Wann und wo [S: Z. 254-261]:** Freitag, 7. Maerz 2025, 15:00 bis 17:00 Uhr Pazifikzeit, kostenlos, per Zoom. Den
  Wochentag habe ich per date geprueft.
- **Wer und was [S: Z. 281-286]:**
  - Die Reihe sei "back after a long break" und beginne mit einem Vortrag von "Professor James Blackmon".
  - Titel: "Isotacheia: How the Epicureans Could Have Derived Time Dilation".
  - Abstract: Myonzerfall, Uhren und Astronauten; Rossi-Hall (1941); eine Herleitung mit Grundalgebra, "classical and
    intuitive".
- **Was fehlt:** Kein weiteres Programm, keine Unterlagen, kein Link zum Aufsatz.
- **Hochschule:** Die Seite nennt Blackmons Hochschule nicht; laut OpenAlex ist es die SFSU [P]. Es war also ein Vortrag
  am eigenen Institut [ES].
- **Zusammenhang mit dem Aufsatz [ES]:**
  - Gleiches Thema, gleiche Herleitung, 25 Tage vor der Veroeffentlichung (1. April 2025 laut OpenAlex [P]).
  - Der Vortrag stellt den Aufsatz vor. Er ist keine eigene Quelle mit Zusatzinhalt.

### 3. PhilArchive- gegen Verlagsfassung

- Ohne weiteren Abruf ist nur das Metadatische sichtbar [P: OpenAlex]:
  - Verlag: "publishedVersion", S. 98-119, Bd. 7 Heft 1, DOI 10.3366/anph.2025.0122, bei OpenAlex nicht als frei gefuehrt.
  - PhilArchive (BLAAEM-3): "submittedVersion", frei.
- Schreibweise: Das Abstract schreibt "isotakheia", der Vortragstitel "Isotacheia" [P, S].
  auf.
- Inhaltliche Unterschiede: **nicht feststellbar.**

### 4. Bezug zu Finns Netz ([ES], wo nicht anders markiert)

**4.1 Isotacheia gegen "jeder Sprung eine Kante je Takt"**

  langsamer, weil seine Teile im Zickzack laufen; Pythagoras liefert den Lorentz-Faktor [P].
  - Die Bausteine "have no mass and orbit each other at the speed of light" (Z. 7).
  - Ihre Geschwindigkeit "has always to be c", und zwar gegenueber "the reference frame at rest" (Z. 53).
  - Das ist eine Annahme des Modells. Sie begruendet nicht, warum alle Sorten dasselbe Tempo haben.
- "Ein Sprung je Takt" (Feynman-Schachbrett, QCA) ist die Gitterform derselben Idee: Jeder Sprung geht mit dem
  Hoechsttempo, langsamere Bewegung entsteht aus dem Zickzack [ES; Schachbrett [L]].
- Das gibt allen Feldern denselben Kegel, aber nicht von selbst dasselbe langwellige Tempo. STRICH-NETZ-1 nennt DP-Weyl
  mit 1/sqrt(3) [P: strich-netz-1/KARTE.md Z. 59-60].
- Fuer Uhrenvergleiche zaehlt das langwellige Grenztempo je Feld; AETHER-UHR-1 vergleicht genau c_A und c_B [P].

**4.2 AETHER-UHR-1**

- Das Ergebnis dort: "Nur eine gemeinsame Grenzgeschwindigkeit macht sie unsichtbar" [P: ERGEBNIS Z. 51-52, dort als
  [H] im Netzbild; gerechnet ist ein 1+1D-Zweifeldmodell].
- Blackmons Isotacheia ist genau diese Bedingung, als Annahme gesetzt.
- Bei Epikur ist die Allgemeinheit billig: Alles, auch das Licht, besteht dort aus Atomen derselben Art [L, nicht
  nachgelesen].
- Finns Netz hat mehrere Sorten mit je eigenem Tempo: Pfeile, Laengen, Fadenenden, Q-Baelle [P: REVIEW, K-A].

**4.3 Begruendet Blackmon das gemeinsame Tempo?**

- In den beiden Abstracts nicht: Er leitet aus einer Lehre her [P: OpenAlex].
- Moeglicherweise gibt der Haupttext Epikurs eigenes Argument wieder: Die Leere bremst nichts, also laufen schwere und
  leichte Atome gleich schnell [L, ungeprueft].
- Das waere ein Grund dafuer, dass das Gewicht nicht bremst. Es waere kein Grund dafuer, dass in einem Netz mit
  verschiedenen Kopplungsregeln alle Sorten denselben Wert haben [ES].
- **Feldregel 6:** Es gibt mindestens drei Wege zu "Bewegung gegen das Ruhesystem unsichtbar":
  2. kovariante Felddynamik mit einem c fuer alle Felder (Lorentz, Bell; AETHER-UHR-1)
  3. gar kein Ruhesystem (Einstein; die Kausalmenge K-B mit gemeinsamer Ordnung [P: REVIEW])
- Die gemeinsame Groesse dahinter ist ein gemeinsamer Lichtkegel, also eine Metrik fuer alle Sektoren.
- Isotacheia ist eine Darstellung dieser Groesse, nicht ihre Ursache. Fuer das Netz lautet die Frage daher: Welcher
  Mechanismus zwingt alle Felder auf denselben langwelligen Kegel?
- Das ist dieselbe Luecke wie im Review: Keine Symmetrie ist bekannt, die die Tempi aufeinander abbildet [P: REVIEW, K-A].

**4.4 "Gemittelt auf Kantenlaengen": Rechenskizze [ES, nicht gerechnet, nur Taylor-Entwicklung]**

- Pythagoras gilt in jedem Augenblick: Das Quertempo ist sqrt(c^2 - v^2).
- Schwankt das Tempo von Sprung zu Sprung (c_i = Kantenlaenge/Takt), dann tickt eine Uhr aus solchen Teilen mit
  <sqrt(c_i^2 - v^2)>/<c_i> statt mit sqrt(1 - v^2/cq^2); cq ist das mittlere Sprungtempo.
- Die Wurzel ist konkav, deshalb legt der Mittelwert das Ergebnis nicht fest.
- Fuer kleine v weicht der Uhrgang um etwa -(1/2) (v^2/cq^2) (sigma^2/cq^2) ab. sigma^2 ist die Varianz der Sprungtempi.
- **Folge:** Gleiche Mittelwerte reichen nicht.
  - Auch die Streuung (und hoehere Momente) muss fuer alle Felder gleich sein oder verschwinden.
  - Sonst haengt der Uhrgang vom Feld ab, und das Ruhesystem wird sichtbar.
  - STRICH-NETZ-1 fuehrt genau das schon als offen: Unordnung koennte die Tempi verschiedener Felder in zweiter Ordnung
    verschieden verschieben [P: KARTE Z. 64-65].
- **Groessenordnung:**
  - Grundlage sind die Schranken aus AETHER-UHR-1, L5 [P, dort L]: Uhrenvergleiche 1e-17 bis 1e-20, also bei v ~ 1,2e-3
    ein Koeffizient unter etwa 1e-11 bis 1e-14.
  - Dann muesste der Unterschied von sigma^2/cq^2 zwischen zwei Feldern in der Groessenordnung 1e-11 bis 1e-14 oder
    darunter liegen (Faktor 2 aus der Skizze ist darin enthalten) [ES].
- **Ist die Streuung fuer alle Felder gleich:** Dann zeigen Uhrenvergleiche zwischen Feldern nichts. Dafuer weicht das
  Dehnungsgesetz selbst ab, am staerksten bei v nahe c; in der Skizze koennen Spruenge mit c_i < v dann nicht mehr
  mithalten [ES].
- **Grenzen der Skizze:**
  - Sie nimmt an, dass jeder Sprung laengs genau v beitraegt und gleich lang dauert.
  - Im echten Netz haben Spruenge Richtungen, und Wellen mitteln anders als Punktlaeufer.
  - Die Pruefung gehoert in STRICH-NETZ-1, Teil C.
  - Der FEM-Weg (alle Kopplungen aus derselben Geometrie, Patch-Test) zielt genau darauf: Das langwellige Tempo soll
    exakt sein, nicht nur gemittelt [P: KARTE Z. 61-63].

### 5. Hinweise fuer Finn vor einer Kontaktaufnahme (nur Notiz, kein Kontakt erfolgt)

- **Name:**
    su3-geometric-triplets-20260930-en-codex/main.tex Z. 25 [S, lokal per grep].
    [P].
    Satz klaeren oder die Autorzeile aendern [ES].
- **Korrespondenz-Satz:**
- **Rahmen:** Blackmon sagt keine Abweichung von der Relativitaetstheorie voraus ("precisely as our standard model
  predicts") [P: OpenAlex]. Die "Asymmetrie" ist eine Frage der Deutung, nicht der Messung. Fuer das Gespraech heisst das
  "Deutung", nicht "Messvorhersage" [ES].
- **MEOW:** ein einzelner Zoom-Vortrag am 7. Maerz 2025, ohne Aufzeichnung oder Unterlagen auf der Seite [S]. Es gibt
  nichts, woran Finn teilnehmen koennte.
- **Blackmon selbst:** an der SFSU [P: OpenAlex]. Ob er angeschrieben wird, entscheidet Finn; von hier aus kein Kontakt.

## Regime und Moderatoren (Feldregel 1)

- **Zugang:**
  - Runde 20 bekam beim Verlag und bei PhilPapers 403 [P]; ich bekam bei PhilArchive 403.
  - OpenAlex fuehrt die Verlagsfassung als nicht frei.
  - Vermuteter Moderator: Browser mit JavaScript gegen Programmzugriff (Cloudflare), nicht der Inhalt. Das OpenAlex-Etikett
    bleibt ungeklaert.
- **Datum 1. oder 2. April 2025:** vermutlich Online-Datum gegen Datum der Heftseite [ES], ungeklaert.
- **Deutung:**
  - "Asymmetrie real" (Vorzugssystem, Lorentz-Deutung) und "symmetrisch" (Einstein) sind zwei Beschreibungsweisen mit
    denselben Vorhersagen, solange die Isotacheia exakt gilt.
  - Moderator: ob alle Bestandteile genau eine Grenzgeschwindigkeit teilen.

## Unterscheidungspunkte (Feldregel 2)

  - Wo beide passen (exakte Isotacheia), gibt es keinen Unterscheidungspunkt. "Mit Uhren nicht messbar" sagt genau das:
    Die Deutungen sind dort empirisch nicht unterscheidbar [ES].
  - Auseinander laufen sie erst, wo die Isotacheia bricht, also bei sortenabhaengigen Grenztempi. Dann zeigt sich ein
    v^2-Gang im Uhrenvergleich (AETHER-UHR-1).
  - Gemessene Schranken: 1e-17 bis 1e-20 [P, dort L]; Licht gegen Schwerkraft 1e-15 [P: REVIEW Z. 174].
- **Exakte Isotacheia gegen Isotacheia im Mittel (Finns Frage):**
  - Sie trennen sich in der Ordnung (v^2/c^2)(sigma^2/c^2).
  - Bei verschiedener Streuung je Feld zeigt es der Uhrenvergleich zwischen Feldern; bei gleicher Streuung die
    Zeitdehnung bei hohem v [ES, Skizze 4.4].

## Gegensweep (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlich | Geprueft? |
|---|---|---|
| G1 | "Professor James Blackmon" (SFSU) ist "J. C. Blackmon" (Aufsatz) | **ja**, lokal: OpenAlex nennt "James C. Blackmon", San Francisco State University [P]. Stimmig |
| G2 | Der 7. Maerz 2025 war ein Freitag, wie die Seite sagt | **ja**, per date: "Friday 2025-03-07" |
| G4 | BLAAEM-3 ist ueberhaupt der Zeitdehnungs-Aufsatz | nur ueber OpenAlex-Metadaten, nicht an der PDF |
| G5 | Epikur begruendet die Isotacheia selbst (die Leere bremst nicht) | nein [L]; wichtig fuer E4, weil das Tempo dann in der Tradition begruendet waere |
| G7 | Das OpenAlex-Abstract stammt aus der Verlagsfassung | unbekannt; es koennte auch aus der PhilArchive-Fassung stammen |

## Kalibrierung

- **(a) Gelesen bzw. gemessen:**
  - der Text der SFSU-Seite [S]
  - Metadaten und Abstract bei OpenAlex [P]
  - der Zugangsausgang der vier Abrufe
- **(b) Nuetzlich verdichtet:**
  - "Blackmon setzt voraus" (aus zwei Abstracts)
  - "Mittel reicht nicht" (Rechenskizze)
  - "drei Wege, ein gemeinsamer Kegel" (Feldregel 6)
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
    QUELLEN-DOSSIER (T4, A1) und RUNDE-41.md (Nachricht an Finn).
  - Alle gehen auf eine einzige Lektuere einer einzigen Sitzung zurueck.
- **Warnzeichen:** Meine Sicherheit fuer "setzt voraus" stieg waehrend der Arbeit, obwohl der Haupttext ungelesen blieb.

## Offene Fragen

   die PhilArchive-Fassung im Browser lesen.
2. Begruendet der Haupttext die Isotacheia, etwa mit Epikurs Argument der Leere? Uebertraegt er sie auf Licht und heutige
   Teilchen?
3. **Behandelt Blackmon nur eine Ausrichtung der Uhr?**
     Umlaufachse exakt. Fuer andere Richtungen ist die Verkuerzung vorausgesetzt (Bell) [P: QUELLEN-DOSSIER T3].
   - Gilt das auch fuer Blackmon, dann reicht die Isotacheia allein nicht. Es braucht dann auch Bindungsdynamik, also
     Kopplung (Feldregel 6) [ES].
4. Was genau meint "velocity Lorentz transformation": nur den Faktor gamma oder mehr?
5. Wie stark weichen eingereichte und gedruckte Fassung voneinander ab (E2)?

## Quellenliste mit Abrufstand

| Nr | Quelle | Abrufstand | Lokale Kopie |
|---|---|---|---|
| Q1 | SFSU Department of Philosophy: "Metaphysics, Epistemology, and Ontology Workshop (M.E.O.W.)", https://philosophy.sfsu.edu/event/metaphysics-epistemology-and-ontology-workshop-meow | curl 2026-10-04 15:47:50 CEST, HTTP 200 (Drupal 10) | quellen/sfsu-meow.html; geschwaerzt: 2 E-Mail-Adressen, 1 Telefonnummer (Fusszeile), Zoom-Kennung mit Passwort; sha256 vor Schwaerzung 27686bf1..., danach 0d8d10a3... |
| Q2 | PhilArchive BLAAEM-3, https://philarchive.org/archive/BLAAEM-3 | curl 15:47:52 CEST: HTTP 403 (Cloudflare "Just a moment..."); WebFetch nach 15:49:14 CEST: HTTP 403 | quellen/blaaem-3.roh (nur die Cloudflare-Seite) |
| Q3 | Wayback, https://web.archive.org/web/2026id_/https://philarchive.org/archive/BLAAEM-3 | curl 15:49:53 CEST: HTTP 404, "The Wayback Machine has not archived that URL." | quellen/blaaem-3-wayback.roh (E-Mail-Adresse des Archivs geschwaerzt) |

## Selbstanzeigen

1. **Hauptquelle ungelesen:** Alles Inhaltliche zum Aufsatz ist [P] oder Abstract. Kein Satz in diesem Dossier zitiert den
   Haupttext.
2. **Zaehlung der Abrufe:**
   - Finns zweiten Link habe ich dreimal angefragt (curl, WebFetch, Wayback); das zaehle ich als drei der vier Abrufe.
   - Keine "verlinkte Seite" abgerufen: Die SFSU-Seite verlinkt nichts Fachliches (nur Zoom und andere Termine), die Links
     bei PhilArchive sind unbekannt.
   - Ob der Wayback-Weg als "Finns Link" gilt, entscheidet die Leitung.
3. **Ueber die Karte hinaus geschwaerzt:** die Zoom-Kennung samt Passwort in der SFSU-Kopie. Die ungeschwaerzte Fassung
   ist nicht aufbewahrt, nur ihr sha256.
4. **Platzhalterzeit:** In ARBEITSFELD.md stand kurz "15:5x" (geschaetzt). Ich habe sie durchgestrichen und durch den
   date-Wert ersetzt.
5. **Ueber die Vorarbeitsliste hinaus gelesen (nur lesend):**
   - OpenAlex-JSON aus Runde 20 und pdf/rtime.txt
   - STRICH-NETZ-1/KARTE.md
   - grep in RUNDE-41.md, RUNDE-35.md, RUNDE-20.md und model-lab/papers
6. **Rechenskizze 4.4:** [ES], ohne Interpreter, nur eine Taylor-Entwicklung. Die Annahmen stehen dort. Sie ist kein
   Netzergebnis.
7. **Epikur-Hinweise** (Leere, alles aus Atomen) stammen aus dem Gedaechtnis [L] und sind nicht nachgelesen.
8. **Kartentitel:** Der Titel nennt "Runde 41", der Ordner liegt in RUNDE-37. Nur notiert.
9. **Zeitbox:** Beginn 15:46:28 CEST. Text bis auf diese Zeile fertig um 16:00:17 CEST (date). Das sind rund 14 von 30
   Minuten.
10. **Tageszaehlung:** Die erste Zaehlung per date ergab 24 Tage. Das war ein Artefakt der Sommerzeit (30.03.2025). In
    UTC sind es 25 Tage; dieser Wert steht im Text.

## Einfach gesagt

Blackmons Aufsatz auf PhilArchive liess sich nicht oeffnen: Die Seite sperrt Programme, und es gibt keine Archivkopie.
Aus einem gespeicherten Datensatz wissen wir aber, dass es die eingereichte Fassung seines Aufsatzes von 2025 ist, und
dort steht, die alten Epikureer haetten die Zeitdehnung herleiten koennen, wenn alle Atome gleich schnell sind. Blackmon
nimmt dieses gleiche Tempo als alte Lehre an und erklaert nicht, warum es fuer alles gleich sein soll; er sagt auch
keine neue Messung vorher. Der Workshop MEOW war ein einziger Zoom-Vortrag von ihm am 7. Maerz 2025 an seiner Uni in San
Francisco. Fuer dein Netz heisst das: Blackmon liefert die Bedingung, nicht den Grund, und "nur im Mittel gleich
schnell" reicht vermutlich nicht, weil auch die Streuung der Kantenlaengen in die Uhren eingeht.
