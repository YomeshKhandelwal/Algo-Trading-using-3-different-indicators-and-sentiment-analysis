from kite_trade import *
import time
enctoken = "gwamAEbFQ7kbmatUyNn7xUq82WCuHE9d5ukUMNAd6vMgZwliCaCm7pBkJ+KjrtybmLbIUA4bR5xvy593M9VRSxtZMYMyvKZTjkjobNAplf5DJSwTisEUgA=="
kite = KiteApp(enctoken=enctoken)

# Get Live Data
print(kite.ltp("NSE:RELIANCE"))
print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))
while True:
    print(kite.quote(["NSE:NIFTY BANK", "NSE:ACC", "NFO:NIFTY22SEPFUT"]))
    time.sleep(1)
    
