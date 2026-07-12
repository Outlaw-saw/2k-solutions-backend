class AppError(Exception):
    status: int = 400
    message: str = ""
    errors: list = []

    def __init__(self, message: str = "", errors: list | None = None, status: int | None = None):
        self.message = message or self.message
        self.errors = errors or []
        if status:
            self.status = status
        super().__init__(self.message)


class NotFoundError(AppError):
    status = 404
    message = "Resource not found"


class ValidationError(AppError):
    status = 422
    message = "Validation failed"


class AuthenticationError(AppError):
    status = 401
    message = "Authentication failed"


class AuthorizationError(AppError):
    status = 403
    message = "You do not have permission to perform this action"


class ConflictError(AppError):
    status = 409
    message = "Resource already exists"
