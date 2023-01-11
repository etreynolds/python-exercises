from flask import Flask, render_template, session, request, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)

app.config['SECRET_KEY'] = "keepitsecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route("/")
def show_homepage():
    """Make the board, then render board in the DOM."""

    board = boggle_game.make_board()
    session['board'] = board

    # Get high score from session to display in DOM. If no high score, show 0
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    return render_template("index.html", board=board, highscore=highscore, numplays=numplays)


@app.route("/check-word")
def check_word():
    """Take the word from the params of our axios GET request and check it against the board we
    have saved in session."""
    word = request.args['word']
    board = session['board']
    response_string = boggle_game.check_valid_word(board, word)
    # this variable will be one of the three strings: "ok", "not-a-word", or "not-on-board"

    return jsonify({'response': response_string})


@app.route("/end-game", methods=["POST"])
def end_game():
    """Get axios POST (score) from endgame function and update high score in session"""
    score = request.json["score"]
    # get current high score from session. if no high score in session set variable to 0
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)
    # update high score in session
    session["highscore"] = max(score, highscore)
    session["numplays"] = numplays + 1
    return "game over"
