from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.main.models import User
from app.main.schemas import users_schema


class UserListResource(Resource):
    decorators = [jwt_required]

    def get(self):
        users = User.query.all()
        results = users_schema.dump(users)
        return {'users': results.data}
