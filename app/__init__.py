from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()



def create_app(config_name):
  
  app = Flask(__name__)



  # initialize extensions
  bootstrap.init_app(app)


  return app