import sys
class Customer:
    """this is the bank our crypto lovers"""
    bankname='MONEYBANK'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
        print("balance after deposit",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("insufficient funds")
            sys.exit()
        self.balance-=amt
        print("balance after withdrawl",self.balance)
print("welcome to the ",Customer.bankname)
name=input("enter the name: ")
c=Customer(name)
while True:
    print('d-Deposit \nw-withdrawl \ne-exit')
    option=input("choose the option")
    if option=="d" or option=="D":
        amt=float(input("enter the amount"))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input("enter the amount: "))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("thanks for coming")
        sys.exit()
    else:
        print("invalid option.. please choose the right option")
