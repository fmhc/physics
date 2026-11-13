# Netz-, Feld- und Kontaktmodelle

Stand: 21. Oktober 2026; Nachträge vom 29. und 31. Oktober 2026; Abschnitt „Stand November 2026“ vom 13. November 2026.

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

- [Aktueller Stand und nächste Schritte](STAND-UND-NAECHSTE-SCHRITTE.md)
- [Historische Ergebnisse mit Methoden und Grenzen](RESULTS.md)
- [Ausgewählte Reproduktionspakete](REPRODUCIBILITY.md)
- [Beteiligte und KI-Unterstützung](BETEILIGTE.md)
- [Bewusste Ausschlüsse des öffentlichen Archivs](AUSSCHLUESSE.md)

Texte, Abbildungen und eigene Daten: [CC BY 4.0](LICENSE). Code: [Apache-2.0](LICENSE-CODE).
Hinweise zur Namensnennung stehen in [NOTICE](NOTICE). Ausnahme: Der Q-Ball-Preprint (Fassungen 0.51, 0.52 und 0.53) und sein Begleitarchiv
stehen für Text, Abbildungen, Daten und Zertifikate unter CC BY 4.0 und für Code unter der MIT-Lizenz.
