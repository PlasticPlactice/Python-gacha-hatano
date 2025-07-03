import random
from fastapi import FastAPI

app = FastAPI()

# Gacha item rarities and their weights
gacha_items = {
    "SSR": 3,
    "SR": 10,
    "R": 37,
    "N": 50,
}

# Create a weighted list of items
weighted_gacha = []
for rarity, weight in gacha_items.items():
    weighted_gacha.extend([rarity] * weight)

@app.get("/gacha")
def pull_gacha():
    result = random.choice(weighted_gacha)
    return {"rarity": result}
