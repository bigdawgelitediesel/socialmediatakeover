"""Merge top100-input.csv with the five why-*.tsv files into top100.tsv and an .xlsx Jacob can open.
usage: python -I build_sheet.py [xlsx_out]"""
import csv, io, sys, statistics, collections
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter

inp = list(csv.DictReader(open("top100-input.csv", encoding="utf-8")))
why = {}
for k in "ABCDE":
    for r in csv.DictReader(io.open(f"why-{k}.tsv", encoding="utf-8-sig"), delimiter="\t", quoting=csv.QUOTE_NONE):
        why[r["id"]] = r
COLS = [("Account", 18), ("Rank", 6), ("Link", 14), ("Views", 12), ("Sent %", 8), ("x their usual", 10), ("Seconds", 8), ("Format", 20),
        ("First 3 seconds", 46), ("Hook (said or on screen)", 40), ("Why it went viral", 60), ("Who sends it, to whom", 36),
        ("Shape you can borrow alone", 50), ("Watched", 8), ("Posted", 11)]
rows = []
for r in inp:
    w = why[r["id"]]
    rows.append([r["handle"], int(r["rank"]), r["url"], int(r["views"]), float(r["share_pct"] or 0), float(r["times_median"] or 0),
                 int(float(r["duration_s"] or 0)), w["format"], w["first_3_seconds"], w["spoken_or_text_hook"], w["why_it_went_viral"],
                 w["who_shares_it_and_to_whom"], w["shape_jacob_can_borrow_alone"], w["watched"], r["date"]])
with open("top100.tsv", "w", encoding="utf-8", newline="") as f:
    cw = csv.writer(f, delimiter="\t"); cw.writerow([c for c, _ in COLS]); cw.writerows(rows)

wb = Workbook(); ws = wb.active; ws.title = "100 posts"
ws.append([c for c, _ in COLS])
head = PatternFill("solid", fgColor="1B1510")
for i, (c, wd) in enumerate(COLS, 1):
    cell = ws.cell(1, i); cell.font = Font(bold=True, color="C9B38C"); cell.fill = head
    cell.alignment = Alignment(wrap_text=True, vertical="center"); ws.column_dimensions[get_column_letter(i)].width = wd
for r in rows:
    ws.append(r); n = ws.max_row
    link = ws.cell(n, 3); link.value = "open"; link.hyperlink = r[2]; link.font = Font(color="0563C1", underline="single")
    ws.cell(n, 4).number_format = "#,##0"; ws.cell(n, 5).number_format = "0.00"; ws.cell(n, 6).number_format = "0.0"
    for c in range(1, len(COLS) + 1): ws.cell(n, c).alignment = Alignment(wrap_text=True, vertical="top")
    if r[10].lower().startswith("avoid"):
        for c in range(1, len(COLS) + 1): ws.cell(n, c).fill = PatternFill("solid", fgColor="F4D6D6")
    elif r[4] >= 2.0:
        ws.cell(n, 5).fill = PatternFill("solid", fgColor="D9EAD3")
ws.freeze_panes = "D2"; ws.auto_filter.ref = ws.dimensions

# sheet 2: by format
ws2 = wb.create_sheet("By format")
ws2.append(["Format", "Posts", "Typical sent %", "Typical views", "Best sent %"])
d = collections.defaultdict(list)
for r in rows: d[r[7]].append(r)
for fmt, v in sorted(d.items(), key=lambda kv: -statistics.median(x[4] for x in kv[1])):
    ws2.append([fmt, len(v), round(statistics.median(x[4] for x in v), 2), int(statistics.median(x[3] for x in v)), max(x[4] for x in v)])
for i, wd in enumerate([28, 8, 14, 14, 12], 1):
    ws2.column_dimensions[get_column_letter(i)].width = wd; ws2.cell(1, i).font = Font(bold=True)
for row in ws2.iter_rows(min_row=2):
    row[3].number_format = "#,##0"

# sheet 3: top 20 by sent %
ws3 = wb.create_sheet("Most sent")
ws3.append(["Account", "Link", "Views", "Sent %", "Format", "Hook", "Why", "Shape you can borrow alone"])
keep = [r for r in rows if not r[10].lower().startswith("avoid")]
for r in sorted(keep, key=lambda x: -x[4])[:20]:
    ws3.append([r[0], "open", r[3], r[4], r[7], r[9], r[10], r[12]]); n = ws3.max_row
    ws3.cell(n, 2).hyperlink = r[2]; ws3.cell(n, 2).font = Font(color="0563C1", underline="single"); ws3.cell(n, 3).number_format = "#,##0"
    for c in range(1, 9): ws3.cell(n, c).alignment = Alignment(wrap_text=True, vertical="top")
for i, wd in enumerate([18, 8, 12, 8, 20, 40, 60, 50], 1):
    ws3.column_dimensions[get_column_letter(i)].width = wd; ws3.cell(1, i).font = Font(bold=True)
out = sys.argv[1] if len(sys.argv) > 1 else "top100.xlsx"
wb.save(out); print("wrote", out, len(rows), "rows")
for r in sorted(keep, key=lambda x: -x[4])[:12]:
    print("%.2f%%  %-16s %-22s %s" % (r[4], r[0], r[7], r[9][:70].encode("ascii", "replace").decode()))
