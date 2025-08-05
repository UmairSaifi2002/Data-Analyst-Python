# 📦 Initial Inventory
inventory = {
    "P001": {"name": "Soap", "qty": 20, "price": 30},
    "P002": {"name": "Shampoo", "qty": 15, "price": 120},
    "P003": {"name": "Toothpaste", "qty": 25, "price": 45},
    "P004": {"name": "Notebook", "qty": 40, "price": 60},
    "P005": {"name": "Pen", "qty": 100, "price": 10},
    "P006": {"name": "Bottle", "qty": 10, "price": 150}
}

# ✅ Main Menu Function
def show_inventory():
    while True:
        print('\n---- Inventory Menu ----')
        print('1. Add Product')
        print('2. View All Products')
        print('3. Update Product')
        print('4. Delete Product')
        print('5. Search Product')
        print('6. Exit')
        print('------------------------')
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            Add_Product()
        elif choice == '2':
            View_All_Products()
        elif choice == '3':
            Update_Product()
        elif choice == '4':
            Delete_Product()
        elif choice == '5':
            Search_Product()
        elif choice == '6':
            print('👋 Thank you for using our Inventory Management System. Have a nice day!')
            break
        else:
            print('⚠️ Invalid choice. Please try again.')

# ✅ Add Product (Uses global inventory)
def Add_Product():
    global inventory
    new_product_name = input('Enter the Product Name: ').strip()
    new_product_quantity = input('Enter the Quantity you want to add: ').strip()
    new_product_price = input('Enter the Price of the Product: ').strip()
    
    if new_product_quantity.isdigit() and new_product_price.isdigit():
        data = {
            'name': new_product_name,
            'qty': int(new_product_quantity),
            'price': int(new_product_price)
        }
        # Generate next product ID
        last_key = list(inventory.keys())[-1]
        last_num = int(last_key[1:])
        key = f"P{last_num + 1:03d}"
        inventory[key] = data
        print('✅ Your product was added successfully!')
    else:
        print('❌ Invalid details. Quantity and price must be numbers.')

# ✅ View All Products
def View_All_Products():
    print("\n📋 Inventory List:")
    for key, value in inventory.items():
        print(f'Product ID: {key} \t Name: {value["name"]} \t Quantity: {value["qty"]} \t Price: ₹{value["price"]}')

# ✅ Placeholder functions (to be implemented later)
def Update_Product():
    print("🛠️ Update functionality coming soon...")

def Delete_Product():
    print("🗑️ Delete functionality coming soon...")

def Search_Product():
    print("🔍 Search functionality coming soon...")

# ✅ Main Execution
print('👋 Welcome to the Inventory Management System')
show_inventory()
