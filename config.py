import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='12334'
    # os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL ='MurimiLudwig@gmail.com'
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ludwig:pass@localhost/pitch'
    
# class Testconfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ludwig:pass@localhost/pitch'
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ludwig:pass@localhost/pitch'
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':Testconfig
}