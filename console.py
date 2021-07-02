
clearConsole = lambda: print('\n' * 150)

def start(current_price, balance):

    selected_market = "BTC-USDT"
    #clearConsole()
    print("\nTrading Bot v1.0\n")

    print("Selected market: ", selected_market)
    print("Current price: ", current_price)
    print("BTC Balance: ", balance, "\n")


    param1 = input("Enter buy-in or type 'market': ")
    param2 = input("Enter stop-win rate in %: ")
    param3 = input("Enter stop-loss rate in %: ")

    print("\n")

    return param1, param2, param3

