def input_positive_int(prompt: str) -> int:
    # check if the input is a positive integer.
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            else:
                print("Value must be a positive integer!")
        except ValueError:
            print("Invalid input Please enter a whole number.")

def input_non_numeric_string(prompt: str) -> str:
    # check if the input is a non-numeric string.
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty Please try again.")
        elif value.isdigit():
            print("Input cannot be a number Please enter text.")
        else:
            return value

def display_inventory(products):
    # Display all products.
    print("\nCurrent Inventory:")
    for prod in products:
        print(f"{prod['name']} | {prod['price']} RS | {prod['quantity']} | {prod['type']}")
    print() 

def display_total_products(products):
    # Print the total number of products in the inventory.
    print(f"Total number of products: {len(products)}\n")

def add_product(products):
    # Add a new product to the inventory with validations.
    print("Enter new product details:")
    name = input_non_numeric_string("Name: ")
    price = input_positive_int("Price in Rs: ")
    quantity = input_positive_int("Quantity (whole number): ")
    ptype = input_non_numeric_string("Type: ")
    
    new_product = {"name": name, "price": price, "quantity": quantity, "type": ptype}
    products.append(new_product)
    print("Product added successfully!")
    display_inventory(products)
    display_total_products(products)

def display_products_by_category(products):
    # Display products filtered by category.
    category = input("Enter category to display (e.g., Leafy green): ").strip().lower()
    print(f"\nProducts in category '{category}':")
    found = False
    for prod in products:
        if prod['type'].lower() == category:
            print(f"{prod['name']} | {prod['price']} RS | {prod['quantity']} | {prod['type']}")
            found = True
    if not found:
        print("No products found in this category.")
    print()

def remove_product(products):
    # Remove a product from the inventory.
    prod_name = input("Enter the product name to remove: ").strip().lower()
    initial_count = len(products)
    products[:] = [prod for prod in products if prod['name'].lower() != prod_name]
    if len(products) < initial_count:
        print(f"{prod_name.capitalize()} removed from inventory.")
    else:
        print("Product not found!")
    print(f"Total products remaining: {len(products)}\n")

def update_quantity(products):
    # Update the quantity of a product by adding a positive integer.
    prod_name = input("Enter the product name to update quantity: ").strip().lower()
    add_qty = input_positive_int("Enter the quantity to add: ")
    updated = False
    for prod in products:
        if prod['name'].lower() == prod_name:
            prod['quantity'] += add_qty
            print(f"Updated {prod['name']} quantity: {prod['quantity']}")
            updated = True
            break
    if not updated:
        print("Product not found!")
    print()

def purchase_products(products):
    # User can purchase products by entering the product name and quantity.
    # After purchases, remove products that are sold out (quantity == 0).
    total_bill = 0
    print("Enter products to purchase. Type 'done' when finished.")
    
    while True:
        item = input("Product name (or type 'done'): ").strip().lower()
        if item == 'done':
            break
        
        qty = input_positive_int("Quantity to purchase (whole number): ")
        found = False
        
        for prod in products:
            if prod['name'].lower() == item:
                found = True
                if prod['quantity'] < qty:
                    print(f"Insufficient stock for {prod['name']}. Available: {prod['quantity']}")
                else:
                    prod['quantity'] -= qty
                    cost = prod['price'] * qty
                    total_bill += cost
                    print(f"Added {qty} of {prod['name']} to purchase (Cost: {cost} RS).")
                    # Inform the user if this purchase sold out the product.
                    if prod['quantity'] == 0:
                        print(f"{prod['name']} is sold out and will be removed from inventory.")
                break
        
        if not found:
            print("Product not found!")
    
    print(f"\nTotal bill (rounded): {round(total_bill)} RS\n")
    
    # Remove all sold-out products.
    sold_out_products = [prod for prod in products if prod['quantity'] == 0]
    if sold_out_products:
        for prod in sold_out_products:
            print(f"Removing {prod['name']} from inventory as it is sold out.")
        products[:] = [prod for prod in products if prod['quantity'] > 0]
    
    print(f"Total number of products remaining: {len(products)}")


def main():
    # inventory list of products.
    products = [
        {"name": "lettuce", "price": 10, "quantity": 50, "type": "Leafy green"},
        {"name": "cabbage", "price": 20, "quantity": 100, "type": "Cruciferous"},
        {"name": "pumpkin", "price": 30, "quantity": 30, "type": "Marrow"},
        {"name": "cauliflower", "price": 10, "quantity": 25, "type": "Cruciferous"},
        {"name": "zucchini", "price": 20, "quantity": 50, "type": "Marrow"},
        {"name": "yam", "price": 30, "quantity": 50, "type": "Root"},
        {"name": "spinach", "price": 10, "quantity": 100, "type": "Leafy green"},
        {"name": "broccoli", "price": 20, "quantity": 75, "type": "Cruciferous"},
        {"name": "garlic", "price": 30, "quantity": 20, "type": "Leafy green"},
        {"name": "silverbeet", "price": 10, "quantity": 50, "type": "Marrow"}
    ]
    
    while True:
        print("====== Inventory System ======")
        print("1. Display total number of products")
        print("2. Add a new product")
        print("3. Display all products")
        print("4. Display products by category")
        print("5. Remove a product")
        print("6. Update product quantity")
        print("7. Purchase products")
        print("8. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_total_products(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            display_inventory(products)
        elif choice == '4':
            display_products_by_category(products)
        elif choice == '5':
            remove_product(products)
        elif choice == '6':
            update_quantity(products)
        elif choice == '7':
            purchase_products(products)
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == '__main__':
    main()
