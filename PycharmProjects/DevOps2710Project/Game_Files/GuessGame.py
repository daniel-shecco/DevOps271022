import random
from Utils_Files.Score import add_score


def generate_number(game_difficulty_choice):
    """ A function that generates a secret random number """


    secret_number = random.randint(1, game_difficulty_choice)
    return secret_number



def get_guess_from_user():
    """A function that takes an input from the user guessing the secret number """

    while True:
        user_guess = input("Please choose a number between 1 and the game difficulty you chose in the previous step \n")
        if user_guess.isnumeric():
            user_guess = int(user_guess)
            return user_guess






def compare_results(secret_number, user_guess):
    if user_guess == secret_number:
        return True

    else:
        return False






def play_guess(game_difficulty_choice):
    """A function that calls the other functions to play the game"""
    secret_number = generate_number(game_difficulty_choice)
    user_guess = get_guess_from_user()
    if compare_results(secret_number, user_guess):

        print('You win')
        add_score()

    else:
        print('You lose')




