### Done with Moath and Dara 

class User:     # declare a class and give it name User
    def __init__(self, name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        if amount < self.account_balance:
            self.account_balance = self.account_balance - amount
        else:    # added
            print ("Check your Amount!")
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def  transfer_money(self, other_user, amount):
        if amount < self.account_balance:
            self.account_balance = self.account_balance - amount
            other_user.account_balance = other_user.account_balance + amount
        else:   # added
            print ("Check your Amount!")

Khalil = User('Khalil', '@axsos')
Dara = User('Dara', '@axsos')
Moath = User('Moathh', '@axsos')

Khalil.make_deposit(10)
Khalil.make_deposit(20)
Khalil.make_deposit(30)
Khalil.make_withdrawal(15)
Khalil.display_user_balance()

Dara.make_deposit(10)
Dara.make_deposit(20)
Dara.make_withdrawal(5)
Dara.make_withdrawal(10)
Dara.display_user_balance()

Moath.make_deposit(500)
Moath.make_withdrawal(100)
Moath.make_withdrawal(50)
Moath.make_withdrawal(20)
Moath.display_user_balance()

Khalil.transfer_money(Moath, 30)
Khalil.display_user_balance()
Moath.display_user_balance()

Moath.make_withdrawal(10000)
Khalil.transfer_money(Moath, 3000)
