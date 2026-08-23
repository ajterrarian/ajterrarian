"""Text -> SVG path outlines, so banner typography renders identically everywhere.

GitHub proxies README images through camo and renders them in SVG secure static
mode: no external font fetches. Outlining the glyphs is the only way to keep
JetBrains Mono instead of falling back to whatever the viewer happens to have.
"""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform


class Face:
    def __init__(self, path):
        self.font = TTFont(path)
        self.upem = self.font["head"].unitsPerEm
        self.glyphs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.hmtx = self.font["hmtx"]

    def advance(self, text, size, tracking=0.0):
        w = 0.0
        for ch in text:
            g = self.cmap.get(ord(ch))
            w += (self.hmtx[g][0] * size / self.upem if g else size * 0.6) + tracking
        return w - tracking if text else 0.0

    def path(self, text, size, x=0.0, y=0.0, tracking=0.0):
        """y is the baseline. Returns an SVG path 'd' string."""
        s = size / self.upem
        cx, out = x, []
        for ch in text:
            g = self.cmap.get(ord(ch))
            if g is None:
                cx += size * 0.6 + tracking
                continue
            spen = SVGPathPen(self.glyphs)
            self.glyphs[g].draw(TransformPen(spen, Transform(s, 0, 0, -s, cx, y)))
            d = spen.getCommands()
            if d:
                out.append(d)
            cx += self.hmtx[g][0] * s + tracking
        return " ".join(out)
