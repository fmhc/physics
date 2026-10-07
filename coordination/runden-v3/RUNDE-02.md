# Runde 2 (v3)

Leitung: claude-primary. Begonnen: 2026-09-30 00:52:49 CEST (gemessen). Explorativ, keine formale Bestaetigung.

## Eingang

- Finns Auftrag: "mach weitere q-ball ideen / ideate 50 verrückte ideen wie q-balls und analogien aus dem größen ganzen
  (biologie) dazu passen könnten." Die 50 Ideen stehen in RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md.
- Aus Runde 1:
  - K-4/QG-3 geparkt bis die GPU frei ist.
- Codex, explorativ:
  - Patch-Knoten mit innerer Phase (exploration-20260930-patch-nodes/)
  - Verdichtungs-Folgefrage (exploration-20260929-qballs/)
- Rechenlage: VS-1 haelt die P5000 bis in die fruehen Morgenstunden. 1D-Tests laufen in einer Portionsluecke wie QG-1.

## Karten und Tests dieser Runde

| Idee | Test | wer, wo | Budget |
|---|---|---|---|
| 9/10 Uhren-Synchronisation | 1D: fuenf Q-Baelle mit leicht verschiedenem omega in einer Kette; Phasenordnung und Frequenzzug (gross neben klein) | Anthropic-Agent schreibt Code, Lauf .69 in einer Luecke | <= 10 min GPU |
| 32 Absorptionsspektrum | 1D: Streuung schwacher Wellen ueber einen Frequenzbereich an einem Q-Ball; Absorption gegen Frequenz, innere Moden | Anthropic-Agent, .69 | <= 10 min GPU |
| **33 Virus, Zufallskarte** | 1D: kleiner Q-Ball verschmilzt mit grossem; Modenspektrum vorher und nachher | Anthropic-Agent, .69 | <= 10 min GPU |
| 31 Gedaechtnis | 3D radial: Q(omega) durch Schiessen, beide Aeste bei gleichem Q; Vakhitov-Kolokolov-Zeichen dQ/domega; Papier plus Sekunden Rechnung | Anthropic-Agent | Minuten |
| 14 Ostwald-Reifung | 3D-Box: Codex' Verdichtung laenger rechnen; Klumpengroessen ueber die Zeit gegen Radius ~ t^(1/3) | Codex, TS440 | <= 10 min CPU |

- Die Zufallskarte ist Idee 33. Gezogen um 00:52:49 mit `shuf -n 1` aus den 43 Ideen ohne 5, 9, 10, 14, 29, 31, 32.
- Geparkt fuer spaetere Runden: 5/29 Teilung und Vererbung der Windung (braucht den 2D-Aufbau von K-4).

## Tests: Ergebnisse

- **Idee 14, Ostwald-Reifung (Codex, TS440, 43,95 CPU-s; RUNDE-02/I14-CODEX.md, i14/):**
  - Kein Nachweis von Ostwald-Reifung, auch keine belastbare Messung des Gesetzes t^(1/3).
  - Die groesseren Strukturen sind ueberwiegend periodisch windende Netze statt getrennter Tropfen.
  - Die Zaehlung haengt von der Schwelle ab und ist raeumlich nicht konvergiert (N24 gegen N32).
  - Kontrollen:
    - Die stabile Kontrolle S = .8 bleibt ohne Komponenten.
    - Energiedrift hoechstens 2,5e-5.
  - Codex' Einordnung: Der Befund ist unbestimmt, keine Widerlegung. Fuer eine echte Reifungsmessung braucht es eine
    Population getrennter Tropfen in einem schwachen Hintergrund.
  - Codex' Anschluss: eine 3D-Ladungsflussprobe zwischen zwei getrennten Q-Baellen (omega = .80 und .85). Sie ergaenzt
    Karte Chemie 1 aus Runde 3.
