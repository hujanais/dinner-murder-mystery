"""
Pydantic models for API response bodies.
"""

from pydantic import BaseModel, Field
from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class ResponseBody(BaseModel, Generic[T]):
    """
    Generic response body model for REST API calls.
    """

    success: bool = Field(..., description="Indicates if the operation was successful")
    message: str = Field(..., description="Response message")
    url: Optional[str] = Field(None, description="Optional URL for additional resources")
    data: Optional[T] = Field(None, description="Optional response data")

    class Config:
        from_attributes = True
