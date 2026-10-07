# Runde 45 nach v3 (eroeffnet 2026-10-04 23:34:23 CEST)

- Leitung claude-primary. Vorgaenger: RUNDE-44.md (geschlossen; Journal claude-runde-v3-44-20261004).
- Deckel:
  - hoechstens 10 Agenten (alle Sitzungen zusammen), davon hoechstens 7 mit Rechenlaeufen
  - seit dem Sitzungslimit (19:53) hoechstens 6 gleichzeitig
  - um Mitternacht wenige, damit die Tagespflichten sicher durchlaufen
- Regeln wie RUNDE-44:
  - Bus bei jedem Tick und vor jedem Journal lesen (--unacked); quittieren nur gelesene IDs.
  - Zusammenfassungen von der letzten gegengelesenen Fassung aus schreiben.
  - Agentenvorschlaege "offen" selbst auf Ableitbarkeit pruefen.
  - Freie Parameter am Code zaehlen, nicht an der Gruppe.
- **Andere Sitzungen:**
  - claude-video (KOMPAKT-1 auf cpu3, cpu4, p4000a)
  - Codex ag-phy-coordination und ag-phy-lat (cpu2)
- **Negativliste:** wie RUNDE-44.md, dazu neu aus Runde 44:
  - "der einfache Weyl-Operator spaltet die beiden Haendigkeiten" (die Zweige trennt ein untergitter-wechselnder Querspin, DIAMANT-NULLSTELLEN-1)
  - "eine natuerliche Massenregel macht die Schwerewellen isotrop" (TT-GRUND-1: keine von sechs)
  - "Gewichte allein reichen generisch nicht fuer TT-Isotropie" (TT-ISO-1 widerlegt)
  - "das 4/3-Richtungsmuster gilt fuer regelmaessige Netze allgemein" (Wuerfelgitter umgekehrt)
  - "RUNDE-39 (BEUTEL-1) belegt Zufallsnetz-Isotropie" (Fundstelle falsch; nur RUNDE-36/zufallsnetz-1, Federnetze)
  - "Netz = Geometrie ist ein Ausweg aus Marolf" (allein weder Gegenbeweis noch hinreichender Ausweg)
  - "stabile Q-Baelle in D = 1 bis 12" (nur radiale Kandidaten mit VK und E < Q)
  - "echtes SU(3) braucht drei Rishons je Kante" (nur in der einfachen Determinanten-Bauweise)

## Karten (Ordner unter RUNDE-37/)

| Karte | Inhalt | Stand |
|---|---|---|
| (keine laufend) | | |

## Warteschlange

1. Tagespflichten nach Mitternacht:
   - index-pruefen, karten-pruefen, index-sichern und rsync .69
   - .69-Kopie nach TS440 (rsync ohne --delete)
   - Git-Tagesschnappschuss mit --pruefen zuerst
2. BOUFOUROU-DR4-L (Literatur, M1-Strang, niedrige Prioritaet; ohne versiegelte Teile).
3. Nach Finns Antworten:
   - MATERIE-NETZ-1 (R1)
   - TORSION-STEIF-1 (Baender auf Linien oder zwischen Zellen; vorher Christiansen/Hu/Lin 2023 lesen)
   - Weiche Kristall oder Glas
4. EIN-TEMPO-2 (Licht und FKM-Fermion auf Finns Netz: gleiches langwelliges Tempo? Erst Ableitbarkeitsprobe, die Normierungen sind frei).
5. FINN-PLATTE-1 (Haendigkeit am Rand; nach FKM neu fassen), PT-AUSGLEICH-1 (Scout 2610.00774).

## Protokoll

- 2026-10-04 23:34:23 CEST: Runde 45 eroeffnet.
  - Runde 44 geschlossen und veroeffentlicht: claude-runde-v3-44-20261004, 27 Quellen, pruefen ohne Befund, rc 0, Index 1 Zeile, Quellen-Hashes 27 von 27 OK.
  - Bus vor dem Journal gelesen (eine Codex-Meldung, quittiert).
  - Keine Agenten aktiv.
- 2026-10-05 00:16:04 CEST: Tagespflichten 05.10.:
  - index-pruefen ohne Verstoss (synchron, Kettenende nr 592); karten-pruefen ohne Verstoss (288 Zeilen, 60 neu ueber das Werkzeug).
  - index-sichern rc 0; rsync zur .69 rc 0; Aussenanker KETTENENDE.log auf der .69 um nr 592 ergaenzt.
  - .69 nach TS440: rsync ohne --delete im Hintergrund gestartet (Start 22:04:57Z laut Log).
  - Git: Pruefdurchgang 5996 Dateien vorgemerkt, 13705 nur gehasht; gitleaks 4 Treffer, alle Fehlalarme (drei Pruefsummen, Zenodo-Dateinamen), Fingerabdruecke in .gitleaksignore, Begruendung in GEHEIMNISPRUEFUNG.md; echter Lauf mit --push laeuft.
  - claude-video meldet KOMPAKT-1 fertig (Journal nr 592), Spuren frei; quittiert.
- 2026-10-05 00:26:48 CEST: Git-Tagesschnappschuss: Commit d0963f6 ("Snapshot research state of 4 Oct 2026 (rounds 37 to 45)"), 6000 Dateien, gitleaks im echten Lauf ohne Treffer, Push 4a264c7..d0963f6 ins LAN-GitLab rc 0; Index sauber. Gedaechtnis ergaenzt.
- 2026-10-05 00:26:56 CEST: .69 nach TS440 fertig (Ende 22:06:30Z, rc 0, Gesamtgroesse 47,5 GB, inkrementell). Laptop-restic laeuft von selbst um 04:30. Tagespflichten 05.10. damit erledigt.
- 2026-10-05 00:27:52 CEST: BOUFOUROU-DR4-L geschrieben (Karte ab 00:27:16; BF1 60 %, BF2 70 %, BF3 60 %; ohne versiegelte Teile) und gestartet (feldforscher, 4 Abrufe, 35 min). Aktiv 1. Nachts bewusst wenig parallel (Sitzungslimit).
- 2026-10-05 00:43:57 CEST: Loop-Tick. Bus leer; Scout ohne neue Titel (22:02Z). DREI-KEGEL-L geschrieben (Karte ab 00:43:12; DK1 70 %, DK2 60 %, DK3 85 % als Kontrolle, vorab ableitbar; Projektsuche: A4 in TETRAEDER-L, Gitter-Kegel als Generationen nicht im Projekt) und gestartet (feldforscher, 6 Abrufe, 45 min). Aktiv 2: BOUFOUROU-DR4-L, DREI-KEGEL-L.

### Ernte BOUFOUROU-DR4-L (RUNDE-37/boufourou-dr4-l/DOSSIER.md; eingetragen 2026-10-05 00:44:28 CEST)

- feldforscher.
  - Zeiten: 00:27:55 bis 00:43:32. 4 von 4 Abrufen, einer durch einen eigenen Parameterfehler fehlgeschlagen.
  - Versiegeltes nicht beruehrt.
- **Urteile:**
  - BF1 eingetroffen.
  - BF2 nur formal eingetroffen.
  - BF3 im Wortlaut verfehlt.
- **Ergebnis [S]:**
  - Zenodo 22073431 ist keine eingefrorene Vorregistrierung, sondern das automatische Archiv einer GitHub-Version vom 24.08.2026.
  - Es enthaelt einen DR4-Protokollentwurf, der Kern und Schwanz trennt:
    - primaer ein bei v-tilde < sqrt2 abgeschnittener Median
    - sekundaer ein Mischfit mit Vorlage fuer Dreifachsysteme
    - Ein Urteil verlangt beide.
  - Schwellen:
    - STOP bei >= 2 % Abweichung in der Kontrollzone.
    - Newton, wenn beide < 1,15.
    - Anomalie, wenn beide > 1,20 mit > 5 sigma und ausserhalb des Systematikbands.
    - Sonst Grauzone.
  - Nicht gebunden sind, wie bei WB-2, der DR4-Katalog, der Code-Hash und die Saaten.
- **Erwartungsverstoesse:**
  - Der Status ist an fuenf Stellen verschieden benannt ("draft v0.95", "Version 1.0", "noch einzufrieren", "eingefroren"). Die Zenodo-v2.0 enthaelt kein Protokoll; einen Hash vom Autor gibt es nicht.
  - Boufourous eigene DR3-Messung liegt ueber Newton: abgeschnittener Median 1,045 [1,025; 1,068] (68 %), also 2,25 sigma; Mischfit etwa 3,1 sigma. Newton passt nur mit dem Exzentrizitaets-Systematikband.
  - Die Einordnung "Boufourou = Newton" aus WB-ZENODO-L gilt nur fuer die Verwerfung von 1,4.
  - Protokoll und Papier passen nicht zusammen: Der Eichwert stammt aus einem aelteren Stand ohne Perspektivkorrektur und mit anderen Schnitten; die Entscheidungsregel liegt nicht als Code bei.
- **Lesart des Agenten [H]:** Wiederholt DR4 die DR3-Lage, urteilt WB-2 "Boost" und Boufourou "Newton". Die Dreifachsysteme erklaeren nach Boufourous eigener Rechnung hoechstens etwa die Haelfte des WB-1-Ueberschusses.
- **Einordnung (Leitung, ohne versiegelte Teile):**
  - Beide fremden DR4-Protokolle sind nicht vollstaendig gebunden (Katalog, Hash).
  - Boufourous trennt Kern und Schwanz, passend zur M1-Lehre.
  - An unserem versiegelten Vertrag aendert das nichts. Nach dem 2.12. sind beide Vergleichsstimmen.
- **Abschaetzung: erledigt.**

### Ernte DREI-KEGEL-L (RUNDE-37/drei-kegel-l/DOSSIER.md; eingetragen 2026-10-05 01:07:34 CEST)

