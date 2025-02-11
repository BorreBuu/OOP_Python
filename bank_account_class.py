class BankAccount:
    #constructor
    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest

    # This method adds the annual interest to the balance of the account
    def add_interest(self):
        self.balance += self.balance * self.annual_interest


#paula's and peter's interest rate is different, the result of adding the interest is different
peters_account = BankAccount("12345-678", "Peter Python", 2000.0, 0.015)
print(peters_account.balance)
paulas_account = BankAccount("23456-890", "Paula Cobra", 2000.00, 0.014)
paulas_account.add_interest()
print(paulas_account.balance)
#annual interest is added only to those accounts which the methdod is called on.
pippas_account = BankAccount("1111-222", "Pippa Programmer", 1500.0, 0.001)
print(pippas_account.balance)