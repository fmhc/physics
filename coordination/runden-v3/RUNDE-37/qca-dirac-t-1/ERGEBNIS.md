# QCA-DIRAC-T-1: Ergebnis (Runde 38)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date):**
  - Start 2026-10-04 08:04:01 CEST; Code ab 08:27; Plantext ab 08:35:50; Text dieser Datei ab 08:41:03 CEST
    (Hauptteil ab 08:54:38).
  - Rauchlaeufe 06:31 bis 06:38 UTC (PLAN.md Abschnitt 7). Plan und Code eingefroren 08:39:28 CEST
    (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe auf der .69 ueber kleintest.sh, je ein ssh-Aufruf, alle rc = 0, hoechstens zwei zugleich
    (UTC = CEST − 2 h):

    | Lauf | Spur | Inhalt | Start bis Ende (UTC) | Dauer |
    |---|---|---|---|---|
    | H-BN | cpu5 | Teil B, Form N, K1 bis K5 | 06:39:37 bis 06:46:22 | 404,3 s |
    | H-BO1 | p4000b | Teil B, Form O, K1 | 06:39:39 bis 06:43:33 | 233,1 s |
    | H-BOP | p4000b | Teil B, Formen O und P, K4 und K5 | 06:44:24 bis 06:49:06 | 280,9 s |
    | H-BO2 | cpu5 | Teil B, Form O, K2 und K3 | 06:46:34 bis 06:51:51 | 315,9 s |
    | H-0 | p4000b | Teil 0: Quelle, Suchkontrolle, Konstruktionen | 06:49:17 bis 06:49:34 | 16,0 s |
    | H-A | p4000b | Teil A, Formen N, N-w0, O | 06:50:12 bis 06:51:25 | 71,7 s |
    | Auswertung, Bilder | cpu5, p4000b | auswertung.py, bild.py | 06:52:01 bis 06:52:09 | |

- **Kennzeichen:**
  - [S] an der Quelle gelesen: D'Ariano/Perinotti, PRA 90, 062106 (2014), S. 5 bis 6 aus der lokalen Kopie in
    qca-tetra-1/quelle/; kein Netzabruf
  - [L] Literatur aus dem Gedaechtnis; [L?] unsicher; [M] eigene Mathematik; [H] Hypothese; [R] im Rauchlauf gesehen
- **Art des Ergebnisses:**
  - Synthetische Rechnung an selbst gebauten Modellen und am Literaturmodell, keine Messdatenbestaetigung.
  - Alle vier Urteile waren am Schreibtisch ableitbar (PLAN.md Abschnitt 3: Beweis S2, Konstruktion S3, Eq. 37 der
    Quelle) und in den Rauchlaeufen vor dem Einfrieren zu sehen. Offen war die Statistik der Suche, und auf ihr beruhen
    die Vermerke "nur Suche".

## Ergebnis zuerst

1. **Masse ohne Symmetriebruch geht, mit 8 Zustaenden [M, numerisch bestaetigt; vorab ableitbar]:**
   - Konstruktion (a) ist die Quellform Eq. (36), E = ((n A, i m I), (i m I, n A^†)), aufgebaut auf dem T-kovarianten
     Weyl-Automaten A = (P_2 − P_2')·S_+ aus QCA-DIAMANT-4; Darstellung 2+2+2'+2' (K4).
   - Sie ist exakt unitaer (≤ 2,8e−16) und unter der vollen Tetraedergruppe T kovariant (≤ 3,3e−16).
   - Bei k = 0 liegen vier Zweifach-Cluster bei ±arcsin(m) und π ± arcsin(m), alle ohne lineare Aufspaltung
     (≤ 1,4e−15). Luecke (mein Mass, halber Abstand = |ω(0)|) arcsin(m), voller Abstand 2 arcsin(m).
   - Kruemmung |κ| = n/(9m) (1,10554; 0,35331; 0,14815 bei m = 0,1; 0,3; 0,6), in allen 400 Richtungen gleich
     (Streuung ≤ 4,7e−7). In jedem Cluster gilt 360 Grad = −1.
   - Deshalb QM-D2 und QM-D3 eingetroffen.
2. **Unter T allein ist Masse nicht der Normalfall [M; die Suche bestaetigt es]:**
   - An einer zweifachen Bandkante bei k = 0 erlaubt T den Term c k·σ, also einen Kramers-Weyl-Kegel.
   - Suche ohne Inversion (Formen N und O, 400 Starts): 42 nichttriviale Treffer, alle mit Kegeln bei k = 0
     (Geschwindigkeiten 0,0033 bis 0,43), keiner massiv.
   - Mit Inversion (Form P, Gruppe T × {1, Π}) sind 17 von 17 nichttrivialen K4-Treffern massiv:
     - 4 isotrop (drei mit Streuung ≤ 3,9e−6, einer fast trivial)
     - 13 anisotrop (Streuung 0,0029 bis 611)
   - Isotropie verlangt mehr als die Inversion: T und Inversion erlauben in zweiter Ordnung den Term b Q·σ.
3. **Teil A bewiesen [M, numerisch bestaetigt]:**
   - Mit r Kopien derselben Spinor-Irrep (T:2+2, 2+2+2+2) gibt es keinen T-kovarianten Automaten mit Spruengen, auch
     nicht mit Vor-Ort-Term.
   - Suche T:2+2:
     - Form N 0 von 200 (kleinster Defekt 4/45)
     - Form N-w0 0 von 200 (0,0974)
     - Form O 95 von 200, alle reine Vor-Ort-Automaten (Sprunggewicht ≤ 1,1e−13)
   - K1 (2+2+2+2): Form N ohne Treffer (8/45), Form O nur triviale Treffer.
   - Deshalb QM-D1 eingetroffen.
4. **Kontrollen:**
   - Quell-Dirac-Automat E^± (Eq. 36, 37): Luecke 2 arcsin(m) auf 1,2e−16, Kruemmung n/(3m) bis 1,7e−7 relativ,
     Streuung ≤ 7,7e−8, Verdoppler H, P, P' gegappt. Deshalb QM-D0 eingetroffen.
   - Suchkontrolle T:2+2': 15 von 40 Treffern, alle mit Weyl-Kegeln v = 1/3 (± 8e−7).
5. **Grenzen:**
   - In Konstruktion (a) und in 13 von 17 Form-P-Treffern bleiben an P und P' Kegel, also masselose Verdoppler.
     P und P' sind die T-invarianten Ecken der Zone.
   - Grund [M, nachtraeglich]: Die Inversion bildet P auf P' ab und schuetzt dort nichts.
   - Nur die 4 isotropen P-Treffer sind auch an P und P' quadratisch [H, ob das allgemein gilt].
   - Nicht gezeigt: Wechselwirkung, ein Higgs-artiger Mechanismus, Messbezug.

## Urteile (lauf-69/auswertung.json, Vorbedingungen erfuellt)

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil |
|---|---|---|---|
| QM-D0 | Kontrolle: L_2-Dirac-Automat der Quelle hat bei k = 0 eine Luecke 2m (bzw. nach Quelle) und isotrope Kruemmung auf 1e−3 | 85 % | eingetroffen |
| QM-D1 | [H] Teil A: 4 Zustaende, 2+2 unter T: kein nichttrivialer unitaerer Automat (Beweis oder ≥ 200 Starts ohne Treffer) | 60 % | eingetroffen (Beweis und 2 × 200 Starts) |
| QM-D2 | [H] Teil B: 8 Zustaende auf BCC, T-kovariant, Luecke bei k = 0 (massiv), tiefste Baender Spin 1/2 | 40 % | eingetroffen |
| QM-D3 | [H] Falls QM-D2: Dispersion um k = 0 isotrop (Richtungsstreuung der Kruemmung ≤ 1e−3) | 50 % | eingetroffen |

- **QM-D0:** E^+ und E^− bei m = 0,1; 0,3; 0,6, alle sechs Faelle erfuellt:
  - Unitaritaet: Koeffizienten 0, Gitter 16³ ≤ 1,2e−15
  - Cluster bei ±arcsin(m), Abweichung ≤ 1,2e−16
  - beide Cluster quadratisch
  - Streuung ≤ 7,7e−8; |κ| gegen n/(3m) ≤ 1,7e−7 relativ
- **QM-D1:** Formen N und N-w0 je 200 Starts ohne Treffer; Suchkontrolle bestanden. Vermerk mit Vor-Ort-Term (Form O):
  ebenfalls eingetroffen, 95 Treffer, alle trivial.
- **QM-D2:** 23 Kandidaten:
  - 6 Konstruktionen: a_spiegel und b_muenze_verschiebung bei drei Massen
  - 17 Suchtreffer, alle aus Form P, K4
  - alle mit Spin 1/2 in jedem Cluster
  - Vermerke: nur Suche eingetroffen; nur Suche ohne Inversionsbedingung (Formen N, O) nicht eingetroffen.
- **QM-D3:** 7 isotrope Kandidaten: a_spiegel bei allen drei m und 4 Suchtreffer aus Form P. Vermerk: nur Suchtreffer
  ebenfalls eingetroffen.
- **Urteil nach Kartenwortlaut:**
  - Fuer QM-D1 bis QM-D3 gleich dem Haupturteil.
  - QM-D0: Die Karte schreibt "Luecke 2m (bzw. nach Quelle)"; nach Quelle (2 arcsin m) eingetroffen.
  - Woertlich 2m weicht relativ um 1,7e−3, 1,6e−2 und 7,3e−2 ab (m = 0,1; 0,3; 0,6). Mit "2m" und Toleranz 1e−3
    waere QM-D0 verfehlt; das "bzw. nach Quelle" der Karte deckt die Lesung.
- **Woran QM-D2 und QM-D3 haengen:**
  - An meiner Festlegung, dass eine gepruefte Konstruktion als Kandidat zaehlt (PLAN.md 1.4).
  - Ohne sie waeren beide ueber Form P (Suche mit Inversion) ebenfalls eingetroffen.
  - Ohne Inversionsbedingung findet die Suche keinen massiven Automaten.

## Tabellen

- "Luecke" in den Tabellen ist mein Mass aus PLAN.md 1.4: der kleinste halbe Abstand eines Clusters bei k = 0 zum
  naechsten, beim Quell-Dirac-Automaten |ω(0)| = arcsin(m). Der volle Abstand der Karte ist doppelt so gross.

### Teil 0: Quell-Dirac-Automat (Eq. 24 und 36, L_2-kovariant, s = 4)

| Automat, m | halbe Luecke = arcsin(m) | |κ| gemessen | n/(3m) | Abw. rel. | Streuung | H, P, P' |
|---|---|---|---|---|---|---|
| E^±, 0,1 | 0,100167 | 3,3166 | 3,3166 | 1,7e−7 | ≤ 6,2e−9 | alle quadratisch |
| E^±, 0,3 | 0,304693 | 1,0599 | 1,0599 | 4,9e−8 | ≤ 2,3e−8 | alle quadratisch |
| E^±, 0,6 | 0,643501 | 0,44444 | 0,44444 | 1,6e−7 | ≤ 7,7e−8 | alle quadratisch |

- L_2-Kovarianz mit Pauli ⊕ Pauli exakt (0); in jedem Cluster K = −I.
- Lesepruefung Eq. (37) an 50 Zufalls-k (beschreibend): E^+ passt zu c_x c_y c_z − s_x s_y s_z, E^− zu
  c_x c_y c_z + s_x s_y s_z (≤ 4,4e−16), mit meiner Konvention e^{+ik·h}. Das ist die Zuordnung "∓" der Quelle.

### Teil A: T:2+2, s = 4 (200 Starts je Form)

| Form | dim (komplex) | Treffer | davon nichttrivial | kleinster Defekt der Nicht-Treffer | Median |
|---|---|---|---|---|---|
| N (8 Spruenge) | 16 | 0 | 0 | 4/45 = 0,08889 | 0,08889 |
| N-w0 (W(0) = I) | 16 | 0 | 0 | 0,09735 | 0,09735 |
| O (mit Vor-Ort-Term) | 20 | 95 | 0 | 0,0444 (2/45) | 0,0444 |

- Die 95 O-Treffer sind W = I ⊗ γ: Sprunggewicht ≤ 1,1e−13, voller Defekt ≤ 6,9e−29.

### Teil B: BCC, s = 8, T-kovariant (40 Starts je Fall)

Treffer: Kegel bei 0 / massiv / trivial; dim = komplexe Dimension des kovarianten Raums.

| Klasse | N: dim | N: Treffer | O: dim | O: Treffer | P: dim | P: Treffer |
|---|---|---|---|---|---|---|
| K1 = 2+2+2+2 | 64 | 0 (D_min 8/45) | 80 | 0 / 0 / 17 | | |
| K2 = 2+2+2+2' | 52 | 0 (4/45) | 62 | 6 / 0 / 10 | | |
| K3 = 2+2+2+2'' | 52 | 0 (4/45) | 62 | 3 / 0 / 10 | | |
| K4 = 2+2+2'+2' | 48 | 12 / 0 / 0 | 56 | 10 / 0 / 5 | 28 | 0 / 17 / 10 |
| K5 = 2+2+2'+2'' | 44 | 9 / 0 / 0 | 50 | 2 / 0 / 5 | 26 | 0 / 0 / 20 |

- **Formen N und O:**
  - Alle 42 nichttrivialen Treffer haben bei k = 0 vier lineare Zweifach-Cluster (Kramers-Weyl-Kegel) mit
    Geschwindigkeiten 0,0033 bis 0,43. 36 der 168 Kegel haben genau 1/3 (Muenze-mal-Verschiebung-artig).
  - Keiner hat eine Inversion (kleinster Singulaerwert des Inversionsoperators nicht ≤ 1e−8).
  - Alle sind projektiv (aus dem Treffer: C2x, C2y eindeutig implementierbar, K = −I), C3 implementierbar
    (≤ 1,6e−15).
  - In Form N ist die Summe der Chiralitaeten der vier Kegel bei Γ null (≤ 3,2e−7), in Form O bis 0,032 (Rest anderswo
    in der Zone [H], nicht gesucht).
- **Form P (Inversion Π = Kopientausch):**
  - K4: alle 17 nichttrivialen Treffer massiv, alle mit Inversion, Spin 1/2 in allen Clustern, Luecke 0,021 bis 0,47.
    Die Wirkung aus dem Treffer selbst ist bei 16 projektiv, bei einem fast trivialen mehrdeutig.
  - K5 (Π = Tausch des 2-Paars, Identitaet auf 2' und 2''): nur triviale Treffer.

### Konstruktionen (Teil 0, K4, V = (2+2') ⊕ (2+2'))

| Konstruktion | m | Klasse | Luecke | lineare Aufspaltung (max) | |κ| (Soll n/(9m)) | Streuung | Inversion | P, P' |
|---|---|---|---|---|---|---|---|---|
| a_spiegel (C = P_2 − P_2') | 0,1 | massiv | 0,10017 | 1,4e−15 | 1,10554 (1,10554) | 3,6e−8 | ja | Vierfach-Kegel |
| a_spiegel | 0,3 | massiv | 0,30469 | 8,2e−16 | 0,35331 (0,35331) | 1,4e−7 | ja | Vierfach-Kegel |
| a_spiegel | 0,6 | massiv | 0,64350 | 2,9e−16 | 0,14815 (0,14815) | 4,7e−7 | ja | Vierfach-Kegel |
| a_allgemein (α, β zufaellig) | 0,1; 0,3; 0,6 | Kegel bei 0 | | 0,25 bis 0,33 | | | nein | Zweifach-Kegel |
| b_muenze_verschiebung | 0,1; 0,3; 0,6 | massiv | arcsin(m) | ≤ 1,2e−15 | 0,106 bis 1,100 | 4,3e−3; 0,062; 0,32 | ja | Vierfach-Kegel |

- An H sind a_spiegel und b massiv (vier quadratische Zweifach-Cluster).
- Bei b haben die beiden Zweige eines Clusters verschiedene Kruemmung (etwa 0,231 und 0,336 bei m = 0,3): Spinaufspaltung
  in zweiter Ordnung, wie S5 sie zulaesst.

### Die vier isotropen Suchtreffer (Form P, K4)

| Sprunggewicht | Vor-Ort-Gewicht | Luecke | |κ| der vier Cluster | Streuung | P, P' |
|---|---|---|---|---|---|
| 6,98 | 1,02 | 0,0644 | 4,622; 4,622; 0,2207; 0,2207 | 3,0e−7 | quadratisch |
| 7,82 | 0,178 | 0,0393 | 8,249; 8,249; 0,0145; 0,0145 | 3,9e−6 | quadratisch |
| 1,38 | 6,62 | 0,4708 | 0,1275; 0,1275; 0,1536; 0,1536 | 3,9e−7 | quadratisch |
| 2,3e−6 (fast trivial) | 8,00 | 0,3469 | 1,8e−4 (alle vier) | 3,1e−4 | quadratisch |

- Je zwei Cluster haben dieselbe |κ| mit entgegengesetztem Vorzeichen: Teilchen- und Antiteilchenband wie bei Dirac.
- Die 13 anisotropen P-Treffer haben an P und P' Kegel; die 4 isotropen sind dort gegappt.
- Bild lauf-69/omega_hochsymmetrie.png zeigt als P-Beispiel den ersten massiven Treffer (anisotrop), nicht einen der
  isotropen (Selbstanzeige 9).

### 360 Grad

- Kandidaten: in jedem Cluster P V(C2x)² P = −P, P V(C3)³ P = −P und P K P = −P (Abweichung ≤ 1e−10, gerechnet
  ≤ 9,2e−16), mit den 2T-Lifts der Darstellung ("Produkt der Darstellungsmatrizen").
- Aus dem Treffer selbst (implementierende Unitaere) projektiv bei allen nichttrivialen Treffern ausser einem fast
  trivialen (mehrdeutig).

## Schreibtisch gegen Rechnung

- **S2 (keine Spruenge bei gleichen Spinor-Irreps):** 0 nichttriviale Treffer in T:2+2 (N, N-w0, O; 600 Starts) und K1
  (N, O; 80 Starts). Die Minima 4/45 (T:2+2) und 8/45 (K1) sind die Vielfachen von 2/45 (T:2, QCA-TETRA-1).
- **S3 (Konstruktion a):** Luecke, Kruemmung n/(9m) und Isotropie wie vorab abgeleitet, bis 1e−7.
  a_allgemein hat wie vorhergesagt Kramers-Weyl-Kegel.
- **S4 (Kramers-Weyl generisch unter T, Inversion erzwingt Masse):** Formen N und O: 42 von 42 nichttrivialen Treffern
  mit Kegeln bei 0. Form P: 17 von 17 nichttrivialen Treffern mit quadratischen Kanten.
- **S5 (Term b Q·σ erlaubt):** 13 von 17 Form-P-Treffern anisotrop; Konstruktion b anisotrop.
- **Nachtraeglich [M]:**
  - P ist unter T invariant (bis auf reziproke Gittervektoren). P und P' sind nicht aequivalent, denn 2P ist kein
    reziproker Gittervektor.
  - Die Inversion bildet P auf P' ab, verbietet also den linearen Term an P nicht. Das erklaert die Kegel an P und P'
    in a_spiegel, b und 13 P-Treffern.
  - Dass genau die isotropen Treffer auch P gappen, ist eine Beobachtung an 17 Treffern [H].
- **Nicht erklaert [H]:**
  - K2 und K3 haben ohne Vor-Ort-Term keine Loesung (4/45), mit ihm schon (Kegel bei 0, Vor-Ort-Gewicht 4).
  - K5 mit der gewaehlten Inversion hat nur triviale Loesungen. Eine andere Wahl von Π habe ich nicht gerechnet.

## Kontrollen

- **Positivkontrolle Quelle:** QM-D0, alle sechs Faelle; Verdoppler der Quelle gegappt, wie Eq. (37) es verlangt
  (an P ist d = ∓1).
- **Suchkontrolle T:2+2' (s = 4):** 15 von 40 Treffern, alle mit zwei Weyl-Kegeln v = 1/3 (0,3333325 bis 0,3333338),
  wie QCA-DIAMANT-4.
- **Gleichwertigkeit K2 gegen K3** (komplexe Konjugation):
  - Form N: beide ohne Treffer, gleiches Minimum 4/45 und gleicher Median 0,0904
  - Form O: 16 gegen 13 Treffer, 6 gegen 3 Kegel, je 10 triviale; Geschwindigkeiten 0,029 bis 1/3 gegen 0,067 bis 1/3
- **Codepruefung je Lauf:** Bahn-gewichteter Defekt gegen vollen Defekt ≤ 2,2e−16 relativ; Jacobi-Matrix gegen
  Differenzenquotient ≤ 5,6e−8.
- **Treffer:**
  - voller Defekt ≤ 2,5e−22 (die meisten ≤ 1e−28), Kovarianz ≤ 1,5e−15
  - Nicht-Treffer ≥ 5,0e−7 (N|K5, O|K5: langsam konvergierende Starts, vermutlich Loesungen [H]), sonst ≥ 1,5e−3
- **Trivial gegen nichttrivial:**
  - Die trivialen Treffer haben Sprunggewicht ≤ 3,7e−12, die nichttrivialen ≥ 0,088.
  - Ausnahme: zwei fast triviale P-Treffer mit 1,8e−9 und 2,3e−6, formal nichttrivial (Schwelle 1e−10).
- **Gruppen und Darstellungen:** T 12, 2T 24, Kern ±I, alle Abweichungen 0 bzw. ≤ 1,3e−15; Projektoren idempotent
  (≤ 1,1e−16).

## Kartenberichtigungen und Festlegungen (vor dem Einfrieren, PLAN.md Abschnitt 1)

1. "2+2'+2+2' oder 2+2+2'+2'" ist dieselbe Darstellung (K4).
2. QM-D0: Luecke nach Quelle 2 arcsin(m); woertlich 2m nur in erster Ordnung (Urteil nach Kartenwortlaut oben).
3. QM-D1: Haupturteil mit den Formen aus QCA-DIAMANT-4 Teil B (N, N-w0); Form O als Vermerk.
4. QM-D2: Luecke phasenfrei als kleinster halber Clusterabstand (= |ω(0)| der Quelle); massiv = alle Cluster bei k = 0
   zweifach und ohne lineare Aufspaltung; Spin 1/2 ueber die Lifts; Konstruktionen zaehlen als Kandidaten.
5. QM-D3: Kruemmung mit Richardson (h = 1e−4), Streuung Standardabweichung durch |Mittel| ueber 400 Richtungen, alle
   Zweige aller Cluster; Schwelle 1e−3 der Karte.
6. Bedeutungsabsatz: Neben "Masse braucht Symmetriebruch" gibt es "Masse braucht eine zusaetzliche Inversion oder eine
   abgestimmte Muenze" (Abschnitt Bedeutung).

## Latten (v3)

- **L1 kann scheitern:** teilweise.
  - Alle vier Ausgaenge waren am Schreibtisch ableitbar und in den Rauchlaeufen zu sehen.
  - Scheitern konnten der Nachbau der Quelle und der Beweis S2: Ein nichttrivialer T:2+2- oder K1-Treffer haette ihn
    widerlegt.
  - Ebenso die Konstruktion (Unitaritaet, Kovarianz, Isotropie) und die Erwartung S4: ein massiver Treffer ohne
    Inversion oder ein Kegel mit Inversion.
- **L2 Gegenprobe:**
  - a_allgemein gegen a_spiegel: dieselbe Familie, nur die Muenze anders; Kegel gegen Masse
  - Konstruktion b: massiv, aber anisotrop
  - Quelle als Positivkontrolle; Suchkontrolle T:2+2'; K2 gegen K3
  - Inversion am Treffer: 0 von 42 ohne, 17 von 17 mit Bedingung
  - Defekt- und Jacobi-Pruefung; Lesepruefung Eq. (37)
- **L3 Numerik:**
  - Treffer: 221 von 231 mit vollem Defekt ≤ 1e−28; Kruemmung gegen Formel ≤ 1,7e−7.
  - Streuung isotrop ≤ 3,9e−6 (ausser dem fast trivialen Treffer, 3,1e−4) gegen anisotrop ≥ 2,9e−3.
  - Lineare Terme massiver Cluster ≤ 1,1e−14 gegen ≥ 3,3e−3 bei Kegeln.
- **L4 schon bekannt:**
  - Dirac-Automat als Kopplung zweier Weyl-Automaten mit Vor-Ort-Masse [S].
  - Kramers-Weyl-Fermionen in chiralen Kristallen: Jede Kramers-Entartung an einem invarianten Punkt ist dort ein
    Weyl-Punkt (Chang et al., Nature Materials 2018) [L]. Inversion verbietet den linearen Term [L].
  - Masse koppelt entgegengesetzte Chiralitaeten gleicher Darstellung (Schur) [L]; Verdoppler (Nielsen-Ninomiya) [L].
  - Ob ein T-kovarianter massiver Quantenautomat auf BCC veroeffentlicht ist, weiss ich nicht [L?].
- **L5 Messbezug:** keiner.
  - Eine richtungsabhaengige effektive Masse (Term b Q·σ) waere bei Planck-Maschenweite unmessbar klein [H, nicht
    geprueft].
  - Masselose Verdoppler an P und P' waeren fuer jede physikalische Lesart ein Problem: zusaetzliche masselose Sorten.

## Bedeutung fuer Finns Bild

- **Belegt im Modell [M, numerisch bestaetigt]:**
  - Auf BCC (acht Tetraederrichtungen je Knoten) traegt eine voll tetraedersymmetrische Quantenregel mit 8 inneren
    Zustaenden ein massives Spin-1/2-Teilchen mit isotroper Traegheit. Die Masse koppelt zwei Kopien derselben
    Spinor-Darstellung mit entgegengesetzter Chiralitaet, wie im Dirac-Automaten der Quelle.
  - Ein Symmetriebruch ist dafuer nicht noetig. Die Alternative "Masse braucht einen Bruch wie beim Higgs-Mechanismus"
    der Karte trifft in diesem Modell nicht zu.
- **Aber nicht von selbst:**
  - Unter T allein haben generische Regeln an den Bandkanten Kramers-Weyl-Kegel, also ein Teilchen mit
    drehsinnabhaengigem Tempo.
  - Eine saubere Dirac-Masse braucht zusaetzlich eine Inversion (Paritaet) oder eine abgestimmte Muenze; Isotropie
    braucht noch mehr Struktur (die Dirac-Form der Quelle oder die vier isotropen P-Treffer).
  - In dieser Lesart verlangt Masse eine zusaetzliche Symmetrie, keinen Bruch [H].
- **Nicht gezeigt:** Verdoppler an P und P' meist masselos; Wechselwirkung; ob die isotropen P-Treffer eine eigene
  Familie bilden.
- **Vorschlag [H, nicht gerechnet]:**
  - Automaten mit voller Gruppe T_h oder O_h (Inversion, Spiegelungen) auf Isotropie und Verdoppler pruefen.
  - Die isotropen P-Treffer auf die Form Eq. (36) zurueckfuehren.
  - Masse aus spontaner Wahl eines Vor-Ort-Feldes (Higgs-artig) gegen die feste Masse vergleichen.

## Selbstanzeigen

1. **Ausgaenge vorab bekannt.** QM-D0 bis QM-D3 waren am Schreibtisch ableitbar und in Rauchlauf 1 bis 3 zu sehen
   (PLAN.md Abschnitt 7). Der Schreibtisch stand vor Rauchlauf 1; aufgeschrieben habe ich ihn erst nach den Rauchlaeufen
   (Plantext ab 08:35:50 CEST). Ein Zeitstempel fuer "vorher" fehlt also.
2. **Beweise nicht gegengelesen.** S2 (mit dem Involutions-Argument) und S3 bis S5 sind meine eigenen; kein frischer
   Leser hat sie geprueft. Die Numerik bestaetigt sie nur.
3. **Regelaenderung nach Rauchlauf 1:** Trivialitaet um "Sprunggewicht < 1e−10" ergaenzt (strenger). Ohne sie waeren
   reine Vor-Ort-Automaten als "massiv" gezaehlt worden.
4. **QM-D2 und QM-D3 als Existenzaussagen** mit Konstruktionen als Kandidaten (Festlegung 1.4, 1.5). Die Vermerke
   "nur Suche" sind ebenfalls eingetroffen, aber nur ueber die Inversionsbedingung (Form P), die ich selbst gesetzt habe.
5. **Fast triviale Treffer:** Zwei P-Treffer haben Sprunggewicht 1,8e−9 und 2,3e−6, nahe der Schwelle 1e−10. Einer davon
   zaehlt als isotrop (Streuung 3,1e−4). Ohne ihn bleiben drei isotrope Suchtreffer (≤ 3,9e−6); kein Urteil haengt an
   ihm.
6. **Laufplan:** H-A lief auf p4000b statt auf cpu5 (Zeitgewinn), Inhalt und Saat unveraendert. Nach dem Einfrieren
   keine Aenderung an Plan, Code oder Regeln; jeder Hauptlauf einmal.
7. **Werkzeuge:**
   - Lokal ausser jq, ssh, scp, sha256sum, date und grep auch mkdir, cp, ls, cat, tail, cut und Shell-Schleifen.
   - Dazu ein lokales sleep 20 und Warteschleifen "until ssh ...; do sleep 10; done", teils im Hintergrund. Ein
     Befehl mit sleep 45 wurde vom Werkzeug abgelehnt und lief nicht.
   - Auf der .69 ausserhalb des Starters: mkdir, mv, ls, sha256sum, grep, tail, uptime.
   - Kein Python ausserhalb des Starters, lokal kein Interpreter.
8. **Quelle:** S. 5 bis 6 der lokalen PDF-Kopie als Bild gelesen; kein Netzabruf (0 von 2).
9. **Bilder:**
   - In treffer_je_zerlegung.png ueberdecken sich die Titel.
   - In omega_hochsymmetrie.png ist der P-Vertreter ein anisotroper Treffer.
   - Die rote Markierung "Luecke/2" steht auch bei Kegel-Treffern; dort ist sie nur der Clusterabstand, keine Masse.
10. **Starts:** 40 je Teil-B-Fall (QCA-DIAMANT-4: 100); hoechstens 300 Iterationen mit Stillstandsabbruch. In N|K5 und
    O|K5 endeten Starts bei D ≈ 5e−7, vermutlich unvollstaendig konvergierte Loesungen; sie zaehlen als Nicht-Treffer.
11. **Gegenlesen an den JSON-Dateien (beide Richtungen):** In meiner ersten Textfassung habe ich sieben Stellen
    berichtigt:
    - Clusterabweichung beim Quell-Dirac 2e−17 statt richtig 1,2e−16
    - relative Abweichung von 2m bei m = 0,6: 7,2e−2 statt 7,3e−2
    - kleinste Kruemmung von b: 0,107 statt 0,106
    - "36 Kegel" ohne Bezug, richtig 36 von 168
    - Spin-Pruefung "≤ 1e−14" statt gemessen ≤ 9,2e−16
    - L3: Streuungsgrenze ohne den fast trivialen Treffer, lineare Terme 1,4e−15 statt 1,1e−14
    - "Luecke" ohne den Hinweis, dass mein Mass der halbe Abstand ist
    Die Urteile sind nicht betroffen. Die Verdoppler-Aussage (P und P') habe ich an beiden Punkten nachgeprueft.
12. **Zeitbox:** 120 min ab 08:04:01 CEST; Text abgeschlossen um 08:58:29 CEST (date).

## Dateien

- **Plan:** PLAN.md und PLAN.md.eingefroren-20261004-083928; Pruefsummen in EINGEFROREN-SHA256.txt.
- **Code:** code/qca_dirac.py, code/auswertung.py, code/bild.py, je mit .eingefroren-20261004-083928.
- **Rauchlaeufe:** rauch-69/ (rauch1 bis rauch3: json, log, png, rauch3_auswertung.json).
- **Hauptlaeufe:** lauf-69/haupt_{0,A,BN,BO1,BO2,BOP}.json/.log, auswertung.json/.log, bild.log,
  treffer_je_zerlegung.png, omega_hochsymmetrie.png, PRUEFSUMMEN.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde38-qca-dirac/ (code/, rauch/, lauf/).

## Einfach gesagt

Ja, ein Teilchen mit halbem Spin kann auf dem Tetraeder-Netz eine Masse bekommen, ohne dass die Symmetrie des Netzes
gebrochen wird, aber nicht von selbst. Mit acht inneren Zustaenden je Knoten haben wir eine Quanten-Spielregel gebaut,
die alle Drehungen des Tetraeders respektiert und trotzdem ein schweres Spin-1/2-Teilchen traegt: Es hat eine
Ruheenergie und ist bei kleinen Impulsen in jede Richtung gleich traege. Der Trick ist, zwei Teilchen mit
entgegengesetztem Drehsinn so zu koppeln, dass die Regel zusaetzlich spiegelsymmetrisch ist; ohne diese Spiegelung hat
fast jede zufaellige Regel an der Stelle der Masse wieder einen Kegel, also ein Teilchen, dessen Tempo von seinem
Drehsinn abhaengt. Mit nur vier Zustaenden geht es gar nicht, das haben wir bewiesen. Das ist eine Rechnung an einem
Modell, keine Messung.
