from core.brain import process_input

print("JARVIS is online. Type 'exit' to stop.")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("JARVIS: Shutting down.")
        break

    response = process_input(user_input)
    print("JARVIS:", response)
