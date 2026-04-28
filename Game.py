# ATM Simulation Project

balance = 1000
transactions = []

def show_balance():
    print("Your current balance is:", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    transactions.append(f"Deposited: {amount}")
    print("Amount deposited successfully!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        transactions.append(f"Withdrawn: {amount}")
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")

def statement():
    print("\nTransaction Statement:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        statement()
    elif choice == "5":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice! Try again.")
        