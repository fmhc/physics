# PLAN WOLFRAM-KEV-SCAN (Runde 37, .69-Ordner runde41-wolfram-kev)

Code-Agent wolfram-kev-scan, Leitung claude-primary. Plan geschrieben 2026-10-04 ab 14:51 CEST (date), nach Abruf,
Aufbereitung, blinder Handeinstufung und Rauchlaeufen 0 und 1; eingefroren vor dem ersten Hauptlauf (Zeit und Hashes in
EINGEFROREN-SHA256.txt). Alle Zeiten per date; .69-Zeiten in den Logs sind UTC (= CEST minus 2 h).

## 1. Ziel

Alle abgerufenen Seiten von wolframphysics.org in Abschnitte teilen und von Kev (kleines Entscheidungsmodell, lokal auf der .69)
nach unseren fuenf Schichten bewerten lassen; Leseliste fuer Leitung und feldforscher (WOLFRAM-SCAN-L). Kev ist fuer Physik nicht
kalibriert: die blinde Gegenprobe entscheidet, ob Kev mehr leistet als eine Stichwortsuche. "Kev hilft nicht mehr als grep" ist ein
zulaessiges Ergebnis.

## 2. Abruf (erledigt, Teil der Datengrundlage, nicht Teil der Pruefung)

- robots.txt (14:20:16): `User-agent: * / Disallow:` (leer) -> alles erlaubt; Sitemap mit 1569 URLs (959 universes, 246
  technical-introduction, 216 visual-gallery, 113 questions, 22 archives, Rest Einzelseiten).
- code/crawl.sh, per `source` im Agenten-Shell (nur curl, sed, grep, sort, cut, sha256sum, date): nacheinander, 1,2 s Pause nach
  jedem Abruf, User-Agent "fmhc-physics-research-scan (contact: project lead)", nur https://www.wolframphysics.org, nur text/html
  (sonst Datei sofort geloescht), Endungsfilter vor dem Abruf (keine PDFs, Notebooks, Programme), Formularseiten
  (ask-a-question, downloads?i=) ausgelassen, hoechstens 600 Abrufe.
- Reihenfolge: P1 Einzelseiten + technical-introduction + questions + archives (266), P2 Registerlisten (61), P3 in P1/P2
  verlinkte, nicht in der Sitemap stehende Seiten (199 entdeckt, 198 geholt), P4 Register-Einzelseiten universes/wm* bis zur
  Obergrenze (75 von 898).
- Ergebnis 14:23:55 bis 14:43:43: 600 Abrufe, 496 HTML-Seiten ok, 55 RSS-Feeds (Sitemap-Eintraege .../feed/, verworfen),
  43 x 404, 4 x 301 (Weiterleitung auf bulletins.wolframphysics.org, nicht verfolgt), 1 fremder Host (writings.stephenwolfram.com),
  1 Abbruch. Index: seiten/INDEX.tsv (URL, Zeit, HTTP, Typ, Bytes, sha256, Ziel-URL, Datei, Status).
- Bekannte Luecken (Selbstanzeige, siehe ERGEBNIS.md): (a) die Bulletins liegen auf der Subdomain bulletins.wolframphysics.org und
  wurden nicht abgerufen; (b) 55 Abrufe gingen an RSS-Feeds und 54 an Dubletten (Links ohne Schraegstrich), dadurch nur 75 der
  898 Register-Einzelseiten; (c) visual-gallery nur die Startseite (Rest sind Bild-/PDF-Downloadseiten).

## 3. Aufbereitung (code/aufbereiten.py, .69, CPU-Spur, Standardbibliothek)

- HTML zu Text mit html.parser; uebersprungen: script, style, nav, header, footer, form, svg u. a. sowie Elemente mit
  Klassen/IDs TableOfContents, side-nav, search, pagination, running-head, menu, copyexpr/c2c (Code-Bilder) u. a.; gibt es
  `<main>`, zaehlt nur dessen Inhalt.
- Abschnitte: Absaetze unter ihrer Ueberschrift sammeln; Abschnitt schliessen, wenn >= 300 Woerter und (neue Ueberschrift oder
  > 450 Woerter), spaetestens bei 600; Absaetze > 450 Woerter an Satzgrenzen teilen; Reste < 150 Woerter an den Vorgaenger
  haengen; Abschnitte < 20 Woerter verwerfen. Kurze Seiten (Register, Q&A) bleiben ein kurzer Abschnitt.
