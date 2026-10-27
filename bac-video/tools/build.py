# Writes index.html and compositions/*.html. Re-run after editing this file; the outputs are plain HTML.
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H, DUR = 1080, 1920, 55

AR = "U+0600-06FF,U+0750-077F,U+0870-088E,U+0890-0891,U+0897-08E1,U+08E3-08FF,U+200C-200E,U+2010-2011,U+204F,U+2E41,U+FB50-FDFF,U+FE70-FE74,U+FE76-FEFC"
LA = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
FONTS = "".join(
    f'@font-face{{font-family:"Alexandria";src:url("assets/fonts/alexandria-{s}-{w}-normal.woff2") format("woff2");font-weight:{w};font-style:normal;unicode-range:{r};}}\n'
    for w in (400, 600, 800, 900) for s, r in (("arabic", AR), ("latin", LA)))

BASE = """
#root{--lime:#D4FF3F;--cobalt:#2E3BFF;--red:#FF3B2F;--paper:#F5F3EE;--ink:#0F0F12;position:absolute;inset:0;overflow:hidden;font-family:"Alexandria",sans-serif;color:var(--ink);direction:rtl;}
.abs{position:absolute;}
.full{position:absolute;inset:0;}
.disp{font-weight:900;line-height:1.05;letter-spacing:0;}
.wm{position:absolute;left:-40px;right:-40px;top:1360px;text-align:center;direction:ltr;font-weight:900;font-size:520px;line-height:1;letter-spacing:-10px;}
"""

def scene(sid, css, body, js, dur):
    return f"""<template>
  <style>
{FONTS}{BASE}{css}
  </style>
  <div id="root" data-composition-id="{sid}" data-width="{W}" data-height="{H}">
{body}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{js}
    tl.set({{}}, {{}}, {dur});
    window.__timelines["{sid}"] = tl;
  </script>
</template>
"""

