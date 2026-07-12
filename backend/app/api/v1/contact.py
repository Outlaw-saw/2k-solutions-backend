from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.middleware.auth import admin_required
from app.services.contact_service import ContactService
from app.utils.helpers import success_response

contact_bp = Blueprint("contact", __name__)
contact_service = ContactService()


@contact_bp.route("", methods=["POST"])
def submit_contact():
    data = request.get_json(silent=True) or {}
    message = contact_service.create(data)
    return jsonify(success_response(
        data=message.to_dict(),
        message="Message sent successfully",
    )), 201


@contact_bp.route("", methods=["GET"])
@jwt_required()
@admin_required
def list_messages():
    result = contact_service.list_paginated()
    return jsonify(success_response(
        data=result["items"],
        meta=result["meta"],
    )), 200


@contact_bp.route("/<message_id>/read", methods=["PATCH"])
@jwt_required()
@admin_required
def mark_as_read(message_id: str):
    message = contact_service.mark_as_read(message_id)
    return jsonify(success_response(
        data=message.to_dict(),
        message="Message marked as read",
    )), 200
