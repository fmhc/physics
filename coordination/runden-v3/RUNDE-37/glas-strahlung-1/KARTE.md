# GLAS-STRAHLUNG-1: Strahlen Finns Zufallsnetze Schwerewellen wie Einstein ab, unabhaengig von der Bahnlage? (Runde 48, Glas-Zweig, Folgekarte zu IMPULS-NETZ-1 und TT-GLAS-2)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 09:01:58 CEST (date), vor jeder Rechnung.
- **Finn (05.10.):** "Meine Tetraeder können zufällig und unregelmäßig sein."
- **Herkunft [P]:**
  - **IMPULS-NETZ-1:** Auf Netz V mit Impulskopplung G_rad/G_N = 1,030 / 1,004 / 0,967; Kreisbahnen je Lage -0,15 % bis +0,12 %, rund 12-mal ueber dem Doppelpulsar (1,3e-4). Der Rest sitzt im nn- und V1-Kanal.
  - **SKALAR-SEKTOR-L:**
    - Der Rest ist eine l = 4-Fehlkopplung ueber die Bewegungsenergie, kein Zusatzskalar.
    - GW170817 (~1e-15) ist fuer Kristallnetze die schaerfere Schranke.
  - **TT-GLAS-2:** Glasnetze sind stabil (112 k-Klassen, 24 Netze), die TT-Spanne faellt wie ~N^-0,5 (4,66 % bei N = 1024).
  - **Projekt-grep (09:01):** Abstrahlung ist auf Glasnetzen nie gerechnet worden.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Rechnung (Code-Agent)

- IMPULS-NETZ-1-Aufbau (Impulskopplung J, schwingender phi-Quadrupol, Kreisbahnen) auf den periodischen Glasnetzen aus TT-GLAS-1 und TT-GLAS-2: N = 128, 256 und 512, je mindestens 4 Saaten.
- Je Netz:
  - G_rad/G_N fuer drei Quellachsen und fuer mindestens 12 Bahnlagen
  - Mittelwert und Streuung ueber die Lagen
  - Anteile der Kanaele (TT, nn, V1)
- **Gewichte:** Hauptarm mit den Gewichten aus IMPULS-NETZ-1 (P1 fuer die Materie, Bewegungsgewichte wie TT-GLAS). Nebenarm, beschreibend: umkreisbasierte Gewichte, also der Takt-konsistente Fall (TAKT-UMKLAPP-1, HT0).
- Kontrolle: Der Code gibt auf Netz V die IMPULS-NETZ-1-Werte wieder.

## Ableitbarkeitsprobe (Leitung, verkettet)

- **Vorab ableitbar [M, P]:**
  - Die Impulsregel M^H p und die Kopplung M^H p = J sind auf jeder Triangulierung erster Klasse (IN1, Schreibtisch, netzunabhaengig) [P]. Das ist hier nur Kontrolle.
  - Ein statistisch homogenes und isotropes Glas hat im Grenzfall unendlicher Groesse keinen richtungsabhaengigen Anteil. Die Lagenstreuung ist ein Effekt endlicher Proben.
- **Nicht ableitbar:**
  - wie schnell die Lagenstreuung mit N faellt (fuer die TT-Spanne gemessen ~N^-0,5; die Leckage kann anders skalieren)
  - der **Mittelwert** von G_rad/G_N. Ein isotroper Rest, z. B. aus dem Energiekanal V1, verschwindet durch Mitteln nicht, und der Doppelpulsar prueft den Betrag.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GS0 | Kontrolle: Der Code gibt auf V die IMPULS-NETZ-1-Werte G_rad/G_N = 1,030 / 1,004 / 0,967 auf 1e-3 wieder | 90 % |
| GS1 | [H] Die Streuung von G_rad/G_N ueber die Bahnlagen faellt mit N mindestens wie N^-0,4 (Anpassung ueber N = 128 bis 512) | 60 % |
| GS2 | [H] Der Mittelwert ueber Lagen und Saaten liegt bei N = 512 innerhalb von 1e-3 bei 1 | 45 % |
| GS3 | [H] Der Energiekanal V1 traegt einen isotropen Rest, der mit N nicht faellt (Mittelwert-Abweichung bei N = 128 und 512 gleich auf 30 %) | 40 % |

**Bedeutung (vorab):**
- **GS1 trifft ein:** Im Glas-Zweig verschwindet die Lagenabhaengigkeit der Abstrahlung von selbst. GW170817 und die Lagen-Schranke des Doppelpulsars waeren dann ohne Abstimmung erfuellt [H].
- **GS2 trifft ein:** Auch der Betrag passt im Rahmen der Rechengenauigkeit. Der Doppelpulsar-Betrag (1,3e-4) braucht dann groessere N.
- **GS3 trifft ein:** Es bleibt ein isotroper Rest, die Energie-Regel (skalarer Sektor, V1) ist dann die naechste Baustelle, auch fuer Zufallsnetze.

## Rahmen

- Code-Agent, Code aus impuls-netz-1/code, tt-glas-1/code und tt-glas-2/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (dicht, wie TT-GLAS-2), sonst cpu und cpu7. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256). Ein ehrlicher Teilbericht ist besser als keiner: zuerst GS0 und N = 128.
- Synthetisch, keine Messdatenbestaetigung.
