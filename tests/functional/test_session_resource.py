import json
from app.climbing.models import Session


def test_session_get_resource(logedInClient, dummyData):
    """
    GIVEN /api/session/<int:session_id> endpoint
    WHEN the endpoint is hit
    THEN return specific session
    """
    token = logedInClient.post('/wctoken').json['access_token']
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = logedInClient.get('/api/session/1', headers=headers)
    session1_json = response.get_json()['session']
    session_from_db = Session.query.get(1)
    assert response.is_json
    assert session1_json['id'] == session_from_db.id
    assert session1_json['type'] == session_from_db.type


def test_session_post_resource(logedInClient, dummyData):
    """
    GIVEN /api/session/<int:session_id> endpoint
    WHEN the endpoint is hit
    THEN return specific session
    """
    token = logedInClient.post('/wctoken').json['access_token']
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = {
        'type': 'ropes',
        'user': '1',
        'routes': [
            {
                'completion': 'onsight',
                'grade': '5.10',
                'letter': 'a',
                'type': 'lead',
                'falls': '0',
            }
        ]
    }
    response = logedInClient.post(
        '/api/session',
        headers=headers,
        data=json.dumps(data)
    )
    new_session = Session.query.get(2)
    assert response.is_json
    assert new_session.id == 2
    assert new_session.user.id == 1
    assert new_session.type == 'ropes'
    assert len(new_session.routes.all()) == 1
