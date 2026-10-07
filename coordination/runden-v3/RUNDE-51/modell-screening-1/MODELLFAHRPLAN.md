# Modellfahrplan nach der Volltextprüfung

07.10.2026, Revision 2. Ziel ist die Suche nach passenden neuen Modellen. Jeder Kandidat bekommt einen günstigen Test, der eine konkrete Annahme widerlegen oder stützen kann. Ein negativer Befund verengt die Suche; er ist kein allgemeines No-go für andere Wirkungen.

## 1. Definitionen vor Rechenzeit

Für jeden Kandidaten festhalten: Freiheitsgrade, Hilbertraum bzw. klassische Konfigurationen, Symmetrien, Wirkung, Randbedingungen, Parameter und Messgrößen. Neue Felder oder Terme als Erweiterung kennzeichnen. Keine Gleichsetzung geometrischer Windung mit elektrischer Ladung oder SU(2)-Eichdynamik mit schwacher Wechselwirkung.

- [SKYRME-NETZ-1](karten/SKYRME-NETZ-1.md): zunächst Topologie und Randbedingungen definieren.
- [HIGGS-NETZ-1](karten/HIGGS-NETZ-1.md): zunächst Wirkung und Eichkovarianz prüfen.
- [VORTEX-MATCH-1](karten/VORTEX-MATCH-1.md): zunächst Feld- und Symmetriewörterbuch.
- [CHIRAL-MAP-1](karten/CHIRAL-MAP-1.md): zunächst Ladungen, Anomalien und Spiegelsektor.
- [ZOPF-SIMPLIZIAL-L](karten/ZOPF-SIMPLIZIAL-L.md): zunächst erlaubte Graphen und Moves.

## 2. Kontrollfall, dann Netz V

Ein bekannter Kontrollfall trennt Implementierungsfehler von neuer Physik. Erst danach dieselbe Definition auf V übertragen. Räumliche Auflösung, physikalische Boxgröße und ggf. zeitliche Ausdehnung unabhängig variieren. Ein kleiner Pilot untersucht Laufzeit und Fehlerquellen; er ersetzt keine Konvergenzstudie.

Die Karten sind revidierte Entwürfe, noch keine eingefrorenen Präregistrierungen. Vor einem numerischen Lauf: konkreten Code-Commit, Parameter, Seeds, Abbruchregeln, Fehlerbudget, Rechenbudget und konkurrierende Ressourcennutzung festhalten. Diese Veröffentlichung startet keine neuen numerischen Läufe.

## 3. Modelle an unabhängigen Größen vergleichen

[HADRON-DISKRIMINATOR-1](karten/HADRON-DISKRIMINATOR-1.md) trennt Anpassung und Vorhersage. Keine Parameter aus allen Zielgrößen bestimmen und anschließend dieselben Größen als Bestätigung zählen. Wenn mehrere Modelle gleich gut passen, die nächste trennende Messgröße benennen. [BOUNDS-PILOT-1](karten/BOUNDS-PILOT-1.md) prüft eine ergänzende Methode zur Ergebnisabsicherung.

## 4. Was einen Fortschrittseintrag rechtfertigt

Ein Ergebnisbericht nennt Modellversion, Rohdatenpfad, reproduzierbaren Aufruf, Kontrollen, Unsicherheiten und Geltungsbereich. Eine Literaturidee wird als [H] geführt, Quellenlektüre als [S], eine analytische Eigenprüfung als [M] und eine ausgeführte Rechnung als [E]. Ein stabiler klassischer Klumpen allein erhöht den Status „Baryon“ nicht; ein bosonischer Higgs-Pilot allein erhöht den Status „schwache Kraft“ nicht.

Die README-Schätzungen bleiben unverändert, insbesondere Hadronen 10 %, schwache Kraft 2 %, Higgs 2 %. Eine Neubewertung braucht neue Befunde und eine explizite Begründung. Die zwölf Erklärgrafiken bleiben schematisch.

Begründungen und Primärquellen: [Volltextvergleich](VOLLTEXT-VERGLEICH-20261007.md). Überblick: [Kandidatenmatrix](KANDIDATENMATRIX.md).

## Wiedergefundene Vorarbeiten

Die [Bestandsaufnahme B13–B23](../../../higgs-bestandsaufnahme-20261007/BESTAND.md) ergänzt bereits gerechnete radiale Higgsportal-Modelle und deren 3D-Dynamik. Vor neuen Portalrechnungen diese Ergebnisse und Normierungen prüfen. Das ist eine andere Modelllinie als HIGGS-NETZ-1; der Portalanschluss ist vorhanden, die Herleitung des Higgsmechanismus aus V weiterhin offen.
