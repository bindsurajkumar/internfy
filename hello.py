import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        # Generate random number between 1 and 100
        secret_number = random.randint(1, 100)
        attempts = 0
        
        while True:
            # Get user's guess
            guess = input("Enter your guess (1-100), or 'quit' to exit: ")
            
            # Check if user wants to quit
            if guess.lower() == 'quit':
                print(f"The secret number was {secret_number}. Thanks for playing!")
                return
            
            # Validate input
            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number or 'quit'.")
                continue
            
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        
        # Ask if user wants to play again
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    number_guessing_game()