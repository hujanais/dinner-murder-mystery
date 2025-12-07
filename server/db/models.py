"""
SQLAlchemy database models.
"""

from sqlalchemy import Column, Integer, String, Boolean, Text, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
import enum

from .database import Base


class DemeanorEnum(enum.Enum):
    """Guest demeanor types - used for validation and reference."""
    SHY = "Shy"
    BRASH = "Brash"
    TALKATIVE = "Talkative"
    # TODO: Add more demeanor types as needed


class GenderEnum(enum.Enum):
    """Gender types."""
    MALE = "Male"
    FEMALE = "Female"


class Demeanor(Base):
    """
    SQLAlchemy model for Demeanor types.
    Stores demeanor types with detailed descriptions in the database.
    """
    __tablename__ = "demeanors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)  # e.g., "BRASH", "SHY", "TALKATIVE"
    display_name = Column(String, nullable=False)  # e.g., "Brash", "Shy", "Talkative"
    description = Column(Text, nullable=False)  # Detailed description of the demeanor

    # Relationships
    guests = relationship("Guest", back_populates="demeanor_rel")
    detectives = relationship("Detective", back_populates="demeanor_rel")


class Guest(Base):
    """
    SQLAlchemy model for Guest characters.
    """
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    demeanor_id = Column(Integer, ForeignKey("demeanors.id"), nullable=False)
    backstory = Column(Text, nullable=False)
    is_criminal = Column(Boolean, default=False, nullable=False)
    gender = Column(SQLEnum(GenderEnum), nullable=False)

    # Relationships
    demeanor_rel = relationship("Demeanor", back_populates="guests")
    # TODO: Add relationships as needed (e.g., clues found, questions asked)


class Detective(Base):
    """
    SQLAlchemy model for Detective (Player).
    Inherits characteristics from Guest but with is_criminal = False.
    """
    __tablename__ = "detectives"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    demeanor_id = Column(Integer, ForeignKey("demeanors.id"), nullable=False)
    backstory = Column(Text, nullable=False)
    gender = Column(SQLEnum(GenderEnum), nullable=False)
    # is_criminal is always False for detectives, so we don't need to store it

    # Relationships
    demeanor_rel = relationship("Demeanor", back_populates="detectives")
    # TODO: Add relationships as needed


class Room(Base):
    """
    SQLAlchemy model for Room/Location entities.
    """
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=False)
    url = Column(String, nullable=True)  # URL to external image or HTML

    # Relationships
    # TODO: Add relationship to clues that can be found in this room


class Clue(Base):
    """
    SQLAlchemy model for Clue entities.
    """
    __tablename__ = "clues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=False)
    url = Column(String, nullable=True)  # URL to external image or HTML
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=True)  # Foreign key to Room

    # Relationships
    room = relationship("Room", backref="clues")


class Story(Base):
    """
    SQLAlchemy model for Story entities.
    """
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=False)
    url = Column(String, nullable=True)  # URL to external image or HTML


class Solution(Base):
    """
    SQLAlchemy model for Solution entities.
    """
    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=False)
    url = Column(String, nullable=True)  # URL to external image or HTML

