from flask import Flask

app = Flask(__name__)

@app.route("/unlimited")
def unlimited():
    return "Unlimited! Let's Go!"

@app.route("/limited")
def limited():
    return "Limited, don't use me"



