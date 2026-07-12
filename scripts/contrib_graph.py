#!/usr/bin/env python3
"""6-month contribution graph -> SVG. Weekly buckets, matrix-green, month labels."""
import re, sys, datetime, urllib.request

USER  = sys.argv[1] if len(sys.argv) > 1 else "keshavjha005"
OUT   = sys.argv[2] if len(sys.argv) > 2 else "dist/github-contrib-6mo.svg"
WEEKS = 26  # ~6 months

req = urllib.request.Request(f"https://github.com/users/{USER}/contributions",
                             headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")

ids = dict(re.findall(r'data-date="(\d{4}-\d{2}-\d{2})"\s+id="(contribution-day-component-\d+-\d+)"', html))
ids = {v: k for k, v in ids.items()}
tips = re.findall(r'<tool-tip[^>]*\bfor="(contribution-day-component-\d+-\d+)"[^>]*>(.*?)</tool-tip>', html, re.S)
daily = {}
for cid, text in tips:
    d = ids.get(cid)
    if d:
        m = re.search(r'(\d+)\s+contribution', text)
        daily[d] = int(m.group(1)) if m else 0
if not daily:
    sys.exit("ERROR: parsed 0 days")

today = datetime.date.today()
end   = today - datetime.timedelta(days=(today.weekday() + 1) % 7)
start = end - datetime.timedelta(weeks=WEEKS - 1)

series = []
for w in range(WEEKS):
    ws = start + datetime.timedelta(weeks=w)
    series.append((ws, sum(daily.get((ws + datetime.timedelta(days=i)).isoformat(), 0) for i in range(7))))

total = sum(v for _, v in series)
W, H = 1000, 300
L, R, T, B = 60, 26, 58, 48
pw, ph = W - L - R, H - T - B
ymax = -(-max(max(v for _, v in series), 1) // 50) * 50

Xf = lambda i: L + pw * i / (len(series) - 1)
Yf = lambda v: T + ph - ph * v / ymax
pts  = [(Xf(i), Yf(v)) for i, (_, v) in enumerate(series)]
line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
area = f"{L},{T+ph} " + line + f" {L+pw},{T+ph}"

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI,Ubuntu,sans-serif">',
 '<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">'
 '<stop offset="0%" stop-color="#00FF41" stop-opacity=".42"/>'
 '<stop offset="100%" stop-color="#00FF41" stop-opacity="0"/></linearGradient></defs>',
 f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="6" fill="#0D1117" stroke="#00FF41" stroke-width="1.5"/>',
 f'<text x="{W/2}" y="27" fill="#00FF41" font-size="16" font-weight="700" text-anchor="middle">Contribution Graph</text>',
 f'<text x="{W/2}" y="45" fill="#8B949E" font-size="11" text-anchor="middle">'
 f'Last 6 Months &#183; weekly &#183; {start.strftime("%b %Y")} &#8594; {today.strftime("%b %Y")}</text>']

for k in range(5):
    v = ymax * k / 4; y = Yf(v)
    s.append(f'<line x1="{L}" y1="{y:.1f}" x2="{L+pw}" y2="{y:.1f}" stroke="#00FF41" stroke-opacity=".12" stroke-dasharray="3 3"/>')
    s.append(f'<text x="{L-10}" y="{y+4:.1f}" fill="#00FF41" font-size="11" text-anchor="end">{int(v)}</text>')

seen = set()
for i, (d, _) in enumerate(series):
    if d.month not in seen:
        seen.add(d.month); x = Xf(i)
        if i: s.append(f'<line x1="{x:.1f}" y1="{T}" x2="{x:.1f}" y2="{T+ph}" stroke="#00FF41" stroke-opacity=".20"/>')
        s.append(f'<text x="{x+4:.1f}" y="{T+ph+21}" fill="#00FF41" font-size="12" font-weight="600">{d.strftime("%b")}</text>')

s.append(f'<polygon points="{area}" fill="url(#g)"/>')
s.append(f'<polyline points="{line}" fill="none" stroke="#00FF41" stroke-width="2.2" stroke-linejoin="round"/>')
for x, y in pts:
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="#FFFFFF"/>')

pi = max(range(len(series)), key=lambda i: series[i][1])
s.append(f'<text x="{Xf(pi):.1f}" y="{Yf(series[pi][1])-11:.1f}" fill="#FFFFFF" font-size="11" font-weight="700" text-anchor="middle">{series[pi][1]}</text>')
s.append(f'<text x="{L}" y="{H-13}" fill="#8B949E" font-size="11">Weekly contributions</text>')
s.append(f'<text x="{L+pw}" y="{H-13}" fill="#00FF41" font-size="11" font-weight="600" text-anchor="end">{total} contributions in 6 months</text>')
s.append('</svg>')
open(OUT, "w").write("\n".join(s))
print(f"wrote {OUT} | {start} -> {today} | {total} contributions")
