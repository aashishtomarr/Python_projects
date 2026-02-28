import random

def play_rps(username):
    print(f"\nWelcome {username}! First to 3 wins takes the game.")
    
    options = ["rock", "paper", "scissors"]
    # Dictionary to define what beats what
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    user_wins = 0
    computer_wins = 0

    while user_wins < 3 and computer_wins < 3:
        computer_choice = random.choice(options)
        
        # Validation Loop
        user_choice = input("\nEnter rock, paper, or scissors: ").lower().strip()
        while user_choice not in options:
            user_choice = input(f"Invalid choice, {username}. Please enter rock, paper, or scissors: ").lower().strip()

        print(f"Computer chose: {computer_choice}")

        # Game Logic
        if user_choice == computer_choice:
            print("It's a tie!")
        elif rules[user_choice] == computer_choice:
            print(f"You win this round! {user_choice.capitalize()} beats {computer_choice}.")
            user_wins += 1
        else:
            print(f"Computer wins this round! {computer_choice.capitalize()} beats {user_choice}.")
            computer_wins += 1

        print(f"Score -> {username}: {user_wins} | Computer: {computer_wins}")

    # Final Result
    if user_wins == 3:
        print(f"\nCONGRATULATIONS {username.upper()}! You beat the computer {user_wins}-{computer_wins}.")
    else:
        print(f"\nGAME OVER! The computer beat you {computer_wins}-{user_wins}.")

    # Replay logic
    retry = input("\nType 'continue' to play again or 'exit' to quit: ").lower().strip()
    if retry == "continue":
        play_rps(username)
    else:
        print(f"Goodbye, {username}!")

if __name__ == "__main__":
    name = input("Enter your username: ")
    play_rps(name)
