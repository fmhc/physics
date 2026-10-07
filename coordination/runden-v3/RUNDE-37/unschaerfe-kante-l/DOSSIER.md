# UNSCHAERFE-KANTE-L: Kann Heisenbergs Unschaerfe durch "Kantenfindung in Dimensionen" erklaert werden? (DOSSIER, feldforscher)

- Finn, woertlich: "Kann Heisenberg unschärfe durch Kantenfindung in Dimensionen in unserem Modell erklärt werden"
- Zusatz (Leitung 05:49, Finn woertlich): "-13.6 eV Quantum+coulomb für Elektronen?" (Abschnitt 7)
- Start 2026-10-05 05:48:08 CEST (date). Text geschrieben ab 06:07:39 CEST (date). Karte KARTE.md, Erwartungen HU1 bis HU5
  unveraendert. Alle Abrufe mit Erwartung vorher und Ausgang danach in ARBEITSFELD.md, Kopien in quellen/.
- Abrufe: 10 von 10 (A1 bis A10). Dazu 5 technische Fehlversuche ohne Inhalt (Abschnitt 13).
- Kennzeichen: [S] Quelle mit Abschnitt oder Gleichung, [S Abstract], [L] Lehrbuch/Gedaechtnis sicher, [L?] Gedaechtnis
  unsicher, [M] Schreibtischrechnung (Kopfrechnung, lokal nichts gerechnet), [ES] eigener Schluss, [H] Hypothese,
  [P] Projektdatei.

---

## 1. Ergebnis zuerst

1. **Nur so, nicht als Ursache.** Die Kantenwahl erklaert Heisenberg nur, wenn sie als **Amplitude** laeuft (Lesart b).
   Dann ist die Unschaerfe die gewoehnliche Fourier-Eigenschaft der Welle auf dem Netz und nichts Zusaetzliches.
   - Als **Zufall** (Lesart a) gibt sie die Form Delta x * m Delta u >= hbar/2 nur, wenn man die Diffusion D = hbar/2m
     einsetzt und Nelsons Zusatzdynamik dazunimmt.
   - Interferenz braucht ausserdem das i, und das kommt erst durch eine imaginaere Flip-Rate (Gaveau/Jacobson/Kac/
     Schulman 1984) bzw. eine Wick-Rotation (Ghose 2026) [S].
   - Die Unschaerfe tragen also Takt (Flip-Rate) und Phase, nicht die Kante selbst [ES].
   - Die Amplituden-Lesart hat das Projekt schon, unter dem Namen Schachbrett: Masse als Flip i eps m (Foster/Jacobson,
     DUNKEL-FLIP-L) und das 1+1-Schachbrett mit Zitterbewegung bei 2m (SCHACHBRETT-KAUSAL-1) [P].
2. **Die Unschaerferelation trennt die Lesarten nicht.** Ghose (arXiv 2609.29248, 24.09.2026) zeigt: Wiener-, Kac-,
   Bohm- und Feynman-Bahnen sind alle mit Delta x Delta p >= hbar/2 vertraeglich [S Abschn. 7, 8].
   - Trennen tun Bell bzw. Lokalitaet, die freie Ausbreitung (Delta x^2 ~ t gegen ~ t^2) und der Gitterrand
     Delta p ~ hbar/l (Abschnitt 5).
3. **Masse aus dem Netz:** Der unkorrelierte Irrweg gibt m = d hbar tau/l^2. Mit Planck-Masche sind das 3 m_Pl (HU5
   eingetroffen).
   - Leichte Teilchen gibt es nur ueber Persistenz: m = p_flip * m_Pl. Das Elektron braucht p_flip = 4,2e-23 je
     Planck-Takt, also eine Umkehr je 2,4e22 Takte [M]. Diese Kleinheit wird eingesetzt, nicht erklaert.
4. **Wasserstoff:** -13,6 eV = -(alpha^2/2) * hbar lambda_e.
   - Das Netz liefert hoechstens die Flip-Rate lambda_e (also die Masse) und D = hbar/2m. alpha und das hbar der
     Quantisierungsbedingung (Wallstrom) bleiben Eingabe.
   - Nelson reproduziert den Grundzustand: Die Diffusion treibt nach aussen, eine osmotische Drift vom Betrag alpha*c
     nach innen [M].
   - Naive Diffusion mit Coulomb-Kraft stuerzt ab [M]. SED-Wasserstoff ionisiert sich in Simulationen selbst
     (Nieuwenhuizen/Liska 2015) [S Abstract].
   - Eine Planck-Masche verschiebt die Niveaus relativ um ~1e-48, das liegt 33 Groessenordnungen unter der
     1S-2S-Genauigkeit von 4,2e-15 [M, S].
   limitation of our knowledge" [S Abstract]. Das ist eine epistemische Deutung im Sinn von de Broglie und Einstein.
   Einen Mechanismus nennt der Abstract nicht, HU4 ist im Wortlaut nicht belegt.

---

## 2. Erwartungsverstoesse (das eigentliche Ergebnis, Wichtigstes zuerst)

| Nr | Erwartet | Gefunden | Folge |
|---|---|---|---|
| V2 | Literatur: nur die allgemeine Nelson-Linie | Ghose, arXiv 2609.29248 (24.09.2026): Unschaerfe + Nelson + **persistente Kac-Dynamik** (Telegraph-Kantenwahl) + Dirac per Wick-Rotation, fast woertlich Finns Frage [S]. Unser eigener Scout hatte die Arbeit am 25.09. im Cache und am 28.09. mit `"topics":{}` eingeordnet, also keinem Projektthema zugeordnet [P: research-scout-claude-20260913/classification-cache.json] | Finns Frage ist Forschungsfront, nicht neu. Die Themenliste des Scouts hat eine Luecke (Unschaerfe, stochastische Mechanik, Kac) |
| V3 | Lesart (d): kein Treffer, der Unschaerfe aus Bewegung in einer verborgenen Richtung herleitet | Jalalzadeh 2023 (Annals Phys. 452, arXiv 2303.11104): Teilchen auf der Brane schwingt laengs der Zusatzdimension; daraus folgen Bohr-Sommerfeld, "a geometrical version of the uncertainty principle", die zeitunabhaengige Schroedinger-Gleichung; laut Highlights ist hbar "in terms of other fundamental constants" berechenbar [S Abstract] | (d) hat einen Literaturvertreter. Nicht gegengelesen (nur Abstract); ausserhalb des 24-Monats-Fensters, im Fenster kein (d)-Treffer |
| V5 | Schreibtisch-Vorgabe: "Delta x Delta k >= 1/2 gilt fuer jede Welle auf dem Netz" (nur gegenlesen) | Auf dem Gitter nicht exakt. Ein auf einem Knoten lokalisierter Zustand hat Delta x = 0 bei beschraenktem Delta k (k periodisch). Robertson mit [x, sin(kl)/l] = i cos(kl) gibt Delta x * Delta(sin(kl)/l) >= (1/2)\|<cos(kl)>\| [M] | Heisenberg gilt auf dem Netz nur fuer k << pi/l. Am Zonenrand geht die Schranke gegen 0. Das ist zugleich der Unterscheidungspunkt Gitter gegen GUP |
| V6 | HU3: GUP-Schranken (beta0) messen die Netz-Unschaerfe | Ein Gitter gibt **keine** Mindestunschaerfe (Delta x -> 0 moeglich), sondern beschraenkten Impuls und eine veraenderte Dispersion [M, ES]. Hossenfelder 2013 trennt GUP und modifizierte Dispersion als Modellklassen [S Abstract]. Fuer das Gitter zaehlt LHAASO 2024: E_QG,1 > 10 E_Pl (linear), E_QG,2 > 6e-8 E_Pl (quadratisch) [S Abstract] | Lineare Gitterkorrekturen sind bei Planck-Masche schon jetzt eingeschraenkt (Koeffizient < ~0,1 [ES]); quadratische sind frei |
| V7 (klein) | Keine Schranke beta0 < 1 | Bushev u. a. 2019: Pendeldaten von 1936 "could potentially lead to ... beta0 << 1", aber "cannot be reliably established" [S Abstract]. Al Ghifari u. a. 2025: "beta = 1.5e-7" ohne Einheit im Abstract [S Abstract]; als dimensionsloses beta0 gelesen waere es physikalisch unmoeglich, also dimensionsbehaftet [ES] | Einheitenfalle: "messen die zwei Zahlen dasselbe?" |
| V8 (klein) | Ghose zitiert Fuerth 1933 (50 %) | nicht zitiert | HU1-Fuerth-Teil bleibt [L?] |

