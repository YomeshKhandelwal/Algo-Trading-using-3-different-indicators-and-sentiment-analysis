import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def calculate_rsi(data, window=14):
    # Calculate daily price changes
    delta = data['Close'].diff(1)

    # Calculate gain and loss
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate average gain and average loss over the specified window
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()

    # Calculate the relative strength (RS)
    rs = avg_gain / avg_loss

    # Calculate the relative strength index (RSI)
    rsi = 100 - (100 / (1 + rs))

    return rsi

def plot_rsi(stock_symbol, start_date, end_date):
    # Download historical stock data using yfinance
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Calculate RSI
    stock_data['RSI'] = calculate_rsi(stock_data)

    # Print RSI values
    print("RSI Values:")
    print(stock_data['RSI'])

    # Plotting the stock prices and RSI
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(stock_data['Close'], label='Close Price')
    plt.title(f'{stock_symbol} Stock Price and RSI')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(stock_data['RSI'], label='RSI', color='orange')
    plt.axhline(70, color='r', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='g', linestyle='--', label='Oversold (30)')
    plt.title('Relative Strength Index (RSI)')
    plt.legend()

    plt.show()

# Example usage
a = input("Enter stock name with .ns : ")
stock_symbol = a
start_date = '2022-01-01'
end_date = '2023-01-01'
plot_rsi(stock_symbol, start_date, end_date)
