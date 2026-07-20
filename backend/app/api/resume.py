from fastapi import APIRouter, File, UploadFile, HTTPException
import tempfile
import os

from app.utils.pdf_parser import extract_text_from_pdf
from app.services.resume_extraction_service import ResumeExtractionService
from app.core.logger import logger

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

resume_service = ResumeExtractionService()


@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )


    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(await file.read())
        temp_path = temp.name

    try:
        resume_text = extract_text_from_pdf(temp_path)
        result = resume_service.extract(resume_text)
        
        return result

    finally:
        os.remove(temp_path)