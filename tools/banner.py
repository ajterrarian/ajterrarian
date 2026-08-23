import os, sys
from common import XB, MONO, MONO_R, t, width, missing, surface, close, THEMES

W, H = 1600, 430
EYEBROW = "UC BERKELEY · SAN FRANCISCO"
NAME = "AARAV JAMDAR"
SUB = "machine learning × computational finance"
CURSOR = "█"


def build(theme="dark"):
    c = THEMES[theme]
    o = surface(c, W, H, f"Aarav Jamdar — {SUB}", gid="b")
    a = o.append
    cx = W / 2

    a(t(MONO_R, EYEBROW, 17, cx, 124, c["accent"], 4.5, anchor="middle", opacity=0.85))

    # bloom pass behind the wordmark, then the crisp glyphs on top
    a(f'<g filter="url(#bbloom)" opacity="0.30">'
      + t(XB, NAME, 76, cx, 228, c["accent"], 5, anchor="middle") + "</g>")
    a(t(XB, NAME, 76, cx, 228, c["ink"], 5, anchor="middle"))

    a(f'<rect x="{cx-100:.0f}" y="268" width="200" height="2" fill="url(#bhair)"/>')

    sw = width(MONO, SUB, 26, 0.4)
    a(t(MONO, SUB, 26, cx - sw / 2, 322, c["muted"], 0.4))
    a(t(MONO, CURSOR, 26, cx + sw / 2 + 12, 322, c["accent"], 0, opacity=0.9))

    return close(o, c, W, H)


if __name__ == "__main__":
    m = missing((XB, MONO, MONO_R), (EYEBROW, NAME, SUB, CURSOR))
    if m:
        sys.exit(f"missing glyphs: {m}")
    out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"))
    if not os.path.isdir(out):
        out = "/Users/aarav/Developer/ajterrarian/assets"
    p = f"{out}/banner.svg"
    open(p, "w").write(build())
    print("banner", os.path.getsize(p) // 1024, "KB")
