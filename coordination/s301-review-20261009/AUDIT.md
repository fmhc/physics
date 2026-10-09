# AUDIT: Was kann das Repo fuer Testteilchenbahnen und Periheldrehung? (S301-Review, 09.10.2026)

- Forschungs-Agent fuer claude-primary. Text ab 2026-10-09 20:00:55 CEST (date). Keine Rechnung, nur Lesen und Schreibtisch.
- Kennzeichen: [E] im Projekt gerechnet (Karte bzw. Ordner genannt), [M] Schreibtisch bzw. vorab ableitbar, [L] Literatur aus dem
  Gedaechtnis, [S] an der Quelle gelesen, [H] Hypothese, [P] Projektdatei gelesen.
- Suche (grep, mit den Pflicht-Ausschluessen, zusaetzlich ohne research-watch/scout): perihel, Praezession/praezession/precession,
  geodaet/geodät/geodesic, Testteilchen/test particle, Kepler, Lense/Thirring/frame dragging/gravitomagnet/Mitfuehrung/Mitführung,
  Shift/N^i/g_0i, PPN, TOV, Bahnintegr, leapfrog/verlet, Lichtablenkung/Shapiro. Treffer ausserhalb der Literaturordner gelesen:
  GR-PRUEFLISTE-v2, GRUNDGLEICHUNG-v3, beta-netz-v (ERGEBNIS, SCHWARZES-LOCH, KARTE, Code-Liste, lauf-69), impuls-netz-1,
  antigravity-nachbau-1, VERMERK-ANTIGRAVITY-20261007, RUNDE-46/47/48/49/50.md (Stellen), ueberleitung-kh-1/-v-1/-v-2 (Stellen),
  regulaer-v-1, RUNDE-52 (IDEE-02, BERICHTIGUNG-IDEE-02-07), gamma-netz-l/DOSSIER, fmhc-physics-public/STAND-UND-NAECHSTE-SCHRITTE.md.

## 1. Kurzfazit

1. **Eine Bahnintegration im Netz-Fernfeld gibt es nicht.** Kein Projektcode integriert Testteilchen- oder Geodaetenbahnen in
   einer aus dem Netz V gerechneten Metrik. Das einzige Skript mit Geodaete und Perihel (RUNDE-37/gravity_nearfield_collapse.py)
   setzt den 1/r^3-Term von Hand ein und ist laut Leitungsvermerk vom 07.10. nicht verwendbar [P].
2. **Die Periheldrehung ist bisher nur vorab abgeleitet, nicht gerechnet.** Der Faktor P = (2 + 2 gamma - beta)/3 aus den
   Netzwerten ist 0,993 bis 1,000 (Variante A) bzw. 1,017 (Bereich 1,000 bis 1,033, Variante B) (antigravity-nachbau-1, AG3) [M auf
   E-Werten]. Die Leitung hat selbst vermerkt: "Perihel-Folgerung ersetzt keinen Bahntest" (RUNDE-50.md, Z. 113) [P]. GR-Pruefliste
   Nr. 12 ist im Fernfeld "erfuellt" nur ueber diese Folgerung.
3. **"beta im Fernfeld 1,00 bis 1,02" ist eine Extrapolation aus Schalen bis r = 11,5 Gitterlaengen** (statisch, L = 16/24/32,
   Stoerungsrechnung zweiter Ordnung, auf 4e-6 gegen die nichtlineare Loesung geprueft). Es haengt an der Eichvariante: In der
   tatsaechlich geloesten KKT-Loesung (Variante B) ist beta = 0,95 +- 0,05, fuenfmal unschaerfer. Die raeumliche zweite Ordnung
   ist nicht bestimmt; die Eichgleichungen zweiter Ordnung sind auf dem Gitter nicht erfuellbar (Rest ~ r^-3) [E, beta-netz-v].

## 2. Tabelle: vorhanden [E] / vorab ableitbar [M] / fehlt

