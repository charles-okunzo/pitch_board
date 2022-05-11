import os
from dotenv import load_dotenv

load_dotenv()


class Config():
  # SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:okunzo254@localhost/pitch_board'
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SECRET_KEY=os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST='app/static/photos'

  MAIL_SERVER='smtp.googlemail.com'
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
  if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://',1)





class DevConfig(Config):
  DEBUG = True



config_options = {
  'production': ProdConfig,
  'development': DevConfig
}