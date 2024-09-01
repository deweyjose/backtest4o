## setup
```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## usage
```
backtest4o git:(main) python src/main.py --help
usage: main.py [-h] --tickers TICKERS --start_date START_DATE --end_date END_DATE --initial_capital INITIAL_CAPITAL --incremental_investment INCREMENTAL_INVESTMENT [--summary_path SUMMARY_PATH] [--show_portfolio]

Download stock data

options:
  -h, --help            show this help message and exit
  --tickers TICKERS     Comma delimited list of stock tickers
  --start_date START_DATE
                        Start date for data retrieval (YYYY-MM-DD)
  --end_date END_DATE   End date for data retrieval (YYYY-MM-DD)
  --initial_capital INITIAL_CAPITAL
                        Initial capital for backtesting
  --incremental_investment INCREMENTAL_INVESTMENT
                        Incremental investment amount for backtesting
  --summary_path SUMMARY_PATH
                        Path to save the summary.csv. Then load into excel or sheets for analysis
  --show_portfolio      Show portfolio performance (close the windown to proceed)
```
