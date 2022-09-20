class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print('Sorry, not enough funds!')

    def statement(self):
        print('Account Balance ${}'.format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s Current Account: Balance ${}".format(self.name, self.balance)
    

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
        
    def __str__(self):
        return "{}'s Savings Account: Balance ${}".format(self.name, self.balance)
    

c1 = Current('Jacquie', 500)
c1.deposit(300)
c1.statement()
c1.withdraw(1000)
c1.statement()
c1.withdraw(800)
c1.statement()
c1.withdraw(100)
c1.statement()
print(c1)
print()

c2 = Savings('Tom', 300)
c2.statement()
c2.withdraw(300)
c2.statement()
c2.withdraw(100)
c2.statement()
print(c2)
print()
