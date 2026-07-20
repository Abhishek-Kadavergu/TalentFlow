from typing import List

from pydantic import BaseModel


class HiringEvaluation(BaseModel):
    final_score: int
    recommendation: str
    strengths: List[str]
    concerns: List[str]
    interview_questions: List[str]
    summary: str