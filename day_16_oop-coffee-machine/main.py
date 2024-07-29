from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

cont = True

while cont:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "report":
        coffee_machine.report()
    elif order == "off":
        cont = False
    else:
        item_order = menu.find_drink(order)
        if item_order is not None:
            can_make = coffee_machine.is_resource_sufficient(item_order)
            if can_make and money_machine.make_payment(item_order.cost):
                coffee_machine.make_coffee(item_order)
            else:
                print("Not enough resources to make your order")
                coffee_machine.report()

