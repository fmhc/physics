# STILLE-AUF-GITTER: Ergebnis (Code-Agent, Runde 23, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-02 22:35:19 CEST (date).
- Plan eingefroren 22:56:18 CEST (PLAN.md.eingefroren-20261002-225618), nach dem Rauchlauf und vor jedem echten Lauf.
  - Code: code/stille_gitter.py, sha256 ab42bce160910308d05697410a70df0571fe0e05863e9081b4fd3f36be7ba1d6 (lokal = .69,
    schreibgeschuetzt).
  - Auswertung: code/auswertung.py, sha256 3a12d848fb76f11ae472aa0e1898a5b993ca628826699d6f50ab3ae245121039.
    Geschrieben 22:57:43 CEST, nach dem Einfrieren und vor dem Lesen des ersten Hauptergebnisses.
- **Hauptlaeufe** (zehn, A und B bei h = 0,5 / 0,4 / 0,3 / 0,25 / 0,2): .69, 20:56:26 bis 21:01:12 UTC (22:56 bis 23:01
  CEST). Alle rc = 0, je 18 Punkte, nichts fehlt.
- **h = 0,15** (nach Plan optional; nach den zehn Laeufen waren noch ~90 min Zeitbox frei):
  - A015 21:01:25 bis 21:06:58 UTC, B015 21:01:25 bis 21:09:31 UTC (8 min 7 s), beide mit `--n1 3 --ohne-p2`
  - getrennte PML-Probe P2 im Modus punkt: A015-P2 21:07:04 bis 21:07:39, B015-P2 21:09:41 bis 21:10:40 UTC
  - Doppelrechnung lief in beiden Scans mit. Boden vollstaendig, also gewertet.
  - Alle rc = 0.
- Auswertung mechanisch mit auswertung.py auf der .69 (kleintest.sh, cpu3): 21:10:45 UTC. Tabellen lokal mit jq aus lauf-69/.
- Ergebnis geschrieben ab 23:05:17 CEST (Entwurf), Fassung ab 23:13:08 CEST (beides date); Ende in der letzten Zeile.
- Explorativ (v3). Deutungen [H, Modell M1, 2D, Sprosse n = 7, Q-Ball auf einem Gitterpunkt, nur A1-Sektor].

## Ergebnis zuerst

1. **Die stille Mode bleibt auf dem Quadratgitter nicht exakt still, aber fast.**
   - Restbreite am Minimum:
     - Stern A (5 Punkte): 2,06e-4 (h = 0,5) bis 1,38e-6 (h = 0,15), **Gamma_min ~ h^(4,15 +- 0,03)**
     - Stern B (isotroper 9-Punkt-Stern): 3,30e-7 bis 1,39e-11, **Gamma_min ~ h^(8,36 +- 0,07)**
   - Die oertlichen Exponenten fallen zu kleinem h auf 4,05 und 8,09 (zwischen h = 0,2 und 0,15).
   - SG1 und SG2 sind eingetroffen.
2. **Der Rest geht fast ganz in den cos 4theta-Kanal** (Fluss am Minimum auf r = 20):
   - Stern A: 0,806 (h = 0,5) bis 0,999 (h = 0,15). Stern B: 1,000.
   - SG3 ist eingetroffen, bei h = 0,5 nur knapp. Auf dem Kontrollkreis r = 22,5 sind es dort 0,757.
   - Der kleine l = 0-Anteil auf dem Messkreis waechst wie r^2 und wie h^4.
     - [H, nachtraeglich] Er passt quantitativ zur anisotropen Gitter-Dispersion: Eine reine l = 4-Welle sammelt vom
       Zentrum an die Phase 0,0905 h^2 r cos 4theta.
