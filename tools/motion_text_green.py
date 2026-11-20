import sys, math, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = sys.argv[1]; OUT = sys.argv[2]
W, H, FPS, DUR = 1920, 1080, 24, 20.04
NF = int(DUR * FPS)

# palette (from the reference swatch)
FOREST = (14, 52, 38)
DEEP = (27, 77, 56)
MID = (62, 123, 79)
OLIVE = (122, 139, 46)
LIME = (197, 216, 109)
SAGE = (226, 234, 190)

FD = "/usr/share/fonts/opentype/inter/"
def font(sz, w="Black"): return ImageFont.truetype(FD + f"InterDisplay-{w}.otf", sz)

def shadowed(img, off=(6, 8), blur=6, alpha=150):
    pad = 30
    base = Image.new("RGBA", (img.width + pad * 2, img.height + pad * 2), (0, 0, 0, 0))
    sh = Image.new("RGBA", base.size, FOREST + (0,))
    a = img.getchannel("A").point(lambda v: v * alpha // 255)
    sh.paste(Image.new("RGBA", img.size, FOREST + (255,)), (pad + off[0], pad + off[1]), a)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(sh); base.alpha_composite(img, (pad, pad))
    return base

def word_img(text, sz, fill=LIME, stroke=FOREST, sw=None):
    f = font(sz); sw = sw if sw is not None else max(4, sz // 14)
    l, t, r, b = f.getbbox(text, stroke_width=sw)
    im = Image.new("RGBA", (r - l + 4, b - t + 4), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((2 - l, 2 - t), text, font=f, fill=fill, stroke_width=sw, stroke_fill=stroke)
    return shadowed(im)

def pill_img(text, sz, bg=LIME, fg=FOREST, padx=None, pady=None, border=None, weight="Black", radius=None, icon=None):
    f = font(sz, weight)
    l, t, r, b = f.getbbox(text)
    padx = padx or int(sz * 0.45); pady = pady or int(sz * 0.28)
    iw = int(sz * 1.1) if icon else 0
    w, h = r - l + padx * 2 + iw, b - t + pady * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=radius if radius is not None else h // 2, fill=bg + (245,),
                        outline=(border + (255,)) if border else None, width=4 if border else 0)
    if icon == "dot":
        cy = h // 2; cx = padx + sz // 3
        d.ellipse((cx - sz // 4, cy - sz // 4, cx + sz // 4, cy + sz // 4), fill=LIME)
    d.text((padx + iw - l, pady - t), text, font=f, fill=fg)
    return shadowed(im, off=(4, 6), blur=8, alpha=120)

def bubble_img(text, sz, side, maxw=760):
    """chat bubble: side='me' (lime) or 'ai' (forest)"""
    f = font(sz, "Bold")
    words, lines, cur = text.split(), [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if f.getlength(test) > maxw and cur: lines.append(cur); cur = wd
        else: cur = test
    lines.append(cur)
    lh = int(sz * 1.25); padx, pady = int(sz * .7), int(sz * .55)
    tw = max(int(f.getlength(l)) for l in lines)
    w, h = tw + padx * 2, lh * len(lines) + pady * 2 - int(sz * .2)
    im = Image.new("RGBA", (w, h + 18), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    bg, fg = (LIME, FOREST) if side == "me" else (DEEP, SAGE)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=int(sz * .8), fill=bg + (245,),
                        outline=None if side == "me" else LIME + (255,), width=0 if side == "me" else 3)
    # tail
    if side == "me": d.polygon([(w - 40, h - 2), (w - 4, h + 16), (w - 70, h - 2)], fill=bg + (245,))
    else: d.polygon([(40, h - 2), (4, h + 16), (70, h - 2)], fill=bg + (245,))
    for i, ln in enumerate(lines):
        d.text((padx, pady + i * lh - f.getbbox("Ag")[1]), ln, font=f, fill=fg)
    return shadowed(im, off=(4, 6), blur=8, alpha=120)

def ease_back(x):
    x = min(max(x, 0), 1); c1 = 1.9; c3 = c1 + 1
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2
def ease_out(x):
    x = min(max(x, 0), 1); return 1 - (1 - x) ** 3

class El:
    def __init__(s, img, x, y, t0, t1, anim="pop", anchor="lt", dur=0.28, **kw):
        s.img, s.x, s.y, s.t0, s.t1, s.anim, s.anchor, s.dur, s.kw = img, x, y, t0, t1, anim, anchor, dur, kw
    def draw(s, canvas, t):
        if t < s.t0 or t >= s.t1: return
        p = (t - s.t0) / s.dur
        sc, dx, dy, a = 1.0, 0, 0, 1.0
        if s.anim == "pop":
            sc = 0.55 + 0.45 * ease_back(p); a = ease_out(p * 1.6)
        elif s.anim == "rise":
            dy = (1 - ease_back(p)) * 60; a = ease_out(p * 1.4)
        elif s.anim == "slide":   # from right, keeps drifting left = "on the move"
            dx = (1 - ease_out(p)) * 700 - (t - s.t0) * 28; a = ease_out(p * 2)
        elif s.anim == "slam":
            sc = 1 + 1.6 * (1 - ease_out(p * 1.3)); a = ease_out(p * 3)
            if p >= 0.6:
                k = (t - s.t0) * 40; amp = 14 * max(0.25, 1 - (t - s.t0) * 1.2)
                dx, dy = math.sin(k) * amp, math.cos(k * 1.3) * amp
        # gentle float after landing
        if s.kw.get("float") and p > 1:
            dy += math.sin((t - s.t0) * 2.4 + s.x * .01) * 5
        # quick exit near t1
        ex = (s.t1 - t) / 0.14
        if ex < 1 and s.kw.get("exit", True): a *= ease_out(ex); sc *= 0.9 + 0.1 * ex
        if a <= 0.01: return
        im = s.img
        if abs(sc - 1) > 0.01:
            im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.BICUBIC)
        if a < 1:
            im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
        bw, bh = s.img.width, s.img.height
        ax = {"l": 0, "c": 0.5, "r": 1}[s.anchor[0]]; ay = {"t": 0, "c": 0.5, "b": 1}[s.anchor[1]]
        cx = s.x - ax * bw + bw / 2 + dx; cy = s.y - ay * bh + bh / 2 + dy
        canvas.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2))) if 0 else \
            paste_clip(canvas, im, int(cx - im.width / 2), int(cy - im.height / 2))

def paste_clip(c, im, x, y):
    x0, y0 = max(0, x), max(0, y); x1, y1 = min(W, x + im.width), min(H, y + im.height)
    if x1 <= x0 or y1 <= y0: return
    c.alpha_composite(im.crop((x0 - x, y0 - y, x1 - x, y1 - y)), (x0, y0))

class Typing:
    """pill whose text types on letter by letter with a blinking cursor"""
    def __init__(s, text, sz, x, y, t0, t1, cps=22, **pk):
        s.text, s.sz, s.x, s.y, s.t0, s.t1, s.cps, s.pk = text, sz, x, y, t0, t1, cps, pk; s.cache = {}
    def draw(s, canvas, t):
        if t < s.t0 or t >= s.t1: return
        n = min(len(s.text), int((t - s.t0) * s.cps) + 1)
        cur = "|" if int(t * 3) % 2 == 0 else " "
        key = (n, cur)
        if key not in s.cache: s.cache[key] = pill_img(s.text[:n] + cur, s.sz, **s.pk)
        im = s.cache[key]
        a = min(1, (t - s.t0) / 0.1) * min(1, (s.t1 - t) / 0.14)
        if a < 1: im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
        paste_clip(canvas, im, s.x, s.y)

class Timer:
    def __init__(s, x, y, t0, t1): s.x, s.y, s.t0, s.t1 = x, y, t0, t1; s.cache = {}
    def draw(s, canvas, t):
        if t < s.t0 or t >= s.t1: return
        sec = int(t - s.t0); dots = "." * (1 + int((t - s.t0) * 3) % 3)
        key = (sec, dots)
        if key not in s.cache:
            s.cache[key] = pill_img(f"Calling Landlord{dots:<3}  0:{sec:02d}", 46, bg=FOREST, fg=SAGE,
                                    icon="dot", border=LIME, weight="Bold")
        im = s.cache[key]
        p = ease_back((t - s.t0) / 0.35)
        paste_clip(canvas, im, s.x - im.width, int(s.y - (1 - p) * 160))
        # pulsing ring around the dot
        r = 14 + ((t - s.t0) % 0.8) / 0.8 * 26; al = int(255 * (1 - ((t - s.t0) % 0.8) / 0.8))
        d = ImageDraw.Draw(canvas)
        cx = s.x - im.width + 65; cy = int(s.y - (1 - p) * 160) + im.height // 2
        d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=LIME + (al,), width=4)

