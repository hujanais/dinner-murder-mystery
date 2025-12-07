"""
Business logic for JWT authentication.
"""

from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext

from ..settings.env import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    
    Args:
        plain_password: The plain text password
        hashed_password: The hashed password to compare against
        
    Returns:
        True if passwords match, False otherwise
    """
    # TODO: Implement password verification
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hash a password.
    
    Args:
        password: The plain text password to hash
        
    Returns:
        The hashed password
    """
    # TODO: Implement password hashing
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token.
    
    Args:
        data: Dictionary containing data to encode in the token (e.g., username)
        expires_delta: Optional expiration time delta
        
    Returns:
        Encoded JWT token string
    """
    # TODO: Implement JWT token creation
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Optional[dict]:
    """
    Verify and decode a JWT token.
    
    Args:
        token: The JWT token string to verify
        
    Returns:
        Dictionary containing decoded token data if valid, None otherwise
    """
    # TODO: Implement token verification
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        return None


def authenticate_user(
    db: Session,
    username: str,
    password: str
) -> Optional[dict]:
    """
    Authenticate a user with username and password.
    
    Args:
        db: Database session
        username: Username for authentication
        password: Password for authentication
        
    Returns:
        Dictionary containing user information if authenticated, None otherwise
    """
    # TODO: Implement user authentication
    # This should:
    # 1. Query the database for the user
    # 2. Verify the password
    # 3. Return user information if valid
    # Note: User model may need to be added to the database schema
    return None