3. **Die Sprosse wandert wie h^2 nach oben**: q = 2,19 (A) und 2,22 (B); c = 3,6e-3 und 4,9e-3.
   - Die h^2-Extrapolation liegt 2,5e-6 (A) bzw. 4,5e-6 (B) unter 0,529266. SG0 ist eingetroffen, K0 bestanden.
   - [H, nachtraeglich] Das Verhaeltnis der Verschiebungen (1,34) entspricht dem der isotropen h^2-Fehlerterme
     (h^2/12 gegen h^2/16, also 4/3).
4. **Der Vorfaktor folgt einer einfachen Regel [H].**
   - Gamma_B/Gamma_A trifft die im Plan notierte Schaetzung (h^2 K^2/30)^2, mit K^2 = (omega + rho)^2 - 1 = 4,216.
   - Messung geteilt durch Schaetzung: 1,30 (h = 0,5), 1,16, 1,07, 1,04, 1,015, 1,003 (h = 0,15; mit den direkten
     Werten 0,997).
   - Lesart: Die Breite ist das Quadrat des cos 4theta-Anteils des Sterns bei der Abstrahl-Wellenzahl.
5. **Rechenboden** (Doppelrechnung plus PML-Probe): 1e-14 bis 5e-9, relativ zur Breite hoechstens 7e-4.
   - Alle zwoelf Breiten liegen mindestens 1400-fach darueber.
   - Bedeutung nach Karte [H, 2D, M1]: Die Stille misst die Anisotropie des Raums; der Breiten-Exponent ist zweimal die
     Anisotropie-Ordnung.
   - Das ist ein Fall des bekannten alpha^-2-Gesetzes fuer gestoerte BICs (L4).

## Vorab gegen Ausgang

Mechanisch nach PLAN.md Abschnitt 5 (auswertung.py), alle zwoelf (Stern, h). Mit nur den zehn Hauptlaeufen (ohne h = 0,15)
gilt dasselbe: p_A = 4,19 +- 0,03, p_B = 8,45 +- 0,07, q = 2,22 und 2,26, Extrapolation -4,4e-6 und -7,5e-6.

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang |
|---|---|---|---|
| SG0 | omega_r^2(h) = omega_r^2(0) + c h^2 fuer beide Sterne (Exponent 2 +- 0,4); Extrapolation innerhalb +-3e-5 um 0,529266 | 70 % | **eingetroffen**: q_A = 2,188 +- 0,022, q_B = 2,224 +- 0,027; Extrapolation (h^2, h <= 0,3) 0,5292635 (-2,5e-6) und 0,5292615 (-4,5e-6) |
| SG1 | Stern A: p = 4 +- 0,8 aus mindestens drei h ueber dem Rechenboden | 55 % | **eingetroffen**: p = 4,151 +- 0,026 aus sechs h, alle ueber dem Boden |
| SG2 | Stern B: p = 8 +- 2 oder unter dem Boden fuer h <= 0,3; und Gamma_min(B) < Gamma_min(A)/30 bei h = 0,3 | 50 % | **eingetroffen** ueber (a): p_B = 8,357 +- 0,068 aus sechs h; (c): Verhaeltnis 1/5848 |
| SG3 | Stern A: am Minimum >= 80 % des Flusses in cos 4theta | 60 % | **eingetroffen**, bei h = 0,5 knapp: 0,806 / 0,929 / 0,979 / 0,990 / 0,996 / 0,999 (h = 0,5 bis 0,15) |

**Bedeutung (nach Karte):**
- SG1 und SG2 treffen ein, SG3 stuetzt. Damit gilt die erste Zeile der Karte:
  - "Die Stille des Teilchens misst die Anisotropie des Raums. Der Breiten-Exponent ist zweimal die Anisotropie-Ordnung
    [H, 2D, M1]."
  - "Auf Gittern bleiben stille Moden 'fast still', in einem genuegend isotropen diskreten Raum praktisch exakt."
  - Zahlen dazu bei h = 0,15: Breite 1,4e-6 (A) gegen 1,4e-11 (B). Die Lebensdauer 1/Gamma ist damit ~7e5 gegen ~7e10
    Zeiteinheiten.
