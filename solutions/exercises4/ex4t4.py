#LunchCard
class LunchCard:
    def __init__(self, starting_balance):
        self.balance = starting_balance
        self.ordinary_price = 3.15
 
    def __str__(self):
        return f"The balance is {self.balance:.1f} euroa"
 
    def eat_ordinary(self):
        if self.balance >= self.ordinary_price:
            self.balance -= self.ordinary_price
 
    def eat_luxury(self):
        if self.balance >= 5.9:
            self.balance -= 5.9
 
    def deposit_funds(self, sum: float):
        if sum < 0:
            raise ValueError("You cannot deposit an amount of funds less than zero")
        self.balance += sum
 
# part1
print("Part 1")
card = LunchCard(50)
print(card)
print()

# part2
print("Part 2")
card.eat_ordinary()
print(card)
card.eat_luxury()
card.eat_ordinary()
print(card)
print()

# part3
print("Part 3")
card3 = LunchCard(10)
print(card3)
card3.deposit_funds(15)
print(card3)
card3.deposit_funds(10)
print(card3)
card3.deposit_funds(200)
print(card3)
print()

# part4
print("Part 4")
peters_card = LunchCard(20)
graces_card = LunchCard(30)
 
peters_card.eat_luxury()
graces_card.eat_ordinary()
 
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
 
peters_card.deposit_funds(20)
graces_card.eat_luxury()
 
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
 
peters_card.eat_ordinary()
peters_card.eat_ordinary()
graces_card.deposit_funds(50)
 
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")