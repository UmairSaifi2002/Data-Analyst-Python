# we will 

class BankCustomer:
    def __init__(self, name, account_no, balance, password):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.password = password

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Account No: {self.account_no}")
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def change_password(self, new_password):
        self.password = new_password
        print("Password changed successfully.")

# Example usage:
if __name__ == "__main__":
    customer = BankCustomer("Alice", "123456", 1000, "pass123")
    customer.show_details()
    customer.deposit(500)
    customer.withdraw(200)
    customer.change_password("newpass456")