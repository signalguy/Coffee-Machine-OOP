from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

flag = True

coffee_maker.__init__()
money_machine.__init__()

while flag:
    sel = input(f"What would you like to drink({menu.get_items()})? ").lower()
    
    if sel == "report":
        coffee_maker.report()
        money_machine.report()
    elif sel == "off":
        print("Turn off ")
        flag = False
    else:
        order = menu.find_drink(sel)
        if order != None:
            if coffee_maker.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)