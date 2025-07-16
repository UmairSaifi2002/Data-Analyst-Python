import re

# Write a program to validate an email address and a password

email = input("Enter your email address: ")
password = input("Enter your password: ")

# function to validate email
def validate_email(email):
    if '@' in email and '.' in email:
        return True
    return False

# function to validate password
def validate_password(password):
    b = False
    for char in password:
        if len(password) >= 8:
            b = True
            break
        if char.isdigit():
            b = True
            break
        if char.isalpha():
            b = True
            break
        if char in ['!', '@', '#', '$', '%', '^', '&', '*']:
            b = True
            break
    return b

# another way to know the strength of password
def is_strong_password(password):
    c1 = bool(re.search(r'[A-Z]', password))  # At least one uppercase letter
    c2 = bool(re.search(r'[a-z]', password))  # At least one lowercase letter
    c3 = bool(re.search(r'[0-9]', password))  # At least one digit
    c4 = bool(re.search(r'[!@#$%^&*]', password))  # At least one special character
    if c1 and c2 and c3 and c4 and len(password) >= 8:
        return "Strong password"
    return "Weak password"

# Validate email and password
if validate_email(email) and validate_password(password):
    print("Email and password are valid.")
else:
    print("Invalid email or password. Please try again.")

