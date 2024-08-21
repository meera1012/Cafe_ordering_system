import json

# Sample menu items with prices
MENU = {
    'Coffee': 2.50,
    'Tea': 2.00,
    'Sandwich': 5.00,
    'Cake': 3.50,
    'Pastry': 4.00
}

# Initialize order
def initialize_order():
    return []

# Display menu
def display_menu():
    print("\n--- Cafe Menu ---")
    for item, price in MENU.items():
        print(f"{item}: ${price:.2f}")

# Take an order from the customer
def take_order():
    order = initialize_order()
    while True:
        display_menu()
        item = input("Enter the item you want to order (or type 'done' to finish): ").capitalize()
        if item == 'Done':
            break
        elif item in MENU:
            order.append(item)
            print(f"{item} added to your order.")
        else:
            print("Item not found. Please choose from the menu.")
    return order

# Calculate the total bill
def calculate_bill(order):
    total = sum(MENU[item] for item in order)
    return total

# Print the bill
def print_bill(order):
    total = calculate_bill(order)
    print("\n--- Bill ---")
    for item in order:
        print(f"{item}: ${MENU[item]:.2f}")
    print(f"Total: ${total:.2f}")
    print("Thank you for your order!")

# Main function
def main():
    while True:
        print("\nWelcome to the Cafe Ordering System")
        order = take_order()
        if order:
            print_bill(order)
        else:
            print("No items ordered.")
        
        again = input("\nDo you want to place another order? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
