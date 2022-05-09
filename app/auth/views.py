
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user
from .forms import RegistrationForm, LoginForm
from ..models import User
from .. import db
from . import auth
from ..email import mail_message


@auth.route('/login', methods=['GET', 'POST'])
def login():
  title = 'Pitch Board | Log In'
  login_form = LoginForm()
  if  login_form.validate_on_submit():
    user = User.query.filter_by(email = login_form.email.data).first()
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user, login_form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or password')

  return render_template('auth/login.html', login_form = login_form, title = title)



@auth.route('/register', methods = ['GET', 'POST'])
def register():
  title = 'Pitch Board | Sign Up'
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username = form.username.data, email = form.email.data, password = form.password.data)
    db.session.add(user)
    db.session.commit()

    mail_message('Welcome to PitchBoard!', 'email/welcome_user', user.email, user = user)


    return redirect(url_for('auth.login'))

  return render_template('auth/register.html', registration_form = form, title = title)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))