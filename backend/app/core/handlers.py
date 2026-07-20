from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import TalentFlowException


async def talentflow_exception_handler(
    request: Request,
    exc: TalentFlowException,
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": exc.message,
            "data": None,
        },
    )