
from . import main
from flask import render_template



@main.route('/')
def index():
  title = 'Welcome to Pitch Board | Make the most out of your minute'
  return render_template('index.html', title = title)