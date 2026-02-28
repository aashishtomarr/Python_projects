import random

def get_valid_int(prompt, error_msg="Invalid input! Please enter a number."):
    """Helper function to handle integer inputs safely."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_msg)

def play_game(username):
    print(f"\n--- Welcome {username}! The 0-100 Number Guessing Game starts now! ---")
    
    # Setup game parameters
    target_number = random.randint(0, 100)
    total_attempts = get_valid_int(f"{username}, how many attempts would you like?: ")
    
    points_per_mistake = round(100 / total_attempts, 2)
    print(f"Each wrong guess costs {points_per_mistake} points. Good luck!\n")

    for current_attempt in range(1, total_attempts + 1):
        remaining_attempts = total_attempts - current_attempt
        current_score = round(100 - ((current_attempt - 1) * points_per_mistake), 2)

        # Get and validate guess
        while True:
            guess = get_valid_int(f"Attempt {current_attempt}/{total_attempts}. Enter your guess: ")
            if 0 <= guess <= 100:
                break
            print("Please stay within the 0-100 range!")

        # Check the guess
        if guess == target_number:
            print(f"Congratulations {username}! You found {target_number}. Score: {current_score}")
            break
        elif guess < target_number:
            print(f"Higher! {remaining_attempts} attempts left.")
        else:
            print(f"Lower! {remaining_attempts} attempts left.")
    else:
        # This block runs only if the loop finishes without 'break'
        print(f"\nGame Over, {username}! You ran out of tries. The number was {target_number}. Final Score: 0")

    # Replay logic
    choice = input("\nType 'yes' to play again or any other key to exit: ").lower()
    if choice == 'yes':
        play_game(username)
    else:
        print(f"Thanks for playing, {username}. Goodbye!")

if __name__ == "__main__":
    user_name = input("Enter your username to start: ")
    play_game(user_name)
