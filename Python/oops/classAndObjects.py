# Great, Umair! Let's begin your deep dive into **Object-Oriented Programming (OOP) in Python** like you're sitting in a computer lab and I'm your teacher.

## 🔰 **What is OOP (Object-Oriented Programming)?**

# OOP is a programming paradigm that organizes code using **objects**—these are real-world entities like a car, person, or bank account. OOP helps you **write clean, reusable, modular, and organized code**.

## 🧱 Four Pillars of OOP (The Foundation)

# We'll start here and go in-depth into each:

# 1. **Class** and **Object** 🧍‍♂️ 
# 2. **Encapsulation** 📦 
# 3. **Inheritance** 🧬 
# 4. **Polymorphism** 🎭 
# 5. **Abstraction** 🔒 (added in advanced OOP) 

## 🔹 1. CLASS and OBJECT

### 📌 Think like this:

# * **Class**: Blueprint (Design)
# * **Object**: Real-world instance of that blueprint

### ✅ Real-world example:


class Car:  # Class
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

# Creating object
my_car = Car("Toyota", "Red")  # Object
my_car.drive()


### 🔍 Explanation:

# * `class Car`: Defines the blueprint.
# * `__init__`: Constructor used to initialize object.
# * `self`: Refers to the current object.
# * `my_car`: Object created from the `Car` class.

## 🎯 **Lab Activity for Today**:


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")

# Create 2 students
s1 = Student("Umair", "A")
s2 = Student("Ali", "B")
s1.display()
s2.display()

## 🧪 Your Homework / Practice:

# 1. Create a class called `Mobile` with attributes: `brand`, `price`.
# 2. Create a method called `show_info()` to display mobile details.
# 3. Create 2 mobile objects and call the method.

# Task
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def show_info(self):
        print(f'The price of {self.brand} mobile is {self.price}.')

mobile = Mobile('Samsung', 50000)

mobile.show_info()

# ----------------- Now we will done with the basic part and now we will learn some cool stuff about classes and objects ------------------------

# Class variables and instance variable

class student:
    school = "ABC High School"  # Class variable
    def __init__(self, name, age):
        self.name = name # Instance variable
        self.age = age # Instance variable
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
    @staticmethod
    def school_info():
        print('This is a high school.')
    # string representation of the object
    def __str__(self):
        return f'Student Name: {self.name}, Age: {self.age}, School: {self.school}'

# class variable is same for all of the instances from the same class
# instance variable means each instance have the different value for the same variable
st1 = student('Umair', 16)
st2 = student('Ali', 17)
print(st1)
st2.change_school('XYZ High School')  # Change class variable
# now we change the class vaiable for all of the instances
print(st2)

print(f'{st1.name} is {st1.age} years old and studies in {st1.school}.')
print(f'{st2.name} is {st2.age} years old and studies in {st2.school}.')
