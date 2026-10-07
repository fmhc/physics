# CDT-HORAVA-L: Arbeitsfeld (feldforscher, Runde 37)

- Start 2026-10-04 03:19:18 CEST (date). Zeitbox 75 min, also Abgabe spaetestens 04:34 CEST.
- Datei angelegt 2026-10-04 03:24:03 CEST (date). Einzige Arbeitsdatei; vor jedem Schritt neu lesen.
  Gestrichenes bleibt stehen (~~so~~), offene Rueckfragen wandern unten mit.
- Gelesen vor dem ersten Abruf: KARTE.md (Fragen 1-5, E1-E5), RUNDE-36/REGEL.md (ganz, v. a. Abschn. 1, 2, 8),
  RUNDE-36/lambda-1/ERGEBNIS.md (ganz), RUNDE-37/RAUMZEIT-NETZ.md (ganz).
- Kennzeichen: [S] an der Quelle gelesen (WebFetch-Wiedergabe oder lokale Volltextkopie, jeweils vermerkt),
  [L] aus dem Gedaechtnis, [L?] unsicher, [ES] eigener Schluss, [M] Rechnung (Schreibtisch, keine Laeufe).
- Budget: hoechstens 15 WebFetch-Abrufe (nur arxiv.org/abs, export.arxiv.org/abs, arxiv.org/pdf). Keine Websuche.

## 0. Fund vor dem ersten Abruf (Gegensweep frueh): lokale Volltexte

Im Projekt liegen bereits Volltexte (aus RUNDE-22, von dortigen Agenten geladen; Treue der Textextraktion nicht
unabhaengig geprueft):
- RUNDE-22/dunkel-zeit/quellen/CDT-review-raw.txt: Ambjorn/Goerlich/Jurkiewicz/Loll, "Nonperturbative Quantum Gravity",
  Phys. Rep. 519 (2012) 127, arXiv:1203.3591 (Volltext, 351 KB; PDF daneben)
- RUNDE-22/geometrie-stand/hilfs/loll-1905.08669.txt: Loll, Review CQG 37 (2020) 013002, arXiv:1905.08669
- RUNDE-22/geometrie-stand/hilfs/ajl-hep-th-0404156.txt und ajl-hep-th-0505113.txt (AJL 2004/2005)
- Vorarbeit im Projekt: RUNDE-22/geometrie-stand/ERGEBNIS.md Abschn. 7 (B-C zweiter Ordnung, A-C erster Ordnung,
  C_dS/C_b [S Loll 2019]); RUNDE-35/graviton-netz-l/DOSSIER.md (CDT de Sitter, Abstracts).
- Folge: Die lokalen Volltexte zuerst lesen (kostet kein Abrufbudget), WebFetch fuer das, was dort fehlt.

## 1. Vorab-Ueberlegung vor jedem Abruf [ES/M, Schreibtisch, aus dem Gedaechtnis, ungeprueft]

- Hořava-Kinetik (2/kappa^2) N sqrt(g) (K_ij K^ij - lambda K^2). Minisuperraum g_ij = a^2 gamma_ij (S^3):
  K^i_j = (adot/(N a)) delta^i_j, also K_ij K^ij - lambda K^2 = 3 (1 - 3 lambda) (adot/(N a))^2.
- Relativ zu Einstein (lambda = 1) ist der kinetische Term des Skalenfaktors mit (3 lambda - 1)/2 multipliziert;
  Potentialterme (a, a^3) unveraendert.
- Eine konstante Umskalierung der Zeit (konstanter Lapse b, bzw. unbekannte Umrechnung Gitterzeit -> Eigenzeit)
  multipliziert Kinetik mit 1/b, Potential mit b. Also ist (3 lambda - 1)/2 in Zeiteinheit und G absorbierbar.
- **Vorab-Schluss [ES]:** Aus V(t) allein ist lambda nicht bestimmbar, solange 3 lambda - 1 > 0 und die Zeiteinheit
  nicht unabhaengig bekannt ist. V(t) unterscheidet nur das Vorzeichen von 3 lambda - 1 (relatives Vorzeichen
  Kinetik/Kruemmungsterm). Unsere Abschaetzung lambda = -1/2 (c = 1/5) liegt auf der anderen Seite (3 lambda - 1 < 0):
  Dort waere der Minisuperraum-Kinetikterm relativ zum Kruemmungsterm umgekehrt, die Loesung kein cos^3-Profil.
- **Pruefbar an der Quelle:** (i) Schreiben AGJL selbst, dass die V(t)-Wirkung lambda nicht festlegt? (ii) Welches
  Vorzeichen hat der gemessene kinetische Term, absolut und relativ zum Kruemmungsterm? (iii) Wird die Gitterzeit-
  Einheit (alpha, Delta) als frei/renormiert behandelt?

## 2. Abrufliste (WebFetch; Erwartung je Abruf vor dem Abruf eingetragen)

Zeitfenster = date-Stempel des Protokolleintrags mit der Erwartung (vorher) und des Eintrags mit dem Ergebnis (nachher),
Abschn. 8. Alle 15 Abrufe verbraucht. PDFs: Das WebFetch-Modell konnte keine PDF lesen; die Dateien wurden vom Werkzeug
gespeichert (tool-results/webfetch-*.pdf) und mit dem Read-Werkzeug seitenweise als Bild gelesen.

