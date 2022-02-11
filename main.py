import console
import logic
import time
import api

def main():

    confirmation = console.start(api.get_current_price(), api.get_balance(), api.get_open_orders())
    if confirmation != "c":
        exit()

    #logic.start()

    

if __name__ == '__main__':
    main()