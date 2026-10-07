# Runde 47 (v3)

- Eroeffnet 2026-10-05 07:20:12 CEST (date), Leitung claude-primary.
- Vorgaenger: Runde 46, Journal claude-runde-v3-46-20261005.

## Karten (Ordner unter RUNDE-37/)

| Karte | Art | Stand |
|---|---|---|
| TT-GLAS-2 | Code-Agent | geerntet 08:34 |
| DANZER-NAEHERUNG-1 | Code-Agent | geerntet 07:41 |
| WELTKRISTALL-L | feldforscher | geerntet 07:30 (Dossier fertig 07:29) |
| OKTA-SCHATTEN-1 | Code-Agent | geerntet 07:53 |
| IMPULS-NETZ-1 | Code-Agent | geerntet 08:29 |
| TAKT-UMKLAPP-1 | Code-Agent | geerntet 08:14 (Ende 08:10:59) |
| CONNOR-HALL-L | feldforscher | geerntet 08:05 (vermutlich Connor Hill [H]; Bestaetigung durch Finn offen) |
| DEFEKT-NETZ-1 | Code-Agent | geerntet 08:32 |
| KAC-DIAMANT-WICK-1 | Code-Agent | geerntet 08:17 (geparkt) |
| BABY-UNIVERSUM-L | feldforscher | geerntet 08:44 |
| TEILE-SCHRANKE-L | feldforscher | geerntet 08:44 |
| DOPPLER-LAUFZEIT-L | feldforscher | laeuft seit 08:44 |
| TAKT-DYNAMIK-1 | Code-Agent | laeuft seit 08:19 (Spuren cpu8 bis cpu10) |
| SKALAR-SEKTOR-L | feldforscher | laeuft seit 08:29 |
| DANZER-NAEHERUNG-2 | Code-Agent | laeuft seit 08:33 (Spuren cpu3, cpu4) |
| GEGENLESEN-R47 | pruefer-opus | geerntet 08:56 |

## Warteschlange

0. (DANZER-NAEHERUNG-2 laeuft seit 08:33.)
1. Codex Rang 1 erfuellt im Vektor-Sektor (IMPULS-NETZ-1); Rang 8 in SKALAR-SEKTOR-L.
2. GEMEINSAMES-NETZ v4 (Leitung, mit Lueckenabgleich 1.1 und frischem Leser).
3. TEILE-SCHRANKE-L, PAAR-Auswege (Literatur), ATEM-VOLLZAEHLUNG-1 (nach Schreibtischprobe), Codex Rang 4, 5, 6, 7, 10.

## Protokoll

