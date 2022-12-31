from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home_page():
    return "Welcome to the Greet homepage!"


@app.route("/welcome")
def welcome_page():
    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    return "welcome home"


@app.route("/welcome/back")
def welcome_back():
    return "welcome back"
