from models.entity import Clue, Room, Solution
from models.guest import Gender, Guest, Deameanor

class Story:
    """
    Story for the game.
    """

    def __init__(self):
        self.title: str
        self.description: str
        self.url: str
        self.story: str
        self.solution: Solution
        self.clues: list[Clue]
        self.rooms: list[Room]
        self.guests: list[Guest]

    def load_story(self, story_path: str):
        """
        Load a story from a file.
        """
        self.title = "Title of the story"
        self.description = "Description of the story"
        self.url = "URL of the story"
        self.story = "Story of the story"
        self.solution = Solution(
            title="Solution of the story",
            description="Description of the solution",
            url="URL of the solution",
        )
        self.clues = [
            Clue(
                title="Clue 1",
                description="Description of the clue 1",
                url="URL of the clue 1",
            ),
            Clue(
                title="Clue 2",
                description="Description of the clue 2",
                url="URL of the clue 2",
            ),
        ]
        self.rooms = [
            Room(
                title="Room 1",
                description="Description of the room 1",
                url="URL of the room 1",
            ),
            Room(
                title="Room 2",
                description="Description of the room 2",
                url="URL of the room 2",
            ),
        ]
        self.guests = [
            Guest(
                name="Olivia Drake",
                gender=Gender.FEMALE,
                age=38,
                description=(
                    "Olivia was Vincent's personal attorney and helped orchestrate the legal side of his bitcoin "
                    "empire. Recently, Vincent accused her of mishandling tax paperwork, putting her law license "
                    "in jeopardy and threatening her career. Olivia has been rumored to be seeking another "
                    "high-profile client and was aware that Vincent planned to switch legal counsel after this "
                    "dinner."
                ),
                is_criminal=False,
                url="olivia-drake",
                demeanor=Deameanor(
                    name="Controlled and Elegant",
                    description=(
                        "Controlled and elegant, Olivia speaks in measured tones and rarely raises her voice. "
                        "She has an air of professionalism, habitually straightening her cuffs or tucking a "
                        "stray hair behind her ear. Her eyes scan her surroundings with quick, analytic flicks."
                    ),
                ),
            ),
            Guest(
                name="Marcus Dunn",
                gender=Gender.MALE,
                age=45,
                description=(
                    "Marcus was the lead engineer behind Vincent's mining operation. He and Vincent co-founded "
                    "the business, but Vincent forced him out of the company just weeks ago, buying out his "
                    "shares at a fraction of their true value. Marcus had developed a new efficiency algorithm "
                    "he claims Vincent stole just before the betrayal."
                ),
                is_criminal=False,
                url="marcus-dunn",
                demeanor=Deameanor(
                    name="Gruff and Impatient",
                    description=(
                        "Gruff, impatient, and a tad defensive, Marcus favors blunt statements and frowns when "
                        "questioned. He drums his thick fingers on any available surface and meets accusation "
                        "with volcanic outbursts. He sometimes lets slip technical jargon in frustration."
                    ),
                ),
            ),
            Guest(
                name="Evelyn Sharpe",
                gender=Gender.FEMALE,
                age=29,
                description=(
                    "Evelyn is Vincent's niece, taken in by him after her parents died. He controlled her trust "
                    "fund—and recently refused to release funds for her tech startup, calling her idea 'naive.' "
                    "There are whispers of late-night arguments and desperate appeals just days before the "
                    "murder."
                ),
                is_criminal=False,
                url="evelyn-sharpe",
                demeanor=Deameanor(
                    name="Youthful and Anxious",
                    description=(
                        "Youthful, anxious, and prone to nervous laughter. Evelyn's sentences trail off "
                        "uncertainly, her hands always fiddling with small objects or her jewelry. Her eyes "
                        "dart around as if she's looking for an escape route."
                    ),
                ),
            ),
            Guest(
                name="Dr. Sanjay Mehta",
                gender=Gender.MALE,
                age=52,
                description=(
                    "Sanjay was Vincent's chief scientific advisor, responsible for the complex hardware running "
                    "the bitcoin mine. A recent audit uncovered missing equipment—a situation Vincent blamed "
                    "entirely on Sanjay. Their professional relationship had soured, and Sanjay was in danger of "
                    "losing his university tenure due to the scandal."
                ),
                is_criminal=False,
                url="sanjay-mehta",
                demeanor=Deameanor(
                    name="Polite but Distant",
                    description=(
                        "Polite but distant, Sanjay chooses his words carefully and speaks softly with a "
                        "faint accent. He habitually adjusts his glasses and avoids direct eye contact, as if "
                        "lost in his own thoughts."
                    ),
                ),
            ),
            Guest(
                name="Helena Voss",
                gender=Gender.FEMALE,
                age=41,
                description=(
                    "Helena was Vincent's recent romantic partner, but their whirlwind romance turned sour when "
                    "Vincent discovered she had concealed a criminal record related to cryptocurrency fraud. He "
                    "planned to end things and expose her to his investors, potentially ruining her for good."
                ),
                is_criminal=True,
                url="helena-voss",
                demeanor=Deameanor(
                    name="Charismatic and Charming",
                    description=(
                        "Charismatic and charming, Helena is quick with a joke or a compliment. She maintains "
                        "a mask of warmth, but her laughter can turn cold when pressed. She often leans in "
                        "conspiratorially, as if sharing a secret."
                    ),
                ),
            ),
        ]

    def save_story(self, story_path: str):
        """
        Save the story to a file.
        """
        pass
