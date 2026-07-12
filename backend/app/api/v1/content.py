from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.middleware.auth import admin_required
from app.services.content_service import ContentService
from app.utils.helpers import success_response

content_bp = Blueprint("content", __name__)
content_service = ContentService()


@content_bp.route("/services", methods=["GET"])
def list_services():
    services = content_service.list_services()
    return jsonify(success_response(data=services)), 200


@content_bp.route("/services", methods=["POST"])
@jwt_required()
@admin_required
def create_service():
    data = request.get_json(silent=True) or {}
    service = content_service.create_service(data)
    return jsonify(success_response(data=service.to_dict(), message="Service created")), 201


@content_bp.route("/services/<service_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_service(service_id: str):
    data = request.get_json(silent=True) or {}
    service = content_service.update_service(service_id, data)
    return jsonify(success_response(data=service.to_dict(), message="Service updated")), 200


@content_bp.route("/services/<service_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_service(service_id: str):
    content_service.delete_service(service_id)
    return jsonify(success_response(message="Service deleted")), 200


@content_bp.route("/testimonials", methods=["GET"])
def list_testimonials():
    testimonials = content_service.list_testimonials()
    return jsonify(success_response(data=testimonials)), 200


@content_bp.route("/testimonials", methods=["POST"])
@jwt_required()
@admin_required
def create_testimonial():
    data = request.get_json(silent=True) or {}
    testimonial = content_service.create_testimonial(data)
    return jsonify(success_response(data=testimonial.to_dict(), message="Testimonial created")), 201


@content_bp.route("/testimonials/<testimonial_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_testimonial(testimonial_id: str):
    data = request.get_json(silent=True) or {}
    testimonial = content_service.update_testimonial(testimonial_id, data)
    return jsonify(success_response(data=testimonial.to_dict(), message="Testimonial updated")), 200


@content_bp.route("/testimonials/<testimonial_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_testimonial(testimonial_id: str):
    content_service.delete_testimonial(testimonial_id)
    return jsonify(success_response(message="Testimonial deleted")), 200


@content_bp.route("/faqs", methods=["GET"])
def list_faqs():
    faqs = content_service.list_faqs()
    return jsonify(success_response(data=faqs)), 200


@content_bp.route("/faqs", methods=["POST"])
@jwt_required()
@admin_required
def create_faq():
    data = request.get_json(silent=True) or {}
    faq = content_service.create_faq(data)
    return jsonify(success_response(data=faq.to_dict(), message="FAQ created")), 201


@content_bp.route("/faqs/<faq_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_faq(faq_id: str):
    data = request.get_json(silent=True) or {}
    faq = content_service.update_faq(faq_id, data)
    return jsonify(success_response(data=faq.to_dict(), message="FAQ updated")), 200


@content_bp.route("/faqs/<faq_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_faq(faq_id: str):
    content_service.delete_faq(faq_id)
    return jsonify(success_response(message="FAQ deleted")), 200


@content_bp.route("/technologies", methods=["GET"])
def list_technologies():
    technologies = content_service.list_technologies()
    return jsonify(success_response(data=technologies)), 200


@content_bp.route("/technologies", methods=["POST"])
@jwt_required()
@admin_required
def create_technology():
    data = request.get_json(silent=True) or {}
    tech = content_service.create_technology(data)
    return jsonify(success_response(data=tech.to_dict(), message="Technology created")), 201


@content_bp.route("/technologies/<tech_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_technology(tech_id: str):
    content_service.delete_technology(tech_id)
    return jsonify(success_response(message="Technology deleted")), 200


@content_bp.route("/milestones", methods=["GET"])
def list_milestones():
    section = request.args.get("section")
    milestones = content_service.list_milestones(section)
    return jsonify(success_response(data=milestones)), 200


@content_bp.route("/milestones", methods=["POST"])
@jwt_required()
@admin_required
def create_milestone():
    data = request.get_json(silent=True) or {}
    milestone = content_service.create_milestone(data)
    return jsonify(success_response(data=milestone.to_dict(), message="Milestone created")), 201


@content_bp.route("/milestones/<milestone_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_milestone(milestone_id: str):
    data = request.get_json(silent=True) or {}
    milestone = content_service.update_milestone(milestone_id, data)
    return jsonify(success_response(data=milestone.to_dict(), message="Milestone updated")), 200


@content_bp.route("/milestones/<milestone_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_milestone(milestone_id: str):
    content_service.delete_milestone(milestone_id)
    return jsonify(success_response(message="Milestone deleted")), 200


@content_bp.route("/steps", methods=["GET"])
def list_steps():
    steps = content_service.list_steps()
    return jsonify(success_response(data=steps)), 200


@content_bp.route("/steps", methods=["POST"])
@jwt_required()
@admin_required
def create_step():
    data = request.get_json(silent=True) or {}
    step = content_service.create_step(data)
    return jsonify(success_response(data=step.to_dict(), message="Step created")), 201


@content_bp.route("/steps/<step_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_step(step_id: str):
    data = request.get_json(silent=True) or {}
    step = content_service.update_step(step_id, data)
    return jsonify(success_response(data=step.to_dict(), message="Step updated")), 200


@content_bp.route("/steps/<step_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_step(step_id: str):
    content_service.delete_step(step_id)
    return jsonify(success_response(message="Step deleted")), 200


@content_bp.route("/differentiators", methods=["GET"])
def list_differentiators():
    differentiators = content_service.list_differentiators()
    return jsonify(success_response(data=differentiators)), 200


@content_bp.route("/differentiators", methods=["POST"])
@jwt_required()
@admin_required
def create_differentiator():
    data = request.get_json(silent=True) or {}
    diff = content_service.create_differentiator(data)
    return jsonify(success_response(data=diff.to_dict(), message="Differentiator created")), 201


@content_bp.route("/differentiators/<diff_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_differentiator(diff_id: str):
    data = request.get_json(silent=True) or {}
    diff = content_service.update_differentiator(diff_id, data)
    return jsonify(success_response(data=diff.to_dict(), message="Differentiator updated")), 200


@content_bp.route("/differentiators/<diff_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_differentiator(diff_id: str):
    content_service.delete_differentiator(diff_id)
    return jsonify(success_response(message="Differentiator deleted")), 200