- **Einschraenkungen:**
  - ein Modell (M1), 2D, eine Sprosse (n = 7)
  - ein Gittertyp (Quadrat) mit zwei Sternen; Q-Ball auf einem Gitterpunkt; nur der A1-Sektor
  - [H] Die "Regel" ist das bekannte Gesetz Gamma ~ (Symmetriebruch)^2 fuer gestoerte BICs, mit der
    Anisotropie-Amplitude des Sterns als Bruchparameter. Sie ist kein neues Gesetz.
  - Ob ein unregelmaessiger Graph (statt eines Gitters) dieselbe Ordnungsregel hat, ist offen.

## Tabellen

**Stern A (5 Punkte).**
- Gamma = -Im rho am Minimum. "Fit" ist das Minimum der Parabel aus der letzten S3-Runde; "direkt" die Rechnung bei x*.
- Boden = |MIN - DOPPEL| + |MIN - P2|.
- F-Anteile: Fluss des offenen Kanals v am MIN-Punkt.

| h | omega_r^2(h) | Gamma_min (Fit) | sigma Fit | Gamma direkt | Boden | Gamma/Boden | a | Re rho | F0 / F4 / F8 (r = 20) | F4 (r = 22,5) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,5 | 0,5302302 | 2,0579e-4 | 2,5e-9 | 2,0579e-4 | 5,3e-9 | 3,9e4 | 2598 | 1,557865 | 0,126 / 0,806 / 0,066 | 0,757 |
| 0,4 | 0,5298599 | 7,8257e-5 | 3,2e-9 | 7,8257e-5 | 2,2e-10 | 3,6e5 | 2881 | 1,557327 | 0,046 / 0,929 / 0,025 | 0,909 |
| 0,3 | 0,5295910 | 2,3375e-5 | 3,6e-9 | 2,3375e-5 | 5,4e-11 | 4,3e5 | 3063 | 1,556934 | 0,013 / 0,979 / 0,007 | 0,974 |
| 0,25 | 0,5294896 | 1,1022e-5 | 3,8e-9 | 1,1022e-5 | 9,2e-12 | 1,2e6 | 3126 | 1,556786 | 0,006 / 0,990 / 0,003 | 0,988 |
| 0,2 | 0,5294082 | 4,4327e-6 | 3,9e-9 | 4,4326e-6 | 8,6e-13 | 5,1e6 | 3174 | 1,556666 | 0,0025 / 0,996 / 0,0013 | 0,995 |
| 0,15 | 0,5293460 | 1,3828e-6 | 3,9e-9 | 1,3827e-6 | 3,3e-14 | 4,2e7 | 3210 | 1,556575 | 0,0008 / 0,999 / 0,0004 | 0,999 |

**Stern B (isotroper 9-Punkt-Stern)**, gleiche Spalten:

| h | omega_r^2(h) | Gamma_min (Fit) | sigma Fit | Gamma direkt | Boden | Gamma/Boden | a | Re rho | F0 / F4 / F8 (r = 20) | F4 (r = 22,5) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,5 | 0,5305745 | 3,2970e-7 | 9,5e-10 | 3,2967e-7 | 9,4e-12 | 3,5e4 | 2613 | 1,558321 | 0,000 / 1,000 / 0,000 | 0,9995 |
| 0,4 | 0,5300656 | 4,5787e-8 | 4,9e-11 | 4,5783e-8 | 1,0e-13 | 4,5e5 | 2849 | 1,557610 | 0,000 / 1,000 / 0,000 | 1,000 |
| 0,3 | 0,5297012 | 3,9974e-9 | 1,6e-12 | 3,9970e-9 | 7,0e-14 | 5,7e4 | 3028 | 1,557091 | 0,000 / 1,000 / 0,000 | 1,000 |
| 0,25 | 0,5295647 | 8,8290e-10 | 3,7e-13 | 8,8274e-10 | 4,0e-14 | 2,2e4 | 3097 | 1,556893 | 0,000 / 1,000 / 0,000 | 1,000 |
| 0,2 | 0,5294556 | 1,4219e-10 | 1,8e-13 | 1,4209e-10 | 1,9e-14 | 7,6e3 | 3154 | 1,556735 | 0,000 / 1,000 / 0,000 | 1,000 |
| 0,15 | 0,5293723 | 1,3875e-11 | 1,6e-13 | 1,3784e-11 | 9,7e-15 | 1,4e3 | 3197 | 1,556613 | 0,000 / 1,000 / 0,000 | 1,000 |

