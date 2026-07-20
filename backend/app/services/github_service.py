import tempfile

from git import Repo

from app.schemas.github import GitHubAnalysis
from app.services.gemini_service import GeminiService
from app.utils.github_loader import load_repository
from app.utils.prompt_loader import load_prompt
from app.core.logger import logger


class GitHubService:

    def __init__(self):
        self.gemini = GeminiService()

    def analyze(self, github_url: str):

        with tempfile.TemporaryDirectory() as temp_dir:

            Repo.clone_from(github_url, temp_dir)
            
            

            repository = load_repository(temp_dir)
            

            prompt = load_prompt("github_analysis.txt")
            logger.info("PROMPT: ", prompt)

            prompt = prompt.replace(
                "{repository}",
                repository
            )

            response = self.gemini.generate_text(prompt)
            logger.info("FINISHED")
            response = response.replace("```json", "")
            response = response.replace("```", "")
            response = response.strip()
            logger.info(response)

            return GitHubAnalysis.model_validate_json(response)
           