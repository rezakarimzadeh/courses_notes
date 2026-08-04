from src.random_generator import random_number_generator
from src.hint_generator import hint_generator
from src.input_validator import input_validator
    
def game_loop():
    score = 100
    random_number = random_number_generator()
    while score > 0:
        guess = input_validator("Guess the chosen number between 1 and 100: ", 1, 100)
        if guess == random_number:
            print(f"Congratulations! You've guessed the correct number: {random_number}. Your score is {score}.")
            break
        else:
            score -= 10            
            hint = hint_generator(guess, random_number)
            if score == 0:
                print(f"Game over! The correct number was {random_number}.")
                break
            print(hint)

def main():
    print("Welcome to the Number Guesser Game!")
    while True:
        game_loop()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()