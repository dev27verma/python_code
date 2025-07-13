print("Thankyou for choosing Dev's Pizza")
number_of_pizza = int(input("How many pizza required? "))

LARGE_PIZZA = 250
MEDIUM_PIZZA = 200
SMALL_PIZZA = 150
EXTRA_CHEESE = 40
PEPPERONI_SMALL = 20
PEPPERONI_MEDIUM_LARGE = 30
bill = 0

for i in range(number_of_pizza):
    size = input("What size of Pizza do you want? S,M or L: ").lower()
    add_pepperoni = input("Do you want Pepperoni? Y or N: ").lower()
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if size == 's':
        bill += SMALL_PIZZA
    elif size == 'm':
        bill += MEDIUM_PIZZA
    else:
        bill += LARGE_PIZZA

    if add_pepperoni == 'y':
        if size == 's':
            bill += PEPPERONI_SMALL
        else:
            bill += PEPPERONI_MEDIUM_LARGE
    if extra_cheese == 'y':
        bill += EXTRA_CHEESE

print(f"Total Cost to Customer: {bill}")