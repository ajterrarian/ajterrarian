import os, sys
from common import XB, MONO, MONO_R, t, width, missing, surface, close, THEMES

W, H = 1600, 350
NAME = "AARAV JAMDAR"
TAGLINE = "applied ai, machine learning, computational finance"
SIGNOFF = "UC BERKELEY"
CURSOR = "█"


def build(theme="dark"):
    c = THEMES[theme]
    o = surface(c, W, H, f"Aarav Jamdar — {TAGLINE}", gid="b")
    a = o.append
    cx = W / 2

    # bloom pass behind the wordmark, then the crisp glyphs on top
    a(f'<g filter="url(#bbloom)" opacity="0.30">'
      + t(XB, NAME, 76, cx, 130, c["accent"], 5, anchor="middle") + "</g>")
    a(t(XB, NAME, 76, cx, 130, c["ink"], 5, anchor="middle"))

    a(f'<rect x="{cx-100:.0f}" y="168" width="200" height="2" fill="url(#bhair)"/>')

    # centre the tagline *including* the cursor, otherwise the block sits right of centre
    tw = width(MONO, TAGLINE, 26, 0.4)
    gap = 12
    left = cx - (tw + gap + width(MONO, CURSOR, 26)) / 2
    a(t(MONO, TAGLINE, 26, left, 218, c["muted"], 0.4))
    a(t(MONO, CURSOR, 26, left + tw + gap, 218, c["accent"], 0, opacity=0.9))

    a(t(MONO_R, SIGNOFF, 17, cx, 272, c["accent"], 4.5, anchor="middle", opacity=0.85))

    return close(o, c, W, H)


if __name__ == "__main__":
    m = missing((XB, MONO, MONO_R), (NAME, TAGLINE, SIGNOFF, CURSOR))
    if m:
        sys.exit(f"missing glyphs: {m}")
    out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"))
    if not os.path.isdir(out):
        out = "/Users/aarav/Developer/ajterrarian/assets"
    p = f"{out}/banner.svg"
    open(p, "w").write(build())
    print("banner", os.path.getsize(p) // 1024, "KB")
