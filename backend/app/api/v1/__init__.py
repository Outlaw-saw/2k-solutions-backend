from flask import Blueprint

api_v1_bp = Blueprint("api_v1", __name__)

from app.api.v1.auth import auth_bp
from app.api.v1.users import users_bp
from app.api.v1.courses import courses_bp
from app.api.v1.enrollments import enrollments_bp
from app.api.v1.contact import contact_bp
from app.api.v1.content import content_bp
from app.api.v1.stats import stats_bp
from app.api.v1.site import site_bp

api_v1_bp.register_blueprint(auth_bp, url_prefix="/auth")
api_v1_bp.register_blueprint(users_bp, url_prefix="/users")
api_v1_bp.register_blueprint(courses_bp, url_prefix="/courses")
api_v1_bp.register_blueprint(enrollments_bp, url_prefix="/enrollments")
api_v1_bp.register_blueprint(contact_bp, url_prefix="/contact")
api_v1_bp.register_blueprint(content_bp, url_prefix="")
api_v1_bp.register_blueprint(stats_bp, url_prefix="/stats")
api_v1_bp.register_blueprint(site_bp, url_prefix="/site")
