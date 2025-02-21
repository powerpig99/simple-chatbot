from .core import Chatbot

def run_chatbot():
    bot = Chatbot()
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye!")
            break
        tokens = bot.process_input(user_input)
        response = bot.get_response(tokens)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    run_chatbot()