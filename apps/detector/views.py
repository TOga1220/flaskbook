from flask import Blueprint, redirect, render_template, url_for

from apps.app import db
from apps.crud.models import User
from apps.detector.models import UserImage

# Blueprintでcrudアプリを生成
dt = Blueprint(
    "detector",
    __name__,
    template_folder="templates",
)

# indexエンドポイントを作成し、index.htmlを返す
@dt.route("/")
def index():
    user_images = (
        db.session.query(User, UserImage)
        .join(UserImage)
        .filter(User.id == UserImage.user_id)
        .all()
    )
    return render_template("detector/index.html", user_images=user_images)

