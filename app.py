import streamlit as st
from clause_extraction import extract_clauses
from risk_detector import detect_risks
from risk_scoring import calculate_risk_score
from LLm.explainer import explain_clause

st.title("Contract Analysis & Risk Assessment Bot")

# Upload file
file = st.file_uploader("Upload Contract", type=["txt"])

if file is not None:
    # Read text
    text = file.read().decode("utf-8")

    # Extract clauses  ← THIS WAS MISSING
    clauses = extract_clauses(text)

    st.success(f"{len(clauses)} clauses detected")

    # Loop through clauses
    for c in clauses:
        risks = detect_risks(c["text"])
        score = calculate_risk_score(risks)

        st.subheader(c["clause_id"])
        st.write(c["text"])
        st.write("**Risk Score:**", score)

        # Button for AI explanation
        if st.button(f"Explain {c['clause_id']}"):
            explanation = explain_clause(c["text"], risks)
            st.write(explanation)

