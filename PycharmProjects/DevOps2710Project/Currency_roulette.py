import requests
import random

""" Create a random range for the amount parameter of the currency API """
random_currency_number = random.randrange(1, 100)


"""Calls the converted result of USD into Shekels"""
url = f'https://api.exchangerate.host/convert?from=USD&to=ILS&amount={random_currency_number}'

response = requests.get(url)
# print(response.json()['result'])
currency_rate = response.json()['result']


def get_guess_from_user(game_difficulty_choice):
    """1. A function that creates an interval from the api currency data
    2. Requests the user's guess for the correct amount of Shekels converted from USD
    3. Checks if the user's guess is in the interval and declares if the user won or lost accordingly"""
    d = game_difficulty_choice
    t = currency_rate
    interval_1 = round(int((t - (5 - d))))
    interval_2 = round(int((t + (5 - d))))
    print(interval_1, interval_2)




    while True:
        currency_guess = input(f'Please guess the amount in ILS of this {random_currency_number} USD number ')
        if currency_guess.isdigit():
            currency_guess = int(currency_guess)
            break

    if currency_guess in range(interval_1, interval_2) or currency_guess == interval_1\
            or currency_guess == interval_2:
        return True
    else:
        return False




def play_currency(game_difficulty_choice):
    """A function to play the game"""
    from Score import add_score
    if get_guess_from_user(game_difficulty_choice):

        print('You Win!')
        add_score()
    else:
        print('You Lose')














