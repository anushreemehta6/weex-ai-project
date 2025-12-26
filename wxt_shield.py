# bot/wxt_shield.py

from bot.state import state

def allocate_wxt(profit):
    if profit > 0:
        state["wxt_pool"] += profit * 0.10
