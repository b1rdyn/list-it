from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/mylists")
def mylists():
    return render_template("mylists.html")

@app.route("/popularlists")
def popularlists():
    return render_template("popularlists.html")