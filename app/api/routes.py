from app.api import api
from app.main.resources import UserListResource
from app.climbing.resources import (
    RouteListResource,
    RouteResource
)


api.add_resource(UserListResource, '/users')
api.add_resource(RouteListResource, '/routes')
api.add_resource(RouteResource, '/route/<int:route_id>')
