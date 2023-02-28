from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def machine():
    is_on = True
    while is_on:
        choice = input(f"Enter the choice ({menu.get_items()})")
        if choice == 'off':
            is_on = False
            exit()
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            is_enough_ingredient = coffee_maker.is_resource_sufficient(drink)
            is_money_received = money_machine.make_payment(drink.cost)
            if is_money_received and is_enough_ingredient:
                coffee_maker.make_coffee(drink)


machine()