**Fit-Exponenten** (Unsicherheit: Standardfehler bzw. Kovarianz des Fits; ohne die Abweichung von reiner Potenzform):

| Groesse | Stern A | Stern B |
|---|---|---|
| p (log Gamma_min gegen log h, alle sechs h) | 4,151 +- 0,026 | 8,357 +- 0,068 |
| oertlich 0,15-0,2 / 0,2-0,25 / 0,25-0,3 / 0,3-0,4 / 0,4-0,5 | 4,05 / 4,08 / 4,12 / 4,20 / 4,33 | 8,09 / 8,18 / 8,28 / 8,48 / 8,85 |
| q (omega_r^2 = w0 + c h^q, alle h) | 2,188 +- 0,022 (w0 = 0,5292795) | 2,224 +- 0,027 (w0 = 0,5292867) |
| Extrapolation w0' (linear in h^2, h <= 0,3) | 0,5292635 (-2,5e-6) | 0,5292615 (-4,5e-6) |
| c' (Steigung in h^2) | 3,631e-3 | 4,875e-3 |

- Die oertlichen Exponenten nehmen zu kleinem h monoton ab und laufen auf 4 bzw. 8 zu. Der Gesamtfit liegt darum leicht
  ueber 4 bzw. 8; die Korrekturen hoeherer Ordnung sind positiv.
- Im Dreiparameter-Fit nimmt q den h^4-Anteil mit auf (q > 2), deshalb liegt sein w0 1,4e-5 bzw. 2,1e-5 zu hoch. Gewertet
  ist nach Plan w0'.
- **Rechenboden:** Stern A 3,3e-14 (h = 0,15) bis 5,3e-9 (h = 0,5), Stern B 9,7e-15 bis 9,4e-12.
  - Die PML-Probe dominiert und ist relativ zur Breite: A 2e-8 bis 2,6e-5, B 2,2e-6 bis 4,5e-4.
  - Bei kleinen B-Breiten zeigt sich ein absoluter Boden um 1e-14; relativ zur Breite ist der Boden hoechstens 7e-4
    (B015).
  - Die Doppelrechnung (anderer Shift) stimmt auf hoechstens 3,5e-15 (B015) ueberein.

## Kontrollen

- **K0 (geplant):** Die h^2-Extrapolation trifft das radiale Kontinuum.
  - Stern A: 0,5292635, Stern B: 0,5292615; Referenz 0,529266 (FEIN) bzw. 0,5292654 +- 2e-6 (F7b, RUNDE-12).
  - Abstand hoechstens 4,5e-6, Schranke 3e-5.
- **Nachtraeglich, nicht im Plan** (Zwei-Punkt-Richardson h = 0,15 und 0,2, linear in h^2):
  - omega_r^2(0): 0,5292659 (A) und 0,5292652 (B), gegen 0,5292654 (F7b).
  - Re rho(0): 1,5564571 (A) und 1,5564565 (B), gegen rho* = 1,556457 (F7b).
  - Kruemmung a(0): 3255 (A) und 3253 (B), gegen 57^2 = 3249 (RUNDE-12: Steigung 57,0 bis 57,2).
  - Die Gitterrechnung setzt also die radiale Kontinuumsrechnung auf ~1e-6 fort, mit einem voellig anderen Code
    (kartesisch, PML, Eigenwertproblem statt Pluecker/Shooting).
