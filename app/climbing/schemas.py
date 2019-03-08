from app import ma
from app.climbing.models import Session, Route


class RouteSchema(ma.ModelSchema):

    class Meta:
        model = Route


class SessionSchema(ma.ModelSchema):

    class Meta:
        model = Session


route_schema = RouteSchema()
session_schema = SessionSchema()