| Nr | Fenster (CEST) | URL | Was gelesen | Erwartung | Verstoss? |
|---|---|---|---|---|---|
| W1 | 03:29:00-03:29:40 | https://arxiv.org/abs/1302.6359 | Abstract | eingetroffen | nein |
| W2 | 03:29:00-03:29:40 | https://arxiv.org/abs/1110.5158 | Abstract | nicht eingetroffen | **ja** (lambda-Messung an Nicht-Volumen-Moden) |
| W3 | 03:29:00-03:29:40 | https://arxiv.org/abs/hep-th/0103186 | Abstract | eingetroffen | nein |
| W4 | 03:29:00-03:29:40 | https://arxiv.org/abs/1405.4585 | Abstract | eingetroffen | nein (Schaerfung E2) |
| W5 | 03:29:40-03:31:50 | https://arxiv.org/pdf/1110.5158 | Volltext S. 1-4 | eingetroffen (lambda < 1/2), Entropie nicht genannt | teilweise |
| W6 | 03:31:50-03:33:18 | https://arxiv.org/abs/1305.4702 | Abstract | nicht eingetroffen | **ja** (keine lambda-Bestaetigung) |
| W7 | 03:31:50-03:33:18 | https://arxiv.org/abs/1111.6634 | Abstract | eingetroffen | nein |
| W8 | 03:31:50-03:33:18 | https://arxiv.org/abs/1002.3298 | Abstract | eingetroffen | nein |
| W9 | 03:31:50-03:33:18 | https://arxiv.org/abs/0807.4481 | Abstract | eingetroffen | nein |
| W10 | 03:33:18-03:36:34 | https://arxiv.org/pdf/hep-th/0103186 | Volltext S. 1-5 | teilweise | **ja** (Heilung setzt indefinites Mass voraus) |
| W11 | 03:33:18-03:36:34 | https://arxiv.org/pdf/1405.4585 | Volltext S. 1-6, 8-13 | eingetroffen | nein |
| W12 | 03:33:18-03:36:34 | https://arxiv.org/abs/2504.11047 | Abstract | eingetroffen | nein |
| W13 | 03:36:34-03:38:58 | https://arxiv.org/pdf/1305.4702 | Volltext S. 2-4, 11-22, 28-30 | teilweise | **ja** (Lapse vor Variation fest = Zusatzfreiheitsgrad) |
| W14 | 03:36:34-03:38:58 | https://arxiv.org/pdf/1302.6359 | Volltext S. 1-8 | eingetroffen, plus lambda < 1 | teilweise (neu: positiv definites Regime) |
| W15 | 03:40:13-03:41:21 | https://arxiv.org/abs/1605.09618 | Abstract | nicht eingetroffen | **ja** (Blaetterung hinterlaesst in Standard-2D-CDT eine Spur) |

## 3. Lokale Lesungen (kein Abrufbudget; Erwartung vor dem Lesen)

| Nr | Zeit (date) | Datei / Stelle | Erwartung | Verstoss? |
|---|---|---|---|---|
| L1 | 03:24:42-03:26:45 | RUNDE-22/dunkel-zeit/quellen/CDT-review-raw.txt (AGJL 2012), Z. 800-850, 5604-5900, 6236-6300, 7105-7245, 7578-7612, 3100-3150, Literatur | Vorzeichen-Satz, Lifshitz-Lesart | **ja**: A-C = Kinetik-Koeffizient durch null; Rest eingetroffen |
| L2 | 03:26:56-03:27:58 | RUNDE-22/geometrie-stand/hilfs/loll-1905.08669.txt, Z. 664-990, 1076-1240, 1373-1535, 1710-1790, Literatur | Ordnung der Uebergaenge, kein inhomogenes lambda | **ja**: negatives effektives Kinetikvorzeichen in C_b |

## 4. Befunde je Erwartung (Stand 03:43)

- E1 (V(t) wie Einstein, mit "falschem" Vorzeichen): **teilweise.** Form ja (Review Z. 6272 [S]); Vorzeichen NEIN: positiv,
  entropisch (Review Z. 5776-5779; Budd S. 2 [S]); lambda = 1 aus V(t) nicht bestimmbar (Review 9.1; RG S. 11 [S]).
- E2 (Horava-artige Bereiche, ein Uebergang zweiter Ordnung): **eingetroffen**, mit Zusatz: B-C_b zweiter, C_b-C_dS zweiter
  oder hoeherer Ordnung (Loll S. 22, 27 [S]); anisotrope Skalierung nur als Deutung (RG-Abstract [S]), z ~ 1 tief in C,
  nahe B-C nicht gemessen (Review Z. 5871 [S]); Kinetik-Koeffizient geht an A-C durch null, in C_b negativ (Loll S. 25-27 [S]).
- E3 (2D-CDT = projizierbare 2D-HL): **eingetroffen** (AGSW [S]), genauer: lambda < 1, Lambda > 0 (S. 8 [S]).
- E4 (keine lambda-Messung fuer inhomogene Moden in 4D): **eingetroffen nach Recherchestand** (in 4D nichts gefunden;
  Budd/Loll S. 3 [S]: Form-Observablen in 4D "not straightforward"), aber in 2+1 gibt es zwei Messungen (Budd 2011 [S]):
  lambda_eff < 1/2. Regel 7 nicht erfuellbar (R1).
- E5 (Bewegungsenergie wesentlich aus der Summe ueber Triangulierungen; c = 1/5 trifft CDT nicht): **erste Haelfte
  eingetroffen** (Review, Loll, 2D "nothing but entropy" [S]); **zweite Haelfte nicht eingetroffen**: Das effektive
  CDT-Regime (2D lambda < 1, 2+1 lambda < 1/2) ist dasselbe positiv definite Regime wie unser c = 1/5 (lambda = -1/2) [ES].

## 5. Erwartungsverstoesse (protokolliert, mit korrigierter Erwartung)

1. **V1 (L1, Budd S. 2):** CDT-Kinetik des Raumvolumens ist positiv, nicht "falsch wie Einstein". Korrigiert: Gesamt-
   vorzeichen umgekehrt, Entropie liefert das positive Vorzeichen, die nackte Einstein-Wirkung das negative.
2. **V2 (W2, W5):** Es gibt eine lambda-Messung jenseits von V(t), in 2+1 (Torus-Modul, lokale Randfluktuationen), mit
   lambda_eff zwischen ~0,03 und ~0,49 < 1/2. Korrigiert: E4 gilt nur fuer 4D; in 2+1 ist die Frage gestellt und vorlaeufig
   beantwortet (positiv definit, nicht Einstein).
3. **V3 (W6, W13):** Die angekuendigte Langfassung bringt die lambda-Messung nicht; Formdynamik "to appear". Korrigiert:
   V2 ruht auf einer Tagungsarbeit mit zwei uneinigen Methoden.
4. **V4 (W13):** Budd/Loll modellieren CDT-Eigenzeit als Lapse = 1 vor der Variation: Hamilton-Bedingung faellt, lokaler
   Zusatzfreiheitsgrad. Korrigiert: Die Literatur kennt unseren Fall "Netz mit aeusserer Uhr" als Deutungsoption fuer CDT.
