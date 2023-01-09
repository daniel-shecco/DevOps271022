import Utils

#### this function is responsible for the score counting of a player in the game #####


def add_score():
    from Live import game_difficulty_choice

    with open(Utils.SCORE_FILE_NAME, 'r') as score:
        initial_score = int((score.read()))
    POINTS_OF_WINNING = (game_difficulty_choice * 3) + 5
    new_score = POINTS_OF_WINNING + initial_score

    with open(Utils.SCORE_FILE_NAME, 'w') as score:
        score.write(str(new_score))
        print(new_score)















