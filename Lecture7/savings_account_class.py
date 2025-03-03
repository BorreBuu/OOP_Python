class SavingsAccount:
    def __init__(self, account_number: str, balance: float, interest_rate: float):
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate
    
        
if __name__ == "__main__":
    """
    account = SavingsAccount("12345", 1000, 0.05)
    # Add the total interest accrued to the balance on the account
    account.add_interest()
    print(account.balance)

    peters_account = SavingsAccount("12345", 100, 0.03)
    annies_account = SavingsAccount("54321", 200, 0.06)

    print("Peter's account:", peters_account.balance)
    print("Annie's account:", annies_account.balance)

    print("The general interest rate is", SavingsAccount.general_rate)

    ulrikas_account = SavingsAccount("67854", 300, 0.02)
    ulrikas_account.add_interest()
    print("Ulrika's account", ulrikas_account.balance)"""