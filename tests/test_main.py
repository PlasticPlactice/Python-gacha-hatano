from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_gacha():
    response = client.get("/gacha")
    assert response.status_code == 200
    json_data = response.json()
    assert "rarity" in json_data
    assert json_data["rarity"] in ["SSR", "SR", "R", "N"]
