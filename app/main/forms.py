from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
  username = StringField('Enter new username', validators=[DataRequired()])
  bio = TextAreaField('Enter bio', validators=[DataRequired()])
  submit = SubmitField('Update')