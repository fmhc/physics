# SPIN-ZUFALLSNETZ-1: Ergebnis (Runde 39, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 09:31:54 CEST.
  - Rauchlaeufe R1 bis R5: 07:47:04 bis 08:01:23 UTC (PLAN Abschnitt 9).
  - Eingefroren 10:01:19 CEST: PLAN.md.eingefroren-20261004-100119 und Code-Kopien *.eingefroren-20261004-100119;
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe: Aufrufe ab 08:01:31 UTC. Gerechnet wurde von 08:04:30 bis 08:23:21 UTC; dazwischen wartete ich auf
    den Lock des Nachbaragenten.
  - Auswertung M8 08:23:24 bis 08:23:28 UTC. Text ab 10:14:33 CEST.
- **Code nach dem Einfrieren unveraendert:** spinnetz.py 460c0af6, auswertung.py f9c22d67. Die Pruefsummen auf der
  .69 (lauf-69/PRUEFSUMMEN.txt), lokal und eingefroren stimmen ueberein. Die lokalen Kopien der Laufdateien stimmen
  mit PRUEFSUMMEN.txt ueberein (sha256sum -c).
- Alles ist synthetische Netzrechnung auf der .69 (numpy 2.4.4, scipy 1.18.0, complex128, 1 Thread). Keine
  Messdaten, keine Messdatenbestaetigung.
- **Kennzeichen:**
  - [E] hier gerechnet
  - [M] eigene Mathematik (nicht gegengelesen)
  - [F] Festlegung im Plan
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [S] an der Quelle gelesen (laut Dossier)
  - [H] Hypothese

## 1. Ergebnis zuerst

1. **Langwellig laeuft der eingesetzte Weyl-Spinor auf dem Zufallsnetz als ein einziger, sauberer Kegel [E].**
   - Ebene Wellen mit abs(k) <= 0,5 haben je eine scharfe Spektralspitze bei E = v abs(k). v liegt zwischen 0,975 und
     1,008, beim kubischen Gitter zum Vergleich zwischen 0,974 und 1,002.
   - 99,2 bis 99,8 % ihres Spektralgewichts liegen beim Energievorzeichen der richtigen Helizitaet.
   - Im untersten Fenster abs(E) <= 0,35, gewichtet mit dem langwelligen Gehalt, ist F_W = 0,991 (Schwelle 0,9).
   - Einen zweiten Kegel zeigt keine Probe.
2. **Trotzdem ist die Zustandsdichte bei E = 0 gross und flach [E].**
   - rho(0) = 0,463 +- 0,002 je Knoten und Energie bei N = 10^5 und 0,459 +- 0,004 bei N = 10^4.
   - Bei eps = 0,2 sind das 685 Kegel-Einheiten statt einer. Das kubische Gitter mit seinen 8 Dopplern hat 8,1 bis
     8,5.
   - SZ1 ist nicht eingetroffen, SZ3 ist eingetroffen.
3. **Wo die Doppler bleiben [E]:**
   - Auf dem Wuerfelgitter bilden die kurzwelligen Zustaende 7 Zusatzkegel. Auf dem Zufallsnetz liegen sie als fast
     flaches Band ueber das ganze Spektrum, auch durch E = 0. Bei N = 2000 reicht es von -2,2 bis 2,2; bei N = 10^5
     reichen einzelne Randzustaende bis etwa +-3,3 (aus der KPM-Schranke).
   - Das Band ist ausgedehnt: IPR x N = 1,7 wie bei Zufallswellen; nur an den Bandraendern sind die Zustaende
     lokalisiert.
   - Nahe null traegt jeder Zustand hoechstens 1e-3 langwelligen Anteil.
   - Der Kegel koppelt nur schwach an das Band: Der Gewichtsverlust 1 - G steigt von 0,002 bei abs(k) = 0,14 auf
     0,007 bei 0,47.
   - Dicht bei E = 0, wo nur dieser schwache Schwanz liegt, ist die Helizitaet zufaellig. Der energieaufgeloeste
     Anteil faellt dort auf 0,5 (unter 0,9 fuer abs(E) < 0,18).
