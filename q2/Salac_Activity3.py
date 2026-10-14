class BankAccount:
    def __init__(self, account_number:int, balance:float):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return f"{self.__balance:.1f}"

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = new_account_number

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("[Warning] The balance must not be a negative number.")

a1 = BankAccount(12345, 1000)
print("Account 1")
print("Account Number:", a1.account_number)
print("Balance:", a1.balance)

a1.balance = -100
print("Account Number:", 12345)
print("Balance:", a1.balance)
    