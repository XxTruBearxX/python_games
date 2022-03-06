from random import randint

#As Sheldon from the T.V. show, "Big Bang Theory" explains, "Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors."

#create a list of play options
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

#assign a random play to the computer
computer = t[randint(0,4)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors, Lizard, Spock?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        elif computer == "Spock":
            print("You lose!", computer, "vaporizes", player)
        elif computer == "Lizard":
            print("You win!", player, "crushes", computer)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        elif computer == "Lizard":
            print("You lose!", computer, "eats", player)
        elif computer == "Spock":
            print("You win!", player, "disproves", computer)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "crushes", player)
        elif computer == "Spock":
            print("You lose!", computer, "smashes", player)
        elif computer == "Lizard":
            print("You win!", player, "decapitates", computer)
        else:
            print("You win!", player, "cut", computer)
    elif player == "Lizard":
        if computer == "Rock":
            print("You lose!", computer, "crushes", player)
        elif computer == "Scissors":
            print("You lose!", computer, "decapitates", player)
        elif computer == "Spock":
            print("You win!", player, "poisons", computer)
        else:
            print("You win!", player, "eats", computer)
    elif player == "Spock":
        if computer == "Lizard":
            print("You lose!", computer, "poisons", player)
        elif computer == "Paper":
            print("You lose!", computer, "disproves", player)
        elif computer == "Scissors":
            print("You win!", player, "smashes", computer)
        else:
            print("You win!", player, "vaporizes", computer)
    else:
        print("That's not a valid play. Check you spelling!")

#player was set to True, but we want it to be False so the loop continues
player = False
computer = t[randint(0,4)]