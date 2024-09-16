from pathlib import Path
import os

basedir = Path(__file__).parent.parent

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')
    UPLOAD_FOLDER = str(Path(basedir, 'apps', 'lottie'))

class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir / "local.sqlite"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir / "testing.sqlite"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'local': LocalConfig
}