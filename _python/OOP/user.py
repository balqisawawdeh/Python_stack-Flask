class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance+=amount

    def make_withdrawal(self, amount):
        self.account_balance-=amount

    def display_user_balance(self):
        print(self.name,"/",self.account_balance)

user1 = User("Balqees",0)
user2 = User("Fatima",0)
user3 = User("Mai",0)

print("User 1:")
user1.make_deposit(100)
print(user1.account_balance)
user1.make_deposit(50)
print(user1.account_balance)
user1.make_deposit(150)
print(user1.account_balance)
user1.make_withdrawal(100)
print(user1.account_balance)

print("User 2:")
user2.make_deposit(50)
print(user2.account_balance)
user2.make_deposit(150)
print(user2.account_balance)
user2.make_withdrawal(100)
print(user2.account_balance)
user2.make_withdrawal(50)
print(user2.account_balance)

print("User 3:")
user3.make_deposit(1000)
print(user3.account_balance)
user3.make_withdrawal(50)
print(user3.account_balance)
user3.make_withdrawal(150)
print(user3.account_balance)
user3.make_withdrawal(150)
print(user3.account_balance)