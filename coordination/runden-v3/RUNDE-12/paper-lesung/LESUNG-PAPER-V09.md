Urteil: Arbeitsfassung traegt mit Auflagen (13 Befunde, keiner blockierend; Pflichtauflage vor jeder Weitergabe: Befund 4 Literatur/Malomed)

# Frische Lesung Paper-Entwurf v0.9 (qball-bic-ladder-20260930)

- Leser: frischer Pruefer, Haus Anthropic, nicht am Entwurf beteiligt
- Auftrag: Leitung claude-primary, Auftragstext in der Nachricht (keine BRIEF-Datei genannt)
- Beginn (gemessen mit date): 2026-10-01 17:12:37 CEST (15:12:37 UTC)
- Ende (gemessen mit date): 2026-10-01 17:27:24 CEST (15:27:24 UTC); Dauer 14 min 47 s (17:12:37 bis 17:27:37 waeren
  15:00, minus 13 s), innerhalb der Zeitbox
- Nur gelesen (cat, sed -n, grep, jq, sha256sum, ls, wc, date); kein python/awk, kein ssh/git, kein Peerbus-Senden.
- Zeitbox: 50 min
- Gegenstand: model-lab/papers/qball-bic-ladder-20260930/ (main.tex, sections/, paper.txt, README.txt)
- Die abgebrochene Teildatei LESUNG-PAPER-V01.abgebrochen-2010.md wurde nicht gelesen.

## 0. Pruefstand Gegenstand (Hashes)

Gelesen 2026-10-01 ab 17:12 CEST (sha256sum, vollstaendig):
- paper.pdf 6119315eb55dc697f6d4ca6c6b2b332bbd572454cf2443c4878cbfc018e23366 (= genanntes Praefix 6119315eb55dc697)
- main.tex 43a80cae2a8ac417..., 435 Zeilen; sections/PROOF.tex f2cbd2fb4cd0d635..., NONLINEAR.tex 1f7f7d601e42f166...,
  MONOPOLE-BOUND.tex f30d04490a002160..., ENVIRONMENT-PROJECTION.tex d3f2b65be16da9ff... (= Hash in PLAN.txt und
  STAGE-REVIEW.txt), LITERATURE.tex 08715e31ff866a7a..., README.txt eaaddc041c427ad7...
- Belege: BEWEIS-2.md 3a21e2a3090142cc... (= genanntes Praefix), BEWEIS.md (BEWEIS-1) d9f14ebc2593b81d...
- Zeilenangaben unten: main.tex:N bzw. PROOF:N, NL:N (NONLINEAR.tex), MB:N (MONOPOLE-BOUND.tex),
  ENV:N (ENVIRONMENT-PROJECTION.tex), LIT:N (LITERATURE.tex).
- Gelesen wurde der LaTeX-Quelltext, nicht das gesetzte PDF (siehe Abschnitt 7).

## 1. Beweisaussagen (Tabelle)

Belege: B1 = RUNDE-07/beweis/BEWEIS.md (Ergebnis, Satz, Nicht behauptet, 7.1, 7.2); B2 = RUNDE-10/beweis2/BEWEIS-2.md
(Ergebnis, Saetze T1/T2, 4.1, 4.4, 6, 8); FL1/FL2 = Fremdlesungen OpenAI (GESAMT-REVIEW.txt); LS = LESUNG-LETZTE-SCHICHT-BEWEIS-2.md;
K1 = RUNDE-09/krein1/ERGEBNIS.md.