5. **V5 (W10):** Die Dasgupta/Loll-Heilung des konformen Vorzeichens verlangt ein Mass im indefiniten Bereich (C < -2/d,
   d. h. lambda > 1/d). Korrigiert: Die richtige DeWitt-Struktur ist dort Voraussetzung, nicht Ergebnis.
6. **V6 (L1, L2):** Der Kinetik-Koeffizient des Volumens ist im Phasendiagramm frei verschiebbar: positiv in C_dS, null an
   A-C, effektiv negativ in C_b. Korrigiert: Das Vorzeichen des konformen Modus ist in CDT eine Phaseneigenschaft, keine
   Symmetriefolge.
7. **V7 (W15):** In Standard-2D-CDT schraenkt die Blaetterung den Konfigurationsraum ein und hinterlaesst eine Spur im
   Kontinuum (Glaser u. a.). Korrigiert: "Schichtung = Artefakt" (Loll 2019) gilt nicht in 2D; Moderator Dimension.

## 6. Offene Rueckfragen (wandern mit)

- R1: Regel 7 (24-Monats-Suche) ist ohne Websuche nicht erfuellbar. Jede negative Aussage ("keine Messung") lautet
  deshalb hoechstens "nach Recherchestand nicht belegt".

## 7. Gestrichenes und Berichtigungen

- Berichtigung 03:43 zu L1 (Zeilenangaben der Review-Textdatei, per grep -n nachgeprueft): "Up to an overall sign" steht
  in Z. 6272 (nicht 6263-6283 als Fundstelle des Satzes); "eventually go through zero" Z. 5781; "This is precisely what we
  observe!" Z. 5800; A-C erster Ordnung Z. 5801-5804 (nicht 5650-5652; dort steht nur die allgemeine Lifshitz-Aussage);
  B-C zweiter Ordnung Z. 5805-5806; d_t ~ 4, d_s ~ 3 Z. 5856, "Delta > 0.3" Z. 5871; "trivial parameter" Z. 5812;
  "residual ambiguity" Z. 7116; "fix the ratio" Z. 7199; "better data are required" Z. 7223.
- ~~L1: "A-C erster Ordnung, Z. 5650-5652"~~ (s. Berichtigung).
- Berichtigung 03:50 zu L2 (Seitenmarken der Loll-Textdatei: 16 bei Z. 686, 18 bei Z. 768, 19 bei Z. 818, 21 bei Z. 915,
  22 bei Z. 995, 25 bei Z. 1143, 27 bei Z. 1238, 33 bei Z. 1531):
  - ~~"S. 18-19 (Z. 669-685)"~~ -> S. 16;
  - ~~"S. 20 (Z. 784-796)"~~ -> S. 19.
  - Die uebrigen Seitenangaben in L2 (21-22, 25, 27, 33) stimmen.
- Selbstanzeige 03:49: Zum Finden der Seitenmarken einmal awk benutzt (nur lesend). Der Auftrag erlaubt nur Read, Write,
  Edit, grep, sed, jq und date; danach mit grep nachgeprueft. Im Dossier unter Selbstanzeigen Nr. 7 vermerkt.

## 8. Protokoll (chronologisch angehaengt; Zeiten per date)

- 2026-10-04 03:24:42 CEST: LOKAL L1 vor dem Lesen. Datei RUNDE-22/dunkel-zeit/quellen/CDT-review-raw.txt (AGJL 2012, arXiv:1203.3591), per grep.
  Erwartung: Der Review enthaelt die V(t)-Wirkung mit positivem kinetischem Term und den Satz, sie sei Einsteins
  (Hartle-Hawking-)Minisuperraum bis auf das Gesamtvorzeichen; dazu einen Hořava-Abschnitt, der das Phasendiagramm
  als Lifshitz-Diagramm liest und Delta (Asymmetrie) mit Anisotropie verbindet; lambda fuer inhomogene Moden fehlt.
- 2026-10-04 03:26:45 CEST: LOKAL L1 Ergebnis (AGJL 2012 Review, lokale Textkopie; Zeilennummern der Textdatei):
  - Z. 6263-6283 [S]: Gemessene Wirkung S = (1/24 pi G) int dt sqrt(g_tt) (g^tt V3dot^2/V3 + k2 V3^(1/3) - lambda V3),
    "Up to an overall sign, this is precisely the Einstein-Hilbert action for the scale factor" (Hartle/Hawking [22]).
    -> Form wie Einstein: JA. Vorzeichen: kinetischer Term POSITIV, Gesamtvorzeichen umgekehrt. **Verstoss gegen E1-Teil
       "falsches Vorzeichen wie in Einsteins Theorie".**
  - Z. 5775-5779 [S]: "well inside phase C we have a positive kinetic term for the scale factor. This term comes from
    entropic contributions", die nackte Wirkung liefert einen negativen kinetischen Term. Fussnote 21: Kur seit [94]
    (Ambjorn/Dasgupta/Jurkiewicz/Loll, hep-th/0201104); Kontinuum ueber Faddeev-Popov-Mass [95] (Dasgupta/Loll,
    hep-th/0103186). -> E5 erste Haelfte gestuetzt (fuer den homogenen Modus).
  - Z. 5779-5785 [S]: Mit wachsendem kappa0 sinkt der Koeffizient des kinetischen Terms, "eventually go through zero";
    im Lifshitz-Bild d2 -> 0, Uebergang (meist erster Ordnung) in die oszillierende Phase A, "This is precisely what we
    observe!" -> **neu (Verstoss gegen meine Vorstellung, E2 betreffend):** Der A-C-Uebergang ist dort, wo der
    Kinetik-Koeffizient des Skalenfaktors durch null geht. [ES] In Horava-Sprache: effektives (1 - 3 lambda)/gamma
    wechselt das Vorzeichen, d. h. ein Durchgang durch die entartete DeWitt-Metrik (lambda = 1/3), nicht durch lambda = 1.
  - Z. 5806-5807, 5650-5652 [S]: B-C "appears to be of second order"; A-C erster Ordnung. Z. 5838-5880 [S]: z = d_s/(d_t - 1);
    fuer Delta > 0,3 d_t ~ 4, d_s ~ 3, also z ~ 1; fuer kleineres Delta keine belastbare Aussage.
  - Z. 5812-5825 [S]: Delta "in some ways a trivial parameter", definiert nur a_t/a_s um; tief in C qualitativ
    unabhaengig von Delta; nahe B-C ungenau, "entropic contributions mix with the bare action terms".
  - Z. 7113-7205 [S], Abschn. 9.1: "residual ambiguity in the interpretation of the time coordinate"; alternative
    Hořava-Wirkung (252) mit lambda und gamma; Minisuperraum (253) mit 3(1 - 3 lambda) adot^2/a^2 - 6 gamma/a^2;
    "not been able to determine the constant k2~ ... which would enable us to fix the ratio (1 - 3 lambda)/2 gamma";
    Z. 7225-7228: "better data are required to discriminate between the actions (229) and (253)".
    -> Meine Vorab-Ueberlegung (Abschn. 1) an der Quelle bestaetigt: V(t) legt lambda nicht fest.
  - Fussnote 27 [S]: lambda steht in der DeWitt-Metrik; Text: "positive definite for lambda < 1/3, indefinite for
    lambda = 1/3 and negative definite for lambda > 1/3". [M] Das ist so falsch: G(h,h) = |h^T|^2 + (1/3 - lambda) h^2,
    also positiv definit fuer lambda < 1/3, entartet bei 1/3, indefinit (eine negative Richtung, Spur) fuer lambda > 1/3.
    Ob Fehler im Original oder in der Textextraktion: offen (PDF nicht geprueft). Fuer uns folgenlos.
  - Fussnote 27 [S]: "The role of lambda in three-dimensional CDT quantum gravity has been analyzed in detail in [98]",
    [98] = T. Budd, "The effective kinetic term in CDT", arXiv:1110.5158; "T. Budd and R. Loll, to appear".
    -> Kandidat fuer Frage 4 und 5. [L?] Budd/Loll spaeter: "Exploring torus universes in CDT" (arXiv-Nr. unsicher).
  - Z. 810-815 [S]: Gitter "may a priori have both Hořava-Lifshitz and 'isotropic' fixed points".
