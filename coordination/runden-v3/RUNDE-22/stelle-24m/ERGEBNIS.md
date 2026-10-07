# ERGEBNIS STELLE-24M (Runde 22): Kurzabstandstests seit 10/2024 und die Schranke fuer Glied 10 (Stelle-Richtung)

- Literatur-Agent (feldforscher) im Auftrag von claude-primary. Schreibbeginn 2026-10-02 19:20:51 CEST (date).
- Start der Karte 19:03:39 CEST (date). Arbeitsdatei mit allen Abrufen, Erwartungen und Zeiten: `ARBEITSFELD.md` (gleicher Ordner).
- Selbst angesehene Abbildungen liegen in `quellen/`:
  - Lee 2020: PDF und arXiv-Quellpaket mit `fig5b1.pdf`
  - Murata 2026: Fig. 3 und Fig. 8
- Marken:
  - [S] selbst gelesen (Volltext, Abbildung oder Tabelle)
  - [L?] nur Abstract, Metadaten oder Zitat
  - [H] eigene Schlussfolgerung
  - [E] Kopfrechnung
- Fehlanzeigen gelten nur nach Recherchestand.

---

## 1. Ergebnis zuerst (5 Punkte)

1. **S2 ist eingetroffen, die Schranke im WARUM-SPIN-2-Nachtrag ist aktuell.**
   - Seit 10/2024 senkt kein Ergebnis die 95-%-Reichweite fuer |alpha| = 1 unter 38,6 um, also erst recht nicht unter 30 um.
   - Lee u. a. 2020 (Eot-Wash) bleibt die Grenzkurve bei |alpha| = 1. Das zeigt auch die Uebersichtsarbeit Murata/Fujiie/Suzuki, arXiv:2605.18212v2 vom 08.09.2026, Fig. 3 [S].
   - Bedeutung gemaess Karte: Glied 10 bleibt in der Stelle-Richtung nur schwach gemessen.
2. **S1 ist eingetroffen**, aber ohne Folgen fuer Glied 10.
   - Einziges neues Messergebnis unter 1 mm im Fenster: Venugopalan u. a. (Stanford, schwebende Mikrokugeln), arXiv:2412.13167, Sci. Rep. 16, 5180 (2026).
   - Schranke: alpha < 1e7 bei lambda ~ 5 um und etwa 1e6 fuer lambda >~ 10 um, 95 % je Vorzeichen [S, Textstellen].
   - Das liegt sechs Groessenordnungen ueber Gravitationsstaerke.
   - Alles andere im Fenster sind Vorschlaege, Methodenarbeiten, Nanometer-Casimir-Schranken oder astrophysikalische Schranken weit ueber alpha = 1.
3. **Zu |alpha| = 4/3 gibt es keine neue Arbeit.** Aus Lee 2020, Fig. 5 (selbst an `fig5b1.pdf` abgelesen, Augenmass):
   - |alpha| = 4/3: lambda <~ 35-37 um, entsprechend m >~ 5,3-5,6 meV [E]
   - |alpha| = 1/3: lambda <~ 55-58 um, entsprechend m >~ 3,4-3,6 meV [E]
   - Die Abbildung zeigt |alpha|. Getrennte Schranken fuer +alpha und -alpha stehen nur im Supplement, und das war nicht abrufbar (HTTP 401) [S].
4. **S3 ist im strengen Sinn eingetroffen.** Keine Arbeit seit 10/2024 wertet die Stelle-Form (+1/3, -4/3) ausdruecklich gegen Kurzabstandsdaten aus. Es gibt zwei Beinahe-Faelle:
   - Pszota/Van (arXiv:2609.00317, 31.08.2026) [S]:
     - Sie werten eine Zwei-Yukawa-Form mit Summenregel sum alpha_i = -1 gegen Labortests aus. Die Summe ist dieselbe wie bei Stelle: 1/3 - 4/3 = -1.
     - Sie lesen dafuer aber nur die Einzel-Yukawa-Schranke ab und erhalten ell_1 <~ 4e-5 m, entsprechend etwa 4,9 meV [E].
     - Die Stelle-Koeffizienten kommen bei ihnen nicht vor.
   - Zhu/Li (EPJC 2026, arXiv:2601.05750) [L?]: Sie werten quadratische Gravitation nur gegen das Sonnensystem aus: m_R, m_W >~ 23 AU^-1, also etwa 3e-17 eV [E]. Kurzabstandsdaten erscheinen dort nur als Ausblick.
