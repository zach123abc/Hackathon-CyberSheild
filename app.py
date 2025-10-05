from flask import Flask, render_template, request, redirect, url_for, session
import os
import random, string

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "default_dev_key")

@app.route("/")
def home():
    return redirect(url_for("menu"))

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        length = int(request.form["length"])
        characters = ""

        if "letters" in request.form:
            characters += string.ascii_letters
        if "numbers" in request.form:
            characters += string.digits
        if "symbols" in request.form:
            characters += string.punctuation

        if not characters:
            password = "Please select at least one character type."
        else:
            password = "".join(random.choice(characters) for _ in range(length))

        return render_template("generate.html", password=password)

    return render_template("generate.html", password=None)


@app.route("/password-safety")
def password_safety():
    return render_template("password_safety.html")


@app.route("/scam-awareness")
def scam_awareness():
    return render_template("scam_awareness.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
