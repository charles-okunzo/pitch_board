from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
  username = StringField('Enter new username', validators=[DataRequired()])
  bio = TextAreaField('Enter bio', validators=[DataRequired()])
  submit = SubmitField('Update')


class PitchForm(FlaskForm):
  title = StringField('Pitch title:', validators=[DataRequired()])
  category = SelectField('Category:', choices=[('Pickup lines'), ('Technology'), ('Innovation'), ('Promotion')], validators=[DataRequired()])
  pitch = TextAreaField('Your Pitch:', validators=[DataRequired()])
  submit = SubmitField('Post')


class CommentForm(FlaskForm):
  comment = TextAreaField('Your Comment:', validators=[DataRequired()])
  submit = SubmitField('Post')