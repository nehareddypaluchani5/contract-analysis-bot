# Contract Analysis & Risk Assessment Bot

## Overview

The **Contract Analysis & Risk Assessment Bot** is a Generative AI–powered legal assistant designed to help **small and medium enterprises (SMEs)** understand complex legal contracts without requiring deep legal knowledge.

The system analyzes uploaded contracts, detects **potential legal and financial risks**, and explains clauses in **simple business language** using **Natural Language Processing (NLP)** and **Large Language Model (LLM)** reasoning.

---

## Problem Statement

Legal contracts often contain:

* Complex legal terminology
* Hidden liabilities
* Unfavorable clauses
* Financial and compliance risks

SMEs frequently sign agreements **without fully understanding these risks**, leading to disputes, penalties, or financial loss.

This project provides an **AI-driven contract review tool** that simplifies legal understanding and highlights risky clauses before signing.

---

## Key Features

### Contract Processing

* Supports **TXT, PDF, and DOCX** formats
* Extracts **plain text** from uploaded documents
* Splits contracts into **individual clauses**

### Legal Risk Detection

Identifies major risky terms such as:

* **Indemnity clauses**
* **Penalty / liquidated damages**
* **Unilateral termination rights**
* **Non-compete restrictions**
* **Auto-renewal lock-ins**
* **Jurisdiction bias**

Each clause is assigned a **risk score**:

* **Low**
* **Medium**
* **High**

---

### AI-Powered Explanation

Using **Generative AI (LLM)**, the system provides:

* Plain-English clause meaning
* Reason for legal risk
* Suggested **safer alternative wording**

This makes the tool useful for **non-lawyers and business owners**.

---

### Multilingual Capability

* Supports **English and Hindi** contracts
* Detects risks in **Hindi legal text**
* Generates explanations in **simple English**

---

### Web Application Interface

Built using **Streamlit**, allowing users to:

* Upload contracts through a browser
* View clause-level risks
* Click to generate AI explanations
* Interactively explore contract insights

---

## Technology Stack

### Programming Language

* **Python**

### NLP & AI

* **spaCy** – text processing & entity handling
* **Rule-based legal risk detection**
* **OpenAI / LLM** – clause explanation & reasoning

### Web Framework

* **Streamlit** – interactive UI

### Document Processing

* **pdfplumber** – PDF text extraction
* **python-docx** – DOCX reading

### Utilities

* **langdetect** – language detection
* **reportlab** – PDF report generation

---

## Project Architecture

### 1. Data Layer

Contains:

* Sample contracts
* Risk dictionary (JSON)
* Contract type keywords

### 2. Processing Layer

Performs:

* Text extraction
* Clause segmentation
* Risk detection & scoring
* AI-based explanation

### 3. Presentation Layer

* Streamlit web interface
* Displays clauses, risks, and explanations

---

## Folder Structure

```
contract_analysis_bot/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── sample_contracts/
│   ├── templates/
│   ├── risk_dictionary.json
│   └── contract_types.json
│
├── nlp/
│   ├── clause_extraction.py
│   ├── risk_detector.py
│   ├── risk_scoring.py
│
├── llm/
│   └── explainer.py
│
└── outputs/
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/contract-analysis-bot.git
cd contract-analysis-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
python -m streamlit run app.py
```

Open browser at:

```
http://localhost:8501
```

---

## Deployment

The application can be deployed using **Streamlit Community Cloud**:

1. Push code to **GitHub**
2. Connect repository to **Streamlit Cloud**
3. Deploy using `app.py` as entry point

This enables **public web access** to the contract analysis tool.

---

## Use Cases

* SME contract review before signing
* Freelancer agreement risk checking
* Vendor & service contract validation
* Legal awareness for non-lawyers
* Educational LegalTech demonstration

---

## Future Enhancements

* Full **PDF risk report download**
* **Clause similarity** with SME-friendly templates
* **Voice-based contract explanation**
* Advanced **NER for legal entities**
* Integration with **legal compliance datasets**

---

## Academic & Practical Value

This project demonstrates:

* Real-world **LegalTech AI application**
* Integration of **NLP + Generative AI + Web UI**
* Practical solution for **SME legal risk awareness**

---

## Author

**Neha Reddy**
AI / Data Science Student

---

## License

This project is for **educational and research purposes**.
