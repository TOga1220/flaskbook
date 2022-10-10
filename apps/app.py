import os
from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from apps.crud import views as cruds_view

# SQLAlchemyをインスタンス化する
db=SQLAlchemy()

base_dir = Path(__file__).parent.parent
SECRET_KEY = "key"
SQLALCHEMY_DATABASE_URI = "sqlite:///local.sqlite"


def create_app():
    app = Flask(__name__)

    # アプリのコンフィグ設定をする
    app.config.from_mapping(
        SECRET_KEY = SECRET_KEY,
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    # SQLALCHEMYと連携する
    db.init_app(app)
    # MIGRATEアプリを連携する
    Migrate(app, db)
     
    # register_blueprintを使用しviewsのcrudをアプリへ登録する
    app.register_blueprint(cruds_view.crud, url_prefix="/crud")
    
    return app

