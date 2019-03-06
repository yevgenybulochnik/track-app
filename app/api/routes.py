from app.api import api
from app.main.resources import UserListResource


api.add_resource(UserListResource, '/users')