| # | Aussage (Datei:Zeile) | Beleg | Urteil |
|---|---|---|---|
| 1 | main:21-23 drei rechnergestuetzte Existenzaussagen (zwei radial, eine Dipol) | B1 Satz; B2 Ergebnis T1, T2 | traegt |
| 2 | main:24-26 unendlicher Radialbereich, analytische Aussenschranken, Kugelarithmetik; nicht aus Kastenbreiten | B1 Ergebnis (Lemma P, J); FL1 Punkt 1 ("Potentialschwanz nicht abgeschnitten") | traegt |
| 3 | main:43-47 projektinterne Lesungen aus zwei Haeusern; keine zweite unabhaengige Intervallimplementierung | B2 6.1, 6.3; B1 7.2 Schluss | traegt (Grenze "kein zweites Programm" eingehalten) |
| 4 | main:59-60, PROOF:89-90 n ist Fortsetzungsetikett, keine zertifizierte Knotenzahl, keine Aussage ueber Zwischenmoden | B2 Ergebnis, 6.5 | traegt |
| 5 | NL:7, NL:249 "first radial mode"; main:354 "first-radial-mode evidence"; main:401-402 "first radial location", "second radial location" | B2 6.5; LS Befund 1 ("erste"/"naechste" setzen eine lueckenlose Leiter voraus) | zu stark (Wortlaut; widerspricht main:59-60), Befund 3 |
| 6 | main:122-124, PROOF:103-107 "embedded" nur operational; kein Satz ueber Generator, Domaene, wesentliches Spektrum | B1 7.2 Auflage 3; B2 Ergebnis Auflage 3, 6.5 | traegt |
| 7 | PROOF:53-64 Viertupel im Kasten, positives globales Profil, r e^{kappa0 r} f -> c*, nichttriviale reelle regulaere Loesung, Schranke K_J e^{-kappa_c r} ab L, Normierung e^{kappa_c r} B -> 1 | B1 Satz 1-2; B2 T1/T2 Punkte 1-2 | traegt |
| 8 | PROOF:65-66 Felder glatt und "in jedem H^s(R^3)" | B1 Satz 4 sagt H^s woertlich; B2 T1/T2 Punkt 4 sagt nur "glatt und exponentiell abfallend" | fuer C0 traegt; fuer C1/C2 knapp ueber dem Wortlaut von B2 (mathematisch naheliegend, H^4_gamma fuer T2 separat belegt laut README v0.8), Befund 8 |
| 9 | PROOF:66-68 bedingt auf Korrektheit der Intervallimplementierung und Bibliotheken; PROOF:244-246 Python-FLINT, Arb/Acb, Ausfuehrung als Vertrauensbasis | B1 Ergebnis ("Vertrauensannahme"); B2 6.2 | traegt (FLINT als Vertrauensannahme eingehalten) |
| 10 | PROOF:94-99 geometrische radiale Einfachheit; keine algebraische Einfachheit, keine Jordan-Ketten ausgeschlossen; l = 1-Multiplett entartet | B1 7.2 Auflage 2; B2 T1/T2 Punkt 3, 6.5 | traegt; "for each fixed parameter pair" sollte "am eingeschlossenen Paar (rho*, omega*)" heissen, Befund 9 |
| 11 | PROOF:214-218 Brouwer/Krawczyk; Eindeutigkeit des Viertupels nicht behauptet | B1 Nicht behauptet; B2 6.4 | traegt |
| 12 | PROOF:222-229 2 kappa0 > kappa_c fuer alle drei Kaesten | B1 7.2 (>= 0,375236); B2 Auflage 1 (im Gesamtflag) | traegt; Kopfprobe C0: 2 x 0,44980 - 0,52437 = 0,37523 |
| 13 | PROOF:233-235 L = 40 / 32 / 36, 256 bit; Zusatzlaeufe groesseres L, 320 bit | B1 3.1 (A2 L40 256 bit, B2 L44 320 bit); B2 4.1 (T1-A L32 256, T1-B L36 320), 4.4 (T2-A L36 256, T2-B/B2 L40 320) | traegt |
| 14 | PROOF:235-239, main:402-406 T2-B bei L = 40 gescheitert; B2 adaptiv (c-Radius vergroessert); C2 ruht allein auf dem ersten erfolgreichen Zertifikat | B2 Ergebnis, 4.4 (c-Radius x 2^17), 6.6; FL2 "T2-A allein: ja" | traegt (Grenze eingehalten) |
| 15 | PROOF:241-243 "Independent mathematical and code reviews found no blocking error" | Urteile FL1, FL2, LESUNG-BEWEIS-2, LS: traegt bzw. traegt mit Auflagen, nichts blockierend; alle projektintern, ohne ODE-/H_0-/Krawczyk-Nachrechnung (B2 6.3) | Inhalt traegt; "Independent" zu stark gegen main:44-45 ("project-internal"), Befund 7 |
| 16 | PROOF:246-248 C0: Einfachheitsungleichung nicht im historischen Gesamtflag, C1/C2 ja | B1 7.2 Auflage 1; B2 Ergebnis | traegt |
| 17 | PROOF:251-255, main:40-41, main:274-276 keine nichtlineare Strahlungsfreiheit, keine nichtlineare Stabilitaet, keine algebraische Einfachheit | B1 Nicht behauptet; B2 6.5 ("keine lineare oder nichtlineare Stabilitaet") | traegt; "linear" fehlt in allen drei Ausschlusslisten, Befund 6 |
| 18 | ENV:30-37 positive Erhaltungsform N = 2<u,(rho I + omega sigma3)u> > 0 fuer rho > abs(omega) (Krein-Form, ohne den Namen) | K1 (E_2 = 2 rho N, gleiche Gewichte rho + omega, rho - omega); B2 T1/T2 Punkt 5 und 6.5: "kein Stabilitaetssatz" | traegt; kein Stabilitaetsschluss im Text, aber auch kein ausdruecklicher Ausschluss an der Stelle; der Text uebernimmt K1s "gutartig"-Deutung NICHT (gut). Befund 6 |
| 19 | LIT:39-45 Beitrag = Existenz an den Kaesten; endlich viele Punkte ergeben keine unendliche Leiter und keine gemeinsame Spektralfolge (verschiedene Hintergruende) | B1, B2, B2 6.5 | traegt |
| 20 | PROOF:188 Ursprungsgewicht mit Masse r^2/10 | FL2 Punkt 1 ("Integralgewichte 1/10 und 1/5"); Kopf: (1/2 - 1/5)/3 = 1/10 | traegt |

Kurz: Alle acht Grenzen des Auftrags sind im Hauptteil der Beweisabschnitte eingehalten (nur linear; eingebettet operational;
einfach = geometrische Dimension 1; n Etikett; kein zweites Programm; FLINT Vertrauensannahme; T2-B gescheitert, B2 adaptiv;
Krein-Form ohne Stabilitaetsschluss). Abweichungen nur im Wortlaut (Zeilen 5, 8, 10, 15, 17, 18).

## 2. Zahlen

### 2.1 Beweiskaesten (PROOF:77-82) gegen B1 Satz und B2 Saetze T1/T2
Alle sechs Mittelwerte und Radien ziffernweise gleich: C0 omega^2 0,797676787111865191750 +- 4,8e-22, rho
1,744617544837398735781 +- 6,8e-22; C1 0,6851289044582160933 +- 2,5e-20, 1,6903565973281434568 +- 4,7e-20;
C2 0,7544960137826372331 +- 7,8e-20, 1,826342030181069956 +- 3,0e-19. **traegt.**
Abgeleitete Zahlen, im Kopf nachgerechnet:
- NL:95 T2-Laborfrequenzen: omega = 0,868617, 2 rho = 3,652684; 0,868617 + 3,652684 = 4,521301; 0,868617 - 3,652684 = -2,784067.
  Stimmt mit 4,52130 / -2,78407 (STATUS-NONLINEAR: +4,5213013603 / -2,7840667604).
- NL:94 T1 ebenfalls offen: omega = 0,82773, 2 rho = 3,38071; Summe 4,208, Differenz -2,553, beide Betraege > 1. Stimmt.
- NL:262 C0-Seitenband: 0,8931275 - 3,4892351 = -2,5961076. Stimmt mit -2,59611.
- NL:169 Abklingraten T2: kappa0^2 = 1 - 0,754496 = 0,245504, also kappa0 = 0,49548 (0,4955^2 = 0,24552). kappa_c^2 >= 0,08276
  (B2 T2 Punkt 4), also kappa_c >= 0,2876 (0,2876^2 = 0,08271). Stimmt mit ">= 0,495 und 0,287". gamma = 1/10 liegt darunter.
- NL:251-252 C0 gerundet 0,7976767871 / 1,7446175448. Stimmt.