- Dubletten: gleiche Seitendatei (sha256) nur einmal (54 verworfen), gleicher Abschnittstext nur einmal (4 verworfen).
- Kev-Zustand je Abschnitt: "Page: <Titel>\nSection: <Ueberschrift>\n\n<Text>".
- Ergebnis (Lauf 14:46, daten/aufbereitung-statistik.json): 548 Abschnitte aus 414 Seiten, 145 932 Woerter, Median 269 Woerter
  (329 unter 300, 219 zwischen 300 und 600, keiner ueber 600); 224 Register, 206 technical-introduction, 71 questions, 47 sonstige.
  Erste Fassung (daten-v1, 651 Abschnitte) hatte Dubletten und ist verworfen; ihre Stichprobe wurde nie gelesen.

## 4. Fragenkatalog (code/fragen.json, englisch, weil Seiten und Kev-Training englisch sind)

| ID | Typ | Frage (gekuerzt) | Antwort |
|---|---|---|---|
| S0 | score 0-10 | discrete substrate with its own dynamics: network/hypergraph rewritten by an update rule | Mittelwert der 11 Stufen |
| S1 | score 0-10 | propagation and relativity: emergent dimension, light cones, maximum speed, Lorentz invariance, frames | dto. |
| S2 | score 0-10 | matter content: particles as stable localized structures, spin 1/2, fermions, photons, gauge fields | dto. |
| S3 | score 0-10 | interactions: charge, coupling strength, forces, scattering, binding | dto. |
| S4 | score 0-10 | gravity: curvature, Einstein equations, general relativity, Newtonian limit, black holes | dto. |
| konkret | noul | concrete, checkable statement (explicit rule, number, recomputable result)? | p(ja) |
| art | choice | derivation / computation / claim / outlook / other | wahrscheinlichste Option |
| kausal | noul | refers to causal graphs or causal sets (causal relations between updating events)? (Bezug Ue3) | p(ja) |

Score-Stufen: "0 (not about this at all)", "1" ... "4", "5 (partly about this)", "6" ... "9", "10 (this is the central topic)".
Alle acht Fragen in einem Durchgang je Abschnitt (Zustand einmal gerechnet, jede Frage als eigene Zeile; Kev-Isolation).

## 5. Modellwahl: kev-0.8b (jaredpalmer/kev-0.8b, Snapshot c917ede), nicht brain-kev-0.8b

- kev-0.8b ist auf allen drei Fragetypen trainiert (decision-v7: englische Klassifikations-, NLI-, BoolQ-, Bewertungs- und
  Regeldaten); unsere Fragen sind englische Themen- und Bewertungsfragen zu Fliesstext, also am naechsten an AG-News/BoolQ/SST.
- brain-kev-0.8b ist ein Delta-Feinschliff (lr 2e-5, 2 Epochen) auf ~6300 deutschen Retrieval-Faellen aus Claude-Sitzungen mit nur
  noul/choice ("Beantwortet der Ausschnitt die Frage?", Kandidatenwahl, Segment, Antwortart) und keinem einzigen score-Beispiel;
  seine guten Werte (brain_relevant Acc 0,892) gelten fuer diese Domaene. Fuer englische Physiktexte mit score-Fragen ist das
  allgemeine Modell die vorsichtigere Wahl. brain-kev bleibt ungetestet (Selbstanzeige, moeglicher Folgeversuch).
- Groesse 0.8B, weil nur dieses Kev auf der .69 liegt (kein Download) und es neben dem dauerhaft geladenen Ollama-Modell
  (qwen3.6-35b, keep_alive unbegrenzt, 5-6 GB je P4000) noch in den freien GPU-Speicher passt.

## 6. Technik (code/kev_lauf.py -> code/kev_bewerten.py)

- Start nur ueber kleintest.sh (Spur p4000b, bei Sperre p4000a; CPU-Spuren sind fuer 548 Abschnitte zu langsam: Xeon E5-2630 v2
  ohne AVX2, ein Kern, geschaetzt > 30 s je Abschnitt). kev_lauf.py (Physik-venv) ruft ~/brain-kev/kev/.venv/bin/python als
  Unterprozess derselben Einheit; kein Server, kein Dienst. HF_HOME zeigt auf runde41-wolfram-kev/hf-leer, Offline-Schalter an,
  PYTHONDONTWRITEBYTECODE=1: in ~/brain-kev wird nichts geschrieben; Modelle ueber absolute Snapshot-Pfade.
