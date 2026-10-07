
Papier-Agent (Anthropic), Auftrag von claude-primary. Nur Papier: keine GPU, keine lokale Rechnung; alle Rechnungen von Hand,
Formeln stehen unten. Explorativ, keine formale Bestaetigung.

- Beginn: 2026-09-30 04:02:52 CEST (date)
- Ende: 2026-09-30 04:25:28 CEST (date, nach dem Schreiben gemessen)

Lesetiefe: **[A]** an der Quelle gelesen (PDF-Seite, PDF-Text oder Abstract), **[A-W]** Quelle ueber das Abrufwerkzeug gelesen
(Zusammenfassung eines Hilfsmodells, Wortlaut nicht selbst gesehen), **[S]** nur Suchtreffer, **[L]** Lehrbuch bzw.
Gedaechtnis, **[P]** Projektdatei, **[E]** eigene Handrechnung, **[ES]** eigener Schluss.

## Kurzantwort

- **MT-1:** Die drei Bilder hinterlassen verschiedene Fingerabdruecke.
  - KK-Turm: +8n/3 je erster Stufe, fuer n = 1 dieselbe Staerke +8/3 bei lambda = R, R/2, R/3 und so weiter.
  - Stelle: genau zwei Terme, -4/3 (Spin-2-Geist) und +1/3 (Skalar); bei r -> 0 heben sie Newton auf (netto -1).
  - Skalar: ein Term mit alpha > 0; universell an die Spur gekoppelt 1/3, sonst frei und oft stoffabhaengig.
- **Behauptung "Literatur 2n statt 8n/3, Differenz = vDVZ 4/3":** Nur halb richtig.
  - 2n steht bei Kehagias/Sfetsos (Newtonsche Poisson-Rechnung) und in der Uebersicht Murata u. a. 2026.
  - 8n/3 steht bei Adelberger/Heckel/Nelson 2003 und Adelberger u. a. 2009, dort mit genau der vDVZ-Begruendung.
  - Eine Fussnote von 2003 fuehrt die 2n auf ein masseloses Radion zurueck. Der Befund ist also nicht neu.
- **Eoet-Wash heute (Lee u. a. 2020):** Kein Vorzeichen ist ausgeschlossen. Begrenzt ist nur die Reichweite: lambda < 38,6 um
  bei |alpha| = 1, groesste Extradimension R* < 30 um. Die vorzeichengetrennten Kurven (Supplement) waren nicht lesbar.
  - Eine gleichmaessige Koernung muesste unter 2e-36 m (linear) bzw. 3e-28 m (quadratisch) liegen, also 13 bis 21
    Zehnerpotenzen unter 1 fm.
- **Vorschlag:** MT-1 parken (Referenzkarte), V1 in M-THEORIE-CALABI-YAU.md durch die Leitung berichtigen. V-3 als Konfliktfrage
  verwerfen, die Mechanismusfrage parken.

## Erwartungsverstoesse (das Wichtigste zuerst)

1. **Die Literatur ist gespalten, und eine Uebersicht von 2026 steht auf der ausgeschlossenen Seite.**
   - Erwartet: Nach Adelberger 2003 verwendet das Feld 8n/3.
   - Gefunden: Murata, Fujiie und Suzuki (arXiv:2605.18212, ueberarbeitet am 08.09.2026) setzen alpha_1 = 2n nach
     Kehagias/Sfetsos, ohne Radion und ohne 4/3 [A-W].
   - Der Unterschied ist kein Fehler einer Seite, sondern eine Normierung (Regime, siehe MT-1). Der 2n-Grenzfall entspricht
     aber einem masselosen Radion, und das ist durch ART-Tests ausgeschlossen (Adelberger 2003, S. 17 [A]).
   - Erwartet: LHAASO sei die entscheidende Grenze (so rahmt die Karte).
     waere ein Delta-gamma-Effekt. Dafuer gilt Delta gamma < 2,1e-15 (1 sigma, 25 bis 325 keV; Bartlett u. a. 2021 [A]).
3. **Die LHAASO-Zahlen im Projekt sind falsch zugeordnet.**
   - VIDEO-6r1au5axOXM.md Z. 191 und LORENTZ.md Z. 63 schreiben "14,7e19 GeV (subluminal)" und "12,0e11 GeV" der
     Kollaborationsarbeit PRL 133, 071501 zu.
   - Diese Zahlen stammen aus einer unabhaengigen Auswertung (Yang, Bi, Yin, JCAP 04 (2024) 060 [A-W]).
   - Die PRL selbst gibt im Text 1,0e20 GeV (linear) und 6,9e11 GeV (quadratisch), beide subluminal [A].
   - Die Koernungszahlen der V-3-Karte (1,3e-36 m, 1,6e-28 m) beruhen auf den falsch zugeordneten Werten. Die Groessenordnung
     bleibt richtig.
