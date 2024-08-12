from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from app.main import app, get_db

def override_get_db():
    db = MagicMock()
    yield db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert {"Fast API running successfully"}
