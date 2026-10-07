# ANTIGRAVITY-NACHBAU-1: Ergebnis

- Rechen-Agent fuer die Leitung claude-primary.
- Zeiten (date; .69 in UTC, CEST = UTC + 2):
  - Karte 02:49:23 CEST, VORAB.md ab 02:54:24 CEST, vor jeder Rechnung.
  - Laeufe auf der .69 von 01:00:21 bis 01:13:28 UTC, alle ueber kleintest.sh (cpu8, cpu9, cpu10).
  - df vor jedem Start: 17 GB frei.
  - Text ab 03:13:49 CEST.
- Kennzeichen: [E] gerechnet, [M] Schreibtisch, [P] Projektdatei, [L] Literatur aus dem Gedaechtnis, ungeprueft, [H]
  Hypothese.
- Alles ist synthetische Rechnung an gedachten Netzen. Keine Messdaten, keine Messdatenbestaetigung.

## 1. Ergebnis zuerst

1. **Der Vermerk der Leitung haelt in allen Punkten, die ich nachgerechnet habe.** Ich habe keinen Fehler in Richtung "die
   Leitung war zu streng" gefunden, mit einer Ausnahme (Punkt 2).
   - Zwei der acht Skripte brechen beim Start ab: dirac_gitter_gpu.py wegen parse_argument, unimodular_pachner.py wegen
     res.maxcv.
   - Drei Skripte setzen das Ergebnis von Hand ein: generationen_dimensionen.py (1, 2, 3 eingetippt),
     gravity_nearfield_collapse.py (alpha = 1,5 ist genau der ART-Wert) und ribbon_frustration.py (alle Zahlen gesetzt).
2. **Ueberraschend tragfaehiger Kern bei AG2, aber nur in einem von drei Netzen [E]:**
   - Die globale Volumenbedingung (Gesamtvolumen fest) entfernt beim Ausnahmezug in s2 die negative Traegheitsrichtung
     und die wachsende Mode. Das gilt in Lesart H, also am Hintergrund.
   - Das ist kein Zufall: Von 10 000 Zufallsbedingungen schafft das nur 1.
   - In s1 und s3 hilft dieselbe Bedingung aber nicht; die wachsende Mode bleibt dort.
   - Die lokale Lesart (Volumen je Ecke fest) entfernt die wachsende Mode zwar ueberall. Das tun aber auch 128 beliebige
     Zufallsbedingungen, es ist also ein Ueberzwang und kein Mechanismus.
3. **Teil C (Peierls, Noether) ist richtig im Aufbau, aber falsch im Vorzeichen [E].**
   - Die Stromformel in THEORIE-ABC.md ist nicht eichinvariant (Abweichung 227 %).
   - Die Ladung hat das falsche Vorzeichen, die Kontinuitaetsgleichung stimmt deshalb nicht (Rest 77 %).
   - Mit e^{-iqA} und -Q geht alles auf 1e-9 auf. Das ist Lehrbuch [L]; neu ist daran nichts.
4. **"3 Generationen = 3 Taeler" [E]:**
   - Ohne Spin-Bahn hat keines der 64 Z2-Flussmuster der kubischen Zelle isolierte Knoten. Alle haben ausgedehnte
     Nullmengen.
   - Mit Spin-Bahn (Fu/Kane/Mele) gibt es genau drei Dirac-Punkte an X, aber nur am isotropen Punkt.
   - Die Massen der drei Taeler lassen sich mit den vier Bindungsstaerken frei einstellen: e:mu:tau = 1 : 206,8 : 3477
     ergibt sich mit Spannungen von hoechstens 25 %, aber mit einer Ausloeschung auf 1e-4. Eine Vorhersage ist das nicht.
5. **AG3 und AG4 [E, vorab ableitbar]:**
   - Der Periheldreh-Faktor aus unseren eigenen Netzwerten gamma und beta ist 0,993 bis 1,000. Die Periheldrehung steckt
     also schon in der gerechneten Grundgleichung (BETA-NETZ-V), nicht in Antigravitys alpha.
   - Der Rotor-Witness ist 32 Groessenordnungen zu klein. Die Formel im Skript ist dimensionsbehaftet, und der Effekt ist
     reine ART, kein Test unseres Modells.

