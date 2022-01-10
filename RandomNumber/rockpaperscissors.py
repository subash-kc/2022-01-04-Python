import random

while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("rock, paper, scissors:\n").lower()

    if player == computer:

        print("Computer Chooses: ", computer)

        print("Player Chooses: ", player)
        print("You Tie with Computer")

    elif player == "rock":
        if computer == "paper":
            print("Computer Chooses: ", computer)
            print("Player Chooses: ", player)
            print("You Lose, Try Again!!!!")
        if computer == "scissors":
            print("Computer Chooses: ", computer)
            print("Player Chooses: ", player)
            print("You Won, Congratulations!!!!!!!")

    elif player == "paper":
        if computer == "rock":
            print("Computer Chooses: ", computer)
            print("Player Chooses: ", player)
            print("You Won, Congratulations!!!!")
        if computer == "scissors":
            print("Computer Chooses: ", computer)
            print("Player Chooses: ", player)
            print("You Lose, Try Again!!!!")

    elif player == "scissors":
        if computer == "paper":
            print("Computer Chooses: ", computer)
            print("Player Chooses: ", player)
            print("You Win, Congratulations!!!!")
        if computer == "rock":
            print("Computer Chooses: ", computer)
            print("Player Chooses: ", player)
            print("You Lose, Try Again!!!!")

    play_again = input("Do you want to play Again? (yes/no): ").lower()

    if play_again != "yes":
            break
print("Game Over!!")




