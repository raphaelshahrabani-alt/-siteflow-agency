import csv, sys
sys.path.insert(0, "tools")
import build_prospecting_sheet as B

with open("montreal-kiosk-prospects.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["#","Tier","Category","Venue","Address","Phone","Email / web","Notes",
                "Status","Contact name","Last contact","Next step"])
    i = 1
    for tier, _c, title, _n, groups in B.TIERS:
        for cat, rows in groups:
            for name, addr, phone, web, note in rows:
                w.writerow([i, tier + " - " + title, cat, name, addr, phone, web, note, "", "", "", ""])
                i += 1
    for name, why in B.FOOT:
        w.writerow([i, "Tier 1 - Walk in this week", "Walk-the-strip category", name, "", "", "", why, "", "", "", ""])
        i += 1
    for name, addr, note in B.CLOSED:
        w.writerow([i, "Dropped", "Closed", name, addr, "", "", note, "CLOSED", "", "", ""])
        i += 1
print("rows:", i - 1)