### 2.2 Leitertabelle (main:160-174) gegen DATENPAKET.json (jq, .stellen, l = 0, beta = 0,5, "Atmung psi_1")
- Anzahl: 15 Stellen A01-A15. Stimmt mit "fifteen radial candidate locations" (main:23, README:12).
- n = 1, 2, 5, 6, 10, 11, 12, 13, 14: gerundet gleich.
- **Abweichungen.** Die Tabelle folgt LEITER-STATUS.txt (Neuheitsaudit, Zahlen aus MODELL-DUENNWAND M:183-191) und nicht dem
  Datenpaket:

| n | Paper | DATENPAKET x (x_quelle) | Differenz |
|---|---|---|---|
| 3 | 0,631449 | 0,6314495672 (A_out-Nullstelle), gerundet 0,631450; Paperwert = W-Fit 0,6314494097 | 6e-7 |
| 4 | 0,601422 | 0,6014214666 (A_out-Nullstelle), gerundet 0,601421; Paperwert = W-Fit 0,6014220856 | 6e-7 |
| 7 | 0,559856 | 0,5598497365 (signierte Wurzel aus drei Dateiwerten) | 6,3e-6 |
| 8 | 0,552628 | 0,5526198964 (signierte Wurzel) | 8,1e-6 |
| 9 | 0,546951 | 0,5469425928 (signierte Wurzel) | 8,4e-6 |
| 15 | 0,528470 | 0,5284694984, gerundet 0,528469 (RUNDE-09.md:423 schreibt 0,528470) | 5e-7 |

  Wirkung im Kopf: Bei n = 8 ist x - 0,5 = 0,05262 und 0,05262^2 = 0,002769. Eine Verschiebung um 8e-6 verschiebt u = 1/(x - 0,5)
  um 8e-6 / 0,002769 = 2,9e-3, also etwa 0,1 % eines Schritts von 2,3. Qualitativ aendert das nichts. Der Satz "Digits and
  qualifiers follow the source records" (main:155-156) stimmt aber nur fuer die Sekundaerquelle (Befund 2).
- **Evidenzklassen** (jq .evidenz):
  - n = 2, 3, 4: "Umlauf aufgeloest"; n = 5: "Vorzeichenwechsel/Kurve".
  - n = 6 und 10: "interpoliert". Bei n = 6 ist das Feinverfahren nicht konvergiert, und zwei Laeufe weichen um 1,8e-5 ab.
  - n = 7-9 und 11-15: "Breitenminimum".
  - Das Paper fuehrt n = 3-5 nur als "Reported numerical location", also schwaecher als im Datenpaket. Seine eigene mittlere
    Stufe ("resolved winding test", main:139-140) kommt in der Tabelle nicht vor.
  - n = 6 steht als "Reported candidate" mit fuenf Nachkommastellen (0,56940). Dass es nicht konvergiert ist und die Laeufe
    um 1,8e-5 abweichen, fehlt (Befund 2).

### 2.3 Vorhersagetabelle (main:204-208) gegen LEITER-STATUS.txt Abschnitt 2 und RUNDE-09.md:423
- Alle zehn Fenster sind gleich.
- Systematischer Versatz des Duennwandmodells: 0,538619 - 0,53860 = 1,9e-5; 0,535468 - 0,535449 = 1,9e-5; 0,532792 - 0,532772 = 2,0e-5;
  0,530490 - 0,530470 = 2,0e-5; 0,528489 - 0,528470 = 1,9e-5. Stimmt mit "about 2e-5 above".
- Vorzeichenmuster der sequentiellen Fortsetzung: n = 11 liegt darueber (0,53867 > 0,53860), n = 12-15 darunter. Stimmt.
- Fensterpruefung: n = 11 |Abstand| 7e-5 < 3e-4; n = 12 9e-6 < 1,2e-4; n = 13 1,2e-5 < 1,2e-4; n = 14 1e-5 < 4e-5; n = 15 1,2e-5 < 5e-5.
  Duennwand mit drei Balken: 1,9e-5 < 7,5e-5 und so weiter. "All five passed" stimmt.
- Schritte (main:259-260):
  - u12 = 1/0,035449 = 28,20954; u13 = 1/0,032772 = 30,51385; u14 = 1/0,030470 = 32,81917; u15 = 1/0,028470 = 35,12469
    (Probe: 0,032772 x 30,5139 = 0,98316 + 0,01684 = 1,00000).
  - Differenzen 2,30431 / 2,30532 / 2,30552. Stimmt mit 2,3043 / 2,3054 / 2,3055 bis auf die Rundung der Eingaben.
  - 2,298 und 2,334 stimmen mit LEITER-STATUS Abschnitt 4 ueberein.
- Nicht in der Tabelle: die eingefrorene MOD2-Vorhersage fuer n = 10 (0,542382 +- 0,000020, LEITER-STATUS Abschnitt 2). Sie ist
  ungetestet, weil n = 10 nicht verfeinert wurde. Ein Fehlschlag wird also nicht verdeckt, die Zahl der Vorhersagen ist aber
  sechs, nicht fuenf (Befund 10).

### 2.4 Nichtlineare Zahlen
- Leistungstabelle NL:210-211 gegen forced/ERGEBNIS.txt:17-20: 2,4239e-7 / 6,0359e-5 / 4,4956e-7 / 9,1587e-5. Stimmt.
- NL:204 "below 7,8e-8": Die Quelle nennt als Groesstwert 7,72e-8 (kombinierte Verfeinerung). Stimmt.
- NL:224 "ODE defects reach 5,3e-6": Die Quellen sind uneinheitlich. forced/ERGEBNIS.txt:43 nennt 5,2e-6,
  reconstruction/ERGEBNIS.txt:21 nennt 5,21e-6, paper-v05/REVIEW.txt:13 nennt "5,3e-6 stimmen mit den gespeicherten Daten".
  Nicht aufgeloest, Befund 11.
- NL:239-244 gegen green-check/ERGEBNIS.txt:13-16: 9,563e-11 ergibt 9,6e-11; 1,258e-11 ergibt 1,3e-11. Die Quadraturaenderung
  1,827e-9 liegt unter "1,9e-9 or smaller". Stimmt.
