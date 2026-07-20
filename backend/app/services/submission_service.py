from app.services.github_service import GitHubService
from app.services.resume_extraction_service import ResumeExtractionService
from app.services.resume_evaluation_service import ResumeEvaluationService
from app.services.hiring_evaluation_service import HiringEvaluationService
from app.utils.pdf_parser import extract_text_from_pdf

from app.schemas.submission import SubmissionResponse


class SubmissionService:

    def __init__(self):
        self.resume_service = ResumeExtractionService()
        self.resume_evaluation_service = ResumeEvaluationService()
        self.github_service = GitHubService()
        self.hiring_service = HiringEvaluationService()

    def analyze(
        self,
        resume_path: str,
        github_url: str,
        job_description: str,
    ):

        # Step 1
        resume_text = extract_text_from_pdf(resume_path)

        # Step 2
        resume = self.resume_service.extract(resume_text)

        # Step 3
        resume_evaluation = self.resume_evaluation_service.evaluate(
            resume.model_dump(),
            job_description,
        )

        # Step 4
        github_analysis = self.github_service.analyze(
            github_url
        )

        # Step 5
        return SubmissionResponse(
            resume=resume,
            resume_evaluation=resume_evaluation,
            github_analysis=github_analysis,
        )