import os
from flask import Flask, render_template
from dotenv import load_dotenv
from enums import MAX_SCORE, NAME, students

load_dotenv()

app =Flask(__name__)


@app.route('/')
def welcom():
    return render_template("index.html")

@app.route('/bace')
def bace():
    return render_template("bace.html", title="Python course")

@app.route("/context")
def context():
    context = {
        "title" : "Python Course",
        "name" : NAME,
        "max_score" : MAX_SCORE,
        "students" : students
    }
    return render_template("context.html", **context)


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))