## 2. Tabelle je Gedankengang

| Gedankengang | Idee (zwei Saetze) | Was richtig ist | Behauptet, nicht gezeigt | Rechenbarer Kern fuer unser Modell | Urteil |
|---|---|---|---|---|---|
| **A: 4D-Pachner-Zug** (THEORIE-ABC A) | Ein 2-3-Zug im 3D-Schnitt ist genau ein 4-Simplex zwischen zwei Zeitschnitten. Mit der 4D-Regge-Wirkung dieses Simplex soll Energie exakt erhalten bleiben und die Kaskade entfallen. | 5 Knoten, 9 bzw. 10 Kanten, ein 4-Simplex: richtig [M]. Kanonische Regge-Rechnung mit Pachner-Zuegen gibt es (Dittrich/Hoehn, "evolving phase spaces" [L]). | "exakte Erhaltung", "Kaskade entfaellt": keine Rechnung. In unserem Code ist die neue Kante nicht frei, sie folgt aus der flachen Doppelpyramide. | Die freie neue Kante waere der Ort, wo Dittrich/Hoehn Zwangsbedingungen bekommen [L]. Das ist eine Karte wert, nicht gerechnet. | teilweise (Geometrie richtig, Folgerung ungezeigt) |
| **A': unimodular_pachner.py** | Haelt man das 4-Volumen fest, kann die innere Kante nicht divergieren. Damit soll die Kaskade gestoppt sein. | Unimodulare Gravitation ist Literatur (Henneaux/Teitelboim [L]). | Skript: Die Wirkung ist ausdruecklich ein Dummy. Das Vorzeichen der Cayley-Menger-Formel ist falsch (V4^2 = -det/9216 [M, E]). Fuer jedes echte Simplex wird das Volumen deshalb 0, die Bedingung ist unerfuellbar. Ziel sqrt(5/96) statt sqrt(5)/96. Die Ausgabe bleibt bei L^2 = 1, danach Absturz [E]. | **Mit Netz-Code (AG2):** In s2 entfernt das feste Gesamtvolumen die Ausnahme-Instabilitaet gezielt, in s1 und s3 nicht. Abschnitt 3.2. | teilweise (Skript traegt nicht; Kern in 1 von 3 Netzen) |
| **B: Dirac exakt, Spin zwingend** | Gefrustete Twist-Phasen auf dem bipartiten Diamant sollen isolierte Dirac-Punkte erzeugen. Untergitter x Taeler soll den 4er-Spinor bilden. | Langwellige Dirac-Kegel aus Gitterbaendern gibt es (Graphen, LW-pi-Fluss, staggered fermions [L]). | Die eta-Phasen in dirac_gitter_gpu.py sind eine reine Eichung (Spektren auf 1e-14 gleich [E]). Das Spektrum ist der schlichte Diamant mit Knotenlinien. TWIST-SPIN-1: Fadenende spinlos, Fluss +1 [P]. | Fu/Kane/Mele (Spin-Bahn) gibt isolierte isotrope Kegel an X [P, E]. Dafuer braucht es aber zwei Zustaende je Knoten, also eingesetzten Spin. | traegt nicht (als Behauptung); Kern nur mit eingesetztem Spin |
| **C: Peierls und Noether** | Der Q-Ball koppelt ueber Phasen e^{iqA} auf den Kanten eichinvariant ans Maxwell-Feld. Die Ladung ist dann exakt erhalten. | Mechanismus richtig, Standard-Gittereichtheorie (Wilson, Peierls [L]). | Formeln: J mit e^{+iqA} ist nicht eichinvariant, Q hat das falsche Vorzeichen, die Kontinuitaet stimmt so nicht [E]. | Korrigiert: J_ij = 2 q W Im(phi_i^* e^{-iqA_ij} phi_j), Q_i = -2 q V Im(phi_i^* D_0 phi_i). Dann gilt dQ/dt + div J = 0 auf 2,6e-9 [E]. Brauchbar als Baustein, nicht neu. | teilweise (richtig bis auf Vorzeichen) |
| **D: Quanten-Rotor-Witness** | Ein Rotor-Fermion in Drehimpuls-Ueberlagerung soll ein Photon durch Lense-Thirring verschraenken. Das soll den PDG-Test liefern. | Gravitomagnetische Laufzeit 4 G J/(c^4 b) je Seite ist ART [L]. | Die Skriptformel G J E/(hbar c^5 b^2) hat die Einheit s/m^2. Der Effekt ist modellunabhaengig, also kein Test unseres Netzes. | Phase fuer ein Elektron: 2,6e-42 rad (1 MeV, b = 1 fm), im besten Fall 2,6e-36 (1 GeV, b = 1e-18 m) [E]. | traegt nicht |
| **E1: Schwache SU(2) aus A/B** | Die zwei Untergitter sollen ein Isospin-Dublett bilden. Die Haendigkeit soll aus dem Vorzeichen der Huepfphase kommen. | Untergitter-Pseudospin ist eine echte 2er-Struktur [L]. | Ein Pseudospin ist keine Eichsymmetrie: keine W/Z-Bosonen, keine chirale Kopplung. Die Huepfphase ist Eichung (siehe B). | keiner gefunden | traegt nicht |
| **E2: 3 Generationen = 3 Taeler** | In D Dimensionen soll das bipartite Gitter D Taeler haben, in 3D also drei Generationen. | 1D (Kette, gleiche Spruenge): 1 Knoten. 2D (Wabe): 2 Knoten. 3D FKM isotrop: genau 3 Dirac-Punkte an X [E]. | Im Skript eingetippt. Ohne Spin-Bahn hat 3D Knotenlinien, und keines von 64 Flussmustern hat Punkte [E]. 1D und 3D sitzen nur am kritischen Punkt. Taeler sind Doppler (Nielsen/Ninomiya [L]), vektoriell, gleich geladen. | Am FKM-Punkt: 3 = Zahl der X-Punkte der fcc-Zone = Raumdimension. Als Zaehlung stimmt das, als Erklaerung der Generationen ist es [H] mit bekannten Hindernissen (Chiralitaet, Doppler). | teilweise (Zaehlung mit Spin-Bahn richtig, Begruendung nicht) |
| **E3: Higgs-Massenhierarchie** | Eine Gitterverzerrung soll die drei Taeler verschieden stark luecken. Daraus soll m_e < m_mu < m_tau zwingend folgen. | Mit Spin-Bahn: Bindungsspannung lueckt die X-Punkte, Luecke = \|t0 +- t1 +- t2 +- t3\| (FKM [L, E]). | Ohne Spin-Bahn sind die "Massen" keine Luecken: Das Zonenminimum ist 3,7e-15, die Linien bleiben [E]. "Zwingend" heisst hier nur: drei Zahlen werden sortiert. | Drei Massen aus vier freien Spruengen: jede Hierarchie ist einstellbar. e:mu:tau braucht t = (1; 1,235; 1,250; 0,985), Ausloeschung auf 1,4e-4 [E]. Keine Vorhersage. | traegt nicht (als Vorhersage) |
| **F1: Nahfeld, Perihel** | Eine nichtlineare Versteifung ~1/r^3 soll die Periheldrehung erzeugen. Der Horizont soll dort liegen, wo die Wellengeschwindigkeit 0 wird. | Eine Zusatzkraft ~1/r^3 dreht Bahnen [M]. Im optischen Bild der ART (isotrope Koordinaten) geht die Lichtgeschwindigkeit am Horizont gegen 0 [L]. | alpha = 1,5 ist eingesetzt: Es gibt erste Ordnung 2 pi alpha Rs/p = 3 pi Rs/p, also genau ART [M, E]. Der "Horizont" liegt bei 1,82 Rs, nicht bei Rs [E]. Das Skript meldet -5,68 rad (Winkel-Umbruch), richtig waere +0,600 rad je Umlauf [E]. | Das Netz hat es schon: (2 + 2 gamma - beta)/3 = 0,993 bis 1,000 aus gerechneten Netzwerten (AG3). FORSCHUNGSSTAND Punkt 5 ("v3 verfehlte das Nahfeld") stimmt nicht. | traegt nicht (Skript); Aussage stimmt aus eigenem Grund |
| **F2: Kollaps, keine Singularitaet** | Eine Fundamentallaenge soll unendliche Dichte verhindern. Kleine Loecher sollen Schmelze, grosse Hohlraeume sein. | Endliche Dichte durch Mindestlaenge ist verbreitete Hypothese (Planck-Sterne, Gravasterne [L]). Arithmetik: Flaeche schlaegt Volumen bei R > 3 sigma/u [M]. | sigma und u sind gesetzt. Beide Energien wachsen schneller als M (M^2, M^3), uebersteigen also die Masse selbst. Kein Netzbezug. | SCHWARZES-LOCH [P]: Auf dem Netz geht der Takt in der Mitte vor dem Horizont auf 0, TOV-nah. Das ist der echte Netzbefund zum Kollaps. | traegt nicht (Skript) |
| **Faden-Riss (ribbon_frustration.py)** | Meson-Faeden sollen frustrierte elastische Baender sein. Sie sollen bei w^2/t > 1 reissen. | Skalierungen der Biege- und Dehnenergie (t^3 w k^2, t w^5 k^4) entsprechen der Bandliteratur [L]. | Das Kriterium laesst die Verdrehung k weg; richtig waere w^2 k/t. Alle Groessen sind gesetzt. Ein Formuebergang ist kein String-Breaking (Paarerzeugung). | keiner; das Netzgegenstueck waere sigma L > 2m (Paarbildung) | traegt nicht |

