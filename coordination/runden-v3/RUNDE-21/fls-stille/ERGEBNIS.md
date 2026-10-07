# ERGEBNIS fls-stille (Runde 21, Literatur-Agent)

- Geschrieben ab 2026-10-02 18:55:26 CEST (date). Zeitbox ab 18:31:08 CEST. Rohprotokoll mit Vorhersage vor jedem Abruf:
  ARBEITSFELD.md (gleicher Ordner).
- Marken: [S] selbst gelesen (Volltext bzw. genannte Seiten); [S/A] Volltext nur ueber das Abrufmodell von WebFetch
  gelesen (vor einem Zitat im Papier selbst nachlesen); [L?] nur Abstract, Titel oder Zitat; [H] eigene Schlussfolgerung
  (entspricht [ES]).
- Erwartungen F1 bis F4 stammen von der Leitung und sind unveraendert; hier nur gewertet.

## 1. Ergebnis (5 Punkte)

1. **Lineare Stoerungen von FLS-Q-Baellen gibt es erst seit Dezember 2024, und nur als Streuproblem.** Azatov/Ho/Khalil
   (arXiv:2412.13885, Abschn. 3) schreiben: "for the first time we have analyzed the perturbations of the FLS Q-ball
   solution" (S. 20) [S]. Zhang/Li/Xie/Zhou (arXiv:2503.04657) rechnen Superradianz an FLS-Solitonen [S/A]. Beide
   behandeln drei gekoppelte Kanaele (eta_+, eta_-, chi). Keine der beiden Arbeiten berechnet Normal- oder Quasinormalmoden
   des Balls, stille Stellen oder einen Radiusscan. F1 ist eingetroffen.
2. **Stille Stellen sind fuer FLS-Q-Baelle und den Friedberg-Lee-Beutel nach Recherchestand nicht beschrieben.** Das gilt
   fuer gebundene Zustaende im Kontinuum, eingebettete und strahlungsfreie Moden. Belege: arXiv "Q-ball" x "bound states
   in the continuum" ergibt ueber alle Jahre 0 Treffer, das 24-Monats-Fenster eingeschlossen. Die Gegenproben liefern nur
   Photonik und BEC: OpenAlex ab 2024-10-01 sowie arXiv "bound states in the continuum" x
   soliton/kink/oscillon/boson star/nontopological ueber alle Jahre. F2 und F4 sind eingetroffen; F4 ist duenn belegt.
3. **Eine Leiter besonderer FLS-Groessen ist nicht beschrieben (F3 trifft im Wortlaut ein), ihr Bauprinzip aber schon.**
   Zhang/Zhou/Zhu (arXiv:2510.27064) zeigen fuer duennwandige Einfeld-Sextik-Q-Baelle: Die Streuverstaerkung ist
   sinusfoermig in sigma_+- r_*, und die Maxima wiederholen sich periodisch im Wandradius (Gl. 108-118, Abb. 3) [S]. Im
   FLS-Modell sind es numerisch "more peaks" fuer groessere Solitonen (2503.04657, Abb. 8) [S/A]. Bei reellen
   phi^6-Oszillonen gibt es eine Folge von Konfigurationen mit stark gedaempfter Abstrahlung: "multiple dips" (arXiv:2004.01202,
   Abschn. 7.5). Der Mechanismus ist die Nullstelle einer Fourier-Transformierten der Quelle (Gl. 7.4) [S].
4. **Frage 4: Das Leiterpapier zitiert die erste FLS-Stoerungsanalyse schon, ohne es zu sagen.** In LITERATURE.tex kommt
   FLS nicht vor. Azatov2024 ist laut bibliography.tex genau arXiv:2412.13885v1, wird aber nur als Arbeit zur
   Einfeld-Sextik beschrieben (LITERATURE.tex Z. 24-31) [S]. Es fehlen die Superradianz-Reihe (2212.03269, 2402.03193,
   2503.04657, 2510.27064) und die Oszillon-Dips (2004.01202).
5. **Bedeutung gemaess Karte:** F2 und F3 treffen ein. Damit sind die stillen Huellenleitern nach Recherchestand in der
   FLS-Literatur nicht beschrieben und ein Kandidat fuer eine neue Aussage; ob sie ins Papier soll, entscheidet Finn.
   Zuschnitt [H]: Neu waere die exakte, per Windungszahl belegte Stille linearer Normalmoden eines FLS-artigen Beutel-Q-Balls
   bei l = 0, 1, 2 und deren Lage auf Leitern. Nicht neu sind drei Bausteine:
   - das lineare FLS-Dreikanalproblem,
   - die Halbwellen-Periodizitaet von Streumerkmalen im Wandradius,
   - Folgen unterdrueckter Abstrahlung bei Oszillonen.

   Diese drei sind zu zitieren und abzugrenzen.

### 1b. Erwartungsverstoesse (das Wichtigste zuerst)

1. **Die Antwort lag im eigenen Literaturverzeichnis (Regel 4).** Erwartet hatte ich, dass Azatov 2024/2025 nur Einfeld-Q-Baelle
   behandelt (Block G3). Tatsaechlich ist Abschn. 3 die erste lineare FLS-Analyse: FLS-Potential Gl. (47), Stoerungen
   Gl. (50), sechs Kanalregime in Abschn. 3.1.1 [S]. Die Arbeit steht bereits als Azatov2024 im Papier.
