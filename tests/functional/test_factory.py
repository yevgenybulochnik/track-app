from app import create_app
from config import Config


def test_config():
    """
    GIVEN Config object
    WHEN app is initialized
    THEN default configs are present
    """
    app = create_app(Config)
    assert app.config['SECRET_KEY'] == 'you-will-never-guess'
    assert not app.config['SQLALCHEMY_TRACK_MODIFICATIONS']
