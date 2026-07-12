from docx import Document


def read_master_resume(path: str) -> str:
    doc = Document(path)

    text = []

    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text)