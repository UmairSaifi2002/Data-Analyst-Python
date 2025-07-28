# Great, Mohammad Umair! 👨‍🏫 Let's continue with the **fourth pillar of OOP in Python: `Polymorphism`**.

# ---

# ## 🧠 What is Polymorphism?

# **Polymorphism** means **"many forms."**
# In OOP, **polymorphism allows objects of different classes to be treated as objects of a common superclass**.

# ---

# ### ✅ Simple Example to Understand:

# Let’s take an example of a `Bird` class:

# ```python
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")
# ```

# Now two child classes:

# ```python
class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
# ```

# Now, let’s use polymorphism:

# ```python
bird1 = Bird()
bird2 = Sparrow()
bird3 = Ostrich()

for bird in (bird1, bird2, bird3):
    bird.intro()
    bird.flight()
# ```

# ✅ **Each object behaves differently depending on the class it's created from.**

# ---

# ## 🔍 Key Concepts of Polymorphism:

# ### 1. **Duck Typing** (Python-specific)

# "If it walks like a duck and quacks like a duck, it must be a duck."

# Example:

# ```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_speak(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_speak(dog)  # Woof!
animal_speak(cat)  # Meow!
# ```

# Python doesn't care what class `dog` or `cat` belong to—it just cares that they have a `.speak()` method.

# ---

# ### 2. **Method Overriding** (Already Covered)

# Child class overrides a method from the parent class.

# ### 3. **Function Polymorphism** (Built-in)

# ```python
print(len("Umair"))      # 5
print(len([1, 2, 3]))     # 3
print(len({'a': 1}))      # 1
# ```

# ✅ The `len()` function behaves differently for string, list, and dictionary.

# ---

# ### 4. **Polymorphism with Class Methods**

# ```python
class Car:
    def fuel_type(self):
        print("Petrol or Diesel")

class ElectricCar:
    def fuel_type(self):
        print("Battery")

def show_fuel(car):
    car.fuel_type()

c1 = Car()
c2 = ElectricCar()

show_fuel(c1)  # Petrol or Diesel
show_fuel(c2)  # Battery
# ```

# ---

# ## 🧪 Real-World Example:

# Imagine a **payment system**:

# ```python
class CreditCard:
    def pay(self):
        print("Paid using Credit Card")

class PayPal:
    def pay(self):
        print("Paid using PayPal")

class Cash:
    def pay(self):
        print("Paid using Cash")
# ```

# A function that uses polymorphism:

# ```python
def checkout(payment_method):
    payment_method.pay()

checkout(CreditCard())
checkout(PayPal())
checkout(Cash())
# ```

# ---

# ## 🧠 Summary:

# | Concept               | Meaning                                      |
# | --------------------- | -------------------------------------------- |
# | Polymorphism          | Many forms - same method, different behavior |
# | Duck Typing           | Python relies on behavior, not class         |
# | Method Overriding     | Redefine parent class method in child        |
# | Function Polymorphism | Same function works with different types     |

# ---

# Would you like to:

# * Practice some **polymorphism questions**?
# * Or jump to a **recap of all four pillars**?
# * Or go into **advanced OOP features** like `abstract classes`, `interfaces` (via ABC module), etc.?

# Let me know how you'd like to continue!
