import requests
import json

WEIGHTS_URL = "https://athena.wynntils.com/cache/get/itemWeights"

def buildWeights():
    # EXTERNAL
    response = requests.get(WEIGHTS_URL)
    externalData = response.json()

    # INTERNAL
    with open('Extern/sources/item_weights.json', 'r', encoding='utf-8') as file:
        internalData = json.load(file)

    # CONVERT
    externalData["wynncycle"] = internalData

    # WRITE
    with open('Extern/pub/item_weights.json', 'w+', encoding='utf-8') as file:
        json.dump(externalData, file)

if __name__ == "__main__":
     buildWeights()