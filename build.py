#!/usr/bin/env python3
"""Simple Skincare creator preview, rebuilt in the Benable brand-portal creator card.

Single source of truth. Emits:
  index.html     local page (images from img-sm/), served on http://localhost:4288
  artifact.html  same page with images inlined as data URIs (for the claude.ai artifact)

Source data: Logan's showcase at logan-simple-skincare-creator-showcase.benny.benable.com
(captured Sep 10, 2026). Card anatomy: influencer-card-prototype/index.html (the current
brand-portal creator card: video carousel, About me, tags, Social Stats, Audience,
"Why they're perfect for this campaign", Shortlist).
"""
import base64
import html
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "img-sm")

PAGE_TITLE = "Simple Skincare Creator Grid" if "--carousel" not in sys.argv else "Simple Skincare Creator Preview"

# "grid" (v2, default): 8 small thumbnails on the left. "carousel" (v1): one big post with arrows.
MODE = "carousel" if "--carousel" in sys.argv else "grid"

CREATORS = [
    dict(
        id="monique",
        lane="Skincare authority",
        name="Monique Flores",
        handle="@skinwithmonique",
        location="Nashville, TN",
        platform="ig",
        avatar="34da08f6a0fc08df5d2c.jpeg",
        about="Licensed esthetician in Nashville, TN. Expert-led routine content for sensitive-skin basics.",
        tags=["Licensed esthetician", "Acne care", "Sensitive-skin routines"],
        followers="4.8K",
        engagement="30.0%",
        aud_location="83% U.S.",
        aud_gender="94% Female",
        aud_age="25 to 34",
        why=[
            "Licensed esthetician with a calm, ingredient-aware, never clinical voice",
            "Already posts sensitive-skin routines, SPF tips and skincare restocks",
            "Best channel: Instagram Reels, for trust, saves and routine education",
        ],
        slides=[
            dict(img="bp-ig-barebabeglow-3966046568409574521-full.jpg", caption="K-beauty restock", href="https://www.instagram.com/p/DcKOldItax5/"),
            dict(img="bp-ig-barebabeglow-reel-3873051503091381467-full.jpg", caption="SPF application tip", href="https://www.instagram.com/reel/DW_19JejfTb/"),
            dict(img="bp-ig-barebabeglow-3943294038667907933-full.jpg", caption="Skincare POV", href="https://www.instagram.com/p/Da5ZQkjt1Nd/"),
        ],
        # grid = Logan's 3 picks, then the 5 most recent reels in admin.benable.com profile_scrape (Sep 11 2026)
        grid=[
            dict(img="bp-ig-barebabeglow-3966046568409574521-full.jpg", caption="K-beauty restock", href="https://www.instagram.com/p/DcKOldItax5/"),
            dict(img="bp-ig-barebabeglow-reel-3873051503091381467-full.jpg", caption="SPF application tip", href="https://www.instagram.com/reel/DW_19JejfTb/"),
            dict(img="bp-ig-barebabeglow-3943294038667907933-full.jpg", caption="Skincare POV", href="https://www.instagram.com/p/Da5ZQkjt1Nd/"),
            dict(img="bp-ig-barebabeglow-reel-3953736030677738918-full.jpg", caption="A hydrating toner essence with magnesium, zinc, white tea", href="https://www.instagram.com/reel/DbeffjcNaWm/"),
            dict(img="bp-ig-barebabeglow-reel-3950924631983454521-full.jpg", caption="Safe to say super approved by me", href="https://www.instagram.com/reel/DbUgQUXtvk5/"),
            dict(img="bp-ig-barebabeglow-reel-3950864414428006981-full.jpg", caption="Brb trying them all", href="https://www.instagram.com/reel/DbUSkCZtopF/"),
            dict(img="bp-ig-barebabeglow-reel-3950533941105376642-full.jpg", caption="There's so many more, but for now I'll leave it here", href="https://www.instagram.com/reel/DbTHbBItb2C/"),
            dict(img="bp-ig-barebabeglow-reel-3949442227292859214-full.jpg", caption="Here you go besties, adding to my linktree", href="https://www.instagram.com/reel/DbPPMfat-tO/"),
        ],
    ),
    dict(
        id="lauren",
        lane="Makeup + beauty educator",
        name="Lauren Vaz",
        handle="@laurenvazzz",
        location="Los Angeles, CA",
        platform="tt",
        avatar="2e88e785b4c16ade9938.jpeg",
        about="Makeup and beauty educator in Los Angeles, CA. Makeup-prep and skin-finish storytelling.",
        tags=["Makeup artist", "Beauty routines", "Drugstore-friendly"],
        followers="4.1K",
        engagement="8.7%",
        aud_location="61% U.S.",
        aud_gender="85% Female",
        aud_age="25 to 34",
        why=[
            "Makeup artist who frames skincare as prep: cleanse, prep, base, finish",
            "Drugstore-friendly beauty and makeup routines, Simple's shelf",
            "Best channel: TikTok video, for discovery through makeup-prep routines",
        ],
        slides=[
            dict(img="bp-tt-laurenvaz-7651653316996255006-full.jpg", caption="Glow routine", href="https://www.tiktok.com/@laurenvaz/video/7651653316996255006"),
            dict(img="bp-tt-laurenvaz-7642159741313273118-full.jpg", caption="Korean skincare", href="https://www.tiktok.com/@laurenvaz/video/7642159741313273118"),
            dict(img="bp-tt-laurenvaz-7561260601289362719-full.jpg", caption="Daily favorites", href="https://www.tiktok.com/@laurenvaz/video/7561260601289362719"),
        ],
        # grid = Logan's 3 picks, then the 5 most recent TikToks in admin.benable.com profile_scrape (Sep 11 2026)
        grid=[
            dict(img="bp-tt-laurenvaz-7651653316996255006-full.jpg", caption="Glow routine", href="https://www.tiktok.com/@laurenvaz/video/7651653316996255006"),
            dict(img="bp-tt-laurenvaz-7642159741313273118-full.jpg", caption="Korean skincare", href="https://www.tiktok.com/@laurenvaz/video/7642159741313273118"),
            dict(img="bp-tt-laurenvaz-7561260601289362719-full.jpg", caption="Daily favorites", href="https://www.tiktok.com/@laurenvaz/video/7561260601289362719"),
            dict(img="bp-tt-laurenvaz-7673265167513226527-full.jpg", caption="Wash once a week, all of these products have rosemary mint", href="https://www.tiktok.com/@laurenvaz/video/7673265167513226527"),
            dict(img="bp-tt-laurenvaz-7673192069585784094-full.jpg", caption="Love doing cornrows on greasy silk press hair", href="https://www.tiktok.com/@laurenvaz/video/7673192069585784094"),
            dict(img="bp-tt-laurenvaz-7672296576710118687-full.jpg", caption="It feels nice to have it out of your face", href="https://www.tiktok.com/@laurenvaz/video/7672296576710118687"),
            dict(img="bp-tt-laurenvaz-7670609759522868510-full.jpg", caption="Rhode skin glazing milk", href="https://www.tiktok.com/@laurenvaz/video/7670609759522868510"),
            dict(img="bp-tt-laurenvaz-7670246530640645406-full.jpg", caption="It's actually very therapeutic", href="https://www.tiktok.com/@laurenvaz/video/7670246530640645406"),
        ],
    ),
    dict(
        id="sharae",
        lane="GRWM / lifestyle bridge",
        name="Sharae Palmer",
        handle="@sharaepalmer",
        location="Atlanta, GA",
        platform="ig",
        avatar="a4048a23e6777bc1be66.jpeg",
        about="Lifestyle and GRWM creator in Atlanta, GA. Everyday getting-ready content with a polished lens.",
        tags=["GRWM", "Lifestyle", "Body care"],
        followers="22.5K",
        engagement="4.3%",
        aud_location="70% U.S.",
        aud_gender="85% Female",
        aud_age="25 to 34",
        why=[
            "Everyday GRWM with a polished lifestyle lens",
            "Puts skincare inside the whole getting-ready rhythm, shower to errands",
            "Best channel: Instagram Reels, for polished lifestyle GRWM context",
        ],
        slides=[
            dict(img="hires-bp-ig-sharaepalmer-reel-3905730666066952697-full.jpg", caption="GRWM routine", href="https://www.instagram.com/reel/DYz8VjrRUH5/"),
            dict(img="ig-sharaepalmer-3864486266625131608-full.jpg", caption="Morning routine", href="https://www.instagram.com/p/DWhacjZkQRY/"),
            dict(img="hires-ig-sharaepalmer-3875323842017737233-full.jpg", caption="Lifestyle styling", href="https://www.instagram.com/reel/DXH6oCBEboR/"),
        ],
        # grid = Logan's 3 picks, then the 5 most recent reels in admin.benable.com profile_scrape (Sep 11 2026)
        grid=[
            dict(img="hires-bp-ig-sharaepalmer-reel-3905730666066952697-full.jpg", caption="GRWM routine", href="https://www.instagram.com/reel/DYz8VjrRUH5/"),
            dict(img="ig-sharaepalmer-3864486266625131608-full.jpg", caption="Morning routine", href="https://www.instagram.com/p/DWhacjZkQRY/"),
            dict(img="hires-ig-sharaepalmer-3875323842017737233-full.jpg", caption="Lifestyle styling", href="https://www.instagram.com/reel/DXH6oCBEboR/"),
            dict(img="bp-ig-sharaepalmer-reel-3961641561007433506-full.jpg", caption="Actually obsessed with this outfit", href="https://www.instagram.com/reel/Db6lAKTRaci/"),
            dict(img="bp-ig-sharaepalmer-reel-3956504126350944000-full.jpg", caption="Essentials every woman should have", href="https://www.instagram.com/reel/DboU4pbg-cA/"),
            dict(img="bp-ig-sharaepalmer-reel-3947737361215343723-full.jpg", caption="What's under my bonnet, a day 5 wash and go", href="https://www.instagram.com/reel/DbJLjbJx0xr/"),
            dict(img="bp-ig-sharaepalmer-reel-3932499807591255144-full.jpg", caption="Day 1 of my solo trip", href="https://www.instagram.com/reel/DaTC71exMxo/"),
            dict(img="bp-ig-sharaepalmer-reel-3929789674008589331-full.jpg", caption="A much needed Sunday reset", href="https://www.instagram.com/reel/DaJauM5R7QT/"),
        ],
    ),
]

