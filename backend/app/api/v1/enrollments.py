from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.middleware.auth import admin_required, get_current_user
from app.services.enrollment_service import EnrollmentService
from app.utils.helpers import success_response, error_response

enrollments_bp = Blueprint("enrollments", __name__)
enrollment_service = EnrollmentService()


@enrollments_bp.route("", methods=["POST"])
@jwt_required()
def create_enrollment():
    user = get_current_user()
    if not user:
        return error_response("User not found", status=404)
    data = request.get_json(silent=True) or {}
    enrollment = enrollment_service.create(str(user.id), data)
    return jsonify(success_response(
        data=enrollment.to_dict(),
        message="Enrolled successfully",
    )), 201


@enrollments_bp.route("", methods=["GET"])
@jwt_required()
def list_enrollments():
    user = get_current_user()
    if not user:
        return error_response("User not found", status=404)
    enrollments = enrollment_service.list_by_user(str(user.id))
    return jsonify(success_response(data=enrollments)), 200


@enrollments_bp.route("/<enrollment_id>", methods=["PATCH"])
@jwt_required()
def update_enrollment(enrollment_id: str):
    data = request.get_json(silent=True) or {}
    enrollment = enrollment_service.update(enrollment_id, data)
    return jsonify(success_response(
        data=enrollment.to_dict(),
        message="Enrollment updated",
    )), 200