- MB:26-35 gegen error-budget-components/ERGEBNIS.txt:
  - E <= 0,001023269269845279... steht im Paper nach oben gerundet als < ...845280.
  - c_low >= 0,001582591541472706... und die Marge >= 0,000559322271627427... stehen nach unten abgeschnitten. Das ist richtig
    gerundet.
  - Kopfprobe der Marge: 1582591541472706 - 1023269269845279 = 559322271627427. Stimmt.
  - Kanal 0/1: false/true. Stimmt mit "first channel remains undecided".
- NL:257 Faktoren 15,97 / 15,89 (BIC-TESTPAKET-ERGEBNIS.txt:17). Stimmt.
- NL:272-273 5,1563e-5 gegen 5,03-5,10e-5 (STATUS-NONLINEAR: 5,15628e-5). Stimmt. Die Abweichung betraegt 1,1 bis 2,5 %
  (0,0563/5,10 und 0,1263/5,03). Das Paper behauptet zu Recht NICHT die "unter 1 Prozent" aus NEUHEITSMATRIX Punkt 4.
- NL:280 I_2-Intervall gegen bic-proof/certificate/ERGEBNIS.txt:5. Stimmt; I_1 enthaelt 0, certificate_pass FALSE. Stimmt.

### 2.5 Modellalgebra (im Kopf)
Alle Pruefungen stimmen:
- omega_c^2 = 1 - 1/(4 beta) = 1/2.
- D = U' + S U'' = 1 - 4S + 4,5 S^2 und C = -2S + 3S^2.
- D_c = 3/2 und C_c = 1 bei S_c = 1.
- k_in^2: Eigenwerte der konstanten 2x2-Matrix.
- G_2 mit A = f(-2 + 4,5 f^2) und C = 1,5 f^3; Q_+, Q_-, Q_0.
- Y10^2 = Y00/sqrt(4 pi) + Y20/sqrt(5 pi).
- Polarisationsnormen: Mit dem Vierermoment (4 pi/15)(abs(chi)^2 + 2 nu^2) folgt
  abs(P2)^2 = (3 nu^2 - abs(chi)^2)/(10 pi) >= nu^2/(5 pi).
- N = -<u,H'(rho)u> = 2<u,(rho + omega sigma3)u>.
- (env:pulse) per Cauchy-Schwarz.
- E - q-Identitaet: U(S) - S/2 = (S/2)(1 - S)^2 >= 0, daraus ess sup S >= (q - E)/(2E).

## 3. Neuheit

### 3.1 Was der Entwurf beansprucht
- Er erhebt keinen Prioritaetsanspruch (main:73-76, LIT:42-43).
- Er beansprucht keine neuen Begriffe: eingebettete Moden, Interferenzunterdrueckung, Q-Ball-Anregungen und
  Duennwandnaeherung gelten als bekannt (main:73-74).
- Als Beitrag beansprucht er "this combination of model-specific linear existence enclosures and numerically tested spacing
  structure" (main:71-72).
- Kein "first". Die Zahl "unter 1 Prozent" aus NEUHEITSMATRIX Punkt 4 uebernimmt er nicht (siehe 2.4).
- Das entspricht der NEUHEITSMATRIX: "Kein 'first' ... keine bewiesene nichtlineare Stabilitaet".

### 3.2 Was die eigenen Audits kennen, das Paper aber nicht nennt
Gesucht in LITERATURE.tex und bibliography.tex; das Ergebnis ist leer. Die Literaturliste hat sechs Eintraege: Coleman, Kovtun,
Ciurla, Friedrich-Wintgen, Yu-Lu, Kasuya-Kawasaki.

| Quelle (projektinterne Fundstelle) | Bezug zum Paper | Fehlt im Paper |
|---|---|---|
| Malomed u. a. 2005: eingebettete Solitonen haeufen sich nach einer Bohr-Sommerfeld-Regel, eps_n = 3,27 n^(-6/5) (RUNDE-11.md:154-156, MESS-2) | Naechster bekannter Fall einer sich haeufenden Folge strahlungsfreier Punkte. Er betrifft genau die beanspruchte "spacing structure". | ja, Befund 4 |
| Azatov/Ho/Khalil, arXiv:2412.13885v1: gekoppelte radiale Streugleichungen in 3+1D mit denselben linearen Koeffizienten (NEUHEITSMATRIX Punkt 2) | Naeher am Modell als Kovtun 2018, das LIT:6-12 als "direct structural comparison" fuehrt | ja, Befund 4 |
| Evslin u. a., arXiv:2604.07713v1: 1+1D, Kleinamplituden-Gegenrotationsmoden, Feshbach-QNM; Primaer-HTML gelesen (NEUHEITSMATRIX Punkt 1, QBALL-LITERATUR [A]) | Gleiche Kanalstruktur wie bei Ciurla | ja, Befund 4 |
| Soffer/Weinstein 1999 (Invent. Math. 136): nichtlineare Fermi-Goldene-Regel, Strahlungsdaempfung eingebetteter Niveaus; Bemerkung (3) zur U(1)-Ausnahme (ALTERNATIVE-PRIORITAET [3]) | Standardrahmen fuer "lineare Mode, nichtlineare Oberwellenstrahlung", also den ganzen Abschnitt nl:section. NL:298-300 nennt nur "earlier real-field shell-model normal forms", ohne Zitat. | ja, Befund 4 |
| Arb/FLINT bzw. Krawczyk-Verfahren | Die Rechensoftware ist Teil der Vertrauensbasis (PROOF:244-246), wird aber nicht zitiert | ja, nicht blockierend, Teil von Befund 4 |

### 3.3 Malomed-Hinweis: fair dargestellt?
Nein, er fehlt. Der Entwurf leitet eps_n ~ 1/(b_inf n) aus dem Duennwandmodell her (main:253-258), also eine Haeufung mit
Exponent -1. MESS-2 grenzt genau darueber ab: "Eine sich haeufende Folge stiller Punkte ist als Idee also nicht neu. Neu bleibt
die Leiter fuer eine lineare Innenmode, mit Haeufungsexponent -1 ... statt -6/5."

