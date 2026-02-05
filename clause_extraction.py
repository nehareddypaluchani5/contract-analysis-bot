import re

def extract_clauses(text):
    pattern = r"\n\d+\.|\n[A-Z][A-Za-z ]+:\n"
    parts = re.split(pattern, text)

    clauses = []
    for i, part in enumerate(parts):
        if len(part.strip()) > 40:
            clauses.append({
                "clause_id": f"C{i+1}",
                "text": part.strip()
            })
    return clauses