# ---------- glyphs ----------
TT_GLYPH = (
    '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89'
    ' 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1v-3.5a6.37 6.37 0 00-.79-.05A6.34 6.34 0 003.15 15.2a6.34 6.34 0 006.34 6.34'
    ' 6.34 6.34 0 006.34-6.34V8.73a8.19 8.19 0 004.76 1.52V6.8a4.84 4.84 0 01-1-.11z" fill="#fff"/></svg>'
)
IG_GLYPH = (
    '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
    '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.4" cy="6.6" r=".9" fill="#fff" stroke="none"/></svg>'
)
VERIFIED = (
    '<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Verified" role="img">'
    '<circle cx="12" cy="12" r="10" fill="#0c8ee9"/>'
    '<path d="M8 12.2l2.6 2.6L16.4 9" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>'
)
SPARKLE = (
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M9.5 3l1.9 5.1L16.5 10l-5.1 1.9L9.5 17l-1.9-5.1L2.5 10l5.1-1.9L9.5 3z" fill="#8f6cff"/>'
    '<path d="M18 13.5l.95 2.55 2.55.95-2.55.95L18 20.5l-.95-2.55-2.55-.95 2.55-.95L18 13.5z" fill="#c4b0ff"/></svg>'
)
CHECK = (
    '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#7a5cfa" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M4.5 12.5l4.8 4.8L19.5 7"/></svg>'
)
PLUS = (
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
    '<path d="M12 5v14M5 12h14"/></svg>'
)
BTN_CHECK = (
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
)
PLAY = '<svg width="18" height="18" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
PLAY_SM = '<svg width="12" height="12" viewBox="0 0 24 24" fill="#1c1c1c" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
CHEV_L = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>'
CHEV_R = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg>'