Anforderungen an den Autor (kein Wortlaut von mir):
- (a) Malomed 2005 vorher an der Primaerquelle lesen. MESS-2 vermerkt, dass das Suchkontingent erschoepft war; Koeffizient und
  Exponent habe ich nicht geprueft.
- (b) Die Abgrenzung muss den Unterschied nennen: nichtlineare eingebettete Solitonen dort, lineare Innenmode auf wechselnden
  Hintergruenden hier (LIT:44-45).
- (c) Der Exponent -1 ist eine Modellfolge der kalibrierten Duennwandnaeherung, kein Messbefund. Laut LEITER-STATUS
  Abschnitt 3 (R9:177-196) ergeben freie Potenzfits Exponenten -0,76 bis -0,88. Die Kehrwertform ist nur um den Faktor 1,2-2
  besser, erwartet war ein Faktor >= 10 und wurde ausdruecklich verfehlt. Diese Diagnose fehlt im Paper ganz. Sie gehoert
  hinein, sobald der Exponent als Abgrenzungsmerkmal dient.
- (d) Gegenfall: Wenn die spaeten Schritte 2,3043 / 2,3054 / 2,3055 durch Lagefehler der interpolierten x-Werte entstehen
  (LEITER-STATUS Abschnitt 4: "Fehlerfortpflanzung ... nicht angegeben"), traegt die Gleichabstaendigkeit allein den
  Unterschied zu -6/5 nicht. Dann muss eine Lageunsicherheit je Zeile her.

### 3.4 Urteil Neuheit
- Die Prioritaetsgrenzen sind sauber, es gibt keine falsche Neuheitsbehauptung.
- Der Literaturstand ist aber unvollstaendig: Vier Vorlaeufer, die das Projekt selbst gelesen oder notiert hat, fehlen.
  Einer davon (Malomed) betrifft direkt den beanspruchten Beitrag "spacing structure".
- Fuer die Arbeitsfassung ist das nicht blockierend, weil nichts veroeffentlicht wird und keine Prioritaet beansprucht wird.
  Vor jeder Weitergabe ist es eine Pflichtauflage.

## 4. Nichtlineares und Anregung

### 4.1 "Offener Kanal plus Quelle ungleich null" gegen "Strahlung nachgewiesen": sauber getrennt
- **NL:5-7** trennt drei Stufen: exakte Quelle, kinematisch offener Kanal und auslaufende Antwort ungleich null.
- **NL:103-106** sagt ausdruecklich: "An open channel and a nonzero local source do not establish radiation: the outgoing source
  overlap can vanish."
- **NL:220-222 (T2, genaeherter Input).** Dort steht "supports second-harmonic leakage ... beyond merely finding open
  channels and nonzero local sources. It does not certify leakage at the exact enclosed BIC." Die Grenzen sind genannt:
  - die Float-Eingaben liegen ausserhalb des Kastens;
  - es gibt ODE-Defekte;
  - die Aussenreste sind nicht propagiert.
- **MB:21-44 (exakte Mode, bedingt).** Nur der zweite Rechenkanal ist von null getrennt, der erste bleibt unentschieden
  (MB:42-43, "does not imply its coefficient vanishes").
  - Die Bedingungen sind T2-Einschluss, regulaerer/Jost-Spann und analytische Schranken.
  - Die Zahlen stimmen mit error-budget-components/ERGEBNIS.txt und dem Review (8425 Gates, GO) ueberein.
- **NL:283-291.** Das I_2 des eingefrorenen Operators wird ausdruecklich nicht als Kontinuumsaussage gefuehrt.
- **NL:7-9 und NL:106.** Die n = 1-Evidenz wird nicht auf T1/T2 uebertragen, die T1-Antwort bleibt offen.
- **Kleine Wortlautpunkte, nicht blockierend (Befund 5):**
  - Das Abstract (main:32) nennt die Quellen "second-harmonic radiation sources". Das setzt Strahlung voraus, bevor die
    Amplitude gezeigt ist; im Sinn von NL:103 besser "Quellen in offenen Kanaelen".
  - Der Schluss (main:379-380) sagt "resolves second-harmonic leakage", der Hauptteil nur "supports" (NL:220).
- **Befund 1, Quelltext von MONOPOLE-BOUND.tex.** MB:1-2 enthaelt noch den LaTeX-Kommentar "Proposed addition, not yet
  incorporated in the canonical manuscript ... Final analytical dependency audit pending".
  - Im PDF ist er unsichtbar, die Quellen widersprechen damit aber dem eingebauten Stand (v0.8/v0.9).
  - Der Audit BEWEISKETTE-KOMPONENTEN.txt (E.2) nennt fuer eine "selbstaendige Paper-Theoremfassung" noch zwei Punkte:
    - die explizite Zusammenstellung der geerbten Hypothesen;
    - die gamma/H^4-Zuordnung. Diese ist inzwischen mit Text-GO erledigt (INTEGRATED-REVIEW-NACHTRAG.txt).
  - Die Zusammenstellung fehlt im Paper weiterhin. MB:21-22 verweist nur auf "accompanying proof dependencies".
  - Das Abstract spricht trotzdem von den "stated ... hypotheses" (main:35-36).
  - Das ist kein Inhaltsfehler, weil die Aussage bedingt bleibt. Die Hypothesen gehoeren aber in den Text, und der
    Kommentar ist zu berichtigen.

### 4.2 "Anregung einer vorhandenen Mode" gegen "Bildung", "Lebensdauer", "Linienbreite": in v0.9 sauber getrennt
- **ENV:53-58.** Eine homogene Loesung mit c(0) = 0 bevoelkert die Projektion nicht; eine lokale Quelle mit <u,S> ungleich 0
  "can drive the mode". Gemeint ist Anregung einer vorhandenen Mode, und so steht es auch da.
- **ENV:63-69.** "mode-projection bound, not a statement about the energy supplied by an unspecified environment ... No globally
  passive port model, loading rate, nonlinear formation mechanism, or indefinite maintenance follows." Indefinitheit von J auf
  dem ganzen Phasenraum ist genannt.