- **Numerik ueber alle 212 Punkte** (Hauptlaeufe, h = 0,15 und P2-Proben):
  - Residuum ||Q(rho) x|| <= 4,6e-14 (x normiert); Arnoldi gegen Nachverfeinerung <= 1,1e-14.
  - Q-Ball-Newton max|F| <= 1,0e-11.
  - Die Auswahl war immer eindeutig: l0-Anteil der gewaehlten Mode 0,968 bis 1,000; andere Kandidaten weit entfernt.
  - Laengste Einzelrechnung 56 s, laengster Lauf 8 min 7 s (B015), alle unter 10 min.
- **Suche:** In allen zwoelf Laeufen lag das S1-Minimum innen (keine Randerweiterung) und der S3-Scheitel im Fenster
  (keine zweite S3-Runde).
  - Bei B015 weichen Fit-Minimum und direkte Rechnung um 0,66 % ab (9e-14). Das liegt innerhalb der Fit-Unsicherheit
    1,6e-13, aber ueber dem geplanten Boden 9,7e-15; der Boden enthaelt die Fit-Unsicherheit nicht.
  - Auch mit dieser Groesse als Boden liegt B015 87-fach darueber.
- **Nebenbefunde (nachtraeglich, ohne Wertung):**
  - **Fernfeld:** Der l = 0-Anteil am Minimum steigt von r = 20 auf 22,5 um den Faktor 1,26 bis 1,28; (22,5/20)^2 = 1,27.
    - F0/F4 waechst wie h^4 (oertlich 4,06 zwischen h = 0,15 und 0,2, bis 5,1 zwischen 0,4 und 0,5).
    - Mit der Phase beta = 0,0905 h^2 r einer reinen l = 4-Welle (vom Zentrum an) erwartet man F0/F4 ~ beta^2/2:
      2,6e-3 bei h = 0,2 (gemessen 2,5e-3) und 1,33e-2 bei h = 0,3 (gemessen 1,37e-2).
    - [H] Am Minimum strahlt also praktisch nur der Gitterkanal l = 4. Der l = 0-Anteil auf dem Kreis ist Messartefakt
      der Kreiszerlegung.
  - **Verschiebungsverhaeltnis:** c'_B/c'_A = 1,343 (Zwei-Punkt-Steigungen: 1,338), gegen 4/3 aus den isotropen
    h^2-Termen (Stern B h^2/12, Stern A (3/4) h^2/12).
  - **Breitenverhaeltnis** gegen die Plan-Schaetzung (h^2 K^2/30)^2: 1,30 / 1,16 / 1,07 / 1,04 / 1,014 / 1,003
    (h = 0,5 bis 0,15).
    - [H] Die Breite wird vom cos 4theta-Anteil des Sterns bei der Abstrahl-Wellenzahl K ~ 2,05 bestimmt.
    - Die Wand des Hintergrunds (Wellenzahlen ~1) wuerde ein anderes Verhaeltnis geben. Ihr Beitrag ist danach klein;
      getrennt gemessen ist das nicht.
  - **Wandradius** Achse minus Diagonale:
    - Stern A -0,026 (h = 0,5) bis -0,0025 (h = 0,15), grob -0,1 h^2.
    - Stern B -0,003 bis -0,001, ohne saubere Skalierung. Das Halbwertsmass (lineare Interpolation auf dem Gitter) ist
      dafuer zu grob.

## Latten (v3)

- **L1 (kann scheitern): ja.**
  - Vier Vorhersagen mit Zahlengrenzen vor jeder Rechnung; jede haette scheitern koennen.
  - SG3 lag bei h = 0,5 nur 0,006 ueber der Grenze, auf dem Kontrollkreis darunter (0,757).
- **L2 (Gegenprobe): ja, teilweise.**
  - Stern B ist die eingebaute Gegenprobe: gleiches Gitter, gleicher Code, andere Anisotropie-Ordnung, anderer Exponent
    (8,36 gegen 4,15).
  - Dazu die Fernfeldzerlegung als Mechanismusprobe, die Doppelrechnung und die PML-Probe.
  - Es fehlt eine unabhaengige zweite Methode auf dem Gitter, etwa eine Zeitentwicklung wie in RUNDE-22.
