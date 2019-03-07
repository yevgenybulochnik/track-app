

def test_user_resource(logedInClient):
    """
    GIVEN /api/users endpoint
    WHEN the endpoint is hit
    THEN return a list of serialized users
    """
    token = logedInClient.post('/wctoken').json['access_token']
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = logedInClient.get('/api/users', headers=headers)
    users = response.json['users']
    assert response.is_json
    assert len(users) == 1
    assert 'email' in users[0]
    assert 'id' in users[0]
    assert 'role' in users[0]


def test_user_resource_unauth(logedInClient):
    """
    GIVEN /api/users endpoint
    WHEN unauthorized use
    THEN return unauthorized
    """
    response = logedInClient.get('/api/users')
    assert response.is_json
    assert response.status_code == 401
    assert response.json['msg'] == 'Missing Authorization Header'
