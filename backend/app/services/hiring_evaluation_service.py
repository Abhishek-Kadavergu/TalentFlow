import json

from app.schemas.hiring import HiringEvaluation
from app.services.gemini_service import GeminiService
from app.utils.prompt_loader import load_prompt


class HiringEvaluationService:

    def __init__(self):
        self.gemini = GeminiService()

    def evaluate(
        self,
        resume,
        github,
        job_description,
    ):

        prompt = load_prompt(
            "hiring_evaluation.txt"
        )

        prompt = prompt.replace(
            "{resume}",
            json.dumps(resume, indent=2),
        )

        prompt = prompt.replace(
            "{github}",
            json.dumps(github, indent=2),
        )

        prompt = prompt.replace(
            "{job_description}",
            job_description,
        )

        response = self.gemini.generate_text(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return HiringEvaluation.model_validate_json(response)