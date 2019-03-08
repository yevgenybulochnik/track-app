from app.api import api
from app.main.resources import UserListResource
from app.climbing.resources import (
    RouteListResource
)


api.add_resource(UserListResource, '/users')
api.add_resource(RouteListResource, '/routes')
