import re, html, base64, sys
sys.path.insert(0, "/home/claude/build")
from content import *

SRC = "/home/claude/src/maya_and_freedom.txt"
LOGO = "/home/claude/vedantanz-logo.png"
OUT = "/home/claude/out"
import os; os.makedirs(OUT, exist_ok=True)

lines = [l.strip() for l in open(SRC, encoding="utf-8").read().split("\n") if l.strip()]
paras = lines[2:]
assert len(paras) == 18, len(paras)

# Corrections (documented in EDITORIAL_NOTE)
p8 = paras[7]
assert "All that day, he was again at the house" in p8
paras[7] = p8.replace("All that day, he was again at the house",
                      "All that day he did not return to his Master. The next day, he was again at the house")
paras[11] = paras[11].replace("क्शुरस्य", "क्षुरस्य")
for i, old, new in [(4, "there appears of wall", "there appears a wall"),
                    (7, "with other two of his children", "with the other two of his children"),
                    (15, "the different is not one of kind", "the difference is not one of kind")]:
    assert old in paras[i], old
    paras[i] = paras[i].replace(old, new)
paras = [re.sub(r"\s*--\s*", " – ", p) for p in paras]
paras[11] = paras[11].replace("so the wise say-hard", "so the wise say – hard")

def esc(s): return html.escape(s, quote=False)

def para_html(i, p):
    t = esc(p)
    if i == 12:  # set the Sanskrit verse and translation apart
        m = re.search(r"(उत्तिष्ठत.*?॥ १४॥)\s*(Arise! Awake! Approach.*)$", t)
        if m:
            before = t[:m.start()].rstrip()
            return (f'<p class="lp"><span class="pn">¶{i}</span>{before}</p>'
                    f'<blockquote class="verse"><span class="dev">{m.group(1)}</span>'
                    f'<span class="tr">{m.group(2)}</span></blockquote>')
    return f'<p class="lp"><span class="pn">¶{i}</span>{t}</p>'

logo_b64 = base64.b64encode(open(LOGO, "rb").read()).decode()
LOGO_URI = f"data:image/png;base64,{logo_b64}"

def lecture_html():
    out = []
    for ptag, ptitle, secs in PARTS:
        out.append(f'<div class="part"><span class="ed-k">{ptag}</span><h2 class="ed">{esc(ptitle)}</h2></div>')
        for n, head, pnums in secs:
            out.append(f'<h3 class="ed"><span class="sn">{n}</span>{esc(head)}</h3>')
            for pn in pnums:
                out.append(para_html(pn, paras[pn - 1]))
    return "\n".join(out)

def summary_html():
    items = "".join(f'<li><strong>{esc(h)}.</strong> {esc(b)}</li>' for h, b in SUMMARY_POINTS)
    return f'<p class="intro">{esc(SUMMARY_INTRO)}</p><ol class="points">{items}</ol>'

def outline_html():
    rows = []
    for ptag, ptitle, secs in PARTS:
        rows.append(f'<li class="op"><span>{ptag}:</span> {esc(ptitle)}<ol>' +
                    "".join(f'<li value="{n}">{esc(h)} <em>(¶{", ".join(map(str,p))})</em></li>' for n, h, p in secs) +
                    '</ol></li>')
    return '<ul class="outline">' + "".join(rows) + '</ul>'

def glossary_html():
    return '<dl class="gloss">' + "".join(f'<dt>{esc(t)}</dt><dd>{esc(d)}</dd>' for t, d in GLOSSARY) + '</dl>'

def bridge_html():
    return (f'<p class="intro">{esc(BRIDGE_INTRO)}</p>' +
            "".join(f'<div class="bridge"><h4>{esc(h)}</h4><p>{esc(b)}</p></div>' for h, b in BRIDGE))

def questions_html():
    return '<ol class="qs">' + "".join(
        f'<li><span class="qk">{esc(k)}</span>{esc(q)}<div class="lines"></div></li>' for k, q in QUESTIONS) + '</ol>'

M = META
