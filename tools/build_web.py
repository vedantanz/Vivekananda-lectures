import sys, json, html, re, base64
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_core as _bc
from content import *
import build_core as B
from themes import theme_for
T = theme_for(B.META['guide_no'])

M = META
esc = B.esc

def lecture():
    out = []
    for ptag, ptitle, secs in PARTS:
        out.append(f'<div class="part"><span class="k">{ptag}</span><h2 class="ed">{esc(ptitle)}</h2></div>')
        for n, head, pnums in secs:
            out.append(f'<h3 class="ed" id="s{n}"><span class="sn">{n}</span>{esc(head)}</h3>')
            for pn in pnums:
                out.append(B.para_html(pn, B.paras[pn - 1]))
    return "\n".join(out)

toc = "".join(
    f'<li><span class="k">{p}</span> {esc(t)}<ol>' +
    "".join(f'<li value="{n}"><a href="#s{n}">{esc(h)}</a></li>' for n, h, _ in secs) + "</ol></li>"
    for p, t, secs in PARTS)

qs = "".join(f'<li><span class="k">{esc(k)}</span>{esc(q)}</li>' for k, q in QUESTIONS)

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Maya and Freedom</title>
<meta name="description" content="Study guide to Swami Vivekananda's lecture Maya and Freedom (London, 1896): summary, sectioned text, glossary, Bridge to Wellbeing and reflection questions.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400&family=Noto+Serif+Devanagari&display=swap" rel="stylesheet">
<style>
:root{{--ac:{T['accent']};--deep:{T['deep']};--soft:{T['soft']};--glow:{T['glow']};--goldl:#E9C987;--maroon:#6B1414;--gold:#9C6B14;--ink:#2a2420;--muted:#6d625a;--bg:#fffdf8;--tint:{T['soft']};--rule:#e6dccb;--card:#fff}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--maroon:#e6a3a3;--gold:#d9ad5b;--ink:#ece6df;--muted:#b5aaa0;--bg:#1b1715;--tint:#2a2320;--rule:#3d3430;--card:#221d1a;--deep:#e3ebf3;--soft:#1f2933;--ac:{T['glow']}}}}}
:root[data-theme="dark"]{{--maroon:#e6a3a3;--gold:#d9ad5b;--ink:#ece6df;--muted:#b5aaa0;--bg:#1b1715;--tint:#2a2320;--rule:#3d3430;--card:#221d1a;--deep:#e3ebf3;--soft:#1f2933;--ac:{T['glow']}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:Lora,Georgia,serif;font-size:15px;line-height:1.75}}
.wrap{{max-width:720px;margin:0 auto;padding:0 16px 64px}}
header.hero{{position:relative;overflow:hidden;text-align:left;padding:24px 16px 30px;min-height:460px;border-bottom:3px solid var(--goldl);color:#fff;
background:radial-gradient(circle at 50% 30%, {T['glow']} 0%, {T['accent']} 38%, {T['deep']} 100%)}}
header.hero .org,header.hero .series{{color:var(--goldl)}} header.hero h1{{color:#fff}} header.hero .del{{color:#e8e0d4}}
header.hero .badge{{border-color:var(--goldl);color:var(--goldl)}}
.heroart{{position:absolute;right:-125px;bottom:0;height:430px;width:auto !important;opacity:.8;pointer-events:none}} .hshade{{position:absolute;inset:0;background:linear-gradient(to right,{T['deep']} 42%,rgba(0,0,0,0) 80%);opacity:.85}} .brandrow{{display:flex;align-items:center;gap:10px}} .htext{{max-width:62%;margin-top:70px}} @media (min-width:600px){{.heroart{{right:4%}} .htext{{max-width:55%}}}} header.hero>*:not(.heroart){{position:relative}}
.plate{{display:flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:50%;background:#fffdf8;box-shadow:0 0 0 2px var(--goldl);flex:none}}
.plate img{{height:44px !important;width:auto !important;margin:0}}
header img{{width:110px;height:auto}}
.org{{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--maroon)}}
.series{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-top:14px}}
h1{{font-size:34px;line-height:1.08;color:var(--maroon);margin:8px 0 4px}}
.by{{font-style:italic}} .del{{color:var(--muted);font-size:13.5px}}
.badge{{display:inline-block;margin-top:12px;border:1px solid var(--gold);color:var(--gold);font-size:11px;letter-spacing:.14em;text-transform:uppercase;padding:3px 10px}}
nav.tabs{{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--rule);overflow-x:auto;white-space:nowrap}}
nav.tabs a{{display:inline-block;padding:12px 12px;color:var(--ac);text-decoration:none;font-size:14px}}
section{{padding-top:28px}}
h2.t{{font-size:21px;color:var(--deep);margin:0 0 8px}}
.k{{display:block;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold)}}
.intro{{font-style:italic;color:var(--muted)}}
ol.points li{{margin-bottom:10px}} ol.points strong{{color:var(--deep)}}
.note{{background:var(--tint);border-left:3px solid var(--gold);padding:12px 14px;font-size:13.5px;line-height:1.6}}
.toc ol{{padding-left:22px}} .toc>ol{{list-style:none;padding:0}} .toc a{{color:var(--ink)}}
.toc>ol>li{{margin-bottom:10px;font-weight:700;color:var(--maroon)}} .toc ol ol{{font-weight:400}}
.part{{margin:32px 0 8px;background:var(--ac);color:#fff;border-radius:10px;padding:14px 16px}} .part .k{{color:var(--goldl)}}
h2.ed{{font-size:19px;color:#fff;margin:2px 0 0}}
h3.ed{{font-size:17px;color:var(--ac);margin:22px 0 6px;scroll-margin-top:56px}}
h3.ed .sn{{display:inline-block;min-width:26px;font-weight:400}}
p.lp{{margin:0 0 14px}} .pn{{font-size:11px;color:var(--ac);margin-right:6px;vertical-align:1px}}
blockquote.verse{{margin:8px 0 16px;padding:12px 14px;border-left:3px solid var(--maroon);background:var(--tint)}}
.dev{{display:block;font-family:"Noto Serif Devanagari",serif;color:var(--maroon);font-size:16px;line-height:1.8}}
.tr{{display:block;font-style:italic;margin-top:6px}}
dl dt{{font-weight:700;color:var(--maroon);margin-top:12px}} dl dd{{margin:0}}
.card{{background:var(--soft);border-left:3px solid var(--ac);border-radius:8px;padding:12px 14px;margin:0 0 12px}}
.card h4{{margin:0 0 4px;color:var(--maroon);font-size:15px}} .card p{{margin:0;font-size:14px}}
ol.qs li{{margin-bottom:14px}}
footer{{text-align:center;color:var(--muted);font-size:13px;margin-top:48px;border-top:1px solid var(--rule);padding-top:20px}}
</style></head><body>
<header class="hero"><img class="heroart" src="cover-art.png" alt="Line drawing of Swami Vivekananda"><div class="hshade"></div>
  <div class="brandrow"><div class="plate"><img src="{B.LOGO_URI}" alt="Ramakrishna Vedanta Centre NZ logo"></div><div class="org" style="font-size:14px;font-weight:700;line-height:1.4">Ramakrishna Vedanta<br>Centre NZ</div></div>
  <div class="htext"><div class="series">Vedanta Lectures of Swami Vivekananda</div>
  <h1>{M['title']}</h1>
  <div class="by">Swami Vivekananda</div><div class="del">{M['delivered']}</div>
  <div class="badge">Study Guide No. {M['guide_no']}</div></div>
</header>
<nav class="tabs"><a href="#summary">Summary</a><a href="#outline">Outline</a><a href="#lecture">Lecture</a><a href="#glossary">Glossary</a><a href="#bridge">Bridge to Wellbeing</a><a href="#questions">Questions</a></nav>
<div class="wrap">
<section id="summary"><span class="k">Before you read</span><h2 class="t">Summary of the Lecture</h2>{B.summary_html()}
<div class="note"><b>Source.</b> {M['source']}. {M['delivered']}.</div></section>
<section id="outline" class="toc"><span class="k">The shape of the lecture</span><h2 class="t">Outline</h2><ol>{toc}</ol></section>
<section id="lecture"><span class="k">The lecture</span><h2 class="t">Maya and Freedom</h2><div class="del">({M['delivered']})</div>{lecture()}</section>
<section id="glossary"><span class="k">Words and references</span><h2 class="t">Glossary</h2><dl>{"".join(f"<dt>{esc(t)}</dt><dd>{esc(d)}</dd>" for t,d in GLOSSARY)}</dl></section>
<section id="bridge"><span class="k">Vedanta and modern understanding</span><h2 class="t">Bridge to Wellbeing</h2><p class="intro">{esc(BRIDGE_INTRO)}</p>{"".join(f'<div class="card"><h4>{esc(h)}</h4><p>{esc(b)}</p></div>' for h,b in BRIDGE)}</section>
<section id="questions"><span class="k">For revision and reflection</span><h2 class="t">Questions</h2><ol class="qs">{qs}</ol></section>
<footer><p style="font-style:italic;color:var(--ink);font-size:14px">Join the <b>Study of Vivekananda Lectures</b> course on our website, <a href="https://vedanta.nz" style="color:var(--ac)">vedanta.nz</a>.</p>{M['org']}<br>{M['course']}<br><a href="https://vedanta.nz" style="color:var(--gold)">vedanta.nz</a></footer>
</div></body></html>"""

open(os.path.join(B.OUT, "index.html"), "w").write(page)
print("WEB written")
