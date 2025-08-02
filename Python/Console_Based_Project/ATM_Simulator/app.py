# ATM Data (Card Number → PIN + Balance)
user_data = {
    "123456": {"pin": 1234, "balance": 5000},
    "654321": {"pin": 4321, "balance": 7000},
    "112233": {"pin": 1111, "balance": 6000},
    "998877": {"pin": 9999, "balance": 8000},
    "445566": {"pin": 2244, "balance": 3000}
}

# ✅ Login Function
def login(card_number, pin):
    if card_number in user_data and user_data[card_number]['pin'] == pin:
        print('✅ Login successful')
        return True
    else:
        print('❌ Incorrect PIN. Try again.')
        return False

# ✅ Show Menu Function with Exit Logic
def show_menu(cardNumber):
    while True:
        print('\n------ ATM MENU ------')
        print('1. Check Balance')
        print('2. Withdraw')
        print('3. Deposit')
        print('4. Exit')
        print('----------------------')
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            check_balance(cardNumber)
        elif choice == '2':
            withdraw(cardNumber)
        elif choice == '3':
            deposit(cardNumber)
        elif choice == '4':
            print("👋 Thank you for using our ATM. Have a nice day!")
            break
        else:
            print('⚠️ Invalid choice. Please try again.')

# ✅ Check Balance
def check_balance(cardNumber):
    print(f"💰 Your current balance is: ₹{user_data[cardNumber]['balance']}")

# ✅ Withdraw
def withdraw(cardNumber):
    amount = input('Enter the amount you want to withdraw: ')
    if amount.isdigit():
        amount = int(amount)
        if amount <= user_data[cardNumber]['balance'] and amount > 0:
            user_data[cardNumber]['balance'] -= amount
            print(f'✅ ₹{amount} withdrawn successfully.')
            print(f'💰 Updated balance: ₹{user_data[cardNumber]["balance"]}')
        else:
            print('❌ Insufficient balance or invalid amount.')
    else:
        print('❌ Please enter a valid number.')

# ✅ Deposit
def deposit(cardNumber):
    amount = input('Enter the amount to deposit: ')
    if amount.isdigit():
        amount = int(amount)
        if amount > 0:
            user_data[cardNumber]['balance'] += amount
            print(f'✅ ₹{amount} deposited successfully.')
            print(f'💰 Updated balance: ₹{user_data[cardNumber]["balance"]}')
        else:
            print('❌ Amount must be greater than zero.')
    else:
        print('❌ Please enter a valid number.')

# ✅ Main Execution
cardNumber = input("Enter your card number: ").strip()
pin_input = input("Enter your PIN: ").strip()

# Check if pin is numeric before converting
if pin_input.isdigit():
    pin = int(pin_input)
    if login(cardNumber, pin):
        show_menu(cardNumber)
    else:
        print("❌ Access denied.")
else:
    print("❌ PIN should be numeric.")
