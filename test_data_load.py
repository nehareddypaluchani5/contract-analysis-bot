import json

with open("data/risk_dictionary.json", encoding="utf-8") as f:
    risk_data = json.load(f)

with open("data/contract_types.json", encoding="utf-8") as f:
    contract_types = json.load(f)

print("Risk keys:", risk_data.keys())
print("Contract types:", contract_types.keys())