4. **Die LHAASO-Front ist nicht geschlossen.**
   - Erwartet: keine LIV-Hinweise.
   - Gefunden: Ofengeim und Piran (2025) deuten ein 300-TeV-Photon von Carpet-3 als Hinweis auf quadratische subluminale LIV
     mit E_LIV2 = 1,30 (+0,56/-0,35) e-7 E_Pl [A-W].
   - Das liegt ueber der Kollaborationsgrenze (6e-8 E_Pl) und am Rand der unabhaengigen DisCan-Grenze (1,49e12 GeV, etwa
     1,2e-7 E_Pl; Hua u. a. 2025 [A]).
   - Zusatz Kollaborationspapier [A]: Das Abstract rundet zu "10 E_Pl". Im Text stehen 1,0e20 GeV, also 8,2 E_Pl bei
     E_Pl = 1,22e19 GeV (PDF-Text Z. 140 und Z. 465).
   Es meint keine Frequenzabhaengigkeit. Eine Stichwortsuche nach "dispersion" liefert dort einen falschen Treffer.

**Bestaetigte Erwartungen (je eine Zeile):**

- Kehagias/Sfetsos rechnen rein Newtonsch mit der (n+3)-dimensionalen Poisson-Gleichung: 2n fuer den Torus, n + 1 fuer die
  Sphaere, kein Radion, kein 4/3 [A].
- Adelberger 2003: 8n/3 mit vDVZ-Begruendung; Radion n/(n+2) [A].
- Adelberger 2009: 8n/3 und lambda = R* [A].
- Lee 2020 nennt zum KK-Turm kein alpha [A]. Das Supplement ist nicht abrufbar (HTTP 401).
- Seit Lee 2020 gibt es keine staerkere Schranke bei 30 bis 50 um (Murata u. a. 2026 [A-W]).
- LHAASO-Abstract: 10 E_Pl und 6e-8 E_Pl [A].
- Stelle-Newtongrenze +1/3 und -4/3 (Lue u. a. 2015, Gl. 4.7a [A]).

---

## Karte MT-1: Yukawa-Fingerabdruck von Turm, Geist und Skalar

### Vorhersage vor der Lektuere (Feld-Regel 3)

- Kehagias/Sfetsos rechnen Newtonsch (2n).
- Die Eoet-Wash-Uebersichten nennen 8n/3 samt 4/3-Begruendung.
- Lee 2020 nennt kein alpha.
- Stelle: +1/3 und -4/3.
- Heute erlaubt ist fuer jedes Vorzeichen nur lambda unter etwa 30 bis 50 um.

### Rechnung von Hand (Formeln)

Parametrisierung: V(r) = -G m1 m2 / r * (1 + alpha exp(-r/lambda)).

**(a) KK-Turm, Zerlegung der 5D-Summe (n = 1), [E] mit Lehrbuchbausteinen [L]:**

- Statischer Austausch zwischen Branen-Quellen in D = 4 + n Dimensionen: T_MN T'^MN - T T'/(D-2), also rho rho' (n+1)/(n+2)
  je KK-Impuls, auch fuer die Nullmode.
- In 4D gilt: masseloses Graviton rho rho'/2, massiver Spin 2 (Fierz-Pauli) rho rho' 2/3. Das Verhaeltnis 4/3 ist der
  vDVZ-Faktor (Glied 8; Hinterbichler Gl. 3.26 nach WARUM-SPIN-2.md [P]).
- n = 1: V_5D = -(2/3) K/r * Sum_j exp(-|j| r/R). Die Nullmode 2/3 zerfaellt in 1/2 (Graviton) und 1/6 (Radion).
  - **Radion schwer:** G_N entspricht K/2. Jede Mode j != 0 hat alpha = (2/3)/(1/2) = 4/3, jede Stufe (+j, -j) 8/3:
    V = -G_N M/r * [1 + (8/3)/(exp(r/R) - 1)]  (geometrische Reihe).
  - **Radion masselos:** G_N entspricht (2/3)K, also alpha = 2 je Stufe. Das ist Kehagias/Sfetsos.
  - Radion allein: (1/6)/(1/2) = 1/3. Allgemein [(n+1)/(n+2)]/(1/2) - 1 = n/(n+2), wie bei Adelberger 2003, S. 18 [A].
- **Gegenprobe der Karte (r -> 0):** Die Summe geht gegen R/r, also V -> -(8/3) G_N M R/r^2. Die Newtonsche 5D-Extrapolation
  gibt 2 G_N M R/r^2. Das Verhaeltnis ist 4/3 = (2/3)/(1/2). **Bestanden.**
- **n >= 2 [ES]:**
  - Adelberger zaehlt nur den Spin-2-Anteil: 8n/3.
  - Mit der vollen D-dimensionalen Struktur (Giudice/Rattazzi/Wells, T_mn T^mn - T^2/(n+2) [L], nicht nachgelesen) tragen auch
    die KK-Skalare bei: 2n * 2(n+1)/(n+2) = 4n(n+1)/(n+2). Das ist die Formel des M-Theorie-Agenten.
  - n = 2: 16/3 gegen 6. Fuer n = 1 sind beide gleich (keine KK-Skalare).

**(b) Stelle, [A] an Lue, Perkins, Pope, Stelle 2015, Gl. (4.7a):**

- V proportional zu -(M/r)(3 + exp(-m0 r) - 4 exp(-m2 r)), also 1 + (1/3) e^(-m0 r) - (4/3) e^(-m2 r).
- m2 gehoert zum massiven Spin-2-Geist, m0 zum massiven Skalar, der kein Geist ist (ebd., Einleitung [A]).
- r -> 0: 1 + 1/3 - 4/3 = 0. Das Potential bleibt endlich, alpha_eff -> -1 (ebd.: V nichtsingulaer [A]).

