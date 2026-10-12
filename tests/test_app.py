from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_utc_time() -> None:
    response = client.get("/time")
    assert response.status_code == 200
    assert response.json()["timezone"] == "UTC"


def test_unknown_timezone() -> None:
    response = client.get("/time/Not_A_Real_Zone")
    assert response.status_code == 404
