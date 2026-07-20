from google import genai

from app.core.config import settings


class GeminiService:
    """
    Service responsible only for communicating with the Gemini API.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = "gemini-3.5-flash"

    def generate_text(self, prompt: str) -> str:
        """
        Generate a text response from Gemini.
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text