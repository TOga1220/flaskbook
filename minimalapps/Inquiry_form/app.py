# 問い合わせフォーム
## 「問い合わせフォーム」画面を表示 get
## 問い合わせ内容をメールで送信 post
## 「問い合わせ完了」画面へリダイレクト redirect
## 「問い合わせ完了」画面を表示

import logging
import os

from email_validator import EmailNotValidError, validate_email
from flask import (Flask, current_app, flash, g, make_response, redirect,
                   render_template, request, session, url_for)
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

app = Flask(__name__)

# SECRET_KEYを設定
app.config["SECRET_KEY"] = "test_key"

# ロギングレベルを設定する
app.logger.setLevel(logging.DEBUG)

# リダイレクトを中断しないようにする
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
# DebugToolbarExtensionにアプリケーションをセットする
toolbar = DebugToolbarExtension(app)

# Mailクラスのコンフィグを追加
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

# flask-mailを拡張する
mail = Mail(app)

@app.route("/contact")
def contact():
    # レスポンスオブジェクトを取得する
    response = make_response(render_template("contact.html"))
    
    # クッキーを設定する
    response.set_cookie("flaskbook key", "flaskbook value")
    
    # セッションを設定する
    session["username"] = "ichiro"
    
    return response

    # return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        ## フォームの値を取得する
        username=request.form['username']
        email=request.form['email']
        description=request.form['description']
        
        # 入力チェック
        is_valid = True
        
        if not username:
            flash("ユーザー名は必須")
            is_valid = False
        
        if not email:
            flash("emailは必須")
            is_valid = False
  
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("正しいメールアドレス形式で入力してください")
            is_valid = False
        
        if not description:
            flash("問い合わせ内容は必須")
            is_valid = False
            
        if not is_valid:
            return redirect(url_for("contact"))
         
        ## メールを送る        
        send_email(
            email,
            "問い合わせありがとうございました。",
            "contact_mail",
            username=username,
            description=description,
        )
        
        ## contactエンドポイントへリダイレクトする
        flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございました。")
        return  redirect(url_for("contact_complete"))
    
    return render_template("contact_complete.html")

def send_email(to, subject, template, **kwargs):
    """メール送信関数"""
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)
    

# アプリケーションコンテキスト
# アプリケーションコンテキストを取得してスタックへpush
ctx = app.app_context()
ctx.push()

# current_appにアクセス可能
print(current_app.name)