2. **Die Halbwellen-Periodizitaet ist Q-Ball-Literatur.** Erwartet hatte ich eine Resonanzbedingung k_in R ~ n pi oder gar
   keine. Gefunden habe ich eine Sinusabhaengigkeit von Summe und Differenz der beiden Innenwellenzahlen,
   sigma_+- = sqrt(-rho_1) +- sqrt(-rho_2) (2510.27064 Gl. 101-102, 109). Die Deutung als Interferenz ist meine [H]; die
   Autoren nennen es nicht so. Ihre Periode im Wandradius ist pi/sigma_+- (Gl. 114-118).
   Bei grossem omega gilt "sigma_+ ~ 2 omega and sigma_- ~ 2 omega_Q" (S. 13) [S]. Diese Periodizitaet zeigt sich dort in
   den Maxima der Verstaerkung, nicht in Nullstellen.
3. **Folgen fast stiller Groessen sind bei Oszillonen bekannt.** Die Abstrahlrate der 3-omega-Harmonischen verschwindet,
   wenn die Fourier-Transformierte der Quelle bei kappa_3 null wird: "if S~(kappa_3) vanishes for some omega, then
   Gamma_(3) also vanishes" (2004.01202, S. 13). Ein Beispiel ist omega_* ~ 0.82 m (Abb. 4). Fuer phi^6 gibt es "multiple dips"
   (S. 18). Die naechste Harmonische strahlt aber weiter (Gamma_5 ungleich 0) [S]. Das Feld ist reell, das Verhalten
   nichtlinear, und es geht nicht um eine Normalmode eines Q-Balls.
4. ~~Bei Oszillonen sei der effektive Massenterm statt einer Fourier-Nullstelle die Ursache~~. Um 18:48 gestrichen: Die effektive
   Masse steckt in der Quelle S_j (Gl. 4.5). Der Mechanismus bleibt die Fourier-Nullstelle.

## 2. Antworten auf die Fragen

### Frage 1: Arbeiten zu linearen Stoerungen, Moden, Anregungen oder Abstrahlung von FLS- bzw. Zweikomponenten-Q-Baellen

- **Azatov, Ho, Khalil 2024** (arXiv:2412.13885v1; PRD 111, 096010 (2025)) [S, S. 1-2, 13-14, 18-20]:
  - Abschn. 3 "Two-field Q-balls": Potential V = g_chiPhi chi^2|Phi|^2 + g_chi(chi^2 - v^2)^2 + m_Phi^2|Phi|^2 + g_Phi|Phi|^4
    (Gl. 47), Profile mit chi -> 0 im Inneren (Abb. 7: g_chiPhi = 4, g_chi = 1, g_Phi = 0.04, v = 1, m_Phi = 0).
  - Lineare Stoerungen in Gl. (50), Streumatrix im Anhang A (Gl. 66-72).
  - Energie- und Ladungsverstaerkung Z_E, Z_Q fallen "very close to the threshold" zweier offener geladener Kanaele auf
    null (S. 18). Das ist ein Schwelleneffekt.
  - Abb. 10: Das Vorzeichen des Energieaustauschs wechselt mit omega ("the sign of Z is not fixed").
  - Abschn. 3.1.1 und Abb. 11: sechs Regime offener und geschlossener Kanaele. "bounded" heisst dort evaneszenter Kanal,
    nicht Eigenmode des Balls.
  - Keine inneren Moden, keine Variation des Radius bei fester Mode.
- **Zhang, Li, Xie, Zhou 2025** (arXiv:2503.04657; PRD 111, 103027) [S/A, HTML]:
  - FLS mit e^2 chi^2|Phi|^2 + g^2/8 (chi^2 - chi_vac^2)^2 (Gl. 1-2), Stoerungen eta_+-, rho_+- (Gl. 32-35), je drei ein- und
    auslaufende Kanaele.
  - "Larger FLS solitons result in more peaks" (Abb. 8). Die Deutung ist auf eine Folgearbeit vertagt (Abschn. IV.1.2).
  - Die Folgearbeit 2510.27064 behandelt aber die Einfeld-Sextik und nicht FLS.
- **Su, Xie, Zhou 2026** (arXiv:2605.25243) [L?]: Hartree-Dynamik von FLS-Q-Baellen mit Ladungsaustausch zwischen
  Mittelfeld und Fluktuationsmoden; ein Fenster, in dem klassisch stabile Baelle quantenmechanisch instabil werden.
- **Murai, Ogawa, Takahashi 2026** (arXiv:2604.04494; PRD 114, 036019) [L?]: reelle FLS-Variante,
  Mehrfeld-Oszillonen; das Abstract nennt keine Abstrahlung.
- **Jaramillo, Zhou 2024** (arXiv:2411.08985) [L?]: Einstein-FLS-Dipole und -Ketten; Stabilitaet per numerischer
  Relativitaet.
- **Loiko, Perapechka, Shnir 2018** (arXiv:1805.11929; PRD 98, 045018) [L?]: haarige FLS-Q-Baelle sind "classically
  stable for all range of values of angular frequency"; die Methode nennt das Abstract nicht.
- **Panin, Smolyakov 2019** (EPJC 79, DOI 10.1140/epjc/s10052-019-6638-2; Wick-Cutkosky, zwei Felder) [L?]: klassische
  Stabilitaet und nichtlineare Entwicklung instabiler Q-Baelle.
- **Ohne Moden** [L?]:
  - Levin/Rubakov 2011 (arXiv:1010.0030)
  - Kim/Nugaev 2023 (arXiv:2309.09661)
  - Kim/Nugaev/Shnir 2024 (arXiv:2405.09262; "Kim" der Karte ist Eduard Kim)
  - Heeck/Sokhashvili 2023 (arXiv:2303.09566)
  - Loiko/Shnir 2019 (arXiv:1906.01943)
