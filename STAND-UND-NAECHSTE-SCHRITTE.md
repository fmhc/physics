# Stand und naechste Schritte (08.10.2026)

Synthetische Modellrechnungen und Hypothesen, nicht begutachtet. Kennzeichen: [E] gerechnet, [M] Mathematik, [L]
Literatur, [H] Hypothese.

## Vorrang nach den beiden Reviews vom 08.10.2026

Die folgende Reihenfolge ersetzt die fruehere Prioritaetenliste am Ende dieser Seite:

1. **Reproduzierbarkeit:** ein kleines Paket fuer den Maxwell-Gewichtsbefund auf V, mit festen Eingaben,
   Umgebung, einem Aufruf, erwarteten Zahlen und Fehlerkriterien. Einstieg: [REPRODUCIBILITY.md](REPRODUCIBILITY.md).
2. **Maxwell-Grundlagen:** Eichidentitaet, Positivitaet der quadratischen Form und Reflexionspositivitaet getrennt
   untersuchen. Die Gewichte einfrieren; neue Richtungen und kleine Impulse pruefen, keine Nachoptimierung am Test.
3. **Konvergenz:** Gitterabstand bei fester physikalischer Box und Boxgroesse bei festem Gitterabstand getrennt
   variieren; beobachtbare Groesse, Skalenabgleich, Auswertefenster und Abbruchkriterien vorab festlegen.
4. **Unterscheidbare Vorhersage:** erst nach diesen Kontrollen Anisotropie oder Dispersion zwischen V und
   Vergleichsgittern testen. Eine Diskretisierungsabweichung ist noch kein messbares Naturgesetz.
5. **Externe Reproduktion:** ein eng begrenztes Teilergebnis zur unabhaengigen menschlichen Begutachtung vorbereiten.
   SU(2)-Flow ist ein Kandidat, braucht aber vorher die Kontrolle der Skalenwahl und des abweichenden zweiten
   Referenzwerts. Es wurde noch niemand mit einer Begutachtung beauftragt.

SU(3), chirale Materie und weitere Higgsportal-Tests bleiben Forschungsfragen, erhalten durch zusaetzliche
Nachkommastellen aber keinen Vorrang vor diesen Grundlagen. Die Prozentwerte werden durch diese organisatorischen
Aenderungen nicht erhoeht. [Review-Antwort](coordination/review-response-20261008/RESPONSE.md),
[Aussagen und Pruefkriterien](CLAIMS.md).

## Neue Higgs-Auswertung (08.10.2026)

[HIGGS-RESPONSE-1](coordination/higgs-response-20261008/ERGEBNIS.md) prüft Näherungen an allen 24 gespeicherten B13-Profilen. Eine räumliche Korrektur zweiter Ordnung besteht das vorab definierte Pilotkriterium in allen acht Parametergruppen. Es handelt sich um eine neue Auswertung bei festgehaltenen Singuletts, keine neue Relaxation und keine Herleitung des Higgsmechanismus. Nächste Frage: konsistente reduzierte Energie und Kräfte, danach selbstkonsistente Profile; parallel bleibt die vollständige Modenprüfung wichtig.

Nachtrag 08.10.2026: Die Folgetests sind gerechnet, alle am selben radialen 3D-Portalmodell und, ab HIGGS-MINIMA-1, an einem
einzigen Parameterpunkt: [Kraefte](coordination/higgs-force-20261008/ERGEBNIS.md),
[selbstkonsistente Profile](coordination/higgs-minima-20261008/ERGEBNIS.md),
[Energiekruemmungen der vollen Theorie](coordination/higgs-modes-20261008/ERGEBNIS.md) und
[radiale Kruemmungen der reduzierten Modelle](coordination/higgs-reduced-modes-20261008/ERGEBNIS.md). Offen bleiben
direkte nichtlineare Zeitentwicklung, weitere Parameter und die Uebertragung auf V. Winkelantwort und lineare
Frequenzen wurden inzwischen geprueft: [Winkelmoden](coordination/higgs-angular-modes-20261008/ERGEBNIS.md),
[lineare Dynamik](coordination/higgs-dynamics-20261008/ERGEBNIS.md). Das ersetzt weder nichtlineare Stabilitaet noch
Konvergenz zur Kontinuumstheorie.

