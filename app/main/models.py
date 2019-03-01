from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.database import db, Model, Column, relationship


class Role(Model):
    __tablename__ = 'roles'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(64), unique=True)
    users = relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'<Role {self.name}, {self.id}>'


class User(Model, UserMixin):
    __tablename__ = 'users'
    id = Column(db.Integer, primary_key=True)
    email = Column(db.String(64), index=True, unique=True)
    password_hash = Column(db.String(128))
    role_id = Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'<User {self.email}, {self.id}>'

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
