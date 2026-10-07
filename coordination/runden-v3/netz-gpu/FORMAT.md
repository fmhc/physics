# NETZ-GPU: gemeinsames Datenformat zwischen Rechenkern (.69, PyTorch/CUDA) und Ansicht (three.js)

- Leitung claude-primary, 05.10.2026. Anlass: Finn, "bau ein richtig ausgewachsenes nices ding mit den gpu funktionen fuer
  das gesamte modell" und "threejs mit collidern und einer physik engine die wir schreiben".
- Rechenkern schreibt, Ansicht liest. Alles kleine Endian, float32, sofern nicht anders gesagt. Keine Pickle-Dateien.

## Ordner eines Datensatzes

```
<datensatz>/
  manifest.json
  netz/ecken.f32        # N_e x 3 Ecklagen (Ruhelage, Einheit: kubische Kante a von V = 1)
  netz/kanten.u32       # N_k x 2 Eckindizes
  netz/dreiecke.u32     # N_d x 3 Eckindizes
  netz/tetraeder.u32    # N_t x 4 Eckindizes (optional)
  frames/000000/<groesse>.f32   # je Bild und Groesse ein Array
  frames/000001/...
```

## manifest.json

```json
{
  "format": "netz-gpu/1",
  "titel": "kurzer Name des Laufs",
  "erzeugt": "2026-10-05T17:30:00+02:00",
  "netz": {"typ": "V", "zellen": [8, 8, 8], "N_ecken": 5120, "N_kanten": 34816, "N_dreiecke": 59392, "N_tetraeder": 29696,
           "box": [8.0, 8.0, 8.0], "periodisch": true},
  "einheiten": {"laenge": "a (kubische Kante von V)", "zeit": "a/c (Eigenzeit der Zeltstangen)"},
  "groessen": [
    {"name": "skalar_betrag2", "ort": "ecke", "komponenten": 1, "bedeutung": "|phi|^2 des Q-Ball-Felds", "min": 0.0, "max": 1.2},
    {"name": "energie", "ort": "ecke", "komponenten": 1, "bedeutung": "Energiedichte je Ecke (alle Sektoren)", "min": 0.0, "max": 3.1},
    {"name": "dehnung", "ort": "kante", "komponenten": 1, "bedeutung": "relative Laengenaenderung delta l / l", "min": -1e-3, "max": 1e-3},
    {"name": "fluss", "ort": "dreieck", "komponenten": 1, "bedeutung": "Lichtfluss durch das Dreieck", "min": -0.5, "max": 0.5},
    {"name": "takt", "ort": "ecke", "komponenten": 1, "bedeutung": "Lapse N - 1", "min": -0.01, "max": 0.0},
    {"name": "rahmen", "ort": "ecke", "komponenten": 4, "bedeutung": "Einheitsquaternion (w, x, y, z) des Drehrahmens", "min": -1.0, "max": 1.0},
    {"name": "verschiebung", "ort": "ecke", "komponenten": 3, "bedeutung": "Anzeige-Verschiebung der Ecke (ueberhoeht)", "min": -0.1, "max": 0.1}
  ],
  "frames": [{"index": 0, "zeit": 0.0, "ordner": "frames/000000"}, {"index": 1, "zeit": 0.05, "ordner": "frames/000001"}],
  "diagnose": {"energie_gesamt": [1.0, 1.0], "ladung": [100.0, 100.0], "gauss_rest": [1e-14, 2e-14]},
  "quelle": {"code": "netzgpu Fassung", "lauf": "Pfad auf der .69", "hinweis": "synthetisch, keine Messdaten"}
}
```

- Jede Groesse ist optional; die Ansicht zeigt nur, was im Manifest steht.
- Bilddateien: frames/<index 6-stellig>/<name>.f32 mit Laenge (Anzahl Orte) x komponenten.
- "min" und "max" sind die festen Farbskalen ueber den ganzen Lauf, nicht je Bild.
- Groesse eines Datensatzes fuer die Ansicht: hoechstens 200 MB, Ziel 20 bis 60 MB (float32 reicht; bei vielen Bildern
  nur die gezeigten Groessen speichern).

## Regeln fuer den Rechenkern

- Vor jedem Lauf `df -h /home` pruefen; abbrechen, wenn weniger als 10 GB frei sind. Zwischenstaende begrenzen
  (hoechstens 2 GB je Lauf, aeltere ueberschreiben).
- Datensaetze fuer die Ansicht nach /home/fmh/fmhc-physics-remote/netz-gpu/datensaetze/<name>/ schreiben.
