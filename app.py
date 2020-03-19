from flask import Flask, request, jsonify, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

import surveys


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

responses = []


@app.route("/")
def populate_survey():
    """Gets the user's survey responses and appends to global response var"""


@app.route("/surveys")
def get_responses():
    """Gets the user's survey responses and appends to global response var"""

    survey_title = surveys.satisfaction_survey.title
    survey_instructions = surveys.satisfaction_survey.instructions
    survey_questions = surveys.satisfaction_survey.questions

    return render_template("base.html", survey_title=survey_title,
                           survey_instructions=survey_instructions,
                           survey_questions=survey_questions)