PLATFORM_NAME = {"ig": "Instagram", "tt": "TikTok"}

CSS = """
:root{--ink:#1c1c1c;--mid:#717171;--line:#e3e3e3;--weak:#f1f1f1;--accent:#7a5cfa;--accent-deep:#6a4be6;--canvas:#f3f2f6;--why-line:#e4ddfb;--why-bg:#fcfbff}
*{box-sizing:border-box}
body{margin:0;background:var(--canvas);color:var(--ink);font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:14px;line-height:1.45;-webkit-font-smoothing:antialiased}
.wrap{max-width:924px;margin:0 auto;padding:44px 22px 96px}
.page-head{padding:0 4px}
.eyebrow{font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
h1{font-size:28px;line-height:1.2;font-weight:600;letter-spacing:-.01em;margin:8px 0;text-wrap:balance}
.page-head p{margin:0;font-size:15px;color:var(--mid);max-width:600px}
.lane{margin-top:36px}
.lane-label{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--mid);margin:0 0 10px 4px}
.card{background:#fff;border-radius:16px;box-shadow:0 4px 24px rgba(0,0,0,.08);padding:22px;display:grid;grid-template-columns:265px minmax(0,1fr);gap:20px;align-items:start}

.media{position:relative;width:265px;height:400px;border-radius:12px;overflow:hidden;background:#e9e8ee}
.media::after{content:"";position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.55));pointer-events:none}
.slide{position:absolute;inset:0;opacity:0;transition:opacity .25s ease}
.slide.on{opacity:1}
.slide img{width:100%;height:100%;object-fit:cover;display:block}
.badge{position:absolute;top:12px;left:12px;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;z-index:2}
.tt{background:#111}
.ig{background:radial-gradient(circle at 30% 110%,#fdf497 0%,#fdf497 5%,#fd5949 45%,#d6249f 60%,#285aeb 90%)}
.play{position:absolute;left:50%;top:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;background:rgba(17,17,17,.55);display:flex;align-items:center;justify-content:center;z-index:2;text-decoration:none;transition:background .15s}
.play:hover{background:rgba(17,17,17,.78)}
.play svg{margin-left:2px}
.arrow{position:absolute;top:50%;width:28px;height:28px;margin-top:-14px;border:0;padding:0;border-radius:50%;background:rgba(255,255,255,.72);color:var(--ink);display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:background .15s}
.arrow:hover{background:#fff}
.arrow.l{left:10px}
.arrow.r{right:10px}
.caption{position:absolute;left:14px;right:14px;bottom:32px;z-index:2;color:#fff;font-size:12px;font-weight:500;text-shadow:0 1px 2px rgba(0,0,0,.4);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dots{position:absolute;left:0;right:0;bottom:12px;display:flex;justify-content:center;gap:6px;z-index:2}
.dots button{width:8px;height:8px;border-radius:50%;border:0;padding:0;background:rgba(255,255,255,.45);cursor:pointer}
.dots button.on{background:#fff}

.grid{display:grid;grid-template-columns:repeat(2,96px);gap:6px}
.tile{position:relative;display:block;width:96px;height:96px;border-radius:8px;overflow:hidden;background:#e9e8ee}
.tile img{width:100%;height:100%;object-fit:cover;object-position:center 30%;display:block}
.tile .ph{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;background:rgba(17,17,17,.28);transition:opacity .12s}
.tile:hover .ph,.tile:focus-visible .ph{opacity:1}
.tile .ph span{width:26px;height:26px;border-radius:50%;background:rgba(255,255,255,.92);display:flex;align-items:center;justify-content:center}
.tile .ph svg{margin-left:2px}

.head{display:flex;align-items:center;gap:12px}
.avatar{width:60px;height:60px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 1px var(--line);flex:none}
.who{min-width:0}
.name{display:flex;align-items:center;gap:6px;font-size:18px;font-weight:600;line-height:1.2}
.handle{font-size:14px;color:var(--mid);margin-top:3px}
.socials{margin-left:auto;display:flex;gap:8px;align-self:flex-start;padding-top:2px}
.soc{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.lab{font-size:14px;font-weight:600;margin:18px 0 6px}
.bio{margin:0;color:var(--mid);font-size:14px;line-height:1.45}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.tag{font-size:13px;line-height:1;padding:6px 11px;border:1px solid var(--line);border-radius:999px;color:var(--ink);background:#fff}
.stats{display:grid;grid-template-columns:auto minmax(0,1fr);gap:12px;margin-top:18px}
.stats .lab{margin:0 0 8px}
.box{border:1px solid var(--line);border-radius:8px;padding:10px 12px;display:flex;gap:28px}
.stat .k{font-size:12px;color:var(--mid);line-height:1.2}
.stat .v{font-size:15px;font-weight:600;margin-top:4px;line-height:1.2;font-variant-numeric:tabular-nums;white-space:nowrap}
.why{margin-top:16px;border:1px solid var(--why-line);border-radius:10px;background:var(--why-bg);padding:14px 16px}
.why-t{display:flex;align-items:center;gap:8px}
.why-t .grad{font-size:15px;font-weight:600;background:linear-gradient(90deg,#7a5cfa 0%,#a67cf2 55%,#cf6dc6 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.why ul{list-style:none;margin:10px 0 0;padding:0}
.why li{display:flex;gap:9px;align-items:flex-start;font-size:14px;line-height:20px;margin-top:6px}
.why li svg{flex:none;margin-top:2px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.src{margin-top:40px;padding:0 4px;font-size:12px;color:var(--mid);line-height:1.5}
.src a{color:inherit}
@media(max-width:720px){
  .card{grid-template-columns:1fr}
  .media{width:100%;height:420px}
  .grid{grid-template-columns:repeat(4,1fr)}
  .tile{width:auto;height:auto;aspect-ratio:1}
  .stats{grid-template-columns:1fr}
  .box{flex-wrap:wrap;gap:16px 28px}
}
@media(prefers-reduced-motion:reduce){.slide,.play,.arrow{transition:none}}
"""

