def risk_action(risk_score, threshold=0.02):
    """
    Decide whether trading is allowed
    """
    if risk_score > threshold:
        return "BLOCK"
    return "SAFE"