- **1D-Tests** (Code RUNDE-02/tests1d/tests1d.py 45fe7baa; gerechnet auf der Kleintest-Spur P4000 23:32:11Z bis
  23:36:48Z UTC; Hauptlauf 162,8 s; Bericht RUNDE-02/tests1d/lauf-69/ausgabe/tests1d_bericht.txt 9571e4a5):
  - **Idee 31, Gedaechtnis (3D radial):** Vorhersage getroffen.
    - Q(omega) hat genau ein Minimum: Q_min = 111,84 bei omega^2 = 0,927.
    - Der Duenne-Wand-Ast ist VK-stabil, der Dicke-Wand-Ast instabil. Bei gleichem Q liegt der dicke Ast hoeher
      (+0,92 bzw. +3,50). Also kein Gedaechtnis mit zwei stabilen Zustaenden.
    - Nebenbefund: E/Q > 1 ab omega^2 von etwa 0,85. Zwischen Q_min und etwa Q = 140 sind die Baelle VK-stabil, aber nur
      metastabil gegen den Zerfall in freie Quanten.
    - Die 3D-Tabelle Q, E(omega) unseres Modells liegt jetzt vor. Kontrollen: Virial 1,3e-6; dE/dQ = omega auf 6e-4;
      1D gegen Anker 3e-8.
  - **Idee 9/10, Uhren:** Vorhersage getroffen.
    - Keine Synchronisation in keinem Lauf.
    - Gleichphasige Ketten verschmelzen (D = 8: 3, D = 11: 1), wechselnde und zufaellige nicht.
    - Ein grosser Ball zieht einen kleinen nicht mit.
    - Kontrolle D = 30 ohne Effekt; L3 22/22.
  - **Idee 32, Absorption:** Vorhersage verfehlt.
    - Statt "keine Absorption (< 1e-4)" gibt es eine Absorptionsspitze von 2e-3 bis 3e-3 bei nu = 2,25 bis 2,4.
    - Die Spitze liegt bei nu - omega ~ 1,48, also bei der inneren Mode Omega = 1,481 aus der Stossprobe. Das deutet auf
      resonanten Einfang bei einer inneren Frequenz hin ("Erkennung").
    - L3 nur 4 von 12: Die Spitze aendert sich grob gegen fein um etwa 35 %. Numerisch nicht konvergiert, kein Befund.
    - **BERICHTIGUNG** 30.09. nach Codex' Nachlesung (exploration-20260930-opus-review/REVIEW.txt), von der Leitung am
      Ergebnis-JSON nachgezaehlt:
      - Die Zahl 4/12 galt fuer die Reflexion R_Q. Fuer die Absorption dA_Q besteht L3 in 0 von 12 Frequenzen.
      - Gemessen ist ein Anteil am einfallenden Ladungsstrom (0,21 bis 0,32 %), nicht an der Ballladung.
      - Die Groesse A ist ein frequenzabhaengiger Rest, der zum Zeitpunkt T = 500 noch innerhalb |x| < 30 steckt
        (Speicherung oder Verzoegerung). Ein dauerhafter "resonanter Einfang" ist damit nicht gezeigt.
      - Die Stossmoden-FFT (Frequenzraster 0,125) identifiziert keinen diskreten gebundenen Eigenmodus.
      - Status: Resonanz- oder Verzoegerungskandidat.
    - **NACHRECHNUNG CODEX** 30.09., auf Finns direkten Auftrag (resonance-20260930/ERGEBNIS.txt 1d0381d8; TS440 CPU 124 s
      plus eine lokale lineare ODE):
      - **Lineare Zwei-Kanal-Randwertrechnung:** Resonanzpol rho = 1,49377696 - 6,716e-5 i.
        - Der publizierte Ciurla-Kalibrierpol wird reproduziert.
        - Ohne Ball gibt es keinen Pol.
      - **Zeitentwicklung auf drei Gittern** (h = 0,1 / 0,05 / 0,025):
        - Die gespeicherte Ladung bei nu = 2,375 klingt mit 1,3414e-4 ab (Fenster T 500 bis 800, feinstes Gitter),
          vorhergesagt ist 2 Gamma = 1,3432e-4. Das ist eine Abweichung von 0,13 %.
        - Mit halbierter Paketstaerke ergibt sich dieselbe Rate: linear.
        - Die gespeicherte Menge bei T 500 betraegt 0,27 / 0,20 / 0,18 % der Paketladung; die letzte Gitteraenderung ist
          12 %.
        - Ein schwacher Stoss gibt eine spaete Frequenz von 1,4925, nahe am Pol.
        - Der Energie- und Ladungsfluss nach aussen ist positiv.
      - **Deutung:** Das ist eine langlebige, ausleckende Resonanz (quasinormale Mode) mit einer Halbwertszeit der
        Amplitude um 10 000 Zeiteinheiten.
        - Keine dauerhafte Aufnahme, kein neues Teilchen, keine Aussage fuer 3D.
        - Der Mechanismus ist Literatur: Ciurla u. a. 2405.06591 (dieselbe Potentialfamilie), Azatov u. a. 2412.13885,
          Evslin u. a. 2604.07713, Saffin u. a. 2212.03269.
        - Neu fuer uns ist der quantitative Abgleich unserer Parameter.
      - **Karte 32:** geklaert als "bekannt" (L4). Die eigene Anthropic-Feinrechnung (tests1d_fein, laeuft) ist die
        Zweithaus-Probe.
    - **FEINRECHNUNG ANTHROPIC** (tests1d_fein.py 212028df auf den P4000-Spuren, 00:07:39Z bis 00:23:20Z; Belege
      RUNDE-02/tests1d/fein-lauf-69/):
      - **Konvergenz:** vier Gitterstufen, bis 243 Punkte je Wellenlaenge. dA_Q(t = 500) an der Spitze:
        - nu = 2,325: 3,68e-3 -> 2,46e-3 -> 2,12e-3 -> 2,03e-3, q = 0,257, Ordnung p = 1,96, Richardson 2,00e-3,
          Urteil "konvergiert"
        - nu = 2,25 und 2,375: ebenso konvergiert (1,24e-3 bzw. 1,68e-3)
        - Kontrollen nu = 1,5 und 1,9: kein Effekt
        - Die Spitze steht bei 2,326 gegen nu_res = omega + Omega_2 = 2,330.
      - **Resonanz aus dem Stoss bei fester Ladung:** Frequenz 1,49369 (Codex-Pol 1,49378), Ladungsrate 1,36e-4 (2 Gamma
        1,343e-4). Der Speicher bei nu = 2,325 faellt von 2,08e-3 (t = 300) auf 2,03e-3 (t = 500), passend zur
        Abklingrate. Randrueckstrom ohne Ball hoechstens 2e-12.
      - **Ueber der Kanalschwelle** (nu = 2,75 und 2,9): Antiteilchenstrom von etwa 3,3 bis 3,7e-4 und ein konvergierter
        Rest von 7,7e-4 bzw. 7,3e-4, also Zwei-Kanal-Streuung.
      - **Groessenprobe:**
        - omega^2 = 0,6: Die Spitze liegt bei 2,151, vorhergesagt aus dem eigenen Stoss nu_res = 2,153; der Speicher ist
          groesser (bis 1,5e-2). Fabry-Perot sagte 2,47, trifft also nicht.
        - omega^2 = 0,8: kein nennenswerter Speicher (~1e-6, schrumpft mit dem Gitter).
        - Das Bild der inneren Resonanz traegt, das Resonatorbild nicht.
      - **Zwei-Haus-Befund (explorativ):** langlebige, ausleckende Resonanz bei nu - omega = 1,494, bekannt aus der
        Literatur; unsere Zahlen stimmen quantitativ.
