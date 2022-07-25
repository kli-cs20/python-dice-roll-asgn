# Python Dice Roll Program

# Import Random 'Tools' to use
import random

# Main Program Loop
loop = True
while loop:
    # Print Main Menu
    print("\nDice Roll Simulator")
    print("1: Roll Dice Once")
    print("2: Roll Dice 5 Times")
    print("3: Roll Dice 'n' Times")
    print("4: Roll Dice until Snake Eyes")
    print("5: Exit")

    # Get Menu Selection from User
    selection = input("Enter Selection (1-5): ")

    # Take Action Based on Menu Selection
    if selection == "1":
        print("\nOption 1")
    elif selection == "2":
        print("\nOption 2")
    elif selection == "3":
        print("\nOption 3")
    elif selection == "4":
        print("\nEXIT")
        loop = False


def roll_dice():
    # Roll a Dice
    randNum1 = random.randrange(1, 7)
    randNum2 = random.randrange(1, 7)
    sum = randNum1 + randNum2

    print(str(randNum1) + "," + str(randNum2) + " (sum: " + str(sum) + ")")


roll_dice()
