import yfinance as yf
import pandas as pd
import requests
import time

symbol_input = input("ENTER STOCK NAME (e.g., 'AAPL' or 'AAPL.NS'): ").upper()

# Add ".NS" suffix if not present
a = symbol_input if symbol_input.endswith('.NS') else f"{symbol_input}.NS"

#Replace with your enctoken
headers = {"Authorization": "enctoken +FIH=="}

def order():
    order_params = {
        "tradingsymbol": symbol_input,
        "exchange": "NSE",
        "transaction_type": b,
        "order_type": "MARKET",
        "quantity": 1,
        "product": "CNC",
        "variety": "regular",
    }

    response = requests.post("https://api.kite.trade/orders/regular", headers=headers, data=order_params)

    if response.status_code == 200:
        print(f"Order placed. ID is: {response.text}")
    else:
        print(f"Failed to place order. Message is: {response.text}")

def calculate_ema(data, window):
    return data['Close'].ewm(span=window, adjust=False).mean()

def calculate_bollinger_bands(data, window=20, num_std_dev=2):
    data['MA'] = data['Close'].rolling(window=window).mean()
    data['UpperBand'] = data['MA'] + (data['Close'].rolling(window=window).std() * num_std_dev)
    data['LowerBand'] = data['MA'] - (data['Close'].rolling(window=window).std() * num_std_dev)
    return data

while True:
    # Download live data
    live_data = yf.download(a, period='1d', interval='1m')
    
    # Calculate live EMA 200 and Bollinger Bands
    live_data['EMA200'] = calculate_ema(live_data, window=200)
    live_data = calculate_bollinger_bands(live_data)
    
    # Print the real-time values
    current_price = live_data['Close'].iloc[-1]
    current_upper_band = live_data['UpperBand'].iloc[-1]
    current_lower_band = live_data['LowerBand'].iloc[-1]
    current_ema = live_data['EMA200'].iloc[-1]

    print(f"Real-time Close Price: {current_price:.2f}")
    print(f"Real-time Upper Bollinger Band: {current_upper_band:.2f}")
    print(f"Real-time Lower Bollinger Band: {current_lower_band:.2f}")
    print(f"Real-time EMA 200: {current_ema:.2f}")

    if current_price < current_lower_band:
        print("YOU SHOULD BUY")
        b = "BUY"
        order()
        print("YOU'VE BOUGHT SUCCESSFULLY")
        
    elif current_price > current_upper_band:
        print("YOU SHOULD SELL")
        b = "SELL"
        order()
        print("YOU'VE SOLD SUCCESSFULLY")
        
    else:
        print("YOU SHOULD WAIT")
    
    time.sleep(1)  