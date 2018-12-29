from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login_out.login'


def register_blueprints(app):
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.login_out import bp as login_out_bp
    app.register_blueprint(login_out_bp)


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    register_blueprints(app)

    return app
