class Account:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self,deposit):
        self.deposite = deposit
        self.balance = deposit.__add__(self.balance)
        return "Deposit Accepted"

    def withdraw(self,withdraw):
        self.withdraw = withdraw
        if self.balance > self.withdraw:
            self.balance = self.balance.__sub__(self.withdraw)
            return "Withdrawal Accepted"
        else:
            return "Funds Unavailable!"

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.balance)
print(acct1.withdraw(100))
