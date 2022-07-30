from unicodedata import name

from flask import Flask, current_app, g, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello flask"

@app.route("/hello/<name>", methods=["GET", "POST"])
def hello(name):
    return f"Hello, {name}!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

with app.test_request_context("/users?updated=1"):
    print(request.args.get("updated"))
    # print(url_for("index"))
    # print(url_for("show_name", name="ichiro", page="1"))
    

# アプリケーションコンテキスト
# アプリケーションコンテキストを取得してスタックへpush
ctx = app.app_context()
ctx.push()

# current_appにアクセス可能
print(current_app.name)

