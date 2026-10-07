# HIGGS-FORCE-1: Die reduzierte Energie liefert brauchbare Portalkräfte

08.10.2026 · [E] neue CUDA-Auswertung von 24 unveränderten B13-Profilen.

Die beste hier geprüfte Energie-Kraft-Kombination, **Ecomp mit vollständiger Kettenregel**, erreicht beim stärkeren Portal einen Kraftfehler von **0,00967–0,01159 %** gegenüber dem archivierten stationären Higgsfeld. Alle drei vorher festgelegten Energie-Kraft-Paare bestehen die 5-%-Pilotprüfung in allen acht Parametergruppen. Das gilt für diese festen Profile, nicht bereits für neue Minima oder Zeitentwicklung.

![Fehler der reduzierten Portalkräfte und Higgsenergien](force-errors.svg)

## Was tatsächlich verglichen wurde

Zwei komplexe Singulettfelder und eine reale Higgsamplitude im **radialen 3D-Modell**. Die 24 Profile umfassen acht Kombinationen aus eta=0,05/0,1, g=0,001/0,005 und c8=0/1 auf jeweils Basisgitter, feinem Gitter und größerer Box. Keine neue Relaxation, keine Fits. Normierung und Randwerte entsprechen B13; Eingabe und Hash sind veröffentlicht.

Der gemessene Kraftfehler ist `||u*(C-Cref)|| / ||u*Cref||`, mit `u_i=r*F_i` und `Cref=b/2*(y_ref²-y0²)`. Er betrifft den zusätzlichen Portalterm in der Singulettgleichung, nicht die Gesamtbeschleunigung. Energiefehler beziehen sich auf den Higgsbeitrag einschließlich seiner Gradientenenergie; keine Verdünnung durch die größere Gesamtenergie.

| Portalkopplung g | Energie/Kraft | Kraftfehler [%] | Higgsenergiefehler [%] | Parametergruppen bestanden |
|---|---|---:|---:|---:|
| 0,001 | E2 / C2 | 0,4080–0,4249 | 0,2114–0,2191 | 4/4 |
| 0,001 | E3 / C3 | 0,02191–0,02283 | 0,008102–0,008385 | 4/4 |
| 0,001 | Ecomp / Ccomp | 0,00002197–0,00002588 | 0,00000693–0,00000807 | 4/4 |
| 0,005 | E2 / C2 | 2,693–2,809 | 1,287–1,335 | 4/4 |
| 0,005 | E3 / C3 | 0,7328–0,7628 | 0,2524–0,2611 | 4/4 |
| 0,005 | Ecomp / Ccomp | 0,009671–0,011592 | 0,003440–0,004090 | 4/4 |

Spannen über vier Fälle auf dem feinen Gitter, keine statistischen Konfidenzintervalle. Die Entscheidung verwendet **alle drei Gitter/Box-Stufen** und den vorab festgelegten Driftaufschlag, siehe [PLAN.md](PLAN.md). Maximaler beobachteter Gitter-/Boxindikator: 2,956e-6 als relativer Fehler, entsprechend 0,000296 Prozentpunkten. Dies ist ein Diskretisierungsindikator, keine bewiesene Fehlerschranke zum Kontinuum.

## Warum die Ableitung der Energie entscheidend ist

[M] Mit Dichte `S=|psi1|²+|psi2|²`, `b=g/0,01`, `y0=0,492` und `K=-Delta+6,25`:

```
chi1 = -K^-1(b*y0*S)
chi2 = -K^-1(b*S*chi1 + 3*a*y0*chi1²)
a = 125²/(2*246²*0,01)

EH(chi,S) = 1/2 <chi,K chi> + <b*y0*S,chi>
            + b/2 ∫ S chi² + a*y0 ∫ chi³ + a/4 ∫ chi⁴

E2 = -1/2 <b*y0*S, K^-1(b*y0*S)>
E3 = E2 + b/2 ∫ S chi1² + a*y0 ∫ chi1³
Ecomp = EH(chi1(S)+chi2(S), S)

C2 = b*y0*chi1
C3 = b*y0*(chi1+chi2) + b/2*chi1²
Ccomp = vollständige funktionale Ableitung von Ecomp nach S
```

Die Integrale verwenden das räumliche 3D-Maß. `chi1` ist erster, `chi2` zweiter Ordnung in b bei festgehaltener Dichte. E3 behält die Energie bis einschließlich dritter Ordnung; Ecomp setzt die angenäherte Antwort in die vollständige statische Energie ein und enthält dadurch weitere, nicht vollständig kontrollierte höhere Ordnungen. Es ist keine exakte Ausintegration des Higgsfeldes.

Selbstadjungiertheit von K liefert die angegebene analytische Formel für C3. Für Ecomp gilt die Kettenregel: Zum expliziten Dichtebeitrag kommt die Rückwirkung der Dichteänderung auf das angenäherte Higgsfeld. Nur bei einer exakt stationären Higgsantwort verschwindet der entsprechende Energieresidualterm exakt.

