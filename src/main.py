import datetime
import argparse
import data as dt
import strategies as st
import backtest as bt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from core import process_tickers
from mplcursors import cursor

def main():
    parser = argparse.ArgumentParser(description="Download stock data")
    parser.add_argument(
        "--tickers",
        type=str,
        help="Comma delimited list of stock tickers",
        required=True,
    )
    parser.add_argument(
        "--start_date",
        type=datetime.date.fromisoformat,
        help="Start date for data retrieval (YYYY-MM-DD)",
        required=True,
    )
    parser.add_argument(
        "--end_date",
        type=datetime.date.fromisoformat,
        help="End date for data retrieval (YYYY-MM-DD)",
        required=True,
    )
    parser.add_argument(
        "--initial_capital",
        type=int,
        help="Initial capital for backtesting",
        required=True,
    )
    parser.add_argument(
        "--incremental_investment",
        type=int,
        help="Incremental investment amount for backtesting",
        required=True,
    )
    parser.add_argument(
        "--summary_path",
        type=str,
        help="Path to save the summary",
        required=False,
    )
    parser.add_argument(
        "--show_portfolio",
        action="store_true",
        help="Show portfolio performance",
        required=False,
    )
    args = parser.parse_args()

    tickers = args.tickers.split(",")
    start_date = args.start_date
    end_date = args.end_date
    initial_capital = args.initial_capital
    incremental_investment = args.incremental_investment
    summary_path = args.summary_path
    show_portfolio = args.show_portfolio


    summary = process_tickers(tickers, start_date, end_date, initial_capital, incremental_investment, show_portfolio)

    if (summary_path):
        summary.to_csv(summary_path, index=False)  


if __name__ == "__main__":
    main()
