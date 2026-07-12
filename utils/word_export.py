from docx import Document


def save_resume(resume_text: str, output_path: str):

    document = Document()

    for line in resume_text.split("\n"):
        document.add_paragraph(line)

    document.save(output_path)

    return output_path