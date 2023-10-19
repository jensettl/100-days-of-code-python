from data import MENU, resources, profit


def is_resource_sufficient(ingredients: {str: int}):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"​Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    total = int(input("how many 50c coins?: ")) * 0.5
    total += int(input("how many 20c coins?: ")) * 0.2
    total += int(input("how many 10c coins?: ")) * 0.1
    total += int(input("ho many 5c coins?: ")) * 0.05
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is €{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name):
    """Deduct the required ingredients from the resources."""
    for ingredient in drink_name["ingredients"]:
        resources[ingredient] -= drink_name["ingredients"][ingredient]
    print(f"Here is your {choice} ☕️. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: €{profit}")

    else:
        if choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(drink)

        else:
            print("Not a valid choice")
