from img.ascii import greetings_coffee, coffee
from src.data import data, menu, cash


def new_order():
    print(greetings_coffee) 
    print("Hello there! Welcome to our Virtual Coffee Machine.")
    while True:     
        ask = input("What would you like? Type Espresso, Latte, Cappuccino (or 'E' for exit): ").lower()
        if ask == "espresso":
            return "espresso"
        elif ask == "latte":
            return "latte"
        elif ask == "cappuccino":
            return "cappuccino"
        elif ask == "off":
            return "off"
        elif ask == "e":
            return "exit"
        elif ask == "report":
            return "report"
        else:
            print("Invalid Request.")


def report():
    water = data[0]["ingredient"] + ": " + str(data[0]["amount"]) + data[0]["measure"]
    milk = data[1]["ingredient"] + ": " + str(data[1]["amount"]) + data[1]["measure"]
    coffee = data[2]["ingredient"] + ": " + str(data[2]["amount"]) + data[2]["measure"]
    print(water + "\n" + milk + "\n" + coffee)
    print(f"Money: ${cash['money']:.2f}")


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        ingredient_data = next((i for i in data if i["ingredient"] == item), None)
        if ingredient_data:
            if order_ingredients[item] > ingredient_data["amount"]:
                print(f"Sorry, there is not enough {item}.")
                return False
        else:
            print(f"Ingredient {item} is not available.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def update_ingredients(order_ingredients):
    for item in order_ingredients:
        ingredient_data = next((i for i in data if i["ingredient"] == item), None)
        if ingredient_data:
            ingredient_data["amount"] -= order_ingredients[item]


def main():
    on = True

    while on:
        order = new_order()
        if order == "off":
            print("Bye bye!")
            on = False
        elif order == "exit":
            print("See you soon!")
            on = False    
        elif order == "report":
            report()
        else:
            if is_resource_sufficient(menu[order]["ingredients"]):
                payment = process_coins()
                if payment >= menu[order]["cost"]:
                    change = round(payment - menu[order]["cost"], 2)
                    cash["money"] += menu[order]["cost"]
                    update_ingredients(menu[order]["ingredients"])
                    print(coffee)
                    print(f"Here is ${change:.2f} in change.")
                    print(f"Enjoy your {order}!\n")
                else:
                    print("Sorry, that's not enough money. Money refunded.")


main()
