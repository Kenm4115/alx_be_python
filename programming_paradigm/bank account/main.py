
from robust_division_calculator import safe_divide
import sys
from bank_account import BankAccount


def main():
    account = BankAccount()  # Start with a default balance of $0

    # Command line argument handling
    if len(sys.argv) < 2:
        print("Usage: main-0.py <operation> [amount]")
        print("Operations: deposit, withdraw, balance")
        return

    operation = sys.argv[1].lower()

    if operation == "deposit":
        if len(sys.argv) != 3:
            print("Usage: main-0.py deposit <amount>")
            return
        try:
            amount = float(sys.argv[2])
            account.deposit(amount)
        except ValueError:
            print("Please enter a valid amount.")

    elif operation == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: main-0.py withdraw <amount>")
            return
        try:
            amount = float(sys.argv[2])
            account.withdraw(amount)
        except ValueError:
            print("Please enter a valid amount.")

    elif operation == "balance":
        account.display_balance()

    else:
        print("Unknown operation. Use: deposit, withdraw, or balance.")


if __name__ == "__main__":
    main()
