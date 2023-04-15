MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def process_coins():
    """Returns the total coins submitted"""
    print("Please enter coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_resource_sufficient(order_ingredients):
    """Returns True if resources enough and False if not"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Return true if payment successful or False if money insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Money is not enough. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}☕")


coffee_machine_on = True
while coffee_machine_on:
    order = input(" What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        print(f'''
                   Water: {resources["water"]}ml
                   Milk: {resources["milk"]}ml
                   Coffee: {resources["coffee"]}g
                   Money: ${profit}
                   ''')

    elif order == "off":
        coffee_machine_on = False
        print("Coffee Machine Closed")

    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
