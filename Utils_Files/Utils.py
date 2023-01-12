import os

#### Utils file for a text score file, a number for a bad returned code ####

SCORE_FILE_NAME = 'C:/Users/danie/PycharmProjects/DevOps2710Project/Utils_Files/templates/Scores.txt'

BAD_RETURN_CODE = 501


def screen_cleaner():
    os.system('cls')


def play_again():
    user_input = input('Would you like to play another round? enter y for yes and n for no  ').lower()
    if user_input == 'y':
        return True
    else:
        return False











