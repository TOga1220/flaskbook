from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello flask"

@app.route("/hello/<name>", methods=["GET", "POST"])
def hello(name):
    return f"Hello, {name}!"

# @app.route("/name/<name>")
# def show_name(name):
#     return render_template("index.html", name=name)

with app.test_request_context():
    print(url_for("index"))
    # print(url_for("show_name"))

    