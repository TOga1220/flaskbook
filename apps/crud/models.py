from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db=SQLAlchemy()

class User(db.Model):
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
