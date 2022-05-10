
from crypt import methods
from app import db, photos
from flask_login import current_user, login_required
from app.main.forms import UpdateProfile, PitchForm, CommentForm
from app.models import Comment, Pitch, User
from . import main
from flask import redirect, render_template, abort, request, url_for



@main.route('/')
def index():
  title = 'Welcome to Pitch Board | Make the most out of your minute'

  pitches = Pitch.query.all()
  pickup = Pitch.query.filter_by(category = 'Pickup lines').all()
  technology = Pitch.query.filter_by(category ='Technology').all()
  innovation = Pitch.query.filter_by(category = 'Innovation').all()
  promotion = Pitch.query.filter_by(category='Promotion').all()
  return render_template('index.html', title = title, pitches = pitches, pickup = pickup, technology = technology, innovation = innovation, promotion = promotion)


@main.route('/profile/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)

  return render_template('profile/profile.html', user = user)


@main.route('/profile/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)

  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data
    user.username = form.username.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('main.profile', uname = user.username))

  return render_template('profile/update.html',form = form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic = path
    db.session.commit()
  return redirect(url_for('main.profile', uname = uname))


@main.route('/create/pitch', methods=['POST', 'GET'])
@login_required
def new_pitch():
  form  = PitchForm()
  if form.validate_on_submit():
    title = form.title.data
    category = form.category.data
    pitch = form.pitch.data

    new_pitch_obj = Pitch(title=title, category=category,pitch=pitch, user_id=current_user._get_current_object().id )
    new_pitch_obj.save_pitch()
    return redirect(url_for('main.index'))

  return render_template('pitchform.html', form = form)


@main.route('/new/comment/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def new_comment(pitch_id):
  comments = Comment.query.all()
  form = CommentForm()
  if form.validate_on_submit():
    comment = form.comment.data

    new_comment_obj = Comment(comment=comment, pitch_id=pitch_id, user_id = current_user._get_current_object().id)

    new_comment_obj.save_comment()
    return redirect(url_for('main.new_comment', pitch_id=pitch_id))

  return render_template('commentform.html', form=form, comments=comments)