4. **Die Karten-Bedeutungssaetze treffen nur halb:**
   - SZ3 "eingetroffen" heisst hier nicht, dass die Unordnung den Kegelpunkt auffuellt. Der Kegel bleibt scharf; die
     Dichte bei null kommt aus dem Doppler-Band.
   - "SZ1 verfehlt durch Doppler-Ueberschuss" stimmt fuer die Zaehlung. Der Ueberschuss ist aber kein zweiter Kegel,
     sondern ein inkohaerentes Band.
5. **Kontrolle SZ0 nach Plan-Regel nicht eingetroffen, nach Kartenwortlaut eingetroffen.**
   - Die 8 Kegel stehen fest: 16 Nullmoden bei L = 6; das Verdrillungsmittel analytisch 8,09 bis 8,41.
   - Mit nur 4 Verdrillungen lagen zwei der fuenf Zaehlwerte knapp ueber der Plan-Toleranz 8,5 (8,51 und 8,53).
     Die exakte Zaehlung an denselben 4 theta gibt bei 0,20 ebenfalls 8,52.
   - Die Toleranz war zu eng gewaehlt (Selbstanzeige 3).
   - Die uebrigen Kontrollen stimmen: KPM gegen exakt, dicht gegen ARPACK gegen Inertia, Eigenvektor-F gegen KPM-F
     (5e-6), Geometrie (Abschluss <= 1,4e-14, Euler 0).

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 7 durch code/auswertung.py; Werte in lauf-69/auswertung.json.

- Die Felder "vermerk" sind per jq nachgetragen.
- Die Maschinenfassung liegt in lauf-69/auswertung.maschine.json (sha256 326753d1, gleich der .69-Datei). Urteile und
  Werte sind bis auf die Vermerke identisch.

| Nr | Vorhersage (Karte, gekuerzt) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| SZ0 | kubisch 8 Weyl-Punkte, rho ~ E^2, Achtfaches | 85 % | **nicht eingetroffen** (Regel (i) knapp verfehlt) | **eingetroffen** | n_s(L = 46) = 8,51; 8,04; 8,53; 8,42; 8,43 (SE 0,18 bis 0,06); analytisch 8,09 bis 8,41; 16 Nullmoden; KPM gegen exakt 0,0025 |
| SZ1 | [H] Zufallsnetz: ein Kegel innerhalb Faktor 1,5, kein Achtfach-Ueberschuss | 35 % | **nicht eingetroffen** | nicht eingetroffen | n_s(N = 10^5) = 685; 438; 304; 223; 171 bei eps = 0,20 bis 0,40; N = 10^4 gleich (683 bis 171) |
| SZ2 | [H] Helizitaetsanteil >= 0,9 im untersten Fenster | 45 % | **eingetroffen** | Lesart abhaengig, siehe 2.1 | F_W = 0,9911 (4 Saaten 0,9909 bis 0,9912); G_richtig 0,992 bis 0,998; kubisch 1,0000 |
| SZ3 | rho(0) > 0 (Unordnungs-Weyl-Uebergang) | 50 % | **eingetroffen** | rho(0) > 0 eingetroffen; Zusatz "Unordnungs-Weyl-Uebergang" nicht gestuetzt | rho0 = 0,463 +- 0,002 (10^5), 0,459 +- 0,004 (10^4); rho_K = 4,2e-5; Verhaeltnis 1,1e4 |

### 2.1 Lesarten

- **SZ0:**
  - Plan-Regel (i) verlangt alle fuenf n_s in [7,5; 8,5]. Bei 0,20 (8,509) und 0,30 (8,530) ist das knapp verfehlt.
  - Ursache ist die Stichprobe von nur 4 Verdrillungen: Die exakte Zaehlung an denselben 4 theta gibt 8,52; 8,10;
    8,34; 8,34; 8,38. Die analytische Gitterkorrektur betraegt + 0,3 eps^2 und nimmt bei 0,40 schon 0,41 der Toleranz
    0,5 weg.
  - Nach Kartenwortlaut (8 Weyl-Punkte, Achtfaches, rho ~ E^2) ist SZ0 eingetroffen.
