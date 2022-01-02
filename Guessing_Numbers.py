# This project is Guessing the number which is ramdomly choosen by our computer and we have guess it.
# This project contain...
# 1. Random package 2. While loop 3. if elif else and more


import random

print("---------------------------------------------")
upper = int(input("Enter a starting number:- "))
lower = int(input("Enter a ending number:- "))
ran = random.randint(upper, lower)
n = int(input("Enter how many chances do you want:- "))
count = 0
while count <= n:
    count += 1
    guess = int(input("Enter your guess users:- "))
    if guess == ran:
        print("Congratulations! you did it in",count," th try")
        print("----------------------------------------------")
        break
    elif guess <= ran:
        print("You guessed too small!")
    elif guess >= ran:
        print("You guess too high!")
    else:
        print("Game Over! Better luck bext time users")
        print("The number which i guessed is",ran)
        print("----------------------------------------------")
