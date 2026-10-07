# KUBISCH-ANKER-L: Laesst sich das kubische Richtungsmuster der Lichtverlangsamung auf Finns regelmaessigem Netz mit vorhandenen Gammablitz-/SME-Schranken schon pruefen? (Runde 44, Literatur, messnah)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-04 22:15:34 CEST (date), vor jedem Abruf.
- **Herkunft:** LICHT-FINN-NETZ-1 (RUNDE-37/licht-finn-netz-1/ERGEBNIS.md, NACHTRAG-PHASE-GRUPPE.md; Ernte in RUNDE-44.md).
  - Maxwell in der Coulomb-Phase auf Finns Netz: a2 = -1/12 (Achsen), -5/48 (Flaechendiagonalen), -1/9 (Raumdiagonalen), Phasenkoeffizienten von omega/k = c [1 + a2 (k l)^2], l = Tetraederkante.
  - Bedingte LHAASO-Schranke l < 7,0e-28 m (Achsen) bzw. 6,1e-28 m (Raumdiagonalen), in der LHAASO-Konvention.
- **Schreibtisch der Leitung [M, ungeprueft]:**
  - Kubische Symmetrie: a2(n) = A + B (n_x^4 + n_y^4 + n_z^4) mit A = -1/8, B = 1/24, exakt fuer die drei Werte.
  - Kugelmittel -1/10. Laufzeitversatz laengs der Raumdiagonalen 4/3-mal so gross wie laengs der Achsen.
  - Der Anteil l = 4 ist fest an den Anteil l = 0 gebunden. Die Ausrichtung der Netzachsen am Himmel ist unbekannt (drei Winkel).
- **Luecke L9 (GEMEINSAMES-NETZ):** eine Vorhersage, die sich von ART und Standardmodell unterscheidet. Ein festes Winkelmuster waere eine, falls l nahe an der Schranke liegt.
- Kennzeichen: [S] an der Quelle gelesen, [S Abstract], [L] Gedaechtnis, [M] Mathematik, [ES] eigener Schluss, [H] Hypothese.

## Ableitbarkeitsprobe und Projektsuche (vor der Karte)

- **Projektsuche** (Kostelecky, Mewes, SME, Himmelsrichtung, anisotrop, Laufzeit):
  - Im Projekt gibt es nur isotrope Laufzeitschranken: LHAASO, JLM, Martynenko in STRANG-ANKER-L und WEYL-LINEAR-1.
  - Dazu kommen Doppelbrechungsgrenzen aus der Polarimetrie (RUNDE-35, GEGENLESEN-R35) und die Uhren-SME-Tabellen (AETHER-UHR-1).
  - Eine Schranke fuer richtungsabhaengige, nicht doppelbrechende Terme der Dimension 6 ist im Projekt nicht gefunden.
- **Ableitbar am Schreibtisch:**
  - die Zerlegung des Musters in Kugelflaechenfunktionen l = 0 und l = 4
  - die Uebersetzung des isotropen LHAASO-Werts auf den l = 0-Anteil
- **Nicht ableitbar:** welche Schranken es fuer den l = 4-Anteil gibt, und ob Daten aus mehreren Richtungen ihn schon trennen.

## Auftrag (feldforscher)

1. Literatur zu richtungsabhaengiger, nicht doppelbrechender Vakuumdispersion von Photonen mit Massendimension 6, also quadratisch in der Energie.
   - Moegliche Stichworte: Kostelecky/Mewes (Operatoren beliebiger Dimension, astrophysikalische Tests), Datentabellen Kostelecky/Russell (neueste Fassung), Analysen mit mehreren Gammablitzen oder AGN-Flares aus verschiedenen Richtungen (Fermi-LAT, MAGIC, H.E.S.S., LHAASO), Schranken fuer c_(6) mit l = 4 bzw. "anisotropic".
2. **Uebersetzen:**
   - Wie sieht Finns Muster in der dort benutzten Parametrisierung aus? Das gilt fuer den Anteil l = 0 und l = 4 und das feste Verhaeltnis, mit Herleitung und als [M] gekennzeichnet.
   - Welche Schranke folgt fuer l, wenn man den l = 4-Anteil allein nimmt?
3. **Pruefbarkeit:** Reichen die vorhandenen Quellen in verschiedenen Himmelsrichtungen, um ein kubisches Muster mit unbekannter Ausrichtung gegen ein isotropes zu trennen?
   - Falls nicht: Was fehlte, etwa Zahl der Quellen, Energie oder Rotverschiebung?
4. **Gegensweep:** Gibt es Arbeiten, die Gitter-Raumzeiten mit kubischer Symmetrie gezielt testen (z. B. "lattice", "cubic anisotropy", "discrete spacetime" mit Photonen)? Gibt es einen Satz, warum ein festes Gitter schon an anderen Stellen ausgeschlossen ist (Vakuum-Cherenkov, Polarimetrie)?

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| KA1 | [H] Es gibt veroeffentlichte Schranken fuer die l = 4-Koeffizienten der Dimension 6 (nicht doppelbrechend) aus Quellen in mehreren Richtungen | 70 % |
| KA2 | [H] Diese Schranken sind fuer den l = 4-Anteil hoechstens so scharf wie die isotropen; die Netzschranke ueber l = 4 allein waere also schwaecher als 7e-28 m | 75 % |
| KA3 | [H] Mit den heutigen Daten ist ein kubisches Muster mit unbekannter Ausrichtung nicht von einem isotropen zu trennen; es braucht ein Signal nahe der isotropen Schranke | 80 % |

**Bedeutung (vorab):**
- **KA3 trifft ein:** Das kubische Muster ist eine echte, aber heute nicht pruefbare Vorhersage. Sie wird erst pruefbar, wenn ueberhaupt eine quadratische Verlangsamung gemessen wird. Fuer L9 heisst das: ein Kandidat, keine Pruefung.
- **KA3 verfehlt:** Vorhandene Mehrrichtungsdaten koennten Finns regelmaessiges Netz schon jetzt staerker einschraenken als die isotrope Schranke.

## Rahmen

- feldforscher, Zeitbox 60 min, hoechstens 8 gezielte Abrufe (arXiv-API oder Verlagsseite per WebFetch), keine Websuche noetig.
- Erwartung mit date-Zeit vor jedem Abruf in ARBEITSFELD.md.
- Schreiben nur in RUNDE-37/kubisch-anker-l/.
