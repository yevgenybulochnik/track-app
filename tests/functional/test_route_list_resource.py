from app.climbing.models import Route


def test_route_list_resource(logedInClient, dummyData):
    """
    GIVEN /api/routes endpoint
    WHEN the endpoint is hit
    THEN return list of serialized routes
    """
    response = logedInClient.get('/api/routes')
    routes = response.get_json()['routes']
    route1_json = routes[0]
    route_from_db = Route.query.get(1)
    assert response.is_json
    assert len(routes) >= 1
    assert route1_json['id'] == route_from_db.id
    assert route1_json['type'] == route_from_db.type
    assert route1_json['completion'] == route_from_db.completion
    assert route1_json['session'] == route_from_db.session.id
