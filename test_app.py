from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_health():
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_status():
    client = app.test_client()

    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json["status"] == "running"
    assert response.json["service"] == "secure-devsecops-api"