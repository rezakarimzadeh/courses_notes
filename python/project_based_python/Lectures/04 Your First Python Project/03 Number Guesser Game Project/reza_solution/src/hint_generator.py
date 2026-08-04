
def hint_generator(guess, chosen_number):
    if guess < chosen_number:
        return "Your guess is too low. Try again."
    elif guess > chosen_number:
        return "Your guess is too high. Try again."
    