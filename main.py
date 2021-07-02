import console
import api

def main():

    buy_in, stop_win, stop_loss = console.start(api.get_current_price(), api.get_balance())



if __name__ == '__main__':
    main()