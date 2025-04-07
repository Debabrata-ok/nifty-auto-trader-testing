print("kite_login module loaded")
# kite_login.py
from kiteconnect import KiteConnect
import os

api_key = "api_key"
api_secret = "api_secret"

request_token = "request_token"  # Obtain manually once by logging in to Kite Connect
access_token_file = "access_token_file"

def get_kite_client():
    kite = KiteConnect(api_key=api_key)

    if os.path.exists(access_token_file):
        with open(access_token_file, "r") as f:
            access_token = f.read().strip()
            kite.set_access_token(access_token)
    else:
        data = kite.generate_session(request_token, api_secret=api_secret)
        access_token = data["access_token"]
        with open(access_token_file, "w") as f:
            f.write(access_token)
        kite.set_access_token(access_token)

    return kite
