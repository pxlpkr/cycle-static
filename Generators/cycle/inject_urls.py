import requests
import json

URLS_URL = "https://raw.githubusercontent.com/Wynntils/Static-Storage/refs/heads/main/Data-Storage/urls.json"

WYNNCYCLE_WEIGHTS_URL = "https://raw.githubusercontent.com/pxlpkr/cycle-static/refs/heads/main/Extern/pub/item_weights.json"
WYNNCYCLE_URLS_URL = "https://raw.githubusercontent.com/pxlpkr/cycle-static/refs/heads/main/Data-Storage/urls.json"

def buildURLs():
    # EXTERNAL
    response = requests.get(URLS_URL)
    externalData = response.json()

    # CONVERT
    for obj in [i for i in externalData if "id" in i and i["id"] == "dataAthenaItemWeights"]:
        obj["url"] = WYNNCYCLE_WEIGHTS_URL

    for obj in [i for i in externalData if "id" in i and i["id"] == "dataStaticUrls"]:
            obj["url"] = WYNNCYCLE_URLS_URL

    # WRITE
    with open('Data-Storage/urls.json', 'w+', encoding='utf-8') as file:
        json.dump(externalData, file, indent=2)

if __name__ == "__main__":
     buildURLs()