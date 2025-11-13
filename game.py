import random

print("Welcome to Rock-Paper-Scissors!")
player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

if player_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please try again.")
else:
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print(f"The computer chose {computer_choice}.")
    print(f"You chose {player_choice}.")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")