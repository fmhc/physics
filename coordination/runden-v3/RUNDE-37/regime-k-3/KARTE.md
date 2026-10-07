# REGIME-K-3: Ist die Zeltstangen-Zeitentwicklung auf Finns gefuelltem Netz V in echter Zeit stabil? (Runde 49, Folgekarte aus REGIME-K-2)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 14:11:50 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - REGIME-K-2: Gefuelltes V mal Zeit ist euklidisch langwellig TT-isotrop (8,0e-9). Die euklidische Hesse hat aber an jedem k 26 Gittermoden negativer Steifigkeit (plus die konforme Richtung); B1 ohne Fuellung hat 7, Kuhn keine. In echter Zeit (komplexes k_tau wie REGGE-WELLE-1) sind die TT-Frequenzen bei |k| = 0,05 leicht komplex (|Im omega|/|k| bis 1,9e-4, waechst wie |k|^2), dazu Wurzeln bei omega ~ 2,5 i; ob das Anwachsen ist, haengt an der Zweigwahl des Logarithmus.
  - REGGE-WELLE-1: Auf Kuhn laufen Wellen ohne Anwachsen.
  - UEBERLEITUNG-KH-1 und UEBERLEITUNG-V-1 (laeuft): der Grenzfall stetiger Zeit. Diese Karte prueft die diskrete Zeit selbst.
- Kennzeichen: [M], [E], [P], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab [M]:** Linear um flach ist ein Zeltstangen-Takt eine lineare Abbildung der Randdaten einer Schicht auf die der naechsten (Transfermatrix je Bloch-k). Sie ist symplektisch; ihre Eigenwerte kommen in Paaren lambda, 1/lambda. Stabil heisst: alle physikalischen Eigenwerte auf dem Einheitskreis. Die Zweigwahl-Frage aus REGIME-K-2 entfaellt so.
- **Nicht ableitbar:** ob Eigenwerte vom Einheitskreis abweichen, fuer welche Moden (TT, Gittermoden) und bei welchen k.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RT0 | Kontrolle [P]: Auf Kuhn liegen alle physikalischen Eigenwerte der Takt-Transfermatrix auf dem Einheitskreis (abs(lambda) - 1 < 1e-10) an allen gerechneten k, passend zu REGGE-WELLE-1 | 80 % |
| RT1 | [H] Auf V liegen fuer die zwei TT-Moden bei |k| <= 0,1 die Eigenwerte auf dem Einheitskreis (abs(lambda) - 1 < 1e-8); die komplexen Frequenzen aus REGIME-K-2 waeren dann ein Effekt der Nullstellensuche | 45 % |
| RT2 | [H] Auf V gibt es an mindestens einem gerechneten k einen Eigenwert mit abs(lambda) > 1 + 1e-6 (Instabilitaet, vermutlich aus den Gittermoden negativer Steifigkeit) | 55 % |
| RT3 | [H] Auf B1 ohne Fuellung gibt es hoechstens halb so viele instabile Eigenwerte je k wie auf V | 50 % |

**Bedeutung (vorab):**
- **RT1 trifft ein, RT2 nicht:** Die 4D-Zeit traegt auf Finns gefuelltem Netz isotrope und stabile Schwerewellen ohne Abstimmung. Regime K wird der Hauptweg.
- **RT2 trifft ein:** Die Zeltstangen-Zeit ist auf V instabil (Gittermoden); dann ist zu klaeren, ob eine andere Zeltstangen-Folge oder eine andere Fuellung das heilt, oder ob V als Netz ausscheidet.
- **RT1 verfehlt:** Auch die langen Schwerewellen wachsen oder daempfen; das waere eine Grenze der diskreten Zeit auf V.

## Rahmen

- Code-Agent. Code aus RUNDE-37/regime-k-2/code (gefuelltes V mal Zeit, Zeltstangen) und RUNDE-37/pachner-takt-1/code (Takt als Abbildung zwischen Schichten, Hoehn) kopieren, dort nichts aendern.
- Transfermatrix je Bloch-k aus der linearisierten Regge-Wirkung einer Schicht (euklidisch gerechnet, Lorentz-Fortsetzung nach der Konvention von REGGE-WELLE-1 im Plan festlegen und begruenden); Eich- und Lapse-/Shift-Richtungen vorab ausweisen.
- k-Raster wie REGIME-K-2 plus BZ-Rand; Netze Kuhn (Kontrolle), V, B1.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu8, cpu9 und cpu10. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256); Ausweichpfade nur mit Meldung.
- Synthetisch, keine Messdatenbestaetigung.

## Nachtrag der Leitung (17:06:58, date): Folgeversuch ohne Karte

- h-Gang (Takt-Transfermatrix fuer h = 1 bis 2^-10 auf V, B1 und Kuhn), gerechnet 15:44:26 bis 16:02:58 ohne Karte (Finn, 05.10. 15:38: "einfach machen"). Ergebnis in H-GANG.md; Zusammenfassung RUNDE-49.md (16:03:39). Keine Vorhersagen, keine Urteile; Karte nachgearbeitet auf Finns Wunsch ("Arbeite ggf die Karten dafuer nach").
