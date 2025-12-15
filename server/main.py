from services.game_engine import GameEngine
from models.entity import Clue, Room
from models.conversation import ConversationItem


def print_help():
    print(
        "\nCommands:\n"
        "  guests              - list guests and select one\n"
        "  use <#|name>        - select guest by number or name\n"
        "  ask <question>      - ask the selected guest\n"
        "  clues               - list known clues\n"
        "  rooms               - list rooms\n"
        "  accuse <name>       - make an accusation\n"
        "  help                - show this help\n"
        "  quit/exit/q         - leave the session\n"
    )


def list_guests(story, current_idx: int):
    print("\nGuests:")
    for idx, guest in enumerate(story.guests):
        marker = "->" if idx == current_idx else "  "
        print(f"  {marker} [{idx}] {guest.name} ({guest.demeanor.name})")


def list_clues(discovered: list[Clue]):
    print("\nClues:")
    if not discovered:
        print("  (no clues discovered yet)")
        return
    for clue in discovered:
        print(f"  - {clue.title}: {clue.description}")


def list_rooms(rooms: list[Room]):
    print("\nRooms:")
    for room in rooms:
        print(f"  - {room.title}: {room.description}")


def find_room_by_name(rooms: list[Room], name: str) -> Room | None:
    name_lower = name.lower()
    for room in rooms:
        if room.title.lower() == name_lower or (room.url and room.url.lower() == name_lower):
            return room
    return None


def get_clues_by_ids(all_clues: list[Clue], ids: set[str]) -> list[Clue]:
    by_url = {c.url: c for c in all_clues if c.url}
    return [by_url[i] for i in ids if i in by_url]


def main():
    engine = GameEngine()
    story = engine.story
    current_idx = 0

    print(f"\n{story.title}")
    print(story.description)
    print("\nType 'help' to see commands.")
    list_guests(story, current_idx)

    while True:
        try:
            raw = input("\nYou> ").strip()
            if not raw:
                continue

            cmd = raw.lower()

            if cmd in {"quit", "exit", "q"}:
                print("\nEnding conversation. Goodbye!")
                break

            if cmd == "help":
                print_help()
                continue

            if cmd == "guests":
                list_guests(story, current_idx)
                continue

            if cmd.startswith("search ") or cmd.startswith("go "):
                # Room search / movement
                _, _, room_query = raw.partition(" ")
                room_query = room_query.strip()
                if not room_query:
                    print("Specify a room name to search, e.g. 'search Dining Hall'.")
                    continue

                room = find_room_by_name(story.rooms, room_query)
                if not room:
                    print("Room not found.")
                    continue

                state = engine.state
                if room.url in state.searched_room_ids:
                    print(f"\nYou search the {room.title} again but find nothing new.")
                    discovered_clues = get_clues_by_ids(
                        story.clues, state.discovered_clue_ids
                    )
                    list_clues(discovered_clues)
                    continue

                state.searched_room_ids.add(room.url or room.title.lower())
                print(f"\nYou carefully search the {room.title}...")

                # Determine which clues are in this room.
                clue_ids = story.room_clues.get(room.url or "", [])
                new_clues = []
                for cid in clue_ids:
                    if cid not in state.discovered_clue_ids:
                        state.discovered_clue_ids.add(cid)
                        new_clues.append(cid)

                if not new_clues:
                    print("You don't uncover any new clues here.")
                else:
                    print("You discover:")
                    discovered = get_clues_by_ids(story.clues, set(new_clues))
                    for clue in discovered:
                        print(f"  - {clue.title}: {clue.description}")
                continue

            if cmd.startswith("use "):
                target = raw[4:].strip()
                if target.isdigit():
                    idx = int(target)
                    if 0 <= idx < len(story.guests):
                        current_idx = idx
                        print(f"Now questioning {story.guests[current_idx].name}.")
                    else:
                        print("Invalid guest index.")
                else:
                    matched = [
                        i
                        for i, g in enumerate(story.guests)
                        if g.name.lower() == target.lower()
                    ]
                    if matched:
                        current_idx = matched[0]
                        print(f"Now questioning {story.guests[current_idx].name}.")
                    else:
                        print("Guest not found.")
                continue

            if cmd == "clues":
                discovered = get_clues_by_ids(
                    story.clues, engine.state.discovered_clue_ids
                )
                list_clues(discovered)
                continue

            if cmd == "rooms":
                list_rooms(story.rooms)
                continue

            if cmd.startswith("accuse "):
                if engine.state.game_over:
                    print("The game is already over.")
                    continue

                target = raw[7:].strip()
                if not target:
                    print("Specify a name to accuse.")
                    continue

                discovered = engine.state.discovered_clue_ids
                if len(discovered) < 3:
                    print(
                        "You don't have enough evidence yet. Find at least three clues before accusing."
                    )
                    continue

                killer_name = story.solution.title.lower()
                engine.state.accused = target
                engine.state.game_over = True

                if target.lower() in killer_name:
                    print("\nAccusation correct! You solved the mystery.")
                    print(f"\nSolution: {story.solution.description}")
                else:
                    print("\nAccusation incorrect. The mystery remains.")
                    print(f"\nThe truth was: {story.solution.title}")
                continue

            if cmd.startswith("ask "):
                question = raw[4:].strip()
            else:
                question = raw

            if not question:
                continue

            guest = story.guests[current_idx]

            # Log the player's question.
            engine.state.conversation_log.append(
                ConversationItem(name="Detective", content=question, url="")
            )
            engine.state.questions_asked[guest.name] = (
                engine.state.questions_asked.get(guest.name, 0) + 1
            )

            print(f"\n{guest.name}: ", end="", flush=True)
            resp = guest.respond(question)
            if resp:
                print(resp)

            # Log guest response.
            engine.state.conversation_log.append(
                ConversationItem(name=guest.name, content=resp or "", url=guest.url)
            )

            # Chance for another guest to interject.
            from random import random

            if len(story.guests) > 1 and random() < 0.4:
                # pick a different guest
                others = [g for g in story.guests if g is not guest]
                interjector = others[0]
                interjection = interjector.interject(engine.state.conversation_log)
                if interjection and interjection.strip():
                    print(f"\n{interjector.name} (interjects): {interjection}")

            print()

        except KeyboardInterrupt:
            print("\n\nEnding conversation. Goodbye!")
            break
        except EOFError:
            print("\n\nEnding conversation. Goodbye!")
            break


if __name__ == "__main__":
    main()
