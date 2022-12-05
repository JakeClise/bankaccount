#FIRST CREATE THE CLASS

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        
        return self


    def withdraw(self, amount):
        
        self.balance = self.balance - amount 

        if amount > self.balance:
            print("Insuficient Balance!!")
        
        if amount <= self.balance:
            print(self.balance)
        
        return self

    def display_account_info(self):
        print(f"The balance on this account is {self.balance}")

        return self
    
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        print(f"The balance of this account with interest is: {self.balance}")

        return self

#CREATE TWO ACCOUNTS
loganAccount = BankAccount(.05, 5000)
romanAccount = BankAccount(.03, 10000)

#IN FIRST ACCOUNT MAKE (3 DEPOSITS, 1 WITHDRAWAL, THEN YIELD INTEREST)
loganAccount.deposit(900).deposit(100).deposit(600).withdraw(250).yield_interest().display_account_info()

#IN THE SECOND ACCOUNT MAKE (2 DEPOSITS, 4 WITHDRAWLS, YIELD INTEREST, AND DISPLAY INFO)
romanAccount.deposit(40).deposit(900).withdraw(90).withdraw(110).withdraw(80).withdraw(400).yield_interest().display_account_info()



