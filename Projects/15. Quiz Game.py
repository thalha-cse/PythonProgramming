# This project is Quiz game, very easy project. Basics of python are used in this project

print("Welcome to My Quiz Game\nInteresting Game to Play")
player = input("Do you want to play the game? ")
if player.lower() != "yes":
    print("Good Bye!")
    quit()

name_player = input("Enter Your Name:- ")
print("Let's Start the game:)",name_player)
score = 0

answer = input("What is CPU stands for?\n")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is GPU stands for?\n")
if answer.lower() == "graphical processing unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is RAM stands for?\n")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is ROM stands for?\n")
if answer.lower() == "read only memory":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("Mouse is an input device or output device?\n")
if answer.lower() == "input device":
    print("Correct")
    score += 1
else:
    print("Wrong")

print("You got the "+str(score)+" correct answers")
print("You got the " + str((score/5)*100)+" Correct answers")
print("Thanks for playing with us")