- 2026-10-04 03:26:56 CEST: LOKAL L2 vor dem Lesen. RUNDE-22/geometrie-stand/hilfs/loll-1905.08669.txt (Loll 2019 Review), per grep.
  Erwartung: nennt C_dS/C_b, B-C und C_dS-C_b als Uebergaenge zweiter bzw. hoeherer Ordnung, Hořava nur kurz,
  keine lambda-Messung fuer inhomogene Moden in 4D; Budd/Loll-Torus vielleicht als Randnotiz.
- 2026-10-04 03:27:58 CEST: LOKAL L2 Ergebnis (Loll 2019, lokale Textkopie; Seitenzahlen der Vorlage, Zeilen der Textdatei):
  - S. 18-19 (Z. 669-685) [S]: Schichtung ist nach Loll wohl Gitterartefakt; aehnelt "superficially" der Hořava-
    Blaetterung, bricht aber keine Diffeomorphismus-Symmetrie, "because the formulation does not have this symmetry to
    start with"; Wirkung ist "just the standard Einstein action"; Hořava-Wirkung explizit nur in 3D versucht [61]
    (arXiv:1111.6634); verallgemeinertes CDT ohne bevorzugte Blaetterung (3D) reproduziert de-Sitter-Form.
  - S. 20 (Z. 784-796) [S]: Delta haengt an alpha (Laengenverhaeltnis Zeit-/Raumkanten), a priori nicht ausgezeichnet;
    im interessanten Bereich "Delta is an independent coupling constant, which may need to be fine-tuned".
  - S. 21-22 (Z. 895-985) [S]: A-C_dS erster Ordnung; B-C_b zweiter Ordnung (Shift-Exponent, Binder-Kumulanten, N4 bis
    160k), bestaetigt durch [68] (arXiv:1610.05245); Doppelpeak erklaert ueber den Entropiefaktor.
  - S. 24-25 (Z. 1098-1131) [S]: Leff = (1/Gamma)(n - m)^2/(n + m) + mu ((n+m)/2)^(1/3) - lambda (n+m)/2.
    "the kinetic term ... vanishes gradually as one approaches the A-C transition ... and is zero at the transition";
    Deutung: Entropie verhindert in C die konforme Divergenz, mit wachsendem kappa0 dominiert der "negative kinetic term
    of the conformal mode in the bare action" [54, 78]. Quelle der Messung [77] = arXiv:1403.5940.
  - S. 26-27 (Z. 1160-1200) [S]: In C_b spaltet der Kinetik-Kern in zwei Gaussglocken; fuer grosse Volumina folgt ein
    "effective kinetic term with a negative sign", von [67] (arXiv:1503.08580) und [79] als skalenabhaengiger
    Signaturwechsel gedeutet; Loll: "rather far-reaching conjecture", da das Volumen nur einer von unendlich vielen
    Moden ist. C_b-C_dS-Uebergang bei Delta in [0,25; 0,3] (kappa0 = 2,2).
  - S. 32-33 (Z. 1478-1528) [S]: 3-Torus: Kinetikterm "identical, including the value of Gamma within measuring
    accuracy" (Gamma ~ 26,3), n^(1/3)-Term fehlt (wie flacher Minisuperraum), Zusatz mu n^(-gamma), gamma = 1,16 +- 0,02.
  - S. 37 Fn. 23 (Z. 1720-1721) [S]: RG-Studie [85] (arXiv:1405.4585) deutet die Messungen "in the more general framework
    of Hořava-Lifshitz gravity, allowing also for a 'deformed' de Sitter universe"; Linien konstanter Physik ueber omega.
  - Bewertung gegen L2-Erwartung: bestaetigt (Ordnung der Uebergaenge, keine inhomogene lambda-Messung erwaehnt).
    Neu und erwartungswidrig: das negative effektive Kinetikvorzeichen in C_b (s. Abschn. 5).
- 2026-10-04 03:29:00 CEST: Nebenfund vor Abruf: RUNDE-22/geometrie-stand (02.10.2026) hat eine 24-Monats-Suche (arXiv-API, OpenAlex) zu CDT/EDT
  gemacht, nicht auf lambda/Hořava gerichtet. Treffer mit Bezug zu inhomogenen Groessen: Maas/Plaetzer/Pressler 2025,
  "Hints for a geon from CDT", arXiv:2504.11047 (Kruemmungskorrelatoren in 4D-CDT wie ein massiver Zustand, dort [L?]).
  Fuer R1 heisst das: Teilabdeckung von Regel 7, aber keine gezielte lambda-Suche.
