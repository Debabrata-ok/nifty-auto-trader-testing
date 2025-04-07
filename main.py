# main.py
from kite_login import get_kite_client
from data_fetcher import fetch_nifty_data
from strategy import generate_signals
from trade_executor import place_order
import time

if __name__ == "__main__":
    kite = get_kite_client()

    while True:
        try:
            df = fetch_nifty_data(kite)
            df = generate_signals(df)

            latest_signal = df.iloc[-1]['signal']
            if latest_signal:
                place_order(kite, latest_signal)
            else:
                print("📉 No trade signal generated.")

        except Exception as e:
            print(f"❌ Error in main loop: {e}")

        time.sleep(900)  # Wait 15 minutes before checking again
