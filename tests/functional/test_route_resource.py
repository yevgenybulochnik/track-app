import json
from app.climbing.models import Route


def test_route_get_resource(logedInClient, dummyData):
    """
    GIVEN /api/route/<int:route_id> endpoint
    WHEN the endpoint is hit
    THEN return specific route
    """
    token = logedInClient.post('/wctoken').json['access_token']
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = logedInClient.get('/api/route/1', headers=headers)
    route1_json = response.get_json()['route']
    route_from_db = Route.query.get(1)
    assert response.is_json
    assert route1_json['id'] == route_from_db.id
    assert route1_json['type'] == route_from_db.type
    assert route1_json['completion'] == route_from_db.completion
    assert route1_json['session'] == route_from_db.session.id


def test_route_put_resource(logedInClient, dummyData):
    """
    GIVEN /api/route/<int:route_id> endpoint
    WHEN the endpoint is hit
    THEN return specific route
    """
    token = logedInClient.post('/wctoken').json['access_token']
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = {
        'completion': 'onsight',
        'grade': '5.11',
        'letter': 'd'
    }
    response = logedInClient.put(
        '/api/route/1',
        headers=headers,
        data=json.dumps(data)
    )
    updated_route = Route.query.get(1)
    assert response.is_json
    assert updated_route.completion == 'onsight'
    assert updated_route.grade == '5.11'
    assert updated_route.letter == 'd'
    assert 'status' in response.get_json()
    assert 'Updated route' in response.get_json()['status']
