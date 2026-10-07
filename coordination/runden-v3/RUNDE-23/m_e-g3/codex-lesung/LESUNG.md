# M_E-G3: Fremdhaus-Gegenlesung (OpenAI)

Root: ag-phy-coordination, 02.10.2026. Auftrag 4ff7ae580fdb446eb49d68baf798cb54. Reine Quellen-/Codelektüre und Papieralgebra; keine neue Numerik. Eingangsbindungen in EINGANG.sha256, Beginn in BEGINN.txt. Autorendateien, WARUM-SPIN-2.md und Manuskripte unverändert.

**Gesamturteil: Klasse C — Herleitung offen, mit einem brauchbaren numerischen Funktionalkandidaten. „Klasse A, vorläufig“ hält als Antwort auf die bindende Karte nicht.** Dies ist weder eine Widerlegung des Kandidaten noch Klasse D. Die stärkste positive Lesart ist ein möglicher führender Log-Koeffizient unter einer noch auszuarbeitenden Rest- und Positivitätskontrolle.

## 1. Führende Ordnung und gleichmäßiger Rest

**Führende Baumordnung: hält. Gleichmäßiger Rest und daraus folgende Schranke: unklar/nicht hergeleitet.**

Mit g=GM², L=log(M/E), e=gL und y=gx gilt unter der eingefrorenen Skalierung exakt y=xi e. Der bisher bei festem x subführende Baumterm gx ist jetzt endlich. Ebenso ist g²L²=e² führend. Das beantwortet einen echten Einwand des Vorläufers; die Skalierung wurde vor den LP-Rechnungen festgelegt.

Die benötigte Folgerung ist jedoch stärker als diese Algebra. Für genau das helizitätsabhängige Funktional muss nach Verschmierung, UV-Integration und Spinsumme eine Schranke |R|<=C_K g auf einem ausdrücklich bestimmten Parameterbereich K gelten. Die Tabelle in ERGEBNIS.md:104–128 weist erwartete Potenzen aus, liefert diese Majorante aber nicht. Die Analogie zu Pionen und die Bezeichnung einer Schleife als „berechenbar“ ersetzen ihre Kontrolle nicht.

Zusätzlich bleibt der Schritt von Ae-By+O(e²,ey,y²)+O(g)>=0 zur oberen Schranke für y bedingt: Ein unkontrollierter y²-Term erlaubt im Allgemeinen einen zweiten großen Ast. Im weiteren Grenzwert e->0 bei beschränktem xi ist y klein, wodurch ein führender Koeffizientenvergleich plausibel wird. Hierfür müssen aber die übrigen Kontaktkopplungen und der zulässige Bereich benannt sein. ARBEITSFELD W2, Zeile 9, benutzt g4~y ohne entsprechende vollständige Festlegung im eingefrorenen Plan. Das Fehlen von Baumkontakten in B2/B3 schließt Kontakt-Schleifen nicht aus.

**Konkrete Textkorrektur:** Bei festem e>0 ist L O(e) kein O(1). ERGEBNIS:118 behält die mögliche Korrektur c0 L[1+O(e)]+O(1); :97–98 und :140–141 lassen sie weg. Das Zusatzregime L=O(g^-1/2) aus :119 ist ein anderer gemeinsamer Grenzweg und darf nicht still den zuerst festgehaltenen e-Grenzwert ersetzen.

## 2. Wörterbuch und komplexe Kopplung

**Normfaktor: hält in den verglichenen Amplitudenkonventionen. FRS-Zuschreibung „g3² bedeutet |g3|²“: unklar als Quellenbehauptung.**

GR-Abgleich gibt M_Pl^-2=8piG. Aus den Dreipunktamplituden folgt g_CH/(2M_Pl)=g_FRS/M_Pl³, also |g_CH|²=4|g_FRS|²/M_Pl⁴. Auch der MHV-Austauschterm passt nach Vertauschung der bezeichneten t/u-Kanäle. Die Kontaktabbildung und der Faktor -1/2 zwischen den angegebenen B4/B0-Regeln sind damit konsistent.