---

## 3. Urteile HU1 bis HU5

| Nr | Urteil | Beleg |
|---|---|---|
| HU1 | **teilweise eingetroffen.** Der Nelson-Teil ist belegt: "Brownian motion with diffusion coefficient hbar/2m and no friction ... leads in a natural way to the Schroedinger equation" [S Abstract, Nelson 1966]. Der Fuerth-Teil ist nicht geprueft [L?] (nicht abrufbar, von Ghose nicht zitiert). | Die Formgleichheit ist am Schreibtisch nachvollziehbar [M]: Mit der osmotischen Geschwindigkeit u = D d/dx ln rho gilt <(x - <x>) u> = -D (partielle Integration), also nach Cauchy-Schwarz Delta x * Delta u >= D. Mit D = hbar/2m folgt Delta x * m Delta u >= hbar/2 (Cramer-Rao-Form). **Bedeutung [ES]:** Die Ungleichung gilt fuer jede glatte Dichte, sobald man "Impuls" als m mal osmotische Geschwindigkeit definiert. Sie ist deshalb inhaltlich schwach; der Inhalt steckt allein in D = hbar/2m. |
| HU2 | **im Kartenwortlaut nicht eingetroffen (V1).** Einzelzeit-Statistik: ja, die Born-Regel ist eingebaut (\|psi\|^2 = rho, Ghose 2604.03214 [S Abstract]). Mehrzeit: mit effektivem Kollaps QM-gleich (D/B 2022 [S Abstract]). Bell: Nelson ja, aber nichtlokal; lokale Kantenwahl nein. | Grabert/Haenggi/Talkner 1979 nicht abrufbar (nicht in INSPIRE), bleibt [L?]; die Kritik selbst ist als "long-standing criticism ... by ... Edward Nelson" belegt [S Abstract D/B]. Neu dazu: **Wallstrom 1994**. Die Quantisierungsbedingung (Kreisintegral grad S dx = n h) folgt nicht aus der stochastischen Dynamik, sie wird aufgesetzt [S Ghose 2609.29248 Abschn. 4.1, Gl. 35]. |
| HU3 | **eingetroffen fuer die belastbaren Schranken, mit Einschraenkung (V6).** Bushev 2019: beta0 < 5,2e6 (Saphir), Quarz-Schaetzung < 4e4 [S Abstract]; Das/Vagenas 2008: Lamb < 1e36, Landau < 1e50, STM < 1e21, elektroschwach <= 1e34 [S Gl. 13, 22, 34]. Im 24-Monats-Fenster kein belastbares beta0 < 1 (A4). | **Einschraenkung [ES]:** Fuer ein Gitter sind die GUP-Schranken die falschen; die richtigen sind die zur Lorentz-Verletzung (LHAASO). Eine Planck-Masche ist nur dann "nicht verboten und nicht pruefbar", wenn ihre Dispersionskorrekturen mindestens quadratisch sind. |
| HU4 | **im Wortlaut nicht eingetroffen.** Der Abstract von SPIE 8832 883219 nennt keinen Radius und keine Bahn, die Deutung ist epistemisch [S Abstract]. | Volltext nicht gelesen (SPIE, nicht frei); SPIE 2011 und 2015 sind bei INSPIRE nicht gefuehrt. Abschnitt 8. |
| HU5 | **eingetroffen [M].** m = d hbar tau/l^2 mit l = l_Pl, tau = t_Pl ergibt m = d hbar/(c l_Pl) = d m_Pl = 3 m_Pl, rund 6,5e-8 kg bzw. 3,7e19 GeV/c^2. | Kopfrechnung: hbar/(c l_Pl) = sqrt(hbar c/G) = m_Pl. Gegengelesen: D = l^2/(2 d tau) gilt je Raumkomponente, und Nelsons D ist ebenfalls je Komponente definiert; die Formel ist also konsistent. |

---

## 4. Tabelle der Lesarten (a) bis (d)

