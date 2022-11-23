from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from apps.config import config
from apps.crud import views as cruds_view
from apps.crud.models import db

csrf = CSRFProtect()

def create_app(config_key):
    app = Flask(__name__)
    
    # アプリのコンフィグ設定をする
    # config_keyにマッチする環境のconfigクラスを読み込む
    app.config.from_object(config[config_key])  
    
    csrf.init_app(app)
    
    # SQLALCHEMYと連携する
    db.init_app(app)
    # MIGRATEアプリを連携する
    Migrate(app, db)
     
    # register_blueprintを使用しviewsのcrudをアプリへ登録する
    app.register_blueprint(cruds_view.crud, url_prefix="/crud")
    
    return app

