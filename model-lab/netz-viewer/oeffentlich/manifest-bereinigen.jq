# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
# Oeffentliche Kopie eines netz-gpu/1-Manifests: interne Pfade (lauf, skript) und Kartenkennungen
# in Klammern entfernen, neutrale Herkunft setzen. Aufruf: jq --arg herkunft "..." -f manifest-bereinigen.jq manifest.json
def ohne_kennung: gsub(" ?\\([A-Z][A-Z0-9]*(-[A-Z0-9]+)+\\)"; "");
.quelle |= (
  { code: (.code // "netzgpu 0.1"), herkunft: $herkunft }
  + (del(.lauf, .skript, .code)
     | with_entries(if (.value | type) == "string" then .value |= ohne_kennung else . end))
)
