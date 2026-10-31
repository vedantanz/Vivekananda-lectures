import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_core import *
from themes import theme_for

T = theme_for(M["guide_no"])
NO = f"{M['guide_no']:02d}"
ART = os.path.join(ROOT, "assets", "vivekananda-lineart.png")
def _make_art():
    from PIL import Image, ImageOps
    im = Image.open(ART).convert("L"); a = ImageOps.invert(im).point(lambda v: 0 if v < 40 else min(255, int((v-40)*1.35)))
    def tint(hexc, k, path):
        rgb = tuple(int(hexc[i:i+2], 16) for i in (1, 3, 5))
        o = Image.new("RGBA", im.size, rgb + (0,)); o.putalpha(a.point(lambda v: int(v*k))); o.save(path, optimize=True)
    tint("#E9C987", 0.9, os.path.join(GUIDE, "cover-art.png"))
    tint(T["accent"], 0.065, os.path.join(GUIDE, "watermark.png"))
_make_art()
COVER_ART = os.path.join(GUIDE, "cover-art.png")
WM = os.path.join(GUIDE, "watermark.png")
FONTS = os.path.join(ROOT, "assets", "fonts")

CSS = f"""
@font-face{{font-family:Lora;src:url(file://{FONTS}/Lora-Variable.ttf);font-weight:400 700;font-style:normal}}
@font-face{{font-family:Lora;src:url(file://{FONTS}/Lora-Italic-Variable.ttf);font-weight:400 700;font-style:italic}}
@font-face{{font-family:FreeSerif;src:url(file://{FONTS}/FreeSerif.ttf)}}
:root{{--maroon:#6B1414;--gold:#9C6B14;--goldl:#E9C987;--ink:#2a2420;--muted:#6d625a;--paper:#fffdf8;--rule:#e6dccb;
--ac:{T['accent']};--deep:{T['deep']};--soft:{T['soft']};--glow:{T['glow']}}}
@page{{size:A4;margin:24mm 20mm 22mm 24mm;background:url(file://{WM}) no-repeat right -14mm bottom 4mm;background-size:118mm auto;
  @top-left{{content:"Vedanta Lectures of Swami Vivekananda";font:8pt Lora,serif;letter-spacing:.08em;color:#a39890}}
  @top-right{{content:"{M['title']}";font:italic 8.5pt Lora,serif;color:{T['accent']}}}
  @bottom-left{{content:"Ramakrishna Vedanta Centre NZ  ·  Join the Study of Vivekananda Lectures course at vedanta.nz";font:italic 7.8pt Lora,serif;color:#8a7f76;vertical-align:top;padding-top:5mm}}@bottom-right{{content:counter(page);font:700 9pt Lora,serif;color:{T['accent']};vertical-align:top;padding-top:4.6mm}}}}
@page cover{{margin:0;background:none;@top-left{{content:none}}@top-right{{content:none}}@bottom-left{{content:none}}@bottom-right{{content:none}}}}
@page opener{{@top-left{{content:none}}@top-right{{content:none}}}}
body{{font-family:Lora,serif;font-size:10.6pt;line-height:1.62;color:var(--ink)}}

/* ---------- Cover ---------- */
.cover{{page:cover;width:210mm;height:297mm;position:relative;overflow:hidden;
  background:radial-gradient(ellipse 120mm 160mm at 150mm 120mm, {T['glow']} 0%, {T['accent']} 45%, {T['deep']} 100%)}}
.art{{position:absolute;left:52mm;bottom:0;height:238mm}}
.shade{{position:absolute;left:0;bottom:0;width:210mm;height:70mm;
  background:linear-gradient(to bottom, rgba(0,0,0,0) 0%, {T['deep']} 78%)}}
.lshade{{position:absolute;left:0;top:0;width:120mm;height:297mm;
  background:linear-gradient(to right, {T['deep']} 0%, rgba(0,0,0,0) 100%);opacity:.55}}
.frame{{position:absolute;left:8mm;top:8mm;width:194mm;height:281mm;border:0.6pt solid rgba(233,201,135,.45)}}
.brand{{position:absolute;left:18mm;top:18mm;display:flex;align-items:center;gap:4mm}}
.brand .lp{{position:relative;flex:none;width:22mm;height:22mm;border-radius:50%;background:#fffdf8;box-shadow:0 0 0 1.2pt var(--goldl)}}
.brand .lp img{{position:absolute;height:17mm;width:14.3mm;left:3.85mm;top:2.5mm}}
.brand .t{{font-size:11pt;letter-spacing:.2em;text-transform:uppercase;color:var(--goldl);line-height:1.45;white-space:nowrap;font-weight:700}}
.bignum{{position:absolute;right:16mm;top:12mm;font-size:60pt;font-weight:700;color:rgba(255,255,255,.12);line-height:1}}
.titleblock{{position:absolute;top:74mm;left:18mm;width:92mm;color:#fff}}
.titleblock .series{{font-size:8.5pt;letter-spacing:.24em;text-transform:uppercase;color:var(--goldl);line-height:1.6}}
.titleblock .rule{{width:18mm;border-top:1.4pt solid var(--goldl);margin:5mm 0}}
.titleblock h1{{font-size:44pt;line-height:1.02;margin:0 0 4mm;font-weight:700}}
.titleblock .by{{font-size:14pt;font-style:italic;color:#f4ece0}}
.quote{{position:absolute;top:156mm;left:18mm;width:82mm;font-size:12.5pt;font-style:italic;color:#f4ece0;line-height:1.5}}
.quote:before{{content:"“";color:var(--goldl);font-size:30pt;display:block;line-height:.6;margin-bottom:1mm}}
.qsrc{{font-size:7.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--goldl);margin-top:2.5mm;font-style:normal}}
.bottom{{position:absolute;left:18mm;bottom:18mm;width:174mm;color:#e8e0d4}}
.chip{{display:inline-block;border:1pt solid var(--goldl);color:var(--goldl);font-size:8pt;letter-spacing:.2em;text-transform:uppercase;padding:1.4mm 4mm;border-radius:10mm}}
.bottom .d{{font-size:9.5pt;margin-top:3mm}}
.bottom .c{{font-size:8.5pt;letter-spacing:.06em;color:var(--goldl);margin-top:1mm}}

/* ---------- Common ---------- */
.np{{break-before:page}}
.kicker{{font-size:8pt;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);margin-bottom:1mm}}
h2.title{{font-size:22pt;color:var(--deep);margin:0 0 4mm;font-weight:700;line-height:1.15}}
h2.title:after{{content:"";display:block;width:16mm;border-top:2pt solid var(--ac);margin-top:3mm}}
.intro{{font-size:11pt;font-style:italic;color:#4a3f38}}

/* Summary */
ol.points{{list-style:none;padding:0;margin:4mm 0 0;counter-reset:pt}}
ol.points li{{counter-increment:pt;position:relative;padding:0 0 0 11mm;margin:0 0 3.2mm;font-size:10pt;line-height:1.55}}
ol.points li:before{{content:counter(pt);position:absolute;left:0;top:0.3mm;width:6.6mm;height:6.6mm;border-radius:50%;
  background:var(--ac);color:#fff;font-size:8.5pt;font-weight:700;text-align:center;line-height:6.6mm}}
ol.points strong{{color:var(--deep)}}
.note{{margin-top:5mm;padding:3mm 4.5mm;background:var(--soft);border-radius:1.5mm;font-size:8.8pt;color:#4a3f38}}
.note b{{color:var(--ac)}}

/* Outline */
.outline{{display:block}}
.ocard{{background:rgba(255,255,255,.82);border:0.7pt solid var(--rule);border-top:2.4pt solid var(--ac);border-radius:2mm;padding:3.2mm 5mm 2.6mm;margin:0 0 4.2mm;break-inside:avoid}}
.ocard .hd{{display:flex;align-items:baseline;gap:3mm;margin-bottom:1.6mm}}
.ocard .pk{{font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);white-space:nowrap}}
.ocard h4{{margin:0;color:var(--deep);font-size:12pt}}
.orow{{display:flex;align-items:baseline;font-size:9.6pt;line-height:1.5;padding:0.9mm 0;border-top:0.4pt solid var(--rule)}}
.orow .on{{width:7mm;flex:none;color:var(--ac);font-weight:700;font-size:8.6pt}}
.orow .ot{{flex:1}}
.orow .op{{flex:none;width:12mm;text-align:right;color:var(--muted);font-size:8.4pt}}

/* Lecture */
.lhead{{text-align:center;padding:10mm 0 6mm}}
.lhead h2{{font-size:26pt;color:var(--deep);margin:1mm 0;letter-spacing:.04em}}
.lhead .del{{font-style:italic;color:var(--muted)}}
.part{{break-before:auto;break-after:avoid;break-inside:avoid;margin-top:9mm !important;background:var(--ac);color:#fff;margin:0 -4mm 6mm -4mm;padding:6mm 6mm 6mm;border-radius:2mm;
  position:relative;overflow:hidden}}
.part.first{{margin-top:0 !important}}
.part .pk{{font-size:8pt;letter-spacing:.26em;text-transform:uppercase;color:var(--goldl)}}
.part h2{{font-size:18pt;margin:1mm 0 0;font-weight:700}}
.part .pn2{{position:absolute;right:6mm;top:-1mm;font-size:50pt;font-weight:700;color:var(--goldl);opacity:.6}}
h3.sec{{font-size:12pt;color:var(--ac);margin:6mm 0 2mm;break-after:avoid;font-weight:700}}
h3.sec .sn{{display:inline-block;width:6.2mm;height:6.2mm;border-radius:50%;border:0.8pt solid var(--ac);font-size:8pt;
  text-align:center;line-height:6mm;margin-right:2.5mm;vertical-align:1pt;font-weight:400}}
p.lp{{text-align:justify;hyphens:auto;margin:0 0 3mm}}
.pn{{float:left;margin-left:-12mm;width:9mm;text-align:right;font-size:7.5pt;color:var(--ac);opacity:.75;padding-top:1.2pt}}
blockquote.verse{{margin:3mm 6mm 4mm;padding:4mm 5mm;background:var(--soft);border-radius:2mm;border-left:2.5pt solid var(--gold);break-inside:avoid}}
.dev{{display:block;font-family:FreeSerif,serif;font-size:12.5pt;line-height:1.7;color:var(--deep)}}
.tr{{display:block;font-style:italic;margin-top:1.5mm}}
.refrain{{color:var(--ac);font-style:italic}}

/* Glossary */
dl.gloss{{columns:2;column-gap:8mm;font-size:9.3pt;line-height:1.5}}
dl.gloss .g{{break-inside:avoid;margin-bottom:3mm}}
dl.gloss dt{{font-weight:700;color:var(--deep)}}
dl.gloss dd{{margin:0.5mm 0 0}}

/* Bridge */
.bridge{{margin:0 0 2.4mm;padding:2.4mm 4.5mm 2.4mm 5.5mm;background:var(--soft);border-radius:2mm;border-left:3pt solid var(--ac);break-inside:avoid}}
.bridge .lab{{font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}}
.bridge h4{{margin:0.5mm 0 1.2mm;color:var(--deep);font-size:11pt}}
.bridge p{{margin:0;font-size:9.1pt;line-height:1.45}}

/* Questions */
ol.qs{{list-style:none;padding:0;counter-reset:q}}
ol.qs li{{counter-increment:q;position:relative;padding-left:11mm;margin:0 0 5mm;break-inside:avoid}}
ol.qs li:before{{content:counter(q);position:absolute;left:0;top:0;width:7.5mm;height:7.5mm;border-radius:50%;
  background:var(--deep);color:#fff;font-weight:700;font-size:9pt;text-align:center;line-height:7.5mm}}
.qk{{display:inline-block;font-size:7pt;letter-spacing:.18em;text-transform:uppercase;color:#fff;padding:0.6mm 2.4mm;border-radius:5mm;margin-bottom:1mm}}
.qk.Understand{{background:var(--ac)}} .qk.Reflect{{background:var(--gold)}} .qk.Apply{{background:var(--maroon)}}
.lines{{height:15mm;background:repeating-linear-gradient(to bottom,transparent 0,transparent 6.6mm,#d9cdb8 6.6mm,#d9cdb8 7mm);margin-top:1mm}}

/* Back */
.back{{page:cover;break-before:page;width:210mm;height:297mm;position:relative;
  background:radial-gradient(circle at 50% 40%, {T['accent']} 0%, {T['deep']} 100%);color:#f4ece0;text-align:center}}
.back .plate{{top:80mm}}
.back .txt{{position:absolute;top:160mm;left:0;width:210mm}}
.back .n{{font-size:12pt;letter-spacing:.24em;text-transform:uppercase;color:var(--goldl);font-weight:700}}
.back p{{font-size:9.5pt;line-height:1.7}}
"""

