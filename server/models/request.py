"""
Pydantic models for API request bodies.
"""

from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    """
    Request body for POST /api/question endpoint.
    """
    guest_id: int = Field(..., description="ID of the guest being questioned", alias="guestId")
    question: str = Field(..., description="The question to ask the guest")

    class Config:
        populate_by_name = True


class SearchRequest(BaseModel):
    """
    Request body for POST /api/search endpoint.
    """
    location: str = Field(..., description="Location/room to search")


class LoginRequest(BaseModel):
    """
    Request body for authentication/login endpoint.
    """
    username: str = Field(..., description="Username for authentication")
    password: str = Field(..., description="Password for authentication")

