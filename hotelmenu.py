#Define the menu of restaurant
menu = {
    'Pizza' :8.5,
    'Pasta' :10,
    'Burger':10,
    'Salad' :9,
    'Coffee':9,
}

#Greet
print("Welcome to Abiha's Kitchen")
print("Pizza: EUR 8.5\nPasta: EUR 10\nBurger: EUR 10\nSalad: EUR 9\nCoffee: EUR 9")

order_total = 0
#9 + 9 = 18

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 8.5
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet ")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")