**(c) Skalar:**

- Massives Brans-Dicke-Feld: alpha = 1/(3 + 2 omega) [L]. f(R) entspricht omega = 0, also alpha = 1/3. Das ist derselbe
  Skalar wie der R^2-Term bei Stelle und wie das Radion fuer n = 1.
- Skalaraustausch zieht gleichartige Koerper an, Spin 1 stoesst ab (Adelberger 2003, S. 22 [A]).

### Ergebnis: Tabelle

| Bild | alpha | Vorzeichen | lambda-Bezug | heute erlaubt? (Lee 2020) | Unterscheidungsmerkmal |
|---|---|---|---|---|---|
| KK-Turm, n kompakte Dimensionen (Glied 8) | erste Stufe 8n/3 (Radion schwer; Adelberger 2003/2009 [A]); 2n bei masselosem Radion (Kehagias/Sfetsos [A], ausgeschlossen); n = 1: jede Stufe j wieder 8/3; dazu ein Radionterm n/(n+2) mit eigener Reichweite | + | lambda_j = R/j (n = 1); lambda_1 = R* = Compton-Laenge der leichtesten KK-Mode | ja, wenn R* < 30 um (Lee [A]; alpha dort nicht genannt, UW-Konvention 8/3 [ES]) | unendliche Summe gleich starker Terme bei R, R/2, ...; fuer r < R steigt alpha_eff wie (8/3) R/r (Uebergang zu 1/r^(2+n)); stoffunabhaengig |
| Stelle, R^2 + Weyl^2 (Glied 10) | -4/3 (Spin-2-Geist, m2) und +1/3 (Skalar, m0) [A] | gemischt; netto -1 bei r -> 0 | zwei unabhaengige Reichweiten: lambda2 = hbar/(m2 c), lambda0 = hbar/(m0 c) | ja, wenn beide kurz genug sind; einzeln interpoliert etwa lambda2 < 36 um (5,5 meV) und lambda0 < 50 um (4 meV) [ES]; eine gemeinsame Auswertung fehlt | genau zwei Terme mit festen Zahlen; Vorzeichenwechsel mit r, wenn m0 < m2; endliches Potential bei r -> 0; stoffunabhaengig |
| reiner Skalar (Glied 5) | frei: universell an die Spur 1/(3+2 omega), f(R) 1/3; Radion n/(n+2); Dilaton und Moduli bis weit ueber 1 (Lee Fig. 5, Theoriebaender) | + (gleichartige Koerper) | eine freie Reichweite hbar/(m c) | ja, wenn lambda < 38,6 um bei alpha = 1 (Dilaton m > 5,1 meV [A]); bei alpha = 1/3 etwa < 50 um [ES] | ein einziger Term ohne Partner; bei nicht-universeller Kopplung stoffabhaengig (EP-Test, Dilaton etwa 0,3 % nach Kaplan/Wise, zitiert bei Adelberger 2003 [A]) |

Zusatz zur Form:

- Ein Randall-Sundrum-II-Szenario gibt ein Potenzgesetz statt eines Yukawa-Terms: V = G m1 m2/r * (1 + 1/(r^2 k^2))
  (Adelberger 2003, S. 21 [A]).
- Ein negatives alpha hat mindestens zwei Wege, den Stelle-Geist und einen Spin-1-Vektor. Das Vorzeichen allein ist also nicht
  diagnostisch (Regel 6).

### Pruefung der Behauptung des M-Theorie-Agenten (V1)

- **"Die Literatur nennt 2n statt 8n/3": als Pauschalaussage falsch.**
  - Kehagias/Sfetsos [A]: "the strength of the potential is alpha = 2n".
  - Floratos/Leontaris 1999 [S] und Murata u. a. 2026 [A-W] sagen ebenfalls 2n.
  - Adelberger/Heckel/Nelson 2003, S. 16 [A] geben dagegen alpha = 8n/3 und lambda = R*.
  - Adelberger u. a. 2009, Abschn. 3.4.1 [A] schreiben: "well approximated by a single Yukawa interaction with alpha = 8n/3
    and lambda = R*".
  - Lee 2020 zitiert fuer die 30 um genau Adelberger 2003 [A].
- **"Die Differenz ist der vDVZ-Faktor 4/3": richtig, aber seit 2003 publiziert.**
  - Adelberger 2003 begruendet die 4/3 woertlich: "a massive spin-2 particle has five polarization states, and the
    longitudinal mode does not decouple".
  - Dessen Fussnote 1 nennt als Grund fuer das andere alpha der Refs. 81/82 (Kehagias/Sfetsos, Floratos/Leontaris) ein
    masseloses Radion im Newton-Potential und Radion-KK-Moden im Yukawa-Term [A].
  - Die Zerlegung des M-Theorie-Agenten [ES] reproduziert das fuer n = 1 exakt. Fuer n >= 2 bleibt ein Unterschied
    (8n/3 gegen 4n(n+1)/(n+2)); er haengt an den KK-Skalaren und ist nicht an einer Quelle geklaert.

