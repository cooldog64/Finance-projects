import yfinance as yf
import pandas as pd
import statsmodels.api as sm
ticker = 'V'
market = '^Gspc' #SandP500

data = yf.download([ticker, market], start = '2021-1-1', 
                   end = '2026-9-27', auto_adjust = True)
prices = data['Close']
monthly_prices = prices.resample("ME").last()
returns = monthly_prices.pct_change()
print(returns.head())
returns = returns.dropna()
returns.columns = ['Stock', 'Market']
import statsmodels.api as sm