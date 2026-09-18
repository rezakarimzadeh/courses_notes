from src.user_input import UserInput
from src.game_components import GameComponents

def main():
    user_input = UserInput()
    game_components = GameComponents()

    print("welcome to the rock paper scissors game!")
    rounds = user_input.get_number_of_rounds()
    print(f"You have chosen to play {rounds} rounds.")
    winer_determined = False
    while not winer_determined:
        print("=" * 30)
        print(f"Round {game_components.user_score + game_components.computer_score + 1} of {rounds}")
        computer_choice = game_components.get_random_choice()
        user_choice = user_input.get_user_choice()
        print(f"Computer chose: {computer_choice}")
        game_components.determine_winner(user_choice, computer_choice)
        print(f"Current Score - You: {game_components.user_score}, Computer: {game_components.computer_score}")

        if game_components.user_score > rounds // 2:
            print("Congratulations! You won the game!")
            winer_determined = True
        elif game_components.computer_score > rounds // 2:
            print("Sorry! The computer won the game!")
            winer_determined = True

if __name__ == "__main__":
    main()