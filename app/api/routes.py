from app.api import api
from app.main.resources import UserListResource
from app.climbing.resources import (
    RouteResource,
    RouteListResource,
    SessionResource
)


api.add_resource(UserListResource, '/users')
api.add_resource(RouteListResource, '/routes')
api.add_resource(RouteResource, '/route/<int:route_id>')
api.add_resource(SessionResource, '/session', '/session/<int:session_id>')
