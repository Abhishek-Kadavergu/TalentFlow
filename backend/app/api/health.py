from fastapi import APIRouter

from app.services.gemini_service import GeminiService

router = APIRouter()

gemini = GeminiService()


@router.get("/llm-test")
async def llm_test():
    response = gemini.generate_text(
        "Reply with exactly: Gemini is workingxx."
    )

    return {
        "response": response
    }