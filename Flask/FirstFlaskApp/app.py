from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home_page():
    html = "<html><body> <h1>Home Page</h1> <p>Welcome to my simple app!</p><a href='/hello'>Go to hello page</a></body></html>"
    return html


@app.route('/hello')
def say_hello():
    html = "<html><body><h1>Hello there!</h1><a href='/'>Go to home page</a></body></html>"
    return html


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
