from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def explain_clause(clause_text, risks):
    prompt = f"""
You are a legal assistant for Indian SMEs.

Explain this contract clause in simple business English.
Mention:
1. What it means
2. Why it is risky (if risks exist)
3. Suggest a safer alternative clause

Clause:
{clause_text}

Detected Risks:
{risks}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content