## 3. Abgleich AG1 bis AG6 (beschreibend, Karte unveraendert)

### 3.1 AG1: Z2-Flussmuster des Diamanten

- **Gerechnet [E]:**
  - kubische Zelle mit 8 Knoten und 16 Kanten, alle 512 Vorzeichenmuster
  - 64 Flussklassen nach Abzug der Windungen
  - Nullstellen auf Gittern N = 16, 32, 48, 96
- **Kein Muster gibt isolierte Knoten:**
  - Die Treffer wachsen in allen 64 Klassen wie N^1,3 bis N^1,8.
  - Die Treffermenge belegt in jeder Klasse und bei jedem N die volle Zonenbreite in allen drei Achsen (Ausdehnung 1,0).
  - Das schliesst auch quadratische Punktknoten aus. Bei ihnen gaebe die Trefferzahl allein ebenfalls D = 1,5.
  - Keine Klasse ist gelueckt, keine hat genau drei Punkte.
  - Der schlichte Diamant (alle +1) ist die Klasse mit den wenigsten Treffern (560 / 1352 / 3320, D = 1,3, Linien).
- **Abgleich:** Die Erwartung der Karte ist eingetroffen: kein natuerliches Muster ohne Spin-Bahn gibt genau 3 isolierte
  Knoten.
