import pytest
from app import create_app
from app.extensions import db as _db
from config import TestConfig


@pytest.fixture(scope="session")
def app():
    app = create_app(TestConfig)
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture(scope="function")
def db(app):
    _db.session.begin_nested()
    yield _db
    _db.session.rollback()


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def auth_headers(client, db):
    from app.models.user import User
    import bcrypt

    password_hash = bcrypt.hashpw(b"password123", bcrypt.gensalt()).decode("utf-8")
    user = User(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        phone="+91 98765 43210",
        password_hash=password_hash,
        role="admin",
        terms_accepted=True,
        is_active=True,
        email_verified=True,
    )
    db.session.add(user)
    db.session.commit()

    resp = client.post("/api/v1/auth/login", json={
        "email": "test@example.com",
        "password": "password123",
    })
    data = resp.get_json()
    token = data["data"]["access_token"]
    return {"Authorization": f"Bearer {token}"}
