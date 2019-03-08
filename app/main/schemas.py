from app import ma
from app.main.models import User, Role


class RoleSchema(ma.ModelSchema):
    class Meta:
        model = Role


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('id', 'email', 'role')
    role = ma.Nested(RoleSchema, only=['name'])


role_schema = RoleSchema()
users_schema = UserSchema(many=True)