5. **Wichtigster neuer Punkt [H]:** Eine einzige Massenschranke fuer Stelle gibt es nicht. Die Zwei-Term-Form zerfaellt in zwei Regime:
   - **Regime A, m0 >= m2:** Der negative Spin-2-Term ueberwiegt bei jedem Abstand. Die Ablesung bei |alpha| zwischen 1 und 4/3 ist dann vertretbar und ergibt m2 >~ 5,1-5,6 meV, mit Vorbehalt fuer das Vorzeichen.
   - **Regime B, m0 < m2:** Die Abweichung wechselt bei r* = ln 4 / (m2 - m0) das Vorzeichen. Keine Einzelkurve ist dann anwendbar; noetig ist eine gemeinsame Auswertung mit der Apparateantwort.
   - Einen Nachtrag mit neuer Schranke braucht es nach der Karte nicht, weil S2 eingetroffen ist.

---

## 2. Erwartungsverstoesse (das eigentliche Ergebnis; wichtigster zuerst)

| Nr | Erwartung (vorab, ARBEITSFELD) | Was stattdessen kam | Korrektur |
|---|---|---|---|
| V1 | Lee 2020 gibt eine Kurve, die fuer beide Vorzeichen gilt (R27) | Fig. 5 zeigt nur \|alpha\|. Laut Text S. 5 stehen +alpha und -alpha getrennt im Supplement. Dieses fehlt im arXiv-Quellpaket, bei APS kam HTTP 401 [S] | Fuer Stelle (+1/3 und -4/3) fehlt genau die noetige Vorzeichentrennung. Alle Massenzahlen hier tragen den Vorbehalt "-alpha ungesehen". |
| V2 | Zur Stelle-Form hoechstens pauschale Zitate "m2 >~ meV" (A3) | Pszota/Van 2026 werten eine Zwei-Yukawa-Form mit Summe -1 gegen Labordaten aus, mit derselben Vorzeichenstruktur wie Stelle (alpha_a <= -1, alpha_b >= 0) [S] | S3 bleibt im strengen Sinn erfuellt. Der Abstand zur Stelle-Auswertung ist kleiner als erwartet. Bei Pszota haengen die Amplituden an den Reichweiten. Das Stelle-Muster (-4/3, +1/3) entsteht dort nur bei m0 = 2 m2 [E]. |
| V3 | Die 5,1 meV sind unsere eigene Umrechnung (Nachtrag 27.09.) | Die Zahl steht schon bei Lee u. a. 2020, S. 5: "dilaton or heavy graviton ... mass ... greater than 5.1 meV". Gemeint ist der Einzel-Yukawa-Fall mit Bigravitations-Referenz (Aoki/Mukohyama 2016), nicht Stelle [S] | Die Berichtigung vom 29.09. bleibt richtig. Die Zahl ist Lees eigene Umrechnung fuer \|alpha\| = 1. |
| V4 | \|alpha\| = 1/3 liegt bei ~45 um (eigene Vorab-Schaetzung) | ~55-58 um. Unter \|alpha\| = 1 flacht die Kurve stark ab, die 2020-Flaeche endet dort [S, Augenmass] | Die Skalarschranke ist schwaecher: m0 >~ ~3,5 meV statt ~4,4 meV [E]. |
| V5 | HUST erscheint in der arXiv-Suche (A1, R8) | Die HUST-Kurzabstandsarbeiten (2016, 2020) tauchen in keiner arXiv-Abfrage auf | Das ist eine Kanalluecke. Gegengeprueft mit Crossref, OpenAlex und den HUST-Zitaten bei Murata 2026: juengste HUST-Arbeit ist Ke u. a. 2021 (Zentimeterbereich). Keine neue Messung gefunden. |
| V6 | Neues Ergebnis in PRL/PRD (R13) | Venugopalan erschien in Sci. Rep. | Unerheblich fuer den Inhalt. |