- WebFetch-Stapel 1, Erwartungen VOR dem Abruf:
  - W1 https://arxiv.org/abs/1302.6359 (Ambjorn/Glaser/Sato/Watabiki 2013): 2D-CDT ist im Kontinuum gleich der
    quantisierten projizierbaren 2D-Hořava-Lifshitz-Gravitation (gleicher Hamiltonoperator); lambda spielt in 1+1 keine
    eigene Rolle.
  - W2 https://arxiv.org/abs/1110.5158 (Budd 2011): In 3D-CDT entsteht der kinetische Term des Volumens aus der
    Abzaehlung (Entropie); Budd bestimmt ein effektives lambda oder zeigt, dass es aus dem Volumen nicht ablesbar ist.
  - W3 https://arxiv.org/abs/hep-th/0103186 (Dasgupta/Loll 2001): Die Faddeev-Popov-Determinante der Eigenzeit-Eichung
    kehrt das Vorzeichen des konformen kinetischen Terms um (stoerungstheoretisch um flachen Raum); Bezug auf den
    DeWitt-Parameter moeglich, aber nicht sicher.
  - W4 https://arxiv.org/abs/1405.4585 (RG-Fluss in CDT 2014): RG-Fluss aus V(t)-Profil und Fluktuationen, Linien
    konstanter Physik, Hořava-Deutung mit "deformiertem" de Sitter; kein lambda-Wert im Abstract.
- 2026-10-04 03:29:40 CEST: Stapel 1 Ergebnisse (Abrufe 1-4 von 15, WebFetch-Wiedergabe der abs-Seite):
  - W1 1302.6359 [S Abstract]: bestaetigt. "this continuum Hamiltonian is the one obtained by quantizing two-dimensional
    projectable Horava-Lifshitz gravity" (Ambjorn, Glaser, Sato, Watabiki; PLB, 26.02.2013). Zu lambda nichts.
  - W2 1110.5158 [S Abstract]: **VERSTOSS.** Budd (J. Phys. Conf. Ser. 360, 012038, 2012): In 2+1-CDT sprechen zwei
    voneinander unabhaengige Messungen dafuer, dass die effektive Kinetik "given by a modified Wheeler-De Witt metric"
    ist: (a) der Modulparameter bei Torus-Raumtopologie, (b) "local metric fluctuations close to a fixed spatial
    boundary". Das sind Nicht-Volumen-Moden, (b) sogar lokal/inhomogen. Erwartet hatte ich nur Entropie-Herkunft des
    Volumen-Kinetikterms oder "nicht ablesbar". -> Voller Zyklus: Volltext (W5).
  - W3 hep-th/0103186 [S Abstract]: bestaetigt. Eigenzeit-Eichung, "divergence due to the conformal modes of the metric
    is cancelled non-perturbatively by a Faddeev-Popov determinant contributing to the effective measure" (unter Annahmen
    zur Renormierung; 3D-Stoerungsrechnung als Illustration). DeWitt-Parameter im Abstract nicht erwaehnt.
  - W4 1405.4585 [S Abstract]: im Wesentlichen bestaetigt, mit Schaerfung fuer E2: "the second-order phase transition
    line ... can be interpreted as a UV phase transition line if we allow for an anisotropic scaling of space and time".
- W5 Erwartung VOR Abruf, https://arxiv.org/pdf/1110.5158 (Budd, Volltext): gemessenes effektives lambda in 2+1 liegt
  unter 1/2 (positiv definite DeWitt-Metrik, passend zum entropisch umgedrehten Volumen-Vorzeichen), also weit weg vom
  Einstein-Wert 1; Entropie wird als Herkunft genannt.