- **Nicht pruefbar** (nur Metadaten): Friedberg/Lee/Sirlin 1976 (PRD 13, 2739) und Lee/Pang 1992 (Phys. Rep. 221, 251).
- **Shnir:** Seine Q-Ball-Modenarbeiten (Ciurla et al. 2024; Evslin et al. 2026) behandeln Einfeld-Modelle in 1+1
  Dimensionen und stehen schon im Papier. Seine FLS-Arbeiten mit Loiko, Kunz und Perapechka behandeln Profile und
  Stabilitaet [L?].
- **Fazit [H]:** Normal- oder Quasinormalmoden von FLS-Q-Baellen sind nach Recherchestand nicht berechnet. Die lineare
  Literatur zu FLS ist Streuung (2024/2025) und Stabilitaet.

### Frage 2: Gebundene Zustaende im Kontinuum, eingebettete oder strahlungsfreie Moden, "stille" Groessen?

- **In FLS- bzw. Zweikomponenten-Q-Baellen:** nach Recherchestand keine Arbeit. Die abgefragten Kombinationen stehen in
  Abschnitt 5; die beiden Volltexte 2412.13885 und 2503.04657 enthalten nichts davon [S bzw. S/A].
- **Naechstliegende Effekte:**
  - (a) Z_E, Z_Q -> 0 an der Kanalschwelle (2412.13885 S. 18). Das ist eine Schwelle, keine Stille einer Mode [S].
  - (b) Reelle Oszillonen haben Konfigurationen, deren fuehrende Abstrahlung verschwindet (2004.01202 Gl. 7.4, Abb. 4,
    Abschn. 7.5) [S]. Vorlaeufer: Mukaida/Takimoto/Yamada 2017 (arXiv:1612.07750) [L?] und Ibe et al. 2019
    (arXiv:1901.06130) [L?, nur Zitat].
  - (c) Einfeld-Q-Baelle: schmale Quasinormalmoden mit nicht verschwindendem Schwanz (Ciurla2024) und
    Feshbach-Quasinormalmoden (Evslin2026). Beide sind im Papier schon abgegrenzt.

### Frage 3: Leiter besonderer Ballgroessen in festem Radiusabstand oder Halbwellen-Bedingung der Innenwelle?

- **Fuer FLS:** keine Leiter beschrieben. Es gibt nur "more peaks" mit wachsender Groesse (2503.04657 Abb. 8) [S/A].
- **Halbwellenstruktur, Einfeld-Sextik** (2510.27064) [S]:
  - Im Duennwandfall ist die auslaufende Teilchenzahl eine rationale Funktion von cos(sigma_- r_*) und sin(sigma_+ r_*)
    (Gl. 108).
  - "thin-wall location r_* plays the central role in controlling the number of peaks" (S. 11).
  - Die Karten ueber (omega, r_*) in Abb. 3 zeigen Baender von Maxima, die sich in r_* periodisch wiederholen.
  - Grosses omega (Gl. 114-118): Das Grundglied geht mit sin^2(2 r_* omega_Q + phi_-). Seine Periode im Radius ist
    pi/sigma_-, also eine halbe Wellenlaenge der Differenzwelle.
  - Abstract: "peak spacing is simply the inverse of the Q-ball size".
- **Oszillonen:** Die "multiple dips" bei phi^6 (2004.01202 Abschn. 7.5) bilden eine Folge besonderer Konfigurationen.
  Einen festen Abstand nennt die Arbeit nicht [S].
  - [H, nicht an der Quelle geprueft] Fuer flache Quellen liegen die Fourier-Nullstellen im Abstand von etwa pi/kappa.
    Massgeblich waere dann die abgestrahlte Welle, nicht die Innenwelle.

### Frage 4: Was sagt LITERATURE.tex schon?