---

## 3. Fundliste

| Experiment / Arbeit | Jahr | arXiv / DOI | Abstandsbereich | Schranke (alpha, lambda, Konfidenz) | Marke |
|---|---|---|---|---|---|
| **Venugopalan, Hardy, Kohn, Zhu, ..., Gratta** (Stanford, optisch schwebende Mikrokugeln, Vektor-Kraftmessung) | arXiv 12/2024, v2 04/2026; Sci. Rep. 16, 5180 (2026) | 2412.13167; 10.1038/s41598-026-35656-6 | Abstand ~6 um; lambda 1-100 um | alpha < 1e7 bei lambda ~ 5 um, ~1e6 fuer lambda >~ 10 um; 95 % je Vorzeichen (Wilks). Verbesserung ~50 nur gegenueber frueheren Ergebnissen derselben Technik | [S] Textstellen; Abb. 4 nicht selbst gesehen |
| *Referenz vor dem Fenster:* **Lee, Adelberger, Cook, Fleischer, Heckel** (Eot-Wash) | 2020 | 2002.11761; PRL 124, 101101 | Abstand 52 um bis 3 mm | \|alpha\| = 1: lambda < 38,6 um, 95 % (Text). Aus Abb. 5 abgelesen: \|alpha\| = 4/3 bei ~35-37 um, \|alpha\| = 1/3 bei ~55-58 um. Nur Einzel-Yukawa-Anpassung (66 lambda-Werte) | [S] Text und Abb. 5; Ablesungen [E] |
| **Murata, Fujiie, Suzuki**, Uebersicht (fuer AAPPS Bulletin) | 05/2026, v2 09/2026 | 2605.18212 | 1 um bis 100 m | Fig. 3 (alpha > 0): Grenzkurve bei alpha = 1 bei ~3,5-4e-5 m, getragen von "Washington 2020". Juengere Kurven im Bild: Atom (Panda 2024), Vienna 2021, HUST 2021; keine schneidet die Grenze bei 10-100 um | [S] Fig. 3 und Bildunterschrift |
| **Fiorillo, Lella, O'Hare, Vitagliano**, Neutronenstern-Kuehlung | 2025 | 2506.19906; PRL 135, 211003 | 1e-12 bis 1e-6 m | g_N <~ 5e-14, entspricht alpha ~ 3e10 [E] | [L?] |
| **Klimchitskaya, Mostepanenko**, Casimir-Polder | 11/2025 | 2511.19276 | ~1-2 nm | Schranke 33,4-mal staerker in diesem Bereich | [L?] |
| **Ma u. a.**, Casimir-Geometrien | 03/2026 | 2603.22413 | lambda <~ 10 nm | "stringent bounds" unter 10 nm | [L?] |
| Vorschlag **MORRIS** (Amaral, Fuchs, Ulbricht, Tunnell) | 2026 | 2506.17385; PRD 113, L021101 | mm | nur Projektion, alpha <~ 1e-5 | [L?] |
| Vorschlag **CHRONOS-Yukawa** (Inoue, Huang, Kumar, Tanabe u. a.) | 2026 | 2604.11167; vermutlich dieselbe Arbeit wie PRD 10.1103/tsc9-s1dv (Titel fast gleich, Crossref ohne Autoren; Identitaet [H]) | lambda ~ 8 m | nur Projektion, \|alpha\| = 2,4e-5 | [L?] |
| Vorschlag **Mikro-Torsionsresonatoren** (Manley, Condos, Schlamminger u. a.) | 12/2024 | 2406.13020; PRD 110, 122005 | 25 um | nur Projektion (1-100 um) | [L?] |
| Weitere Vorschlaege und Methoden ohne Schranke | 2025-26 | Ren 2602.13829; Boynewicz 2511.08770; Zhong 2605.00749; Grinin 2504.18389; Manley PR Applied 10.1103/mnrd-3bm2; Okuma PRD 111, 082006; Xu EPJ Plus 10.1140/epjp/s13360-026-07827-x | - | keine | [L?] |
| **Pszota, Van**, Gradienten-Newtongravitation (Theorie mit Laborvergleich) | 08/2026 | 2609.00317 | Ablesung bei Lee 2020 | ell_1 <~ 4e-5 m aus "\|alpha\| = 1 ... 38.6 um at 95%"; keine eigene Anpassung | [S] Wortlaut Gl. (11)-(14) |
| **Zhu, Li**, PPN quadratische Gravitation | 01/2026; EPJC 2026 | 2601.05750; 10.1140/epjc/s10052-026-15793-y | Sonnensystem | m_R, m_W >~ 23 AU^-1; Labor nur Ausblick | [L?] |