- 2026-10-04 03:31:50 CEST: W5 Ergebnis (Abruf 5 von 15; WebFetch-Modell las die PDF nicht, die PDF lag aber als Datei vor und wurde mit dem
  Read-Werkzeug als Seitenbild gelesen: 4 Seiten, vollstaendig) [S Volltext]:
  - S. 2, Gl. (2): 2+1-Kugel S_eff[V] = int dt (c0 Vdot^2/V - c1 V), c0, c1 > 0; "The only difference is an overall
    minus sign, which ensures that for fixed 3-volume (2) is bounded below while the Einstein-Hilbert one is not."
  - S. 2, Gl. (3): Wheeler-DeWitt-Metrik "positive definite on traceless deformations but negative definite on conformal
    deformations"; daher sei (3) "not a suitable ansatz for an effective action for CDT".
  - S. 2, Gl. (4): G_lambda^abcd = (1/2)(g^ac g^bd + g^ad g^bc) - lambda g^ab g^cd, "positive definite in the regime
    lambda < 1/2, while in general relativity we have the value lambda = 1".
  - S. 3, Gl. (5): Torus: kappa int dt ((1/2 - lambda) Vdot^2/V + (1/(2A[g])) (tau1dot^2 + tau2dot^2)/tau2^2); lambda aus
    den Korrelationen <V V> und <tau tau> im Verhaeltnis zur direkt gemessenen A[g].
  - S. 3, Gl. (6): an fester Rand-Triangulierung: Metrikfluktuationen ~ delta(x - y) G^lambda_abcd (inverse Metrik);
    gemessen ueber die extrinsische Kruemmung N(e) (Tetraederzahl an der Kante), Korrelation "only correlate locally".
    Selbstvorbehalt Budd: Ersetzung g(Delta t) -> K_ab "might have a systematic effect on lambda".
  - S. 4, Abb. 3 (abgelesen, Genauigkeit ~ 0,02): Minisuperraum/Torus (blau) lambda ~ 0,03 bei k0 ~ 1,5 bis ~ 0,45 bei
    k0 ~ 5; extrinsische Kruemmung (rot) ~ 0,37 bei k0 ~ 0,5 bis ~ 0,49 bei k0 ~ 5,5. ALLE Werte < 1/2.
  - S. 4, Diskussion: positiv definites G_lambda (lambda < 1/2) gibt "qualitative agreement"; Methoden weichen ab ("quite
    subtle"); "as we approach the phase transition in CDT, corresponding to a critical coupling k0 ~ 5.6, lambda increases
    to 1/2 at which point G_lambda becomes degenerate." Ausfuehrliche Fassung angekuendigt ("will appear soon").
  - Entropie als Herkunft: im Text NICHT genannt (meine W5-Erwartung insoweit nicht erfuellt; Rest eingetroffen).
  - [M] Umrechnung in unser c (Impulsbild) fuer d Raumdimensionen: c = lambda/(d lambda - 1). d = 2: GR lambda = 1 -> c = 1;
    Budd lambda 0,03 bis 0,49 -> c ~ -0,03 bis ~ -24; unser Kanten-Netz lambda = -1/2 -> c = 1/4 (d = 2) bzw. 1/5 (d = 3).
  - [ES] Zwei Regime der DeWitt-Metrik: lambda < 1/d positiv definit (Budd-CDT effektiv, unser Kanten-Netz), lambda > 1/d
    indefinit (Einstein lambda = 1). Eine Summe positiver Kanten-Bewegungsenergien liegt zwangslaeufig im ersten Regime.
- Stapel 2, Erwartungen VOR dem Abruf:
  - W6 https://arxiv.org/abs/1305.4702 (ID aus dem Gedaechtnis, unsicher; gesucht Budd/Loll "Exploring torus universes in
    CDT"): ausfuehrliche Fassung von W5; lambda_eff < 1/2 in 2+1 bestaetigt, steigt mit k0. Falls ID falsch: anderes Papier.
  - W7 https://arxiv.org/abs/1111.6634 (Anderson/Carlip/Cooperman/Hořava/Kommu/Zulkowski): Hořava-artige Terme in 2+1-CDT
    eingebaut, neue Phase oder Spektraldimension; kein lambda-Wert im Abstract.
  - W8 https://arxiv.org/abs/1002.3298 (CDT meets Hořava-Lifshitz): wie Review Abschn. 7.5: Lifshitz-Phasendiagramm, B-C
    vermutlich zweiter Ordnung, Anisotropie z; kein lambda-Wert.
  - W9 https://arxiv.org/abs/0807.4481 (Nonperturbative quantum de Sitter universe): de-Sitter-Profil und Fluktuationen
    durch Minisuperraum-Wirkung beschrieben, G und Groesse in Planck-Laengen; Vorzeichen/Entropie im Abstract nicht erwaehnt.
- 2026-10-04 03:33:18 CEST: Stapel 2 Ergebnisse (Abrufe 6-9 von 15):
  - W6 1305.4702 [S Abstract]: ID richtig (Budd/Loll, PRD 88, 024015, 2013). **VERSTOSS (W6):** Die angekuendigte
    ausfuehrliche Fassung berichtet im Abstract KEINE lambda-Bestimmung: Fokus Skalenfaktor, "qualitatively new behaviour",
    neue Randbedingungen, Minisuperraum "partial agreement"; "Apart from setting the stage for the analysis of shape
    dynamics on the torus". -> Die lambda-Messung aus W5 bleibt nach Recherchestand eine Tagungsarbeit (2011), zwei
    Methoden uneinig, nicht in einer begutachteten Langfassung bestaetigt (Volltext 1305.4702 nicht gelesen).
  - W7 1111.6634 [S Abstract]: bestaetigt. Diskrete Kruemmungsquadrat-Terme der projizierbaren 2+1-HL-Gravitation in die
    CDT-Wirkung eingebaut (Potentialseite, nicht lambda); bekannte und neue Phasen; Uebergang zwischen zeitabhaengiger
    de-Sitter-artiger und zeitunabhaengiger Phase; "preliminary evidence" fuer Konsistenz mit HL-Loesungen.
  - W8 1002.3298 [S Abstract]: bestaetigt. "striking resemblance with the generic Lifshitz phase diagram"; CDT als
    moeglicher gemeinsamer Rahmen "for anisotropic as well as isotropic theories". Kein lambda.
  - W9 0807.4481 [S Abstract]: bestaetigt. Effektive Wirkung "reconstructed uniquely from Monte Carlo data"; Vorzeichen
    und Entropie im Abstract nicht erwaehnt (stehen im Review, L1).
- LOKAL L2b (Loll 2019, S. 27, Z. 1219-1229) [S]: C_b-C_dS: "strong evidence that the Cb-CdS transition is of second or
  higher order [80]"; Delta_crit = 0,35 +- 0,01 bei kappa0 = 2,2, N41 = 160k; in C_b "modulation" mit Periode Delta t = 2
  (Koordinationszahl springt zwischen benachbarten Schichten). Erwartung E2 (zweite Ordnung) damit fuer B-C_b und C_b-C_dS
  gedeckt.
- Stapel 3, Erwartungen VOR dem Abruf:
  - W10 https://arxiv.org/pdf/hep-th/0103186 (Dasgupta/Loll, Volltext; PDF lokal mit Read lesen): Rechnung mit
    DeWitt-Supermetrik; die FP-Determinante der Eigenzeit-Eichung ueberkompensiert den konformen Kinetikterm; das haengt
    nicht vom DeWitt-Parameter ab bzw. setzt den Einstein-Wert voraus.
  - W11 https://arxiv.org/pdf/1405.4585 (RG-Fluss, Volltext): aus V(t) zwei Groessen (omega, Breite); omega als Hořava-
    Anisotropie gedeutet (Zeit-/Raum-Skalierung, Kombination (1 - 3 lambda)/gamma), lambda nicht einzeln bestimmt.
  - W12 https://arxiv.org/abs/2504.11047 (Maas/Plaetzer/Pressler 2025): Kruemmungs-Zweipunktkorrelatoren in 4D-CDT fallen
    exponentiell (massiv); keine Graviton- oder lambda-Bestimmung.
- 2026-10-04 03:36:34 CEST: Stapel 3 Ergebnisse (Abrufe 10-12 von 15; PDFs per Read als Seitenbild gelesen):
  - W10 hep-th/0103186 Volltext S. 1-5 [S]: S. 3: konformer Faktor g = e^(2 lambda) g-bar, kinetischer Term
    "contribute[s] with the wrong sign" (hier lambda = konformer Faktor, NICHT Horavas lambda). S. 4: im Gitter gibt es
    Geometrien mit "large and negative Euclidean action", in 3D aber grosser Kopplungsbereich ohne Rolle: "a win of
    'entropy over energy'". S. 5: Im Gitter "there is no gauge-fixing - proper time is simply selected from the
    combinatorial data". **Teil-VERSTOSS (W10):** Der Mechanismus (nach Mazur/Mottola) "requires that C < -2/d for the
    constant C appearing in the DeWitt measure, exactly the range where the DeWitt metric is indefinite"; einziger
    ausgezeichneter Wert C = -2. [M] Mit G_C = (1/2)(gg + gg) + (C/2) g g ist lambda = -C/2, also C < -2/d <=> lambda > 1/d,
    C = -2 <=> lambda = 1. Die Heilung setzt also ein Einstein-artiges (indefinites) Mass VORAUS, liefert lambda nicht.
  - W11 1405.4585 Volltext S. 1-6, 8-13 [S]: S. 2: CDT hat "no residual diffeomorphism invariance, which therefore
    cannot be broken either"; 3D-CDT ohne Blaetterung bestaetigt Kernergebnisse. S. 4: Delta ist nackt nur Laengen-
    verhaeltnis, "in the effective quantum action Delta will appear as a coupling constant ... the measure ... becomes as
    important as the classical action". S. 10, Gl. (13)/(14): projizierbare HL-Wirkung K_ij K^ij - lambda K^2 + delta~ R;
    Minisuperraum kappa/kappa~ = (1 - 3 lambda)/3. S. 11, Gl. (15)-(19): Loesung ist eine deformierte 4-Sphaere (Zeit-
    ausdehnung pi chi R, "Unless chi equals its general relativistic value chi = 1"), chi^2 = 9(2 pi^2)^(2/3)/delta;
    "only the ratio of omega and chi^(3/4) appears". S. 12: Annahme konstanter Zeit-/Raum-Einheit = festes omega/chi^(3/4).
    -> bestaetigt die Vorab-Ueberlegung: lambda steckt nur in chi und ist mit der Zeiteinheit entartet. [M] chi^2 =
    (1 - 3 lambda)/(2 delta~), Einstein (1, -1) gibt 1.
  - W12 2504.11047 [S Abstract]: bestaetigt. Maas/Plaetzer/Pressler, PLB 879 (2026) 140600: Kruemmungs-Korrelatoren in
    4D-CDT "consistent with a massive state ... over a certain distance window", "at most a hint". Keine lambda-Bestimmung.
- Stapel 4, Erwartungen VOR dem Abruf:
  - W13 https://arxiv.org/pdf/1305.4702 (Budd/Loll 2013, Volltext, Einleitung und Schluss): erwaehnt die lambda-Messung
    von 2011 als vorlaeufig, kuendigt Formdynamik fuer spaeter an; kein neuer lambda-Wert.
  - W14 https://arxiv.org/pdf/1302.6359 (2D-CDT = 2D-HL, Volltext): 2D-HL-Kinetik ist (1 - lambda) K^2; die Gleichheit
    braucht lambda != 1 (bei 1 verschwindet der Term), lambda wird in die Kopplungen absorbiert.
- 2026-10-04 03:38:58 CEST: Stapel 4 Ergebnisse (Abrufe 13-14 von 15; PDFs per Read gelesen):
  - W14 1302.6359 Volltext S. 1-8 [S]: Gl. (3) HL-Wirkung (1/kappa) int sqrt(g) N [(K_ij K^ij - lambda K^2) + R - 2 Lambda],
    "If lambda = 1 one recovers GR"; Gl. (6) Hamilton-Dichte (kappa/sqrt g)(pi^ij pi_ij - (lambda/(d lambda - 1)) pi^2) - ...
    -> genau unsere Zuordnung c = lambda/(d lambda - 1) [S]. Gl. (9): 1+1: (1 - lambda) K^2 - 2 Lambda. S. 8: "It is
    projectable 2d HL gravity with lambda < 1 and Lambda > 0". Fuer lambda > 1 hat der kinetische Term "the wrong sign
    compared to an ordinary kinetic term (precisely as in ordinary GR)"; klassisch kann man das Gesamtvorzeichen von S
    umdrehen, "However, when coupling to matter and in higher dimensions where one might also have transverse physical
    field degrees of freedom one might not have that option. This needs to be analyzed."
    -> W14-Erwartung eingetroffen (lambda != 1 noetig); neu: CDT sitzt bei lambda < 1, also im positiv definiten Regime
    (lambda < 1/d mit d = 1), wie Budd in 2+1 (lambda < 1/2). Die Autoren benennen selbst den Unterscheidungspunkt:
    Querfreiheitsgrade (TT) in hoeheren Dimensionen.
  - W13 1305.4702 Volltext S. 2-4, 11-17 [S]: S. 3: in 4D "it does not appear straightforward to isolate observables which
    are sensitive to global shape"; Vorsicht bei Uebertrag 3D -> 4D; entropische Masseffekte in 4D. S. 4: Formdynamik in
    "companion paper [9]". **VERSTOSS (W13):** S. 16-17: Budd/Loll modellieren die CDT-Eigenzeit als Einstein-Wirkung mit
    VOR der Variation festgelegtem Lapse N = 1, "without adding the (then missing) Hamiltonian constraint"; dann ist
    delta S/delta N "no longer required to vanish", man gewinnt einen freien Parameter; Fn. 6: "There is an infinite-
    dimensional family of classical solutions due to the presence of a local degree of freedom." S. 17: Gitter-"edge
    distance" und lokale Eigenzeit sind "at a local, microscopic level" nicht gleichzusetzen, nur global (de Sitter).
    -> Das ist woertlich unser Fall "Raum-Netz mit aeusserer Uhr" (REGEL.md Abschn. 8): Zeit-Umbenennung fehlt,
    Hamilton-Bedingung faellt, ein lokaler Zusatzfreiheitsgrad entsteht. Abstract: "partial agreement" mit Minisuperraum.
    lambda-Messung von 2011 auf den gelesenen Seiten nicht erwaehnt.
- 2026-10-04 03:40:13 CEST: Lokal weitergelesen (kein Abruf):
  - 1305.4702 S. 18-22, 28-30 [S]: S. 19: Minisuperraum-Wirkung (N = 1) auf Loesungen positiv "despite the negative kinetic
    term for the volume in (12)". S. 20: fuer k0 -> k0* ~ 5,6 kollabiert der Anteil der 22-Simplizes, Schichten
    "effectively decouple", Profil wird flach. S. 21: bei l0 != l1 fehlt die vorhergesagte Symmetrie; "spatial geometries
    at small time t are oblivious to the final boundary conditions". S. 22: moegliche Gruende (a) Grenzfall von CDT "could
    be genuinely different" vom verallgemeinerten Minisuperraum, (b) zu klein, (c) falsche Randzuordnung; "Forthcoming
    work will analyze the contribution from the moduli parameters to the effective action [9]"; [9] = "T.G. Budd and
    R. Loll, to appear" (ohne arXiv-Nr.). [15] = Jordan/Loll, arXiv:1305.4582 (ohne bevorzugte Blaetterung).
    [ES] k0* ~ 5,6 ist derselbe Wert, bei dem Budd 2011 lambda -> 1/2 fand: Entartung der DeWitt-Metrik faellt mit dem
    Entkoppeln der Schichten zusammen (beide Angaben [S], Verknuepfung [ES]).
  - Review Z. 3139-3147 [S]: 2D: "the theory is nothing but entropy of geometries", Partitionsfunktion ist die erzeugende
    Funktion der Zahl der Geometrien; auch in 4D gibt es einen "entirely entropic expression" (Gl. 195).
    -> Frage 5 in 2D eindeutig: Die Bewegungsenergie (L Pi^2 in AGSW Gl. 17/26) kommt rein aus der Abzaehlung.
- W15 Erwartung VOR Abruf, https://arxiv.org/abs/1605.09618 (ID aus dem Gedaechtnis, unsicher; gesucht Glaser/Sotiriou/
  Weinfurtner, extrinsische Kruemmung in 2D-CDT): ein expliziter K^2-Term in der 2D-CDT-Wirkung aendert den
  Kontinuumslimes nicht (irrelevant), die Kinetik bleibt entropisch bestimmt. Falls ID falsch: anderes Papier.
