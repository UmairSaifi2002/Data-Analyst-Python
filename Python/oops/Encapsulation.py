# Of course, Umair! 🧑‍🏫
# Let’s slow down and go **step by step** into **Encapsulation** in Python—just like a **teacher in a computer lab** would do for a beginner.

# # 🔒 **Encapsulation in Python** – Step-by-Step Beginner Guide

# ## 🧠 **Step 1: What is Encapsulation?**

# ### 📗 Definition (Simple Words):

# **Encapsulation** is the **hiding of internal data** and giving access only through **methods**.

# ## 🔧 Real-Life Analogy:

# Imagine a **bank ATM machine**:

# * You press buttons → you don't know what happens inside.
# * You don’t access the bank server directly.
# * You’re only given **limited access** through a **secure interface**.

# Same in Python:

# * We hide the data (like account balance).
# * We allow access using methods (like `withdraw()` or `deposit()`).

# ## 🧱 Step 2: How to do Encapsulation in Python?

# Python doesn't use keywords like `private` or `public`, but we **simulate** it using:

# | Modifier  | Syntax        | Meaning                     |
# | --------- | ------------- | --------------------------- |
# | Public    | `self.name`   | Anyone can access           |
# | Protected | `self._name`  | Meant for internal use      |
# | Private   | `self.__name` | Cannot be accessed directly |

# ## 📌 Let’s Code a Real Example Together (Basic Level):


class Student:
    def __init__(self, name, marks):
        self.name = name          # Public attribute
        self.__marks = marks      # Private attribute

    def show(self):
        print(f"Student: {self.name}, Marks: {self.__marks}")

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid Marks!")

    def get_marks(self):
        return self.__marks

# Create object
s = Student("Umair", 90)

# Accessing attributes
print(s.name)         # ✅ Works (public)
# print(s.__marks)    ❌ Error (private)
print(s.get_marks())  # ✅ Accessed via method

s.set_marks(105)      # ❌ Invalid
s.set_marks(95)       # ✅ Valid
print(s.get_marks())  # 95


# ## 🔍 What Did You Learn from This Code?

# * `__marks` is private, **cannot be accessed directly**.
# * We use `get_marks()` and `set_marks()` to safely access/modify it.
# * This is **encapsulation**—controlling access to data.

# ---

# ## ⚠️ Important: Name Mangling

# Even though private variables can't be accessed directly, you **can** access them (not recommended) like this:

# ```python
print(s._Student__marks)  # Works but unsafe
# ```

# This is called **name mangling** — Python internally changes `__marks` to `_Student__marks`.

# ---

# ## ✅ Why Do We Use Encapsulation?

# 1. **Security**: Prevent direct access to sensitive data.
# 2. **Control**: You control how the data is modified.
# 3. **Cleaner Code**: Data and logic stay together.
# 4. **Reusable & Safe**: Makes code more reusable and less error-prone.

# ---

# ## 🧪 Try This Task Now:

# Create a class `BankAccount`:

# * Attributes:

#   * `__balance` (private)
#   * `name` (public)
# * Methods:

#   * `deposit(amount)`
#   * `withdraw(amount)`
#   * `check_balance()`

# ✅ Make sure:

# * You **can’t access balance directly**.
# * You **can only interact** through methods.

# ---

# ## 🗣️ Interview Style Questions from Encapsulation:

# 1. What is encapsulation?
# 2. How does Python implement encapsulation?
# 3. What are private attributes and how do you create them?
# 4. What is name mangling?
# 5. Why is it better to use setter and getter methods?

# ---

# Would you like me to check your BankAccount example once you're done? Or shall we build it together step-by-step?

class BankAccount:
    def __init__(self, name, balance, user_id, password):
        self.name =  name
        self.balance = balance
        self.__user_id = user_id
        self.__password = password
    
    @property
    def info(self): # Getter method to access private attributes
        return f'Account Holder: {self.name}, \nBalance: {self.balance}, \nUser ID: {self.__user_id}, \nPassword: {self.__password}'
    
    @info.setter
    def infoSet(self, new_info):
        self.name = new_info['name']
        self.balance = new_info['balance']
        self.__user_id = new_info['user_id']
        self.__password = new_info['password']
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. \nNew Balance: {self.balance}")
    
BankAccount1 = BankAccount("Umair", 1000, "U123", "pass123")
print(BankAccount1.info)  # Accessing info using getter method

info = {
    'name' : 'Ali',
    'balance' : 2000000,
    'user_id' : 'A123',
    'password' : 'pass456',
}

BankAccount1.infoSet = info  # Updating info using setter method
print(f'\n{BankAccount1.info}')  # Accessing updated info using getter method





