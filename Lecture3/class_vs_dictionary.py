#class with only data attributes
class BankAccount:
    def __init__(self, account_number: str, 
                 owner: str, 
                 balance: float, 
                 annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest

peters_account = BankAccount("12345-678", "Peter Python", 1500.00, 0.015)

#bank account with dictionary
paulas_account = {"account_number": "23456-890", 
                  "owner": "Paula Cobra", 
                  "balance": 2000.00, 
                  "annual_interest": 0.014}

print(peters_account.owner, peters_account.balance)
print(paulas_account["owner"], paulas_account["balance"])