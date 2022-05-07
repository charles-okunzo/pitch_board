from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()



def create_app(config_name):
  
  app = Flask(__name__)

  #configurations
  from config import config_options
  app.config[config_options[config_name]]

  #registering blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)



  # initialize extensions
  bootstrap.init_app(app)


  return app