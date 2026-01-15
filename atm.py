class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"\nYour current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Invalid amount.")

# --- Program Logic ---
my_atm = ATM(1000)  # Starting balance of $1000

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        my_atm.check_balance()
    elif choice == '2':
        amt = float(input("Enter deposit amount: "))
        my_atm.deposit(amt)
    elif choice == '3':
        amt = float(input("Enter withdrawal amount: "))
        my_atm.withdraw(amt)
    elif choice == '4':
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")