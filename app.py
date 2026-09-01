from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":
        text = request.form["text"]
        action = request.form["action"]

        if action == "uppercase":
            result = text.upper()

        elif action == "lowercase":
            result = text.lower()

        elif action == "capitalize":
            result = text.capitalize()

        elif action == "remove_spaces":
            result = text.replace(" ", "")

    return render_template("index.html", result=result)


app.run(debug=True)