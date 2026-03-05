class Account:

    # 1. Constructor
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    # 2. Deposit Method
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None

        if amountToDeposit < 0:
            print("You cannot deposit a negative amount")
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    # 3. Withdraw Method
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Incorrect password for this account")
            return None

        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None

        if amountToWithdraw > self.balance:
            print("You cannot withdraw more than you have in your account")
            return None

        self.balance = self.balance - amountToWithdraw
        return self.balance

    # 4. Check Balance
    def getBalance(self, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        return self.balance

    # 5. Show Account Details (for debugging)
    def show(self):
        print("Name:", self.name)
        print("Balance:", self.balance)
        print("Password:", self.password)
        print()
        
oAccount = Account('Joe Schmoe', 1000, 'magic')
newBalance = oAccount.deposit(500, 'magic')
oAccount.withdraw(250, 'magic')
currentBalance = oAccount.getBalance('magic')


print(oAccount.show())
