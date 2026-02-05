import pdfplumber
import docx

def extract_text(file, file_type):
    if file_type == "pdf":
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    elif file_type == "docx":
        doc = docx.Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    elif file_type == "txt":
        return file.read().decode("utf-8")