### Regime und Moderatoren (Regel 1)

- **2n gegen 8n/3: Moderator ist die Reichweite lambda_r des Radions relativ zum Messabstand r und zum Eichabstand von G** [ES].
  - Gilt lambda_r >> r >> R, wirkt das Radion lokal masselos. Relativ zur lokalen Staerke (4/3 G_N fuer n = 1) sieht der
    KK-Term dann wie alpha = 2 aus (Kehagias/Sfetsos).
  - Gilt lambda_r << r, ist alpha = 8/3 relativ zu G_N (UW-Konvention). Lee eicht G an Kugeln auf der cm-Skala (Fig. 2 [A]).
  - Ein Radion mit alpha = 1/3 und lambda_r ueber etwa 50 um waere von denselben Daten ausgeschlossen [ES, Interpolation],
    ein masseloses von ART-Tests [A]. Fuer Lees Normierung ist 8n/3 deshalb der konsistente Parameter, 2n der formale Grenzfall
    eines ausgeschlossenen Falls.
- **n >= 2: zweiter Moderator.** Ob die KK-Skalare mitzaehlen, entscheidet zwischen 8n/3 und 4n(n+1)/(n+2) [ES].
- **Kopplungsgroesse statt Bauteil (Regel 6) [ES]:** Alle Bilder sind Formen einer Groesse, der Spektraldichte rho(m) der
  ausgetauschten Zustaende: alpha_eff(r) = Integral rho(m) exp(-m r) dm.
  - Turm: ein Kamm gleicher Gewichte (8/3 bei m = j/R).
  - Stelle: zwei Deltas (+1/3, -4/3).
  - Skalar: ein Delta.
  - RS-II: ein Kontinuum (Potenzgesetz).
  - Die Summenregel alpha_eff(r -> 0) trennt die Bilder: Turm -> unendlich, Stelle -> -1, Skalar -> alpha.
  - Massiver Spin 2 traegt immer |4/3|, das Vorzeichen sagt "gesund" (+) oder "Geist" (-). Ein spurgekoppelter Skalar traegt
    1/3.

### Unterscheidungspunkte (Regel 2)

| Paar | wo sie messbar auseinanderlaufen | heute zugaenglich? |
|---|---|---|
| Turm gegen Skalar | zweiter Term bei lambda/2 mit gleicher Staerke (n = 1); Stoffabhaengigkeit | Nein. Der zweite Term braucht Abstaende um lambda/2, also unter etwa 15 um bei alpha ~ 3. Lee kam wegen Vibrationen nicht unter 52 um [A]. Der EP-Test ist im Prinzip moeglich (Adelberger 2003, Abschn. 5.3 [A]). |
| Stelle gegen Turm | negatives alpha, oder Vorzeichenwechsel zwischen lambda0 und lambda2 (m0 < m2) | Nein, fuer |alpha| ~ 1 ist der Bereich ueber etwa 30 bis 40 um schon ausgeschlossen. |
| Stelle gegen Vektor (beide alpha < 0) | |alpha| = 4/3 fest, stoffunabhaengig, Partnerterm +1/3; der Vektor ist meist stoffabhaengig | EP-Test ja; Partnerterm nein |
| 8n/3 gegen 2n | nur ueber einen eigenen Radionterm (1/3) zwischen R und lambda_r | nein |
| alle drei bei r << lambda | Turm Potenzgesetz, Stelle endliches V (-1), Skalar 1 + alpha | nein, praktisch unzugaenglich |

Ergebnis: Heute unterscheiden die Daten die drei Bilder nicht. Sie schliessen nur grosse Reichweiten fuer alle drei aus.

### Heute erlaubt: Vorzeichen und Staerken

- **Textanker [A]:**
  - Jede Yukawa-Wechselwirkung gravitativer Staerke hat lambda < 38,6 um (95 %).
  - Groesste Extradimension: Torusradius < 30 um.
  - Dilaton bzw. schweres Graviton: m > 5,1 meV.
  - Radion-Vereinheitlichungsmasse > 7,1 TeV.
  - Bester Fit: lambda = 7,1 um mit Delta chi^2 = 3,3, kein Signal behauptet.
- **Vorzeichen:**
  - Fig. 5 zeigt nur |alpha|. Die Grenzen fuer +alpha und -alpha stehen im Supplement (Abruf: HTTP 401, nicht gelesen).
  - Murata u. a. 2026 zeigen nur alpha > 0 und nennen die Empfindlichkeit fuer alpha < 0 "qualitativ analog" [A-W].
  - Nach Recherchestand ist also **kein Vorzeichen bevorzugt ausgeschlossen**, eine genaue Vorzeichenasymmetrie ist nicht belegt.
- **Zwischenwerte, grob interpoliert [ES], keine Ablesung:**
  - Modell: alpha_max(lambda) ~ (38,6 um/lambda)^2 exp[s_eff (1/lambda - 1/38,6 um)], s_eff = 64 um.
  - s_eff ist an die zwei Anker angepasst: 1 bei 38,6 um [A], 8/3 bei 30 um. Die Zuordnung alpha = 8/3 zu den 30 um ist
    UW-Konvention [ES].
  - |alpha| = 4/3: lambda < etwa 36 um (m > 5,5 meV).
  - alpha = 2: etwa 32 um.
  - alpha = 1/3: etwa 50 um (+-10 um; hier greifen andere Datensaetze, das Modell ist dort unsicher).
  - alpha = 16/3 (n = 2 nach Adelberger): etwa 26 um.
  - Fuer n = 2 mit M* ~ TeV liegt R* ohnehin unter 0,7 um (SN 1987A, Adelberger 2003, S. 16 f. [A]).
