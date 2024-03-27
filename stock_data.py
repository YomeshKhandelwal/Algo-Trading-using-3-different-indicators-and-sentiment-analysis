import yfinance as yf
import pandas as pd

def get_stock_data(symbol, days=200):
    # Download stock data
    stock_data = yf.download(symbol, period=f"{days}d")

    # Filter relevant columns
    stock_data = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']]

    return stock_data

def save_to_csv(data, symbol):
    # Save data to CSV file
    filename = f"{symbol}_stock_data.csv"
    data.to_csv(filename)
    print(f"Stock data saved to {filename}")

if __name__ == "__main__":
    # Replace 'AAPL' with the desired stock symbol
    stock_symbol = 'AAPL'

    # Fetch stock data
    stock_data = get_stock_data(stock_symbol)
    print(stock_data)
    # Save data to CSV file
    save_to_csv(stock_data, stock_symbol)