| Lesart | Mechanismus | Was folgt | Masse bzw. Vorfaktor aus dem Netz | Abweichung von der QM | Datenlage |
|---|---|---|---|---|---|
| **(a) Zufall:** Irrweg, Telegraph/Kac, Nelson | Kante je Takt zufaellig gewaehlt; reelle, positive Wahrscheinlichkeiten | Unkorreliert: Diffusion D = l^2/(2 d tau) [M]. Telegraph: ballistisch fuer t << 1/(2 lambda), diffusiv mit D = v^2/(2 lambda) danach [S Ghose Gl. 54]. Heisenberg-Form nur als Delta x * m Delta u >= hbar/2 mit D = hbar/2m [M]. Schroedinger-Dynamik erst mit Nelsons Zusatzannahmen [S Abstract Nelson 1966; Ghose Gl. 85, 86] | Irrweg: m = d hbar tau/l^2 (Planck-Masche: 3 m_Pl). Telegraph: hbar lambda = m c^2 [S Ghose Gl. 76], also m = p_flip m_Pl bei tau = t_Pl [M] | **Ohne Nelson-Drift:** keine Interferenz, Breite waechst wie sqrt(t) statt linear, naive Coulomb-Bindung kollabiert [M]. **Mit Nelson:** QM-gleich inkl. Mehrzeit (effektiver Kollaps), aber nichtlokal und mit aufgesetzter Quantisierung (Wallstrom) | Bell-Verletzung gemessen [L] schliesst die **lokale** Variante aus. Nelson nach Recherchestand empirisch nicht von QM unterscheidbar (DOPPELSPALT-L Z. 170 [P]; D/B 2022) |
| **(b) Amplitude:** Quantenlauf, Dirac-Automat, Kac nach Wick-Rotation | Kantenwahl mit komplexer Amplitude; Mischrate imaginaer (GJKS) bzw. Zeit Wick-rotiert (Ghose) | Dirac-Gleichung in 1+1 D aus dem Zwei-Sektor-Kac-Prozess [S Abstract GJKS 1984; Ghose Gl. 72 bis 77]; Heisenberg als Fourier-Eigenschaft fuer k << pi/l; am Zonenrand Delta x * Delta(sin kl/l) >= (1/2)\|<cos kl>\| [M] | hbar lambda = m c^2 wie in (a) [S Ghose Gl. 76]; Lichtgeschwindigkeit = Sektorgeschwindigkeit. Auf BCC: Weyl-Automat mit c = 1/sqrt(3) [P QCA-TETRA-1] | Nur bei k ~ pi/l (Dispersion, Anisotropie, Verdoppler: drei weitere Kegel H, P, P' auf BCC [P QCA-TETRA-1]) | LHAASO: lineare Dispersionskorrektur bis 10 E_Pl ausgeschlossen, quadratische offen [S Abstract]. **Auf Finns Diamantnetz mit 2 Zustaenden je Knoten gibt es keinen isotropen unitaeren Automaten [P QCA-TETRA-1]**. Im Projekt schon vorhanden: Masse als Flip i eps m im 3+1-Schachbrett (Foster/Jacobson, fcc/bcc, nicht unitaer) [P DUNKEL-FLIP-L]; 1+1-Schachbrett auf Kausalmenge mit ZB bei 2m [P SCHACHBRETT-KAUSAL-1] |
| **(c) Diskretheit:** kleinste Laenge, GUP | Masche l begrenzt den Impuls (Brillouin-Zone); GUP setzt dagegen eine Mindest-Unschaerfe Delta x >= hbar sqrt(beta) | Gitter: **keine** Mindestunschaerfe, beschraenkter Impuls, modifizierte Dispersion [M]. GUP: Delta x Delta p >= (hbar/2)(1 + beta Delta p^2 + ...) [S Das/Vagenas Gl. 1] | keine Masse; Vorfaktor beta0 ~ 1 bei Planck-Masche [ES]; Mu/Wu/Yang 2009: Mindestlaenge = Kompaktifizierungsradius [S Abstract] | Erst bei Delta p ~ hbar/l, also bei Planck-Impulsen | beta0: belastbar >= 1e4 bis 1e6 (Oszillatoren, mit Vorbehalt fuer Zusammengesetztes), Wasserstoff/Lamb < 1e36 [S]. Planck-Gitter nur ueber LIV pruefbar (V6) |
| **(d) "In Dimensionen":** verborgene bzw. kompakte Richtung [H] | Bewegung bzw. Kantenwahl in einer Zusatzrichtung erscheint in 3D als Masse bzw. Unschaerfe | Kaluza-Klein: Impuls in der Zusatzrichtung erscheint als Masse [L]. Jalalzadeh 2023: Schwingung laengs der Zusatzdimension gibt "a geometrical version of the uncertainty principle" und die Schroedinger-Gleichung [S Abstract]. Magpantay 2011: Bulk-Bewegung **modifiziert** Heisenberg zeitabhaengig [S Abstract] | KK: m = n hbar/(R c) bei Radius R [L]; Jalalzadeh: hbar aus anderen Konstanten (Formel nicht gelesen) [S Abstract, Highlights] | Lake u. a. 2023: bei Planck-Kompaktifizierung keine Abweichung, nur grosse Zusatzdimensionen aendern die Unschaerfe [S Abstract] | Keine Messung trennt; grosse Zusatzdimensionen sind an Collidern eingeschraenkt [L?]. Im 24-Monats-Fenster kein (d)-Treffer |

**Lesart (e), aus Finns Wortlaut moeglich [ES/H]:** "Dimension" als Hausdorff-Dimension des Pfades.
- Feynman-Pfade skalieren brownsch, Delta x ~ eps^(1/2) (Abbott/Wise 1981, zitiert bei Ghose Gl. 4 bis 6 [S]).
- Ein Telegraph-Pfad hat unterhalb der Persistenzlaenge c/(2 lambda) = hbar/(2 m c) die Dimension 1, darueber 2 [M].
- Beim Elektron liegt der Uebergang bei 1,9e-13 m, der halben reduzierten Compton-Laenge [M].
- So gelesen macht die Kantenwahl keine Unschaerfe. Sie legt nur fest, ab welcher Laenge der Pfad zweidimensional
  wird, und das ist D = hbar/2m.

---

## 5. Regime, Moderatoren und Unterscheidungspunkte

### 5.1 Regime (Regel 1)

| Widerspruch in der Literatur | Regime A | Regime B | Moderator |
|---|---|---|---|
| "Unschaerfe ist ontisch" gegen "Unschaerfe ist Statistik ueber Bahnen" | Amplitude (komplex) | Wahrscheinlichkeit (reell, positiv) | reelle gegen imaginaere Flip-Rate bzw. reelle gegen Wick-rotierte Zeit [S GJKS, Ghose Abschn. 6.2] |
| Nelson scheitert an Mehrzeit-Korrelationen gegen Nelson stimmt | Prozess ohne Messmodell (GHT-/Nelson-Kritik) | Prozess mit effektivem Kollaps (Blanchard 1986, D/B 2022) | ob die Messung den Prozess veraendert [S Abstract] |
| Kantenwahl verletzt Bell nicht gegen doch | lokale Drift (Knoten kennt nur Nachbarn) | Drift aus psi im Konfigurationsraum | Lokalitaet [L, S Abstract D/B] |
| SED gibt den H-Grundzustand gegen SED ionisiert | kurze Simulationszeit (Cole/Zou 2003, laut N/L-Abstract) | lange Zeit, voll 3D (Nieuwenhuizen/Liska 2015) | Simulationsdauer [S Abstract] |
| Telegraph-Elektron ballistisch gegen diffusiv | t << 1/(2 lambda) = 6,4e-22 s | t >> 6,4e-22 s | Zeitfenster (Compton-Zeit) [M] |
| GUP-Schranke 5e6 gegen 1e21 bis 1e36 | Schwerpunkt makroskopischer Koerper | elementare Teilchen (Atom, STM) | Zusammengesetzt gegen elementar [S Abstract Bosso 2023] |

### 5.2 Unterscheidungspunkte (Regel 2)

| Erklaerungspaar | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|
| Klassischer Irrweg (ohne Nelson-Drift) gegen QM | Freie Breite: Delta x^2 = Delta x0^2 + 2 D t gegen Delta x0^2 + (hbar t/(2 m Delta x0))^2 [L]; Interferenz | ja, laengst gegen den Irrweg entschieden (Einzelteilchen-Interferenz [L]) |
| Nelson gegen QM | Einzel- und Mehrzeit-Statistik gleich; Trennung hoechstens ausserhalb des Quantengleichgewichts oder ueber Ghoses vorgeschlagene Abstandsskala fuer Bell-Grenzen [S Abstract 2604.03214] | nach Recherchestand **empirisch nicht unterscheidbar** |
| Lokale Kantenwahl gegen QM | CHSH > 2 | ja, gemessen [L]; lokal ausgeschlossen |
| Telegraph (reell) gegen Dirac (Amplitude) | mittlere Geschwindigkeit: Telegraph <v> = c exp(-2 lambda t) (Zerfall), Dirac <v> = c cos(2 Delta t/hbar) (Schwingung) bei t ~ hbar/(m c^2) [P five-why, Projekt hat beides gerechnet] | am freien Elektron nicht (~1e-21 s); im Analogon gezeigt (Gerritsma 2010 [P]) |
| Gitter gegen GUP | Gitter: Delta x -> 0 erlaubt, p beschraenkt, Schranke (1/2)\|<cos kl>\| -> 0 am Zonenrand. GUP: Delta x_min = hbar sqrt(beta), p unbeschraenkt [M] | nur bei Delta p ~ hbar/l, also unzugaenglich |
| Planck-Gitter gegen Kontinuum | Lichtlaufzeit je Energie: linear bei E/E_Pl, quadratisch bei (E/E_Pl)^2 | linear ja (LHAASO), quadratisch nein [S Abstract] |
| (d) Planck-kompakte Zusatzrichtung gegen 3D | keine Abweichung bei Planck-Radius [S Abstract Lake 2023] | **nicht unterscheidbar** |

---

## 6. Gegenlesen der Schreibtisch-Vorgaben der Leitung

| Vorgabe | Gegengelesen | Kennzeichen |
|---|---|---|
| Jede Welle erfuellt Delta x Delta k >= 1/2, also gilt Heisenberg auf dem Netz | Im Kontinuum ja. Auf dem Gitter nur fuer k << pi/l; exakt gilt Delta x * Delta(sin kl/l) >= (1/2)\|<cos kl>\|, Herleitung aus [x, T] = -l T fuer die Verschiebung T = exp(i k l) (V5) | [M], Gegenlese-Befund |
| Irrweg: D = l^2/(2 d tau) | stimmt, je Komponente; auf dem Diamantnetz unveraendert (Abschnitt 9) | [M] |
| Telegraph: D = c^2/(2 lambda), mit lambda = m c^2/hbar folgt D = hbar/(2m) | stimmt; Ghose Gl. 54, 58, 59, 76 woertlich [S]. Zu beachten: In 1D halbiert sich die Korrelationszeit, 1/(2 lambda) statt 1/lambda (Ghose Gl. 51, 52) [S]. Bei voller Neuwahl der Richtung in 3D waere D = c^2/(3 lambda) [M] | [S], [M] |
| Masse aus dem Netz m = d hbar tau/l^2 | stimmt algebraisch; HU5 [M] | [M] |
| Elektron: lambda ~ 7,8e20/s, eine Umkehr je ~2e22 Planck-Takte (m_e/m_Pl ~ 4,2e-23) | stimmt: lambda_e = 8,19e-14 J/1,055e-34 J s = 7,76e20 1/s; lambda_e t_Pl = m_e/m_Pl = 4,19e-23, also 2,39e22 Takte je Umkehr | [M] |

---

## 7. Wasserstoff (-13,6 eV)

### 7.1 Was muesste die Kantenwahl liefern? Eingabe gegen Ergebnis

- Lehrbuchwert [L, M gegengelesen]: E_1 = -alpha^2 m_e c^2/2 = -13,606 eV. Dazu gehoeren a_0 = hbar/(alpha m_e c) =
  5,29e-11 m und das Minimum von hbar^2/(2 m r^2) - e^2/(4 pi eps0 r) bei r = a_0.
- **Umgeschrieben [M]:** E_1 = -(alpha^2/2) * hbar lambda_e mit hbar lambda_e = m_e c^2 [S Ghose Gl. 76]. Die
  Bindungsenergie ist also der Bruchteil alpha^2/2 = 2,66e-5 der "Flip-Energie" des Telegraph-Elektrons.

| Groesse | Was das Netz liefern koennte | Status |
|---|---|---|
| m_e | Flip-Rate lambda_e = 7,76e20 1/s, bzw. p_flip = 4,19e-23 je Planck-Takt | **Eingabe.** Die Kantenwahl uebersetzt nur Rate in Masse, warum p_flip so klein ist, sagt sie nicht [ES] |
| hbar (in D) | D = c^2/(2 lambda) liefert nur das **Verhaeltnis** hbar/m = 2 D | halbes Ergebnis: Takt und Masche geben D, aber nicht hbar und m getrennt [M] |
| hbar (in E = hbar omega und in der Quantisierung) | Rate in Energie umrechnen und die Bedingung "Kreisintegral grad S dx = n h" | **Eingabe** (Planck-Einstein bzw. Wallstrom [S Ghose Abschn. 4.1]). Nur wenn die Masche definitorisch die Planck-Wirkung je Takt traegt (hbar = m_Pl c l_Pl), ist es eine Einheitenwahl [ES] |
| e bzw. alpha | Coulomb-Staerke | **Eingabe;** die Kantenwahl sagt nichts ueber Ladung |

- **Folgerung [ES]:** Die Kantenwahl kann hoechstens erklaeren, dass hbar/m als Diffusion auftritt. Die Zahl -13,6 eV
  braucht m_e und alpha von aussen, und fuer die diskreten Niveaus ein zweites hbar (Quantisierung).

### 7.2 Klassisch-stochastische Erklaerungen am Wasserstoff

- **Nelson, Grundzustand [M, Schreibtisch]:**
  - rho = exp(-2r/a_0)/(pi a_0^3). Daraus folgt die osmotische Geschwindigkeit u = (hbar/2m) grad ln rho =
    -(hbar/(m a_0)) r^, vom Betrag alpha c = 2,19e6 m/s nach innen. Die Stromgeschwindigkeit ist v = 0.
  - Energie: (m/2)<u^2 + v^2> + <V> = alpha^2 m c^2/2 - alpha^2 m c^2 = -alpha^2 m c^2/2. Grundlage ist die
    Madelung-Identitaet <p^2>/2m = (m/2)<v^2 + u^2> [L, M].
  - Bild: Die Diffusion (D = hbar/2m) treibt nach aussen, eine konstante Drift alpha c nach innen. Das Gleichgewicht ist
    der Grundzustand.
  - Yordanov 2024 (Phys. Scr. 101): Bahnsimulationen des Brownschen Elektrons konvergieren gegen die Born-Verteilungen
    und die QM-Energiemittel. L_z = m hbar kommt erst nach auferlegter Eindeutigkeit der Phase [S Abstract].
  - Lynd 2025: Das Geschwindigkeitsfeld wird aus Potential **und Gesamtenergie** berechnet, die Energie ist also
    Eingabe [S Abstract].
- **Naive Diffusion mit Coulomb-Kraft [M]:** Ueberdaempfte Bewegung mit Drift F/(m gamma) hat die stationaere Dichte
  exp(-V/(m gamma D)) = exp(+k/(r m gamma D)). Die ist bei r -> 0 nicht normierbar, das Elektron stuerzt ab. Nelsons
  Drift ist nicht die Kraft, sondern folgt aus dem stochastischen Newton-Gesetz. Genau diese Zusatzannahme verhindert
  den Absturz.
- **SED (Nullpunktfeld):** Nieuwenhuizen/Liska 2015 [S Abstract]:
  - "Though short time results suggest a trend towards confirmation, in all attempted modelings the atom ionises at
    longer times."
  - Mit relativistischen Korrekturen "the self-ionisation ... remains present"; als Ursache vermuten sie die
    Punktladung (Found. Phys. 45).
  - Cole/Zou 2003 (kuerzer, laut N/L-Abstract) war noch zustimmend.
  - Im 24-Monats-Fenster kein neuer SED-Wasserstoff-Treffer (INSPIRE-Freitext, A6). Urteil: nach Recherchestand
    nicht geloest, nicht "widerlegt".
- **Zusammen [ES]:** Klassischer Zufall allein ergibt keinen Wasserstoff. Mit Nelsons Dynamik, D = hbar/2m und
  aufgesetzter Quantisierung ergibt er ihn exakt. SED liefert ihn nach Recherchestand nicht.

### 7.3 Messdaten und Schranken (erweitert HU3)

- 1S-2S: Parthey u. a. 2011: f = 2 466 061 413 187 035 (10) Hz, relativ 4,2e-15 [S Abstract]. Matveev u. a. 2013
  liegt in derselben Groessenordnung [L?, nicht abgerufen].
- GUP am Wasserstoff, Das/Vagenas 2008: relative Korrektur der Lamb-Verschiebung ~0,47e-48 beta0 (Gl. 12), daraus
  beta0 < 1e36 bei einer Lamb-Genauigkeit von 1e-12 (Gl. 13) [S].
- Eigene Abschaetzung fuer die Bindungsenergie [M]:
  - Delta E = (beta0/(m M_Pl^2 c^2)) <p^4> mit <p^4>_1S = 5 (m alpha c)^4.
  - Daraus Delta E/\|E_1\| = 10 beta0 alpha^2 (m_e/M_Pl)^2, rund 0,9e-48 beta0, also etwa 1e-47 eV bei beta0 = 1.
  - Das liegt rund 33 Groessenordnungen unter der 1S-2S-Genauigkeit. Allein aus 1S-2S folgt keine Schranke, weil 1S-2S
    die Rydberg-Konstante mitbestimmt [ES].
  - Fuer ein **Gitter** statt GUP gilt dieselbe Groessenordnung [M]: Die Gitterdispersion (hbar^2/(m l^2))(1 - cos kl)
    hat den p^4-Term -(l^2/(24 hbar^2 m)) Summe p_i^4. Bei l = l_Pl entspricht das einem \|beta0\| ~ 1/24, mit
    anisotroper Form. Die Aussage "Planck-Masche ~1e-48 relativ" gilt also fuer beide Lesarten (c).
- Fuer ein Gitter zaehlt zusaetzlich LHAASO: E_QG,1 > 10 E_Pl, E_QG,2 > 6e-8 E_Pl [S Abstract].
- **HU3 erweitert:** Auch Wasserstoff laesst eine Planck-Masche unbegrenzt (beta0 ~ 1 liegt 36 Groessenordnungen unter
  der Lamb-Schranke).

### 7.4 Larmor: Was heisst der klassische Absturz fuer unsere Modelle? [ES]

- Lehrbuch [L, M Kopfrechnung]: Ein klassisches Punktelektron auf der Bohr-Bahn strahlt und stuerzt in
  a_0^3/(4 r_e^2 c) = 1,6e-11 s ab.
- **Punktfoermiges bzw. kompaktes Soliton auf einer Bahn:** Es strahlt genauso, sobald es Ladung traegt und
  beschleunigt wird. Ein Q-Ball, der den Kern **umlaeuft**, ist kein Atom [ES].
- **Stationaere Feldwolke:**
  - Ein Q-Ball dreht nur seine innere Phase; seine Ladungsdichte \|phi\|^2 ist zeitlich konstant und strahlt nicht
    [M]. Eine um den Kern **gebundene stationaere Feldwolke** umgeht Larmor wie Schroedingers Ladungswolke [ES].
  - Dann liefert das klassische Feld aber nur **Frequenzen** omega_n, keine Energien. -13,6 eV braucht E = hbar
    omega, also eine gequantelte Ladung Q = hbar.
  - Genau die fehlt der klassischen Gesamtformel: "Q bleibt klassisch kontinuierlich" [P HILBERT.md Abschn. 2].
- **Codex-Vermittler** (g chi \|phi\|^2, Masse m als Yukawa-Reichweite [P RUNDE-35.md Z. 277]):
  - Ein massiver Vermittler kann unterhalb seiner Massenschwelle (Bahnfrequenz < m c^2/hbar) nicht abstrahlen, liefert
    aber kein 1/r.
  - Ein Vermittler, der 1/r liefert, ist (fast) masselos und strahlt bei Bahnbewegung ab [ES].
  - Zielkonflikt: Coulomb-Form und Strahlungsfreiheit gibt es nur zusammen mit einer stationaeren Wolke, nicht mit einer
    Bahn [ES, H]. Gegen die Modelldateien ist das **nicht** geprueft.

---


- **SPIE 8832, 883219 (2013), "The physical origins of the uncertainty theorem"**, DOI 10.1117/12.2022656
  [S Abstract, ueber INSPIRE]:
  - Die Unschaerfe sei "not a property of the physical world but rather a limitation of our knowledge about the actual
    state of a physical process. This view conforms to the quantum theory of Louis de Broglie and to Albert Einstein's
    interpretation."
- **SPIE 8832, 88320H (2013), "The nature of the photon in the viewpoint of a generalized particle model"**
  [S Abstract]: Teilchen seien ausgedehnt, die Masse ohne Higgs; zur Unschaerfe nichts.
- **Website [P fmhc-physics-fulltext.md Z. 304 bis 311]:** Welle-Teilchen-Dualitaet "classically understood according to
  gelesen.
- **Andockpunkt [ES]:**
    deterministische Gegenstueck zum Zwei-Sektor-Telegraph (Sektoren +c und -c): periodische Umkehr statt
    Poisson-Umkehr.
  - Seine epistemische Unschaerfe waere dann Unkenntnis der inneren Phase.
  - Pruefstein: Ein deterministischer Umlauf ohne Zufall gibt dem Schwerpunkt **keine** Diffusion (D = 0). Eine
    Unkenntnis der Phase erzeugt Delta x ~ hbar/(m c) nur auf der Compton-Skala, nicht Delta x Delta p >= hbar/2 fuer
    grosse Wellenpakete.

---

## 9. Bezug zu Finns Netz [H]

- **Was "Finns Netz" im Projekt ist [P LICHT-FINN-NETZ-1 PLAN.md]:** regelmaessige Tetraeder, die sich an den Ecken
  beruehren (Pyrochlor). Die Diamant-Knoten sind die Tetraedermitten.
  - Die 4 Kanten je Knoten sind also die Bindungen des Diamant-Graphen der Tetraedermitten [P].
  - Pyrochlor ist der Kantengraph des Diamantnetzes [L]. Eine **Kantenwahl auf dem Diamanten ist eine Platzwahl auf
    Finns Pyrochlor-Ecken**, die "Kante" ist also selbst ein Ort von Finns Netz [ES].
- **Vorfaktor (Diamant, 4 Kanten) [M]:**
  - Unkorrelierte Wahl: Die vier Tetraedervektoren summieren sich zu null (keine Drift). Wegen der kubischen Symmetrie
    ist das zweite Moment isotrop, je Komponente l^2/3.
  - Also D = l^2/(6 tau), **unabhaengig von der Koordinationszahl.** Die 4 Kanten aendern am Vorfaktor nichts.
  - Persistente Regeln aendern ihn: D = (l^2/(6 tau)) (1 + gamma)/(1 - gamma) mit gamma = mittlerer Kosinus
    aufeinanderfolgender Schritte.
  - Ohne Ruecksprung ist gamma = 1/3, D verdoppelt sich. Gleiche Bindung zurueck heisst auf dem Diamanten Hin-und-her
    (gamma = -1).
- **Geradeauslauf auf dem Diamanten [M]:** Es gibt keine gerade Fortsetzung, nur Zickzack entlang <110>, mit der
  Geschwindigkeit sqrt(2/3) l/tau = 0,8165 l/tau.
  - Dieselbe Zahl steht als isotrope Kegelgeschwindigkeit des W-D-Operators auf Finns Netz ("abs(c) = 2b/3 = 0,8165")
    [P DIAMANT-FERMION-L ARBEITSFELD.md Z. 31 und DOSSIER.md Z. 125, dort aus LICHT-FINN-NETZ-1].
  - Gleiche Zahl, Zusammenhang nicht geprueft [ES]. Fuer tau = l/c heisst das: Die effektive Lichtgeschwindigkeit des
    Netzes ist kleiner als l/tau. Das aendert m nur um O(1).
- **Takt:** Das Elektron braucht eine Umkehr je 2,4e22 Planck-Takte [M]. Ein Netz mit Planck-Takt muss diese kleine
  Zahl tragen; das Hierarchieproblem wird damit zu einer Frage an die Flip-Wahrscheinlichkeit [ES].
- **Verborgene Haelfte [H]:**
  - Der Kac-Prozess hat zwei Sektoren (+c und -c). Auf dem Diamanten liegen sie natuerlich in den Untergittern A und B,
    denn von A fuehren die Richtungen e_i weg, von B die Richtungen -e_i [M].
  - Das Tensor-Drittmoment der Tetraedervektoren (proportional \|eps_abc\|) wechselt zwischen A und B das Vorzeichen.
    Ueber zwei Schritte hebt es sich auf [M].
  - Ob die verborgene Haelfte mit eigenem Takt (Finns "dark tick", SPIEGEL-HAELFTE-1 [P RUNDE-42.md Z. 29]) das
    fehlende i liefert, also den reellen Kac-Prozess zu einem unitaeren macht (Kawabata/Ashida/Ueda: "hidden entangled
    partner" [P RUNDE-45.md Z. 232]), ist offen. Das waere der einzige Weg, auf dem Lesart (a) ohne Wick-Rotation zu (b)
    wuerde [H].
- **"In Dimensionen" [ES]:** Eine verborgene Richtung kann in 3D als **Masse** erscheinen (KK [L]; Umlauf bzw.
  Zitterbewegung).
  - Als **Unschaerfe** erscheint sie nur ueber eine Amplitude oder eine Phase.
  - Jalalzadeh 2023 behauptet mehr (geometrische Unschaerfe, hbar berechenbar) [S Abstract]; das ist ungelesen und zu
    pruefen.

---

## 10. Kartenvorschlag (hoechstens einer)

**KAC-DIAMANT-WICK-1: Gibt die Wick-rotierte Kantenwahl auf Finns Diamantnetz einen isotropen Dirac-Kegel mit
hbar lambda = m c^2?**

- **Frage:**
  - Zustand = gerichtete Kante (Knoten A oder B, eine der 4 Richtungen). Der Erzeuger hat Transport c e_i . k je
    Sektor und eine reelle Mischrate lambda zwischen den Richtungen.
  - Mischregel einmal gleichverteilt, einmal ohne Ruecksprung.
  - Wick-Rotation nach Ghose: t -> i t, v -> -i v [S Ghose Gl. 66 bis 77].
  - Gefragt: Hat das 8x8-Bloch-Spektrum bei k = 0 einen isotropen linearen Kegel, mit Masse aus hbar lambda und
    welcher Entartung?
- **Ableitbarkeitsprobe (vor der Karte):**
  - Vorab ableitbar [M]:
    - die k = 0-Niveaus der Mischmatrix (Singulett und Triplett der 4 Richtungen);
    - das reelle D = (l^2/(6 tau))(1 + gamma)/(1 - gamma);
    - dass die erste Ordnung je Untergitter anisotrop ist. Der Triplett-Block ist proportional zur Matrix [[0, k_z,
      k_y], [k_z, 0, k_x], [k_y, k_x, 0]], deren Eigenwerte von der Richtung abhaengen. Ueber A und B wechselt das
      Vorzeichen.
  - **Nicht vorab ableitbar** (hier nicht entschieden): ob der Zwei-Untergitter-Erzeuger nach der Rotation einen
    isotropen Kegel, Knotenlinien oder gar kein Kegelspektrum hat. Davon haengt ab, ob die Wellen der Kantenwahl auf
    Finns Netz ueberhaupt Heisenberg-Wellen eines Dirac-Teilchens sind.
  - Der Ausgang kann also scheitern und bestehen.
- **Projekt-grep (alle Dateitypen, Ausschluesse wie vorgeschrieben, 06:03 CEST):**
  - "Wallstrom": nur diese Karte.
  - "GJKS|Gaveau|Goldstein-Kac|Kac-Prozess|Kac process|Kac-Dirac|telegrapher": nur diese Karte und Scout-Cache.
  - "Wick-Rotation" mit Kac oder Telegraph: nur diese Karte (sonst CDT-Quellen).
  - **Nachgrep im Gegensweep (06:11 CEST), Schachbrett-Vokabular "checkerboard|Schachbrett|Foster/Jacobson":** Treffer.
    Das Thema ist im Projekt unter anderem Namen bekannt:
    - DUNKEL-FLIP-L: Foster/Jacobson (arXiv 1610.01142), 3+1-Schachbrett mit Spin auf fcc bzw. bcc, doppler-frei,
      "nicht unitaer"; Masse als Chiralitaets-Flip mit Amplitude i eps m je Schritt; Zitterbewegung bei 2m
      [P DUNKEL-FLIP-L DOSSIER Z. 30, 48, 63, 75]. Das ist GJKS mit imaginaerer Flip-Rate.
    - SCHACHBRETT-KAUSAL-1: 1+1-Fermion als Feynman-Zickzack auf einer Kausalmenge, im Mittel wie im Kontinuum;
      Zitterbewegung bei 1,98 ~ 2m [P ERGEBNIS Abschn. 1].
  - Naechste Verwandte ausserdem:
    - QCA-TETRA-1: 2 Zustaende je Knoten, unitaerer Schrittautomat, auf Diamant kein isotropes Spektrum [P].
    - LICHT-FINN-NETZ-1 bzw. DIAMANT-FERMION-L: W-D-Operator (i/2) sigma . n_ij auf Diamant mit Dirac-Punkt bei Gamma,
      Knotenschleifen durch W, Kegel 2b/3 = 0,8165 [P].
  - **Was neu bliebe:** das Schachbrett bzw. der Kac-Erzeuger mit 4 Richtungszustaenden auf **Finns Diamantnetz**
    (A/B im Wechsel). Foster/Jacobson nutzen fcc bzw. bcc. Die Karte muss vorab gegen alle vier Ergebnisse gelesen
    werden. Liefert die Foster/Jacobson-Konstruktion den Diamantfall schon mit, entfaellt sie.
- **Umfang:** Schreibtisch plus Kleintest (Eigenwerte einer 8x8-Matrix ueber Richtungen) auf der Kleintest-Spur der .69.
  Vorab binden: Kegel isotrop ja/nein (Richtungsstreuung gegen die QCA-TETRA-1-Eichung 2,8e-3 bei \|k\| = 0,05),
  Masse = hbar lambda/c_eff^2 ja/nein.

---

## 11. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendliche Annahme | Geprueft? | Befund |
|---|---|---|---|
| G1 | "Delta x Delta k >= 1/2 gilt fuer jede Welle auf dem Netz" (Vorgabe) | **ja** | Auf dem Gitter nur fuer k << pi/l (V5) [M] |
| G3 | "Finns Netz = Diamant mit 4 Kanten" | **ja** | Finns Netz ist Pyrochlor (Tetraeder an den Ecken); Diamant = Tetraedermitten [P LICHT-FINN-NETZ-1]. Falls Finn mit "Kante" die Tetraederkanten an den Ecken meint, hat jeder Platz 6 Nachbarn. Der Vorfaktor D = l^2/(6 tau) bleibt (kubisch isotrop), Sektorzahl und Zickzack aendern sich [M]. Rueckfrage an Finn |
| G4 | "Das Projekt kennt die neue Literatur nicht" | **ja** | Der Scout hatte Ghose 2609.29248 ab 25.09. im Cache (arxiv-records.jsonl mehrerer Ticks), Einordnung 28.09.: `"topics":{}` [P classification-cache.json]. Gesehen, aber keinem Thema zugeordnet |
| G5 | Bell-Satz gilt fuer Finns Kantenwahl | nein | Gilt nur, wenn jeder Knoten nur lokal gespeicherte Information nutzt. Ist das Netz selbst das nichtlokale Medium (Drift aus dem globalen Zustand), greift die Bell-Schranke nicht, dann ist das aber Nelson- bzw. Bohm-artig [ES] |
| G7 | INSPIRE-Freitext deckt das 24-Monats-Fenster ab | nein | quant-ph ist bei INSPIRE unvollstaendig. "Kein SED-Wasserstoff-Treffer im Fenster" ist eine Aussage ueber diese Abdeckung |
| G8 | Mein Projekt-grep nach "Kac, GJKS, Telegraph" deckt das Thema Masse als Flip ab | **ja** | Nein. Unter "Schachbrett, Foster/Jacobson" stehen DUNKEL-FLIP-L (3+1-Schachbrett, Masse als Flip i eps m, nicht unitaer) und SCHACHBRETT-KAUSAL-1 (1+1 auf Kausalmenge, ZB bei 2m) [P]. Die Amplituden-Lesart (b) ist im Projekt also schon gerechnet bzw. gelesen; der Kartenvorschlag ist entsprechend eingeengt. Derselbe Vokabular-Fehler steht schon als Selbstanzeige 2 in DUNKEL-FLIP-L [P Z. 310] |

---

## 12. Offene Fragen

1. An Finn: Welche Kante, die Diamant-Bindung (4 je Knoten) oder die Tetraederkante (6 je Ecke)? Welche "Dimensionen":
   Raumrichtungen, eine verborgene Richtung oder die Pfad-Dimension (Lesart e)?
2. Woher kommt im Netz das **zweite hbar** (Quantisierung, Wallstrom)? Derakhshani 2015 (arXiv 1510.06391) schlaegt
   Zitterbewegung als Antwort vor [S Ghose Ref. 18, nicht gelesen]. Das passt zum Zitterbewegungs-Modell des Projekts
   [P five-why].
3. Hat Finns Netz lineare (n = 1) Dispersionskorrekturen? DIAMANT-FERMION-L nennt fuer den W-D-Operator "a1 =
   +-(b/sqrt3) abs(q^(n) x n): 110 -> +-sqrt2/4 = +-0,3536; 100 und 111 -> 0" [P DIAMANT-FERMION-L ARBEITSFELD.md
   Z. 31]. Ob das eine Lichtlaufzeit-Korrektur der Ordnung E/E_mesh ist, habe ich nicht
   geprueft. Falls ja, waere eine Planck-Masche mit Koeffizient 0,35 gegen LHAASO (< ~0,1) zu pruefen [H].
4. Jalalzadeh 2023: Wie wird hbar "berechnet", und ist das zirkulaer?
6. GHT 1979 und Fuerth 1933 im Original (beide [L?]).

---

## 13. Kalibrierung, Quellen, Selbstanzeigen

### 13.1 Kalibrierung

- **(a) Gemessen:**
  - 1S-2S 4,2e-15 (Parthey 2011);
  - LHAASO E_QG,1 > 10 E_Pl, E_QG,2 > 6e-8 E_Pl;
  - Bushev beta0 < 5,2e6;
  - Bell-Verletzung [L].
  - Keine dieser Messungen trennt Nelson von QM.
- **(b) Nuetzlich verdichtet:**
  - D = v^2/(2 lambda) und hbar lambda = m c^2 (Ghose, GJKS);
  - m = d hbar tau/l^2 bzw. m = p_flip m_Pl;
  - E_1 = -(alpha^2/2) hbar lambda_e;
  - Nelson-Grundzustand mit Drift alpha c;
  - Gitter-Unschaerfe (1/2)\|<cos kl>\|.
- **(c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):**
  - Meine Sicherheit fuer "nur als Amplitude" ist gestiegen, waehrend sich die Frage in vier Teile zerlegte: D, das i,
    Nichtlokalitaet, Quantisierung.
  - Dafuer gibt es keine neue Messung. Ob Lesart (a) "erklaert", haengt an der Definition von "erklaeren": Fuer
    Nelson-Anhaenger erklaert sie, bei eingesetztem hbar. Ghose sagt ausdruecklich, die Relationen waehlen nicht
    zwischen den Bahnbildern [S].

### 13.2 Quellenliste

Abgerufen (Kopien in quellen/, Abrufzeiten in ARBEITSFELD.md):

  the viewpoint of a generalized particle model. Proc. SPIE 8832, 88320H. https://doi.org/10.1117/12.2022650
- A2 Hossenfelder, S. (2013): Minimal Length Scale Scenarios for Quantum Gravity. Living Rev. Rel. 16.
  https://arxiv.org/abs/1203.6191
- A2 Bawaj, M. u. a. (2015): Probing deformed commutators with macroscopic harmonic oscillators.
  https://arxiv.org/abs/1411.6410
- A2 Bushev, P. A. u. a. (2019): Testing the generalized uncertainty principle with macroscopic mechanical oscillators
  and pendulums. Phys. Rev. D 100. https://arxiv.org/abs/1903.03346
- A2 Bosso, P. u. a. (2023): 30 years in: Quo vadis generalized uncertainty principle? Class. Quant. Grav. 40.
  https://arxiv.org/abs/2305.16193
- A2/A10 Das, S.; Vagenas, E. C. (2008): Universality of Quantum Gravity Corrections. Phys. Rev. Lett. 101.
  https://arxiv.org/abs/0810.5333 (Volltext, Gl. 1, 12, 13, 22, 34)
- A3 Derakhshani, M.; Bacciagaluppi, G. (2022): On Multi-Time Correlations in Stochastic Mechanics.
  https://arxiv.org/abs/2208.14189
- A3 Nieuwenhuizen, T. M.; Liska, M. T. P. (2015): Simulation of the hydrogen ground state in Stochastic
  Electrodynamics. https://arxiv.org/abs/1502.06856 ; dies. (2015): ...-2: Inclusion of relativistic corrections.
  Found. Phys. 45. https://arxiv.org/abs/1506.06787
- A3 Parthey, C. G. u. a. (2011): Improved Measurement of the Hydrogen 1S-2S Transition Frequency. Phys. Rev. Lett. 107.
  https://arxiv.org/abs/1107.3101
- A4 Al Ghifari, M. H. u. a. (2025): Bound on generalized uncertainty principle parameter from nuclear matter and slow
  rotating neutron stars. Gen. Rel. Grav. 57 (kein arXiv); Paliathanasis, A. (2026): Cosmological constraints on the
  GUP from redshift-space distortions. Phys. Dark Univ. 52. https://arxiv.org/abs/2604.01713 ; Valero, E. (2025): The
  generalized uncertainty principle. New bounds and trends. Class. Quant. Grav. 43. https://arxiv.org/abs/2505.06598
- A5 Nelson, E. (1966): Derivation of the Schroedinger equation from Newtonian mechanics. Phys. Rev. 150, 1079.
  https://doi.org/10.1103/PhysRev.150.1079
- A5 Gaveau, B.; Jacobson, T.; Kac, M.; Schulman, L. S. (1984): Relativistic extension of the analogy between quantum
  mechanics and Brownian motion. Phys. Rev. Lett. 53, 419. https://doi.org/10.1103/PhysRevLett.53.419
- A6 Ghose, P. (2026): Nelson's Stochastic Mechanics: Measurement, Nonlocality, and the Classical Limit.
  https://arxiv.org/abs/2604.03214 ; Yordanov, V. (2024): Revisiting the Bohr model of the atom through Brownian motion
  of the electron. Phys. Scr. 101. https://arxiv.org/abs/2412.19918 ; Lynd, N. A. (2025): Computational Stochastic
  Mechanics of a Simple Bound State. https://arxiv.org/abs/2504.08669
- A7 Jalalzadeh, S. (2023): Intrinsic quantum dynamics of particles in brane gravity. Annals Phys. 452.
  https://arxiv.org/abs/2303.11104 ; Lake, M. J.; Liang, S.-D.; Watcharapasorn, A. (2023): Dimensionally-dependent
  uncertainty relations. Front. Astron. Space Sci. 10. https://arxiv.org/abs/2303.16620 ; Magpantay, J. A. (2011):
  Geodesics, Mass and the Uncertainty Principle in a Warped de Sitter Space-time. https://arxiv.org/abs/1108.0750 ; Mu,
  B.; Wu, H.; Yang, H. (2009/2011): The Generalized Uncertainty Principle on the Presence of Extra Dimensions. Chin.
  Phys. Lett. 28. https://arxiv.org/abs/0909.3635
- A8 LHAASO Collaboration (2024): Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB
  221009A. Phys. Rev. Lett. 133, 071501. https://arxiv.org/abs/2402.06009
- A9 Ghose, P. (2026): The Uncertainty Principle, Uncertainty Relations, and Underlying Trajectories: Feynman, Nelson,
  Bohm, and Persistent Kac-Dirac Dynamics. https://arxiv.org/abs/2609.29248 (Volltext v1, Gl. 4 bis 6, 35, 49 bis 59,
  66 bis 77; Abschn. 4.1, 5, 6.2, 7, 8)

