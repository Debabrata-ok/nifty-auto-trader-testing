# data_fetcher.py
from kiteconnect import KiteConnect
import pandas as pd
from datetime import datetime, timedelta


def fetch_nifty_data(kite: KiteConnect, symbol="NIFTY 50", interval="15minute", days=10):
    instrument_token = 256265  # NIFTY 50 index token

    to_date = datetime.now()
    from_date = to_date - timedelta(days=days)

    data = kite.historical_data(
        instrument_token,
        from_date.strftime("%Y-%m-%d %H:%M:%S"),
        to_date.strftime("%Y-%m-%d %H:%M:%S"),
        interval
    )

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    return df
