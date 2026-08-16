# ATM Banking System

account = {
    "name": "Maha",
    "pin": "1234",
    "balance": 10000,
    "transactions": []
}


def check_balance():
    print("\nCurrent Balance: ₹", account["balance"])


def deposit():
    amount = float(input("\nEnter deposit amount: ₹"))

    if amount > 0:
        account["balance"] += amount
        account["transactions"].append(
            f"Deposited ₹{amount}"
        )
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")


def withdraw():
    amount = float(input("\nEnter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid amount!")

    elif amount > account["balance"]:
        print("Insufficient balance!")

    else:
        account["balance"] -= amount
        account["transactions"].append(
            f"Withdrawn ₹{amount}"
        )
        print("Please collect your cash.")


def transfer():
    receiver = input("\nEnter receiver name: ")
    amount = float(input("Enter transfer amount: ₹"))

    if amount <= 0:
        print("Invalid amount!")

    elif amount > account["balance"]:
        print("Insufficient balance!")

    else:
        account["balance"] -= amount

        account["transactions"].append(
            f"Transferred ₹{amount} to {receiver}"
        )

        print("Money transferred successfully!")


def transaction_history():
    print("\n===== TRANSACTION HISTORY =====")

    if len(account["transactions"]) == 0:
        print("No transactions available.")

    else:
        for transaction in account["transactions"]:
            print("-", transaction)


def change_pin():
    old_pin = input("\nEnter current PIN: ")

    if old_pin == account["pin"]:

        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")

        if new_pin == confirm_pin:
            account["pin"] = new_pin
            print("PIN changed successfully!")
        else:
            print("PINs do not match!")

    else:
        print("Incorrect current PIN!")


# ================= LOGIN =================

print("===== WELCOME TO ATM =====")

attempts = 3

while attempts > 0:

    pin = input("Enter your 4-digit PIN: ")

    if pin == account["pin"]:
        print("\nLogin successful!")
        print("Welcome", account["name"])

        break

    else:
        attempts -= 1
        print("Incorrect PIN!")
        print("Attempts remaining:", attempts)

else:
    print("Your account is locked!")
    exit()


# ================= ATM MENU =================

while True:

    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Transaction History")
    print("6. Change PIN")
    print("7. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        transfer()

    elif choice == "5":
        transaction_history()

    elif choice == "6":
        change_pin()

    elif choice == "7":
        print("\nThank you for using our ATM!")
        break

    else:
        print("Invalid choice!")