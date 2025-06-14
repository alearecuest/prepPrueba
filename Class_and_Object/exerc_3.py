#!/usr/bin/python3
'''### **Exercise 3: Encapsulation**
1. Create a class BankAccount with:
   - Private attributes: __balance
   - Methods:
     - deposit(amount) (add to the balance)
     - withdraw(amount) (subtract from the balance if sufficient funds are available)
     - get_balance() (return the current balance)
2. Test the class by creating an account, performing deposits and withdrawals, and accessing the balance.
'''


class BankAccount():
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited U$S {amount}. New balance: U$S {self.__balance}")
        else:
            print("Deposit must be positive")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdraw U$S {amount}. New balance: U$S {self.__balance}")
            else:
                print(f"Insufficient founds. Current balance: U$S {self.__balance}")
        else:
            print("Withdraw amount must be positive")
    
    def get_balance(self):
        balance = self.__balance
        return balance

account = BankAccount()
account.deposit(356)
account.withdraw(139)
print(f"Your balance is: U$S {account.get_balance()}")