JS = """
(function(){
  document.querySelectorAll('.media').forEach(function(m){
    var slides = Array.prototype.slice.call(m.querySelectorAll('.slide'));
    var dots = Array.prototype.slice.call(m.querySelectorAll('.dots button'));
    var play = m.querySelector('.play'), cap = m.querySelector('.caption');
    var i = 0;
    function go(n){
      i = (n + slides.length) %% slides.length;
      slides.forEach(function(s, k){ s.classList.toggle('on', k === i); });
      dots.forEach(function(d, k){ d.classList.toggle('on', k === i); d.setAttribute('aria-current', k === i ? 'true' : 'false'); });
      play.href = slides[i].getAttribute('data-href');
      play.setAttribute('aria-label', 'Open ' + slides[i].getAttribute('data-caption') + ' on ' + m.getAttribute('data-platform'));
      cap.textContent = slides[i].getAttribute('data-caption');
    }
    m.querySelector('.arrow.l').addEventListener('click', function(){ go(i - 1); });
    m.querySelector('.arrow.r').addEventListener('click', function(){ go(i + 1); });
    dots.forEach(function(d, k){ d.addEventListener('click', function(){ go(k); }); });
    go(0);
  });
})();
"""


def img_src(name, inline):
    path = os.path.join(IMG, name)
    if not inline:
        return "img-sm/" + name
    mime = "image/jpeg"
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode("ascii"))