def write(path, txt):
    p = os.path.join(ROOT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(txt)

# ---------- shared objects ----------
BRANCHES = ["علوم تجريبية", "رياضيات", "تقني رياضي", "تسيير واقتصاد", "آداب وفلسفة", "لغات أجنبية"]

def sheet(pid, branch, rows=4, cls="sheet"):
    lines = "".join(f'<div class="ln" style="width:{w}%"></div>' for w in ([92, 70, 84, 58, 88, 64][:rows]))
    return f"""<div id="{pid}" class="{cls}">
      <div class="sh-rep" data-layout-ignore>الجمهورية الجزائرية الديمقراطية الشعبية</div>
      <div class="sh-ttl" data-layout-ignore>امتحان بكالوريا التعليم الثانوي</div>
      <div class="sh-br"><span id="{pid}-br">الشعبة: {branch}</span></div>
      <div class="sh-ex" data-layout-ignore>التمرين الأول</div>
      {lines}
    </div>"""

SHEET_CSS = """
.sheet{position:absolute;width:420px;height:560px;background:#fff;border:3px solid var(--ink);border-radius:10px;
  box-shadow:14px 14px 0 var(--ink);padding:26px 28px;direction:rtl;}
.sh-rep{font-size:16px;font-weight:600;text-align:center;opacity:.75;}
.sh-ttl{font-size:22px;font-weight:800;text-align:center;margin-top:8px;}
.sh-br{margin-top:16px;font-size:40px;font-weight:900;}
.sh-br span{padding:2px 10px;border-radius:6px;background-image:linear-gradient(var(--lime),var(--lime));background-repeat:no-repeat;background-size:var(--hl,0%) 100%;background-position:right;}
.sh-ex{margin-top:22px;font-size:24px;font-weight:800;border-bottom:3px solid var(--ink);display:inline-block;padding-bottom:4px;}
.ln{height:12px;border-radius:6px;background:#D9D7D0;margin-top:26px;}
"""

# ---------- S1 hook (0 - 6.0) ----------
s1_pages = ""
for i in range(9):
    s1_pages += f'<div id="s1-pg{i}" class="pg" style="left:{150 + (i%3)*40}px;top:{850 - i*36}px"><div class="pl" style="width:80%"></div><div class="pl" style="width:62%"></div><div class="pl" style="width:74%"></div><div class="pt" data-layout-ignore>حفظ</div></div>\n'
s1_css = """
#s1-bg{background:var(--lime);}
#s1-t1,#s1-t2{right:0;left:0;text-align:center;font-size:250px;}
#s1-t1{top:170px;} #s1-t2{top:450px;}
.pg{position:absolute;width:780px;height:300px;background:#fff;border:3px solid var(--ink);border-radius:10px;box-shadow:10px 10px 0 var(--ink);padding:34px 40px;}
.pl{height:16px;border-radius:8px;background:#CFCDC6;margin-bottom:26px;}
.pt{position:absolute;left:36px;bottom:24px;font-weight:900;font-size:56px;color:#B9B7B0;}
#s1-clock{left:700px;top:560px;width:250px;height:250px;}
#s1-band{left:-40px;right:-40px;top:700px;height:330px;background:var(--ink);display:flex;align-items:center;justify-content:center;}
#s1-band-t{color:var(--lime);font-size:150px;}
#s1-iris{background:var(--paper);clip-path:circle(0% at 50% 50%);}
"""
s1_body = f"""    <div id="s1-bg" class="full"></div>
    <div id="s1-wm" class="wm" data-layout-ignore style="color:#C3EE2C">BAC</div>
    <div id="s1-pages" class="full">{s1_pages}</div>
    <svg id="s1-clock" class="abs" viewBox="0 0 250 250"><circle cx="125" cy="125" r="110" fill="#fff" stroke="#0F0F12" stroke-width="12"/>
      <g id="s1-hand"><rect x="119" y="40" width="12" height="90" rx="6" fill="#0F0F12"/></g><circle cx="125" cy="125" r="14" fill="#0F0F12"/></svg>
    <div id="s1-t1" class="abs disp">صحاب</div>
    <div id="s1-t2" class="abs disp">الباك!</div>
    <div id="s1-band" class="abs"><div id="s1-band-t" class="disp">حبسوا دقيقة</div></div>
    <div id="s1-iris" class="full"></div>"""
s1_js = """
    tl.fromTo("#s1-t1", { scale: 1.12 }, { scale: 1, duration: 0.3, ease: "expo.out" }, 0);
    tl.fromTo("#s1-t2", { scale: 1.12 }, { scale: 1, duration: 0.3, ease: "expo.out" }, 0.4);
    // the old way: revision pages pile up while he says "تحفظوا في كلش"
    for (let i = 0; i < 9; i++) {
      const rot = [-4, 3, -2, 5, -3, 2, -5, 4, -1][i];
      tl.fromTo("#s1-pg" + i, { y: -1500, rotation: rot * 3, opacity: 1 }, { y: 0, rotation: rot, duration: 0.42, ease: "power4.out" }, 1.0 + i * 0.26);
    }
    tl.to(["#s1-t1", "#s1-t2"], { y: -60, scale: 0.82, duration: 0.6, ease: "power3.inOut" }, 1.2);
    // "وتضيعوا في وقتكم" - the clock spins away
    tl.fromTo("#s1-clock", { scale: 0, rotation: -40 }, { scale: 1, rotation: 0, duration: 0.45, ease: "back.out(1.8)" }, 2.45);
    tl.fromTo("#s1-hand", { rotation: 0, transformOrigin: "50% 94%" }, { rotation: 1440, duration: 1.3, ease: "power2.in" }, 2.5);
    // "حبسوا دقيقة": hard stop band
    tl.fromTo("#s1-band", { scaleY: 0 }, { scaleY: 1, duration: 0.22, ease: "expo.out" }, 3.8);
    tl.to(["#s1-t1", "#s1-t2"], { opacity: 0, filter: "blur(8px)", duration: 0.18 }, 3.8);
    tl.fromTo("#s1-band-t", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.15 }, 3.86);
    // pages blow out, paper iris opens on "واش درنا؟"
    for (let i = 0; i < 9; i++) {
      tl.to("#s1-pg" + i, { x: (i % 2 ? 1 : -1) * (900 + i * 40), rotation: (i % 2 ? 25 : -25), duration: 0.45, ease: "power3.in" }, 5.2 + (8 - i) * 0.02);
    }
    tl.to("#s1-clock", { scale: 0, duration: 0.25, ease: "power3.in" }, 5.2);
    tl.to("#s1-band", { scaleY: 0, duration: 0.25, ease: "power3.in" }, 5.45);
    tl.to("#s1-iris", { clipPath: "circle(80% at 50% 50%)", duration: 0.4, ease: "power3.in" }, 5.55);
"""
write("compositions/s1.html", scene("s1", s1_css, s1_body, s1_js, 6.0))

# ---------- S2 collect (6.0 - 15.3) local ----------
fan = [(-330, 520, -9), (-110, 470, -3), (110, 470, 3), (330, 520, 9), (-220, 860, -6), (220, 860, 6)]
s2_sheets = "".join(sheet(f"s2-sh{i}", b) for i, b in enumerate(BRANCHES))
s2_css = SHEET_CSS + """
#s2-bg{background:var(--paper);}
#s2-q{right:0;left:0;top:200px;text-align:center;font-size:190px;}
.sheet{left:330px;top:640px;}
#s2-dev{left:140px;top:1500px;width:800px;height:420px;background:var(--cobalt);border:4px solid var(--ink);border-radius:46px;box-shadow:16px 16px 0 var(--ink);}
#s2-slot{position:absolute;left:90px;right:90px;top:70px;height:44px;border-radius:22px;background:var(--ink);border:4px solid var(--lime);}
#s2-ai{position:absolute;left:0;right:0;top:115px;text-align:center;color:#fff;font-size:120px;font-weight:900;direction:ltr;}
#s2-ai-sub{position:absolute;left:0;right:0;top:250px;text-align:center;color:var(--lime);font-size:40px;font-weight:800;direction:ltr;}
#s2-flood{background:var(--cobalt);clip-path:inset(100% 0 0 0);}
"""
s2_body = f"""    <div id="s2-bg" class="full"></div>
    <div id="s2-wm" class="wm" data-layout-ignore style="color:#EAE7DF">BAC</div>
    <div id="s2-q" class="abs disp">واش درنا؟</div>
    {s2_sheets}
    <div id="s2-dev" class="abs"><div id="s2-slot"></div><div id="s2-ai">AI</div><div id="s2-ai-sub">Intelligence Artificielle</div></div>
    <div id="s2-flood" class="full"></div>"""
s2_js = "    const fan = " + json.dumps(fan) + ";\n" + """
    tl.fromTo("#s2-q", { opacity: 0, filter: "blur(10px)", scale: 1.15 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: 0.2, ease: "power4.out" }, 0.0);
    tl.to("#s2-q", { y: -40, scale: 0.6, duration: 0.5, ease: "power3.inOut" }, 0.85);
    // "جبنا كامل les sujets" - each branch's paper is dealt onto the table
    fan.forEach((f, i) => {
      tl.fromTo("#s2-sh" + i, { x: 1200, y: f[1] - 640 + 200, rotation: 30, scale: 0.92 }, { x: f[0], y: f[1] - 640, rotation: f[2], scale: 0.66, duration: 0.5, ease: "expo.out" }, 1.0 + i * 0.32);
    });
    // "في كامل les branches" - each branch name gets marked
    for (let i = 0; i < 6; i++) tl.fromTo("#s2-sh" + i + "-br", { "--hl": "0%" }, { "--hl": "100%", duration: 0.25, ease: "power2.out" }, 4.45 + i * 0.12);
    tl.to("#s2-q", { opacity: 0, filter: "blur(8px)", duration: 0.2 }, 5.5);
    // "ودخلناهم فـ l'Intelligence Artificielle" - the AI device rises and swallows them
    tl.fromTo("#s2-dev", { y: 0 }, { y: -620, duration: 0.6, ease: "expo.out" }, 5.6);
    fan.forEach((f, i) => {
      tl.to("#s2-sh" + i, { x: 0, y: 60, rotation: 0, scale: 0.1, opacity: 0, duration: 0.42, ease: "power3.in" }, 6.0 + i * 0.12);
    });
    tl.fromTo("#s2-ai-sub", { opacity: 0 }, { opacity: 1, duration: 0.2 }, 6.45);
    tl.to("#s2-dev", { y: -1000, duration: 0.6, ease: "power3.inOut" }, 7.0);
    // "des modèles prédictifs" - the device becomes the cobalt world
    tl.to("#s2-dev", { scale: 6, duration: 0.5, ease: "power3.in" }, 8.5);
    tl.to("#s2-flood", { clipPath: "inset(0% 0 0 0)", duration: 0.3, ease: "power3.in" }, 8.6);
"""
write("compositions/s2.html", scene("s2", s2_css, s2_body, s2_js, 9.3))

# ---------- S3 scan (15.3 - 26.4) ----------
QS = ["١) أدرس تغيّرات الدالة f", "٢) احسب النهاية عند ∞+", "٣) استنتج معادلة المماس"]
qrows = ""
for i, q in enumerate(QS):
    qrows += f'<div id="s3-q{i}" class="qrow"><div id="s3-hl{i}" class="qhl"></div><div class="qtx">{q}</div><div class="qln"></div></div>\n'
s3_css = """
#s3-bg{background:var(--cobalt);}
#s3-h{right:0;left:0;top:160px;text-align:center;font-size:100px;white-space:nowrap;color:#fff;}
#s3-sheet{left:90px;top:330px;width:900px;height:740px;background:#fff;border:4px solid var(--ink);border-radius:14px;box-shadow:18px 18px 0 var(--ink);padding:40px 50px;}
.s3-rep{font-size:24px;font-weight:600;text-align:center;opacity:.7;}
.s3-ttl{font-size:34px;font-weight:900;text-align:center;margin-top:10px;}
.s3-ex{margin-top:26px;font-size:34px;font-weight:900;display:inline-block;border-bottom:4px solid var(--ink);padding-bottom:4px;}
.qrow{position:relative;margin-top:44px;height:118px;}
.qhl{position:absolute;inset:-10px -16px;border-radius:12px;background:var(--lime);transform:scaleX(0);transform-origin:right center;}
.qtx{position:relative;font-size:44px;font-weight:800;}
.qln{position:relative;height:12px;width:70%;border-radius:6px;background:#D9D7D0;margin-top:22px;}
#s3-scan{left:60px;top:330px;width:960px;height:18px;background:var(--lime);border:4px solid var(--ink);border-radius:9px;}
#s3-stamp{left:120px;top:555px;padding:14px 26px;border:7px solid var(--ink);border-radius:14px;background:var(--lime);font-size:52px;font-weight:900;}
#s3-why{left:110px;top:750px;padding:10px 24px;background:var(--ink);color:#fff;border-radius:12px;font-size:46px;font-weight:900;}
#s3-pat{left:0;top:0;width:1080px;height:1920px;}
#s3-trap{left:70px;top:855px;width:940px;height:190px;}
#s3-trap-tag{left:120px;top:1070px;padding:12px 28px;background:var(--red);color:#fff;border:4px solid var(--ink);border-radius:12px;font-size:58px;font-weight:900;box-shadow:8px 8px 0 var(--ink);}
#s3-pat-tag{left:770px;top:262px;padding:8px 22px;background:var(--ink);color:var(--lime);border-radius:10px;font-size:42px;font-weight:800;direction:ltr;}
"""
s3_body = f"""    <div id="s3-bg" class="full"></div>
    <div id="s3-h" class="abs disp"><span class="w">هاد</span> <span class="w">الـ</span> <span class="w" style="direction:ltr;display:inline-block">AI</span> <span class="w">حلّل</span> <span class="w">كلش!</span></div>
    <div id="s3-sheet" class="abs">
      <div class="s3-rep" data-layout-ignore>الجمهورية الجزائرية الديمقراطية الشعبية</div>
      <div class="s3-ttl">امتحان بكالوريا التعليم الثانوي · رياضيات</div>
      <div class="s3-ex">التمرين الأول</div>
      {qrows}
    </div>
    <svg id="s3-pat" class="abs" viewBox="0 0 1080 1920" data-layout-ignore>
      <path id="s3-patpath" d="M 1010 650 C 1060 730, 1060 790, 1010 850 S 960 970, 1010 1030" fill="none" stroke="#D4FF3F" stroke-width="12" stroke-linecap="round" pathLength="100" stroke-dasharray="100 120" stroke-dashoffset="110"/>
      <circle id="s3-n0" cx="1010" cy="650" r="20" fill="#D4FF3F" stroke="#0F0F12" stroke-width="6"/>
      <circle id="s3-n1" cx="1010" cy="850" r="20" fill="#D4FF3F" stroke="#0F0F12" stroke-width="6"/>
      <circle id="s3-n2" cx="1010" cy="1030" r="20" fill="#D4FF3F" stroke="#0F0F12" stroke-width="6"/>
    </svg>
    <div id="s3-pat-tag" class="abs">patterns</div>
    <div id="s3-scan" class="abs"></div>
    <div id="s3-stamp" class="abs">تتعاود</div>
    <div id="s3-why" class="abs">علاش؟</div>
    <svg id="s3-trap" class="abs" viewBox="0 0 940 190"><rect x="6" y="6" width="928" height="178" rx="40" fill="none" stroke="#FF3B2F" stroke-width="12" pathLength="100" stroke-dasharray="100 120" stroke-dashoffset="110" id="s3-ring"/></svg>
    <div id="s3-trap-tag" class="abs">! العفسة</div>"""
s3_js = """
    tl.fromTo("#s3-h .w", { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.13, stagger: 0.16 }, 0.0);
    tl.fromTo("#s3-sheet", { y: 1300, rotation: 6 }, { y: 0, rotation: 0, duration: 0.6, ease: "expo.out" }, 0.25);
    // the AI scan
    tl.fromTo("#s3-scan", { y: 0, opacity: 1 }, { y: 740, duration: 1.3, ease: "power2.inOut" }, 0.8);
    tl.to("#s3-scan", { opacity: 0, duration: 0.15 }, 2.1);
    tl.to("#s3-h", { opacity: 0, filter: "blur(8px)", duration: 0.2 }, 2.0);
    // "لي ديما تتعاود" - repeated question marked and stamped
    tl.to("#s3-hl0", { scaleX: 1, duration: 0.3, ease: "power3.out" }, 2.9);
    tl.fromTo("#s3-stamp", { scale: 2.4, opacity: 0, rotation: -14 }, { scale: 1, opacity: 1, rotation: -8, duration: 0.25, ease: "back.out(2)" }, 3.3);
    // "les patterns" - the hidden thread between questions
    tl.fromTo(["#s3-n0", "#s3-n1", "#s3-n2"], { scale: 0, transformOrigin: "50% 50%" }, { scale: 1, duration: 0.2, stagger: 0.1, ease: "back.out(2)" }, 4.3);
    tl.to("#s3-patpath", { strokeDashoffset: 0, duration: 0.7, ease: "power2.inOut" }, 4.5);
    tl.fromTo("#s3-pat-tag", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.15 }, 4.8);
    // "علاش les profs يحطوا هاد les questions"
    tl.to("#s3-hl1", { scaleX: 1, duration: 0.3, ease: "power3.out" }, 6.1);
    tl.fromTo("#s3-why", { scale: 0, rotation: 10 }, { scale: 1, rotation: 4, duration: 0.3, ease: "back.out(2)" }, 6.4);
    // "العفسة" - the trap
    tl.to("#s3-sheet", { x: -8, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }, 9.05);
    tl.to("#s3-ring", { strokeDashoffset: 0, duration: 0.35, ease: "power2.out" }, 8.95);
    tl.fromTo("#s3-trap-tag", { scale: 0, rotation: -10 }, { scale: 1, rotation: -3, duration: 0.28, ease: "back.out(2.2)" }, 9.1);
    // whip out
    tl.to(["#s3-sheet", "#s3-trap", "#s3-trap-tag", "#s3-stamp", "#s3-why", "#s3-pat", "#s3-pat-tag"], { x: 1400, filter: "blur(18px)", duration: 0.3, ease: "power3.in" }, 10.75);
"""
write("compositions/s3.html", scene("s3", s3_css, s3_body, s3_js, 11.1))

# ---------- S4 chaos -> order (26.4 - 32.5) ----------
TOPICS = ["الدوال", "المتتاليات", "الأعداد المركبة", "الاحتمالات", "الهندسة في الفضاء", "الدالة الأسية", "اللوغاريتم"]
chaos = [(-240, -420, -18, 1.5), (260, -260, 12, 1.2), (-180, 40, 8, 1.7), (220, 210, -14, 1.0), (-60, -120, 22, 1.3), (300, 430, 9, 1.4), (-280, 380, -10, 1.15)]
s4_words = "".join(f'<div id="s4-w{i}" class="tw" data-layout-allow-overlap><span class="tn">{i+1}</span><span class="tt">{t}</span></div>\n' for i, t in enumerate(TOPICS))
s4_css = """
#s4-bg{background:var(--paper);}
#s4-flood{background:var(--lime);clip-path:circle(0% at 50% 55%);}
.tw{position:absolute;left:190px;width:700px;height:92px;top:420px;display:flex;align-items:center;gap:22px;background:#fff;border:4px solid var(--ink);border-radius:14px;box-shadow:8px 8px 0 var(--ink);padding:0 26px;}
.tn{width:56px;height:56px;border-radius:12px;background:var(--ink);color:var(--lime);font-size:34px;font-weight:900;display:flex;align-items:center;justify-content:center;direction:ltr;}
.tt{font-size:46px;font-weight:800;}
#s4-h{right:0;left:0;top:240px;text-align:center;font-size:150px;z-index:3;-webkit-text-stroke:0;}
#s4-h span{background:var(--ink);color:var(--paper);padding:0 30px;border-radius:18px;}
#s4-h2,#s4-h3{right:0;left:0;top:240px;text-align:center;font-size:118px;}
#s4-h3{font-size:104px;}
#s4-page{left:440px;top:760px;width:200px;height:260px;background:#fff;border:4px solid var(--ink);border-radius:12px;box-shadow:10px 10px 0 var(--ink);}
"""
s4_body = f"""    <div id="s4-bg" class="full"></div>
    <div id="s4-flood" class="full"></div>
    <div id="s4-h2" class="abs disp">افهم اللعبة</div>
    <div id="s4-h3" class="abs disp">خمّم كيما الأستاذ</div>
    {s4_words}
    <div id="s4-h" class="abs disp"><span>عشوائي؟</span></div>
    <div id="s4-page" class="abs"></div>"""
s4_js = "    const chaos = " + json.dumps(chaos) + ";\n" + """
    // "بدل ما تقرا عشوائي" - topics thrown everywhere
    chaos.forEach((c, i) => {
      tl.fromTo("#s4-w" + i, { x: c[0] * 3, y: c[1] * 2.5 + 300, rotation: c[2] * 3, scale: c[3] }, { x: c[0], y: c[1] + 300, rotation: c[2], scale: c[3], duration: 0.5, ease: "expo.out" }, 0.05 + i * 0.07);
    });
    tl.fromTo("#s4-h", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, 1.05);
    // "تولي فاهم اللعبة" - order: a clean ranked ladder, lime floods in
    tl.to("#s4-h", { opacity: 0, filter: "blur(8px)", duration: 0.15 }, 1.75);
    tl.to("#s4-flood", { clipPath: "circle(120% at 50% 55%)", duration: 0.45, ease: "power2.inOut" }, 1.8);
    chaos.forEach((c, i) => {
      tl.to("#s4-w" + i, { x: 0, y: i * 104, rotation: 0, scale: 1, duration: 0.55, ease: "power3.inOut" }, 1.8 + i * 0.05);
    });
    tl.fromTo("#s4-h2", { opacity: 0, filter: "blur(10px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.2 }, 2.35);
    // "وعقلية لي حط le sujet" - the ladder reads like the examiner's plan
    tl.to("#s4-h2", { opacity: 0, filter: "blur(8px)", duration: 0.15 }, 3.55);
    tl.fromTo("#s4-h3", { opacity: 0, filter: "blur(10px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.2 }, 3.65);
    tl.to("#s4-h3", { opacity: 0, filter: "blur(8px)", duration: 0.15 }, 5.0);
    // collapse into one page (it becomes the PDF)
    tl.fromTo("#s4-page", { scale: 0, opacity: 1 }, { scale: 1, duration: 0.3, ease: "back.out(1.6)" }, 5.35);
    for (let i = 0; i < 7; i++) tl.to("#s4-w" + i, { x: 0, y: 420, scale: 0.15, opacity: 0, duration: 0.35, ease: "power3.in" }, 5.1 + i * 0.03);
    tl.to("#s4-flood", { clipPath: "circle(0% at 50% 55%)", duration: 0.4, ease: "power2.inOut" }, 5.55);
"""
write("compositions/s4.html", scene("s4", s4_css, s4_body, s4_js, 6.1))

# ---------- S5 the PDF (32.5 - 44.3) ----------
TABS = ["علوم تجريبية", "رياضيات", "تقني رياضي", "تسيير واقتصاد", "آداب وفلسفة", "لغات أجنبية"]
BARS = [("الدوال", 92), ("المتتاليات", 74), ("الاحتمالات", 66), ("الأعداد المركبة", 58), ("الهندسة", 41)]
tabs = "".join(f'<div id="s5-tab{i}" class="tab{" sel" if i == 1 else ""}" data-layout-allow-overlap style="top:{150 + i*96}px">{t}</div>' for i, t in enumerate(TABS))
bars = "".join(f'<div class="brow"><div class="blab">{n}</div><div class="btrack"><div id="s5-bar{i}" class="bfill" style="width:{v}%"></div></div></div>' for i, (n, v) in enumerate(BARS))
s5_css = """
#s5-bg{background:var(--paper);}
#s5-doc{left:150px;top:260px;width:700px;height:900px;}
.dpage{position:absolute;inset:0;background:#fff;border:4px solid var(--ink);border-radius:16px;box-shadow:18px 18px 0 var(--ink);overflow:hidden;}
#s5-cover-top{position:absolute;left:0;right:0;top:0;height:470px;background:var(--cobalt);}
#s5-pdftag{position:absolute;left:40px;top:40px;padding:6px 22px;background:var(--lime);border:4px solid var(--ink);border-radius:10px;font-size:52px;font-weight:900;direction:ltr;}
#s5-ctitle{position:absolute;right:46px;left:46px;top:170px;color:#fff;font-size:76px;font-weight:900;line-height:1.15;}
#s5-csub{position:absolute;right:46px;left:46px;top:520px;font-size:40px;font-weight:800;line-height:1.35;}
#s5-cfoot{position:absolute;right:46px;left:46px;bottom:46px;font-size:30px;font-weight:600;opacity:.7;}
.tab{position:absolute;right:-250px;width:210px;height:80px;background:#fff;border:4px solid var(--ink);border-radius:0 14px 14px 0;font-size:30px;font-weight:800;display:flex;align-items:center;padding-right:24px;padding-left:16px;}
.tab.sel{background:var(--lime);}
#s5-tabs{position:absolute;left:880px;top:260px;width:10px;height:900px;}
.tab{right:auto;left:-40px;}
#s5-in{background:#fff;}
#s5-in-h{position:absolute;right:46px;top:46px;font-size:54px;font-weight:900;}
#s5-in-sub{position:absolute;right:46px;top:120px;font-size:30px;font-weight:600;opacity:.7;direction:rtl;}
#s5-chart{position:absolute;right:46px;left:46px;top:200px;}
.brow{display:flex;align-items:center;gap:20px;height:96px;}
.blab{width:250px;font-size:34px;font-weight:800;}
.btrack{flex:1;height:50px;background:#ECEAE4;border-radius:10px;overflow:hidden;}
.bfill{height:100%;background:var(--cobalt);border-radius:10px;transform-origin:right center;}
#s5-hist{position:absolute;right:46px;left:46px;top:720px;height:90px;}
#s5-hist-line{position:absolute;left:0;right:0;top:40px;height:8px;background:var(--ink);border-radius:4px;transform-origin:right center;}
.hdot{position:absolute;top:24px;width:40px;height:40px;border-radius:50%;background:var(--lime);border:6px solid var(--ink);}
#s5-hist-l{position:absolute;right:0;top:-48px;font-size:30px;font-weight:800;direction:ltr;}
#s5-one{left:700px;top:200px;width:200px;height:200px;border-radius:50%;background:var(--lime);border:6px solid var(--ink);display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:900;}
#s5-one b{font-size:84px;line-height:1;direction:ltr;} #s5-one i{font-style:normal;font-size:40px;direction:ltr;}
#s5-up{left:110px;top:430px;width:300px;height:420px;}
#s5-grade{left:80px;top:860px;padding:12px 28px;background:var(--ink);color:var(--lime);border-radius:14px;font-size:58px;font-weight:900;}
#s5-easy{left:430px;top:1060px;padding:10px 28px;background:var(--lime);border:5px solid var(--ink);border-radius:14px;font-size:54px;font-weight:900;box-shadow:8px 8px 0 var(--ink);}
#s5-flood{background:var(--lime);clip-path:circle(0% at 50% 50%);}
"""
dots = "".join(f'<div class="hdot s5-hd" style="left:{k}%"></div>' for k in (0, 22, 44, 66, 88))
s5_body = f"""    <div id="s5-bg" class="full"></div>
    <div id="s5-wm" class="wm" data-layout-ignore style="color:#EAE7DF">PDF</div>
    <div id="s5-tabs">{tabs}</div>
    <div id="s5-doc" class="abs">
      <div id="s5-cover" class="dpage">
        <div id="s5-cover-top"><div id="s5-pdftag">PDF</div><div id="s5-ctitle">مواضيع الباك محلّلة بالـ AI</div></div>
        <div id="s5-csub">الأسئلة لي تتعاود · العفسات · les patterns</div>
        <div id="s5-cfoot">منظم حسب الشعبة</div>
      </div>
      <div id="s5-in" class="dpage">
        <div id="s5-in-h">les statistiques</div>
        <div id="s5-in-sub">مثال توضيحي</div>
        <div id="s5-chart">{bars}</div>
        <div id="s5-hist"><div id="s5-hist-l">l'historique · BAC</div><div id="s5-hist-line"></div>{dots}</div>
      </div>
    </div>
    <div id="s5-one" class="abs"><b>1</b><i>fichier</i></div>
    <svg id="s5-up" class="abs" viewBox="0 0 300 420"><path d="M150 10 L290 170 L200 170 L200 410 L100 410 L100 170 L10 170 Z" fill="#D4FF3F" stroke="#0F0F12" stroke-width="12" stroke-linejoin="round"/></svg>
    <div id="s5-grade" class="abs">النقطة تاعك</div>
    <div id="s5-easy" class="abs">بأقل جهد</div>
    <div id="s5-flood" class="full"></div>"""
s5_js = """
    // the page from the ordered plan grows into the PDF
    tl.fromTo("#s5-doc", { scale: 0.29, y: 0, rotation: 0 }, { scale: 1, y: 0, rotation: -2, duration: 0.6, ease: "expo.out" }, 0.0);
    tl.set("#s5-in", { opacity: 0 }, 0);
    tl.fromTo("#s5-ctitle", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.2 }, 0.45);
    tl.fromTo("#s5-csub", { opacity: 0 }, { opacity: 1, duration: 0.2 }, 0.8);
    // "fichier PDF واحد"
    tl.fromTo("#s5-pdftag", { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2)" }, 1.95);
    tl.fromTo("#s5-one", { scale: 0, rotation: -30 }, { scale: 1, rotation: 8, duration: 0.3, ease: "back.out(2)" }, 2.5);
    tl.to("#s5-one", { scale: 0, duration: 0.2, ease: "power3.in" }, 3.4);
    // "منظم وواجد لشعبتك" - branch tabs slide out, yours is lit
    for (let i = 0; i < 6; i++) tl.fromTo("#s5-tab" + i, { x: -240 }, { x: 0, duration: 0.35, ease: "expo.out" }, 3.4 + i * 0.07);
    tl.fromTo("#s5-tab1", { scale: 1 }, { scale: 1.12, duration: 0.2, ease: "back.out(2)" }, 4.25);
    // "فيه قاع الـ data و les statistiques" - open the PDF
    tl.to("#s5-tabs", { opacity: 0, duration: 0.2 }, 4.95);
    tl.to("#s5-cover", { rotationY: -90, transformOrigin: "100% 50%", duration: 0.35, ease: "power3.in" }, 4.95);
    tl.fromTo("#s5-in", { opacity: 0 }, { opacity: 1, duration: 0.01 }, 5.25);
    tl.to("#s5-doc", { rotation: 0, duration: 0.4, ease: "power3.inOut" }, 5.0);
    for (let i = 0; i < 5; i++) tl.fromTo("#s5-bar" + i, { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: "expo.out" }, 6.0 + i * 0.1);
    // "l'historique تاع البكالوريات"
    tl.fromTo("#s5-hist-line", { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: "power2.inOut" }, 7.8);
    tl.fromTo(".s5-hd", { scale: 0 }, { scale: 1, duration: 0.2, stagger: 0.1, ease: "back.out(2)" }, 7.9);
    // "باش تضمن النقطة تاعك بأقل جهد"
    tl.fromTo("#s5-up", { y: 500, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "expo.out" }, 9.35);
    tl.fromTo("#s5-grade", { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2)" }, 9.6);
    tl.fromTo("#s5-easy", { scale: 0, rotation: 12 }, { scale: 1, rotation: -4, duration: 0.28, ease: "back.out(2.2)" }, 10.7);
    // carry: everything shrinks to the CTA's PDF icon while lime floods
    tl.to(["#s5-up", "#s5-grade", "#s5-easy"], { opacity: 0, scale: 0.6, duration: 0.2, ease: "power3.in" }, 11.3);
    tl.to("#s5-doc", { scale: 0.2, y: 120, duration: 0.45, ease: "power3.in" }, 11.3);
    tl.to("#s5-flood", { clipPath: "circle(120% at 50% 50%)", duration: 0.45, ease: "power2.inOut" }, 11.35);
"""
write("compositions/s5.html", scene("s5", s5_css, s5_body, s5_js, 11.8))

# ---------- S6 CTA (44.3 - 55.0) ----------
s6_css = """
#s6-bg{background:var(--lime);}
#s6-h{right:0;left:0;top:200px;text-align:center;font-size:140px;}
#s6-end{right:0;left:0;top:190px;text-align:center;font-size:136px;line-height:1.3;}
#s6-end .acc{display:inline-block;background:var(--ink);color:var(--lime);padding:0 26px;border-radius:18px;}
#s6-timer{left:415px;top:520px;width:250px;height:250px;}
#s6-btn{left:120px;top:760px;width:840px;height:170px;background:var(--ink);color:var(--lime);border-radius:28px;display:flex;align-items:center;justify-content:center;gap:28px;font-size:66px;font-weight:900;box-shadow:12px 12px 0 #fff;}
#s6-btn .pdf{direction:ltr;background:var(--lime);color:var(--ink);padding:2px 16px;border-radius:10px;font-size:52px;}
#s6-arrow{left:460px;top:975px;width:160px;height:192px;}
"""
s6_body = """    <div id="s6-bg" class="full"></div>
    <div id="s6-wm" class="wm" data-layout-ignore style="color:#C3EE2C">BAC</div>
    <div id="s6-h" class="abs disp"><span class="w">ما</span> <span class="w">تضيعش</span> <span class="w">الفرصة</span></div>
    <svg id="s6-timer" class="abs" viewBox="0 0 300 300">
      <circle cx="150" cy="150" r="128" fill="#fff" stroke="#0F0F12" stroke-width="10"/>
      <circle id="s6-ring" cx="150" cy="150" r="104" fill="none" stroke="#FF3B2F" stroke-width="40" pathLength="100" stroke-dasharray="100 100" stroke-dashoffset="0" transform="rotate(-90 150 150)"/>
      <rect x="140" y="20" width="20" height="30" rx="6" fill="#0F0F12"/>
    </svg>
    <div id="s6-btn" class="abs"><span>اشري الـ</span><span class="pdf">PDF</span><span>درك</span></div>
    <svg id="s6-arrow" class="abs" viewBox="0 0 200 240"><path d="M70 10 H130 V130 H190 L100 230 L10 130 H70 Z" fill="#FF3B2F" stroke="#0F0F12" stroke-width="10" stroke-linejoin="round"/></svg>
    <div id="s6-end" class="abs disp">اربح مئات<br/><span class="acc">الساعات</span><br/>بذكاء</div>"""
s6_js = """
    tl.fromTo("#s6-h .w", { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.13, stagger: 0.25 }, 0.0);
    // "والوقت راه يجري" - the clock runs out
    tl.fromTo("#s6-timer", { scale: 0, rotation: -30 }, { scale: 1, rotation: 0, duration: 0.4, ease: "back.out(1.8)" }, 0.8);
    tl.fromTo("#s6-ring", { strokeDashoffset: 0 }, { strokeDashoffset: -100, duration: 1.5, ease: "none" }, 0.95);
    // "اضغط على الرابط لي لتحت"
    tl.to("#s6-timer", { scale: 0, duration: 0.25, ease: "power3.in" }, 2.0);
    tl.fromTo("#s6-btn", { y: 600, scale: 0.8 }, { y: 0, scale: 1, duration: 0.55, ease: "expo.out" }, 2.1);
    tl.fromTo("#s6-arrow", { y: -120, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: "expo.out" }, 2.5);
    [3.0, 3.5, 4.0, 4.5, 5.0, 5.5].forEach(t => {
      tl.to("#s6-arrow", { y: 34, duration: 0.12, ease: "power2.out" }, t);
      tl.to("#s6-arrow", { y: 0, duration: 0.3, ease: "power2.inOut" }, t + 0.12);
    });
    // "اشري الـ PDF تاعك درك" - the press
    tl.to("#s6-btn", { scale: 0.93, duration: 0.08, ease: "power2.in" }, 3.7);
    tl.to("#s6-btn", { scale: 1, duration: 0.35, ease: "back.out(3)" }, 3.78);
    // end line: "واربح مئات الساعات بذكاء"
    tl.to("#s6-h", { opacity: 0, filter: "blur(8px)", duration: 0.18 }, 5.25);
    tl.fromTo("#s6-end", { opacity: 0, scale: 1.25, filter: "blur(10px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.3, ease: "expo.out" }, 5.4);
    tl.fromTo("#s6-end .acc", { scale: 0.6 }, { scale: 1, duration: 0.35, ease: "back.out(2)" }, 6.1);
"""
write("compositions/s6.html", scene("s6", s6_css, s6_body, s6_js, 10.7))

# ---------- captions (0 - 55) ----------
words = json.load(open(os.path.join(ROOT, "tools/words.json")))
SIZES = [2,4,3,2,2,2,4,5,2,5,4,4,4,5,2,3,4,2,4,4,3,4,5,3,2,5,2,4,4,3,4,5,3,2,4,2,3,3,5,6,4]
assert sum(SIZES) == len(words), (sum(SIZES), len(words))
groups, k = [], 0
for n in SIZES:
    groups.append(words[k:k+n]); k += n
cap_html, cap_js = "", ""
for gi, g in enumerate(groups):
    start = max(0.1, g[0][1] - 0.06)
    nxt = groups[gi+1][0][1] - 0.06 if gi + 1 < len(groups) else g[-1][2] + 0.6
    end = min(nxt, g[-1][2] + 0.5)
    spans = " ".join(f'<span id="c{gi}w{wi}" class="cw">{w[0]}</span>' for wi, w in enumerate(g))
    cap_html += f'    <div id="c{gi}" class="cg"><div class="cbox">{spans}</div></div>\n'
    cap_js += f'    tl.fromTo("#c{gi}", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.1, ease: "power3.out" }}, {start:.3f});\n'
    for wi, w in enumerate(g):
        cap_js += f'    tl.set("#c{gi}w{wi}", {{ color: "#D4FF3F" }}, {w[1]:.3f});\n'
    cap_js += f'    tl.to("#c{gi}", {{ opacity: 0, duration: 0.08 }}, {end - 0.08:.3f});\n    tl.set("#c{gi}", {{ opacity: 0, visibility: "hidden" }}, {end:.3f});\n'
cap_css = """
.cg{position:absolute;left:0;right:0;top:1190px;text-align:center;opacity:0;}
.cbox{display:inline-block;max-width:900px;background:var(--ink);border-radius:14px;padding:12px 28px 16px;line-height:1.35;font-size:54px;font-weight:800;color:#fff;}
.cw{display:inline;}
"""
write("compositions/captions.html", scene("captions", cap_css, cap_html, cap_js, DUR))

# ---------- root ----------
SCENES = [("s1", 0, 6.0), ("s2", 6.0, 9.3), ("s3", 15.3, 11.1), ("s4", 26.4, 6.1), ("s5", 32.5, 11.8), ("s6", 44.3, 10.7)]
hosts = "".join(f'      <div id="{s}" data-composition-id="{s}" data-composition-src="compositions/{s}.html" data-start="{a}" data-duration="{d}" data-track-index="1" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:1"></div>\n' for s, a, d in SCENES)
# (id, file, start, volume, duration) - starts put each file's measured peak one frame after its picture
SFX = [("sfx-whoosh1", "whoosh.mp3", 5.6, 0.7, 0.57), ("sfx-whoosh2", "whoosh-short.mp3", 14.65, 0.7, 0.57), ("sfx-pop1", "pop.mp3", 18.66, 0.9, 0.72),
       ("sfx-pop2", "pop.mp3", 21.65, 0.7, 0.72), ("sfx-impact", "impact-bass-1.mp3", 24.36, 0.8, 2.1), ("sfx-whoosh3", "whoosh.mp3", 25.95, 0.6, 0.57),
       ("sfx-whoosh4", "whoosh-short.mp3", 28.1, 0.6, 0.57), ("sfx-riser", "riser.mp3", 29.06, 0.5, 4.4), ("sfx-pop3", "pop.mp3", 34.92, 0.9, 0.72),
       ("sfx-whoosh5", "whoosh-short.mp3", 37.33, 0.6, 0.57), ("sfx-pop4", "pop.mp3", 43.12, 0.8, 0.72), ("sfx-whoosh6", "whoosh.mp3", 43.72, 0.6, 0.57),
       ("sfx-click", "click.mp3", 47.96, 1.0, 0.36)]
sfx = "".join(f'      <audio id="{i}" class="clip" src="assets/audio/{f}" data-start="{t}" data-duration="{d}" data-track-index="{5 + n % 2}" data-volume="{v}"></audio>\n' for n, (i, f, t, v, d) in enumerate(SFX))
VARS = [{"id": "color-ground", "type": "color", "label": "Lime", "default": "#D4FF3F"}]
index = f"""<!doctype html>
<html lang="ar" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      :root {{ --lime: #D4FF3F; --cobalt: #2E3BFF; --red: #FF3B2F; --paper: #F5F3EE; --ink: #0F0F12; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: {W}px; height: {H}px; overflow: hidden; background: var(--lime); }}
      #root {{ position: relative; width: 100%; height: 100%; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="{W}" data-height="{H}">
{hosts}      <div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{DUR}" data-track-index="2" data-track-kind="captions" data-width="{W}" data-height="{H}" style="z-index:5"></div>
      <audio id="voiceover" class="clip" src="assets/audio/voiceover.mp3" data-start="0" data-track-index="3" data-volume="1"></audio>
      <audio id="music" class="clip" src="assets/audio/music.mp3" data-start="0" data-duration="{DUR}" data-track-index="4" data-volume="0.16" data-fade-in="0.2" data-fade-out="2.5"></audio>
{sfx}    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
write("index.html", index)
print("built")
