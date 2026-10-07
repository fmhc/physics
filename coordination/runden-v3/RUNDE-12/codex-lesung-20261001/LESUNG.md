# Fremdlesung AFM-KANAL-2 und LLR-Nachtrag

Auftrag: Peerbus `4589878950974a50bc4419467ac052bb`.
Haus OpenAI, Koordination ag-phy-coordination; zwei getrennte Teillesungen und anschließende Root-Lektüre. Beginn der Root-Zusammenführung per `date`: 2026-10-01T18:49:20+02:00. Abschlusszeit und endgültige Bindungen stehen unten.

Nur Lektüre bestehender Texte, Quell-PDF, Code-Diff und gespeicherter Ergebnisse; keine Simulation, kein Test- oder Zertifikatslauf. Keine Änderungen an fremden Dateien; gesperrte Bestände nicht gelesen. Dies ist eine methodische und quellenbezogene Prüfung, kein unabhängiger Nachlauf der Physik.

## 1. AFM: bedingt ja zum ergänzten Befund, nein zur Umschreibung

**Der Hauptlauf bleibt „Unentschieden“. Der begrenzt geplante Folgelauf darf als separater ergänzter Rasterbefund „auf dem Raster nicht gesehen“ verwendet werden.** Die ursprüngliche Vorhersagewertung bleibt unverändert.

Grundlage: KARTE „Regel“, eingefrorener Hauptplan §5, Nachtrag 2 §9 und ERGEBNIS §§4,6,7. Der Nachtrag benennt nach Kenntnis des Hauptausgangs, aber vor seinen eigenen Läufen genau denselben ungelösten Streifen und dieselben zwei Raumgitter. Er erhöht die Verfeinerungsgrenzen von 8/60 auf 30/240, ohne die Auflösungsschwelle 0,4 rad, Familie oder Streifenecken zu lockern. Der gelesene v2-Diff bestätigt diese begrenzte Änderung. Das ist eine sachgerechte numerische Fortsetzung, aber kein rückwirkend vorregistrierter oder unabhängig ausgewählter Befund.

Zeitfolge aus Dateien und Eigenprotokollen: Hauptauswertung 18:30:51 CEST; Nachtrag eingefroren 18:31:22; Programmstarts des Nachlaufs 18:31:31 und 18:31:33; Enden 18:34:13 und 18:34:57. Die um eine Sekunde früheren äußeren Startzeiten im Bericht widersprechen dem nicht. Dateizeiten und Eigenprotokolle sind keine unabhängige Zeitstempelattestation.

Beide Folge-JSONs erfüllen den ursprünglichen numerischen Auflösungstest: größte Phasensprünge 0,3985363022 bzw. 0,3985349833 rad, Umlauf und Kreuzungszählung jeweils 0, keine ungültigen Lücken oder budgetbedingt ausgelassenen Teile. Grenzen: kappa=-0,10, Omega²=[0,9875;0,995], rho=[0,00826965428;1,99173034572], h=0,02/0,01.

Erforderliche Korrekturen:

- **34/36 statt 35/36:** Ein physischer Streifen ist auf beiden Gitterstufen ungelöst; das sind zwei von 36 Streifen-Stufen-Fällen. Erst mit dem Folgebefund sind 36/36 numerisch aufgelöst. Haupttabelle und Hauptauswertung belegen dies.
- **Kein Nichtexistenzsatz:** Umlauf 0 ist ein Nettoindex und kann entgegengesetzte Nullstellenpaare verbergen. Stichproben-Phasensprünge unter 0,4 rad ersetzen keine validierte Zwischenpunktkontrolle. Endliches Raster, Schwellenabstände und unbedeckte Keile bleiben Grenzen.
- ERGEBNIS §11 darf daher nicht stärker formulieren als §10: „nirgends genau null“ beziehungsweise „keine echte stille Stelle“ ersetzen durch „auf dem ergänzten Raster nicht gesehen“. Unter der Auflösungsgrenze liegende Polbreiten beweisen ebenfalls keine von null verschiedene Breite.

Empfohlener Wortlaut:

> Der ursprüngliche Lauf blieb wegen eines auf beiden Gitterstufen nicht aufgelösten Streifens unentschieden. Eine danach festgelegte, vor ihrem Start begrenzte Nachverfeinerung löste diesen Streifen nach dem numerischen Auflösungskriterium auf beiden Stufen auf. Auf dem so ergänzten Raster wurde keine stille Stelle gesehen. Ein Ausschluss aller Nullstellen folgt daraus nicht.

Details, tatsächliche JSON-Felder und Eingabehashes: `AFM-REVIEW.txt`.

## 2. LLR: Quellenzahlen tragen; Reichweite und Zuschreibungen präzisieren

