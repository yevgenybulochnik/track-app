from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_apispec import FlaskApiSpec

from app.database import db

from config import Config

migrate = Migrate()
jwt = JWTManager()
login = LoginManager()
login.login_view = 'auth.login'
ma = Marshmallow()
api = Api()


def register_blueprints(app):
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    register_blueprints(app)
    api.init_app(app)

    return app
