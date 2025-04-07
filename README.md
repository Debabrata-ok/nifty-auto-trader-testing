# 📊 Automated Nifty 50 Trading Strategy

This project is a fully automated trading system built using Python and Zerodha's KiteConnect API. It is designed to execute trades on **Nifty 50 futures** based on a data-driven strategy using **RSI**, **EMA**, and **ATR** indicators.

## ✅ Features

- 🔐 **KiteConnect API Login**  
  Handles secure authentication with Zerodha.

- 📈 **Real-Time & Historical Data Fetching**  
  Pulls Nifty futures data using KiteConnect.

- ⚙️ **Strategy Engine**  
  Uses technical indicators to generate precise buy/sell signals.

- 💰 **Live Order Execution**  
  Places market orders directly on the NSE via Zerodha.

- ⏱️ **15-Minute Interval Trading**  
  Executes logic and places trades every 15 minutes.

- 📦 **Modular Design**  
  Easy to read, debug, and extend.

## 🧠 Strategy Logic
- **Entry Signals**: Based on EMA crossovers and RSI threshold.
- **Exit Signals**: Based on RSI reversal and ATR-based stop-loss.
- **Stop Loss / Take Profit**: Implemented for risk management.

## 📁 Project Structure
```bash
nifty50-auto-trader/
├── main.py               # Main execution loop
├── kite_login.py         # Zerodha login logic
├── data_fetcher.py       # Fetch OHLC data
├── strategy.py           # Signal generation logic
├── trade_executor.py     # Live trading logic
```

## 🧰 Installation
```bash
git clone https://github.com/Debabrata-ok/nifty50-auto-trader.git
cd nifty50-auto-trader
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

> 📌 Make sure to place your Kite API key, secret, and token inside `kite_login.py` securely.

## ⚠️ Disclaimer
> This bot is designed for **educational purposes only**. Trading involves financial risk. Always backtest and paper trade before deploying with real money. Use at your own risk.

## 📬 Contributions
Pull requests and issues are welcome!

---

Built with 💼 for traders by [Debabrata sahababu](https://github.com/Debabrata-ok)  
