class CreditCard:
    # the attribute number is private, while the attribute name is accessible
    def __init__(self, number: str, name: str, balance: float):
        self.__number = number
        self.name = name
        self.__balance = balance

    def deposit_money(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def withdraw_money(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def retrieve_balance(self):
        return self.__balance

card = CreditCard("123456","Randy Riches", 100)
print(card.name)
card.name = "Charlie Churchmouse"
print(card.name)

#Trying to print out the card number causes an error:
card2 = CreditCard("654321","Scrooge McDuck", 1000)
print(card2.name)
#print(card2.__number)


#testing the encapsulated balance attribute:
card3 = CreditCard("321654", "Bertha Filthy-Riches", 5000)
print(card3.retrieve_balance())
card3.deposit_money(100)
print(card3.retrieve_balance())
card3.withdraw_money(500)
print(card3.retrieve_balance())
# The following will not work because the balance is not sufficient
card3.withdraw_money(10000)
print(card3.retrieve_balance())