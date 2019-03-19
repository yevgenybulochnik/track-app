import os
import json
from flask import Flask, url_for
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

from app.database import db

from config import Config

migrate = Migrate()
jwt = JWTManager()
login = LoginManager()
login.login_view = 'auth.login'
ma = Marshmallow()


def register_blueprints(app):
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from app.climbing import bp as climbing_bp
    app.register_blueprint(climbing_bp)
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    register_blueprints(app)

    def include_asset(asset, type):
        static_path = app.static_folder
        manifest_file = os.path.join(static_path, 'assets', 'manifest.json')
        try:
            with open(manifest_file) as f:
                manifest = json.loads(f.read())
        except IOError:
            raise IOError('Manifest not found')
        bp, asset_name = asset.split('/')
        if type == 'js':
            asset_key = '/'.join([bp, asset_name, f'{asset_name}.js'])
            asset_hash = manifest.get(asset_key)
            return f'<script src="static/assets/{asset_hash}"></script>'
        if type == 'css':
            asset_key = '/'.join([bp, asset_name, f'{asset_name}.css'])
            asset_hash = manifest.get(asset_key)
            return f'<link rel="stylesheet" href="static/assets/{asset_hash}">'

    app.add_template_global(include_asset)

    return app