- feldforscher.
  - Fertig 01:06. 6 von 6 Abrufen, per curl statt WebFetch (Selbstanzeige).
  - Gruppentheorie von Hand [M], nicht gegengelesen.
- **Urteile:**
  - DK1 eingetroffen.
  - DK2 verfehlt.
  - DK3 eingetroffen (Kontrolle, vorab ableitbar).
- **Ergebnis [M, S]:**
  - Die drei X-Kegel geben die Zahl drei, aber kein festes A4-Multiplett.
    - Ohne Spin traegt das Untergitter am Drehzentrum 1 + 1' + 1'', das andere ein 3.
    - Mit Spin bleibt unter dem Punktgruppen-A4 nur 2(2 + 2' + 2'').
    - Unter der vollen Raumgruppe sind die zwoelf Zustaende eine irreduzible Darstellung.
  - Ein zweites A4 aus fcc-Translationen modulo einfach-kubisch und einer 120-Grad-Drehung macht die Kegel auch mit Spin zum Triplett (12 = 4 x 3).
    - Das ist dieselbe Bauweise wie das Orbifold-A4 bei Altarelli/Feruglio/Lin 2007, dort im Ortsraum, hier im Impulsraum [H].
  - Der FKM-Massenterm ist die Ma/Rajasekaran-Invariante mit gleichen Kopplungen.
    - Massen trennen sich nur mit eingesetzter Brechung.
    - Mischung zwischen den Kegeln verlangt einen Bruch der Gittertranslationen.
  - Literatur:
    - Catterall nutzt Taste-Vielfachheiten fuer die 16 Komponenten einer Generation, nicht fuer drei Generationen.
    - Doppler als Generationen gibt es nur am Rand (Schmelzer 2002; Jourjine 2010 mit vier).
    - "nach Recherchestand nicht belegt"
- **Fehler der Leitung:** Meine Kartenbegruendung (Klein-Vierergruppe haelt die Achsen fest, also 1 + 1' + 1'') trug nicht. Die Vorzeichen auf dem zweiten Untergitter machen ein Triplett.
- **Gegensweep:**
  - Zeitumkehr paart 1' mit 1''. Bei exakter C3 und Zeitumkehr spalten die Kegel hoechstens 1 + 2.
  - Es gibt keinen strengen Ausschlusssatz, aber drei Hindernisse:
    - Die Kegel sind vektorartig.
    - Bei gleichen Massen gibt es keine spontane Flavour-Brechung (Giordano 2023).
    - Ohne Translationsbruch gibt es keine Mischung.
- **Kartenvorschlag des Agenten:** DREI-KEGEL-NEUTRINO-L. Schranke an die Masche aus generationsabhaengiger Dispersion (Dimension 6) gegen IceCube.
- **Abschaetzung: parken.**
  - Der Anschluss an das Orbifold-A4 ist eine reizvolle Hypothese fuer Finn; sie geht an ihn als [H].
  - DREI-KEGEL-NEUTRINO-L kommt in die Warteschlange (messnah, aber bedingt: Neutrinos als FKM-Kegel auf Finns Netz).
- 2026-10-05 01:08:25 CEST: DREI-KEGEL-NEUTRINO-L geschrieben (Karte ab 01:07:49; Vorschlag aus DREI-KEGEL-L woertlich; DN-1 60 %; Zusatz Leitung: Laengeneinheit und Phase/Gruppe umrechnen) und gestartet (feldforscher, 4 Abrufe, 30 min). Aktiv 1.

### Ernte DREI-KEGEL-NEUTRINO-L (RUNDE-37/drei-kegel-neutrino-l/DOSSIER.md; eingetragen 2026-10-05 01:28:51 CEST)

- feldforscher.
  - Zeiten: 01:08:24 bis 01:28:05. 3 von 4 Abrufen, per curl (Selbstanzeige).
- **Urteil:** DN-1 nach Wortlaut eingetroffen (l < ~20 bis 40 l_P), die Begruendung nur teilweise.
- **Ergebnis [S, M]:**
  - Die IceCube-Schranken gelten nur fuer den richtungsgemittelten Anteil, und der unterscheidet die drei Kegel nicht.
  - Genaue Form: a2_r(n) = -3/8 + S4/24 + n_r^4/4. Nur n_r^4/4 trennt die Kegel, und sein Kugelmittel ist fuer alle gleich. Das ganze Signal steckt in der Himmelsrichtung.
  - Die einzige veroeffentlichte richtungsabhaengige Schranke (Telalovic/Bustamante 2025, IceCube-Daten) gibt l < ~20 bis 40 l_P.
  - Zwei Regime [M, eigener Schluss]:
    - A: Kegel = Flavours. Die IceCube-tau-tau-Grenze (3e-42), auf das Muster uebertragen, gaebe l < ~0,08 l_P, also ausgeschlossen. Das ist keine veroeffentlichte Grenze.
    - B: Kegel = Massenzustaende. Die Flavour-Messung ist blind, es bleiben ~30 bis 50 l_P; die Hypothese ueberlebt.
    - Welches Regime gilt, haengt daran, woher die Mischung kommt (Bruch der Translationen).
- **Erwartungsverstoesse:**
  - Richtungsabhaengige Schranken sind rund 5 Groessenordnungen schwaecher als tau-tau; teils erklaert durch die niedrigere Schwelle, der Rest ist offen.
  - Das Isotrop-Halten der Kegel (t = 4 lambda) ist eine Abstimmung. Sie muss auf ~2e-28 stimmen, sonst greifen die d = 4-Schranken (< 8e-29). Die Kartenzeile "haengt nicht an einer Abstimmung" trifft nicht zu.
- **Gegensweep:**
  - Die flavourblinden Grenzen gelten nur fuer Ueberlichtgeschwindigkeit; das Modell ist ueberall langsamer als Licht.
  - Die Laengeneinheit ist schon die Tetraederkante.
  - Oszillationen messen die Phase, also Faktor 1.
- **Bedeutung (vorab):**
  - Eine erste unterscheidende Vorhersage der Kegel-Lesart existiert: "Kompass-Asymmetrie" der Neutrino-Sorten nach Himmelsrichtung.
  - Heute begrenzt sie die Masche auf l < ~20 bis 40 l_P (Regime B) bzw. schliesst die Lesart aus (Regime A).
  - Gegen die Karte haengt das an einer Abstimmung (2e-28).
- **Abschaetzung: erledigt.**
  - Fuer Finns Weiche "Kristall oder Glas" kommt eine zweite Feinabstimmung dazu: Fermion-Isotropie auf 2e-28, neben der Schwerewellen-Isotropie auf 1e-15.
  - Das geht in den Bericht an Finn.
- 2026-10-05 04:15:15 CEST: Finn, woertlich: "Führe alle Themen weiter und stell mir die Fragen noch mal bzw teste herum.was richtig ist". Fragen per Auswahl gestellt; Antworten:
  - R1 (Energie in der Eckregel, Materie im Ecktakt): "Teste beide Varianten".
  - Q-Baelle: "Nur fürs Teilchenmodell".
  - Netzart: "Teste beides" (Kristall und Glas).
  - Baender: "Teste beides" (auf den Linien und zwischen den Zellen).
  - Folge: Tests fuer beide Zweige jeder Weiche; Q-Baelle nur als Materie im Netz; alle uebrigen Themen weiter. Deckel wieder bis 6 gleichzeitig.
- 2026-10-05 04:19:16 CEST: Vier Testkarten nach Finns Antworten geschrieben (alle ab 04:16:30) und gestartet:
  - TT-GLAS-1 (Glas-Zweig: Schwerewellen auf Zufalls-Tetraedernetz; TG-G0 80 %, TG-G1 65 %, TG-G2 85 % Kontrolle, TG-G3 50 %; Code-Agent, cpu3/cpu4, 120 min)
  - DANZER-L (Kristall-Zweig mit Grund: ikosaedrischer Tetraeder-Quasikristall, isotrop bis Tensorstufe 5 [H, M]; DZ1 85 %, DZ2 80 %, DZ3 75 %; feldforscher, 8 Abrufe, 60 min)
  - MATERIE-NETZ-1 (R1 beide Varianten: Energie in der Eckregel plus Ecktakt gegen nur Ecktakt; MN0 75 % Kontrolle, MN1 60 %, MN2 75 %; Q-Ball nur als Materie-Quelle; Code-Agent, cpu5/cpu10, 90 min)
  - TORSION-STEIF-1 (Baender beide Zweige: Torsion zwischen Zellen festgelegt? Rahmen um Gelenkkante = Fehlwinkel; Vorschlag aus REGGE-TORSION-L woertlich; TS0 85 %, TS1 45 %, TS2 55 %; Code-Agent, cpu/cpu11, 90 min)
  - Aktiv 4 von 6.
- 2026-10-05 04:23:23 CEST: PT-AUSGLEICH-L geschrieben (ab 04:20:55) und gestartet (Finns "Ausgleich", Lesart N9, Luecke L5 "Masse ohne Verlust"):
  - Frage: Laesst sich das Umklappen mit verborgener Haelfte (SPIEGEL-HAELFTE-1, 44 % Rueckfluss) PT-symmetrisch schreiben, und ist es dann verlustfrei oder nur umformuliert?
  - Vorab ableitbar [L]: ungebrochene PT-Symmetrie ist pseudo-hermitesch, also einer gewoehnlichen unitaeren Theorie aequivalent.
  - Erwartungen: PA1 60 % (aequivalent, keine neue Physik), PA2 55 % (Rueckfluss bleibt, in der eta-Metrik gezaehlt), PA3 65 % (reelle Spektren auf verzweigten Gittern nur bei abgestimmter Verzweigung).
  - feldforscher, 5 Abrufe, 50 min. Aktiv 5 von 6.
- 2026-10-05 04:23:23 CEST: Bus gelesen (--unacked): keine neuen Nachrichten seit 2026-10-04 23:56 CEST (claude-video, schon in RUNDE-44 verarbeitet).
- 2026-10-05 04:30:15 CEST: PAAR-LICHT-L geschrieben (ab 04:28:38) und gestartet. Sie ersetzt EIN-TEMPO-2 in der alten Form.
  - Ableitbarkeitsprobe der Leitung:
    - Gleiches Tempo von Eis-Licht und FKM-Fermion ist eine Einheitenwahl; Wilson-Dirac auf demselben Netz hat 0,8165 statt 2,8284. Also keine Rechnung.
    - Offen ist nur Gegensweep G7 aus LICHT-GLEICH-L: Licht aus Weyl-Paaren (Bisio/D'Ariano/Perinotti), dazu O2.
  - Schreibtisch [M]: Eine einzelne fcc-Schale gibt Summe (n.d)^4 = 3 - S4. Eis-Licht und der Mittelwert der FKM-Kegel haben beide die Form (S4 - 3).
    - Gemittelt unterscheidet die Himmelsrichtung also nicht zwischen Eis- und Paar-Licht; nur die Groesse relativ zum Fermion (1/4) tut es.
    - Je Kegel gilt das nur tetragonal; ein Photon oder drei ist offen.
  - feldforscher, 6 Abrufe, 50 min. Aktiv 6 von 6.
- 2026-10-05 04:30:56 CEST: Scout-Eingang (Lauf 02:04Z, nur Abstracts aus dem Scout-Speicher, kein Abruf):
  - 2610.03479 (Gielen/Ried): unimodulare Henneaux-Teitelboim-Gravitation mit euklidischem Regge-Kalkuel diskretisiert.
    - Die unimodulare Zeit ist eine Randgroesse, die das eingeschlossene 4-Volumen misst. Der Kontinuumslimes laesst sich ueber sie statt ueber die Eigenzeit definieren [S Abstract].
    - Bezug [H]: Ein Takt, der Zellen zaehlt, waere auf Finns Netz die natuerliche unimodulare Zeit. Kandidat fuer eine spaetere Literaturkarte (Takt = gezaehltes Volumen; Folgen fuer L1 und die kosmologische Konstante).
    - Erst nach der Ernte abschaetzen.
  - 2610.03247 (Boguna/Krioukov): In Poisson-Sprenkelungen der Raumzeit (Kausalmengen) haengen Link-Statistiken auch bei wachsender Punktzahl von der Abschneideregion ab, weil der Raum der Rapiditaeten randdominiert ist (d >= 2) [S Abstract].
    - Bezug: Fuer TT-GLAS-1 (raeumliche Poisson-Delaunay-Netze, euklidisch) gilt das nicht direkt [M: der euklidische Raum ist amenabel]. Erst bei einem Raumzeit-Glas wichtig. Notiz, keine Karte.
- 2026-10-05 04:38:13 CEST: Finn "Check die neuen paper jetzt". Die Leitung hat beide Scout-Arbeiten selbst im Volltext gelesen; Erwartungen vorab im Arbeitsfeld (04:34), Kopien in RUNDE-45/quellen-leitung/.
  - Gielen/Ried 2610.03479: G1 bis G4 eingetroffen.
    - Zeit = 4-Volumen als Randgroesse im euklidischen Regge-Netz; Lambda wird Integrationskonstante; klassisch dieselben Loesungen.
    - Die Randzeit ist auch diskret eichfrei.
    - Keine gleich grossen Zellen, keine Lorentz-Fassung.
    - Geschlossene Raumzeiten haben Volumen 0 [S Gl. 33].
    - Fuer uns: Literaturanker zu "Takt = Volumenzaehler" [H]; keine Karte (Datenseite everpresent Lambda gegen DESI schon in Glied 10).
  - Boguna/Krioukov 2610.03247: B1, B2, B4 eingetroffen, B3 teilweise.
    - Linkstatistik aus endlichen Raumzeit-Sprenkelungen haengt in 2+1 und 3+1 bleibend vom Schnitt ab, in 1+1 nicht.
    - Projektpruefung [M]: KAUSAL-1, KAUSAL-SWERVE-1 und KAUSAL-WELLE-4D nicht betroffen (1+1 bzw. Vergleich gegen die Erwartung des endlichen Gebiets).
    - Glas-Zweig TT-GLAS-1 raeumlich, nicht betroffen.
- 2026-10-05 04:43:32 CEST: Finn "Was macht der Codex Agent?" Pruefung:
  - Prozesse per Liste mit [c]odex-Muster: lokal laeuft die Codex-App (app-server mit Fernsteuerung) seit 04.10. 21:33, CPU gering, keine Werkzeug-Kindprozesse ausser ruhenden REPLs; auf der .69 kein Codex-Prozess.
  - Bus: letzte Codex-Meldung 23:16 CEST (lineare Feldmodenansicht), alle schon gelesen.
  - Dateien: particle-lenia-review-20261004/ zuletzt 23:16 (MODEL-STATUS.txt); seither ausserhalb meiner Ordner nichts von Codex.
  - Befund: Codex ruht seit 23:16, sein eigener Strang ist abgeschlossen. Offen laut MODEL-STATUS: uebriges Spektrum, nichtlineare Stabilitaet und Stoesse, selbstkonsistente Quellbreite, Bildung aus ungebundenen Anfangsdaten.
- 2026-10-05 04:43:32 CEST: REGGE-HADRON-REF-L gestartet (Finn-Auftrag: alle Referenzen von arXiv 2512.21805 pruefen und einordnen). Karte ab 04:40:32; Artikel ist Regge-Theorie der Hadronen (Winney/Szczepaniak, Enzyklopaedie-Artikel), nicht Regge-Kalkuel.
  - RH1 80 %, RH2 60 %, RH3 40 %, RH4 90 %, RH5 75 %.
  - feldforscher, 45 Abrufe (INSPIRE, arXiv, Crossref), 90 min.
  - Aktiv 7 (Finn-Auftrag; ueber meinem Deckel 6, unter Finns 10).

### Ernte PT-AUSGLEICH-L (RUNDE-37/pt-ausgleich-l/DOSSIER.md; eingetragen 2026-10-05 04:48:32 CEST)

- feldforscher, 04:21:33 bis 04:43:48, 5 von 5 Abrufen.
  - PDFs gespeichert und gelesen.
  - F3 bis F5 sind Antworten des Abrufwerkzeugs, nicht woertlich geprueft (Selbstanzeige).
- **Urteile:**
  - PA1 im Wortlaut nicht eingetroffen, im Kern ("keine neue Physik") eingetroffen
  - PA2 nicht eingetroffen
  - PA3 teilweise
- **Ergebnis [M nicht gegengelesen, S]:**
  - Gewinn und Verlust zwischen den Haelften brechen die PT-Symmetrie bei k = 0 fuer jedes gamma > 0, weil die Haelften dort entkoppelt sind: U_gamma(0) = e^(i alpha - gamma) P_2 + e^(i beta + gamma) P_2'. Die Leitung hat das von Hand nachvollzogen.
  - Im Projektlauf (alpha = 0, beta = pi) gibt es gar keine PT-Symmetrie, nur eine vom Teilchen-Loch-Typ.
  - Ohne Gewinn und Verlust ist die Dynamik bei W = 0 pseudo-unitaer; die eta-Norm ist sichtbares plus verborgenes Gewicht. Das ist eine Umformulierung (Mostafazadeh [L]).
  - Die 44 % Rueckfluss stehen in keiner eta-Metrik. Bei W = 2 pi sind sie rein inkohaerent (0,2237 gegen 0,222), also Dekohaerenz der sichtbaren Haelfte.
  - Verzweigte PT-Gitter: Der Knoten ist die schwaechste Stelle. Die Schwelle faellt von 0,5 auf 0,185 (2601.03189 [S]); am isolierten Knoten bricht der Ausgleich fuer jedes gamma_0 (2610.00774, S. 15 [S]).
  - Masse: Fuer das PT-Dimer gilt E = +-sqrt(m^2 - gamma^2) [M, von der Leitung geprueft]; der Ausgleich verkleinert eine Masse nur.
    - Mit Eichfeld: "Gauge invariance is restored when the Hermitian and anti-Hermitian masses are of equal magnitude, and the theory reduces to that of a single massless Weyl fermion" [S Abstract 1509.01203; die Leitung hat es um 04:45 an der Quelle gelesen].
  - Kawabata/Ashida/Ueda 2017: Der "hidden entangled partner" ist Finns verborgene Haelfte in Literaturform [S Abstract].
- **Gegensweep des Agenten:**
  - Eigene Berichtigung: Streifen um Entartungsebenen statt Ausnahmekugel.
  - Offen: r = 0,44 ist nur bei sigma = 4 gerechnet.
  - Die PT-Definition fuer Zeitschritt-Laeufe stammt aus dem Gedaechtnis [L].
- **Kartenvorschlag RUECKFLUSS-INFO-1:** Spurabstand der sichtbaren Haelfte bei festen gegen neu gezogene Takte (Information oder Rauschen).
  - Zusatz Leitung: eine sigma-Leiter 4, 8, 16 fuer r, weil GEMEINSAMES-NETZ v3 (L5) die 44 % als Zahl fuehrt.
- **Abschaetzung: erledigt.**
  - Der PT-Ausgleich als Weg zu L5 ist verworfen: keine Massenquelle, langwellig gebrochen. Die eta-Umformulierung ist bekannt.
  - RUECKFLUSS-INFO-1 mit sigma-Leiter kommt in die Warteschlange (Rechenplatz, klein).
  - Vor jeder Uebernahme in v4 liest ein frischer Leser S4 und S5.
- **Negativliste:**
  - "PT-Ausgleich macht das Umklappen verlustfrei"
  - "Ausgleich als Massenquelle"
  - "Die 44 % werden in einer eta-Metrik gezaehlt"
  - "44 % unabhaengig von der Paketbreite" (ungeprueft)
- **Bedeutung:** Fuer L5 bleibt nur der kohaerente, unitaere Teil-Umklapp mit fester Phase (Dirac-Automat) [L, P]. Finns verborgener Takt je Knoten verwuerfelt genau diese Phase.
- Aktiv 6 (PT-AUSGLEICH-L fertig).
- 2026-10-05 04:48:32 CEST: Finn, woertlich: "schau dir das an was codex gemacht hat und dann lass ihn weiter arbeiten. keine arbeiten doppelt, nur kurze reviews und ideation runden mit jeweils anstößen".
  - Kurzreview (R1 bis R3) und Ideation-Runde 1 (A1 bis A5) an Codex geschickt (RUNDE-45/bus/an-codex-review-anstoss-1.md): Bildung ohne Dissipation, kritische Breite, Drehimpuls der T2-Moden, Saettigung, Konkurrenzzustaende.
  - Per Bus und codex queue an den Codex-Faden; dass Codex sie gelesen hat, ist nicht bestaetigt.
  - Mein Vorschlag "Codex rechnet MATERIE-NETZ-1 nach" ist damit verworfen. Regel im Gedaechtnis.

### Ernte DANZER-L (RUNDE-37/danzer-l/DOSSIER.md; eingetragen 2026-10-05 04:53:18 CEST)

- feldforscher, ab 04:18:35, 8 von 8 Abrufen.
  - Selbstanzeigen: PDFs per curl, ein awk ohne Programm, ein leerer erster Abruf.
- **Urteile:**
  - DZ1 eingetroffen, mit Vermerken: Spiegelbilder noetig, kein Prototil regulaer; face-to-face in der gelesenen Quelle nicht belegt.
  - DZ2 eingetroffen fuer die Tensoraussage, Licht-a2 und "erste Anisotropie bei l = 6". Beim TT-Tempo nur bedingt.
  - DZ3 eingetroffen; Phasonen sind in echten Quasikristallen diffusiv bzw. eingefroren.
- **Ergebnis:**
  - Gruppentheorie bestaetigt [M]: Invarianten unter I bei l = 0, 6, 10, 12, 15.
    - Spin-2-Gradiententensor: 4 / 9 / 5 Invarianten (isotrop / kubisch / ikosaedrisch).
    - Isotrop fuer beliebige Massen je Kachelsorte.
    - Der lineare Weyl-Aufspaltterm (Stufe 3, a1 auf Finns Diamant) waere unter I verboten [M].
  - Gemessen: Isotropie auf 0,07 % (AlCuLi, Spoor u. a. 1995) [S Abstract].
  - Die TT-Steifigkeit ist ein Tensor 6. Stufe. Isotrop ist sie nur, weil die Eichinvarianz das l = 6-Stueck verbietet [M]; bei Finns Regge-Laengen gegeben (TT-ISO-1).
  - Phasonen sind der Moderator:
    - In 2D macht die Phonon-Phason-Kopplung den Schall oktagonal anisotrop (Mendoza-Coto u. a. 2024 [S]).
    - In 3D am Schreibtisch [M, ungeprueft]: Die Phason-Steifigkeit ist l = 6-anisotrop, die Kopplung allein gibt l = 6 beim Laengsschall.
    - Mitlaufende Phasonen: drei zusaetzliche masselose Felder und wieder Richtungsabhaengigkeit.
    - Gepinnte Phasonen (Kachel-Umklappungen mit Barriere): Die Isotropie bis Stufe 5 traegt.
  - Danzer ist nicht Finns Pyrochlor: vier unregelmaessige Tetraeder, raumfuellend wie Finns gefuelltes Netz V.
  - Eine Rechnung zu Licht oder Schwerewellen auf einem ikosaedrischen Raumnetz gegen Messgrenzen fand sich nicht (24-Monats-Abfrage).
- **Kartenvorschlag DANZER-NAEHERUNG-1:** Licht und Skalar auf kubischen Naeherungszellen 1/1, 2/1, 3/2; l = 4-Anteil faellt ~ 1/F_n^2 [H]. Hauptaufwand ist der Bau.
- **Abschaetzung: erledigt.** DANZER-NAEHERUNG-1 wartet auf Finns Weiche:
  - regulaere Tetraeder Pflicht?
  - Phasonen in seinem Takt gepinnt oder frei (Kachel-Umklappungen als Pachner-Zuege, PACHNER-TAKT-1 [H])?
- **Negativliste:**
  - "Ein ikosaedrisches Netz ist von selbst isotrop" (nur mit eingefrorenen bzw. gepinnten Phasonen)
  - "Die Stufe-5-Regel deckt die TT-Steifigkeit" (Stufe 6, braucht Eichinvarianz)
  - "Danzer = Finns Netz"
- **Bedeutung:** Eine dritte Antwort auf Finns Weiche: ein geordnetes, aperiodisches Tetraeder-Netz, das ohne Abstimmung isotrop ist (Licht bis k^4, TT-Masse). Das ist der Grund, den TT-GRUND-1 im Kristall nicht fand. Preis: Die Phasonen muessen ruhen.

### Ernte TORSION-STEIF-1 (RUNDE-37/torsion-steif-1/ERGEBNIS.md; eingetragen 2026-10-05 04:53:18 CEST)

- Code-Agent; eingefroren 04:38:49, Laeufe ueber kleintest.sh (cpu, cpu11) bis 04:46; 2 Abrufe.
- **Urteile:**
  - TS0 verfehlt, nach Kartenwortlaut und nach Plan. Physikalisch erfuellt: Rahmendrehung = Fehlwinkel auf <= 2,1e-14 in 28 Faellen, Eichnullmoden exakt. Die arccos-Auswertung bei delta = 0 lieferte nur 2e-8; mit atan2 im Nachtrag <= 8e-16.
  - TS1 eingetroffen, war aber vorab ableitbar: 18 Rahmendrehungen gegen 14 Kantenbedingungen je Zelle, also mindestens 4. Die Karte hatte "nicht ableitbar" woertlich aus dem Vorschlag uebernommen; Rueckfall der Leitung, im Gedaechtnis vermerkt.
    - Gemessen sind nur: genau 4 bei allgemeinem k, 5 auf Gamma-X, 6 an X und M, 13 bei +-(pi/2)(1,1,1), 8 mit festem Startpunkt.
  - TS2 verfehlt: 25 statt 21 Nullmoden.
- **Ergebnis:**
  - Die 4 Nullmoden sind kruemmungsfreie Rahmendrehungen vom Weitzenboeck-Typ, wie beim Guertel-Feld. Kein Logarithmus-Artefakt, nicht durch die Mittelung.
  - Mit Guertel-Energie auf der Holonomie breiten sie sich aus (Cosserat-Typ, ~ kappa k^2). Q + 2 kappa wird dabei auf Flaechen im k-Raum singulaer.
  - 4 Nullmoden der vollen Matrix bleiben: gedrehte Rahmen bei h = 1, die diese Energie nicht sieht.
  - Christiansen/Hu/Lin 2023 enthaelt nur die Kinematik [S].
- **Abschaetzung: erledigt.** Fuer Finns Weiche "Baender":
  - Baender auf den Linien messen die Kruemmung exakt.
  - Baender zwischen den Zellen tragen eine Verdrehung, die die Regeln nicht festlegen: 4 je Zelle, frei. Erst eine eigene Rahmenenergie macht sie beweglich, ein Rest bleibt frei.
  - Folgekarte (welche Energie hebt den Rest, etwa ein Torsionsquadrat?) erst nach Schreibtisch-Zaehlung und Finns Reaktion.
- **Negativliste:**
  - "Torsion auf dem Netz algebraisch festgelegt"
  - "Guertel-Energie hebt alle Rahmen-Nullmoden"
- 2026-10-05 04:53:18 CEST: RUECKFLUSS-INFO-1 geschrieben (ab 04:50:39) und gestartet.
  - Bau: Vorschlag aus PT-AUSGLEICH-L woertlich, dazu sigma-Leiter und Spurabstand-Technik als Zusatz Leitung.
  - RI0 85 % (Kontrolle), RI1 55 %, RI2 55 %, RI3 45 %.
  - Code-Agent, p4000a/cpu6, 90 min.
  - Aktiv 5: TT-GLAS-1, MATERIE-NETZ-1, PAAR-LICHT-L, REGGE-HADRON-REF-L, RUECKFLUSS-INFO-1. Ein Platz bleibt Puffer fuer Finns Auftraege.

### Ernte PAAR-LICHT-L (RUNDE-37/paar-licht-l/DOSSIER.md; eingetragen 2026-10-05 04:56:03 CEST)

- feldforscher, 24 von 50 min.
  - Selbstanzeigen: Abrufe per curl, erster Abruf leer, nur arXiv-v1 gelesen.
- **Urteile:**
  - PL1, PL2 und PL4 eingetroffen.
  - PL3 nach Wortlaut eingetroffen, die Begruendung der Quellen traegt aber nicht; Urteil offen.
- **Ergebnis [S, M]:**
  - Bisio/D'Ariano/Perinotti (arXiv:1407.6928, Ann. Phys. 368, 2016): omega(k) = 2 omega_W(k/2), langwellig Maxwell.
    - Gleiches Tempo kinematisch, nur fuer freie Felder und nur fuer fast gleich laufende Bausteine.
    - Kleiner Laengsanteil; vier statt zwei bosonische Moden, zwei davon mit Frequenz 0.
    - Wegen des chiralen Weyl-Automaten hat das Tempo ein lineares, richtungsabhaengiges Glied. Der Agent findet fuer Gl. (44) einen um 3 sqrt3 kleineren Vorfaktor.
  - Bose-Statistik: Beide Entwarnungen (Bisio "10^90 modes", Perkins Ein-Moden-Rechnung) zaehlen den falschen Fall.
    - Eigene Rechnung des Agenten [ES/M, ungeprueft]: Im Breitband tragen die Bausteinmoden im Mittel 8 n (n = Photonen je Mode). Bose-Verhalten verlangt n << 1/8.
    - Stimmt das, waeren gemessene Rayleigh-Jeans-Spektren (n >> 1) ein Problem fuer den 3D-Paarbau. Kein "widerlegt".
    - Die Bose-Tests an Photonen (DeMille 1999, English 2010) treffen den Paarbau nicht, weil dort die Photon-Erzeuger exakt kommutieren.
  - Finns Netz [M, nicht gegengelesen]:
    - Formabschnitte der Leitungs-Probe gegengelesen, kein Fehler.
    - Mit FKM-Kegeln (a1 = 0) ist Paar-Licht im k^2-Glied nie langsamer als ein FKM-Fermion, also kein Vakuum-Cherenkov aus diesem Glied.
    - Unterscheidung: Eis-Licht hat 1/3 des kegelgemittelten Fermion-a2, Paar-Licht 1/4.
    - Drei Kegel geben drei Photonsorten. Gleich gekoppelt verdreifachten sie die Photon-Freiheitsgrade im fruehen Universum (BBN, CMB) [L, ES]; ein einziges Photon braucht eine besondere Kopplung [H].
    - Mit Kegeln = Neutrino-Generationen ist Paar-Licht woertlich de Broglies Neutrinotheorie des Lichts [H].
  - Weyl-QCA (D'Ariano/Perinotti): Das Elektron erbt das lineare Glied voll, das Paar-Photon halb.
    - Bei gebrochener Symmetrie mit Vorzugssystem: Vakuum-Cherenkov ab ~2e4 GeV, gegen PeV-Elektronen im Krebsnebel [L] ausgeschlossen.
    - Bei deformierter Symmetrie (DSR) nicht. Finns FKM-Netz betrifft das nicht.
  - Breitere Buendelung (Querimpuls eps k) macht das Licht um 2 eps^2 langsamer; fuer |c_e - c_gamma| < 1e-14 braucht es eps < 7e-8.
- **Kartenvorschlag PAAR-SAETTIGUNG-L** (Literatur und Schreibtisch): Haelt "Bausteinbesetzung ~ 8 n", kennt die Komposit-Boson-Literatur eine Aufhebung, was zeigen Jordan 1935 und Pryce 1938?
- **Abschaetzung: weiter, aber zuerst ein frischer Leser.**
  - Die 8n-Rechnung traegt die staerkste Folgerung (Rayleigh-Jeans-Daten gegen den Paarbau). Sie geht erst nach dem Gegenlesen als Befund an Finn.
  - Gegenlesen und PAAR-SAETTIGUNG-L werden in einem Auftrag zusammengelegt (gleiche Frage), zusammen mit den ungeprueften Schreibtischteilen von PT-AUSGLEICH-L (S4, S5) und DANZER-L (3.4).
- **Negativliste:**
  - "Paar-Licht ist exakt Maxwell" (Laengsanteil, Zusatzmoden)
  - "Bose-Tests an Photonen schliessen den Paarbau aus" (treffen ihn nicht)
  - "Die 10^90-Entwarnung traegt" (falscher Fall)
- **Bedeutung:**
  - Der dritte Weg zu einem Tempo fuer alles existiert kinematisch, und auf Finns Netz liefe Paar-Licht den Elektronen nicht hinterher.
  - Preise: drei Photonsorten, Zusatzmoden, offene Schleifen und vielleicht eine Grenze fuer helles Licht.
- 2026-10-05 04:57:02 CEST: GEGENLESEN-R45 geschrieben (ab 04:56:10) und gestartet; frischer Leser, Haus Anthropic, kein Autor der Dossiers. Drei Teile:
  - A: 8n-Rechnung von PAAR-LICHT-L plus Kartenvorschlag PAAR-SAETTIGUNG-L (Literatur, woertlich)
  - B: PT-AUSGLEICH-L S4 und S5
  - C: DANZER-L 3.2 und 3.4
  - Erwartungen: GL1 60 %, PS1 60 %, PS2 65 %, PS3 70 %, GL2 80 %, GL3 55 %. Zeitbox 90 min, 8 Abrufe.
  - Aktiv 5: TT-GLAS-1, MATERIE-NETZ-1, REGGE-HADRON-REF-L, RUECKFLUSS-INFO-1, GEGENLESEN-R45. Ein Platz bleibt Puffer.
- 2026-10-05 05:02:53 CEST: Loop-Tick. Codex hat auf die Ideation-Runde 1 geantwortet (04:52 und 04:54; gelesen und quittiert):
  - Eigener Strang: A2 (kritische Quellbreite, E-Nulldurchgang, D2d-Folgeform) und A5 (Konkurrenz) haben Vorrang.
    - Papieretappe CRITICAL-WIDTH-PAPER.
    - GAUSSIAN-ENERGY-COMPACTNESS-DRAFT liegt beim Nichtautor.
    - A3 als klassische Kontrolle; A4 zuerst analytisch.
  - Codex' Lektuere unserer Zweige (Entwuerfe, nur gelesen):
    - MATERIE-NETZ-1: gamma_S = 1 bzw. 0 ist eine Konstruktionsidentitaet. Offen ist die Lichtkopplung (Einheits- gegen Laengengewichte); bisher keine Strahlverfolgung durch das inhomogene Quellfeld.
    - TT-GLAS-1: Superzellen-Stabilitaet bei kleinem k ist keine Glas-Stabilitaet.
  - Vorschlag C fuer uns: Lichtpaket auf inhomogener Geometrie, gleiche Quelle, Einheits- gegen geometrische Maxwell-Gewichte, Kontrolle homogene Skalierung. Kandidat nach der MATERIE-NETZ-1-Ernte.
  - KOMPAKT- und WICKEL-Hinweis an claude-video weitergegeben.
  - Bus sonst leer. Scout: kein neuer Lauf seit 02:04Z. Aktiv 5, ein Platz Puffer.
- 2026-10-05 05:06:39 CEST: Finn, woertlich: "Wir brauchen alternative Ideen zum Doppelspaltexperiment" (vor 05:04:59). DOPPELSPALT-L geschrieben (ab 05:05:32) und gestartet.
  - Lesart der Leitung: (a) alternative Erklaerungen, (b) schaerfere bzw. andere Experimente.
  - Ableitbarkeitsprobe [M]: Lineare Wellen auf jedem Netz geben das gewoehnliche Muster und I3 = 0 (Sorkin), also keine Rechnung dazu.
  - Offen:
    - Soliton- bzw. Q-Ball-Teilchen mit innerer Uhr (Streifen nach innerer Frequenz oder nach Masse?)
    - I3-Schranken als Latte fuer nichtlineare Teilchenmodelle
    - Teilchen mit innerer Uhr als Welcher-Weg-Zeuge (Margalit u. a. 2015 [L?])
  - Erwartungen: DS1 80 %, DS2 70 %, DS3 55 %, DS4 70 %, DS5 75 %.
  - feldforscher, 10 Abrufe, 60 min.
  - Aktiv 6 (Puffer fuer Finns Auftrag genutzt): TT-GLAS-1, MATERIE-NETZ-1, REGGE-HADRON-REF-L, RUECKFLUSS-INFO-1, GEGENLESEN-R45, DOPPELSPALT-L.

### Ernte MATERIE-NETZ-1 (RUNDE-37/materie-netz-1/ERGEBNIS.md; eingetragen 2026-10-05 05:09:40 CEST)

- Code-Agent, Start 04:18:53, eingefroren 04:38:20, Text fertig 05:08:22. Alle Laeufe auf der .69 mit rc = 0; L = 16, 24, 32.
  - Ein frischer Leser (pruefer-opus) fand 5 falsche Zahlen und eine falsche Bereichsaussage; eingearbeitet, kein Urteil geaendert. Die letzte Fassung hat er nicht gesehen.
  - Die Meldung kam mit noch laufender Hintergrundarbeit des Agenten; moegliche Nachmeldung beachten.
- **Urteile:**
  - MN0 eingetroffen (Plan und Wortlaut).
  - MN1 nicht eingetroffen.
  - MN2 eingetroffen.
  - Die Ausgaenge von MN0 und MN1 standen vorab fest (PLAN 1.2). gamma_S = 2 kappa'/kappa_g gilt exakt an jeder Ecke, also war "Nahfeld-gamma weicht ab" (MN1) unmoeglich. Rueckfall der Leitung (Karte: "Nahfeld nicht ableitbar"), im Gedaechtnis vermerkt.
- **Ergebnis:**
  - Beide Varianten geben Newtons Takt mit Einsteins Vorzeichen (Uhr nahe der Masse langsamer), fuer Punktquellen und Q-Ball.
    - Fernfeld mu = -A/r mit A = 0,028135 = 1/(8 sqrt2 pi), wie am Schreibtisch.
    - Takt-Operator an allen 32 767 Gitter-k positiv [E].
  - gamma ueber die Eck-Skalierung exakt 1 (V1) bzw. 0 (V2), auf 5e-13. Die Statik haengt weder von der Paarung noch vom Spur-Eichdefekt ab, denn bei p = 0 faellt die Bewegungsenergie heraus.
    - Woertlich (kappa' = 0) hat V2 gar keine Takt-Gleichung; gerechnet als Grenzfall "Raum unendlich steif" (Festlegung).
  - Nahfeld [E, nicht vorab festgelegt]:
    - Ab 1,5 l_P folgt der Takt im Schalenmittel Newton auf 1 %; Einzelecken weichen bis +15 % ab.
    - Der Q-Ball-Takt folgt dem Kontinuum auf <= 0,53 %.
  - Die Zusatzlesart gamma_K traegt so nicht (Referenzfehler); der Nachtrag misst nur Takt gegen Newton.
  - **Maxwell [E, vorab M]:** Mit Einheitsgewichten (LICHT-FINN-NETZ-1, rein topologisch) spuert das Licht die Laengen nicht. Dann ist n = 1/N, also auch in V1 nur die halbe Ablenkung.
    - Mit Gewichten aus den Kantenlaengen faellt das Tempo wie 1/lambda: n = lambda/N = 1 - (1 + gamma) Phi.
- **Abschaetzung: erledigt.**
  - Codex' Vorschlag C (Lichtpaket durch das inhomogene Feld) ist nach Abschnitt 5 im Eikonal-Limes ableitbar (n = lambda/N). Er waere Vorfuehrung bzw. Kontrolle, keine Messung; geparkt.
  - Offen bleiben nur Gitter-Nahfeld, Anisotropie und Dispersion der Ablenkung.
- **Negativliste:**
  - "gamma = 1 auf dem Netz gemessen" (Konstruktionsidentitaet)
  - "V1 gibt die volle Lichtablenkung" ohne den Zusatz "nur mit Laengengewichten fuer Maxwell"
  - "Maxwell auf Finns Netz spuert die Geometrie" (Einheitsgewichte: nein)
- **Bedeutung:** Damit Finns Netz die gemessene Lichtablenkung liefert, braucht es beides:
  - die Energie der Masse in der Eckregel, und Materie tickt mit (V1)
  - Licht, dessen Kopplungen von den Kantenlaengen abhaengen
  - Fehlt das zweite, ist es die halbe Ablenkung, und die ist ausgeschlossen. Im Bild "Raum = Netz" waeren Laengengewichte naheliegend [H].

### Ernte REGGE-HADRON-REF-L (RUNDE-37/regge-hadron-ref-l/DOSSIER.md; eingetragen 2026-10-05 05:15:52 CEST)

- feldforscher, Finn-Auftrag.
  - 23 von 45 Abrufen (3 fehlgeschlagen), 1 von 3 Websuchen.
  - Selbstanzeige: einmal awk in einer Pipe, ohne Wirkung.
- **Urteile:**
  - RH1 knapp eingetroffen: streng 98,3 % fehlerfrei, mit ungenauen Zuordnungen 96,2 %.
  - RH2 und RH4 eingetroffen.
  - RH3 nicht eingetroffen: kein Pomeron als Graviton, kein Brower/Polchinski/Strassler/Tan.
  - RH5 teilweise: kein rotierender String; die lineare Form wird ueber den Oszillator erklaert.
- **Referenzbilanz:**
  - 238 Referenzen, keine erfunden; 237 nachgewiesen. [41] ist ein unveroeffentlichter Konferenzbericht, nicht pruefbar.
  - 216 in Ordnung, 9 kleine bibliografische Fehler.
  - 4 Stellen, an denen die Quelle die Aussage nicht stuetzt; 5 ungenaue Zuordnungen; 3 ohne Abstract nicht pruefbar.
  - Rund 190 Zitierstellen sind nur am Titel geprueft.
- **Einordnung:**
  - JPAC-Auftragskapitel, erschienen in der Encyclopedia of Particle Physics, Bd. 1 (Elsevier 2026), S. 681-704. Die Verlagsfassung hat die Fehler uebernommen.
  - Fehler im Detail:
    - Abb. 9 nennt die falsche JPAC-Arbeit.
    - "CLAS12" statt der Daten des aelteren CLAS.
    - [150] wird fuer alpha_rho(t -> -inf) = -1 zitiert, sagt aber 0 (stoerungstheoretische QCD); die -1 traegt nur [149].
    - "Rising" Wirkungsquerschnitte werden mit Daten von 1961 bis 1965 belegt, die konstant oder fallend sind.
  - Regge-Theorie ist nicht Regge-Kalkuel; die Arbeit von 1961 ist nicht zitiert.
- **Programmbezug [H]:**
  - Glied 7: Unitaritaet verlangt Reggeisierung jedes Austauschs mit l > 1 (hadronisches Vorbild der CEMZ-Turm-Aussage).
    - Zwei Regime: schwach gekoppelt (schmale, lineare Tuerme, Veneziano, CEMZ) gegen stark gekoppelt (|alpha| hoechstens ~ sqrt(s) log s, breite Resonanzen, Tuerme koennen enden: Childers [97], [222], [223]).
    - Hintergrund, kein Beleg fuer Glied 7.
  - Pomeron: Meyer/Teper-Steigung 0,28 alpha'_R ~ 0,25 GeV^-2 = Donnachie/Landshoff. Das 2++-Glueball ist ein massives zusammengesetztes Spin-2 im Turm, nicht das Graviton.
  - Isotacheia: Der Artikel sagt nichts zu Enden mit c; tragfaehig sind [157] und [161].
  - Finns Netz mit Faeden: [167] Y-Knoten 0,47 fm gegen Roehre 0,38 fm (Knoten 25 % dicker); Strukturanalogon auf fm-Skala, nicht die Raumzeit.
  - Q-Baelle: Volkov/Woehnert, J = NQ [S Volltext]. RG-1 (J ~ E^2 bei Ringen) folgt vielleicht aus N ~ R, Q ~ R [ES, nicht gerechnet]. Frage an Finn: Regge-Bahnen oder J = NQ-Leitern?
  - "BPST" heisst im Projekt das Instanton; die Pomeron-Arbeit immer ausschreiben.
- **Kartenvorschlag HISH-GLUEBALL-L** (Literatur): Erklaert HISH (Sonnenschein/Weissman 2019) das Scheitern von PAAR-REGGE-1 am festen Intercept? Gestartet, siehe naechste Zeile.
- **Abschaetzung: erledigt.**
- **Negativliste:**
  - "Der Artikel belegt Enden mit c" (nein)
  - "[150] belegt alpha -> -1" (nein)
  - "BPST" ohne Ausschreiben
- 2026-10-05 05:16:30 CEST: HISH-GLUEBALL-L geschrieben (ab 05:15:52) und gestartet. Vorschlag aus REGGE-HADRON-REF-L woertlich; G1 70 %, G2 65 %, G3 60 %, G4 60 %; feldforscher, 10 Abrufe, 45 min.
  - Aktiv 5: TT-GLAS-1, RUECKFLUSS-INFO-1, GEGENLESEN-R45, DOPPELSPALT-L, HISH-GLUEBALL-L. Ein Platz Puffer.
- 2026-10-05 05:29:15 CEST: Finn, woertlich: "Zum Photon/Licht: Probe mal ob Licht ein Mini Teilansammlung ist was eine Welle erzeugt und was sich splitten kann und dann teile abgibt. Also was wenn Teile aus reiner Energie bestehen bzw viel kleiner sind? Kann man ein Photon spalten?" (vor 05:27:52)
  - LICHT-TEILE-L geschrieben (ab 05:28:18) und gestartet.
  - Ableitbarkeitsprobe [M, P]: Energieerhaltung; Furry; unterlichtschnelle (konkave) Dispersion verbietet jede Vakuumspaltung, also zerfaellt auf Finns Netz kein Photon. Keine Rechnung.
  - Offen: Spaltung in Materie und Feldern, g^(2)(0)-Rekorde, Kompositheits-Schranken, Strukturfunktion des Photons, Subquanten-Ideen.
  - Erwartungen: LT1 85 %, LT2 70 %, LT3 75 %, LT4 50 %, LT5 80 %.
  - feldforscher, 8 Abrufe, 50 min. Kopplung an DOPPELSPALT-L (Grangier/Roger/Aspect dort lesen, nicht doppelt abrufen) und PAAR-LICHT-L.
  - Aktiv 6 (Puffer fuer Finns Auftrag genutzt).

### Ernte DOPPELSPALT-L (RUNDE-37/doppelspalt-l/DOSSIER.md; eingetragen 2026-10-05 05:34:53 CEST)

- feldforscher, Finn-Auftrag, 26 von 60 min.
  - Abrufe 10 von 10, Websuche 2 von 2.
  - Ein Abruf scheiterte an HTTP 429, einer an HTTP 404.
- **Urteile:**
  - DS1 eingetroffen, mit Nuance: Die Tropfen-Nachpruefungen fanden Doppelspaltmuster, aber quantitativ andere, mit scharfen Spitzen.
  - DS2 in der Groessenordnung eingetroffen. Beste gefundene Einzelphoton-Schranke I3 ~ 4e-4 +- 5e-4 (2021), 2-sigma etwa 1,4e-3. Fuer massive Teilchen vermutlich ~1e-2 (ungeprueft).
  - DS3 nicht entschieden, Tendenz verfehlt: Es gibt Vorarbeit, Darrow/Bush 2025 und einen Soliton-Doppelspalt 2015.
  - DS4 eingetroffen, belegt durch das Experiment von Namdar u. a. (2112.06965), nicht durch Sorkin oder Ududec.
  - DS5 eingetroffen (Margalit u. a. 2015).
- **Ergebnis:**
  - Darrow/Bush 2025 (PRR 7, 033288) [S]: Ein klassisches Teilchen mit Compton-Zitterbewegung trifft die Fraunhofer-Muster fuer Einzel- und Doppelspalt (Guete 1,36 bzw. 0,89). Die Streifenlaenge ist aber nur (b/68)^2 mal die de-Broglie-Laenge (b = Kopplung) und gilt nur fuer langsame Teilchen. Die innere Uhr allein liefert nicht h/p.
  - Namdar u. a.: Nichtlineare Dynamik erzeugt messbar I3 != 0. Born-Regel-Bruch und nichtlineare Entwicklung trennt man ueber die Staerke der Nichtlinearitaet.
  - Soliton-Doppelspalt 2015 (1508.06837): Das Soliton teilt sich und vereint sich wieder; das Muster verschwindet bei Spaltabstand groesser als das Soliton. Nur aus dem Suchmaschinenauszug bekannt, vor jeder Q-Ball-Karte lesen.
  - Q-Ball [M, Schreibtisch des Agenten]: Die Phasenwelle eines bewegten Balls, 2 pi/(gamma omega v), ist Q- bis 1,41 Q-mal laenger als die de-Broglie-Laenge des ganzen Balls (aus Derrick-Skalierung und E < m Q).
  - Gegensweep, Fehler der Leitung: Die Kartenzeile "Sorkin/Dreifachspalt nicht im Projekt" war falsch. gitter-checkliste.json (09.09.) fuehrt W3 "Dreispalt-Test des Sorkin-Parameters" als harte Messung, verknuepft mit dem inneren Uhren-Bild; Pruefpunkt "Rabi-Runner" offen. Mein grep lief nur ueber *.md; im Gedaechtnis vermerkt.
- **Kartenvorschlag QBALL-DOPPELSPALT-1** mit vier Vorhersagen, die scheitern koennen: Reichweite, Takt ~ 1/(gamma v), I3 >= 0,05, Doppelklick. Schwellen an Gitter- und Stossparameter-Konvergenz gebunden. Dazu vier weitere Anstoesse.
- **Abschaetzung: erledigt.** QBALL-DOPPELSPALT-1 wird gestartet, mit Pflichtlektuere von 1508.06837 vorab.
- **Negativliste:**
  - "Die innere Uhr gibt die de-Broglie-Laenge" (Darrow/Bush: (b/68)^2; Q-Ball: Q-fach zu lang)
  - "Tropfen zeigen keinen Doppelspalt" (sie zeigen einen, aber einen anderen)
  - "Dreifachspalt im Projekt neu"

### Ernte GEGENLESEN-R45 (RUNDE-37/gegenlesen-r45/GEGENLESEN.md; eingetragen 2026-10-05 05:34:53 CEST)

- Frischer Leser, Haus Anthropic; 04:57:00 bis 05:31:43.
  - 7 von 8 Abrufen, nur 2 mit Inhalt; die arXiv-API sperrte, Selbstanzeige paralleler Erstabruf.
- **Urteile:** GL1, PS2, GL2 und GL3 eingetroffen; PS1 und PS3 offen.
- **Teil A, Paar-Licht:**
  - Die 8n-Zaehlung haelt fuer jede Verschmierung; 8 ist bei zwei Bausteinen sogar das Minimum (Jensen).
  - Harte Pauli-Grenze: n <= 1/8 je Polarisation (unpolarisiert), 1/4 bei einer Linearpolarisation.
  - Keine Aufhebung, auch nicht mit gefuelltem See.
  - Der Fremdmoden-Term steckt schon in Bisios Kriterium (Gl. (34)); nur dessen Abschaetzung in Abschn. VI laesst ihn weg.
  - Korrekturen: Der Abzug 2 eps^2 gilt nur bei querem Relativimpuls (sonst 4/5 bzw. 4/3 eps^2). Die Cherenkov-Formel lautet E^3 ~ m_e^2 E_P/(4 |a1|). Der 3 sqrt3-Faktor zu Gl. (44) haelt (Folgearbeit 1608.02004).
  - Auswege offen: Dichtebau mit Dirac-See (Jordan, Bosonisierung) und N innere Zustaende (8 n/N).
- **Teil B, PT:** haelt, mit zwei Auflagen im Wortlaut (A-8: nur fuer Zustaende in den alpha-Baendern; A-9: zwei verschiedene Theta).
- **Teil C, Danzer:** haelt exakt.
  - tr B^3 = 29/27, 26/27, 687/729.
  - Laengsanteile 16/25, 4/25, 16/225; Kugelmittel 48/175.
  - Zaehlung 4/9/5, Eichprobe und l = 6-Aussage bestaetigt.
- **Bindend fuer Berichte und v4:** A-1 bis A-9 duerfen nicht stehen; V-1 bis V-7 nur mit Vorbehalt (GEGENLESEN.md, Abschn. 4). Fuer Finn gilt V-1 woertlich mit Vorbehalt.
- **Abschaetzung: erledigt.**

### Ernte RUECKFLUSS-INFO-1 (RUNDE-37/rueckfluss-info-1/ERGEBNIS.md; eingetragen 2026-10-05 05:34:53 CEST)

- Code-Agent; eingefroren 05:08:54; acht Hauptlaeufe und die Auswertung auf der .69 mit rc = 0 (03:09 bis 03:28 UTC).
- **Urteile:**
  - RI0 eingetroffen.
  - RI1 nicht eingetroffen.
  - RI2 nach Plan nicht auswertbar, nach Wortlaut nicht eingetroffen.
  - RI3 eingetroffen.
- **Ergebnis:**
  - Bei festen Takten und W = 2 pi steigt D(t) nie wieder an: Summe der Anstiege im Mittel 0, groesster Einzelanstieg 9,0e-4. Die 44 % bremsen den Verlust, kehren ihn nicht um. (Vorab abschaetzbar, so im Plan.)
  - Neu: Die sichtbaren Teile von A und B bleiben orthogonal (>= 0,999996), also folgt D genau dem Gewicht (q = 1,002).
    - Wer die Takte kennt, kann das zurueckgekommene Gewicht voll zuordnen.
    - Wer sie nicht kennt, sieht kein Spin-Gedaechtnis (Spin-Schranke 0,1648 = FJ-Wert).
    - Einen Wiederanstieg gibt es nur bei teilweise kohaerenten Takten (W = pi: einmal +0,0059 bei t = 2).
  - r(100) = 0,4401 +- 0,0017 (sigma 4), 0,4354 (sigma 8), 0,4319 (sigma 12); bei sigma 4 bis t = 200 bei 0,443.
    - Mit neu gezogenen Takten r ~ 0,49 (Kopfrechnung).
    - Die 44 % sind also eine Kennzahl fester Takte, kaum breitenabhaengig.
  - Der Gram-Schaetzer mit M = 8 ist stark verzerrt (Nullkontrolle 0,443 statt 0); so im Plan angekuendigt.
- **Selbstanzeigen:**
  - erster Startbefehl fehlerhaft (nur 1 von 3 Ketten)
  - Heimatverzeichnis der .69 gelistet
  - rekursiver grep ohne Ausschluesse ueber spiegel-haelfte-1 (nichts Versiegeltes)
  - jq-Zaehlfilter
- **Abschaetzung: erledigt.** Die Zahl 44 % in GEMEINSAMES-NETZ v4 bleibt, mit "r = 0,43 bis 0,44 fuer sigma 4 bis 12, feste Takte".
- **Negativliste:**
  - "Die 44 % bringen Information zurueck", ohne den Zusatz "nur fuer einen Beobachter, der die Takte kennt"
  - "Die 44 % gehen gegen 1/2" (fuer feste Takte nein)
- Aktiv 3: TT-GLAS-1, HISH-GLUEBALL-L, LICHT-TEILE-L.
- 2026-10-05 05:36:38 CEST: Gepruefte Pauli-Grenze (Gegenlesen V-1, woertlich mit Vorbehalt) an LICHT-TEILE-L weitergegeben, zum Einbeziehen in Abschnitt 4 und 5 (Kopplung "Teilansammlung" und Paar-Licht).
- 2026-10-05 05:36:38 CEST: QBALL-DOPPELSPALT-1 geschrieben (ab 05:35:29) und gestartet.
  - Vorschlag aus DOPPELSPALT-L woertlich; Zusaetze der Leitung: Energiebilanz-Pflichtzeile (d), Ableitbarkeit (e), Pflichtlektuere 1508.06837 zuerst.
  - V-Q1 85 % (Kontrolle), V-Q2 35 %, V-Q3 55 %, V-Q4 40 %.
  - Code-Agent, p4000a/p4000b, 150 min.
  - Aktiv 4: TT-GLAS-1, HISH-GLUEBALL-L, LICHT-TEILE-L, QBALL-DOPPELSPALT-1.

## Abschaetzung am Rundenende (2026-10-05 05:37:45 CEST)

| Karte | Ausgang | Abschaetzung |
|---|---|---|
| BOUFOUROU-DR4-L | BF1 ja, BF2 nur formal, BF3 nein; fremdes DR4-Protokoll nicht gebunden; Boufourous DR3 2,25 sigma ueber Newton | erledigt |
| DREI-KEGEL-L | DK1 ja, DK2 nein, DK3 ja (Kontrolle); Triplett nur unter Translations-A4 [H] | parken |
| DREI-KEGEL-NEUTRINO-L | DN-1 nach Wortlaut ja; l < ~20 bis 40 l_P (Regime B), Regime A ausgeschlossen; Isotropie braucht Abstimmung auf ~2e-28 | erledigt |
| PT-AUSGLEICH-L | PA1 Kern ja, PA2 nein, PA3 teilweise; Ausgleich bricht bei k = 0, ist keine Massenquelle | erledigt (als L5-Weg verworfen) |
| DANZER-L | DZ1 bis DZ3 ja (DZ2 beim TT-Tempo bedingt); isotrop bis Stufe 5, solange Phasonen ruhen | weiter, nach Finns Weiche (regulaere Tetraeder? Phasonen?) |
| TORSION-STEIF-1 | TS0 nein (Auswerteformel), TS1 ja (vorab ableitbar), TS2 nein; 4 freie Rahmendrehungen je Zelle | erledigt; Folgekarte nach Finn |
| PAAR-LICHT-L | PL1, PL2, PL4 ja; PL3 offen | erledigt; Pauli-Grenze nach Gegenlesen (V-1, mit Vorbehalt) |
| MATERIE-NETZ-1 | MN0 ja, MN1 nein (vorab entschieden), MN2 ja | erledigt; volle Ablenkung nur mit V1 plus Laengengewichten |
| REGGE-HADRON-REF-L | RH1 knapp ja, RH2 und RH4 ja, RH3 nein, RH5 teilweise; 238 Referenzen, keine erfunden | erledigt; HISH-GLUEBALL-L laeuft |
| DOPPELSPALT-L | DS1, DS4, DS5 ja; DS2 Groessenordnung; DS3 offen | weiter: QBALL-DOPPELSPALT-1 laeuft |
| GEGENLESEN-R45 | GL1, PS2, GL2, GL3 ja; PS1, PS3 offen | erledigt; A-1 bis A-9 bindend |
| RUECKFLUSS-INFO-1 | RI0 und RI3 ja, RI1 nein, RI2 nicht auswertbar; r = 0,43 bis 0,44 fuer sigma 4 bis 12 | erledigt |
| Leitung: zwei Scout-Arbeiten | Gielen/Ried (Zeit = 4-Volumen im Regge-Netz) und Boguna/Krioukov (Linkstatistik randabhaengig); kein Projektergebnis betroffen | erledigt |
| Leitung: Codex | Kurzreview und Ideation-Runde 1; Codex nimmt A2 und A5, berichtigt A1 | laufend (Codex-Strang) |

**Uebergabe an Runde 46:**
- Laufend: TT-GLAS-1, HISH-GLUEBALL-L, LICHT-TEILE-L, QBALL-DOPPELSPALT-1.
- Offene Fragen an Finn:
  - regulaere Tetraeder bzw. Phasonen (Danzer)
  - Q-Ball-Anregungen: Regge-Bahnen oder J = NQ-Leitern?
  - Licht mit Laengengewichten (naheliegend im Bild "Raum = Netz")
- Warteschlange:
  - DANZER-NAEHERUNG-1 (nach Finn)
  - Torsions-Folgekarte (nach Zaehlung und Finn)
  - GEMEINSAMES-NETZ v4 (Leitung, nach TT-GLAS-1, mit A-Liste von GEGENLESEN-R45)
  - PAAR-Auswege (Jordan/Bosonisierung, N innere Zustaende)
  - FINN-PLATTE-1 geparkt

### Ernte TT-GLAS-1 (RUNDE-37/tt-glas-1/ERGEBNIS.md; eingetragen 2026-10-05 05:39:22 CEST)

- Code-Agent; fertig 05:38, 80 von 120 min.
  - Volles Hamilton-Netz auf Zufallsnetzen; den Rayleigh-Ersatz nicht gerechnet, weil er vorab fast sicher isotrop gewesen waere.
  - Ein frischer Leser (pruefer-opus) fand 5 A-, 12 B- und 9 C-Befunde, alle uebernommen, kein Urteil geaendert. Den N = 512-Nachtrag hat er nicht gesehen.
- **Urteile:**
  - TG-G0 eingetroffen: regelmaessiges Netz V 6,3389 % gegen 6,3388 %.
  - TG-G1 eingetroffen: p = -0,475, 95 %-Bereich -0,537 bis -0,413.
  - TG-G2 verfehlt, allein durch N = 128: 3 von 13 Richtungen ueber 2 SE, groesster Wert 3,23. Lesart des Agenten Zufall [H], weil die Regel die t-Verteilung bei 12 Netzen nicht beruecksichtigte; nicht nachtraeglich gelockert.
  - TG-G3 verfehlt (hochgerechnet 2,17 % bei N = 8000), nach Wortlaut nicht entscheidbar (N = 8000 nicht gerechnet).
- **Ergebnis [E]:**
  - Das Glas traegt Schwerewellen: Alle 48 Netze (N = 32 bis 256, je 12 Saaten) haben an allen 16 Punkten genau zwei masselose TT-Moden; nichts waechst. Geprueft nur bei kleinem k, der TT-Anteil nur in drei Richtungen.
  - Spanne je Netz in omega^2/k^2: 29,7 / 22,9 / 15,3 / 11,4 % (N = 32 bis 256), dazu N = 512: 7,2 %. In der Geschwindigkeit etwa die Haelfte; der groessere Teil ist Doppelbrechung.
  - Die affine Regge-Steifigkeit ist isotrop (<= 8,2e-6, N = 256 bis 8000). Die Spanne kommt also aus der Bewegungsenergie bzw. der nichtaffinen Relaxation, nicht getrennt gerechnet.
  - Bewegungsgewichte: J ~ V macht die meisten Netze instabil; J ~ 1/V ist stabil, aber anisotroper; J = 1 ist am isotropsten.
- **Selbstanzeigen:**
  - N-Leiter nur 32 bis 256 statt 500 bis 8000 (dichte Rechnung ~ E^3; so im Plan).
  - |k| und Klassenschwellen vor dem Einfrieren geaendert, ohne Werte zu kennen.
  - Rauchlauf ohne --rauch.
  - tg_auswertung.py einmal per scp ueberschrieben (gleicher Inhalt, gegen die mv-Regel).
  - jq min/max und einmal lokal awk.
  - Nachtrag nach Sicht der Ergebnisse.
- **Abschaetzung: weiter.**
  - Der Glas-Zweig traegt die zwei TT-Moden ohne Abstimmung. Der Preis ist eine Anisotropie je Netz ~ N^-0,47, ueberwiegend Doppelbrechung.
  - Offen: Stabilitaet bei endlichem k, nichtaffine Relaxation, groessere N.
  - Messbezug [H, ES]: Fuer eine Welle der Laenge lambda zaehlt N ~ (lambda/l)^3. Die Anisotropie faellt dann wie (l/lambda)^1,4 und ist fuer Gravitationswellen (lambda ~ 1e3 bis 1e7 m) bei jeder kleinen Masche verschwindend. Das gilt nur, wenn sie sich ueber die Wellenlaenge mittelt; nicht geprueft.
- **Negativliste:**
  - "Glas ist von selbst isotrop" (nur im Mittel; jedes Netz anisotrop, ~ N^-0,47)
  - "Auf Zufallsnetzen stabil" (nur kleines k)

### Ernte HISH-GLUEBALL-L (RUNDE-37/hish-glueball-l/DOSSIER.md; eingetragen 2026-10-05 05:39:22 CEST)

- feldforscher, 05:16:32 bis 05:37:06; 10 von 10 Abrufen, drei ohne Inhalt (INSPIRE-Syntax, arXiv-Drosselung).
- **Urteile:** G1 bis G4 eingetroffen (gefaltet geschlossen, alpha'/2 ~ 0,45 GeV^-2, Intercept frei, keine Endmassen; Daten Meyer, Lucini/Teper/Wenger u. a.).
- **Bedeutung nach Karte (G2):** PAAR-REGGE-1 ist teils literaturbekannt.
  - Bekannt war: Das leichteste 2++ liegt zu tief fuer eine String-Gerade ("lower than we would expect", HISH 2015), und der Intercept gilt als frei.
  - Eigener Befund bleibt: der Fit mit Endmassen bei festem Intercept 0 bzw. 1/12.
- **Erwartungsverstoesse:**
  - Finns Paar mit doppeltem String ist veroeffentlicht.
    - Sharov 2006 bis 2008: geschlossener String mit zwei Punktmassen (nur Abstracts).
    - Sonnenschein/Weissman 2020: Massen an den Faltstellen geben einen festen Intercept, 2 fuer geschlossene und 1 fuer offene Strings. Gitter-Vergleich nur angeregt.
  - Sonnenschein/Weissman legen 2++ und 4++ auf verschiedene Trajektorien: Gerade durch 0++, angeregtes 2++, 4++, 6++ mit Steigung 0,43(3) gegen Meyer/Teper 0,28(2). Das Datenpaar von PAAR-REGGE-1 mischt nach ihrer Lesart zwei Trajektorien.
  - 1/12 ist nur der Casimir-Anteil; fuer rotierende Strings gilt 1 bzw. 2. Das Vorzeichen in ihrer Gl. (3.12) ist umgekehrt.
- **Kartenvorschlag PAAR-REGGE-2:** das Paar mit dem Literatur-Intercept 2 bzw. 1 rechnen; vorher Sharov im Volltext lesen. Ausgang offen (ohne Massen liegen beide Varianten unter den Gitterwerten).
- **Abschaetzung: erledigt.** PAAR-REGGE-2 in die Warteschlange; Finns rotierendes Paar ist damit Literatur mit offenem Gittertest.
- **Negativliste:**
  - "PAAR-REGGE-1 ist ein neuer Befund" (nur der Teil mit Endmassen bei festem Intercept)
  - "Intercept 1/12 fuer rotierende Strings" (nur Casimir)

**Nachtrag zur Abschaetzung am Rundenende:**

| Karte | Ausgang | Abschaetzung |
|---|---|---|
| TT-GLAS-1 | TG-G0, TG-G1 ja; TG-G2 verfehlt (N = 128); TG-G3 verfehlt hochgerechnet bzw. nicht entscheidbar; zwei TT-Moden in allen 48 Netzen | weiter (endliches k, groessere N) |
| HISH-GLUEBALL-L | G1 bis G4 ja; PAAR-REGGE-1 teils bekannt; Finns Paar = Sharov bzw. Sonnenschein/Weissman 2020 | erledigt; PAAR-REGGE-2 in die Warteschlange |

- Laufend in Runde 46: LICHT-TEILE-L, QBALL-DOPPELSPALT-1.
- 2026-10-05 05:41:04 CEST: Runde 45 geschlossen und veroeffentlicht: claude-runde-v3-45-20261005, Journal nr 593, 35 Quellen mit sha256, pruefen ohne Befund, rc 0. Bus vor dem Journal gelesen (keine offenen Nachrichten).
  - Das Ergebnisfeld musste auf <= 1800 Zeichen gekuerzt werden; die lange Fassung liegt als journal-filter.jq.bak-lang.
  - A-Liste aus GEGENLESEN-R45 beachtet: kein "widerlegt", V-1 mit Vorbehalt, PT ohne Pseudo-Unitaritaet ausserhalb der alpha-Baender.
