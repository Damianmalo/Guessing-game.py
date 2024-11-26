import random
#Damian Malo and Manny Pulgarin 
def print_welcome_message():
    """Prints the welcome message for the game."""
    print("=" * 50)
    print("🎉 Lets play a little game. 🎉")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("You have a maximum of 10 attempts. Or you die.")
    print("=" * 50)

def get_player_guess(attempt, max_attempts):
    """
    Prompts the player for their guess.
    Ensures the input is a valid integer.
    """
    while True:
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))
            return guess
        except ValueError:
            print("⚠️ Invalid input. Enter a valid number lil bro.")

def play_game():
    """Main function to play the game."""
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    # guessing loop
    while attempts < max_attempts:
        guess = get_player_guess(attempts + 1, max_attempts)

        # Check if the guess is correct
        if guess == target_number:
            print(f"\n🎉 Congrats, You guessed the number in {attempts + 1} attempts. Get out of here before I kill you.")
            break
        elif guess < target_number:
            print("📉 Too low buddy, Try again.")
        else:
            print("📈 Too high buddy, Try again.")
        
        attempts += 1  

    # If the player uses all attempts without guessing correctly
    if attempts == max_attempts:
        print(f"\n😢 Game Over! The correct number was {target_number}. You're dead lil bro.")

def play_again():
    """Asks the player if they want to play again."""
    while True:
        response = input("Would you like to play again? (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("⚠️ Please enter 'yes' or 'no'.")

def number_guessing_game():
    """Coordinates the flow of the game."""
    print_welcome_message()
    while True:
        play_game()
        if not play_again():
            print("\n🎮 Thanks for playing, *dead*. 🎮")
            break


if __name__ == "__main__":
    number_guessing_game()
