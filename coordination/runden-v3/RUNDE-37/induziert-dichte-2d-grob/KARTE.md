# INDUZIERT-DICHTE-2D-GROB: Gegenprobe auf groeberem Netz bei gleichen Wellen (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 09:00:21 CEST (date), vor jeder Rechnung.
- **Anlass:** Gegenleser zu INDUZIERT-DICHTE-2D (RUNDE-37/induziert-dichte-2d/gegenlesen/GEGENLESEN.md): "TRAEGT MIT
  EINSCHRAENKUNG".
  - Der Wert -0,0123 ist im Kern eine Steigung mit Gewicht bei abs(k) ~ 0,3 und Netzabstand 1. Das k^4-Glied ist
    unbestimmt (d = -0,055 +- 0,062), fuer k -> 0 ergibt das 0,7 bis 1,2 P.
  - N = 16 000 gegen 64 000 hatte dieselbe Dichte (L = sqrt N) und prueft nur die Torusgroesse.
  - Empfohlene Gegenprobe: gleiche k (in Torus-Einheiten) auf einem groeberen Netz, N = 16 000 auf L = sqrt(64 000).
    Dann ist k in Netzabstaenden doppelt so gross, und d laesst sich auf etwa +-0,005 bestimmen.
- Kennzeichen: [M] Mathematik, [H] Hypothese.

## Test (Code-Agent)

- Code aus RUNDE-37/induziert-dichte-2d/code/ als Kopie mit L als eigenem Argument (L = sqrt N ist fest verdrahtet).
  Sonst nichts aendern: S = 0,5, Abbildung, Neuvernetzung, Messung und Ausgleich wie im eingefrorenen Plan.
- **Laeufe:**
  - (a) N = 16 000 auf L = sqrt(64 000) ~ 253, gleiche k-Werte in Torus-Einheiten wie der Hauptlauf (also abs(k) bis ~0,6
    in Netzabstaenden), so viele Saaten wie fuer +-0,005 in d noetig (vorab abschaetzen).
  - (b) zur Kontrolle derselbe Code mit L = sqrt N (N = 16 000) gegen den Hauptlauf.
- **Auswertung:**
  - c(k) gegen k^2 mit k^0-, k^2- und k^4-Glied ueber beide Dichten gemeinsam, in Netzabstands-Einheiten.
  - Daraus der Grenzwert k -> 0 der konformen Steifigkeit und d.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IG0 | Kontrolle (b): Der Kopie-Code mit L = sqrt N gibt den Hauptlauf (N = 16 000: -0,0131 +- 0,0022) innerhalb 2 SE wieder | 90 % |
| IG1 | d (k^4-Glied) ist auf <= +-0,01 bestimmt | 70 % |
| IG2 | [H] Der Grenzwert k -> 0 liegt zwischen 0,7 P und 1,2 P (P = -1/(24 pi)) | 60 % |
| IG3 | [H] Der Grenzwert liegt innerhalb 15 % von P | 35 % |

**Bedeutung (vorab):**
- **IG2 trifft ein:** Das 2D-Ergebnis haelt auch bei kurzer Netzweite relativ zur Welle. "Zahl = Volumen" gibt
  Polyakovs Antwort in der Groesse.
- **IG3 trifft ein:** Die Aussage darf auf "Polyakov innerhalb 15 %" verschaerft werden.
- **IG2 verfehlt:** Die Uebereinstimmung war eine Fenster-Steigung. Die Aussage bleibt bei "negativ, Polyakov-Groessenordnung".

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