- **Bildung:** main:303-340 grenzt Fragmentierung und Energie-Ladungs-Schranke ausdruecklich als "not a formation result" ab.
- **Lebensdauer:** NL:216, NL:293-298, MB:49, main:382; nirgends behauptet.
- **Linienbreite:** main:26, main:220, NL:204; nirgends als Null- oder Breitenaussage verwendet.

### 4.3 Dipolpuls-Ergebnisse vom 1.10. (events.jsonl, jq nach id)
- **15:01:00 UTC, b2a1cf0b..., vorlaeufig.** Vorab gewaehlter Puls (T = 1, Y10, chi = (r-1)^2 (2-r)^2). Die Quellenprojektion
  ist von null getrennt mit abs(L) in [598538585 x 2^-38, 74880585 x 2^-35].
  - Kopfprobe der Grenzen: 2^38 = 274877906944 und 2^35 = 34359738368; das gibt etwa [0,0021775, 0,0021793].
  - Gegenprobe mit den gedruckten Huellen (Re 0,00059 +- 2,78e-6, Im -0,00210 +- 4,19e-6): abs(L) liegt in etwa
    [0,002177, 0,002186]. Das ist vertraeglich.
- **15:04:01 UTC, db29e93e..., Annahme nach zwei Nichtautorpruefungen.** Fuer abs(delta) <= 1/2 gilt abs(L(delta)) > 7/8000.
  Der Eintrag sagt woertlich: "keine Linienbreite oder Lebensdauer", "N/Anregungsenergie wurden nicht bestimmt", "kein
  Q-Ball-Bildungs- oder Selbstversorgungsnachweis".
- **Stand v0.9.** Beide Eintraege sagen "kanonisches v0.9 bleibt ... unveraendert". v0.9 enthaelt die Pulsergebnisse
  tatsaechlich nicht, und ENV behauptet nur die bedingte Moeglichkeit. Ein Widerspruch zum Paper besteht nicht.
- **Anforderungen an den angekuendigten Einschub (Befund 12, nicht blockierend fuer v0.9):**
  - (a) Er heisst "Anregung der vorhandenen zertifizierten Mode im linearen Modell".
  - (b) Er nennt weder Amplitude noch Energie, solange N nicht berechnet ist.
  - (c) Die Verstimmungsschranke ist eine konservative Pulsabschaetzung, keine Linienbreite, Guete oder Lebensdauer.
  - (d) Der Antrieb ist idealisiert auf der zertifizierten Frequenz definiert, nicht als realer Sender.
  - (e) Das Y00-Ergebnis ist nur ein direkter Ueberlapp null; es verbietet weder andere Moden noch nichtlineare Antworten.
  - (f) Die Bedingungen sind c(0) = 0, verschwindender Randterm, epsilon reell ungleich 0, N > 0 und die geerbten Huellen.
  - (g) Er verwendet exakte Dyaden statt gedruckter Dezimalen als Praezisionsangabe.

## 5. Rueckwaerts (Abstract, Einleitung, Schluss gegen Hauptteil)

Vorgehen: Ich habe jeden Satz aus Abstract (main:16-41), Status (main:43-47), Einleitung (main:50-76), Interpretation
(main:270-276) und Schluss (main:372-383) gegen die zugehoerige Hauptteilstelle gelesen. Kein Satz widerspricht dem Hauptteil.
Bei folgenden Saetzen ist der Rahmen etwas staerker oder knapper als der Hauptteil:

| Rahmenstelle | Hauptteil | Abweichung | Gewicht |
|---|---|---|---|
| main:26-28 Abstract: "A thin-wall phase-matching description accounts for the observed near-uniform spacing" | main:247-251 "wall phase theta and dressed level shift ... remain calibrated ... not a parameter-free prediction"; main:261 "supports a useful spacing description" | "kalibriert" fehlt im Abstract, "accounts for" ist staerker als "supports" | nicht blockierend (Befund 5) |
| main:28-29 Abstract: "Sequential and author-blinded comparisons locate further linewidth minima" | main:192-196 "reportedly blinded ... at the author level. Some target results were already known to the coordinating team" | "reportedly" und die Kenntnis der Koordination fehlen. Ausserdem lokalisieren die Vergleiche keine Minima, sie testen Vorhersagen | nicht blockierend (Befund 5) |
| main:31-32 Abstract: "second-harmonic radiation sources" | NL:103-106 | siehe 4.1 | nicht blockierend (Befund 5) |
| main:35-36 Abstract: "conditional on the stated exact-mode and analytic enclosure hypotheses" | MB:21-22 verweist nur auf "accompanying proof dependencies" | Die Hypothesen sind nicht im Text "stated" | nicht blockierend (Befund 1) |
| main:379-380 Schluss: "resolves second-harmonic leakage for an approximate input" | NL:220 "supports" | etwas staerker, aber mit dem Zusatz "approximate input" | nicht blockierend (Befund 5) |
| main:40-41 Abstract, PROOF:251-255 und main:274-276: Ausschluss nur der *nichtlinearen* Stabilitaet | B2 6.5: "keine lineare oder nichtlineare Stabilitaet"; ENV:30-37 zeigt eine positive Krein-artige Form | Ein Leser kann aus N > 0 plus fehlendem Ausschluss "linear stabil" lesen | nicht blockierend (Befund 6) |
| main:354 Ausblick und NL:7, NL:249 "first radial mode" | main:59-60 "n is a continuation label" | Ordnungswort gegen die eigene Etikettregel | nicht blockierend (Befund 3) |

Gegenrichtung (Hauptteil staerker als Rahmen): keine Stelle gefunden. Die Einschraenkungen der Beweisabschnitte (PROOF:4-8,
PROOF:251-255) erscheinen sinngleich im Abstract (main:24-30) und im Schluss (main:373-375).
Titel ("localized linear modes") und README-SCOPE (README:11-18) stimmen mit dem Hauptteil.

## 6. Befunde (nummeriert, blockierend / nicht blockierend)

Kein blockierender Befund. Keine Beweisaussage ist falsch. Alle Zertifikatszahlen und alle nichtlinearen Ergebniszahlen
stimmen mit den Quellen, bis auf eine uneinheitliche Quellenlage (Befund 11). Die Auflagen betreffen Wortlaut, Herkunft und
Literatur.

