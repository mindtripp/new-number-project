from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
  
    number = random.randint(1, 100)

    return render_template("index.html", number=number)

@app.route("/", methods=["POST"])
def guess():

    guess = int(request.form.get("guess"))

    number = int(request.form.get("number"))

    if guess > number:
        result = "Too high"
    elif guess < number:
        result = "Too low"
    else:
        result = "Correct"
  
    return render_template("index.html", result=result, guess=guess, number=number)
