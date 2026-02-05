def calculate_risk_score(risks):
    if not risks:
        return "Low"

    levels = [r["level"] for r in risks]

    if "High" in levels:
        return "High"
    elif "Medium" in levels:
        return "Medium"
    return "Low"
