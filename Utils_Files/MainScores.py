from flask import Flask, render_template
from Utils_Files.Utils import SCORE_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)


@app.route('/')
def score_server():
    f = open(SCORE_FILE_NAME)
    score = f.read()

    return render_template('scores.html', score=score)


@app.route('/')
def error():
    with open(BAD_RETURN_CODE, 'r') as error:
        e = error.read()

    return render_template('scores.html', error=e)


if __name__ == "__main__":
    app.run(debug=True)
