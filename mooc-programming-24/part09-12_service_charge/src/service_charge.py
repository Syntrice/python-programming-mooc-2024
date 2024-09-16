# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, owner: str, account_no: str, balance: float) -> None:
        self.__owner = owner
        self.__acount_no = account_no
        self.__balance = balance
    
    def deposit(self, amount: float) -> None:
        self.__balance += amount
        self.__service_charge()

    
    def withdraw(self, amount: float) -> None:
        self.__balance -= amount
        self.__service_charge()
    
    def __service_charge(self) -> None:
        self.__balance *= 0.99
    
    @property
    def balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
