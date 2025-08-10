import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Gacha item rarities and their weights
gacha_items = {
    "大吉": 3,
    "凶": 10,
    "大凶": 37,
    "めっちゃ凶": 50,
}

# Create a weighted list of items
weighted_gacha = []
for rarity, weight in gacha_items.items():
    weighted_gacha.extend([rarity] * weight)


@app.get("/gacha")
def pull_gacha():
    result = random.choice(weighted_gacha)
    return {"rarity": result}