- Laden: Basis Qwen3.5-0.8B-Base (Revision dc7cdfe) direkt auf die GPU in fp16 (device_map), LoRA eingerechnet (Delta in fp32
  berechnet, auf fp16 gerundet), Einbettungstabelle (248320 x 1024) auf der CPU nachgeschlagen, Rest auf der GPU (960 MiB nach dem
  Laden, Spitze 1,5 GiB). Abweichung vom Kev-Referenzpfad (fp32, Autor: bf16 weicht um hoechstens 0,017 ab): Pascal kennt kein
  bf16-GEMM, fp32 passt nicht sicher in den freien Speicher. Gated-DeltaNet und causal_conv1d laufen in der langsamen
  PyTorch-Referenz (flash-linear-attention nicht installiert; korrekt, nur langsamer).
- Je Abschnitt: kev.model.encode (max_state 8192 wie kev.serve), DecisionModel.prefix (Zustand) und _branch_rows_from_prefix
  (acht Fragezeilen), kev.api.to_answers; Rohwahrscheinlichkeiten werden mitgeschrieben. Eine JSON-Zeile je Abschnitt,
  anhaengend; Folgelaeufe setzen fort. Kein neuer Abschnitt nach 530 s seit Prozessstart (Einheit endet hart nach 600 s).
- Hauptlauf: Abschnitte abwechselnd auf zwei Haelften verteilt (lauf-69/ids-a.txt, ids-b.txt, je 274), parallel auf p4000a und
  p4000b, je Haelfte so viele <= 10-min-Laeufe wie noetig (Ausgabe lauf-69/kev-a.jsonl, kev-b.jsonl, Logs lauf-69/lauf-*.log).
  Ist eine Spur gesperrt, laufen beide Haelften nacheinander auf der freien Spur.

## 7. Rauchlaeufe (vor dem Einfrieren)

- Rauch 0 (12:31-12:41 UTC, p4000b, Laden ueber die CPU): Speicherspitze 4,0 GB = MemoryMax, Einheit nach 600 s ohne Bewertung
  beendet; Ursache: kalte HDD (Seagate ST3250310AS, ~18 MB/s unter Last) und Laden ueber den Host-Speicher. Daraufhin Lader
  umgebaut (direkt auf die GPU).
- Rauch 1 (12:43-12:50 UTC, p4000b, vier synthetische Zustaende, keine Seitenabschnitte): laeuft; Importe 344 s (kalte HDD),
  Laden 13 s, erster Abschnitt 19 s (Aufwaermen), danach ~0,62 s; keine NaN; Host-Spitze 1,3 GB. Plausibilitaet: Schwerkrafttext
  S4 8,53 (Schuhticket 4,25), Hypergraphtext S0 8,42 und kausal 0,99 (andere <= 0,05), Teilchentext S3 7,15, aber S2 nur 5,57;
  das Schuhticket bekommt trotzdem S0 5,82 und S3 5,39: Kev-Scores sind stark gestaucht (Masse auf den beschrifteten Stufen 5 und
  10), nur die Rangfolge ist brauchbar, nicht der Absolutwert.
- Rauch 2 (12:50:54-12:56:22 UTC, p4000b, neun echte Abschnitte, nicht aus der Stichprobe, sechs davon die laengsten):
  Importe 211 s (kalte HDD; gleichzeitig lud Ollama ein Modell von derselben Platte, IO-Druck ~40 %), Laden 69 s, erster
  Abschnitt 19,6 s (Aufwaermen), danach 0,71 bis 1,55 s je Abschnitt (Median 1,16 s; Zustaende 201 bis 1169 Token), keine NaN,
  GPU-Spitze 1532 MiB, Einheit-Speicher <= 2,7 GB. Hochrechnung: 548 Abschnitte ~ 11 min reine Rechenzeit, verteilt auf zwei
  Spuren je ~5-6 min plus Import/Laden; ein bis zwei Runden je Spur. Auswertungscode an diesen neun Abschnitten mit
  willkuerlichen Testlabels (rauch-69/hand-test.json, keine Gegenprobe) ohne Fehler durchgelaufen (rauch-69/auswertung-test/).
- Hinweis: Zustaende bis ~1200 Token liegen ueber Kevs Trainingslaenge (384 Zustandstoken); Kev erlaubt 8192, ist aber dort nicht
  trainiert (Kev-README, Limitations).

## 8. Gegenprobe (blind, Karte Schritt 3)

