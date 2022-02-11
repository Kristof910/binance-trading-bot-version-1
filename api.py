from binance.client import Client
import setup


binance_client = Client(setup.binance_api_key, setup.binance_api_secret)


def get_balance():
    balance = binance_client.futures_account_balance()
    return balance[1]['balance']

def get_current_price():
    result = binance_client.futures_symbol_ticker(symbol=setup.symbol)
    return result["price"]

def change_leverage(leverage):
    leverage_change = binance_client.futures_change_leverage(symbol=setup.symbol, leverage=leverage)

def open_trade(quantity, side):

    positionSide = ""
    if side == "BUY":
        positionSide = "LONG"
    elif side == "SELL":
        positionSide = "SHORT"    

    #test_hedge_mode = binance_client.futures_get_position_mode()
    #print("TEST HERE 1: ", test_hedge_mode)

    #test_hedge_mode_2 = binance_client.futures_coin_change_position_mode(dualSidePosition = "true")
    #print("TEST HERE 2:", test_hedge_mode_2)

    binance_client.futures_create_order(
        symbol=setup.symbol,
        type='LIMIT', # for testing, otherwise "MARKET"
        timeInForce='GTC',  
        price=65000,  # for testing, otherwise clear this line
        positionSide=positionSide,  
        side=side,
        quantity=quantity  
    )


def get_open_orders():
    result = binance_client.futures_get_open_orders(symbol=setup.symbol)
    return result

