from flask import request
from marshmallow import ValidationError
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.database import db
from app.climbing.models import Session, Route
from app.climbing.schemas import route_schema, session_schema


class RouteListResource(Resource):
    decorators = [jwt_required]

    def get(self):
        routes = Route.query.all()
        results = route_schema.dump(routes, many=True)
        return {'routes': results}


class RouteResource(Resource):
    decorators = [jwt_required]

    def get(self, route_id):
        route = Route.query.get(route_id)
        results = route_schema.dump(route)
        return {'route': results}

    def put(self, route_id):
        data = request.get_json()
        current_route = Route.query.get(route_id)
        try:
            updated_route = route_schema.load(data, instance=current_route)
        except ValidationError as err:
            return {'status': 'validation error', 'error': err.messages}
        db.session.add(updated_route)
        db.session.commit()
        return {'status': 'Updated route'}
