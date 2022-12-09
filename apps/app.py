from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from apps.auth import views as auths_view
from apps.config import config
from apps.crud import views as cruds_view
from apps.crud.models import db, login_maneger
from apps.detector import views as dt_views

# インスタンス化
csrf = CSRFProtect()

# login_view属性に未ログイン時リダイレクトするエンドポイントを指定
login_maneger.login_view = "auth.signup"
# login_message属性にログイン後表示するメッセージを指定
login_maneger.login_message = "ログイン！"

def create_app(config_key):
    app = Flask(__name__)
    
    # アプリのコンフィグ設定をする
    app.config.from_object(config[config_key])  
    
    # アプリと連携
    csrf.init_app(app)
    login_maneger.init_app(app)
    db.init_app(app)
    
    # MIGRATEアプリを連携する
    Migrate(app, db)
     
    # register_blueprintを使用しviewsのcrudをアプリへ登録する
    app.register_blueprint(cruds_view.crud, url_prefix="/crud")
    
    # register_blueprintを使用しviewsのauthをアプリへ登録する
    app.register_blueprint(auths_view.auth, url_prefix="/auth")
    
    # register_blueprintを使用しviewsのdetectorをアプリへ登録する
    app.register_blueprint(dt_views.dt)
    
    return app

