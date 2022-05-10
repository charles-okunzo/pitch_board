from enum import unique

from sqlalchemy import ForeignKey
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin, db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255), nullable = False, unique = True)
  email = db.Column(db.String(255), unique = True, nullable = False)
  pass_secure = db.Column(db.String(128), unique = True, nullable = False)
  bio = db.Column(db.String())
  profile_pic = db.Column(db.String(255), nullable = False)
  pitches = db.relationship("Pitch", backref = 'pitch', lazy = 'dynamic')
  upvotes = db.relationship('Upvote', backref = 'upvote', lazy = 'dynamic')
  comments = db.relationship('Comment', backref = 'comment', lazy = 'dynamic')
  downvotes = db.relationship('Downvotes', backref = 'downvote', lazy = 'dynamic')


  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)


  def verify_password(self, password):
    return check_password_hash(self.pass_secure, password)


  def __repr__(self):
      return f"User {self.username}"


class Pitch(db.Model):
  __tablename__='pitches'

  id = db.Column(db.Integer, primary_key=True)
  pitch = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  category = db.Column(db.String)
  upvotes = db.relationship('Upvote', backref='upvote', lazy = 'dynamic')
  downvotes = db.relationship('Downvote', backref='downvote', lazy = 'dynamic')
  comments = db.relationship('Comment', backref = 'comment', lazy = 'dinamic')

  def save_pitch(self):
    db.session.add(self)
    db.session.commit()


  def __repr__(self) -> str:
      return f'User {self.pitch} {self.category}'


class Comment(db.Model):
  __tablename__='comments'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  comment = db.Column(db.String)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

  def save_comment(self):
    db.session.add(self)
    db.session.commit()
  

  def __repr__(self):
    return f'User {self.title} {self.comment}'


class Upvote(db.Model):
  __tablename__='upvotes'

  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


  def save_upvote(self):
    db.session.add(self)
    db.session.commit()


class Downvote(db.Model):
  __tablename__='downvotes'

  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


  def save_downvote(self):
    db.session.add(self)
    db.session.commit()