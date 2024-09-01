import pandas as pd
import yfinance as yf
import os

def download_stock_data(ticker, start_date, end_date, interval='1d'):
    if not os.path.exists(f'data/{ticker}.csv'):
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date, interval=interval, back_adjust=True)
        if not os.path.exists('data'):
            os.makedirs('data')
        data.to_csv(f'data/{ticker}.csv')
        return data
    else:
        data = pd.read_csv(f'data/{ticker}.csv', parse_dates=['Date'])
        data.set_index('Date', inplace=True)
        data.index = pd.to_datetime(data.index, utc=True)        
        return data
