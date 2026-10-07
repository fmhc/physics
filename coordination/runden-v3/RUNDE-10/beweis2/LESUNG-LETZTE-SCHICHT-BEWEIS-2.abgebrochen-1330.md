Urteil: offen (Lesung laeuft)

# Lesung der letzten Schicht, BEWEIS-2

- Leser: frischer Leser, Haus Anthropic (Claude), im Auftrag der Leitung claude-primary
- Beginn (date): 2026-09-30 13:19:47 CEST
- Ende (date): offen
- Zeitbox: 25 min
- Gegenstand: RUNDE-10/beweis2/ (BEWEIS-2.md Abschnitt 8 und geaenderte Stellen, BEWEIS-2-PLAN.md, STAND.md, zertifikat/)

## 0. Pruefung der Hashes und des Zertifikats

- BEWEIS-2.md sha256 3ad62460291f3a2d... und BEWEIS-2-PLAN.md 0f8f0790dd8b262e... stimmen mit der Nennung der Leitung.
- `sha256sum -c zertifikat/SHA256SUMS.txt`: 37 von 37 OK. Nicht gelistet ist nur SHA256SUMS.txt selbst
  (a105dcf9...). Alle 38 Dateien in zertifikat/ haben mtime <= 12:41, also vor den .bak-Dateien (13:13) und vor
  Abschnitt 8. "zertifikat/ unveraendert" trifft zu.
- Die .bak-Fassungen (BEWEIS-2.md fe83a463..., PLAN 099f6335...) sind genau die Fassungen, an die die OpenAI-Lesung
  gebunden ist (GESAMT-REVIEW.txt:110-111). Beide Lesungen lasen also dieselbe Vorfassung.
- Laut diff hat STAND.md nur zwei neue Zeilen am Ende, alte Zeilen sind unveraendert. Der PLAN hat drei Einschuebe
  (4.1, 4.4, 4.5). In BEWEIS-2.md sind 18 Stellen geaendert (Ergebnis, 1, 2, 3, 4.3, 4.5, 5.4, 6, 7, neu 8,
  Einfach gesagt).

## 1. Vorwaerts: Auflage -> Stelle -> umgesetzt

