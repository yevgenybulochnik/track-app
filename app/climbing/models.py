from datetime import datetime
from app import db


class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    type = db.Column(db.String(32))
    routes = db.relationship('Route', backref='session', lazy='dynamic')


class Route(db.Model):
    __tablename__ = 'routes'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    timestamp = db.Column(db.DateTime)
    grade = db.Column(db.String(32))
    letter = db.Column(db.String(32))
    completion = db.Column(db.String(32))
    falls = db.Column(db.String(32))
