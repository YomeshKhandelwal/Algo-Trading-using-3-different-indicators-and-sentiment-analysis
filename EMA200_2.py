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

# Download historical data as a DataFrame
data = yf.download(a, period='1d', interval='1m')

# Calculate EMA200
data['EMA200'] = calculate_ema(data, window=200)

# Print the real-time Close Price and EMA200
current_price = data['Close'].iloc[-1]
current_ema = data['EMA200'].iloc[-1]

print(f"Real-time Close Price: {current_price:.2f}")
print(f"Real-time EMA200 Price: {current_ema:.2f}")

while True:
    if current_price < current_ema:
        print("YOU SHOULD BUY")
        b = "BUY"
        order()
        print("YOU'VE BOUGHT SUCCESSFULLY")
        
    elif current_price > current_ema:
        print("YOU SHOULD SELL")
        b = "SELL"
        order()
        print("YOU'VE SOLD SUCCESSFULLY")

    time.sleep(1)