- **L3 (Numerik): ja.**
  - Boden 1e-14 bis 5e-9, alle Breiten >= 1400-fach darueber.
  - Die Kontinuumsgrenze trifft die radiale Rechnung (geplant auf 4,5e-6, nachtraeglich per Richardson auf <= 8e-7).
  - Offen: nur ein Innengebiet (PML ab 24), nur eine PML-Familie je Probe, nur eine Fernfeld-Definition.
- **L4 (schon bekannt): teilweise.**
  - [S] Koshelev u. a., Phys. Rev. Lett. 121, 193903 (2018), arXiv:1809.00330, an der Quelle gelesen:
    - Gl. (3): Q_rad = Q_0 alpha^-2; die quadratische Abhaengigkeit sei ein "universal behavior" von Quasi-BICs.
    - Gl. (2a): gamma_rad als Summe ueber alle offenen Kanaele.
    - Unser Befund ist dieses Gesetz mit alpha ~ h^2 (A) bzw. h^4 (B).
  - [S] Zhen u. a., Phys. Rev. Lett. 113, 257401 (2014), arXiv:1408.0237, Abstract gelesen: BICs entstehen "through
    fine-tuning parameters in the wave equation or exploiting the separability of the wave equation due to symmetry".
    - Die 2D-Sprosse nutzt beides: Die Drehsymmetrie trennt die Kanaele, omega^2 stimmt l = 0 ab.
    - Das Gitter hebt die Trennung auf.
  - [L?] Hsu u. a., Nat. Rev. Mater. 1, 16048 (2016), Uebersicht ueber BICs. Nicht an der Quelle gelesen; die
    Nature-Seite war nicht abrufbar.
  - [L?] Patra und Karttunen, Numer. Methods Partial Differ. Equ. 22, 936 (2006), isotrope Sterne. Nicht abrufbar (403).
    - Die Isotropie des 9-Punkt-Sterns in Ordnung h^2 und der cos 4theta-Term in Ordnung h^4 sind hier selbst
      nachgerechnet (PLAN.md Abschnitt 1).
  - [L?] Stille Moden bzw. BICs von Q-Baellen oder Oszillonen auf Gittern: nicht gesucht. Das Websuche-Kontingent dieser
    Sitzung war erschoepft.
    - Ob die Kopplung "Exponent = zweimal die Ordnung des Sterns" fuer nichtlineare Feldmoden beschrieben ist, bleibt
      offen.
- **L5 (Messbezug): nein.**
  - [H] Bezug hoechstens zu Gittersimulationen: Lebensdauern stiller Moden sind dort Gitterartefakte der Groesse ~h^4
    (5-Punkt-Stern), mit dem isotropen Stern ~h^8.

## Selbstanzeigen

- **Rauchlauf vor dem Einfrieren** (h = 0,45, 0,35, 0,22; kommen in keinem echten Lauf vor, im Plan offengelegt):
  - Er zeigte die Groessenordnungen und den Exponententrend (A 0,45 und 0,22: lokal ~4,2; B: ~8,4).
  - Die Vorhersagen der Karte standen vorher fest und sind unveraendert.
  - Die Schaetzung B/A ~ (h^2 K^2/30)^2 habe ich am Schreibtisch vor dem Rauchlauf gerechnet, aber erst nach ihm in den
    Plan geschrieben. Der Rauchlauf zeigte bei h = 0,45 9,9e-4 gegen geschaetzt 8,1e-4. Punkt 4 von "Ergebnis zuerst"
    ist darum keine Vorab-Vorhersage im strengen Sinn.
