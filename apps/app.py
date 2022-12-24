from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from apps.config import config

# インスタンス化
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()

# login_view属性に未ログイン時リダイレクトするエンドポイントを指定
login_manager.login_view = "auth.signup"
# login_message属性にログイン後表示するメッセージを指定
login_manager.login_message = "ログイン！"

def create_app(config_key):
    app = Flask(__name__)
    
    # アプリのコンフィグ設定をする
    app.config.from_object(config[config_key])  
    
    db.init_app(app)
    # MIGRATEとアプリを連携する
    Migrate(app, db)
    
    # アプリと連携
    csrf.init_app(app)
    login_manager.init_app(app)
    
    # crudパッケージからviewsをimportする
    # これから作成するauthパッケージからviewsをimportする
    from apps.auth import views as auth_views
    from apps.crud import views as crud_views
    # これから作成するdetectorパッケージからviewsをimportする
    from apps.detector import views as dt_views

    # register_blueprintを使用しviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    
    # register_blueprintを使用しviewsのauthをアプリへ登録する
    app.register_blueprint(auth_views.auth, url_prefix="/auth")
    
    # register_blueprintを使用しviewsのdetectorをアプリへ登録する
    app.register_blueprint(dt_views.dt)
    
    return app

