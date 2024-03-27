import requests

def order():
    
    while True:
        x=[]
        a = int(input("Enter number of stocks : "))
        for i in range(0,a):
            b = input(f"Enter the trading symbol {i+1} : ")
            x.append(b)
        #x = input("Enter the trading symbol (e.g., RELIANCE): ")
            y = int(input(f"Enter the Quantity {i+1} : "))
            z = input(f"Enter the transaction_type (BUY/SELL) {i+1} : ").upper()
            print(z)


            if z not in ["BUY", "SELL"]:
                print("GIVE THE INPUT AGAIN : ")
                z = input(f"Enter the transaction_type (BUY/SELL) {i + 1} : ").upper()
                print("OKAY")
                print(z)
            
            e = input(f"Enter the product type (MIS/CNC) {i+1} : ").upper()

            if e not in ["MIS", "CNC"]:
                print("GIVE THE INPUT AGAIN : ")
                e = input(f"Enter the transaction_type (MIS/CNC) {i + 1} : ").upper()
                print("OKAY")
                print(e)
            
            f = input(f"Enter the order_type (Market/Limit/Stoploss Limit/SL-Market) {i+1} : ").upper()

            if f not in ["MARKET", "LIMIT", "STOPLESS LIMIT", "SL MARKET"]:
                print("GIVE THE INPUT AGAIN : ")
                f = input(f"Enter the transaction_type (Market/Limit/Stoploss Limit/SL Market) {i + 1} : ").upper()
                print("OKAY")
                print(f)

            g = input(f"Enter the Exchange type (NSE/BSE) {i+1} : ").upper()

            if g not in ["NSE", "BSE"]:
                print("GIVE THE INPUT AGAIN : ")
                g = input(f"Enter the Exchange type (NSE/BSE) {i + 1} : ").upper()
                print("OKAY")
                print(g)

            order_params = {
            "tradingsymbol": x,
            "exchange": g,
            "transaction_type": z,
            "order_type":f,
            "quantity": y,
            "product": e,
            "variety": "regular",
            tag:"Yomesh's Trade"
            }

            headers = {"Authorization": "enctoken vE49MmfyTYDhCQ5ve6HiolxCdpRHIDFvkNaTvjlIu5wOPfwTEIB7zBXYxczO+XWbdETIoUEj5nWK8UaWwnvj6JMLH3na/O6pt7akRTAXWZwSksBhjgF42A=="}

            response = requests.post("https://api.kite.trade/orders/regular", headers=headers, data=order_params)

            if response.status_code == 200:
                print(f"Order placed. ID is: {response.text}")
            else:
                 print(f"Failed to place order. Message is: {response.text}")

       
        order_repeat = input("Do you want to place another order? (yes/no): ").lower()
        if order_repeat != 'yes':
            break

if __name__ == "__main__":
    order()