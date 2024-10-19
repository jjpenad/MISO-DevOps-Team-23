from flask import request, jsonify
from flask_restful import Resource
from models import Blacklist
from schemas import BlacklistSchema
from extensions import db, jwt
from flask_jwt_extended import jwt_required, create_access_token

blacklist_schema = BlacklistSchema()


class AddToBlacklist(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        email = data.get('email')
        app_uuid = data.get('app_uuid')
        blocked_reason = data.get('blocked_reason', None)
        ip_address = request.remote_addr

        if Blacklist.query.filter_by(email=email).first():
            return {"message": "Email already blacklisted."}, 400

        new_blacklist_entry = Blacklist(
            email=email, app_uuid=app_uuid, blocked_reason=blocked_reason, ip_address=ip_address)
        db.session.add(new_blacklist_entry)
        db.session.commit()

        return {"message": "Email added to blacklist successfully."}, 201


class CheckBlacklist(Resource):
    @jwt_required()
    def get(self, email):
        blacklist_entry = Blacklist.query.filter_by(email=email).first()
        if not blacklist_entry:
            return {"blacklisted": False}, 404

        result = blacklist_schema.dump(blacklist_entry)
        return {"blacklisted": True, "data": result}, 200


class Login(Resource):
    def post(self):
        # Este token puede ser estático para propósitos de prueba
        access_token = create_access_token(identity='user')
        return jsonify(access_token=access_token)
