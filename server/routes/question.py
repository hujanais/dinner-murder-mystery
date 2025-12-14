"""
API routes for question/interrogation functionality.
"""

from fastapi import APIRouter, HTTPException, status

from ..models.request import QuestionRequest
from ..models.response import ResponseBody

router = APIRouter()


@router.post("/question", response_model=ResponseBody)
async def ask_question(request: QuestionRequest):
    """
    POST /api/question
    Ask a question to a guest.
    Response is handled via WebSocket with the guest's answer.

    Args:
        request: QuestionRequest containing guestId and question

    Returns:
        ResponseBody with success status and message
    """
    # TODO: Implement question handling logic
    # This should trigger a WebSocket message with the guest's answer
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Question endpoint not yet implemented")
