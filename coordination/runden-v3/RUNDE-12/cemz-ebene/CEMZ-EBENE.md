# CEMZ-EBENE: Regime I gegen Fuenfte Kraft in der Ebene (l_eff, |alpha|)

- Auftrag: claude-primary, Runde 12 (v3, explorativ), Schwerpunkt Glieder 7 und 10 der Spin-2-Kette.
- Arbeitsordner `coordination/runden-v3/RUNDE-12/cemz-ebene/`. Beginn (date): 2026-10-01 18:08:49 CEST. Zeitbox 50 min (bis 18:58:49).
- Gelesen vor dem ersten Abruf (nur intern): RUNDE-11/cemz-mess/CEMZ-MESS.md ganz; WARUM-SPIN-2.md Z. 672-773 (nur gelesen, nicht geaendert).
- Lesetiefe: [A] an der Quelle gelesen (Seite/Gl./Tabelle), [A-Bild] aus Abbildung abgelesen, [S] Abstract/Suchtreffer,
  [L?] Gedaechtnis, [H] Hypothese, [ES] eigener Schluss. Nur [A] traegt.

# BERICHT

Geschrieben ab 18:23:26 (date davor), Quellen und Rechenwege im Arbeitsfeld darunter.

## Kurzfazit (10 Zeilen)

1. **Scheiterregel, woertlich: besteht.** Fuer alle l_eff in [1, 35] km erlaubt die Fuenfte Kraft nur |alpha| <~ 3e-4 bis 6e-4
   (AHN 2003 "95%", Fischbach & Talmadge 1996 "2 sigma", [A-Bild]); fuer anziehendes +alpha bei 1-20 km eher ~1e-3 bis 2e-3 [ES].
2. **Belegstufe:** Bildablesung, keine Tabellenwerte gefunden -> Karte nur auf Faktor ~2 gueltig (Zusatz der Regel). Der Ausgang
   haengt nicht daran: Abstand zu 1e-2 mindestens Faktor ~5 (+alpha), sonst ~16.
3. 1-20 km tragen nur **vier Turmversuche 1988-1994** (WTVD, WABG, Erie, BREN), ab ~20 km Earth-LAGEOS; laut AHN seit 1999
   "essentially unchanged" [A]; 2010-2023 nicht geprueft, 2024-2026 nichts gefunden (ohne Websuche).
4. **Bedingt:** gilt nur in Regime I mit alpha ~ 1 (EGHS: "parametrically equal to gravitational") und lambda ~ l_eff (CEMZ S. 48:
   "no sharp bound", Logarithmus) [A]. Engste Stelle: l_eff ~ 1 km, Turm ~9x schwerer, +alpha: ~7e-3, knapp unter 1e-2 [ES/H].
5. **Unterscheidungspunkt:** lambda ~ 2-20 km (nur Turmdaten). CEMZ in D = 4 (24 Monate): nichts, was umstoesst oder rettet [S].

## Erwartungsverstoesse (das Wichtigste zuerst)

**V0 (mittel bis gross) - CEMZ binden die Turmmasse nicht scharf an l_eff.** Erwartet (E13, 18:26:30): CEMZ fixieren die
Kopplungen nur ueber "vergleichbar", sonst nichts. Gefunden (R11, CEMZ S. 48 [A]): "Due to the presence of the logarithm we did not
find a sharp bound between the corrections to the graviton three point amplitude, alpha, and the Regge slope alpha'"; S. 34: Effekte
bei "b^2 ~ alpha' log(s alpha')"; und "Besides string theory, we do not know if there are other ways of doing this." Damit ist der
RUNDE-11-Befund "GW-Laenge und Turmmasse sind dieselbe Skala, geprueft: ja (EGHS S. 12-13)" nur parametrisch richtig; die
Gleichsetzung lambda = l_eff in der Ebene ist eine Setzung bis auf einen Logarithmus. Korrigierte Erwartung: Der Ausgang haengt an
drei Faktoren (alpha ~ 1, Vorzeichen, lambda/l_eff); nur zusammen wird es eng (engste Stelle: l_eff ~ 1 km, lambda ~ 100 m, +alpha
~7e-3 [ES/H]).

**V1 (mittel) - Die km-Kurve ist fuer negatives alpha gezeichnet.** Erwartet (E1, 18:11:31): |alpha|, wie in AHN beschriftet.
Gefunden (R8, Fischbach & Talmadge 1996, Fig. 1, S. 8 [A-Bild]): Hochachse "**-alpha**", also abstossende Zusatzkraft; AHN 2003
zeichnet dieselbe Kurvenform als |alpha|. Kopfrechnung [ES]: Romaides u. a. 1994 melden -33 +- 30 uGal in 493 m [S]; ein anziehender
Zusatz senkt die Schwere oben am Turm, also erlaubt der 2-sigma-Bereich alpha in etwa [-4,8e-4; +1,7e-3]. Die -alpha-Seite trifft das
Plateau der Abbildung (~5e-4), die +alpha-Seite ist ~3x schwaecher. Korrigierte Erwartung: Fuer eine anziehende Turmkraft (gerade
Spins, positive Residuen) gilt bei 1-20 km eher ~1e-3 bis 2e-3 als 5e-4. Der Ausgang bleibt "besteht", der Abstand schrumpft von ~20
auf ~5.

**V2 (mittel) - Der duennste Bereich ist ein flaches Plateau, keine Delle.** Erwartet (E7): Turm/Bohrloch nur bis ~1 km,
Erde-Satellit-Grenzen weichen nach unten mit 1/lambda auf, also eine Luecke bei 1-5 km. Gefunden (R1, R8): flaches Plateau von ~1 km
bis ~20 km, in Fig. 1 von 1996 mit "Tower" beschriftet. Kopfrechnung [ES, R3]: Ein Turmversuch vergleicht die Schwere oben mit der
Laplace-Fortsetzung der Bodendaten; der Yukawa-Fehlbetrag ist 2 pi G rho alpha h fuer lambda >> h, also **unabhaengig von
lambda**. Deshalb tragen 500-m-Tuerme bis zu Reichweiten von zig km. Korrigierte Erwartung: duennster Bereich 2-20 km
(nur Turmdaten), nicht 1-5 km.

**V3 (klein) - "95 %" ist die Beschriftung der Zusammensteller.** AHN 2003 und Adelberger 2009 schreiben "95%", Fischbach &
Talmadge 1996 "2 sigma" (R1, R7, R8). Fuer Gauss-Fehler gleichwertig; die Turm-Originale habe ich nicht gelesen.

Bestaetigt (je eine Zeile): E2 keine Tabellenwerte, Kette Fischbach & Talmadge -> AHN 2003 -> Adelberger 2009 (R7, R8); E4 EGHS nur
parametrisch (R5); E5/E6 CEMZ: Yukawa nur in der Stossparameterdarstellung, je Zustand positiv in der t-Kanal-unitaeren
Konfiguration (R6); E8/E12 keine neue km-Messung 2024-2026 (R4, R9); E9 nichts Neues zu CEMZ in D = 4, das umstoesst oder rettet
(R2); E11/E14 ell (Maenaut) = c3^(1/4)/Lambda (EGHS), Faktor 1, gleiche R^3-Kontraktion (R10, R12).

## Literaturstand: Fuenfte-Kraft-Grenzkurve 1-35 km

Konvention: V = -G m1 m2 (1 + alpha e^(-r/lambda))/r (AHN Gl. 2); alpha > 0 heisst anziehender Zusatz.

