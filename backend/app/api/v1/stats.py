from flask import Blueprint, jsonify

from app.models.user import User
from app.models.enrollment import Enrollment
from app.models.contact_message import ContactMessage
from app.models.milestone import Milestone
from app.utils.helpers import success_response

stats_bp = Blueprint("stats", __name__)


@stats_bp.route("", methods=["GET"])
def get_stats():
    total_students = User.query.filter_by(role="student").count()
    total_enrollments = Enrollment.query.count()
    total_messages = ContactMessage.query.count()
    unread_messages = ContactMessage.query.filter_by(is_read=False).count()

    milestones = Milestone.query.order_by(Milestone.display_order).all()

    return jsonify(success_response(data={
        "total_students": total_students,
        "total_enrollments": total_enrollments,
        "total_messages": total_messages,
        "unread_messages": unread_messages,
        "milestones": [m.to_dict() for m in milestones],
    })), 200