def esc(s):
    return html.escape(s, quote=True)


def card(c, inline):
    p = c["platform"]
    glyph = (TT_GLYPH if p == "tt" else IG_GLYPH)
    slides = "".join(
        '<div class="slide%s" data-href="%s" data-caption="%s"><img src="%s" alt="%s: %s"></div>'
        % (" on" if k == 0 else "", esc(s["href"]), esc(s["caption"]), img_src(s["img"], inline), esc(c["name"]), esc(s["caption"]))
        for k, s in enumerate(c["slides"])
    )
    dots = "".join(
        '<button type="button"%s aria-label="Post %d of %d"></button>' % (' class="on"' if k == 0 else "", k + 1, len(c["slides"]))
        for k in range(len(c["slides"]))
    )
    tags = "".join('<span class="tag">%s</span>' % esc(t) for t in c["tags"])
    why = "".join("<li>%s<span>%s</span></li>" % (CHECK, esc(w)) for w in c["why"])
    first = c["slides"][0]
    if MODE == "grid":
        tiles = "".join(
            '<a class="tile" href="%s" target="_blank" rel="noreferrer" aria-label="Open %s on %s" title="%s"><img src="%s" alt=""><span class="ph"><span>%s</span></span></a>'
            % (esc(t["href"]), esc(t["caption"]), PLATFORM_NAME[p], esc(t["caption"]), img_src(t["img"], inline), PLAY_SM)
            for t in c["grid"][:8]
        )
        media_html = f'<div class="grid" data-platform="{PLATFORM_NAME[p]}">{tiles}</div>'
    else:
        media_html = f"""<div class="media" data-platform="{PLATFORM_NAME[p]}">
      {slides}
      <span class="badge {p}" title="{PLATFORM_NAME[p]}">{glyph.format(s=20)}</span>
      <a class="play" href="{esc(first["href"])}" target="_blank" rel="noreferrer" aria-label="Open {esc(first["caption"])} on {PLATFORM_NAME[p]}">{PLAY}</a>
      <button type="button" class="arrow l" aria-label="Previous post">{CHEV_L}</button>
      <button type="button" class="arrow r" aria-label="Next post">{CHEV_R}</button>
      <div class="caption">{esc(first["caption"])}</div>
      <div class="dots">{dots}</div>
    </div>"""
    return f"""
<section class="lane">
  <div class="lane-label">{esc(c["lane"])}</div>
  <article class="card" aria-label="{esc(c["name"])}">
    {media_html}
    <div class="info">
      <div class="head">
        <img class="avatar" src="{img_src(c["avatar"], inline)}" alt="">
        <div class="who">
          <div class="name">{esc(c["name"])} {VERIFIED}</div>
          <div class="handle">{esc(c["handle"])}</div>
        </div>
        <div class="socials"><span class="soc {p}" title="{PLATFORM_NAME[p]}">{glyph.format(s=15)}</span></div>
      </div>
      <div class="lab">About me</div>
      <p class="bio">{esc(c["about"])}</p>
      <div class="tags">{tags}</div>
      <div class="stats">
        <div>
          <div class="lab">Social Stats</div>
          <div class="box">
            <div class="stat"><div class="k">Followers</div><div class="v">{esc(c["followers"])}</div></div>
            <div class="stat"><div class="k">Engagement</div><div class="v">{esc(c["engagement"])}</div></div>
          </div>
        </div>
        <div>
          <div class="lab">Audience</div>
          <div class="box">
            <div class="stat"><div class="k">Location</div><div class="v">{esc(c["aud_location"])}</div></div>
            <div class="stat"><div class="k">Gender</div><div class="v">{esc(c["aud_gender"])}</div></div>
            <div class="stat"><div class="k">Age Range</div><div class="v">{esc(c["aud_age"])}</div></div>
          </div>
        </div>
      </div>
      <div class="why">
        <div class="why-t">{SPARKLE}<span class="grad">Why they're perfect for this campaign</span></div>
        <ul>{why}</ul>
      </div>
    </div>
  </article>
</section>"""


