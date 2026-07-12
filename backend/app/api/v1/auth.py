from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required

from app.middleware.auth import get_current_user
from app.services.auth_service import AuthService
from app.utils.helpers import success_response, error_response

auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}
    try:
        result = auth_service.register(data)
        return jsonify(success_response(
            data=result,
            message="Account created successfully",
        )), 201
    except Exception as e:
        raise e


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    try:
        result = auth_service.login(data)
        return jsonify(success_response(
            data=result,
            message="Login successful",
        )), 200
    except Exception as e:
        raise e


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    claims = get_jwt()
    result = auth_service.refresh(identity, claims.get("role", "student"))
    return jsonify(success_response(data=result, message="Token refreshed")), 200


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    return jsonify(success_response(message="Logged out successfully")), 200


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    user = get_current_user()
    if not user:
        return error_response("User not found", status=404)
    return jsonify(success_response(data=user.to_dict())), 200
