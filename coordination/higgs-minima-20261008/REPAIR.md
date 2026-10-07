# QA-Abbruch vor der ersten Relaxation

Der erste Lauf brach im unabhängigen Gradientenvergleich vor jeder Relaxation ab.
Die QA-Metrik war versehentlich float32, sodass die skalare Vormultiplikation
rundete, obwohl Energie und Gradient float64 waren. Korrektur ausschließlich:
`torch.tensor([1.,1.,.5],device='cuda',dtype=torch.float64)`.
Der alte Code und die erste Provenienz bleiben in initial-failure erhalten.
Plan, Parameter, Toleranzen und Rechenweg unverändert. Keine Ergebnisdaten
werden überschrieben; erneuter Start nach neuem Codehash.
