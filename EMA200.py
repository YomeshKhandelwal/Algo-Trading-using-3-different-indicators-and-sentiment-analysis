import yfinance as yf
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import requests



def calculate_ema(data, window):
    return data['Close'].ewm(span=window, adjust=False).mean()

a = input("ENTER STOCK NAME WITH .NS: ")

# Download historical data as a DataFrame
data = yf.download(a, period='2d', interval='1m')

# Calculate EMA200
data['EMA200'] = calculate_ema(data, window=200)

fig, ax = plt.subplots()
 
def animate(i):
    # Download updated data
    data = yf.download(a, period='2d', interval='1m')
    # Calculate EMA200 with updated data
    data['EMA200'] = calculate_ema(data, window=200)
    
    # Print the real-time Close Price
    current_price = data['Close'].iloc[-1]
    current_ema = data['EMA200'].iloc[-1]
    print(f"Real-time Close Price: {current_price:.2f}")
    print(f"Real-time EMA200 Price: {current_ema:.2f}")
    
    ax.clear()
    ax.plot(data.index, data['EMA200'], label='EMA200', color='green')  
    ax.plot(data.index, data['Close'], label='Price', color='blue')
    ax.set_title(f'EMA200 and Close Price of {a} Over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True)
    
# Set interval to 60000 milliseconds (or 60 seconds)
ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()