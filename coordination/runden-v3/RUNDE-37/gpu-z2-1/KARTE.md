# GPU-Z2-1: Gibt eine GPU-Fassung der Spin-Schwellenrechnung die CPU-Werte genau wieder, und wie schnell ist sie? (Runde 49, Vorstufe zu Z2-SCHUTZ-3)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 15:35:51 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - Finn, 05.10.2026: "wie bekommen wir eine große rechnung hochgradig performant auf einer gpu hin?"
  - Z2-SCHUTZ-2: Die Barriere waechst bei festem Kern stark mit der Kugel (25,0 / 45,6 / 76,8 bei R = 20 / 24 / 32). Ob sie
    bei groesserem R saettigt, ist offen. (10, 32) mit 150 713 Knoten lag schon an der 10-min-Wandzeit der CPU-Spuren.
  - Code: RUNDE-37/z2-schutz-2/code (z2s2.py, z2.py, guertel2.py, finn.py; reines numpy, CPU).
  - Rechner .69 (nvidia-smi, 15:33): 2 x Quadro P4000 (8 GB), 1 x Quadro P5000 (16 GB), Pascal (Rechenfaehigkeit 6.1).
    Belegt durch ruhende Fremddienste 5,5 / 5,8 / 11,2 GB, Auslastung 0 %.
- Kennzeichen: [M], [E], [P], [ES], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab [M, ES]:**
  - Die Guertel-Energie je Bindung haengt nur von zwei Nachbarquaternionen ab: 4 (1 - (q_i . q_j)^2).
  - Gradient und FIRE-Schritt sind daher Nachbarsummen. Mit etwa 26 Rechenoperationen auf 128 Byte je Bindung in FP64 ist
    die Rechnung durch den Speicher begrenzt, nicht durch die Rechenleistung. Doppelte Genauigkeit kostet auf Pascal
    deshalb nur etwa die doppelte Bytezahl, nicht den Faktor 32 der FP64-Rechenleistung.
  - Grobe Erwartung [ES]: P4000 etwa 240 GB/s. Bei 150 713 Knoten (etwa 300 000 Bindungen) dauert ein Gradient unter 1 ms.
- **Nicht ableitbar:**
  - die tatsaechliche Geschwindigkeit samt Startkosten der Kernel und Atomics
  - ob die Pfadsuche (CI-NEB, Bisektion) auf der GPU dieselben Saettel findet
  - der Speicherbedarf bei gebuendelten Bildern
  - ob torch mit CUDA fuer Pascal auf der .69 bereitsteht

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GZ0 | Kontrolle [P]: Die GPU-Fassung (FP64) gibt E_S fuer (10, 20), (10, 24) und (8, 24) auf 1e-10 relativ und die gueltigen Barrieren 25,0284 / 45,59 / 33,89 aus Z2-SCHUTZ-2 auf 1e-4 relativ wieder | 80 % |
| GZ1 | [ES] Ein Gradient bei (10, 32) ist auf einer P4000 mindestens 30-mal schneller als im CPU-Code bei gleicher Genauigkeit (FP64) | 70 % |
| GZ2 | [ES] Eine ganze Barrierenrechnung bei (10, 32) (Start S, Pfadsuche, Sattelpruefung) laeuft auf p4000a in hoechstens 10 min Wandzeit durch und gibt 76,8 auf 1e-3 relativ wieder | 60 % |

- **Messziel ohne Vorhersage:** Laufzeit und Speicher je Knoten und je Pfadbild. Daraus eine Hochrechnung fuer
  (10, 40), (10, 48), (10, 64) und (10, 96) auf P4000 und P5000, jeweils mit dem heute freien Speicher.

**Bedeutung (vorab):**
- **GZ0 und GZ2 treffen ein:** Die GPU-Fassung ist fuer Z2-SCHUTZ-3 freigegeben (Saettigung der Barriere bei festem Kern,
  R bis 64 oder 96). Die grosse Rechnung braucht Finns Budget-Freigabe und den gemeinsamen Lock.
- **GZ0 verfehlt:** keine grossen Rechnungen; zuerst die Abweichung klaeren.

## Rahmen

- Code-Agent. Code aus RUNDE-37/z2-schutz-2/code kopieren, dort nichts aendern. Der Netzbau (finn.py) darf auf der CPU
  bleiben. Energie, Gradient, FIRE, Pfadsuche und Sattelpruefung kommen auf die GPU.
- **Hinweise der Leitung (Zusatz, keine Vertragsvorgabe):**
  - Alles bleibt auf der Karte; je Schritt nur Kontrollzahlen zurueckholen.
  - Nachbarschaften als Indexlisten (gather plus index_add_) oder als zwei Teilgitter mit festen Versaetzen ohne Atomics.
  - Alle Pfadbilder in einem Tensor buendeln.
  - Energien als Summe der Aenderungen gegen den Referenzzustand S in FP64.
  - Sattelpruefung mit Lanczos ueber Hesse-Vektor-Produkte statt voller Hesse-Matrix.
  - Zwischenstaende speichern.
  - torch.compile bzw. Triton laufen auf Pascal nicht; eager PyTorch oder CuPy-Kernel verwenden.
- **Umgebung:**
  - Zuerst per Rauchtest pruefen, ob in der Physik-Umgebung auf der .69 torch mit CUDA fuer Pascal (cu118/cu121)
    importierbar ist und die Karte sieht.
  - Fehlt das: nichts in gemeinsame Umgebungen installieren, sondern die Leitung fragen. Eine eigene Umgebung nur in
    /home/fmh/fmhc-physics-remote/gpu-z2-1/ und erst nach Rueckfrage.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (GPU). Keine Laeufe auf der P5000 in dieser Karte.
  Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256). Die CPU-Werte aus Z2-SCHUTZ-2 sind Referenz, keine Vorhersage.
- Synthetisch (Modellfeld), keine Messdatenbestaetigung.

## Vermerk der Leitung (17:06:58, date)

- Seit 15:38 (Finn: "jo ne nicht als karte sondern einfach machen") ist diese Karte nicht mehr bindend: kein Einfrieren, keine Urteile, kein Leser. Der Agent baut die GPU-Fassung, gleicht sie einmal mit der CPU ab und rechnet grosse Kugeln (R = 40, 48, 64, wenn moeglich 80, 96) bei r0 = 10. Die Vorhersagen GZ0 bis GZ2 werden nicht beurteilt.
