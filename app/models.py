from flask.ext.login import LoginManager, UserMixin
from app import db, lm


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False) #ids for oAuth
    nickname = db.Column(db.String(64))
    email = db.Column(db.String(64))


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))