CHLPSD behandelt die Kopplung ausdrücklich komplex. FRS schreibt g3²; die gelesenen Stellen legen keine entsprechende komplexe Konvention ausdrücklich fest. Für reelles g3 gibt es keinen Unterschied. Für eine hermitesche Erweiterung mit konjugierten (+++) und (---)-Vertices entsteht das Betragsquadrat. Diese Erweiterung als eigene begründete Konvention kennzeichnen, nicht als wörtliche FRS-Definition. Sie ist kein neuer Zahlenfehler des Faktors vier. Entsprechend braucht auch die x-Formel in Abschnitt 2 bei komplexem g3 Betragsstriche. Ein festes Betragslimit fixiert nicht automatisch die Phase. Der geprüfte Faktor -1/2 betrifft die angezeigten Niederenergieglieder; eine Identität der vollständigen Funktionale ist damit nicht geprüft.

## 3. Funktional, Gitter und Klasse A

**Ein numerisch untersuchter Kandidat: hält. Hinreichender Nachweis für Klasse A: hält nicht.**

Die gelesene Implementierung hat passende CHLPSD-Kerne, Spinselektion und q-Normierung. c≈895 ist als berichteter numerischer Baumkoeffizient nachvollziehbar; in dieser Gegenlesung wurde er nicht neu berechnet. Er ist noch kein bewiesener universeller Schrankenkoeffizient.

Offen bleiben Zwischenmassen, J>3000, der vollständige gemeinsame Groß-J/Groß-m-Übergang sowie zertifizierte Vorzeichen bei aktiven LP-Bedingungen. Ein Besselgrenzwert und einige Schwanzkoeffizienten liefern ohne uniformen Rest keinen endlichen Anschluss an das geprüfte Gebiet. Die sehr kleinen negativen Werte können Rundung sein, sind ohne Einschließung aber nicht bewiesen gleich null.

Konkrete Berichtspräzisierung: Die Materieprüfung startet tatsächlich bei m_l=10^-3; ERGEBNIS:83 „(0,M]“ ist zu weit. Der im LP-Skript verbliebene 700-Punkte-Schwellentest ist für J=3000 nicht ausreichend; die gesonderte 6200-Punkte-Prüfung ist dafür die relevante Nachprüfung, aber weiterhin nur an endlich vielen Massen. Kein gefundenes Gegenbeispiel zur neuen q=.95-Lösung wird behauptet.

Der Autor legt diese Grenzen bereits im eingefrorenen Plan offen. Diese Offenlegung ist korrekt, erfüllt aber die bindende Anforderung „Schranke hergeleitet, Rest gleichmäßig kontrolliert“ nicht. Die Kombination „Klasse A, aber kein Positivitätsbeweis“ behebt diese Lücke nicht.

## 4. B4 und exakter Vorwärtsgrenzwert

**Hindernis für den naiven un-subtrahierten Vorwärtswert/-Ableitung: hält. Allgemeines B4-Unmöglichkeitsergebnis: hält nicht.**

FRS F.7 enthält im dort angegebenen Regime die Struktur log(-t/E²)/t. Sie lässt einen ungeschützten exakten Vorwärtswert oder dessen Ableitung nicht als gleichmäßig kontrollierten Baustein zu. Das stützt den Verzicht auf diesen Baustein im jetzigen Kandidaten.

Daraus folgt kein Ausschluss jeder subtrahierten, kombinierten oder verschmierten B4-Konstruktion. Auch die im Bericht erwähnte Vermischung mit g4/g5 ist eine Eigenschaft des gezeigten Funktionals, kein allgemeiner Satz über alle Funktionale. Genaue Formulierung: „Hier wurde kein kontrollierter B4-Anteil konstruiert; der direkte Vorwärtsgrenzwert ist durch F.7 problematisch.“ Die geschätzten o(L)-Wege in W5e bleiben Vorschläge ohne Nachweis.