Nur ueber Ghoses Literaturverzeichnis bekannt (nicht abgerufen): Wallstrom, T. C. (1994), Phys. Rev. A 49, 1613;
Abbott, L. F.; Wise, M. B. (1981), Am. J. Phys. 49, 37; Derakhshani, M. (2015), arXiv 1510.06391; Schmelzer, I.
(2011), arXiv 1101.5774; Kac, M. (1974), Rocky Mountain J. Math. 4, 497; Goldstein, S. (1951), Q. J. Mech. Appl. Math.
4, 129.

Nicht abgerufen, [L?]: Fuerth, R. (1933), Z. Phys. 81, 143; Grabert, H.; Haenggi, P.; Talkner, P. (1979), Phys. Rev. A
19, 2440; Matveev, A. u. a. (2013), Phys. Rev. Lett. 110, 230801; Cole, D. C.; Zou, Y. (2003), Phys. Lett. A 317, 14
(im N/L-Abstract genannt); Blanchard, Ph. u. a. (1986) (im D/B-Abstract genannt).

Projekt [P]: gesamtformel-20260921/HILBERT.md Abschn. 2; dashboard-overview-20260909/.../five-why/report-source.md
Z. 80 bis 92; RUNDE-37/qca-tetra-1/ERGEBNIS.md; RUNDE-37/doppelspalt-l/DOSSIER.md Z. 116, 170;
RUNDE-37/dunkel-flip-l/DOSSIER.md Z. 30, 48, 63, 75; RUNDE-37/schachbrett-kausal-1/ERGEBNIS.md Abschn. 1; RUNDE-35.md
Z. 277; RUNDE-42.md Z. 29; RUNDE-45.md Z. 232; pdf-nachrechnung.md Z. 10; fmhc-physics-fulltext.md Z. 113, 304 bis 311;
methodik-review/review-20260928/GEGENLESEN-KARTEN-20260928.md; research-scout-claude-20260913/classification-cache.json.

