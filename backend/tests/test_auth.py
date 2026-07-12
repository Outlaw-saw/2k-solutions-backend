def test_register_success(client):
    resp = client.post("/api/v1/auth/register", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "+91 98765 43210",
        "password": "password123",
        "terms_accepted": True,
    })
    data = resp.get_json()
    assert resp.status_code == 201
    assert data["success"] is True
    assert "access_token" in data["data"]
    assert "refresh_token" in data["data"]
    assert data["data"]["user"]["email"] == "john@example.com"


def test_register_duplicate_email(client):
    client.post("/api/v1/auth/register", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "dup@example.com",
        "phone": "+91 98765 43210",
        "password": "password123",
        "terms_accepted": True,
    })
    resp = client.post("/api/v1/auth/register", json={
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "dup@example.com",
        "phone": "+91 98765 43211",
        "password": "password123",
        "terms_accepted": True,
    })
    assert resp.status_code == 409


def test_register_validation_errors(client):
    resp = client.post("/api/v1/auth/register", json={
        "first_name": "",
        "email": "invalid",
        "password": "12",
        "terms_accepted": False,
    })
    assert resp.status_code == 422


def test_login_success(client):
    client.post("/api/v1/auth/register", json={
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane@example.com",
        "phone": "+91 98765 43210",
        "password": "password123",
        "terms_accepted": True,
    })
    resp = client.post("/api/v1/auth/login", json={
        "email": "jane@example.com",
        "password": "password123",
    })
    data = resp.get_json()
    assert resp.status_code == 200
    assert data["success"] is True
    assert "access_token" in data["data"]


def test_login_invalid_credentials(client):
    resp = client.post("/api/v1/auth/login", json={
        "email": "nonexistent@example.com",
        "password": "wrong",
    })
    assert resp.status_code == 401


def test_me_endpoint(client):
    reg_resp = client.post("/api/v1/auth/register", json={
        "first_name": "Me",
        "last_name": "Test",
        "email": "me@example.com",
        "phone": "+91 98765 43210",
        "password": "password123",
        "terms_accepted": True,
    })
    token = reg_resp.get_json()["data"]["access_token"]

    resp = client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token}"})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data["data"]["email"] == "me@example.com"
