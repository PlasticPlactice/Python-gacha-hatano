from fastapi.testclient import TestClient
from src.main import app, pull_gacha

client = TestClient(app)


def test_gacha_logic():
    result = pull_gacha()
    assert "rarity" in result
    assert result["rarity"] in ["大吉", "凶", "大凶", "めっちゃ凶"]


def test_gacha_response_format():
    result = pull_gacha()
    assert isinstance(result, dict)
    assert "rarity" in result
    assert isinstance(result["rarity"], str)


def test_gacha_endpoint():
    response = client.get("/gacha")
    assert response.status_code == 200
    data = response.json()
    assert "rarity" in data
    assert data["rarity"] in ["大吉", "凶", "大凶", "めっちゃ凶"]
