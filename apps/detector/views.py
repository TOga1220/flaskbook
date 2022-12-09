from flask import Blueprint, redirect, render_template, url_for

# Blueprintでcrudアプリを生成
dt = Blueprint(
    "detector",
    __name__,
    template_folder="templates",
)

# indexエンドポイントを作成し、index.htmlを返す
@dt.route("/")
def index():
    return render_template("detector/index.html")

