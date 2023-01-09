import  os
from time import sleep
from IPython.display import clear_output

#### Utils file for a text score file, a number for a bad returned code ####

SCORE_FILE_NAME = 'templates/Scores.txt'

BAD_RETURN_CODE = 501


def screen_cleaner():
    os.system('cls')


def play_again():
    user_input = input('Would you like to play another round? enter y for yes and n for no  ').lower()
    if user_input == 'y':
        return True
    else:
        return False











clear_output()
