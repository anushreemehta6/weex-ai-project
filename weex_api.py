# bot/weex_api.py

import requests

def get_klines(symbol="BTCUSDT", interval="1m", limit=100):
    url = "https://api.weex.com/api/v2/market/kline"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["data"]
