class SavingsAccount:
    #Static variable (Class variable)
    general_rate = 0.03

    def __init__(self, account_number: str, balance: float, interest_rate: float):
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate

    def add_interest(self):
        # The total interest rate equals 
        # the general rate + the interest rate of the account
        total_interest = SavingsAccount.general_rate + self.__interest_rate
        self.__balance += self.__balance * total_interest

    @property
    def balance(self):
        return self.__balance

    @property
    #access to the total rate of the savings account from outside the SavingsAccountClass
    def total_interest(self):
        return self.__interest_rate + SavingsAccount.general_rate
    
if __name__ == "__main__":
    # Access to the class attribute through the name of the class
    print("General interest rate:", SavingsAccount.general_rate)

    peters_account = SavingsAccount("12345", 100, 0.03)
    annies_account = SavingsAccount("54321", 200, 0.06)

    print("General interest rate:", SavingsAccount.general_rate)
    print("Peter's account:", peters_account.total_interest)
    print("Annie's account:", annies_account.total_interest)
    print()
    # The general rate of interest is now 10 percent
    SavingsAccount.general_rate = 0.10

    print("General interest rate:", SavingsAccount.general_rate)
    print("Peter's account:", peters_account.total_interest)
    print("Annie's account:", annies_account.total_interest)