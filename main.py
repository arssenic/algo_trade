import pandas as pd
from data_fetcher import fetch_stock_data
from strategy import generate_signals
from backtester import run_backtest
from google_sheets_logger import log_to_sheets
from ml_model import run_ml_model
from telegram_alert import send_telegram_alert
import logging
logging.basicConfig(level=logging.INFO)

STOCKS = ['SBIN.NS', 'INFY.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'TATASTEEL.NS']
INTERVAL = '1d'
PERIOD = '6mo'

def main():
    for stock in STOCKS:
        try:
            data = fetch_stock_data(stock, INTERVAL, PERIOD)
            df=pd.DataFrame(data)
            df= generate_signals(df)
            result = run_backtest(df, stock)
            log_to_sheets(result, stock)
            acc = run_ml_model(df, stock)
            send_telegram_alert(f"{stock} | ML accuracy: {acc:.2f}")
        except Exception as e:
            send_telegram_alert(f"Error for {stock}: {e}")

if __name__ == "__main__":
    main()
