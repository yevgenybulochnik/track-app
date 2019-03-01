from datetime import datetime
from app.database import db, Model, Column, relationship


class Session(Model):
    __tablename__ = 'sessions'
    id = Column(db.Integer, primary_key=True)
    user_id = Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = Column(db.DateTime, default=datetime.utcnow)
    type = Column(db.String(32))
    routes = relationship('Route', backref='session', lazy='dynamic')


class Route(Model):
    __tablename__ = 'routes'
    id = Column(db.Integer, primary_key=True)
    session_id = Column(db.Integer, db.ForeignKey('sessions.id'))
    timestamp = Column(db.DateTime)
    type = Column(db.String(32))
    grade = Column(db.String(32))
    letter = Column(db.String(32))
    completion = Column(db.String(32))
    falls = Column(db.String(32))
