# Summe der Zaehler aus den "fertig"-Zeilen (eine JSON-Zeile je Lauf)
reduce .[] as $s ({}; reduce ($s|keys[]) as $k (.; .[$k] = ((.[$k] // 0) + (if $k == "r_maske_max" then 0 else $s[$k] end)))) 