### 13.3 Selbstanzeigen

1. **Fuenf technische Fehlversuche:**
   - export.arxiv.org per http gab 301 (curl ohne -L, 0 Byte, zweimal).
   - Dreimal kam per https "Rate exceeded" (HTTP 429).
   - Kein Inhalt erhalten, nicht als Abruf gezaehlt. Kanalwechsel auf INSPIRE (A2 bis A8) und arxiv.org (A9, A10).
2. **Werkzeug:** Alle Abrufe liefen per curl statt WebFetch, damit die Kopien in quellen/ liegen. pdftotext lokal zur
   Textwandlung, keine Rechnung.
3. **A7-Abfrage verrauscht:** Der Begriff "Heisenberg" zog viele Fremdtreffer. Wesson und Dolce (5D bzw. kompakte
   Zeit) fehlen; das kann an der Abfrage liegen.
4. **Alle [M]-Zahlen sind Kopfrechnungen**, maschinell nicht nachgeprueft:
   - 3 m_Pl, 7,76e20/s, 2,39e22, 1,6e-11 s, 0,9e-48 beta0, sqrt(2/3);
   - Nelson-Drift alpha c, Gitter-Robertson.
5. **Abstract-Fassungen:** Ghoses Abstract bei INSPIRE und im PDF v1 weichen leicht voneinander ab. Zitiert ist aus dem
   PDF, wo Gleichungen genannt sind.
