class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful")

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"


#використання класу BankAccount
account1 = BankAccount("1234567890", 1000)
print(account1)  # Виводить: Account Number: 1234567890, Balance: 1000

account1.withdraw(500)  # Виводить: Withdrawal of 500 successful
print(account1)  # Виводить: Account Number: 1234567890, Balance: 500

account1.deposit(200)  # Виводить: Deposit of 200 successful
print(account1)  # Виводить: Account Number: 1234567890, Balance: 700