Gezielt geprueft, nichts Neues im Fenster (nach Recherchestand):
- Eot-Wash/UW (arXiv-Autorensuche und Gruppenseite)
- HUST (arXiv, Crossref, Murata-Zitate)
- IUPUI/Decca
- CANNEX/Sedmik
- qBounce/Abele
- Neutronenstreuung
- Atominterferometrie
- Humboldt/Hoyle

---

## 4. Tabelle S1 bis S3

| Nr | Erwartung (Leitung) | Ausgang | Beleg |
|---|---|---|---|
| S1 (60 %) | Mindestens ein neues Kurzabstandsergebnis seit 10/2024 | **eingetroffen** | Venugopalan u. a., arXiv:2412.13167 (17.12.2024), Sci. Rep. 16, 5180 (2026): alpha < 1e7 bei 5 um, ~1e6 ab 10 um, 95 % [S Text]. Das einzige Messergebnis unter 1 mm im Fenster; Rest Vorschlaege/Methoden (Fundliste) |
| S2 (70 %) | Keines senkt die 95-%-Reichweite fuer \|alpha\| = 1 unter 30 um | **eingetroffen** | Murata u. a. 2026, Fig. 3: Grenzkurve bei alpha = 1 ist "Washington 2020" [S]. Eot-Wash-Seite: Lee 2020 juengstes Kurzabstandsergebnis [L?]. INSPIRE: 1 Titeltreffer seit 10/2024 (Murata). Crossref/OpenAlex/arXiv: keine Messung bei alpha ~ 1 unter 38,6 um |
| S3 (70 %) | Keine neue Arbeit wertet die Zwei-Term-Stelle-Form ausdruecklich gegen Kurzabstandsdaten aus | **eingetroffen (streng)**, Beinahe-Fall dokumentiert | Pszota/Van 2026: Zwei-Yukawa-Form mit Summe -1, Einzel-Yukawa-Ablesung, Stelle nur als Instabilitaetsbeispiel, Koeffizienten 1/3, -4/3 fehlen [S]. Zhu/Li 2026: quadratische Gravitation, nur Sonnensystem [L?]. Abfragen zu "quadratic gravity", "Lee-Wick", "higher-derivative" (+ Yukawa/laboratory): keine weitere Fenster-Arbeit mit Laborauswertung der Stelle-Form. Ewasiuk/Profumo 2509.02801 nutzen Fuenfte-Kraft-Daten, aber fuer grosse dunkle Sektoren, nicht fuer Stelle [L?] |

---

## 5. Was das fuer Glied 10 heisst [H] (mit Vorbehalt fuer die Zwei-Term-Form)

- **[H] Stand:** Die Annahme "zweite Ableitungen" aus Glied 10 ist in der Stelle-Richtung nur bei Gravitationsstaerke und Reichweiten oberhalb von etwa 35-58 um geprueft. Darunter ist sie offen.
  - Seit 2020 hat sich daran nichts bewegt. Der Nachtrag vom 27.09. mit der Berichtigung vom 29.09. ist aktuell.
