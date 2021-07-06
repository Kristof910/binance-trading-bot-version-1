import console
import api
import time

def main():

    confirmation = console.start(api.get_current_price(), api.get_balance(), api.get_open_orders())
    if confirmation != "confirm":
        exit()

    #for i in range(10):
        #console.status(api.get_current_price(), api.get_balance(), api.get_open_orders(), i)

    for i in range(100):
          print(api.get_current_price())
          time.sleep(1)



    api.open_trade("BUY", "MARKET", "0.002", 0, 0, 0)

    

if __name__ == '__main__':
    main()