from flask import Flask, request, jsonify, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

import surveys


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

RESPONSES_KEY = "responses"


@app.route("/survey")
def start_survey():
    """Gets the user's survey responses and appends to global response var"""

    session[RESPONSES_KEY] = []

    survey_title = surveys.satisfaction_survey.title
    survey_instructions = surveys.satisfaction_survey.instructions

    return render_template("base.html", survey_title=survey_title,
                           survey_instructions=survey_instructions)


@app.route("/questions/<int:question_num>")
def populate_questions(question_num):
    """Gets the user's survey responses and appends to global response var"""

    survey_question = surveys.satisfaction_survey.questions[question_num]
    return render_template("question.html", survey_question=survey_question)


@app.route("/answer", methods=["POST"])
def post_answer():
    """Gets the user's survey responses and appends to global response var"""

    answer = request.form("answer")

    responses = session[RESPONSES_KEY]
    responses.append(answer)
    session[RESPONSES_KEY] = responses

    if (len(responses) == len(surveys.satisfaction_survey.questions)):

        return redirect("/complete")

    return redirect(f"/questions/{len(responses)}")


@app.route("/complete")
def complete_survey():
    """Stuff"""

    return render_template("complete.html")
