# strategy.py
import pandas as pd
import ta

def generate_signals(df):
    df['ema'] = ta.trend.ema_indicator(df['close'], window=20).ema_indicator()
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    df['atr'] = ta.volatility.average_true_range(df['high'], df['low'], df['close'], window=14)

    df['signal'] = None

    for i in range(1, len(df)):
        if df['close'][i] > df['ema'][i] and df['rsi'][i] < 30:
            df.loc[i, 'signal'] = {'type': 'BUY'}
        elif df['close'][i] < df['ema'][i] and df['rsi'][i] > 70:
            df.loc[i, 'signal'] = {'type': 'SELL'}

    return df
