# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to Kayla's food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected menu category name {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            customer_item_number = input(f"Type {menu_category_name} item number: ")

            # 3. Check if the customer typed a number
            if customer_item_number.isdigit():
                if int(customer_item_number) in menu_items.keys():

                    # Ask the customer for the quantity of the menu item
                    customer_quantity = input("Enter quantity ")
                    
                    # Check if the quantity is a number, default to 1 if not
                    if customer_quantity.isdigit():
                    
                        # Add the item name, price, and quantity to the order list
                        order_list.append({
                            "item_name": menu_items[int(customer_item_number)]["Item name"],
                            "item_price": menu_items[int(customer_item_number)]["Price"],
                            "item_quantity": int(customer_quantity)
                        })
                    
                    else:
                        # quantity defaults to 1
                        order_list.append({
                            "item_name": menu_items[int(customer_item_number)]["Item name"],
                            "item_price": menu_items[int(customer_item_number)]["Price"],
                            "item_quantity": 1
                        })
                
                else:
                    # Tell the customer they didn't select a valid option
                    print(f"{customer_item_number} is not a menu option.")

            else:
                # Tell the customer they didn't select a number
                print("You didn't select a number.")
       
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    # Ask the customer if they would like to order anything else
    keep_ordering = input("Enter (Y)es to keep ordering or anything else to stop ").upper()

    # Trying out the match-case syntax
    # I decided to treat N and any other typo as the same thing
    match keep_ordering.split():
        case ["Y"]:
            continue
        case _:
            print("Thank you for your order!")
            break

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Print final order headings
print("Item # | Item name                 | Price    | Quantity | Amount     ")
print("-------|---------------------------|----------|----------|------------")

# 6. Loop through the items in the customer's order
i = 1
for customer_item in order_list:

    # 7. Store the dictionary items as variables
    customer_item_name = customer_item["item_name"]
    customer_item_price = '{:6.2f}'.format(float(customer_item["item_price"]))
    customer_item_quantity = '{:3d}'.format(customer_item["item_quantity"])
    customer_item_amount = '{:6.2f}'.format(float(customer_item["item_price"]) * customer_item["item_quantity"])

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(customer_item_name)

    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    six_spaces = " " * 6

    # 10. Print the item name, price, and quantity
    # I realize that variable i should be formatted in case item numbers > 9
    print(
        f"{i}{six_spaces}"
        + f"| {customer_item_name}{item_spaces}"
        + f"| ${customer_item_price}  "
        + f"| {customer_item_quantity}{six_spaces}"
        + f"| ${customer_item_amount}"
    )
    i+=1

# 11. Calculate the cost of the order using list comprehension
# Please note that I could also have summed up my variable customer_item_amount
customer_order_total = [ordered_item["item_price"] * ordered_item["item_quantity"] for ordered_item in order_list]

# Multiply the price by quantity for each item in the order list, then sum()
# and print the total price.
print(f"\nYour total is $" '{:0.2f}'.format(sum(customer_order_total)))
