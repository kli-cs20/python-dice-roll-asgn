# Python Dice Roll Program

# Import Random 'Tools' to use
import random

# Roll Function


def roll_dice():
    # Roll a Dice
    randNum1 = random.randrange(1, 7)
    randNum2 = random.randrange(1, 7)
    sum = randNum1 + randNum2

    print(str(randNum1) + "," + str(randNum2) + " (sum: " + str(sum) + ")")

    return sum


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
        # Roll Once
        roll_dice()
    elif selection == "2":
        # Roll Five Times
        n = 1
        while n <= 5:
            roll_dice()
            n += 1
    elif selection == "3":
        # Roll n times
        n = 1
        num_rolls = int(input("How many rolls would you like? "))
        while n <= num_rolls:
            roll_dice()
            n += 1
    elif selection == "4":
        # Roll Dice until Snake Eyes
        roll = True
        n = 0
        while roll:
            sum = roll_dice()
            n += 1
            if sum == 2:
                roll = False
                print("SNAKE EYES! It took " + str(n) +
                      " rolls to get snake eyes")

    elif selection == "5":
        print("\nEXIT")
        loop = False
