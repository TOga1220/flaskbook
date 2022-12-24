from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required

from apps.app import db
from apps.crud.forms import UserForm
from apps.crud.models import User

# Blueprintでcrudアプリを生成
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# indexエンドポイントを作成し、index.htmlを返す
@crud.route("/")
@ login_required
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
@ login_required
def sql():
    db.session.query(User).all()
    return "コンソールログを確認してください"
    
@crud.route("/users/new", methods = ["GET", "POST"])
@ login_required
def create_user():
    # UserFormをインスタンス化する
    form = UserForm()
    # フォーム値をvalidateする
    if form.validate_on_submit():
        #ユーザ作成
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data,
        )
        # ユーザを追加してコミットする
        db.session.add(user)
        db.session.commit()
        # ユーザの一覧画面へリダイレクトする
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)
    
@crud.route("/users")
@ login_required
def users():
    users = User.query.all()
    return render_template("crud/index.html", users=users)      

# ユーザ編集エンドポイント
@crud.route("/users/<user_id>", methods=["GET", "POST"])
@ login_required
def edit_user(user_id):
    form = UserForm()
    
    user = User.query.filter_by(id=user_id).first()
    
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data    
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    
    # GETの場合はhtmlを返す
    return render_template("crud/edit.html", user=user, form=form)

# ユーザ削除エンドポイント
@crud.route("/users/<user_id>/delete", methods=["POST"])
@ login_required
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))
