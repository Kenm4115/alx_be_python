
class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account with an optional initial balance.
        self.account_balance = initial_balance

    def deposit(self, amount):
        # Deposit a specified amount into the account.
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw a specified amount from the account if funds are sufficient.
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                print(f"Withdrew: ${amount:.1f}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        # Display the current account balance.
        print(f"Current Balance: ${self.account_balance:.2f}")


if __name__ == "__main__":
    # For testing the class directly
    account = BankAccount(100)  # Starting with a balance of $100
    account.display_balance()
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()


"""
Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

Task Description:
You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

bank_account.py:
Class Definition:

Define a class named BankAccount.
Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
Encapsulation and Behaviors:

Implement deposit(amount), withdraw(amount), and display_balance() methods.
deposit should add the specified amount to account_balance.
withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
display_balance should print the current balance in a user-friendly format.

Implementation Notes for you:
Ensure your BankAccount class in bank_account.py correctly implements the specified functionalities and adheres to the principles of encapsulation.
Use main.py to test your BankAccount class by performing various operations. Adjust the initial balance as needed for testing different scenarios.
This task combines learning OOP concepts with practical command line interaction, enhancing your understanding of Python programming.

"""