- **SZ2:**
  - Die Plan-Lesart gewichtet jeden Zustand im Fenster mit seinem Ebene-Wellen-Gehalt (abs(k) <= 0,5, m != 0). Das
    ergibt F_W = 0,991, getragen von der Kegelspitze bei abs(E) ~ 0,29.
  - Der Kartenwortlaut spricht von "langwelligen Eigenzustaenden im untersten Energiefenster". Die Zustaende
    unmittelbar bei E = 0 sind aber nicht langwellig: In K4 haben die 20 tiefsten einen Gehalt <= 9,8e-4.
  - Ihr kleiner langwelliger Anteil hat keine definierte Helizitaet. Energieaufgeloest faellt der Anteil fuer
    abs(E) < 0,18 unter 0,9 und erreicht bei E = 0 genau 0,5 (bild-helizitaet.png links).
  - Lesart "die langwelligen Zustaende" (Kegel): eingetroffen. Lesart "die energetisch untersten Zustaende": nicht
    eingetroffen; dort ist nichts Langwelliges mit Helizitaet.
- **SZ3:**
  - Die Plan-Regel ist mit Abstand erfuellt: rho0/rho_K = 1,1e4, rund 210 SE, N-Verhaeltnis 0,99.
  - Die Deutung der Karte (Unordnungs-Weyl-Uebergang, instabiler Weyl-Ast) zeigen die Spektralfunktionen nicht. Die
    Kegelspitzen sind scharf, und die Dichte bei null kommt aus Zustaenden ohne langwelligen Anteil.

### 2.2 Agenten-Vorhersagen (PLAN Abschnitt 10; nach den Rauchlaeufen R1 und R3 geschrieben, also nicht unabhaengig)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (95 %) | SZ0 eingetroffen, n_s 8,0 bis 8,45 | **nicht eingetroffen** (8,51 und 8,53 bei 0,20 und 0,30) |
| A2 (95 %) | SZ1 nicht eingetroffen, n_s(0,2) > 300 bei N = 10^5 | **eingetroffen** (685) |
| A3 (85 %) | SZ3 eingetroffen, rho0 in [0,35; 0,55] bei beiden N | **eingetroffen** (0,463; 0,459) |
| A4 (80 %) | SZ2 eingetroffen, F_W >= 0,97 | **eingetroffen** (0,991) |
| A5 (75 %) | K4: F aus Eigenvektoren gleich F aus KPM auf 0,02 | **eingetroffen** (5e-6) |
| A6 (80 %) | K4: die 20 tiefsten Zustaende mit Gehalt < 0,01 | **eingetroffen** (<= 9,8e-4) |
| A7 (50 %) | K4: Zustaende nahe null staerker lokalisiert (IPR >= 3 x Median) | **nicht eingetroffen** (1,75 gegen 1,73) |
| A8 (60 %) | N = 10^5: v_Spitze aller 7 Richtungen in [0,95; 1,00], Spanne <= 0,03 | **nicht eingetroffen** ((1,1,0) 1,008 bei Rasterunsicherheit +-0,013; Spanne 0,033) |
| A9 (40 %) | N = 10^5: rho(E) gegen rho(-E) um > 5 % verschieden | **nicht eingetroffen** (max 2,2 %, im Rauschen) |

## 3. Tabellen

### 3.1 Zahl der Kegel n_s(eps) = n(abs(E) < eps) 3 pi^2/eps^3 (KPM, verdrillungsgemittelt) [E]

| eps | kubisch L = 46 (16 Proben) | kubisch analytisch (200 theta) | Zufallsnetz N = 10^4 (4 Saaten, 32 Proben) | Zufallsnetz N = 10^5 (2 Saaten, 16 Proben) |
|---|---|---|---|---|
| 0,20 | 8,51 +- 0,18 | 8,09 | 683,1 +- 3,1 | 685,3 +- 1,3 |
| 0,25 | 8,04 +- 0,13 | 8,14 | 437,2 +- 1,6 | 438,3 +- 0,7 |
| 0,30 | 8,53 +- 0,10 | 8,21 | 303,4 +- 0,9 | 304,0 +- 0,4 |
| 0,35 | 8,42 +- 0,07 | 8,31 | 222,7 +- 0,6 | 223,2 +- 0,2 |
| 0,40 | 8,43 +- 0,07 | 8,41 | 170,5 +- 0,5 | 170,8 +- 0,2 |

