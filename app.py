from flask import Flask, render_template, request, redirect, url_for, session
import random, string

app = Flask(__name__)
app.secret_key = ""


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        length = int(request.form["length"])  # get the length from form
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        return render_template("generate.html", password=password)
    return render_template("generate.html", password=None)