- **Mit Spin-Bahn (FKM, t = 4 lambda):** genau drei Nullstellen an X, Zonenminimum 7e-15 [E, wie DIAMANT-NULLSTELLEN-1].
  Spin-Bahn ist aber kein Z2-Flussmuster, sondern eine Zusatzstruktur.
- **Grenze:**
  - Nur die kubische 8er-Zelle; groessere Zellen sind nicht gezaehlt.
  - Die Einordnung "Linie gegen Flaeche" ist bei D = 1,5 bis 1,8 nicht scharf. Fuer die Kartenfrage (Punkte ja oder
    nein) reicht sie.

### 3.2 AG2: Unimodulare Bedingung an M_eff (NETZ-NICHTLINEAR-1, nn.py unveraendert importiert)

Bedingung als lineare Zwangsbedingung an die Kantengeschwindigkeiten (VORAB.md). Erster Ausnahmezug je Netz, Arm P.

| Netz, Rolle | M_eff neg. ohne / global / lokal (Start lokal) | neg. Kinetik ohne / global / lokal | wachsende Moden ohne / global / lokal |
|---|---|---|---|
| s2 Start | 128 / 128 / 117 | 0 / 0 / 0 | 0 / 0 / 0 |
| s2 neu, Hintergrund (Lesart H) | 130 / 129 / 118 (117) | **1 / 0 / 0** | **1 / 0 / 0** |
| s2 neu, gedehnt (G1) | 130 / 129 / 118 | 1 / 0 / 0 | 1 / 2 / 0 |
| s1 neu, Hintergrund | 130 / 130 / 112 (112) | 1 / **1** / 0 | 1 / **1** / 0 |
| s1 neu, gedehnt | 129 / 129 / 112 | 0 / 0 / 0 | 0 / 2 / 0 |
| s3 (2. Zug, 2-3) neu, Hintergrund | 130 / 130 / 115 (114) | 1 / **1** / 0 | 1 / **1** / 0 |
| s3 neu, gedehnt | 130 / 129 / 115 | 1 / 0 / 0 | 4 / 3 / 0 |