| Baustein | Stand | Fundstelle | Bemerkung |
|---|---|---|---|
| Newton-Grenzfall, statisch, erste Ordnung (1/r-Takt, A = 0,05627 l_P je Einheitsquelle) | [E] | MATERIE-NETZ-1, beta-netz-v Abschn. 4 | linear um flach |
| gamma = 1 (erste Ordnung) | [E] als Identitaet der isotropen Eichung (2,5e-16); physikalisch ueber Lichtablenkung: Takt und Laengen je zur Haelfte, 0,999 bis 1,001 | beta-netz-v Pkt. 4; RUNDE-50.md Z. 47-53 (licht-ablenkung-v) | γ ist damit ueber die Lichtablenkung gestuetzt, nicht nur Eichung |
| Lichtablenkung, Shapiro im Fernfeld | [E] ueber Brechungsindex n - 1 = -2 Phi (DEC-Licht), keine Strahlintegration in einer Metrik | licht-ablenkung-v (RUNDE-50.md Z. 47-53) | nicht gegengelesen |
| beta (zweite Ordnung im Takt) | [E] Fernfeld 1,00 bis 1,02 (A), 0,95 +- 0,05 (B); beta(r) ~ 1 - 10/r^3 in Gitterlaengen; Nahfeld 0,58 (2,6 l) bis 0,85 (3,5 l) | beta-netz-v Tab. 3 | ohne Karte, nicht gegengelesen; Massenrenormierung A2/A ~ 0,12 bis 0,17 |
| raeumliche zweite Ordnung (delta) | fehlt (Schalen 0,13 bis 1,77 bzw. -5,9 bis 4,4: nicht bestimmbar) | beta-netz-v Pkt. 4 | fuer 1PN-Perihel nicht noetig [L] |
| Periheldreh-Faktor (2 + 2 gamma - beta)/3 | [M] 0,993 bis 1,000 (A); 1,017 (1,000 bis 1,033) (B) | antigravity-nachbau-1 Abschn. 3.3 | setzt voraus, dass alle uebrigen PPN-Parameter null sind; auf dem Netz nicht gezeigt |
| Geodaeten bzw. Bahnintegration in der Netzmetrik | **fehlt** | - | Netzfelder (N_v, l_e) sind in lauf-69 nur als Schalenmittel gespeichert, nicht je Ecke |
| Periheldrehung als Netzrechnung (Bahn), mit Aufloesung | **fehlt** | - | - |
| Bahnlagenabhaengigkeit (Gitterorientierung) einer Bahn | **fehlt** fuer Bahnen; fuer Abstrahlung gerechnet: Kreisbahnen auf V mit J_iso abs(G - 1) <= 1,5e-5, Rest ~ (kl)^2 | impuls-netz-1, v1-aufhebung-1 (Vermerk) | Strahlung, nicht Bahnmechanik |
| Starkes Feld, statisch (Takt -> 0 vor Horizont, TOV-artig) | [E] | beta-netz-v/SCHWARZES-LOCH.md, bn_tov.py | kugelfoermige Quelle mit Druck; kein Horizont, keine Bahnen |
| Testkoerper = Q-Ball auf geodaetischer Bahn (Aequivalenzprinzip) | **fehlt**; metrische Kopplung mit Spannungsterm laut Grundgleichung v3 "Pflicht" | GRUNDGLEICHUNG-v3, Nachtrag 17:25:45 | Virialrest ~0,1 (a/R)^2 |
| Shift/gravitomagnetischer Sektor | [E] linear, langwellig, vor-v3-Traegheit | impuls-netz-1; siehe GRAVITOMAGNETISMUS.md | - |
| Netz-Kantenlaenge l (physikalische Skala) | nur Schranke: l < 1,6e-27 m (LHAASO, DEC-Licht auf V), Doppelbrechung grob a < ~2e-30 m [ES] | GR-PRUEFLISTE-v2 Z. 11; RUNDE-49.md (HOEHE-ISOTROP-1) | keine Festlegung aus der Wirkung |

## 3. Was traegt "beta im Fernfeld 1,00 bis 1,02"?

- Gemessen ist die lokale Takt-Quelle zweiter Ordnung gegen Einsteins Wert, je Schale (Probe R = 2 beta - 1 aus Lap n2 =
  (2 beta - 1) |grad n1|^2), auf unendliches Volumen extrapoliert (L = 16, 24, 32; Rest <= 0,0016 fuer r >= 4,5) [E].
