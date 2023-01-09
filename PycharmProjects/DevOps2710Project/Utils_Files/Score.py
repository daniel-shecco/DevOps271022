from Utils_Files.Utils import SCORE_FILE_NAME
#### this function is responsible for the score counting of a player in the game #####

start_score = 0
def add_score():
    from Live import game_difficulty_choice

    with open(SCORE_FILE_NAME, 'r+') as score:
        initial_score = (score.write(str(start_score)))
        initial_score = int(initial_score)
    POINTS_OF_WINNING = (game_difficulty_choice * 3) + 5
    new_score = POINTS_OF_WINNING + initial_score

    with open(SCORE_FILE_NAME, 'w') as score:
        score.write(str(new_score))
        print(new_score)















