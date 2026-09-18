class UserInput:
    def __init__(self):
        self.rounds = None

    def get_number_of_rounds(self):
        while True:
            try:
                rounds = int(input("Please enter the number of rounds you want to play (3, 5, or 7): "))
                if rounds in [3, 5, 7]:
                    self.rounds = rounds
                    return rounds
                else:
                    print("Invalid input. Please enter 3, 5, or 7.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def get_user_choice(self):
        while True:
            choice = input("Please enter your choice (rock, paper, or scissors): ").lower()
            if choice in ["rock", "paper", "scissors"]:
                return choice
            else:
                print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")