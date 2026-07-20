from app.schemas.evaluation import ResumeEvaluation
from app.schemas.github import GitHubAnalysis
from app.schemas.resume import ResumeExtraction
from pydantic import BaseModel


class SubmissionResponse(BaseModel):
    resume: ResumeExtraction
    resume_evaluation: ResumeEvaluation
    github_analysis: GitHubAnalysis