| lambda | AHN 2003 Abb. 4, \|alpha\|, "95%" [A-Bild] | F&T 1996 Fig. 1, -alpha, "2 sigma" [A-Bild] | +alpha, Schaetzung [ES] | Traeger laut Abbildung |
|---|---|---|---|---|
| 1 km | ~6e-4 | ~6e-4 | ~1e-3 bis 2e-3 | Turm |
| 2 km | ~5e-4 | ~5e-4 | ~1e-3 bis 2e-3 | Turm |
| 5 km | ~5e-4 | ~5e-4 | ~1e-3 bis 2e-3 | Turm (Ozean bis 5 km: G auf 2e-3 genau, Zumberge 1991 [S]) |
| 10 km | ~5e-4 | ~4,5e-4 | ~1e-3 bis 2e-3 | Turm |
| 20 km | ~4,5e-4 | ~4,3e-4 | ~1e-3 bis 2e-3 | Turm, Uebergang Earth-LAGEOS |
| 35 km | ~2,5e-4 | ~3e-4 | nicht geschaetzt | Earth-LAGEOS |

- Ablesegenauigkeit etwa Faktor 1,5 (+-10 px bei 58 bzw. 74 px je Dekade). Beide Abbildungen zeigen dieselben Daten.
- Einzelmessungen, nur Abstract [S]: Jekeli/Eckhardt/Romaides 1990 "alpha to be less than 0.001" (ohne lambda, Niveau,
  Vorzeichen); Romaides 1994 "-33 +- 30 uGal at 493 m"; Eckhardt 1988 "(-500 +- 35) x 10^-8 m s^-2" (nach Gelaendekorrektur
  zurueckgenommen, F&T 1996 S. 6 [A]).
- +alpha-Spalte: Kopfrechnung aus einem Turm und dessen groesster Abweichung, Dichte 2,7 g/cm^3 angenommen (Arbeitsfeld R8).
- Stoffabhaengige Kraefte begrenzt das Aequivalenzprinzip viel staerker: eta(Be, Al) = (-1,5 +- 1,5) x 10^-13, auf lambda < 10 km
  und > 1000 km umgerechnet (Adelberger 2009 [A, Text]).

## Abbildung des Turms auf (lambda, alpha)

