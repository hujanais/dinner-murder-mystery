"""
API routes for search functionality.
"""

from fastapi import APIRouter, HTTPException, status

from ..models.request import SearchRequest
from ..models.response import ResponseBody

router = APIRouter()


@router.post("/search", response_model=ResponseBody)
async def search_location(request: SearchRequest):
    """
    POST /api/search
    Search a location for clues.
    Probabilistic chance to return NONE or a clue from the specified location.

    Args:
        request: SearchRequest containing location

    Returns:
        ResponseBody with success status, message, and optional clue data
    """
    # TODO: Implement search logic with probabilistic clue discovery
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Search endpoint not yet implemented")