- Die Zahl 1,00 bis 1,02 ist die Extrapolation r -> unendlich je nach Ansatz c/r^3 oder c/r^2; die letzte gemessene Schale ist
  r = 11,5 Gitterlaengen (1,004) [E].
- Sie gilt fuer Variante A (Takt-Quelle ohne den Eichrest M lam2). Die echte KKT-Loesung (B) gibt 0,95 +- 0,05, Schalen 0,88 bis
  1,05 [E].
- Vorab erwartet: Regge geht im Kontinuum in Einstein ueber (Wong 1971, Barrett/Williams 1988 [L, ungeprueft]); dann ist beta = 1
  im Fernfeld zu erwarten. **Was die Rechnung zeigt, ist also vor allem, dass die Gitter-Nichtlinearitaet von V das nicht
  verdirbt** (beta-netz-v Pkt. 5).
- Fuer Bahnen heisst das: Der 1PN-Faktor ist aus beta und gamma vorab ableitbar; eine Bahnrechnung pruefte die Kette (PPN-Lesart,
  Eichvariante, Massenrenormierung, Gitterorientierung), nicht neue Physik.

## 4. Skalen: S301 und S2 in Netz-Einheiten [M]

- r_g = G M/c^2 = 1476,6 m x 4,297e6 = 6,345e9 m (M aus 2607.12664 [S]).
- S301: r_p = 272 r_g = 1,73e12 m; p = a(1 - e^2) = 539,6 r_g = 3,42e12 m; Schwarzschild 6 pi r_g/p = 0,0349 rad = 2,00 Grad/Umlauf.
- S2 [L: a ~ 125,5 mas, e ~ 0,8846]: r_p ~ 2830 r_g, p ~ 5330 r_g, 6 pi r_g/p = 3,54e-3 rad = 12,2 Bogenminuten/Umlauf (passt zu "about
  12'" in 2607.12664 [S]).
- Mit l < 1,6e-27 m ist r_p/l > 1e39 (S301). Alle bekannten Gitterkorrekturen des Netzes skalieren mit (l/r)^2 (Dispersion,
  l = 4-Anteil) oder (l/r)^3 (beta(r)); sie sind fuer S301 kleiner als 1e-78 relativ. **Astrophysisch ist ein Bahntest deshalb
  ein Konsistenzcheck des Kontinuumslimes, kein Test von Gittereffekten.**
- Auf dem Gitter ist r_p/r_g frei: In der Stoerungsrechnung zweiter Ordnung waehlt man die Quellstaerke s so, dass U(r_p) = r_g/r_p
  den Zielwert hat. Der 1PN-Faktor haengt (bis auf 2PN-Reste ~ U ~ 4e-3 bei S301, ~3e-4 bei S2) nicht von r_p/r_g ab. Die
  Unterscheidung 272 gegen 3000 r_g betrifft also erst 2PN, und dafuer braucht man die dritte Ordnung, die nicht gerechnet ist.

## 5. Minimaler reproduzierbarer Schwarzschild-Referenztest mit Netzverfeinerung (Definition)

**Art: Konsistenzcheck.** Frage: Reproduziert die statische Netzloesung auf V, als effektive Metrik gelesen, die
1PN-Periheldrehung 6 pi G M/(c^2 p) im Grenzfall l/r_p -> 0, und welche der beiden Eichvarianten traegt die Bahn?

1. **Was gerechnet wird:**
   - Netzfelder: bn.py Modus pert (vorhandener Code, unveraendert) bei L = 32 und 40 (nur Quelle P0), mit einer zusaetzlichen Ausgabe der Felder
     je Ecke (mu1, mu2, a1, a2 bzw. psi). Kein Neulauf der beta-Auswertung selbst; nur die Felder werden neu geschrieben, weil
     lauf-69 sie nicht enthaelt.
   - Effektive Metrik: ds^2 = -N^2 dt^2 + psi^4 dx^2 mit N = 1 + s mu1 + s^2 mu2 und psi^4 aus dem konformen Anteil der
     Kantendehnungen je Ecke (nicht-konformer Rest 0,5 bis 1,2 % von a2 wird mitgefuehrt und als Fehler ausgewiesen).
   - Stufe 1 (Schalen, kugelsymmetrisch): Perihelvorschub per Quadratur fuer die Schalenprofile N(r), psi(r).
   - Stufe 2 (3D): zeitartige Geodaeten in der interpolierten Metrik (lokale quadratische Ausgleichsinterpolation ueber die
     2-Ring-Nachbarschaft; Gegenvariante P1), drei Bahnebenen (Normalen [001], [111], (1,2,3)).
   - Masse aus der Bahn selbst (Kepler-Periode der gleichen Bahn, wie in der Astrometrie), damit die Massenrenormierung A2/A
     nicht als Praezession erscheint.
2. **Bei welchen r_p/r_g:** U(r_p) = 1/272 (S301) und 1/3000 (S2) ueber die Quellstaerke s; e = 0,3 (Apozentrum 1,86 r_p), weil
   e = 0,983 auf einem Torus nicht passt. Das ist zulaessig, weil die 1PN-Formel nur ueber p von e abhaengt [L].
3. **Aufloesungen:** r_p/l = 3, 4, 6, 8 auf L = 40, Torusprobe gegen L = 32 fuer r_p/l <= 6 (Apozentrum <= L/2,5; Torus-Korrektur wie in
   beta-netz-v).
4. **Erwartete Konvergenzordnung [M/H]:** Die Abweichung von P_unendlich faellt wie (l/r_p)^q mit q zwischen 2 (Dispersion,
   l = 4-Anteil des Laplace) und 3 (beta(r) ~ 1 - 10/r^3). Die Bahnlagenabhaengigkeit faellt wie (l/r_p)^2 mit kubischem l = 4-Muster.
5. **Schranken:** P_unendlich aus den tatsaechlich geloesten Feldern (enthaelt den Eichrest, also Variante B) in [0,99; 1,01] erwartet (Kette A), scheitert ausserhalb [0,98; 1,05]; Lagenspanne bei r_p/l = 8 unter 1e-2 (Einzelheiten KARTE-S301-1).
   Messbezug zur Einordnung: S2 f_SP ~ 1,1 +- 0,1 (GRAVITY 2020/2024 [L]); S301 f_SP = 0,94 +- 0,88 [S].
6. **Kosten:** pert bei L = 24 mit drei Quellen 231 s, 539 MB (lauf-69/pert-L24.log); L = 40 mit einer Quelle geschaetzt ~6 min [M,
   Skalierung L^3]. Quadratur und Geodaeten: Sekunden. Alles ueber kleintest.sh, CPU-Spuren, je Lauf <= 10 min.

Die eingefrorene Kurzfassung steht in KARTE-S301-1.md.

## 6. Trennung Konsistenzcheck gegen neue Physik

| Frage | Art | Grund |
|---|---|---|
| Netz reproduziert 6 pi G M/(c^2 p) im Limes l/r -> 0 | Konsistenzcheck | Regge -> Einstein ist erwartet [L]; P aus beta, gamma vorab 0,993 bis 1,000 |
| Welche Eichvariante (A/B) traegt die Bahn | Konsistenzcheck mit offenem Ausgang | B liegt bis 1,033; eine Bahnrechnung entscheidet, ob der Eichrest physikalisch ist |
| Bahnlagenabhaengigkeit, beta-Nahfeld | Gittereffekt | ~ (l/r)^2 bzw. (l/r)^3; fuer S301 < 1e-78; kein Datenbezug |
| Abweichung von ART bei S301 oder S2 | neue Physik | wuerde eine physikalische Netzskala >> l < 1,6e-27 m oder einen skalenfreien Effekt verlangen; beides fehlt (VORZUGSRICHTUNG.md) |

## Einfach gesagt

Unser Netz kann bisher noch keine Sternbahn ausrechnen. Wir haben nur Zahlen fuer die Schwerkraft um eine ruhende Masse, und
aus denen folgt mit einer Lehrbuchformel, dass sich Bahnen wie bei Einstein drehen muessten. Das ist eine Folgerung, kein
Bahntest. Der vorgeschlagene Test rechnet die Bahnen wirklich im Netz und macht das Netz immer feiner. Er prueft, ob das Netz
richtig zu Einstein wird; neue Physik fuer S301 kann er nicht zeigen, weil die Netzmaschen dafuer viel zu klein sind.
