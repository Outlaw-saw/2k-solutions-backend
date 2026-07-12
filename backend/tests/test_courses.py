def test_list_courses(client):
    resp = client.get("/api/v1/courses")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["success"] is True


def test_get_course_not_found(client):
    resp = client.get("/api/v1/courses/nonexistent")
    assert resp.status_code == 404


def test_list_services(client):
    resp = client.get("/api/v1/services")
    assert resp.status_code == 200


def test_list_testimonials(client):
    resp = client.get("/api/v1/testimonials")
    assert resp.status_code == 200


def test_list_faqs(client):
    resp = client.get("/api/v1/faqs")
    assert resp.status_code == 200


def test_list_technologies(client):
    resp = client.get("/api/v1/technologies")
    assert resp.status_code == 200


def test_list_steps(client):
    resp = client.get("/api/v1/steps")
    assert resp.status_code == 200


def test_list_differentiators(client):
    resp = client.get("/api/v1/differentiators")
    assert resp.status_code == 200


def test_get_stats(client):
    resp = client.get("/api/v1/stats")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["success"] is True


def test_submit_contact(client):
    resp = client.post("/api/v1/contact", json={
        "name": "Test User",
        "email": "test@example.com",
        "message": "This is a test message",
    })
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["success"] is True


def test_get_site_settings(client):
    resp = client.get("/api/v1/site")
    assert resp.status_code == 200
