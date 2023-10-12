from flask import Flask

app =Flask(__name__)


@app.route('/')
def welcom():
    return "This is the main page of Arina"


if __name__ == "__main__":
    app.run(debug=True)