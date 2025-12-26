import random
import numpy as np

def predict_volatility(prices=None):
    """
    AI volatility estimator.
    Uses simulated prices if none provided.
    """
    if prices is None:
        prices = [100 + random.uniform(-1, 1) for _ in range(50)]

    prices = np.array(prices)
    returns = np.diff(prices) / prices[:-1]
    volatility = np.std(returns)

    return float(volatility)
