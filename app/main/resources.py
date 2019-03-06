from flask_apispec import marshal_with, MethodResource
from flask_jwt_extended import jwt_required
from app.main.models import User
from app.main.schemas import UserSchema


@marshal_with(UserSchema(many=True))
class UserListResource(MethodResource):
    decorators = [jwt_required]

    def get(self):
        return User.query.all()