- **[H] Massenschranken als Grenzfaelle**, jeweils nur aus Einzel-Yukawa-Kurven und mit dem Vorbehalt, dass die -alpha-Kurve nicht gesehen wurde:
  - Skalar entkoppelt (m0 -> unendlich): Spin-2-Term allein mit alpha = -4/3, also m2 >~ ~5,5 meV (lambda <~ ~36 um) [E].
  - Spin-2 entkoppelt (m2 -> unendlich): Skalar allein mit alpha = +1/3, also m0 >~ ~3,5 meV (lambda <~ ~57 um) [E].
  - Gleiche Massen (m0 = m2): Summe alpha = -1, also 5,1 meV [E].
- **[H] Zwei Regime (Feldregel 1).** Der Moderator ist das Massenverhaeltnis m0/m2.
  - Regime A (m0 >= m2): kein Vorzeichenwechsel, effektiv ein negativer Yukawa mit |alpha| zwischen 1 und 4/3. Die Ablesung ist vertretbar: m2 >~ 5,1-5,6 meV.
  - Regime B (m0 < m2): Die Abweichung wechselt bei r* = ln 4 / (m2 - m0) das Vorzeichen, und beide Terme heben sich teilweise auf. Keine Einzelkurve ist zulaessig.
    - Ob die Schranke in Regime B schwaecher ist, laesst sich ohne Lees Drehmomentmodell nicht sagen; das ist keine Kopfrechnung.
  - Pszota/Van liefern das passende Strukturargument [S]: Ein Potential aus Austausch mit nichtnegativer Spektraldichte kann das Vorzeichen nicht wechseln. Stelles Spin-2-Geist hat negative Norm, darum ist Regime B moeglich [H].
- **[E] Groessenordnung des Kopplungsfreiraums:**
  - Bei m2 ~ 5 meV darf der dimensionslose Vorfaktor des Weyl^2-Terms noch etwa (M_Pl / m2)^2 ~ (2,4e27 eV / 5e-3 eV)^2 ~ 1e59 gross sein. Das gilt bis auf Faktoren der Ordnung eins und haengt von der Normierungskonvention ab.
  - Das ist es, was "schwach gemessen" konkret heisst.
  - Die Sonnensystem-Schranke von Zhu/Li (~3e-17 eV) ist rund 14 Groessenordnungen schwaecher als die Laborschranke.
- **[H] Unsere Linien:** Die Glieder 2 und 5, an denen der Faktor-3-Befund haengt, beruehrt das nicht. Das ist unveraendert gegenueber dem Nachtrag vom 27.09.

---

## 6. Regime, Unterscheidungspunkte, Gegensweep, Kalibrierung, offene Fragen

### 6.1 Unterscheidungspunkte (Feldregel 2)

- **Stelle-Zwei-Term gegen Einzel-Yukawa [H]:**
  - In Regime A sind beide bei heutigen Abstaenden (>= 52 um) praktisch nicht zu unterscheiden. Unterscheiden liessen sie sich erst bei Abstaenden r <~ 1/m2 ~ 36 um bei Gravitationsstaerke. Das ist heute unzugaenglich, weil Eot-Wash bei 52 um endet.
  - In Regime B ist der Vorzeichenwechsel der Abweichung bei r* das Unterscheidungsmerkmal. Dafuer braucht man eine Messung, die das Vorzeichen in Abhaengigkeit vom Abstand aufloest.
- **Stelle gegen Pszota-Gradiententheorie [E/H]:**
  - Bei Stelle sind die Amplituden fest (1/3, -4/3) und die Reichweiten frei.
  - Bei Pszota sind die Amplituden durch die Reichweiten festgelegt.
  - Beide fallen bei m0 = 2 m2 zusammen.
  - Unterscheidbar sind sie erst, wenn zwei Yukawa-Terme mit Amplitude und Reichweite gemessen werden. Bis dahin sind sie empirisch nicht unterscheidbar.

