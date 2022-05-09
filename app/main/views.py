
from flask_login import login_required
from app.main.forms import UpdateProfile
from app.models import User
from . import main
from flask import redirect, render_template, abort, url_for



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


@main.route('/profile/unsme/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)

  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data
    user.username = form.username.data

    return redirect(url_for('main.profile', uname = user.username))

  return render_template('profile/update.html',form = form)
