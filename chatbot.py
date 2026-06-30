# Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hi", "hello"]:
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

print("Welcome to the Chatbot! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Bye! 👋")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
