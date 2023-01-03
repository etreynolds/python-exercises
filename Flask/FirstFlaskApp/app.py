from flask import Flask, request, render_template, redirect, flash
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "keepitsecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route('/hello')
def say_hello():
    # html = "<html><body><h1>Hello there!</h1><a href='/'>Go to home page</a></body></html>"
    # return html
    """Returns template"""
    return render_template("hello.html")


@app.route('/goodbye')
def say_bye():
    return "Goodbye"


@app.route('/thank-you')
def thank_you():
    html = "<html><body><h1>Thank you!</h1></body></html>"
    return html


@app.route('/search')
def search():
    # print(request.args)
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search results for: {term}</h1><p>Sorting by: {sort}</p>"

# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "You made a post request!"


# @app.route("/post", methods=["GET"])
# def get_demo():
#     return "You made a get request!"

"""Handling POST requests"""
@app.route('/add-comment')
def add_comment_form():
    """Show form for adding a comment."""

    return """
    <form method="POST">
        <input name="comment">
        <button>Submit</button>
    </form
    """


@app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""

    comment = request.form["comment"]

    # TODO: save that into a database!

    return f"<h1>Received '{comment}'.</h1>"


"""Handling variables in a URL"""
@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    """Show subreddit name"""
    return f"<h1>Welcome to the <i>{subreddit}</i> subreddit!</h1>"


POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo!",
    3: "Double rainbow all the way",
    4: "YOLO OMG (kill me)"
}


@app.route('/posts/<int:id>')
def find_post(id):
    """Show post with given integer"""
    post = POSTS.get(id, "Post not found")
    return f"<p>{post}</p>"


# USING TEMPLATES


@app.route("/lucky")
def show_lucky_num():
    """Example of simple dynamic template"""
    num = randint(1, 10)
    return render_template("lucky.html", luckynum=num, msg="You are so lucky!")

# GREETER EXAMPLE


@app.route("/form")
def show_form():
    return render_template("form.html")


@app.route("/form-2")
def show_form_2():
    return render_template("form_2.html")


COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "legit"]


@app.route("/greet")
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)


@app.route("/greet-2")
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet_2.html", username=username, wants_compliments=wants, compliments=nice_things)

# USING LOOPS


@app.route("/spell/<word>")
def spell_word(word):
    caps_word = word.upper()
    return render_template("spell_word.html", word=caps_word)

# REDIRECTS


@app.route("/old-home-page")
def redirect_to_home():
    """Redirects to new homepage"""
    flash('That page has moved! This is our new page')
    return redirect("/")


MOVIES = {'Gladiator', 'LOTR', 'La La Land'}


@app.route('/movies')
def show_all_movies():
    """Show list of all movies in fake DB"""
    return render_template('movies.html', movies=MOVIES)


@app.route('/movies/new', methods=['POST'])
def add_movie():
    title = request.form['title']
    # Add to pretend DB
    if title in MOVIES:
        flash('Movie already exists!', 'error')
    else:
        MOVIES.add(title)
        flash('Movie added!', 'success')
    return redirect('/movies')