7. **Lesarten-Wahl:** Die Lesart (e) Pfad-Dimension ist meine Zugabe, nicht Teil der Karte; als [ES/H] markiert.
8. **Projekt-grep zuerst zu eng:** Ich habe nach "Kac, GJKS, Telegraph, Wick" gesucht, nicht nach "Schachbrett,
   Foster/Jacobson". DUNKEL-FLIP-L und SCHACHBRETT-KAUSAL-1 fand erst der Gegensweep (G8). Der Kartenvorschlag ist
   danach eingeengt worden, nicht verworfen.
9. **Zeit:** Die Zeitbox von 65 min ist eingehalten, das Textende steht in ARBEITSFELD.md.

---

## 14. Einfach gesagt

- Wenn ein Teilchen auf Finns Netz bei jedem Takt zufaellig eine Kante waehlt, verschmiert es wie ein Tropfen Tinte im
  Wasser.
- Das sieht der Unschaerfe aehnlich, aber es gibt keine Interferenzstreifen. Ausserdem muss man die Groesse der
  Verschmierung (hbar/2m) von Hand einsetzen.
- Erst wenn die Kantenwahl wie eine Welle mit Phase laeuft, kommt echte Quantenmechanik heraus, und dann ist die
  Unschaerfe einfach eine Eigenschaft jeder Welle.
- Fuer das Wasserstoffatom (-13,6 eV) braucht man ausserdem die Elektronenmasse und die Staerke der elektrischen Kraft,
  und beides liefert das Netz nicht von selbst.
- Ein Physiker hat genau diese Idee vor elf Tagen veroeffentlicht. Die Frage ist also aktuell, aber offen.
