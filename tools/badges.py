import os
from common import MONO, t, width, THEMES

BADGES = ["email", "linkedin", "github"]
FS, H, PADX = 26, 68, 26


def badge(theme, label):
    c = THEMES[theme]
    w = int(PADX * 2 + 20 + width(MONO, label, FS, 0.4))
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{H}" viewBox="0 0 {w} {H}" role="img" aria-label="{label}">']
    o.append(f'<rect x="1" y="1" width="{w-2}" height="{H-2}" rx="16" fill="{c["chip"]}" '
             f'stroke="{c["chip_stroke"]}" stroke-width="2"/>')
    o.append(f'<circle cx="{PADX}" cy="{H//2}" r="5" fill="{c["accent"]}"/>')
    o.append(t(MONO, label, FS, PADX + 20, H // 2 + 9, c["ink"], 0.4, opacity=0.92))
    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"))
    if not os.path.isdir(out):
        out = "/Users/aarav/Developer/ajterrarian/assets"
    for label in BADGES:
        open(f"{out}/badge-{label}.svg", "w").write(badge("dark", label))
    print("badges:", len(BADGES))
