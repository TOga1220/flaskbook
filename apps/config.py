from pathlib import Path

basedir = Path(__file__).parent

## BaseConfigクラスを作成する
class BaseConfig:
    SECRET_KEY = "aaa"
    WTF_CSRF_SECRET_KEY = "bbb"
    
#BaseConfigクラスを継承してLocalConfigクラスを作成する
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///local.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///testing.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
# config辞書にマッピング
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}

    
    