class BankAccount:
    def __init__(self,name,int_rate,balance=0):
        self.name = name 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        self.balance-=amount
        if self.balance<0:
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print("account balance is: ",self.balance,"$")
        return self

    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        return self
		
user1 = BankAccount("Balqees",0.07)
user2 = BankAccount("Fatima",0.07)
user3 = BankAccount("Mai",0.07)

print("User 1:")
user1.deposit(1000).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()
print(user1.balance)

print("User 2:")
user2.deposit(1000).deposit(200).withdraw(300).withdraw(50).withdraw(100).withdraw(100).yield_interest().display_account_info()
print(user2.balance)

print("User 3:")
user3.deposit(1000).deposit(200).withdraw(300).withdraw(50).withdraw(100).withdraw(100).yield_interest().display_account_info()
print(user3.balance)
