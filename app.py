
from flask import Flask, render_template, request, redirect, url_for, session
import random, string

app = Flask(__name__)
app.secret_key = "why_u_looking_at_secerts" 

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


if __name__ == "__main__":
    app.run(debug=True, port=8080)
