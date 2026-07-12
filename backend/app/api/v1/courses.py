from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.middleware.auth import admin_required
from app.services.course_service import CourseService
from app.utils.helpers import success_response

courses_bp = Blueprint("courses", __name__)
course_service = CourseService()


@courses_bp.route("", methods=["GET"])
def list_courses():
    result = course_service.list_paginated()
    return jsonify(success_response(
        data=result["items"],
        meta=result["meta"],
    )), 200


@courses_bp.route("/active", methods=["GET"])
def list_active_courses():
    courses = course_service.list_active()
    return jsonify(success_response(data=courses)), 200


@courses_bp.route("/<slug>", methods=["GET"])
def get_course(slug: str):
    course = course_service.get_with_modules(slug)
    return jsonify(success_response(data=course)), 200


@courses_bp.route("", methods=["POST"])
@jwt_required()
@admin_required
def create_course():
    data = request.get_json(silent=True) or {}
    course = course_service.create(data)
    return jsonify(success_response(data=course.to_dict(), message="Course created")), 201


@courses_bp.route("/<slug>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_course(slug: str):
    data = request.get_json(silent=True) or {}
    course = course_service.update(slug, data)
    return jsonify(success_response(data=course.to_dict(), message="Course updated")), 200
