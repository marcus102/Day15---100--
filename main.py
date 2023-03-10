from coffee_machine_data import MENU, resources
from art import logo

def payment_process(first_coin, second_coin, third_coin, fourth_coin):
    total = first_coin * 0.25 + second_coin * 0.10 + third_coin * 0.05 + fourth_coin * 0.01
    return total

def flavors_choice(the_menu):
    if the_menu == 'espresso':
        flavor = MENU["espresso"]
        requirement = flavor["ingredients"]
        requirement["milk"] = 0
    elif the_menu == 'latte':
        flavor = MENU["latte"]
    elif the_menu == 'cappuccino':
        flavor = MENU["cappuccino"]
    return flavor

coffee_machine_on = True
first = resources["water"]
second = resources["milk"]
third = resources["coffee"]

final_report_list = []
final_report_list.append(resources["water"])
final_report_list.append(resources["milk"])
final_report_list.append(resources["coffee"])
print(logo)
copy_list = final_report_list.copy()
profit = 0
while coffee_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        coffee_machine_on = False
    elif user_choice == 'report':
        print(f"Water: {final_report_list[0]}")
        print(f"Milk: {final_report_list[1]}")
        print(f"Coffee: {final_report_list[2]}")
        print(f"Money: ${profit}")
        
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        flavors_types = flavors_choice(the_menu = user_choice)
        ingredient = flavors_types["ingredients"]
        
        water_availability = final_report_list[0] - ingredient["water"]
        final_report_list[0] = water_availability
        milk_availabilty = final_report_list[1] - ingredient["milk"]
        final_report_list[1] = milk_availabilty
        coffee_availabilty = final_report_list[2] - ingredient["coffee"]
        final_report_list[2] = coffee_availabilty
        
        if final_report_list[0] >= 0 and final_report_list[1] >=0 and final_report_list[2] >= 0:
            print("Please insert coins")
            quaters = float(input("How many quaters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            
            amount_to_pay = payment_process(first_coin= quaters, second_coin= dimes, third_coin= nickles, fourth_coin= pennies)        
            coffee_price = flavors_types["cost"]
            remainder = amount_to_pay - coffee_price
            if remainder > 0:
                print("Here is {:0.2f} dollars in change.".format(remainder))
                print(f"Here is your {user_choice}. Enjoy!")
                profit += coffee_price 
                copy_list = final_report_list.copy()
            elif remainder == 0:
                print(f"Here is your {user_choice}. Enjoy!")
                profit += coffee_price
                copy_list = final_report_list.copy()
            else:
                final_report_list = copy_list
                print("Sorry that's not enough money. Money refunded.")
                
        elif final_report_list[1] < 0 and final_report_list[0] and final_report_list[2] < 0:
            print("Sorry there is not enough resources.")
            final_report_list = copy_list
        elif final_report_list[1] < 0 and final_report_list[0] < 0:
            print("Sorry there is not enough water and milk.")
            final_report_list = copy_list
        elif final_report_list[2] < 0 and final_report_list[0]:
            print("Sorry there is not enough water and coffee.")
            final_report_list = copy_list
        elif final_report_list[1] < 0 and final_report_list[2] < 0:
            print("Sorry there is not enough milk and coffee.") 
            final_report_list = copy_list
        elif final_report_list[0] < 0:
            print("Sorry there is not enough water.") 
            final_report_list = copy_list
        elif final_report_list[1] < 0:
            print("Sorry there is not enough milk.") 
            final_report_list = copy_list
        elif final_report_list[2] < 0:
            print("Sorry there is not enough coffee.") 
            final_report_list = copy_list
    else:
        print("No such option!")