- Die Zaehlung je Knoten bei N = 10^5 ist n = 0,1852; 0,2313; 0,2772; 0,3231; 0,3692. Sie steigt linear in eps, also
  ist die Dichte konstant. Ein Kegel gaebe eps^3/(3 pi^2) = 2,7e-4 bei 0,2.
- Bild: lauf-69/bild-zustandsdichte.png. Links rho(E) mit den Kontinuumslinien fuer 1 und 8 Kegel, rechts n_s(eps).

### 3.2 Zustandsdichte bei null (SZ3) [E]

| Groesse | N = 10^5 | N = 10^4 |
|---|---|---|
| rho0 = n(0,05)/0,1 | 0,4631 +- 0,0022 | 0,4587 +- 0,0036 |
| Fit rho(E) = rho0 + c E^2 auf [0,05; 0,30]: rho0 | 0,4641 | 0,4638 |
| Fit: c (ein Kegel haette + 0,0507) | -0,064 | -0,062 |

- Die Dichte steigt nicht wie E^2 an. Sie ist flach und faellt leicht bis abs(E) ~ 0,3.
- K4 (dicht, N = 2000, volles Spektrum):
  - Die Dichte liegt bei 0,47 nahe null, mit einem flachen Minimum von 0,45 bei abs(E) ~ 0,3 und Maxima von 0,62 bis
    0,65 bei abs(E) ~ 1,2 bis 1,4. Die Bandraender liegen bei +-2,22.
  - Bild: lauf-69/bild-k4-spektrum.png.

### 3.3 Spektralfunktionen ebener Wellen [E]

**N = 10^4, alle Wellen mit abs(k) <= 0,5 (19 k x 2 Helizitaeten je Saat), M = 2048:**

| Saat | F_W (Fenster 0,35) | G_richtig Mittel | v_Spitze Median |
|---|---|---|---|
| 1 | 0,99091 | 0,9945 | 0,982 |
| 2 | 0,99117 | 0,9946 | 0,982 |
| 3 | 0,99109 | 0,9946 | 0,982 |
| 4 | 0,99106 | 0,9945 | 0,982 |
| gepoolt | 0,99106 (51,09 richtig, 0,461 falsch, 152 Wellen) | 0,9945 (min 0,9923) | |

**N = 10^5, Saat 1, Auswahl, M = 1024** (v-Rasterunsicherheit +-0,0025/abs(k)):

| m | abs(k) | v_Spitze Netz | v_Spitze kubisch L = 46 | G_richtig Netz | Gewicht im Fenster richtig / falsch |
|---|---|---|---|---|---|
| (1,0,0) | 0,136 | 0,989 | 0,980 | 0,998 | 0,997 / 0,0015 |
| (1,1,0) | 0,193 | 1,008 | 0,999 | 0,997 | 0,994 / 0,0019 |
| (1,1,1) | 0,237 | 0,990 | 1,002 | 0,997 | 0,990 / 0,0022 |
| (2,0,0) | 0,272 | 0,993 | 0,984 | 0,996 | 0,983 / 0,0024 |
| (2,2,0) | 0,385 | 0,987 | 0,991 | 0,994 | 0,086 / 0,0031 (Spitze ausserhalb) |
| (3,0,0) | 0,407 | 0,982 | 0,974 | 0,994 | 0,049 / 0,0033 (Spitze ausserhalb) |
| (2,2,2) | 0,472 | 0,975 | 0,987 | 0,993 | 0,026 / 0,0036 (Spitze ausserhalb) |

- F_W der Auswahl bei N = 10^5: 0,9956. Das kubische Gitter hat F_W = 1,0000 (L = 22) und G = 1,0000 (L = 46); dort
  sind die ebenen Wellen exakte Eigenzustaende.
