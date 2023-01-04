from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "keepitsecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES = "responses"


@app.route("/")
def show_survey_start():
    """Allow user to select a survey"""

    return render_template("start_survey.html", survey=survey)


@app.route("/begin", methods=["POST"])
def start_survey():
    session[RESPONSES] = []

    return redirect("/questions/0")


@app.route("/answer", methods=["POST"])
def handle_question():
    choice = request.form['answer']

    responses = session[RESPONSES]
    responses.append(choice)
    session[RESPONSES] = responses

    if (len(responses) == len(survey.questions)):
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/questions/<int:question_id>")
def show_questions(question_id):
    """Show current question"""
    responses = session.get(RESPONSES)

    if (responses is None):
        return redirect("/")

    if (len(responses)) == len(survey.questions):
        return redirect("/complete")

    if (len(responses) != question_id):
        flash(f"Invalid question id: {question_id}.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[question_id]
    return render_template("questions.html", question_num=question_id, question=question)


@app.route("/complete")
def complete():
    return render_template("completion.html")
