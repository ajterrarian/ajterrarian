<div align="center">
  <img alt="Aarav Jamdar — applied ai, machine learning, computational finance" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/banner.svg" width="100%">
</div>

<p align="center">
  <a href="mailto:aaravjamdar@gmail.com"><img alt="email" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/badge-email.svg" height="34"></a>
  <a href="https://www.linkedin.com/in/aaravjamdar/"><img alt="linkedin" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/badge-linkedin.svg" height="34"></a>
  <a href="https://aaravjamdar.com"><img alt="website" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/badge-website.svg" height="34"></a>
</p>

## about me

i study math, cs, and data science at uc berkeley. i'm interested in the intersection of machine learning, quantitative finance, and financial markets, and i've been building projects across trading systems, statistical arbitrage, and model evaluation.

## featured projects

<table>
<tr>
<td width="50%" valign="top">

**[rl-trading-agent](https://github.com/ajterrarian/rl-trading-agent)**<br>
<sub>`deep q-network` · `live paper trading`</sub>

a DQN built from scratch, trading SPY, deployed to live paper trading behind a risk layer: kill switch, data sanity checks, equity-capped position sizing.

**

</td>
<td width="50%" valign="top">

**[equiface](https://github.com/ajterrarian/equiface)**<br>
<sub>`bias audit` · `fairface` · `resnet18`</sub>

a demographic bias audit of a resnet18 gender classifier, finding a statistically significant performance disparity across groups (z = 5.51, p ≈ 3.7 × 10⁻⁸).

**

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[stat-arb](https://github.com/ajterrarian/stat-arb)**<br>
<sub>`cointegration` · `pairs trading`</sub>

a cointegration-based pairs-trading backtester, tested with `pytest` against hand-calculated values.

**

</td>
<td width="50%" valign="top">

**also public**<br>
<sub>`smaller things`</sub>

[stock-return-classifier](https://github.com/ajterrarian/Stock-Return-Classifier) — supervised classification of forward equity returns

[moving-average-backtest](https://github.com/ajterrarian/moving-average-backtest) — MA-crossover backtest over 2000–2025

[neetcode-submissions](https://github.com/ajterrarian/neetcode-submissions) — neetcode problem submissions

</td>
</tr>
</table>

## currently working on

**forexpred** — a pattern-to-payoff prediction pipeline for foreign exchange markets, built with [@xild076](https://github.com/xild076). 

every bar across 5 currency pairs and 4 timeframes is labelled by an ATR-scaled, gap-aware run classifier. a causal dilated TCN-GRU predicts whether a payoff starts on the next bar, and a cluster memory of time-warped shape prototypes only emits a directional call when its 95% Wilson lower bound beats chance. validation is strictly chronological — the gate trains on ≤ 2024, validates on 2025, and every reported number comes from an unseen 2026+ holdout, with 0.8 pip of spread deducted on every trade.

## Stack

<div align="center">
  <img alt="Stack — Python; PyTorch, scikit-learn, Gymnasium; NumPy, SciPy, statsmodels, pandas; walk-forward CV, cointegration, backtesting, risk sizing; matplotlib, Parquet, yfinance, Alpaca, pytest, Git" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/stack.svg" width="100%">
</div>