def body(inline):
    cards = "".join(card(c, inline) for c in CREATORS)
    return f"""
<div class="wrap">
  <header class="page-head">
    <div class="eyebrow">Benable × Simple Skincare</div>
    <h1>Creator preview</h1>
    <p>Three ways Simple can show up in real routines: expert skincare, beauty prep, and polished everyday GRWM.</p>
  </header>
  {cards}
  <p class="src">{"Thumbnails" if MODE == "grid" else "Post examples"} link to the live posts. Stats and audience figures as of Sep 10, 2026.</p>
</div>
<script>{JS}</script>"""


FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap">'


def build():
    css = CSS + (".card{grid-template-columns:198px minmax(0,1fr)}\n" if MODE == "grid" else "")
    local = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{PAGE_TITLE}</title>
{FONT}
<style>{css}</style>
</head>
<body>{body(inline=False)}
</body>
</html>
"""
    artifact = f"""<title>{PAGE_TITLE}</title>
{FONT}
<style>{css}</style>
{body(inline=True)}
"""
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(local)
    artifact_name = "artifact-grid.html" if MODE == "grid" else "artifact.html"
    with open(os.path.join(ROOT, artifact_name), "w") as f:
        f.write(artifact)
    print("index.html %d bytes, %s %d bytes (mode=%s)" % (len(local.encode()), artifact_name, len(artifact.encode()), MODE))


if __name__ == "__main__":
    build()
