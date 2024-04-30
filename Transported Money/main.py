# Declaration of variables
BIG_CAPACITY = 80
MEDIUM_CAPACITY = 50
SMALL_CAPACITY = 20
BIG_WORTH = 60000
MEDIUM_WORTH = 30000
SMALL_WORTH = 10000
bigCounter = 0
mediumCounter = 0
smallCounter = 0
totalValue = 0
remainingCapacity = 0
inputVolume = 0

# Displaying the main menu

print("Welcome to the Money Bag Transport Calculator (M.B.T.C)")
print("-------------------------------------------------------")
print()
inputVolume = int(input("What is the volume of the truck (>= 100L): "))

while inputVolume < 100:
    inputVolume = int(input("What is the volume of the truck (>= 100L): "))
print()

# Handling the logic of calculating the required number of bags

bigCounter = inputVolume // BIG_CAPACITY
remainingCapacity = inputVolume - (bigCounter * BIG_CAPACITY)
if remainingCapacity >= MEDIUM_CAPACITY:
    mediumCounter = remainingCapacity // MEDIUM_CAPACITY
    remainingCapacity = remainingCapacity - (mediumCounter * MEDIUM_CAPACITY)
if remainingCapacity >= SMALL_CAPACITY:
    smallCounter = remainingCapacity // SMALL_CAPACITY
    remainingCapacity = remainingCapacity - (smallCounter * SMALL_CAPACITY)

totalValue = (bigCounter * BIG_WORTH) + (mediumCounter * MEDIUM_WORTH) + (smallCounter * SMALL_WORTH)

# Displaying the result

print("Packing plan")
print("------------")
print(str(bigCounter) + " big bags")
print(str(mediumCounter) + " medium bags")
print(str(smallCounter) + " small bags")
print()
print("Space left : " + str(remainingCapacity) + "L")
print("Total value: " + str(totalValue) + "kr")