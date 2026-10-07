# ARBEITSFELD blackmon-meow-l (feldforscher, eine Arbeitsdatei nach Feldregel 5)

- Angelegt 2026-10-04 15:47:17 CEST (date), nach dem Lesen von KARTE.md und der Vorarbeit, vor jedem Abruf.
- Gestrichenes bleibt stehen (~~so~~). Offene Rueckfragen stehen unten und wandern mit.
- Abrufzaehler: 0 von 4.

## Vorarbeit gelesen (nur lesend)

- RUNDE-20 ERGEBNIS F7 (Z. 103-107) [P]: DOI 10.3366/anph.2025.0122, Datum 2025-04-01 (OpenAlex); Volltext damals 403.
- AETHER-UHR-1 [P]: zwei Wellensorten mit verschiedener Grenzgeschwindigkeit verraten Bewegung; nur gemeinsame
  Grenzgeschwindigkeit macht sie unsichtbar (Lorentz' korrespondierende Zustaende [L]).
- WELTMODELL-REVIEW-1 [P]: K-A (Finns Netz) Ruhesystem, eigenes Tempo je Sorte (Levin/Wen stimmen t ab),
  GW170817 1e-15, Collins u. a. 2004 Prozentbereich ohne Feinabstimmung; Rettung nur durch Symmetrie, die die Tempi
  aufeinander abbildet (keine bekannt).
- Auffaellig an der Karte: Titel sagt "Runde 41", Ordner ist RUNDE-37. Nur notiert.

## Eigene Vorhersagen je Abruf (vor dem Abruf, Feldregel 3)

### Abruf 1: SFSU-Seite (MEOW)
- Vorhersage: Veranstaltungsseite des Philosophie-Instituts der SFSU mit Titel, Datum, Ort und einer Vortragsliste;
  Blackmon steht dort als Vortragender oder Organisator; Vortragstitel nah am Papier (Zeitdehnung/Epikur), aber ohne
  Abstract. Unsicher: ob Blackmon ueberhaupt vortraegt (50 %).

### Abruf 2: PhilArchive BLAAEM-3
- Vorhersage: PDF (Autorenfassung) von "An Epicurean Model of Time Dilation". Gegenhypothese 35 %: Die Kennung -3
  zeigt, dass es mindestens zwei aeltere Eintraege mit denselben Titelinitialen gibt; BLAAEM-3 koennte ein anderes
  oder ein Folgepapier sein (gleiche Initialen "An Epicurean Model ..."). Erwartet im Text: Isotacheia, Pythagoras-

## Abrufprotokoll

1. **Abruf 1** curl 15:47:50 CEST, https://philosophy.sfsu.edu/event/metaphysics-epistemology-and-ontology-workshop-meow
   - HTTP 200, Drupal 10; Kopie quellen/sfsu-meow.html; sha256 vor Schwaerzung 27686bf1...; geschwaerzt: 2 E-Mail,
     1 Telefon (Fusszeile des Instituts), Zoom-Kennung mit Passwort (Selbstanzeige: ueber die Karte hinaus).
   - Inhalt [S, Z. 254-285 der Kopie]: M.E.O.W., Freitag 7. Maerz 2025, 15-17 Uhr PT, kostenlos, Ort Zoom.
     "back after a long break"; Vortrag "Professor James Blackmon", Titel "Isotacheia: How the Epicureans Could Have
     Derived Time Dilation"; mit Abstract (Rossi-Hall 1941; "simple theorem of kinematics"; "only basic algebra";
     "classical and intuitive, and all terms have direct physical interpretations"). Keine Links zum Papier.
   - **Verstoss gegen meine Vorhersage und gegen E3:** Es gibt ein Abstract mit Inhalt. Ort ist kein Raum, sondern Zoom.
     Datum liegt vor der Verlagsfassung (April 2025). Seite nennt Blackmons Institut nicht.
2. **Abruf 2** curl 15:47:52 CEST, https://philarchive.org/archive/BLAAEM-3
   - HTTP 403, Cloudflare-Seite "Just a moment..." (JS-Pruefung). Kein Inhalt. Rohdatei quellen/blaaem-3.roh
     (Cloudflare-Seite, keine Personendaten).
   - Vorhersage nicht pruefbar; nur Zugangsfehler.

### Abruf 3 (vor dem Abruf, ~~15:5x~~ eingetragen vor 15:49:14 laut date; Berichtigung: "15:5x" war ein geschaetzter Platzhalter): WebFetch derselben PhilArchive-Adresse (gleiches Ziel, zweiter Weg)
- Vorhersage: scheitert ebenfalls an Cloudflare (60 %). Falls nicht: Autorenfassung als PDF, Text nur ueber das
  WebFetch-Kleinmodell lesbar, also Wortlaut nicht garantiert -> Zitate dann als [S-WF] markieren.
- Zaehlung: Ich zaehle jeden Versuch. Danach bleibt hoechstens ein Abruf fuer eine verlinkte Seite.

- **Abruf 3** WebFetch 15:49:14 CEST (date davor): HTTP 403. Vorhersage bestaetigt, eine Zeile.

