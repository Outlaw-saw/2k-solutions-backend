from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.middleware.auth import admin_required
from app.services.user_service import UserService
from app.utils.helpers import success_response

users_bp = Blueprint("users", __name__)
user_service = UserService()


@users_bp.route("", methods=["GET"])
@jwt_required()
@admin_required
def list_users():
    result = user_service.list_paginated()
    return jsonify(success_response(
        data=result["items"],
        meta=result["meta"],
    )), 200


@users_bp.route("/<user_id>", methods=["GET"])
@jwt_required()
@admin_required
def get_user(user_id: str):
    user = user_service.get_by_id(user_id)
    return jsonify(success_response(data=user.to_dict())), 200


@users_bp.route("/<user_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_user(user_id: str):
    data = request.get_json(silent=True) or {}
    user = user_service.update(user_id, data)
    return jsonify(success_response(data=user.to_dict(), message="User updated")), 200
