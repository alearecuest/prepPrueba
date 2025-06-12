#!/usr/bin/python3
'''
### **Exercise 5: Abstraction with Abstract Classes**

1. Import `ABC` and `abstractmethod` from the `abc` module.
2. Create an abstract class `Payment` with an abstract method `process_payment()`.
3. Implement subclasses `CreditCardPayment` and `PayPalPayment`, each providing their own implementation of `process_payment()`.
4. Demonstrate polymorphism by processing payments using both subclasses.
'''


from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod

    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number, expiry_date, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self):
        masked_card = f"****-****-****-{self.card_number[-4:]}"
        return f"Processing $ {self.amount:.2f} payment via Credit Card {masked_card}"

class PayPalPayment(Payment):

    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process_payment(self):
        return f"Processing $ {self.amount:.2f} payment via PayPal account: {self.email}"

def process_customer_payment(payment):
    print(payment.process_payment())
    print("Payment successful!")
