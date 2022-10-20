import json

# Opening JSON files
with open("eltoquedataEUR1000.json") as euro_file, open("eltoquedataMLC1000.json") as mlc_file, open("eltoquedataUSD1000.json") as usd_file:
    euro_data = json.load(euro_file)
    mlc_data = json.load(mlc_file)
    usd_data = json.load(usd_file)