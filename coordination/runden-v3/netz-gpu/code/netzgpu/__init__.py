# -*- coding: utf-8 -*-
"""netzgpu: GPU-Rechenkern (PyTorch/CUDA) fuer Finns gefuelltes Tetraedernetz V (fmhc-physics, 05.10.2026).

Synthetische Modellrechnung, keine Messdaten. Module:
  netz       periodische Netze V, S, Kuhn (kubische Superzellen), Inzidenzen d0, d1, d2, gewichtete Hodge-Sterne
  licht      DEC-Maxwell mit Takt (Lapse) und Laengen
  skalar     komplexes Q-Ball-Feld (U(S) = S - S^2 + S^3/2), Ladung, Energie, stationaere Baelle
  rahmen     Drehrahmen-Feld (Einheitsquaternionen, Energie 4(1 - c^2) je Kante)
  kopplung   Takt N = 1 + Phi aus einer Quelle (Poisson auf dem Netz), konforme Laengen
  geometrie  Schwerewellen-Sektor der stetigen Grenze (spektral, je k)
  integrator Stoermer-Verlet, FIRE
  diagnose   Energie, Ladung, Gauss, Bloch-Reduktion (Tempo, Isotropie)
  datensatz  Schreiber fuer FORMAT.md (netz-gpu/1)
"""
FASSUNG = "netzgpu 0.1 (2026-10-05)"
