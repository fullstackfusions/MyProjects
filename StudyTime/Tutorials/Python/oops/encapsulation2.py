class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number  # Non-public attribute
        self._balance = balance                # Non-public attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}; New Balance: {self._balance}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}; New Balance: {self._balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance

# Create a bank account
account = BankAccount("12345678", 1000)

# Deposit and withdraw
account.deposit(500)
account.withdraw(200)

# Accessing balance (not directly accessing the attribute)
print("Account Balance:", account.get_balance())