- 2026-10-04 03:41:21 CEST: W15 Ergebnis (Abruf 15 von 15; Budget erschoepft) [S Abstract]: ID richtig. Glaser/Sotiriou/Weinfurtner, PRD 94, 064014
  (2016): CDT-Quantisierung direkt auf 2D-HL angewandt; Kontinuums-Hamiltonoperator "matches exactly" den kanonisch
  quantisierten HL-Operator. **VERSTOSS (W15):** "Unlike the standard CDT case, here the introduction of a foliated lattice
  does not impose further restriction on the configuration space and, as a result, lattice quantisation does not leave any
  imprint on continuum physics". -> Im Standard-CDT-Fall (2D) schraenkt die Blaetterung den Konfigurationsraum also ein und
  hinterlaesst eine Spur im Kontinuum. Erwartet hatte ich "K^2-Term irrelevant, Kinetik entropisch". Das widerspricht in 2D
  der Lesart "Schichtung ist reines Gitterartefakt" (Loll 2019, S. 18-19) -> Moderator Dimension (2D vs. 3D-Jordan/Loll).

## 9. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. lambda bei Budd, AGSW, RG-Arbeit und Hořava ist dieselbe Konvention (G = (1/2)(gg + gg) - lambda gg, GR = 1).
   GEPRUEFT: Budd Gl. (4), AGSW Gl. (3), RG Gl. (13), Review Fn. 27 [alle S]. Haelt.
