from services.game_engine import GameEngine


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


def list_clues(story):
    print("\nClues:")
    for clue in story.clues:
        print(f"  - {clue.title}: {clue.description}")


def list_rooms(story):
    print("\nRooms:")
    for room in story.rooms:
        print(f"  - {room.title}: {room.description}")


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
                list_clues(story)
                continue

            if cmd == "rooms":
                list_rooms(story)
                continue

            if cmd.startswith("accuse "):
                target = raw[7:].strip()
                killer_name = story.solution.title.lower()
                if target.lower() in killer_name:
                    print("\nAccusation correct! You solved the mystery.")
                else:
                    print("\nAccusation incorrect. The mystery remains.")
                continue

            if cmd.startswith("ask "):
                question = raw[4:].strip()
            else:
                question = raw

            if not question:
                continue

            guest = story.guests[current_idx]
            print(f"\n{guest.name}: ", end="", flush=True)
            resp = guest.respond(question)
            if resp:
                print(resp)
            print()

        except KeyboardInterrupt:
            print("\n\nEnding conversation. Goodbye!")
            break
        except EOFError:
            print("\n\nEnding conversation. Goodbye!")
            break


if __name__ == "__main__":
    main()