def lecture():
    out = []
    for i, (ptag, ptitle, secs) in enumerate(PARTS):
        num = ptag.split()[-1]
        out.append(f'<div class="part{" first" if i == 0 else ""}"><div class="pn2">{i+1}</div>'
                   f'<div class="pk">{ptag}</div><h2>{esc(ptitle)}</h2></div>')
        for n, head, pnums in secs:
            out.append(f'<h3 class="sec"><span class="sn">{n}</span>{esc(head)}</h3>')
            for pn in pnums:
                h = para_html(pn, paras[pn - 1])
                h = h.replace("And this is Maya.", '<span class="refrain">And this is Maya.</span>')
                out.append(h)
    return "\n".join(out)

def outline():
    return '<div class="outline">' + "".join(
        f'<div class="ocard"><div class="hd"><span class="pk">{p}</span><h4>{esc(t)}</h4></div>' +
        "".join(f'<div class="orow"><span class="on">{n}</span><span class="ot">{esc(h)}</span>'
                f'<span class="op">\u00b6{", ".join(map(str, ps))}</span></div>' for n, h, ps in secs) +
        '</div>' for p, t, secs in PARTS) + '</div>'

def gloss():
    return '<dl class="gloss">' + "".join(f'<div class="g"><dt>{esc(t)}</dt><dd>{esc(d)}</dd></div>' for t, d in GLOSSARY) + '</dl>'

