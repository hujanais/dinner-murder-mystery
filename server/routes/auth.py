"""
API routes for authentication and JWT token management.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models.request import LoginRequest
from ..models.response import ResponseBody
from ..db import get_db
from ..services import auth_service

router = APIRouter()


@router.post("/login", response_model=ResponseBody)
async def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    """
    Login endpoint for user authentication.
    Generates and returns a JWT token upon successful authentication.
    
    Args:
        request: LoginRequest containing username and password
        db: Database session
        
    Returns:
        ResponseBody with success status, message, and JWT token in data
    """
    # TODO: Implement JWT authentication logic
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Login endpoint not yet implemented"
    )


@router.post("/token", response_model=ResponseBody)
async def generate_token(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    """
    Token generation endpoint.
    Alternative endpoint for generating JWT tokens.
    
    Args:
        request: LoginRequest containing username and password
        db: Database session
        
    Returns:
        ResponseBody with success status, message, and JWT token in data
    """
    # TODO: Implement JWT token generation logic
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Token generation endpoint not yet implemented"
    )

