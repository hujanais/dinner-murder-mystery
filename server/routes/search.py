"""
API routes for search functionality.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models.request import SearchRequest
from ..models.response import ResponseBody
from ..db import get_db
from ..services import search_service

router = APIRouter()


@router.post("/search", response_model=ResponseBody)
async def search_location(
    request: SearchRequest,
    db: Session = Depends(get_db)
):
    """
    POST /api/search
    Search a location for clues.
    Probabilistic chance to return NONE or a clue from the specified location.
    
    Args:
        request: SearchRequest containing location
        db: Database session
        
    Returns:
        ResponseBody with success status, message, and optional clue data
    """
    # TODO: Implement search logic with probabilistic clue discovery
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Search endpoint not yet implemented"
    )