def bridge():
    return (f'<p class="intro">{esc(BRIDGE_INTRO)}</p>' + "".join(
        f'<div class="bridge"><div class="lab">A modern lens</div><h4>{esc(h)}</h4><p>{esc(b)}</p></div>' for h, b in BRIDGE))

def questions():
    def cls(k): return k.split()[0] if k.split()[0] in ("Understand", "Reflect", "Apply") else "Understand"
    return '<ol class="qs">' + "".join(
        f'<li><span class="qk {cls(k)}">{esc(k)}</span><br>{esc(q)}<div class="lines"></div></li>' for k, q in QUESTIONS) + '</ol>'

def doc():
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{M['title']}</title><style>{CSS}</style></head><body>
<section class="cover">
  <img class="art" src="file://{COVER_ART}" alt="Line drawing of Swami Vivekananda">
  <div class="lshade"></div><div class="shade"></div><div class="frame"></div>
  <div class="bignum">{NO}</div>
  <div class="brand"><div class="lp"><img src="{LOGO_URI}" alt="logo"></div><div class="t">Ramakrishna Vedanta<br>Centre NZ</div></div>
  <div class="titleblock"><div class="series">Vedanta Lectures of<br>Swami Vivekananda</div><div class="rule"></div>
    <h1>{M['title']}</h1><div class="by">Swami Vivekananda</div></div>
  <div class="quote">{esc(COVER_QUOTE)}<div class="qsrc">From the lecture</div></div>
  <div class="bottom"><span class="chip">Study Guide {NO}</span><div class="d">{M['delivered']}</div><div class="c">{M['course']} · {M['web']}</div></div>
