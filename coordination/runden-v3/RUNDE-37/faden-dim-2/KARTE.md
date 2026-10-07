# FADEN-DIM-2: Verschiebt Rauheit die Dimensionsgrenze 3 der Faeden, wenn die Rauheit ueber L konstant bleibt und L bis 64 geht? (Runde 43, Fast Lane)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 21:58:27 CEST (date), vor jeder Rechnung.
- **Herkunft:** FADEN-DIM-1 (RUNDE-37/faden-dim-1/ERGEBNIS.md, Ernte in RUNDE-43.md).
  - F2 traf nach Plan knapp ein: Grenze 4 bei Rauheit p = 0,6, D = 4, Steigung -0,20 ueber L = 8 bis 32, Schwelle -0,25.
  - Nach Kartenwortlaut traf F2 nicht ein.
  - Die Steigung wird mit L steiler: -0,18 (L = 8 bis 16), dann -0,27 (L = 16 bis 32).
  - Luecke im Plan: Geschlossene Faeden haben bei kleinem L weniger Knicke (bis 0,33 statt 0,6). Die Rauheit wuchs also mit L.
- **Finn (04.10. abends):** Pendeln sich die Dimensionen bei 3 bis 4 ein? Bis wann bleibt was stabil?
- Kennzeichen: [M] Mathematik, [E] Rechnung, [L] Gedaechtnis, [H] Hypothese.

## Ableitbarkeitsprobe (Leitung, Schreibtisch, vor der Karte)

- **Glatt (G), bekannt:** Der Querabstand der Faeden ist eine Irrfahrt in d = D - 1 Richtungen.
  - Treffen bis T = 4 L^2 auf dem Torus: P ~ T/L^d = L^(3-D) fuer D >= 4. So war es in FADEN-DIM-1 (-0,86 / -1,85 / -2,92).
- **Rau (RP) [M, Leitung, ungeprueft]:**
  - Der relative Querverlauf zweier rauer Faeden ist eine Irrfahrt-Bruecke mit etwa 2 p L Querschritten.
  - Die starre Verschiebung bewegt sie als Ganzes; Treffen heisst, dass die Verschiebung die Spur der Bruecke trifft.
  - Das gibt P ~ T cap(Spur)/L^d.
  - Kapazitaet der Spur einer Irrfahrt mit n Schritten (Lawler [L]): ~ n^(1/2) in d = 3, ~ n/log n in d = 4, ~ n in d >= 5.
  - **Folgerung fuer die Trefferrate:**
    - D = 4: ~ L^(-1/2), statt L^(-1) bei glatten Faeden.
    - D = 5: ~ L^(-1)/log L, statt L^(-2).
    - D = 6: ~ L^(-2), statt L^(-3).
  - Rauheit macht den Abfall also flacher, aber in jedem D >= 4 faellt P weiter. Die Grenze 3 bleibt asymptotisch.
  - FADEN-DIM-1 passt grob dazu: Rate nach Sicht ~ L^-0,6 (rau) gegen L^-1,1 (glatt) bei D = 4; Steigungen -0,885 (D = 5) und -1,84 (D = 6).
- **Was daraus folgt:**
  - Die Richtung von FD1 und FD2 ist ableitbar, wenn diese Skizze stimmt. Die Karte prueft die Skizze an groesserem L, mit Rauheit, die ueber L konstant gehalten wird.
  - Die Zahlenwerte bei endlichem L sind nicht ableitbar (Saettigung bei P nahe 1, Ortsbewegung der Bruecke).

## Auftrag (Code-Agent)

1. **Code:** faden-dim-1/code/faden.py kopieren, dort nichts aendern.
2. **Konstante Rauheit:** kappa je (D, L) so waehlen, dass die gemessene mittlere Knickdichte der geschlossenen Faeden 0,6 ist.
   - Kalibrierlaeufe vor dem Einfrieren sind erlaubt, wenn sie nur Knickdichte und kappa ausgeben, keine Treffzahlen.
   - Toleranz im Plan festlegen.
3. **Laeufe:**
   - D = 4: RP mit L = 16, 24, 32, 48, 64 und G mit L = 32, 48, 64.
   - Beschreibend: D = 5, RP mit L = 8, 12, 16, 24, soweit das Budget reicht.
   - T = 4 L^2 wie in FADEN-DIM-1. Paarzahl je L im Plan nach Budget, mindestens 512 bei D = 4.
4. **Auswertung:**
   - Treffanteil P mit Wilson-Intervall.
   - Lokale Steigung d ln P / d ln L zwischen L = 32 und 64.
   - Rate -ln(1 - P) mit Exponent ueber L = 16 bis 64 (gewichtete Gerade, Bootstrap).
   - Knickdichte am Start und am Ende.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| FD0 | Kontrolle: G bei D = 4 gibt P L zwischen L = 32 und 64 konstant bis Faktor 1,5 | 85 % |
| FD1 | [H, M Kapazitaet] RP mit konstanter Rauheit 0,6 bei D = 4: Exponent der Rate -ln(1 - P) ueber L = 16 bis 64 zwischen -0,75 und -0,35 | 60 % |
| FD2 | [H] RP mit konstanter Rauheit 0,6 bei D = 4: lokale Steigung von P zwischen L = 32 und 64 unter -0,25, nach der Schwellregel von FADEN-DIM-1 also Grenze 3 | 75 % |

**Bedeutung (vorab):**
- **FD1 und FD2 treffen ein:** Raue Faeden treffen sich in 4 Raumdimensionen leichter, aber mit wachsender Groesse immer seltener.
  - Die Grenze 3 fuer Faeden (Brandenberger/Vafa) ist robust gegen Rauheit.
  - Rauheit halbiert ungefaehr den Abfallsexponenten [H].
- **FD2 verfehlt:** Auch bei L = 64 und konstanter Rauheit bleibt der Abfall flacher als die Schwelle.
  - Die Frage nach der Grenze 4 bleibt dann offen.
  - Die Kapazitaets-Skizze waere fuer diese Groessen falsch oder unvollstaendig (Ortsbewegung der Bruecke).
- **FD1 verfehlt bei eingetroffenem FD2:** Die Grenze bleibt 3, aber die Skizze trifft den Exponenten nicht.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu10. cpu2 meiden, dort liegt ein Codex-Lock.
- Je Lauf hoechstens 10 min, 1 Thread. Zeitbox 60 min.
