import pytest
from app import create_app
from app.database import db
from app.main.models import User
from app.climbing.models import Session, Route
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


@pytest.fixture
def logedInClient(client, database):
    data = {
        'email': 'user1@test.com',
        'password': 'password1'
    }
    client.post('/login', data=data)

    yield client


@pytest.fixture
def dummyData(database):
    user1 = User.query.get(1)

    route1 = Route(
        type='lead',
        grade='5.10',
        letter='a',
        completion='onsight',
        falls='0'
    )

    route2 = Route(
        type='top rope',
        grade='5.9',
        letter='',
        completion='redpoint',
        falls='0'
    )

    session1 = Session(
        user=user1,
        type='ropes',
        routes=[route1, route2]
    )
    database.session.add(session1)
    database.session.commit()
