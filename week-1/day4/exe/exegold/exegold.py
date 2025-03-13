class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.authenticated = False
        self.balance = balance
    
    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
        else:
            raise Exception("Authentication failed.")
    
    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to perform this action.")
        if amount <= 0:
            raise Exception("Deposit must be a positive value.")
        self.balance += amount
    
    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to perform this action.")
        if amount <= 0:
            raise Exception("Withdrawal must be a positive value.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Withdrawal must be a positive value.")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw: balance will fall below minimum balance.")
        self.balance -= amount

class ATM:
    def __init__(self, account_list, try_limit=2):
        if not all(isinstance(account, (BankAccount, MinimumBalanceAccount)) for account in account_list):
            raise Exception("All accounts must be instances of BankAccount or MinimumBalanceAccount.")
        if try_limit <= 0:
            raise Exception("Try limit must be a positive number.")
        
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
    
    def show_main_menu(self):
        while True:
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Exiting the ATM system.")
                break
    
    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                self.show_account_menu(account)
                return
            except Exception:
                pass
        
        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            print(f"Max attempts reached. Shutting down.")
            return
        else:
            print("Incorrect credentials. Try again.")
    
    def show_account_menu(self, account):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                try:
                    account.deposit(amount)
                    print(f"Deposit successful. New balance: {account.balance}")
                except Exception as e:
                    print(e)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                try:
                    account.withdraw(amount)
                    print(f"Withdrawal successful. New balance: {account.balance}")
                except Exception as e:
                    print(e)
            elif choice == "3":
                print("Logging out.")
                break
 
account1 = BankAccount("user1", "pass1", 1000)
account2 = MinimumBalanceAccount("user2", "pass2", 2000, minimum_balance=500)
 
atm = ATM([account1, account2])
 
atm.show_main_menu()
