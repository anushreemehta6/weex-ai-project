import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEEX_API_KEY")
SECRET_KEY = os.getenv("WEEX_API_SECRET")
PASSPHRASE = os.getenv("WEEX_API_PASSPHRASE")

BASE_URL = "https://api-contract.weex.com"
