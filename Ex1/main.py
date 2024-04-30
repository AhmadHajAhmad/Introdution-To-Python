# Declaration of variables
BUDGET_PRICE = 500
ECONOMY_PRICE = 750
VIP_PRICE = 2000
BAG_PRICE = 200
MEAL_PRICE = 150
totalPrice = 0
bagCounter = 0
mealCounter = 0
menuOption = 0

# Displaying the ticket types menu
print("Ticket types:\n1. Budget  ( 500kr)\n2. Economy ( 750kr)\n3. VIP     (2000kr)")

# User choosing the ticket type
ticketOption = int(input("Input ticket type "))

# The total price is updated based on the user choice
if ticketOption == 1:
    totalPrice = totalPrice + BUDGET_PRICE
    chosenTicketPrice = BUDGET_PRICE
elif ticketOption == 2:
    totalPrice = totalPrice + ECONOMY_PRICE
    chosenTicketPrice = ECONOMY_PRICE
elif ticketOption == 3:
    totalPrice = totalPrice + VIP_PRICE
    chosenTicketPrice = VIP_PRICE

while menuOption != 5:

    # Displaying the main menu
    print("Currently you have:")
    print("    " + str(bagCounter) + " bag(s) registered")
    print("    " + str(mealCounter) + " meal(s) registered")
    print()
    print("Here are your options:")
    print("1. Add bag (max 1)\n"
          "2. Add meal (max 1)\n"
          "3. Remove bag\n"
          "4. Remove meal\n"
          "5. Finalize ticket")
    menuOption = int(input("Your choice "))

    # Handling different menu option
    if menuOption == 1 and bagCounter == 0:
        bagCounter = bagCounter + 1
        totalPrice = totalPrice + BAG_PRICE
    elif menuOption == 2 and mealCounter == 0:
        mealCounter = mealCounter + 1
        totalPrice = totalPrice + MEAL_PRICE
    elif menuOption == 3:
        if bagCounter == 1:
            bagCounter = bagCounter - 1
            totalPrice = totalPrice - BAG_PRICE
    elif menuOption == 4:
        if mealCounter == 1:
            mealCounter = mealCounter - 1
            totalPrice = totalPrice - MEAL_PRICE

# Displaying the receipt
print("Receipt:")
print("Ticket :{:>5}kr".format(chosenTicketPrice))
if bagCounter == 1:
    print("Bag    :{:>5}kr".format(BAG_PRICE))
if mealCounter == 1:
    print("Meal   :{:>5}kr".format(MEAL_PRICE))
print("        -------")
print("Total  :{:>5}kr".format(totalPrice))