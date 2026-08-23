<div align="center">
  <img alt="Aarav Jamdar — applied ai, machine learning, computational finance" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/banner.svg" width="100%">
</div>

<p align="center">
  <a href="mailto:aaravjamdar@gmail.com"><img alt="email" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/badge-email.svg" height="34"></a>
  <a href="https://www.linkedin.com/in/aaravjamdar/"><img alt="linkedin" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/badge-linkedin.svg" height="34"></a>
  <a href="https://aaravjamdar.com"><img alt="website" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/badge-website.svg" height="34"></a>
</p>

## about me

I study math, CS, and data science at UC Berkeley. Almost everything I build sits where machine learning meets markets — trading agents, backtesters, and the occasional audit of somebody else's model.

What I actually care about is whether a result survives scrutiny. Two of the three projects below report a negative or heavily-caveated finding, because that is what the data said. I'd rather ship an honest null than a dressed-up number.

## Featured projects

<table>
<tr>
<td width="50%" valign="top">

**[rl-trading-agent](https://github.com/ajterrarian/rl-trading-agent)**<br>
<sub>`deep q-network` · `live paper trading`</sub>

A DQN built from scratch, trading SPY, deployed to live paper trading behind a risk layer: kill switch, data sanity checks, equity-capped position sizing.

*Validation matched buy-and-hold exactly — converged to buy-once-and-hold-forever.*

</td>
<td width="50%" valign="top">

**[equiface](https://github.com/ajterrarian/equiface)**<br>
<sub>`bias audit` · `fairface` · `resnet18`</sub>

A demographic bias audit of a ResNet18 gender classifier, finding a statistically significant performance disparity across groups (z = 5.51, p ≈ 3.7 × 10⁻⁸).

*Reproduces the core finding of the Gender Shades study on a different model and dataset.*

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[stat-arb](https://github.com/ajterrarian/stat-arb)**<br>
<sub>`cointegration` · `pairs trading`</sub>

A cointegration-based pairs-trading backtester, tested with `pytest` against hand-calculated values.

**

</td>
<td width="50%" valign="top">

**Also public**<br>
<sub>`smaller things`</sub>

[Stock-Return-Classifier](https://github.com/ajterrarian/Stock-Return-Classifier) — supervised classification of forward equity returns

[moving-average-backtest](https://github.com/ajterrarian/moving-average-backtest) — MA-crossover backtest over 2000–2025

[neetcode-submissions](https://github.com/ajterrarian/neetcode-submissions) — NeetCode problem submissions

</td>
</tr>
</table>

## Currently working on

**ForexPred** — a pattern-to-payoff prediction pipeline for Foreign Exchange markets, built with [@xild076](https://github.com/xild076). Private for now.

Every bar across 5 currency pairs and 4 timeframes is labelled by an ATR-scaled, gap-aware run classifier. A causal dilated TCN-GRU predicts whether a payoff starts on the next bar, and a cluster memory of time-warped shape prototypes only emits a directional call when its 95% Wilson lower bound beats chance. Validation is strictly chronological — the gate trains on ≤ 2024, validates on 2025, and every reported number comes from an unseen 2026+ holdout, with 0.8 pip of spread deducted on every trade.

## Stack

<div align="center">
  <img alt="Stack — Python; PyTorch, scikit-learn, Gymnasium; NumPy, SciPy, statsmodels, pandas; walk-forward CV, cointegration, backtesting, risk sizing; matplotlib, Parquet, yfinance, Alpaca, pytest, Git" src="https://raw.githubusercontent.com/ajterrarian/ajterrarian/main/assets/stack.svg" width="100%">
</div>
