from app.utils.pdf_parser import extract_text_from_pdf

text = extract_text_from_pdf(
    r"D:\Projects\talentflow\backend\resume.pdf"
)

print(text)