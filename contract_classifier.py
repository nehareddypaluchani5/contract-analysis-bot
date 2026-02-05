import json

with open("data/contract_types.json", encoding="utf-8") as f:
    CONTRACT_TYPES = json.load(f)

def classify_contract(text):
    text = text.lower()
    scores = {}

    for ctype, keywords in CONTRACT_TYPES.items():
        scores[ctype] = sum(1 for kw in keywords if kw in text)

    return max(scores, key=scores.get)
