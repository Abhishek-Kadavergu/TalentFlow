from typing import List
from pydantic import BaseModel


class ResumeEvaluation(BaseModel):
    overall_score: int
    technical_match: int
    experience_match: int
    project_match: int
    strengths: List[str]
    missing_skills: List[str]
    recommendations: List[str]