### Abruf 4 (vor dem Abruf): Wayback-Aufnahme derselben Adresse (Finns Link ueber Archiv, kein neues Ziel)
- Begruendung der Wahl: Die SFSU-Seite verlinkt nichts Fachliches; die PhilArchive-Seite ist gesperrt, ihre Links sind
  also unbekannt. Die Verlagsfassung (DOI) ist von keiner selbst gelesenen Seite verlinkt -> nach Karte nicht zulaessig.
  Bleibt nur Finns zweiter Link ueber einen anderen Weg.
- Vorhersage: Wayback hat eine Aufnahme der PDF (40 %). Wenn ja: Autorenfassung von "An Epicurean Model of Time

- **Abruf 4** curl 15:49:53 CEST, https://web.archive.org/web/2026id_/https://philarchive.org/archive/BLAAEM-3:
  HTTP 404, "The Wayback Machine has not archived that URL." Vorhersage (Nein-Seite, 60 %) bestaetigt, eine Zeile.
  Abrufzaehler: 4 von 4, Kontingent erschoepft. Die Arbeit selbst habe ich nicht gelesen.

## Lokale Funde (kein Webabruf, nur Projektdateien)

  - **Verstoss gegen meine Erwartung "lokal liegt nichts Neues":** Er enthaelt das Abstract der Arbeit (als Wortindex;
    per jq zusammengesetzt, Auszug quellen/openalex-W4409085798-auszug.json).
  - Abstract: "derived from the Epicurean atomist doctrine of isotakheia, which states that all (Epicurean) atoms have
    equal speed"; "could have anticipated time dilation measurements precisely as our standard model predicts".
  - Orte: Verlag (publishedVersion, is_oa false); philarchive.org/rec/BLAAEM-3 und philpapers.org/archive/BLAAEM-3.pdf
    als **submittedVersion**. Seiten 98-119, Bd. 7 Heft 1. Autor "James C. Blackmon", San Francisco State University.
  - Damit: BLAAEM-3 gehoert nach OpenAlex zu diesem Werk (E1 Teil 1 gestuetzt, Metadaten). Etikett "submittedVersion"
    spricht eher gegen E2 (schwach; Etiketten sind automatisch [L?]).
  at the speed of light"; "has always to be c" gegen "the reference frame at rest". Prämisse des Modells, keine
  Begruendung fuer ein gemeinsames Tempo aller Sorten.

## Befunde je Erwartung

  bzw. [ES] ueber Volltextindex; Schwerkraft nicht pruefbar.
- E2: offen; einziges Indiz "submittedVersion" spricht eher dagegen (schwach).
- E4: Teil 2 (vorausgesetzt) auf Abstract-Ebene gestuetzt ("derived from the ... doctrine"); Teil 1 (fuer Licht und
  Materie verlangt) nicht gestuetzt: Abstract sagt "(Epicurean) atoms" und rahmt historisch-kontrafaktisch.
- E3: teilweise. Workshop und Vortrag zum Thema ja; Datum ja; Ort = Zoom; Programm = ein Vortrag; aber Abstract mit
  Inhalt vorhanden (gegen "keine weiteren Inhalte").

## Gegensweep (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. "Professor James Blackmon" (SFSU) = "J. C. Blackmon" (Papier)? **Geprueft** (lokal): OpenAlex nennt "James C.
   Blackmon", San Francisco State University. Konsistent.
2. Ist der 7. Maerz 2025 ein Freitag (Seite sagt "Friday")? **Geprueft** per date: Friday 2025-03-07.
   su3-geometric-triplets-20260930-en-codex/main.tex Z. 25 (und weitere).
4. BLAAEM-3 = Zeitdehnungs-Papier? Nur ueber OpenAlex-Metadaten, nicht am PDF. Offen.
5. Hat Epikur selbst eine Begruendung fuer die Isotacheia (die Leere leistet keinen Widerstand)? Nur [L], nicht geprueft.
   Wichtig fuer E4: Dann waere die gleiche Geschwindigkeit in der Tradition begruendet, nicht bloss gesetzt.
7. Stammt das OpenAlex-Abstract aus der Verlags- oder der PhilArchive-Fassung? Unbekannt.

## Kalibrierung

- Meine Sicherheit fuer "Blackmon setzt das Tempo voraus" stieg im Lauf der Arbeit, aber nur aus zwei Abstracts; den
  Text der Arbeit habe ich nicht gelesen. Warnzeichen, gehoert ins Dossier.

## Abschluss

- DOSSIER.md geschrieben ab 15:57:09 CEST, fertig bis auf Selbstanzeige 9 um 16:00:17 CEST (date).
- Nebenbefund: Die Tageszaehlung 7.3. bis 1.4.2025 ergab in Ortszeit 24 (Sommerzeit am 30.03.), in UTC 25. Im Dossier
  steht 25.
  (Z. 239-243), STRICH-NETZ-1 KARTE (Z. 59-65), rtime (Z. 7, 9, 53) und Hashes geprueft. Schranke in 4.4 auf
  "Groessenordnung 1e-11 bis 1e-14" berichtigt; die erste Fassung "2e-11 bis 2e-14" war eine Scheingenauigkeit.

## Offene Rueckfragen

- ~~Welche zwei Zusatzseiten? Erst nach Abruf 1 und 2 entscheiden.~~ SFSU-Seite verlinkt nichts Fachliches (nur Zoom und
  andere Veranstaltungen). PhilArchive gesperrt, Links dort unbekannt.