- Stichprobe: 25 Abschnitte, random.Random(20261004).sample der sortierten IDs (daten/gegenprobe-ids.txt).
- Handeinstufung je Schicht und fuer kausal (0/1) mit Notiz: gegenprobe-hand.json, geschrieben 14:47:47 (date), sha256
  b05aae2f...; zu diesem Zeitpunkt lagen keine Kev-Werte fuer Seitenabschnitte vor (nur Rauch 0 ohne Werte, Rauch 1 synthetisch
  und noch nicht gelesen). Regel: 1 = substantieller Inhalt zur Schicht, nicht nur ein Stichwort; Grenzfaelle in der Datei.
- Verteilung der Handlabels: S0 20, S1 3, S2 2, S3 0, S4 1, kausal 12 von 25. S3 entfaellt (k = 0); S1, S2, S4 haben wenig
  Trennschaerfe (Selbstanzeige: Stichprobe ist klein und vom Register dominiert).
- Stichwort-Vergleich (code/stichworte.json): je Schicht ein grep-artiger Ausdruck (case-insensitiv), Wert = Trefferzahl im
  Abschnittstext. So wuerde man ohne Kev vorsortieren.
- Kennzahlen je Schicht (code/auswertung.py): k = Zahl der Hand-relevanten; Treffer@10 = erwartete Zahl Hand-relevanter unter den
  10 hoechstbewerteten der 25 (Gleichstaende zufaellig aufgeloest, exakt als Erwartungswert); Zufallserwartung 10*k/25;
  Spearman (Wert gegen 0/1-Label, mittlere Raenge) und AUC, jeweils fuer Kev und Stichwort.

## 9. Urteilsregeln (vor dem Hauptlauf festgelegt)

- **WK0** gilt, wenn alle 548 Abschnitte einen Kev-Eintrag ohne NaN haben und jeder Lauf innerhalb seiner Einheit (<= 600 s)
  endet; sonst nicht (Abdeckung wird in jedem Fall berichtet).
- **WK1** gilt, wenn fuer jede Schicht S0 bis S4 mit k >= 1 gilt: Kev-Treffer@10 >= min(6, k). (Woertlich "mindestens 6 der
  Top 10, soweit die Stichprobe welche enthaelt": bei k < 6 muessen alle k Relevanten in Kevs Top 10 liegen.) Schichten mit
  k = 0 zaehlen nicht.
- **WK2** gilt, wenn das Mittel der Kev-Treffer@10 ueber die Schichten S0 bis S4 mit k >= 1 echt groesser ist als das Mittel der
  Stichwort-Treffer@10 ueber dieselben Schichten. Gleichstand = nicht besser. Spearman/AUC und kausal werden berichtet, entscheiden
  aber nicht.
- Weil k fuer S1, S2, S4 nur 3, 2, 1 ist, ist jedes Urteil dort schwach; ERGEBNIS.md nennt das ausdruecklich und wertet zusaetzlich
  (nicht urteilsrelevant) die Ueberlappung der Kev- und Stichwort-Top-15 auf dem ganzen Bestand.

## 10. Ausgabe (lauf-69/auswertung.json, lauf-69/tabellen.md, ERGEBNIS.md)

- Top 15 je Schicht S0 bis S4 und fuer kausal: URL, Ueberschrift, Auszug, alle Kev-Werte, Stichworttreffer; Reihenfolge nach
  Kev-Wert, bei Gleichstand nach konkret.
- Leseliste 30 Seiten: Seitenwert = Mittel ueber S0 bis S4 des jeweils besten Abschnittswerts der Seite; Gleichstand nach
  konkret. (S0 ist auf dieser Seite fast ueberall hoch; die Rangfolge entsteht vor allem aus S1 bis S4.)
- Abdeckung: Abrufe, HTML-Seiten, Seiten mit Abschnitten, Abschnitte, bewertet, NaN, Rechenzeit, Laeufe.
- Verteilungen der Kev-Werte je Frage (Stauchung pruefen), Stichwort-Top-15 und Ueberlappung.

## 11. Einfrieren

Vor dem ersten Hauptlauf: Kopien `<datei>.eingefroren-<zeit>` von PLAN.md, code/kev_lauf.py, code/kev_bewerten.py,
code/fragen.json, code/stichworte.json, code/auswertung.py, code/aufbereiten.py, code/crawl.sh; sha256 dieser Kopien sowie von
daten/abschnitte.jsonl, daten/gegenprobe-ids.txt, gegenprobe-hand.json, seiten/INDEX.tsv in EINGEFROREN-SHA256.txt. Danach werden
diese Dateien nicht mehr geaendert; Fehler werden als Selbstanzeige berichtet, nicht still behoben.
