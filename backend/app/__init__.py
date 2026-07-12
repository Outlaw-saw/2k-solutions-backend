import logging
import sys

from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.extensions import db, migrate, jwt
from config import Config


def create_app(config_object: object = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    configure_extensions(app)
    configure_logging(app)
    register_root_route(app)
    register_blueprints(app)
    register_error_handlers(app)
    init_request_logger(app)

    return app


def configure_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(
        app,
        origins=app.config["CORS_ORIGINS"],
        supports_credentials=True,
    )
    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=[app.config["RATELIMIT_DEFAULT"]],
        storage_uri="memory://",
    )


def configure_logging(app: Flask) -> None:
    log_level = getattr(logging, app.config["LOG_LEVEL"].upper(), logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ))
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    sql_logger = logging.getLogger("sqlalchemy.engine")
    sql_logger.setLevel(logging.WARNING)


def register_blueprints(app: Flask) -> None:
    from app.api.v1 import api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix="/api/v1")


def register_root_route(app: Flask) -> None:
    @app.route("/")
    def health():
        return {"status": "ok", "message": "2K Solutions API is running"}

def register_error_handlers(app: Flask) -> None:
    from app.middleware.error_handler import register_error_handlers as _register
    _register(app)


def init_request_logger(app: Flask) -> None:
    from app.middleware.request_logger import init_request_logger as _init
    _init(app)
