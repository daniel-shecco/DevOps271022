from Game_Files.GuessGame import play_guess
from Game_Files.Currency_roulette import play_currency
from Game_Files.Memory_Game import play_memory
from Utils_Files.Utils import play_again


def welcome():
        """This Function Welcomes the player to the game and requires a string input"""

name = ''
while True:



    name = str(input('Hello what is your name? ').title())
    if name.isalpha():
        print(f'Hello {name} and welcome to WoG!\n')
        break


    if name.isnumeric():
        print('Please type a name with letters from A-Z')

def load_game():

        """ A function that asks the player to choose a game.
        Takes an integer from 1-3 and asks a player to choose a difficulty between 1-5
        And calls the different games according to the user's choice"""


while True:


    game_of_choice = input('''Please Choose a game to play \n
                    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n
                    2. Guess Game - guess a number and see if you chose like the computer\n
                    3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n
                            ''')


    if game_of_choice.isnumeric():
        game_of_choice = int(game_of_choice)
    if game_of_choice in range(1, 4):
        break
    else:
        print('Not a number between 1-3')




while True:

    game_difficulty_choice = input('Please choose a game difficulty between 1-5 ')
    if game_difficulty_choice.isnumeric():
        game_difficulty_choice = int(game_difficulty_choice)
        if game_difficulty_choice in range(1, 6):
            print(f'your game difficulty of choice is:  {game_difficulty_choice}')

            if game_of_choice == 1:
                play_memory(game_difficulty_choice)
                while True:
                    if play_again():
                        play_memory(game_difficulty_choice)
                    else:
                        break

                break


            elif game_of_choice == 2:
                while True:
                    play_guess(game_difficulty_choice)
                    if play_again():
                        play_guess(game_difficulty_choice)
                    else:
                        break
                    break



            elif game_of_choice == 3:
                while True:
                    play_currency(game_difficulty_choice)
                    if play_again():
                        play_currency(game_difficulty_choice)
                    else:
                        break
                    break


        else:
            print('Not a number between 1-5. Please choose your difficulty')































