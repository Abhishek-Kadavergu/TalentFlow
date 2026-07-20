from fastapi import APIRouter
from pydantic import BaseModel

from app.services.resume_evaluation_service import ResumeEvaluationService

router = APIRouter(
    prefix="/evaluation",
    tags=["Evaluation"]
)

service = ResumeEvaluationService()


class EvaluationRequest(BaseModel):
    resume: dict
    job_description: str


@router.post("/resume")
async def evaluate_resume(request: EvaluationRequest):
    return service.evaluate(
        request.resume,
        request.job_description
    )