- **Zeitangabe geschaetzt statt gemessen:**
  - Im Plan steht fuer R2 "bis ~20:59 UTC". Gemessen endeten A-h0.22 um 20:56:13 und B-h0.22 um 20:57:25 UTC.
  - B-h0.22 lief also noch 67 s nach dem Einfrieren und nach dem Start der Hauptlaeufe (gleicher Code). Sein Ergebnis
    steht nicht im Plan.
- **Fehler im ersten Code** (Nachverfeinerung mit der LU bei sigma, Residuum ~1e-3): im Rauchlauf R1 gefunden und vor dem
  Einfrieren behoben. Die R1-Werte sind dadurch auf ~1e-6 ungenau; sie wurden nur fuer Startwerte genutzt.
- **Schreibtisch-Fehler** (PLAN.md Luecke 2): Die Mischung im Fernfeld habe ich von der Wand an gerechnet (~0,7 %).
  - Richtig ist vom Zentrum an; das gibt bei h = 0,5 ~10 %, gemessen 12,6 %.
  - Darum war SG3 bei h = 0,5 knapp. Messkreis und Regel blieben wie geplant.
- **auswertung.py** wurde nach dem Einfrieren geschrieben (22:57:43 CEST) und setzt Abschnitt 5 woertlich um.
  - A030 endete 22:57:42 CEST, eine Sekunde vorher; gelesen habe ich das Ergebnis erst danach.
  - Am Skript wurde nach dem Lesen nichts geaendert.
- **Nachtraegliche Pruefungen** (Richardson, rho(0), a(0), 4/3, B/A, r^2-Gesetz des Fernfelds) stehen getrennt und
  ohne Wertung.
- **Lokal kein Python.** Lokal benutzt: jq, sha256sum, rsync, ssh, scp, cp, chmod und das Lese-Werkzeug fuer das PDF von
  Koshelev u. a.
- **Speicher:** Die Zeilen "Memory peak" (1 bis 4 MB) in den Logs gehoeren zum systemd-Huellprozess, nicht zur Rechnung.
  Den Speicherbedarf habe ich nicht gemessen; MemoryMax 4G wurde nie ueberschritten (alle rc = 0).
- **Sonst:** nur Spuren cpu, cpu2, cpu3, cpu4 und cpu6, nicht cpu5, keine GPU, jeder Lauf unter 10 min. Kein git, kein
  Peerbus, kein Journal, keine Unteragenten, keine Aenderung an Karten oder anderen Runden.
  - Auf der .69 wurde nichts in place ueberschrieben (Upload als .neu, dann mv).

## Ablage

- lokal: code/ (stille_gitter.py, auswertung.py), PLAN.md und PLAN.md.eingefroren-20261002-225618 (sha256
  370c807be4d064a3a1989e9e99cce3904c09a0b7853fb81c8b267bace1cfac97)
- lauf-69/: rauch/, rauch2/ (Rauchlaeufe), haupt/ (12 Scans und 2 P2-Proben, je .json und .log), auswertung10/
  (nur zehn Hauptlaeufe), auswertung/ (gewertet, alle zwoelf)
- .69: /home/fmh/fmhc-physics-remote/runde23-stille-auf-gitter/ (identisch)

## Einfach gesagt

Im Computer ist der Raum ein Gitter aus Punkten, nicht glatt. Wir wollten wissen, ob unser "stilles" Teilchen, das im
glatten Raum schwingt, ohne Energie abzustrahlen, auf so einem Gitter still bleibt. Es leckt ein kleines bisschen, und
zwar in einem Kleeblattmuster mit vier Blaettern, das die vier Richtungen des Gitters nachzeichnet. Halbiert man den
Punktabstand, wird das Lecken beim einfachen Gitter-Rezept etwa 16-mal kleiner, beim "runderen" 9-Punkt-Rezept etwa
256-mal kleiner. Je weniger der Raum eine Richtung bevorzugt, desto stiller bleibt das Teilchen.

---
Letzte Aenderung dieser Datei: 2026-10-02 23:16:22 CEST (date). Zeitbox 120 min ab 22:35:19 eingehalten.
