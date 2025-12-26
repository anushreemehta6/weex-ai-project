import requests

def get_price_history(symbol="BTCUSDT", limit=50):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": "1m",
        "limit": limit
    }
    data = requests.get(url, params=params).json()

    prices = [float(candle[4]) for candle in data]  # close prices
    return prices
