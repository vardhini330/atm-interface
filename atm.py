class Account:
    def __init__(self, acc_no, pin, balance=0):
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited.")
        else:
            print("Invalid amount.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print("Insufficient funds or invalid amount.")


class ATM:
    def __init__(self):
        self.accounts = {
            "1234": Account("1234", "0000", 1000)
        }

    def login(self):
        acc_no = input("Enter account number: ")
        pin = input("Enter PIN: ")
        account = self.accounts.get(acc_no)

        if account and account.pin == pin:
            print("Login successful!")
            self.menu(account)
        else:
            print("Login failed.")

    def menu(self, account):
        while True:
            print("\n1. Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Select option: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amt = float(input("Enter amount to deposit: ₹"))
                account.deposit(amt)
            elif choice == "3":
                amt = float(input("Enter amount to withdraw: ₹"))
                account.withdraw(amt)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


atm = ATM()
atm.login()