from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
  username = StringField('Enter your username', validators=[DataRequired('Username is required')])
  email = StringField('Enter email address', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
  password_confirm = PasswordField('Confirm password', validators=[DataRequired()])
  submit = SubmitField('Sign Up')