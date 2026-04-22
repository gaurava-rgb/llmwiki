---
title: "I have gone personally through quant interviews at institutional firms"
reader_id: "01kk4hvjjzra85jx2ejeq7kcth"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kk4hvjjzra85jx2ejeq7kcth"
source_url: "https://x.com/i/status/2030142337771524504/?rw_tt_thread=True"
author: "Roan"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-07"
saved_at: "2026-03-07"
reading_time: "19 mins"
summary: "Quant interviews focus mainly on technical math and problem-solving skills, not market knowledge or tools. Quants use advanced math like stochastic calculus to solve complex finance problems every day. Preparing well with the right resources and understanding math deeply is key to success."
content_hash: "8b5109fd9f71bd528ec405ea810dddc8074393d8d923d40aee17a9404a9f7601"
---

I have gone personally through quant interviews at institutional firms. This article is the closest thing to an insider breakdown I have ever seen shared publicly.

Read it tonight.

This kind of content does not stay public forever.

![](https://pbs.twimg.com/profile_images/2006055825714913281/u6yl2H6t.jpg)

[Phosphen](<https://twitter.com/phosphenq>) [@phosphenq](<https://twitter.com/phosphenq>)

[ ](<https://twitter.com/phosphenq/status/2029610565132505510>)

![Wall Street Pays $300,000 a Year to Quant Who Think This Way ](https://pbs.twimg.com/media/HCpl8MqW8AA344w.png)

The interviewer slides a piece of paper across the table. One handwritten problem, no charts, no Bloomberg terminal, no prior knowledge of markets required.

Three problems and ninety minutes to show how your brain works. The math isn't the hard part. The thinking is.

This is how Wall Street decides if you're worth $300,000 a year.

## Someone made a mock quant interview on YouTube

**Full format:** 2-math problems, 1-coding test, real-time feedback between rounds.

The interviewer explains what he's looking for after each answer.

What struck me wasn't the difficulty of the problems.

It was how completely different this is from any job interview most people have ever sat through.

For a quant, 90% of the interview is technical.

No _"tell me about a time you showed leadership."_

No competency frameworks.

You sit down, u get a pen, and you solve problems out loud while someone watches how your brain works.

## What Quants Actually Do

A quant is a mathematician embedded in a financial firm.

**Every day:** math, statistics, algorithms: applied to the hardest problems in finance.

But "quant" isn't one job. There are two completely different worlds.

**Sell-side quants work at banks:** Goldman Sachs, JPMorgan.

They price derivatives, manage risk, validate models. The math is heavy on Itô calculus and partial differential equations.

**Buy-side quants work at hedge funds.**

They generate alpha, they build trading strategies, they find edges before anyone else and exploit them until they disappear.

The competitive one. Entry-level compensation at top firms starts around $300,000

That's before the bonus.

**My friend wrote a detailed breakdown of how all of this works structurally:**

![](https://pbs.twimg.com/profile_images/1975113774680920064/-dpcubqz.jpg)

[gemchanger](<https://twitter.com/gemchange_ltd>) [@gemchange_ltd](<https://twitter.com/gemchange_ltd>)

[ ](<https://twitter.com/gemchange_ltd/status/2028904166895112617>)

![How I'd Become a Quant If I Had to Start Over Tomorrow](https://pbs.twimg.com/media/HCgcPCZXkAA4osL.jpg)

In 2025, entry-level quants at top firms pulled $300K-$500K total comp.

AI/ML hiring in finance grew 88% year-over-year.

This article is everything I wish someone had handed me when i started my path laid out in the exact order you should learn it.

_The path is like layers of a video game, where you can't skip levels._

Every concept builds on the last. But if you put in real work, not watching some lame ahh YouTube videos about finance, that's just wasting your time, actual problem-solving work - you can go from knowing nothing to being something in about 18 months.

**_Disclaimer:_**

Not Financial Advice & Do Your Own Research & Markets involve risk.

My own project - [@coldvisionXYZ](<https://x.com/@coldvisionXYZ>)

## Forget everything you think you know about trading

Most people think quantitative trading is about picking stocks. Having opinions on Tesla. Predicting earnings.

Quant trading is about math.

You are mostly working with statistical relationships, pricing inefficiencies, and structural edges that exist because markets are complex systems run by humans who make systematic errors.

## Part **I** : Probability is the Language of Uncertainty

Everything in quantitative finance reduces kinda to 1 question:

_What are the odds, and are the odds in my favor?_

That's probability. If you don't understand probability at a deep level, nothing else in this article matters.

**_Conditional thinking_**

Most people think in absolutes. Something is true or it isn't.

Quants think in conditionals. Given what I know, how likely is this?

![Image](https://pbs.twimg.com/media/HCei_w7XcAAjMwU.png)

The probability of A given B equals the probability of both happening divided by the probability of B. Profound implications.

A stock goes up 60% of days - that's the base rate. But on days when volume is above average, it goes up 75% of the time.

That conditional probability is a NOT BS. The raw 60% is NOISY BS.

**_Bayes' theorem_**

![Image](https://pbs.twimg.com/media/HCejMkSbgAAeuXv.png)

Your updated belief equals

(how likely you'd see this data if your hypothesis were true) * (your prior belief) / (the total probability of seeing this data under any hypothesis).

The denominator sums over all hypotheses.

In practice, you compute this with Monte Carlo sampling.

But the logic is the same. Bayes is how you update your conviction in real time.

A model says a stock should be worth $50. Earnings come out, revenue is 3% above estimate. The Bayesian posterior shifts upward. The traders who update fastest and most accurately win bread.

**_Expected value and variance your two best friends_**

![Image](https://pbs.twimg.com/media/HCejtL7XsAA5vQ7.png)

![Image](https://pbs.twimg.com/media/HCejv0UXIAACqgx.png)

Expected value is your conviction.

Variance is your risk.

If your strategy has positive expected value and you can survive the variance, you likely will make money.

**Level 1 homework (3-4 weeks at 2 hours/day):**

_1\. Read_****

Blitzstein & Hwang, _Introduction to Probability_ (free PDF from Harvard). Every problem in Chapters 1-6.

_2\. Code_****

Simulate 10,000 coin flips, verify the law of large numbers visually.

_3\. Code 2_****

Implement a Bayesian updater takes a prior and likelihood, returns a posterior.


    import numpy as np
    import matplotlib.pyplot as plt

    # Law of large numbers: running average converges to true probability
    np.random.seed(42)
    flips = np.random.choice([0, 1], size=10000, p=[0.5, 0.5])
    running_avg = np.cumsum(flips) / np.arange(1, 10001)

    plt.figure(figsize=(10, 4))
    plt.plot(running_avg, linewidth=0.7)
    plt.axhline(y=0.5, color='r', linestyle='--', label='True probability')
    plt.xlabel('Number of flips')
    plt.ylabel('Running average')
    plt.title('Law of Large Numbers in Action')
    plt.legend()
    plt.savefig('lln.png', dpi=150)
    print(f"After 10,000 flips: {running_avg[-1]:.4f} (true: 0.5000)")


## Part **II** : Statistics

Once you speak probability, you need to learn to listen to data.

![Image](https://pbs.twimg.com/media/HCgQBaXXYAEaXBx.png)

That's statistics and the #1 lesson statistics teaches is "most of what looks like NOT A BS is actually NOISY BS"

Hypothesis testing is the BS detector

You build a model. It backtests at 15% annual return. Is it real?

Set up H_0: "this strategy has zero expected return."

Compute a test statistic.

Calculate a p-value - the probability of seeing results this good if H_0 were true.

BUT If you test 1,000 random strategies, 50 of them will show p-values below 0.05 purely by chance.

That's the multiple comparisons problem.

Ur fix is Bonferroni correction divide your significance threshold by the number of tests

Or use Benjamini-Hochberg for false discovery rate control.

Every single beginner massively overestimates how much NOT A BS they've found. Your first 10 strategies will all be NOISY BS. Accept this now and save yourself a lot of money.

**_Regression decomposing returns_**

Linear regression y=Xβ+ϵ is the workhorse.

In finance, you regress your strategy's returns against known risk factors:

![Image](https://pbs.twimg.com/media/HCgDDAkaEAEvrzK.png)

The intercept α is your **alpha**

the return that can't be explained by known factors. If α is zero after accounting for factors, your "edge" is just disguised market exposure.

The OLS estimator:

![Image](https://pbs.twimg.com/media/HCgDMxxXIAA4zDW.png)

The most important number is α.

Use **Newey-West standard errors** financial data has autocorrelation and heteroskedasticity, so default OLS standard errors are wrong. Using them is like driving with a cracked windshield.

**_Maximum Likelihood Estimation_**

Given data x_1,…,x_n,​ from a model with parameter θ:

![Image](https://pbs.twimg.com/media/HCgQ6rLXUAAaw9F.png)

Set the derivative to zero and solve. (or it's over gng)

MLE is how you calibrate every model in finance fit a GARCH model to volatility, estimate jump-diffusion parameters, calibrate option pricing to market quotes.

It's asymptotically efficient no other consistent estimator has lower variance for large samples (the Cramér-Rao lower bound).

When someone at a firm says they're "calibrating" a model, they almost, like always mean MLE.

**Level 2 homework (4-5 weeks):**

_1\. Read_****

Wasserman,_All of Statistics_ , Chapters 1-13.

_2\. Code_****

Download real stock returns with yfinance. Test normality (they'll fail). Fit a t-distribution via MLE. Compare.

_3\. Code_****

Run a Fama-French 3-factor regression on a stock portfolio using statsmodels.

_4\. Code_****

Implement a permutation test shuffle dates 10,000 times, compare shuffled performance to actual.


    import numpy as np
    from scipy import optimize, stats

    # Demonstrate fat tails: MLE fit of Student-t to return data
    np.random.seed(42)

    # Simulate "realistic" returns (fat tails, slight positive drift)
    true_df = 4
    returns = stats.t.rvs(df=true_df, loc=0.0005, scale=0.015, size=1000)

    def neg_log_likelihood(params, data):
        df, loc, scale = params
        if df <= 2 or scale <= 0:
            return 1e10
        return -np.sum(stats.t.logpdf(data, df=df, loc=loc, scale=scale))

    result = optimize.minimize(
        neg_log_likelihood, x0=[5, 0, 0.01], args=(returns,),
        method='Nelder-Mead'
    )
    fitted_df, fitted_loc, fitted_scale = result.x

    print(f"MLE degrees of freedom: {fitted_df:.2f} (true: {true_df})")
    print(f"MLE location:           {fitted_loc:.6f}")
    print(f"MLE scale:              {fitted_scale:.6f}")

    # Normality test
    _, p_normal = stats.normaltest(returns)
    print(f"\nNormality test p-value: {p_normal:.2e}")
    print(f"Reject normality? {'YES  fat tails confirmed' if p_normal < 0.05 else 'NO'}")


## Part **III** : Linear Algebra

Linear algebra sounds boring. It's the machinery that runs everything: portfolio construction, PCA, neural networks, covariance estimation, factor models. You cannot be a quant without being fluent in matrices.

![Image](https://pbs.twimg.com/media/HCgSDNfawAUriXT.jpg)

**_Thinking in matrices_**

A covariance matrix Σ captures how every asset moves relative to every other asset. For 500 stocks, Σ is 500×500 with 125,250 unique entries. Portfolio variance collapses to a single expression

![Image](https://pbs.twimg.com/media/HCgEBHmWkAIWTsh.png)

This quadratic form is the core of Markowitz portfolio theory, of risk management, of everything.

**_Eigenvalues is what actually matters in a universe of stocks_**

Look at a 500-stock universe and the first 5 eigenvectors explain 70% of all variance. Everything else is NOISY BS.

The first time eigendecomposition u use it the whole world changes. Look at a 500-stock universe and the first 5 eigenvectors explain 70% of all variance. Dimensionality reduction, and it's the foundation of factor investing.

**Level 3 homework (4-6 weeks):**

_1\. Watch_****

Gilbert Strang's MIT 18.06 lectures all of them. Non-negotiable.

_2\. Read_****

Strang,_Introduction to Linear Algebra_. Do the problems.

_3\. Code_****

PCA decomposition of S &P 500 returns. Plot eigenvalue spectrum. Identify top 3 components.

_4\. Code_****

Markowitz mean-variance optimization from scratch.


    import numpy as np
    import cvxpy as cp

    # ============================================
    # Markowitz optimization with cvxpy
    # ============================================
    np.random.seed(42)
    n_assets = 10
    mu = np.random.uniform(0.04, 0.15, n_assets)
    A = np.random.randn(n_assets, n_assets) * 0.1
    cov = A @ A.T + np.eye(n_assets) * 0.01

    w = cp.Variable(n_assets)
    objective = cp.Minimize(cp.quad_form(w, cov))
    constraints = [
        mu @ w >= 0.08,      # minimum return
        cp.sum(w) == 1,       # fully invested
        w >= -0.1,            # max 10% short
        w <= 0.3              # max 30% long
    ]

    prob = cp.Problem(objective, constraints)
    prob.solve()

    ret = mu @ w.value
    vol = np.sqrt(w.value @ cov @ w.value)
    sharpe = (ret - 0.03) / vol

    print(f"Portfolio return:  {ret:.4f}")
    print(f"Portfolio vol:     {vol:.4f}")
    print(f"Sharpe ratio:      {sharpe:.4f}")
    print(f"Weights: {np.round(w.value, 4)}")


## Part **IV** : Calculus & Optimization

Calculus is the language of change. In finance, everything changes: prices, volatilities, correlations, the entire probability distribution shifts second by second. Calculus describes and exploits those changes.

**Derivatives** (the math kind): appears in every neural network backpropagation and every Greek calculation.

**Taylor expansion** :

![Image](https://pbs.twimg.com/media/HCgE6k4boAA07fr.png)

Delta hedging is the first-order approximation.

Gamma hedging adds the second-order correction.

And the reason Itô calculus differs from ordinary calculus is precisely because the second-order Taylor term doesn't vanish for random processes. **Just** **Remember it**

**Level 4 homework (4-5 weeks):**

_1\. Read_

Boyd & Vandenberghe, _Convex Optimization_ (free PDF from Stanford), Chapters 1-5.

_2\. Code_****

Implement gradient descent from scratch. Minimize the Rosenbrock function.

_3\. Code_****

Solve a portfolio optimization problem with cvxpy including transaction cost constraints.

## Part **V** : Stochastic Calculus

Before stochastic calculus, you're a data scientist who likes finance.

After it, you're a quant. QUANTATIVE FINANCE EXPERT, you heard?

![Image](https://pbs.twimg.com/media/HCgU9xXW8AAmAc_.png)

This is where you learn to model randomness in continuous time, derive the Black-Scholes equation from first principles, and understand why the trillion-dollar derivatives market works the way it does.

**_Brownian motion pure randomness, formalized_**

A Brownian motion (Wiener process) W_t is a continuous-time random walk:

  * W_0 = 0
  * Increments W_t - W_s ~ N(0, t - s) for t > s
  * Non-overlapping increments are independent
  * Paths are continuous but _nowhere differentiable_



The critical insight that everything else depends on: dW_t has "size" dt, which means (dW_t)^2 = dt. This sounds like a technicality, but its the single most important fact in quantitative finance.

**Geometric Brownian Motion** models stock prices:

![Image](https://pbs.twimg.com/media/HCgHgzZWIAAmud7.png)

**_Itô's lemma_**

In normal calculus, df = f'(x)dx. You Taylor-expand, and the (dx)^2 term is infinitesimally small you drop it.

But when x is a stochastic process, (dW_t)^2 = dt is _first order_. You can't drop it.

**Itô's lemma** :

![Image](https://pbs.twimg.com/media/HCgHxPzawAE8TWR.png)

Apply it to an option price and you get Black-Scholes. Formula is the engine behind the entire derivatives industry.

**_Deriving Black-Scholes from scratch_**

Follow along with pen and paper.

**Step 1** : Let V(S,t) be an option price. Apply Itô's lemma:

![Image](https://pbs.twimg.com/media/HCgH4u8W8AAi9NX.png)

**Step 2** : Construct a delta-hedged portfolio Π=V−∂S/∂V​⋅S. Compute dΠ:

![Image](https://pbs.twimg.com/media/HCgIDXgXoAA_PP_.png)

The dW_t​ terms cancel perfectly. The portfolio is locally riskless.

**Step 3** : A riskless portfolio must earn the risk-free rate: dΠ=rΠ dtd\Pi = r\Pi \, dt dΠ=rΠdt.

**Step 4** : Substitute and rearrange:

![Image](https://pbs.twimg.com/media/HCgIfdGWYAEfPl8.png)

This is the **Black-Scholes PDE**.

Notice what happened - the drift μ vanished. The option price doesn't depend on the expected return of the stock. Risk preferences don't matter. You can price options as if everyone is risk-neutral. The first time this sinks in genuinely mind-bending.

Solving this PDE for a European call with strike K and expiry T gives:

![Image](https://pbs.twimg.com/media/HCgIq17boAAZdI7.png)

![Image](https://pbs.twimg.com/media/HCgIyuuawAAEWtg.png)

![Image](https://pbs.twimg.com/media/HCgI4E5WoAAzATN.png)

The Greeks

  * **Delta** Δ is How much the option moves per $1 stock move. Your hedge ratio.
  * **Gamma** Γ​: How fast delta changes. Your convexity exposure.
  * **Theta** Θ: Time decay. Typically negative for long options.
  * **Vega** V: Sensitivity to volatility. Where most derivatives money is made.
  * **Rho** ρ: Sensitivity to interest rates.



Delta tells you your hedge ratio. Gamma tells you how often to re-hedge. Theta is the cost of holding. Vega is the bread and butter of vol trading desks.

**Level 5 homework (6-8 weeks - the hardest level):**

_1\. Read_****

Shreve,_Stochastic Calculus for Finance II_. The gold standard.

_2\. Alternative_****

Arguin,_A First Course in Stochastic Calculus_ (newer, more accessible).

_3\. Derive_****

Apply Itô's lemma to f(S)=ln⁡(S) where S follows GBM. Get the −σ^2/2.

_4\. Derive_****

The full Black-Scholes equation from the delta-hedging argument.

_5\. Code_****

Black-Scholes from scratch. Compare to Monte Carlo. Verify convergence.


    import numpy as np
    from scipy.stats import norm

    def black_scholes(S, K, T, r, sigma, option_type='call'):
        d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        if option_type == 'call':
            return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
        else:
            return K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)

    def monte_carlo_option(S0, K, T, r, sigma, n_sims=500_000):
        """Price via risk-neutral simulation (drift = r, not mu)"""
        Z = np.random.standard_normal(n_sims)
        ST = S0 * np.exp((r - sigma**2/2)*T + sigma*np.sqrt(T)*Z)
        payoffs = np.maximum(ST - K, 0)
        price = np.exp(-r*T) * np.mean(payoffs)
        stderr = np.exp(-r*T) * np.std(payoffs) / np.sqrt(n_sims)
        return price, stderr

    def greeks(S, K, T, r, sigma):
        d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        return {
            'delta': norm.cdf(d1),
            'gamma': norm.pdf(d1) / (S * sigma * np.sqrt(T)),
            'theta': -(S*norm.pdf(d1)*sigma)/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2),
            'vega':  S * np.sqrt(T) * norm.pdf(d1),
            'rho':   K * T * np.exp(-r*T) * norm.cdf(d2),
        }

    # Verify: Monte Carlo converges to Black-Scholes
    S, K, T, r, sigma = 100, 105, 1.0, 0.05, 0.2

    bs = black_scholes(S, K, T, r, sigma)
    mc, err = monte_carlo_option(S, K, T, r, sigma)
    g = greeks(S, K, T, r, sigma)

    print(f"Black-Scholes: ${bs:.4f}")
    print(f"Monte Carlo:   ${mc:.4f} ± {err:.4f}")
    print(f"Difference:    ${abs(bs - mc):.4f}\n")
    for name, val in g.items():
        print(f"  {name:>6}: {val:.6f}")


## Polymarket

This is the most interesting market in the world right now and the math behind it connects everything in this article: probability, information theory, convex optimization, integer programming

**_How LMSR prices beliefs_**

The **Logarithmic Market Scoring Rule (LMSR)** , invented by Robin Hanson, powers automated prediction markets. The cost function for n outcomes:

![Image](https://pbs.twimg.com/media/HCgK1C4X0AAdWZK.png)

where q_i​ tracks outstanding shares of outcome i and b is the liquidity parameter. The price of outcome i:

![Image](https://pbs.twimg.com/media/HCgK60sXYAEqP3I.png)

That's the **softmax function** \- function powering every neural network classifier.

Prices always sum to 1, always lie in (0,1), and always exist providing infinite liquidity. The market maker's maximum loss is bounded at b * ln(n)

## The Quant Career Landscape

** _4 archetypes:_**

Quant Researcher

The most-cracked guy who finds patterns in petabytes, builds predictive models, designs strategies. Needs PhD-level math/stats/ML, or exceptional undergraduate achievement. At firms like Jane Street, QRs work with tens of thousands of GPUs.

**Quant Developer/Engineer**

The mid-cracked guy, mostly the builder. Trading platforms, execution engines, real-time data pipelines. Makes the researcher's model actually trade. Needs production C++/Rust/Python, low-latency systems.

**Quant Trader**

Either the biggest degen or the most-cracked guy, mostly the decision-maker. Runs capital, manages risk, makes real-time calls. Highest compensation variance - eight figures in exceptional years.

**Risk Quant**

The most-cracked guy or just insanely experienced corporate guy, mostly the guardian. Model validation, VaR, stress testing, regulatory compliance. Steadier career, lower ceiling. The emerging AI/ML Quant role signal generation with deep learning is the fastest-growing, with hiring up 88% year-over-year in 2025.

**_What it pays:_**

**Level Top Tier (Jane Street, Citadel, HRT)**

New grad $300K-$500K+ total comp

Mid career (3-7yr)$550K-$950K

Senior (8+yr)$1M-$3M+

Star trader/PM $3M-$30M+

****

Mid Tier (Two Sigma, DE Shaw)

New grad $250K–$350K

Mid career (3-7yr) $350K–$625K

Senior (8+yr) $575K–$1.2M

Star trader/PM idk

Jane Street's average employee compensation was reported at $1.4 million/year in H1 2025. That's the average though

**_The interview gauntlet_**

**Resume screen** ->

**Online assessment** (mental math via Zetamac - target 50+, logic puzzles) ->

**Phone screen** (probability problems, betting games) ->

**Superday** (3-5 back-to-back interviews, mock trading, coding, whiteboard derivations).

Jane Street gives problems intentionally too hard to solve alone - they test how you use hints and collaborate.

Over two-thirds of their recent intern class studied CS; over a third studied math. Finance knowledge generally not required.

**The #1 prep resource**

 _Xinfeng Zhou's Green Book_ (_A Practical Guide to Quantitative Finance Interviews_) - 200+ real problems.

Supplement with [QuantGuide.io](<http://QuantGuide.io/>) ("LeetCode for quants")

Brainstellar

Jane Street's Figgie card game

## The Complete Toolbox

**Python stack**

 _Data:_ pandas, polars (Polars is 10-50x faster on large datasets)

_Numerics:_ numpy, scipy

 _ML (tabular):_ xgboost, lightgbm, catboost

 _ML (deep):_ pytorch

 _Optimization:_ cvxpy

 _Derivatives:_ QuantLib (Industry-grade, C++ backend)

_Stats:_ statsmodels

 _Backtesting:_ NautilusTrader

 _Backtesting (simpler):_ backtrader, vectorbt (Easier starting point)

_Quant research:_ Microsoft Qlib (17K+ stars, AI-oriented)

_RL for trading:_ FinRL (10K+ stars)

**_C++ and Rust_**

Tbh i don't know anything about this. This is what I've found:

_C++ libraries:_ QuantLib, Eigen, Boost.

_Rust:_ RustQuant for option pricing, NautilusTrader as the Rust+Python paradigm (Rust core for speed, Python API for research).

**_Data sources_**

 _Free_ : yfinance, Finnhub (60 calls/min), Alpha Vantage.

_Mid-range_ : [Polygon.io](<http://Polygon.io/>) ($199/mo, sub-20ms latency), Tiingo.

_Enterprise:_ Bloomberg Terminal (~$32K/yr), Refinitiv, FactSet.

_Blockchain:_ Alchemy (free tier with archive access).

**_Solvers_**

 _Gurobi:_ Fastest commercial MIP solver, free academic license. Essential for combinatorial arbitrage.

_Google OR-Tools_ : Strongest free solver.

_PuLP/Pyomo:_ Python modeling interfaces.

## The Reading List (In Order)

**Mathematics**

  1. Blitzstein & Hwang - _Introduction to Probability_ (free PDF from Harvard)
  2. Strang - _Introduction to Linear Algebra_ \+ MIT 18.06 lectures
  3. Wasserman - _All of Statistics_
  4. Boyd & Vandenberghe - _Convex Optimization_ (free PDF from Stanford)
  5. Shreve - _Stochastic Calculus for Finance I & II_



**Quant finance**

  1. Hull - _Options, Futures, and Other Derivatives_
  2. Natenberg - _Option Volatility and Pricing_
  3. López de Prado - _Advances in Financial Machine Learning_
  4. Ernest Chan - _Quantitative Trading_
  5. Zuckerman - _The Man Who Solved the Market_



Interview prep

  1. Zhou - _Practical Guide to Quantitative Finance Interviews_ (Green Book #1)
  2. Crack -_Heard on the Street_
  3. Joshi - _Quant Job Interview Questions_



**Competitions**

  * Jane Street Kaggle ($100K prize)
  * WorldQuant BRAIN (100K+ users, pays for alpha signals)
  * Citadel Datathon (fast-track to employment)
  * Jane Street monthly puzzles (above interview difficulty)



## Three things I wish I'd known earlier

**Estimation error is the real enemy.**

Full Kelly betting, unconstrained Markowitz, ML models with too many features - they all fail for the same reason: overfitting NOISY BS in parameter estimates.

The math works perfectly with true parameters. You never have true parameters. The gap between theory and practice is always estimation error, and the best quants are the ones who respect it.

**Tools have democratized. Conviction hasn't.**

Anyone can access QuantLib, [Polygon.io](<http://Polygon.io/>), and PyTorch. Technology is necessary but not sufficient. Edge lives in unique data, unique models, or unique execution - not better pip installs.

**The math is the moat**

AI can write code and suggest strategies. But the ability to derive _why_ Itô's lemma has an extra term, to prove that discounted prices are martingales under the risk-neutral measure, to know when a convex relaxation is tight versus loose in a combinatorial market that mathematical fluency separates quants who build edge from quants who borrow it. And borrowed edge expires.

## What comes in Part 2

Part 2 covers: exotic derivatives (barriers, Asians, lookbacks), stochastic volatility (Heston model calibration), jump-diffusion (Merton), advanced measure theory (martingale representation, optional stopping), stochastic control for optimal execution (Almgren-Chriss), reinforcement learning for market making, transformer architectures for financial time series, FPGA trading infrastructure, WebSocket feeds, parallel execution, Frank-Wolfe with Gurobi for combinatorial arbitrage across thousands of conditions.

The math gets harder. The paycheck gets longer

[Posted Mar 3, 2026 at 6:43PM](<https://twitter.com/gemchange_ltd/status/2028904166895112617>)

**This piece is about something more specific:** what the door looks like, and what it takes to walk through it.

## Problem 1: Correlation Matrix

** _n_ random variables. Any two have the same pairwise correlation _ρ._ What is the valid range of _ρ_?**

Before writing anything, the candidate explains their logic. This isn't a formality. It's the first thing the interviewer is evaluating.

Two properties define a valid correlation matrix.

**First:** the diagonal elements are always 1, and the matrix is symmetric.

**Second:** the matrix must be positive semidefinite: no linear combination of the variables can have negative variance, because variance is never negative. no linear combination of the variables can have negative variance, because variance is never negative.

**looks like this:**


    A = (1 − ρ)·I + ρ·11ᵀ


**A matrix of this form (an equicorrelation matrix) has exactly two distinct eigenvalues:**


    λ₁ = 1 + (n−1)ρ    (multiplicity 1)
    λ₂ = 1 − ρ         (multiplicity n−1)


**For A to be positive semidefinite, both eigenvalues must be ≥ 0:**


    1 − ρ ≥ 0   →   ρ ≤ 1
    1 + (n−1)ρ ≥ 0   →   ρ ≥ −1/(n−1)


**Answer: ρ ∈ [−1/(n−1), 1]**

![Image](https://pbs.twimg.com/media/HCqXopeaUAMYvzA.png)

**Two sanity checks worth doing out loud:**

**With n = 2:** the range collapses to [−1, 1]

That's the standard result for two variables. Makes sense.

**With n = 3:** the floor is −1/2

**Here's why:** if you have three variables and their sum is constant, say X₁ + X₂ + X₃ = c

Then Var(X₁ + X₂ + X₃) = 0, which forces 3σ² + 6ρσ² = 0, giving ρ = −1/2

The geometry is a perfect equilateral triangle in probability space. You can't push them further apart than that.

More variables, tighter floor. The constraint is real.

_Most candidates jump straight to calculation. The ones who get the offer usually pause first and ask: "What property of the matrix am I actually enforcing here?" The answer: variance must be non-negative. That is the whole insight. Everything else is algebra._

## Problem 2: Conditional Regression

**X and Y are IID, both uniform on [0,1]. What is β in the regression of Y on X, given X + Y > 1?**

**The formula for β in simple regression:** Cov(X, Y) / Var(X), computed under the conditional distribution.

Start geometrically. X and Y uniform on [0,1] means their joint distribution is uniform over the unit square.

The condition **X + Y > 1** restricts it to the upper-right triangle.

Since **P(X + Y > 1) = 0.5**, the conditional density on that triangle becomes 2

![Image](https://pbs.twimg.com/media/HCqZDbBXwAAs0CU.jpg)

**Computing all moments under f(x,y | X+Y >1) = 2:**


    E(X | X+Y>1)   = 2/3
    E(X² | X+Y>1)  = 1/2
    E(XY | X+Y>1)  = 5/12

    Cov = 5/12 − (2/3)² = 15/36 − 16/36 = −1/36
    Var = 1/2  − (2/3)² =  9/18 −  8/18 =  1/18

    β = (−1/36) / (1/18) = −1/2


**Answer: β = −1/2**

**The interviewer pushes back._"Is there a faster way?"_**

This is where most people slow down. The follow-up isn't a harder problem. It's a test of whether you can step back from computation and think structurally.

**The answer:** β in a linear regression is just E(Y | X = x), read as a function of x

**Given X = x with X + Y > 1:** Y must be greater than 1−x. Under the conditional distribution, Y | {X = x, X+Y > 1} is uniform on (1−x, 1)


    E(Y | X = x, X+Y > 1) = (1−x + 1) / 2 = 1 − x/2


## The coefficient on x is −1/2. Same answer. Two lines instead of a page of integrals

**Here's what took me a moment to see:** **X** and **Y** are completely independent before any conditioning.

But given **X + Y > 1**, they become negatively correlated.

If **X** is large,**Y** had less room to be large.

And vice versa, сonditioning on their sum created a dependency that wasn't there.

**Berkson's paradox**

It's a specific form of collider bias, a phenomenon where conditioning on a shared consequence of two independent causes makes them appear correlated.

**Joseph Berkson first described it in hospital data in 1946:**

Patients admitted for any reason looked like disease**A** and disease **B** were negatively correlated, simply because hospitalization was a function of both. The math here is the same structure.

_Knowing the name won't get you the job. Understanding why conditioning flips the sign will_

## Problem 3: Target Sum

**Given an array of integers and a target, count the number of ways to assign + or − to each element so the total equals the target.**

**Example:** [1, 1, 1, 1, 1], target = 3

First instinct: depth-first search.

Build a decision tree. Each node is [index, running_sum]. At each step, branch left (+) or right (−)

Count the leaves where running_sum == target.

![Image](https://pbs.twimg.com/media/HCqbAtXXoAAb-Vc.png)

The candidate codes this up. It passes 69 of 141 test cases

Then: Time Limit Exceeded. **Current complexity:**


    O(2ⁿ)  exponential: binary tree of depth n, 2ⁿ leaves


The problem is redundancy, many branches in the tree reach the same (index, running_sum) state through different paths.

The code recomputes the same subproblem over and over.

**Fix:** memoization. Cache each state the first time you reach it.


    class Solution:
        def findTargetSumWays(self, nums: List[int], target: int) -> int:
            dp = {}
            n = len(nums)

            def dfs(i, total):
                if i == n:
                    return 1 if total == target else 0
                if (i, total) in dp:
                    return dp[(i, total)]
                dp[(i, total)] = (
                    dfs(i+1, total + nums[i]) +
                    dfs(i+1, total - nums[i])
                )
                return dp[(i, total)]

            return dfs(0, 0)


![Image](https://pbs.twimg.com/media/HCqbnJ2XUAAPaob.jpg)

**New complexity:**


    O(n × T)  where T = number of unique running sum values


**Answer: 5**

**You can verify by hand:** with [1,1,1,1,1] and target 3, you need exactly 4 positive and 1 negative (since 4−1 = 3). That's C(5,4) = 5 ways, one for each position of the minus sign.

**_The brute-force solution isn't the failure here. The failure would be not knowing why it's slow. Recognizing redundant subproblems, naming the fix, and implementing it cleanly: that sequence is what the coding round is testing. is what the coding round is testing. The interviewer already knows the answer. They're watching whether you do._**

## What Three Problems Actually Reveal

The interviewer says this explicitly in the video: the problems are basic. In reality, quant interviews run 10+ rounds. These are the warm-up questions.

What's being evaluated isn't whether you've seen these problems before. How you explain your thinking. Talking through your logic before writing anything is the primary signal. A candidate who gets the right answer silently is less useful than one who gets halfway there with clear reasoning.

Quants work in teams. They have to communicate models to other quants, to traders, to risk managers.

Whether you adapt. The follow-up on Problem 2 wasn't harder. It was a different angle. Switching methods under gentle pressure is a signal that your understanding isn't brittle.

How you handle being stuck. Asking for a hint is acceptable. The interviewer says so directly. Stopping and saying "I don't know" is not.

**The expectation:** try different approaches, say what you're trying, ask if you're still stuck after genuine effort.

Whether you understand complexity. Not what the formula is. Why it matters. And what to do when your first solution isn't good enough.

**_The gap between people who pass and people who don't is rarely raw mathematical ability. It's whether they can show their thinking clearly, adapt when pushed, and stay composed when the first approach fails._**

## Want to try it yourself? These will hurt

**Correlation matrices:**

  * Strang, Introduction to Linear Algebra
  * Horn & Johnson, Matrix Analysis
  * MIT 18.06 Lecture 25 (video)
  * Statistical Odds & Ends, "Equicorrelation Matrix"



**Berkson's paradox:**

  * Berkson, "Limitations of Fourfold Table Analysis"
  * Elwert & Winship, "Endogenous Selection Bias"
  * Pearl, Causal Inference in Statistics: A Primer



**Dynamic programming:**

  * Demaine, MIT 6.006 Lectures 15-18
  * Cormen et al., Introduction to Algorithms
  * LeetCode #494



**Quant interview prep:**

  * Zhou, A Practical Guide to Quantitative Finance Interviews
  * Crack, Heard on The Street
  * Joshi, Quant Job Interview Q&A
  * Mosteller, Fifty Challenging Problems in Probability
  * Sheffield, MIT 18.600

![Image](https://pbs.twimg.com/media/HCqfzbnX0AExFQZ.png)




[Posted Mar 5, 2026 at 5:30PM](<https://twitter.com/phosphenq/status/2029610565132505510>)
