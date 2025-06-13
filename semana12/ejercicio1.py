# 1. Cree una clase de `BankAccount` que:
#     1. Tenga un atributo de `balance`.
#     2. Tenga un método para ingresar dinero.
#     3. Tengo un método para retirar dinero.
    
#     Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
#     1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#     2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede debajo del `min_balance`. Es decir que sí se pueden hacer retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.


class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
        print("The start balance is: ",balance)
    
    
    def savemoney(self,amount):
        amount=int(amount)
        print("You want to save: ", amount)
        self.balance=self.balance+amount
        print("Your new balance is: ",self.balance)
    

    def takemoney(self,amount):
        amount=int(amount)
        print("You want to take: ", amount)
        if self.balance > amount:
            self.balance=self.balance-amount
            print("Your new balance is: ",self.balance)
        else:
            print("You current balance isn't sufficient to cover the withdraw")


   
#     Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
#     1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#     2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede debajo del `min_balance`. Es decir que sí se pueden hacer retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.

account1=BankAccount(100)
account1.savemoney(100)
account1.takemoney(300)

class SavingsAccount(BankAccount):
    def __init__(self, balance=500, min_balance=200):
        self.balance=balance
        self.min_balance=min_balance
        print("This account has a balance of: ", balance)
        print("And a minimum balance of: ", min_balance)
    
    def savemoney(self,amount):
        amount=int(amount)
        print("You want to save:", amount)
        self.balance=self.balance+amount
        print("Your new balance is: ",self.balance)    
    
    def take_money(self, amount):
        amount=int(amount)
        if (self.balance - amount)<self.min_balance:
            print("You cannot take this amount as you'd be leaving the account with less than the minimum balance")
        else:
            self.balance=self.balance-amount
            print('Your new balance is: ',self.balance)            

account2=SavingsAccount()
account2.savemoney(3500)
account2.takemoney(300)

