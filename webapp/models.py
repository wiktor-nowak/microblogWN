from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from webapp import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Pierwszy argoment to nazwa klasy budującej tabelę SQL,
    # do której się odnosi relacja ( a więc duże P )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User --> {self.username}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # user.id w tym przypadku user to tabela w bazie danych zbudowanej
    # przez Alchemie na bazie klasy User przez duże U... O_O

    def __repr__(self):
        return f'<Post body: {self.body}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
