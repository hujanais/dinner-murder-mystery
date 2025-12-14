"""
Routes package initialization.
"""

from fastapi import APIRouter

# Import route modules
from . import question, search, auth, websocket

# Create main router
api_router = APIRouter(prefix="/api")

# Include sub-routers
api_router.include_router(question.router, tags=["question"])
api_router.include_router(search.router, tags=["search"])
api_router.include_router(auth.router, tags=["authentication"])
api_router.include_router(websocket.router, tags=["websocket"])

__all__ = ["api_router"]
