import pandas as pd
import numpy as np

def backtest_strategy_by_shares(data, signals, initial_capital=100000.0, shares=10, interest_rate=0.05):    
    # apply the strategy to the portfolio
    portfolio = pd.DataFrame(index=data.index) 
    
    # setup our holdings
    portfolio['shares_aquired'] = shares * signals['signal']    
    portfolio['original'] = initial_capital    
    portfolio['shares_total'] = portfolio['shares_aquired'].cumsum()
    portfolio['asset_price'] = data['Close']
    portfolio['purchase_total'] = portfolio['shares_aquired'] * data['Close']
    portfolio['asset_value'] = data['Close'] * portfolio['shares_total']    

    # deal with our cash
    portfolio['cash'] = initial_capital
    portfolio['cash'] = portfolio['cash'] - portfolio['purchase_total'].cumsum()
    
    portfolio['cash_30_day_rolling_mean'] = portfolio.groupby(portfolio.index.tz_localize(None).to_period('M'))['cash'].transform('mean')
    portfolio['cash_30_day_mean'] = 0.0
    last_days = portfolio.groupby(portfolio.index.tz_localize(None).to_period('M')).tail(1).index
    portfolio.loc[last_days, 'cash_30_day_mean'] = portfolio.loc[last_days, 'cash_30_day_rolling_mean']
    portfolio.drop(columns=['cash_30_day_rolling_mean'], inplace=True)

    #portfolio.iloc[29::30, portfolio.columns.get_loc('cash_30_day_mean')] = portfolio['cash_30_day_rolling_mean'].iloc[29::30].values                           
    portfolio['interest_payment'] = portfolio['cash_30_day_mean'] * interest_rate / 12
    portfolio['interest_total']  = portfolio['interest_payment'].cumsum()

    # compute the total and daily returns    
    portfolio['total'] = portfolio['cash'] + portfolio['asset_value']
    portfolio['total_with_interest'] = portfolio['total'] + portfolio['interest_total']
    portfolio['cash_with_interest'] = portfolio['cash'] + portfolio['interest_total']
    portfolio['returns'] = portfolio['total'].pct_change()
    return portfolio

def backtest_strategy_by_amount(data, signals, initial_capital=100000.0, incremental_investment=1000, interest_rate=0.05):    
    # apply the strategy to the portfolio
    portfolio = pd.DataFrame(index=data.index) 
    
    # setup our holdings

    portfolio['shares_aquired'] = (incremental_investment / data['Close']) * signals['signal']    
    portfolio['original'] = initial_capital 
    portfolio['shares_total'] = portfolio['shares_aquired'].cumsum()
    portfolio['asset_price'] = data['Close']
    portfolio['purchase_total'] = portfolio['shares_aquired'] * data['Close']
    portfolio['asset_value'] = data['Close'] * portfolio['shares_total']    

    # deal with our cash
    portfolio['cash'] = initial_capital
    portfolio['cash'] = portfolio['cash'] - portfolio['purchase_total'].cumsum()
    
    portfolio['cash_30_day_rolling_mean'] = portfolio.groupby(portfolio.index.tz_localize(None).to_period('M'))['cash'].transform('mean')
    portfolio['cash_30_day_mean'] = 0.0
    last_days = portfolio.groupby(portfolio.index.tz_localize(None).to_period('M')).tail(1).index
    portfolio.loc[last_days, 'cash_30_day_mean'] = portfolio.loc[last_days, 'cash_30_day_rolling_mean']
    portfolio.drop(columns=['cash_30_day_rolling_mean'], inplace=True)
    
    portfolio['interest_payment'] = portfolio['cash_30_day_mean'] * interest_rate / 12
    portfolio['interest_total']  = portfolio['interest_payment'].cumsum()

    # compute the total and daily returns    
    portfolio['total'] = portfolio['cash'] + portfolio['asset_value']
    portfolio['total_with_interest'] = portfolio['total'] + portfolio['interest_total']
    portfolio['cash_with_interest'] = portfolio['cash'] + portfolio['interest_total']
    portfolio['returns'] = portfolio['total'].pct_change()
    return portfolio
