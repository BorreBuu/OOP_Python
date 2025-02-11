class Wallet:
    def __init__(self):
        self.__money = 0

    # A getter method
    # @poperty decorator must be introduced before the setter method,
    # or there will be an error
    @property
    def money(self):
        return self.__money

    # A setter method
    @money.setter
    def money(self, money):
        if money >= 0:
            self.__money = money
        #else:
            #raise ValueError("The amount must not be below zero")
        
wallet = Wallet()
print(wallet.money)

wallet.money = 50
print(wallet.money)

wallet.money = -30
print(wallet.money)