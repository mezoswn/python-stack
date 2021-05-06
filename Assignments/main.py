#done by mohammad raddad & Moath
class BankAccount:
    def __init__(self,name,int_rate,balance):
        self.balance=balance
        self.int_rate=int_rate
        self.balance=0
        self.name=name

    def deposite(self,amount):
        self.balance+=amount
        return self

    def withdrwal(self,amount):
        self.balance-=amount
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate + self.balance
            return self

    def display_account_info(self):
        print(f"name: {self.name}, Balance : $ {self.balance} , int_rate: {self.int_rate}")
        return self






u1 =BankAccount("moath",5, 0)
u2 =BankAccount("mohammad",10,300)

u1.deposite(100).deposite(300).deposite(500).withdrwal(200).display_account_info()




u2.deposite(400).deposite(4000).withdrwal(200).withdrwal(200).withdrwal(200).withdrwal(200).yield_interest().display_account_info()







