

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
    assert response.is_json
    assert len(response.json) == 1
    assert 'email' in response.json[0]
    assert 'id' in response.json[0]
    assert 'role' in response.json[0]


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