- **Kartenmass (negative M_eff-Richtungen):**
  - s2 faellt mit der globalen Bedingung von 130 auf 129, wie vorab per Interlacing abgeleitet (eine Bedingung, hoechstens
    eine Richtung weniger).
  - Auf 128 faellt es nicht. Auch lokal bleibt in s2 eine Richtung mehr als am Start (118 gegen 117).
  - Die Erwartung "s2 behaelt 130" trifft im Wortlaut nicht ganz (129). Das Scheiterkriterium "faellt auf 128" ist aber
    nicht eingetreten. Beschreibend: Das Kartenmass bestaetigt den Stopp nicht.
- **Dynamisch wichtiger, nicht auf der Karte [E]:**
  - In s2, Lesart H, macht die globale Bedingung die Kinetik positiv und entfernt die wachsende Mode.
  - Gegenprobe (ag2k): Von 10 000 Gauss-Bedingungen schafft das 1, von 10 000 positiven Kantengewichten keine, von 1000
    permutierten Volumenableitungen 10. Die echte Volumenbedingung ist hier also besonders: c^T Ar c = -0,0038 < 0.
  - In s1 und s3 (Lesart H) scheitert dieselbe Bedingung. Der Kern traegt also in 1 von 3 Ausnahmezuegen.
  - In Lesart G1 erzeugt die globale Bedingung sogar zwei wachsende Moden. Sie sind wie in NETZ-NICHTLINEAR-1 schon in der
    alten Zerlegung am Kreuzungspunkt da (alt_gd: 2 bis 4).
- **Lokale Lesart ist kein Befund [E]:** 128 Gauss-Bedingungen, Zufallsgewichte mit gleicher Besetzung und permutierte
  Volumenableitungen machen in 12 von 12 Versuchen je Art ebenfalls alles stabil (s2 und s3). 128 von 487 Freiheitsgraden
  festzuhalten, toetet jede einzelne Instabilitaet generisch.
- **Kontrolle:** Die TT-Mode (Gravitationswelle der Box) liegt fast im Kern beider Bedingungen (cos 0,004 global, 0,003
  lokal). Die Bedingung verbietet also nicht die Welle selbst.
- **Grenzen:** nur lineares Spektrum direkt nach dem Zug, kein Dynamiklauf mit Bedingung. Nur der erste Ausnahmezug je
  Netz. Meine Lesart "Volumen fest" als Geschwindigkeitsbedingung (VORAB.md); eine 4-Simplex-Lesart ist im Code nicht frei.

### 3.3 AG3: Periheldrehung aus gamma und beta

- Grundlage [P]: gamma = 1,000 (Laengen/Takt 0,999 bis 1,001, LICHT-ABLENKUNG-V), beta = 1,00 bis 1,02 (Variante A) bzw.
  0,95 +- 0,05 (Variante B, BETA-NETZ-V).
- P = (2 + 2 gamma - beta)/3 [E]: 0,993 bis 1,000 (A), mit gamma +- 0,001 0,9927 bis 1,0007. Variante B: 1,017 (Bereich
  1,000 bis 1,033).
- **Abgleich:** Erwartung 1,00 +- 0,02 ist fuer Variante A eingetroffen. Fuer B liegt der Mittelwert innerhalb, der
  Rand (1,033) knapp ueber der Scheitergrenze 0,03.
