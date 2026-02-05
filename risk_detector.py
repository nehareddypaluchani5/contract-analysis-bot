import json

with open("data/risk_dictionary.json", encoding="utf-8") as f:
    RISK_DATA = json.load(f)

def detect_risks(text):
    found = []
    text = text.lower()

    for risk, details in RISK_DATA.items():
        for kw in details["keywords"]:
            if kw.lower() in text:
                found.append({
                    "risk": risk,
                    "level": details["risk_level"],
                    "reason": details["reason"]
                })
    return found
