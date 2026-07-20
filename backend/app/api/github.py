from fastapi import APIRouter
from pydantic import BaseModel

from app.services.github_service import GitHubService

router = APIRouter(
    prefix="/github",
    tags=["GitHub"]
)

service = GitHubService()


class GitHubRequest(BaseModel):
    github_url: str


@router.post("/analyze")
async def analyze(request: GitHubRequest):

    return service.analyze(
        request.github_url
    )