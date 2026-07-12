from flask import Flask, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_jwt_extended.exceptions import NoAuthorizationError
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from app.utils.errors import AppError


def register_error_handlers(app: Flask) -> None:
    @app.errorhandler(AppError)
    def handle_app_error(error: AppError) -> tuple:
        return jsonify(success=False, message=error.message, errors=error.errors, status=error.status), error.status

    @app.errorhandler(ValidationError)
    def handle_validation_error(error: ValidationError) -> tuple:
        return jsonify(success=False, message="Validation failed", errors=error.messages, status=422), 422

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(error: IntegrityError) -> tuple:
        app.logger.error(f"Database integrity error: {str(error)}")
        return jsonify(success=False, message="A database constraint was violated", errors=[], status=409), 409

    @app.errorhandler(SQLAlchemyError)
    def handle_db_error(error: SQLAlchemyError) -> tuple:
        app.logger.error(f"Database error: {str(error)}")
        return jsonify(success=False, message="A database error occurred", errors=[], status=500), 500

    @app.errorhandler(NoAuthorizationError)
    def handle_no_auth(error: NoAuthorizationError) -> tuple:
        return jsonify(success=False, message="Authentication token is missing", errors=[], status=401), 401

    @app.errorhandler(ExpiredSignatureError)
    def handle_expired_token(error: ExpiredSignatureError) -> tuple:
        return jsonify(success=False, message="Token has expired", errors=[], status=401), 401

    @app.errorhandler(InvalidTokenError)
    def handle_invalid_token(error: InvalidTokenError) -> tuple:
        return jsonify(success=False, message="Invalid token", errors=[], status=401), 401

    @app.errorhandler(404)
    def handle_404(error) -> tuple:
        return jsonify(success=False, message="Resource not found", errors=[], status=404), 404

    @app.errorhandler(405)
    def handle_405(error) -> tuple:
        return jsonify(success=False, message="Method not allowed", errors=[], status=405), 405

    @app.errorhandler(500)
    def handle_500(error) -> tuple:
        app.logger.error(f"Internal server error: {str(error)}")
        return jsonify(success=False, message="Internal server error", errors=[], status=500), 500
