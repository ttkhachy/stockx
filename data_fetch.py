import yfinance as yf
import pandas as pd

def get_stock_data(ticker, period):
    """
    try:

        ticker = yf.Ticker(ticker_input)
        current_price = ticker.info["currentPrice"]
        data = ticker.history(period=period_slct)

        return current_price, data
    except:
        return "Error: Invalid Ticker", None
    """
    pass

def get_dividend_data(ticker: str, input_period: str):
    
    if dividends.empty:
        print("No dividend data available for the selected ticker.")
    else:
        print(dividends)




ticker = yf.Ticker("AAPL")
print(ticker.info["shortName"])
dividends = ticker.dividends  # Fetch all available dividend data

df_test = ticker.dividends.reset_index()  # Convert to DataFrame
#print(df_test)

# Rename columns for clarity
df_test.columns = ["Date", "Dividend"]
print(df_test["Date"])
