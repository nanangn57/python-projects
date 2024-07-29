from menu import MENU, resources


def make_coffee(flavor):
    for resource in ["water", "milk", "coffee"]:
        resources[resource] -= MENU[flavor]["ingredients"][resource]
    return resources


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {resources['money']}")


def input_coins():
    quarters = int(input("Please input number of quarters?"))
    dimes = int(input("Please input number of dimes?"))
    nickles = int(input("Please input number of nickles?"))
    pennies = int(input("Please input number of quarters?"))
    return quarters, dimes, nickles, pennies


def process_coin(quarters, dimes, nickles, pennies):
    coin = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return round(coin, 2)


off = False

while not off:
    user_require = input("What would you like? (espresso/latte/cappuccino): ")

    if user_require == 'report':
        report()

    elif user_require in ['espresso', 'latte', 'cappuccino']:
        for resource_type in ["water", "milk", "coffee"]:
            if resources[resource_type] < MENU[user_require]["ingredients"][resource_type]:
                print(f"Not enough of resources to make {user_require}. Please come back next time")
                cont = False
                break
            else:
                cont = True

        if cont:
            print(f"Thanks for ordering {user_require}. Your order will cost ${MENU[user_require]['cost']}.Please "
                  f"insert coins.")
            changes = -1
            coins_input = 0

            while changes < 0:
                input_quarters, input_dimes, input_nickles, input_pennies = input_coins()
                coins_input += process_coin(input_quarters, input_dimes, input_nickles, input_pennies)
                changes = round(coins_input - MENU[user_require]['cost'], 2)
                print(f"You input {round(coins_input,2)}. Flavor {user_require} costs {MENU[user_require]['cost']}$")
                # check successful transaction
                if changes >= 0:
                    resources = make_coffee(user_require)
                    resources['money'] += MENU[user_require]['cost']
                    print(f"Here is your {user_require}")
                    if changes > 0:
                        print(f"Here is ${changes} dollars in change")
                else:
                    print(f"You don't input enough money. Please insert ${-changes} more dollars!")

    elif user_require == 'off':
        off = True
