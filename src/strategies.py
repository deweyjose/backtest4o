import pandas as pd
import numpy as np

def moving_average_strategy(data, short_window=40, long_window=100):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    # Create short simple moving average
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    # Create long simple moving average
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)       
    return signals

def buy_on_day_of_week(data, day_of_week=0):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    # Setup day of week 
    signals['day_of_week'] = data.index.dayofweek
    # Create signals
    signals['signal'] = np.where(signals['day_of_week'] == day_of_week, 1.0, 0.0)    
    return signals
