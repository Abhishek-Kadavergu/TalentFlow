import json

from app.schemas.resume import ResumeExtraction
from app.services.gemini_service import GeminiService
from app.utils.prompt_loader import load_prompt


class ResumeExtractionService:

    def __init__(self):
        self.gemini = GeminiService()

    def extract(self, resume_text: str) -> ResumeExtraction:

        prompt = load_prompt(
            "resume_extraction.txt"
        )

        prompt = prompt.replace(
            "{resume_text}",
            resume_text
        )

        response = self.gemini.generate_text(prompt)

        data = json.loads(response)

        return ResumeExtraction.model_validate(data)