- **Reichweite:** EGHS S. 13 [A]: "r ~ c3^(1/4)/Lambda", also lambda ~ l_eff, parametrisch. Turmmasse ~ Lambda/c3^(1/4).
  Maenaut Gl. (1) [A]: ell^4 lambda_ev R^3 mit |lambda_ev| = 1; EGHS Gl. (2.5) [A] gleiche Kontraktion, also dieselbe Laenge (R10, R12).
  **CEMZ selbst binden die Turmmasse nicht scharf an die Korrektur** (R11 [A]): S. 48 "m^2 ~ 1/alpha", aber "Due to the presence of
  the logarithm we did not find a sharp bound between ... alpha, and the Regge slope alpha'"; S. 34: Turmeffekte erscheinen bei
  "b^2 ~ alpha' log(s alpha') rather than the more naive expectation of b^2 ~ alpha'". lambda = l_eff ist also eine Setzung bis
  auf einen logarithmischen Faktor (bei Nukleonen grob sqrt(ln(alpha' s)) ~ 9, Kopfrechnung [H]).
- **Kopplungsstruktur:** CEMZ S. 34 [A]: "a tower of particles with increasing spins and intricate relations between them ...
  Besides string theory, we do not know if there are other ways of doing this." alpha ~ 1 ist damit Stringtheorie-Analogie.
- **Staerke:** EGHS S. 8 [A]: "couplings such as to allow mediation of long range forces of gravitational strength between any
  matter fields"; S. 13: "strength will be parametrically equal to gravitational". Keine Formel, kein O(1)-Faktor.
- **Haengt alpha ~ 1 von Kopplungen ab? Ja, nach meiner Lesart [ES/H]:** Das Eikonal Graviton-an-Materie legt nur das Produkt
  g(hhX) g(XSS) fest, die Kraft zwischen zwei Materieteilchen aber g(XSS)^2. alpha ~ 1 folgt erst mit der Zusatzannahme
  g(hhX) ~ sqrt(G) (alle Turmkopplungen gravitativ, wie in der Stringtheorie). Eine Hierarchie g(hhX) = kappa sqrt(G) gaebe
  alpha ~ 1/kappa^2; um die Daten zu unterlaufen, braeuchte es kappa ~ 20 bis 45. Ob CEMZ das ausschliesst, habe ich an der Quelle
  nicht gefunden. Offene Frage 2.
- **Vorzeichen und Aufhebung:** CEMZ S. 24 [A]: in der t-Kanal-unitaeren Konfiguration "a strictly positive answer for the time
  delay for the contribution of any particle with a non-zero coupling". Dort heben sich Spins also nicht auf. Fuer die statische
  Kraft zwischen ruhenden Massen sagt keine der beiden Arbeiten etwas. [ES] Gerade Spins ziehen gleichartige Teilchen an, ungerade
  stossen sie ab; eine Aufhebung muesste fuer lambda >> h die Summe sum_n alpha_n auf ~1e-3 genau treffen, also Feinabstimmung.

## Die Ebene (l_eff, |alpha|) und der Ausgang

GW-Schranke: Maenaut u. a. 2024, Tab. I (aus RUNDE-11, R19 [A]): sign(lambda_ev) ell in [-32,2; +34,3] km, 95 %, nur
paritaetsgerade kubisch; der paritaetsungerade Vertex hat keine Ringdown-Schranke. Die GW-Daten begrenzen ell, nicht alpha: in
der Ebene ist das eine senkrechte Grenze.

| l_eff | GW (kubisch, gerade) | Fuenfte Kraft, \|alpha\| 95 % | +alpha [ES] | Regime I sagt | Befund |
|---|---|---|---|---|---|
| 1 km | erlaubt | <~ 6e-4 | ~1e-3 bis 2e-3 | alpha ~ 1 | Regime I ausgeschlossen, Faktor >~ 500 |
| 2 km | erlaubt | <~ 5e-4 | ~1e-3 bis 2e-3 | alpha ~ 1 | ausgeschlossen |
| 5 km | erlaubt | <~ 5e-4 | ~1e-3 bis 2e-3 | alpha ~ 1 | ausgeschlossen |
| 10 km | erlaubt | <~ 5e-4 | ~1e-3 bis 2e-3 | alpha ~ 1 | ausgeschlossen |
| 20 km | erlaubt | <~ 4,5e-4 | ~1e-3 bis 2e-3 | alpha ~ 1 | ausgeschlossen |
| 35 km | ausgeschlossen (> 34,3 bzw. > 32,2 km) | <~ 3e-4 | - | alpha ~ 1 | zweifach ausgeschlossen |

**Scheiterregel, woertlich angewandt:**
- "faellt, wenn fuer irgendein l_eff in [1, 35] km die 95-%-Grenze noch |alpha| >= 0,1 zulaesst": nirgends (Maximum ~6e-4).
- "besteht, wenn dort ueberall |alpha| <= 1e-2 gilt": ja, ueberall, auch auf der geschaetzten +alpha-Seite (<~ 2e-3).
- **Ausgang: besteht.** Belegstufe: [A-Bild] aus zwei Zusammenstellungen, keine Tabelle, also Karte auf Faktor ~2 (Zusatz der
  Regel). Der Ausgang haengt nicht an diesem Faktor.
- Was die Regel nicht prueft: ob alpha ~ 1 gilt (Abschnitt oben) und ob Regime I in D = 4 ueberhaupt gilt (CEMZ-MESS V1).
  "Besteht" heisst also: **wenn** Regime I mit gravitativer Turmkopplung, **dann** keine messbare kubische Korrektur.
- **Engste Stelle der Ebene [ES/H]:** Die Regel setzt lambda = l_eff. Ist der Turm um den Log-Faktor ~9 schwerer (CEMZ S. 48
  laesst das offen), wandert l_eff = 1 km nach lambda ~ 100 m; dort |alpha| <~ 2e-3 bis 3e-3 (AHN, F&T), auf der +alpha-Seite
  bei Faktor ~3 etwa 7e-3. Das waere knapp unter 1e-2, also noch "besteht", aber nur noch mit Faktor ~1,4 Abstand und auf zwei
  ungeprueften Annahmen. Fuer laengere Reichweiten wird der Ausschluss staerker.

## Regime und Moderatoren

| Regime | Voraussetzung | km-Korrektur | Beleg |
|---|---|---|---|
| I | CEMZ in D = 4 + Turmkopplung gravitativ (alpha ~ 1) | ausgeschlossen, Faktor >~ 500 | EGHS [A], Kurven [A-Bild] |
| I-kappa [H] | wie I, aber Kopplungshierarchie, alpha ~ 1/kappa^2 | offen ab kappa ~ 20 bis 45 | keine Quelle |
| I' | infrarote Kausalitaet statt asymptotischer | reine Tensor-Korrektur fuer heutige Daten unsichtbar, ohne Turm | Nie u. a. [A, RUNDE-11], 2608.10871 [S] |
| II | keine Kausalitaetsvorgabe | nur GW: \|ell\| <~ 32-34 km | Maenaut [A] |

Moderatoren der Fuenfte-Kraft-Seite: **Vorzeichen von alpha** (die gezeichnete Kurve ist -alpha), **Messart** (Turm-Fortsetzung
flach in lambda gegen Kepler-Vergleich Erde-LAGEOS), **Stoffabhaengigkeit** (dann greift das Aequivalenzprinzip, viel staerker).
Moderatoren der Theorieseite: **Verhaeltnis der Turmkopplungen** an Gravitonen und an Materie; **Verhaeltnis lambda/l_eff**
(Logarithmus, CEMZ S. 48 "no sharp bound").

## Unterscheidungspunkte

- **U1 (I gegen II/I'):** Fuenfte Kraft bei lambda ~ l_eff mit Empfindlichkeit <= 1e-2. Gemessen: Regime I liegt Faktor >~ 500
  darueber. Entschieden.
- **U2 (I gegen I-kappa / teilweise Aufhebung):** liegt im **duennsten Bereich lambda ~ 2-20 km**: Plateau ~5e-4 (-alpha),
  +alpha vermutlich ~1e-3 bis 2e-3, getragen nur von vier Turmversuchen aus 1988-1994 mit Gelaendemodell-Systematik (WTVD-Anomalie
  1988 nach Gelaendekorrektur zurueckgenommen). Zugaenglich, anders als beim Wasser: ein heutiger Turm- oder Hochhausversuch mit
  Absolutgravimetern koennte die Grenze dort um eine Groessenordnung senken [ES].
- **U3 (anziehend gegen abstossend):** Romaides' Zentralwert bevorzugt +alpha mit 1,1 sigma, also nichts. Getrennte +alpha- und
  -alpha-Grenzen je lambda gibt es in den gelesenen Quellen nicht.
- **U4 (lambda = l_eff gegen lambda = l_eff / Log-Faktor):** trennt sich nur bei kleinem l_eff: fuer l_eff ~ 1 km liegt die
  Fuenfte-Kraft-Messung dann bei lambda ~ 100 m (Turm-/See-Plateau, |alpha| <~ 2e-3 bis 3e-3). Dort ist der Ausschluss am
  knappsten (+alpha ~7e-3 [ES/H]). Theoretisch zu klaeren (Log-Faktor im statischen Grenzfall), experimentell mit denselben
  Turmdaten.

## Gegensweep-Befunde

Sechs Selbstverstaendlichkeiten benannt, vier an der Quelle geprueft (Arbeitsfeld Abschn. 3 und R11):
1. Kurve ist vorzeichenblind |alpha|: **geprueft, nein** (F&T 1996 zeigt -alpha) -> V1.
2. Niveau "95 %": **geprueft**, F&T sagen 2 sigma, gleichwertig -> V3.
3. GW-ell = EGHS-l_eff: **geprueft, ja, Faktor 1** (Maenaut Gl. 1, EGHS Gl. 2.5: dieselbe R^3-Kontraktion, R12).
4. Reichweite = l_eff genau: ~~nicht geprueft; [ES] unkritisch, fuer 0,1 l_eff bis 10 l_eff bleibt |alpha| <~ 3e-3.~~ **Nachgeprueft (R11):**
   CEMZ S. 48 "no sharp bound" (Logarithmus). Fuer |alpha| unkritisch (<~ 3e-3 bei 0,1 bis 10 l_eff), fuer +alpha bei 0,1 l_eff knapp
   (~7e-3) [ES/H] -> V0.
5. Stoffunabhaengigkeit: teilweise geprueft; stoffabhaengig waere schaerfer begrenzt (eta ~ 1e-13).
6. Turm wirkt wie Einzel-Yukawa: nicht geprueft; Aufhebung braeuchte Feinabstimmung auf ~1e-3 [ES].

## Kalibrierung

- **(a) Gemessen:** Turmabweichungen (Romaides 1994 -33 +- 30 uGal [S]; Jekeli 1990 alpha < 0,001 [S]), Ozean-G auf 2e-3 [S], zwei
  Kurven [A-Bild], GW-Grenze auf ell [A], Aequivalenzprinzip eta [A].
- **(b) Nuetzlich verdichtet:** die Ebene, die Flachheit der Turmempfindlichkeit [ES], die +alpha-Schaetzung [ES].
- **(c) Gewachsene Gewissheit ohne neue Evidenz:** "alpha ~ 1". Seit dem 24.09. wiederholt; sie ruht auf einem Satz bei EGHS
  ("parametrically equal"). Neue Evidenz dafuer habe ich nicht gefunden.
- **Warnzeichen:** Meine Sicherheit, dass die Regel "besteht", stieg, waehrend die Frage in Vorzeichen, Reichweitenfaktor und
  Kopplungshierarchie zerfiel. Der Ausgang ist robust gegen Bildablesung und Vorzeichen, aber nicht gegen die ungepruefte Annahme
  alpha ~ 1; und lambda = l_eff ist laut CEMZ S. 48 selbst nur bis auf einen Logarithmus festgelegt (V0). Je einzeln haelt der
  Ausgang; treffen Vorzeichen und Log-Faktor zusammen, bleibt bei l_eff ~ 1 km nur Faktor ~1,4 Abstand [ES/H].

## Offene Fragen

1. +alpha-Grenzen je lambda aus den Turm-Originalen (Romaides 1994, Speake 1990, Thomas 1989, Jekeli 1990; APS, nicht frei) oder
   aus Fischbach & Talmadge 1999 (Buch, Fig. 2.13).
2. Legt das CEMZ-Argument das Verhaeltnis der Turmkopplungen an Gravitonen und an Materie fest (kappa ~ 1), oder ist alpha frei? [H]
3. Statischer Grenzfall: Der Turm laege 15 Groessenordnungen unter der Elektronenmasse. Wie sieht die Regge-summierte statische Kraft
   zwischen schweren Teilchen aus (Reichweite eher ell sqrt(ln(alpha' s)) ~ 9 ell, oder Turm um diesen Faktor schwerer?) [H].
   CEMZ S. 48 lassen das Verhaeltnis alpha zu alpha' ausdruecklich offen [A]. Keine Quelle fuer den statischen Fall gefunden.
4. Paritaetsungerader Vertex c~3: weiter keine GW-Schranke; die Ebene gilt GW-seitig nur fuer den geraden.
5. Gilt Regime I in D = 4 (CEMZ-MESS V1)? Unveraendert offen.
6. Abstract des CSS-Vorschlags ("Earth as a Spin and Mass Source") nicht gelesen.

## Kleinster Folgeschritt mit Scheiterregel

Primaerquellen der vier Turmversuche beschaffen und +alpha-Grenzen je lambda in ~~1-35 km~~ 0,1-35 km (wegen V0) als Tabelle.
**Scheiterregel, vorab:** Liegt die +alpha-Grenze irgendwo in [1, 35] km bei >= 1e-2, wird der heutige Ausgang "besteht" fuer
anziehende Turmkraefte zu "unentschieden"; liegt sie ueberall <= 3e-3, bleibt er. Liegt sie nur bei 0,1-1 km ueber 1e-2, haengt
der Ausgang am Log-Faktor (U4) und ist so zu kennzeichnen. Parallel, Schreibtisch: CEMZ Abschn. 4-5 auf eine Festlegung von kappa
und auf das Verhaeltnis alpha/alpha' im statischen Fall lesen.

## Quellenliste (dieser Lauf; Hashes in quellen/SHA256SUMS.txt und im Arbeitsfeld)

- Adelberger, Heckel, Nelson 2003, Tests of the Gravitational Inverse-Square Law, Ann. Rev. Nucl. Part. Sci. 53, 77, https://arxiv.org/abs/hep-ph/0307284 [A-Bild Abb. 4; A Text 4.5, Gl. 2]
- Fischbach, Talmadge 1996, Ten Years of the Fifth Force, https://arxiv.org/abs/hep-ph/9606249 [A Text S. 4, 6, 7; A-Bild Fig. 1]
- Adelberger, Gundlach, Heckel, Hoedl, Schlamminger 2009, Torsion balance experiments: A low-energy frontier of particle physics, Prog. Part. Nucl. Phys. 62, 102, https://doi.org/10.1016/j.ppnp.2008.08.002 [A, Text der Scratchpad-Kopie; Abb. nicht gesehen]
- Zumberge u. a. 1991, Submarine measurement of the Newtonian gravitational constant, PRL 67, 3051, https://doi.org/10.1103/PhysRevLett.67.3051 [S]
- Eckhardt, Jekeli, Lazarewicz, Romaides, Sands 1988, Tower Gravity Experiment: Evidence for Non-Newtonian Gravity, PRL 60, 2567, https://doi.org/10.1103/PhysRevLett.60.2567 [S]
- Jekeli, Eckhardt, Romaides 1990, Tower gravity experiment: No evidence for non-Newtonian gravity, PRL 64, 1204, https://doi.org/10.1103/PhysRevLett.64.1204 [S]
- Romaides, Sands, Eckhardt, Fischbach, Talmadge, Kloor 1994, Second tower experiment: Further evidence for Newtonian gravity, PRD 50, 3608, https://doi.org/10.1103/PhysRevD.50.3608 [S]
- Nur ueber F&T 1996 zitiert, nicht gelesen: Speake u. a., PRL 65, 1967 (1990); Thomas u. a., PRL 63, 1902 (1989); Ander u. a., PRL 62, 985 (1989).
- Endlich, Gorbenko, Huang, Senatore 2017, JHEP 09 (2017) 122, https://arxiv.org/abs/1704.01590 [A: S. 8, 12-13]
- Camanho, Edelstein, Maldacena, Zhiboedov 2014/2016, Causality Constraints on Corrections to the Graviton Three-Point Coupling (Zeitschrift JHEP 02 (2016) 020 [L?]), https://arxiv.org/abs/1407.5597 [A: S. 3-4, 23-25, 30-31, 33-34, 48, Fn. 6]
- Maenaut, Carullo, Cano, Liu, Cardoso, Hertog, Li 2024, https://arxiv.org/abs/2411.17893 [A: Gl. 1; Tab. I aus RUNDE-11]
- Bucciotti, Creminelli, Longo, McBlain, Trincherini 2026, https://arxiv.org/abs/2605.00089 [nur Zitate ueber INSPIRE]
- Lippstreu 2026, Unitarity and the Forward Direction in Theories with Long-Range Forces, https://arxiv.org/abs/2609.16896 [S]
- Jeong, Kim, Lee 2026, Gravitational Faraday rotation, ... spin-refined causality analysis ..., https://arxiv.org/abs/2608.10871 [S]
- Iorio 2002, Constraints to a Yukawa gravitational potential from laser data to LAGEOS satellites, Phys. Lett. A 298, https://arxiv.org/abs/gr-qc/0201081 [S]
- Lucchesi, Peron 2011 (arXiv-Datum), Accurate Measurement in the Field of the Earth of the General-Relativistic Precession of the LAGEOS II pericenter and new constraints on non-Newtonian gravity, https://arxiv.org/abs/1106.2905 [nur Titel]
- Ewasiuk, Profumo 2025, Precision gravity constraints on large dark sectors, https://arxiv.org/abs/2509.02801 [S]
- Fiorillo, Lella, Raffelt, Selimovic, Vitagliano 2026, Neutron Star Bounds on Muonic Fifth Forces ..., https://arxiv.org/abs/2605.24094 [S]
- Werkzeuge: INSPIRE-API (refersto:recid:3150820, refersto:recid:1307098 mit de > 2026-03, Titelsuche de > 2024-09), arXiv-API. WebSearch erschoepft.

---

# ARBEITSFELD

## 0. Uebernommene Scheiterregel (woertlich aus dem Auftrag; Fassung CEMZ-MESS.md, Bericht "Kleinster Folgeschritt")

- Die Aussage "Regime I schliesst messbare kubische Korrekturen aus" faellt, wenn fuer irgendein l_eff in [1, 35] km die
  95-%-Grenze noch |alpha| >= 0,1 zulaesst.
- Sie besteht, wenn dort ueberall |alpha| <= 1e-2 gilt.
- Dazwischen ist sie unentschieden.
- Zusatz aus CEMZ-MESS.md (woertlich dort): "Findet sich fuer 1-35 km keine Quelle mit Tabellenwerten, ist die Karte nur
  auf Faktor ~2 gueltig und so zu kennzeichnen."

## 1. Vorab-Erwartungen (date 18:11:31, vor jedem Abruf, auch vor dem Lesen der lokalen AHN-Kopie ueber grep hinaus)

Grundhypothese [H0]: Zwei Regime, Moderator = Kopplung des Turms an Materie (Staerke, Stoffabhaengigkeit, Vorzeichen).
Mit alpha ~ 1 besteht die Aussage deutlich; haengt alpha an einem freien Kopplungsverhaeltnis, wird die Ebene zur
Bedingung "alpha_Turm >= 1e-2 bis 1e-3", nicht zum Ausschluss.

- E1 (AHN 2003, Fig. 4 und Text 4.5): Bildunterschrift nennt 95 %; Abbildung "adaptiert" nach Fischbach & Talmadge 1999;
  keine Tabelle; der Bereich 1-35 km heisst "geophysical" bzw. "Earth-LAGEOS". -> nur [A-Bild].
- E2 (Quelle mit Tabellenwerten fuer 1-35 km): keine der Standard-Zusammenstellungen (Fischbach & Talmadge 1999,
  AHN 2003, Adelberger et al. 2009, Murata & Tanaka 2015) hat Tabellenwerte fuer 1-35 km. Einzelexperimente (Ozean/U-Boot
  Zumberge 1991, Turm Romaides 1997, Bohrloch Thomas/Vogel 1990, Groenland Ander 1989) geben eine G-Abweichung mit
  Fehler oder eine Bildkurve, meist 1 sigma oder 2 sigma. Bestenfalls [A] fuer einzelne (lambda, alpha)-Punkte, etwa
  |alpha| <~ 2e-3 bei lambda ~ 1-5 km.
- E3 (Konfidenzniveau): "95 %" ist eine Umrechnung der Kompilatoren; die geophysikalischen Originale nennen kein 95 %.
- E4 (EGHS, Staerke): "parametrically equal to gravitational" ohne Herleitung von Vorzeichen oder Stoffabhaengigkeit;
  keine alpha-Formel. alpha ~ 1 ist Groessenordnungs-Schaetzung unter der Annahme, alle Turmkopplungen seien von
  gravitativer Staerke.
- E5 (CEMZ, Kopplung an Materie): CEMZ verlangen Austausch zwischen Graviton und dem Streupartner, Kopplung "gravitational
  strength"; "Yukawa-like" nur in der Stossparameterdarstellung (e^(-mb)); nichts zur statischen Kraft zwischen ruhenden
  Massen. Das Eikonal fixiert nur das Produkt g(hhX) g(XSS), nicht g(XSS)^2 allein. [H] Das ist die Luecke fuer "alpha ~ 1".
- E6 (Vorzeichen): Positive Residuen (CEMZ-Voraussetzung) -> im Eikonal keine Aufhebung. Zwischen identischen Teilchen
  im t-Kanal nur gerade Spins [L?]. Keine Arbeit, die eine Aufhebung zwischen Spins behandelt. Im statischen Limes offen.
- E7 (Ebene): Mit |alpha|_max ~ 1e-3 (1-10 km) und ~1e-4 bis 5e-4 (10-35 km) besteht die Aussage nach der Scheiterregel,
  aber nur mit Bildgenauigkeit (Faktor ~2) und bedingt auf alpha ~ 1. Duennster Bereich: lambda ~ 1-5 km (zwischen
  Turm-/Bohrloch-Experimenten <= 1 km und Erde-Satellit-Vergleichen >= 10 km, deren Grenze ~ 1/lambda nach unten aufweicht).
- E8 (24 Monate, Fuenfte Kraft km): kein neuer stoffunabhaengiger ISL-Test bei 1-35 km 2024-2026; hoechstens
  Schwerefeld-Analysen (GRACE-FO, GOCE, Mond-Schwerefeld), gleich stark oder schwaecher.
- E9 (24 Monate, CEMZ in D = 4): ausser Bucciotti et al. 2026 ein bis drei Arbeiten zu D = 4 mit IR-Logarithmus
  (Caron-Huot u. a. Linie), keine, die CEMZ in D = 4 umstoesst oder rettet; keine, die den Turm mit Fuenfte-Kraft-Daten
  verbindet.

## 2. Abrufprotokoll (Erwartung -> Befund)

- **R1 (Eintrag 18:12:37) Adelberger/Heckel/Nelson 2003, hep-ph/0307284, lokale Kopie aus RUNDE-11 (quellen/hep-ph-0307284.pdf,
  sha256 24b85b5eefd8cfc1914cb0182ed19b18eb255d2851f202213645cc1f36892d69), Abb. 4 auf PDF-S. 76 bei 200 dpi neu gerendert
  und abgelesen, Text 4.5 (txt Z. 2715-2731). [A-Bild]** Erwartung E1 **bestaetigt** (eine Zeile): Bildunterschrift
  "95%-confidence-level constraints ... with lambda > 1 cm ... the remaining constraints are based on Keplerian tests. This plot is
  based on Figure 2.13 of Reference (14) [Fischbach & Talmadge 1999]"; keine Tabelle. Ablesung (Achsen: 1 Dekade lambda ~ 36 px,
  1 Dekade alpha ~ 58 px; Fehler ~ +-10 px = Faktor ~1,5): Plateau "geophysical" ~2e-3 bis 3e-3 bei 1-100 m, Abfall auf
  ~7e-4 bei ~700 m; **lambda = 1 km: ~6e-4; 2 km: ~5e-4; 5 km: ~5e-4; 10 km: ~5e-4; 20 km: ~4,5e-4; 35 km: ~2,5e-4**; ab ~20 km
  faellt die Kurve ("Earth-LAGEOS", Pfeil bei ~100 km, ~1e-5). Der Abschnitt 1-20 km ist im Bild **unbeschriftet** (zwischen den
  Pfeilen "geophysical" bei <= 1 km und "Earth-LAGEOS" bei ~100 km) -> welche Messung ihn traegt, sagt die Abbildung nicht.
- **Werkzeuglage 18:13:** WebSearch erschoepft (200/200). Weiter nur INSPIRE-API und arXiv-API per curl. "Nicht gefunden" ist ab
  hier schwaecher als mit Websuche.
- **R2 (Eintrag ~~18:15:40~~ geschaetzt; gemessen: geschrieben vor 18:16:13) INSPIRE refersto:recid:3150820 (Bucciotti u. a., 2 Zitate) und refersto:recid:1307098 (CEMZ) mit
  de > 2026-03 (28 Treffer), quellen/insp-cites-bucciotti.json, insp-cites-cemz-2026.json; Abstracts von acht Kandidaten
  quellen/abs-e9.xml. [S]** Erwartung E9 **bestaetigt** (eine Zeile): keine Arbeit stoesst CEMZ in D = 4 um oder rettet es,
  keine verbindet den Turm mit Fuenfte-Kraft-Daten. Naechstliegend: 2609.16896 (09/2026, IR-skalenfreie Unitaritaetsschranken bei
  langreichweitigen Kraeften, nichtrelativistisches Modell, "no infrared scale entering at any stage") und 2608.10871 (08/2026,
  infrarote Kausalitaet auf Kerr: "black hole's spin slightly enhances the causality constraints on EFT coefficients"); beide
  [S], ~~beide staerken eher Regime I' (infrarot) als Regime I (asymptotisch)~~ (Berichtigung, geschrieben vor 18:25:35: nur 2608.10871 staerkt
  Regime I'; 2609.16896 betrifft Unitaritaets-/Positivitaetsschranken ohne IR-Skala in einem Modell, keine Kausalitaetsaussage).
- **R3 (Eintrag ~~18:15:40~~ vor 18:16:13) INSPIRE-Abstracts der km-Experimente, quellen/insp-geophys.json. [S]** Erwartung E2 **im Kern
  bestaetigt, mit einer Einzelheit, die traegt:**
  - Zumberge u. a. 1991 (PRL 67, 3051): U-Boot im Ozean bis 5000 m, "G = (6.677 +- 0.013) x 10^-11 ...; the fractional
    uncertainty is 2 parts in 1000 ... consistent with laboratory determinations". Kein alpha, kein lambda, kein Niveau im Abstract.
  - Jekeli/Eckhardt/Romaides 1990 (PRL 64, 1204): Neuauswertung des AFGL-Turms (600 m) "including detailed topographic
    information ... in fact, no such evidence exists ... constrains the Yukawa-potential coupling constant alpha to be less than
    0.001". Kein lambda-Bereich, kein Niveau im Abstract. Vorgeschichte: Eckhardt u. a. 1988 (PRL 60, 2567) hatten mit demselben
    Turm "(-500 +- 35) x 10^-8 m s^-2" Abweichung gemeldet ("evidence for non-Newtonian gravity").
  - Romaides u. a. 1994 (PRD 50, 3608): WABG-Turm 610 m, Bodendaten bis 8 km dicht, Archivdaten bis 300 km; "largest
    discrepancy being -33 +- 30 uGal at 493 m"; "set further restrictions" - Zahl fuer alpha nicht im Abstract.
  - **[ES] Kopfrechnung, warum Turmversuche den Bereich 1-35 km tragen:** Halbraum der Dichte rho, Yukawa-Anteil
    g_Y(z) = 2 pi G rho alpha lambda e^(-z/lambda). Die Laplace-Fortsetzung der Bodendaten setzt ihn hoehenkonstant fort; der
    Fehlbetrag in Hoehe h ist 2 pi G rho alpha lambda (1 - e^(-h/lambda)) -> 2 pi G rho alpha h fuer lambda >> h, also
    **unabhaengig von lambda**. Mit rho = 2,7 g/cm^3: 2 pi G rho ~ 0,113 mGal/m, bei h = 493 m ~ 56 mGal; 30 uGal / 56 mGal
    ~ 5e-4. -> Ein Turmversuch der 1990er-Genauigkeit gibt |alpha| <~ 1e-3 flach fuer h << lambda << (Datenradius, Erdradius).
    Das passt zum unbeschrifteten Plateau ~5e-4 bei 1-20 km in AHN Abb. 4 (R1) und zu "alpha < 0.001" bei Jekeli 1990.
    Nicht an einer Quelle belegt; die Turmarbeiten selbst (APS) nicht gelesen.
- **R4 (Eintrag ~~18:15:40~~ vor 18:16:13) arXiv-API, sechs Suchen (Yukawa/fifth force/inverse-square x geophysical/LAGEOS/tower/kilometer/
  satellite), quellen/arxiv-yuk-geophys.xml, arxiv-yuk-multi.xml. [S]** Erwartung E8 **bestaetigt** (eine Zeile): kein neuer
  stoffunabhaengiger Test bei 1-35 km 2024-2026. Treffer: LAGEOS-Arbeiten nur bei ~Erdradius (Iorio 2002, gr-qc/0201081:
  "|alpha| < 10^-5 - 10^-8 for distances of the order of 10^9 cm"; Lucchesi & Peron 2010, 1106.2905), Theorie-Abbildung
  2509.02801 (Dunkelsektoren auf Yukawa-Grenzen), stoffabhaengig 2605.24094 (Myonen, Neutronensterne).
- **R5 (Eintrag ~~18:19~~ Zukunftszeit; gemessen: geschrieben vor 18:18:23) EGHS 1704.01590, lokale txt-Kopie aus RUNDE-11 (PDF-sha256 0d054f26...3b3393), Z. 362-382 (S. 8) und
  728-766 (S. 12-13). [A]** Erwartung E4 **bestaetigt** (eine Zeile): keine alpha-Formel, kein Vorzeichen, keine
  Stoffabhaengigkeit. Woertlich S. 8: "the couplings such as to allow mediation of long range forces of gravitational strength
  between any matter fields"; S. 13: Turm "coupled both to the graviton and to the matter particle on which the graviton is
  scattering ... a new force between all Standard Model particles, basically through the same set of diagrams but with graviton
  replaced with the second matter field ... range ... r ~ c3^(1/4)/Lambda and the strength will be parametrically equal to
  gravitational". Zusatz S. 13: kubische Terme "always lead to faster-than-GR propagation, independently of any assumption about
  the UV completion. However, this is not obviously enough to violate causality".
- **R6 (Eintrag ~~18:19~~ vor 18:18:23) CEMZ 1407.5597v1, lokale Kopie art-grenzen-20260921/cemz-gegenpruefung-codex-quellen/1407.5597v1.txt,
  Z. 645-672 (S. 23-24 mit Fn. 6) und Z. 1070-1080 (S. 24-25). [A]** Erwartung E5 **teilweise bestaetigt, E6 bestaetigt:**
  - "For a massive particle this gives something going like e^(-mb) for large mb, a Yukawa-like potential" mit Fn. 6
    (2 pi)^((2-D)/2) (m/b)^((D-4)/2) K_((D-4)/2)(mb): nur Stossparameterdarstellung des Eikonals, keine statische Kraft
    zwischen ruhenden Massen.
  - S. 24: "If the polarizations of particle 2 and 4 are the same as those of 1 and 3, then the configuration is constrained by
    unitarity along the t-channel. Therefore in this case we should get a strictly positive answer for the time delay for the
    contribution of any particle with a non-zero coupling." -> In dieser Konfiguration traegt **jeder** ausgetauschte Zustand
    mit positivem Vorzeichen bei; eine Aufhebung zwischen Spins gibt es dort nicht.
  - Zur Staerke der Kopplung an Materie sagt CEMZ an den gegrepten Stellen nichts Eigenes (grep "Yukawa|all particles|
    gravitational strength|universal|any particle": nur die zwei Stellen oben). Die Materieseite stammt von EGHS.
- **R7 (Eintrag ~~18:19~~ vor 18:18:23) Adelberger/Gundlach/Heckel/Hoedl/Schlamminger 2009, PPNP 62, 102, Textkopie im Sitzungs-Scratchpad
  (adelberger2009.txt, sha256 3a8fee01c98388f67bab60022e434c63851f4a8852ffd9045d27360374befb31; Herkunft der Kopie nicht von mir
  protokolliert), Z. 446-456, 540-548, 892-897. [A, Text; Abbildung nicht gesehen]** Erwartung E2 **bestaetigt** (eine Zeile):
  Fig. 10 (lambda >= 1 cm) "excluded at the 95% confidence level ... geophysical and astronomical constraints are taken from an
  earlier review [2]" -> keine neue Datenlage, Kette Fischbach & Talmadge 1999 -> AHN 2003 -> Adelberger 2009. Nebenbefund fuer den
  Gegensweep: Eoet-Wash-Aequivalenzprinzip mit der Erde als Quelle, eta(Be, Al) = (-1,5 +- 1,5) x 10^-13, umgerechnet auf
  stoffabhaengige Yukawa-Kopplungen "for lambda < 10 km" mit Topographie, Erdmodell ab 1000 km.
- **~~Vorab (18:21, vor R8)~~ KEINE Vorab-Erwartung: nachgetragen vor 18:20:25, NACH dem Abruf (Abstract 18:18:23, PDF 18:18:37); vorab galt nur E2:** E10 (Fischbach & Talmadge 1996, hep-ph/9606249, "Ten Years of the Fifth Force"): eine Abbildung
  |alpha|(lambda) wie AHN, Niveau 2 sigma oder 95 %, keine Tabelle.
- **R8 (Eintrag ~~18:22~~ Zukunftszeit; gemessen: geschrieben vor 18:20:25) Fischbach & Talmadge 1996, hep-ph/9606249v1, quellen/hep-ph-9606249.pdf (sha256
  08828178d60d20c3a754b9848d286480678e93dccb2ccfc6419eac2c4daa4940), Text S. 4 (txt Z. 83-92), Bildunterschriften S. 7,
  Fig. 1 S. 8 bei 170 dpi gerendert und abgelesen. [A, Text; A-Bild]** Erwartung E10 **VERLETZT, in zwei Punkten:**
  - **Achse "-alpha", nicht |alpha|.** Fig. 1 ("Constraints on alpha and lambda ... composition-independent experiments")
    traegt auf der Hochachse **-alpha**: gezeigt sind die Grenzen fuer **negatives** alpha (abstossender Zusatz in der
    Konvention V = -G m1 m2 (1 + alpha e^(-r/lambda))/r). AHN 2003 Abb. 4 beschriftet dieselbe Kurvenform als |alpha|.
  - **Niveau 2 sigma**, nicht "95 %": "the shading denotes the regions ... which are excluded by the data at the 2 sigma level";
    "the lower boundary of the shaded region is determined by superimposing the results of a number of different experiments".
  - **Traeger im km-Bereich benannt:** Pfeil "Tower" auf ~1e2 m und ~1e3 m; das Plateau ~5e-4 reicht von ~1 km bis ~20-25 km,
    danach "Earth - LAGEOS". Ablesung (1 Dekade lambda ~ 46 px, alpha ~ 74 px): **1 km ~6e-4; 2 km ~5e-4; 5 km ~5e-4;
    10 km ~4,5e-4; 20 km ~4,3e-4; 35 km ~3e-4** - deckungsgleich mit AHN (R1) innerhalb der Ablesegenauigkeit.
  - Text S. 6 (txt Z. 161-168): WTVD-Turm (Eckhardt 1988) sah "an attractive ('sixth') force"; nach der Gelaendekorrektur von
    Bartlett & Tew "agreed to within errors"; WABG (Romaides 1994), Erie (Speake 1990, PRL 65, 1967) und BREN (Thomas 1989,
    PRL 63, 1902) "found agreement with Newtonian gravity".
  - **Analysezyklus Z-1 (Vorzeichen):** [ES] Kopfrechnung mit R3: Ein anziehender Zusatz (alpha > 0) laesst die Schwere oben
    am Turm **unter** die Laplace-Fortsetzung fallen (Fehlbetrag -alpha x 2 pi G rho h); Eckhardt 1988 deutete "-500 uGal" genau
    so als anziehend (R3, Abstract) - Vorzeichenlogik stimmt. Romaides 1994: -33 +- 30 uGal bei 493 m -> 2-sigma-Bereich der
    Abweichung [-93; +27] uGal -> alpha in [-27/56 000; +93/56 000] = **[-4,8e-4; +1,7e-3]**. Die -alpha-Seite (4,8e-4) trifft das
    Plateau der Abb. (~5e-4) fast genau; die +alpha-Seite ist nach dieser Schaetzung **etwa dreimal schwaecher (~1,7e-3)**.
    Nur ein Turm, nur die "largest discrepancy", Dichte 2,7 angenommen: Faktor-2-Schaetzung, keine Quelle.
  - **Korrigierte Erwartung:** "|alpha| <~ 5e-4 bei 1-20 km" ist die Grenze fuer **abstossende** Zusatzkraefte. Fuer eine
    **anziehende** Turmkraft (gerade Spins, positive Residuen, R6) ist die einschlaegige Grenze im Bereich 1-20 km
    vermutlich um einen Faktor ~3 schwaecher, also ~1e-3 bis 2e-3 [ES]. Das aendert den Ausgang nach der Scheiterregel nicht
    (Abstand zu 1e-2 bleibt Faktor ~5), verkleinert aber den Sicherheitsabstand.
- **Zeitberichtigung (date 18:20:35):** Die Eintragszeiten bei R2-R8 waren geschaetzt, zwei davon lagen in der Zukunft; oben
  gestrichen und durch "geschrieben vor <date>" ersetzt. E10 war keine Vorab-Erwartung (nach dem Abruf geschrieben); der
  Erwartungsverstoss bei R8 wird deshalb gegen E1/E2 (Vorab 18:11:31: "Bildunterschrift nennt 95 %", "|alpha|") gemessen, nicht
  gegen E10. Ab hier nur date-Werte, Vorab-Eintraege vor dem Abruf.
- **Vorab (date 18:21:00, vor R9/R10):**
  - E11 (Maenaut 2411.17893, lokale Kopie, Definition von ell): ell steht in der Wirkung als ell^4 vor den R^3-Termen mit einem
    eigenen Zahlenvorfaktor (z. B. lambda_ev / 16 pi G); die Umrechnung auf EGHS c3^(1/4)/Lambda kostet hoechstens einen
    Faktor ~2 in der Laenge.
  - E12 (INSPIRE, 2024-2026, Fuenfte Kraft / Abstandsgesetz mit Yukawa bei Metern bis km): keine neue stoffunabhaengige
    km-Messung; hoechstens Vorschlaege (Atominterferometer, hohe Gebaeude, Gravimeter) oder Neuauswertungen.
- **R9 (Abruf 18:21:05; Eintrag danach) INSPIRE, Titel mit "fifth force" / "inverse-square law" / "non-Newtonian" / "Yukawa gravity",
  de > 2024-09, 25 Treffer, quellen/insp-isl-2024-2026.json. [S, nur Titel]** Erwartung E12 **bestaetigt** (eine Zeile): keine neue
  stoffunabhaengige Messung bei 1-35 km. Naechstliegend nur Titel "Constraining the Fifth Force Using the Earth as a Spin and Mass
  Source from the Chinese Space Station" (Vorschlag, Bahnhoehe ~400 km, also eher lambda >~ 100 km; Abstract nicht gelesen),
  sonst Labor (CHRONOS, MORRIS, Kurzreichweiten-Uebersicht), Galaxien, Galaktisches Zentrum, Schatten von Sgr A*/M87*.
- **R10 (Abruf 18:21:15) Maenaut u. a. 2411.17893, lokale txt-Kopie aus RUNDE-11 (PDF-sha256 111fc528...b0b0), Z. 115-135, Gl. (1).
  [A]** Erwartung E11 **bestaetigt, sogar enger** (eine Zeile): S = Int d^4x sqrt|g| /(16 pi G) [R + ell^4 lambda_ev R^3 + ...],
  R^3 = R_mn^rs R_rs^dg R_dg^mn, Grenze auf sign(lambda_ev) ell bei |lambda_ev| = 1. Gegen EGHS Gl. (2.5) (-R + c3 R^3/Lambda^4)
  ist das ell = c3^(1/4)/Lambda bis auf Vorzeichenkonvention, **Faktor 1**, sofern EGHS dieselbe Kontraktion R^3 meinen (dort
  nicht nachgelesen).

## 3. Gegensweep (geschrieben vor 18:22:21, date direkt danach)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
1. **Dass die km-Grenze vorzeichenblind |alpha| ist.** GEPRUEFT (R8): Die aeltere Zusammenstellung zeigt -alpha; die
   +alpha-Seite ist im Turmbereich nach Romaides' Zentralwert vermutlich ~3x schwaecher [ES]. -> Erwartungsverstoss V1.
2. **Dass "95 %" das Niveau der Kurve ist.** GEPRUEFT (R8): Fischbach & Talmadge 1996 schreiben "2 sigma"; AHN 2003 schreiben
   "95%". Fuer eine Gauss-Grenze ist das gleichwertig (95,4 %); die Original-Turmarbeiten habe ich nicht gelesen.
3. **Dass ell (GW) und ell_eff (EGHS) dieselbe Zahl sind.** GEPRUEFT (R10): ja bis auf Vorzeichenkonvention, Faktor 1, wenn
   dieselbe R^3-Kontraktion gemeint ist.
4. **Dass die Turmkraft genau die Reichweite lambda = ell_eff hat.** NICHT an einer Quelle geprueft (EGHS: "r ~", parametrisch).
   [ES] Unempfindlich: Fuer lambda zwischen 0,1 ell und 10 ell (100 m bis 350 km) bleibt die Grenze nach AHN Abb. 4 unter
   ~3e-3; laengere Reichweite (Regge-Verbreiterung ~ ell sqrt(ln(alpha' s)), [H]) verschaerft sie sogar (Earth-LAGEOS 1e-4 bis 1e-6).
5. **Dass die Turmkraft stoffunabhaengig ist.** Teilweise geprueft (R7): Ist sie stoffabhaengig, greifen Aequivalenzprinzip-Tests
   mit eta ~ 1e-13 bei lambda von < 10 km bis > 1000 km; das verschaerft die Grenze, schwaecht sie nicht [ES].
6. **Dass ein Turm wie eine Einzel-Yukawa wirkt.** Nicht geprueft. [ES] Gerade gegen ungerade Spins koennten sich teilweise
   aufheben; die Turmversuche messen fuer lambda >> h die Summe sum_n alpha_n, also muesste sich die Summe auf ~1e-3 genau
   wegheben (Feinabstimmung). CEMZ S. 24 [A]: in der t-Kanal-unitaeren Konfiguration traegt jeder Zustand positiv bei.

## 4. Protokollschluss (date 18:26:13)

- **Kurzfazit gekuerzt (vor 18:26:13)** auf 10 Zeilen. Gestrichene Fassungen, hier erhalten statt geloescht:
  - ~~"Seit 1996 keine neue Messung dort (Adelberger 2009 uebernimmt die Kurve; 2024-2026 nichts gefunden, ohne Websuche)."~~
    Zu stark: 2010-2023 nicht geprueft.
  - ~~"zwei neue Arbeiten staerken die infrarote Kausalitaet [S]"~~ Nur 2608.10871 tut das; 2609.16896 ist eine
    Unitaritaets-/Positivitaetsarbeit im Modell.
  - ~~Punkt 6 eigener Punkt~~ in Punkt 5 zusammengezogen; Einzelheiten stehen unter "Erwartungsverstoesse" und R2.
- Quellenliste: CEMZ-Zeitschrift als [L?] markiert; Lucchesi/Peron mit arXiv-Datum 2011 statt 2010 [L?]; Jekeli/Eckhardt/Romaides
  per INSPIRE-Datensatz 299717 bestaetigt (Abruf 18:25:21).
- **Regelverstoesse:** (1) Eintragszeiten R2-R8 zuerst geschaetzt, zwei in der Zukunft; berichtigt (Zeitberichtigung 18:20:35).
  (2) E10 war keine Vorab-Erwartung (nach dem Abruf geschrieben); als solche gekennzeichnet.
- Nicht gemacht: kein python/python3/awk, kein ssh, kein git, kein Peerbus, keine Unteragenten. WARUM-SPIN-2.md und CEMZ-MESS.md nur
  gelesen. Keine Sperrbereiche geoeffnet. Rechnungen nur Kopfrechnung (Turmempfindlichkeit, +alpha-Schaetzung, kappa).
- Geschrieben nur in RUNDE-12/cemz-ebene/ (diese Datei, quellen/ mit SHA256SUMS.txt). Bild-Renderings liegen im Scratchpad.

## 5. Nachlauf in der Zeitbox (Vorab, date 18:26:30, vor R11)

- E13 (CEMZ, Stellen zur Groesse der Turmkopplungen, lokale Kopie): CEMZ legen die Kopplung nur ueber die Forderung fest, dass
  der Turmbeitrag bei b ~ 1/m vergleichbar mit der Korrektur ist ("of order" G bzw. alpha_2/m^2-artig); zum Verhaeltnis
  Graviton- zu Materiekopplung sagen sie nichts; im Stringabschnitt sind alle Kopplungen ~ g_s.
- **R11 (Abruf ab 18:26:30; Eintrag vor dem naechsten date) CEMZ 1407.5597v1, lokale Kopie, grep "of order|comparable|g_s|coupl...|
  tower|Regge", gelesen Z. 96-134 (S. 3-4), 1325-1372 (S. 30-31, Abschn. 4.2), 1455-1500 (S. 33-34, Abschn. 4.4), 2050-2058 (S. 48). [A]**
  Erwartung E13 **teilweise VERLETZT -> Analysezyklus Z-2:**
  - S. 34: "since their size increases with mass logarithmically, we see that at high energies their effects appear at
    b^2 ~ alpha' log(s alpha') rather than the more naive expectation of b^2 ~ alpha'".
  - S. 48: "this type of tree level causality violation can only be fixed, at tree level, by higher spin particles at a mass scale
    m^2 ~ 1/alpha ... **Due to the presence of the logarithm we did not find a sharp bound between the corrections to the graviton
    three point amplitude, alpha, and the Regge slope alpha'.**"
  - S. 34: "We need a tower of particles with increasing spins and intricate relations between them so that the expansion can be
    resummed ... **Besides string theory, we do not know if there are other ways of doing this.**"
  - S. 31: massive Spin-2-Teilchen loesen das Problem nicht ("cannot be fixed by adding massive particles with spins J <= 2").
  - Zum Verhaeltnis der Turmkopplungen an Gravitonen und an Materie (kappa) steht an diesen Stellen nichts. Offene Frage 2 bleibt.
  - **Korrigierte Erwartung:** Nicht nur die Staerke, auch die **Reichweite** ist bei CEMZ nur parametrisch an l_eff gebunden:
    Turmmasse m^2 ~ 1/alpha, aber ausdruecklich ohne scharfe Schranke zwischen alpha und alpha' (Logarithmus). [ES] Fuer die Ebene
    heisst das: lambda = l_eff ist eine Setzung. Ein laengerer Bereich (Regge-Verbreiterung) verschaerft die Grenze (Earth-LAGEOS),
    ein kuerzerer (Turm schwerer um einen Faktor bis ~sqrt(log) ~ 9, [H]) schiebt l_eff = 1 km nach lambda ~ 100 m: dort |alpha|
    <~ 2e-3 bis 3e-3 (AHN, F&T); auf der +alpha-Seite unbekannt, bei Faktor ~3 wie im Turmbereich ~7e-3, also nahe an 1e-2.
    Das ist die engste Stelle der ganzen Ebene, und sie haengt an zwei ungeprueften Annahmen zugleich.
  - "intricate relations" + "Besides string theory, we do not know" [A]: Die Kopplungsstruktur des Turms ist bei CEMZ die der
    Stringtheorie, nicht abgeleitet. alpha ~ 1 ist damit eine Stringtheorie-Analogie, keine Folgerung.
- **Bericht nach R11 nachgezogen (vor 18:29:06):** V0 neu, Abbildung/Reichweite, Engste Stelle, U4, Gegensweep 4, Kalibrierung, Offene Frage 3,
  Folgeschritt. Kurzfazit Punkt 4 ersetzt; alte Fassung, hier erhalten: ~~"Bedingt: gilt nur in Regime I mit alpha ~ 1, und dafuer
  steht bei EGHS nur 'parametrically equal to gravitational' [A]. Eine Turmkraft muesste ~500- bis 2000-mal schwaecher als
  Gravitation sein, um durch die Daten zu passen."~~ (Die Zahl 500-2000 steht weiter in Ebene und U1.)
- Gegensweep-Zaehlung: sechs benannt, vier geprueft (1, 2, 3 an F&T/Maenaut; 4 an CEMZ S. 48).
- **Vorab (date 18:29:16, vor R12):** E14 (EGHS, Definition von R^3 bei Gl. 2.5, lokale Kopie): R^3 = R_mn^ab R_ab^cd R_cd^mn, dieselbe
  Kontraktion wie bei Maenaut; R~R^2 mit Dualem fuer c~3.
- **R12 (Abruf 18:29:16) EGHS 1704.01590, lokale txt-Kopie, Z. 340-362 (S. 5-6, Gl. 2.5). [A]** E14 **bestaetigt** (eine Zeile):
  S_eff = 2 Mpl^2 Int d^4x sqrt(-g) [-R + c3 R_mnrs R^mn_ab R^abrs / Lambda^4 + c~3 R~_mnrs R^mn_ab R^abrs / Lambda^4]; dieselbe
  Kontraktion wie Maenaut Gl. (1). Damit ell (Maenaut, |lambda_ev| = 1) = c3^(1/4)/Lambda (EGHS) bis auf Vorzeichenkonvention, Faktor 1.
- Ende (date): 2026-10-01 18:29:55 CEST. Zeitbox nicht ueberschritten.