- **Karte 33, Verschmelzungskarte** (Test 3K, 32 Stoesse, L3 32/32):
  - Gleiche Frequenz (0,55 gegen 0,55), gleichphasig: verschmilzt bei v = 0,02, 0,05 und 0,10, laeuft bei 0,20 durch.
  - Gegenphasig: prallt bei v <= 0,1 ab.
  - Schon 0,60 gegen 0,55 verschmilzt bei keinem v (vorhergesagt waren mindestens 2 von 4).
  - 0,65 verschmilzt nur bei v = 0,02.
  - 0,70, 0,80 und 0,90 verschmelzen nie.
  - Ergebnis: Verschmelzen fast nur bei gleicher Frequenz und kleinem Tempo. Die Kausalfrage aus der Codex-Nachlesung ist
    damit im Ein-Feld-1D-Modell beantwortet: Der Frequenzunterschied entscheidet.
  - **Idee 33, Virus (Zufallskarte):** Vorhersage verfehlt.
    - Der kleine Ball (omega^2 0,9) verschmilzt bei v = 0,1 in keiner der 8 Kontaktphasen mit dem grossen (0,55); M = 0,003.
    - Nur 0,004 Ladung wandert vom kleinen zum grossen.
    - L3 8/8. Wahrscheinlicher Grund: Die relative Phase dreht mit Periode 31 zu schnell, und die Anziehung mittelt sich weg.
    - BERICHTIGUNG 30.09. (Codex-Nachlesung): Der Frequenzunterschied wurde nicht variiert, die Ursache ist also nicht
      isoliert. Kein allgemeiner Satz "ungleiche Frequenzen verhindern Verschmelzen". Die Karte (Test 3K) prueft das jetzt.
  - Ebenfalls berichtigt:
    - "VK-stabil" bedeutet im Code nur dQ/domega < 0, kein volles Stoerspektrum.
    - E/Q > 1 heisst "freier Endkanal energetisch erlaubt", nicht "gemessene Zerfallszeit".
    - Codex' unabhaengiges Profil bei omega = 0,8 (Q 1172,34, E 997,909) stimmt mit unserer Zeile omega^2 = 0,64 ueberein.
      Das ist ein Implementierungsabgleich.
