import datetime
import argparse
from data import download_stock_data

def main():
    parser = argparse.ArgumentParser(description='Download stock data')
    parser.add_argument('--ticker', type=str, help='Stock ticker symbol', required=True)
    parser.add_argument('--start_date', type=datetime.date.fromisoformat, help='Start date for data retrieval (YYYY-MM-DD)', required=True)
    parser.add_argument('--end_date', type=datetime.date.fromisoformat, help='End date for data retrieval (YYYY-MM-DD)', required=True)
    args = parser.parse_args()

    ticker = args.ticker
    start_date = args.start_date
    end_date = args.end_date

    data = download_stock_data(ticker, start_date, end_date)
    print(data.head())

if __name__ == "__main__":
    main()
