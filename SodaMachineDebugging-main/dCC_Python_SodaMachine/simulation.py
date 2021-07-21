from customer import Customer
from soda_machine import SodaMachine
from coins import Coin


class Simulation:
    def __init__(self):
        self.name = (Coin)
        self.value = (Coin)
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()       #add from customer import Customer  ##add name value line 10
        soda_machine = SodaMachine()    # add from soda_machine import SodaMchine
        will_proceed = False
        while will_proceed:
            user_option = self.user_interface.simulation_main_menu() #add self. user_interface
            if user_option == "1":      #added '==' to fix syntax error.
                soda_machine.begin_transaction(customer)
            elif user_option == "2":
                customer.check_coins_in_wallet()
            elif user_option == "3":
                customer.check_backpack()
            else:
                will_proceed = False
