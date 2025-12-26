# bot/trader.py

from bot.state import state

def execute_trade(signal):
    if signal == "BUY":
        state["balance"] += 20
    elif signal == "SELL":
        state["balance"] -= 10

    state["max_balance"] = max(state["max_balance"], state["balance"])