2. Unsere Zuordnung c = lambda/(3 lambda - 1) (REGEL.md, LAMBDA-1). GEPRUEFT: AGSW Gl. (6) schreibt die Hamilton-Dichte
   als pi^ij pi_ij - (lambda/(d lambda - 1)) pi^2 [S]. Haelt, unabhaengig von unserem Projekt.
3. CDT ist ein Netz mit Einstein-Wirkung (nackt lambda = 1). GEPRUEFT: Loll 2019 S. 18-19 "just the standard Einstein
   action" [S]; Budd Gl. (1) "derived from the Regge action" [S]; RG Gl. (1) [S]. Haelt. Folge: CDT ist KEIN "Raum-Netz
   mit Kanten-Bewegungsenergie", sondern Lesart 3 (Raumzeit-Netz mit Schichten). Die Karte hat CDT als Test der
   Raum-Netz-Hypothese gerahmt; das trifft nur halb.
4. Euklidisch positiv = Lorentzsch stabil (Vergleich Budd-lambda mit LAMBDA-1). NUR TEILWEISE GEPRUEFT: Dasgupta/Loll S. 3
   [S]: Ersetzung durch Boltzmann-Gewichte ist "ad hoc ... potentially inequivalent"; AGSW S. 8 [S]: Vorzeichen klassisch
   umdrehbar, in hoeheren Dimensionen mit Querfreiheitsgraden vielleicht nicht. Der Vergleich bleibt [ES].
5. Budds lambda-Wert ist belastbar. GEPRUEFT soweit moeglich: Langfassung verschiebt die Formdynamik auf "[9] to appear"
   [S]; eine spaetere Veroeffentlichung kenne ich nicht [L?]; Suche unmoeglich (R1).
6. Gitterzeit = physikalische Zeit. GEPRUEFT: Budd/Loll S. 17 [S] (nur global, nicht lokal); RG S. 12 [S] (feste
   Zeit-/Raumeinheit ist Annahme); Review 9.1 [S] (Restmehrdeutigkeit).

- 2026-10-04 03:53:11 CEST: Abgabe. DOSSIER.md geschrieben (ab 03:46:39) und rueckwaerts gegengelesen; Berichtigungen dabei:
  Loll-Seiten (S. 16 statt 18-19), REGGE-4D-1-Satz (nicht selbst gelesen), Vorzeichen in der Horava-Dispersion
  (omega^2 = -((lambda - 1)/(3 lambda - 1)) xi k^2), Projizierbarkeit von 4D-CDT als [ES] markiert.
  Offene Rueckfrage R1 (Regel 7) bleibt offen und steht im Dossier unter Selbstanzeigen Nr. 1.