## 5. Äußere Gravitonen und schwächste Übertragung

**Verwendung des M_E-Rahmens für äußere Gravitonen grundsätzlich: gestützt. Für diese gesamte Herleitung und Skalierung: unklar.**

Die schwächste Stelle ist die Übertragung der Regge-/Eikonal- und funktionalen Restkontrolle auf das konkrete helizitätsabhängige B2/B3-Superkonvergenzfunktional bei endlicher kanonischer R³-Kopplung. Es braucht eine Darstellung mit Helizitätsgewichten, Crossing und gemeinsamer Fehlerabschätzung. Die Universalität des führenden weichen Faktors allein erledigt die harte hochenergetische Amplitude nicht.

Ein konkreter zu schließender Anschluss: BBIRRS 4.10 nennt s≫q_max²; q_max=.95M liefert an s=M² keine solche Hierarchie. Eine getrennte Kontrolle der weichen Region und des regulären Restes kann diesen Anschluss möglicherweise liefern, ist hier aber nicht durchgeführt. Das ist kein Gegenbeweis gegen die Wahl .95M. Ebenso genügt das Fehlen linearer g³-Terme im MHV-Baum allein nicht als Ausschluss sämtlicher entsprechender Schleifenreste; ein tatsächlicher Gegenbeitrag wird hier nicht behauptet.

Die stärkste Gegenposition zu einem pauschalen Nein lautet: BBIRRS lässt weitere kurzreichweitige Kopplungen zu, und FRS Anhang F verwendet M_E bereits für äußere Gravitonen. Wir verwerfen daher weder äußere Gravitonen noch die Skalierung selbst. Offen ist die konkrete zusätzliche Brücke samt uniformer Kontrolle. Sie per Definition im Plan zum „Teil des Rahmens“ zu erklären ist noch keine Ableitung.

## Quellen und Lesetiefe

Selektive Originaltextlektüre, kein vollständiger Beweis-Audit:

- [BBIRRS v2](https://arxiv.org/html/2512.13780v2), §§3–5 und Schluss: Gl.3.10–3.12 zum Eikonal-/Regge-Schritt; 4.8 zur Nichtvertauschbarkeit; 4.10 funktionale Unitarität; 5.13 verlangt sämtliche Spins/Massen; 5.16–5.17 geben die gravitative Restordnung an. Lokaler Text insbesondere Z.500–622,724–844,1015–1124,1840–1868; HTML-Version zusätzlich geöffnet.
- [CHLPSD](https://arxiv.org/abs/2201.06602), §§2.1–2.4, insbesondere 2.6–2.7,2.25–2.35 und Anhang-A-Kerne. Die B2/B3-Baumformeln enthalten ausdrücklich zusätzliche Materie-/Schleifenbeiträge.
- [FRS v2](https://arxiv.org/abs/2603.15755v2), Gl.2.3, Dreipunktstelle S.9,4.39 sowie F.1–F.10. F.7 wird innerhalb F.4 gelesen, nicht als globaler No-go-Satz.

Teilberichte: NORMIERUNG-B4.txt, POSITIVITAET.txt, SKALIERUNG.txt; Root-Papieralgebra in ROOT-ARBEIT.txt. Code- und Ergebnislektüre ist keine unabhängige Wiederholung der numerischen LP-Läufe.

## Nächster enger Schritt

Zuerst den Anspruch auf Klasse C und c≈895 als Kandidat berichtigen. Danach entweder eine globale Positivitätsbescheinigung für genau ein festes Funktional oder eine fallbezogene Restherleitung mit benannten Kopplungsbereichen ausarbeiten. Eine weitere größere Gitterabtastung allein schließt die Hauptlücken nicht. Faktor36 bzw. dessen achte Wurzel≈1.57 bleiben algebraische Koeffizientenvergleiche; daraus folgt gegenwärtig keine etablierte neue Teilchen-Massenschranke.
