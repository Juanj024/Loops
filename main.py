#def functions menu item
menuItems = ["Taco","Burrito","Nachos","Soft Drink","Quit"]
def menu():
    for i in range (1,6):
        print(i, menuItems[i - 1])

#salute
print("Welcome to Taco Palace!  Please view the menu below and make a selection")

#initilization of the lists before the loop
order = []
price = []

choice = 0
while choice != 5:
    menu() # printing menu
    choice = int(input("Select your option \n"))    # asking the user for his choice
    print()
    print("You have selected", menuItems[choice - 1])
    print()

    #attaching the name and the price to each selection adding them to a list
    if menuItems[choice - 1] == menuItems[0]:
        order.append("Tacos")
        price.append(4.00)
    elif menuItems[choice - 1] == menuItems[1]:
        order.append("Burrito")
        price.append(6.50)
    elif menuItems[choice - 1] == menuItems[2]:
        order.append("Nachos")
        price.append(2.25)
    elif menuItems[choice - 1] == menuItems[3]:
        order.append("Soft Drink")
        price.append(4.00)

separation = " and "

print("You ordered",(separation.join(order)) + ".", "And your total is $" + str(sum(price)))













