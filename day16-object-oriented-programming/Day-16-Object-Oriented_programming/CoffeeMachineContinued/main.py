#My completed version 07/28/25
from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_atm = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    choices = menu.get_items()
    choice = input(f"What would you like? ({choices})").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        my_atm.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and my_atm.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)