| Auflage | Stelle (neu) | umgesetzt | Anmerkung |
|---|---|---|---|
| Anthropic A1 (F1, F2): Ursache T2-B, M1 nennen, l=1-Breite nur der Zeilensumme der a- und om-Zeile in A/B2 zuordnen, STAND neue Zeile | 4.5 (Z. 217-254), STAND Z. 32 | teilweise | Ursache und M1 sind richtig berichtigt. STAND hat eine neue Zeile, die alte bleibt stehen. Zuordnung nur "ueber die a-Zeile" (Befund 6); "kaum kleiner" und "davon 0,0342" sind ungenau (Befunde 5, 7) |
| Anthropic A2 (F6): z0_rho neu uebertragen | 4.3 Z. 172 | ja | z0_rho stimmt. Der mitgeaenderte Abstand 0,108 delta ist aber falsch (Befund 1) |
| Anthropic A3 (F7): Gesamtflag T1 praezisieren, R < r_j durch Abbruch | 3 Z. 107-111, 121-122; 4.5 Z. 197 | ja | Umgesetzt im Wortlaut der Lesung. Der Mechanik nach ist "Abbruch" falsch (Befund 4) |
| Anthropic A4 (F3, F4): Plan vor jedem Lauf einfrieren (kuenftig) | 6 Punkt 8 Z. 380-383 | ja | Als Zusage fuer kuenftige Beweise; die Nichterfuellung ist offen benannt |
| Anthropic A5 (F8): Herkunft der Breite klaeren | 4.5 Z. 250-254; 6 Punkt 9; 8 "offen" | ja | Als offene Frage mit zwei ungeprueften Kandidaten gefuehrt (so verlangt: "vor weiteren Laeufen") |
| Anthropic A6 (F9, optional) | 5.4 Z. 336; PLAN 4.5 Z. 121-122; 1 Z. 45; 6 Punkt 10 | ja | Die Obergrenze ...846998028 ist richtig nach aussen gerundet (Abschnitt 2) |
| Anthropic F5: B2 nicht vorab | Ergebnis Z. 14-19; 4.5 Z. 239-242; 6 Punkt 6 | ja | - |
| OpenAI A1: reelle Y_1m-Basis, sonst Y_lm* | Satz T2 Punkt 4 Z. 89-94; PLAN 4.1 Z. 67-72 | ja | Die Begruendung im PLAN habe ich im Kopf nachvollzogen: Der conj(psi)-Term bringt conj(Z) ins Band e^{i rho t}, also muss Z = conj(Y) sein |
| OpenAI A2: Ableitungskern erklaeren | PLAN 4.4 Z. 106-108 | ja | Aus K_B = e^{kc r} G_B e^{-kc s} folgt (d_r - kc) K_B = e^{kc r}(d_r G_B) e^{-kc s}. Mit d'(u), g'(u) ergibt sich die Schranke (2 + 2/x + 1/x^2)/2 = b2 fuer x = kc L >= 1 (Kopfrechnung) |
| OpenAI A3: Reproduktion mit historischem Hash | 7 Z. 421-424 | ja | diff c1f85f81 gegen die Endfassung: nur --dcexp, der Parameterschluessel dcexp und delta[1] mal 2^dcexp. "Derselbe Weg ohne --dcexp" stimmt; das JSON bekommt zusaetzlich 'dcexp': 0 |
| OpenAI A4: n nur Leiterzuordnung, Krein kein Stabilitaetssatz | Ergebnis Z. 21; Saetze Punkt 5; 6 Punkt 5 | teilweise | PLAN 2 Z. 25 ist unveraendert: "n = 2 heisst nur: die Eigenfunktion hat mehr Knoten" (Befund 3) |
| OpenAI Grenzen (radiale Einfachheit je Kanal, Multiplett, keine Stabilitaet, eingebettet operational) | 6 Punkt 5 Z. 353-361 | ja | - |
| OpenAI Codehinweis (l-Bereich, Kommentar A'(0) = 1) | 6 Punkt 10 | ja | vermerkt, keine Codeaenderung |

Quote vorwaerts: 11 ja, 2 teilweise, 0 nein (13 Auflagen und Hinweise).

## 2. Rueckwaerts: neue und geaenderte Zahlen gegen zertifikat/

Mit jq habe ich nur Werte ausgelesen und im Kopf umgerechnet. Die Umrechnung der Dyadiken lief ueber die
Stellenzahl der Mantisse und log10(2) = 0,30103. Beispiel: 2^-299 = 10^-90,00797 = 9,818e-91 und 2^-294 = 32 * 2^-299
= 3,1418e-89.

**T2-B, Ursache (4.5, ZERT-T2-B-L40.json):**
- c-Zeile von Y, export.Y[1]:
  - 4,8356e89 * 2^-299 = 0,4748
  - 1,0278e90 * 2^-299 = 1,0091
  - 4,7436e90 * 2^-294 = 149,03
  - 1,0347e90 * 2^-294 = 32,51
  - Also (-0,4748; 1,0091; -149,0; 32,51). **stimmt**
- Radien von D in Spalte a, radius_m_e:
  - 635629269 * 2^-4 = 3,973e7
  - 28010829 * 2 = 5,602e7
  - 673630391 * 2^-39 = 1,225e-3
  - 562067713 * 2^-37 = 4,090e-3
  - **stimmt**. Die "text"-Felder zeigen 4,76e7 usw., weil die Dezimalrundung der Mitte eingerechnet ist; die Autor-Werte
    kommen richtig aus radius_m_e.
- Relativ (D_relbreite): 4,04e-10 und 1,21e-9. **stimmt**
- Summe Spalte a:
  - 0,4748 * 3,973e7 = 1,886e7 und 1,0091 * 5,602e7 = 5,653e7, zusammen 7,539e7
  - Mk[1][0] = 7,54e7. **stimmt**
  - Beitrag der Zeilen 3 und 4: 149,03 * 1,225e-3 = 0,183 und 32,51 * 4,09e-3 = 0,133, zusammen 0,316 = "0,32". **stimmt**
- Spalte om:
  - 169813713 * 2^-2 = 4,245e7 und 12516749 * 4 = 5,007e7
  - 0,4748 * 4,245e7 + 1,0091 * 5,007e7 = 2,016e7 + 5,052e7 = 7,068e7; Mk[1][3] = 7,07e7. **stimmt**
  - Zeilen 3 und 4 in Spalte om: 1053808541 * 2^-40 = 9,58e-4 und 879286913 * 2^-38 = 3,20e-3, also
    149,03 * 9,58e-4 + 32,51 * 3,20e-3 = 0,143 + 0,104 = 0,247 = "0,25". **stimmt**
- delta:
  - delta_a = 1,74509e-21, delta_c = 6,88736e-15, delta_om = 2,23108e-21
  - 7,54e7 * 0,253376e-6 = 19,10 und 7,07e7 * 0,323938e-6 = 22,90, zusammen 42,0
  - protokoll.zeilensumme_gewichtet 41,998580. **stimmt**
- H_0,1(z0) = [-2,219e-14 +- 2,29e-18]: "Breite <= 2,3e-18" stimmt als Radius; so verwendet das Dokument "Breite".
- M1: rowsum = 19,102934, BESTANDEN false. In B2: 1,4574382e-4, und 19,102934 / 1,31072 = 14,5744, also
  19,10 / 2^17. **stimmt**
- T1-B: M1.rowsum 0,034217 und M3.rowsum 0,084514. **Zahlen stimmen**; zur Zuordnung siehe Befund 7.

**T2-A und B2 (4.5):**
- a-Zeile von Y, T2-A: 5,1312e76 * 2^-256 = 0,4431 und 4,4769e76 * 2^-258 = 0,0967; in B2 gleich (0,4431; 0,0967).
  **stimmt**
- T2-A:
  - Mk[0] = (7,70e-4; -; 1,50e-8; 6,02e-4), delta_om / delta_a = 2,70199 / 2,11068 = 1,2802
  - 7,70e-4 + 7,706e-4 = 1,5406e-3; M3.rowsum 1,5401e-3. **stimmt**
- B2: Mk[0][0] ist 9,39e-4, nicht 9,38e-4. Mit 9,38e-4 ergibt die Zeile 1,876e-3, mit 9,39e-4 ergibt sie 1,877e-3.
  M3.rowsum ist 1,8769e-3. **Abschreibfehler, harmlos**
- D_relbreite, Zeilen 3 und 4, Spalte a: T2-A 1,34e-3 / 1,26e-3; B und B2 1,64e-3 / 1,54e-3. Die Spanne "1,3e-3 bis
  1,6e-3" stimmt; "in B kaum kleiner als in A" stimmt nicht (Befund 5).
- relw_f_bei_L T2-A = 2871,5, im Text "2872". **stimmt**
- Schrittzahlen T1: 350 / 362 / 487 / 508. **stimmt**, ebenso R_kleiner_rj_alle = true in allen vier Protokollen der T1-Laeufe.
  Die T1-Flags enthalten weder 0 < h < R noch N/qfac. **stimmt**

**z0_rho und Empfindlichkeit T1-B (4.3):**
- protokoll.Z.rho von T1-A:
  - untere Grenze 1,690356597328143456807519406878...
  - obere Grenze 1,690356597328143456846998027298...
  - Mitte 1,6903565973281434568272587170887...
  - z0_rho = ...827258717 **stimmt**. Die Obergrenze ...846998028 ist richtig aufgerundet (exakt ...8469980272986).
- **Abstand Kr - z0 falsch:**
  - Kr.mitte_m_e und z0 haben beide den Exponenten -195.
  - Mantissendifferenz 2576307198503953... - 1965816698309891... (die letzten 37 Stellen) = 6,10490500e35
  - relativ zur z0-Mantisse 8,48843226e58 sind das 7,19203e-24; mal z0_rho 1,6903566 ergibt 1,2157e-23
  - Mit delta_rho(T1-B) = 1,047951e-22 folgt 0,1160 delta_rho. Im Text steht **1,13e-23 = 0,108 delta_rho**.
- **Kr-Radius:** exakt 306205361 * 2^-108 = 9,436e-25 = 0,0090 delta_rho. Im Text steht 0,017; das ist der Radius der
  gedruckten Kugel.
- Probe: Die gedruckte Kr-Mitte ...82727 liegt 8,74e-25 von der exakten Mitte ...827270874 entfernt. Zusammen mit
  9,436e-25 ergibt das 1,818e-24, gedruckt als 1,82e-24. Die Rechnung ist also in sich geschlossen.
- Ursache: Autor und Lesung haben die 24-stellige Textmitte benutzt statt export.Kr.mitte_m_e.

## 3. Absolute Aussagen

(offen)

## 4. Wortlaut der Grenzen

(offen)

## 5. Befunde (nummeriert)

(offen)
