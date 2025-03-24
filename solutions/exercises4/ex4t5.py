class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def load_funds(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class PaymentTerminal:
    def __init__(self):
        # The register initially has 1000 euros
        self.funds = 1000
        self.ordinaries = 0
        self.luxuries = 0

    def eat_ordinary(self, payment: float):
        # An affordable meal costs 2.95 euros
        # Increase the register's funds by the price of the affordable meal and return the change
        # If the given payment is not sufficient, the meal is not sold and the method returns the full amount
        if payment >= 2.95:
            self.funds += 2.95
            payment -= 2.95
            self.ordinaries += 1
        return payment

    def eat_luxury(self, payment: float):
        # A delicious meal costs 5.90 euros
        # Increase the register's funds by the price of the delicious meal and return the change
        # If the given payment is not sufficient, the meal is not sold and the method returns the full amount
        if payment >= 5.90:
            self.funds += 5.90
            payment -= 5.90
            self.luxuries += 1

        # Return either the remaining or the original funds
        return payment

    def eat_ordinary_lunchcard(self, card: LunchCard):
        # An affordable meal costs 2.95 euros
        # If the card has enough funds, deduct the price from the card and return True
        # Otherwise, return False
        if card.subtract_from_balance(2.95):
            self.ordinaries += 1
            return True
        else:
            return False

    def eat_luxury_lunchcard(self, card: LunchCard):
        # A delicious meal costs 5.90 euros
        # If the card has enough funds, deduct the price from the card and return True
        # Otherwise, return False
        if card.subtract_from_balance(5.90):
            self.luxuries += 1
            return True
        else:
            return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.load_funds(amount)
        self.funds += amount
        

if __name__ == "__main__":
    #Part1
    """card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)"""

    #Part2
    """exactum = PaymentTerminal()

    change = exactum.eat_ordinary(10)
    print("The change returned was", change)

    change = exactum.eat_ordinary(5.9)
    print("The change returned was", change)

    change = exactum.eat_luxury(5.9)
    print("The change returned was", change)

    print(f"Funds available at the terminal: {exactum.funds:.2f}")
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries)"""

    #Part 3
    """exactum = PaymentTerminal()

    change = exactum.eat_ordinary(10)
    print("The change returned was", change)

    card = LunchCard(9)

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_ordinary_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries)"""

    #Part4
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries)