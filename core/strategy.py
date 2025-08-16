
import pandas as pd
import ta

def generate_signals(df):
    # Ensure Close is a 1D series by using .squeeze()
    close_series = df['Close'].squeeze()  
    
    # Calculate indicators
    df['RSI'] = ta.momentum.RSIIndicator(close=close_series).rsi()
    df['20DMA'] = close_series.rolling(window=20).mean()
    df['50DMA'] = close_series.rolling(window=50).mean()
    
    # Original 'and' is too strict. Using 'or' will generate more signals.
    df['Buy'] = (df['RSI'] < 30) | (df['20DMA'] > df['50DMA'])

    return df