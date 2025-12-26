# bot/strategy.py

import pandas as pd
import ta

def prepare_indicators(raw_data):
    df = pd.DataFrame(raw_data)
    df.columns = ["timestamp", "open", "high", "low", "close", "volume"]

    df["close"] = df["close"].astype(float)

    df["ema20"] = ta.trend.ema_indicator(df["close"], 20)
    df["ema50"] = ta.trend.ema_indicator(df["close"], 50)
    df["rsi"] = ta.momentum.rsi(df["close"], 14)

    return df


def generate_signal(df):
    latest = df.iloc[-1]

    if latest["ema20"] > latest["ema50"] and latest["rsi"] < 70:
        return "BUY"
    elif latest["ema20"] < latest["ema50"]:
        return "SELL"
    else:
        return "HOLD"
