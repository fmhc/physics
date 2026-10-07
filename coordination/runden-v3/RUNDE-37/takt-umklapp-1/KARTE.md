# TAKT-UMKLAPP-1: Ist Finns Takt der Hodge-Laplace des Netzes, und bleibt das Netz stabil, wenn Delaunay entscheidet, welche Zelle umklappt? (Runde 47, Finn-Auftrag Umklappen, Folgekarte)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 07:20:29 CEST (date), vor jeder Rechnung.
- **Finn (05.10.):** "Zellen umklappen - wie und mit welchem Mechanismus? Try it."
- **Herkunft:**
  - **Teil A** ist der Kartenvorschlag HODGE-TAKT-1 aus HODGE-L (RUNDE-37/hodge-l/DOSSIER.md, Abschnitt 7). HT0 bis HT3 und die Ableitbarkeitsprobe sind **woertlich bindend**; HT1 ist dort schon durchgestrichen und durch HT1' ersetzt.
  - **Teil B (Zusatz Leitung)** ist der Mechanismus-Vorschlag aus UMKLAPP-1 [H]: Umklappen als Taktschritt (M-C), Delaunay waehlt die Flaeche (M-B).
    - UMKLAPP-1 zeigt: Zufaelliges Umklappen erzeugt wachsende Moden, etwa eine negative Regge-Richtung je fuenf Zuege.
    - V wird nach 12 Delaunay-Zuegen je Zelle Delaunay, bleibt stabil, die Spanne waechst aber von 6,3 auf 15,4 % [E, P].
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Teil A (woertlich aus HODGE-L, Abschnitt 7)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| HT0 | Kontrolle, vorab ableitbar: Auf V und S gilt P = -W^H B W = c d0^T *1 d0 mit einem festen c an allen k (auf 1e-10). Grundlage Glickenstein Satz 34, flach. Kann scheitern, wenn W nicht die Eckskalierung mit Kantenmitten ist oder anders normiert | 75 % |
| HT1' | [H] Auf V sind trotz der negativen *2 alle *1-Eintraege > 0, passend zu P > 0 [P]. V_D (V nach den 12 symmetrischen 2-3-Zuegen je Zelle) ist Delaunay. S: offen | 55 % |
| HT2 | [H] Nach f = 0,2 zufaelligen 2-3-Zuegen (UMKLAPP-1-Netze) gibt es negative *2-Eintraege, und P bleibt trotzdem an allen k positiv semidefinit (Doehrman/Glickenstein-Tendenz) | 55 % |
| HT3 | Folge, vorab ableitbar: Bekommt P eine negative Richtung, hat B auf der Zwangsflaeche der Eckregel genau so viele negative Moden mehr (Haynsworth), sofern B seine Zahl negativer Richtungen behaelt | 85 % |

- **Ableitbarkeitsprobe (woertlich, gekuerzt):**
  - Ableitbar: HT0 (Satz) und HT3 (lineare Algebra), nur Kontrollen; V nicht gut zentriert und nicht Delaunay [M].
  - Nicht ableitbar: Vorzeichen von *1 auf V, Delaunay-Eigenschaft von V_D und S (HT1'), Vorzeichen nach Zuegen (HT2), Zahl negativer Richtungen von B nach Zuegen.
  - Die Konstante c ist vorab unbekannt (Erwartung 8 [H]) und geht in kein Urteil ein.

## Teil B (Zusatz Leitung): gesteuertes Umklappen als Taktschritt

- **Rechnung:**
  - Auf Glasnetzen (N = 128, 12 Saaten wie TT-GLAS-1) und auf V die Ecken zufaellig um a = 1e-3 bzw. 1e-2 verschieben.
  - Dann **nur die Zuege ausfuehren, die Delaunay wiederherstellen** (M-B waehlt).
  - Danach TT-Spektrum, Stabilitaet und Zahl negativer Richtungen wie in UMKLAPP-1.
  - Vergleich mit gleich vielen zufaelligen Zuegen.
- **Vorhersage:**

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TU1 | [H] Delaunay-gesteuerte Zuege lassen das Netz in mindestens 90 % der Faelle stabil (keine wachsenden Moden), gleich viele zufaellige Zuege nicht | 55 % |

- **Ableitbarkeitsprobe:**
  - Delaunay macht die Hodge-Sterne in 3D positiv (Hirani u. a. 2013) [S]. Ob das die Regge-Bewegungsstabilitaet sichert, ist nicht ableitbar; V ist stabil, ohne Delaunay zu sein (UMKLAPP-1).
  - Nicht ableitbar: TU1.

**Bedeutung (vorab):**
- **HT0 trifft ein:** Finns Takt ist der Hodge-Laplace des Netzes (Mathematik statt Setzung).
- **TU1 trifft ein:** Mit Delaunay als Auswahlregel ist Umklappen ein stabiler Taktschritt. Das ist ein Mechanismus fuer Finns "Zellen umklappen".
- **TU1 verfehlt:** Auch gesteuertes Umklappen braucht mehr, etwa eine Energie- bzw. Wirkungsbedingung (Bezug L10).

## Rahmen

- Code-Agent; Code aus umklapp-1/code, materie-netz-1/code und hodge-l (falls Code) kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (mit TT-GLAS-2 geteilt, Lock), sonst cpu3 bzw. cpu4. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Ein ehrlicher Teilbericht ist besser als keiner: zuerst Teil A (HT0, HT1'), dann Teil B.
