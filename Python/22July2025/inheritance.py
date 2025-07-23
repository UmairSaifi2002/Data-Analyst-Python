# Simple class for arithmetic operations
class calc:
    # Adds two numbers
    def add(self, x, y):
        print("Addition:", x + y)
    # Subtracts two numbers
    def sub(self, x, y):
        print("Subtraction:", x - y)

# Class for operations on lists
class calculator:
    # Adds all elements in list x, sums all elements in list y, and prints their total
    def add(self, x, y):
        s1 = 0
        for i in x:
            s1 += i  # Sum elements of list x
        print("Addition:", s1)
        s2 = sum(y)  # Sum elements of list y
        print("Addition:", s2)
        print('x+y', s1 + s2)  # Print total sum of both lists

# Child class inheriting from calculator and calc
class UserDemo(calculator, calc):
    # Uses inherited add method to perform operations
    def perform_operations(self):
        list1 = [10, 20, 30]  # First list
        list2 = [5, 15, 25]   # Second list
        self.add(list1, list2)  # Calls add method from calculator (due to MRO)

obj = UserDemo()
obj.perform_operations()

#What is MRO?
# MRO (Method Resolution Order) is the order in which Python looks for a method in a hierarchy of classes.
# When you call a method on an object, Python checks the classes from left to right as listed in the inheritance.
# In your code, UserDemo(calculator, calc) means Python will look for methods in UserDemo, then calculator, then calc.

# So, when you call self.add(list1, list2) in UserDemo, Python uses the add method from calculator (not from calc), because calculator comes first in the inheritance list.

print(UserDemo.__mro__)
print(UserDemo.__dict__)
print(UserDemo.__module__)

# Hybrid inheritance
# Method Ovveridding
# Interfaces