- [S, LITERATURE.tex Z. 1-89; bibliography.tex, 15 Eintraege]:
  - FLS, Friedberg, Lee, Sirlin, "bag" und Zweifeldmodelle kommen nicht vor.
  - Q-Ball-Stoerungen: Kovtun2018 (Kopplung omega +- rho), Azatov2024 (3D-Partialwellen "in the same sextic model
    family"), Ciurla2024 (gebundene, halb-propagierende und Quasinormalmoden; "small but nonzero radiation tail").
    Dazu Evslin2026 (2604.07713, Feshbach-Quasinormalmoden) und Battye/Sutcliffe2000.
  - Mechanismen der Stille: Friedrich/Wintgen1985, Yu/Lu2025 (rigoroser Dreikanal-BIC) und Malomed2005 (Haeufung
    eingebetteter Solitonen, n^(-6/5)).
  - Das Papier beansprucht ausdruecklich keine Prioritaet und keine unendliche Leiter (Z. 84-87).
- **Luecken [H]:**
  - Azatov2024 Abschn. 3 (FLS) wird nicht als FLS-Arbeit genannt.
  - Es fehlen Zhang/Li/Xie/Zhou 2025 (FLS-Streuung), Zhang/Zhou/Zhu 2025 (Halbwellenstruktur, Einfeld-Sextik, also die
    Familie des Leiterpapiers selbst) und Saffin/Xie/Zhou 2022/2023 (PRL 131, 111601).
  - Es fehlt Zhang/Amin/Copeland/Saffin/Lozanov 2020 (Folge von Abstrahlungs-Dips bei phi^6-Oszillonen, gleiche
    Potentialform wie das Einfeldmodell).

### Frage 5: Hadronenbruecke (fermionischer Friedberg-Lee-Beutel)

- **Gefunden** sind Arbeiten zu angeregten Zustaenden, keine zu strahlungsfreien Beutelschwingungen:
  - Saly/Sundaresan 1984 (PRD 29, 525) [L?]: radial angeregte Zustaende gerader und ungerader Paritaet im FL-Solitonbeutel,
    die den Parameterbereich "restrict severely". Die Arbeit erweitert Goldflam/Wilets 1982 (PRD 25, 1951; nur ueber dieses
    Zitat bekannt).
  - Iwasaki/Kondo 1987 (PLB 199, 437) [nur Titel und Schlagworte]: Oberflaechenbewegung des Solitonbeutels,
    semiklassische Quantisierung, P11 (Roper) und P33.
  - Haider 1993 (Nuovo Cim. A 106, 335) [nur Titel und Schlagworte]: radial angeregte Nukleonzustaende im FL-Modell.
  - Kowata/Arima 2001 (nucl-th/0101019; PTP 105, 449) [L?]: Der erste angeregte Zustand positiver Paritaet stammt aus der
    "0s-excitation of the scalar meson".
  - Ke-Pan Xie 2024 (arXiv:2405.01227; JHEP 09(2024)077) [L?]: fermionische Solitonprofile ohne Schwingungen.
- **Naechster Verwandter ausserhalb von FL:** "Phase Shifts of the Skyrmion Breathing Mode" (PRL 53, 889, 1984) [nur Titel],
  eine Resonanz mit Breite.
- **[H]:** Eine hadronische stille Stelle waere eine Beutelmode oberhalb der Mesonschwelle mit Breite null. Nach
  Recherchestand ist so eine Mode nicht beschrieben. Die Belege fuer F4 sind duenn, weil zum Altbestand Abstracts fehlen.

## 3. Erwartungen F1 bis F4 (Leitung) und Ausgang

| Nr | Erwartung (Leitung, vorab) | Wahrsch. | Ausgang | Beleg |
|---|---|---|---|---|
| F1 | Mindestens eine Arbeit zu linearen Moden oder Abstrahlung von FLS- oder Zweikomponenten-Q-Baellen | 80 % | eingetroffen | 2412.13885 Abschn. 3 (Gl. 47, 50; S. 18-20) [S]; 2503.04657 [S/A]; ergaenzend 2605.25243 und Panin/Smolyakov 2019 [L?]. Einschraenkung: nur Streuung bzw. Stabilitaet, keine Normal- oder Quasinormalmoden des Balls |
| F2 | Keine berichtet strahlungsfreie oder eingebettete Moden (BIC) in FLS-Q-Baellen | 75 % | eingetroffen (nach Recherchestand) | arXiv Q-ball x BIC: 0 (alle Jahre); OpenAlex ab 2024-10-01: nur Photonik; arXiv BIC x soliton/kink/oscillon/boson star: 20 Treffer ohne Q-Ball; Volltexte 2412.13885 und 2503.04657 ohne BIC |
| F3 | Keine berichtet eine Leiter besonderer Groessen in festem Radiusabstand | 85 % | eingetroffen im Wortlaut, eingeschraenkt | Fuer FLS keine Leiter. Bauprinzip vorhanden: Halbwellen-Periodizitaet der Streumaxima im Wandradius (2510.27064 Gl. 108-118, Abb. 3) [S]; Folge von Abstrahlungs-Dips bei phi^6-Oszillonen (2004.01202 Abschn. 7.5) [S] |
| F4 | Zum FL-Hadronenbeutel keine Arbeit zu strahlungsfreien Beutelschwingungen | 70 % | eingetroffen (duenn belegt) | Saly/Sundaresan 1984 und Kowata/Arima 2001 [L?] ohne Abstrahlung; Iwasaki/Kondo 1987 und Haider 1993 nur Titel; Lee/Pang 1992 und Wilets 1989 nicht pruefbar |

### 3b. Regime und Moderatoren (Regel 1)

- **Vier Regime [H, gestuetzt auf die genannten Stellen].** Die Literatur zu "Q-Ball-Stoerungen" ist nicht
  widerspruechlich, sie misst verschiedene Groessen:
  - (R1) Streuung bei fester reeller Frequenz und offenen Kanaelen. Gemessen werden Verstaerkung und Maxima: 2412.13885,
    2503.04657, 2510.27064, 2212.03269.
  - (R2) Gebundene Moden unterhalb der Schwelle: Kovtun2018, Chen/Andersson/Li 2026 (JHEP 02(2026)078) [L?].
  - (R3) Quasinormal- und halb-propagierende Moden mit kleiner Breite ungleich null: Ciurla2024, Evslin2026.
  - (R4) Nichtlineare Oszillon-Abstrahlung mit Dips: 2004.01202, 1612.07750.
- **Moderatoren:**
  - Kanaloffenheit: sechs Regime in 2412.13885 Abschn. 3.1.1.
  - Wanddicke: 2510.27064 rechnet nur im Duennwandfall, n = 1.
  - Dimension: 1+1 gegenueber 3+1.
  - linear gegenueber nichtlinear.
  - Ein Feld gegenueber Beutel aus zwei Feldern.
- **Einordnung der stillen Stellen:** Sie liegen an der Schnittstelle von R1 und R3, als Normalmode bei offenem Kanal mit
  Breite genau null. Keine der Arbeiten hat diese Schnittstelle bisher abgetastet.
- **Regel 6 (Kopplung vor Bauteil) [H].** In der gefundenen Literatur gibt es drei Wege zu verschwindender Abstrahlung:
  - (i) Nullstelle eines Ueberlapps bzw. einer Fourier-Transformierten der Quelle (2004.01202 Gl. 7.4),
  - (ii) Interferenz zweier Resonanzen (Friedrich-Wintgen, im Papier zitiert),
  - (iii) Kanalschliessung an der Schwelle (2412.13885 S. 18).

  Gemeinsame Groesse ist vermutlich die Phase der Innenwelle an der Wand relativ zum offenen Kanal. Daraus folgt eine
  Halbwellen-Periodizitaet unabhaengig davon, ob das Modell FLS oder Einfeld ist. Dazu passt, dass das Einfeldmodell
  ebenfalls eine Leiter hat.

### 3c. Unterscheidungspunkte (Regel 2) [H]

- **Exakte BIC (stille Stelle) gegen ein Maximum oder Minimum der Streuverstaerkung (2510.27064).**
  - Beide zeigen dieselbe Halbwellen-Periodizitaet.
  - Unterscheidbar an der Breite der nahen Resonanz als Funktion von R: Bei einer BIC geht sie am stillen Punkt auf null
    (Fano-Kollaps), bei einem reinen Interferenz-Extremum nicht.
  - Diese Region ist im Projekt zugaenglich, in der Literatur nicht vermessen.
- **Ueberlapp- bzw. Fourier-Null (eine Resonanz) gegen Friedrich-Wintgen (zwei Resonanzen).**
  - Friedrich-Wintgen verlangt am stillen Punkt eine Annaeherung zweier Moden (vermiedene Kreuzung der Realteile), die
    Ueberlapp-Null nicht.
  - Unterscheidbar am Abstand zur naechsten Mode am stillen Punkt.
  - Wenn dort keine zweite Mode nahe kommt, sind die beiden Erklaerungen nur ueber diesen Abstand unterscheidbar.
- **Leiterperiode: drei Kandidaten.** In Frage kommen pi/k_in (eine Kanalwelle innen), pi/sigma_+- (Summen- oder
  Differenzwelle, 2510.27064) und pi/kappa (abgestrahlte Welle, Fourier-Nullstellen flacher Quellen).
  - Die drei laufen bei grossem omega auseinander, denn dort gilt sigma_+ ~ 2 omega und sigma_- ~ 2 omega_Q.
  - Dasselbe gilt bei Variation von omega_Q.
  - Wo sie zusammenfallen, sind sie empirisch nicht unterscheidbar.
- **Hadronen:** Eine stille Beutelschwingung ist nur oberhalb der Mesonschwelle von einer gewoehnlichen Resonanz
  unterscheidbar. Dazu gibt es keine Literatur.

### 3d. Gegensweep (Regel 4): Was war zu selbstverstaendlich?

1. **Dass "still" in der Literatur "BIC" oder "embedded" heisst.** Geprueft unter den Namen Fano, reflexionsfrei,
   Ramsauer, radiationless und non-radiating, dazu Oszillon-Zerfallsraten (Bloecke K bis L). Ergebnis: Unter dem Namen
   "dips" oder "exceptionally stable configurations" steht in der Oszillon-Literatur ein naher Verwandter
   (Erwartungsverstoss 3).
2. **Dass Schreibvarianten erfasst sind.** Geprueft mit all:Friedberg AND all:Sirlin (21 Treffer). Neu waren nur zwei
   Profilarbeiten. Die wichtigste FLS-Stoerungsarbeit (2412.13885) nennt "Friedberg-Lee-Sirlin" im Abstract nicht
   ("FLS Q-balls") und waere ueber arXiv-Schlagworte allein durchgefallen. Gefunden wurde sie ueber die OpenAlex-Zitation
   von FLS 1976.
3. **Dass die 24-Monats-Front ueber "Q-ball" abgedeckt ist.** Geprueft mit OpenAlex ab 2024-10-01 und mit arXiv BIC x
   soliton/kink/oscillon/boson star/nontopological. Kein Feldtheorie-Treffer.
4. **Dass M2 dem FLS-Modell der Literatur gleicht.** Nicht geprueft. M2 hat zusaetzlich eine psi-Masse und die
   Selbstwechselwirkung -S^2 + S^3/2. Die Literatur rechnet reines FLS (m_Phi = 0 in 2412.13885 Abb. 7).
5. **Dass der Hadronen-Altbestand ueber OpenAlex lesbar ist.** Nein: Abstracts fehlen (Iwasaki/Kondo, Haider, Lee/Pang).
6. **Dass Radu/Volkov 2008 (arXiv:0804.1357) mit "non-radiating" nur omega < m meint.** Nicht geprueft.

### 3e. Kalibrierung

- **(a) Gemessen bzw. gelesen:**
  - 2412.13885 S. 1-2, 13-14, 18-20; 2510.27064 S. 11-14; 2004.01202 S. 1-4, 12-19, 23-24 (selbst gelesen).
  - LITERATURE.tex und bibliography.tex (lokal).
  - Sonst Abstracts und Titel.
- **(b) Nuetzlich verdichtet [H]:**
  - "drei Bausteine sind Literatur, die exakte Stille nicht",
  - die Regimekarte R1 bis R4,
  - die gemeinsame Phasengroesse als Ursache der Halbwellen-Periodizitaet.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:** Die Neuheit der exakten Stille.
  - **Warnzeichen:** Meine Sicherheit stieg, waehrend die Frage schmaler wurde. Aus "Leiter stiller Stellen" wurde
    "exakte, per Windungszahl belegte Stille linearer Normalmoden eines FLS-Beutel-Q-Balls". Je schmaler der Begriff,
    desto leichter faellt eine Fehlanzeige.
  - Die Fehlanzeigen beruhen auf Abstract-Suchen, auf der OpenAlex-Rangfolge und auf einem Altbestand ohne Abstracts.
  - Das Urteil lautet daher "nach Recherchestand nicht beschrieben", nicht "neu".

## 4. Fundliste

| Arbeit | Jahr | arXiv / DOI | Moden, Abstrahlung, stille Stellen | Marke |
|---|---|---|---|---|
| Azatov, Ho, Khalil: Q-ball perturbations with more details: linear analysis vs lattice | 2024/2025 | 2412.13885; 10.1103/PhysRevD.111.096010 | Abschn. 3: FLS-Stoerungen erstmals, drei Kanaele, Z_E/Z_Q, Null an der Kanalschwelle (S. 18), sechs Kanalregime (3.1.1); keine inneren Moden, keine BIC, kein Radiusscan. Im Papier als Azatov2024, aber nur fuer die Sextik genannt | [S] |
| Zhang, Li, Xie, Zhou: Superradiance of FLS solitons | 2025 | 2503.04657; 10.1103/PhysRevD.111.103027 | FLS-Streuung, Verstaerkungsspitzen, "more peaks" fuer groessere Solitonen (Abb. 8), Deutung vertagt; keine BIC | [S/A] |
| Zhang, Zhou, Zhu: Q-ball superradiance: Analytical approach | 2025 | 2510.27064 | Einfeld-Sextik (Gl. 3), Stufenhintergrund; Verstaerkung sinusfoermig in sigma_+- r_* (Gl. 108-118); Abb. 3 periodische Baender in r_*; Spitzenabstand ~ 1/Groesse; keine Nullstellen | [S] |
| Saffin, Xie, Zhou: Q-ball superradiance | 2022/2023 | 2212.03269; PRL 131, 111601 | Superradianzkriterien, gekoppelte Kanaele, Einfeld | [L?] |
| Zhang, Chang, Saffin, Xie, Zhou: Spinning Q-ball superradiance in 3+1D | 2024 | 2402.03193; PRD 110, 043504 | Partialwellen, Verstaerkung rotierender Q-Baelle | [L?] |
| Cardoso, Vicente, Zhong: On energy extraction from Q-balls | 2023 | 2307.13734 | Energieentnahme als blauverschiebungsartiger Streueffekt | [L?] |
| Su, Xie, Zhou: Quantum-corrected Q-balls in the FLS model | 2026 | 2605.25243 | Hartree, Fluktuationsmoden, Instabilitaetsfenster; keine Abstrahlungsnullstellen | [L?] |
| Murai, Ogawa, Takahashi: Multi-field oscillons/I-balls in the FLS model | 2026 | 2604.04494; PRD 114, 036019 | reelle FLS-Variante, Mehrfeld-Oszillonen; Abstract ohne Abstrahlung | [L?] |
| Jaramillo, Zhou: Dipoles and chains of solitons in the FLS model | 2024 | 2411.08985 | Einstein-FLS-Multisolitonen, Stabilitaet per numerischer Relativitaet | [L?] |
| Loiko, Perapechka, Shnir: Q-balls without a potential | 2018 | 1805.11929; PRD 98, 045018 | haarige FLS-Q-Baelle klassisch stabil; Methode nicht im Abstract | [L?] |
| Loiko, Shnir: Q-balls in the U(1) gauged FLS model | 2019 | 1906.01943 | Profile (Titel/Abstract ohne Moden) | [L?] |
| Levin, Rubakov: Q-balls with scalar charges | 2010/2011 | 1010.0030; MPLA 26, 409 | FLS mit verschwindendem Potential, Skalarladung; keine Moden | [L?] |
| Kim, Nugaev: Effectively flat potential in the FLS model | 2023 | 2309.09661 | Profile, effektive Theorie; keine Moden | [L?] |
| Kim, Nugaev, Shnir: Large solitons flattened by small quantum corrections | 2024 | 2405.09262 | UV-vervollstaendigtes FLS, Ein-Schleifen-Potential; keine Moden | [L?] |
| Heeck, Sokhashvili: Revisiting the FLS soliton model | 2023 | 2303.09566; EPJC 83, 526 | Profile, analytische Naeherungen | [L?] |
| Panin, Smolyakov: Classical behaviour of Q-balls in the Wick-Cutkosky model | 2019 | 10.1140/epjc/s10052-019-6638-2 | Zweifeld, klassische Stabilitaet, nichtlineare Entwicklung | [L?] |
| Friedberg, Lee, Sirlin: Class of scalar-field soliton solutions in three space dimensions | 1976 | 10.1103/PhysRevD.13.2739 | Ursprung des Modells; nicht gelesen | nur Metadaten |
| Lee, Pang: Nontopological solitons | 1992 | 10.1016/0370-1573(92)90064-7 | Review; kein Abstract greifbar | nur Metadaten |
| Zhang, Amin, Copeland, Saffin, Lozanov: Classical decay rates of oscillons | 2020 | 2004.01202; JCAP 07(2020)055 | Gamma_(3) ~ [S~(kappa_3)]^2 (Gl. 7.4); Dip bei omega_* ~ 0.82 m (Abb. 4); phi^6: "multiple dips" (Abschn. 7.5); reell, nichtlinear | [S] |
| Mukaida, Takimoto, Yamada: On longevity of I-ball/oscillon | 2017 | 1612.07750; JHEP 03(2017)122 | effektive U(1), exponentiell unterdrueckter Zerfall, Attraktoren | [L?] |
| Ibe, Kawasaki, Nakano, Sonomoto: Decay of I-ball/oscillon in classical field theory | 2019 | 1901.06130; JHEP 04(2019)030 | Dips im phi^6-Fall (nur als Zitat [51] in 2004.01202) | [L?, Zitat] |
| Honda, Choptuik: Fine structure of oscillons in the spherically symmetric phi^4 Klein-Gordon model | 2002 | hep-ph/0110065; PRD 65, 084037 | "resonant (and critical) behavior" mit Zeitskalengesetz (Abstract); Abhaengigkeit von den Anfangsdaten nicht nachgelesen | [L?] |
| Chen, Andersson, Li: Stability analysis for Q-balls with spectral method | 2026 | 10.1007/JHEP02(2026)078 | Einfeld; Oszillationsmoden werden imaginaer; keine BIC | [L?] |
| Elphick: Relativistic (3+1)-dimensional nontopological solitons under perturbations | 1997 | 10.1103/PhysRevD.55.7749 | allgemeine Stoerungsmethode, kollektive Koordinaten | [L?] |
| Zhou: Non-topological solitons and quasi-solitons (Review) | 2025 | 2411.16604; Rep. Prog. Phys. | FLS-Abschnitt II.6.1; keine BIC (nur Teile gesehen) | [L?] |
| Saly, Sundaresan: Excited states in the soliton bag model | 1984 | 10.1103/PhysRevD.29.525 | radial angeregte Zustaende im FL-Beutel; keine Abstrahlung | [L?] |
| Iwasaki, Kondo: Surface collective motion in the soliton bag model | 1987 | 10.1016/0370-2693(87)90948-8 | Oberflaechenbewegung, P11/P33 | nur Titel/Schlagworte |
| Haider: Excited states of the nucleon within the Friedberg-Lee model | 1993 | 10.1007/BF02771449 | radial angeregte Nukleonzustaende | nur Titel/Schlagworte |
| Kowata, Arima: Excitation spectrum in the Friedberg-Lee model | 2001 | nucl-th/0101019; PTP 105, 449 | 0s-Anregung des Skalarmesons als erster Zustand positiver Paritaet | [L?] |
| Ke-Pan Xie: Revisiting the fermion-field nontopological solitons | 2024 | 2405.01227; JHEP 09(2024)077 | fermionische Profile, keine Schwingungen | [L?] |
| Goldflam, Wilets: Soliton bag model | 1982 | 10.1103/PhysRevD.25.1951 | nur ueber Saly/Sundaresan bekannt | Zitat |
| (Autor nicht erhoben): Phase shifts of the Skyrmion breathing mode | 1984 | 10.1103/PhysRevLett.53.889 | Skyrmion-Atmung als Resonanz (nicht FL) | nur Titel |

Bereits im Leiterpapier und nicht erneut gesucht: Coleman1985, BattyeSutcliffe2000, Kovtun2018, Azatov2024 (= 2412.13885,
oben neu gelesen), Ciurla2024 (JHEP 07(2024)196), Evslin2026 (2604.07713), FriedrichWintgen1985, YuLu2025, Malomed2005,
SofferWeinstein1999.

## 5. Suchprotokoll und Grenzen

**Zeiten:**
- Gemessen (date) sind Start 18:31:08, Anlage der Arbeitsdatei 18:32:12, 18:42:41 sowie alle Zeiten ab Block I.
- Die Einzelzeiten in den Bloecken A bis H waren geschaetzt und sind in ARBEITSFELD.md berichtigt. Diese Bloecke liegen
  sicher zwischen 18:32:12 und 18:42:41.

| Block, Zeit | Abfrage (Quelle) | Treffer, Ergebnis |
|---|---|---|
| A, 18:32-18:42 | arXiv abs:"Friedberg-Lee-Sirlin" | 19 |
| A | arXiv "two-component/two-field Q-ball(s)" | 3, ohne Moden |
| A | arXiv "Q-ball" AND "bound states in the continuum" | 0 |
| A | arXiv "Q-ball" AND quasinormal | 2 (2604.07713, 2604.25223) |
| A | arXiv "soliton bag" AND radiation | 0 |
| B | arXiv "Friedberg-Lee" AND Modenbegriffe | 17, meist Neutrino-Symmetrie |
| B | arXiv "Q-ball" AND embedded | 4, irrelevant |
| B | arXiv "Q-ball" AND radiationless/non-radiating/trapped mode | 1 (0804.1357) |
| B | arXiv "soliton bag" | 7 |
| B | arXiv "nontopological soliton" AND vibration/breathing/normal modes/radiation | 3 |
| C | arxiv.org/abs 2503.04657, 2604.04494, nucl-th/0101019; HTML 2503.04657 | siehe Fundliste |
| D | arXiv au:Zhou_Shuang_Yong, au:Xie_Qi_Xin | 0 (Syntaxfehlschlag) |
| D | abs 2605.25243, 2411.08985 | ohne Moden |
| E | Semantic Scholar: Zitationen von 2503.04657 | 3, darunter 2510.27064 |
| E | arXiv superradiance AND (Q-ball/soliton) | 43 |
| E | OpenAlex: FLS 1976 | W1999778725, 499 Zitate |
| F | HTML 2510.27064 (zweimal), abs 2510.27064 | Abrufmodell, spaeter selbst nachgelesen (P2) |
| F | OpenAlex cites:W1999778725 + Modenbegriffe | 198, zwei Seiten Titel |
| F | OpenAlex Beutel + Atmung/Roper | 5 |
| G | OpenAlex-DOIs PRD 55 7749, PRD 111 096010, JHEP 02(2026)078, Rep. Prog. Phys. 2025 | siehe Fundliste |
| H | arXiv-API | HTTP 429 |
| H | Semantic Scholar | HTTP 404 und 429 |
| H | OpenAlex-Titelsuche | ergab 2412.13885 |
| H | HTML 2412.13885; OpenAlex JHEP 09(2024)077 | siehe Fundliste |
| I, 18:43:29-18:44:17 | HTML 2412.13885 gezielt; HTML 2411.16604 | siehe Fundliste |
| I | OpenAlex "soliton bag" + Anregung | 219 |
| I | OpenAlex Friedberg-Lee + Anregung | 71 |
| J, 18:44:17-18:45:29 | OpenAlex-DOIs PRD 29 525, PLB 199 437, Nuovo Cim. A 106 335; abs 1010.0030, 1805.11929 | zwei ohne Abstract |
| K, 18:45:29-18:46:29 | OpenAlex Oszillon-Zerfall | 607 |
| K | OpenAlex BIC ab 2024-10-01 | 3626, nur Photonik |
| K | OpenAlex Q-ball + reflectionless/Fano/... | 4094, MRT-ueberlagert |
| K', 18:46:29-18:47:27 | abs 2004.01202 | siehe Fundliste |
| K' | arXiv BIC AND (soliton/kink/oscillon/boson star/nontopological) | 20, ohne Q-Ball |
| L, 18:47:27-18:48:41 | PDF 2004.01202 | WebFetch binaer, mit dem Read-Werkzeug gelesen |
| L | OpenAlex EPJC 2019 (Wick-Cutkosky) | siehe Fundliste |
| M, 18:48:41-18:49:25 | abs 1612.07750, hep-ph/0110065; OpenAlex Phys. Rep. 1992 | Phys. Rep. ohne Abstract |
| N, 18:49:25-18:50:23 | arXiv all:Friedberg AND all:Sirlin | 21 |
| N | OpenAlex "breathing mode" | 23536, ueberlagert |
| N | abs 2405.09262 | siehe Fundliste |
| O, 18:50:23-18:51:43 | abs 2303.09566 | siehe Fundliste |
| P, 18:51:43-18:53:04 | PDF 2412.13885v1 (S. 1-2, 13-14, 18-20); PDF 2510.27064v1 (S. 11-14) | selbst gelesen |

**Fehlschlaege:**
- arXiv-API HTTP 429 (einmal); Semantic Scholar HTTP 429 und 404.
- Die Autorensyntax au:Name_Vorname_Vorname ergab 0 Treffer.
- WebFetch kann PDFs nicht lesen. Die gespeicherte Datei wurde mit dem Read-Werkzeug gelesen.
- OpenAlex hat fuer den Altbestand keine Abstracts.
- Das Abrufmodell nannte fuer 2412.13885 falsche Gleichungsnummern ("48-49" statt 46-47); am PDF berichtigt.

**Grenzen:**
- WebSearch stand nicht zur Verfuegung.
- Nur drei Volltexte sind selbst gelesen. 2503.04657 ist nur ueber das Abrufmodell gelesen ([S/A]); vor einem Zitat im
  Papier selbst nachlesen.
- Keine Bibliothekszugriffe: Lee/Pang 1992, Wilets 1989 (Buch), Friedberg/Lee 1977/78.
- Nicht geprueft, ob die M2-Hybridform (FLS plus psi-Masse plus Sextik) anderswo vorkommt.
- Die Fehlanzeigen beruhen ueberwiegend auf Schlagwort- und Abstractsuchen.

**Offene Fragen:**
- An die Leitung bzw. Finn: Soll das Papier Azatov2024 auch als FLS-Arbeit zitieren und die Superradianz-Reihe sowie die
  Oszillon-Dips abgrenzen?
- Projektseitig [H]: Liegt die M2-Leiterperiode bei pi/k_in, bei pi/sigma_+- oder bei pi/kappa? Kollabiert die Breite
  einer nahen Resonanz am stillen Punkt? Kommt dort eine zweite Mode nahe (Friedrich-Wintgen)?
- Literaturseitig: Behandeln Iwasaki/Kondo 1987 oder Haider 1993 Breiten von Beutelschwingungen? Mit den verfuegbaren
  Abstracts ist das nicht pruefbar.

## 6. Einfach gesagt

Wir haben nachgesehen, ob schon jemand die "stillen Stellen" unseres Zwei-Felder-Balls kennt: Ballgroessen, bei denen eine
Schwingung keine Wellen nach aussen abgibt. Fuer das Friedberg-Lee-Sirlin-Modell haben wir nichts davon gefunden. Wellen an
solchen Baellen untersucht ueberhaupt erst seit Ende 2024 jemand, und dann nur, wie Wellen am Ball abprallen. Zwei
Nachbarideen sind aber bekannt. Erstens wiederholen sich besondere Effekte, wenn der Ball um eine halbe Wellenlaenge
waechst. Zweitens gibt es bei schwingenden Klumpen eines einfachen Feldes Groessen, bei denen fast nichts abgestrahlt wird.
Unser Papier zitiert eine dieser Arbeiten schon, sagt aber nicht, dass sie auch das Zwei-Felder-Modell behandelt. Neu waere
also vor allem die exakte Stille selbst, nicht der Abstand der Leitersprossen.
