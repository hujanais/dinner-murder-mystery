from services.game_engine import GameEngine


def main():
    engine = GameEngine()
    guest = engine.story.guests[0]
    
    print(f"\nYou are questioning {guest.name}.")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    while True:
        try:
            question = input("You: ").strip()
            
            if question.lower() in ["quit", "exit", "q"]:
                print("\nEnding conversation. Goodbye!")
                break
            
            if not question:
                continue
            
            print(f"\n{guest.name}: ", end="", flush=True)
            guest.agent.print_response(question)
            print()  # Add a blank line after response
            
        except KeyboardInterrupt:
            print("\n\nEnding conversation. Goodbye!")
            break
        except EOFError:
            print("\n\nEnding conversation. Goodbye!")
            break


if __name__ == "__main__":
    main()
