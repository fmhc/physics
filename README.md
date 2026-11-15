# Netz-, Feld- und Kontaktmodelle

Stand: 21. Oktober 2026; Nachträge vom 29. und 31. Oktober 2026; Abschnitt „Stand November 2026“ vom 13. November 2026, Nachtrag vom 15. November 2026.

Der folgende Einstieg beschreibt den Arbeitsstand vom 21. Oktober. Seit dem 31. Oktober liegt der Schwerpunkt auf dem
Ziel, aus Punktregeln eine lokale nichtabelsche Eichdynamik und daran Confinement mit thermischer Gegenprobe zu begründen;
den neueren Stand beschreibt der Abschnitt [„Stand November 2026“](#stand-november-2026).

Dieses Repository dokumentiert ein KI-gestütztes Forschungsvorhaben unter der Leitung von Finn Hinrichsen.
Ausgangspunkt ist ein räumliches Tetraedernetz mit Feldern. Aktuell untersuchen wir, wie sich diese
Netz- und Feldbeschreibung mit Kontaktmodellen in einer gemeinsamen Wirkung zusammenführen lässt.
A/B-Bereiche und Membran- beziehungsweise Kontaktgeometrien sind dabei Modellannahmen, deren Zusammenhang
weiter geklärt wird.

Im Mittelpunkt stehen positive Energiebilanzen, die Rückwirkung zwischen den beteiligten Bereichen
und die Bedingungen für gebundene, stabile Konfigurationen. Die Verbindung der Teilmodelle zu einem
gemeinsam geprüften Gesamtmodell bleibt eine offene Forschungsaufgabe.

Der räumliche Vergleich behandelt Fragestellungen in einer, zwei und drei Dimensionen. Raumdimension,
Feldkomponenten und innere Symmetrien werden getrennt ausgewiesen; Ergebnisse eines Modells gelten
nicht automatisch in einer anderen Dimension.

Mathematische Ableitungen, numerische Prüfungen und formale Nachweise werden separat dokumentiert.
Für die aktuellen Kontaktableitungen steht die formale Bestätigung durch Lean weiterhin aus.
Die bisherigen Modellrechnungen begründen keine experimentell bestätigte Theorie und keine Herleitung
von Elementarteilchen oder Atomen.

GitHub dient als kuratierte Übersicht mit ausgewählten reproduzierbaren Ergebnissen. Laufende Modelle,
Reviews und Notebooks werden im internen Forgejo geführt. Neue Ergebnisse erhalten vor einer öffentlichen
Übernahme eine gesonderte Prüfung und Freigabe. Bereits veröffentlichte Ergebnisdokumente bleiben
mit ihrem ursprünglichen Datum und Geltungsbereich erhalten.

**Nachtrag 29. Oktober 2026 (nach gesonderter Prüfung freigegeben).** Der Q-Ball-Preprint 0.51
(*Radiative cancellations and localized linear modes in three-dimensional sextic Q-balls*, Finn Hinrichsen; ein
Kontinuumsmodell, keine Rechnung auf dem Netz) ist als Release
[qball-bic-v0.51](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.51) mit Quellen in
[model-lab/papers/qball-bic-ladder-v0.51/](model-lab/papers/qball-bic-ladder-v0.51/README.md) veröffentlicht: drei
computergestützte Existenzeinschlüsse linearer Moden, alles Weitere numerisch oder bedingt, nicht begutachtet.
Noch am selben Tag erschien der Preprint 0.52 (Release
[qball-bic-v0.52](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.52), Quellen in
[model-lab/papers/qball-bic-ladder-v0.52/](model-lab/papers/qball-bic-ladder-v0.52/README.md)): neu sind eine Widmung,
ein allgemeinverständlicher Überblick und eine Übersichtsabbildung; Ergebnisse und Zahlen sind unverändert.
**Nachtrag 31. Oktober 2026:** Aktuelle Fassung ist der Preprint 0.53 (Release
[qball-bic-v0.53](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.53) mit Begleitarchiv Revision 3, Quellen in
[model-lab/papers/qball-bic-ladder-v0.53/](model-lab/papers/qball-bic-ladder-v0.53/README.md)): Leiter als ausdrückliche
Vermutung, Grenzen und offene Fragen, numerische Ladungssteigung dQ/dω, Matching-Rechnung für die Indizes 5 und 11–14;
kein Zertifikat oder Lemma geändert.
Seit dem 28. Oktober rechnen wir zuerst die reine SU(3)-Eichtheorie (nur Gluonen) auf dem Netz BCC-r\* × Z; Universalität
und Kontinuumsexistenz sind dabei Setzungen, Confinement ist offen. Erste Skalen- und Topologiebefunde, ihre Fehlschläge
und Grenzen stehen im [Stand vom 29.10.](STAND-UND-NAECHSTE-SCHRITTE.md) und in
[RESULTS](RESULTS.md#status-29-oct-2026), Abbildungen in [assets/stand-20261029/](assets/stand-20261029/README.md).

## Stand November 2026

<!-- Stand 13.11.2026. Jeder Satz mit Quelle im Kommentar davor. J: = coordination/research-journal/<id>.json,
     REG = coordination/runden-v3/RUNDE-52/IDEEN-REGISTER.md, GOAL = coordination/GOAL-CONFINEMENT-EMERGENZ-20261031.txt
     (Arbeitsprojekt, nicht öffentlich). Website-Stand 3.11.: Quellentabelle coordination/lagebericht/lagebericht-20261103-QUELLEN.md,
     Gegenlesung coordination/lagebericht/GEGENLESEN-20261103.md. Gegenlesung dieses Abschnitts:
     coordination/publication-review-20261112/CODEX-LESUNG-OEFFENTLICHE-TEXTE-20261112.md (T1). -->

<!-- GOAL Z. 8–10 (Ziel-Wortlaut); Codex T1-1 -->
Seit dem 31. Oktober 2026 leitet ein Ziel den größten Teil der Arbeit: Aus ausdrücklichen Regeln für die Punkte des
Netzes soll eine lokale nichtabelsche Eichdynamik begründet und daran Confinement mit thermischer Gegenprobe geprüft
werden; die Entstehung des Raums ist ein getrenntes Teilziel.
<!-- Website-Stand 3.11. (https://physics.fmhc.io/, Abschnitt "Research status") -->
Der ausführliche, nach Belegart gekennzeichnete Stand vom 3. November steht auf [physics.fmhc.io](https://physics.fmhc.io/).
Alles Folgende sind synthetische Modellrechnungen oder Papierargumente: keine Messdaten, nicht begutachtet, überwiegend
KI-erstellt. Jede Aussage gilt nur für die genannten Regeln, Größen und Zufallsfolgen.

- **Raum aus Punkten, wieder verfolgt.**
  <!-- GOAL Z. 125–127 (Pausenbeschluss 1.11.; im Website-Stand 3.11. dokumentiert, spätere Varianten); REG I-2046 (Auftrag Randverkleben, 7.11.); Codex T1-2 -->
  Die Frage, ob Regeln für Punkte einen ausgedehnten dreidimensionalen Raum bilden, wird nach der im Bericht vom 3. November dokumentierten Pause
  wieder verfolgt; am 7. November beauftragte die Projektleitung dazu eine Variante, die Ränder verklebt.
  <!-- J:raum-randverkleben-1-ausgang-bruch-ohne-inneres-20261108; REG I-2046; Codex T1-3 -->
  Eine Regel, die Kanten zwischen Teilen der Nachbarschaft eines Punktes schließt, ergab bei insgesamt 8000 Punkten in
  beiden untersuchten Varianten und drei Zufallsfolgen unter den jeweils 4000 älteren Punkten keinen mit kugelförmig
  geschlossener Nachbarschaft nach dem verwendeten kombinatorischen Kriterium.
  <!-- J:rk2-klein-1-ausgang-ohne-s2-20261108; REG I-2057 mit Zusatz; Codex T1-4 -->
  Eine zweite Schließregel, eine Stufe höher angesetzt, ergab bei insgesamt 2000 Punkten in drei Zufallsfolgen unter
  den jeweils 1000 älteren Punkten ebenfalls keine solche Nachbarschaft. Beides sind Befunde dieser Regeln und dieser
  Diagnose im endlichen Netz, kein Mechanismusnachweis und keine allgemeine Unmöglichkeit.
  <!-- J:raum-kantenteilung-1-kleinwelt-20261108; REG I-2095 mit Zusatz REG:15920; REG I-2097 mit Zusatz REG:15926; Codex T1-5 -->
  Eine Regel mit Kantenteilung und Kantenlöschung ergab zwischen 2000 und 32 000 Punkten in drei Zufallsfolgen nur
  schwaches Wachstum der Netzabstände, gemessen von 16 festen älteren Punkten aus: Das Wachstumsverhältnis lag nahe beim
  Bezugswert eines zufälligen Baums und unter dem eines Würfelgitters. Die Zuordnung „Kleinwelt“ ist eine operative
  Fensterklasse, deren Schnitte mit Kenntnis der Bezugswerte gesetzt wurden, kein Dimensionsnachweis. Mit der später
  geprüften Schranke wurde dieser Ausgang nicht vorab hergeleitet.
  <!-- REG I-2099 mit Zusätzen (REG:15930, REG:15935); REG I-2102; J:raum-ortsteilung-1-w-elter-uneinig-20261113;
       J:raum-ortsteilung-2-raumartig-selten-20261113; coordination/runden-v3/RUNDE-52/raum-randverkleben-1/ortsteilung-1/AUSGANG-RAUM-ORTSTEILUNG-1.md;
       .../ortsteilung-2/AUSGANG-RAUM-ORTSTEILUNG-2.md §2.3, §2.4, §3 und Berichtigung 1 (B4)  -->
  Eine weitere, vorab festgelegte Regel teilt eine Kante, die ein „Wanderer“ örtlich auswählt; danach geht der Wanderer
  zum anderen Elternpunkt. Diese Regel
  ergab in einer vorab gebundenen Schätzung über 64 Zufallsfolgen, zwischen 2000 und 32 000 Punkten und gemessen von
  16 festen älteren Punkten aus, nur in 4 Fällen die operative Tabellenklasse „raumartig“ (exaktes binomiales
  95-%-Intervall etwa 2–15 %); am häufigsten waren die Klassen „kleinweltartig“ (23) und „dicht-zwischen“ (21). Das
  sind operative Fensterklassen mit nach Sicht gesetzten Schnitten, kein Dimensionsnachweis; mit anderen Schnitten
  könnte die Zahl anders ausfallen, und das Intervall setzt gleichartige, unabhängige Zufallsfolgen voraus. Es gilt
  nur für diese Regel und diese Größen.
- **Vorbehalt zu kleinen exakten Rechnungen.**
  <!-- J:vorbehalt-torus-ed-20261104; J:berichtigung-verweise-torus-zeiten-20261104 (supersedes ed-ordnung-1, ed-v-scan-1);
       coordination/runden-v3/RUNDE-52/emergenz-confinement-1031/VORBEHALT-TORUS-ED-20261104.md; Codex T1-7 -->
  Auf der periodischen 2×3×2-Box mit 24 Punkten, auf der die auf physics.fmhc.io genannten exakten Rechnungen zum
  gewählten Trimermodell liefen, sind 720 der 792 Sechsermotive mit jeweils vier möglichen Zerlegungen in zwei Trimere
  nichtlokale Umlaufmotive, die im großen Gitter nicht vorkommen. Diese exakten Ergebnisse gelten deshalb für das gewählte
  Modell einschließlich dieser Motive auf genau dieser Box; eine entsprechende Aussage für das lokale Modell im großen
  Volumen folgt daraus nicht.
- **Weiter offen.**
  <!-- Website-Stand 3.11., Liste "Open, stated honestly"; J:opus-pruefung-vier-saeulen-agy-20261102; Codex T1-8 -->
  SU(3) ist auf dem Gitter von Hand gesetzt. Aus den Regeln für die Punkte ist bisher weder SU(3) noch Spin ½,
  Confinement oder Licht hergeleitet; das ist ein fehlender Nachweis, keine Widerlegung.
  <!-- Website-Stand 3.11., Punkt "Lattice checks, status 30 October (unchanged)"; J:vorab-skala-m12-1-gebunden-20261106 (nur Plan); Codex T1-9 -->
  Die auf der Webseite gesondert aufgeführten Gitterprüfungen der reinen SU(3)-Eichtheorie auf BCC-r\* × Z behalten ihren
  Stand vom 30. Oktober; der dort berichtete Krafttest und der Abschluss der Glueball-Serie sind davon getrennt.

### Nachtrag 15. November 2026

<!-- Stand 15.11.2026. J: = coordination/research-journal/<id>.json (bei Berichtigungen gilt nur die neueste Fassung),
     REG = coordination/runden-v3/RUNDE-52/IDEEN-REGISTER.md, Einträge und Zusätze I-2104 bis I-2113 (Z. 15942–15978).
     Gegenlesung: coordination/publication-review-20261115/. Eine Übersicht als Grafik steht auf https://physics.fmhc.io/. -->
Alles Folgende sind synthetische Modellrechnungen oder Papierargumente: keine Messdaten, nicht begutachtet, überwiegend
KI-erstellt. „Papier“ heißt Papierbefund oder Hypothese ohne Rechnung, keine Messung. Jede Aussage gilt nur für das
gewählte Modell und die genannten Größen und Annahmen.

- **Farbe: Woher könnte SU(3) kommen?**
  <!-- Rahmen: J:uhr-schliesst-so3-ungeklaert-b2-20261113 (meaning); J:dichte-so3-1-ungeklaert-b1-20261113 (question) -->
  Damit SU(3) aus dem Netz entsteht, statt gesetzt zu werden, müsste die eigene Dynamik des Modells ein Dreierniveau so
  von Ort zu Ort tragen, dass SU(3) entsteht. Die folgenden Punkte prüfen einzelne Glieder dieser Kette im gewählten
  Quanten-Trimermodell; keiner weist einen solchen Transport nach.
  <!-- J:perron-komponenten-h-2-ausgang-b1-20261113 (result, meaning); REG I-2106 Zusätze REG:15962, REG:15966 -->
  - *Tiefste Komponenten eines reduzierten Operators in einer gepinnten Röhre (gerechnet, synthetisch).* Auf einem röhrenförmigen Stück des
    raumzentrierten Gitters (Länge 6, Querschnitt 2×2; eine Röhre, kein Gitter) mit festgehaltenen Löchern wurde für einen
    reduzierten Operator vierter Ordnung geprüft, ob das tiefste Niveau je Lochanordnung in einer oder in mehreren gleich
    tiefen Komponenten liegt. Von sieben nichtleeren Anordnungen ergaben drei eine, vier zwei innerhalb der Toleranz; die
    Zweifachheit ist durch die räumliche Symmetrie erklärt, die die Löcher festhält. Das gilt für g ≠ 0. Es ist keine
    vollständige Zerlegung in Symmetrietypen; das volle Pinmodell hat bei endlicher Größe genau einen tiefsten Zustand,
    und aus der Zahl folgt keine Eignung oder Nichteignung als Transportkanal. Ob ein zweiter Rechner dieselben Klassen
    liefert, ist ungeprüft. Codex: „TRÄGT MIT VERMERKEN: … tragen den begrenzten Ausgang FAST-ENTARTET-STAB“.
  <!-- J:uhr-schliesst-so3-ungeklaert-b2-20261113 (result, meaning); REG I-2107 Zusätze REG:15958, REG:15963;
       Zeitschritte: REG I-2112 Zusatz REG:15971 -->
  - *Kann ein Zusatzelement SU(3) vervollständigen? (Papier).* Die Gruppentheorie trägt: so(3) ist maximal in su(3), und
    ein geeignetes komplexes Zusatzelement, etwa eine dreiwertige Uhrphase, erzeugte zusammen mit einer dichten SO(3) die
    SU(3). Im Modell selbst ist kein solches Element nachgewiesen und keines endgültig ausgeschlossen; eine dichte SO(3)
    gibt es im Bestand nicht. Ein Negativbefund gilt nur eingeschränkt: Reelle statische oder geometrische Transporte auf
    einer reell geschlossenen, rangstabilen Dreierfaser und reelle Pfadsummen bei festem reellem E bleiben in O(3). Eine
    Phase aus der Zeitentwicklung bleibt algebraisch geeignet und bedingt offen; nach Entscheidung der Projektleitung vom
    13. November zählen Zeitschritte nicht zu den räumlichen Transporten, sondern bilden einen eigenen späteren Zweig.
    Ausgang ungeklärt. Codex: „UNGEKLÄRT statt SCHLIESST-NICHT gedeckt, weil die tragende Gruppentheorie die offenen
    Transport-, Erhaltungs- und Dynamikvoraussetzungen des nativen Modells nicht ersetzt.“
  <!-- J:dichte-so3-1-ungeklaert-b1-20261113 (result, meaning); REG I-2110 Zusatz REG:15969 -->
  - *Gibt es eine dichte SO(3)? (Papier).* Im Bestand entscheidet keine ablesbare Zahl. Der zuvor untersuchte
    Oktaeder-Triplett-Transport hat in zweiter Ordnung in λ Rang eins. Unter Symmetrievoraussetzungen gibt ein bedingter
    Ansatz (Überlappungstransport eines isolierten Dreierniveaus längs einer Achse und einer Raumdiagonale, Schleifen über
    kleine Dreiecke) genau dann eine dichte Gruppe, wenn ein einziges Vorzeichen der Raumdiagonal-Bindung negativ ist.
    Das Vorzeichenkriterium betrifft die determinantenkorrigierte Schleifengruppe aus den Drehanteilen der
    Überlappungsmatrizen. Offen bleiben das Dreierniveau, der volle Rang, das Vorzeichen und die physische Rechtfertigung
    dieser Ersetzung; der Prüfplan ist nur ein Entwurf. Erst nach dem Nachweis von Dreierniveau, Rang 3 und weiteren
    Strukturvoraussetzungen (Zustandsraum, Transportdefinition, Parität, Kovarianz, Spektralzweig, zertifizierte Fehler)
    hinge die Dichte an diesem Vorzeichen. Auch eine dichte SO(3) wäre
    noch keine SU(3)-Struktur, weil ein Zusatzelement nötig bleibt. Codex: „… trägt nach BERICHTIGUNG 1 mit Vermerken als
    bedingte Papierargumentation mit Modell-Ausgang UNGEKLÄRT“.
  <!-- J:okt-wegsummen-rang-1-kandidat-b1-20261115 (result, meaning); REG I-2111 Zusatz REG:15976 -->
  - *Rang 1 oder Rang 3 zwischen zwei Oktaedern? (Papier).* Für die ausgewählte Bindung G1–G3 der betrachteten
    Oktaederanordnung hat der Dreiertransport im gepinnten Sektor mit genau einer Anregung bis zur zweiten Ordnung in λ
    (der Kopplung) Rang eins. In vierter Ordnung öffnen Wege über die Kontaktdreiecke zwei weitere, schwache Richtungen.
    In führender Ordnung ist das Verhältnis des kleinsten zum größten Singulärwert (53/2880) λ² im einen und
    (7/2880) λ² im anderen Schema. Keine Symmetrie erzwingt Rang eins. Das ist ein formaler Rang-3-Befund eines
    Bindungstransporters für kleine λ ≠ 0, sehr anisotrop; kein Rangzertifikat und keine vom Rechenschema unabhängige
    Dreierfaser. Das Dreierniveau je Platz ist schon in zweiter Ordnung stärker aufgespalten als jedes Hüpfen. Bei λ = 1 ist
    der Störungsbefund nicht kontrolliert: Schon am offenen Paar gleichartiger Oktaeder hat der Resolvent bei
    festgehaltener ungestörter Energie einen Pol bei λ ≈ 0,861. Das ist keine nachgewiesene Singularität des
    physikalischen Spektrums; zudem hängt der Rang des Bindungsblocks vom Schema ab.
    Codex: „RANG-3-KANDIDAT bleibt der richtige Abschluss …“.
  <!-- J:t-niveau-oh-1-t6-nicht-durchfuehrbar-20261113; REG I-2108 Zusätze REG:15973, REG:15974 -->
  - *Niveaus eines symmetrisch gepinnten Blocks.* Eine exakte Rechnung auf einem periodischen Würfel der Kantenlänge 6
    erwies sich vor dem Bau als nicht durchführbar. Die Arbeit an einem offenen Block mit voller Oktaedersymmetrie um einen
    Punkt läuft; ein Ergebnis gibt es nicht.
- **Raum.**
  <!-- J:dimensionsmass-e2-strangende-b1-20261113 (result, meaning); REG I-2109 Zusätze REG:15960, REG:15964 -->
  Eine Messvorschrift für die Dimension des wachsenden Netzes (Rückkehr einer Irrfahrt, Kugelwachstum als Kontrolle) trug
  zweimal in der Gegenlesung nicht; nach der Abbruchregel ist dieser Strang beendet, gerechnet wurde nichts. Im
  Suchumfang ist damit kein skalarer Dimensionsschätzer gebunden. Die für die Raumregeln genannten Klassen sind operativ
  und kein Dimensionsnachweis: Das zugrunde liegende Wachstumsverhältnis ist nur eine bedingte Potenzschätzung und gibt
  einem Würfelgitter nur etwa 2,5–2,6.
  <!-- J:kantentransfer-strang-beendet-20261113; J:kantentransfer-e3-endgueltig-abgebrochen-20261113;
       REG I-2104 Zusätze REG:15965, REG:15972 -->
  Eine weitere Wachstumsregel, bei der Kanten zwischen Punkten übertragen werden, wurde auf Papier ausgearbeitet und mit
  einem Messplan versehen. Der Messplan trug in der Gegenlesung nicht; nach der Abbruchregel ist der Strang beendet und
  ruht nach Entscheidung der Projektleitung. Gemessen wurde nichts; die Abstandsklasse dieser Regel ist ungemessen.
- **Röhre (Papier).**
  <!-- J:randableitung-roehre-ungeklaert-b1-20261115 (result, meaning); REG I-2113 mit Zusatz REG:15975, REG:15978 -->
  Auf röhrenförmigen Gitterstücken mit offenem Seitenrand enthält die Dynamik vierter Ordnung des gewählten Trimermodells
  ein Potential für einzelne Trimere, das zählt, wie viele andere Dreiecke mit dem besetzten Trimer eine Kante teilen;
  dieser Randterm gilt im gewählten Modell vierter Ordnung nur für einen von null verschiedenen Strafparameter κ (bei
  κ = 0 verschwindet er), für Röhrenlängen ab 4 und für windungserhaltende Züge. Auf der Röhre der Länge 6 mit
  Querschnitt 3×1 ist er im Sektor nicht konstant. Für die von der Herleitung gedeckten
  Röhrengeometrien und Längen mit nichtleeren, durch die Dynamik erhaltenen Windungssektoren und translationsinvariantem
  Operator ist der Sektorenergieabstand null, wenn 3 das Querschnittsprodukt nicht teilt (etwa Länge 6, Querschnitt 2×2); dazu muss 3 die Länge teilen.
  Eine Änderung des Koeffizienten des Randpotentials erhält diese Gleichheit. Bei Querschnitt 3×1 bleibt die Wirkung auf
  den nichttrivialen Sektorabstand offen. Codex: „Für die D-6-Frage nach
  der tatsächlichen Wirkung der Randdiagonale auf den nichttrivialen Sektorenergieabstand ist nach dieser Lesung
  UNGEKLÄRT richtig; RAND-NEUTRAL gilt bedingt für die translationsverbundenen Sektoren, während RAND-WIRKT für ΔE durch
  die vorgelegten Papierzeugen nicht folgt.“ Eine Spektralrechnung auf 3×1-Röhren ist geplant, aber nicht durchgeführt;
  sie entschiede nur für diesen Querschnitt.
- **Verfahren.**
  <!-- REG I-2104 Zusatz REG:15972 (Entscheidung 13.11.); J:kantentransfer-strang-beendet-20261113 (meaning) -->
  Seit dem 13. November gilt nach Entscheidung der Projektleitung: Ein Strang endet, sobald er irgendwo im Strang zum
  zweiten Mal das Urteil „trägt nicht“ erhält. Eine kurz zuvor angewandte Zählung je Stufe wurde als Lockerung der Regel
  verworfen. Für die reine SU(3)-Gittertheorie gibt es keine neuen gerechneten Ergebnisse.

- [Aktueller Stand und nächste Schritte](STAND-UND-NAECHSTE-SCHRITTE.md)
- [Historische Ergebnisse mit Methoden und Grenzen](RESULTS.md)
- [Ausgewählte Reproduktionspakete](REPRODUCIBILITY.md)
- [Beteiligte und KI-Unterstützung](BETEILIGTE.md)
- [Bewusste Ausschlüsse des öffentlichen Archivs](AUSSCHLUESSE.md)

Texte, Abbildungen und eigene Daten: [CC BY 4.0](LICENSE). Code: [Apache-2.0](LICENSE-CODE).
Hinweise zur Namensnennung stehen in [NOTICE](NOTICE). Ausnahme: Der Q-Ball-Preprint (Fassungen 0.51, 0.52 und 0.53) und sein Begleitarchiv
stehen für Text, Abbildungen, Daten und Zertifikate unter CC BY 4.0 und für Code unter der MIT-Lizenz.