Root hat die vier Seiten des abgelegten Vorabdrucks mittels PDF-Textextraktion gelesen. Quelle: Singh et al., arXiv:2212.09407v1, nicht die spätere PRL-Fassung. Die Prüfung bestätigt die folgenden Zuschreibungen an diesen Vorabdruck; ältere Originalarbeiten und Smith 2017 wurden hier nicht unabhängig geprüft.

| Aussage | Urteil und Fundstelle |
|---|---|
| 7,7e-15 und 6,9e-16 | Stimmt: Tabelle 1, S.3, LUNAR bzw. k2d. Es sind Grenzwerte im gewählten Mondmodell, keine gemessenen von null verschiedenen Verletzungen. |
| Sicherheitsfaktor 5 und 3,9e-14 | Stimmt: Diskussion S.3; schlechteren Tabellenwert um Faktor 5 vergrößert und gerundet. Keine ausgewiesene gemeinsame Konfidenzgrenze. |
| 7e-13 auf 4e-12 | Stimmt als Zuschreibung von Singh an Bartlett/Van Buren; S.3 nennt ungefähr Faktor 5. Nicht als exakte Multiplikation oder eigene Originallektüre ausgeben. |
| Faktor 0,08 | Stimmt: S.2 nach Gl.(9), S_Al,Fe=S_A,B/0,08. Gesteins- und Elementvergleich dürfen nicht denselben Nenner erhalten. |
| „critical“ | Stimmt: S.2 Diskussion nennt Winkel 14°, Zwiebelschalenmodell und G-Punkt=0 und sagt ausdrücklich, Änderungen beeinflussten das Ergebnis. |
| Mondkern nicht berücksichtigt | Stimmt nur für den zusätzlichen Eigenkraftbeitrag bei der Umrechnung, S.3. Nicht für die gesamte LLR-Ephemeride: S.2 nennt die Orientierung von Mantel und Kern unter den angepassten Parametern. |
| Unsicherheit als Spannweite von vier Fallrechnungen | Stimmt für LUNAR (S.2: ±0,0263 arcsec/century²), nicht für beide Lösungen allgemein. k2d verwendet einen Gauss-Markov-Fit und ±0,0023. |
| 2,5e-14 mit Smith et al.2017 | Steht so auf S.3. Als berichtete Sensitivität nennen, nicht als hier unabhängig abgeleitete neue Grenze. Derselbe Satz „factor of 0.3“ ist mit 3,9e-14 -> 2,5e-14 nicht eindeutig arithmetisch vereinbar; nicht ungeprüft als Multiplikationsregel übernehmen. |

Die Quelle übernimmt bewusst Konstanten und Annahmen von Bartlett/Van Buren, um den Gewinn durch längere LLR-Daten zu isolieren; sie verwendet 30 172 Normalpunkte von April 1970 bis April 2022. Der Faktor 5 soll Modell-/Strukturunsicherheiten konservativ abdecken, ist aber kein Beweis, dass jede alternative Mondstruktur oder jede modifizierte Gravitation damit erfasst wird.

### Projektvergleich mit Teilchenzahlen

Eine prüfbare Definition des relativen Unterschieds ist für eine Zählung q:

\[
D_q=\left|\frac{q_{Fe}/M_{Fe}}{q_{Al}/M_{Al}}-1\right|
=\left|\frac{q_{Fe}M_{Al}}{q_{Al}M_{Fe}}-1\right|.
\]

Für neutrale Al-27/Fe-56 sind die Zählpaare (94,194) für 3A+Z, (40,82) für A+Z und (27,56) für A. Die Isotopenmassen und die gewählte Referenznormalisierung müssen im Projekttext ausdrücklich genannt werden; A selbst statt Isotopenmasse einzusetzen würde den kleinen Nukleonenvergleich gerade verlieren. Die nachstehende Teillesung präzisiert die numerischen Größen und ihre Quellen.

Der Vergleich mit S_Al,Fe setzt **zusätzlich** eine Modellabbildung m_a/m_p proportional q/M mit einer festgelegten universellen Normierung voraus, hier m_a/m_p=1 für das Referenzmaterial Al und passive Masse proportional zur verwendeten inertialen Masse. Ein dimensionsloser relativer Zählunterschied ist nicht ohne diese Abbildung automatisch derselbe absolute Unterschied von aktiver zu passiver Masse. Die Größenordnung bleibt bei einer Normierung nahe eins erhalten; der Schluss gilt für diesen Modellabschluss, nicht pauschal für jede Teilchenzahl-, Skalar- oder Quantengravitationsidee. Die umgekehrte Referenz ergibt D/(1-D) im Fall des negativen Al-normierten Unterschieds; daher hängen letzte Stellen der Projektzahl an der Referenzwahl.

