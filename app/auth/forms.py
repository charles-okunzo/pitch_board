from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
  username = StringField('Enter your username', validators=[DataRequired('Username is required')])
  email = StringField('Enter email address', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
  password_confirm = PasswordField('Confirm password', validators=[DataRequired()])
  submit = SubmitField('Sign Up')


  def validate_username(self, data_field):
    if User.query.filter_by(username = data_field.data).first():
      raise AttributeError('An account with this email exists')


  def validate_email(self, data_field):
    if User.query.filter_by(email = data_field.data).first():
      raise AttributeError('Username exists')