#working
import yfinance as yf

def fetch_stock_data(symbol, interval, period):
    data = yf.download(symbol, interval=interval, period=period)
    data.dropna(inplace=True)
    return data