- **Stelle:**
  - Der Fall m0 = m2 ist ein einziger Term mit alpha = -1, also lambda < etwa 38,6 um, falls die -alpha-Kurve der
    +alpha-Kurve gleicht.
  - Sonst braucht es eine gemeinsame Zwei-Term-Auswertung mit Apparateantwort (wie im Nachtrag vom 29.09. in WARUM-SPIN-2.md).

### Belege MT-1

| Quelle | Lesetiefe |
|---|---|
| Kehagias, A.; Sfetsos, K. (1999/2000): *Deviations from the 1/r^2 Newton law due to extra dimensions*. Phys. Lett. B 472, 39. [arXiv:hep-ph/9905417](https://arxiv.org/abs/hep-ph/9905417) | [A] S. 1 bis 5, Gl. 2, 6, 10, 14, 23, Fn. 1 |
| Adelberger, E. G.; Heckel, B. R.; Nelson, A. E. (2003): *Tests of the gravitational inverse-square law*. Ann. Rev. Nucl. Part. Sci. 53, 77. [arXiv:hep-ph/0307284](https://arxiv.org/abs/hep-ph/0307284) | [A] S. 13 bis 22 (Abschn. 2.2, 2.4), Fn. 1, Abschn. 5.3, Refs. 79 bis 85 |
| Adelberger, E. G.; Gundlach, J. H.; Heckel, B. R.; Hoedl, S.; Schlamminger, S. (2009): *Torsion balance experiments: A low-energy frontier of particle physics*. Prog. Part. Nucl. Phys. 62, 102. [PDF](https://gwern.net/doc/science/physics/2009-adelberger.pdf), [Verlag](https://www.sciencedirect.com/science/article/abs/pii/S0146641008000720) | [A] Gl. 18, Abschn. 3.4.1 |
| Lee, J. G.; Adelberger, E. G.; Cook, T. S.; Fleischer, S. M.; Heckel, B. R. (2020): *New Test of the Gravitational 1/r^2 Law at Separations down to 52 um*. PRL 124, 101101. [arXiv:2002.11761](https://arxiv.org/abs/2002.11761) | [A] lokale PDF v1, S. 1 bis 5 (coordination/zusatzdimension-20260924/quellen-messlage/); Supplement nicht gelesen (HTTP 401) |
| Murata, J.; Fujiie, T.; Suzuki, S. (2026): *Short-Range Tests of the Gravitational Inverse-Square Law*. [arXiv:2605.18212](https://arxiv.org/abs/2605.18212) | [A] Abstract; [A-W] Text |
| Lue, H.; Perkins, A.; Pope, C. N.; Stelle, K. S. (2015): *Spherically Symmetric Solutions in Higher-Derivative Gravity*. [arXiv:1508.00010](https://arxiv.org/abs/1508.00010) | [A] PDF-Text, Einleitung und Gl. 4.7a |
| Floratos, E. G.; Leontaris, G. K. (1999): Phys. Lett. B 465, 95 | [S] nur als Ref. 82 bei Adelberger 2003 |
| Giudice, G. F.; Rattazzi, R.; Wells, J. D. (1999): Nucl. Phys. B 544, 3 (arXiv:hep-ph/9811291) | [L] nicht nachgelesen |
| Projekt: M-THEORIE-CALABI-YAU.md (V1, MT-1), VIDEO-6r1au5axOXM.md (V-2), WARUM-SPIN-2.md (Glieder 5, 8, 10; Nachtraege 27.09. und 29.09.) | [P] |

### Latten MT-1

- **L1 (kann scheitern):**
  - Ja. Die Zerlegung haette nicht 4/3 je Mode geben koennen.
  - Fuer n = 1 gab sie 4/3, und Adelberger 2003 stuetzt das [A].
  - Fuer n >= 2 ist 4/3 je Stufe nicht eindeutig (KK-Skalare).
- **L2 (Grenzfaelle):**
  - Der r -> 0-Grenzfall gibt das 5D-Gesetz mit Faktor 4/3: bestanden.
  - Stelle bei r -> 0 endlich: bestanden [A].
  - Radion n/(n+2) aus (n+1)/(n+2): bestanden [A].
- **L3 (Genauigkeit):**
  - Die Textanker sind exakt.
  - Die interpolierten lambda_max sind auf +-10 bis 20 % unsicher.
  - Vorzeichengetrennte Kurven fehlen.
- **L4 (Literatur):**
  - Alles Wesentliche ist bekannt: Adelberger 2003 (8n/3, 4/3, Radion), Lue u. a. 2015 (Stelle), Kehagias/Sfetsos (2n).
  - Neu sind nur die Gegenueberstellung, die Regime-Lesung ueber lambda_r und die Spektraldichte-Sicht [ES].
- **L5 (Messbezug):**
  - Ja: Lee 2020.
  - Eine Trennung der Bilder braucht Abstaende unter 52 um.

### Vorschlag MT-1

- **Parken** als Referenzkarte, weil keine Rechnung offen ist.
- Die Leitung sollte in M-THEORIE-CALABI-YAU.md V1 berichtigen: 8n/3 steht bei Adelberger 2003 und 2009, 2n bei
  Kehagias/Sfetsos, Floratos/Leontaris und Murata 2026; Moderator ist die Radion-Reichweite.
- WARUM-SPIN-2.md habe ich nicht angefasst.
- Weiter nur, wenn die +alpha/-alpha-Kurven verfuegbar werden (PRL-Supplement oder Dissertation J. G. Lee 2020, UW, Ref. 19
  bei Lee). Dann folgt eine Papierauswertung des Stelle-Paars (zwei Terme, entgegengesetzte Vorzeichen).

---


### Vorhersage vor der Lektuere (Feld-Regel 3)

  Konflikt.
- LHAASO: E_QG,1 > etwa 10 E_Pl, E_QG,2 > etwa 6e-8 E_Pl.

### Ergebnis


  Gleichung auf das Shapiro-Experiment von 1970 und merkt an, sie folge auch aus der ART.
- Gl. (6.3), Z. 500 bis 520: c_eff = c (1 - g N/(c^2 r))^p, mit Quellteilchenzahl N und eigener Konstante g.
- Mechanismus, Z. 435 bis 444: Austauschteilchen des Bindungsfeldes lenken lichtartige Teilchen zufaellig ab (Random Walk).
  Die mittlere Geschwindigkeit sinkt, "its microscopic speed is still the speed of light c".
- **In keiner Formel steht eine Groesse der Probe** (Energie, Frequenz, Wellenlaenge). "dispersion" steht nur als dc/dy
  (Z. 802).
- Webseiten-Volltext und alle pdf/*.txt: keine Aussage zu energieabhaengigem c (grep [A]).
- Websuche: keine [S].
  (Glied 2/3), nicht die Ausbreitung.

**2. LHAASO-Grenzen [A], 95 %, v = c[1 - s (n+1)/2 (E/E_QG,n)^n], s = +1 subluminal:**

| Quelle | linear (sub / super) | quadratisch (sub / super) | Lesetiefe |
|---|---|---|---|
| LHAASO-Kollaboration 2024, GRB 221009A, WCDA, Photonen 0,2 bis 7 TeV | 1,0e20 / 1,1e20 GeV (Abstract gerundet "10 E_Pl") | 6,9e11 / 7,0e11 GeV ("6e-8 E_Pl") | [A] Abstract und PDF-Text |
| Yang, Bi, Yin 2024 (unabhaengig, LHAASO-Daten 0,2 bis 13 TeV) | 14,7e19 / 6,5e19 GeV | 12,0e11 / 7,2e11 GeV | [A-W] |
| Hua, Bi, Yang, Yin 2025 (DisCan, WCDA + KM2A) | 21,1e19 / 13,8e19 GeV | 14,9e11 / 13,7e11 GeV | [A] Abstract |
| LHAASO-Kollaboration 2022, UHE-Photonen (Crab u. a.), nur superluminal (Photonzerfall) | > etwa 1e5 E_Pl | > 1e-3 E_Pl | [A] Abstract |
| Mrk-421-Flare 2014 (JCAP 07 (2024) 044, nach Suchtreffer kein LHAASO-Papier) | 2,7e17 / 3,6e17 GeV | 2,6e10 / 2,5e10 GeV | [S] |

- Eine Flare-Auswertung durch LHAASO habe ich nicht gefunden. Die Suche war kurz; das Ergebnis lautet "nicht gefunden",
  nicht "gibt es nicht".

**3. Konflikt: nein.**

- Eine energieunabhaengige Verlangsamung, auch eine grosse, verschwindet in der unbekannten Emissionszeit.


- **Im QG-1-Rahmen** (RUNDE-01.md Z. 45; L = A|dt psi|^2 - B|grad psi|^2 - C U [P]):
  - Eine masselose Welle (U = 0) hat omega^2 = (B/A) k^2, also v = c sqrt(B/A), unabhaengig von k.
  - Das gilt fuer alle Varianten A, B und C: **Ohne eigene Laengenskala entsteht keine Dispersion.**
  - Das ist der Unterschied zu QG-1: Ein Q-Ball bringt mit omega eine innere Skala mit, ein Photon nicht.
- **Mit einer Skala l** (Zusatz -+ l^2 (grad^2 psi)^2, derselbe Typ wie der UV-Term der Karte V-1):
  - omega = c k (1 -+ l^2 k^2)^(1/2), also v_g = c (1 -+ (3/2) l^2 k^2).
  - Das ist genau LHAASOs quadratische Form mit E_QG,2 = hbar c / l. Linear gilt analog E_QG,1 = hbar c / l.
- **Gleichmaessige Koernung** (hbar c = 1,973e-16 GeV m):
  - linear: l < 1,973e-16 / 1,0e20 = 2,0e-36 m (DisCan: 9,4e-37 m)
  - quadratisch: l < 1,973e-16 / 6,9e11 = 2,9e-28 m (DisCan: 1,3e-28 m)
  - Gegen 1 fm sind das Faktoren 5e20 bzw. 3e12. Eine hadronische Skala waere schon bei GeV-Energien offensichtlich.
  - Bartlett u. a. 2021: Delta gamma < 2,1e-15 (1 sigma, 25 bis 325 keV, Shapiro-Verzoegerung mit grossraeumiger Struktur) [A].
  - Ueberschlag fuer LHAASO [E]:
    - Laufzeitaufloesung etwa 5 TeV Energiehebel / 1,0e20 GeV x K(z)/H0 (etwa 7e16 s), also etwa 3 s.
    - Milchstrassen-Shapiro etwa 2GM/c^3 ln(d/b), etwa 6,7e7 s (M = 6e11 Sonnenmassen, ln etwa 11,4).
    - Daraus folgt Delta gamma(0,3 bis 5 TeV) < etwa 1e-7.
- **Kausalitaet [ES, mit L: Kramers-Kronig, Jackson Kap. 7.10]:**
  - "Mikroskopisch c, im Mittel langsamer" bedeutet Frontgeschwindigkeit c, also n(unendlich) = 1, und zugleich n(0) = c/c_eff > 1.
  - Ein lineares kausales Medium mit diesen Eigenschaften muss dispersiv sein und in einem Band absorbieren.
- **Gegenprobe (Karten-L2):**
  - Plasma: omega^2 = c^2 k^2 + omega_p^2 gibt v_g = c(1 - omega_p^2/(2 omega^2)), also Delta t proportional zu nu^-2
    (Dispersionsmass). Bestanden.
  - Vakuum: omega = c k gibt Delta t = 0. Bestanden.

### Regime und Moderatoren (Regel 1)


- (i) **metrikartig** (geometrische Brechung wie die optische Metrik der ART): keine Dispersion, kein LHAASO-Bezug.
  die Reichweite der Austauschteilchen unbegrenzt (Z. 465 bis 470).
- (iii) **an Materie gebundenes Medium** (proportional zu N/r): Delta-gamma-Grenzen.

### Unterscheidungspunkt (Regel 2)

- Fuer l ~ 1 fm laege das bei etwa 200 MeV und damit im Fermi- und LHAASO-Bereich.

### Belege V-3

| Quelle | Lesetiefe |
|---|---|
| LHAASO Collaboration (Cao, Z. u. a.) (2024): *Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A*. PRL 133, 071501. [arXiv:2402.06009](https://arxiv.org/abs/2402.06009) | [A] Abstract, PDF-Text Z. 126, 140, 465 bis 470 |
| Yang, Y.-M.; Bi, X.-J.; Yin, P.-F. (2024): *Constraints on Lorentz invariance violation from the LHAASO observation of GRB 221009A*. JCAP 04 (2024) 060. [Verlag](https://iopscience.iop.org/article/10.1088/1475-7516/2024/04/060) | [A-W] |
| Hua, Y.-C.; Bi, X.-J.; Yang, Y.-M.; Yin, P.-F. (2025): *Probing Lorentz Invariance Violation at High Energies Using LHAASO Observations of GRB221009A via DisCan Algorithm*. [arXiv:2511.05062](https://arxiv.org/abs/2511.05062) | [A] Abstract |
| LHAASO Collaboration (2022): *Exploring Lorentz Invariance Violation from Ultrahigh-Energy gamma Rays Observed by LHAASO*. PRL 128, 051102. [arXiv:2106.12350](https://arxiv.org/abs/2106.12350) | [A] Abstract |
| Ofengeim, D. D.; Piran, T. (2025): *The 300 TeV photon from GRB 221009A: a Hint at Non-linear Lorentz Invariance Violation?* [arXiv:2508.07153](https://arxiv.org/abs/2508.07153) | [A-W] |
| Bartlett, D. J.; Bergsdal, D.; Desmond, H.; Ferreira, P. G.; Jasche, J. (2021): *Constraints on Equivalence Principle Violation from Gamma Ray Bursts*. PRD 104, 084025. [arXiv:2106.15290](https://arxiv.org/abs/2106.15290) | [A] Abstract |
| Mrk-421-Flare: JCAP 07 (2024) 044 ([ADS](https://ui.adsabs.harvard.edu/abs/2024JCAP...07..044A/abstract)) | [S], Autorenschaft nicht geprueft |
| Jackson, J. D.: *Classical Electrodynamics*, Kap. 7.10 (Kramers-Kronig) | [L] |
| Projekt: RUNDE-01.md (QG-1, Z. 43 bis 55); LORENTZ.md (§4.2 ab Z. 377; Z. 63); UNGEPRUEFT.md (Z. 115 bis 117); VIDEO-6r1au5axOXM.md (V-3, Z. 445 bis 469; Z. 191) | [P] |

### Latten V-3

- **L1 (kann scheitern):**
  - Er hat keine, also lautet das Ergebnis "keine Vorhersage". Das hatte die Karte als moeglichen Ausgang vorgesehen.
- **L2 (Proben):**
  - Die Plasma- und die Vakuumprobe sind bestanden.
  - Das UV-Modell reproduziert LHAASOs Faktor 3/2.
- **L3:** entfaellt. Es sind nur Umrechnungen; PRL- und DisCan-Grenzen unterscheiden sich um den Faktor 2.
- **L4 (Literatur):**
  - LIV- und Delta-gamma-Grenzen sind Standard.
- **L5 (Messbezug):** Ja: LHAASO GRB 221009A, Bartlett 2021.

### Vorschlag V-3

- Als Mechanismusfrage **parken**. Falls die Leitung weitergehen will, braucht es eine Papierkarte "Random Walk kohaerent oder
  inkohaerent" mit zwei Ueberschlaegen:
  - (a) Kramers-Kronig-Skala gegen Fermi/LHAASO.
  - (b) Bildunschaerfe eines inkohaerenten Zickzacks gegen die Radiointerferometrie am Sonnenrand (siehe Gegensweep).
- Die Fehlzuschreibung der LHAASO-Zahlen in VIDEO Z. 191 und LORENTZ.md Z. 63 sollte die Leitung berichtigen.

---

## Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Punkt | geprueft? | Ergebnis |
|---|---|---|
| GS1: Die 30 um bei Lee beruhen auf alpha = 8/3 | indirekt | Lee nennt kein alpha. Das UW-Review 2009 nennt fuer die 44-um-Grenze alpha = 8n/3 [A]; dieselbe Konvention ist wahrscheinlich. |
| GS2: Die Schranke ist vorzeichensymmetrisch | nein (HTTP 401) | offen; Murata 2026 nennt alpha < 0 "qualitativ analog", ohne Kurve [A-W] |
| GS5: Die LHAASO-Zahlen im Projekt stimmen | **ja** | Nein, sie sind falsch zugeordnet (Yang/Bi/Yin 2024 statt PRL). Erwartungsverstoss 3. |
| GS6: KK-Skalare bei n >= 2 | nein | 8n/3 gegen 4n(n+1)/(n+2) offen [L] |
| GS7: Kein Screening im Labor (Vainshtein fuer ein schweres Graviton, Chamaeleon fuer Skalare) | nein | offen. Die Tabelle gilt nur fuer lineare, ungeschirmte Kopplung. |
| GS8: Ein wortwoertlicher Random Walk erzeugt nur eine mittlere Bremsung | nein, nur Ueberschlag [ES] | Ein inkohaerenter Zickzack mit mittlerer Bremsung delta braucht einen Winkelrauschpegel von etwa sqrt(2 delta). Am Sonnenrand (Phi ~ 2e-6) waeren das etwa 2e-3 rad Unschaerfe. Das gilt nur, wenn die Zacken groesser als die Wellenlaenge sind. Gegen Radiointerferometrie nicht an einer Quelle geprueft. |

## Kalibrierung

- **(a) Gemessen:**
  - Lee 2020: 38,6 um, 30 um, 5,1 meV, 7,1 TeV, bester Fit 7,1 um ohne Signal.
  - LHAASO-Grenzen, die unabhaengigen Auswertungen und Bartlett (Delta gamma).
- **(b) Nuetzlich verdichtet:**
  - Die alpha-Werte der drei Bilder sind Theorie, an den Quellen belegt.
  - Ebenso die Tabelle, die Spektraldichte-Sicht, die Koernungsumrechnung und die Interpolation lambda_max(alpha).
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "8/3 ist die richtige Zahl": Sie haengt am Radion-Regime, und keine Messung legt es heute fest.
  - Die Stelle-Reichweiten aus der Interpolation.
- **Warnzeichen:**
  - Meine Sicherheit fuer 8n/3 stieg waehrend der Recherche, waehrend sich die Frage in eine Normierungsfrage aufloeste.
  - Die ehrliche Fassung lautet: Beide Zahlen sind richtig, jede in ihrem Regime.

## Offene Fragen

1. Vorzeichengetrennte Eoet-Wash-Kurven (Supplement oder Dissertation Lee 2020) fuer eine Zwei-Term-Auswertung von Stelle.
2. n >= 2: Tragen die KK-Skalare bei (GRW-Struktur an der Quelle pruefen)?
3. Screening kurzreichweitiger Terme im Labor (GS7).
   - Ist der Random Walk kohaerent (dann ein Medium mit Dispersionsskala) oder inkohaerent (dann Bildunschaerfe)?
   - Haengt die Brechung von der Energie der inneren Bestandteile ab, braeche das auch das passive Aequivalenzprinzip, weil der
5. Carpet-3-Photon: Gehoert es wirklich zu GRB 221009A? Davon haengt der LIV-Hinweis ab.

## Einfach gesagt

Wenn es winzige Extra-Dimensionen oder neue Schwerkraft-Teilchen gibt, aendert sich die Anziehung auf Abstaenden unter einem
Zehntelmillimeter ein wenig. Jede Idee hinterlaesst dabei eine eigene Handschrift. Extra-Dimensionen verstaerken die Anziehung
in vielen gleich grossen Stufen, die Stelle-Theorie schwaecht sie mit festen Zahlen ab, und ein einzelnes neues Feld verstaerkt
sie genau einmal. Die Waage in Seattle sieht bisher nichts und sagt nur, dass solche Effekte unter etwa 40 Mikrometern Reichweite
Streit gaebe es erst, wenn sein Mechanismus genauer ausgerechnet wuerde.
