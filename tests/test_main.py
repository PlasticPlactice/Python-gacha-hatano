from src.main import pull_gacha

def test_gacha_logic():
    result = pull_gacha()
    assert "rarity" in result
    assert result["rarity"] in ["大吉", "凶", "大凶", "めっちゃ凶"]
