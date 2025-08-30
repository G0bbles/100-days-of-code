from recipes import MENU

machine_resources = {
    "water": 500,
    "milk": 250,
    "coffee": 100,
    "money": 10.00,
}

COINS = {
    "£2": 2.00,
    "£1": 1.00,
    "50p": 0.50,
    "20p": 0.20,
    "10p": 0.10,
    "5p": 0.05,
    "2p": 0.02,
    "1p": 0.01,    
}

def report():
    '''Prints a report of machine resources.'''
    print("The machine currently has:\n"
              f"Water: {machine_resources['water']}ml\n"
              f"Milk: {machine_resources['milk']}ml\n"
              f"Coffee: {machine_resources['coffee']}g\n"
              f"Money: £{machine_resources['money']:.2f}\n")
    return coffee_machine()

def check_resources(user_choice):
    '''Checks if there are enough resources to make the drink. If True, returns cost of drink.'''
    for key, value in MENU[user_choice]['ingredients'].items():
        if machine_resources[key] < value:
            print(f"There is not enough {key.capitalize()}. Please refill the machine.")
            return coffee_machine()
    return MENU[user_choice]['cost']

def insert_coins():
    '''Takes coins from the user. Adds them to the machine resources and returns the total amount'''
    total_paid = 0
    for key, value in COINS.items():
        total_paid += int(input(f"How many {key} coins: ")) * value
    machine_resources["money"] += total_paid
    return total_paid

def make_drink(user_choice):
    '''Removes resources from the machine based on drink ingredients.'''
    for key, value in MENU[user_choice]['ingredients'].items():
        machine_resources[key] -= value
    print(f"Enjoy your {user_choice.capitalize()}")
    return coffee_machine()

def refill():
    '''Resets the machine resources to default. Returns total profit so far.'''
    machine_resources["water"] = 500
    machine_resources['milk'] = 250
    machine_resources["coffee"] = 100
    return coffee_machine()

def coffee_machine():
    '''The main function. A machine that handles the primary program.'''
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'off':
        exit

    elif user_choice == 'report':
        report()

    elif user_choice == 'refill':
        refill()

    elif user_choice in MENU.keys():
        price = check_resources(user_choice)
        print(f"That will be £{price:.2f}. Please insert coins.")
        total_paid = insert_coins()

        if total_paid < price:
            print("That is not enough money. Money has been refunded.")
            machine_resources["money"] -= total_paid
            coffee_machine()
        else:
            if total_paid > price:
                print(f"Here is your change: £{(total_paid-price):.2f}")
                machine_resources["money"] -= total_paid - price
            make_drink(user_choice)
    else:
        print("You have not selected a valid option.")
        coffee_machine()

coffee_machine()