</section>
<section class="np" style="page:opener">
  <div class="kicker">Before you read</div><h2 class="title">Summary of the Lecture</h2>
  <p class="intro">{esc(SUMMARY_INTRO)}</p>
  <ol class="points">{"".join(f'<li><strong>{esc(h)}.</strong> {esc(b)}</li>' for h, b in SUMMARY_POINTS)}</ol>
  <div class="note"><b>Source.</b> {M['source']}. {M['delivered']}.</div>
</section>
<section class="np"><div class="kicker">The shape of the lecture</div><h2 class="title">Outline</h2>{outline()}</section>
<section class="np"><div class="lhead"><div class="kicker">The Lecture</div><h2>{M['title'].upper()}</h2><div class="del">({M['delivered']})</div></div>{lecture()}</section>
<section class="np"><div class="kicker">Words and references</div><h2 class="title">Glossary</h2>{gloss()}</section>
<section class="np"><div class="kicker">Vedanta and modern understanding</div><h2 class="title">Bridge to Wellbeing</h2>{bridge()}</section>
<section class="np"><div class="kicker">For revision and reflection</div><h2 class="title">Questions</h2>{questions()}</section>
<section class="back"><div class="plate"><img src="{LOGO_URI}" alt=""></div>
  <div class="txt"><div class="n">{M['org']}</div><p>{M['series']}<br>{M['course']}<br>{M['web']}</p></div></section>
</body></html>"""

if __name__ == "__main__":
    from weasyprint import HTML
    pdf = os.path.join(OUT, f"Vivekananda_Lecture_{NO}_" + M["title"].replace(" ", "_") + ".pdf")
    HTML(string=doc(), base_url="/").write_pdf(pdf)
    print("PDF", pdf, T["name"])
