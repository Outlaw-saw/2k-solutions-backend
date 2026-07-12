from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.middleware.auth import admin_required
from app.services.content_service import ContentService
from app.utils.helpers import success_response

site_bp = Blueprint("site", __name__)
content_service = ContentService()


@site_bp.route("", methods=["GET"])
def get_site_settings():
    settings = content_service.get_site_settings()
    return jsonify(success_response(data=settings)), 200


@site_bp.route("", methods=["PATCH"])
@jwt_required()
@admin_required
def update_site_settings():
    data = request.get_json(silent=True) or {}
    settings = content_service.update_site_settings(data)
    return jsonify(success_response(data=settings, message="Site settings updated")), 200
