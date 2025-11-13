print("Welcome to Rock-Paper-Scissors!")

player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

if player_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please try again.")
else:
    print(f"You chose {player_choice}.")