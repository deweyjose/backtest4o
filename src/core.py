import datetime
import argparse
import data as dt
import strategies as st
import backtest as bt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mplcursors import cursor

week_days = [0, 1, 2, 3, 4]

week_day_map = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}


def show_portfolio_performance(data, portfolio, ticker, week_day):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    asset_value = portfolio["asset_value"].iloc[-1]
    cash = portfolio["cash"].iloc[-1]
    interest_total = portfolio["interest_total"].iloc[-1]
    total = portfolio["total"].iloc[-1]
    original = portfolio["original"].iloc[-1]

    ax1.yaxis.get_major_formatter().set_scientific(False)
    ax1.set_ylabel("Portfolio value in $")
    ax1.plot(
        portfolio.index,
        portfolio["asset_value"],
        label=f"Asset Value: ${asset_value:,.2f}",
    )
    ax1.plot(portfolio.index, portfolio["cash"], label=f"Cash:  ${cash:,.2f}")
    ax1.plot(
        portfolio.index,
        portfolio["interest_total"],
        label=f"Interest: ${interest_total:,.2f}",
    )
    ax1.plot(portfolio.index, portfolio["total"], label=f"Total Value: ${total:,.2f}")
    ax1.plot(
        portfolio.index,
        portfolio["original"],
        label=f"Initial Investment: ${original:,.2f}",
    )

    ax2 = ax1.twinx()
    ax2.set_ylabel("Price in $")
    ax2.plot(data.index, data["Close"], label="Close Price", color="blue", alpha=0.3)

    ax1.legend(loc="upper left")
    ax2.legend(loc="lower right")
    plt.title(f"Portfolio Value - {week_day_map[week_day]} buys {ticker}")
    plt.grid()
    plt.show()


def build_summary(ticker, week_day, portfolio, summary):
    asset_value = portfolio["asset_value"].iloc[-1]
    cash = portfolio["cash"].iloc[-1]
    interest_total = portfolio["interest_total"].iloc[-1]
    total = portfolio["total"].iloc[-1]
    original = portfolio["original"].iloc[-1]

    # Create a new row as a dictionary
    new_row = pd.DataFrame(
        {
            "Ticker": [ticker],
            "WeekDay": [week_day],
            "Original": [original],
            "Assets": [asset_value],
            "Cash": [cash],
            "Interest": [interest_total],
            "Total": [total],
        }
    )

    new_row = new_row.dropna(axis=1, how="all")

    # Append the new row to the summary DataFrame
    summary = pd.concat([summary, new_row], ignore_index=True)

    return summary

def process_tickers(tickers, start_date, end_date, initial_capital, incremental_investment, show_portfolio):
    summary = pd.DataFrame(
        columns=["Ticker", "WeekDay", "Original", "Assets", "Cash", "Interest", "Total"]
    )

    for ticker in tickers:
        data = dt.download_stock_data(ticker, start_date, end_date)
        for week_day in week_days:
            signals = st.buy_on_day_of_week(data, week_day)
            portfolio = bt.backtest_strategy_by_amount(
                data, signals, initial_capital, incremental_investment
            )
            if show_portfolio:
                show_portfolio_performance(data, portfolio, ticker, week_day)
            summary = build_summary(ticker, week_day, portfolio, summary)                    

    return summary
