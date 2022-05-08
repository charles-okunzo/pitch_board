# import os
from dotenv import load_dotenv

load_dotenv()


class Config():
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:okunzo254@localhost/pitch_board'
  SQLALCHEMY_TRACK_MODIFICATIONS=False



class ProdConfig(Config):
  pass



class DevConfig(Config):
  DEBUG = True



config_options = {
  'production': ProdConfig,
  'development': DevConfig
}