1. **MONOPOLE-BOUND.tex:1-2, MB:21-22, main:35-36. Nicht blockierend.**
   - Der Quelltextkommentar "Proposed addition, not yet incorporated ... Final analytical dependency audit pending" ist
     veraltet. Der Abschnitt ist seit v0.8 eingebaut und vom Review gedeckt (8425 Gates, GO).
   - Die geerbten Hypothesen stehen nicht im Text. BEWEISKETTE-KOMPONENTEN.txt E.2 verlangt fuer eine selbstaendige
     Satzfassung ihre explizite Zusammenstellung. Das Abstract nennt sie trotzdem "stated".
   - Auflage: den Kommentar berichtigen und die Hypothesenliste in den Text aufnehmen, mindestens:
     - T2-Einschluss;
     - regulaerer/Jost-Spann;
     - Aussenraumschranke bei der exakten Frequenz;
     - analytische Volterra- und Schwanzschranken;
     - gemeinsame Normierung.
2. **main:155-156 und main:160-174 (Leitertabelle), main:150-152. Nicht blockierend.**
   - Die Werte stammen aus LEITER-STATUS.txt, nicht aus dem Datenpaket. Bei n = 3, 4, 7, 8, 9 und 15 weichen sie vom
     DATENPAKET ab, um bis zu 8,4e-6 (Tabelle in 2.2).
   - "Digits ... follow the source records" stimmt nur fuer die Sekundaerquelle.
   - n = 3-5 sind schwaecher etikettiert als im Datenpaket (dort "Umlauf aufgeloest" bzw. "Vorzeichenwechsel").
   - Bei n = 6 fehlt der Hinweis: nicht konvergiert, zwei Laeufe um 1,8e-5 auseinander. Gedruckt sind trotzdem fuenf
     Nachkommastellen.
   - main:152 "no corresponding rigorous winding enclosure" legt nahe, andere Zeilen haetten strenge Umlaufschranken. Der
     Umlauftest ist aber ueberall nur numerisch (DATENPAKET.evidenzklassen).
   - Auflage: Quelle je Zeile nennen, Datenpaketwerte verwenden oder die Abweichung begruenden, und die mittlere Stufe der
     eigenen Hierarchie in der Tabelle ausweisen.
3. **NL:7, NL:249 (Ueberschrift 7.6, auch im Inhaltsverzeichnis), main:354, main:401-402. Nicht blockierend.**
   - Dort steht "first radial mode", "first radial location", "second radial location".
   - Ordnungswoerter setzen eine lueckenlose Leiter voraus. Genau das hat LS Befund 1 in BEWEIS-2 entfernt, und main:59-60
     schliesst es selbst aus.
   - Auflage: durch Etiketten ersetzen (C0/C1, Leiteretikett n = 1).
4. **LIT:1-47, sections/bibliography.tex. Nicht blockierend fuer die Arbeitsfassung, Pflicht vor jeder Weitergabe.**
   - Es fehlen Vorlaeufer, die das Projekt selbst gelesen oder notiert hat:
     - Malomed u. a. 2005 (Haeufung eingebetteter Solitonen, eps_n ~ n^(-6/5));
     - Azatov/Ho/Khalil 2412.13885 (gleiche 3+1D-Radialgleichungen);
     - Evslin u. a. 2604.07713;
     - Soffer/Weinstein 1999 (nichtlineare Fermi-Goldene-Regel, U(1)-Ausnahme);
     - Arb/FLINT bzw. Krawczyk als Methodenzitat.
   - Die beanspruchte "spacing structure" (main:71-72) ist ohne Malomed nicht fair eingeordnet.
   - Die Fitdiagnose fehlt: freie Exponenten -0,76 bis -0,88, Kehrwertform nur Faktor 1,2-2 besser.
   - Anforderungen siehe 3.3 (a) bis (d).
5. **main:26-29, main:31-32, main:379-380. Nicht blockierend.** Der Rahmen ist etwas staerker als der Hauptteil:
   - "accounts for" ohne "calibrated";
   - "author-blinded" ohne "reportedly" und ohne die Kenntnis der Koordination;
   - "locate further linewidth minima";
   - "radiation sources";
   - "resolves leakage".
   - Siehe Tabelle in 5.
6. **main:40-41, PROOF:251-255, main:274-276, ENV:30-37. Nicht blockierend.**
   - Ausgeschlossen wird nur die *nichtlineare* Stabilitaet. B2 6.5 schliesst auch die lineare aus.
   - ENV zeigt eine positive Krein-artige Erhaltungsform, sagt aber nicht ausdruecklich, dass daraus kein Stabilitaetssatz
     folgt (B2 T1/T2 Punkt 5, FL2 A4).
   - Auflage: Ausschluss "weder lineare noch nichtlineare Stabilitaet" an beiden Stellen.
   - Positiv: Die "gutartig"-Deutung aus KREIN-1 ist nicht uebernommen.
7. **PROOF:241. Nicht blockierend.** "Independent mathematical and code reviews" sollte "project-internal cross-house reviews"
   heissen, wie in main:44-45. Alle Lesungen sind projektintern, ohne ODE-, H_0- oder Krawczyk-Nachrechnung (B2 6.3).
8. **PROOF:65-66. Nicht blockierend.** "every Sobolev space H^s" steht woertlich nur in B1 (C0). B2 sagt fuer C1/C2 "glatt und
   exponentiell abfallend". Auflage: Beleg nennen (Lemma R/R-l1 plus ODE-Argument) oder den Wortlaut auf B2 begrenzen.
9. **PROOF:94. Nicht blockierend.** "For each fixed parameter pair" meint das eingeschlossene Paar (rho*, omega*). So
   praezisieren.
10. **main:189-196 und main:203-209. Nicht blockierend.**
    - MOD2 hatte sechs eingefrorene Vorhersagen; die fuer n = 10 (0,542382 +- 0,000020) fehlt. Sie ist ungetestet, also wird
      kein Fehlschlag verdeckt.
    - Auflage: in einem Satz nennen.
