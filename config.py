import os
from dotenv import load_dotenv

load_dotenv()


class Config():
  SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SECRET_KEY=os.environ.get('SECRET_KEY')



class ProdConfig(Config):
  pass



class DevConfig(Config):
  DEBUG = True



config_options = {
  'production': ProdConfig,
  'development': DevConfig
}