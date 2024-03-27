from kite_trade import *
#Replace with your enctoken
enctoken = "Ph=="
kite = KiteApp(enctoken=enctoken)

# Place Order
order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NSE,
                         tradingsymbol="SUZLON",
                         transaction_type=kite.TRANSACTION_TYPE_BUY,
                         quantity=1,
                         product=kite.PRODUCT_MIS,
                         order_type=kite.ORDER_TYPE_MARKET,
                         price=None,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="Yomesh's Trade")


print(order)