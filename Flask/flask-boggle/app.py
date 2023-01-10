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

    return render_template("index.html", board=board)


@app.route("/check-word")
def check_word():
    """Take the word from the params of our axios GET request and check it against the board we
    have saved in session."""
    word = request.args['word']
    board = session['board']
    response_string = boggle_game.check_valid_word(board, word)
    # this variable will be one of the three strings: "ok", "not-a-word", or "not-on-board"

    return jsonify({'response': response_string})