## Neuer Literatur- und Modellvergleich

Der [Volltextvergleich vom 07.10.2026](coordination/runden-v3/RUNDE-51/modell-screening-1/VOLLTEXT-VERGLEICH-20261007.md) prüft sechs arXiv-Arbeiten und zwei ältere Kontrollen. Der [revidierte Modellfahrplan](coordination/runden-v3/RUNDE-51/modell-screening-1/MODELLFAHRPLAN.md) enthält sieben konkrete Prüfkarten. Schwerpunkt: Hadronmodelle, chirale Materie, Higgs und belastbare Auswertung. Dies ist Quellenlektüre [S] und Modellplanung [H], keine neue Simulation. Die Prozentwerte bleiben unverändert.

## Neu seit der ersten Fassung

- **Starke Kraft (QUANT-3, S5):** Mit Wilson-Flow-Skalen stimmt das dimensionslose Verhaeltnis w0/Wurzel(t0) auf dem
  Netz (1,032) mit dem Hyperkubus (1,034) auf 0,2 +- 0,7 % ueberein [E].
  - T_c*Wurzel(t0) weicht um -2,7 % ab, haengt aber stark an der Lage des Uebergangs auf dem Netz.
  - Die Fadenspannung (S4) blieb unentschieden.
  - Zweiter Gitterabstand (S6): T_c*Wurzel(t0) +0,9 +- 2,2 %, w0/Wurzel(t0) -2,2 +- 0,9 %; empfindlich auf beta_c(Netz) +- 0,03 und das Volumen ([ERGEBNIS-S6](coordination/runden-v3/RUNDE-37/quant-3/ERGEBNIS-S6.md)).
  - Ordner: coordination/runden-v3/RUNDE-37/quant-3/.
- **Netzdynamik (VOLUMEN-G2-1):** Ohne Bedingung bricht die Umklapp-Dynamik in allen vier Testnetzen ab. Haelt man
  das Gesamt-4-Volumen fest (unimodulare Bedingung), laufen drei von vier Netzen zehn Schwingungen stabil [E].
  - Die Zwangskraft ist so gross wie die Netzkraefte.
  - Ein Netz zeigt weiter grosse Spruenge.
  - Die Rechnung ist noch nicht voll nichtlinear.
- **Schwerkraft:** Die Periheldrehung folgt aus den gerechneten Netzwerten fuer Lichtablenkung und beta. Der Faktor
  gegenueber der ART liegt bei 0,993 bis 1,000 [E, PPN-Arithmetik]. Ordner: antigravity-nachbau-1/.
- **Dimensionsmessung (DS-EICHUNG-2D-1):** Das Werkzeug ist korrekt, konvergiert aber langsam.
  - Auf Zufallsflaechen mit bekannter Hausdorff-Dimension 4 zeigt es bei bis zu 10^5 Bausteinen nur 3,4 bis 3,8 an [E].
  - Grosse 4D-Laeufe brauchen deshalb mehrere Groessen und eine Vergleichsflaeche.
- **Gepruefte KI-Entwuerfe (ANTIGRAVITY-NACHBAU-1):** Behauptete Durchbrueche zu Generationen, Dirac-Gleichung und
  Kollaps trugen beim ehrlichen Nachrechnen nicht.
  - Ein echter Kern: Die Volumenbedingung beim Umklappen (siehe oben).


## Schaetzwerte (subjektiv) und Aenderungen gegenueber der Fassung vom 07.10. mittags

