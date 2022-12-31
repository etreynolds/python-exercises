from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

"""Responds to 4 different routes. Each route does a math operation with two numbers, 
a and b, which will be passed in as URL GET-style params

For example, a URL like http://localhost:5000/add?a=10&b=20 should 
return a string response of exactly 30.
"""


@app.route("/add")
def add_nums():
    """Add a and b nums"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)


@app.route("/sub")
def sub_nums():
    """Subtract a and b nums"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)


@app.route("/mult")
def mult_nums():
    """Multiply a and b nums"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)


@app.route("/div")
def div_nums():
    """Divide a and b nums"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)


# FURTHER STUDY

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<operation>")
def do_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operation](a, b)
    return str(result)