11. **NL:224 "5,3e-6". Nicht blockierend.** forced/ERGEBNIS.txt:43 nennt 5,2e-6, reconstruction/ERGEBNIS.txt:21 nennt
    5,21e-6, paper-v05/REVIEW.txt:13 nennt 5,3e-6 "stimmen mit den gespeicherten Daten". Auflage: Gitter und Quelle der
    Zahl angeben.
12. **Dipolpuls (events.jsonl 15:01/15:04 UTC). Nicht blockierend fuer v0.9, da nicht eingebaut.** Fuer den Einschub gelten
    die Anforderungen 4.3 (a) bis (g).
13. **sections/PROOF-SOURCES.txt:18-20 gegen SOURCE-SHA256SUMS.txt:2-3 und main:397-398. Nicht blockierend.**
    - PROOF.tex wurde gegen BEWEIS-2.md 3ad62460... geschrieben. Das ist die Sicherung bak-20260930-1949, also der Stand vor
      Einarbeitung von LS L1-L5 und Nachpruefung; der PLAN entsprechend 0f8f0790... (bak-1949).
    - Das Manifest fuehrt die Endfassung 3a21e2a3... / 4b6b3c1b... als "versions read".
    - Inhaltlich finde ich in PROOF.tex keine Folge. Die Ordnungswoerter (Befund 3) sind aber genau die in L1 entfernte Art.
    - Auflage: PROOF.tex gegen die Endfassung gegenlesen und das Manifest wahrheitsgemaess fuehren.

## 7. Nicht geprueft

- **Satz und Darstellung.** Das gesetzte PDF habe ich nicht gelesen, ebenso wenig paper.html. paper.txt nur als Stichprobe:
  Draft 0.9, Zahlen 0,601422 / 0,559856 / 0,000559322271627427 / 5,3e-6 und die Ordnungswoerter stimmen mit dem Quelltext.
- **Lemmakonstanten** in PROOF:124-177 (K_P, eta, Lambda, a1, b1, a2, b2, epsilon) habe ich nicht gegen BEWEIS-PLAN.md /
  BEWEIS-2-PLAN.md geprueft. Ebenso nicht das Positivitaetsargument PROOF:218-220 im Einzelnen.
- **Duennwandherleitung** (R_tw, Wandphase, b_inf, 2,298 / 2,334) nicht gegen MODELL-DUENNWAND.md. Geprueft habe ich nur
  k_in^2, D_c, C_c und die Uebernahme aus LEITER-STATUS.
- **Verblindung und Zeitstempel** der Vorhersagen (RUNDE-09.md, VORHERSAGEN-MOD2.md, Hashes) nicht geprueft. Die Fensterzahlen
  stammen nur aus LEITER-STATUS bzw. RUNDE-09.md:423.
- **Primaerliteratur** nicht gelesen: Coleman, Kovtun, Ciurla, Friedrich-Wintgen, Yu-Lu, Kasuya-Kawasaki, Malomed 2005, Azatov
  u. a., Evslin u. a., Soffer-Weinstein. Kein Webzugriff.
- **Nichtlineare Rechnungen:** Code, Methode und Zertifikatskette (forced/, reconstruction/, error-budget-components/,
  GEWICHTETE-REGULARITAET, BEDINGTES-FORTSETZUNGSLEMMA, POLARISATIONS-LEMMA-L2) nicht nachgeprueft. Geprueft habe ich nur
  Ergebniszahlen und Review-Urteile.
- **Herleitungen:** KREIN-1 und die G/J-Identitaet in ENV:22-29 nicht nachgerechnet. Nachgerechnet nur N = -<u,H'u> und die
  Pulsschranke.
- **Dipolpuls:** die Dateien unter environment-source-overlap/ (RESULT.json, Reviews, Paper-Insert-Draft) nicht gelesen, nur
  die zwei Peerbus-Eintraege.
- **Lesungen:** LESUNG-BEWEIS-2.md und NACHPRUEFUNG-1949 nur Urteilszeilen und Befund 1; ihr Inhalt ist ueber B2 Abschnitt 8
  erfasst.
- **Bewusst nicht geoeffnet:** LESUNG-PAPER-V01.abgebrochen-2010.md, KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/,
  ks-1-dk-lauf*/, Datendateien (.npz, .dat), Geheimnisse.

## 8. Quote

- **Beweisaussagen:** 20 geprueft. 14 tragen ohne Einschraenkung, 4 tragen mit Wortlautauflage (Zeilen 8, 10, 17, 18),
  2 sind zu stark im Wortlaut (Zeilen 5, 15). Falsch ist keine.
- **Zahlen:** 62 gegen Quellen geprueft. 55 stimmen.
  - 6 Leiterwerte weichen vom Datenpaket ab, um hoechstens 8,4e-6. Sie stimmen aber mit der genannten Sekundaerquelle
    LEITER-STATUS.
  - 1 Zahl hat uneinheitliche Quellen (5,3e-6).
  - Aufschluesselung der 62: Beweiskaesten 6; Leiter 15; Vorhersagefenster 10; abgeleitete Frequenzen, Raten und Rundungen 7;
    Schritte und Modellwerte 5; Versatz 1; nichtlineare Zahlen 18.

## Einfach gesagt

Der Entwurf beschreibt besondere Schwingungen eines Q-Balls, die in der vereinfachten (linearen) Rechnung keine Wellen
abstrahlen. Drei davon sind mit garantierter Rechnerarithmetik bewiesen (zwei Atmungs-, eine Kippschwingung); von den fuenfzehn
radialen Stellen sind die uebrigen dreizehn nur numerisch gefunden. Ich habe jede
Beweisaussage und jede Zahl gegen die Beweisakten und Ergebnisdateien gelegt. Falsche Aussagen habe ich nicht gefunden, aber
einige zu forsche Formulierungen und sechs Tabellenwerte, die leicht vom Datenpaket abweichen. Die wichtigste Auflage betrifft
die Literatur: Eine bekannte Arbeit ueber sich haeufende stille Punkte (Malomed 2005) und drei weitere Vorlaeufer fehlen und
muessen vor jeder Weitergabe eingeordnet werden.