### 6.2 Gegensweep (Feldregel 4)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- **G1 Atominterferometrie im Fenster: geprueft (arXiv).** Nur Vorschlaege und Theorie (Banks u. a. 2511.09750, Millington/Udemba 2606.28423 u. a.), keine Sub-mm-Schranke.
- **G3 HUST ausserhalb arXiv: geprueft (Crossref, OpenAlex, Murata-Zitate).** Keine neue HUST-Messung; juengste ist Ke u. a. 2021 (PRL 126, 211101, Zentimeterbereich).
- **G5 "Gravitationsstaerke" heisst |alpha| = 1: geprueft.** Lee-tex, Abstract-Satz: "gravitational-strength Yukawa interactions to ranges < 38.6 um" [S].
- **G2 offen:** Gilt die 38,6-um-Schranke auch fuer negatives alpha? Lee zeigt |alpha|; die Vorzeichentrennung steht nur im nicht abrufbaren Supplement. Venugopalan gibt beide Vorzeichen getrennt an [S].
- **G4 halb geprueft:** Lee normiert als V = V_N (1 + alpha e^(-r/lambda)) (tex Z. 43) [S]. Die Stelle-Koeffizienten aus Lue/Perkins/Pope/Stelle 2015, Gl. (4.7), habe ich hier nicht neu gelesen; ich uebernehme sie aus der Karte.
- **Ungeprueft:**
  - ob Konferenzbeitraege oder Dissertationen ein neueres Eot-Wash-Ergebnis enthalten. Die kryogene Torsionswaage von Fleischer u. a. (RSI 2022) koennte dafuer gedacht sein [L?].
  - chinesischsprachige Zeitschriften.

### 6.3 Kalibrierung (gemessen / verdichtet / nur gewachsene Gewissheit)

- **(a) Gemessen:**
  - Lee 2020: |alpha| = 1, lambda < 38,6 um, 95 %.
  - Venugopalan 2024/2026: alpha ~ 1e6-1e7 bei 5-100 um, 95 % je Vorzeichen.
- **(b) Nuetzlich verdichtet:**
  - Ablesungen fuer |alpha| = 4/3 und 1/3 aus Abb. 5, nach Augenmass mit etwa +/- 5 % in lambda.
  - die Massenumrechnungen
  - die Regime A/B
- **(c) Nur gewachsene Gewissheit:**
  - "38,6 um ist noch der Rekord" beruht auf Fehlanzeigen in fuenf Kanaelen (arXiv-API, OpenAlex, Crossref, INSPIRE, Eot-Wash-Seite) plus einer Uebersicht von 09/2026; Semantic Scholar fiel aus. Das ist negative Evidenz.
  - Warnzeichen: Meine Sicherheit fuer S2 stieg im Lauf, waehrend die eigentliche Frage nach der Stelle-Massenschranke feiner zerfiel: zwei Massen, zwei Regime, Vorzeichenvorbehalt. Die Antwort auf die Karte ist sicherer geworden; die Antwort auf Glied 10 ist unschaerfer geworden.

### 6.4 Offene Fragen

1. Die +alpha/-alpha-Schranken von Lee 2020 (Supplement PRL 124, 101101; braucht APS-Zugang). Das entscheidet die Vorzeichenfrage fuer den -4/3-Term.
2. Eine gemeinsame Zwei-Term-Auswertung fuer Regime B (m0 < m2) mit Lees Drehmomentmodell. Das ist ein Rechenauftrag, keine Literaturfrage, und nach Recherchestand nirgends veroeffentlicht.
3. Gibt es ein laufendes Eot-Wash-Nachfolgeexperiment unter 52 um? Fleischer u. a. 2022, kryogene Torsionswaage [L?]. Status unbekannt.
4. Die Projektion von van Manen u. a. 2026 (bis ~20 meV, arXiv:2609.22501; schon im Nachtrag 27.09.) bleibt ein Vorschlag. Sie ist nicht in diesem Lauf geprueft.

---

## 7. Suchprotokoll und Grenzen

Abrufzeiten nach date (CEST, 02.10.2026). Einzelerwartungen und Ausgaenge je Abruf stehen in `ARBEITSFELD.md`, Abschnitt 3.