- Isotropie: Bei aehnlichem abs(k) stimmen Achsen, Flaechen- und Raumdiagonalen auf 0,5 bis 2 % ueberein. Das liegt
  innerhalb der Rasterunsicherheit. Netz und Wuerfelgitter haben dieselbe Groessenordnung der Kruemmung (v ~ 0,98 bei
  abs(k) ~ 0,4).
- Bild: lauf-69/bild-helizitaet.png. Links der energieaufgeloeste Helizitaetsanteil, rechts die Spektralfunktion der
  ersten zwei Schalen mit Spitzen bei abs(k).

## 4. Kontrollen

- **Geometrie** (6 Hauptnetze, dazu Rauch- und Kontrollnetze):
  - Euler V - E + F - T = 0. Jedes Dreieck liegt in genau zwei Tetraedern; jede Umkugel liegt im Saum.
  - Abschluss sum_j A_ij n_ij: <= 3,7e-15 (N = 10^4) und <= 1,0e-14 (N = 10^5; Rauchnetz 1,4e-14).
  - Volumensumme <= 2,2e-16. A_ij > 0 ueberall, Bildversaetze eindeutig.
  - Mittlerer Grad 15,505 bis 15,581 (Literatur fuer Poisson-Delaunay 3D etwa 15,54 [L]).
  - sum_i M_i = L^3 * 1 auf 1e-15 [E]; Herleitung in PLAN Abschnitt 3 [M].
  - Spurfreie Schwankung von M_i/V_i: rms 0,25.
  - Kein Netz ist in der Auswertung als fehlerhaft markiert.
- **Operator:**
  - hermitesch auf Maschinengenauigkeit
  - Nullmoden-Residuum bei theta = 0 unter 1e-10 (Pruefung in auswertung.py)
  - Kramers-Paare (dicht, N = 1000) auf 2,5e-14, genau 2 Nullmoden
  - Spur H^3 = 0 auf 1e-16, wie in D6 vorhergesagt
- **K1** (kubisch dicht gegen analytisch, L = 6 und 7, mit und ohne Verdrillung): <= 2,0e-14. Nullmoden: 16 bei
  L = 6, 2 bei L = 7.
- **K2** (Zufallsnetz N = 1000, Saat 999):
  - ARPACK (Shift-Invert) gegen dicht: 2,5e-15.
  - Inertia (LDL^H) zaehlt 328 Zustaende in abs(E) < 0,35, dicht ebenfalls 328.
  - KPM gegen dicht je theta: max 0,033 je Knoten bei 2 Vektoren je theta (Stichprobe).
- **K3** (kubisch L = 12, KPM gegen analytisch je theta): 0,022 je Knoten.
- **K4** (Zufallsnetz N = 2000, Saat 998, alle Eigenpaare dicht):
  - F aus Eigenvektoren 0,98407 gegen KPM 0,98408 (Fenster 0,6, Abstand 5e-6). Das bestaetigt die Identitaet aus
    PLAN Abschnitt 7 numerisch.
  - Ebene-Wellen-Gehalt im Fenster: 14,351 gegen 14,365.
- **Kubisch L = 46:** KPM gegen analytisch je theta max 0,0025 je Knoten (Schwelle 0,01).
- **Waechter:** abs(mu_n) <= 1 in allen KPM-Laeufen (max 1,000000).
- **Reproduktion:** M1 (Hauptlauf) gibt K1 bis K4 wie R5 (Rauch, gleiche Codefassung), gleich bis auf die letzte
  Stelle (ARPACK-Startvektor: 2,498e-15 gegen 2,491e-15).

## 5. Latten (v3)

- **L1 (kann scheitern):** ja.
  - SZ1 konnte eintreffen und ist gescheitert.
  - SZ2 konnte an der Mischung mit dem Doppler-Band scheitern. Bei G ~ 0,5 waere es gescheitert; nahe E = 0 ist die
    Helizitaet tatsaechlich zufaellig.
  - Von meinen eigenen Vorhersagen sind A1, A7, A8 und A9 gescheitert.
