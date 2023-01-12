import random
import time
from Utils_Files.Utils import screen_cleaner
from Utils_Files.Score import add_score

#### Create a sequence list ####
sequence_list = []

for i in range(1, 101):
    sequence_list.append(str(i))


def generate_sequence(game_difficulty_choice):
    """A function to generate a random sequnce of numbers depending on the difficulty the user has chosen
in the previous step, shows them to the user and disappear after 0.7 seconds """

    sequence = random.sample(sequence_list, game_difficulty_choice)

    print(sequence)
    time.sleep(0.7)
    print("\n time is up\n\n\n\n")
    screen_cleaner()
    return sequence


def get_list_from_user():
    """a function that gets the user list of numbers they remember from the sequence showed to the user in
The previous step """

    while True:

        user_list = input('Please enter the list of numbers shown to you in the correct order ').split()
        if len(user_list) >= 1:
            return user_list


def is_list_equal(sequence, user_list):
    """A function that compares if the list that the user guessed is the same as the sequence
        (Checks number by number and outputs if the guess is correct or not"""

    for x, y in zip(sequence, user_list):
        if x == y or y == x:

            return True
        else:

            return False


def play_memory(game_difficulty_choice):
    """A function that calls the other functions to play the game"""
    sequence = generate_sequence(game_difficulty_choice)
    user_list = get_list_from_user()

    if is_list_equal(user_list, sequence):

        print(f'{user_list} is Correct')
        add_score()
    else:
        print(f'{user_list} are the wrong numbers, the correct numbers are: {sequence}')
