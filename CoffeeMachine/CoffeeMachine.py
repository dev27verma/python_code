from menu import resources, MENU

profit = 0

def resources_sufficient(order_ingredient):
    for item in order_ingredient:
        if resources[item] < order_ingredient[item]:
            print("Ingredient not available")
            return False
    return True

def processed_coin():
    total = int(input("Enter the money "))
    return total

def transaction_successful(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Please take change Rs {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Transaction failed, try again")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Enjoy your drink")

def coffee_machine():
    is_on = True
    while is_on:
        choice = input("Enter a choice ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water {resources['water']}")
            print(f"Milk {resources['milk']}")
            print(f"Coffee {resources['coffee']}")
            print(f"Profit {profit}")
        else:
            drink = MENU[choice]
            if resources_sufficient(drink['ingredients']):
                payment = processed_coin()
                if transaction_successful(payment, drink['cost']):
                    make_coffee(choice,drink['ingredients'])
coffee_machine()