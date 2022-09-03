from flask import Flask

from apps.crud import views as cruds_view


def create_app():
    app = Flask(__name__)
    
    # register_blueprintを使用しviewsのcrudをアプリへ登録する
    app.register_blueprint(cruds_view.crud, url_prefix="/crud")
    
    return app

