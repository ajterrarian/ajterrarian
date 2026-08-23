import os, sys
from common import MONO, MONO_R, t, width, missing, surface, close, THEMES

W, PAD = 1600, 96
LABEL_COL = 280
ROW = 76
PADY = 54

GROUPS = [
    ("LANGUAGE",   ["Python"]),
    ("ML / DL",    ["PyTorch", "scikit-learn", "Gymnasium"]),
    ("SCIENTIFIC", ["NumPy", "SciPy", "statsmodels", "pandas"]),
    ("QUANT",      ["walk-forward CV", "cointegration", "backtesting", "risk sizing"]),
    ("DATA & OPS", ["matplotlib", "Parquet", "yfinance", "Alpaca", "pytest", "Git"]),
]


def stack(theme="dark"):
    c = THEMES[theme]
    h = PADY * 2 + ROW * len(GROUPS)
    o = surface(c, W, h, "Stack: " + "; ".join(f"{g} — {', '.join(i)}" for g, i in GROUPS), gid="k")
    a = o.append

    for i, (label, items) in enumerate(GROUPS):
        y = PADY + 38 + ROW * i + 8
        a(t(MONO_R, label, 18, PAD, y, c["accent"], 2.6, opacity=0.85))
        x = PAD + LABEL_COL
        for it in items:
            iw = width(MONO, it, 22, 0.3)
            a(f'<rect x="{x:.0f}" y="{y-31:.0f}" width="{iw+40:.0f}" height="44" rx="12" '
              f'fill="{c["chip"]}" stroke="{c["chip_stroke"]}" stroke-width="1"/>')
            a(t(MONO, it, 22, x + 20, y, c["ink"], 0.3, opacity=0.9))
            x += iw + 54

    return close(o, c, W, h)


if __name__ == "__main__":
    strings = [g for g, _ in GROUPS] + [i for _, its in GROUPS for i in its]
    m = missing((MONO, MONO_R), strings)
    if m:
        sys.exit(f"missing glyphs: {m}")
    out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"))
    if not os.path.isdir(out):
        out = "/Users/aarav/Developer/ajterrarian/assets"
    p = f"{out}/stack.svg"
    open(p, "w").write(stack())
    print("stack", os.path.getsize(p) // 1024, "KB")
