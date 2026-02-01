from core.brain import process_input

print("JARVIS is online. Type 'exit' to stop.")

exit_commands = {"exit", "quit", "shutdown", "stop", "bye", "goodbye", "see you"}

while True:
    user_input = input("You: ").lower()

    if user_input in exit_commands:
        print("JARVIS: Shutting down.")
        break

    response = process_input(user_input)
    print("JARVIS:", response)
