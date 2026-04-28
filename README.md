# black_scholes_option_pricer 

NOTE :- Tis project was made by me in Mar'25, subsequently preserved and published on Apr11'26.

THEORY :-

1. Introduction 

==> The Black-Scholes model is a differential equation used to solve for the theoretical value of European-style options. It assumes that stock prices follow a Geometric Brownian Motion (random walk with drift) and that markets are efficient.

2. The Mathematical Core
 
==> The value of a Call option is essentially the "Expected Value" of the stock at expiration minus the "Present Value" of the cost to buy it.

 => $$ C = S_0 N(d_1) - K e^{-rT} N(d_2) $$

where the components are:

 => $​S_0 N(d_1)$: The expected value of the stock, weighted by the probability of finishing "in-the-money."

 => $​K e^{-rT} N(d_2)$: The cost of exercising the option, discounted back to today's dollars.

 => $​N(\cdot)$: The Cumulative Standard Normal Distribution (the norm.cdf in my code).

​3. The Probability Factors ($d_1$ and $d_2$)

==> ​These variables are the "engine" of the Black-Scholes model:

 => $$ d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})T}{\sigma \sqrt{T}} $$

 => $$ d_2 = d_1 - \sigma \sqrt{T} $$

 => $d_1$ (Moneyness): Measures how far the option is "in-the-money" relative to the standard deviation of the stock’s returns.

 => $d_2$ (Exercise Probability): Represents the risk-adjusted probability that the option will be exercised at expiration (T).

4. Computational Logic

==> Input Variables used in the Simulation:

 => Stock Price ($S$): $150.00 (Current market value).

 => Strike Price ($K$): $155.00 (The price at which we have the right to buy).

 => Volatility ($\sigma$): 30% (Annualized standard deviation of returns).

 => Time ($T$): 0.5 years (6 months until expiration).

 => Risk-Free Rate ($r$): 5% (The yield on a "safe" asset like a Treasury bond).

5. The Python Implementation:
 
==> Stochastic Library: Utilizes scipy.stats.norm to access the Cumulative Distribution Function ($CDF$) of a standard normal distribution, which is required for the $N(d)$ terms.

==> Error Handling: The code includes a robust "Guard Clause" system to prevent mathematical errors (e.g., negative prices or zero volatility which would cause a division-by-zero).

==> Precision: Calculations are performed with high floating-point precision to ensure accurate Greeks (sensitivities) could be derived in future iterations.

 6. Results & Analysis
 
 ==> According to the output generated:

=> Theoretical Call Value: $12.14

7. Interpretation:

Even though the stock price ($150) is currently lower than the strike price ($155), the option still has a value of $12.14. This is due to Time Value and Volatility—there is a statistical chance that the stock will climb above $155 within the next 6 months.

8. Core Packages :-

==> NumPy: Used for vectorized logarithmic and exponential calculations (computing $d_1$, $d_2$, and the continuous discounting factor $e^{-rT}$).
==> SciPy (`scipy.stats`): Utilized for the Cumulative Distribution Function (CDF) of the standard normal distribution, essential for calculating the delta-adjusted probabilities. 

9. Installation :-

==> Cloning the repository :-

git clone https://github.com/SauravSujitChakraborty/black_scholes_option_pricer.git

==> Installing the dependencies :-

pip install -r requirements.txt
