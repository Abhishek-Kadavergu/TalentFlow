import os
import tempfile

from fastapi import APIRouter, File, Form, UploadFile

from app.services.submission_service import SubmissionService

router = APIRouter(
    prefix="/submission",
    tags=["Submission"],
)

service = SubmissionService()


@router.post("/analyze")
async def analyze_submission(
    resume: UploadFile = File(...),
    github_url: str = Form(...),
    job_description: str = Form(...),
):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:

        temp.write(await resume.read())

        temp_path = temp.name

    try:

        result = service.analyze(
            temp_path,
            github_url,
            job_description,
        )

        return result

    finally:

        os.remove(temp_path)