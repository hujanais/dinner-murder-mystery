** This is for server-side implementation team only **

Introduction
Objective:

Develop a reusable, turn-based framework for dinner murder mystery-type interactive games. The player takes on the role of a detective attempting to uncover the truth by asking questions to guests at the scene.

Gameplay Overview
Role: Player acts as the detective.
Mechanics:
Interrogation: Guests and the killer have predefined sets of instructions and knowledge for answering the detective’s questions.
Interjections: Other guests may interject with comments or questions when relevant, enhancing the narrative.
Framework Overview
Genre: Interactive Detective Story / Puzzle Game

Concept:

The player solves mysteries through interactive dialogue and exploration.
Configurability: Easily adaptable scenarios with new characters and plots.
Features:

Customizable Profiles: Create and manage profiles for guests and the killer.
Thematic Flexibility: Support for varied settings to enhance replayability and thematic richness.
Gameplay Elements
Core Mechanics:

Interrogation System:
Flexible dialogue options, driven by character profiles.
Clue Discovery:
Interactive opportunities for the player to find evidence and progress the story.
Dynamic Story Progression:
Narrative adapts based on player decisions, ensuring a unique experience each playthrough.
Technical Requirements
Platform:

Responsive web-based application accessible via major desktop and mobile browsers.

# Server-side Requirements
Server framework: FastAPI, SQLAlchemy
Model: Pydantic
Database: Postgres

## Core Game Components
    Detective (Player): A single detective character.
    Guests: Multiple guest characters, each with distinct attributes.
    Locations: Various rooms like Library, Garden, etc., each potentially containing clues.
    Clues: Objects that provide narrative details or advance the story.

### API Routes
    POST /api/question:
    Request: {guestId: 123, question: ""}
    Response: Handled via WebSocket with the guest's answer.
    POST /api/search:
    Request: {location}
    Operation: Probabilistic chance to return NONE or a clue from the specified location.

    - All RestAPI calls shall have a dedicated RequestBody and ResponseBody
    - For ResponseBody, it could be generic and have {success: True or False, message: str, url: str}

### Database and Schemas
Guest (BaseModel)
    Name: Name of the guest.
    Age: Age of the guest.
    Demeanor: Enum [Shy, Brash, Talkative, etc.].
    Backstory: Knowledge base including potential motives.
    IsCriminal: Boolean flag indicating if this guest is the criminal.
    Gender: Enum [Male, Female].
    Detective: Inherits from Guest with IsCriminal = False.

Demeanor
    name = Column(String, nullable=False, unique=True, index=True)  # e.g., "BRASH", "SHY", "TALKATIVE"
    display_name = Column(String, nullable=False)  # e.g., "Brash", "Shy", "Talkative"
    description = Column(Text, nullable=False)  # Detailed description of the demeanor

EntityBase (BaseModel)
    Title: Title of the entity (e.g., Room, Clue).
    Description: Description of the entity.
    URL: URL to an external image or HTML for display.
    Room, Clue, Story, Solution: Extend EntityBase.

### Error Handling
Handling: Use FastAPI exception handling to return 501 Not Implemented responses for unimplemented features.
Error Message: Provide meaningful error messages in the response.

### Authentication
Method: Implement JWT (JSON Web Tokens) for authenticating users.
Endpoints: Include login and token generation endpoints to manage sessions.

### WebSockets
Implementation: The team will manage WebSocket connections using FastAPI, facilitating dynamic interactions like guest responses and real-time updates.

### Unit Testing: Not required at this phase, but integration testing will be considered.

### Folder structure
db: Contains database related utitlies and db models
models: Contains pydantic models.
routes: Contains routes related.
services: Contains the business logic.