- **L2 (Gegenprobe):**
  - dieselbe Funktion matrix() auf dem kubischen Gitter (8 Kegel)
  - vier Verfahren fuer dieselben Zahlen: dicht, ARPACK, Inertia, KPM
  - Eigenvektor-F gegen KPM-F
  - zwei N (10^4 und 10^5), vier bzw. zwei Saaten, Mittel ueber Randbedingungen
- **L3 (Numerik):**
  - Geometrie und Operator 1e-14
  - KPM-Zaehlung gegen exakt 2e-3 bis 3e-2 je Knoten (stichprobenbegrenzt)
  - Spektral-F 5e-6
  - v_Spitze nur auf das Energieraster genau (+-0,0025/abs(k))
- **L4 (schon bekannt):**
  - Zufallsgitter-Fermionen: Christ/Friedberg/Lee 1982 [L]. Griffin/Kieu 1992: "the doublers suppressed in the free
    field case are revived [...] unless gauge interactions are implemented in a non-invariant way" [S Abstract, laut
    Dossier]. Kieu u. a. 1994, Cohen 2006 [S Abstract, laut Dossier].
  - Unser langwelliger Befund (ein Kegel, keine kohaerenten Doppler) passt zu "suppressed in the free field case".
  - Eine flache, ausgedehnte Nullenergie-Dichte rauer Zustaende kenne ich aus der Literatur nicht [L?]. Den Titel
    "Random Lattice Fermions at E=0 without Doubling" (Hatsugai/Wen/Kohmoto 1996, laut Dossier nur Titel) habe ich
    nicht gelesen. Er koennte dazu passen oder widersprechen; vor einer Folgekarte lesen.
  - Weyl-Halbmetalle mit Unordnung: Schwache Unordnung ist fuer den 3D-Kegel irrelevant. Ein endliches rho(0) gibt es
    erst bei starker Unordnung oder durch seltene Gebiete [L]. Hier stammt rho(0) aus dem Doppler-Band, nicht aus dem
    Kegel.
- **L5 (Messbezug):** keiner direkt.
  - Die Rechnung ist ein freies Modell auf einem gedachten Netz.
  - Messbar waere erst eine Folge, etwa eine Neutrino-Dispersion v(k) < 1 aus der Kegelkruemmung (1 - v ~ 1-2 % bei
    abs(k) ~ 0,4 in Netzeinheiten). Das gaebe nur eine Schranke an die Netzweite wie in REGGE-WELLE-1 [H].

## 6. Selbstanzeigen

1. **Vorwissen aus Rauchlaeufen:**
   - R1 (N = 1000, dicht) zeigte die flache Nullenergie-Dichte, R3 (N = 10^4) F_W = 0,991. SZ1, SZ2 und SZ3 waren
     damit vor dem Hauptlauf absehbar (PLAN Abschnitt 9).
   - Meine Vorhersagen A1 bis A9 sind nach R1 und R3 geschrieben, A5 bis A7 vor dem Lesen von R5 (K4).
2. **Nach R1 festgelegt (vor dem Einfrieren):** die SZ3-Regel und der Weg ueber Spektralprojektionen fuer SZ2. Die
   Fenster standen vorher im Code (sha 75d4eb57). Eine Schwelle habe ich nach keinem Rauchlauf geaendert.
3. **SZ0-Toleranz zu eng (Planfehler):**
   - Ich kannte die Gitterkorrektur (8,38 bei 0,40, PLAN Abschnitt 4) und habe trotzdem +-0,5 aus dem Dossier
     uebernommen. Das Rauschen von nur 4 Verdrillungen habe ich nicht eingerechnet.
   - Damit ist die Kontrolle nach Plan "nicht eingetroffen", obwohl der Code die 8 Kegel nachweislich richtig
     zaehlt (exakt je theta, 16 Nullmoden).
   - Eine Regel mit dem analytischen Verdrillungsmittel als Soll und 3 SE haette bestanden; sie stand aber nicht im
     Plan. Das Urteil bleibt.