els = []
def words(seq, x, y, sz, gap, anchor="rt", t1=None, hl=None):
    """seq: list of (time, text); stacked lines; hl = index rendered as lime pill"""
    for i, (t0, txt) in enumerate(seq):
        img = pill_img(txt, int(sz * 1.05)) if i == hl else word_img(txt, sz)
        els.append(El(img, x, y + i * gap, t0, t1, "pop", anchor, float=True))

# SHOT 1 (0 - 1.92)  interviewer on left -> text in right sky
words([(0.00, "SO,"), (0.96, "HOW WAS"), (1.42, "YOUR"), (1.54, "YEAR?")], 1880, 150, 104, 150, "rt", 1.92, hl=3)
# SHOT 2 (1.92 - 5.04) man centre -> split sides
els.append(El(word_img("HONESTLY,", 100), 50, 140, 3.00, 5.04, "pop", "lt", float=True))
els.append(El(word_img("A YEAR OF", 92), 1880, 120, 4.04, 5.04, "pop", "rt", float=True))
els.append(El(pill_img("MORE.", 150), 1880, 260, 4.54, 5.04, "slam", "rt"))
# SHOT 3 (5.04 - 10.04) night bus -> window top-right
els.append(El(word_img("I TRAVELED", 92), 1870, 90, 7.36, 10.04, "pop", "rt", float=True))
els.append(El(word_img("A LOT,", 118), 1870, 215, 8.32, 10.04, "pop", "rt", float=True))
els.append(El(pill_img("ALWAYS ON THE MOVE  →", 58, bg=FOREST, fg=LIME, border=LIME), 1890, 400, 8.94, 10.04, "slide", "rt", dur=0.45))
# SHOT 4 (10.04 - 12.58) desk -> wall above monitors, typed
els.append(El(word_img("BUILT MY OWN", 84), 60, 70, 10.32, 12.58, "rise", "lt", float=True))
els.append(Typing("AI APP", 96, 60, 195, 10.92, 12.58, cps=14))
# SHOT 5 (12.58 - 17.33) phone -> chat thread on the monitors
els.append(El(bubble_img("Write my landlord an excuse.", 46, "me"), 880, 70, 12.90, 17.33, "rise", "rt"))
els.append(El(bubble_img("I can't help with that.", 46, "ai"), 60, 245, 14.50, 17.33, "rise", "lt"))
els.append(El(pill_img("Calling your landlord…", 46, bg=OLIVE, fg=SAGE, weight="Bold", border=LIME, icon="dot"), 60, 400, 15.88, 17.33, "pop", "lt"))
els.append(El(word_img("NO!", 230, fill=LIME, sw=14), 1700, 260, 16.92, 17.33, "slam", "cc", exit=False))
# SHOT 6 (17.33 - end) wide -> call banner + NO! echo
els.append(El(word_img("NO!", 200, fill=LIME, sw=13), 1500, 600, 17.33, 18.6, "slam", "cc", dur=0.2))
els.append(Timer(1880, 60, 17.55, 21))

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-i", SRC,
    "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
    "-filter_complex", f"[0:v]scale={W}:{H}:flags=lanczos,setsar=1[b];[b][1:v]overlay=0:0:shortest=1[v]",
    "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", OUT], stdin=subprocess.PIPE)
for i in range(NF):
    t = i / FPS
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for e in els: e.draw(c, t)
    ff.stdin.write(c.tobytes())
ff.stdin.close(); ff.wait()
print("done", ff.returncode)