- Vorab ableitbar (Arithmetik aus vorhandenen Zahlen), also keine Messung.
- Grenze: PPN-Formel setzt voraus, dass alle uebrigen PPN-Parameter null sind; das ist auf dem Netz nicht gezeigt.

### 3.4 AG4: Groessenordnung des Rotor-Witness

- Delta phi = 4 G J E/(hbar c^4 b) [L]:
  - Elektron (J = hbar/2), 1 MeV, b = 1 fm: 2,6e-42 rad
  - b = Compton-Laenge: 6,9e-45 rad
  - 1 GeV, b = 1e-18 m: 2,6e-36 rad
- Gegen grob 1e-10 rad beste Phasenauflosung: 32 bzw. 34 Groessenordnungen zu klein. Im extremen Fall 1 GeV / 1e-18 m
  sind es 26. Atominterferometer (1e-3 rad je Schuss): 33 bis 41.
- **Abgleich:**
  - Erwartung (mindestens 30) bei physikalisch sinnvollem b eingetroffen. Beim gewaehlten Extremfall 26, also knapp
    darunter.
  - Scheiterkriterium (< 10) weit verfehlt.
  - Vorab abschaetzbar.
- Das Skript gibt 2,08e-35 "rad" aus; seine Formel hat die Einheit s/m^2.

### 3.5 AG5: Fadenend-Fermion auf dem Diamant

- Fadenend-Huepfer mit Fluss +1 (TWIST-SPIN-1) [P] ergibt das schlichte Diamant-Modell [M].
- Knotenlinie X-W: |Delta| hoechstens 6,7e-16 [E]. Treffer 672 und 1680 (N = 24, 48), D = 1,32: Linien [E].
- Die eta-Phasen des GPU-Skripts (1, -1, i, -i) sind exakt die Eichung k0 = (pi/4, 0, -pi/2), phi = pi/4 (Probe 1e-16)
  [E].
  - Auf dem Torus L = 4: Spektren gleich auf 1,1e-14, je 42 Nullmoden.
  - Bei L = 3 (ungerade) verschieden (0,90): Dort wirkt die Phase als verdrehter Rand, nicht als Physik.
- Komponenten: zwei (A, B), spinlos; keine 4er-Struktur ohne zusaetzliche Zustaende je Knoten.
- **Abgleich:** Erwartung (keine isolierten isotropen Kegel, Knotenlinien) eingetroffen.

### 3.6 AG6: ribbon_frustration.py

- Skript gelesen und unveraendert gerechnet [E]: "instabil" ab w = 0,1, weil w^2/t = 1 bei t = 0,01.
- Alle Eingaben gesetzt (t = 0,01, Verdrehung 3,14). Keine Netzgroesse, und das Kriterium ignoriert die Verdrehung, mit
  der die Energien rechnen.
- **Abgleich:** Erwartung "Platzhalter, keine Aussage ueber Finns Netz" eingetroffen.

## 4. Pruefung des Vermerks der Leitung (auch "Leitung irrt")

| Vermerk-Punkt | nachgerechnet | Befund |
|---|---|---|
| generationen: eingetippt, Diamant hat Knotenlinien, A/B ist Pseudospin | ja | stimmt [E]. Ergaenzung: Mit Spin-Bahn gibt es genau 3 X-Punkte; die "3" ist also nicht ganz aus der Luft, nur nicht begruendet. |
| unimodular_pachner: Dummy, Kaskade nicht gezeigt | ja | stimmt. Zusaetzlich Vorzeichenfehler und Absturz. **Der Leitung entgangen:** Mit Netz-Code entfernt die globale Volumenbedingung die Instabilitaet in s2 gezielt (1 von 3 Netzen). |
| gravity: alpha von Hand | ja | stimmt; alpha = 1,5 ist genau der ART-Wert, "Horizont" bei 1,82 Rs. |
| Teil B widerspricht TWIST-SPIN-1 / DIAMANT-NULLSTELLEN-1 | ja | stimmt; eta ist Eichung. |
| Teil D unmessbar, kein PDG-Test | ja | stimmt, 26 bis 41 Groessenordnungen. |
| Teil C korrekte Standardformeln | ja | **zu milde:** Standard im Aufbau, aber zwei Vorzeichenfehler; so geschrieben nicht eichinvariant. |

