import json
import pandas as pd

# File where inventory data is stored
INVENTORY_FILE = 'inventory.json'

class inventory_management_system:

    def __init__(self):
        print('Hello Welcome to our Inventory Management System')

    def show_menu(self):
        # Display the main menu and handle user choices
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
                self.add_item()
            elif choice == '2':
                self.view_all_products()
            elif choice == '3':
                self.update_item()
            elif choice == '4':
                self.remove_item()
            elif choice == '5':
                self.search_item()
            elif choice == '6':
                print('👋 Thank you for using our Inventory Management System. Have a nice day!')
                break
            else:
                print('⚠️ Invalid choice. Please try again.')

    def view_all_products(self):
        # Load and display all products in the inventory
        with open(INVENTORY_FILE, 'r') as file:
            products = json.load(file)
            df = pd.DataFrame(products).T.reset_index()
            df.columns = ['Product ID', 'Product Name', 'Quantity', 'Price']
            print(df)

    def save_inventory(self, data):
        # Save updated inventory data to the file
        with open(INVENTORY_FILE, 'w') as file:
            json.dump(data, file, indent=4)

    def add_item(self):
        # Add a new product to the inventory
        pId = 0
        new_data = {}

        with open(INVENTORY_FILE, 'r') as file:
            new_data = json.load(file)

            if new_data:
                last_id = list(new_data.keys())[-1]  # Get the last ID
                num = int(last_id[1:]) + 1           # Calculate next ID
                pId = f'P{num:03d}'                  # Format new ID (e.g., P005)
            else:
                pId = 'P001'                         # First product if inventory is empty

        p_name = input('Enter the name of new product : ').strip()
        p_qty = input('Enter the Quantity of new product : ').strip()
        p_price = input('Enter the per piece price of a new product : ').strip()

        if p_price.isdigit() and p_qty.isdigit():
            new_data[pId] = {
                'name': p_name,
                'qty': p_qty,
                'price': p_price
            }

            with open(INVENTORY_FILE, 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            print('Invalid details.')

    def remove_item(self):
        # Remove a product from the inventory
        remove_product_name = input('Enter the name of item you want to remove : ').strip().lower()
        pId = ''

        with open(INVENTORY_FILE, 'r') as file:
            data = json.load(file)
            key = list(data)
            names = []

            for i in key:
                names.append(data[i]['name'])

            if remove_product_name in names:
                for i in key:
                    if remove_product_name == data[i]['name']:
                        pId = i
                if pId:
                    data.pop(pId)
            else:
                print(f"❌ Product '{remove_product_name}' not found.")

        if pId:
            with open(INVENTORY_FILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"🗑️ Product '{remove_product_name}' deleted successfully.")

    def update_item(self):
        # Update existing product details
        print('Which product you want to Update')
        name = input('Please Enter the name of the Product : ').strip()
        pId = ''
        data = ''

        with open(INVENTORY_FILE, 'r') as file:
            data = json.load(file)
            key = list(data)
            names = []

            for i in key:
                names.append(data[i]['name'])

            if name in names:
                for i in key:
                    if name == data[i]['name']:
                        pId = i
            else:
                print(f"❌ Product '{name}' not found.")

        print('What you want to update')
        print('1. Product Name')
        print('2. Product Quantity')
        print('3. Product Price')

        choice = input('Enter your choice : ').strip()

        if choice == '1':
            data[pId]['name'] = input('Enter the New Name of Product : ')
        elif choice == '2':
            data[pId]['qty'] = input('Enter the Updated Quantity of a Product : ')
        elif choice == '3':
            data[pId]['price'] = input('Enter a Updated Price of a Product : ')
        else:
            print('Enter a Valid Choice...')

        with open(INVENTORY_FILE, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"✅ Product '{name}' updated successfully.")

    def search_item(self):
        # Search for a product in the inventory
        search_product = input('Enter the name of the product you wants to search : ').strip().lower()

        with open(INVENTORY_FILE, 'r') as file:
            data = json.load(file)
            key = list(data)
            names = []

            for i in key:
                names.append(data[i]['name'])

            if search_product in names:
                print('✅ Product is in Stock')
            else:
                print('❌ Product is not in Stock')


# Start the inventory management system
inventory = inventory_management_system()
inventory.show_menu()