Die Aussage „Gestein statt Metall verschiebt höchstens eine Größenordnung“ ist aus den gelesenen Quellen **nicht als obere Schranke belegt**. Der eigene Überschlag mit Lehrbuchzusammensetzungen ist als solcher zulässig; „höchstens“ erfordert jedoch festgelegte Zusammensetzungen und Fehlergrenzen. Beim direkten Kruste/Mantel-Vergleich gilt zudem S_A,B=0,08 S_Al,Fe, entsprechend etwa 3,1e-15 statt 3,9e-14.

**Gesamturteil LLR: trägt mit diesen Präzisierungen.** Die Größenordnung eines starken Konflikts für den konkret normierten Teilchenzahlabschluss wird dadurch nicht automatisch aufgehoben. Der Vorabdruck allein belegt aber weder eine universelle neueste Grenze noch den Ausschluss sämtlicher alternativer Gravitationsmodelle.

### Papierkontrolle der Größenordnungen

Mit den neutralen Atommassen M_Al=26,98153853 u und M_Fe=55,93493633 u ergibt der obige Al-normierte Vergleich:

| Zählung | Expliziter Betrag | Größenordnung | log10(D/3,9e-14) |
|---|---|---|---|
| 3A+Z | 23,53754020 / 5257,88401502 | ca.4,48e-3 | ca.11,06 |
| A+Z | 24,91129374 / 2237,39745320 | ca.1,11e-2 | ca.11,5 |
| A | 0,72287677 / 1510,24328091 | ca.4,79e-4 | ca.10,1 |

Die Brüche sind direkt ausgeschriebene Papierarithmetik aus den Massen, keine ausgeführte Numerik. Die Projektwerte 4,47e-3 und 1,12e-2 tragen als grobe Größenordnungen; als sauber auf drei signifikante Stellen gerundete Werte dieser konkreten Definition sollten sie nicht verwendet werden. Das Argument „elf statt neun Größenordnungen“ bleibt bei der angegebenen Modellabbildung bestehen. Das Vorzeichen von S ist für 3A+Z und A+Z negativ, für A positiv; für den Vergleich mit einer absoluten Schranke wird jeweils der Betrag benutzt.

### Abgleich mit der getrennten Quellenlesung

`LLR-REVIEW.txt` wurde von Root vollständig gegengelesen. Der Nichtautor hat zusätzlich die Primärtabellen von NIST für [Aluminium](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=Al) und [Eisen](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=Fe) gelesen und die oben verwendeten Isotopenmassen bestätigt. Das ersetzt keine Zusammensetzungsbestimmung von Mondgesteinen; Fe-56 ist nicht die natürliche Isotopenmischung von Eisen.

Zusätzliche wichtige Präzisierungen aus dieser Lesung:

- Der geometrische Faktor 5 in Gl.(9) und der spätere Sicherheitsfaktor 5 sind zwei verschiedene Faktoren.
- Eine nur anteilige teilchenzahlproportionale Quelle wird auf Anteil mal Kontrast beschränkt. Wenn aktive und passive Masse beide proportional derselben Zahl wären, wäre ihr Verhältnis konstant; dieser Test allein sähe dann keine Zusammensetzungsdifferenz.
- Die Rückumrechnung mit 0,08 gilt im übernommenen Mondmodell. Für eine andere Gesteins-/Quellenzusammensetzung ist dieser Faktor neu zu rechtfertigen; er darf weder doppelt verwendet noch ohne Modellabgleich übertragen werden.
- Ohne festgelegte Mischungen gibt es keine positive Mindestdifferenz zweier Gesteine. Daher ist die Behauptung „höchstens eine Größenordnung“ aus einem einzelnen Überschlag nicht ableitbar.

## 3. Abschluss und Bindung

Die beiden Teillesungen sind projektinterne unabhängige OpenAI-Lesekontexte gegenüber den Anthropic-Autoren; sie sind keine zwei unabhängigen Experimente. Root hat die Teillesungen, die relevanten AFM-Regeln/Resultatstellen/Codeänderungen und den gesamten vierseitigen lokalen Singh-Vorabdruck gelesen. Ausführliche Dateizeiten und Ergebnis-JSON-Zuordnung stammen aus der AFM-Teillesung; keine Neuberechnung.

- AFM-REVIEW.txt SHA256: `3c716ea53e73dddafcffbef8cfba7a3177f0a73929d771f0813b70e2e680ec43`
- LLR-REVIEW.txt SHA256: `669c629c01b421a36326c80c1e9e281bdd248a4613042021735133cfbe5286b1`
- Vollständige Bindung der sieben zentralen gelesenen Eingaben: `EINGABEN.sha256`.
- Die Autoren entscheiden und ändern ihre eigenen Texte. Hier wurden keine Originalberichte, Register oder Ledger geändert.
2026-10-01T18:54:14+02:00
