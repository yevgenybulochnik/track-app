from app.models import User
from app.climbing.models import Session, Route


def test_session(client, database):
    """
    GIVEN a Session Model
    WHEN a new Session is created
    THEN check associated user, timestamp, session type and associated routes
    """
    user = User.query.get(1)
    route = Route(
        type='lead',
        grade='5.10',
        letter='a',
        completion='redpoint',
        falls='1'
    )
    climbing_session = Session(type='ropes', user=user, routes=[route])
    database.session.add(climbing_session)
    database.session.commit()
    assert climbing_session.id
    assert climbing_session.user == user
    assert climbing_session.type == 'ropes'
    assert climbing_session.timestamp
    assert climbing_session.routes.all()[0] == route
    assert user.sessions.all()[0] == climbing_session
