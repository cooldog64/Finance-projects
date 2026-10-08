import yfinance as yf
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
# Get ticker info and set up market we are using
print("Welcome to this interactive Beta calculator.\n ---")
ticker = input("Enter a ticker: ")
ticker = ticker.upper()

market = '^GSPC' #SandP500
# Download data from yfinance
data = yf.download([ticker, market], start = '2021-1-1', 
                   end = '2026-9-27', auto_adjust = True)
prices = data['Close']
monthly_prices = prices.resample("ME").last()
returns = monthly_prices.pct_change()
print(returns.head())

# Set up regression
returns = returns.dropna()
returns.columns = ['Stock', 'Market']
X = returns['Market']
Y = returns['Stock']
X = sm.add_constant(returns['Market'])
model = sm.OLS(Y, X).fit()

#Print output
print(model.summary())
Beta = model.params['Market']
print(f"\nThe beta is: {Beta:.2f}")

sns.scatterplot(x=returns['Date'], y='Stock', data=returns)
plt.show()
