from customer import Customer
from soda_machine import SodaMachine
from coins import Coin
import user_interface

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()       
        soda_machine = SodaMachine()    # add from soda_machine import SodaMchine
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu() #add self. user_interface
            if user_option == "1":      #added '==' to fix syntax error.
                soda_machine.begin_transaction(customer)
            elif user_option == "2":
                customer.check_coins_in_wallet()
            elif user_option == "3":
                customer.check_backpack()
            else:
                will_proceed = False
