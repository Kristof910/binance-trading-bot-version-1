from binance.spot import Spot
from binance.client import Client
import setup

#import logging
#from binance.lib.utils import config_logging

spot = Spot(key=setup.api_key, secret=setup.api_secret)
client = Client(setup.api_key, setup.api_secret)

def api_check():
    pass

def get_balance():
    data = spot.account()
    return data["balances"][0]["free"]

def get_current_price():
    #data = client.get_symbol_info('BTCUSDT')
    #data2 = client.get_exchange_info()
    #logging.info(spot.avg_price("BTCUSDT"))
    data = spot.avg_price("BTCUSDT")
    return data["price"]

def trade(param1, param2, param3):
    pass



def test():

    client = Spot()
    print(client.time())

    client = Spot(key=api_key, secret=api_secret)

    # Get account information
    print(client.account())

    # Post a new order
    '''params = {
        'symbol': 'BTCUSDT',
        'side': 'SELL',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 0.002,
        'price': 9500
    }

    response = client.new_order(**params)
    print(response)'''

