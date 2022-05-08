from app.models import User
from . import main
from flask import render_template, abort



@main.route('/')
def index():
  title = 'Welcome to Pitch Board | Make the most out of your minute'
  return render_template('index.html', title = title)


@main.route('/profile/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)

  return render_template('profile/profile.html', user = user)