from fastapi.testclient import TestClient

from app.db.session import get_db
from app.main import app

client = TestClient(app)


def test_health_check_ok():
    """API is up and connected to the database."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "database": "ok",
        "environment": "development",
    }


def test_health_check_database_unavailable():
    """If the database fails, /health still answers and reports it."""

    class BrokenSession:
        def execute(self, *args, **kwargs):
            raise Exception("database is down")

    app.dependency_overrides[get_db] = lambda: BrokenSession()
    try:
        response = client.get("/health")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json()["status"] == "degraded"
    assert response.json()["database"] == "unavailable"