Die Prozentwerte sind eine subjektive, grobe Entwicklungsschaetzung bis zu einem vollstaendigen physikalischen
Mechanismus. Sie sind keine Wahrscheinlichkeit, kein Messwert und kein bestaetigter Anteil, und sie werden nicht
gemittelt. Die Befunde in den verlinkten Ergebnissen haben Vorrang.

| Bereich | alt | neu | Grund |
|---|---|---|---|
| Netz und Raum | 65 % | 65 % | unveraendert |
| Schwerkraft | 55 % | 55 % | unveraendert |
| Licht | 55 % | 55 % | unveraendert |
| Materiefeld (Q-Baelle) | 30 % | 30 % | unveraendert, wieder als eigene Zeile |
| Spin 1/2 | 20 % | 20 % | unveraendert |
| Starke Kraft | 35 % | 40 % | S6: Flow-Skalen bei zwei Gitterabstaenden vertraeglich mit dem Hyperkubus; SU(3) fehlt |
| Mesonen, Baryonen | 5 % | 10 % | QBALL-DREIPOL-2/3 gepruefte Struktur- und Stabilitaetsbefunde in 2D/3D; weiterhin kein Einschluss und keine Hadronen |
| Schwache Kraft | 0 % (gemeinsam) | 2 % | getrennt; Literaturvorarbeit RUNDE-20/ew-baelle, kein eigener Mechanismus |
| Higgs | 0 % (gemeinsam) | 2 % | getrennt; Portalmodell-Rechnungen B13 bis B23 mit gesetzten Higgsparametern (siehe [BESTAND](coordination/higgs-bestandsaufnahme-20261007/BESTAND.md)), kein eigener Mechanismus; KI-Entwurf zur Massenhierarchie hielt nicht |
| Generationen | 0 % (gemeinsam) | 2 % | getrennt; nur Negativbefund aus ANTIGRAVITY-NACHBAU-1 |
| Vergleich mit Messdaten | 5 % | 5 % | unveraendert |
| Quantengravitation | 7 % | 7 % | unveraendert |

## Fruehere Arbeitsliste (durch die Review-Prioritaeten oben nachgeordnet)

1. **Starke Kraft:**
   - Zweiter Gitterabstand (S6) erledigt; SU(3) an den Codex-Strang uebergeben.
   - Als Naechstes SU(3) auf dem Netz mit demselben Flow-Protokoll.
   - Danach die Fadenspannung ueber einen Potentialfit mit echten Punktlagen.
2. **Volumenregel pruefen und gegebenenfalls in die Grundgleichung aufnehmen:**
   - voller G2 mit allen Ableitungen der Traegheit
   - Lesarten P, R und H
   - das Problemnetz s4
   - Herkunft der grossen Zwangskraft
   - Haelt die Regel, wird sie Teil einer Grundgleichung v4 (unimodular) [H].
3. **Selbst umbauendes Netz in gross:**
   - Erst die Grundsatzfrage: Sind Zeitschichten als Regel erlaubt? Strenge Zeitschichten sind eine echte Zusatzannahme
     [L, Kausalmengen-Literatur].
   - Dann Laeufe mit N4 >= 10^5 nach dem geeichten Protokoll: 3 bis 4 Groessen, Vergleichsflaeche, Ansatz mit Versatz.
4. **Spin 1/2 dynamisch:**
   - "Zweites Blatt": Quaternion-Rahmen mit dynamischem Vorzeichen; die Faeden sind die Vorzeichengrenzen.
   - Rohr-Drehung: Spinor-Mitdrehung an den Knicken, als Schachbrett in 3D.
   - Ziel ist, dass Spin und Statistik aus einer Ursache kommen.
5. **Datenkontakt:**
   - Perihel und Lichtablenkung ins Register.
   - Gitterschranken aus GW170817, Doppelbrechung, Torsionswaagen und LHAASO zusammenfuehren.
6. **Schwache Kraft, Higgs, Generationen:** noch ohne Mechanismus. Erst nach Spin 1/2 sinnvoll anzugehen.
