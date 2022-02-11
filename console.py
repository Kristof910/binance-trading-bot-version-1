import setup

clearConsole = lambda: print('\n' * 150)

def start(current_price, balance, open_trades):

    info(current_price, balance, open_trades)

    confirmation = input("\nType 'c' to confirm or anything else to quit: ")
    return confirmation

def status(current_price, balance, open_trades, phase_number, phase_rounds):

    info(current_price, balance, open_trades)
    print("\nCurrent phase number: ", phase_number)
    print("Successful phase rounds: ", phase_rounds)


def info(current_price, balance, open_trades):

    clearConsole()
    print("\nTrading Bot v1.0", "\n")

    print("Selected market: ", setup.symbol)
    print("Current coin price: ", current_price)
    print("Selected account balance: ", balance)
    print("Open trades: ", len(open_trades), "\n")

    print("Upper TP: ", setup.upper_tp, "%")
    print("Lower TP: ", setup.lower_tp, "%")
    print("First short: ", setup.first_short, "%")
    print("First amount: ", setup.first_amount, "$\n")

    print("Price increaser list: \n")
    for i in range(len(setup.price_increaser_list)):
        print(i+1, "value: ", setup.price_increaser_list[i], "x")  