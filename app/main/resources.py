from flask_apispec import marshal_with
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.main.models import User
from app.main.schemas import UserSchema


class UserListResource(Resource):
    decorators = [jwt_required]

    @marshal_with(UserSchema(many=True))
    def get(self):
        return User.query.all()
