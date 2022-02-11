import api
import setup


def start():
    stop = False
    
    while stop is False: # program infinite loop
        all_open_trades = [] # storing open trades for stop-loss, take-profit data
        phase = 0

        all_open_trades.append(make_trade(1, 1, 'SELL', '123', '456')) # first step
        new_phase_value = 0 # set up new_phase_value here
        new_phase_side = True # True = Long, False = Short

        while stop is False: # main phase loop (1sec repeating)
            if len(all_open_trades) == 0: # checking for finished sequence, WARNING -> this can be problematic if the code stops if there are no open orders at the moment
                break
            else: 

                all_open_trades = check_triggers(all_open_trades) # with check_triggers the all_open_reades list is changed
                new_phase_side, new_phase_value, phase = regular_sequence(new_phase_side, new_phase_value, phase) # REGULAR SEQUENCE
                    

def regular_sequence(new_phase_side, new_phase_value, phase):
    modified_phase = phase
    modified_nps = new_phase_side
    modified_npv = new_phase_value

    if new_phase_side is True: # Long
        if api.get_current_price > new_phase_value: # new phase section (new trade opening), have to be made
            # what to do -> give new modified_nps/npv and make new trade too
            modified_phase += 1
    elif new_phase_value is False: # Short
        if api.get_current_price < new_phase_value: # new phase section (new trade opening), have to be made
            # what to do -> give new modified_nps/npv and make new trade too
            modified_phase += 1  

    return modified_nps, modified_npv, modified_phase        

def make_trade(leverage, quantity, side, stop_loss, take_profit): # this def should give back a dictionary what contains the data for the trade to be stored
    api.change_leverage(leverage)
    current_trade = api.open_trade(quantity, side) # NEEDS TO BE MADE
    order_info = {'id': 'trade_id_here', 'stop_loss' : stop_loss, 'take_profit' : take_profit} 
    return order_info

def check_triggers(all_open_trades): # loop for checking all open trades for stop-loss, take-profit triggers
    modified_trade_list = all_open_trades 
    counter = 0 # for indexing

    for trade in all_open_trades:
        if trade['stop_loss'] >= api.get_current_price():
            # close order write here
            del modified_trade_list[counter] # remove trade from new list
            #pass
        elif trade['take_profit'] <= api.get_current_price():
            # close order write here
            del modified_trade_list[counter] # remove trade from new list
            #pass
        else:
            pass
        counter += 1

    return modified_trade_list
