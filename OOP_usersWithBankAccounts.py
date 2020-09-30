#Created by Shelley Ophir
#Coding Dojo Sep. 30, 2020
# Practice writing classes with associations
# Update your existing User class to have an association with the BankAccount class. You should not have to change anything in the BankAccount class. The method signatures of the User class (the first line of the method with the def keyword) should also remain the same.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accountCheck = BankAccount()
        self.accountSav = BankAccount()

    def make_deposits(self, amount, account):
        if (account == "savings"):
            self.accountSav.deposit(amount)

        else if (account == "checking"):
            self.accountCheck.deposit(amount)
    
    # make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawl(self, amount, account):
        if (account == "savings"):
            self.accountSav.withdrawl(amount)

        else if (account == "checking"):
            self.accountCheck.withdrawl(amount)

    # display_user_balance(self) - have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print("User:", self.name, "\nChecking Balance:", self.accountCheck.balance)
        print("User:", self.name, "\nSavings Balance:", self.accountSav.balance)

    # BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount, account):
        if (account == "savings"):
            self.accountSav.withdrawl(amount)
        else if (account == "checking"):
            self.accountCheck.withdrawl(amount)
            
        other_user.make_deposits(amount)

    # SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

class BankAccount:
    def __init__(self, amount = 0, rate = 0.01):
        self.balance = amount

    # The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)
        self.rate = rate

    # The class should also have the following methods:
    # deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount

        return self

    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdrawl(self, amount):
        if (self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        
        return self

    # display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print("Balance:", self.balance)

    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if (self.balance > 0):
            self.balance = format(self.balance * (1 + self.rate), ".2f")
            #round to 2 decimal places
        
        return self

