# This project is dice roller simulator
# The Dice Roll Simulation can be done by choosing a random integer between 1 and 6 for which we can use the random module in the Python programming language

import random

min_val = 1
max_val = 2

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the Dice")
    print("Dice Values are : ")

    print(random.randint(min_val, max_val))

    print(random.randint(min_val, max_val))

    roll_again = input("Roll the dices again? ")
