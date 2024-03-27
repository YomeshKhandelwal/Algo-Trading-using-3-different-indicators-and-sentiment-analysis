import yfinance as yf
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def calculate_ema(data, window):
    return data['Close'].ewm(span=window, adjust=False).mean()

def calculate_bollinger_bands(data, window=20, num_std_dev=2):
    data['MA'] = data['Close'].rolling(window=window).mean()
    data['UpperBand'] = data['MA'] + (data['Close'].rolling(window=window).std() * num_std_dev)
    data['LowerBand'] = data['MA'] - (data['Close'].rolling(window=window).std() * num_std_dev)
    return data

a = input("ENTER STOCK NAME WITH .NS: ")

# Download historical data as a DataFrame
data = yf.download(a, period='2d', interval='1m')

# Calculate EMA200 and Bollinger Bands
data['EMA200'] = calculate_ema(data, window=200)
data = calculate_bollinger_bands(data)

fig, ax = plt.subplots()

def animate(i):
    # Download updated data
    data = yf.download(a, period='2d', interval='1m')
    
    # Calculate EMA200 and Bollinger Bands with updated data
    data['EMA200'] = calculate_ema(data, window=200)
    data = calculate_bollinger_bands(data)
    
    # Print the real-time Close Price
    current_price = data['Close'].iloc[-1]
    current_ema = data['EMA200'].iloc[-1]
    current_upper_band = data['UpperBand'].iloc[-1]
    current_lower_band = data['LowerBand'].iloc[-1]
    
    print(f"Real-time Close Price: {current_price:.2f}")
    print(f"Real-time EMA200 Price: {current_ema:.2f}")
    print(f"Real-time Upper Bollinger Band: {current_upper_band:.2f}")
    print(f"Real-time Lower Bollinger Band: {current_lower_band:.2f}")
    
    ax.clear()
    ax.plot(data.index, data['EMA200'], label='EMA200', color='green')  
    ax.plot(data.index, data['Close'], label='Price', color='blue')
    ax.plot(data.index, data['UpperBand'], label='Upper Bollinger Band', color='red', linestyle='solid')
    ax.plot(data.index, data['LowerBand'], label='Lower Bollinger Band', color='violet', linestyle='solid')
    
    ax.set_title(f'EMA200 and Bollinger Bands of {a} Over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True)

# Set interval to 60000 milliseconds (or 60 seconds)
ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()