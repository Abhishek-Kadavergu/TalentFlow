from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger
from contextlib import asynccontextmanager
from app.core.exceptions import TalentFlowException
from app.core.handlers import talentflow_exception_handler
from app.schemas.response import ApiResponse
from app.api.health import router as health_router
from app.api.resume import router as resume_router
from app.api.evaluation import router as evaluation_router
from app.api.github import router as github_router
from app.api.submission import router as submission_router



app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_exception_handler(
    TalentFlowException,
    talentflow_exception_handler,
)


app.include_router(health_router)
app.include_router(resume_router)
app.include_router(evaluation_router)
app.include_router(github_router)
app.include_router(submission_router)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application started")
    yield
    logger.info("Application shutting down")



@app.get("/", response_model=ApiResponse[str])
async def root():
    return ApiResponse(
        success=True,
        message="Backend is running",
        data="Welcome to TalentFlow AI"
    )