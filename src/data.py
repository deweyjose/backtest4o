import pandas as pd
import yfinance as yf
import os


def download_stock_data(ticker, start_date, end_date, interval="1d"):
    """
    Download stock data for a given ticker and save it to a CSV file.
    
    Args:
        ticker (str): Ticker symbol of the stock.
        start_date (str): Start date of the data in the format 'YYYY-MM-DD'.
        end_date (str): End date of the data in the format 'YYYY-MM-DD'.
        interval (str, optional): Interval of the data (default is '1d').
    
    Returns:
        pandas.DataFrame: Stock data.
    """
    if not os.path.exists(f"data/{ticker}_{start_date}_{end_date}.csv"):
        stock = yf.Ticker(ticker)
        data = stock.history(
            start=start_date, end=end_date, interval=interval, back_adjust=True
        )
        if not os.path.exists("data"):
            os.makedirs("data")
        data.to_csv(f"data/{ticker}_{start_date}_{end_date}.csv")
        return data
    else:
        data = pd.read_csv(f"data/{ticker}_{start_date}_{end_date}.csv", parse_dates=["Date"])
        data.set_index("Date", inplace=True)
        data.index = pd.to_datetime(data.index, utc=True)
        return data
