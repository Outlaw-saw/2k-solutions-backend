from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt, verify_jwt_in_request

from app.models.user import User


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims.get("role") != "admin":
            return jsonify(success=False, message="Admin access required", errors=[], status=403), 403
        return f(*args, **kwargs)
    return wrapper


def get_current_user() -> User | None:
    from flask_jwt_extended import get_jwt_identity
    user_id = get_jwt_identity()
    if user_id:
        return User.query.filter_by(id=user_id).first()
    return None
