# To create the Rock, Paper and Scissors game with Python, we need to take the user’s choice and 
# then we need to compare it with the computer choice which is taken using the random module in Python from a list of choices, 
# and if the user wins then the score will increase by 1:


import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
comp_score = 0
player_score = 0
player = False
while True:
    player = input("Rock, Paper, Scissors ? ").capitalize()
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            comp_score += 1
        else:
            print("You Win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Rock":
            print("You win!", player, "covers", computer)
            player_score += 1
        else:
            print("You Lose!", computer, "cuts", player)
            comp_score += 1
    elif player == "Scissors":
        if computer == "Paper":
            print("You Win!", player, "cuts", computer)
            player_score += 1
        else:
            print("You lose!", computer, "smashes", player)
    elif player == "End":
        print("Final Score : ")
        print(f"Computer Score : {comp_score}")
        print(f"Player_Score : {player_score}")
        break
