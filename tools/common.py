import os, re
from typo import Face

BASE = os.path.dirname(os.path.abspath(__file__))
JB = os.path.join(BASE, "fonts/fonts/ttf")
SA = os.path.join(BASE, "fonts/satoshi/Satoshi_Complete/Fonts/WEB/fonts")

# Satoshi carries the display voice; JetBrains Mono carries anything technical.
BLACK = Face(f"{SA}/Satoshi-Black.ttf")
BOLD = Face(f"{SA}/Satoshi-Bold.ttf")
MED = Face(f"{SA}/Satoshi-Medium.ttf")
REG = Face(f"{SA}/Satoshi-Regular.ttf")
MONO = Face(f"{JB}/JetBrainsMono-Medium.ttf")
MONO_R = Face(f"{JB}/JetBrainsMono-Regular.ttf")
XB = Face(f"{JB}/JetBrainsMono-ExtraBold.ttf")

_NUM = re.compile(r"-?\d+\.\d+")


def _r(m):
    return f"{float(m.group()):.1f}".rstrip("0").rstrip(".")


def t(face, text, size, x, y, fill, tracking=0.0, anchor="start", opacity=None):
    w = face.advance(text, size, tracking)
    if anchor == "middle":
        x -= w / 2
    elif anchor == "end":
        x -= w
    d = _NUM.sub(_r, face.path(text, size, x, y, tracking))
    op = f' opacity="{opacity}"' if opacity is not None else ""
    return f'<path d="{d}" fill="{fill}"{op}/>'


def width(face, text, size, tracking=0.0):
    return face.advance(text, size, tracking)


def missing(faces, strings):
    out = set()
    for f in faces:
        for s in strings:
            for ch in s:
                if ord(ch) not in f.cmap:
                    out.add((ch, hex(ord(ch))))
    return sorted(out)


# Single committed look: cyan on black. No light variant — the panels stay dark
# in both GitHub themes on purpose.
THEMES = {
    "dark": dict(
        bg="#000000", ink="#E8F5FF", muted="#6F8B9E", accent="#5AD8FF",
        glow="#5AD8FF", glow_op=0.10, edge="#5AD8FF", edge_op=0.22,
        chip="#070D14", chip_stroke="#15242F", hair="#5AD8FF", hair_op=0.20,
        grid="#5AD8FF", grid_op=0.030,
    ),
}

def esc(s):
    """aria-label is an XML attribute: an unescaped & silently kills the whole file."""
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


RADIUS = 28


def surface(c, w, h, label, gid="s"):
    """A rounded, softly-lit card. Transparent corners let the page show through,
    so the panel reads as a floating surface in both GitHub themes."""
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">']
    o.append("<defs>")
    o.append(f'<clipPath id="{gid}clip"><rect width="{w}" height="{h}" rx="{RADIUS}"/></clipPath>')
    o.append(f'<radialGradient id="{gid}glow" cx="0.5" cy="0" r="0.9">'
             f'<stop offset="0" stop-color="{c["glow"]}" stop-opacity="{c["glow_op"]}"/>'
             f'<stop offset="1" stop-color="{c["glow"]}" stop-opacity="0"/></radialGradient>')
    o.append(f'<linearGradient id="{gid}hair" x1="0" y1="0" x2="1" y2="0">'
             f'<stop offset="0" stop-color="{c["accent"]}" stop-opacity="0"/>'
             f'<stop offset="0.5" stop-color="{c["accent"]}" stop-opacity="1"/>'
             f'<stop offset="1" stop-color="{c["accent"]}" stop-opacity="0"/></linearGradient>')
    o.append(f'<pattern id="{gid}grid" width="40" height="40" patternUnits="userSpaceOnUse">'
             f'<path d="M40 0H0V40" fill="none" stroke="{c["grid"]}" stroke-opacity="{c["grid_op"]}" stroke-width="1"/>'
             "</pattern>")
    o.append(f'<filter id="{gid}bloom" x="-30%" y="-30%" width="160%" height="160%">'
             '<feGaussianBlur stdDeviation="14"/></filter>')
    o.append("</defs>")
    o.append(f'<g clip-path="url(#{gid}clip)">')
    o.append(f'<rect width="{w}" height="{h}" fill="{c["bg"]}"/>')
    o.append(f'<rect width="{w}" height="{h}" fill="url(#{gid}grid)"/>')
    o.append(f'<rect width="{w}" height="{h}" fill="url(#{gid}glow)"/>')
    # bright top edge — light catching the material
    o.append(f'<rect width="{w}" height="1" fill="{c["edge"]}" opacity="{c["edge_op"]}"/>')
    return o


def close(o, c, w, h):
    o.append("</g>")
    o.append(f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="{RADIUS}" fill="none" '
             f'stroke="{c["hair"]}" stroke-opacity="{c["hair_op"]}" stroke-width="1"/>')
    o.append("</svg>")
    return "".join(o)
