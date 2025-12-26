from .weex_client import weex_get

def get_position():
    path = "/capi/v2/account/position/singlePosition"
    query = "?symbol=cmt_btcusdt"
    response = weex_get(path, query)
    return response.status_code, response.text

def get_balance():
    path = "/capi/v2/account/assets"
    response = weex_get(path)
    return response.status_code, response.text