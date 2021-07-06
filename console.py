import setup

clearConsole = lambda: print('\n' * 150)

def start(current_price, balance, open_trades):

    info(current_price, balance, open_trades)

    confirmation = input("\nType 'confirm' to start: ")
    return confirmation

def status(current_price, balance, open_trades, phase_number):

    info(current_price, balance, open_trades)
    print("Phase number: ", phase_number)


def info(current_price, balance, open_trades):

    clearConsole()
    print("\nTrading Bot v1.0", "\n")

    print("Test server: ", setup.test_server)
    print("Selected market: ", setup.symbol)
    print("Current price: ", current_price)
    print("Balance: ", balance)
    print("Open trades: ", len(open_trades), "\n")

    print("Upper TP: ", setup.upper_tp, "%")
    print("Lower TP: ", setup.lower_tp, "%")
    print("First short: ", setup.first_short, "%")
    print("First amount: ", setup.first_amount, "$\n")

    print("Price increaser list: \n")
    for i in range(len(setup.price_increaser_list)):
        print(i+1, "value: ", setup.price_increaser_list[i], "x")  