import pytest
from app import create_app
from app.database import db
from app.main.models import User
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False


@pytest.fixture
def client():
    app = create_app(TestConfig)
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture
def database():
    db.create_all()

    user1 = User(email='user1@test.com', password='password1')

    db.session.add(user1)
    db.session.commit()

    yield db

    db.drop_all()
