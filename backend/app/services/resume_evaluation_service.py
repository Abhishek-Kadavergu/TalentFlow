import json

from app.schemas.evaluation import ResumeEvaluation
from app.services.gemini_service import GeminiService
from app.utils.prompt_loader import load_prompt


class ResumeEvaluationService:

    def __init__(self):
        self.gemini = GeminiService()

    def evaluate(self, resume_json: dict, job_description: str):

        prompt = load_prompt("resume_evaluation.txt")

        prompt = prompt.replace(
            "{resume}",
            json.dumps(resume_json, indent=2)
        )

        prompt = prompt.replace(
            "{job_description}",
            job_description
        )

        response = self.gemini.generate_text(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        data = json.loads(response)

        return ResumeEvaluation.model_validate(data)