4. **Eigenpaare bei N = 10^4 entfallen:** R2 haengte 6,5 min in ARPACK (Speicherspitze 1,5 GB). Ich habe die eigene
   Unit gestoppt. Die Eigenzustands-Ebene deckt K4 ab (N = 2000, dicht).
5. **Eigene Units und Aufrufe beendet:**
   - R2 und R4 per systemctl --user stop. R4 war nach dem KPM-Teil, den ich fuer die Laufzeit brauchte, im
     Spektralteil.
   - Zwei wartende eigene Aufrufe habe ich per kill der eigenen flock-PID beendet:
     - M4 wurde als M45 neu gestartet, Saaten 1 bis 4 in einem Lauf statt M4 und M5. Das spart einen Lock-Durchgang;
       Saaten, Optionen und Auswertung bleiben gleich.
     - M1 lag in der Schlange von p4000b und wurde auf cpu5 neu gestartet.
   - Fremde Prozesse habe ich nicht angefasst.
6. **M7 ohne Spektralteil, Spektral-M = 1024 bei N = 10^5:** vor dem Einfrieren festgelegt (Laufzeit). Die v_Spitze
   bei N = 10^5 hat deshalb eine Rasterunsicherheit bis +-2 % bei abs(k) = 0,14.
7. **Breite nicht gemessen:** Die Breite der Kegelspitze Gamma(k) habe ich nicht ausgewertet, nur Lage, Gewicht und
   Vorzeichenanteil. Die Aussage "schwache Kopplung" stuetzt sich auf 1 - G und die Schwanzgewichte.
8. **Hintergrundaufrufe:** Das Werkzeug legt je Hintergrundaufruf eine (leere) Ausgabedatei im Sitzungsordner
   /tmp/claude-1000/.../tasks/ an. Alle Ausgaben habe ich in den Kartenordner umgeleitet. Ich selbst habe dort nichts
   abgelegt.
9. **Lokal:**
   - kein python, awk oder perl
   - benutzt: jq, sed, grep, sha256sum, date, ssh, scp
   - zum Lesen und Ablegen: cat, head, tail, ls, stat, cut, tr, cp, mv, mkdir
   - sleep nur in Warteschleifen
10. **Auf der .69 ausserhalb des Starters:**
    - kein Python
    - mkdir, mv, cat (Starter gelesen), ls, sha256sum, ps
    - systemctl --user list-units, stop und is-active fuer eigene Units, kill fuer eigene PIDs
11. **Ungeprueft:** D5 (Kramers), D6 (Spur H^3 = 0), der Divergenzsatz fuer sum_i M_i und die Identitaet
    F = Spektralprojektion sind eigene Mathematik. Numerisch sind sie bestaetigt, gegengelesen nicht.
12. **Spuren:** cpu5 und p4000b, nie mehr als zwei eigene Laeufe zugleich. Wartende eigene Aufrufe lagen zeitweise
    zusaetzlich in der Lock-Schlange.

## 7. Bedeutung

- **Antwort auf die Kartenfrage:**
  - Ein eingesetzter Weyl-Spinor laeuft auf dem ungeordneten 3D-Netz langwellig sauber: ein Kegel, v ~ 0,98 bis 1,
    Helizitaet zu ueber 99 %.
  - Die Doppler kehren nicht als Kegel zurueck. Sie verschwinden aber auch nicht: Die rauen Zustaende fuellen die
    Energie null mit einer grossen, flachen, ausgedehnten Dichte.
- **Bedeutungssaetze der Karte, einzeln:**
  - "SZ1 und SZ2 treffen ein": trifft nicht zu, weil SZ1 gescheitert ist.
  - "SZ1 verfehlt durch Doppler-Ueberschuss": In der Zaehlung stimmt das. Die Folgerung "Dann braucht es
    Zusatzglieder (Wilson-artig) oder eine andere Bauweise" gilt fuer alles, was die Nullenergie-Dichte sieht:
    - Vakuum und Dirac-See, Waerme, Wechselwirkungen
    - nach Griffin/Kieu besonders Eichfelder [S Abstract, laut Dossier]
    - Fuer ein einzelnes freies langwelliges Teilchen ist sie nicht noetig.
  - "SZ3 trifft ein: Die Unordnung fuellt den Kegelpunkt auf; masseloser Weyl-Ast instabil": nicht gestuetzt.
    rho(0) > 0 stimmt, der Kegel bleibt aber scharf. Die Dichte stammt aus dem Doppler-Band.
  - Zur Hypothese "Zufallsnetz mit Zahl = Volumen traegt Schwerkraft aus Materie und Fermionen zugleich": Der
    langwellige Teil spricht dafuer. Das raue Band wuerde aber in jede induzierte Groesse (etwa INDUZIERT-DICHTE)
    mit seiner vollen Dichte eingehen. Ungeprueft [H].