## 5. Grenzen und Regelabweichungen

- **Grenzen:**
  - AG2 ist eine lineare Momentaufnahme, kein Lauf mit Bedingung. Nur s1, s2, s3 und je der erste Ausnahmezug.
  - AG1 betrachtet nur die 8er-Zelle.
  - Literatur [L] ist aus dem Gedaechtnis und nicht abgerufen: Dittrich/Hoehn, Henneaux/Teitelboim, FKM, Nielsen/Ninomiya,
    Band-Skalierung, Gravastern/Planck-Stern, ob das Rotor-Papier existiert.
- **Regelabweichungen und Pannen:**
  - Zwei Laeufe scheiterten an eigenen Fehlern und wurden wiederholt:
    - bloch.log: Bahnschleife zu kurz bei dt = 0,002
    - ag1-ausdehnung.log: JSON-Typ
    - Beide Logs liegen bei. Die Korrekturen gingen per scp auf .neu und mv; die Pruefsummen beider Fassungen stehen in
      UPLOAD-SHA256.txt.
  - Die ersten Fassungen habe ich per scp neu angelegt (keine laufende Instanz).
  - Die acht Antigravity-Skripte liefen unveraendert in einem Unterprozess desselben Interpreters (ag_original.py), alles
    innerhalb eines kleintest-Laufs.
  - Lokal nur Datei- und Anzeigebefehle (ls, cat, sed, grep, jq zum Lesen, sha256sum, scp/ssh). Lokal kein Python, awk
    oder perl.
  - jq hat beim Lesen einmal auf 4 Stellen gerundet (smin in AG1); daraus ist keine neue Zahl entstanden.
  - Kein /tmp. Die Hintergrund-Aufrufe des Werkzeugs selbst schreiben ihre Ausgabe in den Sitzungsordner unter
    /tmp/claude-1000 (Harness, nicht von mir gewaehlt).
  - Kein grep ueber Projektordner mit Sperrinhalten. Die greps liefen nur ueber einzelne Dateien in netz-nichtlinear-1,
    diamant-nullstellen-1 und meinem Ordner, deshalb ohne Ausschlusslisten.
  - Kein Journal, kein Peerbus, kein Commit.
- **Abweichung von der Karte:** keine Erwartung geaendert. Zusaetzlich gerechnet und markiert:
  - AG2-Dynamik (Kinetik, wachsende Moden) mit Gegenproben
  - Teil C
  - Higgs-Hierarchie
  - Ausfuehrung der Originalskripte

## 6. Dateien und Pruefsummen

- Code (lokal code/, .69 /home/fmh/fmhc-physics-remote/antigravity-nachbau-1/code/):
  - ag_bloch.py: AG1, AG5, Dimensionen, Teil C, Zahlen
  - ag1_ausdehnung.py
  - ag2_unimod.py
  - ag2_kontrolle.py
  - ag2_kontrolle_lokal.py
  - ag_original.py
- Ergebnisse: lauf-69/ (bloch.json, ag1-ausdehnung.json, ag2-*.json, ag2k-*.json, ag2kl-*.json, original.json, Logs).
- PRUEFSUMMEN: lauf-69/PRUEFSUMMEN.txt (auf der .69 erzeugt, 22 Dateien). Lokal mit sha256sum -c geprueft: 22 OK.
- UPLOAD-SHA256.txt: hochgeladene Skripte, auf der .69 gegengeprueft.

## 7. Einfach gesagt

Wir haben die Ideen aus den Antigravity-Sitzungen mit unserem echten Netz-Code nachgerechnet statt mit Platzhaltern.
Fast alles, was dort als Durchbruch steht, war von Hand eingesetzt, hatte Rechen- oder Vorzeichenfehler oder ist bekanntes
Lehrbuchwissen. Eine Idee hat aber einen echten Kern: Haelt man beim Umklappen das Gesamtvolumen des Netzes fest, verschwindet
in einem von drei Testnetzen die gefaehrliche wachsende Schwingung, und zwar gezielt, nicht zufaellig. In den anderen
beiden Netzen hilft es nicht; das ist also ein Hinweis, keine Loesung.
