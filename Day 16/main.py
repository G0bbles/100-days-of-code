from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
MACHINE_ON = True

while MACHINE_ON:
    user_choice = input("What drink would you like? (espresso/latte/cappuccino/): ").lower()
    if user_choice == 'report':
        coffee_machine.report()
        money_machine.report()
    elif user_choice == 'off':
        MACHINE_ON = False
    elif user_choice in menu.get_items().split('/'):
        drink = menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    else:
        print("Please enter a valid choice.")