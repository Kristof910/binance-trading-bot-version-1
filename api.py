from binance.spot import Spot
from binance.client import Client
import setup
import time


if setup.test_server: # test server
    spot = Spot(key=setup.testnet_api_key, secret=setup.testnet_api_secret, base_url="https://testnet.binance.vision")
    client = Client(setup.testnet_api_key, setup.testnet_api_secret)
else: # binance server
    spot = Spot(key=setup.binance_api_key, secret=setup.binance_api_secret)
    client = Client(setup.binance_api_key, setup.binance_api_secret)


def get_balance():
    data = spot.account()
    return data["balances"][0]["free"] # 0 is BTC balance and can't be referred as setup.symbol

def get_current_price():
    data = spot.avg_price(setup.symbol)
    time.sleep(1)
    return data["price"]

def open_trade(side, type, quantity, price, stop_win, stop_loss):
    params = {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "MARKET",
    #"timeInForce": "GTC",
    "quantity": 0.002,
    #"price": 9500,
}
    
    trade_setup = spot.new_margin_order(**params)
    print(trade_setup)

def get_open_orders():
    return spot.get_open_orders(setup.symbol)



#data = client.get_symbol_info('BTCUSDT')
#data2 = client.get_exchange_info()