- **Idee 14, Ostwald (Codex):** siehe oben, nicht gezeigt.

## Abschaetzung

Abschaetzung der Leitung, 2026-09-30 01:37:45 CEST (gemessen).

| Karte | L1 | L2 | L3 | L4 | L5 | Nutzen | Entscheidung | Grund |
|---|---|---|---|---|---|---|---|---|
| 31 Gedaechtnis | ja | ja | ja | ja (VK bekannt) | nein | mittel (3D-Tabelle als Werkzeug) | parken ("bekannt") | kein Bistabil; die Q(omega)-Tabelle dient kuenftigen Karten |
| 9/10 Uhren | ja | ja | ja | teilweise | nein | niedrig | verwerfen | keine Synchronisation, nur Verschmelzen oder Auseinanderlaufen |
| 32 Absorption | ja | ja | **nein** (4/12) | nein | nein | mittel bis hoch | **weiter** | Resonanzspitze bei nu - omega ~ innere Mode; erst mit feinerem Gitter konvergieren |
| 33 Virus (Zufall) | ja | ja | ja | teilweise | nein | mittel | **weiter** | Verschmelzen scheitert bei verschiedenen Frequenzen; Fusionsbedingung in (Delta omega, v) kartieren |
| 14 Ostwald (Codex) | ja | ja | nein (raeumlich) | teilweise | nein | mittel | parken | Netze statt Tropfen; erst mit getrennten Tropfen im schwachen Hintergrund neu stellen |

**Latten-Bilanz:**
- L3 stoppte 32 vorerst.
- L4 traf 31.
- L5 (Messbezug) fehlt bei allen Karten der Runde.
- **Zufall gegen Auswahl:** Die Zufallskarte 33 geht weiter; von den gewaehlten Karten geht eine weiter (32).

## Einfach gesagt

Die Biologie-Vergleiche halten meist nicht: Q-Baelle takten sich nicht wie Gluehwuermchen, und sie haben kein Gedaechtnis
mit zwei Zustaenden. Zwei Ueberraschungen gibt es aber. Ein Q-Ball schluckt Wellen einer ganz bestimmten Frequenz etwas
mehr als andere, fast wie ein Schloss, das nur einen Schluessel nimmt; das muessen wir noch genauer nachrechnen. Und ein
kleiner Q-Ball, der auf einen grossen trifft, verschmilzt nicht mit ihm, wenn ihre inneren Uhren zu verschieden ticken.