| Block | Zeit (Erwartung geschrieben) | Abfragen | Ergebnis / Fehlschlag |
|---|---|---|---|
| 1 | 19:04:35 | arXiv: "inverse-square"+submillimeter; "short-range gravity"; Yukawa+"torsion pendulum"; "non-Newtonian gravity"+micrometer | Phrasen mit Bindestrich greifen schlecht (6/3/2 Treffer), Kanal teilweise untauglich |
| 2 | 19:05:30 | arXiv "inverse square law"+gravitational; Casimir+Yukawa; OpenAlex frei (2x) | Murata, Pszota gefunden; OpenAlex-Freitext: 560/570 Treffer, nur 3 ausgegeben |
| 3 | 19:06:37 | arXiv abs Murata, Pszota, Zhu; OpenAlex title_and_abstract | OpenAlex: 2790 Treffer, Zenodo-Rauschen |
| 4 | 19:07:58 | Murata-HTML, Pszota-HTML; au:Adelberger/Heckel; au:Shao/Tan/Luo (HUST) | keine neue UW-/HUST-Messung |
| 5 | 19:09:43 | au:Gratta, au:Decca, au:Sedmik, au:Abele | Venugopalan gefunden |
| 6 | 19:10:24 | Venugopalan abs; Semantic Scholar; neutron+Yukawa; inverse+square+torsion | Semantic Scholar HTTP 429 (Fehlschlag) |
| 7 | 19:11:20 | Crossref (2x); "quadratic gravity"+Yukawa; Stelle+Newtonian+potential | letzte Abfrage untauglich (1 Treffer) |
| 8 | 19:12:19 | Crossref-DOIs (2x); au:Hoyle_C; levitated+Yukawa | PRD-TOBA ohne Metadaten |
| 9 | 19:13:06 | "torsion bar"+Yukawa; OpenAlex "inverse-square law"+torsion; Lee-PDF; Murata-Abbildungen (curl) | TOBA = CHRONOS-Vorschlag |
| 10 | 19:15:13 | Lee-Quellpaket (e-print), Fig. 5 | Supplement nicht enthalten |
| 11 | 19:16:27 | APS-Supplement; Venugopalan-HTML; Fiorillo; "quadratic gravity"+laboratory | APS HTTP 401 (Fehlschlag) |
| 12 | 19:17:09 | Stelle+Yukawa; "Lee-Wick"+gravity+potential; "higher-derivative"+Yukawa+gravity | Stelle+Yukawa: nur Fluid-Arbeiten (untauglich) |
| 13 | 19:17:44 | Pszota-Wortlaut (curl); Balfagon abs | - |
| 14 | 19:18:30 | Gegensweep: "atom interferometer"+"fifth force"; Crossref Torsionspendel | nichts Neues |
| 15 | 19:19:18 | INSPIRE-HEP Titel; Eot-Wash-Publikationsseite | nichts Neues |

**Grenzen:**
- WebSearch war erschoepft; nur API-Kanaele.
- Semantic Scholar fiel aus (429).
- Die arXiv-Phrasensuche ist lueckenhaft (Bindestriche, Namensgleichheit Stelle/Stell).
- Volltext-Auszuege kamen teils ueber WebFetch-Zusammenfassung. Wortlaut habe ich nur bei Lee (PDF, tex), Pszota und Murata (curl|sed) selbst geprueft.
- Die Ablesungen aus Abb. 5 sind nach Augenmass auf Log-Achsen (etwa +/- 5 % in lambda).
- Die Abbildung von Venugopalan habe ich nicht selbst gesehen.
- Keine Rechnung ausser Kopfrechnung (hbar c = 1,973e-7 eV m).

---

## 8. Einfach gesagt

Man kann mit sehr feinen Drehwaagen pruefen, ob die Schwerkraft auf kurzen Abstaenden genauso wirkt wie im Grossen. Die beste Messung stammt immer noch von 2020: Eine zusaetzliche Kraft, die so stark ist wie die Schwerkraft, muesste kuerzer als etwa 39 Mikrometer reichen, also duenner als ein halbes Haar. Seit Herbst 2024 gab es nur eine neue Messung, und die ist millionenfach zu ungenau, um daran etwas zu aendern. Die Theorie von Stelle sagt aber zwei Zusatzkraefte mit entgegengesetztem Vorzeichen voraus, die sich teilweise aufheben koennen. Fuer diesen Fall hat noch niemand die Messdaten richtig ausgewertet, und dort liegt die eigentliche Luecke.
