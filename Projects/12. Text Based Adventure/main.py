# This project is about text based adventure
# A text-based adventure game is a completely text-based and very simple game. In this game, users have options to tackle a situation and with each input provided by the user, 
# the game will continue to increase by putting more situations and more options. This is what a good task for a beginner to get their hands on.

name = input("Enter you name:- ")
print(f"{name} you stuck at work")
print("You are still working and suddenly you saw a ghost, now you have two options")
print("1.Run \n2.Jump from the window")
user = int(input("Enter the option 1 or 2:- "))
if user == 1:
    print("You did it")
elif user == 2:
    print(f"You are not that much smart {name}")
else:
    print("Enter the option correctly")
