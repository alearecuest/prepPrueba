'''
**Exercise 3: Encapsulation**
1. Create a class BankAccount with:
   - Private attributes: __balance
   - Methods:
     - deposit(amount) (add to the balance)
     - withdraw(amount) (subtract from the balance if sufficient funds are available)
     - get_balance() (return the current balance)
2. Test the class by creating an account, performing deposits and withdrawals, and accessing the balance.
'''

class BankAccount():
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds")
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1500)

account.deposit(400)
print(account.get_balance())