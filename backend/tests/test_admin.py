def test_admin_list_users(client, auth_headers):
    resp = client.get("/api/v1/users", headers=auth_headers)
    assert resp.status_code == 200


def test_admin_unauthorized(client):
    resp = client.get("/api/v1/users")
    assert resp.status_code == 401
