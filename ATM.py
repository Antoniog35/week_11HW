class ATM:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")

    def show_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

# --- Program Execution ---
atm = ATM()

while True:
    atm.show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please try again.")
