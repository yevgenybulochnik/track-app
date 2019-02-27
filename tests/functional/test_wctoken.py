import pytest
import json
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
    data = json.loads(response.data)
    identity = decode_token(data['access_token'])['identity']
    assert response.is_json
    assert data['access_token']
    assert identity == 1


def test_wctoken_unauth(client, database):
    """
    GIVEN a direct request
    WHEN wctoken endpoint is hit
    THEN a 302 redirect to login should occur
    """
    response = client.post('/wctoken')
    assert response.status_code == 302
