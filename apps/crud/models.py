from datetime import datetime

from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

# インスタンス化
db=SQLAlchemy()
login_maneger = LoginManager()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
     
     
    # パスワードリセットするためのプロパティ
    @property
    def password(self):
        raise AttributeError("読み取り不可")
    
    # PWをセットするためのsetter関数でハッシュ化したPWをセットする。
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    # パスワードをチェックする
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # メールアドレス重複をチェックする
    def is_duplicate_email(self):
        return User.query.filter_by(email = self.email).first() is not None

# ログインしているユーザ情報を取得する
@login_maneger.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
    
    