- **Mechanismus [H, Zahlen E]:**
  - Langwellig sieht eine glatte Welle nur den gemittelten Geschwindigkeitstensor, und der ist exakt isotrop
    (sum_i M_i = L^3 * 1).
  - An raue Zustaende koppelt sie ueber die lokale Schwankung des Tensors (rms 0,25), proportional zu abs(k).
  - Nach der Goldenen Regel waere der Gewichtsverlust etwa proportional zu k^2. Gemessen ist 1 - G = 0,002 bei 0,14
    und 0,007 bei 0,47 (N = 10^5), also schwaecher als k^2. Ein Skalierungstest war nicht geplant.
- **Naechste Karten [H]:**
  - (a) Laplace-Zusatzglied r L (x) 1 (Wilson-artig, fuer einen einzelnen Weyl-Spinor erlaubt, bricht nur E -> -E):
    Schiebt es das raue Band aus E = 0, ohne den Kegel zu stoeren?
  - (b) Zufaellige U(1)-Phasen auf den Kanten: Koppelt der Kegel dann staerker an das Band (Griffin/Kieu)?
  - (c) Breite der Kegelspitze Gamma(k) bei groesserem M, um den Kopplungsexponenten zu messen.
  - Vorher Hatsugai/Wen/Kohmoto 1996 am Volltext lesen.

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-100119, EINGEFROREN-SHA256.txt
- code/: spinnetz.py, auswertung.py (je mit Kopie *.eingefroren-20261004-100119)
- rauch-69/: Logs und JSONs von R1 bis R5 (kontrolle, netz1e4, netz1e4b, netz1e5, kontrolle2)
- lauf-69/:
  - Logs M1, M2, M3, M45, M6, M7, M8 sowie M1-abgebrochen-wartend.log und M4-abgebrochen-wartend.log
  - kontrolle.json, gitter46.json, gitter22.json, netz1e4-a.json (Saaten 1 bis 4), netz1e5-1.json, netz1e5-2.json
  - auswertung.json (mit Vermerken), auswertung.maschine.json, PRUEFSUMMEN.txt (.69)
  - Bilder: bild-zustandsdichte.png, bild-helizitaet.png, bild-k4-spektrum.png
- Auf der .69: /home/fmh/fmhc-physics-remote/runde39-spin-zufall/ (code/, rauch/, lauf/)

## 9. Einfach gesagt

Wir haben ein Teilchen mit halbem Spin, so etwas wie ein Neutrino, auf einem ganz unregelmaessigen Netz aus
Zufallspunkten laufen lassen; die Spinrichtung haben wir von Hand an die Netzlinien geheftet. Lange Wellen laufen
sauber als ein einziges Teilchen mit fast genau der eingestellten Geschwindigkeit, und ihre Drehrichtung stimmt in
ueber 99 von 100 Faellen. Kopien des Teilchens wie auf dem regelmaessigen Wuerfelgitter, wo es gleich acht Stueck gibt,
tauchen nicht auf. Ganz weg sind sie aber nicht: Das Netz hat dafuer einen grossen Vorrat an kurzwelligen, zitternden
Zustaenden bei allen Energien, auch bei null, der mit dem Teilchen kaum spricht. Ob dieses Rauschen stoert, haengt
davon ab, ob das Teilchen mit etwas anderem wechselwirkt; das ist der naechste Test, und alles hier ist Rechnung auf
einem gedachten Netz, keine Messung.
