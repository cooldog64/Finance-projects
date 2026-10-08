from datetime import date
import yfinance as yf
import pandas as pd
import statsmodels.api as sm
# function to get beta for inputted stock
today = date.today()
def get_beta(ticker, start='2021-1-1', end=today, market='^GSPC'):
    ''' Give ticker and optionally the market start and end dates in 
    year-month-day format and get beta back. Options for markets, 
    SandP500: ^GSPC, Nasdaq: ^NDX, DowJones: ^DJI '''
    
    print("\nWelcome to this Beta calculator.\n ---")
    ticker = ticker.upper()
    
    # Download data from yfinance
    data = yf.download([ticker, market], start, end, auto_adjust = True)
    prices = data['Close']
    monthly_prices = prices.resample("ME").last()
    returns = monthly_prices.pct_change()
    returns = returns.dropna()
    returns.columns = ['Stock', 'Market']
    X = returns['Market']
    Y = returns['Stock']
    X = sm.add_constant(returns['Market'])
    model = sm.OLS(Y, X).fit()
    Beta = model.params['Market']
    
    print(f"\nThe beta for {ticker} for the {market} from {start} to {end} is: {Beta:.2f}")
         