- 07:20:29 (date) Karte TAKT-UMKLAPP-1 geschrieben (RUNDE-37/takt-umklapp-1/KARTE.md). Teil A: HODGE-TAKT-1 woertlich aus HODGE-L (HT0 75 %, HT1' 55 %, HT2 55 %, HT3 85 %). Teil B: Zusatz der Leitung, Delaunay-gesteuerte Zuege gegen gleich viele Zufallszuege (TU1 55 %). Code-Agent gestartet, Spuren p4000a und p4000b, Zeitbox 150 min.
- 07:22:52 (date) Peerbus gelesen, keine offenen Nachrichten. UMKLAPP-1-Agent meldet nur das Ende seines Wartezeitgebers; der Bericht war schon in Runde 46 geerntet.
- 07:25 Finn: "Check Connor Hall Theorien im subagents". Projektsuche 07:25 (alle Dateitypen, Ausschluesse): "Connor Hall" im Projekt nicht vorhanden. Karte CONNOR-HALL-L ab 07:26:16 (CH0 45 %, CH1 60 %, CH2 65 %, CH3 55 %, CH4 35 %); feldforscher gestartet 07:27, 60 min, hoechstens 15 Abrufe, Websuche erst testen (Budget am 04.10. erschoepft), sonst nur Fach-APIs. Das ist der 7. gleichzeitige Agent (Deckel 6 seit dem Sitzungslimit, RUNDE-45). Ich ueberschreite ihn auf Finns direkten Auftrag hin, weil die Karte ohne Rechenlauf auskommt; Finns Grenze von 10 Agenten, davon 7 mit Rechenlaeufen, bleibt eingehalten.
- 07:26 Finn: "Mach takt umklapp jetzt". TAKT-UMKLAPP-1 laeuft bereits seit 07:21. Nachricht an den Agenten 07:27: Vorrang, Zusatzspuren cpu8 bis cpu10, ZWISCHENSTAND-A.md nach HT0/HT1', Zusatz der Leitung woertlich in PLAN.md.
- 07:30:47 (date) **Ernte WELTKRISTALL-L** (Dossier fertig 07:29, 8 von 8 Abrufen, keine Websuche). Peerbus gelesen, keine offenen Nachrichten.
  - H1 [S, M]: "Flach im Mittel = Zaehlung" ist der Kern der dynamischen Triangulierung (AGJL 2012, Gl. 70): N1/N3 = 6 arccos(1/3)/(2 pi), also q = 5,1043 und f6 = 10,43 %. Lambda ist dort Abstand zur Zaehlschwelle (Feinabstimmung). Reine Zaehlung ergibt Knaeuel, nicht flach. Die Zufallsform ~ N^(-1/2) passt nur in 4D zu Lambda; als 3D-Raumkruemmung ist sie um rund 32 Groessenordnungen ausgeschlossen.
  - H2 [M, S]: Die Hopf-Faserung der 600-Zelle (12 Zehnecke ueber einem Ikosaeder) ist eine diskrete Fock-Kugel, keine Kustaanheimo/Stiefel-Bruecke. Der faserfeste Teil des Laplace ist das doppelte Ikosaeder-Laplace (0; 5,528; 12; 14,472), geprueft gegen ZELLE600-1.
  - H3 [S]: Das 600-Zellen-Universum im Regge-Kalkuel gibt es seit Collins/Williams 1973; die unimodulare Zeit ist klassisch vorab ableitbar.
  - H4 [S Abstract]: In Kleinerts Weltkristall ist Torsion gegen Kruemmung eine Eichwahl, und die Versetzungen sind kondensiert. Die 4 freien Rahmendrehungen sind also zuerst Eichrichtungen, nicht automatisch Versetzungen.
  - Fund [S, L]: In C15 (MgCu2), der geordnet "geplaetteten" 600-Zelle, bilden die Defektlinien ein Diamantgitter (Doye/Wales 2001), und das Cu-Teilgitter ist ein Pyrochlor.
  - Urteile: WK1 bis WK3 in der Sache eingetroffen (WK1 nur ueber Sekundaerquellen); WK4 nach Wortlaut eingetroffen, die Bedeutung ("eigene Hypothese") traegt nur eingeschraenkt.
  - **Ableitbarkeitsprobe der Leitung zu DEFEKT-NETZ-1 [M, L]:**
    - C15 je kubischer Zelle: 16 Z12 + 8 Z16, also (192 + 128)/2 = 160 Kanten. Die 6er-Kanten sind die Mg-Mg-Bindungen, 8 x 4/2 = 16. Damit 816/6 = 136 Tetraeder und q = 816/160 = 5,1000 (f6 = 10 %). Die 6er-Kanten bilden das Diamantgitter der Mg.
    - A15: 2 Z12 + 6 Z14, also 54 Kanten und 6 Kettenkanten. q = 276/54 = 46/9 = 5,1111.
    - DN0 ist damit vorab ableitbar, wie der Agent schreibt.
    - DN1 bis DN3 (Spanne) sind es nicht: Kubisch bleibt ein freier l = 4-Koeffizient, sein Wert haengt an den verzerrten Kantenlaengen. Sie koennen scheitern und bestehen.
    - Die Zahl 0,0043 (f* - f6(C15)) ist ein Zahlenzufall gegen R17/R22 (dort eine Energiedifferenz), kein Befund.
  - **Negativliste:**
    - "Lambda bzw. Flachheit aus der Defektzaehlung ist eine neue Idee" (Kern ist DT)
    - "Die Zufallsschwankung erklaert die Flachheit des 3D-Raums"
    - "Die 600-Zelle verbindet Wasserstoff ueber Kustaanheimo/Stiefel" (nur Fock)
    - "Die freien Rahmendrehungen sind Versetzungen" (zuerst Eichrichtungen)
  - **Abschaetzung: erledigt.** DEFEKT-NETZ-1 als Warteschlange 0 (Finns Weiche "Kristall/Glas: beide Zweige"). H1 geht als DT-Lesart, nicht als eigene Hypothese, in GEMEINSAMES-NETZ v4.
- 07:3x Finn: "Benutze Chrome zur websuche oder nutz das qognio websuchen Ding". Pruefung der Leitung bis 07:40:04 (date):
  - WebSearch geht wieder: CONNOR-HALL-L nutzte es sechsmal (ABRUFE.md, Abrufe 4, 9, 10, 13, 14, 15).
  - Bis Abruf 15 kein Connor Hall mit Physik-Theorien: arXiv, INSPIRE und Zenodo ohne Treffer, im Netz nur Namensvettern, auch die Schreibweisen Conor und Conner.
  - Chrome laeuft, die Claude-Erweiterung ist aber nicht verbunden (list_connected_browsers leer). Das kann nur Finn beheben.
  - search.qognio.com (SearXNG) antwortet 403, weil das Admin-VPN qognio-admin nicht aktiv ist (aktiv nur wunderland). Die Leitung schaltet das VPN nicht selbst ein.
  - Gedaechtnis feedback-websuche-ausweichwege angelegt. Rueckfrage an Finn: Link oder Quelle zu Connor Hall; Erweiterung verbinden bzw. VPN-Freigabe.

- 07:41:03 (date) Karte DEFEKT-NETZ-1 geschrieben: DN0 bis DN3 woertlich aus WELTKRISTALL-L, Ableitbarkeitsprobe der Leitung, Zusatz der Leitung getrennt gekennzeichnet (Gleichstaende zaehlen, nicht per Zitter aufloesen, Symmetriekontrolle; Grund DANZER-NAEHERUNG-1). Code-Agent gestartet 07:41, Spuren cpu3 und cpu4, Zeitbox 120 min. Aktiv 6: TT-GLAS-2, OKTA-SCHATTEN-1, IMPULS-NETZ-1, TAKT-UMKLAPP-1, CONNOR-HALL-L, DEFEKT-NETZ-1.
- 07:41:52 (date) **Ernte DANZER-NAEHERUNG-1** (Code-Agent, Plan und Code eingefroren 07:21:15, alle Laeufe ueber kleintest.sh mit rc 0, L1-Wiederholung bitgleich). Peerbus gelesen, keine offenen Nachrichten.
  - Netze: Ammann-Kramer-Schnitt aus Z^6, periodisches Delaunay; Naeherungen 1/1, 2/1, 3/2 mit 32, 136, 576 Ecken je Zelle, je 8 Saaten. Alle Kontrollen bestanden; *1 und *2 nie negativ (Delaunay).
  - **N2 eingetroffen nach Plan, geteilt ueber alle Zweige:** Der kubische l = 4-Anteil beta von a2 ist ueberall negativ und faellt. Skalar -0,00345 -> -0,00083 -> -0,00060 (R = 0,17); Maxwell-Mittel -0,00163 -> -0,00077 -> -0,00043 (R = 0,26, nur etwa 1,5 Standardfehler unter der Drittel-Grenze); Zweig hi R = 0,35 (nicht). Der Abfall folgt nicht der linearen Phason-Kopplung (kein Vorzeichenwechsel bei 2/1).
  - **N1 nicht eingetroffen (Kontrolle):** Das Grundtempo haengt je Saat um 1 bis 7 % von der Richtung ab (6,8 / 2,9 / 1,4 %), etwa wie 1/Wurzel(V). Ursache ist die Bauweise: Der Zitter loest Delaunay-Gleichstaende zufaellig auf, und Einheitsgewichte belasten Kanten mit *1 = 0 (8,8 % der Kanten) voll. Das ist ein glasartiger Bau-Effekt, keine Folge der Ikosaederordnung. Die "vorab ableitbare" Kontrolle setzte kubische Symmetrie des Netzes voraus, die der Bau brach.
  - **N3 nicht eingetroffen, vorab absehbar:** a2 ist eine quartische Form, ihr l = 6-Anteil ist bis auf den Symmetriebruch je Saat null; der Rest faellt wie das Quadrat der Grundtempo-Anisotropie.
  - **Selbstanzeigen des Agenten:** einmal awk lokal auf /dev/null (ohne Wirkung), einmal python auf der .69 ausserhalb kleintest.sh (Umgebungstest), fuenf Rauchtests (zwei ueber Rechen- und Auswertewege, nur Rueckgabecodes gelesen), eigener Rayleigh-Ritz statt dichtem op_maxwell ab 2/1 (gegen exakte Eigenwerte auf 3,3e-8). Regelverstoesse vermerkt; die Regel "lokal kein awk, python auf der .69 nur ueber kleintest.sh" steht jetzt woertlich in jedem neuen Auftrag.
  - **Abschaetzung: weiter.** Lehre fuer alle Netzkarten [M, P]: Unregelmaessige Netze sind nur dann von selbst isotrop, wenn die Gewichte die Entartungen nicht sehen; Hodge-Gewichte leisten das, Einheitsgewichte nicht. Das ist dieselbe Spur wie HODGE-L und TAKT-UMKLAPP-1 Teil A. DANZER-NAEHERUNG-2 (DEC-Gewichte, 5/3) in die Warteschlange.
- 07:4x Finn: "Conor hall ist ein 18 jähriger der komplexe Strukturen untersucht hat" und "Ein ggf Youtuber oder so jetzt am MIT".
  - CONNOR-HALL-L, erster Durchgang fertig (Dossier, 15 von 15 Abrufen, 18 min 31 s): CH0 verfehlt, CH1 bis CH4 nicht entscheidbar (leere Menge, bewusst nicht gezaehlt). Kein Physik-Profil in OpenAlex, Zenodo, arXiv oder INSPIRE; acht Websuchen ohne namensgenauen Treffer. Die Suchmaschine tauscht den Namen auch in Anfuehrungszeichen gegen Namensvettern (Connor Dalton, Connor Behan).
  - Selbstanzeigen des Agenten: zwei geschaetzte Zeiten ueberschrieben statt gestrichen; einige grep-Laeufe ohne volle Ausschlussliste. Versiegeltes wurde nicht beruehrt, mit find nachgeprueft.
  - Agent fortgesetzt mit beiden Finn-Hinweisen als Zusatz der Leitung: Schreibweise Conor, 18 Jahre, vielleicht YouTuber, jetzt MIT; +10 Abrufe (hoechstens 25), +30 min.
    - Spur [H]: Finns Bezout/Kepler-Frage (KEGEL-4D-L) klingt nach einem Mathe-Video, etwa SoME.
    - Nur oeffentliches Werk, junger Mensch, respektvoll. Ergebnis als Nachtrag im Dossier.
- 07:4x Finn: "Ist Hodge wiederlegt oder anerkannt?" Antwort der Leitung, drei Lesarten:
  - Hodge-Theorie (Hodge-Stern, Hodge-Zerlegung, Hodge-Laplace) ist bewiesene Mathematik [L]; numerisch als DEC/FEEC Standard.
  - Hodge-Vermutung (Millennium-Problem): Erwartung vor Abruf "offen, hoechstens unbestaetigte Beweisansprueche". Eine WebSearch (07:48) bestaetigt das:
    - Es gibt Beweisansprueche (arXiv 2507.09934, Preprints.org 202602.0462, Zenodo 01/2026).
    - Laut Presse spricht OpenAI von "substanziellem Fortschritt", es gibt Widerspruch aus der Mathematik.
    - Kein anerkannter Beweis, keine Clay-Anerkennung, kein Gegenbeispiel.
    - Bekannt [L]: wahr fuer Divisoren (Lefschetz (1,1)); die ganzzahlige Fassung ist falsch (Atiyah/Hirzebruch 1962), die Kaehler-Verallgemeinerung auch (Voisin 2002).
  - Im Modell ist "Takt = Hodge-Laplace" eine Hypothese [H], TAKT-UMKLAPP-1 laeuft.
- 07:53:26 (date) **Ernte OKTA-SCHATTEN-1** (Code-Agent, Plan eingefroren 07:40:44, alle Laeufe auf der .69, Pruefsummen 11 von 11). Peerbus gelesen, keine offenen Nachrichten.
  - OS0 nach Plan eingetroffen, nach Wortlaut nicht: Ohne Sechseck-Plaketten sind alle 8 Baender flach (2 bei null, 6 bei omega^2 = 8); Licht laeuft gar nicht. Vorab im Plan festgelegt, keine Messung.
  - OS1 nach Plan eingetroffen, nach Wortlaut geteilt: Mit Sechsecken keine Nullmode an 789 k; Licht isotrop, mit umkreisbasierten Hodge-Gewichten c = 1 ohne Doppelbrechung; 2 flache Baender bei omega^2 = 8 bleiben (vorab abgeleitet). Neu gemessen: a2 = -5/64 + S4/24, also -0,0365 (Achsen) bis -0,0642 (Raumdiagonale); c^2 = 8q/(1 + 2q) mit q = w_H/w_D (Kopfrechnung des Agenten, trifft 7 von 7 Abtastwerten).
  - OS2 nicht eingetroffen: Hauptwahl H3 (Oktaeder in 4 Tetraeder, ueber 3 Diagonalen gemittelt) waechst in 3 von 13 bzw. 12 von 23 Richtungen; [210] mit omega^2/k^2 = -0,28; Bewegungsenergie an 6 von 511 k nicht positiv; Regge-Steifigkeit selbst isotrop 0,25.
  - OS3 nicht entscheidbar (instabil). Der eingefrorene Code meldet nach Wortlaut "eingetroffen", weil er -542 % mit 6,34 % vergleicht. Der Agent wertet inhaltlich "nicht entscheidbar" und zeigt die Regelluecke selbst an. Die Leitung folgt dem Agenten.
  - Beschreibend:
    - Starres ganzes Oktaeder (R12): exakt isotrop, omega^2/k^2 = 1,5, Spanne 3,9e-7, stabil; vorab ableitbar.
    - Mittelpunkt mit 8 Tetraedern (Z8): stabil, aber Spanne 100 %.
    - Feste Diagonale (D1z): Spanne 95 % und eine wachsende Mode.
    - Die Diagonalwahl als verstecktes Drei-Zustands-Feld kostet im flachen Netz nichts (Schur-Komplement gleich starrem Oktaeder auf 7e-9, *1 der Diagonale 0, Takt gleich); sichtbar nur ueber die Bewegungsenergie.
    - Die Rhombendodekaeder tragen die Takt-Gewichte exakt: W^+ B W = -2 L_{*1} an 524 k auf 1e-8. Das bestaetigt HODGE-L 4.4 b an diesem Netz (wie HT0 mit c = 2).
  - Selbstanzeigen: KeyError im Bildcode (Bild aus nachtraeglich eingefrorenem bild_okta.py); *2-Werte der Wabendreiecke fehlen (Codefehler); Agenten-Vorhersage A7 verfehlt (6e-9 statt <= 1e-10). Fuenfeck-Dodekaeder aus Finns Wortlaut nicht gerechnet.
  - **Lesart [H]:** Schattenformen tragen Kraefte in zwei Weisen:
    - Ihre Flaechen geben dem Licht Halt; ohne Sechsecke steht jede Welle.
    - Als starre Zellen machen sie das Netz flach und isotrop.
    - Jede innere Groesse einer Schattenform wird ueber die Bewegungsenergie zur eigenen Dynamik und schadet.
  - **Abschaetzung: erledigt.** Fuenfeck-Dodekaeder laufen ueber DEFEKT-NETZ-1: Die Voronoi-Zellen der Z12-Plaetze in C15 bzw. A15 sind Fuenfeck-Dodekaeder, und die Voronoi-Zerlegung von A15 ist der Weaire-Phelan-Schaum [L]. Auf S^3 ist es die 120-Zelle (ZELLE600-1).
- 07:53:33 (date) Karte KAC-DIAMANT-WICK-1 geschrieben (Vorschlag UNSCHAERFE-KANTE-L; KW0 90 %, KW1 20 %, KW2 50 %, KW3 15 %). Ableitbarkeitsprobe der Leitung mit 4x4-Schreibtisch je Untergitter: laengs [100] exaktes massives Dirac-Paar, laengs [111] gekippt; offen ist die 8x8-Kopplung von A und B. Code-Agent gestartet 07:54, Spuren cpu7 bzw. cpu, Zeitbox 75 min. Vorrang vor DANZER-NAEHERUNG-2, weil dessen Hauptausgang vorab ableitbar ist (Grundtempo mit Hodge-Gewichten symmetrisch [M]); KAC zielt auf Luecke T1 und Finns Unschaerfe-Frage. Aktiv 6: TT-GLAS-2, IMPULS-NETZ-1, TAKT-UMKLAPP-1, CONNOR-HALL-L, DEFEKT-NETZ-1, KAC-DIAMANT-WICK-1.
- 08:0x Finn: "Check in diesen Kontexten Beweisführungen zu Baby Universen". Projektsuche 08:03 (alle Dateitypen, Ausschluesse): nur RUNDE-22/geometrie-stand Z. 242 (CDT: keine Baby-Universen, Loll 2019 "appears to be essential") und Quellentexte; keine eigene Karte. Karte BABY-UNIVERSUM-L ab 08:04:00 (BU1 85 %, BU2 75 %, BU3 85 %, BU4 60 %, BU5 60 %, BU6 90 %); feldforscher gestartet 08:05, 60 min, hoechstens 15 Abrufe. Das ist wieder ein 7. Agent ohne Rechenlauf, auf Finns direkten Auftrag (Begruendung wie bei CONNOR-HALL-L); Finns Grenze von 10 Agenten, davon 7 mit Rechenlaeufen, bleibt eingehalten.
- 08:05:28 (date) **Ernte CONNOR-HALL-L** (Nachtrag nach Finns Hinweisen, 25 von 25 Abrufen, Ende 08:03:59).
  - Gemeint ist sehr wahrscheinlich **Connor Hill** [H, Finn muss bestaetigen]: erster Preis der Regeneron Science Talent Search 2026 (mit 17), Preprint "The complete set of noble polyhedra" (arXiv 2607.28711, Mathematik). Rechnergestuetzter Beweis: neben zwei unendlichen Familien genau 146 edle Vielflaechner (alle Ecken und alle Flaechen gleichwertig) [S].
  - MIT und YouTube sind nicht belegt. Die 146 sind nicht unabhaengig bestaetigt; belegt sind die Teilsummen und zwei Funde von Ben Klein in der Liste.
  - Urteile: CH0 verfehlt (Mathematik, keine physikalische Theorie); CH1 teilweise; CH2 eingetroffen (trivial); CH3 teilweise (nur Bausteine wie Tetraedervolumen und Disphenoide); CH4 eingetroffen (methodisch, modellintern).
  - Phase 1 unter "Connor Hall": 15 Abrufe ohne Treffer.
  - Selbstanzeigen: wirkungsloses awk-Fragment (awk 'NR>=0' /dev/null) lokal, das ist der dritte awk-Ausrutscher heute; einige grep ohne volle Ausschlussliste, Versiegeltes nicht beruehrt; Phase-2-Urteile nach dem Lesen geschrieben, die Karte selbst unveraendert.
  - Kartenvorschlag ATEM-VOLLZAEHLUNG-1: die isotropen Atemformen der 8-Tetraeder-Zelle (ISO-ATEM-1: zwei Formen aus 600 Zufallsstarts) nach Hills Weg vollstaendig abzaehlen, je Symmetrie-Untergruppe als Polynomsystem. Kann scheitern (dritte Form) und bestehen.
  - **Abschaetzung: erledigt,** die Bestaetigung der Person durch Finn ist offen. ATEM-VOLLZAEHLUNG-1 in die Warteschlange, nach eigener Schreibtischprobe der hochsymmetrischen Untergruppen.
  - Notiz [L]: Edle Tetraeder sind die Disphenoide (vier kongruente spitzwinklige Dreiecke). Die Delaunay-Zellen des bcc-Gitters sind solche Disphenoide und fuellen den flachen Raum ohne Fehlwinkel (4 x 90 = 6 x 60 = 360 Grad). Das ist ein moeglicher Kandidat fuer Finns Netz aus gleichen Zellen. Projektsuche dazu steht noch aus.
- 08:14:32 (date) **Ernte TAKT-UMKLAPP-1** (Start 07:21:17, Ende 08:10:59; Plan eingefroren 07:45:03; alle Laeufe auf cpu8 bis cpu10 mit rc 0, laengster 354 s; Pruefsummen lokal verifiziert). Peerbus gelesen.
  - **HT0 eingetroffen (vorab ableitbar):** Finns Takt-Operator ist exakt P = 8 d0^T *1 d0 mit umkreisbasiertem *1. Das gilt auf V und S an je 252 k (Rest <= 6,6e-16), in jedem einzelnen Tetraeder und auf 76 weiteren Netzen. c = 8, wie in der Karte erwartet [H].
  - **HT1' eingetroffen:** Auf V sind alle *1 positiv (1/720 bis 1/2); 12 von 116 *2 sind -8/9. V_D ist nach 12 Zuegen je Zelle Delaunay, S ist schon Delaunay (neu). Plan und Zwischenstand nannten "*1 > 0 auf V" zu Unrecht schon gerechnet; das ist datiert berichtigt.
  - **HT2 verfehlt (Hauptbefund):** Nach zufaelligen Zuegen ist P in allen 12 UMKLAPP-1-Netzen an keinem der 100 k positiv semidefinit (13 bis 148 negative Richtungen). B hat ueberall genau V negative Richtungen, und n_-(B_red) = n_-(P) ist exakt die Instabilitaetszahl aus UMKLAPP-1. Die Instabilitaet sitzt also ganz im Takt.
  - **HT3 nach eingefrorener Regel verfehlt, inhaltlich erfuellt:** 1 122 von 1 124 Punkten. An 2 Punkten (N = 256) zaehlte die Schwelle 1e-9 einen Eigenwert von etwa -7e-10 relativ als null. Das Urteil bleibt "verfehlt".
  - **TU1 eingetroffen:** Delaunay-gesteuert 26 von 26 Netzen stabil, gleich viele Zufallszuege 10 von 26 (a = 1e-3: 10 von 12; a = 1e-2: 0 von 12; V2: 0 von 2). In allen 52 Netzen gilt stabil <=> P psd. Mechanismus [H]: Die Eckbewegung bestimmt ueber Delaunay, welche Zelle umklappt; das haelt jede duale Flaeche und damit den Takt positiv.
  - **Berichtigung PUMPE-NETZ-1 [M]:** In 3D sind P1-Gewichte (3D-Kotangens) und umkreisbasierter *1 verschieden.
    - Gegenprobe der Leitung von Hand am Ecktetraeder (0, e1, e2, e3): Kante 0-e1 mit P1 1/6, umkreisbasiert 1/4. Am regulaeren Tetraeder sind beide gleich (je 0,0589 bei Kante 1).
    - Der Satz "P1 = umkreisbasierter Stern *1 [M]" in PUMPE-NETZ-1 gilt nicht. Seine Zahlen (1/60 bis 1/2) sind P1-Zahlen und stimmen.
    - Folge fuer L10: Die Materiekopplung in PUMPE-NETZ-1 nutzte P1, der Takt ist umkreisbasiert, also zwei verschiedene Hodge-Laplace-Operatoren (Galerkin gegen diagonal).
    - Hinweis an IMPULS-NETZ-1 geschickt (Gewichte nennen, umkreisbasierter Nebenarm, wenn moeglich).
  - **Selbstanzeige der Leitung [M]:** TU1 war vorab weitgehend ableitbar: Delaunay => *1 >= 0 in 3D (HKV 2013), dann mit HT0 P psd, und mit HT3 stabil. Die Karte nannte TU1 "nicht ableitbar", weil V stabil ist, ohne Delaunay zu sein. Das passt aber gerade dazu: Auf V sind alle *1 positiv. Neu und nicht ableitbar war nur die Zahl der Zufallszug-Netze mit negativem *1 (HT2) und die Quote 10 von 26.
  - Selbstanzeigen des Agenten: awk lokal in einer Lese-Pipe (vierter awk-Ausrutscher heute, ohne Wirkung auf Zahlen); zwei beschreibende Nachtraege nach dem Einfrieren (P1-Vergleich, HT3-Schwellenfall).
  - **Abschaetzung: weiter.**
    - Finns Mechanismus fuer "Zellen umklappen" steht als Modellbefund: Die Ecken bewegen sich, Delaunay waehlt die Zelle, der Takt bleibt positiv.
    - Offen und nicht ableitbar ist die Dynamik: Bleibt das Netz waehrend laufender Wellen durch Umklappen stabil und energieerhaltend?
    - An der Flip-Stelle ist die duale Flaeche null, also ist P stetig [M]. Die Integratorfehler sind offen.
    - Kartenidee TAKT-DYNAMIK-1 (nach IMPULS-NETZ-1, weil gekoppelt): Wellenpaket auf einem Delaunay-Glas mit Umklappen im Lauf, Energiebilanz gegen Zufallszuege.
- 08:17:39 (date) **Ernte KAC-DIAMANT-WICK-1** (Start 07:54:25, Ende 08:15:24; Plan mit allen Zahlen vor der Rechnung, Laeufe auf der .69 bestaetigen die Herleitung).
  - Nur das aeussere Bandpaar taugt: E0 = Delta = hbar lambda. Richtungsstreuung bei \|k\| = 0,05 (in 1/Bindungslaenge): 1,45e-4 (gleichverteilt) bzw. 1,63e-4 (ohne Ruecksprung), weit unter 2,8e-3.
  - Masse = Nelson-Masse m = hbar/(2D) (Ghose Gl. 58). Gleichverteilt: c_eff = Wurzel(2/3) c, m = 1,5 hbar lambda/c^2. Ohne Ruecksprung: c_eff = c, m = hbar lambda/c^2, laengs [111] exakt Ghoses 1D-Dirac-Paar.
  - Urteile:
    - KW0 eingetroffen.
    - KW1 nach Plan eingetroffen; die Formschwelle setzte der Agent erst nach der Schreibtischrechnung (Selbstanzeige). Bei exakter Dirac-Form nicht eingetroffen.
    - KW2 nicht eingetroffen: ohne Ruecksprung 1,12-fach groessere Streuung, am Schreibtisch 9/8.
    - KW3 eingetroffen (Delta = 1 hbar lambda, m auf 1e-8 bzw. 7e-8).
  - **Selbstanzeige der Leitung:** Meine Karte nannte "A-B-Kopplung hebt die Kippung auf" nicht ableitbar. Es folgt aber aus dem Tausch A <-> B, denn das Spektrum ist gerade in k; die kleine-k-Isotropie folgt aus der Wuerfelsymmetrie [M]. Das ist der zweite Ableitbarkeits-Fehler der Leitung heute nach TU1. Alle vier Urteile waren vorab ableitbar.
  - **Grenze:**
    - Bei c k = lambda streut das Paar um 3 bis 4 % (Standardabweichung) bzw. 12 bis 15 % (Spannweite).
    - Die Grenzgeschwindigkeit ist c laengs [111], 0,816 c laengs [110] und c/Wurzel(3) laengs [100]: Der Grenzkegel ist tetraedrisch, nicht rund.
    - Dazu kommen sechs weitere Baender mit Richtungsabhaengigkeit.
    - Das i kommt aus der Wick-Rotation, also von Hand. T1 ist nicht geschlossen.
  - **Datennah [H, Schranken nicht abgerufen]:** Waere ein Elektron ein solches Teilchen mit hbar lambda = m_e c^2, haette es oberhalb von p ~ m_e c eine richtungsabhaengige Grenzgeschwindigkeit von Ordnung 1. Laborschranken an Elektronen (SME-Datentabellen, Kostelecky/Russell [L]) liegen viele Groessenordnungen darunter. Als Elektronenmodell ist die Konstruktion damit ausgeschlossen, falls die Schranken bestaetigt werden.
  - Selbstanzeigen des Agenten: \|k\| in 1/Bindungslaenge (bei Wuerfelkante etwa 3/16 so grosse Streuungen; ueber 2,8e-3 erst ab \|k\| l ~ 0,2); Bild nach dem Hauptlauf neu gezeichnet und als Nachtrag eingefroren; KW0-Schwelle 1e-9 nur ueber den exakten Stoerungskoeffizienten.
  - **Abschaetzung: parken.** Antwort auf Finns Unschaerfe-Frage: Die Kantenwahl gibt Unschaerfe und Teilchenmasse nur, wenn man das i von Hand einsetzt; langsam ist das Teilchen richtungsgleich, schnell richtungsabhaengig.
- 08:15:27 (date) Karte TEILE-SCHRANKE-L geschrieben (Vorschlag LICHT-TEILE-L, datennah; TS0 90 %, TS1 70 %, TS2 60 %, TS3 85 %, TS4 70 %); feldforscher gestartet 08:16, 60 min, hoechstens 15 Abrufe.
- 08:18:29 (date) Karte TAKT-DYNAMIK-1 geschrieben (Fast Lane nach TU1; TD0 85 %, TD1 55 %, TD2 75 %, TD3 45 %, TD4 85 %).
  - Ableitbarkeitsprobe mit verketteten Bausteinen: P am Zug stetig, Rueckkehr der Zerlegung (Eindeutigkeit), Zugzahl aus UK1 und Instabilitaet im Zufallsarm aus HT2/HT3 sind vorab ableitbar. Offen bleiben Energiedrift und Streuung.
  - Code-Agent gestartet 08:19, Spuren cpu8 bis cpu10, Zeitbox 150 min.
  - Aktiv 6: TT-GLAS-2, IMPULS-NETZ-1, DEFEKT-NETZ-1, BABY-UNIVERSUM-L, TEILE-SCHRANKE-L, TAKT-DYNAMIK-1.
- 08:29:23 (date) **Ernte IMPULS-NETZ-1** (Text fertig 08:24:40; frischer Gegenleser pruefer-opus ohne urteilskippenden Fehler, 7 B- und 10 C-Befunde eingearbeitet). Peerbus gelesen.
  - **IN0 eingetroffen** (Kontrolle).
  - **IN1 eingetroffen (Schreibtisch ableitbar):** Die Impulsregel ist die Verschiebungsregel M^H p, erster Klasse. Die Materie koppelt als M^H p = J mit J' = -M^H sigma; Identitaetsproben <= 3e-11 an 5 600 k.
  - **Neu:** Ohne J haengt die Leckage an der Eichwahl (Laengskopplung bei [111] 0,013 bis 0,044 je Eichung). Die PUMPE-NETZ-1-Zahlen 1,18 / 0,91 / 0,98 waren damit keine Eigenschaft des Netzes. Das berichtigt meine Meldung an Finn aus Runde 46.
  - **IN3 eingetroffen:**
    - Mitfuehrung wie Einstein, 1 + 7,4e-6 bei kl = 0,01, ueber 200 Richtungen 0,9999967 bis 1,0000132.
    - Das folgt weitgehend aus der Abstimmung J_iso, denn bei isotropem TT-Tempo haben alle spurfreien Tensoren denselben Koeffizienten. Der Agent sah das erst nach Sicht.
    - Mit J = 1 streut die Mitfuehrung von 0,975 bis 1,036.
    - GP-B (-37,2 +- 7,2 gegen -39,2 mas/Jahr) und LARES (0,991 +- 0,02) sind vertraeglich [S, Abstract].
  - **IN2 nicht eingetroffen:**
    - G_rad/G_N = 1,030 / 1,004 / 0,967. Der Laengskanal verschwindet (<= 6e-11), der nn-Kanal sinkt auf ein Siebtel bis ein Viertel, der Energiekanal V1 bleibt.
    - Mit glatteren Quellen (w = 2,0 l_P) wird es 1,000 / 1,005 / 1,005.
    - Kreisbahnen schwanken -0,15 % bis +0,12 % (vorher -0,75 % bis +3,4 %), rund 12-mal ueber dem Doppelpulsar (1,3e-4).
  - **Umkreisbasierter Nebenarm (beschreibend):** Kompakte Quellen, Kreisbahnen und Isotropie bleiben auf 1e-6 gleich. Nur die gittergrosse Kartenquelle wird schlechter (mit J 1,072 / 0,951 / 0,939). Die Urteile nutzen P1; die Formulierung braucht P1 = *1 nicht.
  - Selbstanzeigen: lokal versehentlich `python3 -` gestartet, zwischen 07:35:24 und 07:41:49, ohne Skript und ohne Rechnung. Regelverstoss. Dazu Spuren cpu5/cpu6 anders belegt als im Plan und zwei Nachtraege nach Sicht ohne Urteil.
  - **Lesart [H]:** Der Vektor-Sektor ist einsteinsch, Codex Rang 1 (Gegenseitigkeit) ist dort erfuellt. Der Rest sitzt im skalaren Sektor (zweite Klasse, Energiequelle auf dem Gitter nicht erhalten).
  - **Abschaetzung: weiter** mit SKALAR-SEKTOR-L (Literatur und Schreibtisch, verbindet die Projektbefunde Horava aus R41 und Kommutator aus R42 mit den Datenschranken; Codex Rang 8 inbegriffen).
- 08:28:00 (date) Karte SKALAR-SEKTOR-L geschrieben (SS1 80 %, SS2 70 %, SS3 45 %, SS4 70 %, SS5 55 %).
  - Ableitbarkeitsprobe verkettet: "lokal erster Klasse und physikalischer Takt" ist im Kontinuum ausgeschlossen (Refoliations-Symmetrie) [L].
  - Projektsuche 08:26: Horava-Zuordnung (R41), Kommutator (R42), L1 und L8 (GEMEINSAMES-NETZ v3), alpha_1/alpha_2 offen (R43 O5).
  - feldforscher gestartet 08:29, 75 min. Aktiv 6: TT-GLAS-2, DEFEKT-NETZ-1, BABY-UNIVERSUM-L, TEILE-SCHRANKE-L, TAKT-DYNAMIK-1, SKALAR-SEKTOR-L.
- 08:32:00 (date) **Ernte DEFEKT-NETZ-1** (alle Laeufe rc 0, Zeitbox eingehalten; frischer Leser im Agentenlauf, Endfassung nicht mehr gesehen).
  - **C15 ist Finns Netz S [P, M, E]:** S aus EINE-WELT-LOCH-1, um (3/8, 3/8, 3/8) verschoben, ist genau die C15-Zerlegung (136 von 136 Tetraedern gleich). s(C15) = 2,68 % stand damit schon in TT-ISO-1. DN1 und DN3 waren vorab ableitbar; die C15-Rechnung ist eine Reproduktion.
  - **Selbstanzeige der Leitung:** dritter Ableitbarkeits-Fehler heute, nach TU1 und KAC.
    - Meine Probe nannte DN1 bis DN3 nicht ableitbar.
    - Die Karte sagte "den Kristall-Zweig deckte bisher nur V ab".
    - Meine Projektsuche suchte nach Namen (C15, MgCu2, Laves), nicht nach Kennzahlen (24 Ecken und 136 Tetraeder je Zelle, q = 5,1).
  - **DN0 eingetroffen (ableitbar):** keine Gleichstaende, Delaunay gleich kristallographisch, q = 5,1 und 46/9 exakt, die 6er-Kanten von C15 bilden ein Diamantnetz. Zusatz der Leitung geprueft: volle kubische Symmetrie, Grundtempo isotrop.
  - **DN2 verfehlt, einziges neues Ergebnis:** s(A15) = 0,934 %, etwa ein Drittel von C15 und ein Siebtel von V. Das Netz mit weniger Ikosaederplaetzen (1/4 gegen 2/3) ist das gleichmaessigere. Fuer "DN1 ja, DN2 nein" hat die Karte keinen Bedeutungssatz.
  - Alle drei Kristalle sind regulaer: je 2 masselose TT-Moden, nichts waechst bei kleinem k und an 511 Gitterpunkten. Die Spanne ist die Aufspaltung der zwei Polarisationen laengs [100]. Kontrolle V 6,3388 %, auf 3,3e-7 wie TT-ISO-1.
  - Selbstanzeigen des Agenten:
    - Rauchtests liefen vor dem Plantext (Plan ab 08:02:27), gelesen wurden nur Rueckgabecodes; die Ergebnisse sind bitgleich mit den Hauptlaeufen.
    - eigene Delaunay-Funktion statt woertlich TT-GLAS-1-Code
    - AFLOW zweimal 404, Lagen vom NRL-Spiegel (Wyckoff bzw. Nevitt)
    - Bild nach dem Einfrieren neu gezeichnet
  - **Lesart [H]:** Ikosaedrische Nahordnung sagt die TT-Isotropie im Kristall-Zweig nicht voraus. A15 hat als Voronoi-Zerlegung den Weaire-Phelan-Schaum mit Fuenfeck-Dodekaedern [L]; Finns Schattenformen tauchen also beim gleichmaessigsten Kristallnetz auf, erklaeren dessen Isotropie aber nicht.
  - Ohne Abstimmung sind alle Kristallnetze von GW170817 (c_T = c auf ~1e-15 [L?]) weit entfernt; mit J_iso ist Isotropie einstellbar (R45).
  - **Negativliste:** "Ikosaedrische Nahordnung macht TT isotroper" (im Kristall-Zweig nicht gestuetzt).
  - **Abschaetzung: erledigt.**
- 08:32:16 (date) Karte DANZER-NAEHERUNG-2 geschrieben.
  - Vorhersagen: D2-0 85 %, D2-1 60 %, D2-2 50 %, D2-3 50 %.
  - Ableitbarkeitsprobe verkettet: An Gleichstaenden ist das duale Mass null. Damit sind die DEC-Operatoren unabhaengig von der Aufloesung, die volle kubische Symmetrie bleibt und das Grundtempo ist isotrop; das ist die Kontrolle D2-0.
  - Kennzahlen-Abgleich: Die Naeherungsnetze gibt es nur aus DANZER-1.
  - Code-Agent gestartet 08:33, Spuren cpu3 und cpu4, Zeitbox 120 min.
  - Aktiv 6: TT-GLAS-2, BABY-UNIVERSUM-L, TEILE-SCHRANKE-L, TAKT-DYNAMIK-1, SKALAR-SEKTOR-L, DANZER-NAEHERUNG-2.
- 08:34:20 (date) **Ernte TT-GLAS-2** (Start 06:47:39, Ende 08:32:43, innerhalb der Zeitbox; ohne frischen Leser).
  - **TG2-0 eingetroffen:** TT-GLAS-1 auf 1,9e-9 reproduziert.
  - **TG2-1 eingetroffen:**
    - Alle 24 Netze (N = 128 und 256, je 12 Saaten) ueber das volle 6^3-Gitter der Superzelle (112 k-Klassen): Nirgends waechst eine Mode.
    - Nullmoden nur bei Gamma, genau 6 je Netz (homogene Verzerrungen, ableitbar).
  - **TG2-2 verfehlt, Planzerlegung entartet:**
    - Lange TT-Wellen sind bis auf 1e-5 die projizierten affinen Wellen, also (a) = (b); nichtaffine Relaxation traegt nichts bei (per Stoerungsrechnung vorab ableitbar, im Plan uebersehen).
    - Die Anisotropie sitzt in der Bewegungsenergie. Mit isotroper Ersatzmasse A3 bleibt etwa die Haelfte (7,1 % statt 15,3 % bei N = 128; 5,7 % statt 11,4 % bei N = 256), und dieser Rest kommt aus der Projektion auf den Eichvertreter (unprojiziert 0,00 %).
  - **TG2-3 eingetroffen:**
    - N = 1024: Spanne 4,66 +- 0,28 % (4 Netze); N = 512: 6,8 %.
    - Exponent -0,56, mit TT-GLAS-1 -0,52. Der Doppelbrechungsanteil bleibt 0,84 bis 0,88.
    - Dicht auf der P4000 gerechnet (im Plan begruendet); zwei N = 1024-Laeufe auf p4000a mit Speichermangel, auf p4000b mit demselben eingefrorenen Code nachgeholt.
    - Nachtrag 4 weitere Netze N = 512: 8,9 %, zusammen 7,9 %, ohne Urteilswirkung.
  - **Regelverstoesse (Selbstanzeigen):**
    - einmal scp an Ort und Stelle vor Rauchtest r2
    - die Hash-Datei kurz in RUNDE-37/, inzwischen verschoben
    - ein `python -c` auf der .69 ausserhalb kleintest.sh
  - **Lesart [H, M]:**
    - Ein statistisch homogenes und isotropes Glas ist im Langwellen-Grenzfall isotrop.
    - Die gemessene Spanne ist ein Effekt endlicher Proben, ~N^(-1/2).
    - Bei Planck-grossen Zellen enthaelt eine Schwerewellenlaenge ~1e120 Zellen. GW170817 waere damit ohne Abstimmung weit erfuellt, anders als bei den Kristallnetzen (V 6,34 %, C15 2,68 %, A15 0,93 %).
  - **Abschaetzung: erledigt.** Der Glas-Zweig ist von selbst isotrop und stabil; Kristallnetze brauchen J_iso. Frischer Leser in GEGENLESEN-R47.
- 08:34:25 (date) Karte GEGENLESEN-R47 geschrieben (GR1 85 %, GR2 85 %, GR3 75 %, GR4 85 %, GR5 45 %, GR6 90 %).
  - Frischer Leser (pruefer-opus) fuer TAKT-UMKLAPP-1, TT-GLAS-2, OKTA-SCHATTEN-1 und KAC-DIAMANT-WICK-1, dazu die Ecktetraeder-Handrechnung der Leitung.
  - Nur lokal, Zeitbox 60 min, gestartet 08:35.
  - Der Journaleintrag der Runde 47 wartet auf seine A-Liste.
  - Aktiv 6: BABY-UNIVERSUM-L, TEILE-SCHRANKE-L, TAKT-DYNAMIK-1, SKALAR-SEKTOR-L, DANZER-NAEHERUNG-2, GEGENLESEN-R47.
  - Notiz: GEGENLESEN-R45 Teil A deckte Jordan/Pryce und die Komposit-Bosonen schon ab (PS1 bis PS3). Vor einer Karte PAAR-Auswege zuerst dessen Ergebnis lesen.
- 08:44:51 (date) **Ernte TEILE-SCHRANKE-L** (08:16 bis 08:42, 15 von 15 Abrufen, 3 ohne Ertrag).
  - Beim Nachweis: Sichtbares Licht verliert hoechstens ~1e-4 an unsichtbare Teile (PQED gegen Kryoradiometer, 60 bis 180 ppm). Gamma: Energie ausserhalb h nu (-1,4 +- 4,4)e-7 (Rainville 2005).
  - Unterwegs gibt es keine Laborschranke. Kosmisch, ohne Zeitdehnung: hoechstens ~2 % der Rotverschiebung bis z ~ 1,2, also ~1,5e-28 je Meter (DES, b = 1,003 +- 0,005 +- 0,010).
  - Urteile:
    - TS0 eingetroffen (nur Schreibtisch, IAEA-Seite gesperrt)
    - **TS1 verfehlt:** Glasfaser-Uhrenvergleiche gleichen einen symmetrischen Verlust selbst aus; Pound/Rebka misst Differenzen.
    - TS2 teilweise: TES setzt E = n h nu in der Eichung voraus.
    - TS3 und TS4 eingetroffen.
  - Offene Fenster: Verlust in Glas oder Luft; Verlust, der zugleich die Zeitabstaende streckt; Teile ohne Energie und Impuls; energieabhaengiger Verlust.
  - Negativliste: "Glasfaser begrenzt den Verlust auf 3e-19", "TES zeigt n h nu", "Pound/Rebka begrenzt den Verlust", "Muedes Licht ist widerlegt" (nur als alleinige Ursache ausgeschlossen).
  - **Abschaetzung: weiter** mit dem Vorschlag DOPPLER-LAUFZEIT-L (Raumsonden: Doppler gegen Laufzeit).
- 08:44:51 (date) **Ernte BABY-UNIVERSUM-L** (15 von 15 Abrufen, Abschluss 08:43:10).
  - Urteile: BU1 und BU6 eingetroffen; BU2, BU3, BU4 und BU5 teilweise.
  - Kein anerkannter Beweis fuer oder gegen Baby-Universen; strenge Saetze nur in Modellen, etwa exakt loesbarer 2D-Gravitation.
  - Colemans Lambda -> 0 gilt nicht als Loesung:
    - Behebt man das Vorzeichen des konformen Faktors, kehrt sich das Maximum um.
    - Ein Phasenfaktor beschraenkt das Argument auf d = 2 mod 4.
    - Es widerspricht den Daten (Lambda != 0).
    - Im 2D-Modell scheitert es (Hamada/Kawai/Kawana 2022).
  - **BU5 im Teil "Stabilitaet strittig" verfehlt:** Euklidische Axion-Wurmloecher gelten seit 2024/25 als perturbativ stabil. Hertog u. a. 2024 zeigten ueber die Hodge-Dualitaet, dass 2-Form- und Skalarbild gleichwertig sind; Marolf/Missoni und Loveridge/Sun 2025 stuetzen das. Strittig ist nur noch, ob sie zum Pfadintegral beitragen.
  - **CDT:** verbietet nur das Verzweigen in der Zeit, raeumliche Verzweigung ist erlaubt (Loll 2019). 3D-CDT kennt eine Phase, in der der Raum zu einem Schaum aus Baby-Universen zerfaellt (AJL 2002). Ob erst Kausalitaet de Sitter ermoeglicht, ist offen (EDT mit Massterm).
  - **Datenkontakt:** Ambjorn/Watabiki erklaeren die beschleunigte Expansion durch Absorption von Baby-Universen; in reiner Form passt das schlecht zu Planck und DESI 2024 (Muralidharan/Cline 2024).
  - **Glied 10:** Der Hilbertraum eines geschlossenen Universums ist bei festem Lambda eindimensional, bei unimodular freiem Lambda unendlichdimensional (Gielen 2026).
  - **Finns Netz:**
    - Pachner-Zuege aendern die Topologie nie [M].
    - Schreibtisch D1 (ungeprueft): 2-3-Zuege erzeugen nie einen minimalen Hals (vier Dreiecke ohne ihr Tetraeder); nur 3-2- oder 1-4-Zuege koennen das.
    - Die UMKLAPP-1-Instabilitaet ist damit kein Baby-Universum-Effekt. Sie ist ohnehin durch HT2 erklaert (negative duale Flaechen).
  - **Hodge:** Werkzeug an drei Stellen der Debatte: Axion gegen 2-Form, Lambda gegen 4-Form-Fluss, Kopplungen als Top-Formen. Zur Hodge-Vermutung kein Bezug.
  - Selbstanzeigen: lokal awk in einer Pipe, Ausgabe verworfen (fuenfter awk-Fall heute; dieser Auftrag hatte noch die aeltere Regelfassung); zu lange Zitate in der ersten Fassung, berichtigt; drei geschaetzte Zeiten durchgestrichen und ersetzt.
  - **Abschaetzung: erledigt.** MINIMALHALS-1 geparkt (Instabilitaet durch HT2 erklaert). BU-ABSORPTION-1 geparkt (Nachbau mit wenig Neuem). Gielen 2026 fuer Glied 10 vormerken.
- 08:43:21 (date) Karte DOPPLER-LAUFZEIT-L geschrieben (DL0 90 %, DL1 80 %, DL2 35 %, DL3 55 %).
  - Ableitbarkeitsprobe verkettet: Pioneer begrenzt eine andere Groesse (zeitliche Drift statt streckenproportionaler Verlust).
  - feldforscher gestartet zwischen 08:43:21 und 08:44:51 (date-Klammer), 60 min.
  - Aktiv 5: TAKT-DYNAMIK-1, SKALAR-SEKTOR-L, DANZER-NAEHERUNG-2, GEGENLESEN-R47, DOPPLER-LAUFZEIT-L. Ein Platz bleibt frei: Leitung schreibt Journal und GEMEINSAMES-NETZ v4.
- 08:56:42 (date) **Ernte GEGENLESEN-R47** (pruefer-opus, 08:35:25 bis 08:55:14). Peerbus gelesen.
  - GR1 bis GR6 eingetroffen (6 von 6). Keine falsche Zahl und kein falsches Urteil.
  - **A-Liste:**
    - **A1 TAKT-UMKLAPP-1:** "die ganze Instabilitaet" bzw. "genau dort wachsen Stoerungen" ist zu stark. Belegt ist: Der Anteil der Instabilitaet, der in B_red sitzt, kommt ganz aus dem Takt (n_-(B) = V, also n_-(B_red) = n_-(P)). Wo die Bewegungsenergie nicht positiv definit ist (V2-Z-Arm; UMKLAPP-1 f = 0,2), kommen weitere wachsende Moden hinzu (74 gegen 70). Die raeumliche Zuordnung ist nicht gerechnet.
    - **A2 TT-GLAS-2:** "ganze Brillouin-Zone" zu stark; gerechnet sind 112 k-Klassen des 6^3-Gitters.
  - **Berichtigung der Leitung:**
    - Mein Ernte-Eintrag 08:14:32 (HT2: "Die Instabilitaet sitzt also ganz im Takt") und meine Meldung an Finn ("genau dort wachsen Stoerungen") hatten denselben zu starken Satz. Die Berichtigung geht an Finn.
    - Datierte Berichtigungsnotizen stehen oben in takt-umklapp-1/ERGEBNIS.md und tt-glas-2/ERGEBNIS.md (Sicherungen .bak-20261005-085628).
  - **B-Liste, fuer v4:**
    - B1: Meine TU1-Selbstanzeige ("ableitbar aus HKV + HT0 + HT3") braucht zusaetzlich n_-(B) = V und eine positive Bewegungsenergie. Beides sind beobachtete Befunde, keine Saetze.
    - B3: "sogar etwas steiler" haelt nicht (-0,47 im Vertrauensbereich).
    - B5: haupt.json in KAC traegt keinen Code-Hash.
    - B6: In KAC heisst es "Welle mit Masse" statt "Teilchen"; meine Meldung an Finn sagte "Teilchen". Die Berichtigung geht an Finn.
    - B7: In OKTA haengt das Tempo auch an den Dreiecken, nicht "genau an diesen Flaechen".
  - **Bestaetigt:**
    - OS3 "nicht entscheidbar" ist eine Verschaerfung, keine Lockerung.
    - Die KAC-Formschwelle stand 7 s vor dem Hauptlauf im eingefrorenen Plan, gesetzt in Kenntnis der Schreibtischwerte (offen angezeigt).
    - Die p4000b-Wiederholung traegt den Hash des eingefrorenen dk.py.
    - Die Ecktetraeder-Handrechnung stimmt (1/6 gegen 1/4; Kante 1-2: 0 gegen -1/24; Summenregel je 1/2).
- 08:57:56 (date) **Runde 47 geschlossen.** Journal claude-runde-v3-47-20261005, Nr. 595: 29 Quellen, pruefen ohne Befunde, rc 0 (RUNDE-47/journal/). Peerbus vor dem Eintrag gelesen, keine offenen Nachrichten. Laufende Karten wandern nach Runde 48: TAKT-DYNAMIK-1, SKALAR-SEKTOR-L, DANZER-NAEHERUNG-2, DOPPLER-LAUFZEIT-L.