[E] Die naheliegende Abkürzung `Cplug=b*y0*(chi1+chi2)+b/2*(chi1+chi2)²` lässt diese Kettenregel weg. Bei g=0,005 hat sie **0,617–0,673 % Kraftfehler**; der ausgelassene Beitrag beträgt **0,609–0,663 %** der Ccomp-Kraft. Die zwei vorab festgelegten Dichtevariationen zeigen zudem einen gemischten Ableitungsdefekt von **0,580–0,594 %**. Für eine zweimal differenzierbare skalare Energie müssen diese Kreuzableitungen symmetrisch sein: Cplug ist damit in dieser Diskretisierung keine konsistente Ersatzkraft für Ecomp. Bei g=0,001 ist der Defekt kleiner, aber ebenfalls aufgelöst (0,01997–0,02039 %).

Die sehr kleinen Ecomp-Fehler sind numerische Ergebnisse dieser Profile. Die stationäre Struktur erklärt, warum eine unvollkommene Feldantwort trotzdem eine besonders genaue Energie liefern kann; sie garantiert die beobachtete Kraftgenauigkeit nicht für beliebige Dichten.

## Prüfung und Reproduzierbarkeit

Alle 24 Fälle bestanden vor der Einordnung:

- Analytisches C3 gegen automatische Differentiation: maximaler relativer Fehler **2,43e-16**.
- Unabhängige zentrale Richtungsdifferenzen, Schritte 0,01; 0,005; 0,0025: beim kleinsten Schritt maximal **2,60e-8** für E3, **6,09e-8** für Ecomp; vollständige Folgen in QA.json.
- Symmetrie der gemischten Richtungsableitungen: maximal **4,50e-16** für E3, **2,49e-16** für Ecomp.
- Nullkopplung: Antwort und Energiekorrektur exakt null im ausgeführten Test.

Vorabplan und Rechencode wurden vor Ausführung gehasht und im gemeinsamen Arbeitsprotokoll angekündigt. CUDA float64 auf Quadro P5000, Torch 2.5.1+cu121; Kernrechnung 2,558 s, begrenzter Dienst insgesamt 5,330 s. CPU für Ablauf, Datei-I/O, skalare Zusammenfassung und Matplotlib. Der Lauf nutzte den gemeinsamen GPU-Lock und eine anschließend freigegebene Ressourcenpacht. Keine Laptop-Numerik.

- [Vorabplan](PLAN.md), [Rechencode](run.py), [Grafikskript](report.py)
- [Ergebnisse und alle Gruppenentscheidungen](results/RESULT.json), [QA einschließlich Einzelabweichungen](results/QA.json)
- [Laufprovenienz](results/PROVENANCE.json), [Exportprovenienz](PROVENANCE.json)
- [Unveränderte B13-Eingabe](../higgs-response-20261008/B13-PROFILES.json), SHA256 `1aa779f171b0ab3c3eb1b844d98934b18cb6dc129b398fff10ea7e33ce801a7d`

Zur Reproduktion beide benachbarten Ergebnisordner erhalten, dieses Verzeichnis in ein frisches Arbeitsverzeichnis kopieren und dort die archivierte `results`-Kopie entfernen bzw. vorher getrennt sichern. `python run.py` erfordert CUDA und schreibt ausschließlich einen neu anzulegenden Ergebnisordner; `python report.py` liest ihn und erstellt die Grafik. Im exportierten Rechencode wurde ausschließlich der Eingabepfad auf die veröffentlichte Nachbardatei umgestellt. Original- und Exporthash sind getrennt vermerkt; keine erneute Rechnung nur wegen des Exports.

## Einordnung und nächster Entscheidungstest

**Idee 1 aus den zehn Verbindungen hat jetzt einen zusätzlichen berechneten Baustein:** eine auf den Archivprofilen geprüfte reduzierte Energie samt konsistenter Kraft. Ecomp ist innerhalb dieses Vergleichs am genauesten; E3 bleibt eine explizite, nach Ordnungen abgeschnittene Alternative. Eine billigere oder schnellere Dynamik wurde noch nicht gemessen.

Als nächster abgegrenzter Test bieten sich selbstkonsistente Minima bei festem Q an: gleiche Startprofile und Parameter, volle Portalenergie gegen E3 und Ecomp, vorab festgelegte Kriterien für Profil, Energie, Frequenz, Residuum und Gitterabhängigkeit. Erst anschließend sind Zeitentwicklung, Energieerhalt und vollständige Modenprüfung aussagekräftig. Das ist ein Vorschlag, noch kein ausgeführter Test.

Die funktionale Kettenregel gilt ebenso in 1D und 2D; Green-Funktion, Integrationsmaß, Randwerte und Ladungsnormierung ändern sich. Die Zahlen hier gelten nur für radialen 3D-Raum, nicht für ein 1D-Modell und nicht für alle nicht-radialen Störungen. Auf dem gefüllten Netz V muss die Ableitung mit dem dortigen Gewichtsmaß und diskreten Operator erneut geprüft werden.

Keine neue Herleitung von Higgsmasse oder Vakuumwert, keine elektroschwache Eichdynamik, keine Hadronenidentifikation. Die subjektiven Entwicklungsschätzungen bleiben deshalb unverändert: Higgs 2 %, schwache Kraft 2 %, Mesonen/Baryonen 10 %.
