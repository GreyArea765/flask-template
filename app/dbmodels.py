from app import db, login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


# Callback to alllow flask_login to retrieve user objects from database.
@login.user_loader
def load_user(id):
    # Flask passes id's as String so we cast to int.
    return User.query.get(int(id))


# Class to represent the user table.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User {}> <Password {}>'.format(self.username,
            self.password)


    def check_password(self, password):
        return check_password_hash(self.password, password)