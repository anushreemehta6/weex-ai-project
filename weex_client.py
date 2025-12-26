import time
import hmac
import hashlib
import base64
import json
import requests
from .config import API_KEY, SECRET_KEY, PASSPHRASE, BASE_URL


def sign_get(timestamp, method, path, query):
    message = timestamp + method.upper() + path + query
    signature = hmac.new(
        SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).digest()
    return base64.b64encode(signature).decode()


def sign_post(timestamp, method, path, query, body):
    message = timestamp + method.upper() + path + query + body
    signature = hmac.new(
        SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).digest()
    return base64.b64encode(signature).decode()


def weex_get(path, query=""):
    timestamp = str(int(time.time() * 1000))
    signature = sign_get(timestamp, "GET", path, query)

    headers = {
        "ACCESS-KEY": API_KEY,
        "ACCESS-SIGN": signature,
        "ACCESS-TIMESTAMP": timestamp,
        "ACCESS-PASSPHRASE": PASSPHRASE,
        "Content-Type": "application/json",
        "locale": "en-US"
    }

    return requests.get(BASE_URL + path + query, headers=headers)


def weex_post(path, body, query=""):
    timestamp = str(int(time.time() * 1000))
    body_json = json.dumps(body)
    signature = sign_post(timestamp, "POST", path, query, body_json)

    headers = {
        "ACCESS-KEY": API_KEY,
        "ACCESS-SIGN": signature,
        "ACCESS-TIMESTAMP": timestamp,
        "ACCESS-PASSPHRASE": PASSPHRASE,
        "Content-Type": "application/json",
        "locale": "en-US"
    }

    return requests.post(BASE_URL + path, headers=headers, data=body_json)
