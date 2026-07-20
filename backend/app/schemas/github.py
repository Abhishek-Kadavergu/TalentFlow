from typing import List

from pydantic import BaseModel


class GitHubAnalysis(BaseModel):
    project_name: str
    summary: str
    tech_stack: List[str]
    architecture: str
    strengths: List[str]
    issues: List[str]
    code_quality_score: int
    documentation_score: int
    overall_score: int