from clause_extraction import extract_clauses
from risk_detector import detect_risks
from risk_scoring import calculate_risk_score

with open("data/sample_contracts/employment_agreement_1.txt", encoding="utf-8") as f:
    text = f.read()

clauses = extract_clauses(text)

for c in clauses:
    risks = detect_risks(c["text"])
    score = calculate_risk_score(risks)

    print(c["clause_id"], score, risks)
