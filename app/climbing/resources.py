from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.climbing.models import Session, Route
from app.climbing.schemas import route_schema, session_schema


class RouteListResource(Resource):

    def get(self):
        routes = Route.query.all()
        results = route_schema.dump(routes, many=True)
        return {'routes': results}
