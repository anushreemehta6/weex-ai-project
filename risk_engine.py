def calculate_risk(volatility, exposure=1.0):
    """
    Risk score calculator.
    exposure = position size multiplier (default demo = 1.0)
    """
    risk_score = volatility * exposure
    return float(min(risk_score, 1.0))
