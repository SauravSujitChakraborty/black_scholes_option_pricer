import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """
    Calculates the theoretical price of a European Call option using 
    the Black-Scholes-Merton model.

    Parameters:
    -----------
    S : float
        Current price of the underlying asset (Stock Price).
    K : float
        Exercise price of the option (Strike Price).
    T : float
        Time to expiration in years (e.g., 0.5 for 6 months).
    r : float
        Annualized risk-free interest rate (decimal, e.g., 0.05 for 5%).
    sigma : float
        Annualized volatility of the asset returns (decimal, e.g., 0.3 for 30%).

    Returns:
    --------
    call_price : float
        Theoretical value of the European Call option.
    d1 : float
        The 'moneyness' factor representing the risk-adjusted probability.
    d2 : float
        The probability that the option will be exercised at expiration.

    Raises:
    -------
    ValueError : 
        If inputs are mathematically invalid (e.g., negative price, 
        zero volatility, or zero time to expiration).
    """
    
    # --- ERROR HANDLING ---
    if S <= 0 or K <= 0:
        raise ValueError("Stock Price (S) and Strike Price (K) must be greater than zero.")
    if T <= 0:
        raise ValueError("Time to Expiration (T) must be positive. The option has already expired.")
    if sigma <= 0:
        raise ValueError("Volatility (sigma) must be greater than zero to calculate d1.")

    # --- CALCULATION LOGIC ---
    # 1. Calculate d1 (The 'Moneyness' of the option)
    # Measures how far the option is in-the-money relative to volatility over time.
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    
    # 2. Calculate d2 (The probability of exercise)
    # Represents the strike-adjusted probability of the option ending in-the-money.
    d2 = d1 - sigma * np.sqrt(T)
    
    # 3. Calculate Call Price via Black-Scholes Formula
    # Call = [Expected Asset Value] - [Present Value of Exercise Cost]
    call_price = (S * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))
    
    return call_price, d1, d2

# --- MARKET DATA INPUTS ---
try:
    S = 150.0      # Current Price
    K = 155.0      # Strike Price
    T = 0.5        # 6 Months (0.5 years)
    r = 0.05       # 5% Interest
    sigma = 0.30   # 30% Volatility

    # Run Calculation
    price, d1, d2 = black_scholes_call(S, K, T, r, sigma)

    # --- FORMATTED QUANT REPORT ---
    print("\n--- 📈 BLACK-SCHOLES QUANT REPORT ---")
    print(f"{'Metric':<18} | {'Value':>14}")
    print("-" * 35)

    print(f"{'Stock Price':<18} | {S:14.2f}")
    print(f"{'Strike Price':<18} | {K:14.2f}")
    print(f"{'Volatility (σ)':<18} | {sigma:14.2f}")
    print("-" * 35)

    print(f"{'d1 (Moneyness)':<18} | {d1:14.4f}")
    print(f"{'d2 (Prob)':<18} | {d2:14.4f}")
    print("-" * 35)

    # Currency Formatting
    price_str = f"${price:.2f}"
    print(f"{'CALL OPTION VAL':<18} | {price_str:>14}")
    print("-" * 35)

except ValueError as e:
    print(f"INPUT ERROR: {e}")
except Exception as e:
    print(f"AN UNEXPECTED ERROR OCCURRED: {e}")
