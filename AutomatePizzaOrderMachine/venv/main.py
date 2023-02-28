MEDIUM_AND_LARGE_PIZZA_PEPPERONI = 3
EXTRA_CHEESE = 70
LARGE_PIZZA = 700
SMALL_PIZZA = 300
MEDIUM_PIZZA = 500
SMALL_PIZZA_PEPPERONI = 140

size = input("Enter Pizza Size Large, Medium and Small ")
add_pepperoni = input("Add Pepperoni or not ")
add_EXTRA_CHEESE = input("Add Extra Cheese or not ")
if size == 'l':
    if add_pepperoni == 'y' and add_EXTRA_CHEESE == 'y':
        bill = LARGE_PIZZA + MEDIUM_AND_LARGE_PIZZA_PEPPERONI + EXTRA_CHEESE
        print("Final Bill ", bill)
    elif add_pepperoni == 'y' and add_EXTRA_CHEESE == 'n':
        bill = LARGE_PIZZA + MEDIUM_AND_LARGE_PIZZA_PEPPERONI
        print("Final Bill ", bill)
    elif add_PEPPERONI == 'n' and add_EXTRA_CHEESE == 'y':
        bill = LARGE_PIZZA + EXTRA_CHEESE
        print("Final Bill ", bill)
    else:
        bill = LARGE_PIZZA
        print("Final Bill ", bill)
elif size == 'm':
    if add_pepperoni == 'y' and add_EXTRA_CHEESE == 'y':
        bill = MEDIUM_PIZZA + MEDIUM_AND_LARGE_PIZZA_PEPPERONI + EXTRA_CHEESE
        print("Final Bill ", bill)
    elif add_pepperoni == 'y' and add_EXTRA_CHEESE == 'n':
        bill = MEDIUM_PIZZA + MEDIUM_AND_LARGE_PIZZA_PEPPERONI
        print("Final Bill ", bill)
    elif add_pepperoni == 'n' and add_EXTRA_CHEESE == 'y':
        bill = MEDIUM_PIZZA + EXTRA_CHEESE
        print("Final Bill ", bill)
    else:
        bill = MEDIUM_PIZZA
        print("Final Bill ", bill)
elif size == 's':
    if add_pepperoni == 'y' and add_EXTRA_CHEESE == 'y':
        bill = SMALL_PIZZA + SMALL_PIZZA_PEPPERONI + EXTRA_CHEESE
        print("Final Bill ", bill)
    elif add_pepperoni == 'y' and add_EXTRA_CHEESE == 'n':
        bill = SMALL_PIZZA + SMALL_PIZZA_PEPPERONI
        print("Final Bill ", bill)
    elif add_pepperoni == 'n' and add_EXTRA_CHEESE == 'y':
        bill = SMALL_PIZZA + EXTRA_CHEESE
        print("Final Bill ", bill)
    else:
        bill = SMALL_PIZZA
        print("Final Bill ", bill)
else:
    print("Invalid Order")