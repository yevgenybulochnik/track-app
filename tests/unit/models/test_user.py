import pytest
from app.models import User


def test_new_user(client, database):
    """
    GIVEN a User Model
    WHEN a new User is created
    THEN check the email, hashed_password,
    """
    user = User(email='user2@test.com', password='password2')
    database.session.add(user)
    database.session.commit()

    assert user.email == 'user2@test.com'
    assert user.id >= 2
    assert user.verify_password('password2')
    with pytest.raises(AttributeError):
        assert user.password
