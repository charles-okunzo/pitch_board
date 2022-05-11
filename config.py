import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config():
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
  if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://')
  SQLALCHEMY_TRACK_MODIFICATIONS=True
  SECRET_KEY=os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST='app/static/photos'

  MAIL_SERVER='smtp.googlemail.com'
  MAIL_PORT=465
  MAIL_USE_TLS=True
  MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
  if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://')





class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
  DEBUG = True



config_options = {
  'production': ProdConfig,
  'development': DevConfig
}