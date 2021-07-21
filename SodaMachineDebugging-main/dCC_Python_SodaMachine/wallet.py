from coins import Coin #add from coins import Coins line 1 (wallet.py)

class Wallet:
    def __init__(self):
        self.money = []
        self.fill_wallet = ()
        self.coins = Coin #add self.coins = coins line 7, wallet.py


def fill_wallet(self, coins): #add coins as param line 10 wallet.py
    """Method will fill wallet's money list with certain amount of each type of coin when called."""
    for index in range(8):
        self.money.append(coins.Quarter())
    for index in range(10):
        self.money.append(coins.Dime())
    for index in range(20):
        self.money.append(coins.Nickel())
    for index in range(50):
        self.money.append(coins.Penny())
