import pytest
from flask_jwt_extended import decode_token


def test_wctoken(client, database):
    """
    GIVEN a user is loged in
    WHEN the wctoken endpoint is hit
    THEN a jwt token is generated
    """
    data = {
        'email': 'user1@test.com',
        'password': 'password1'
    }
    client.post('/login', data=data)
    response = client.post('/wctoken')
    assert response.is_json
    assert 'access_token' in response.json
    assert decode_token(response.json['access_token'])['identity'] == 1


def test_wctoken_unauth(client, database):
    """
    GIVEN a direct request
    WHEN wctoken endpoint is hit
    THEN a 302 redirect to login should occur
    """
    response = client.post('/wctoken')
    assert response.status_code == 302
